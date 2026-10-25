import json, math, random, pathlib, html, csv, zipfile, textwrap, collections
import networkx as nx
from PIL import Image,ImageDraw,ImageFont
BASE=pathlib.Path('/mnt/data/cristal_semantico_integral');random.seed(20261016)
AXES={
'identidad':('#4B7BAC','Identidad','Contorno / reconocimiento'),
'autorref':('#8166B5','Autorreferencia','Espejos / retorno'),
'cierre':('#C28B3C','Cierre','Anillo / coherencia'),
'trama':('#3E977F','Trama común','Tejido / copresencia'),
'escala':('#398A9B','Escala y continuidad','Semilla / graduación'),
'diferencia':('#C86D63','Diferencia / novedad','Bifurcación'),
'episteme':('#8B82A1','Justificación','Lupa / prueba'),
'dinamica':('#C17A4D','Transformación','Flecha / variación'),
'linguistica':('#6C8DA4','Símbolo / lenguaje','Palabra / signo')}
FAMS={
'narrativa':'01 · Narrativa y lenguaje','ontologia':'02 · Ontología mínima',
'estructura':'03 · Trama, módulo y cristal','matematica':'04 · Cuantificación y forma',
'dinamica':'05 · Transformación y física propuesta','epistemologia':'06 · Epistemología / ROSI',
'computacion':'07 · Preguntas y computación'}
# id | etiqueta | english | familia | principales ejes | narrativa | ontologia | representacion formal posible | símbolo | nota de uso (percepción) 
RAW='''palabra|Palabra|word|narrativa|linguistica,trama|Signo que trae otras asociaciones al ser pronunciado.|No es la cosa ni su referencia necesariamente.|Elemento w de un vocabulario W.|Voz|Una palabra tiene usos polisémicos; no siempre nombra un objeto.
concepto|Concepto|concept|narrativa|linguistica,identidad|Una idea reconocible en contextos distintos.|Contenido articulable por relaciones, no simple etiqueta.|Clase de usos o estructura intensional definida por contexto.|Foco|Se confunde con la palabra que lo expresa.
simbolo|Símbolo|symbol|narrativa|linguistica,trama|Una imagen que hace presente algo por asociación.|Puente comunicativo; no demuestra la noción.|Representación tipada S→contenido según interpretación.|Emblema|Un símbolo puede cambiar de lectura cultural.
metafora|Metáfora|metaphor|narrativa|linguistica,diferencia|Una relación que transporta imágenes entre campos.|Puede orientar búsqueda, nunca sustituir contraste.|Correspondencia parcial entre dos dominios.|Puente|Parecido evocador no equivale a identidad formal.
narrativa|Narrativa|narrative|narrativa|linguistica,dinamica|La historia que permite comprender cómo surge una distinción.|Precede a ontología en nuestro método.|Secuencia explicativa; no una ecuación.|Hilo|Narrar no obliga a que lo narrado sea causal o verdadero.
sentido|Sentido|sense / meaning|narrativa|linguistica,trama|Dirección hacia la que orienta una expresión.|Significación situada en contexto.|Interpretación C de un término o enunciado.|Brújula|Sentido puede significar dirección, percepción o significado.
significado|Significado|meaning|narrativa|linguistica,identidad|Aquello que una palabra permite reconocer.|Depende del uso y de la trama, no sólo del diccionario.|Semántica asignada a expresiones.|Huella|No se agota en una traducción literal.
etimologia|Etimología|etymology|narrativa|linguistica,escala|Rastro de por dónde llegó una palabra.|Historia del signo, no prueba de su ontología.|Relación histórica entre formas léxicas documentadas.|Raíces|Origen no impone significado actual.
uso_actual|Uso actual|current usage|narrativa|linguistica,episteme|Lo que una comunidad entiende hoy al oír un término.|Capa pública distinta de convención técnica.|Datos de corpus y encuestas, cuando existan.|Conversación|Las intuiciones públicas requieren contraste, no son universales.
comprender|Entender|understand|narrativa|trama,identidad|Una idea encuentra lugar entre otras y permite operar.|Integración de relaciones para responder otras preguntas.|Transferencia exitosa a consultas nuevas, prueba operativa.|Cristal habitado|Comprender no exige conciencia de una máquina.
recordar|Recordar|remember / recall|narrativa|escala,linguistica|Recuperar una representación antes accesible.|Persistencia o recuperación sin garantía de integración.|Recuperación de estado o dato almacenado.|Archivo|Recordar datos no equivale a comprenderlos.
habitar|Habitar|inhabit / dwell|narrativa|trama,identidad|Estar en un espacio y sostener una relación con él.|Condición posible de integración, no suficiente para hogar.|Predicado Habita(s,l,t) bajo contrato.|Umbral|Habitar puede ser físico o figurado.
casa|Casa|house|narrativa|identidad,linguistica|Construcción o lugar destinado a vivir.|Referencia de espacio, no pertenencia asegurada.|Predicado Casa(l) declarado.|Techo|En uso cotidiano también puede significar familia o linaje.
hogar|Hogar|home|narrativa|trama,identidad|Lugar o comunidad en que puede reconocerse continuidad propia.|Depende de relaciones de pertenencia, no solo de edificio.|Hogar(l,s,C) requiere criterio contextual.|Fuego|Hogar no requiere propiedad ni casa física estable.
intuicion|Intuición|intuition|narrativa|linguistica,diferencia|Una forma aparece antes que su demostración.|Origen de hipótesis, no evidencia suficiente.|Propuesta H sometible a pruebas.|Chispa|Sentir claridad no garantiza corrección.
unidad|Unidad|unit / unity|ontologia|identidad,cierre|Algo que puede ser reconocido como uno.|Límite singular y luego estructura reconocible por cierre.|Objeto U con criterio de equivalencia de identidad.|Uno|Unidad contable y unidad estructural no son idénticas.
autorreferencia|Autorreferencia|self-reference|ontologia|autorref,identidad|Lo expresado vuelve a tomarse como referencia.|Condición reflexiva; no garantiza coherencia.|Relación R(x,x) o referencia a su propia descripción.|Espejo|No equivale a conciencia ni autoafirmación.
reflexion|Reflexión|reflection|ontologia|autorref,diferencia|Una imagen se devuelve hacia su referencia.|Primer gesto narrativo de diferenciación comparable.|Operación ρ: X→X con condiciones declaradas.|Espejo doble|Reflexión mental, óptica y algebraica son sentidos distintos.
cierre_en_si|Cierre en sí|self-closure|ontologia|cierre,autorref|La estructura se reconoce desde relaciones propias suficientes.|Nombre narrativo preferido de cierre consistente relativo a contrato.|Cierre_C(x) con criterio de consistencia y suficiencia.|Anillo vivo|Self-closure es término del programa, no una acepción universal.
cierre_propio|Cierre propio|own closure / intrinsic closure|ontologia|identidad,cierre|Algo termina o se sostiene por lo propio.|Alternativa léxica menos explícita en autorreferencia.|Sólo equivale con definición adicional.|Sello|Propio puede sugerir propiedad o exclusión.
cierre_autorreferencial|Cierre autorreferencial|self-referential closure|ontologia|autorref,cierre|Las relaciones vuelven a su referente y cierran.|Subraya mecanismo reflexivo sin garantizar consistencia por nombre.|Circuito consistente y criterio de clausura.|Bucle|Autorreferencia puede ser paradójica.
identidad|Identidad|identity|ontologia|identidad,cierre|Reconocer lo mismo entre transformaciones.|Cierre persistente con criterio de pertenencia.|Equivalencia o invariante bajo transformaciones.|Contorno|No es mera igualdad de etiquetas.
diferencia|Diferencia|difference|ontologia|diferencia,identidad|Algo no coincide enteramente con su referencia.|Anterior a distancia y número físico.|Relación de discernibilidad D_C(a,b).|Grieta|No toda diferencia es longitud medible.
referencia|Referencia|reference|ontologia|identidad,autorref|Aquello respecto de lo cual se compara.|Puede ser interior a la unidad.|Objeto, marco o expresión respecto del cual se evalúa.|Punto guía|No requiere observador consciente.
relacion|Relación|relation|ontologia|trama,diferencia|Lo que pone términos en comparación.|Regla que puede conservar una diferencia.|R⊆A×B o relación de aridad mayor.|Enlace|No equivale siempre a arista binaria.
comparacion|Comparación|comparison|ontologia|diferencia,episteme|Se interroga una relación bajo algún criterio.|Separa determinación acreditable de residuo.|Consulta Q_C(x) con criterio explícito.|Balanza|Comparar no significa siempre elegir un ganador.
indeterminacion|Indeterminación|indeterminacy|ontologia|diferencia,episteme|Todavía caben distinciones por resolver.|Estado relacional abierto sin necesidad de azar.|Conjunto o cociente con varias clases distinguibles.|Niebla|No equivale automáticamente a probabilidad.
residuo|Residuo|residue|ontologia|diferencia,escala|Lo que sigue sin resolverse para una pregunta.|Diferencia pertinente pendiente, no sustancia física.|Información discriminante que falta para Q.|Resto visible|Residuo no implica error o basura.
resolucion|Resolución|resolution|ontologia|cierre,dinamica|Una pregunta deja de quedar abierta en algún sentido.|Transformación de diferencia pendiente en estructura acreditada.|T_Y(J)=∃Y J para realización formal.|Nudo resuelto|Resolver no exige elegir una única configuración interna.
novedad|Novedad|novelty|ontologia|diferencia,dinamica|Aparece una distinción no fijada antes.|Aumento de discriminación o estructura en un contrato.|Δr>0 en realización lineal particular.|Brote|Nuevo nombre no necesariamente es novedad estructural.
recursion|Recursión|recursion|ontologia|autorref,dinamica|Un resultado se convierte en nueva referencia.|Cierre que puede participar en nuevos cierres.|Operación iterada F(F(x)).|Espiral|No toda repetición constituye recursión informativa.
cardinalidad|Cardinalidad|cardinality|matematica|escala,diferencia|Se hacen contables las referencias distinguidas.|La cuenta es posterior a diferencia.|Número de elementos de un conjunto finito.|Marcas|El mismo número no acredita el mismo mecanismo.
trama_comun|Trama común|shared relational fabric|estructura|trama,identidad|Relaciones que se sostienen juntas en un presente.|Preferible a herencia cuando hay comunidad actual.|Familia de compatibilidades compartidas.|Tejido|No presupone transmisión temporal.
familia_soluciones|Familia de soluciones|solution family|estructura|trama,diferencia|Varias respuestas participan de una regla.|Clase estructural de realizaciones, no necesariamente genealogía.|S_Q={x:Q(x)=sí} o clase por contrato.|Ramas|Puede tener miembros distintos sin equivalencia total.
herencia|Herencia|inheritance|estructura|escala,trama|Algo ya constituido sigue disponible después.|Reservar para transmisión o procedencia real.|Mapa entre niveles que preserva contenido declarado.|Semilla|No confundir con copresencia estructural.
continuidad|Continuidad|continuity|estructura|escala,identidad|Algo se mantiene al cambiar de forma.|Persistencia de invariantes o coherencia de relaciones.|P_Z(J_t)=P_Z(J_{t+1}) en realización.|Hilo|No significa necesariamente continuidad topológica.
pertenencia|Pertenencia|belonging / membership|estructura|identidad,trama|Lo que puede reconocerse como parte de una trama.|Relación entre sistema y estructura bajo criterio.|s∈C o B_C(s,l) según contexto.|Raíz|Sentimiento, posesión y pertenencia formal difieren.
reconocimiento|Reconocimiento|recognition|estructura|identidad,episteme|Se identifica una estructura como la misma.|Operación situada con criterios, no mero nombrar.|Predicado Reconoce_C(s,x).|Espejo compartido|No implica consciencia en todos los usos técnicos.
capsula|Cápsula|capsule|estructura|cierre,identidad|Una unidad guarda una organización interna.|Estructura con interior, relaciones e interfaz.|C=(Ω,R,D) en formalización previa.|Vaina|No es objeto material por definición.
interior|Interior|interior|estructura|identidad,cierre|Lo que sostiene la unidad desde dentro.|Suprimir lo irrelevante depende de la frontera.|Conjunto I de variables internas.|Núcleo|Interior ontológico no es necesariamente espacial.
frontera|Frontera|boundary|estructura|cierre,diferencia|Donde una unidad puede relacionarse con otra.|Delimitación funcional de preguntas futuras.|Corte I⊔Z con interfaz Z.|Membrana|No requiere pared física.
interfaz|Interfaz|interface|estructura|trama,episteme|La cara por donde una estructura se deja consultar.|Contenido suficiente para ciertas preguntas.|K_Z=π_Z(J).|Puerta|Una interfaz suficiente para Q no lo es para toda Q.
proyeccion|Proyección|projection|estructura|escala,episteme|Se muestra un aspecto conservando alguna relación.|La pérdida de detalle requiere contrato.|π_Z(J)=∃I J.|Sombra|Proyección no garantiza reversibilidad.
cristal_relacional|Cristal relacional|relational crystal|estructura|trama,cierre|Estructura presente de compatibilidades conjuntas.|Formalización distinta del atlas de las palabras.|J=S_C ⋈ S_E ⋈ B.|Cristal facetado|No es cristal mineral ni catálogo de sinónimos.
cristal_semantico|Cristal semántico|semantic crystal|estructura|linguistica,trama|Mapa facetado de palabras, diferencias y símbolos.|Atlas editorial y epistemológico apoyado en el programa.|Red de conceptos y discriminantes tipados.|Prisma|No confundir con el cristal relacional matemático.
nucleo_suficiente|Núcleo suficiente|sufficient core|estructura|cierre,episteme|Lo mínimo que todavía responde una pregunta.|Minimalidad siempre relativa a pregunta y contexto.|C_q* minimiza cardinalidad con respuesta preservada, si existe.|Piedra angular|Mínimo en tamaño no equivale a mínimo en cómputo.
raices_latentes|Raíces latentes|latent roots|estructura|diferencia,episteme|Varias tramas siguen siendo compatibles.|No cerrar antes de obtener discriminantes.|Core_L(R) de raíces máximas compatibles.|Semillas|No equivale a múltiples verdades actuales.
sector|Sector|sector|estructura|identidad,dinamica|Región donde una identidad admite transformaciones.|Clase conectada por transformaciones admisibles.|Componente por preservación de invariantes.|Territorio|Sector físico exige definición independiente.
imagen|Imagen|image / representation|estructura|autorref,identidad|Algo se presenta en referencia a otra cosa.|Reflejo o representación no necesariamente visual.|I(x), representación formal situada.|Reflejo|Imagen puede ser mental, matemática o visual.
invariante|Invariante|invariant|matematica|identidad,episteme|Algo permanece al transformarse.|Criterio posible de identidad.|f(Tx)=f(x).|Ancla|Invariante no selecciona dinámica por sí solo.
normalizacion|Normalización|normalization|matematica|escala,cierre|Una estructura puede tratarse como una unidad.|Conserva información pertinente bajo contrato.|Norm(J) con preservación de semántica declarada.|Regla / uno|Normalizar no borra procedencia ni certifica costo bajo.
complemento|Complemento|complement|matematica|diferencia,cierre|Lo que queda del universo declarado.|Relativo al universo y operación elegidos.|U\A.|Pieza faltante|Complemento no significa automáticamente solución compatible.
resto|Resto|remainder|matematica|diferencia,escala|Lo que falta o queda luego de operación.|Puede reingresar como relación relevante.|U\A u operación de residuo declarada.|Fragmento|Resto aritmético y residuo relacional no son sinónimos.
escala|Escala|scale|matematica|escala,identidad|Grado de referencia de una magnitud.|Solo luego de declarar comparabilidad.|Factor o unidad a.|Regla|No existe escala física primitiva en ontología.
radio|Radio|radius / relational reach|matematica|escala,trama|Extensión relacional desde una referencia.|Antes de puente físico no presupone longitud métrica.|r_C o radio euclidiano bajo modelo.|Rayo|Radio conceptual no equivale a radio físico.
distancia|Distancia|distance|matematica|diferencia,escala|Cuánto separa referencias bajo una medida.|Requiere criterio y dominio para cuantificar.|d:X×X→ℝ≥0 con axiomas de métrica cuando aplique.|Segmento|Diferencia no siempre es distancia.
longitud|Longitud|length|matematica|escala,episteme|Medida de un enlace o recorrido.|No queda determinada por mera adyacencia.|ℓ_ij, unidades declaradas.|Cinta métrica|Una arista de grafo carece de longitud si no se asigna.
orientacion|Orientación|orientation|matematica|identidad,dinamica|Dirección relativa de una estructura.|Dato distinto de escala y posición.|R∈SO(3) en modelo geométrico.|Brújula|No confundir orientación espacial con significado.
dimension|Dimensión|dimension|matematica|diferencia,escala|Dirección independiente de variación.|No igual a cantidad de nodos o enlaces.|rank G en una realización euclidiana completa.|Eje|Una quinta cápsula no obliga 4D salvo restricciones específicas.
ortogonalidad|Ortogonalidad|orthogonality|matematica|diferencia,episteme|Variaciones independientes según producto interno.|No es noción ontológica primitiva.|⟨u,v⟩=0 bajo estructura declarada.|Ángulo recto|Independencia informativa no siempre es perpendicularidad.
siete_mas_uno|Siete más uno|seven plus one|matematica|escala,cierre|Una totalidad se recompone desde siete y complemento.|La lectura depende del tipo de unidad y reflexión.|7+1=8; identidades aritméticas no prueban unicidad ontológica.|Octágono incompleto|No igualar ocho booleano, octeto físico y octava aritmética.
bit_relacional|Bit relacional|relational bit|matematica|diferencia,escala|Primer contraste binario acreditable.|No prueba que la ontología sea digital.|log₂2=1 en partición binaria.|Interruptor|No toda distinción equivale a bit independiente de Shannon.
trama_metricas|Compatibilidad métrica|metric compatibility|matematica|trama,escala|Las longitudes de un módulo pueden coexistir.|Condiciones geométricas declaradas para representar relaciones.|G=−1/2 JD²J semidefinida positiva, datos completos.|Tetraedro|No toda lista de longitudes es embebible.
configuracion|Configuración|configuration|computacion|trama,diferencia|Una forma posible del sistema.|Admisible no implica efectivamente realizada.|ω∈Ω.|Patrón|No confundir posible con real.
solucion|Solución|solution|computacion|cierre,episteme|Una respuesta satisface la pregunta formulada.|Relativa a regla y contexto; puede cambiar otra consulta.|x∈S_Q.|Llave|Solución única no significa vía única.
respuesta|Respuesta|answer|computacion|cierre,linguistica|Aquello que contesta una pregunta.|Debe venir con discriminantes suficientes.|Q(ω).|Punto final|Responder no implica acreditar.
pregunta|Pregunta|question|epistemologia|episteme,diferencia|Se hace visible qué aún necesitamos distinguir.|Define relevancia del núcleo suficiente.|Consulta Q:Ω→Y.|Signo de interrogación|Cambiar pregunta cambia suficiencia.
discriminante|Discriminante|discriminant|epistemologia|episteme,diferencia|La relación capaz de separar alternativas.|Debe ser necesaria o suficiente bajo contrato claro.|D_q(A,B;C), predicado que separa respuestas.|Prisma|El discriminante no siempre es una palabra única.
determinante|Determinante semántico|semantic determinant|epistemologia|episteme,trama|Relación mínima candidata que explica una distinción.|Puede convertirse en nodo, si conserva trazabilidad.|D*_q; minimizar conjunto de discriminantes con respuesta estable.|Bisagra|No confundir con determinante de una matriz.
evidencia|Evidencia|evidence|epistemologia|episteme,identidad|Lo que sostiene una afirmación.|Distinta de intuición o ilustración.|Dato, prueba o resultado según dominio.|Huella comprobable|Una metáfora nunca basta como evidencia.
justificacion|Justificación|justification|epistemologia|episteme,cierre|Explicar por qué una conclusión se sostiene.|Obliga a nombrar inferencias y límites.|Demostración / argumento / fuente comprobable.|Lupa|Una explicación persuasiva puede ser inválida.
falsador|Falsador|falsifier|epistemologia|episteme,diferencia|Un resultado que pondría en aprietos la afirmación.|Obligación de contrastabilidad para hipótesis.|Condición F cuya observación contradice H.|Prueba adversa|No todo resultado negativo refuta la ontología entera.
hipotesis|Hipótesis|hypothesis|epistemologia|episteme,diferencia|Propuesta que orienta prueba.|No equivale a hallazgo validado.|H bajo condiciones y falsadores.|Borrador|No elevar a teorema por repetición.
teorema|Teorema|theorem|epistemologia|episteme,cierre|Resultado deducido bajo premisas explícitas.|Verdad condicional al sistema formal usado.|Premisas ⊢ T.|Demostración|No acredita por sí mismo un observable físico.
rosi|ROSI / RC-1|ROSI relational evaluator|epistemologia|episteme,trama|Audita rutas, discriminantes y residuos.|Clasificador metodológico, no validador físico.|Estados RESOLVED / OPEN / SUPERPOSED / COLLAPSED.|Lupa de rutas|No convertir puntuaciones de ROSI en prueba ontológica.
economia_minima|Economía mínima|minimum relational economy|epistemologia|episteme,trama|Solo la estructura necesaria, sin perder diferencias relevantes.|Principio de suficiencia, no oráculo de minimización global.|Economía evaluada frente a Q y contrato.|Tejido exacto|Brevedad no significa economía.
suficiencia|Suficiencia|sufficiency|epistemologia|cierre,episteme|La información alcanza para una pregunta.|Siempre relativa a preguntas y futuros admitidos.|P_Z(J), Q, G.|Llave justa|No debe universalizarse una interfaz contextual.
acreditacion|Acreditación|warrant / verification|epistemologia|episteme,cierre|Una solución cuenta como justificada.|Diferente de poseerla o adivinarla.|Certificado o procedimiento aceptado.|Sello de prueba|Determinado no implica acreditado.
representacion|Representación|representation|computacion|linguistica,escala|Forma codificada de una trama.|Su tamaño y acceso importan en cómputo.|Enc(R) con semántica preservada.|Mapa|La forma compacta no asegura elaboración eficiente.
algoritmo|Algoritmo|algorithm|computacion|dinamica,episteme|Regla ejecutable de transformación.|Capa posterior a la ontología.|Procedimiento finito bien especificado.|Engranaje|Una descripción breve no implica ejecución barata.
costo_computo|Costo computacional|computational cost|computacion|episteme,dinamica|Recursos para realizar una operación.|No es el trabajo físico originario.|T(n), espacio S(n), modelo de cálculo.|Reloj discreto|Costo depende de codificación y máquina abstracta.
p_clase|P (clase)|P (complexity class)|computacion|episteme,dinamica|Problemas de decisión resolubles eficientemente en modelo estándar.|Noción de complejidad, no atributo ontológico de la unidad.|Tiempo polinómico determinista.|Ruta corta|No se redefine cambiando una metáfora de unidad.
np_clase|NP (clase)|NP (complexity class)|computacion|episteme,diferencia|Problemas cuyo certificado puede verificarse eficientemente.|No significa necesariamente difícil.|Certificado de longitud polinómica verificable.|Sello verificable|NP no quiere decir no-polinómico.
p_vs_np|P frente a NP|P versus NP|computacion|episteme,diferencia|Pregunta si resolver siempre puede ser tan eficiente como verificar.|Problema abierto; no se infiere del cierre semántico.|¿P=NP? en codificación estándar.|Dos caminos|Pruebas en familias restringidas no deciden igualdad general.
transformacion|Transformación|transformation|dinamica|dinamica,identidad|La trama cambia de estado.|Debe respetar o alterar invariantes declarados.|T:X→X o relación de evolución.|Flecha|Cambio no equivale a movimiento físico.
dinamica|Dinámica|dynamics|dinamica|dinamica,escala|Regla que selecciona continuaciones posibles.|No determinada únicamente por economía.|x_{t+1}=F(x_t) cuando haya regla.|Flujo|Conservar invariantes no selecciona trayectoria.
tiempo|Tiempo|time|dinamica|dinamica,escala|Se comparan órdenes y ritmos de cambios.|No se presume como contenedor primordial.|Orden t o tiempo físico con puente.|Reloj|Actualización no equivale a segundos.
ritmo|Ritmo|rhythm / rate|dinamica|dinamica,escala|Repetición que permite comparar transformaciones.|Un reloj emerge cuando una recurrencia sirve de referencia.|ω según contrato espectral.|Pulso|Frecuencia relacional no es automáticamente Hz.
velocidad|Velocidad|velocity|dinamica|dinamica,escala|Cambio comparado con un ritmo o tiempo.|Exige especificar cantidad y referencia temporal.|v=dx/dt bajo modelo físico.|Flecha larga|Un salto por enlace no determina metros por segundo.
aceleracion|Aceleración|acceleration|dinamica|dinamica,diferencia|Variación de la velocidad.|Su lectura relacional precede a F=ma.|a=dv/dt o segunda diferencia, según contrato.|Flecha curva|Segunda diferencia de amplitud no prueba fuerza física.
modo_a|Modo A|mode A|dinamica|dinamica,autorref|Capacidad de reajuste entre proyecciones.|Separar potencial de respuesta efectiva.|A=V×R en rama propuesta; puente pendiente.|Rotor|No basta su magnitud para fijar orientación futura.
conservacion|Conservación|conservation|dinamica|identidad,escala|La estructura reconoce algo que permanece.|No equivale a inmovilidad.|I(Tx)=I(x) bajo hipótesis.|Ancla cambiante|Conservación informativa no es siempre energía física.
redistribucion|Redistribución|redistribution|dinamica|trama,dinamica|La diferencia cambia dónde se expresa.|No se destruye necesariamente la información.|Mapas de transferencia con invariantes.|Corriente|Mover información no significa preservar toda distinción.
sintonia|Sintonía|attunement|dinamica|trama,dinamica|Las diferencias admisibles se reducen al compararse.|Propuesta para gravedad relacional.|Minimizar D bajo restricciones explícitas.|Diapasón|No toda minimización es ley física.
gravedad|Gravedad relacional (propuesta)|relational gravity proposal|dinamica|dinamica,trama|Una convergencia de relaciones modifica lo distinguible.|Hipótesis física, no resultado derivado universal.|q̇^a=−M^{ab}∂_bD+J^a (candidata).|Órbita|No afirmar recuperación de gravedad observada sin pruebas.
fuerza|Fuerza física|physical force|dinamica|dinamica,episteme|Generador de cambio medible en física.|No debe anteceder a ontología mínima.|F=ma en dominio newtoniano.|Empuje|No equivale a vínculo abstracto.
trabajo_fisico|Trabajo físico|physical work|dinamica|dinamica,escala|Magnitud asociada a fuerza y desplazamiento.|Capa posterior a diferencia y cierre.|W=∫F·dr bajo modelo físico.|Polea|No es sinónimo de costo computacional.
energia|Energía física|physical energy|dinamica|dinamica,escala|Cantidad física de los modelos dinámicos.|No primitiva del núcleo ontológico.|E con unidades y observables.|Reserva|No igualar información con energía por analogía.'''
NODES=[]
for line in RAW.splitlines():
 parts=line.split('|');assert len(parts)==10,(len(parts),line)
 ident,label,en,fam,axes,narr,onto,math,sym,uso=parts
 NODES.append(dict(id=ident,label=label,en=en,family=fam,axes=axes.split(','),narr=narr,onto=onto,formal=math,symbol=sym,current=uso))
