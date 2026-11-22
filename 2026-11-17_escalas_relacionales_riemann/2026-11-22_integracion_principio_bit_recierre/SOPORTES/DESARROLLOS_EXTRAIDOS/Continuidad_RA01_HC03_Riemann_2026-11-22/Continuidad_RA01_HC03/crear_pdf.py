from pathlib import Path
import csv, math
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether, HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

base=Path(__file__).resolve().parent
rows=list(csv.DictReader((base/'bloques_hc03_2_22.csv').open(encoding='utf-8')))
X=[int(r['j']) for r in rows]
YT=[float(r['B_total_div_critico']) for r in rows]
YP=[float(r['B_primos_div_critico']) for r in rows]
plt.figure(figsize=(8.6,3.3))
plt.plot(X,YT,marker='o',markersize=2.5,label='Desbalance total B(j)')
plt.plot(X,YP,marker='s',markersize=2.5,label='Solo primos nuevos B_pr(j)')
plt.xticks([1,3,5,7,9,11,13,15,17,19,21]);plt.xlabel('Octava j (escala inicial 2^j)')
plt.ylabel('Máximo / [sqrt(2^j) (j+1)^2]')
plt.grid(True,alpha=.2);plt.legend(fontsize=9);plt.tight_layout()
plt.savefig(base/'contraste_bloques.png',dpi=190)
plt.close()

