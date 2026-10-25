# O70 — La caja de espejos como calculadora de comunes y el residuo dinámico de la semilla

**Programa de Geometría Relacional** · **Le Matt Ansatz Di Ego** · **21 octubre 2026**  
**Estado:** suplemento aditivo; identidades exactas de simetría y un laboratorio numérico Fourier–Galerkin. **No es una solución de regularidad de Navier–Stokes 3D**.

## 0. Del relato a la prueba

**[O]** La caja de espejos permite que las relaciones de una configuración se proyecten y comparen. Una coincidencia puede constituir una referencia común, pero las relaciones no habitadas por una proyección pueden participar en la configuración completa. La semilla no exige una copia material idéntica ni que los participantes sean las mismas partículas: exige información que haga posible reconstruir la continuidad de la relación. El múltiplo que normalizó una configuración es su referente aritmético transportable; no lo identificamos de antemano con un número de espejos o una magnitud física.

**[N]** En O68 la sincronía de dos giros admitía una descomposición por Bézout, pero O69 mostró que dos trazadores materiales del anillo no permanecen bloqueados a un par entero constante. Para evaluar una referencia **colectiva** en lugar de dos trazadores, consideramos el conjunto de los reflejos de **todo el campo de velocidad**. La pregunta ya no es «¿qué dos partículas coinciden?», sino «¿qué parte de todo el campo permanece común a las operaciones de la caja?», y luego «¿basta esa parte para computar su continuación?».

**Advertencia de correspondencia:** los ocho operadores elegidos son las simetrías *discretas* del cuadrado transversal (grupo D₄) actuando sobre un campo vectorial en una caja periódica, **no** el grupo óptico de imágenes infinitas de las paredes enfrentadas de O59. Este laboratorio sirve de puente formal; no demuestra equivalencia entre ambos montajes.

## 1. La operación de los ocho espejos

Sea \(G=D_4\), generado por rotaciones de \(90^\circ\) alrededor del eje del anillo y una reflexión en un plano que contiene dicho eje. Para \(g\in G\), su acción física sobre un campo vectorial es:

\[
(g\cdot u)(x)=g\,u(g^{-1}x).
\]

La **referencia común calculada por la caja** es la media de grupo:

\[
\boxed{\mathcal P_Gu=\overline u=\frac1{|G|}\sum_{g\in G}g\cdot u,\qquad |G|=8.} \tag{70.1}
\]

**[T]** Si el grupo actúa ortogonalmente sobre el espacio de campos con el producto escalar L², entonces \(\mathcal P_G\) es una proyección ortogonal: \(\mathcal P_G^2=\mathcal P_G\), su imagen es el espacio de campos invariantes bajo el grupo, y \(u=u_\mathrm{común}+u_\mathrm{diferencia}\), con \(u_\mathrm{común}=\mathcal P_Gu\), \(\mathcal P_Gu_\mathrm{diferencia}=0\). Las partes son ortogonales en el producto interno escogido. No se afirma que ambas sean fuerzas o sustancias independientes.

El **ocho** es la cardinalidad de nuestras operaciones seleccionadas, **no** el múltiplo ontológico de O40/O68. Un reflejo no conserva los componentes vectoriales sin transformarlos: hay que aplicar simultáneamente el cambio de coordenadas y la transformación vectorial (70.1).

## 2. La ecuación exacta que la caja computa

Consideremos Navier–Stokes incompresible sin fuerza externa en un dominio periódico compatible con \(G\), con \(\nu>0\):

\[
\partial_t u+\nabla\cdot(u\otimes u)+\nabla p=\nu\Delta u,\quad \nabla\cdot u=0.
\]

El operador \(\mathcal P_G\) conmuta con derivadas y con la proyección de Leray \(\mathbb P\) **en el sentido de la acción geométrica sobre vectores y tensores**. La referencia común obedece exactamente:

\[
\boxed{\partial_t\bar u=F(\bar u)-\mathbb P\nabla\cdot\tau,}\tag{70.2}
\]

\[
F(v)=-\mathbb P\nabla\cdot(v\otimes v)+\nu\Delta v,
\quad
\boxed{\tau=\mathcal P_G^{(2)}(u\otimes u)-\bar u\otimes\bar u.}\tag{70.3}
\]

Aquí \(\mathcal P_G^{(2)}\) promedia tensores con la acción \(gT(g^{-1}x)g^{T}\). La tensión de relaciones \(\tau\) es el residuo exacto de haber promediado antes de calcular las interacciones cuadráticas. En este laboratorio \(\tau\) es un tensor de covarianza por órbitas del grupo, **no** una nueva tensión superficial ni una nueva ley fundamental. La identidad se deriva aplicando el promedio de grupo a las ecuaciones y sumando y restando \(\nabla\cdot(\bar u\otimes\bar u)\).

