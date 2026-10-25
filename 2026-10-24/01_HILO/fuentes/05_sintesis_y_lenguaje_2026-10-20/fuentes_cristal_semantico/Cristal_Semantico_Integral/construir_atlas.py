#!/usr/bin/env python3
"""Build printable / readable semantic atlas from validated relational JSON.
No automatic ROSI evaluation; discriminant states are editorial hypotheses.
"""
import json, csv, re, html
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Table, TableStyle, Image, HRFlowable, CondPageBreak)

ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'CRISTAL_DATOS.json').read_text(encoding='utf-8'))
N={n['id']:n for n in D['nodes']};AX=D['axes']
COLORS={k:colors.HexColor(v['color']) for k,v in AX.items()}

def assert_valid():
    assert len(N)==len(D['nodes'])
    assert len(D['discriminants'])==len({x['id'] for x in D['discriminants']})
    assert set(D['families'])=={n['family'] for n in D['nodes']}
    for n in D['nodes']:
        assert n['axes'] and set(n['axes']) <= set(AX) and n['primary'] in AX
        assert n['source'] and n['epistemic'] and n['history_status']
    for col in ('links','discriminants'):
        for e in D[col]: assert e['a'] in N and e['b'] in N, e
    assert set(d['status'] for d in D['discriminants']) <= {'CANDIDATO','INTERPRETACIÓN','DERIVABLE','FORMAL SEGÚN CONTRATO','ABIERTO','ESTÁNDAR','OPEN','FORMAL'}
assert_valid()

