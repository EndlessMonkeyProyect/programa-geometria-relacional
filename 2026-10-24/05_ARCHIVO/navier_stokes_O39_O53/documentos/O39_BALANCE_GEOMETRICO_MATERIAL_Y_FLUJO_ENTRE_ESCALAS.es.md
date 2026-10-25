# O39 — Espejo lateral, radio móvil, orientación y balance en Navier–Stokes 3D

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego** · 20 de octubre de 2026  
**Estado:** suplemento independiente de investigación, sin modificación de la Imagen Total v3.6.0 ni del Núcleo Canónico.  
**Leyenda:** `[O]` interpretación ontológica · `[D]` definición e hipótesis · `[T]` teorema exacto bajo hipótesis · `[C]` teorema condicionado · `[F]` falsador/no-go · `[E]` prueba reproducible · `[A]` abierto · `[P]` puente físico no derivado.

## 0. Pregunta precisa y respuesta

Inspiración: toroide vorticial, resorte cerrado, doble orientación, radio de referencia que cambia durante el desplazamiento, diferencia de ritmos entre parte interior/exterior, reorganización y posibilidad de fragmentación. La semilla del uno es referencia estructural en la ontología; no se identifica con una partícula, un punto fijo del fluido ni una singularidad analítica. La pregunta: **¿obliga Navier–Stokes 3D a que el canal transversal o la expansión de un radio disipen o redistribuyan lo suficiente para impedir concentración infinita de vorticidad?**

**Resultado:** (i) existen identidades exactas que separan estiramiento, disipación por gradiente de intensidad, disipación por gradiente espacial de orientación y flujo a través de una referencia móvil; (ii) existe un ejemplo explícito de datos iniciales suaves y **energía finita** para los cuales la vorticidad se intensifica materialmente sin girar y sin gradiente local de dirección: **no existe compensación perpendicular punto a punto universal**; (iii) hay un criterio suficiente condicionado, matemáticamente legítimo, para la continuación de soluciones 3D que requiere una cota genuina de agotamiento geométrico del estiramiento; (iv) el transporte entre ventanas o escalas no puede confundirse con disipación global; en una partición de la unidad, los flujos de interfaz se cancelan exactamente.

No afirmamos regularidad global, que cada remolino tenga una superficie material, ni que tensión superficial sea parte de Navier–Stokes de fluido homogéneo. Los chorros, olas, resorte y anillos de aire bajo el agua son comparaciones de **modelos físicos distintos**; la tensión superficial exige una interfaz multifásica.

## 1. Contrato físico [D]

Considérese una solución clásica de Navier–Stokes incompresible y no forzado en todo el espacio `R³`, con viscosidad `ν>0`, datos iniciales solenoidales suaves de energía finita y decaimiento suficiente para realizar las integraciones:

\[
\partial_t u+u\cdot\nabla u=-\nabla p+\nu\Delta u,\qquad \nabla\cdot u=0,
\quad \omega=\nabla\times u,\quad D_t=\partial_t+u\cdot\nabla.
\tag{1}
\]

La ecuación de vorticidad es
\[
D_t\omega=(\omega\cdot\nabla)u+\nu\Delta\omega=S\omega+\nu\Delta\omega,
\quad S=\tfrac12(\nabla u+\nabla u^\top).
\tag{2}
\]

En el conjunto donde `q=|ω|>0`, sean `ξ=ω/q`, `α=ξ·Sξ`. **No** confundir `q` con carga eléctrica, `ξ` con una dirección material rígida ni `α` con una frecuencia. Una línea de vorticidad y su geometría espacial cambian con el tiempo. En los ceros de `q`, fórmulas en `ξ` deben interpretarse solo en el conjunto `q>0` y mediante extensión del producto ponderado `q²|∇ξ|²`, cuando exista.

## 2. O39-T1 — Los dos canales exactos de evolución material [T]

La identidad `ω=qξ` y `ξ·D_tξ=0` dan, donde `q>0`,
\[
\boxed{D_t\log q=\alpha+\nu\left(\frac{\Delta q}{q}-|\nabla\xi|^2\right).}\tag{3}
\]

La parte perpendicular satisface
\[
\boxed{D_t\xi=P_\xi^\perp S\xi+\nu\left[\Delta\xi+2\nabla\log q\cdot\nabla\xi+|\nabla\xi|^2\xi\right],\quad P_\xi^\perp=I-\xi\otimes\xi.}\tag{4}
\]

