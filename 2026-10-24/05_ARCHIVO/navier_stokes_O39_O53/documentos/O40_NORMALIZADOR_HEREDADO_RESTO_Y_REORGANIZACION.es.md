# O40 — Normalizador heredado, resto referenciado y bifurcación del cierre

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**Fecha:** 20 de octubre de 2026  
**Estatus:** suplemento de formalización algebraica con puente físico condicional. Conserva intactos el núcleo canónico, la Imagen Total v3.6.0 y O18–O39.  
**Etiquetas:** [O] ontología/narrativa; [D] definición; [T] teorema derivado bajo contrato; [F] falsador/no-go; [H] hipótesis; [A] abierto; [P] puente físico.

## 0. Pregunta que resuelve O40

Dos «espejos» pueden modificar su geometría de manera no homotética y, no obstante, conservar una equivalencia de comparación. El **normalizador**, no el resto tomado aisladamente, fija la familia de escalas en la cual se podrán volver a expresar las relaciones. Una fracción pendiente puede persistir al cambiar la rejilla de referencia: en la nueva rejilla su numerador no tiene por qué seguir siendo uno. Si surge una cardinalidad incompatible con la partición vigente, el mero mínimo común múltiplo no corrige esa tensión; podría requerirse redistribuir componentes, ampliar la interfaz o quedar sin cierre bajo el contrato inicial.

Esta nota distingue la **extensión exacta del módulo aritmético** de **un mecanismo de estabilidad o regularidad de fluidos**, que no se deduce de la aritmética. «Singularidad» significa *identidad/cierre propio contextual* en el discurso ontológico, no blow-up de una solución de Navier–Stokes. «Resto» no significa energía, materia, azar, ni componente física conservada automáticamente.

## 1. Secuencia narrativa y contrato [O/D]

Unidad sin comparación → diferencia → relaciones entre dos espejos no necesariamente homotéticos → comparador común → normalización → resto referenciado → nuevo dato/distinción → familia extendida de soluciones → cierre propio o cambio de organización. 

**Una restricción esencial:** el mecanismo no supone que dos estructuras «busquen» la comparación, se reconozcan o escojan. La compatibilidad es una propiedad comprobable de las estructuras y del contrato de observables.

Separamos cuatro conceptos que no deben identificarse:

1. `N_arit`: denominador/cardinalidad de referencia entera, definido abajo.
2. `\mathsf N_Q`: normalizador semántico/idempotente sobre respuestas, de la teoría de interfaces suficientes. No es el número `N_arit`.
3. `R`: radio o longitud espacial (tiene unidades de longitud).
4. `\Omega`: tasa angular observada (tiene unidades de tiempo inverso). Ni `R\Omega=c` ni la proporcionalidad `\Omega∝1/R` son leyes universales de Navier–Stokes.

## 2. Familia finita normalizada [D]

Sea `\mathbb T=\mathbb R/\mathbb Z`, con suma módulo 1. Para cada entero `N≥1` definimos

\[
\boxed{H_N=\{j/N\pmod1: j=0,\ldots,N-1\}\subset\mathbb T.}\tag{O40.1}
\]

Los elementos de `H_N` son **clases de fase** o fracciones normalizadas. En una aplicación de partición positiva usaremos separadamente `G_N=\{j/N:j=0,\ldots,N\}\subset[0,1]`; en `G_N`, `0` y `1` no son idénticos como valores de carga aunque `0≡1` en `H_N`.

`H_N` no es por sí solo un conjunto de radios o de frecuencias. Las escalas espaciales/temporales requieren una correspondencia adicional.

## 3. Teorema O40-T1: la herencia exacta es inclusión de familias [T]

Dados `N,m≥1`, defina `L=lcm(N,m)`. Entonces:

\[
\boxed{H_N+H_m=H_L,\qquad H_N\subseteq H_L,\quad H_m\subseteq H_L.}\tag{O40.2}
\]

