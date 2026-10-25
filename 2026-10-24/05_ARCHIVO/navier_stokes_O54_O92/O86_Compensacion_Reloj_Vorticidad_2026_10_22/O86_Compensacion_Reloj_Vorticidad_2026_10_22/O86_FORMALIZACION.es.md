# O86 — El determinante dinámico: compensación, fase y reloj endógeno

**Programa de Geometría Relacional** — autoría del programa: **Le Matt Ansatz Di Ego**  
22 de octubre de 2026 · suplemento aditivo posterior a O85.  
**Estado:** [O] ontología preservada; [T] identidad o proposición exacta bajo contrato; [E] comprobación computacional; [F] control adversarial; [A] pendiente.  
**Alcance:** resultados instantáneos y criterio condicional de continuación para Navier–Stokes tridimensional sin fuerza. **No** se demuestra regularidad global para datos 3D arbitrarios.

## 0. El encargo y qué se reutiliza

[O] El cierre propio de la singularidad del programa no es una forma fija. Anillo, esfera y ola se consideran manifestaciones posibles de una regla relacional; no se identifica un cierre ontológico con una singularidad analítica. La referencia que normalizó debe poder transportar los comunes; la novedad puede reorganizar el resto. La conservación de representación aritmética **no** implica por sí sola disminución física de una magnitud.

No se repiten como preguntas sin resolver la definición del tiempo ni del eco: **O40/O58** probaron conservación de relaciones de representación y estelas; **O25/O45** formularon relojes y referencias de flujo; **O39** dio la identidad exacta de vorticidad; **O79** probó el papel de la fase; **O80–O85** desarrollaron presupuestos, referencias actualizables y pruebas adversariales. O86 busca la conexión mínima entre *estiramiento*, *disipación* y *tiempo generado por la propia escala de vorticidad*, y una prueba de que la compensación no ocurre automáticamente.

## 1. Contrato de la ecuación

Dominio periódico `T³=(R/2πZ)³`, viscosidad `ν>0`, fuerza nula, soluciones suaves y solenoidales en el intervalo considerado. `⟨f⟩` designa el **promedio espacial** sobre `T³`; equivale a la integral dividida por el volumen fijo. Definimos:

\[
\partial_t u+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\quad\nabla\cdot u=0,
\quad\omega=\nabla\times u,
\quad S=\tfrac12(\nabla u+\nabla u^T).
\]

\[
A(t)=\langle|\omega|^2\rangle,\qquad
B(t)=\langle|\nabla\omega|^2\rangle,\qquad
P(t)=\langle\omega\cdot S\omega\rangle.
\]

Son los objetos de O39. Se restringen las fórmulas con divisiones a intervalos con `A,B>0`. Por integrar la ecuación de vorticidad, la derivada exacta es

