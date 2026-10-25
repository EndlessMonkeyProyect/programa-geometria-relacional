# O59 — Autorreferencia de la unidad y sectores no habitados

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**Fecha:** 21 de octubre de 2026  
**Naturaleza:** formalización candidata, independiente y aditiva.  
**Secuencia:** narrativa → ontología → modelo de espejos → teoremas del modelo → puente y límites.

## 1. Narrativa y distinción ontológica [O]

La totalidad contiene una trama de relaciones admisibles; una unidad, al reflejarse, no tiene que habitar la totalidad. Se reconoce como unidad a través de la continuidad de una familia de reflexiones referidas a ella misma. Los sectores no habitados no son necesariamente relaciones imposibles: pueden no pertenecer al cierre propio de esa unidad, o pueden ser accesibles tras más reflexiones pero no haber aparecido a la profundidad observada.

La novedad puede aparecer cuando una nueva marca, un operador nuevo o una distinción contextual producen una familia no reducible a la anterior. Repetir indefinidamente la misma operación cerrada no obliga por sí solo a crear novedad.

**Precaución:** «autorreferencia» se interpreta operacionalmente como cierre de una familia de representaciones bajo reglas, no como la exigencia de que cada imagen sea un punto geométrico fijo.

## 2. Modelo exacto: cubo de espejos [D]

Sea `L>0` el lado del cubo ideal, `X=R³` el espacio de posiciones de las imágenes virtuales desplegadas, y `G_L` el grupo generado por las seis reflexiones en los planos `x_i=0`, `x_i=L`, `i∈{1,2,3}`. Una marca inicial `p=(p_1,p_2,p_3)`, con `p_i∈(0,L)`, da una órbita

\[
\mathcal O_L(p)=\{(2n_1L+\epsilon_1p_1,2n_2L+\epsilon_2p_2,2n_3L+\epsilon_3p_3):n_i\in\mathbb Z,\ \epsilon_i\in\{-1,1\}\}.
\]

Este conjunto representa **posiciones de imágenes virtuales**, no distribución de intensidad luminosa, trayectorias ópticas visibles desde cualquier observador ni estados fluidodinámicos.

Defina la «coordenada plegada» por eje

\[
\rho_L(x):=\operatorname{dist}(x,2L\mathbb Z)\in[0,L],\quad I_L(x)=\bigl(\rho_L(x_1)/L,\rho_L(x_2)/L,\rho_L(x_3)/L\bigr).
\]

La `I_L` es una firma adimensional de las posiciones bajo el contrato de reflejos fijos.

## 3. Teoremas exactos del laboratorio ideal [T]

**T1: cierre propio como órbita.** Para todo `g∈G_L`, `g O_L(p)=O_L(p)`. Las órbitas de puntos distintos son idénticas o disjuntas. Por ello una sola unidad puede ser cerrada bajo todas sus reflexiones sin habitar todas las posiciones de `X`.

**Prueba.** Una órbita es `G_L p`. La composición con un elemento de `G_L` sólo permuta los elementos de la órbita. Si dos órbitas comparten una imagen, las acciones inversas identifican ambos puntos en la misma órbita. ∎

**T2: firma normalizada exacta.** `q∈O_L(p)` si y sólo si `I_L(q)=I_L(p)`. El grupo generado por reflejos `s_0(x)=-x` y `s_L(x)=2L-x` actúa en un eje por `x↦±x+2nL`; dos números pertenecen a la misma órbita si y sólo si tienen igual distancia a `2L Z`. Cada eje se factoriza por separado. ∎

**T3: escala exterior y ausencia de novedad automática.** Para todo `k>0`, `I_{kL}(kq)=I_L(q)`. Por tanto un cambio uniforme de escala de la escena completa conserva la firma. No introduce por sí una relación nueva.

**T4: tres clases de sectores respecto de una profundidad finita `m`.** Si `O_L^{(m)}(p)` contiene las imágenes alcanzadas mediante a lo sumo `m` reflexiones, entonces:

- `O_L^{(m)}(p)`: imágenes ya alcanzadas a la profundidad del laboratorio;
- `O_L(p)\setminus O_L^{(m)}(p)`: imágenes del mismo cierre aún no alcanzadas;
- `X\setminus O_L(p)`: posiciones que no son imágenes de esa unidad bajo las reglas fijas.

Estas tres clases no equivalen respectivamente a «resuelto / azar / imposible» en física: son categorías dentro del contrato geométrico.

**T5: novedad estructural por cambio de contrato.** Repetir las mismas reflexiones jamás permite alcanzar un punto externo a `O_L(p)`. Para habitarlo hay que introducir una marca en otra órbita, modificar/ampliar los operadores admitidos, o refinar qué observables identifican estados. Un nuevo color o etiqueta en una posición ya alcanzada puede ser novedad *semántica*, pero no una nueva órbita espacial.

## 4. Ejemplo discriminante verificable [T]

En un eje con `L=1`, parta de `p=1/4`.

- La reflexión en `x=1` da `7/4`, que pertenece a la misma órbita y tiene firma `1/4`: es una imagen aún pendiente si el laboratorio sólo había contado profundidad cero.
- El punto `3/4` no pertenece a la órbita: su firma es `3/4`.
- Si se agrega una marca inicial nueva en `3/4`, aparece otra órbita sin que la primera pierda cierre.
- Si en vez de cambiar la marca se introduce un espejo adicional en `x=3/4`, éste refleja `1/4` a `5/4`, cuya firma original es `3/4`; al ampliar los operadores, la antigua partición por órbitas deja de ser válida.

Así distinguimos **agotamiento de una referencia** de **novedad por relación adicional**. No es necesario crear una cuarta dimensión.

## 5. Enlace con el normalizador y la estela de escalas [H/T]

La firma `I_L` es una normalización geométrica exacta. Al transportar escena completa `(L,p)↦(kL,kp)` se conserva; ese transporte es una analogía controlada del traslado del múltiplo que normalizó la configuración anterior.

**No identificar sin prueba:** `I_L` con el normalizador aritmético `N`, con la condición cuadrática `a²+b²+1=N²`, con la «unidad de resto» o con una cantidad dinámica de Navier–Stokes. Ninguna de esas correspondencias se deriva de la acción de espejos.

En una secuencia de marcos `\mathcal C_n`, la «estela» se puede registrar como una familia de firmas, órbitas y operadores `\{(I_n,\mathcal O_n,G_n)\}_n`. El cambio real se registra sólo si una transición altera clases de equivalencia o incorpora un observable independiente; el cambio uniforme de tamaño sólo cambia coordenadas.

## 6. Contrato de avance hacia O60 [ABIERTO]

1. Definir operacionalmente qué cuenta como unidad/reflejo/relación en el modelo de vorticidad sin confundirlo con una posición de imagen virtual.
2. Proponer una regla de normalizador heredado que indique qué clasificaciones permanecen y cuáles se refinan bajo novedad.
3. Determinar si existe una firma *de un flujo* suficiente para una pregunta dinámica dada. Un mero cierre de órbita de espejos no equivale a cierre predictivo de Navier–Stokes.
4. Conservar separados los contratos aritméticos `(N−1)(N+1)+1=N²` y `a²+b²+1=N²` hasta que se acredite su puente.

**Resultado:** el laboratorio muestra exactamente cómo una unidad puede reflejarse de forma cerrada sin agotar el espacio de posibilidades; no demuestra por sí la ontología universal, el criterio físico de persistencia del vórtice, P=NP ni regularidad global tridimensional.
