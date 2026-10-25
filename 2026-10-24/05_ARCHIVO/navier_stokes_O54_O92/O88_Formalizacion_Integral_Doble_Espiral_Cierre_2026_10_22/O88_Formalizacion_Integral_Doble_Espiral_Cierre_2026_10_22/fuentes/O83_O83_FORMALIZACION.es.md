# O83 — Actualización recursiva de referencias y prueba adversarial del certificado

**Programa de Geometría Relacional** · Le Matt Ansatz Di Ego  
**22 de octubre de 2026** · Suplemento posterior a O80–O82 · sin reemplazar sus fuentes.

**Estatus:** `[O]` ontología del programa; `[T]` proposición exacta bajo contrato; `[E]` verificación computacional; `[F]` falsador/límite; `[A]` puente abierto. **No se ha demostrado la regularidad global de Navier–Stokes 3D para datos arbitrarios.**

## 0. La pregunta, bien formulada

El usuario propone una regla generativa, no una forma fija: el múltiplo que normalizó una configuración transporta la posibilidad de reconstruir lo acreditado; el resto permite reorganización. Un anillo de cuatro gotas, una esfera o una ola podrían realizar cierres propios diferentes. Ya están formalizados transporte de referencias (`O40`), estelas y ramificaciones aritméticas (`O58`), tiempo/ritmo del flujo (`O25`, `O45`), diferencias de fase (`O79`) y certificados físicos críticos (`O80–O82`). **No se deben declarar ausentes esos resultados.**

Aquí la pregunta no es si la referencia puede actualizarse algebraicamente —eso ya tiene una construcción— sino si actualizar una **referencia física aproximada** reduce el defecto de Navier–Stokes con garantías cuantitativas, y qué se requeriría para iterarlo sin interrupción.

Las referencias de O83 **no** se identifican automáticamente con el normalizador cardinal de O40/O58. Son una realización PDE concreta y falsable del patrón «referencia + diferencia pendiente + nuevo cierre».

## 1. Contrato PDE y revisión de O82 [T]

En el toro `T³=(R/2πZ)³` y `ν>0`, sin fuerzas, con media cero:

\[
\partial_tu+\mathcal N(u)=\nu\Delta u,
\qquad\mathcal N(u):=\mathbb P\nabla\cdot(u\otimes u),\qquad\nabla\cdot u=0.
\]

Para un campo `f` con coeficientes complejos de Fourier `\hat f_k` definimos

\[
R(f)=\sum_{k\ne0}\frac{|\hat f_k|}{|k|},\quad
S(f)=\sum_{k\ne0}|\hat f_k|,\quad
Q(f)=\sum_{k\ne0}|k|\,|\hat f_k|.
\]

La referencia `U(t)` es suave, solenoidal, de media cero y **no** tiene que resolver Navier–Stokes. Definimos su defecto

\[
F_U=\partial_tU+\mathcal N(U)-\nu\Delta U,
\quad B_U(t)=R(F_U(t)),\quad v=u-U.
\]

Entonces, mientras exista una solución suave,

\[
D^+ R(v)+\nu Q(v)\le R(v)Q(v)+2S(U)\sqrt{R(v)Q(v)}+B_U.
\tag{83.1}
\]

Como en O82, en el intervalo donde `R(v)≤ν/2`, se obtiene

\[
D^+R(v)+\frac\nu4Q(v)\le\frac4\nu S(U)^2R(v)+B_U.
\tag{83.2}
\]

Para un intervalo `[a,b]`, ponemos

\[
G_U(t;a)=\frac4\nu\int_a^t S(U(s))^2ds,\quad
\mathfrak M_{[a,b]}(U,r_a)
=e^{G_U(b;a)}\left[r_a+\int_a^b e^{-G_U(s;a)}B_U(s)ds\right].
\tag{83.3}
\]

**Teorema O83-T1 (certificación local por defecto).** Si `R(u(a)-U(a))≤r_a` y el valor computable `(83.3)` es **estrictamente menor que `ν/2`**, entonces existe continuación suave de la solución hasta `b` y, en dicho intervalo,

