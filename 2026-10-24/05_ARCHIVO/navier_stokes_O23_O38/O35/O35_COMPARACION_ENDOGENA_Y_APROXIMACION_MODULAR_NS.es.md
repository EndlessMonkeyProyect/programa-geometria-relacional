# O35 — Acercamiento modular endógeno de dos formas vorticiales

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**Fecha:** 20 de octubre de 2026 · **Estado:** suplemento independiente, *no modifica* la Imagen Total ni el Núcleo Canónico.  
**Clave epistémica:** `[D]` definiciones/hipótesis; `[T]` identidad o teorema; `[E]` experimento computacional de integrales; `[F]` adversario/no-go; `[O]` correspondencia ontológica; `[A]` abierto.

## 0. Pregunta y declaración de resultado

¿Puede la dinámica de Navier–Stokes hacer que dos remolinos inicialmente distintos **reduzcan una diferencia relacional propia**, sin que exista previamente simetría de sus orientaciones y sin postular un coeficiente de sincronización `K`? Sí: para dos gaussianas elípticas de vorticidad del mismo signo, inicialmente separadas, se demuestra por la interacción lejana de Biot–Savart que hay orientaciones para las que la **diferencia de fases cuadrupolares disminuye inicialmente**, y orientaciones espejo para las que aumenta. La fase relativa no está inicialmente bloqueada. Por continuidad, los signos persisten durante **algún intervalo temporal no nulo** y las etiquetas siguen espacialmente distinguibles durante un intervalo suficientemente corto.

**No se demuestra** convergencia posterior hasta fase igual, bloqueo estable, órbitas periódicas rígidas, persistencia eterna de dos núcleos, fusión ni Navier–Stokes 3D. Los términos “módulo”, “comparación”, “forma propia” y “cierre” no indican actos cognitivos de los remolinos.

## 1. Contrato físico [D]

En el plano infinito `R²`, para viscosidad `ν>0`, vorticidad suave `ω=ω_A+ω_B` no negativa:

\[
\partial_t\omega+u\cdot\nabla\omega=\nu\Delta\omega,\qquad
\nabla\cdot u=0,\qquad
u=K_{BS}*\omega,\quad K_{BS}(x)=\frac{Jx}{2\pi|x|^2}.
\]

Cada etiqueta satisface transporte-difusión por **la misma** velocidad total `u`: `∂t ω_i + u·∇ω_i = ν Δω_i`. Cada circulación `Γ_i=∫ω_i` permanece positiva y constante. El etiquetado representa una descomposición elegida en el dato inicial, no un detector ontológico único de remolinos.

Para cada etiqueta se definen centro `c_i`, segundo momento `S_i` y cuadrupolo complejo:

\[
c_i=\frac1{\Gamma_i}\int x\omega_i\,dx,\quad
S_i=\frac1{\Gamma_i}\int |x-c_i|^2\omega_i\,dx,\quad
Q_i=\frac1{\Gamma_i}\int (z-C_i)^2\omega_i\,dx.
\]

`z=x₁+ix₂`, `C_i=c_{i1}+ic_{i2}`. Si `Q_i ≠0`, `φ_i=arg Q_i` es **fase de la forma** y la orientación de su eje es `φ_i/2 mod π`. No es la fase de giro material. No hay garantía de fase para un vórtice circular, para el que `Q_i=0`.

La ecuación exacta de O29–O32 es

\[
\boxed{\dot Q_i=\frac2{\Gamma_i}\int(z-C_i)(u_1+iu_2)\omega_i\,dx.}\tag{1}
\]

La difusión no aparece **explícitamente** en (1) porque `Δ(z−C)²=0`; influye indirectamente al cambiar el campo.

## 2. Una fase relacional invariante al marco orientado [D/T]

Sea `r=c_A−c_B`, con `r≠0`, y `α=arg(r)`. Para números coprimos positivos `p,q`, definimos

\[
\boxed{\Psi_{p:q}=q\,\arg Q_A-p\,\arg Q_B-2(q-p)\arg r\pmod{2\pi}.}\tag{2}
\]

**Teorema T1.** Bajo giro de las coordenadas en ángulo `β`, `Q_i→e^{2iβ}Q_i`, `r→e^{iβ}r`; los términos suman `2qβ−2pβ−2(q−p)β=0`. Por ello `Ψ` es invariante bajo giro común de marco. Además, sin giros externos:

\[
\boxed{\dot\Psi_{p:q}=q\Im(\dot Q_A/Q_A)-p\Im(\dot Q_B/Q_B)-2(q-p)\Omega_{orb},\qquad
\Omega_{orb}=\Im(\dot r_c/r_c).}\tag{3}
\]

