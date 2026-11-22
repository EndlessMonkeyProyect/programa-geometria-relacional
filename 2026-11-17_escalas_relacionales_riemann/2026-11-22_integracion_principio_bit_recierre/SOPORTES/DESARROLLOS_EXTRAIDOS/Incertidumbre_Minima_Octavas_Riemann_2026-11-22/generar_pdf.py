#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone PDF academico en ReportLab a partir de tablas auditadas."""
from pathlib import Path
import sys, csv, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                               Image, PageBreak, KeepTogether, HRFlowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BASE=Path(__file__).resolve().parent
FONTDIR='/usr/share/fonts/truetype/dejavu'
pdfmetrics.registerFont(TTFont('DejaVu',FONTDIR+'/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBold',FONTDIR+'/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('DejaVu',normal='DejaVu',bold='DejaVuBold',italic='DejaVu')
NAVY=colors.HexColor('#14283D')
INK=colors.HexColor('#1E2730')
MUTED=colors.HexColor('#5C6A75')
HAIR=colors.HexColor('#D9E0E5')
GRAY=colors.HexColor('#F4F6F8')
TEAL=colors.HexColor('#187F83')

with (BASE/'tabla_octavas.csv').open(encoding='utf-8',newline='') as f:
    rows=list(csv.DictReader(f))
for r in rows:
    for k in list(r):
        if k!='j' and k!='m' and r[k]!='':
            try:r[k]=float(r[k])
            except:pass
    r['j']=int(r['j']);r['m']=int(r['m'])

# Academic plots
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titlesize':11,
  'axes.labelsize':9, 'xtick.labelsize':9,'ytick.labelsize':9})
c0=2+0.5772156649015329-math.log(4*math.pi)
fig,ax=plt.subplots(figsize=(7.2,2.95),dpi=175)
js=[r['j'] for r in rows if r['j']>=3]
Y=[r['error_por_logaritmo'] for r in rows if r['j']>=3]
ax.plot(js,Y,color='#1a6177',marker='o',linewidth=2.0,markersize=5,label='Residual × ln(escala)')
ax.axhline(c0,color='#9a6924',linewidth=1.3,linestyle='--',label='Referencia condicional C₀')
ax.set_ylim(0.0445,0.0575)
ax.set_xlim(2.8,11.3)
ax.set_xticks(range(3,12))
ax.grid(axis='y',alpha=.25)
ax.spines[['top','right']].set_visible(False)
ax.set_xlabel('Índice de octava j (escala = 2ʲ)')
ax.set_ylabel('E(2ʲ) · ln(2ʲ)')
ax.legend(frameon=False,loc='upper right',fontsize=8)
fig.tight_layout(pad=1.1)
fig.savefig(BASE/'normalizacion.png',dpi=180)
plt.close(fig)

fig,ax=plt.subplots(figsize=(7.2,2.85),dpi=175)
xx=[r['j'] for r in rows[:-1]][2:]
zz=[r['desfase'] for r in rows[:-1]][2:]
ax.bar(xx,zz,color=['#1a6177' if x>=0 else '#a16a36' for x in zz],width=.62)
ax.axhline(0,color='#56616b',lw=1)
ax.set_xticks(xx)
ax.set_ylabel('εⱼ = (j+2)θⱼ − 1')
ax.set_xlabel('Octava j')
ax.spines[['top','right']].set_visible(False)
ax.grid(axis='y',alpha=.2)
fig.tight_layout(pad=1.0)
fig.savefig(BASE/'desfase.png',dpi=180)
plt.close(fig)