\[
R(u(t)-U(t))\le\mathfrak M_{[a,b]}(U,r_a),\qquad
\int_a^b Q(u-U)dt\le\frac4\nu\mathfrak M_{[a,b]}(U,r_a).
\tag{83.4}
\]

*Prueba:* aplicar (83.2) con factor integrante `e^{-G_U}`, cerrar por el primer tiempo de cruce de `ν/2`, y usar `e^{-G_U(s;a)}≥e^{-G_U(b;a)}` en la desigualdad integrada. La cota sobre `∫||∇u||_∞` es finita si `∫Q(U)` lo es, lo que permite la continuación clásica en un intervalo finito. Ésta es la adaptación **local** del teorema O82: no se presupone globalidad de la referencia.

## 2. Una refutación exacta de la necesidad del certificado O82 [T/F]

Tomar `ν=1` y los datos iniciales

\[
\boxed{u_0(x,y,z)=(4\sin(2y),\,4\sin x,\,0).}\tag{83.5}
\]

Es un campo suave, periódico, incompresible y de media cero. Al no depender de `z` ni poseer componente `z`, su evolución pertenece al **sector bidimensional**, para el que la regularidad global con viscosidad positiva es un teorema clásico. Esto **no** pretende ser una solución 3D genérica.

El selector O82 permite conjuntos `F` finitos y simétricos que retengan o no los **dos pares** de modos activos. Si falta la onda `sin(2y)`, el resto inicial tiene `R≥4/2=2`. Si falta la onda `sin x`, tiene `R≥4`. En ambos casos el presupuesto O82 supera `ν/2=0.5` antes de incorporar defectos.

Si ambos pares se seleccionan, la referencia de calor es

\[
U^{[0]}(t)=(4e^{-4t}\sin2y,\,4e^{-t}\sin x,\,0).
\tag{83.6}
\]

Su término no lineal proyectado es explícito. Para amplitudes generales `A,B>0` y vectores `k_+=(1,2)`, `k_-=(1,-2)`, defina

\[
W=\mathcal N(u_0)=AB\left[
(\tfrac35,-\tfrac3{10},0)\sin(x+2y)+
(\tfrac35,\tfrac3{10},0)\sin(x-2y)\right].\tag{83.7}
\]

Como `|k_±|=√5`, tenemos

\[
S(W)=\frac{3AB}{\sqrt5},\quad
R(W)=\frac{3AB}{5}.
\tag{83.8}
\]

Para `A=B=4`:

\[
F_{U^{[0]}}(t)=e^{-5t}W,
\quad B_{U^{[0]}}(t)=\frac{48}{5}e^{-5t},
\quad\boxed{\int_0^\infty B_{U^{[0]}}dt=\frac{48}{25}=1.92>0.5.}\tag{83.9}
\]

Como `e^{G∞-G(t)}≥1`, el presupuesto O82 en horizonte infinito es al menos `1.92`. **Ningún selector `F` del tipo O82 puede certificar ese dato**, aunque la solución sea globalmente suave por el teorema bidimensional.

Por tanto: **falla del certificado ≠ singularidad física; certificado suficiente ≠ clasificación exhaustiva.**

## 3. Primera actualización del cierre: Picard 1 [T]

Introducimos, únicamente a partir de los datos iniciales,

\[
\boxed{U^{[1]}(t)=e^{t\Delta}u_0-
\int_0^t e^{(t-s)\Delta}\mathcal N(U^{[0]}(s))ds.}\tag{83.10}
\]

Como las frecuencias de `W` tienen `|k|²=5`, y `\mathcal N(U^{[0]}(s))=e^{-5s}W`, el integral es **exactamente** `t e^{-5t}W`. Por ello:

\[
\boxed{U^{[1]}(t)=U^{[0]}(t)-t e^{-5t}W.}\tag{83.11}
\]

**El perfil actualizado conserva los cuatro modos nuevos generados por la primera interacción** (dos parejas conjugadas). Es una ampliación dinámica concreta de la semilla: las relaciones nuevas proceden de la ecuación, no de una selección arbitraria posterior.

Como `∂_tU^{[1]}-ΔU^{[1]}=-\mathcal N(U^{[0]})`, el defecto nuevo es

\[
\boxed{F_{U^{[1]}}=\mathcal N(U^{[1]})-\mathcal N(U^{[0]})}.\tag{83.12}
\]