md=[]
def M(s=''):md.append(s)
M('# CRISTAL SEMÁNTICO INTEGRAL')
M('**Atlas de lenguaje y diferencias del Programa de Geometría Relacional — edición 1.0 · 16 de octubre de 2026**  ')
M('**Obra del programa:** Le Matt Ansatz Di Ego · **Organización del atlas:** asistencia de ChatGPT')
M('')
M('**Alcance.** Este atlas cubre los **100 términos seleccionados** del corpus consultado, no todas las palabras de todas las conversaciones. Contiene **30 relaciones con determinante propuesto o formalizado** y **101 conexiones de lectura**. Es un artefacto de investigación extensible, no un diccionario de autoridad ni un evaluador ROSI ejecutado.')
M('')
M('## 1. Principio y secuencia')
M('Una palabra entra en la mente como símbolo, experiencia y uso social. Un concepto no es idéntico a su nombre: puede sostenerse en una trama de relaciones. Comparar dos conceptos equivale a formular una pregunta contextual sobre lo que comparten y aquello que los distingue. El determinante candidato de una comparación es la **relación mínima suficiente para decidir esa pregunta bajo un contrato declarado**. Una vez acreditada, esa diferencia puede servir como nueva referencia o nodo; ello no asegura verdad universal ni identidad con el vocabulario ordinario.')
M('')
M('**Orden:** narrativa y evocación → ontología del programa → epistemología y historia de uso → formalización → prueba, falsador o estado abierto. Esto evita introducir matemática o lecturas físicas antes de establecer el objeto de comparación.')
M('')
M('## 2. Dos matrices diferentes')
M('### Siete capas de lectura de cada palabra')
for i,x in enumerate(['Narrativa: situación que la palabra permite contar.', 'Ontología: qué supone el programa que existe o se sostiene.', 'Epistemología: qué puede justificarse y qué sigue abierto.', 'Historia y etimología: recorrido de la expresión, con fuente verificable cuando exista.', 'Uso social actual: sentidos esperables y posibles confusiones.', 'Símbolo: imagen mental probable; orienta, pero no demuestra.', 'Traducción y formalización: equivalentes condicionados en inglés y realización matemática con dominio declarado.'],1):M(f'{i}. {x}')
M('')
M('### Nueve orientaciones cromáticas (no son puntuaciones)')
M('| Color | Orientación | Símbolo público |')
M('|---|---|---|')
for id,a in AX.items(): M(f"| `{a['color']}` | {a['label']} | {a['image']} |")
M('')
M('## 3. Protocolo ROSI/RC-1 para los determinantes')
M('**No es ejecución del plugin ROS-1 Lite.** Es aplicación editorial de su especificación: `REQUEST_DISCRIMINANT`, estado `OPEN / RESOLVED / SUPERPOSED / COLLAPSED`, prueba de suficiencia y preservación del residuo. El protocolo distingue el concepto de su ejemplo y una metáfora de un resultado comprobado.')
M('')
M('**Entrada:** pareja de conceptos `A,B`, pregunta `q`, contexto `c`, familia de futuras comparaciones permitidas, fuentes. **Salida:** coincidencias, diferencia candidata, condición de suficiencia, falsador y estado. **Regla:** si cambiar `A` por `B` no modifica la respuesta a `q` bajo `c`, esa pregunta **no acredita** una diferencia. Si una relación aislada no basta, preservar un conjunto o familia de determinantes, sin fusionarlos por estética.')
M('')
M('### Definición metodológica de diferencia mínima')
M('Sea `E` un repertorio finito de distinciones candidatas y `F_(q,c)` una función de respuesta declarada. Un conjunto `D⊆E` es **suficiente para distinguir** A de B cuando sus respuestas son distintas usando D y siguen siendo distintas para el repertorio pertinente. El conjunto es **irreducible** cuando quitar cualquiera de sus elementos destruye esa suficiencia. Entre conjuntos irreducibles, puede buscarse cardinalidad mínima relativa a E y a q. **No se ha demostrado** una distancia numérica universal, unicidad del determinante, simetría, desigualdad triangular ni invariancia ante cambios de vocabulario; tampoco se declara que el determinante sea siempre una sola palabra.')
M('')
M('### Estados y límites')
M('- **CANDIDATO:** diferencia plausible sujeta a ejemplos y contraejemplos.')
M('- **INTERPRETACIÓN:** distinción de lenguaje del programa, no teorema.')
M('- **DERIVABLE:** consecuencia demostrable solo al fijar el contrato mencionado.')
M('- **FORMAL SEGÚN CONTRATO:** diferenciación referida a definiciones declaradas.')
M('- **ABIERTO:** la pregunta aún necesita un discriminante.')
M('- **ESTÁNDAR:** distinción matemática o terminológica conocida, que puede coexistir con otra lectura ontológica.')
M('- **OPEN:** todavía no se recupera el discriminante suficiente; conservar la pregunta abierta.')
M('- **FORMAL:** diferencia sostenida por definiciones operativas bajo condiciones declaradas.')
M('')
M('## 4. Recorridos esenciales')
for title,path,why in [
 ('Nacimiento de unidad', 'Narrativa → Reflexión → Diferencia → Relación → Comparación → Cierre en sí → Unidad', 'No equiparar reflexividad con consistencia; el cierre es relativo a relaciones suficientes.'),
 ('Trama común', 'Unidad → Trama común → Familia de soluciones → Interfaz → Núcleo suficiente → Continuidad', 'Herencia se reserva para transmisión; la comunidad de relaciones puede ser simultánea.'),
 ('Casa y hogar', 'Casa → Pertenencia relacional (candidata) → Hogar', 'Es el sistema que habita y se reconoce; no atribuimos autorreflexión a un inmueble.'),
 ('Comprensión', 'Recordar → Integración operativa (candidata) → Entender', 'Entender una idea implica poder relacionarla y usarla en preguntas nuevas; no equivale a memoria literal.'),
 ('Cristal matemático', 'Cápsula → Cristal relacional J → Contenido persistente P → Estado suficiente N → Resolución → Cierre relativo', 'La equivalencia de interfaz depende de preguntas y futuros admitidos.'),
 ('Gravedad', 'Diferencia → Sintonía → Redistribución → Modo A → Gravedad relacional (hipótesis)', 'Metáfora y mecanismo postulado no equivalen a una ley observacional derivada.'),
 ('Computación', 'Representación → Configuración → Solución → Respuesta → Algoritmo → P/NP', 'Probar semántica o compresión particular no demuestra P=NP; costo computacional es distinto de trabajo físico.')]:
 M(f'### {title}\n**Ruta:** {path}.\n\n**Condición:** {why}\n')