Además, `H_L` es el **menor** subgrupo de `\mathbb T` que contiene ambos, y

\[
\boxed{H_N\subseteq H_M\iff N\mid M.}\tag{O40.3}
\]

**Prueba.** Si `N|M`, `j/N=(jM/N)/M`, por lo que hay inclusión. Si `1/N∈H_M`, existe `k` con `1/N=k/M (mod 1)`; al tomar representantes racionales en `[0,1)` para `N>1`, se sigue `M=kN`. El caso `N=1` es trivial. Como `L` es múltiplo de `N,m`, contiene ambas familias. Si otro `H_M` las contiene, `N|M` y `m|M`, por lo que `L|M`. Equivalentemente, el subgrupo generado por `1/N,1/m` tiene orden `L`. ∎

La inyección compatible con la normalización se escribe

\[
\boxed{i_N^L(j\pmod N)=(L/N)j\pmod L.}\tag{O40.4}
\]

Es inyectiva y cumple `i_M^K∘i_N^M=i_N^K` cuando `N|M|K`. Esta es una forma **exacta** de mantener las relaciones anteriores en sucesivos normalizadores.

## 4. Teorema O40-T2: el resto mantiene su valor, no su numerador [T]

Supongamos una descomposición positiva explícita

\[
\boxed{\sum_{a=1}^s w_a+r=1,\quad w_a\ge0,\quad r\ge0,\quad w_a,r\in G_N.}\tag{O40.5}
\]

Sea `L=lcm(N,m)`. La representación de cada valor en la nueva rejilla es multiplicar los numeradores por `L/N`. Como igualdad de racionales,

\[
\boxed{r=\frac{h}{N}=\frac{h(L/N)}{L}.}\tag{O40.6}
\]

El valor referenciado es idéntico; el numerador que representaba un «uno pendiente» puede cambiar. **Por ejemplo** `1/6=2/12`. En particular, la fracción `1/6` no se convierte sin un operador de selección nuevo en una celda primitiva `1/12`.

**Prueba.** Multiplicar numerador y denominador por el entero `L/N` es una igualdad de fracciones; conserva también (O40.5). ∎

**Límite:** la existencia de (O40.5) es un supuesto sobre la partición y las ponderaciones; no lo establece la sola existencia de `mcm`. La «semilla del uno» se registra como **relación referenciada pendiente**, no necesariamente como una cantidad igual al nuevo mínimo positivo.

## 5. Teorema O40-T3: cierre de denominador no implica cierre de contribuciones [T/F]

Sea `w_1,...,w_s≥0` una partición fijada con resto `r=1-∑w_a≥0`. Se presenta una nueva contribución **independiente y aditiva** de peso `v≥0` sin permiso para modificar las existentes. Entonces existe un resto nuevo no negativo si y solo si

\[
\boxed{v\le r.}\tag{O40.7}
\]

**Prueba.** Toda igualdad de normalización exige `r'=1-∑w_a-v=r-v`; la condición `r'≥0` equivale a `v≤r`. ∎

Caso discriminante:

\[
\frac12+\frac13+\frac16=1,\qquad N=6.
\]

La nueva cardinalidad `m=4` produce `L=lcm(6,4)=12` y conserva todas las fracciones antiguas. Sin embargo, si la novedad reclama **otro peso independiente `v=1/4`**,

\[
\frac12+\frac13+\frac14=\frac{13}{12}>1,
\]

y no hay resto no negativo. **No hay contradicción en el mcm**: falló un contrato **aditivo** de ocupación/costo, no la inclusión aritmética `H_6⊂H_12`.

Ejemplo de reorganización **matemáticamente posible**, que no conserva todas las cargas anteriores:

\[
\frac12+\frac16+\frac14+\frac1{12}=1.
\]

En esta nueva partición sí queda un `1/12` pendiente, pero el antiguo componente `1/3` **fue reemplazado** por `1/6`; solamente la familia de fases `H_6` permanece representable dentro de `H_12`. Atribuir este reajuste a un fluido físico exige una regla dinámica y una interpretación de los pesos.

