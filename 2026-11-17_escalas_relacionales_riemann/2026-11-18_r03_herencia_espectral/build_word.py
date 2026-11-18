from pathlib import Path
import subprocess
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

base=Path(__file__).resolve().parent
source=base/'_R03_Word_combined.md'
header='''# Conservación, herencia y localización de los ceros

**Formalización R–01 / R–02 · Adición v1.1**  
**R–03 · Examen bilingüe · 18 de noviembre de 2026**

Endless Monkey Project  
Relational Geometry Program  \n**Le Matt Ansatz Di Ego**

---

**Edición española / English edition**

Dos anexos de incorporación a R–01/R–02 y dos versiones paralelas del examen R–03. Conserva la formalización original como fuente; este documento no reemplaza una traducción completa de R–01/R–02. / Two insertion addenda and two parallel R–03 editions. The original formalization remains the source; this document is not a full replacement translation of R–01/R–02.

---

'''
chunks=[header]
for name in ['ANEXO_V1_1_CONSERVACION_CEROS_ES.md','R03_HERENCIA_Y_LOCALIZACION_ES.md','ADDENDUM_V1_1_ZERO_PRESERVATION_EN.md','R03_SPECTRAL_INHERITANCE_EN.md']:
    chunks.append((base/name).read_text(encoding='utf-8'))
    chunks.append('\n\n---\n\n')
source.write_text('\n'.join(chunks),encoding='utf-8')
out=base/'R03_Anexo_Bilingue.docx'
subprocess.run(['pandoc',str(source),'--from=markdown+tex_math_dollars+tex_math_single_backslash','--to=docx','--standalone','--output',str(out)],check=True)

doc=Document(out)
section=doc.sections[0]
section.top_margin=Inches(.78);section.bottom_margin=Inches(.7)
section.left_margin=Inches(.83);section.right_margin=Inches(.80)
section.header_distance=Inches(.36)
section.footer_distance=Inches(.36)
styles=doc.styles
for style_name in ['Normal','Body Text']:
    if style_name in styles:
        st=styles[style_name]
        st.font.name='Aptos'
        st.font.size=Pt(9.3)
        st.font.color.rgb=RGBColor(35,42,50)
        st.paragraph_format.space_after=Pt(5.5)
        st.paragraph_format.line_spacing=1.15
for n,size,color in [(1,16,RGBColor(36,57,83)),(2,12,RGBColor(47,77,108)),(3,10,RGBColor(41,81,104))]:
    st=next(st for st in styles if st.name==f'Heading {n}')
    st.font.name='Aptos Display';st.font.size=Pt(size);st.font.bold=True;st.font.color.rgb=color
    st.paragraph_format.space_before=Pt(13 if n==1 else 10)
    st.paragraph_format.space_after=Pt(5)
    st.paragraph_format.keep_with_next=True

# Separate the English edition and main R–03 chapters cleanly.
for p in doc.paragraphs:
    t=p.text.strip()
    if t.startswith(('R–03 · Herencia espectral','R–03 · Spectral inheritance','Addendum to R–01 / R–02')):
        p.paragraph_format.page_break_before=True
    if p.style.name=='Title':
        p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    if p.style.name.startswith('Heading') and p.text.startswith('Conservación, herencia'):
        p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    # Avoid large gaps due to direct pandoc styling
    if p.style.name=='Normal':
        p.paragraph_format.widow_control=True

for table in doc.tables:
    table.alignment=WD_TABLE_ALIGNMENT.CENTER
    table.autofit=True
    for i,row in enumerate(table.rows):
        for cell in row.cells:
            cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            if i==0:
                tcPr=cell._tc.get_or_add_tcPr()
                shd=OxmlElement('w:shd');shd.set(qn('w:fill'),'EAF0F5');tcPr.append(shd)
            for p in cell.paragraphs:
                p.paragraph_format.space_after=Pt(2)

hdr=section.header.paragraphs[0]
hdr.text='Endless Monkey Project  |  R–03  |  ES / EN'
hdr.style=styles['Caption'] if 'Caption' in styles else styles['Normal']
hdr.alignment=WD_ALIGN_PARAGRAPH.RIGHT
footer=section.footer.paragraphs[0]
footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
run=footer.add_run('Relational Geometry Program · 18 XI 2026 · ')
run.font.size=Pt(8);run.font.color.rgb=RGBColor(88,98,107)
field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE')
footer._p.append(field)

doc.save(out)
print(out)
