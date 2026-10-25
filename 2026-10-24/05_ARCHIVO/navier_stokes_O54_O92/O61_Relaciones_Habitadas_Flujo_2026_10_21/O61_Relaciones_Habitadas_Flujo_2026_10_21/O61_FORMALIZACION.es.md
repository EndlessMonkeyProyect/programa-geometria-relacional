---
title: "O61 — Relaciones disponibles y habitadas: un puente exacto de ocupación dinámica a Navier–Stokes"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-21"
status: "Suplemento autónomo: teoremas exactos para una clase NS 3D, simulación espectral convergente, no-go parcial y puente físico abierto"
parents: ["O40", "O44N", "O45", "O53", "O54", "O57", "O58", "O59", "O60", "Imagen Total v3.8.1"]
---

# O61 — De una totalidad de relaciones a la ocupación dinámica de un flujo

## 0. El hilo de la razón

**[O, ontología propuesta del programa]** La totalidad contiene relaciones que una unidad no necesariamente habita. Una unidad se sostiene por su propia referencia; las distintas configuraciones pueden compartir relaciones y diferir en cuáles están realizadas. El normalizador que permitió expresar una configuración ha de permanecer reconstruible al pasar a otra. **La dirección es una consecuencia de las relaciones, no el principio ontológico que las genera.** El espejo móvil hace comparables escalas y ritmos sin imponer un cambio de estado físico. La novedad puede significar que una relación disponible participe de una configuración que antes no la realizaba.

**[T]** En Navier–Stokes hay una manera directa de distinguir (i) relaciones de transferencia *admisibles* por la ecuación y (ii) transferencias *activas* para un estado concreto. Una clase invariante explícita contiene datos con idénticos modos activos iniciales, energía cinética y enstrofía, pero con transferencia inmediata nula o no nula a un tercer modo. El resultado es **exacto para la PDE** a nivel de su derivada inicial y para la reducción que sigue; la integración de sus coeficientes es numérica controlada.

**[A]** Esta realización no convierte el conteo `a²+b²+1=N²` de O58–O60 en una ley de NS, no demuestra que el vórtice toroidal O53 exhiba el mismo patrón, no identifica el `1` del resto con un modo ni demuestra regularidad global. Tampoco impone que los modos Fourier mantengan ocupación monotónica.

## I. ¿Qué relación puede estar disponible y no habitada? [D]

Fijamos Navier–Stokes incompresible, no forzado, viscoso, en el toro periódico tridimensional `T³=(R/2πZ)³`:

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\quad \nabla\cdot u=0,\quad \nu>0.\tag{61.1}
\]

La expansión de Fourier `u(x,t)=\sum_{k\in\mathbb Z³}\hat u_k(t)e^{ik\cdot x}` permite distinguir:

- **Relaciones disponibles:** triples de índices `p+q=k` que podrían contribuir a la ecuación para el modo `k` en algún estado solenoidal admitido. Una condición de suma de índices es necesaria, **no** suficiente: polarización y proyección de presión pueden anular el acoplamiento.
- **Relaciones habitadas en un estado:** índices con `\hat u_k\ne0` y, más específicamente, tríadas con transferencia instantánea no nula para el estado completo. Ocupación y transferencia no son lo mismo: un modo puede estar ocupado y no producir novedad.
- **Referencia del total:** el espacio de estados admitidos y la norma física del campo. No se supone que un número finito `N²` enumere todos los modos posibles de NS general.

Para `k\ne0` defina el proyector solenoidal `P_k=I-kk^\top/|k|²`. Para dos amplitudes vectoriales `a,b` con `p\cdot a=q\cdot b=0`, el posible acoplamiento de la pareja hacia `k=p+q` es proporcional a

\[
\boxed{\mathcal T(p,q;a,b)=P_k\big[(a\cdot q)b+(b\cdot p)a\big].}\tag{61.2}
\]

Esta contracción se obtiene del término advectivo tras agrupar las contribuciones ordenadas `(p,q)` y `(q,p)`. El factor `-i` y los factores de normalización de la base no afectan a decidir si la transferencia se anula. La magnitud `|\mathcal T|` es invariante ante una rotación conjunta de vectores, índices y marco euclídeo. En un toro periódico fijo, sólo algunas rotaciones preservan exactamente la retícula periódica; para las demás hay que rotar también el dominio.

