# O22 — Continuidad de interfaces, quinta referencia y cierre del espacio

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**Fecha:** 19 de octubre de 2026  
**Continuidad:** O19 (reflexiones centrales y caja), O20 (crecimiento especular por caras), O21 (origen métrico y octaedro), O14 (composición por interfaces), O15/O16 (magnitud y contención).  
**Estado epistemológico:** [O] interpretación ontológica, [D] definición/hipótesis formal, [T] teorema condicionado a las hipótesis, [E] ensayo exacto finito, [F] contraejemplo, [A] obligación abierta.

## 0. Tesis y resultado principal

**[O]** Una unidad que se reproduce conserva un conjunto de relaciones suficientes para reconocer nuevas unidades. La repetición de una forma es una operación; conseguir que varias formas compartan interfaces y ocupen por completo un espacio es otra. La «diferencia pendiente» puede expresarse matemáticamente como la información de empalme que una cara todavía no determina.

**[T, geometría euclídea]** Existe una construcción explícita de todo \(\mathbb R^3\) mediante tetraedros regulares y octaedros regulares congruentes por tipo, todos con lado \(\sqrt2\), utilizando solo una red de paridad y reglas locales de empalme. Los tetraedros ocupan 1/3 del espacio por volumen, los octaedros 2/3. En el empaquetamiento periódico aparecen **dos tetraedros por cada octaedro**.

**[T, nueva conexión O20→O22]** La quinta referencia dada por la reflexión de un tetraedro en su cara es *exactamente el centroide de la cara opuesta de un octaedro vecino que comparte aquella cara*. De este modo, la referencia especular del O20 puede reconstruirse desde tres vértices de la celda complementaria, sin contarla como otro vértice del entramado.

**[A]** Esta realización exige estructura euclídea, distancias comunes, una regla de prolongación y una red periódica. No demuestra todavía que tales reglas nazcan necesariamente de la ontología, ni establece propiedades de espacio-tiempo, masa o dinámica física.

## 1. Presupuestos y tipos de relaciones

[D1] La métrica en cada tetraedro es euclídea y las seis distancias son iguales a \(a>0\); O21 ya probó cómo sale esto *si se adopta invariancia S₄ de las longitudes*. El grafo K₄ aislado no suministra \(a\) ni la geometría euclídea.

[D2] Las nuevas celdas se empalman cara a cara, con el mismo valor de arista en la interfaz compartida. Cada punto interior pertenece a una sola celda tridimensional; una cara común puede pertenecer a dos celdas. Es el **contrato de ocupación**, distinto del contrato de **reflexión y referencia** de O20.

[D3] Para esta realización constructiva se toma una red transitable de puntos

\[
\Lambda=\{(i,j,k)\in\mathbb Z^3:i+j+k\equiv0\pmod2\}.
\]

La paridad utilizada en esta red es una etiqueta combinatoria. No es el «signo» ontológico de escala/referente que el programa usa para multiplicar/dividir entre escalas.

## 2. Construcción por celdas unitarias

[D] En un cubo de la retícula entera \(C_z=z+[0,1]^3\), los cuatro vértices cuya suma de coordenadas es par pertenecen a \(\Lambda\). Su envolvente es el tetraedro \(T_z\). Los otros cuatro vértices, cuya suma es impar, son centros de octaedros.

Para \(z=(0,0,0)\):

\[
T_0=\operatorname{conv}\{(0,0,0),(1,1,0),(1,0,1),(0,1,1)\},
\]

con lado \(a=\sqrt2\) y volumen \(V_T=1/3\).

Para cada esquina impar \(w\) del cubo se forma el simplejo con \(w\) y sus tres vecinos pares dentro del mismo cubo. Cada pieza tiene volumen \(1/6\).

**[T1: partición exacta de un cubo]** El cubo es la unión de ese tetraedro y esas cuatro piezas; sus interiores son disjuntos:

\[
\boxed{V(C_z)=V(T_z)+4V(\mathrm{pieza})=\tfrac13+4\cdot\tfrac16=1.}
\]

### Demostración por desigualdades exactas

Para \(C_0=[0,1]^3\), el tetraedro central se caracteriza por cuatro desigualdades:

\[
x+y+z\le2,\qquad x\le y+z,\qquad y\le x+z,\qquad z\le x+y.
\]

