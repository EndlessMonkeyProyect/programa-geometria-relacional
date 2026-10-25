# Sincronización entre cierres persistentes y expansión de U

**EndLessMonkey · revisión interna 5.9 · anexo de desarrollo matemático · 8 octubre 2026**  
**Autoría del programa:** Le Matt Ansatz Di Ego  
**Estado:** teoremas condicionales en modelo auxiliar; puente con gravedad física **OPEN**.

## 0. Continuidad ontológica y objetivo preciso

Una identidad relacional mantiene su radio particular `r_i` mientras dure su régimen de cierre; la escala global de referencia `L_U(t)` puede variar, y las separaciones `d_ij(t)` pueden hacerlo independientemente. El nuevo contexto `r_i/L_U` distingue información que el contrato entre partículas no distingue. Una *operación de sincronización* es una hipótesis ulterior, no una consecuencia de la comparación. *Singularidad* designa aquí **identidad distinguible persistente**, no divergencia de curvatura.

Esta nota conserva los documentos históricos sobre diferencia relacional, Poisson, estructura estelar y MF80, sin cambiar sus postulados silenciosamente. Intenta derivar obligaciones verificables para una operación de sincronización utilizando solamente definiciones explícitas. No se identifica `L_U` con `||U||`, factor de escala `a(t)`, horizonte de Hubble o radio cosmológico sin contrato operacional.

## 1. Contrato de fases (S0–S2)

Sea `I=[0,∞)`, `L_U(t)>0`, `r_i>0` constante por identidad estable, y `θ_i(t)∈R/(2πZ)` una fase **auxiliar** de comparación, todavía no observable físico identificado. Sean `ω_i` frecuencias propias de las referencias cerradas y `Ω_U(t)` ritmo elegido como referencia global. Una posibilidad ilustrativa sería `Ω_U=c/L_U`; **no** deriva un ritmo gravitatorio ni implica el espín o la frecuencia de Compton.

Sin interacción:

\[
\dot θ_i=ω_i-Ω_U(t).
\]

**Teorema S1 — cancelación de referencia común.** Para `δ_ij=θ_i−θ_j`:

\[
\boxed{\dot δ_{ij}=ω_i-ω_j}. 
\]

*Demostración.* Restar las ecuaciones. En particular, `L_U(t)` no sincroniza por sí mismo frecuencias particulares, incluso si `Ω_U(t)` no es constante. **No-go bajo este contrato**, no un no-go universal de gravedad.

## 2. Generador mínimo para dos identidades (S3–S5)

**Postulado de dinámica auxiliar, no consecuencia del núcleo ontológico.** Introducimos el acoplamiento simétrico `γ w(t)` con `γ>0` (unidad s^-1), `w(t)≥0` adimensional:

\[
\begin{aligned}
\dot θ_1 &= ω_1-Ω_U(t)-γ w(t)\sin(θ_1-θ_2),\\
\dot θ_2 &= ω_2-Ω_U(t)+γ w(t)\sin(θ_1-θ_2).
\end{aligned}
\]

Por resta:

\[
\boxed{\dot δ=Δω-2γ w(t)\sin δ},\quad Δω=ω_1-ω_2.
\]

**Teorema S2 — sincronización con acoplamiento constante.** Si `w>0` es constante, existe una diferencia de fase estacionaria si y sólo si `|Δω|≤2γw`. Para desigualdad estricta, la solución `sin δ_*=Δω/(2γw)` con `cos δ_*>0` es localmente asintóticamente estable; la rama con coseno negativo es inestable. En igualdad, no hay estabilidad asintótica exponencial lineal. La estabilidad se sigue de `d(\dot δ)/dδ=-2γw cosδ`.

**Teorema S3 — fórmula exacta cuando las frecuencias propias coinciden.** Si `Δω=0`, `δ(0)∈(-π,π)` y `w(t)≥0` localmente integrable, entonces:

\[
\boxed{\tan\frac{δ(t)}{2}=\tan\frac{δ(0)}2\,\exp\left[-2γ\int_0^t w(s)ds\right]}.
\]