styles={
'kicker':ParagraphStyle('kicker',fontName='DejaVuBold',fontSize=8.3,leading=11.5,textColor=TEAL,spaceAfter=10),
'title':ParagraphStyle('title',fontName='DejaVuBold',fontSize=22,leading=28,textColor=NAVY,spaceAfter=10),
'subtitle':ParagraphStyle('subtitle',fontName='DejaVu',fontSize=11.3,leading=17,textColor=MUTED,spaceAfter=13),
'h1':ParagraphStyle('h1',fontName='DejaVuBold',fontSize=13,leading=17,textColor=NAVY,spaceBefore=14,spaceAfter=8),
'h2':ParagraphStyle('h2',fontName='DejaVuBold',fontSize=10.4,leading=15,textColor=NAVY,spaceBefore=10,spaceAfter=6),
'body':ParagraphStyle('body',fontName='DejaVu',fontSize=9.3,leading=15.0,textColor=INK,spaceAfter=7),
'small':ParagraphStyle('small',fontName='DejaVu',fontSize=8,leading=12.6,textColor=MUTED,spaceAfter=6),
'caption':ParagraphStyle('caption',fontName='DejaVu',fontSize=8,leading=12,textColor=MUTED,spaceAfter=9),
'formula':ParagraphStyle('formula',fontName='DejaVuBold',fontSize=12.7,leading=20,textColor=NAVY,alignment=TA_CENTER,spaceBefore=7,spaceAfter=12),
'bullet':ParagraphStyle('bullet',fontName='DejaVu',fontSize=9.1,leading=14,textColor=INK,leftIndent=12,firstLineIndent=-8,spaceAfter=6),
'footer':ParagraphStyle('footer',fontName='DejaVu',fontSize=8,leading=10,textColor=MUTED)
}

S=[]
def p(t,style='body'):S.append(Paragraph(t,styles[style]))
def h(t):p(t,'h1')
def small(t):p(t,'small')
def formula(t):p(t,'formula')
def img(path,w=474):
    import PIL.Image
    with PIL.Image.open(path) as im:
        x,y=im.size
    S.append(Image(str(path),width=w,height=y*w/x))

p('NOTA DE INVESTIGACIÓN  ·  22 NOVIEMBRE 2026','kicker')
p('Diferencia mínima, memoria<br/>y desfase entre octavas','title')
p('Proyección ortogonal · Herencia aritmética · Normalización diádica','subtitle')
S.append(HRFlowable(width='100%',thickness=.7,color=HAIR,spaceBefore=5,spaceAfter=16))
p('<b>Resumen.</b> La diferencia mínima por escala se define como el menor error cuadrático de reconstrucción de la unidad dentro de las referencias disponibles. Al pasar de una octava a la siguiente, ese error se reparte exactamente entre diferencia resuelta y diferencia pendiente. Una segunda identidad cuantifica la oscilación del error una vez normalizado por el número de octavas. El ensayo utiliza diez transiciones publicadas hasta 2048, distingue el resultado geométrico exacto de la conjetura de cierre y conserva la precisión de la fuente.')

h('1. Definición operacional')
p('Sea <b>H</b> un espacio de Hilbert, <b>χ</b> la unidad de referencia, y <b>V<sub>m</sub> ⊆ V<sub>2m</sub></b> los espacios de reconstrucción admitidos en dos escalas sucesivas. Denótese por <b>P<sub>m</sub></b> la proyección ortogonal sobre V<sub>m</sub>.')
formula('E(m) = ||χ − P<sub>m</sub>χ||²  =  min<sub>v ∈ V<sub>m</sub></sub> ||χ − v||²')
p('Aquí «mínima» alude a la mejor aproximación disponible dentro del espacio elegido. Es un resto estructural del problema de aproximación, no una afirmación sobre una cantidad ontológica universal.')

h('2. Identidad de herencia y cierre')
formula('E(m) = Δ(m) + E(2m)')
formula('Δ(m) = ||(P<sub>2m</sub> − P<sub>m</sub>)χ||² ≥ 0')
p('<b>Prueba.</b> La diferencia entre las proyecciones pertenece al subespacio nuevo, perpendicular al error que permanece tras proyectar sobre V<sub>2m</sub>. La descomposición de χ − P<sub>m</sub>χ en esos dos componentes y Pitágoras producen la igualdad. En particular, E(2m) ≤ E(m).')
p('La totalidad se conserva en una igualdad; la diferencia pendiente puede reducirse sin que se destruya la información heredada. Este es el contenido formal del modelo de memoria.')
small('Estado: identidad demostrada en cualquier espacio de Hilbert con subespacios anidados; su lectura ontológica se mantiene separada.')