Escriba `D=U^{[1]}-U^{[0]}`. Entonces `F_1=\mathcal N(U^{[0]},D)+\mathcal N(D,U^{[0]})+\mathcal N(D,D)`, donde `\mathcal N(f,g)=\mathbb P\nabla\cdot(f\otimes g)`. La desigualdad de Fourier de O80 da

\[
\boxed{B_{U^{[1]}}(t)\le2S(U^{[0]}(t))S(D(t))+S(D(t))^2.}\tag{83.13}
\]

Poniendo `L=A+B=8`, `T=S(W)=48/√5`, y usando `S(U^{[0]})≤L`, `S(D)≤Tt`, para cualquier `δ>0`:

\[
\int_0^\delta B_{U^{[1]}}dt\le LT\delta^2+\frac{T^2}{3}\delta^3,
\quad G_{U^{[1]}}(\delta;0)\le4\delta(L+T\delta)^2.
\tag{83.14}
\]

Así, con resto inicial **nulo** y `ν=1`,

\[
\boxed{\mathfrak M_{[0,\delta]}(U^{[1]},0)\le
\exp\big[4\delta(L+T\delta)^2\big]
\left(LT\delta^2+\tfrac{T^2}{3}\delta^3\right).}\tag{83.15}
\]

## 4. Comparación inequívoca en el mismo intervalo [T/E]

Fijamos `δ=9/800=0.01125`.

**Referencia de calor:** sobre `[0,δ]`, su defecto es `B_0(t)=9.6e^{-5t}` y su exposición es `g_0(t)=4(4e^{-4t}+4e^{-t})²`. Sean `g_min=g_0(δ)` y `b_min=B_0(δ)`. Por monotonía:

\[
\mathfrak M_{[0,\delta]}(U^{[0]},0)
\ge b_{\min}\frac{e^{g_{\min}\delta}-1}{g_{\min}}
>0.5334>0.5.
\tag{83.16}
\]

**Referencia actualizada:** de (83.15):

\[
\boxed{\mathfrak M_{[0,\delta]}(U^{[1]},0)<0.4667<0.5.}\tag{83.17}
\]

**Certificación exacta sin dependencia de redondeo:** el programa genera también cotas con fracciones racionales. Para la primera se usa `e^{-x}≥1-x` y `e^x−1≥Σ_{n=1}^8x^n/n!`, con `δ=9/800`; resulta una **cota inferior estricta `>0.5303308`**. Para Picard se reemplaza `48/√5<2147/100` y se usa una serie de Taylor de `e^x` hasta grado 20 con cola geométrica mayorante `x^{21}/21!/(1−x/22)`; se obtiene la **cota superior estricta `<0.4666714`**. Por tanto ambas comparaciones con `0.5` son pruebas algebraicas/racionales, independientemente de integración por cuadratura.

En síntesis: **para el mismo dato y el mismo tiempo, la referencia anterior NO pasa y la referencia enriquecida SÍ pasa el criterio suficiente**. Es una mejora certificada del *método*, no la solución de NS 3D general. La prueba numérica independiente del soporte Fourier del defecto sirve solo de control.

## 5. Recursión de intervalos: el teorema que podemos sostener [T]

Sean tiempos `0=t₀<t₁<...` y campos de referencia `U_j(t)` explícitamente conocidos en `[t_j,t_{j+1}]`, todos suaves, solenoidales y de media cero. Sea `r_j` una cota **certificada** de `R(u(t_j)−U_j(t_j))`.

Construimos

\[
\boxed{M_j=e^{G_j(t_{j+1})}
\left[r_j+\int_{t_j}^{t_{j+1}}e^{-G_j(s)} B_j(s)ds\right],\quad
G_j(t)=\frac4\nu\int_{t_j}^t S(U_j)^2ds.}\tag{83.18}
\]

Si `M_j<ν/2`, el teorema O83-T1 certifica el intervalo y la propagación de la interfaz satisface

\[
\boxed{r_{j+1}\le M_j+R\big(U_j(t_{j+1})-U_{j+1}(t_{j+1})\big).}\tag{83.19}
\]