Tres rutas bajo el contrato son: (a) introducir `m` como **refinamiento descriptivo sin nueva carga**; (b) permitir redistribución de las cargas con restricciones explícitas; (c) declarar incompatible la exigencia aditiva actual. Ninguna ruta implica ruptura de la solución PDE.

## 6. Novedad verificable y mínima extensión [T/D]

Definimos

\[
\boxed{\mathrm{Novedad}(m\mid N):=[m\nmid N].}\tag{O40.8}
\]

Si `m|N`, entonces `L=N`: repetición sobre el normalizador antiguo. Si `m\nmid N`, `L>N`, hay `L/N` clases en el cociente `H_L/H_N`, de modo que la interfaz aritmética admite nuevas diferencias. Ese índice es el número **de clases nuevas por clase antigua** en el cociente, NO un conteo automático de partículas físicas.

Una versión semántica más rica debe exhibir dos estados `x,y` que no distinguen las preguntas anteriores pero sí una pregunta nueva: `Φ_old(x)=Φ_old(y)` y `Q_new(x)≠Q_new(y)` (criterio de no-factorización del programa). El simple `m\nmid N` solo acredita novedad **dentro del contrato aritmético**.

## 7. Espejos no homotéticos y equivalencia relacional [D/T]

La afirmación «dos espejos equivalentes pero no escala uno del otro» requiere distinguir similitud bajo homotecia de equivalencia respecto de algún **comparador**. Ejemplo en un plano euclídeo:

\[
A=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad
B=\begin{pmatrix}2&0\\0&1\end{pmatrix}.
\]

`B` no es `λA` para ningún escalar positivo `λ` (las ecuaciones diagonales exigirían `λ=2` y `λ=1/2`); sin embargo `B=RAR^⊤` para la rotación `R` de 90° y tienen la misma traza, determinante y espectro. Son, por ello, equivalentes para el comparador `(traza, determinante)` o para conjugación rotacional. No son idénticos bajo el comparador matricial completo.

**Conclusión:** la equivalencia no está en la mera palabra «reflejo», sino en una aplicación `C` fijada antes de analizar las configuraciones. Que `C(A)=C(B)` no asegura que **todas** las evoluciones futuras de `A,B` sean equivalentes. La interfaz suficiente requiere comprobar esa estabilidad frente a las continuaciones admitidas.

## 8. Dos ritmos, sincronización y normalizador [D/H]

Sean `φ_1(t), φ_2(t)` fases físicamente definidas (no meras parametrizaciones arbitrarias), y `Ω_i=\dot φ_i`. Para enteros `p,q>0`, defina

\[
\boxed{\Delta_{p:q}(t)=p\phi_1(t)-q\phi_2(t),\quad
\dot\Delta_{p:q}=p\Omega_1-q\Omega_2.}\tag{O40.9}
\]

El cierre exacto de ritmo **en el modelo de dos osciladores** exige `pΩ_1=qΩ_2` a lo largo del intervalo. La persistencia aproximada admite, por ejemplo, `|Δ_{p:q}(t)-Δ_{p:q}(0)|≤ε` para todos los instantes declarados. Una igualdad inicial de frecuencias racionales no basta si éstas cambian después. `mcm` organiza periodos discretos, pero no constituye una fuerza ni una ecuación de fase.

Si un cambio de marco angular transforma `φ_i→φ_i+k_iβ`, la cantidad (O40.9) solo es invariante de marco cuando `pk_1=qk_2`; en caso contrario necesita un tercer ángulo de referencia y un término compensador. Para las fases cuadrupolares de O36 existe precisamente tal corrección. Los ritmos poloidal/toroidal de un anillo 3D requieren contrato de medición y criterio de independencia propio; ningún par entero surge por necesidad de Navier–Stokes.