M('## 5. Catálogo de términos (100 fichas)')
for fam,title in D['families'].items():
    M(f'\n### {title}')
    for k,n in enumerate((x for x in D['nodes'] if x['family']==fam),1):
        M(f"\n#### {n['label']} · `{n['id']}`")
        M(f"**Inglés:** {n['en']} · **Facetas:** {', '.join(AX[a]['label'] for a in n['axes'])} · **Símbolo:** {n['symbol']}")
        M(f"- **Narrativa:** {n['narr']}")
        M(f"- **Ontología:** {n['onto']}")
        M(f"- **Realización matemática candidata:** {n['formal']}")
        M(f"- **Uso y confusión actual:** {n['current']}")
        M(f"- **Historia de la palabra:** {n['history']} **[{n['history_status']}]**")
        M(f"- **Estado epistémico:** {n['epistemic']}. **Procedencia:** {n['source']}.")
M('\n## 6. Determinantes en el cristal (30 fichas)')
M('Cada diamante en el mapa corresponde a una pregunta de discriminación entre dos nodos y **no** a una equivalencia. El protocolo es una aplicación editorial, no una salida certificada del evaluador.')
for d in D['discriminants']:
    M(f"\n### {d['id'].upper()} · {N[d['a']]['label']} ↔ {N[d['b']]['label']}")
    M(f"**Diferencia propuesta:** **{d['label']}** · **Estado:** {d['status']}")
    M(f"- **Pregunta:** {d['question']}")
    M(f"- **Contraste:** {d['contrast']}")
    M(f"- **Contexto / contrato:** {d['scope']}")
    M(f"- **Falsador o límite:** {d['falsifier']}")
    M(f"- **Rastro:** {d['source']}.")
M('\n## 7. Conexiones de lectura (101)')
M('Estas aristas indican recorridos editoriales. Una conexión no constituye implicación, equivalencia semántica ni prueba de relación necesaria.')
for e in D['links']:M(f"- {N[e['a']]['label']} ↔ {N[e['b']]['label']} · {e['type']} · {e['why']}")
M('\n## 8. Bibliografía interna y trazabilidad')
for key,filename in D['sources'].items():M(f'- **{key}:** `{filename}`.')
M('- **ROSI: regla aplicable, no ejecución.** La especificación de RC-1 clasifica respuestas y pide discriminantes; no demuestra por sí misma qué definición de hogar o de cierre es universal.')
M('- **Etimologías:** salvo referencias históricas explícitamente verificadas, las fichas son pistas etimológicas para cotejar antes de publicación. No son afirmaciones de investigación lexicográfica completada.')
M('- **Cobertura:** 100 conceptos seleccionados del material accesible; edición ampliable. «Todo» aquí significa un atlas integral de las áreas principales, no una afirmación de exhaustividad del historial.')
M('- **Sincronización:** el JSON es la fuente estructurada para visualizaciones y nuevos nodos; las tablas CSV son exportaciones, y este documento conserva el razonamiento en lenguaje.')
M('\n## 9. Criterios de crecimiento futuro')
M('Al crear otro determinante: (1) declarar A y B; (2) declarar pregunta y contexto; (3) identificar lo común y la diferencia; (4) dar un testigo que separe; (5) intentar quitar relaciones candidatas sin perder respuesta; (6) definir falsador; (7) distinguir traducción/uso público/ontología/formalización; (8) registrar el estado; (9) si se acredita, permitir que ese determinante sea también nodo. No hacer crecer el cristal por analogía decorativa.')
mdpath=ROOT/'ATLAS_COMPLETO.md';mdpath.write_text('\n'.join(md)+'\n',encoding='utf-8')

