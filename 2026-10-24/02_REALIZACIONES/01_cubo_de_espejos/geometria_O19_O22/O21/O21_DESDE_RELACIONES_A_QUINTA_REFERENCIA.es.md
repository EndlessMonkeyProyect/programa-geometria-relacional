# O21 — De las relaciones mínimas al tetraedro, la quinta referencia y el octaedro

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 19 de octubre de 2026**  
**Estado:** formalización condicional + teoremas de geometría euclídea + 50 pruebas exactas de regresión.  
**Continuidad:** O19 (cubo por espejos centrales), O20 (cuatro reflejos de cara y radio global creciente), núcleo de cierre propio, O5 (contrato de preguntas), O14/O16 (interfaces y contención).  
**Alcance:** no demuestra que las relaciones abstractas generen por sí solas un espacio físico, ni una ley de masa, tiempo o gravitación.  

## 1. Narrativa: primer cierre y capacidad de repetición [O]

Una unidad admite diferencias acreditadas por comparación. Cuando ciertas relaciones se sostienen simultáneamente, pueden usarse como una referencia común. Una nueva comparación puede revelar una diferencia que requiere ampliar la representación. En la lectura propuesta, la primera estructura tridimensional repetible puede representarse mediante cuatro referencias, y una quinta aparece al continuar las relaciones de una cara.

En el laboratorio hay que distinguir **(a) la estructura de conectividad**, **(b) la métrica que hace comparables las aristas**, **(c) la elección de la continuación**, **(d) la ocupación del espacio**. Son exigencias sucesivas; las cuatro no se siguen automáticamente unas de otras. «Indefinición» no significa identidad de longitudes. La igualdad de seis longitudes será aquí una condición de simetría física declarada.

## 2. Datos mínimos del laboratorio [D]

`K₄` posee cuatro nodos y seis enlaces. Por sí solo no asigna longitudes ni volumen. Introducimos:

- **H1:** el espacio de realización geométrica es euclídeo, con producto escalar y puntos medios;
- **H2:** la función de distancia sobre los seis enlaces es invariante bajo todas las permutaciones de las cuatro referencias (`S₄`), y su longitud común `a` es estrictamente mayor que cero;
- **H3:** una continuación admisible desde una cara conserva las tres distancias `a` desde la nueva referencia a los tres vértices de esa cara;
- **H4:** cuando estudiamos un nuevo módulo se exige una referencia distinta del vértice anterior; para no privilegiar cara alguna estudiamos conjuntamente las cuatro posibilidades.

H1 y H2 no han sido deducidas del núcleo ontológico. H2 es *isotropía de aristas*, no una afirmación sobre homogeneidad de todo el espacio. H3 y H4 constituyen el contrato de continuación.

## 3. Teorema O21-T1 — La igualdad de seis enlaces [T]

Las permutaciones de `S₄` actúan transitivamente sobre los seis pares no ordenados de vértices. Si una asignación de longitudes es invariante bajo todas esas permutaciones, entonces las seis longitudes son iguales. En una realización euclídea su tetraedro es regular.

Para cuatro posiciones centradas `v₁,…,v₄`, con `∑vᵢ=0`, la matriz de Gram viene determinada solo por el lado `a`:

\[
\boxed{G_{ij}=\frac{a^2}{2}\left(\delta_{ij}-\frac14\right)},\qquad
\operatorname{rank}G=3.
\]

En consecuencia existe una realización en dimensión tres, única salvo isometría euclídea global, incluyendo reflexión. Es el menor número de puntos que puede afinar un simplex tridimensional no degenerado. Pero **K₄ sin H2 admite realizaciones irregulares**; incluso cuatro puntos equidistantes de un centro no necesariamente tienen seis distancias mutuas iguales. La equiparación de «sin foco privilegiado» con «todas las aristas iguales» es una elección interpretativa y debe conservar ese estatus.

## 4. Teorema O21-T2 — Una cara conserva dos posibilidades [T]

Para una cara triangular equilátera de lado `a`, las tres esferas de radio `a` centradas en sus vértices se cortan en dos puntos tridimensionales, uno a cada lado del plano de la cara. Ambos están a altura de magnitud

\[
\boxed{h=a\sqrt{\frac23}}.
\]

Una realización corresponde al vértice que completaba el tetraedro inicial; la otra, a la continuación reflejada. La condición **«nueva referencia distinta»** de H4 elige esta segunda realización *una vez declarada la cara*. No elige cuál de las cuatro caras usar. Si ninguna cara está privilegiada por las relaciones externas, el sistema admite cuatro continuaciones simétricas o la colección de las cuatro.

Esta es una **ambigüedad de realización relativa a una cara y a una historia de orientación**, no un bit de signo fundamental del programa. El signo relacional del programa indica composición/división entre escala y referente, no la positividad o negatividad de coordenadas auxiliares.