*Demostración.* `d log|tan(δ/2)|/dt=\dot δ/\sinδ=-2γw` para `δ≠0` y prolongación continua en el equilibrio. Para datos iniciales no triviales en ese intervalo:

\[
\boxed{δ(t)\to0 \quad\Longleftrightarrow\quad \int_0^\infty w(t)dt=+\infty.}
\]

Si la integral es finita, el desfase residual es no nulo en general. No se está demostrando disipación de *energía física*: `1−cosδ` es solo un funcional auxiliar de desajuste.

**Corolario S3a — referencia global en expansión exponencial.** Si `L_U=L_0 e^{Ht}`, `H>0`, y se elige como **hipótesis adicional** `w(t)=w_0(L_0/L_U(t))^p`, `w_0>0`, entonces para `p>0`:

\[
\int_0^\infty w(t)dt=\frac{w_0}{pH}<\infty,
\]

por lo que la sincronización perfecta **no ocurre para un desfase inicial no trivial**, en este modelo. Para `p=0`, la integral diverge, y sí hay convergencia; para `p<0`, también diverge, aunque el acoplamiento crece sin cota. Una expansión homogénea no garantiza sincronía; la ley de interacción decide.

**Corolario S3b — expansión en ley de potencias.** Para `L_U=L_0(1+t/t_0)^a`, `a>0`, y `w=w_0(L_0/L_U)^p`, `p>0`, la integral diverge si y sólo si `ap≤1` (logarítmicamente para `ap=1`). Si `ap>1`, persiste un desfase residual. Es un **umbral matemático de un modelo auxiliar**, no un umbral cosmológico observado.

**Teorema S4 — frecuencias diferentes y acoplamiento evanescente.** Si `Δω≠0` y `w(t)→0`, entonces no puede existir un límite de diferencia de fase constante en un levantamiento continuo a R. En efecto, para tiempos suficientemente grandes, `|2γ w(t) sinδ|<|Δω|/2`, de modo que `\dot δ` conserva el signo de `Δω` y `|\dot δ|>|Δω|/2`. **Sincronización eventual es imposible** bajo ese contrato.

## 3. Extensión a una red (S6)

Para grafo no dirigido con pesos `w_ij=w_ji≥0` y frecuencias iguales, considere el límite **lineal cerca de la sincronía**:

\[
\dot{\boldsymbol θ}= (ω-Ω_U)\mathbf1-γ L_G\boldsymbol θ,\quad
(L_G)_{ii}=\sum_j w_{ij},\ (L_G)_{ij}=-w_{ij}.
\]

Al restar la fase media, `z=(I−\mathbf1\mathbf1^T/N)θ`, queda `\dot z=-γL_G z`. Para un grafo conectado y pesos constantes:

\[
\|z(t)\|\le e^{-γ\lambda_2(L_G)t}\|z(0)\|.
\]

`λ₂>0` describe cierre de fases en la red **finita postulada**. No es el *mass gap* de Yang–Mills, ni la ley de Newton, ni una derivación del espacio físico. El componente de referencia global vuelve a cancelarse.

## 4. Test de referencia versus observabilidad (S7)

Los cocientes `η_i=r_i/L_U`, `η_j=r_j/L_U`, `χ_ij=d_ij/L_U` cambian bajo una reetiqueta `L_U→λL_U` manteniendo `r_i,r_j,d_ij`.

**Lema S5 — invariancia de una referencia arbitraria.** Si la intensidad postulada `w=F(η_i,η_j,χ_ij)` es invariante bajo **toda** reetiqueta `L_U→λL_U`, entonces (cuando `χ>0`) existe `f` tal que:

\[
\boxed{F(η_i,η_j,χ)=f(η_i/χ,η_j/χ)=f(r_i/d_{ij},r_j/d_{ij}).}
\]

*Prueba.* Invariancia exige `F(sa,sb,sc)=F(a,b,c)` para todo `s>0`. Escoger `s=1/c` da el resultado. La escala global desaparece. **Si se pretende un efecto físico propio de `L_U`, hay que dar a esa escala una medición operacional**: no puede ser solo normalización arbitraria del lenguaje.

## 5. Qué se puede cerrar del diccionario hacia la fuente de Poisson (S8)