`r_c=r_x+i r_y` y la derivada de `r` es la derivada relativa de los centros calculada por O30 desde Biot–Savart. En el canal `p=q=1` basta `ψ=φ_A−φ_B`.

Definimos error relativo de fase **sin definir energía física**:

\[
\boxed{E_{rel}=1-\cos\Psi_{p:q},\qquad
\dot E_{rel}=\sin\Psi_{p:q}\,\dot\Psi_{p:q}.}\tag{4}
\]

Por lo tanto, `dot E_rel <0` significa **acercamiento instantáneo al canal seleccionado**. No es lo mismo que bloqueo ni atractor. Cuando `p≠q`, la referencia orbital en (2) resulta imprescindible; usar `qφ_A−pφ_B` sin ella dependería de cómo orientamos los ejes.

## 3. Gaussianas elípticas como datos exactos de Navier–Stokes [D]

Para semiejes de desviación estándar `a>b>0`, circulación `γ>0`, ángulo `θ` y centro `c`, declaramos

\[
\omega_{c,\theta}(x,0)=\frac{\gamma}{2\pi\sqrt{\det\Sigma_\theta}}
\exp\left[-\frac12(x-c)^\top\Sigma_\theta^{-1}(x-c)\right],\quad
\Sigma_\theta=R_\theta\operatorname{diag}(a^2,b^2)R_\theta^\top.
\]

Para cada forma, `S=a²+b²`, `Q=(a²−b²)e^{2iθ}` y `Γ=γ`. Como datos lisos y localizados generan solución regular 2D para todo tiempo, pero a continuación **solo** se usan derivadas instantáneas y continuidad local.

Se fijan centros `c_A=(-d/2,0)` y `c_B=(d/2,0)`, `θ_A=0`, `θ_B=\mp\vartheta` donde `0<ϑ<π/2`, `γ_A=γ_B=γ`. No se impone equivalencia de orientaciones, así que `ψ(0)=\pm2ϑ≠0`.

## 4. Cálculo exacto del autoacoplamiento [T2]

La contribución del propio núcleo a (1) se escribe, por antisimetría del núcleo de Biot–Savart y dos variables gaussianas independientes `X,Y`,

\[
\dot Q_i^{self}=\gamma\,\mathbb E\left[D_c K_{BS,c}(D)\right],\qquad D=X-Y,
\]

donde `D_c=D_x+iD_y`, `K_{BS,c}=i D_c/(2π|D|²)` y `D\sim N(0,2Σ_θ)`.

La integral angular gaussiana se evalúa exactamente:

\[
\mathbb E\frac{D_c^2}{|D|^2}=e^{2i\theta}\frac{a-b}{a+b},\quad
\boxed{\dot Q_i^{self}=\frac{i\gamma}{2\pi}\frac{a-b}{a+b}e^{2i\theta}}.\tag{5}
\]

Por división por `Q`:

\[
\boxed{\Im\frac{\dot Q_i^{self}}{Q_i}=\frac{\gamma}{2\pi(a+b)^2}.}\tag{6}
\]

Dos elipses con los mismos semiejes y circulación poseen idéntico aporte propio a la **tasa de fase**, independientemente de su orientación; en la diferencia `dot ψ` se cancelan exactamente. El signo de la comparación surge por el acoplamiento cruzado.

## 5. Derivación de la interacción lejana [T3]

Para separación `d` grande respecto de `a,b`, la expansión del campo inducido por cada núcleo alrededor del centro del otro produce un gradiente de primer orden

\[
\nabla u_B(c_A)=\frac{\gamma}{2\pi d^2}
\begin{pmatrix}0&-1\\-1&0\end{pmatrix}+o(d^{-2})
\]

para `r` orientado sobre el eje horizontal. La derivada de la parte constante no cambia `Q_i` por la identidad `∫(z−C_i)ω_i=0`. Al aplicar (1) al término lineal obtenemos

\[
\boxed{\dot Q_i^{cross}=-\frac{i\gamma S}{\pi d^2}+o(d^{-2}),\qquad i=A,B.}\tag{7}
\]

El resto `o(d^{-2})` se justifica por momentos finitos de las gaussianas: expandir en la región central `|x-c_i|+|y-c_j|<d/2` y controlar el complemento por su cola exponencial; la singularidad integrable del núcleo no invalida el límite. **No se afirma (7) como igualdad exacta a distancia finita.**

Con `D_Q=a²−b²>0`, `S=a²+b²`, `θ_A=0`, `θ_B=±ϑ`, y (6) cancelada,

