# Markdown-to-PDF export

`convert_md_to_pdf.py` exports Markdown directly to customer-facing PDF using
Pandoc and headless Chromium/Chrome. It does not use or change the Word copies.

The script was added without converting any repository documents. Syntax,
dependency checks and non-rendering tests were run; the first real PDF export
still needs a visual check before customer issue.

## Setup

- Python 3.10 or later (standard library only).
- Pandoc 3 or later: https://pandoc.org/installing.html
- Chromium or Google Chrome 131 or later. Page-number margin boxes require this version.

Put both programs on PATH or supply `--pandoc` and `--browser` with their full
executable paths. Install dependencies on the machine that will run the exports.

Check dependencies without creating anything:

```sh
python convert_md_to_pdf.py --check
```

## Preview the plan — no conversions

```sh
python convert_md_to_pdf.py 00-manual/QM-001_Quality_Manual.md --dry-run
python convert_md_to_pdf.py --all --dry-run
```

Dry-run lists source/output paths without invoking the conversion engines,
reading document content or creating output directories.

## Conversion commands — for later use

One document:

```sh
python convert_md_to_pdf.py 00-manual/QM-001_Quality_Manual.md
```

Selected documents:

```sh
python convert_md_to_pdf.py 03-forms/QF-027_Equipment_List.md 03-forms/QF-028_Measurement_Equipment_List.md 03-forms/QF-030_Calibration_Schedule.md
```

Custom output, including the separate courtesy survey attachment:

```sh
python convert_md_to_pdf.py supplier-paperwork/karman/submission/QA-1003_QM-001_Cross_Reference.md --output pdf-output/QA-1003_Cross_Reference.pdf
```

Batch export:

```sh
python convert_md_to_pdf.py --all
```

`--all` selects Markdown from `00-manual`, `01-procedures`, `02-work-instructions`,
`03-forms`, `04-supporting` and `06-registers`. It excludes implementation guides,
completion reports, project/status/agent notes and customer working folders.
Supply any of those files explicitly if an export is wanted. Selection does not
filter out drafts or establish that a document is approved for customer issue.

Default outputs go under `pdf-output/`, retaining repository subfolders. Existing
PDFs are protected; use `--overwrite` deliberately to replace them. `--output`
requires one source; `--output-dir` selects another export directory. A complete
PDF is staged before publication; engine failures leave existing outputs intact.
If a batch stops partway through, earlier successfully exported files remain.

## Formatting and options

- US Letter pages, company footer, actual document ID/revision and page numbers.
- Markdown headings, lists, tables, code blocks and local images.
- Repeated table headers and automatic landscape when a table exceeds seven columns.
- Override with `--orientation portrait` or `--orientation landscape`.
- Raw Markdown HTML and remote resources are disabled. Use ordinary Markdown and local images.
- No document number/revision is invented for unnumbered courtesy attachments.
- Draft labels, blank values and approval information are preserved from the source.
- `--timeout 180` changes the per-engine timeout in seconds.
- `--no-sandbox` is available for trusted container environments that require it;
  the browser sandbox stays enabled by default.

Review initial exports for wide/tall tables, diagrams, fonts and page breaks
before sending them to customers. Exporting does not approve, sign, certify or
change the meaning of the source document.

## Non-rendering tests

```sh
python -m unittest discover -s tests -p 'test_convert_md_to_pdf.py' -v
```

These tests cover selection, metadata, layout decisions, overwrite protection,
collisions and dry-run behavior without invoking the engines or creating a PDF.
