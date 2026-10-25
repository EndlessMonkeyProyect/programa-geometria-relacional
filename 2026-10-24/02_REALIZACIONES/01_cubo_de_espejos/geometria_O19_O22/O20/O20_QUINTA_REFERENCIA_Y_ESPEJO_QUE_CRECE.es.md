# O20 — Quinta referencia, reflexiones de caras y escala radial

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 19 de octubre de 2026**  
**Continuidad:** O19 (cubo por planos centrales), G-R3/O8–O14 (foco, reflexión, interfaces), O16 (interpretación de contención).  
**Estatus:** [O] propuesta ontológica; [T] teorema euclídeo bajo regularidad; [V] 18 pruebas exactas; [A] problema abierto. Este suplemento no reemplaza la Imagen Total.

## 1. Narrativa

La unidad mínima tetraédrica establece una configuración cerrada de cuatro referencias. La reflexión por una de sus caras produce una quinta referencia y con ella una nueva unidad local congruente. Esa continuación admite cuatro direcciones alternativas, una por cara de la unidad de origen. La realización de las cuatro direcciones conjuntamente reconstruye otra unidad global de cuatro puntos con el mismo centro; el nuevo conjunto está a una distancia radial mayor.

La distinción ontológica propuesta es **cierre de una forma / cierre de una regla de continuación**: una regla finita puede describir infinitas etapas de generación, mientras cada etapa deja abiertas nuevas interfaces. Esto expresa repetibilidad de la construcción, no resolución automática de toda incertidumbre.

## 2. Contrato geométrico [D]

Se adopta como realización auxiliar un tetraedro euclídeo regular centrado en `O=0` con radio circunscrito `R>0`, vértices `v_0,...,v_3` y producto escalar `v_i·v_j=-R²/3` para `i≠j`; todos tienen norma `R`. Su lado tiene cuadrado `a²=8R²/3`.

La cara opuesta a `v_i` está en el plano `v_i·x=-R²/3`. Se define el espejo **de cara** que refleja el vértice opuesto a través de ese plano. Esta operación difiere de los tres espejos **centrales** de O19, que fijan el origen y producen el tetraedro complementario del cubo.

## 3. Teorema O20-T1: la quinta referencia [T]

La reflexión de `v_i` en su cara opuesta produce

\[
\boxed{w_i=-\frac53v_i},\qquad \boxed{\|w_i\|=\frac53R}.
\]

Prueba: con normal `v_i`, la reflexión en el plano `v_i·x=-R²/3` transforma

\[
v_i\longmapsto v_i-2\frac{R²+R²/3}{R²}v_i=-\frac53v_i.
\]

Los tres vértices de la cara permanecen en su sitio. El tetraedro adyacente formado por ellos y `w_i` es congruente al original: mantiene lado `a` y radio **local** `R` respecto de su propio centro. El centro local se desplaza a