**Teorema O83-T2 (continuación bajo una cadena de certificados):** Si para todo `T<∞` hay una cantidad **finita** de intervalos certificados que cubren `[0,T]`, con cada `M_j<ν/2` y referencias de gradiente temporalmente integrable, entonces el campo inicial tiene solución suave en todos los tiempos. La prueba concatena (83.4) en cada intervalo finito y emplea el criterio de continuación por `∫||∇u||_∞`.

Para el caso de **infinitos intervalos acumulados en un tiempo finito** `T*`, basta adicionalmente, por ejemplo, la condición cuantitativa

\[
\boxed{\sum_j\left[\int_{t_j}^{t_{j+1}}Q(U_j)dt+\frac{4M_j}{\nu}\right]<\infty.}\tag{83.20}
\]

Entonces `∫_0^{T*}||∇u||_∞dt` es finito y puede continuarse. Esta condición es **suficiente, no necesaria**. Sin control de acumulación, obtener certificados en intervalos cada vez más pequeños no prueba que no haya concentración en el instante límite.

**Advertencia crucial:** O83-T2 es una implicación condicionada. No se ha construido desde **cada** `u₀` suave una cadena que satisfaga universalmente estas hipótesis. Afirmarlo sería equivalente a haber probado una forma de regularidad global que aquí no existe.

## 6. La fase, el reloj y la singularidad del programa [O/T/A]

- El entero normalizador y la inclusión de clases de `O40/O58` continúan vigentes. Las nuevas frecuencias de (83.11) son información *física* generada por no linealidad, no la definición del «resto uno».
- Las fases de los modos determinan las transferencias (`O79`); `R,S,Q` las **mayoran** por desigualdad triangular. Es una estimación que no requiere conocer las fases futuras, aunque no aprovecha sus cancelaciones favorables.
- El reloj endógeno ya se deriva en `O25/O45`. Reparametrizar por `ds/dt=v_*/ℓ(t)` no impone un tiempo físico mínimo entre nuevos cierres. Una profundidad o frecuencia relacional que diverge conforme `t→T*` no excluye por sí sola singularidad.
- «Singularidad» como **cierre propio** en el programa no debe confundirse con una pérdida de regularidad PDE. La familia generativa de anillos/esferas/olas requiere un teorema de **cobertura** antes de identificarse con todas las posibles concentraciones de soluciones tridimensionales.

## 7. Resultado, frontera y próximo ensayo

| Afirmación | Estatus |
|---|---|
| Un flujo globalmente regular puede fallar todos los selectores espectrales O82 | `[T]` Demostrado por el ejemplo bidimensional incrustado |
| Incorporar la primera interacción reduce el defecto y permite certificar un intervalo que la referencia de calor no certifica | `[T]` Demostrado con fracciones racionales |
| El defecto de una referencia arbitraria cumple (83.1) | `[T]` Demostrado en el contrato Fourier |
| Concatenar certificados finitos y controlar el caso Zeno implica continuación | `[T]` Condicionado, demostrado |
| El programa construye esas referencias para cualquier dato 3D, hasta cualquier tiempo físico | `[A]` NO demostrado |
| El multiplicador entero de O58 por sí mismo controla `\int||∇u||∞dt` | `[A/F]` NO demostrado |

**Conclusión:** la regla de «referencia + nueva relación + resto reestimado» tiene una realización dinámica constructiva que mejora un certificado físico; su limitación actual no es la forma inicial del anillo, sino demostrar un **presupuesto uniforme a través de todas las actualizaciones**, sin exigir de antemano lo que se quiere demostrar. El candidato de siguiente trabajo es examinar si la actualización puede operar con **bloques de escala** que eviten crecimiento excesivo del presupuesto `S(U)^2` y ofrezcan márgenes uniformes de tiempo y defecto.

### Reproducir

Ejecutar `python codigo/o83_verificar.py`. Requiere NumPy y, para la figura, Matplotlib. La salida `resultados/verificacion.json` contiene ambos certificados racionales, y el CSV compara residuos instantáneos calculados con aritmética Fourier finita. El resultado de regularidad bidimensional y las desigualdades son pruebas analíticas; la ejecución es un chequeo complementario, no una prueba numérica de PDE global.
