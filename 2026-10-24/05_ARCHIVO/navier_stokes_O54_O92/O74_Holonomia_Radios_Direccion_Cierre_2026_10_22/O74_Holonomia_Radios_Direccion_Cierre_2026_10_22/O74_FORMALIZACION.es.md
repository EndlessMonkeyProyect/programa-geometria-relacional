# O74 — Holonomía del cierre, radios variables y separación de las libertades

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**22 de octubre de 2026 · Suplemento autónomo y aditivo O72–O73**  
**Estado:** proposiciones exactas de un modelo de enlaces `[D]`; dos ejemplos de soluciones exactas de Navier–Stokes `[D-NS]`; contraejemplos de suficiencia `[T]`; puente ontológico y físico `[H]`. **No resuelve regularidad global de Navier–Stokes 3D.**

## 0. Del lenguaje a la hipótesis

[N] Cuatro cápsulas pueden conservar cada una su cierre propio. La proyección de la configuración tetraédrica a un circuito plano no destruye sus relaciones: escoge las cuatro periféricas como condiciones **activas** y deja dos diagonales disponibles, no necesariamente habitadas. La diferencia de giros puede coincidir alrededor de la totalidad del circuito, con una libertad de ejecución. Esa coincidencia no implica por sí sola que la geometría ni las partículas permanezcan fijas.

[O] La referencia normalizadora no es energía. El cambio de radios es absorbible si las relaciones que componen el circuito retornan a su referencia. **La normalización de la coincidencia entre enlaces y la normalización del conjunto no deben identificarse automáticamente**: que un producto real regrese a 1 no demuestra que exista un múltiplo entero que describa una repetición temporal completa. La orientación, la fase y la información que el observador plano no reconstruye se conservan como distinciones. La singularidad ontológica no significa una singularidad de la solución diferencial.

**Pregunta:** ¿Cuál es la condición matemática mínima para que cuatro contactos de giro compartan movimiento no nulo al cambiar sus radios? ¿Basta esa condición para evitar que el anillo se degenere? ¿La impone Navier–Stokes?

## 1. Proposición O74.1 — Cierre de contactos no necesariamente idénticos [D]

Sean cuatro variables angulares con signo `ω_i` y cuatro enlaces consecutivos `i→i+1` (índices módulo 4). En el enlace `i`, las distancias **efectivas de contacto** de los dos giros son `a_i>0` y `b_i>0`. Modelamos un contacto de engrane exterior sin deslizamiento mediante

\[
 a_i\omega_i+b_i\omega_{i+1}=0.\tag{74.1}
\]

**Atención:** `a_i,b_i` son brazos del **enlace**, por lo que un nodo puede tener brazos distintos según cuál de sus dos vecinos toca. No son necesariamente los radios geométricos `R,r` del anillo vorticial.

Por sustituciones sucesivas,

\[
 \omega_5=(-1)^4\prod_{i=1}^4\frac{a_i}{b_i}\;\omega_1
 =H\omega_1,\quad H:=\prod_{i=1}^4 \frac{a_i}{b_i}>0.\tag{74.2}
\]

Como `ω_5=ω_1` corresponde al mismo primer nodo, el sistema de cuatro enlaces tiene una solución **no nula** si y solo si

\[
 \boxed{H=1.}\tag{74.3}
\]

Cuando `H=1`, las cuatro condiciones dejan **exactamente un grado de libertad escalar**, pues cada velocidad está determinada por `ω_1`. Si `H≠1`, sólo se admite la solución de velocidades nulas bajo las cuatro condiciones ideales **simultáneas**. Esto no significa que un dispositivo real tenga que inmovilizarse: podría patinar, perder contacto o deformar las condiciones, fenómenos no descritos por (74.1).

Para un circuito de `n` contactos exteriores, `ω_{n+1}=(-1)^n H_nω_1`. Como `H_n>0`, un ciclo **impar** no admite giro no nulo con esa regla, mientras un ciclo **par** necesita adicionalmente `H_n=1`. La paridad habilita el cierre, pero no lo garantiza con contactos asimétricos.

## 2. Proposición O74.2 — Radios cambiantes, normalización telescópica [D]

Si cada nodo ofrece **el mismo radio efectivo** `r_i(t)>0` a sus dos vecinos, podemos poner

\[
 a_i(t)=r_i(t),\qquad b_i(t)=r_{i+1}(t).
\]