\[
\boxed{O_i'=-\frac23v_i}.
\]

La distancia del nuevo vértice al centro **original** es `5R/3`, mientras la distancia al centro **local** nuevo es `R`. La quinta referencia desarrolla así, bajo este contrato geométrico, la distinción radio local / radio respecto de un foco global.

Las cinco referencias constituyen una **bipirámide triangular** (dos tetraedros que comparten una cara). Un prisma triangular usual requiere seis vértices. Si se quiere llamar «prisma» a una cápsula relacional, ese uso debe especificarse como lenguaje y no como equivalencia geométrica.

## 4. Teorema O20-T2: cuatro continuaciones reconstruyen un foco común [T]

Aplicar cada una de las cuatro reflexiones de cara, tomando de cada una su quinta referencia, produce

\[
T_1=\{w_0,w_1,w_2,w_3\}=-\frac53T_0.
\]

El conjunto `T_1` es otro tetraedro regular, de radio `5R/3`, orientación invertida y centro

\[
\boxed{\frac14\sum_{i=0}^{3}w_i=0=O}.
\]

**Lectura:** una continuación aislada desplaza su centro local; las cuatro continuaciones completas conservan el centro global y admiten una referencia de nueva escala. La simetría de las cuatro ramas, no una quinta referencia por sí sola, restablece el foco global.

## 5. Teorema O20-T3: repetición y radio que crece [T]

La misma regla, ahora aplicada a todas las caras del tetraedro global `T_j`, da

\[
\boxed{T_{j+1}=-\frac53T_j},\qquad
\boxed{R_j=R_0\left(\frac53\right)^j},\qquad O_j=O.
\]

La razón de escala `5/3` resulta de la geometría euclídea del tetraedro regular **y de la elección concreta de espejo sobre caras**. No es un factor universal deducido de la ontología y tampoco la ganancia `g_j` de disipación en el canal O18.

Esta recurrencia genera infinitas capas concéntricas de referencias para `j≥0`. Las capas son conjuntos finitos de puntos y la regla por sí sola no demuestra una teselación del volumen tridimensional. Para la cobertura completa se necesitan reglas adicionales de ocupación, empalme, compatibilidad y no superposición de módulos.

## 6. Distinción entre las dos operaciones de espejo [T]

- **O19 (planos centrales):** cada espejo interno conserva el radio global `R`; una imagen complementaria junto al tetraedro original determina los ocho vértices de un cubo de radio circunscrito `R` (en la normalización de vértices); las tres reflexiones forman un grupo finito.
- **O20 (planos de caras):** cada espejo fija una cara local y crea una quinta referencia a radio `5R/3` del centro inicial. Las cuatro continuaciones reunidas forman otra capa tetraédrica y permiten una regla recursiva de escalamiento.

Son operaciones geométricas distintas; se complementan como laboratorios del foco fijo, del radio local y del radio que crece.

## 7. La diferencia pendiente y el límite dimensional [T/A]

Si se exige un quinto punto a la misma distancia `a` de **los cuatro vértices** originales, se está intentando realizar cinco puntos mutuamente equidistantes. En espacio euclídeo la dimensión mínima de un conjunto de cinco puntos mutuamente equidistantes es cuatro (simplex regular de dimensión 4). Por eso la quinta referencia que construimos en tres dimensiones se conecta con los tres vértices de la cara por distancia `a`, mientras la distancia al cuarto vértice es `a√(8/3)`.

Este es un discriminante exacto entre **crear una continuación local** y **exigir cinco referencias todas equivalentes**. Si el programa asocia la segunda exigencia con una dimensión nueva, habrá que precisar qué comparaciones obligan a añadir esa relación.

## 8. Tres obligaciones antes de llamar al mecanismo una ley del programa [A]

1. **Elección sin foco exterior:** definir desde la relación abstracta K4 y su incertidumbre qué operación selecciona el espejo de cara, la colección de cuatro caras y su escala; la regularidad euclídea es aquí una hipótesis geométrica.
2. **Repetibilidad compatible:** demostrar que las continuaciones forman una trama global utilizable, con sus intersecciones, interfaces y holonomías explícitas. El tetraedro regular por sí solo no tesela exactamente todo R³.
3. **Puentes físicos:** derivar una magnitud de contención y una dinámica que vinculen las distancias y los nuevos módulos con masa, tiempo y grados de libertad observables; el factor geométrico `5/3` no es una medición de gravedad ni de masa.

## Dictamen

**Hallazgo exacto:** quinta referencia por espejo de cara, radio global `5R/3`, módulo local congruente, cuatro quintas referencias que forman una siguiente escala tetraédrica de foco global fijo, y repetición formal indefinida `R_j=(5/3)^j R_0`. **Hipótesis a investigar:** esta regla podría representar un mecanismo de cierre propio y nacimiento de nuevas escalas desde la mínima unidad; requiere derivar su operación desde las relaciones antes de interpretarla físicamente.
