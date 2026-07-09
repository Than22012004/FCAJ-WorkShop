from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import mm
import os

INPUT_MD = os.path.join(os.path.dirname(__file__), '..', 'workshop_report_vi.md')
OUTPUT_PDF = os.path.join(os.path.dirname(__file__), '..', 'workshop_report_vi.pdf')

def md_to_paragraphs(md_text):
    lines = md_text.splitlines()
    styles = getSampleStyleSheet()
    normal = styles['Normal']
    title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=18, leading=22)
    h2_style = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, leading=18)
    h3_style = ParagraphStyle('H3', parent=styles['Heading3'], fontSize=12, leading=16)
    code_style = ParagraphStyle('Code', parent=styles['Code'], fontName='Courier', fontSize=8, leading=10)

    story = []
    in_code = False
    code_buf = []

    for line in lines:
        if line.strip().startswith('```'):
            in_code = not in_code
            if not in_code:
                # flush code buffer
                code_text = '<br/>'.join(code_buf)
                story.append(Paragraph('<font face="Courier">%s</font>' % code_text.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'), code_style))
                code_buf = []
            continue
        if in_code:
            code_buf.append(line)
            continue
        if line.startswith('# '):
            story.append(Paragraph(line[2:].strip(), title_style))
            story.append(Spacer(1, 6))
            continue
        if line.startswith('## '):
            story.append(Paragraph(line[3:].strip(), h2_style))
            story.append(Spacer(1, 4))
            continue
        if line.startswith('### '):
            story.append(Paragraph(line[4:].strip(), h3_style))
            continue
        if line.startswith('- '):
            story.append(Paragraph('• ' + line[2:].strip(), normal))
            continue
        if line.strip() == '---':
            story.append(Spacer(1, 6))
            continue
        if line.strip() == '':
            story.append(Spacer(1, 4))
            continue
        # fallback
        story.append(Paragraph(line.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'), normal))

    return story


def build_pdf():
    with open(INPUT_MD, 'r', encoding='utf-8') as f:
        md = f.read()
    doc = SimpleDocTemplate(OUTPUT_PDF, pagesize=A4,
                            rightMargin=20*mm, leftMargin=20*mm,
                            topMargin=20*mm, bottomMargin=20*mm)
    story = md_to_paragraphs(md)
    doc.build(story)
    print('PDF generated at', OUTPUT_PDF)

if __name__ == '__main__':
    build_pdf()