# PDF authored with reportlab; semantic text remains in markdown/JSON.
pdfmetrics.registerFont(TTFont('DejaVu','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu-Bold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
WHITE=colors.HexColor('#14273A'); MUTED=colors.HexColor('#5A7082'); GOLD=colors.HexColor('#A87937')
styles={}
styles['big']=ParagraphStyle('big',fontName='DejaVu-Bold',fontSize=24,leading=29,textColor=WHITE,spaceAfter=14)
styles['subtitle']=ParagraphStyle('sub',fontName='DejaVu',fontSize=11,leading=17,textColor=MUTED,spaceAfter=22)
styles['h1']=ParagraphStyle('h1',fontName='DejaVu-Bold',fontSize=14.8,leading=20,textColor=WHITE,spaceBefore=15,spaceAfter=9,keepWithNext=True)
styles['h2']=ParagraphStyle('h2',fontName='DejaVu-Bold',fontSize=10.4,leading=15,textColor=WHITE,spaceBefore=11,spaceAfter=7,keepWithNext=True)
styles['txt']=ParagraphStyle('txt',fontName='DejaVu',fontSize=8.4,leading=13,textColor=WHITE,spaceAfter=6)
styles['small']=ParagraphStyle('small',fontName='DejaVu',fontSize=7.5,leading=11.5,textColor=MUTED,spaceAfter=3)
styles['term']=ParagraphStyle('term',fontName='DejaVu-Bold',fontSize=10.7,leading=15,textColor=WHITE,spaceBefore=8,spaceAfter=5,keepWithNext=True)
styles['label']=ParagraphStyle('label',fontName='DejaVu-Bold',fontSize=8,leading=12,textColor=GOLD,spaceAfter=4)

def esc(s):return html.escape(str(s)).replace('\n','<br/>')
def para(s,style='txt'):return Paragraph(esc(s),styles[style])

def sec(text): return Paragraph(esc(text),styles['h1'])
def mini(text):return Paragraph(esc(text),styles['h2'])

pdfpath=ROOT/'ATLAS_SEMANTICO_COMPLETO.pdf'
page_w,page_h=A4

def footer(canvas,doc):
 canvas.saveState();canvas.setStrokeColor(colors.HexColor('#C5D1D9'));canvas.line(18*mm,17*mm,page_w-18*mm,17*mm)
 canvas.setFont('DejaVu',7);canvas.setFillColor(colors.HexColor('#6D8193'))
 canvas.drawString(18*mm,12*mm,'CRISTAL SEMÁNTICO  /  ATLAS INTEGRAL · ED. 1.0')
 canvas.drawRightString(page_w-18*mm,12*mm,str(doc.page))
 canvas.restoreState()

doc=SimpleDocTemplate(str(pdfpath),pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=20*mm,bottomMargin=22*mm,title='Cristal semántico integral',author='Le Matt Ansatz Di Ego · Atlas con asistencia de ChatGPT')
story=[]
story.append(Spacer(1,25*mm));story.append(para('CRISTAL SEMÁNTICO','big'))
story.append(para('Atlas integral de diferencias, símbolos y relaciones del Programa de Geometría Relacional','subtitle'))
story.append(para('100 términos  ·  30 determinantes  ·  101 relaciones de lectura  ·  7 familias  ·  9 orientaciones'))
story.append(Spacer(1,12*mm))
story.append(para('Narrativa → Ontología → Epistemología e historia → Matemática → Contraste','h2'))
story.append(para('El cristal compara conceptos sin colapsar sus sentidos. Una conexión no es por defecto sinónimo, implicación ni distancia semántica validada. Su determinante es una diferencia relativa a una pregunta y un contexto, sujeta a prueba y a contraejemplos.'))
story.append(Spacer(1,18*mm))
story.append(para('Edición de investigación · 16 de octubre de 2026','small'))
story.append(para('Alcance: corpus accesible, no exhaustivo; etimologías marcadas como pendientes de verificación; evaluación ROSI aplicada manualmente, plugin no ejecutado.','small'))
story.append(PageBreak())
story.append(sec('Cómo leer el cristal'))
for t in [
'Cada término reúne siete capas: narrativa, ontología, epistemología, historia, uso actual, símbolo y traducción/formalización. Una palabra puede evocar más de una imagen; eso se registra sin imponer sinonimia.',
'Los nueve colores señalan orientación semántica y no grados de verdad, frecuencia social, fuerza causal ni proximidad métrica. Los diamantes del mapa son determinantes explícitos o candidatos.',
'ROSI/RC-1 propone exigir pregunta, respuesta que se modifica, diferencia que la justifica, falsador y estado de resolución. Este atlas aplica editorialmente esas reglas: no se ejecutó el evaluador.',
'La mínima diferencia depende de un repertorio de distinciones y de una pregunta. Una diferencia irreducible puede tener varias piezas; puede haber más de un determinante mínimo. No se ha demostrado una métrica universal entre palabras.',
'No confundir los cristales: «cristal semántico» es un atlas lingüístico; «cristal relacional» es una estructura de compatibilidades conjuntas J. La formalización previa define J=S_C join S_E join B, contenido persistente P_Z y estados suficientes N_Q,G bajo un contrato.'
]:story.append(para(t))
story.append(sec('Orientaciones cromáticas'))
for k,a in AX.items():
 tbl=Table([[Paragraph('<font color="'+a['color']+'"><b>●</b></font>',styles['txt']),Paragraph(esc(a['label']),styles['txt']),Paragraph(esc(a['image']),styles['small'])]],colWidths=[9*mm,52*mm,105*mm]);tbl.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),4)]));story.append(tbl)
