---
title: "O60 — De los sectores no habitados a la estela de escalas: ocupación simétrica y normalización cuadrática"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-21"
status: "Suplemento aditivo candidato; modelos finitos y teoremas exactos, puente físico abierto"
parents: ["O40", "O44N", "O45", "O54", "O55", "O56", "O57", "O58", "O59", "Imagen Total v3.8.1"]
---

# O60 — La unidad se autorreferencia; la totalidad no tiene que estar habitada

## 0. Resultado en el orden correcto

**[O — narrativa del programa].** Las relaciones disponibles forman una totalidad; los reflejos habitan determinadas relaciones. Una unidad puede sostener su cierre propio sin habitar toda la totalidad. La estructura normalizada se conserva como referencia, admite diferentes configuraciones y restringe las continuaciones por el total. La dirección física es consecuencia eventual de las relaciones, no su fundamento. El múltiplo que normalizó la etapa anterior debe permanecer reconstruible en la siguiente. Una nueva ocupación no debería obligar a «desresolver» una relación ya acreditada si se adopta ese principio ontológico.

**[D/H — contrato aritmético aún por confirmar].** Adoptamos **condicionalmente** la traducción fuerte de O58:

\[
\boxed{a^2+b^2+1=N^2,\quad a,b,N\in\mathbb Z_{>0}.}\tag{60.1}
\]

El símbolo `1` expresa una **unidad bruta del registro**, no necesariamente un resto fraccionario conservado, una partícula, una celda óptica real o una tercera fuerza. Esto no sustituye la identidad bilateral canónica, válida para todo `N`:

\[
N^2-(N-1)(N+1)=1.\tag{60.2}
\]

**[T — nueva realización exacta].** Existe un laboratorio **finito con reflexiones y giros** en el que toda solución positiva de (60.1) admite dos familias habitadas de tamaños `a²`, `b²` y **un único punto central todavía deshabitado**, conservando la simetría completa del laboratorio. En ciertos cambios de escala la nueva ocupación puede construirse exclusivamente dentro del sector antes pendiente, sin borrar nada anterior. Esto produce una estela anidada infinita en una subfamilia exacta.

**[A — no demostrado].** No se deduce de ello que (60.1) sea la ley de los radios del vórtice, que los reflejos físicos de O59 impongan tal partición, que un único punto origine cada familia por reflexión, ni la regularidad de Navier–Stokes tridimensional.

## I. Del cubo de espejos a una distinción no negociable

El laboratorio de **espejos enfrentados de O59** da, por coordenada de un eje de longitud `L=1`, las posiciones `2k±p`, `k∈Z`. Una unidad ocupante de `p=1/3` no ocupa la familia de `p=2/3`; ambas poseen denominador `3`. Es decir, **el normalizador aritmético por sí solo no determina qué familia habita una unidad**. La novedad de ocupación puede aparecer sin aumentar el denominador.

Tampoco toda referencia admite (60.1): `N=4` tiene posiciones ópticas perfectamente válidas, mientras que `a²+b²=15` no tiene solución entera positiva. El puente entre laboratorio de reflejos y condición cuadrática debe **construirse y probarse**, nunca darse por universal.

Por ello introducimos una segunda realización, con un **contrato de simetría distinto** del cubo de espejos de O59. No se afirma que sus operadores sean automáticamente los mismos que las reflexiones sucesivas entre caras opuestas del cubo.

## II. Laboratorio cuadrado de ocupación autorreferenciada [D]

Sea `N≥3` impar, `h=(N−1)/2`, y la cuadrícula centrada:

\[
\mathcal Q_N=\{(i,j)\in\mathbb Z^2:-h\le i,j\le h\},\qquad |\mathcal Q_N|=N^2.\tag{60.3}
\]

Sea `D₄` el grupo de las ocho simetrías del cuadrado generado por reflexiones, actuando por intercambiar `i,j` y cambiar signos. Las órbitas son las **familias de posiciones intercambiables bajo las operaciones admitidas**. Establecemos una partición:

\[
\mathcal Q_N=A_N\sqcup B_N\sqcup E_N,\quad
|A_N|=a^2,\quad |B_N|=b^2,\quad E_N=\{(0,0)\}.\tag{60.4}
\]