\[
\boxed{\tfrac12 A'(t)=P(t)-\nu B(t).}\tag{86.1}
\]

### T86.1 — El reloj de compensación que ya estaba implícito

Tomemos la longitud endógena de O25:

\[
\ell_\omega^2(t)=\frac{A(t)}{B(t)}
\]

y definamos **una segunda parametrización adimensional del mismo tiempo físico**, dependiente de la tasa viscosa en esa longitud:

\[
\boxed{\tau_\nu(t)=\int_0^t\frac{\nu}{\ell_\omega(s)^2}\,ds=\int_0^t\nu\frac{B(s)}{A(s)}\,ds.}\tag{86.2}
\]

No se postula tiempo como fondo exterior ni se modifica la dinámica: `τ_ν` es una lectura endógena distinta del reloj de fases de O45. Si no hay una fase física identificable, (86.2) sigue siendo un observable definido mientras `A,B>0`.

Definimos el **cociente de compensación**:

\[
\boxed{\Gamma_\nu(t):=\frac{P(t)}{\nu B(t)}.}\tag{86.3}
\]

Al dividir (86.1) por `A`, y luego por `dτ_ν/dt=νB/A`, se obtiene **exactamente**:

\[
\boxed{\frac{d\log A}{d\tau_\nu}=2(\Gamma_\nu-1).}\tag{86.4}
\]

- `Γ_ν>1`: aumenta instantáneamente la vorticidad cuadrática;
- `Γ_ν=1`: su derivada instantánea se anula;
- `Γ_ν<1`: disminuye.

No se afirma que `Γ_ν` sea constante, que tenga que valer 1, ni que su positividad sea señal de explosión. **La regla de actualización del normalizador entero de O58 no se identifica con Γ_ν.**

### T86.2 — Una condición precisa de continuación (condicional)

En un intervalo suave con `A>0`, integramos:

\[
\boxed{A(t)=A(0)\exp\left[2\int_0^{\tau_\nu(t)}(\Gamma_\nu-1)\,d\tau_\nu\right].}\tag{86.5}
\]

Por tanto, para un tiempo físico finito `T*`, si

\[
\boxed{\int_0^{T*}(\Gamma_\nu(t)-1)_+\,d\tau_\nu(t)<\infty,}\tag{86.6}
\]

entonces `sup_{t<T*} A(t)<∞`. Para datos suaves periódicos, una cota uniforme de la enstrofía impide la pérdida de regularidad en `T*` mediante criterios clásicos de continuación. **(86.6) es condición suficiente; aún no fue derivada para todos los datos 3D.** Su valor es convertir la prueba buscada en un objeto explícito *medido en el reloj del flujo*. No convierte una identidad de balance en un nuevo teorema global.

## 2. Separación de la orientación ya demostrada en O39

En puntos donde `q=|ω|>0`, escribamos `ξ=ω/q`, `α=ξ^TSξ`. O39 demostró:

\[
P=\langle q^2\alpha\rangle,\qquad
B=\langle|\nabla q|^2\rangle+\langle q^2|\nabla\xi|^2\rangle.
\]

Así

\[
\boxed{\Gamma_\nu=
\frac{\langle q^2\alpha\rangle}
{\nu\left(\langle|\nabla q|^2\rangle+\langle q^2|\nabla\xi|^2\rangle\right)}.}\tag{86.7}
\]

El denominador reúne disipación por gradientes de magnitud y por orientación. Cambiar la dirección vorticial puede contribuir a la compensación; **no se sigue de la geometría sola que siempre compense el estiramiento**.

## 3. F86.1 — Prueba adversarial tridimensional exacta de la fase

Reutilizamos la tríada de O79, pero calculamos ahora el **balance global de enstrofía**, no solamente la transferencia de un modo. Consideremos:

\[
\begin{aligned}
 k&=(1,0,0), &L&=(0,1,1),&m&=k+L=(1,1,1),&h&=(0,0,1),\\
 A_0&=(0,1,0),&B_0&=(1,0,0),&C_0&=(1,1,-2),&D_0&=(1,0,0),
\end{aligned}
\]

\[
\boxed{u_0=aA_0\cos(k\cdot x)+bB_0\cos(L\cdot x)+cC_0\sin(m\cdot x)+dD_0\cos(h\cdot x).}\tag{86.8}
\]

Los cuatro modos satisfacen `k·A₀=L·B₀=m·C₀=h·D₀=0`. Los tres vectores `k,L,h` son linealmente independientes. Por tanto, para `a,b,c,d≠0`, el campo es un polinomio trigonométrico **genuinamente dependiente de las tres coordenadas**, incompresible y suave. Su solución NS existe al menos localmente.

Usando únicamente productos de Fourier y la proyección de Leray, se obtienen las identidades algebraicas exactas:

\[
\boxed{P(0)=\frac34abc,\quad
A(0)=\frac{a^2+2b^2+18c^2+d^2}{2},\quad
B(0)=\frac{a^2+4b^2+54c^2+d^2}{2}.}\tag{86.9}
\]

**Fase continua, sin cambiar las magnitudes.** Sustituya en (86.8) el término `c C₀ sin(m·x)` por `C₀ sin(m·x+φ)=C₀[cos φ sin(m·x)+sin φ cos(m·x)]`, dejando `a=b=1`, `d=1/3`. La versión simbólica con dos coeficientes `c,e` verifica exactamente:

\[
\boxed{P(\phi)=\tfrac34\cos\phi,\qquad A(\phi)=\tfrac{95}{9},\qquad B(\phi)=\tfrac{266}{9}.}\tag{86.9b}
\]

Así la variación **continua de fase**, no de magnitud, modifica el estiramiento global y deja fijas las cantidades cuadráticas. Los extremos `φ=0,π` son los dos casos presentados a continuación.

El modo `h` no forma una tríada resonante inicial adicional que contribuya a `P(0)`; sí contribuye positivamente a `A` y `B`. El script calcula todos los coeficientes en aritmética simbólica, no toma `P` de una cuadratura.

Para `a=b=1`, `d=1/3`, `c=+1` o `−1`, y `ν=1/100`, las **dos configuraciones tienen igual A, B y ℓω**, pero cambia el signo de `P`:

\[
\boxed{A=\frac{95}{9},\quad B=\frac{266}{9},\quad \ell_\omega^2=\frac{95}{266}.}\tag{86.10}
\]

| Dato inicial | `P` | `Γν=P/(νB)` | `½ A' = P−ν B` |
|---|---|---|---|
| `c=+1` | `+3/4` | `+675/266 ≈ +2.53759` | `+409/900 ≈+0.45444` |
| `c=−1` | `−3/4` | `−675/266 ≈ −2.53759` | `−941/900 ≈−1.04556` |

**Consecuencia demostrada:** el mismo referente espectral, la misma distribución inicial de enstrofía por magnitudes de modos y la misma viscosidad pueden acompañarse de estiramiento neto positivo o negativo dependiendo de la fase. No hay una desigualdad universal `P≤νB` ni, a fortiori, `P≤νD_ang`, para todo dato suave 3D. Tampoco puede inferirse `Γ≤1` solo del transporte de una referencia cardinal.

**Importante:** un crecimiento inicial positivo **no** implica singularidad posterior. La pareja es un falsador de compensación instantánea universal, no una solución que explota.

### Control de amplitud

Multiplicar los cuatro coeficientes de (86.8) por `λ>0` (viscosidad fija) da:

\[
P_\lambda(0)=\lambda^3 P(0),\qquad
A_\lambda(0)=\lambda^2 A(0),\qquad
B_\lambda(0)=\lambda^2 B(0),\qquad
\boxed{\Gamma_{\nu,\lambda}(0)=\lambda\Gamma_\nu(0).}
\tag{86.11}
\]

No existe un límite superior universal fijo para `Γν(0)` en todos los datos suaves de esta familia. Esto **no** contradice que la solución exista suavemente durante un intervalo temporal local dependiente de los datos.

## 4. T86.3 — Invariancia bajo la transformación de escala de Navier–Stokes

Para escala **espacial y temporal** entera `n≥1` en el mismo toro periódico, la transformación natural es

\[
u_n(x,t)=n u(nx,n^2t),\qquad p_n(x,t)=n^2p(nx,n^2t).
\]

Los promedios cambian según `A_n=n⁴A(n²t)`, `B_n=n⁶B(n²t)`, `P_n=n⁶P(n²t)`. En consecuencia:

\[
\boxed{\ell_{\omega,n}^2(t)=n^{-2}\ell_\omega^2(n^2t),\quad
\Gamma_{\nu,n}(t)=\Gamma_\nu(n^2t),\quad
\tau_{\nu,n}(t)=\tau_\nu(n^2t).}\tag{86.12}
\]

**Es una covariancia exacta del reloj y del cociente**, no una prueba de que estos permanezcan acotados. Contrastar con (86.11): *reescalar la PDE* y *aumentar la amplitud física con viscosidad fija* son operaciones diferentes.

## 5. T86.4 — Control positivo: campo de Beltrami de intensidad arbitraria

Sea

\[
V(x,y,z)=(\sin z+\cos y,\ \sin x+\cos z,\ \sin y+\cos x).
\]

Cumple `∇·V=0`, `curl V=V`, `ΔV=−V`. Entonces `U(x,t)=M e^{−νt}V(x)` satisface Navier–Stokes para todo `t≥0` y todo `M∈R`, con presión `p=−|U|²/2` hasta constante espacial. Por la identidad `(U·∇)U=∇(|U|²/2)−U×curl U`, el transporte no lineal queda absorbido en la presión porque `U×curl U=0`.

En esta familia el estiramiento global es `P=0`; `Γν=0` mientras `U≠0`; `A(t)=A(0)e^{−2νt}` y `ℓω=1`. Puede ser arbitrariamente intensa sin perder suavidad. **Ni magnitud grande ni frecuencia alta constituyen, por sí solas, singularidad.**

## 6. Qué falta de verdad para un teorema universal [A]

La igualdad (86.4) identifica el determinante; el trabajo nuevo **no** es demostrar de nuevo esa identidad, sino obtener una restricción física adicional **no circular** sobre `∫(Γ−1)_+dτ` para todos los datos relevantes. Las propiedades de cierre propio y normalización heredada de O40/O58 han de vincularse explícitamente con `P` y `B`. De lo contrario, sólo transportan representación.

Un posible siguiente lema, sometido a prueba adversarial, sería hallar una *cantidad de fase-orientación corregida* `J[u]` y funciones `C(u₀,ν,T)` calculables **sin conocer la solución futura**, tales que:

\[
\int_0^T (P-\nu B)_+\frac{dt}{A}
\ \le\ C(u_0,\nu,T)<\infty\quad\text{para todo }T<\infty.
\tag{86.13}
\]

La izquierda es el exceso en el reloj de compensación porque `(Γ−1)_+dτ=(P−νB)_+dt/A`. **(86.13) constituye la meta, no una propiedad ya establecida.** Una fórmula que sólo replique `(86.1)` sin una cota independiente no sirve como demostración general.

Para someter a prueba una condición candidata:

1. Debe respetar las simetrías y el reescalado físico (86.12).
2. Debe admitir tanto `Γ>1` instantáneo (tríada de fases) como `Γ=0` en grandes datos exactos (Beltrami).
3. Debe conectarse con el control temporal de O25/O45 y con los certificados acumulativos O84, **sin asignar gratis una cota a la fase**.
4. Su argumento debe aplicarse a una sola evolución NS, no a una sucesión fabricada con campos iniciales distintos.

**Resultado epistemológico:** O86 establece una identidad exacta dimensionalmente coherente y un falsador de compensación instantánea universal. La regularidad global sin fuerza en 3D sigue abierta bajo las hipótesis generales de este documento.

## 7. Reproducción

Ejecutar `python codigo/o86_verificar.py`. Requiere `sympy`, `numpy`, `matplotlib`. Verifica simbólicamente `P, A, B`, el cociente `Γ`, el balance (86.4), cuatro cambios de amplitud, y el control Beltrami; coteja la tríada con FFT en mallas `16³`, `24³`, `40³` para ambos signos de la fase; genera `resultados/verificacion.json`, `resultados/verificacion_fourier.csv` y `graficos/o86_fase_y_compensacion.png`. **No integra una solución temporal 3D:** los controles son datos instantáneos exactos.