assert len({n['id'] for n in NODES})==len(NODES)
# Existing explicit sources: keep documentation filenames, not unsupported source claims.
SOURCE={
'ONTOLOGY':'ONTOLOGY_CANONICAL_V1_0_CANDIDATE_ES.md (27-09-2026)',
'CRYSTAL':'cristal_relacional_v0_1.pdf (29-09-2026)',
'ATLAS':'CRISTAL_SEMANTICO_v0_1.md (16-10-2026)',
'ROSI':'RC1_EVALUATION_STATES.md; paper_1_method_formal_residue.md',
'CONT':'SOURCE_AUDIT_v0_53.md',
'CONCEPT':'CONCEPT_MAP.md',
'INTERFACE':'ONTOLOGY_INTERFACE_AS_CAPSULE_ES.md'}
FAM_DOC={'narrativa':'ATLAS','ontologia':'ONTOLOGY','estructura':'CRYSTAL','matematica':'CONCEPT','dinamica':'CONT','epistemologia':'ROSI','computacion':'CRYSTAL'}
HISTORY={
'palabra':'Del latín parabŏla, y ésta del griego parabolḗ; uso general evolucionado hacia vocablo.',
'concepto':'Del latín conceptus, participio de concipere, concebir.',
'simbolo':'Del griego sýmbolon, señal de reconocimiento.',
'metafora':'Del griego metaphorá, traslado.',
'narrativa':'De narrar, familia del latín narrare.',
'sentido':'Familia de sentir, del latín sentire.',
'significado':'De significar, del latín significare.',
'etimologia':'Del griego étymon (sentido verdadero) y -logía.',
'comprender':'De comprender, del latín comprehendere, abarcar o tomar juntamente.',
'recordar':'Del latín recordari, volver a pasar por el corazón/mente; asociación etimológica habitual.',
'habitar':'Del latín habitare, frecuentativo de habere.',
'casa':'Del latín casa, choza o cabaña.',
'hogar':'Del latín focaris, relacionado con focus, fuego/hogar.',
'intuicion':'Del latín intuitio, contemplación.',
'unidad':'Del latín unitas.',
'autorreferencia':'Compuesto moderno de auto- (griego autós, uno mismo) y referencia.',
'reflexion':'Del latín reflexio, vuelta hacia atrás.',
'cierre_en_si':'Construcción propuesta para el programa: cierre + locución filosófica en sí.',
'cierre_propio':'Locución castellana formada por cierre y propio (latín proprius).',
'cierre_autorreferencial':'Compuesto técnico: cierre + autorreferencial.',
'identidad':'Del latín tardío identitas, mismo.',
'diferencia':'Del latín differentia.',
'referencia':'Del latín referre, volver a llevar o remitir.',
'relacion':'Del latín relatio, relación o relato.',
'comparacion':'Del latín comparatio.',
'indeterminacion':'Con prefijo in- y determinar, de terminus (límite).',
'residuo':'Del latín residuum, lo que queda.',
'resolucion':'Del latín resolutio, deshacer/soltar; sentidos históricos múltiples.',
'novedad':'De nuevo, del latín novus.',
'recursion':'Del latín recurrere, volver a correr.',
'cardinalidad':'De cardinal, del latín cardo, bisagra/eje.',
'trama_comun':'Trama procede del latín trama; metáfora de hilos entretejidos.',
'familia_soluciones':'Familia: latín familia; soluciones: latín solutio.',
'herencia':'Del latín hereditas, transmisión patrimonial.',
'continuidad':'Del latín continuitas.',
'pertenencia':'De pertenecer, del latín pertinere.',
'reconocimiento':'De reconocer, latín recognoscere.',
'capsula':'Del latín capsula, cajita; metáfora técnica en el programa.',
'interior':'Del latín interior, más adentro.',
'frontera':'De frente, latín frons, con evolución romance.',
'interfaz':'Calco técnico del inglés interface; término informático contemporáneo.',
'proyeccion':'Del latín proiectio, acción de lanzar hacia delante.',
'cristal_relacional':'Cristal remite a griego krýstallos vía latín; aquí metáfora formal propuesta.',
'cristal_semantico':'Compuesto técnico propuesto; cristal + semántico (griego sēmantikós).',
'nucleo_suficiente':'Núcleo (latín nucleus) y suficiente (sufficere).',
'raices_latentes':'Raíz (latín radix), latente (latín latens).',
'sector':'Del latín sector, el que corta.',
'imagen':'Del latín imago.',
'invariante':'Formación moderna: prefijo in- + variante.',
'normalizacion':'De norma (latín norma, escuadra/regla).',
'complemento':'Del latín complementum, lo que completa.',
'resto':'De restar; familia latina restare.',
'escala':'Del latín scala, escalera.',
'radio':'Del latín radius, rayo o varilla.',
'distancia':'Del latín distantia, estar separado.',
'longitud':'Del latín longitudo.',
'orientacion':'De oriente, latín oriens, lo que nace o surge.',
'dimension':'Del latín dimensio, medida.',
'ortogonalidad':'Del griego orthós (recto) y gōnía (ángulo).',
'siete_mas_uno':'Expresión aritmética corriente; la lectura relacional pertenece al programa.',
'bit_relacional':'Bit, contracción inglesa de binary digit; relacional precisa el contexto.',
'configuracion':'Del latín configuratio, forma conjunta.',
'solucion':'Del latín solutio.',
'respuesta':'De responder, del latín respondere.',
'pregunta':'De preguntar, familia latina percontari (etimología a contrastar).',
'discriminante':'De discriminar, latín discriminare, separar.',
'determinante':'De determinar, latín determinare; aquí uso relacional, no matricial.',
'evidencia':'Del latín evidentia, claridad patente.',
'justificacion':'De justificar, latín iustificare.',
'falsador':'Formación moderna desde falso, latín falsus.',
'hipotesis':'Del griego hypóthesis, supuesto.',
'teorema':'Del griego theṓrēma, objeto de contemplación.',
'rosi':'Sigla técnica del sistema de evaluación del programa.',
'economia_minima':'Economía: griego oikonomía, administración de la casa; metáfora de suficiencia.',
'suficiencia':'Del latín sufficientia.',
'acreditacion':'De acreditar, crédito desde latín creditum.',
'representacion':'Del latín repraesentatio.',
'algoritmo':'Nombre derivado históricamente del matemático al-Juarismi (al-Khwārizmī).',
'costo_computo':'Costo del comercio; cómputo del latín computare.',
'p_clase':'Letra P: denominación formal de complejidad polinómica.',
'np_clase':'NP: sigla de nondeterministic polynomial time.',
'p_vs_np':'Composición de las denominaciones técnicas P y NP.',
'transformacion':'Del latín transformare, cambiar de forma.',
'dinamica':'Del griego dynamikós, fuerza/capacidad.',
'tiempo':'Del latín tempus.',
'ritmo':'Del griego rhythmós.',
'velocidad':'Del latín velocitas.',
'aceleracion':'Del latín acceleratio.',
'modo_a':'Nombre técnico propuesto para esta rama del programa.',
'conservacion':'Del latín conservatio.',
'redistribucion':'Compuesto: re- + distribución, familia latina distribuere.',
'sintonia':'De sintonizar, griego sýn (junto) + tónos (tono/tensión).',
'gravedad':'Del latín gravitas, peso o gravedad.',
'fuerza':'Del latín fortia, fortaleza.',
'trabajo_fisico':'Trabajo (etimología tradicional relacionada con tripalium, discutida en detalle); aquí físico.',
'energia':'Del griego enérgeia, actividad o acto.'}
UNCERTAIN={'pregunta','trabajo_fisico','recordar'}
for n in NODES:
 n['history']=HISTORY.get(n['id'],'Origen léxico específico pendiente de verificación documental; acepción técnica contextualizada.')
 n['history_status']='APROXIMACIÓN — VERIFICAR' if n['id'] in UNCERTAIN or n['id'] not in HISTORY else 'SÍNTESIS ETIMOLÓGICA — VERIFICAR FUENTE'
 n['source']=SOURCE[FAM_DOC[n['family']]]
 n['primary']=n['axes'][0]; n['epistemic']='PROPUESTA LÉXICA';
 if n['family'] in ('ontologia','estructura'):n['epistemic']='CONVENCIÓN ONTOLÓGICA / FORMAL SEGÚN CONTRATO'
 if n['family'] in ('dinamica',):n['epistemic']='MODELO / HIPÓTESIS FÍSICA SI APLICA'
 if n['id'] in ('cristal_relacional','nucleo_suficiente','trama_metricas','complemento','cardinalidad'):n['epistemic']='DEFINICIÓN FORMAL BAJO CONTRATO'
 if n['id'] in ('p_vs_np','p_clase','np_clase'):n['epistemic']='DEFINICIÓN ESTÁNDAR / PROBLEMA ABIERTO'