Entonces, para cualquier elección de radios positivos,

\[
 H(t)=\frac{r_1}{r_2}\frac{r_2}{r_3}\frac{r_3}{r_4}\frac{r_4}{r_1}=1
\]

y las velocidades admisibles son

\[
 \boxed{\omega_i(t)=\frac{(-1)^{i-1}s(t)}{r_i(t)}}.\tag{74.4}
\]

Ésta es una **compatibilidad cinemática instantánea** para cualquier función `s(t)`. No hemos demostrado que la dinámica determine ese `s`, que las cápsulas permanezcan en contacto al modificar radios, ni que se preserve el número entero de vueltas entre los nodos.

Si cada lado usa brazos diferentes, por ejemplo `a_i=c_i r_i`, `b_i=d_i r_{i+1}`, entonces

\[
 \boxed{H(t)=\prod_{i=1}^4\frac{c_i(t)}{d_i(t)}}.\tag{74.5}
\]

En particular, si una relación aumenta en 10 % sin compensación, `H=1,1` y el sistema de **cuatro contactos exactos** ya no tiene un giro compartido no nulo. Una compensación multiplicativa en otro enlace restaura `H=1`. Esto da un significado matemático preciso a «absorber un cambio de radio» para este modelo.

Si `H(t)>0` es diferenciable y `H(0)=1`, mantener el cierre durante un intervalo requiere

\[
 \boxed{\frac{d}{dt}\log H(t)=\sum_i\left(\frac{\dot a_i}{a_i}-\frac{\dot b_i}{b_i}\right)=0\quad\text{en todo ese intervalo}.}\tag{74.6}
\]

La ecuación no es una ley de conservación obtenida de Navier–Stokes; es la condición **que tendría que cumplir** la dinámica si el contacto ideal permaneciera realizado.

### Qué significa «múltiplo» y qué todavía no significa

El cierre real `H=1` no obliga a una repetición simultánea en un número entero de vueltas. Para velocidades **constantes**, una recurrencia exacta de las fases `θ_i mod 2π` requiere que todas las razones `ω_i/ω_j` entre frecuencias no nulas sean racionales. Ejemplos:

- Radios `(1,2,1,2)` y `s=1`: velocidades `(1,-1/2,1,-1/2)`. Regresan simultáneamente después de `T=4π`.
- Radios `(1,√2,1,√2)` y `s=1`: velocidades `(1,-1/√2,1,-1/√2)`. Cierran los cuatro **contactos**, pero no existe tiempo positivo `T` de repetición exacta de todas las fases.

Por tanto, **cierre de velocidades**, **sincronización de fases** y **múltiplo entero de repetición** son tres condiciones diferentes. Si el múltiplo ontológico tiene que ser entero, falta una regla que lo derive de la física; no debe identificarse sin prueba con `H`.

### Obstrucción adicional: el cierre no acota la frecuencia [T]

El contraejemplo más directo usa `r_i(t)=(T-t)\bar r_i` para `0≤t<T`, con `\bar r_i>0` fijos y `s(t)=1`. Por (74.4),

\[
 H(t)\equiv1,\qquad |\omega_i(t)|=\frac{1}{(T-t)\bar r_i}\xrightarrow[t\uparrow T]{}\infty.\tag{74.4a}
\]

Por tanto, **una referencia que cierra exactamente en todo instante puede coexistir con frecuencias no acotadas en tiempo finito**. Esta construcción es un sistema cinemático prescrito, **no una solución de Navier–Stokes**, y no demuestra que tal divergencia sea físicamente posible en un vórtice. Refuta únicamente que `H=1` implique una cota dinámica por sí solo. Hay que derivar una restricción de evolución adicional.

## 3. Proposición O74.3 — Libertad geométrica y fallo de no-reintegración [T]

El modelo O72 del rombo articulado de lado `ℓ` puede representarse como

\[
 X_1=(0,0),\ X_2=(\ell,0),\ X_3=(\ell+\ell\cos\varphi,\ell\sin\varphi),\ X_4=(\ell\cos\varphi,\ell\sin\varphi).
\]

Las cuatro longitudes periféricas son `ℓ`, y el área orientada satisface

\[
 \boxed{A_z=\ell^2\sin\varphi}.\tag{74.7}
\]

Las dos diagonales miden