## 5. Teorema O21-T3 — Regla local, escala global, foco [T]

Sea `O` el centroide intrínseco de los cuatro vértices y `vᵢ` la posición de cada vértice respecto de `O`. Para un tetraedro regular, los otros tres vértices pertenecen al plano `vᵢ·x=−R²/3`, donde `R=||vᵢ||`. El vértice adicional obtenido por reflexión de `vᵢ` en ese plano es

\[
\boxed{w_i=-\frac53 v_i},\qquad \boxed{||w_i||=\frac53R}.
\]

Cada una de las cuatro continuaciones conserva el tamaño y las distancias internas del tetraedro inicial; su centroide local es `O−(2/3)vᵢ`. La colección completa de los cuatro nuevos vértices es

\[
\boxed{T_1=-\frac53T_0},\qquad \boxed{\operatorname{centroide}(T_1)=O}.
\]

Repitiendo el mismo contrato sobre *las cuatro caras de cada tetraedro global*:

\[
\boxed{T_j=\left(-\frac53\right)^jT_0},\qquad
\boxed{R_j=R_0\left(\frac53\right)^j}.
\]

La transformación es `S₄`-equivariante: renumerar vértices solo renumera las cuatro continuaciones. El foco es el centroide reconstruido desde todas las relaciones de la capa, no un quinto punto exterior.

**Precisión geométrica descubierta en O21:** el volumen del tetraedro de generación `j` no contiene todos los vértices de la generación `j−1`. En coordenadas baricéntricas respecto del tetraedro exterior, cada viejo vértice tiene coeficientes `(-1/5, 2/5, 2/5, 2/5)` (en su orden correspondiente). El coeficiente `−1/5` certifica que está fuera de ese sólido. Por tanto las capas no son tetraedros sólidos anidados: la regla conserva un **centro común y radios de vértices crecientes**.

## 6. Teorema O21-T4 — El octaedro está implícito en los seis enlaces [T]

Los seis puntos medios de las seis aristas de un tetraedro regular son seis puntos distintos. Los puntos medios de aristas opuestas son antipodales respecto de `O`. Los otros doce pares se separan por la distancia `a/2`; forman las doce aristas de **un octaedro regular**.

Si `m_{ij}=(v_i+v_j)/2`, entonces

\[
 m_{ij}=-m_{k\ell}\quad\text{para aristas opuestas},\qquad
 \boxed{a_{\mathrm{octa}}=\frac{a_{\mathrm{tetra}}}{2}}.
\]

En la normalización de O19/O20, `vᵢ` son las cuatro ternas de signos con producto `+1` y los puntos medios son las seis posiciones `±e₁, ±e₂, ±e₃`. Las reflexiones centrales de O19 completan los ocho vértices del cubo `[-1,1]³`, mientras esos puntos medios son los vértices del octaedro dual de ese cubo. Comparten el mismo centro.

**Lectura relacional condicional:** las seis relaciones originales pueden ofrecer seis referencias derivadas, si se admite la operación geométrica de punto medio. Ni la operación de promedio ni la distancia euclídea están contenidas solo en la definición combinatoria de `K₄`. Además, el octaedro derivado tiene lado **mitad** del tetraedro original: hacerlos encajar como celdas de la misma red requiere un ajuste de escala adicional, cuya selección no está deducida todavía.

## 7. Teorema O21-T5 — La repetición tetraédrica no tesela R³ [T]

El ángulo diedro interior de un tetraedro regular es `θ_t=arccos(1/3)≈70.528779°`. Para una teselación cara a cara exclusivamente con tetraedros regulares congruentes, alrededor de cada arista interior debería caber un número entero de estos ángulos sumando 360°. Sin embargo,

\[
5\theta_t<360^\circ<6\theta_t.
\]

Por tanto **no existe tal teselación de todo R³ con únicamente estos tetraedros regulares congruentes**.

El octaedro regular tiene ángulo diedro `θ_o=arccos(−1/3)=180°−θ_t`, y satisface

\[
\boxed{2\theta_t+2\theta_o=360^\circ}.
\]

Esto es compatible con la teselación tetraédrico-octaédrica conocida, donde las dos celdas regulares poseen aristas del mismo tamaño. Los seis puntos medios del tetraedro inicial proporcionan la forma octaédrica, pero no por sí solos el escalamiento y las reglas de empalme que garantizan esta teselación.

## 8. Falsador geométrico del relleno por reflejos [F]

Un tetraedro regular con vértices `(0,0,0),(1,1,0),(1,0,1),(0,1,1)` comparte su cara inclinada con el octaedro regular de centro `(1,1,1)` y seis vértices `(1,1,1)±e_i`. Ambas celdas tienen lado `√2`.