S.append(PageBreak())
p('IDENTIDAD DE DESFASE','kicker')
h('3. Renormalización: qué significa la «diferencia mínima»')
p('Para la octava j, defínanse E<sub>j</sub> = E(2<sup>j</sup>), la fracción resuelta θ<sub>j</sub> = (E<sub>j</sub> − E<sub>j+1</sub>)/E<sub>j</sub>, y el resto normalizado A<sub>j</sub> = (j+1)E<sub>j</sub>, siempre que E<sub>j</sub> &gt; 0.')
formula('ε<sub>j</sub> = (j+2)θ<sub>j</sub> − 1')
formula('A<sub>j+1</sub> − A<sub>j</sub> = −E<sub>j</sub> ε<sub>j</sub>')
p('<b>Prueba.</b> La herencia da E<sub>j+1</sub> = E<sub>j</sub>(1 − θ<sub>j</sub>). Multiplicar por j+2 y restar (j+1)E<sub>j</sub> produce la identidad. El perfil exacto E<sub>j</sub> = K/(j+1) implica θ<sub>j</sub> = 1/(j+2) y ε<sub>j</sub> = 0.')
p('Cuando ε<sub>j</sub> es positivo, el resto normalizado disminuye; cuando es negativo, aumenta. En ambos casos el error real E<sub>j</sub> continúa siendo no creciente. El desfase mide la variación relativa a una referencia, no una acumulación de error nuevo.')
S.append(Spacer(1,5))
img(BASE/'desfase.png',w=450)
p('Figura 1. Desfase de ganancia en las octavas j=3…10. El único valor negativo mostrado aparece en j=10, asociado al retorno 1024→2048. Cálculo desde datos publicados redondeados.','caption')

h('4. Lectura numérica de la última octava')
p('Entre 1024 y 2048, la fracción resuelta es <b>θ<sub>10</sub> ≈ 0,06644</b>: el error absoluto baja desde ≈0,00667063 hasta ≈0,00622744. Sin embargo, el resto normalizado sube desde <b>A<sub>10</sub> ≈ 0,0733769</b> hasta <b>A<sub>11</sub> ≈ 0,0747293</b>, una subida relativa de aproximadamente <b>1,84 %</b>.')
p('Este cambio de signo es exactamente lo que detecta ε<sub>10</sub> ≈ −0,2027. La cota rígida anterior falla en esa octava, mientras una condición de contracción flexible permanece compatible con los diez casos.')

S.append(PageBreak())
p('ENSAYO ARITMÉTICO','kicker')
h('5. Contraste en diez retornos')
p('La tabla siguiente reconstruye el resto E<sub>j</sub> usando E<sub>1</sub> ≈ 0,289965 y las diez ganancias Δ<sub>j</sub> de la nota del 20-XI-2026. El «certificado» se refiere a una semilla publicada: la columna es su cota inferior relativa, no una verificación de todas las escalas.')

head=['j','Escala','Eⱼ','θⱼ (%)','(j+2)θⱼ','C. semilla']
table_data=[head]
for r in rows[:-1]:
    j=r['j']
    table_data.append([str(j),str(r['m']),f"{r['error']:.6f}",f"{r['theta']*100:.2f}",f"{r['c_critico']:.3f}",f"{r['c_semilla']:.3f}"])
T=Table(table_data,colWidths=[33,65,92,90,99,95],hAlign='CENTER',repeatRows=1)
T.setStyle(TableStyle([
 ('BACKGROUND',(0,0),(-1,0),NAVY),('TEXTCOLOR',(0,0),(-1,0),colors.white),
 ('FONTNAME',(0,0),(-1,0),'DejaVuBold'),('FONTSIZE',(0,0),(-1,0),8.5),
 ('FONTNAME',(0,1),(-1,-1),'DejaVu'),('FONTSIZE',(0,1),(-1,-1),8.0),
 ('TEXTCOLOR',(0,1),(-1,-1),INK),('ALIGN',(0,0),(-1,-1),'CENTER'),
 ('VALIGN',(0,0),(-1,-1),'MIDDLE'),('TOPPADDING',(0,0),(-1,-1),7),
 ('BOTTOMPADDING',(0,0),(-1,-1),7),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,GRAY]),
 ('LINEBELOW',(0,0),(-1,0),.7,NAVY),
 ('LINEABOVE',(0,-1),(-1,-1),.8,TEAL),
]))
S.append(T)
S.append(Spacer(1,12))
p('<b>Controles finitos.</b> El criterio θ<sub>j</sub> ≥ 0,75/(j+2) pasa las diez octavas. El certificado de semilla ≥ 0,50 E<sub>j</sub>/(j+2) también pasa las diez, incluso permitiendo media unidad del último decimal de cada dato publicado. La versión θ<sub>j</sub> ≥ 1/(j+2) falla en j=10.')