**Nota:** la relación disponible no está «deshabitada» porque no la hayamos medido. Decimos que no está activada porque el acoplamiento calculado del estado es cero. Éste es el contrato observable, no una metáfora.

## II. Dos configuraciones físicamente distinguibles dentro de una clase exacta [T]

Sean `A,B>0`, `\nu>0`, `\theta\in[0,\pi/2]`, `x=(x,y,z)` coordenadas periódicas, y defina

\[
 s=A\sin\theta,\qquad c=A\cos\theta.\tag{61.3}
\]

Datos iniciales:

\[
\boxed{u_\theta(x,y,z,0)=\big(0,\ s\cos x,\ c\cos x+B\cos y\big).}\tag{61.4}
\]

Son campos suaves, de media cero y sin divergencia. Todos tienen idénticos índices de Fourier inicialmente ocupados: `\pm(1,0,0)` y `\pm(0,1,0)`; las magnitudes de sus amplitudes por índice son las mismas: el modo `x` tiene amplitud vectorial de norma `A/2` y el modo `y` de norma `B/2`. Por tanto, su espectro escalar inicial, su energía y su enstrofía coinciden:

\[
\boxed{E_\theta(0)=\frac14(A²+B²),\quad
H_\theta(0)=\frac14(A²+B²),}\tag{61.5}
\]

con `E=\frac12\langle|u|²\rangle`, `H=\frac12\langle|\operatorname{curl}u|²\rangle` y promedio espacial normalizado. El modo nuevo `k=(1,1,0)` está exactamente vacío inicialmente, en todas las preparaciones.

**Teorema O61-T1 (clase exacta e invariante bajo NS).** La solución de Navier–Stokes que parte de (61.4) tiene para todo tiempo finito la forma

\[
\boxed{u_\theta(t)=\big(0,\ se^{-\nu t}\cos x,\ ce^{-\nu t}\cos x+w(x,y,t)\big),}\tag{61.6}
\]

con presión constante y `w` solución de

\[
\boxed{\partial_t w+s e^{-\nu t}\cos x\,\partial_y w
=\nu(\partial_{xx}+\partial_{yy})w,\qquad w(0)=B\cos y.}\tag{61.7}
\]

**Prueba.** En esa forma `u_x=0`, `u_y` no depende de `y`, y `u_z` no depende de `z`: luego `\nabla\cdot u=0`. La única componente convectiva no nula es `u_y\partial_yu_z=s e^{-\nu t}\cos x\partial_y w` en la componente `z`. La componente `y` satisface exactamente calor unidimensional; la porción `ce^{-\nu t}\cos x` de la componente `z` también. El término no lineal restante es exclusivamente (61.7), que es una ecuación escalar de advección-difusión lineal con coeficientes suaves y acotados; tiene solución suave global. La presión puede elegirse constante. Por sustitución obtenemos una solución exacta y suave de NS 3D en esta clase. ∎

Hay dos niveles de autorreferencia formal posibles: la subfamilia `u=(0,0,w(x,y))`, que evoluciona por calor sin transferencia convectiva, y la familia ampliada `u=(0,v(x),w(x,y))`, que permanece estable como clase aunque active otros índices. **«Familia invariante» es aquí una propiedad PDE demostrada; no identificamos automáticamente esa familia con una singularidad ontológica.**

## III. Novedad en el mismo total, sin un denominador nuevo [T]

A tiempo cero:

\[
(u_\theta\cdot\nabla)u_\theta
=\big(0,0,-sB\cos x\sin y\big).\tag{61.8}
\]

Este campo no tiene divergencia, por lo que la presión no cancela su componente. Además

\[
\cos x\sin y=\tfrac12[\sin(x+y)+\sin(y-x)].\tag{61.9}
\]

De aquí:

\[
\boxed{\partial_tu_z\big|_{t=0}\supset
\frac{AB\sin\theta}{2}\sin(x+y).}\tag{61.10}
\]

**Teorema O61-T2 (mismos soportes y totales iniciales; futuros distintos).** El coeficiente de `sin(x+y)` en la derivada inicial es cero cuando `\theta=0`, y es `AB\sin\theta/2\ne0` para `0<\theta\le\pi/2`. Para `\theta=0`, en realidad no se crea ningún modo nuevo nunca: todo el campo satisface calor. Para `\theta>0`, el modo `(1,1,0)` aparece para tiempos suficientemente pequeños y positivos por continuidad diferenciable y derivada inicial no nula. ∎