En el manuscrito histórico se **adopta** `ρ_rel=κ ω_m²ρ_m`, `∇²Φ=4παρ_rel`, `G=ακω_m²`. Hay una justificación dimensional **condicional** que podemos completar sin pretender derivación dinámica:

- `ρ_m` es densidad de masa (`M L^-3`);
- `κ` es volumen específico relacional (`L³ M^-1`);
- `ω_m` es ritmo angular (`T^-1`);
- fuente de Poisson para un potencial específico `Φ` tiene unidades `T^-2`;
- se exige **linealidad en `ρ_m`** y se admiten solo `κ`, `ω_m` y un factor adimensional.

**Teorema S6 — forma monomial forzada por dimensiones y linealidad.** Si `S=C κ^a ω_m^b ρ_m`, con `C` adimensional, y `[S]=T^-2`, entonces `a=1`, `b=2`; así `S=C κω_m²ρ_m`. Si se permiten dependencias adicionales adimensionales, la forma más general es `S=κω_m²ρ_m F(η,χ,\ldots)`. **Análisis dimensional selecciona exponentes, no el mecanismo de gravedad, ni `F=1`, ni la ecuación de Poisson.** Tampoco demuestra que `κ` sea volumen de una celda física.

En la convención histórica **específica** `ω_U=m_pc²/ℏ`, `ω_m²=(1−2^{-n})ω_U²`, `R_V=2^{n/2}ℏ/(m_pc)`, `κ=(4π/3)R_V³/m_p`, se deduce exactamente:

\[
\boxed{κω_m²=\frac{4π}{3}\,2^{3n/2}(1-2^{-n})\frac{ℏ c}{m_p²}}.
\]

Con `n=4`:

\[
\boxed{κω_m²=80π\frac{ℏ c}{m_p²},\qquad G=80πα\frac{ℏ c}{m_p²}}.
\]

En consecuencia la calibración histórica equivale a:

\[
\boxed{α=\frac{1}{80π}\frac{Gm_p²}{ℏ c}=\frac{α_G^{(p)}}{80π}\approx2.35\times10^{-41}}.
\]

Es una identidad interna a esa convención. **No predice `G`** ni es una constante determinada independientemente. Si se adopta la otra convención arquitectónica `m_p=ℏω_m/c²`, cambian los factores de radio y el resultado numérico; el diccionario físico debe elegirse antes de comparar datos.

### Receta condicional para recuperar la fuerza

Si, *además*, se postula un campo potencial específico `Φ` en R³ que cumple `∇²Φ=4πακω_m²ρ_m`, condiciones de contorno apropiadas y aceleración de prueba `a=−∇Φ`, se recupera `a=−GM rhat/r²` para una fuente puntual. La dependencia `1/r²` proviene del operador laplaciano y la geometría 3D asumidos: no surge de una reducción de desfase entre osciladores.

## 6. Separación física indispensable

1. El término `−γw sinδ` es **relajación de fase** en un modelo auxiliar. Disipa un funcional matemático `1−cosδ`; en un sistema cerrado no puede interpretarse como disipación física sin especificar sector receptor y conservación de energía-momento.
2. Igualdad de fases o instantes de coincidencia no implica igualdad de aceleraciones; el principio de equivalencia débil necesita una ley de respuesta de partículas de prueba.
3. La acción Newton–Poisson de `02_DINAMICA_MINIMA_CONSERVATIVA_Y_LIMITES.md` es conservativa bajo sus supuestos; la relajación propuesta aquí no se obtiene de esa acción. Unificar ambas exige un generador conjunto y contabilidad de energía.
4. `LCM(16,15)=240` es un hecho aritmético de pesos cuadrados, no el período común de `ω_m/ω_V=√15`.
5. `L_U` no debe introducir una referencia absoluta espuria; elegir radio de Hubble, factor de escala o horizonte causal genera contratos distintos.

## 7. Determinantes nuevos y falsadores