\[
\boxed{
\dot\psi(0)=-\frac{\gamma S}{\pi D_Q d^2}[1-\cos(2\vartheta)]+o(d^{-2})<0
}\tag{8}
\]

para separaciones suficientemente grandes. El signo es estrictamente negativo para cualquier `ϑ∈(0,π/2)` fijo. **Dos configuraciones adversarias:**

- `θ_B=−ϑ` da `ψ(0)=+2ϑ`, `sin ψ>0` y `dot E_rel(0)<0` (acercamiento inicial).
- `θ_B=+ϑ` da `ψ(0)=−2ϑ`, `sin ψ<0` y `dot E_rel(0)>0` (alejamiento inicial).

Las formas poseen los **mismos semiejes, circulaciones, radios cuadráticos y separación**; el signo depende de la orientación relacional. Aquí tenemos un testigo físico de que los radios no agotan la relación, sin postular `Rω=v_*` para remolinos materiales.

## 6. Cuadratura exacta de la derivada, evaluación numérica [E]

Para evitar depender solo de la aproximación asintótica, evaluamos la contribución cruzada **exacta de la derivada instantánea de NS** para gaussianas. Sean `X_A~N(c_A,Σ_A)`, `X_B~N(c_B,Σ_B)`, `D=X_A−X_B~N(r,Σ)`, `Σ=Σ_A+Σ_B`, `B=Σ_AΣ^{-1}`, `e=(1,i)^T`. Por regresión gaussiana,

\[
\mathbb E[X_A-c_A\mid D]=B(D-r),
\]

y, en notación compleja,

\[
\boxed{\dot Q_A^{cross}=\frac{i\gamma}{\pi}\mathbb E_D
\frac{(e^TB(D-r))(e^TD)}{|D|^2}.}\tag{9}
\]

Análoga expresión corresponde a `B` intercambiando las etiquetas. El script evalúa (9) mediante dos rutas independientes: **transformada de Laplace** (`1/|D|²=∫₀∞e^{−s|D|²}ds`) y **cuadratura bidimensional Gauss–Hermite** sobre `D` con media `r` y covarianza `Σ`. No integra temporalmente la PDE.

Para `a=.9`, `b=.5`, `γ=1`, `d=6`, `θ_A=0`, `ν=.02` (que no entra explícitamente en la derivada inicial):

| Dato B | `ψ(0)` | `dot ψ(0)` | `dot E_rel(0)` | Lectura |
|---|---:|---:|---:|---|
| `θ_B=−.35` rad | `+.70` | `−0.004750381` | `−0.003060279` | Acercamiento inicial |
| `θ_B=+.35` rad | `−.70` | `−0.004750381` | `+0.003060279` | Alejamiento inicial |

La coincidencia de cuadraturas verifica los valores numéricos dentro de tolerancia; el **signo para distancias suficientemente grandes es teorema por (8)**. Para `d=6` los signos son **resultado de evaluación numérica**, no de una cota certificada con aritmética de intervalos.

El límite predicho en ambos casos es

\[
\lim_{d\to\infty}d^2\dot\psi=-\frac{1.06}{\pi(0.56)}(1-\cos0.7)\approx-0.14168614285.
\]

El control numérico `d=80` coincide a error menor que `0.001`.

## 7. El intervalo temporal y la preservación de diferencias [T4]

**Proposición.** Para los datos gaussianos en el canal de **acercamiento**, y para distancia inicial `d` suficientemente grande (en particular en una región abierta de parámetros donde se demuestra (8)), existe `T>0` tal que simultáneamente:

1. `E_rel(t)` decrece estrictamente en `[0,T]`.
2. `Q_A(t)` y `Q_B(t)` siguen distintos de cero y, por lo tanto, cada etiqueta conserva una firma de forma cuadrupolar.
3. Dos discos disjuntos contienen cada uno al menos el `75 %` de la circulación de su etiqueta.

**Prueba.** La derivada de `E_rel` es inicialmente negativa y es continua para soluciones suaves con `Q_i(0)≠0`; permanece negativa en algún intervalo `[0,T_1]`. Por continuidad, `Q_i(t)≠0` para `[0,T_2]`. Inicialmente `S_i(0)=1.06` y `d>4\sqrt{1.06}`; O31-T4 con `k=2`, la cota `U_0` y las funciones de extensión concede un intervalo `[0,T_3]` con discos disjuntos conteniendo al menos `75 %` de cada etiqueta. Basta tomar `T=min(T_1,T_2,T_3)>0`. Esto prueba existencia, **no calcula T** ni garantiza convergencia a cero de `E_rel`. QED.