Con `p=(1,0,0)`, `q=(0,1,0)`, `a=A(0,\sin\theta,\cos\theta)`, `b=B(0,0,1)` se tiene exactamente

\[
\boxed{|\mathcal T(p,q;a,b)|=AB|\sin\theta|.}\tag{61.11}
\]

**Interpretación relacional:** la totalidad de índices y la magnitud de los dos modos estaban disponibles en todas las configuraciones. La relación transversal entre los componentes del flujo decide la activación efectiva. La dirección vectorial aparece aquí como **la manera matemática en que NS expresa esa relación**; no es un postulado ontológico de dirección anterior a la unidad.

**Resultado negativo importante.** La firma compuesta sólo de `(soporte de índices, magnitudes por modo, energía, enstrofía)` **no es suficiente** para predecir incluso la aparición del modo `(1,1,0)` en esta subclase. Una normalización que solo almacene esas cantidades tampoco lo será. La información que falta ya es visible en (61.2), antes de observar el futuro.

## IV. La estela física de modos: ecuación exacta y cálculo controlado [T/E]

Como (61.7) conserva el número de onda `y=\pm1` pero mezcla armónicos en `x`, escribimos

\[
 w(x,y,t)=\operatorname{Re}\!\left(e^{iy}\sum_{m\in\mathbb Z}c_m(t)e^{imx}\right),\quad
 c_m(0)=B\delta_{m0}.\tag{61.12}
\]

La PDE es exactamente equivalente al sistema infinito:

\[
\boxed{\dot c_m=-\nu(m²+1)c_m
-\frac{is}{2}e^{-\nu t}(c_{m-1}+c_{m+1}).}\tag{61.13}
\]

El sistema es un **camino relacional de ocupación**: el índice `m` puede comunicarse con `m±1`, pero si `s=0` ese vínculo no se activa. La interconexión no obliga a poblar todo el espacio a una amplitud mínima.

Con `A=B=1`, `\nu=0.025`, `T=1.26` se integró (61.13) con `|m|\le M`, `M=6,12,24`, tolerancia estricta. Se reporta `|c_1(T)|` (amplitud compleja en la convención de (61.12), **no** peso de energía del modo en el espacio completo). Los cálculos dan:

| Configuración | `E(0)` | `H(0)` | `|c_1(T)|` | `E(T)` | `H(T)` |
|:--|--:|--:|--:|--:|--:|
| `\theta=0°` | 0.5 | 0.5 | 0 | 0.469471737 | 0.469471737 |
| `\theta=30°` | 0.5 | 0.5 | 0.281915061 | 0.468541281 | 0.512026967 |
| `\theta=90°` | 0.5 | 0.5 | 0.485866841 | 0.465782233 | 0.636721992 |

Diferencias máximas M=12→24 entre `(E,H,|c1|)` al tiempo final: menos de `4×10⁻¹⁵` en estos ensayos. El residuo algebraico del balance energético calculado a partir del sistema espectral es inferior a `6×10⁻¹⁷` para las configuraciones reportadas. **Son comprobaciones de esta clase integrable y de su truncación**, no certificación general de NS ni convergencia de O53.

El balance general sigue siendo

\[
\boxed{\frac{dE}{dt}=-2\nu H.}\tag{61.14}
\]

En el presente sistema:

\[
E(t)=\frac14\!\left(A²e^{-2\nu t}+\sum_m|c_m|²\right),\quad
H(t)=\frac14\!\left(A²e^{-2\nu t}+\sum_m(m²+1)|c_m|²\right).\tag{61.15}
\]

La transferencia a modos más finos puede aumentar `H(t)` aunque `E(t)` decrezca. La «estela» no equivale a que toda magnitud individual crezca o a que su historial no pueda cambiar.

## V. Qué puede significar «el total limita» en este contrato [T/F]

Si `e_k=|\hat u_k|²`, `Z=\sum_k e_k>0` y `w_k=e_k/Z`, entonces `\sum_k w_k=1`. Para cualquier `\varepsilon>0`:

\[
\boxed{\#\{k:w_k\ge\varepsilon\}\le\lfloor1/\varepsilon\rfloor.}\tag{61.16}
\]

**Prueba:** si hubiera más de `1/ε` modos con peso al menos `ε`, sus pesos superarían la unidad. ∎

La totalidad normalizada restringe la **cantidad de modos con un peso apreciable**, pero no obliga a que exista un número finito de modos estrictamente no nulos. Tampoco genera automáticamente un «1» indivisible en el resto ni un entero `N²` seleccionado por NS. El umbral `ε` representa una pregunta o una resolución declarada, **no** una unidad física ontológica universal.

La ocupación binaria `\hat u_k\ne0` es matemáticamente precisa, pero no robusta ante perturbaciones pequeñas: cuando `s\to0`, la transferencia inicial se aproxima continuamente a cero aunque el estado «no cero» cambie de clase. Para una ontología de novedad estable se necesitaría fijar un contrato más informativo que un test de cero numérico.

## VI. El normalizador que sí existe y el que no hemos obtenido [D/T/A]

El normalizador físico `Z(t)` permite fracciones sin dimensiones, y el espejo exterior de O45 permite expresar índices/longitudes en un marco móvil. No son la misma operación:

1. `Z(t)` — normaliza pesos modales para una pregunta espectral;
2. `N_arit` — organiza referencias racionales de O40/O58/O60, sin regla automática desde NS;
3. `N_Q` — identifica estados equivalentes para una familia de preguntas futuras, como en O45;
4. `L(t)` — cambia la escala del espejo/observador y no modifica por sí misma la solución física.

El **mismo total inicial** no selecciona una dinámica porque la transferencia de (61.11) aporta una relación independiente. La novedad puede ocurrir sin cambiar `N_arit`; el mínimo común múltiplo es insuficiente como ley de actualización.

### Traducción tentativa entre laboratorios

| En O60 (cuadrícula D₄) | En O61 (flujo NS) | Estatus |
|---|---|---|
| totalidad de posiciones | espacio de modos y tríadas físicamente posibles | comparación de contratos, no identidad |
| familia habitada | modos/transferencias activas para un estado | modelo candidato operacional |
| centro pendiente de una celda | modos no activados desde la configuración | **sin correspondencia 1↔1** |
| refinamiento `N→mN` | posible transferencia a resoluciones más finas | **no derivado** |
| ocupación sin borrar | conservación de una interfaz suficiente entre estados | **no demostrada** para NS general |
| nuevo canal dentro del total | nueva amplitud modal creada por la evolución | ejemplo exacto, ecuaciones (61.8)–(61.13) |

**No-go sobre los dos cuadrados más uno:** la ecuación `a²+b²+1=N²` se conserva como hipótesis del modelo aritmético O58–O60. No se deduce de Parseval, del balance de energía, de incompresibilidad ni de este ensayo. Una correspondencia física no puede elegirse a posteriori para forzar la igualdad.

## VII. Siguiente paso preciso: O62, volver al anillo, pero con predicción [A]

O61 ha determinado qué información omite un comparador hecho sólo de magnitudes: **la transferencia entre relaciones**. Para llevarlo al toroide de O53 proponemos:

1. Definir en la preparación del anillo una familia concreta de modos o bandas y su transferencia triádica, **antes** de simular.
2. Registrar una cantidad invariante de marco para esas transferencias (un presupuesto de activación) junto con los dos radios, la escala del espejo, y la ocupación presente.
3. Construir dos anillos con magnitudes comparables pero acoplamientos distintos; predecir cuál activa antes la banda que estaba vacía.
4. Contrastar qué conserva la referencia normalizadora entre configuraciones, sin exigir ocupación monotónica de amplitudes Fourier ni convertir el residuo cuadrático en un modo físico por definición.

Si la regla no discrimina, habrá que precisar el comparador. **Regularidad global de Navier–Stokes 3D sigue abierta.**

## VIII. Reproducción y trazabilidad

Ejecutar `python codigo/verificar_o61.py` desde este suplemento con `numpy`, `scipy`, `matplotlib`. Escribe `resultados/resumen_o61.json`, `resultados/series_o61.csv` y `graficos/o61_modo_nuevo_y_energia.png`. Las tres resoluciones modales son `M=6,12,24`; el sistema infinito de la PDE no se truncó al definir los teoremas. La numeración de controles que imprime el script corresponde a aserciones específicas agrupadas, no a validación experimental de la totalidad del programa.

**Autoría:** Le Matt Ansatz Di Ego. **Bibliografía externa:** contexto comparativo, nunca origen de las reglas ontológicas.