`A_N` y `B_N` deben ser **uniones completas de órbitas** de `D₄`. Se llaman aquí dos *canales de ocupación*; no se identifican con los dos radios físicos de un toroide. El punto `(0,0)` pertenece al espacio de relaciones pero **no** a la ocupación de esos dos canales.

En `N=3`, las órbitas son exactamente las cuatro esquinas, los cuatro centros de borde y el centro. Una ocupación posible es:

```
A B A
B · B
A B A
```

Las dos familias tienen 4 posiciones y la central queda deshabitada:

\[
\boxed{4+4+1=9\quad (a,b,N)=(2,2,3).}\tag{60.5}
\]

Un `·` no es ausencia de luz o una singularidad física. **Es una relación disponible que no ha sido habitada por las dos familias elegidas.** Si se siembra una marca central, pertenece a su propia órbita; no estaba prohibida.

## III. Teorema de las órbitas: la totalidad restringe la ocupación [T]

**T60.1 (censo exacto).** En `\mathcal Q_N` hay:

\[
\boxed{1\text{ órbita de tamaño }1,\quad
N-1\text{ órbitas de tamaño }4,\quad
\frac{(N-1)(N-3)}8\text{ órbitas de tamaño }8.}\tag{60.6}
\]

**Prueba.** El origen es fijo por las ocho simetrías. Cada radio sobre eje o diagonal de distancia `k∈{1,...,h}` genera una órbita de cuatro puntos: `2h=N−1` órbitas. Para pares de coordenadas de valores absolutos distintos y no nulos `1≤u<v≤h`, las ocho imágenes son distintas: `h(h−1)/2=(N−1)(N−3)/8` órbitas. Su cardinalidad total es `1+4(N−1)+(N−1)(N−3)=N²`. ∎

**T60.2 (realización de todo cierre cuadrático positivo).** Si `a,b,N>0` son enteros que satisfacen (60.1), entonces existe una partición (60.4) donde ambos canales son invariantes bajo `D₄`.

**Prueba.** O58 demuestra que `N` es impar y `a,b` son pares. Así, `a²` y `b²` son múltiplos de `4`. Las órbitas no centrales tienen tamaño `4` u `8`; como existen `N−1≥2` órbitas de tamaño `4`, los números posibles de celdas al escoger uniones de órbitas comprenden **todos los múltiplos de cuatro** entre `0` y `N²−1`: en unidades de cuatro, los bloques de tamaño cuatro aportan `1` y los de ocho aportan `2`; los intervalos `[2k,2k+(N-1)]` cubren todos los enteros consecutivos desde `0` hasta `(N²−1)/4`. Escoja una unión de órbitas `A_N` de tamaño `a²`; el complemento, excepto el centro, es `B_N` y tiene `b²` elementos. ∎

**Alcance decisivo.** Es una realización de cardinalidades cuadráticas mediante **ocupación compatible con las simetrías**, no una prueba de que existen dos cuadrados geométricos disjuntos de lados `a,b` que recubran la cuadrícula. De hecho, en una cuadrícula `3×3` **no** caben dos cuadrados geométricos contiguos `2×2` disjuntos; todos los pares de tales bloques se solapan. Los cuadrados en (60.1) son **cantidades de relaciones**, no formas físicas ya identificadas.

## IV. La estela entre normalizadores: ocupación sin borrado [D/T]

Sea `(a,b,N)` una configuración válida y otra `(a',b',N')` con `N'=mN`, `m∈\mathbb Z_{>0}`. Por paridad de ambos normalizadores, `m` es impar. **Refinamos** cada celda vieja a un bloque `m×m` de celdas nuevas (no un simple movimiento del espejo):

\[
(i,j)\longmapsto
\{(mi+u,mj+v): |u|,|v|\le(m-1)/2\}.\tag{60.7}
\]

La operación respeta exactamente las simetrías `D₄`: primero reflejar el bloque y luego refinar es lo mismo que primero refinar y luego reflejar. **El múltiplo `m=N'/N` es la referencia explícita de transporte de esa organización.**

Mantengamos las celdas ya habitadas por `A,B` como bloques completos de sus respectivos colores. El antiguo `·` se convierte en un bloque central `m×m` deshabitado. Allí puede incorporarse la novedad, dejando todavía un centro `·`.