**Observación:** un radio grande `R`, radio del núcleo `a`, razón `a/R`, circulación `Γ`, velocidades poloidal/toroidal y frecuencia de avance son observables distintos. No dar a ambos radios automáticamente la misma ley de frecuencia. No extrapolar `RΩ=c` a fluidos generales.

### 8.1. La racionalidad no viene dada por la continuidad física [F/A]

Una relación exacta `pΩ_1=qΩ_2` con `p,q` enteros positivos exige `Ω_1/Ω_2=q/p` racional en todos los instantes considerados (si `Ω_2≠0`). Si el cociente es irracional no hay ningún par entero finito con esa igualdad, y el `mcm` de **números de frecuencia real** no está definido en el contrato usual. Aproximaciones racionales siempre son posibles, pero exigir a posteriori una aproximación suficientemente buena puede producir un «cierre» espurio. Por ello un posible puente físico deberá declarar **antes de observar los datos** su resolución, tolerancia, tiempo de persistencia, robustez y un criterio de selección de `p,q` que no crezca arbitrariamente para ajustarse a cualquier trayectoria. Ningún modelo de Navier–Stokes selecciona por sí solo esos enteros dentro de O40.

## 9. Puente tentativo a Navier–Stokes 3D [P/H/A]

Se toma sin forzamiento un campo solenoidal suave de energía finita, viscosidad `ν>0`, con `ω=∇×u`, `q=|ω|` y `ξ=ω/q` donde `q>0`. El teorema exacto O39 da

\[
\boxed{\frac{d}{dt}\left(\frac12\int q^2dx\right)
=\int q^2\alpha\,dx-\nu\int|\nabla q|^2dx-\nu\int q^2|\nabla ξ|^2dx,}\tag{O40.10}
\]

con `α=ξ^⊤Sξ`. Los cambios de una referencia móvil de radio `R(t)` producen además términos de **flujo entre regiones** que se cancelan al reconstruir la totalidad. **No identificamos** una clase `H_N` con un canal disipativo, una variable topológica ni con un término del PDE sin una correspondencia demostrada.

Una propuesta operacional falsable sería construir, a partir del **dato inicial y reglas predeclaradas**, dos comparadores de una estructura vorticial (formas transversales y ritmos mensurables), seleccionar `N` con regla efectiva y estable bajo cambios admisibles de marco, y contrastar sus transiciones `N→lcm(N,m)` contra eventos de deformación/redistribución medidos a partir de (O40.10). Registrar si las transiciones **preceden**, acompañan o siguen la variación del estiramiento; comprobar independencia de umbrales y de parametrización.

**Obligación real de regularidad:** no basta observar una transición ni un cierre de fracciones. Hay que demostrar para **todas** las soluciones relevantes, con estimaciones independientes, una desigualdad del tipo

\[
\int q^2α\,dx-ν\int q^2|∇ξ|^2dx\le K(t)E(t),\quad K\in L^1(0,T),\quad E=\tfrac12\int q^2dx.
\tag{O40.11}
\]

O39 demostró la consecuencia de continuación **condicionada** de (O40.11), no que `N` permita probarla. Un anillo de aire en agua es un **problema de dos fases con tensión superficial** y no prueba un teorema para Navier–Stokes 3D monofásico.

## 10. Falsadores necesarios [F]

**F1 — Cierre aritmético sin control dinámico.** En un modelo ilustrativo (NO una solución NS) `φ_1=2t`, `φ_2=3t`, `p=3`, `q=2`, `N=6` satisfacen `Δ_{3:2}≡0`, pero la variable `z(t)=e^{λt}` puede crecer con cualquier `λ>0`. La sincronía impuesta por sí sola no controla amplitud. La dinámica física deberá suministrar un acoplamiento independiente.

