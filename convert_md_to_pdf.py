#!/usr/bin/env python3
"""Export selected QMS Markdown to PDF using Pandoc and Chromium.

No Python packages are required. Run --help, --check or --dry-run without
rendering a PDF. Requires Pandoc 3+ and Chromium/Chrome 131+ for conversion.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from html import escape
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
CONTROLLED_DIRS = (
    '00-manual', '01-procedures', '02-work-instructions', '03-forms',
    '04-supporting', '06-registers',
)
CSS = r'''
@page {
  size: Letter ORIENTATION;
  margin: 0.65in 0.5in 0.7in;
  @bottom-left { content: "Torchworx LLC"; font: 8pt Arial, sans-serif; color: #555; }
  @bottom-center { content: FOOTER; font: 8pt Arial, sans-serif; color: #555; }
  @bottom-right { content: "Page " counter(page) " of " counter(pages);
                  font: 8pt Arial, sans-serif; color: #555; }
}
html { font-size: 10pt; }
body { margin: 0; max-width: none; color: #222;
       font-family: Arial, "DejaVu Sans", sans-serif; line-height: 1.4; }
h1, h2, h3, h4, h5, h6 { color: #243b53; break-after: avoid; line-height: 1.2; }
h1 { font-size: 19pt; margin: 0.5em 0; }
h2 { font-size: 14pt; margin-top: 1.3em; }
h3 { font-size: 11.5pt; margin-top: 1em; }
h4, h5, h6 { font-size: 10pt; }
p, li { orphans: 3; widows: 3; }
table { width: 100%; border-collapse: collapse; table-layout: fixed;
        font-size: 8.5pt; margin: 0.8em 0; }
thead { display: table-header-group; }
tfoot { display: table-footer-group; }
tr { break-inside: avoid; }
th, td { border: 0.5pt solid #aab4be; padding: 5pt;
         vertical-align: top; overflow-wrap: anywhere; }
th { background: #e9eef3; font-weight: bold; text-align: left; }
pre { white-space: pre-wrap; overflow-wrap: anywhere; font-size: 8pt;
      padding: 7pt; background: #f4f6f8; border: 0.5pt solid #ccd3da; }
code { font-family: "DejaVu Sans Mono", Consolas, monospace; font-size: 0.9em; }
blockquote { margin-left: 1em; padding-left: 0.8em; border-left: 2pt solid #bbc6d0; }
img { max-width: 100%; max-height: 8in; }
a { color: #243b53; text-decoration: underline; overflow-wrap: anywhere; }
hr { border: 0; border-top: 0.5pt solid #aab4be; }
'''


@dataclass(frozen=True)
class Export:
    source: Path
    destination: Path


def metadata(text: str) -> dict[str, str]:
    """Read only the leading control table, never later tables with Title columns."""
    result = {}
    started = False
    for line in text.lstrip('\ufeff').splitlines():
        if not line.strip():
            if started:
                break
            continue
        if not line.startswith('|'):
            break
        started = True
        cells = [c.strip().replace('**', '') for c in line.strip('|').split('|')]
        if len(cells) == 2 and cells[0] in ('Document No.', 'Title', 'Revision'):
            result[cells[0]] = cells[1]
    return result


def wide_table(text: str) -> bool:
    """Choose landscape for Markdown tables with more than seven columns."""
    return any(
        len(re.split(r'(?<!\\)\|', line.strip().strip('|'))) > 7
        for line in text.splitlines() if line.lstrip().startswith('|')
    )


def stylesheet(text: str, orientation: str) -> str:
    info = metadata(text)
    # Include the actual revision, including draft status, without implying approval.
    label = ' | '.join(filter(None, [info.get('Document No.', ''),
                                  'Rev ' + info['Revision'] if info.get('Revision') else '']))
    quoted = json.dumps(label, ensure_ascii=False).replace('<', r'\3c ')
    page = 'landscape' if orientation == 'landscape' or (
        orientation == 'auto' and wide_table(text)) else 'portrait'
    return CSS.replace('ORIENTATION', page).replace('FOOTER', quoted)


def plan_exports(files: list[str], all_documents: bool, root: Path,
                 output_dir: Path, output: Path | None, overwrite: bool) -> list[Export]:
    if all_documents and files:
        raise ValueError('Choose explicit Markdown files or --all, not both.')
    if all_documents:
        sources = [p.resolve() for directory in CONTROLLED_DIRS
                   for p in (root / directory).rglob('*.md')]
    else:
        sources = [Path(p).resolve() for p in files]
    sources = sorted(set(sources))
    if not sources:
        raise ValueError('No Markdown files selected. Supply paths or --all.')
    if output is not None and len(sources) != 1:
        raise ValueError('--output requires exactly one input file.')
    exports = []
    seen = set()
    for source in sources:
        if not source.is_file() or source.suffix.lower() != '.md':
            raise ValueError(f'Not a Markdown file: {source}')
        if output is not None:
            destination = output.resolve()
        else:
            try:
                relative = source.relative_to(root)
            except ValueError:
                relative = Path(source.name)
            destination = (output_dir / relative).with_suffix('.pdf').resolve()
        if destination.suffix.lower() != '.pdf':
            raise ValueError(f'Output must end in .pdf: {destination}')
        key = str(destination).casefold()
        if key in seen:
            raise ValueError(f'Multiple inputs map to the same output: {destination}')
        seen.add(key)
        if destination.exists() and (not overwrite or not destination.is_file()):
            raise ValueError(f'Output already exists: {destination}; use --overwrite to replace a file.')
        exports.append(Export(source, destination))
    return exports


def executable(explicit: str | None, candidates: tuple[str, ...]) -> str:
    for candidate in ((explicit,) if explicit else candidates):
        found = shutil.which(candidate)
        if found:
            return found
    raise ValueError('Required program not found: ' + (explicit or ' / '.join(candidates)))


def engine_version(program: str, minimum: int) -> str:
    result = subprocess.run([program, '--version'], check=True, text=True,
                            capture_output=True, timeout=20)
    version = (result.stdout or result.stderr).strip().splitlines()[0]
    match = re.search(r'\b(\d+)\.', version)
    if not match or int(match[1]) < minimum:
        raise ValueError(f'Unsupported version: {version}; minimum major version {minimum}.')
    return version


def convert_one(job: Export, pandoc: str, browser: str, orientation: str,
                timeout: int, overwrite: bool, no_sandbox: bool,
                engine: str = 'chromium') -> None:
    text = job.source.read_text(encoding='utf-8-sig')
    job.destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.qms-pdf-', dir=job.destination.parent) as folder:
        temp = Path(folder)
        header = temp / 'header.html'
        # Raw Markdown HTML is disabled below. Local images resolve relative to source.
        # CSP prevents remote resources or scripts in the rendered document.
        header.write_text(
            '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; '
            'img-src file: data:; style-src \'unsafe-inline\'; font-src file: data:">\n'
            f'<base href="{escape(job.source.parent.as_uri() + "/", quote=True)}">\n'
            '<style>' + stylesheet(text, orientation) + '</style>', encoding='utf-8')
        page, staged = temp / 'document.html', temp / 'document.pdf'
        subprocess.run([
            pandoc, '--from=gfm-raw_html', '--to=html5', '--standalone', '--wrap=none',
            '--metadata', 'pagetitle=' + metadata(text).get('Title', job.source.stem),
            '--metadata', 'lang=en-US', '--include-in-header', str(header),
            '--output', str(page),
        ], input=text, text=True, check=True, capture_output=True, timeout=timeout)
        command = [browser, '--headless', '--disable-gpu', '--disable-extensions',
                   '--disable-background-networking', '--no-first-run',
                   '--no-pdf-header-footer', '--allow-file-access-from-files',
                   '--user-data-dir=' + str(temp / 'profile'),
                   '--print-to-pdf=' + str(staged)]
        if no_sandbox:
            command.append('--no-sandbox')
        command.append(page.as_uri())
        if engine == 'weasyprint':
            from weasyprint import HTML
            from weasyprint.urls import URLFetcher
            default_url_fetcher = URLFetcher()

            def local_resources(url, *args, **kwargs):
                if not url.startswith(('file:', 'data:')):
                    raise ValueError('Remote resources are disabled: ' + url)
                return default_url_fetcher(url, *args, **kwargs)

            HTML(filename=str(page), url_fetcher=local_resources).write_pdf(str(staged))
        else:
            subprocess.run(command, check=True, capture_output=True, timeout=timeout)
        if not staged.is_file():
            raise ValueError('Browser completed without creating a PDF.')
        with staged.open('rb') as stream:
            if stream.read(5) != b'%PDF-':
                raise ValueError('Browser output is not a PDF.')
        if overwrite:
            os.replace(staged, job.destination)
        else:
            # Same-filesystem hard link publishes the complete PDF without replacing
            # a file created by another process since the initial preflight.
            os.link(staged, job.destination)


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('files', nargs='*', help='Markdown paths; quote paths containing spaces')
    p.add_argument('--all', action='store_true', help='Select numbered controlled folders (see README); excludes internal working notes')
    p.add_argument('--root', type=Path, default=ROOT, help='Repository root (default: script directory)')
    out = p.add_mutually_exclusive_group()
    out.add_argument('--output', type=Path, help='Exact PDF path for a single input')
    out.add_argument('--output-dir', type=Path, help='Export directory (default: <root>/pdf-output)')
    p.add_argument('--orientation', choices=('auto', 'portrait', 'landscape'), default='auto')
    p.add_argument('--overwrite', action='store_true', help='Replace existing PDFs')
    p.add_argument('--dry-run', action='store_true', help='List planned exports without invoking engines or writing files')
    p.add_argument('--check', action='store_true', help='Check engine availability/versions only; write no files')
    p.add_argument('--pandoc', help='Pandoc executable name or path')
    p.add_argument('--browser', help='Chromium/Chrome executable name or path')
    p.add_argument('--engine', choices=('chromium', 'weasyprint'), default='chromium',
                   help='PDF renderer; WeasyPrint is an optional Python dependency')
    p.add_argument('--timeout', type=int, default=120, help='Seconds per engine invocation (default: 120)')
    p.add_argument('--no-sandbox', action='store_true', help='Disable browser sandbox when required by a trusted container runtime')
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.timeout <= 0:
            raise ValueError('--timeout must be positive.')
        if args.check and (args.files or args.all or args.dry_run):
            raise ValueError('--check is a standalone dependency check.')
        if not args.check:
            root = args.root.resolve()
            jobs = plan_exports(args.files, args.all, root,
                                args.output_dir.resolve() if args.output_dir else root / 'pdf-output',
                                args.output, args.overwrite)
            if args.dry_run:
                for job in jobs:
                    print(f'{job.source} -> {job.destination}')
                print(f'{len(jobs)} planned export(s); no files written.')
                return 0
        pandoc = executable(args.pandoc, ('pandoc',))
        browser = '' if args.engine == 'weasyprint' else executable(
            args.browser, ('chromium', 'chromium-browser', 'google-chrome', 'chrome', 'msedge'))
        for program, minimum in ((pandoc, 3),) + (((browser, 131),) if browser else ()):
            print(engine_version(program, minimum))
        if args.engine == 'weasyprint':
            try:
                import weasyprint
            except ImportError as exc:
                raise ValueError('Install the optional engine: python -m pip install weasyprint') from exc
            print('WeasyPrint ' + weasyprint.__version__)
        if args.check:
            return 0
        for job in jobs:
            try:
                convert_one(job, pandoc, browser, args.orientation,
                            args.timeout, args.overwrite, args.no_sandbox, args.engine)
            except (OSError, ValueError, subprocess.SubprocessError) as exc:
                raise ValueError(f'{job.source}: {exc}') from exc
            print(f'Created: {job.destination}')
        return 0
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        if isinstance(exc, subprocess.CalledProcessError) and exc.stderr:
            detail = exc.stderr.decode(errors='replace') if isinstance(exc.stderr, bytes) else exc.stderr
            print(detail[-3000:], file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())