| Pregunta | Test o criterio | Estado |
|---|---|---|
| ¿La referencia sola sincroniza? | S1: cancelación exacta | `NO-GO` en el contrato |
| ¿Una interacción explícita sincroniza? | S2 y S3, umbral e integral de acoplamiento | `RESOLVED` condicional |
| ¿Expansión puede impedir sincronización? | S3a/S3b, `∫w<∞` | `RESOLVED` condicional |
| ¿Se puede eliminar `L_U` por redefinición? | S5, homogeneidad del comparador | `RESOLVED` condicional |
| ¿Por qué `κ ω_m²ρ_m`? | S6: unidades + linealidad | `RESOLVED` solo como selección dimensional |
| ¿Por qué Laplaciano, carga gravitatoria y `α`? | Debe venir de acción de recierre y fuente identificada | `OPEN` |
| ¿Sincronía implica gravedad, WEP, relatividad? | Faltan fuerza, energía-momento, equivalencia y causalidad | `OPEN` |
| ¿Hay predicción física nueva? | Seleccionar `w` desde cierre, fijar observables y contrastes antes de datos | `OPEN` |

**Resultado:** el lenguaje actual permite construir y falsar mecanismos relacionales de sincronización en sistemas matemáticos. **No autoriza afirmar derivada la gravedad física**. El siguiente salto exige un **generador de recierre que determine `w(L_U,r_i,r_j,d_ij)` y la carga de campo en una misma dinámica conservativa o covariante**, sin fijarlos retrospectivamente con `G`.

## 8. Puente conservativo mínimo y no-go de la «fuerza = desajuste» (S9)

La relajación de fase de §2 no es una ley gravitatoria conservativa. Para separar los conceptos podemos definir **otro** candidato matemático, ahora con acción. Para dos fases con inercia `I>0` (en unidades de energía·tiempo²), y `δ=θ_1−θ_2`, consideremos:

\[
L_\delta=\frac I4\dot δ^2-K(d,L_U)(1-\cos δ), \qquad K>0\ \text{(energía)}.
\]

Si `d,L_U` se tratan como parámetros dados y no hay pérdidas, Euler–Lagrange da:

\[
\boxed{\ddot δ+\frac{2K}{I}\sinδ=0.}
\]

Con `K` constante, el sistema es conservativo: puede oscilar alrededor de `δ=0`, pero **no converge generalmente a `δ=0`** sin amortiguamiento o pérdida de energía hacia otro sector. Si se añade **por postulado** un término disipativo Rayleigh `\mathcal D=(Γ/2)\dotδ²`, `Γ>0`, entonces:

\[
\ddotδ+\frac{2Γ}{I}\dotδ+\frac{2K}{I}\sinδ=0,
\qquad E_\delta=\frac I4\dotδ²+K(1-\cosδ).
\]

Cuando `K=K(t)` depende de una referencia global prescrita desde fuera:

\[
\boxed{\dot E_\delta=-Γ\dotδ^2+\dot K\,(1-\cosδ)}.
\]

Por tanto la expansión de la escala puede intercambiar trabajo con este subsistema. **Conservación total exige dotar de dinámica y energía al sector global o al ambiente**; una función `L_U(t)` impuesta no constituye un universo cerrado.

**Teorema S7 — fuerza nula tras sincronización perfecta para potencial de puro desajuste.** Si se propone que la energía potencial gravitatoria entre los cierres sea exclusivamente

\[
V_{\rm diff}(d,δ,L_U)=K(d,L_U)\,[1-\cosδ],
\]

entonces la fuerza radial instantánea `F_d=−∂V_diff/∂d` satisface

\[
\boxed{F_d\big|_{δ=0}=0}
\]

para **toda** función derivable `K`. *Demostración:* `−∂_d V_diff=−K_d(1−cosδ)`. Por tanto esta elección concreta de «gravedad = costo de diferencia de fase» **no reproduce una atracción newtoniana no nula en estados ya sincronizados**. Es un falsador interno de un candidato, no de la ontología general.

Otra energía, por ejemplo `V=−K(d,L_U)cosδ`, sí permite una fuerza no nula en `δ=0`; pero la forma de `K` queda completamente libre. Elegir `K=Gm_1m_2/d` **introduce el potencial de Newton en la premisa**, no lo deriva del sincronismo. Esta comparación exhibe la obligación principal: **la ley de interacción debe seleccionar tanto el acoplamiento radial como el mecanismo de fase, conservando las identidades y el balance energético**.