# Discriminant cards: question-relative candidate; these are hypernode identities, not global synonym labels.
# fields A|B|determinante|pregunta|diferencia A/B|alcance|falsador|estado
PAIRS='''casa|hogar|Pertenencia relacional|¿Cuándo un lugar se reconoce como hogar?|La casa puede ser edificio sin continuidad reconocida; el hogar puede ser comunidad sin casa física.|Bajo la acepción de hogar como trama de pertenencia.|Un caso de hogar sin criterio de pertenencia bajo esta definición exigiría revisarla.|CANDIDATO
recordar|comprender|Integración operativa|¿Cuándo recuperar una idea se convierte en entenderla?|Recordar la recupera; entenderla permite usarla y relacionarla con nuevas preguntas.|Comprensión operacional, no teoría general de conciencia.|Si una tarea nueva puede resolverse sin integración observable, la prueba propuesta no discrimina.|CANDIDATO
cierre_propio|cierre_en_si|Autorreferencia suficiente|¿Qué hace explícito «en sí»?|Propio evoca pertenencia; en sí exige reconocimiento desde relaciones suficientes.|Convención léxica del programa.|Que la expresión «propio» implique siempre autorreferencia fuerte invalidaría esta divergencia.|INTERPRETACIÓN
reflexion|cierre_en_si|Consistencia de cierre|¿Por qué reflexionar no basta para cerrar?|Una reflexión puede volver sobre sí sin sostener una unidad consistente.|Dada regla de consistencia.|Contraejemplo a la supuesta consistencia o autorreferencia.|DERIVABLE
herencia|trama_comun|Copresencia estructural|¿Cuándo «herencia» sugiere demasiado tiempo?|Herencia apunta a transmisión; trama indica relaciones sostenidas simultáneamente.|Usos presentes vs transmisión genealogía.|Si la tarea exige procedencia temporal, trama sola deja información fuera.|CANDIDATO
familia_soluciones|trama_comun|Tipo de comunidad|¿Qué comparten familia y trama?|Familia es clase de realizaciones; trama es organización de relaciones.|Una misma trama puede admitir múltiples familias.|Una relación uno-a-uno universal requeriría pruebas que no tenemos.|INTERPRETACIÓN
unidad|identidad|Persistencia reconocible|¿Qué convierte el uno en identidad?|Unidad reconoce entidad, identidad exige criterio bajo cambio.|Transformaciones declaradas.|Una unidad sin invariantes bajo los cambios relevantes rompe identidad persistente.|DERIVABLE
novedad|cierre_en_si|Dependencia acreditada|¿Cuándo nueva diferencia pasa a cierre?|Novedad añade discriminación; cierre puede resultar de relaciones ya sustentadas.|Modelo específico de clausura.|Si el dato novedoso fuera automáticamente cierre siempre, el criterio no distingue.|DERIVABLE
relacion|comparacion|Pregunta operativa|¿Qué hace una comparación respecto de una relación?|Relación conecta; comparación pide una respuesta concreta a partir de ella.|Una relación puede no haber sido consultada.|Respuesta sin pregunta definida invalida su acreditación.|INTERPRETACIÓN
diferencia|distancia|Medición declarada|¿Cuándo una diferencia se vuelve distancia?|Diferencia precede a escala; distancia requiere regla métrica.|Dominio con función de distancia.|Diferencias no metrizadas prueban la no equivalencia.|DERIVABLE
distancia|longitud|Objeto medido|¿Cuándo distancia entre puntos es longitud de vínculo?|La distancia mide separación; longitud se aplica a un enlace o recorrido definido.|Geometría etiquetada.|Enlaces abstractos sin medida distinguen ambos.|INTERPRETACIÓN
proyeccion|interfaz|Suficiencia de consulta|¿Cuándo una proyección sirve como interfaz?|Una proyección puede perder información; una interfaz suficiente preserva respuestas permitidas.|Q y futuros G declarados.|Encontrar Q donde la proyección responde distinto.|DERIVABLE
normalizacion|resolucion|Semántica preservada|¿Una normalización resuelve automáticamente?|Normalizar expresa forma; resolver cambia qué preguntas quedan abiertas.|Se exige preservación del contenido exterior declarado.|Una forma normal que cambia respuestas no es normalización fiel.|DERIVABLE
complemento|resto|Universo de referencia|¿Por qué la parte que falta no es cualquier residuo?|Complemento es U\\A; resto puede referir otra operación.|Con universo U fijado.|Cambiar U cambia complemento aunque la palabra resto permanezca.|DERIVABLE
indeterminacion|residuo|Relevancia de la pregunta|¿Qué queda pendiente?|Indeterminación son alternativas abiertas; residuo es aquello que la consulta necesita distinguir.|Pregunta Q explícita.|Alternativa abierta irrelevante para Q no constituye residuo pertinente.|DERIVABLE
pregunta|discriminante|Testigo separador|¿Qué información decide entre alternativas?|Pregunta fija el objetivo; discriminante separa respuestas diferentes.|Relativo a Q y C.|Un supuesto testigo que no cambia respuesta no discrimina.|DERIVABLE
hipotesis|teorema|Prueba deductiva|¿Cuándo una hipótesis alcanza estado de teorema?|Hipótesis propone; teorema se deduce bajo premisas explícitas.|Marco formal y prueba revisable.|Un paso inválido de inferencia cancela el estatus de teorema.|DERIVABLE
evidencia|metafora|Prueba independiente|¿Qué permite justificar y qué solo ilustrar?|Evidencia contrasta; metáfora orienta.|Dominio de afirmación declarado.|Una analogía atractiva sin observables no constituye prueba.|DERIVABLE
costo_computo|trabajo_fisico|Magnitud y unidades|¿Por qué «trabajo» no es el costo computacional?|Costo cuenta recursos del algoritmo; trabajo físico integra fuerza y desplazamiento.|Modelos de cómputo vs leyes físicas.|Una equivalencia exigiría puente físico explícito.|DERIVABLE
p_clase|np_clase|Tipo de verificación|¿Qué distingue las clases P y NP?|En P se decide en tiempo polinómico; en NP hay certificado polinómico verificable.|Complejidad estándar; P⊆NP.|No sabemos si se separan estrictamente.|FORMAL
siete_mas_uno|normalizacion|Unidad de referencia|¿Qué convierte una cuenta en normalización estructural?|7+1=8 es igualdad aritmética; normalización requiere contrato que preserve información.|No igualar distintos «ochos».|Otro objeto con mismo cardinal demuestra que el número no basta.|INTERPRETACIÓN
rosi|determinante|Discriminante auditado|¿Qué aporta ROSI al determinante?|ROSI exige pregunta, raíces, residuo y falsador; no impone una sola palabra.|Protocolo de auditoría, no verdad semántica automática.|Cierre sin nombrar discriminante es COLLAPSED.|DERIVABLE
autorreferencia|cierre_autorreferencial|Consistencia comprobable|¿Basta con referirse a uno mismo?|Autorreferencia puede paradojar; cierre requiere consistencia bajo criterio.|Dominio y reglas declaradas.|Ejemplo de paradoja autorreferente.|DERIVABLE
imagen|representacion|Medio de codificación|¿Todo lo representado es imagen?|Imagen evoca percepción o reflexión; representación es más general.|Uso ontológico y matemático separado.|Una codificación sin forma visual rompe sinonimia.|INTERPRETACIÓN
conservacion|redistribucion|Lugar de la información|¿Puede conservarse algo aunque cambie de soporte?|Conservar es preservar invariante; redistribuir cambia dónde reside.|Invariante declarado.|Si todas las distinciones relevantes se pierden, no hay conservación.|DERIVABLE
sintonia|gravedad|Puente observable|¿La sintonía ya demuestra gravedad?|Sintonía es mecanismo propuesto; gravedad física requiere predicción contrastable.|Puente campo dinámico- observable.|Falta de predicción independiente mantiene hipótesis.|OPEN
velocidad|aceleracion|Cambio del cambio|¿Cómo se distingue la aceleración de velocidad?|Velocidad compara variación de posición; aceleración compara variación de velocidad.|Tiempo/ritmo cuantificados.|Sin magnitudes y referencia no hay valor físico.|DERIVABLE
cierre_en_si|cristal_relacional|Contrato y contenido persistente|¿Cómo se realiza el cierre narrativo en un cristal formal?|Cierre es condición de reconocimiento; cristal es relación conjunta de compatibilidad.|Preguntas Q y futuros G declarados.|Un contexto futuro que distingue dos supuestos equivalentes.|DERIVABLE
cristal_semantico|cristal_relacional|Nivel de formalización|¿Es lo mismo el atlas que el cristal formal?|Uno organiza términos y asociaciones; otro formaliza compatibilidades de configuraciones.|Herramienta editorial versus objeto formal.|Que el atlas visual sea interpretable no prueba el objeto formal.|DERIVABLE
informacion|dato|Interpretación de diferencia|¿Cuándo un dato constituye información?|Dato codificado no implica distinción pertinente para una pregunta.|Depende del contrato Q.|Dato que cambia código pero no respuesta.|OPEN'''
# Last pair will be added as node definitions below.
for ident,label,en,fam,axes,narr,onto,form,sym,uso,hist in [
 ('informacion','Información','information','ontologia',['diferencia','trama'],'Diferencia pertinente sostenida por relaciones.','No implica magnitud física de Shannon sin contrato.','Conjunto de distinciones que cambia Q.','Marca','Información no equivale a datos ni energía.','Del latín informatio, dar forma.'),
 ('dato','Dato','datum / data','epistemologia',['episteme','linguistica'],'Registro o valor recibido.','No siempre es una diferencia relevante.','d∈D bajo codificación.','Ficha','Acumular datos no garantiza información pertinente.','Del latín datum, lo dado.')]:
 NODES.append(dict(id=ident,label=label,en=en,family=fam,axes=axes,narr=narr,onto=onto,formal=form,symbol=sym,current=uso,history=hist,history_status='SÍNTESIS ETIMOLÓGICA — VERIFICAR FUENTE',source=SOURCE['ONTOLOGY' if fam=='ontologia' else 'ROSI'],primary=axes[0],epistemic='CONVENCIÓN ONTOLÓGICA / FORMAL SEGÚN CONTRATO'))