La igualdad `ξ·Δξ=-|∇ξ|²` garantiza que (4) es perpendicular a `ξ`. Las identidades son conocidas y concuerdan con el antecedente O27 y con el manuscrito del cambio material. **Importante:** el giro *material* `|D_t ξ|` no es la misma variable que el gradiente *espacial* `|∇ξ|`. El segundo figura en la disipación viscosa; del primero no se obtiene por pura geometría una cota de estiramiento.

## 3. O39-T2 — Descomposición de la disipación y enstrofía [T]

Para cada coordenada `j`, `∂_jω=(∂_jq)ξ+q∂_jξ`, y `ξ·∂_jξ=0`. Por Pitágoras:
\[
\boxed{|\nabla\omega|^2=|\nabla q|^2+q^2|\nabla\xi|^2.}\tag{5}
\]

Definimos la enstrofía `E(t)=½∫_{R³}|ω|² dx`. Al multiplicar (2) por `ω`, integrar y usar `∇·u=0`, queda
\[
\boxed{
E'(t)=\underbrace{\int q^2\alpha\,dx}_{P(t):\,estiramiento}
-\underbrace{\nu\int|\nabla q|^2dx}_{D_{\rm amp}}
-\underbrace{\nu\int q^2|\nabla\xi|^2dx}_{D_{\rm ang}}.}
\tag{6}
\]

`D_ang≥0` es **la aportación disipativa de diferencias espaciales de orientación**: un candidato controlado para el lenguaje del espejo lateral. No es una energía nueva ni equivale al cambio de frecuencia poloidal de un toroide. El término `P` no tiene signo universal. Donde la dirección espacial es uniforme, `D_ang=0`; la intensidad aún puede crecer si `P>D_amp`.

## 4. O39-T3 — Balance de una referencia espacial móvil y creciente [T]

Sean `X(t)∈R³`, `R(t)>0` funciones diferenciables, y `Φ∈C_c^∞(R³)` no negativa. Elegimos *antes* de medir el campo el localizador
\[
\phi_{X,R}(x,t)=\Phi\!\left(\frac{x-X(t)}{R(t)}\right),\qquad E_\phi(t)=\frac12\int\phi_{X,R}|\omega|^2dx.
\tag{7}
\]

Para un localizador general suave, la identidad de enstrofía con interfaz es
\[
\boxed{\begin{aligned}
E_\phi'={}&\int\phi q^2\alpha\,dx-\nu\int\phi|\nabla\omega|^2dx\\
&+\frac12\int q^2\bigl[\partial_t\phi+u\cdot\nabla\phi+\nu\Delta\phi\bigr]dx.
\end{aligned}}\tag{8}
\]

La regla de la cadena da **exactamente**
\[
\boxed{(\partial_t+u\cdot\nabla)\phi_{X,R}
=\left[u-\dot X-\frac{\dot R}{R}(x-X)\right]\cdot\nabla\phi_{X,R}.}\tag{9}
\]

Así `B_{X,R}` (la tercera integral) cuantifica la transferencia **relativa a una referencia cuya posición y radio cambian**. `\dot R/R` representa expansión/contracción del marco de lectura, sin atribuir a ese radio una ley física universal. `u−dot X` indica advección respecto al centro; `νΔφ` registra difusión en la interfaz. Ninguno tiene signo fijo: la parte exterior de un toroide no disipa necesariamente más por tener mayor área; la fuerza/arrastre exige evaluar gradientes y geometría reales.

Utilizando (5) podemos separar nuevamente dentro de la región
\[
E_\phi'=P_\phi-D_{{\rm amp},\phi}-D_{{\rm ang},\phi}+B_{X,R}.\tag{10}
\]

**Convergencia de referencias:** para una partición suave no negativa `∑_j φ_j≡1` con integraciones justificadas, `∑_j B_j=0` y `∑_j E_{φ_j}=E`. Por tanto, los flujos de interfaz **redistribuyen**, pero no restan enstrofía del sistema total. La posible disipación de lo transportado pertenece a `ν‖∇ω‖²`. Esta identidad impide confundir liberación/traslado de estructura con regularización demostrada.

## 5. O39-T4 — Índice crítico del radio observado [T/D]