pdfmetrics.registerFont(TTFont('DVS','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVS-B','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('DVS',normal='DVS',bold='DVS-B')
INK=colors.HexColor('#1B2F46')
ACC=colors.HexColor('#3E627B')
LIGHT=colors.HexColor('#EEF2F5')
BODY=colors.HexColor('#303B43')
styles={
 'title':ParagraphStyle('title',fontName='DVS-B',fontSize=20,leading=26,textColor=INK,spaceAfter=10),
 'subtitle':ParagraphStyle('subtitle',fontName='DVS',fontSize=10,leading=15,textColor=ACC,spaceAfter=10),
 'heading':ParagraphStyle('heading',fontName='DVS-B',fontSize=11.3,leading=17,textColor=INK,spaceBefore=14,spaceAfter=7),
 'normal':ParagraphStyle('normal',fontName='DVS',fontSize=8.9,leading=14,textColor=BODY,spaceAfter=8),
 'small':ParagraphStyle('small',fontName='DVS',fontSize=7.8,leading=12,textColor=BODY,spaceAfter=5),
 'note':ParagraphStyle('note',fontName='DVS',fontSize=8.6,leading=13.5,textColor=BODY,spaceAfter=7,leftIndent=7),
 'formula':ParagraphStyle('formula',fontName='DVS-B',fontSize=10.6,leading=18,textColor=INK,alignment=TA_CENTER,spaceBefore=10,spaceAfter=10),
 'th':ParagraphStyle('th',fontName='DVS-B',fontSize=7.1,leading=10,textColor=colors.white),
 'td':ParagraphStyle('td',fontName='DVS',fontSize=7.3,leading=12,textColor=BODY),
}
from xml.sax.saxutils import escape
P=lambda s,sty='normal': Paragraph(s,styles[sty])
PAGE_W,PAGE_H=A4

class Doc(SimpleDocTemplate):
 def __init__(self,filename):
  super().__init__(filename,pagesize=A4,rightMargin=20*mm,leftMargin=20*mm,topMargin=22*mm,bottomMargin=19*mm,title='De la herencia a la discrepancia de primos nuevos',author='Endless Monkey Project / Relational Geometry Program')

def footer(can,doc):
 can.saveState()
 can.setStrokeColor(colors.HexColor('#BBC9D2'))
 can.line(20*mm,15.1*mm,PAGE_W-20*mm,15.1*mm)
 can.setFont('DVS',7.3);can.setFillColor(ACC)
 can.drawString(20*mm,11*mm,'NOTA TÉCNICA  ·  22 NOV 2026  ·  Continuidad RA–01 / HC–02 / HC–03')
 can.drawRightString(PAGE_W-20*mm,11*mm,str(doc.page))
 can.restoreState()

story=[]
story+=[P('De la herencia de potencias a la discrepancia de primos nuevos','title'),
 P('Continuidad matemática  ·  Revisión de RA–01, HC–02 y HC–03  ·  22 de noviembre de 2026','subtitle'),
 HRFlowable(width='100%',thickness=1,color=ACC,spaceBefore=0,spaceAfter=14),
 P('<b>Resultado central.</b> La discrepancia por octava se separa exactamente en eventos de primos ordinarios y eventos de potencias primas heredadas. HC–02 ya proporciona una cota incondicional para la segunda contribución. El control crítico restante corresponde a la fluctuación firmada de los primos ordinarios.'),
 P('1. Definiciones y proposición','heading'),
 P('En la octava de enteros L = 2ʲ ≤ m &lt; 2L, sea C(j,m) la suma de Λ(n) en [L,m] menos la longitud m−L+1. Sea P(j,m) la misma suma restringida a primos ordinarios y H(j,m) la suma de los eventos heredados pᵏ, k ≥ 2.'),
 P('C(j,m) = P(j,m) + H(j,m),     0 ≤ H(j,m) ≤ U(2L)','formula'),
 P('Aquí U(x)=ψ(x)−ϑ(x) es la contribución acumulada de las potencias primas. La desigualdad demostrada en HC–02 afirma, para x ≥ 4:'),
 P('U(x) ≤ C₀ √x,     C₀ = 4 ln(2) + 24/e &lt; 11,602','formula'),
 P('Si B(j) y Bpr(j) denotan los máximos de |C(j,m)| y |P(j,m)| dentro de la octava, respectivamente, se obtiene:'),
 P('|B(j) − Bpr(j)| ≤ U(2L) ≤ C₀ √(2L)','formula'),
 P('<b>Demostración.</b> La identidad ψ=ϑ+U separa los generadores primos de sus potencias. Cada término de H es no negativo, por lo que H(j,m) queda limitado por U(2L). La desigualdad triangular inversa para las normas del máximo prueba el resultado. La estimación final se toma de HC–02.'),
 P('<b>Corolario.</b> La cota crítica B(j)=O(2<super>j/2</super>(j+1)²) de HC–03 es equivalente a la misma cota para Bpr(j). Según el criterio clásico citado en HC–03, ambas son equivalentes a RH. Se trata de una localización del término pendiente, no de su acotación.'),
 P('2. Vínculo con la incertidumbre por escala','heading'),
 P('La diferencia acumulada puede oscilar alrededor de la referencia aun cuando cada contribución heredada sea positiva. Ese aporte puede compensar una desviación negativa de los primos o reforzar una positiva. Esta distinción describe de manera cuantitativa el desfase sin identificarlo automáticamente con una incertidumbre ontológica irreductible.'),
]
story.append(PageBreak())
story+=[P('3. Ensayo finito ampliado','heading'),
 P('Se reprodujo HC–03 por un procedimiento separado: criba para primos, enumeración de potencias primas, sumas acumuladas por octava y un contraste en puntos seleccionados con math.fsum. El intervalo cubre los enteros de 1 a 4.194.303, incluidos 295.947 primos y 399 eventos de potencias primas heredadas.'),
]
cols=['Octava j','Enteros','B(j) total','Bpr(j) nuevos','H de la octava']
show=[10,15,20,21]
labels={10:'1.024–2.047',15:'32.768–65.535',20:'1.048.576–2.097.151',21:'2.097.152–4.194.303'}
tbl=[[P(escape(s),'th') for s in cols]]
for j in show:
 r=rows[j-1]
 tbl.append([P(str(j),'td'),P(labels[j],'td'),P(f"{float(r['B_total']):,.2f}".replace(',','X').replace('.',',').replace('X','.'),'td'),P(f"{float(r['B_primos_nuevos']):,.2f}".replace(',','X').replace('.',',').replace('X','.'),'td'),P(f"{float(r['H_potencias_heredadas']):,.2f}".replace(',','X').replace('.',',').replace('X','.'),'td')])
t=Table(tbl,colWidths=[20*mm,53*mm,30*mm,35*mm,32*mm],hAlign='LEFT')
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#D4DFE6')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,LIGHT]),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
story+=[t,Spacer(1,10),P('Los máximos se calculan sobre todas las posiciones enteras de cada octava. En j=15 la herencia amplía el máximo absoluto; en j=21 lo reduce, pese a que todas sus contribuciones son positivas.','small'),Spacer(1,8),Image(str(base/'contraste_bloques.png'),width=165*mm,height=63*mm),
 P('Gráfico. Amplitud máxima en cada octava dividida por la escala crítica de HC–03. Su tamaño relativamente pequeño en una muestra finita no establece una cota universal.','small'),
 P('En la octava j=21 (2.097.152 a 4.194.303), B=1.230,454; Bpr=1.718,476; y el aporte heredado acumulado es 637,259. Las razones normalizadas son 0,001756 y 0,002452, respectivamente.','normal'),
 P('La igualdad de separación se verificó con error de redondeo máximo inferior a 9×10⁻¹⁰ en doble precisión. Doce puntos de cuatro octavas fueron contrastados por un segundo algoritmo con math.fsum. Los valores decimales son ensayos, no cotas certificadas con aritmética de intervalos.','small')
]
story.append(PageBreak())
story+=[P('4. Qué aporta RA–01 y qué falta probar','heading'),
 P('RA–01 trabaja en otro contrato: el error funcional Q(j) es la norma cuadrática de una proyección en L². Allí la identidad Q(j)=Q(j+1)+Δ(j) es exacta. La divergencia de una suma de ganancias relativas <b>certificadas</b> es un criterio suficiente para que Q(j) tienda a cero. S–RA–01 mide esas ganancias para una semilla de Möbius, de forma finita.'),
 P('La nueva separación de HC–03 concierne a la masa aritmética ponderada de los primos en una ventana. Los eventos «primo nuevo» no son automáticamente las direcciones nuevas del espacio funcional de RA–01. Ambos criterios están conectados con RH, pero no consta una desigualdad que transfiera sus magnitudes sin añadir un argumento aritmético.'),
 P('Obligación matemática pendiente','heading'),
 P('Encontrar una constante K, independiente de j y de la posición m, que garantice para toda octava:'),
 P('máx |Σ log(p) − longitud| ≤ K · 2ʲᐟ² · (j+1)²','formula'),
 P('La suma es sobre los primos del intervalo [2ʲ,m]; la longitud es m−2ʲ+1. En virtud de la proposición de la primera página, esta estimación sería suficiente para HC–03 y equivale a la cota clásica de RH. La desigualdad sigue abierta.'),
 P('Una segunda vía es demostrar las condiciones de ganancias acumuladas certificadas en RA–01 para la familia aritmética concreta. En ambas rutas hay que establecer compensaciones cuantitativas entre aportes nuevos, además de la conservación de referencias heredadas.'),
 P('5. Observación sobre la diferencia mínima','heading'),
 P('La corrección menor que 1/8 de HC–03 mide el defecto de una fórmula de reconstrucción mediante diferencias finitas. Es una cota superior sobre ese defecto, no sobre todo el desbalance de los primos ni una cota mínima de existencia. La lectura relacional de incertidumbre permanece como interpretación que debe vincularse a una magnitud matemática definida.'),
 P('6. Procedencia y control','heading'),
 P('HC–02: <i>Herencia de potencias primas y certificado de transferencia entre escalas</i> (21-XI-2026). HC–03: <i>Diferencia mínima, aparición de referencias y acumulación aritmética</i> (21-XI-2026). RA–01 v5: nota de auditoría matemática (21-XI-2026). S–RA–01: laboratorio de semilla de Möbius incluido en la propuesta de integración v3.5.','small'),
 P('Archivos que acompañan esta nota: REVISION_CONTINUIDAD_ES.md, verificar_bloques_hc03.py, contraste_fsum.py, bloques_hc03_2_22.csv, control.json y contraste_fsum.json. Los scripts no requieren repositorios externos; el primero requiere numpy y el segundo únicamente la biblioteca estándar.','small'),
 Spacer(1,13),HRFlowable(width='100%',thickness=.7,color=ACC),Spacer(1,10),
 P('<b>Dictamen:</b> separación aritmética y cota heredada demostradas a partir de identidades clásicas; verificación finita ampliada. La cota uniforme de los generadores primos y la hipótesis de Riemann permanecen abiertas en este expediente.'),
 P('Endless Monkey Project / Relational Geometry Program','small')]

Doc(str(base/'REVISION_CONTINUIDAD_ES.pdf')).build(story,onFirstPage=footer,onLaterPages=footer)
print('PDF',base/'REVISION_CONTINUIDAD_ES.pdf')