story.append(sec('Ruta de construcción del determinante'))
for t in ['1. Declarar los dos conceptos y la pregunta que obliga a distinguirlos.', '2. Identificar semejanzas y diferencias condicionadas por el contexto.', '3. Dar un testigo que cambie la respuesta al sustituir un concepto por otro.', '4. Retirar relaciones candidatas hasta encontrar un conjunto irreducible; si la respuesta no cambia, no hay discriminante acreditado para esa pregunta.', '5. Registrar falsador, procedencia y estado; mantener la duda cuando no hay cierre suficiente.', '6. Solo después, usar el determinante como nuevo nodo, si sostiene comparaciones adicionales.']:
 story.append(para(t))
story.append(PageBreak())
story.append(sec('Recorridos centrales'))
for name,path,limit in [
 ('Unidad y cierre','Narrativa → Reflexión → Diferencia → Comparación → Cierre en sí → Unidad','La autorreferencia no garantiza por sí sola consistencia.'),
 ('Trama y suficiencia','Trama común → Familia de soluciones → Interfaz → Núcleo suficiente → Continuidad','La equivalencia siempre depende de la pregunta y futuros permitidos.'),
 ('Casa y hogar','Casa → pertenencia relacional (candidata) → Hogar','Quien se reconoce es el sistema habitante, no el edificio.'),
 ('Recordar y entender','Recordar → integración operativa (candidata) → Entender','Memoria literal y comprensión no son equivalentes.'),
 ('Cristal relacional','Cápsula → J → P_Z → N_Q,G → Resolución → Cierre relativo','Eliminar variables conserva semántica bajo contrato, pero no garantiza economía universal.'),
 ('Física y epistemología','Sintonía → Redistribución → Modo A → Gravedad propuesta','El puente observacional sigue sujeto a prueba.'),
 ('Computación','Representación → Solución → Respuesta → P / NP','No inferir P=NP de normalizaciones particulares.')]:
 story.append(mini(name));story.append(para(path));story.append(para(limit,'small'))
story.append(PageBreak())

