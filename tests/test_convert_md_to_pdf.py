"""Non-rendering tests: never invoke Pandoc/Chromium or create a PDF."""
import contextlib
import importlib.util
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'convert_md_to_pdf.py'
spec = importlib.util.spec_from_file_location('pdf_export', SCRIPT)
pdf = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = pdf
spec.loader.exec_module(pdf)


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / '00-manual' / 'A document.md'
        self.source.parent.mkdir()
        self.source.write_text('# Example\n', encoding='utf-8')
        self.output = self.root / 'pdf-output'

    def test_metadata_does_not_pick_up_later_title(self):
        text = '\ufeff| Field | Value |\n| --- | --- |\n| Document No. | QM-001 |\n| Title | Quality Manual |\n| Revision | C |\n\n# Body\n\n| Title | Wrong |'
        self.assertEqual(pdf.metadata(text), {
            'Document No.': 'QM-001', 'Title': 'Quality Manual', 'Revision': 'C'})
        self.assertEqual(pdf.metadata('# Courtesy attachment\n\n| Title | Something |'), {})

    def test_draft_status_is_preserved(self):
        style = pdf.stylesheet('| Document No. | QP-010 |\n| Revision | B — draft |', 'portrait')
        self.assertIn('B — draft', style)
        self.assertNotIn('Rev A', style)

    def test_wide_tables_and_escaped_pipes(self):
        self.assertTrue(pdf.wide_table('| a | b | c | d | e | f | g | h |'))
        self.assertFalse(pdf.wide_table(r'| a\|b | c |'))
        self.assertIn('Letter landscape', pdf.stylesheet('| a | b | c | d | e | f | g | h |', 'auto'))
        self.assertIn('Letter portrait', pdf.stylesheet('| a | b |', 'auto'))
        self.assertIn('Letter portrait', pdf.stylesheet('| a | b | c | d | e | f | g | h |', 'portrait'))

    def test_output_preserves_repository_structure(self):
        jobs = pdf.plan_exports([str(self.source)], False, self.root, self.output, None, False)
        self.assertEqual(jobs[0].destination, self.output / '00-manual' / 'A document.pdf')
        self.assertFalse(self.output.exists())

    def test_batch_does_not_select_internal_documents(self):
        private = self.root / 'supplier-paperwork' / 'karman' / 'working'
        private.mkdir(parents=True)
        (private / 'notes.md').write_text('internal')
        (self.root / 'STATUS.md').write_text('internal')
        jobs = pdf.plan_exports([], True, self.root, self.output, None, False)
        self.assertEqual([x.source for x in jobs], [self.source])

    def test_existing_output_protected(self):
        # An ordinary text placeholder exercises collision checks without making a PDF.
        destination = self.root / 'existing.pdf'
        destination.write_text('existing placeholder')
        with self.assertRaisesRegex(ValueError, 'already exists'):
            pdf.plan_exports([str(self.source)], False, self.root, self.output, destination, False)
        self.assertEqual(destination.read_text(), 'existing placeholder')

    def test_collisions_and_invalid_input(self):
        external = self.root / 'outside'
        external.mkdir()
        other = external / self.source.name
        other.write_text('# Other')
        with self.assertRaisesRegex(ValueError, 'same output'):
            pdf.plan_exports([str(self.source), str(other)], False, self.root / 'different-root', self.output, None, False)
        with self.assertRaisesRegex(ValueError, 'exactly one'):
            pdf.plan_exports([str(self.source), str(other)], False, self.root, self.output, self.root / 'one.pdf', False)
        with self.assertRaisesRegex(ValueError, 'not both'):
            pdf.plan_exports([str(self.source)], True, self.root, self.output, None, False)
        with self.assertRaisesRegex(ValueError, 'Not a Markdown'):
            pdf.plan_exports([str(self.root / 'missing.md')], False, self.root, self.output, None, False)

    def test_dry_run_never_calls_engines_or_writes_output(self):
        before = set(self.root.rglob('*'))
        with patch.object(pdf.subprocess, 'run') as run, patch.object(pdf, 'convert_one') as convert:
            with contextlib.redirect_stdout(io.StringIO()):
                result = pdf.main([str(self.source), '--root', str(self.root), '--dry-run'])
        self.assertEqual(result, 0)
        run.assert_not_called()
        convert.assert_not_called()
        self.assertEqual(before, set(self.root.rglob('*')))

    def test_dependency_check_never_renders(self):
        with patch.object(pdf, 'executable', side_effect=['pandoc', 'chromium']), \
             patch.object(pdf, 'engine_version', return_value='available'), \
             patch.object(pdf, 'convert_one') as convert:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(pdf.main(['--check']), 0)
        convert.assert_not_called()
        self.assertFalse(self.output.exists())

    def test_no_input_is_an_error_and_does_not_render(self):
        with patch.object(pdf, 'convert_one') as convert, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(pdf.main(['--root', str(self.root)]), 1)
        convert.assert_not_called()


if __name__ == '__main__':
    unittest.main()