\[
 \boxed{d_{13}=2\ell\cos(\varphi/2),\quad d_{24}=2\ell\sin(\varphi/2)}.\tag{74.8}
\]

Mientras `0<φ<π`, el circuito tiene área positiva. Al aproximarse a `φ→0`, `d24→0`; al aproximarse a `φ→π`, `d13→0`. En ambos casos los enlaces periféricos **conservan su longitud**. Si las cápsulas tienen radio material `a_c<ℓ/2`, el modelo de discos excluyentes requeriría, al menos, evitar que `d13` o `d24` caigan bajo `2a_c`. Esto equivale a

\[
 \boxed{2\arcsin(a_c/\ell)\le\varphi\le\pi-2\arcsin(a_c/\ell)}.\tag{74.9}
\]

Los contactos periféricos exigen condiciones físicas adicionales; aquí sólo comprobamos el criterio geométrico de no solapamiento entre vértices opuestos. En el modelo de O74.2 podemos mantener `H=1` para **todos** los valores de `φ`, pues las condiciones de fase no contienen `φ`. Por tanto, **holonomía nula (H=1) no implica separación geométrica ni área mínima**. El modelo idealizado con restricción de giro y bisagras no constituye un sistema de engranajes sólidos físicamente realizable en todas las formas dibujadas; es una demostración de la insuficiencia lógica de imponer sólo esas condiciones.

La **dirección normal orientada** puede distinguir `+e_z` y `−e_z` sólo cuando `A_z≠0`, y requiere un orden de recorrido; no puede derivarse únicamente del patrón alternado de giros. Deformar el anillo y cambiar el sentido de los giros son dos libertades inicialmente independientes.

## 4. Puente real con Navier–Stokes I — Flujo afín que comprime un anillo material [D-NS]

Una clase de soluciones exactas de Navier–Stokes incomprensible en todo `R³` es

\[
 u(x,y,z)=(-\lambda x,-\lambda y,2\lambda z),\quad
 p(x,y,z)=-\frac{\rho\lambda^2}{2}(x^2+y^2+4z^2),\quad \lambda>0.\tag{74.10}
\]

Comprobación: `div u=0`, `Δu=0`, `u·∇u=(λ²x,λ²y,4λ²z)` y `−∇p/ρ` es ese mismo vector. Como `∂_t u=0`, satisface las ecuaciones para cualquier viscosidad `ν>0`.

El flujo material es

\[
 \Phi_t(x,y,z)=(e^{-\lambda t}x,e^{-\lambda t}y,e^{2\lambda t}z),\quad\det D\Phi_t=1.\tag{74.11}
\]

Un cuadrado material de lado `ℓ` situado en `z=0` conserva su orientación pero su área evoluciona como

\[
 \boxed{A(t)=A(0)e^{-2\lambda t}}.\tag{74.12}
\]

Su volumen ambiental puede permanecer incompresible porque el eje `z` se dilata. **El área tiende a cero sólo cuando `t→∞`; no desaparece en tiempo finito.** El campo es suave para todo `t` y su vorticidad es **idénticamente cero**. Por tanto, ni la contracción del anillo material ni la conservación de orientación constituyen por sí mismas una prueba de una singularidad de vorticidad.

**Limitación crítica:** la solución afín crece linealmente con `|x|` y **no tiene energía cinética total finita en `R³`**; es un test exacto local/geométrico, no un ejemplo admitido como dato inicial de energía finita en el problema de Clay.

## 5. Puente real con Navier–Stokes II — La circulación de un anillo material puede cambiar por viscosidad [D-NS]

Para un lazo **material** `C(t)` transportado por una solución suave incomprensible sin fuerzas no conservativas externas, la forma viscosa del teorema de Kelvin es

\[
 \boxed{\frac{d}{dt}\oint_{C(t)}u\cdot dX=\nu\oint_{C(t)}\Delta u\cdot dX}.\tag{74.13}
\]

No equivale a conservación en general. Un test exacto, periódico, sin presión variable ni no linealidad advectiva es

\[
 \boxed{u(x,y,z,t)=U_0e^{-\nu k^2t}\sin(ky)e_x.}\tag{74.14}
\]

Es una solución de Navier–Stokes en el toro periódico apropiado: `div u=0`, `(u·∇)u=0`, `u_t=νΔu`. Tomemos inicialmente un rectángulo material de longitud `L` en `x`, comprendido entre `y=0` y `y=π/(2k)`, con orientación positiva en el plano `xy`. Sus puntos cambian `x` por cizalla pero mantienen `y`; mediante Stokes o integración directa,