Es un ejemplo de **cambio relacional en el mismo flujo con persistencia temporal de las diferencias propias**. No sería correcto denominarlo “atractor de sincronización”, y la etiqueta difusa no es un contorno material rígido.

## 8. No-go: no existe par periódico rígido exacto sin cambio de escala [T5/F]

Si la circulación total es `Γ>0` y la vorticidad no negativa tiene segundo momento finito, el centro global `C` es constante y

\[
\boxed{I(t)=\int|x-C|^2\omega(x,t)\,dx=I(0)+4\nu\Gamma t.}\tag{10}
\]

Una traslación y una rotación rígidas preservan la varianza central `I`. Por tanto, si `ν>0` y `T>0`, **no puede** cumplirse que toda la configuración vorticial se repita exactamente después de `T` únicamente tras trasladarse y rotarse. Se obtendría simultáneamente `I(t+T)=I(t)` y `I(t+T)-I(t)=4νΓT>0`, contradicción.

Esta restricción no prohíbe formas que se repitan aproximadamente, sincronización relativa durante un intervalo, autosimilitud con **dilatación**, forzamiento, ni condiciones de contorno distintas. Para un caso de la tabla con `ν=.02`, `Γ=2`, la tasa `dot I=0.16` es positiva.

**Lección:** “frecuencia común” no debe confundirse con “estructura rígida periódica idéntica”. La disipación impone comparación de escalas.

## 9. Qué se acredita y qué no se acredita [O/A]

| Acreditado | No acreditado |
|---|---|
| La forma cuadrupolar tiene ecuación exacta en NS 2D | Una forma cuadrupolar representa íntegra cada identidad |
| Existe canal modular 1:1 invariante ante rotación | La ley `Rω=v*` se aplica a cualquier remolino |
| Ciertas orientaciones producen acercamiento local por NS | Los remolinos necesariamente sincronizan sus fases |
| Existen intervalos con acercamiento y dos concentraciones todavía distintas | Coexistencia eterna de dos núcleos |
| La viscosidad impide repetición rígida exacta de toda la vorticidad positiva | Imposibilidad de patrones autosimilares o cuasiperiódicos |
| La forma/posición del par altera el signo de la comparación | Una ley universal de cierre físico, regularidad NS 3D o nueva fuerza |

**Lectura relacional:** la comparación no necesita un agente. Los mismos módulos radiales permiten resultados distintos porque la **información de orientación relativa** forma parte de la configuración. Aquí la nueva relación puede empezar a aproximarse sin extinguir la identidad de las dos poblaciones. La ontología sugiere preguntas; no sustituye los cálculos de Navier–Stokes.

## 10. Próximo discriminante: de acercamiento a verdadero cierre

Una prueba de atracción genuina exige deducir, para una región abierta de datos (no solo simetrías exactas ni un instante), una desigualdad del tipo

\[
\dot E_{rel}(t)\le-\lambda E_{rel}(t),\qquad \lambda>0,
\]

para un horizonte declarado y acompañado de una condición que conserve dos formas distinguibles. Actualmente no se ha demostrado. Esta desigualdad debe surgir de (1), el operador Biot–Savart y los momentos superiores de forma; no debemos imponer una `K` retrospectiva ni extrapolar el signo inicial a todo tiempo. También habrá que evaluar el canal `p:q` en un marco orbital y ensayar controles con vórtices circulares, contra-rotantes y formas con igual cuadrupolo pero diferente estructura de cuarto orden.

## 11. Fuentes y antecedentes

Internos: núcleo generativo canónico (comparación/residuo); MF-43 (ritmo lógico y límites físicos); O25–O34, especialmente O30, O31, O32, O33, O34. La Imagen Total no fue editada.

Externos (resultados de análisis vorticial preexistentes, no se reclama prioridad física):

- Thierry Gallay, *Interaction of vortices in viscous planar flows*, arXiv:0908.2518, https://arxiv.org/abs/0908.2518 (interacciones, núcleo deformado, límite inviscido de colección de vórtices).
- Thierry Gallay y C. Eugene Wayne, *Invariant manifolds and the long-time asymptotics of the Navier–Stokes and vorticity equations on R²*, arXiv:math/0102197, https://arxiv.org/abs/math/0102197 (asintótica y perfiles en variables auto-similares; contraste con O34).

**Conclusión O35.** Existen configuraciones de dos remolinos suaves y separados cuya dinámica produce inicialmente una **disminución de una diferencia modular de forma**, manteniéndose ambos distinguibles durante algún intervalo. El resultado inverso para la orientación reflejada impide declarar una regla universal basada solo en los radios. Una relación que comienza a ajustarse no es todavía un nuevo cierre propio estable.