h('6. Un perfil logarítmico de comparación')
img(BASE/'normalizacion.png',w=465)
p('Figura 2. E(2<sup>j</sup>) ln(2<sup>j</sup>) para j=3…11. La línea horizontal corresponde a C₀ = 2+γ−ln(4π) ≈ 0,0461914, referencia asintótica <b>condicional</b>; no es una cota inferior puntual establecida en esta nota.','caption')

S.append(PageBreak())
p('ALCANCE MATEMÁTICO','kicker')
h('7. Cota inferior y límite interpretativo')
p('El resultado clásico de Burnol establece una obstrucción asintótica inferior en el problema de Nyman–Beurling, expresada mediante los ceros de ζ situados sobre la recta crítica y sus multiplicidades. La constante total C₀ = 2+γ−ln(4π) resulta como referencia bajo RH con ceros simples; Bettin–Conrey–Farmer obtienen la asintótica superior correspondiente bajo RH y otra hipótesis cuantitativa sobre ζ′.')
p('Así, un resto estrictamente positivo a escala finita es compatible con la interpretación de una «incertidumbre mínima por nivel». El límite E(m)→0 —que el criterio de Báez-Duarte relaciona con RH— es una afirmación diferente. Una cota <b>inferior</b> describe la cantidad que debe permanecer; demostrar el cierre exige controlar el resto <b>desde arriba</b> o garantizar suficientes ganancias acumuladas.')

h('8. Certificado de reducción y condición suficiente')
formula('Δ(m) ≥ |⟨r<sub>m</sub>,g⟩|² / ||(I−P<sub>m</sub>)g||²')
p('La desigualdad vale para toda semilla admisible g del nuevo espacio. Se obtiene por Cauchy–Schwarz, con r<sub>m</sub> = χ − P<sub>m</sub>χ. Convertirla en una ley global requiere acotar el cociente en términos de E(m) para todas las referencias aritméticas.')
formula('θ<sub>j</sub> ≥ c/(j+2),  c &gt; 0,  j suficientemente grande')
p('Si esta cota suficiente se demostrara aritméticamente, la suma de las ganancias relativas divergiría, el producto E<sub>J</sub> = E<sub>1</sub>∏<sub>j&lt;J</sub>(1−θ<sub>j</sub>) tendería a cero y se cumpliría la condición equivalente a RH en la realización precisa del criterio. Las identidades geométricas y los datos finitos no establecen todavía esa cota.')

h('9. Dictamen')
p('<b>Demostrado:</b> conservación del presupuesto de proyección e identidad del desfase renormalizado.<br/><b>Contrastado:</b> diez octavas; caída de la cota rígida; reducción real y subida renormalizada simultáneas en la última.<br/><b>Abierto:</b> una ley de ganancia aritmética válida para todas las octavas, obtenida sin suponer RH.')

h('Fuentes y reproducción')
small('Mecanismos del programa frente a la regla de eliminación entre escalas (20-XI-2026), tabla de diez octavas; DICTAMEN O18 (19-X-2026); L. Báez-Duarte (2002), arXiv:math/0202141; J.-F. Burnol (2001/2002), arXiv:math/0103058; S. Bettin, J. B. Conrey y D. W. Farmer (2012/2013), arXiv:1211.5191.')
small('El script certificar_incertidumbre.py comprueba la recurrencia, la identidad de fase, las comparaciones y el margen del redondeo. No reejecuta la matriz de Gram original. Ningún resultado se declara prueba de RH.')
p('Endless Monkey Project / Relational Geometry Program','small')

OUT=BASE/'NOTA_INCERTIDUMBRE_RELACIONAL_ES.pdf'
doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=57,leftMargin=57,topMargin=55,bottomMargin=58,
    title='Diferencia mínima, memoria y desfase entre octavas',author='Endless Monkey Project / Relational Geometry Program')

def footer(canvas,doc):
    canvas.saveState()
    canvas.setStrokeColor(HAIR)
    canvas.line(57,49,A4[0]-57,49)
    canvas.setFont('DejaVu',7.4)
    canvas.setFillColor(MUTED)
    canvas.drawString(57,36,'Investigación matemática · 22.11.2026')
    canvas.drawRightString(A4[0]-57,36,f'{doc.page}')
    canvas.restoreState()

doc.build(S,onFirstPage=footer,onLaterPages=footer)
print('PDF:',OUT)