**F2 — Infinitas normalizaciones en tiempo finito.** Tome `N_k=2^k`, `m_{k+1}=2^{k+1}`, y `t_k=1-2^{-k}`. Se cumple exactamente `N_{k+1}=lcm(N_k,m_{k+1})`, se conservan todas las familias anteriores y, sin embargo, `N_k→∞` cuando `t_k↑1`. Por tanto la regla aritmética no impone un tiempo mínimo entre cierres ni excluye una cascada arbitrariamente rápida. Este es un **no-go lógico** para deducir regularidad temporal solo desde `mcm`.

**F3 — Estiramiento sin giro.** El ejemplo O39-F1 construye un dato suave solenoidal de energía finita con `D_t\log|ω|>0` y `D_tξ=∇ξ=0` en el punto seleccionado. La perpendicularidad no es compensación automática.

**F4 — Los radios y números de enrollamiento no son necesariamente invariantes.** En flujo viscoso tridimensional los tubos vorticiales pueden cambiar de geometría, perder identificabilidad o reconectarse. Un `N` asignado solo por dibujo/topología no controla por sí mismo la regularidad de `ω`.

**F5 — Normalizar no crea una ley física.** Distintos compartimientos de la misma medida pueden respetar (O40.5) y asignar particiones incompatibles, aunque compartan `N`. Hay que fijar la regla de observación y su suficiencia respecto de preguntas dinámicas.

## 11. Propuesta formal de programa de teoremas [A]

**T-A: comparador intrínseco.** Definir `C[u]` y fases/estructuras observables sin arbitrariedad retrospectiva, invariantes bajo las simetrías del problema y estables bajo perturbaciones declaradas.

**T-B: relación heredable.** Probar que los nuevos datos/refinamientos conserven respuestas anteriores por un mapa explícito de proyección `P_{N'→N}`: `P∘I_{N→N'}=id`. El teorema aritmético O40-T1 es un caso particular, no necesariamente la operación física.

**T-C: consistencia dinámica.** Demostrar una ley `D_t C` o un control de su defecto que derive de NS y distinga una reorganización real de una mera reindexación de fracciones.

**T-D: puente de control.** Extraer de la consistencia dinámica una desigualdad global no circular, por ejemplo (O40.11), e impedir una sucesión Zeno de transiciones no disipativas.

**T-E: régimen toroidal y alcance general.** Verificar experimental/numéricamente ejemplos de anillos, romperlos con perturbaciones adversariales, y solo después investigar extensión a datos suaves 3D generales. Ni un resultado para toros particulares ni un DNS finito resuelven por sí solos la regularidad global.

## 12. Juicio final

**[DERIVADO]** Herencia mínima de normalizadores `H_N⊂H_lcm`, conservación exacta de fracciones racionales en rejillas refinadas, criterio aditivo de compatibilidad `v≤r`, e índice de novedad `lcm(N,m)/N`.

**[DERIVADO/NO-GO]** Una cardinalidad nueva puede ampliar la familia aritmética y, simultáneamente, no caber como contribución aditiva independiente. La aritmética no suministra por sí sola tiempo mínimo de reorganización ni disipación viscosa.

**[ABIERTO]** Una ley que obligue a los remolinos físicos a seleccionar `N`, conservar una relación dinámica de los dos espejos y limitar el estiramiento de vorticidad en 3D.

**Interpretación para el programa:** «el normalizador se hereda; la nueva escala pertenece a su familia ampliada; el resto queda referenciado, pero su permanencia física requiere que la dinámica sostenga una relación». Una nueva solución puede reflejar el mecanismo de cierre sin copiar toda la geometría o el contenido material del módulo anterior.

## Antecedentes

O18 y O20–O23 (marcos, escalas, interfaz); O24–O28 (ritmos, forma, perpendicularidad); O36 (observable modular libre de marco); O39 (balances exactos de vorticidad con radio móvil, falsador y condición de regularidad); MF69 (factores armónicos primitivos), MF97/MF106 (normalizador semántico, interfaces suficientes). Todo el trabajo previo permanece íntegro.