Las regiones que incumplen cada una de esas desigualdades corresponden a las cuatro piezas de esquina, respectivamente en los vértices impares \(111,100,010,001\). Dentro del cubo, dos incumplimientos estrictos no pueden darse simultáneamente (por ejemplo \(x>y+z\) y \(y>x+z\) son incompatibles; y \(x>y+z\) requiere \(x+y+z<2\)). En consecuencia, los interiores no se superponen y ninguna zona queda fuera. Las otras celdas unitarias son imágenes congruentes de esta partición.

## 3. Los ocho sectores reconstruyen un octaedro

Definimos para cada punto impar \(w\in\mathbb Z^3\) el sólido:

\[
O_w=\Big\{x\in\mathbb R^3:\sum_{i=1}^3|x_i-w_i|\le1\Big\}.
\]

Es un octaedro regular cuyo centro es \(w\) y cuyos seis vértices son \(w\pm e_1,w\pm e_2,w\pm e_3\). Todos pertenecen a la red par \(\Lambda\). Sus doce aristas miden \(\sqrt2\), como las del tetraedro.

**[T2]** Cada uno de los ocho cubos unitarios vecinos de \(w\) aporta una octava parte del octaedro, de volumen \(1/6\). Por tanto

\[
\boxed{V_O=8\cdot\frac16=\frac43=4V_T.}
\]

La unión de T1 sobre todos los cubos y T2 sobre todas las esquinas impares produce una teselación global de \(\mathbb R^3\). La interfaz de dos celdas es una cara triangular completa, una arista o un vértice.

**Densidades exactas:** por cada volumen unitario aparece un tetraedro y contribuye la mitad de un octaedro completo. Por consiguiente los números de celdas se relacionan como \(N_T:N_O=2:1\), mientras sus fracciones de volumen son \(1/3:2/3\).

## 4. El quinto punto es la referencia de la cara opuesta

Tomemos la cara del tetraedro \(T_0\)

\[
F=\{(1,1,0),(1,0,1),(0,1,1)\}\subset\{x+y+z=2\}.
\]

El octaedro vecino \(O_{(1,1,1)}\) comparte exactamente \(F\). Su cara opuesta contiene los vértices

\[
F'=\{(2,1,1),(1,2,1),(1,1,2)\}\subset\{x+y+z=4\}.
\]

La reflexión de \((0,0,0)\) sobre el plano de \(F\) es

\[
q=(4/3,4/3,4/3).
\]

Por otra parte,