Si \(\mathcal P_Gu=u\) inicialmente, el campo es exactamente simétrico; mientras existe y es única la solución suave, la equivariancia conserva esa simetría y \(\tau=0\). Pero si sólo conocemos \(\bar u\), en general \(\tau\) no está determinada por ese dato, y (70.2) **no es una ecuación autónoma cerrada**.

**[T, obstrucción a la computación autónoma]** Existen dos campos incompresibles suaves con la **misma** proyección \(\bar u(0)\) y distintas derivadas \(\partial_t\bar u(0)\) bajo Navier–Stokes. En consecuencia, ningún algoritmo que reciba exclusivamente \(\bar u(0)\) puede determinar ambas evoluciones proyectadas por una misma ley determinista autónoma. A continuación construimos un testigo numérico reproducible en un sistema finito, y la identidad (70.2) justifica su mecanismo en el continuo.

## 3. La familia adversarial de tres anillos

**[E]** Recuperamos los operadores y la condición inicial del anillo O53–O69, Fourier–Galerkin periódico en \([-\pi,\pi)^3\), núcleos de \(R=1\), \(a=.35\), circulación nominal \(\Gamma=6\), \(\nu=.025\), mallas de \(32^3\) y \(40^3\). Sea \(u_0\) el anillo de referencia sin perturbación; sea \(u_{14}\) el preparado con perturbación relativa 14 %. Definimos, *sin ajustar fases a posteriori*,

\[
 v=u_{14}-\mathcal P_Gu_{14},\quad \mathcal P_Gv=0,\quad
 \boxed{u_c(0)=u_0+c v,\quad c\in\{0,1,2\}.}\tag{70.4}
\]

Por construcción, \(\mathcal P_Gu_c(0)=u_0\) para los tres campos: la caja entrega la **misma** referencia. No estamos asegurando que el campo total sea idéntico o tenga igual energía; de hecho, no lo es. La medición de normas se utiliza solamente como test observable, no como fundamento ontológico.

Como \(u_0\) es invariante y \(v\) está en el núcleo de la proyección, los términos cruzados lineales en \(v\) desaparecen al proyectar. La diferencia inicial entre la evolución colectiva de \(u_c\) y la de \(u_0\) es exactamente **cuadrática** en \(c\):

\[
\boxed{\mathcal P_GF(u_0+c v)-F(u_0)= -c^2\,\mathbb P\nabla\cdot\mathcal P_G^{(2)}(v\otimes v).}\tag{70.5}
\]

Esto se deduce del carácter cuadrático de la no linealidad y de la equivariancia de su derivada lineal en torno a \(u_0\). **No** procede de sincronizar artificialmente las frecuencias y no es una ley de cuantización. La ecuación (70.5) es exacta en el sistema Galerkin discretizado; tiene el análogo formal exacto para soluciones suficientemente suaves del continuo periódico.

### Valores observados

| Magnitud, unidades adimensionales | N=32 | N=40 |
|---|---:|---:|
| RMS del sector omitido \(\|v\|\) | 0.04455806 | 0.04458251 |
| Defecto inicial \(c=0\) | \(<10^{-14}\) | \(<10^{-14}\) |
| Defecto inicial \(c=1\) | 0.01398969 | 0.01466583 |
| Defecto inicial \(c=2\) | 0.05595876 | 0.05866331 |
| Distancia entre referencias evolucionadas a \(t=0.032\), \(c=1\) | 0.00042216 | 0.00043980 |
| Distancia entre referencias evolucionadas a \(t=0.032\), \(c=2\) | 0.00168984 | 0.00176090 |

El *defecto inicial* se calcula como la norma RMS de \(\mathcal P_GF(u)-F(\mathcal P_Gu)\). La distancia final compara cada proyección evolucionada con la evolución **del campo base a igual tiempo**. El factor 4 es exacto en el tiempo inicial dentro del error numérico; en tiempos positivos hay correcciones dinámicas.

**[E]** El residuo de verificar la identidad de tensión (70.2) numéricamente es \(4.58\times10^{-16}\) para N=32 y \(6.10\times10^{-16}\) para N=40, error de cálculo de punto flotante. La equivariancia del operador Galerkin frente a los ocho operadores se confirmó hasta ~\(6\times10^{-16}\). Las trayectorias se integraron con RK4, \(\Delta t=.004\), horizonte \(T=.032\). Este es un ensayo *corto* sobre dos mallas, no certificación de convergencia del PDE.