story.append(sec('I. Los cien términos del cristal'))
for f,title in D['families'].items():
 story.append(CondPageBreak(42*mm))
 story.append(sec(title))
 for n in (x for x in D['nodes'] if x['family']==f):
  elements=[Paragraph(esc(n['label'])+' <font color="#61788A">/ '+esc(n['en'])+'</font>',styles['term']),
            para('Narrativa. '+n['narr']), para('Ontología. '+n['onto']),para('Formalización. '+n['formal']),
            para('Uso actual. '+n['current'],'small'),para('Etimología. '+n['history']+' ['+n['history_status']+']','small'),
            para('Símbolo: '+n['symbol']+'  ·  Facetas: '+', '.join(AX[a]['label'] for a in n['axes']),'small'),
            para('Estado: '+n['epistemic']+'  ·  Fuente: '+n['source'],'small'),
            Spacer(1,4*mm)]
  story.append(KeepTogether(elements))
story.append(PageBreak())
story.append(sec('II. Los treinta determinantes'))
for d in D['discriminants']:
 a,b=N[d['a']],N[d['b']]
 elements=[Paragraph(esc(d['id'].upper()+' · '+a['label']+' ↔ '+b['label']),styles['term']),
 para('Determinante: '+d['label']+'  ·  '+d['status'],'label'),
 para('Pregunta. '+d['question']),para('Contraste. '+d['contrast']),
 para('Contexto. '+d['scope'],'small'),para('Falsador o límite. '+d['falsifier'],'small'),
 para('Rastro: '+d['source'],'small'),Spacer(1,4*mm)]
 story.append(KeepTogether(elements))
story.append(PageBreak());story.append(sec('III. Procedencia, cautelas y edición'))
for key,src in D['sources'].items():story.append(para(key+' — '+src))
for s in ['Este atlas usa fuentes internas accesibles y algunas etimologías de trabajo. Las notas de historia señaladas para verificar requieren control lexicográfico antes de publicar como hechos establecidos.', 'Cada vínculo de los 101 recorridos editoriales se encuentra en CRISTAL_DATOS.json y en ATLAS_COMPLETO.md. La visualización interactiva conserva su recorrido, color, estado, origen y pregunta.', 'El evaluador ROS-1 Lite no se ejecutó como plugin durante esta edición; los estados de los determinantes son aplicaciones editoriales de un protocolo documentado.', 'La normalización 7+1, los puentes dinámicos y las formalizaciones de P/NP se incluyen como conceptos del programa, sin declararlos demostraciones físicas ni soluciones de problemas abiertos.']:
 story.append(para(s))
story.append(Spacer(1,8*mm));story.append(para('Para ampliar el cristal, editá CRISTAL_DATOS.json y regenerá el PDF; los determinantes deben conservar pregunta, alcance, falsador, estado y procedencia.','small'))
doc.build(story,onFirstPage=footer,onLaterPages=footer)

with (ROOT/'README.txt').open('w',encoding='utf-8') as f:
 f.write('CRISTAL SEMÁNTICO INTEGRAL — v1.0, 16-10-2026\n')
 f.write('100 conceptos · 30 determinantes · 101 relaciones · 7 familias · 9 orientaciones\n\n')
 f.write('ABRIR: CRISTAL_INTERACTIVO.html con navegador moderno; no necesita internet.\n')
 f.write('VER POSTER: CRISTAL_INTEGRAL.png.\n')
 f.write('LEER ATLAS: ATLAS_SEMANTICO_COMPLETO.pdf o ATLAS_COMPLETO.md.\n')
 f.write('REUTILIZAR DATOS: CRISTAL_DATOS.json, TERMINOS.csv, DETERMINANTES.csv.\n')
 f.write('MODIFICAR: generar.py y crear_visual.py (origen de mapa), construir_atlas.py (atlas).\n\n')
 f.write('ADVERTENCIAS: no es diccionario normativo ni una métrica universal; los vínculos no prueban equivalencia; los determinantes son editoriales ROSI, evaluador/plugin no ejecutado. Las etimologías están marcadas para verificación.\n')
 f.write('Rastro principal: ontología canónica (27-09), cristal relacional (29-09), ROSI/RC-1, cristal semántico v0.1 (16-10), CONCEPT_MAP.md y otras fuentes señaladas en JSON.\n')
print('Built',mdpath,len(md),'sections; PDF',pdfpath,pdfpath.stat().st_size)