\[
 \boxed{\Gamma_C(t)=-L U_0e^{-\nu k^2t},\quad\dot\Gamma_C=-\nu k^2\Gamma_C}.\tag{74.15}
\]

La circulación disminuye suavemente en magnitud mientras el fluido sigue siendo regular. La continuidad de una identidad colectiva **no puede postular la conservación de toda circulación material viscosa**. Este caso no es un toroide vorticial; es un falsador sencillo de una inferencia que resultaría incorrecta.

## 6. Qué sí sabemos de la separación de partículas bajo Navier–Stokes [D]

Mientras exista una velocidad clásica Lipschitz espacial y dos partículas sigan trayectorias `X(t),Y(t)` en una región donde `L(t)=||∇u(t)||∞` sea finito e integrable, se cumple

\[
 \boxed{|X(t)-Y(t)|\ge|X(0)-Y(0)|\exp\!\left(-\int_0^t L(s)\,ds\right).}\tag{74.16}
\]

Esto deriva de la ecuación de trayectorias y Grönwall. **No demuestra regularidad global de Navier–Stokes**: asegurar `∫_0^T||∇u||∞<∞` sin presuponer continuidad suave es precisamente parte de la dificultad. El resultado tampoco garantiza que una estructura identificada como vórtice conserve su topología como conjunto definido por umbrales de vorticidad: ése no es un conjunto de partículas necesariamente material.

## 7. Lectura de la caja de espejos y regla de siguiente prueba [H/F]

Lo que O74 demuestra del modelo abstracto:

1. **Paridad:** con inversión de signo en cada enlace, el ciclo par permite giro no nulo; el impar no.
2. **Holonomía:** aun con cuatro enlaces, el cociente de brazos de contacto debe satisfacer `H=1`.
3. **Diferencias de referencia:** la variación de radios de cada cápsula puede cancelarse al cerrar el circuito, sin fijar el ritmo libre `s(t)`.
4. **No-periodicidad:** `H=1` no implica necesariamente múltiplo entero de vueltas ni retorno completo de fases.
5. **Separación geométrica:** la misma coincidencia no basta para impedir `A→0` o la proximidad de vértices.
6. **Física:** la dinámica de Navier–Stokes puede deformar un circuito material y variar su circulación sin singularidades. No conserva automáticamente la regla de los engranajes.

Por tanto la semilla capaz de determinar la evolución de un **campo de fluido** necesitaría una regla más fuerte que `H=1`. Cualquier candidato debe definir **desde `u(x,t)`**, sin seleccionar manualmente cuatro cápsulas ni contactos, las magnitudes comparadas, su orientación y sus fases; demostrar su ley de evolución; y establecer una restricción a priori que impida pérdida de regularidad bajo los datos admitidos. La comparación con el momento hidrodinámico O73 debe mantenerlo separado del momento ontológico de ejecución.

### Candidato preciso para O75

Definir una **holonomía transportada por el campo** (si existe) a partir de secciones y trayectorias materialmente identificables de un anillo; calcular `d log H/dt` usando Navier–Stokes y evaluar si equivale a cero, tiene signo, o sólo satisface una estimación dependiente de derivadas ya desconocidas. Comparar contra el anillo O53/O69 y contra la solución exacta viscosa (74.14), que rompe la conservación general de circulación. La pregunta no es si encontramos un `H` que coincida por definición: es si **la dinámica selecciona de forma no trivial una referencia suficiente**.

## 8. Reproducción y control

`python codigo/verificar_o74.py` genera `datos/resumen.json`, `datos/o74_serie.csv` y dos gráficos SVG. Verifica el cierre telescópico en 1000 familias aleatorias de cuatro radios, 500 familias asimétricas y compensadas, paridad para ciclos de 3 a 8 nodos, geometría de 701 rombos, una familia de deformaciones afines incompresibles y 501 evaluaciones de la identidad viscosa de Kelvin. No constituye exploración numérica de regularidad general.

**Antecedentes internos:** O68 (Bézout y normalización entera), O69 (fases materiales no sincronizadas), O70–O71 (promedio de espejos e información residual), O72 (grafo bipartito y dos libertades), O73 (impulso y normalización de vorticidad sin swirl). Se conservan como trabajos anteriores sin reescribirlos.