\[
\operatorname{centroide}(F')=\frac13\big[(2,1,1)+(1,2,1)+(1,1,2)\big]
=(4/3,4/3,4/3)=q.
\]

**[T3]** El punto especular es el centro de la cara opuesta del octaedro, no un vértice de esta teselación de arista constante. El tetraedro reflejado sobre F tiene cuatro vértices contenidos en el octaedro, volumen 1/3 frente al volumen 4/3 del octaedro. Reflejar la referencia y rellenar el volumen son operaciones matemáticas con salidas distintas pero relacionadas.

**Contraste con O20:** el radio \(R_j=(5/3)^jR_0\) concierne a los tetraedros completos obtenidos por reflexión de todas sus caras alrededor de un *centro de familia*. La teselación de O22 conserva una arista local \(a=\sqrt2\) a lo largo de la red, mientras los centros de las celdas cambian de ubicación. No se identifica el factor 5/3 con una ley de escala de la retícula.

## 5. Qué aporta la interfaz [D/T]

Una cara equilátera común posee tres referencias y tres vínculos internos. Bajo una interfaz declarada de arista \(a\):

- Para una continuación tetraédrica especular: se añade un punto y tres enlaces con la cara. Ese punto queda fijado si se especifica la orientación de continuación en 3D.
- Para un octaedro regular con esa misma cara: se añaden tres nuevos puntos y nueve enlaces adicionales a los tres ya presentes en la cara. Estos vínculos reconstruyen también el quinto punto especular como el centroide de su cara opuesta.

Estos números son **conteos de nodos y relaciones**, no medidas directas de bits, entropía ni masa. La cantidad de distinciones contenidas depende además de las preguntas y de los contextos admisibles de O5/O14/O17.

De aquí surge una lectura ontológica que puede someterse a nuevos experimentos: la indefinición asociada a la interfaz puede resolverse de distintas maneras, y un contrato global de ocupación distingue qué continuaciones participan de una misma trama espacial.

## 6. Foco global y focos locales

En O20 la familia concéntrica de tetraedros generados mediante cuatro reflexiones simultáneas conserva un centro global. En O22 la teselación es invariante bajo traslaciones de la red \(\Lambda\); sus tetraedros y octaedros tienen centros locales que pueden reconstruirse, y las caras compartidas determinan una estructura global de concordancia.

**[T4]** Una red periódica infinita invariante bajo una traslación \(t\neq0\) no puede privilegiar un punto único \(f\) fijo bajo *todas* las traslaciones, porque \(f+t\neq f\). Por ello el «foco compartido» de la teselación significa **coherencia de referencias locales**. La singularidad focal concéntrica de O20 y la coherencia translacional de O22 son dos regímenes geométricos bien tipados.

Si la ontología requiere un centro único en toda su extensión, habrá que añadir un estado de referencia, una condición de frontera o una selección de familia; no sale de la sola invariancia de una red infinita.

## 7. Invariante de esquina y prueba finita periódica

En cada vértice \(v\in\Lambda\) de la teselación confluyen **ocho tetraedros** (uno por cubo incidente) y **seis octaedros** (uno por cada vecino impar a distancia 1). Las caras triangulares se emparejan una a una, tetra–octa.

**[E]** El laboratorio `laboratorio_o22.py` realiza:

- distancias y volúmenes con fracciones exactas;
- partición de cubos pares e impares con muestreo racional;
- partición del octaedro en ocho sectores;
- coincidencia de la quinta referencia y el centroide de cara opuesta;
- cobertura y pares de caras de redes periódicas \((\mathbb Z/4\mathbb Z)^3\) y \((\mathbb Z/6\mathbb Z)^3\);
- contraste entre el octaedro de puntos medios de O21 (lado \(a/2\)) y el octaedro de relleno de O22 (lado \(a\)).

El toro de tamaño \(N=4\) contiene 64 tetraedros y 32 octaedros, con volumen total 64; hay 256 caras triangulares, cada una compartida exactamente por un tetraedro y un octaedro. La prueba sobre todas las celdas unitarias se fundamenta en T1 y T2; los controles finitos auditan su implementación.

## 8. Qué se ha demostrado y qué continúa abierto

| Enunciado | Estado |
|---|---|
| El modelo euclídeo tetra–octa tesela todo el espacio sin huecos ni solapamientos | [T] |
| El quinto punto especular es el centroide de la cara opuesta del octaedro vecino | [T] |
| Las celdas forman interfaces triangulares compartidas en una red periódica | [T], con [E] finito |
| La misma arista local puede usarse entre tetraedros y octaedros | [T], en la construcción |
| El núcleo abstracto de cuatro relaciones obliga a escoger esa teselación | [A] |
| El llenado geométrico implica una unidad de información contenida en un plano | [O/A], requiere contratos de observación |
| La trama es el espacio físico del universo | [A], requiere correspondencias y mediciones |
| El relleno selecciona una ley de masa, radiación, gravedad o NS | [A] |

**Siguiente obligación O23:** estudiar desde la interfaz triangular qué contrato mínimo discrimina la continuación tetraédrica y la octaédrica y por qué ese contrato puede transmitirse sin escoger un origen o centro privilegiado. Investigar la invariancia de los empalmes al cambiar de escala, sin identificar los centros de O20 con los de O22 ni el factor geométrico \(5/3\) con dimensiones físicas.

## 9. Convenciones lingüísticas del programa

- «Comunes» expresa las relaciones que varios módulos sostienen en una misma trama.
- «Cierre propio» expresa que la unidad puede reconocerse mediante las comparaciones declaradas.
- «Signo» de escala describe el cambio de referente mediante multiplicación/división. Los signos de coordenadas de esta representación son herramientas matemáticas.
- «Masa es la contención de la información en este plano» se mantiene como hipótesis física ontológica y no se identifica con el volumen de una celda ni con el conteo de sus aristas.
- «Indefinición» describe alternativas de comparación abiertas, no necesariamente una fluctuación física aleatoria.