Definimos:

\[
\Delta_A=a'^2-m^2a^2,\qquad
\Delta_B=b'^2-m^2b^2.\tag{60.8}
\]

Por las dos ecuaciones cuadráticas:

\[
\boxed{\Delta_A+\Delta_B=m^2-1.}\tag{60.9}
\]

**T60.3 (criterio necesario y suficiente dentro de esta regla de refinamiento).** Se puede realizar una ocupación `D₄`-invariante de todo el nuevo sector central excepto una celda, **sin desocupar ninguna de las celdas anteriores**, si y sólo si:

\[
\boxed{\Delta_A\ge0\quad\text{y}\quad\Delta_B\ge0.}\tag{60.10}
\]

**Prueba.** Necesidad: ocupar sólo sectores vacantes no puede disminuir el número de celdas que ya pertenecen a un canal. Suficiencia: cada delta es múltiplo de cuatro (a,b,a',b' pares), y (60.9) llena exactamente `m²−1` celdas. Aplicar T60.2 en su versión de selección de órbitas al bloque central de lado impar `m`: elegir `\Delta_A` celdas como unión de órbitas no centrales y asignar las restantes `\Delta_B` a B. La central permanece vacante; toda la partición es D₄-invariante, porque la coloración anterior y el refinamiento ya lo eran. ∎

**Importante:** las fracciones de ocupación `a²/N²` y `b²/N²` generalmente **cambian**. Conservar la referencia y las relaciones realizadas como *subestructura embebida* no es conservar sus pesos porcentuales ni su dirección espacial. Ésta es una regla exacta del presente modelo, no una obligación deducida de Navier–Stokes.

## V. Tres continuaciones desde la misma unidad [T]

| Camino | Multiplicador `m` | `ΔA` | `ΔB` | Admite ocupación sin borrar |
|---|---:|---:|---:|---|
| `(2,2,3)→(4,8,9)` | 3 | −20 | 28 | **No** |
| `(2,2,3)→(34,38,51)` | 17 | 0 | 288 | **Sí** |
| `(2,2,3)→(70,70,99)` | 33 | 544 | 544 | **Sí** |

Cuentas de los dos caminos permitidos:

\[
34^2+38^2+1=51^2=2601,
\qquad
70^2+70^2+1=99^2=9801.\tag{60.11}
\]

En `3→51`, los dos primeros canales ocupaban `4×17²=1156` celdas cada uno tras refinar. El antiguo centro produce `17²=289` celdas; 288 pasan a B, una sigue vacía. El primer canal no necesita redefinir sus posiciones anteriores.

En `3→99`, las cuatro esquinas y los cuatro centros de borde originales se refinan a bloques de `33²=1089`: cada canal inicia con 4356 celdas. De las 1089 celdas del centro, se añaden 544 a A, 544 a B y una queda vacante. Así se obtiene exactamente `4900+4900+1=9801`.

El camino `3→9` es una **continuación aritmética**, pero no una *extensión de ocupación sin borrado* en esta representación: su canal A bajaría de `4×3²=36` a `4²=16` celdas. No queda «matemáticamente prohibido»; queda fuera del contrato adicional de conservar cada relación previamente ocupada.

**Conclusión:** la regla de no desocupar reduce la familia de caminos, pero **no selecciona uno solo**. Los caminos `3→51` y `3→99` siguen siendo distintos y admisibles.

## VI. Una estela infinita con el centro puntual persistente [T]

Parta de una solución simétrica de Pell:

\[
N^2-2a^2=1,
\quad (N,a)=(3,2).\tag{60.12}
\]

Defina un sucesor mediante el cubo algebraico:

\[
\boxed{N'=N(4N^2-3),\qquad a'=a(4N^2-1),\qquad b'=a'.}\tag{60.13}
\]

Esto es exactamente `(N+a\sqrt2)^3=N'+a'\sqrt2`. Por multiplicatividad de la norma `x²−2y²`, `N'^2−2a'^2=1`; por construcción `N|N'`. Además, con `m=4N²−3`, se tiene `a'>ma`, ya que `4N²−1>4N²−3`. Por tanto, los deltas de ambos canales son **positivos** y T60.3 se aplica a cada salto.

La sucesión comienza:

