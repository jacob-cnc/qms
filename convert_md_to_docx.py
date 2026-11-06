"""
QMS Markdown to DOCX Converter

Converts QMS Markdown documents into properly formatted Word .docx files
suitable for printing, auditing, and shop-floor use.

Usage:
    python convert_md_to_docx.py <input.md> [output.docx]
    python convert_md_to_docx.py --all  (converts all .md files in qms/ tree)
"""

import sys
import os
import re
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml, OxmlElement


# --- Style Constants ---
FONT_BODY = 'Arial'
FONT_MONO = 'Consolas'
FONT_SIZE_BODY = Pt(10)
FONT_SIZE_H1 = Pt(14)
FONT_SIZE_H2 = Pt(12)
FONT_SIZE_H3 = Pt(10.5)
FONT_SIZE_HEADER_TABLE = Pt(9)
FONT_SIZE_SMALL = Pt(8)

COLOR_HEADER_BG = 'D9E2F3'  # Light blue-gray for header table
COLOR_TABLE_HEADER_BG = 'E2EFDA'  # Light sage green for table headers
COLOR_DARK = '2F3640'  # Near-black for body text
COLOR_ACCENT = '2E4057'  # Dark steel blue for headings


def set_cell_shading(cell, color):
    """Set background color on a table cell."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)


def set_table_borders(table):
    """Apply borders to all cells in a table."""
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}/>') 
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        '  <w:top w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
        '  <w:left w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
        '  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
        '  <w:right w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
        '  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
        '  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
        '</w:tblBorders>'
    )
    # Remove existing borders if any
    existing = tblPr.find(qn('w:tblBorders'))
    if existing is not None:
        tblPr.remove(existing)
    tblPr.append(borders)


def parse_markdown_table(lines):
    """Parse markdown table lines into a list of rows (each row is list of cells)."""
    rows = []
    for line in lines:
        line = line.strip()
        if not line.startswith('|'):
            continue
        # Skip separator line (|---|---|)
        if re.match(r'^\|[\s\-:|]+\|$', line):
            continue
        cells = [c.strip() for c in line.split('|')[1:-1]]
        rows.append(cells)
    return rows


def add_formatted_text(paragraph, text, bold=False, italic=False, font_name=FONT_BODY, font_size=FONT_SIZE_BODY):
    """Add a run to a paragraph with formatting."""
    run = paragraph.add_run(text)
    run.font.name = font_name
    run.font.size = font_size
    run.font.color.rgb = RGBColor.from_string(COLOR_DARK)
    run.bold = bold
    run.italic = italic
    return run


def process_inline_formatting(paragraph, text, font_size=FONT_SIZE_BODY):
    """Process bold, italic, and code formatting in text."""
    # Pattern to match **bold**, *italic*, and `code`
    pattern = r'(\*\*(.+?)\*\*|\*(.+?)\*|`(.+?)`|([^*`]+))'
    
    for match in re.finditer(pattern, text):
        full = match.group(0)
        if full.startswith('**') and full.endswith('**'):
            add_formatted_text(paragraph, full[2:-2], bold=True, font_size=font_size)
        elif full.startswith('*') and full.endswith('*') and not full.startswith('**'):
            add_formatted_text(paragraph, full[1:-1], italic=True, font_size=font_size)
        elif full.startswith('`') and full.endswith('`'):
            add_formatted_text(paragraph, full[1:-1], font_name=FONT_MONO, font_size=font_size)
        else:
            add_formatted_text(paragraph, full, font_size=font_size)


def convert_md_to_docx(md_path, docx_path=None):
    """Convert a QMS markdown file to a formatted .docx file."""
    
    md_path = Path(md_path)
    if docx_path is None:
        docx_path = md_path.with_suffix('.docx')
    else:
        docx_path = Path(docx_path)
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Create document
    doc = Document()
    
    # Set default font
    style = doc.styles['Normal']
    font = style.font
    font.name = FONT_BODY
    font.size = FONT_SIZE_BODY
    font.color.rgb = RGBColor.from_string(COLOR_DARK)
    
    # Set margins (narrower for more content space)
    for section in doc.sections:
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)
    
    # --- Parse and render ---
    i = 0
    in_table = False
    table_lines = []
    in_code_block = False
    first_table_is_header = True  # First table in file is the document control header
    
    while i < len(lines):
        line = lines[i]
        
        # Skip horizontal rules
        if line.strip() == '---':
            if not in_table and table_lines:
                # Flush pending table
                _render_table(doc, table_lines, is_header_table=first_table_is_header)
                if first_table_is_header:
                    first_table_is_header = False
                table_lines = []
            # Add a subtle separator
            p = doc.add_paragraph()
            p.space_before = Pt(6)
            p.space_after = Pt(6)
            i += 1
            continue
        
        # Code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            i += 1
            continue
        
        if in_code_block:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(1.0)
            run = p.add_run(line)
            run.font.name = FONT_MONO
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor.from_string('4A4A4A')
            i += 1
            continue
        
        # Table detection
        if line.strip().startswith('|') and '|' in line.strip()[1:]:
            table_lines.append(line)
            i += 1
            continue
        elif table_lines:
            # End of table - render it
            _render_table(doc, table_lines, is_header_table=first_table_is_header)
            if first_table_is_header:
                first_table_is_header = False
            table_lines = []
        
        # Headings
        if line.startswith('# '):
            p = doc.add_paragraph()
            p.space_before = Pt(12)
            p.space_after = Pt(6)
            run = p.add_run(line[2:].strip())
            run.font.name = FONT_BODY
            run.font.size = FONT_SIZE_H1
            run.font.color.rgb = RGBColor.from_string(COLOR_ACCENT)
            run.bold = True
            i += 1
            continue
        
        if line.startswith('## '):
            p = doc.add_paragraph()
            p.space_before = Pt(12)
            p.space_after = Pt(4)
            run = p.add_run(line[3:].strip())
            run.font.name = FONT_BODY
            run.font.size = FONT_SIZE_H2
            run.font.color.rgb = RGBColor.from_string(COLOR_ACCENT)
            run.bold = True
            i += 1
            continue
        
        if line.startswith('### ') or line.startswith('#### '):
            p = doc.add_paragraph()
            p.space_before = Pt(8)
            p.space_after = Pt(3)
            run = p.add_run(line.split(' ', 1)[1].strip())
            run.font.name = FONT_BODY
            run.font.size = FONT_SIZE_H3
            run.font.color.rgb = RGBColor.from_string(COLOR_ACCENT)
            run.bold = True
            i += 1
            continue
        
        # Numbered list items
        num_match = re.match(r'^(\d+)\.\s+(.+)', line.strip())
        if num_match:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(1.0)
            p.paragraph_format.first_line_indent = Cm(-0.5)
            p.space_after = Pt(3)
            process_inline_formatting(p, f"{num_match.group(1)}. {num_match.group(2)}")
            i += 1
            continue
        
        # Bullet list items
        bullet_match = re.match(r'^[-*]\s+(.+)', line.strip())
        if bullet_match:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(1.0)
            p.paragraph_format.first_line_indent = Cm(-0.3)
            p.space_after = Pt(2)
            process_inline_formatting(p, f"• {bullet_match.group(1)}")
            i += 1
            continue
        
        # Checkbox items (☐)
        if '☐' in line:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.5)
            p.space_after = Pt(3)
            process_inline_formatting(p, line.strip())
            i += 1
            continue
        
        # Bold-label lines (like "**NCR Number:** ...")
        if line.strip().startswith('**') and ':**' in line:
            p = doc.add_paragraph()
            p.space_after = Pt(3)
            process_inline_formatting(p, line.strip())
            i += 1
            continue
        
        # Regular paragraph
        if line.strip():
            p = doc.add_paragraph()
            p.space_after = Pt(4)
            process_inline_formatting(p, line.strip())
        
        i += 1
    
    # Flush any remaining table
    if table_lines:
        _render_table(doc, table_lines, is_header_table=first_table_is_header)
    
    # Add footer with document number and revision
    _add_footer(doc, lines)
    
    # Save
    doc.save(str(docx_path))
    print(f"  Created: {docx_path}")
    return docx_path


def _render_table(doc, table_lines, is_header_table=False):
    """Render a markdown table as a Word table."""
    rows = parse_markdown_table(table_lines)
    if not rows:
        return
    
    num_cols = len(rows[0])
    num_rows = len(rows)
    
    table = doc.add_table(rows=num_rows, cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    set_table_borders(table)
    
    for row_idx, row_data in enumerate(rows):
        for col_idx, cell_text in enumerate(row_data):
            if col_idx >= num_cols:
                continue
            cell = table.rows[row_idx].cells[col_idx]
            cell.text = ''
            p = cell.paragraphs[0]
            p.space_before = Pt(2)
            p.space_after = Pt(2)
            
            font_size = FONT_SIZE_HEADER_TABLE if is_header_table else FONT_SIZE_BODY
            
            if row_idx == 0 and not is_header_table:
                # Header row styling
                set_cell_shading(cell, COLOR_TABLE_HEADER_BG)
                run = p.add_run(cell_text)
                run.bold = True
                run.font.size = font_size
                run.font.name = FONT_BODY
            elif is_header_table:
                # Document control header - shade the label column
                if col_idx == 0:
                    set_cell_shading(cell, COLOR_HEADER_BG)
                    run = p.add_run(cell_text)
                    run.bold = True
                    run.font.size = font_size
                    run.font.name = FONT_BODY
                else:
                    run = p.add_run(cell_text)
                    run.font.size = font_size
                    run.font.name = FONT_BODY
            else:
                process_inline_formatting(p, cell_text, font_size=font_size)
    
    # Add spacing after table
    p = doc.add_paragraph()
    p.space_before = Pt(4)


def _add_footer(doc, lines):
    """Add a footer with the document number and page numbers."""
    # Extract doc number from first table
    doc_no = ""
    title = ""
    revision = ""
    for line in lines:
        # Use only the first match: later tables may have their own "Title" column.
        if '| Document No.' in line and not doc_no:
            parts = line.split('|')
            if len(parts) >= 3:
                doc_no = parts[2].strip()
        if '| Title' in line and not title:
            parts = line.split('|')
            if len(parts) >= 3:
                title = parts[2].strip()
    
    # Unnumbered courtesy attachments and internal notes have no controlled footer.
    if not doc_no:
        return
    for line in lines:
        if line.startswith('| Revision |'):
            revision = line.split('|')[2].strip()
            break

    for section in doc.sections:
        footer = section.footer
        footer.is_linked_to_previous = False
        p = footer.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        label = " — ".join(value for value in (doc_no, title, f"Rev {revision}" if revision else "") if value)
        run = p.add_run(label)
        run.font.size = FONT_SIZE_SMALL
        run.font.name = FONT_BODY
        run.font.color.rgb = RGBColor.from_string('808080')
        p.add_run(" — Page ")
        for index, field_name in enumerate(("PAGE", "NUMPAGES")):
            if index:
                p.add_run(" of ")
            field = OxmlElement('w:fldSimple')
            field.set(qn('w:instr'), field_name)
            p._p.append(field)


def convert_all(qms_root):
    """Convert all .md files in the qms/ folder tree to .docx."""
    qms_path = Path(qms_root)
    md_files = list(qms_path.rglob('*.md'))
    
    # Exclude this script's own readme or any non-QMS files
    md_files = [f for f in md_files if not f.name.startswith('README')]
    
    print(f"Converting {len(md_files)} markdown files to .docx...")
    print()
    
    for md_file in sorted(md_files):
        docx_file = md_file.with_suffix('.docx')
        convert_md_to_docx(md_file, docx_file)
    
    print(f"\nDone. {len(md_files)} files converted.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python convert_md_to_docx.py <input.md> [output.docx]")
        print("  python convert_md_to_docx.py --all")
        sys.exit(1)
    
    if sys.argv[1] == '--all':
        # Find qms/ root relative to this script
        script_dir = Path(__file__).parent
        convert_all(script_dir)
    else:
        md_input = sys.argv[1]
        docx_output = sys.argv[2] if len(sys.argv) > 2 else None
        convert_md_to_docx(md_input, docx_output)