Reflejar el vértice `(0,0,0)` por el plano de la cara `x+y+z=2` da `q=(4/3,4/3,4/3)`. Este punto `q` está sobre la **cara opuesta del octaedro**, y el tetraedro reflejado completo queda **dentro** de ese octaedro. Su volumen es `1/3`, frente a `4/3` del octaedro.

Por lo tanto, en la realización de relleno tetraédrico-octaédrico, **la reflexión local de un tetraedro no puede sustituir al octaedro adyacente sin solaparlo**. Necesitamos diferenciar el operador de generación de referencias del operador de ocupación espacial. La comparación sirve precisamente para detectar una relación o tipo de módulo que faltaba.

## 9. Cinco referencias y nueva dimensión [T/A]

La quinta referencia reflejada conserva tres distancias iguales a su cara, pero no la distancia a los cuatro vértices. Si exigimos cinco posiciones mutuamente equidistantes, la matriz de Gram centrada tiene rango 4; en espacio euclídeo eso requiere al menos cuatro dimensiones.

Este es el límite preciso entre «quinto punto como continuación tridimensional» y «quinto punto equidistante de los cuatro anteriores». Un módulo adicional no equivale automáticamente a una nueva dimensión. El cambio dimensional surge si exigimos una familia de comparaciones que no cabe en la representación tridimensional actual.

## 10. Estado respecto del Programa [O/T/A]

| Noción | Resultado | Estatus |
|---|---|---|
| Primera unidad | K₄ con 4 nodos, 6 pares | [T, combinatorio] |
| Regularidad | todas las longitudes iguales si la métrica respeta S₄ | [T, condicional a H2] |
| Quinta referencia | continuación especular sobre una cara | [T, con H1/H3] |
| Indefinición | cara sin elegir y dos realizaciones antes de usar historia | [T, relativo a preguntas] |
| Cierre generativo | cuatro ramas forman otro tetraedro con mismo centro | [T, geométrico] |
| Radio creciente | razón 5/3 por generación completa | [T, geométrico] |
| Octaedro interno | seis puntos medios de las relaciones | [T, geométrico] |
| Ocupación total de R³ | tetraedros regulares solos no lo consiguen | [F] |
| Teselación tetra–octa | posible bajo regla de empalme y escala común | [T conocido / A derivación propia] |
| Memoria, masa, tiempo, gravedad | ninguna dinámica física deducida aquí | [A] |

## 11. Qué conviene investigar en O22 [A]

**A. Origen de la isotropía.** Definir, mediante preguntas relacionales, cuándo una familia de seis enlaces debe compartir un parámetro de longitud, y cuándo distintas métricas son indistinguibles. Sin esto, la regularidad es un contrato geométrico, no una consecuencia del núcleo ontológico.

**B. Reconciliar reflexión y ocupación.** Elegir una regla puramente relacional que produzca y empalme las piezas tetraédricas y octaédricas, con aristas compatibles, sin doble ocupación ni huecos. Comprobarla en una celda finita antes de extrapolar a volumen infinito.

**C. Contención y costo de reconstrucción.** Contar qué comparaciones conserva la interfaz triangular entre módulos y qué información adicional exige introducir una celda octaédrica. Aplicar el criterio de O17-A, sin equiparar ese conteo con masa física todavía.

**D. Radio que crece y radio fijo.** Distinguir el radio local de una celda, el radio de los vértices respecto del foco común, el radio métrico de la teselación y el radio físico medible. La razón 5/3 describe una operación geométrica de espejo de caras, no constituye por sí sola una ley física universal.

**E. Criterio experimental.** Explorar los laboratorios de espejos y esferas para probar qué consultas locales permiten reconstruir el centro y detectar huecos. No convertir una imagen de reflexión en evidencia de memoria o tiempo físico si no se dispone de dinámica medible.

## 12. Disciplina editorial

El «signo» ontológico del programa identifica el rol de escala/referente, expresable como multiplicar o dividir al cambiar de nivel. Los signos `−` usados en vectores, coordenadas y determinantes son herramientas de representación geométrica, no una atribución ontológica de negatividad a masa o información. «Masa es la contención de información en este plano» se mantiene como hipótesis física candidata, sin reinterpretarla como cancelación de vectores.

No existe en O21 un puente demostrado hacia Compton, radio del protón, ley de gravitación o viscosidad hiperdifusiva. Este suplemento prepara un discriminante geométrico para esos puentes al separar referencias nuevas, distancias, interfaces y ocupación.

## Dictamen final

La operación de espejo de caras puede construir la quinta referencia a partir de una cara con tres relaciones equivalentes, reconstruir cuatro continuaciones simétricas y generar capas de radio creciente con foco global común. Los seis enlaces del tetraedro regular generan además el octaedro de sus puntos medios. **La repetición de módulos y el relleno espacial requieren operaciones distintas**, lo que identifica una nueva obligación verificable para la formalización relacional.