La simetría parabólica de Navier–Stokes con viscosidad fija es `u_λ(x,t)=λ u(λx,λ²t)`. Con `X_λ=X/λ`, `R_λ=R/λ` (en los tiempos correspondientes), la vorticidad escala como `ω_λ=λ²ω` y
\[
\boxed{\mathcal C_{X,R}(t):=\frac{R(t)}{2\nu^2}\int\phi_{X,R}(x,t)|\omega(x,t)|^2dx}
\tag{11}
\]

es **adimensional e invariante bajo escala**. Es un indicador computable de concentración relativa a la referencia elegida, no un número universal, un mínimo molecular, una frecuencia ni un criterio suficiente de regularidad por sí solo. Su derivada queda exactamente fijada por (10) y la derivada del factor `R`:
\[
\mathcal C'_{X,R}=\frac{\dot R}{\nu^2}E_\phi+\frac{R}{\nu^2}\bigl(P_\phi-D_{{\rm amp},\phi}-D_{{\rm ang},\phi}+B_{X,R}\bigr).
\tag{12}
\]

Un eventual sincronismo `mΩ_1=nΩ_2` entre ritmos declarados pertenece a la capa **hipotética** `[P]`. No se desprende de (3)–(12), ni del mínimo común múltiplo entre cardinalidades; un toroide geométrico tiene curvas poloidales/toroidales, pero el fluido no aporta automáticamente dos osciladores autónomos con frecuencias cerradas.

## 6. O39-F1 — Contraejemplo 3D con dato inicial de energía finita [T/F]

Fijemos `γ>0`, `Ω>0` y el campo lineal, de divergencia nula,
\[
v(x,y,z)=(-\tfrac\gamma2 x-\Omega y,\,-\tfrac\gamma2 y+\Omega x,\,\gamma z).\tag{13}
\]

Sea `χ∈C_c^∞(R³)` con `χ≡1` en un entorno del origen y defina el potencial vectorial `A=−\tfrac13χ(x)\,x\times v(x)` y la velocidad inicial
\[
\boxed{u_0=\nabla\times A.}\tag{14}
\]

Es suave, compactamente soportada y solenoidal, por lo que tiene energía finita y genera una solución clásica al menos en un intervalo inicial. Cerca del origen la identidad `∇×(x×v)=−3v` implica `u_0=v`. Allí
\[
\omega_0=(0,0,2\Omega),\quad S_0=\mathrm{diag}(-\gamma/2,-\gamma/2,\gamma),\quad \nabla\omega_0=0,\quad \Delta\omega_0=0.
\]

En `(x,t)=(0,0)` la ecuación (2), sin necesidad de calcular la presión, da
\[
\boxed{D_t\log|\omega|=\gamma>0,\qquad D_t\xi=0,\qquad |\nabla\xi|=0.}\tag{15}
\]

La circulación/rotación local `Ω` se puede mantener fija mientras `γ` crece arbitrariamente. **No existe una ley universal de la forma** `|D_t ξ|≥c(D_t\log q)_+`, `|∇ξ|≥c(D_t\log q)_+` o un enlace obligatorio entre esa rotación local y el estiramiento, con `c>0` independiente de los datos. O39-F1 destruye esas leyes **puntuales** incluso entre datos suaves de energía finita. No afirma nada sobre una cota *global integral* más elaborada. La evolución posterior del campo truncado no permanece lineal.

## 7. O39-C1 — Una condición suficiente de control geométrico [C]

Sea `T>0` el tiempo máximo candidato de una solución suave sin fuerza y de energía finita. Supongamos que existe una función `K(t)≥0` conocida o acotada independientemente, con `K∈L¹(0,T)`, tal que para todo `t<T`
\[
\boxed{
\int_{R^3} q^2\alpha\,dx
-\nu\int_{R^3}q^2|\nabla\xi|^2dx
\ \le\ K(t) E(t).
}\tag{16}
\]

Entonces (6) implica
\[
E'(t)+\nu\int|\nabla q|^2dx\le K(t)E(t),\qquad
\boxed{E(t)\le E(0)\exp\!\left(\int_0^tK(s)ds\right).}\tag{17}
\]

Para datos iniciales suficientemente suaves en `R³`, la energía cinética acotada y la equivalencia `‖∇u‖₂=‖ω‖₂` implican una cota uniforme `H¹` en cada intervalo hasta `T`. El criterio estándar de continuación de soluciones fuertes permite prolongar la solución más allá de `T`. **Esto es un teorema condicional y una reformulación en términos del canal angular de un balance enstrofía conocido**, NO una demostración de que toda solución 3D satisfaga (16). El gran problema es demostrar (16) *desde el propio NS*, con `K` integrable y una cota que no presuma lo que se intenta probar. La existencia de `K(t)` definido retrospectivamente usando `P-D_ang` es circular si no puede controlarse independientemente.