## 4. Interpretación de la semilla y «apagar los espejos»

**[O/H]** El común es una relación reconstruible por la caja. La diferencia omitida no está necesariamente ausente del sistema: puede influir en la evolución del común, y su primer aporte aparece como \(\tau\). Al «apagar» la operación de reflexión, el flujo continúa según su dinámica interna. La referencia puede persistir cuando el sistema pertenece al subespacio simétrico, pero una configuración no simétrica puede tener proyección simétrica sin que esa proyección determine por sí sola su futuro.

**No confundamos:**

1. Apagar la **operación de comparar** reflejos con retirar **paredes físicas** o cambiar el contorno de un fluido.
2. La unidad de normalización del programa con el divisor \(8\) del promedio de grupo.
3. La falta de información en una proyección con ausencia física de movimiento en las partes descartadas.
4. Reconstruir una referencia con **resolver** la regularidad general 3D de Navier–Stokes.

Si se conserva todo el campo original (o la lista completa de sus imágenes etiquetadas, que incluye la identidad), se puede evolucionar con un solucionador de Navier–Stokes, pero se pierde la compresión que pretendía proporcionar una semilla pequeña. Si sólo se conserva \(\bar u\), la dinámica no cierra. Agregar \(\tau\) mejora el conocimiento de la derivada instantánea, pero su propia evolución puede depender de correlaciones de orden superior: **la caja no ha demostrado todavía un cierre finito exacto para datos generales**.

## 5. Conexión con los radios y frecuencias

La caja selecciona relaciones espaciales entre partes transformadas de un campo. Su proyección no identifica por sí misma los radios \(R,r\), ni los dos ritmos de O68–O69; cualquier identificación adicional debe declarar qué funcional del campo mide radio, fase y coincidencia. O69 rechazó una razón entera constante de dos trazadores. O70 demuestra que, incluso si existe una referencia colectiva, **la proyección común puede perder información dinámica de segundo orden**. Para modelar «semilla y múltiplo» hace falta registrar una relación que sea suficiente para la transición, no solamente un número que coincida en cada instantánea.

### Candidato para la próxima prueba — no teorema

Investigar si el dato ampliado \((\bar u,\tau)\), expresado en variables adimensionales de dos radios y ritmos, permite cerrar una subfamilia de vórtices con un conjunto finito de parámetros y predice su dirección y modificación de escala. La prueba adversarial será producir dos campos con los mismos parámetros ampliados pero distinta derivada de esos parámetros. Si falla, subir a una nueva relación o demostrar la necesidad de memoria temporal; no elegir retrospectivamente un múltiplo para rescatar cada caso.

Para el problema general de Navier–Stokes, incluso un cierre colectivo predictivo no bastaría: habría que derivar además una cota *a priori* que excluya concentración de gradientes, para todos los datos suaves admisibles. **O70 no la obtiene**.

## 6. Procedencia, verificación y límites

- Fuentes matemáticas del experimento: código O53/O62/O63 reutilizado de O69 sin cambiar las ecuaciones de evolución; observables y proyección añadidos en `codigo/experimento_o70.py` y `codigo/verificar_cierre_o70.py`.
- Sistema: periódico, sin forzamiento, discretización Fourier–Galerkin dealias 2/3, RK4; N32 y N40; ventana T=.032; viscosidad .025.
- Controles: 14 aserciones sobre proyectividad, equivariancia, identidad dinámica, cuadraticidad, igualdad de referencia inicial y divergencia posterior, más dos comprobaciones independientes de identidad con tensor de segundo orden. Los 16 controles pasaron: los 14 del simulador y los dos residuos tensoriales fueron menores de 10⁻¹⁵. **Las 16 pruebas no son 16 teoremas físicos.**
- Reproducibilidad: Python con `numpy`, `scipy` y para gráficos `matplotlib`; instrucciones en `LEER_PRIMERO.md`.
- Dependencia: formalización física sobre Navier–Stokes incompresible sin forzamiento; no equivale al laboratorio óptico original O59 ni a la identidad aritmética O40/O68.

**Conclusión:** la caja **sí computa un común exacto** y revela una condición física que cualquier candidato a semilla dinámica debe satisfacer: si elimina información que participa en el término no lineal, no puede determinar la evolución futura del común. La relación que continúa exige un normalizador que preserve la información dinámica necesaria, o un mecanismo adicional de cierre que demuestre cuándo esa información omitida se cancela.