IDS={x['id'] for x in NODES}; PAIR_DATA=[]
for line in PAIRS.splitlines():
 p=line.split('|');assert len(p)==8,(p,len(p))
 a,b,det,q,contrast,scope,falsifier,status=p
 assert a in IDS and b in IDS,(a,b)
 det_id='d'+str(len(PAIR_DATA)+1).zfill(2)
 PAIR_DATA.append(dict(id=det_id,a=a,b=b,label=det,question=q,contrast=contrast,scope=scope,falsifier=falsifier,status=status,source=SOURCE['ROSI']))
# additional scaffold links: relation labels are typed and only claim editorial similarities
LINKS=[]
def link(a,b,kind='implica_en_modelo',why='Relación propuesta en la secuencia del programa'):
 assert a in IDS and b in IDS,(a,b);LINKS.append(dict(a=a,b=b,type=kind,why=why))
CHAINS=[
['narrativa','reflexion','diferencia','indeterminacion','relacion','comparacion','resolucion','recursion','cardinalidad','cierre_en_si','identidad','sector'],
['palabra','concepto','significado','sentido','comprender','cristal_semantico'],
['casa','habitar','pertenencia','hogar'],
['capsula','interior','frontera','interfaz','proyeccion','nucleo_suficiente','cristal_relacional'],
['imagen','reflexion','autorreferencia','cierre_autorreferencial','cierre_en_si'],
['diferencia','radio','distancia','longitud','trama_metricas'],
['solucion','acreditacion','respuesta'],
['pregunta','discriminante','determinante','rosi'],
['transformacion','dinamica','ritmo','tiempo','velocidad','aceleracion'],
['conservacion','redistribucion','sintonia','gravedad'],
['representacion','algoritmo','costo_computo','p_clase','np_clase','p_vs_np'],
['trama_comun','familia_soluciones','raices_latentes','novedad','residuo'],
['escala','normalizacion','complemento','siete_mas_uno']]
for chain in CHAINS:
 for a,b in zip(chain,chain[1:]):
  link(a,b,'ruta_conceptual','Vecindad de una lectura; no es implicación lógica ni equivalencia.')