Una versión con margen `δ` también sirve: si `P≤(1−δ)(D_amp+D_ang)+K E` con `0<δ≤1`, entonces `E'+δ(D_amp+D_ang)≤KE`. No se introduce un mecanismo físico adicional con el cambio de escritura.

## 8. Hipótesis falsable O39-P1 — Cierre móvil entre escalas [P/A]

Reformulamos la intuición del toroide sin imponer una velocidad universal. Para una familia de ventanas `φ_{X_j,R_j}` fijada mediante una regla basada únicamente en datos admitidos antes de la evolución, registrar los canales observables `(P_j,D_amp,j,D_ang,j,B_j,\mathcal C_j)` y, si están definidos independientemente, los ritmos locales `Ω_j` y radios (mayor, menor). Examinar si ante eventos de alto estiramiento se cumple, con probabilidades/umbrales y error declarados a priori, una respuesta compensatoria de disipación geométrica y flujos hacia escalas donde se disipa. El **criterio fuerte** exigible es derivar de ese mecanismo una cota del tipo (16), no solo correlación de un desfase con una ruptura visual.

Falsadores: (i) dato compacto O39-F1 con crecimiento y giro cero; (ii) geometrías con `ξ` casi uniforme y gran `α`; (iii) ventanas con entrada de enstrofía en lugar de salida; (iv) patrones de poloidal/toroidal compatibilidad racional sin la cota (16); (v) observables que dependen del umbral o de la segmentación retrospectiva; (vi) observar dos frecuencias pero no controlar el término de presión/no localidad ni `∇ω`.

La presión no aparece explícitamente en (2), pero contribuye al gradiente de velocidad mediante la solución incompresible. **Una estructura toroidal aislada, un anillo de aire bajo el agua y un toroide vorticial monofásico no son el mismo sistema**: aire/agua requiere modelos de dos fases y tensión superficial; un fluido homogéneo con vorticidad no tiene interfaz material intrínseca.

## 9. Resultados que sí y que no [O]

**Sí:** representación cuantitativa del espejo lateral como (a) orientación espacial y disipación angular y (b) referencia móvil de radio variable; balance exacto; índice crítico; falsador fuerte de compensación automática; criterio condicionado de continuación.

**No:** mínimo común múltiplo como ley dinámica, conservación material de radios del toroide, umbral molecular de gotas, fragmentación garantizada antes de cualquier posible singularidad, regularidad global para datos arbitrarios ni demostración de una frecuencia perpendicular universal. Tampoco se prueba que todo cambio de escala conserve una forma ontológica única.

La lectura prudente del programa es: una estructura puede sostenerse por relaciones de forma, giro, extensión y transporte; el cambio de marco/escala no destruye necesariamente esas relaciones. Pero una identidad de balance **no impone** un control favorable de todos sus términos.

## 10. Procedencia y literatura

- Antecedentes internos: `O27_PERPENDICULARIDAD_Y_CIERRE_VORTICIAL.es.md`, `O18_CANALES_POR_OCTAVAS`, `O24–O26`, `O28–O38`, `manuscript(1).md` (*Material Vorticity Amplification in Growth Coordinates*). Las fórmulas de dirección y las advertencias sobre no-go ya existían en O27 y en septiembre 2026; O39 especifica **localización con radio móvil, cancelación de flujos de interfaz y falsador de energía finita**.
- Constantin y Fefferman, *Direction of Vorticity and the Problem of Global Regularity for the Navier–Stokes Equations*, Indiana Univ. Math. J. 42 (1993): https://iumj.org/article/3627/.
- Z. Grujić, *Geometry of turbulent dissipation and the Navier–Stokes regularity problem*, artículo de perspectiva: https://pmc.ncbi.nlm.nih.gov/articles/PMC8065050/.
- P. Constantin, I. Procaccia y D. Segel, *Creation and dynamics of vortex tubes in three-dimensional turbulence*, Phys. Rev. E 51 (1995): https://doi.org/10.1103/PhysRevE.51.3207.

**Conclusión:** el espejo lateral tiene una lectura PDE exacta. El tramo verdaderamente abierto es demostrar coerción/agotamiento del estiramiento desde la geometría misma sin circularidad. O39 no modifica la Imagen Total v3.6.0.