\[
\boxed{3\longrightarrow99\longrightarrow3\,880\,899\longrightarrow\cdots}\tag{60.14}
\]

Cada etapa puede contener a la anterior como bloques ocupados, mientras se ocupa parte de la única zona central pendiente. Al normalizar la cuadrícula completa a un cuadrado de lado uno, la única celda deshabitada tiene área relativa `1/N_j²`, y `N_j→∞`. Los cuadrados centrales pendientes están encajados y su intersección geométrica es **un punto**: el centro.

Ésta es una realización exacta de la expresión **«una estela de escalas con una referencia puntual»**: el centro permanece referencialmente identificable mientras las escalas de resolución aumentan. No significa que una singularidad física de flujo esté probada, ni que ese punto tenga masa, energía o una curvatura infinita.

## VII. Qué aprendimos y qué no [O/T/F/A]

**[T]** El laboratorio de simetría finita exhibe una totalidad con más relaciones que las habitadas por cada familia. La ocupación compatible forma un cierre propio bajo el grupo de operaciones; lo pendiente puede conservarse como una única celda central por etapa.

**[T]** La condición cuadrática, el transporte por un múltiplo y la **ocupación monotónica** pueden combinarse en estelas infinitas sin exigir que se pierdan relaciones previamente acreditadas. Se obtiene un criterio matemático que descarta ciertas transiciones y conserva otras.

**[T/F]** Es falso que el denominador por sí solo decida qué relación está habitada: `1/3` y `2/3` en O59 pertenecen a órbitas distintas con igual denominador. También es falso que una suma de cuadrados asegure la disposición como dos cuadrados físicos disjuntos, o que un canal grande pueda generarse necesariamente desde **una sola imagen** bajo `D₄`: cada órbita individual posee a lo sumo ocho puntos, mientras que un canal puede reunir muchas órbitas.

**[A]** No hemos derivado una correspondencia única entre (60.1) y los radios `R,r` del toroide, entre las celdas ocupadas y la vorticidad `\omega`, ni una regla que convierta el índice de escala en tiempo físico. El espejo de O45 sigue siendo una referencia de comparación. La incompresibilidad y la ecuación de transporte de vorticidad de O53–O57 no obligan a usar esta partición discreta.

**[A]** El ensayo físico decisivo exigiría definir desde el estado completo del flujo y *antes* de ver el futuro un mapa `\mathfrak C[u]` hacia referencias, unidades, relaciones y ocupación; exigir que sea independiente de cambios permitidos de observador; y demostrar una ley de actualización **derivada** de Navier–Stokes. No basta elegir `N` a posteriori para acomodar los números. Una ley de selección tendría que distinguir, por ejemplo, el paso hacia `51` del paso hacia `99`, o explicar la coexistencia de ambos como soluciones de distinta circunstancia.

## VIII. Propuesta de continuación O61

**No empezar por otra simulación sin contrato.** Preparar primero el mapa de correspondencias físicas para una familia concreta de anillos de O53:

1. Definir **qué objeto del flujo** constituye una unidad autorreferenciada observable (por ejemplo, una familia de material trazado o un soporte de vorticidad definido sin umbral arbitrario).
2. Definir el **total y la relación todavía deshabitada** mediante operaciones verificables sobre ese objeto; evitar clasificar como «no habitado» algo simplemente no medido.
3. Proponer **cómo extraer** dos cantidades de naturaleza cuadrática y una referencia normalizadora a partir de invariantes de ese flujo, controlando unidades físicas y observadores.
4. Comprobar si la supuesta regla discreta persiste bajo una perturbación pequeña de datos continuos. Si no, queda como laboratorio aritmético, no como ley general del PDE.

## IX. Reproducción

`python codigo/verificar_o60.py` reconstruye exactamente el grupo de simetrías de cada retícula, censos de órbitas, particiones compatibles, contrafactuales `3→9`, `3→51`, `3→99`, los controles del modelo óptico, el ejemplo de no teselación mediante dos cuadrados `2×2`, y la cadena de Pell hasta `3,880,899`. La muestra incluye **186 aserciones agrupadas**, no certificación física; los teoremas de este documento son la garantía general dentro del modelo finito.

**Este O60 es un suplemento aditivo, no edita O58/O59 ni reemplaza la Imagen Total.**