extra=[('cierre_en_si','trama_comun'),('cierre_en_si','cristal_relacional'),('comparacion','pregunta'),('pregunta','suficiencia'),('suficiencia','interfaz'),('suficiencia','acreditacion'),('unidad','normalizacion'),('unidad','cierre_en_si'),('cierre_en_si','invariante'),('nucleo_suficiente','determinante'),('rosi','falsador'),('rosi','episteme') if False else ('rosi','hipotesis'),('continuidad','conservacion'),('continuidad','trama_comun'),('raices_latentes','discriminante'),('residuo','discriminante'),('siete_mas_uno','complemento'),('cierre_en_si','novedad'),('reflexion','normalizacion'),('herencia','trama_comun'),('cardinalidad','bit_relacional'),('palabra','etimologia'),('palabra','uso_actual'),('palabra','simbolo'),('simbolo','metafora'),('concepto','evidencia'),('teorema','justificacion'),('cristal_semantico','determinante'),('narrativa','ontologia') if False else ('narrativa','unidad'),('representacion','proyeccion'),('representacion','cristal_relacional'),('trabajo_fisico','fuerza'),('fuerza','energia'),('trabajo_fisico','costo_computo'),('modo_a','aceleracion'),('modo_a','sintonia'),('interfaz','herencia'),('diferencia','informacion'),('informacion','dato'),('pregunta','respuesta'),('respuesta','resolucion'),('identidad','invariante'),('imagen','simbolo')]
for a,b in extra:link(a,b,'converge_o_contrasta','Ver determinante y contrato antes de tratar como equivalencia.')
# No invented ROSI scores; present only labelled candidate contrasts.
DATA=dict(title='Cristal semántico integral del Programa de Geometría Relacional',version='1.0 · atlas extensible',date='2026-10-16',author='Le Matt Ansatz Di Ego (autoría del programa); atlas elaborado con asistencia de ChatGPT',axes={k:{'color':v[0],'label':v[1],'image':v[2]} for k,v in AXES.items()},families=FAMS,nodes=NODES,links=LINKS,discriminants=PAIR_DATA,sources=SOURCE,epistemology={'no_equivalence':'Un vínculo no es sinónimo ni implicación salvo demostración','no_metric':'Los valores de orientación de facetas son marcadores editoriales, no distancias semánticas validadas','rosi':'Reglas del protocolo aplicadas manualmente; evaluador/plugin ROS-1 no ejecutado','coverage':'Corpus recuperable al 16-10-2026; no exhaustivo de todo el historial ni de todos los idiomas','history':'Las notas etimológicas son pistas de investigación; verificar con diccionarios y corpus antes de publicarlas como hechos documentados.'})
(BASE/'CRISTAL_DATOS.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2),encoding='utf-8')
with (BASE/'TERMINOS.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['id','label','en','family','axes','narr','onto','formal','symbol','current','history','history_status','source','epistemic']);w.writeheader()
 for node in NODES:w.writerow({k:','.join(v) if isinstance(v,list) else v for k,v in node.items() if k in w.fieldnames})
with (BASE/'DETERMINANTES.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(PAIR_DATA[0]));w.writeheader();w.writerows(PAIR_DATA)
print('CREATED',len(NODES),'terms',len(PAIR_DATA),'discriminants',len(LINKS),'relations')
