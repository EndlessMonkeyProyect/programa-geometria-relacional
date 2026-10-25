# O34 — Atractor de forma y residuo entre escalas en Navier–Stokes 2D

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**20 de octubre de 2026 · Suplemento independiente de investigación**  
**No altera el Núcleo Canónico, la Imagen Total ni O25–O33.**

**Clasificación:** `[O]` lectura ontológica; `[D]` contrato declarado; `[T]` identidad/teorema condicionado; `[C]` resultado clásico de la literatura; `[E]` prueba reproducible; `[F]` falsador; `[A]` cuestión abierta.

## 0. Pregunta y conclusión central

¿Puede el propio flujo conducir configuraciones inicialmente diferentes hacia una **forma común estable**, sin que esa coincidencia haya sido impuesta por una simetría inicial ni por un coeficiente artificial de sincronización?

**Sí, en un sentido matemático preciso.** En Navier–Stokes bidimensional no forzado sobre el plano, la distribución total de vorticidad no negativa y de circulación positiva, observada en coordenadas autosimilares, se aproxima a la forma gaussiana del vórtice de Lamb–Oseen. Puede demostrar una tasa explícita mediante entropía relativa cuando la entropía inicial es finita. La estabilidad asintótica, para una clase incluso más amplia de datos integrables, es un teorema clásico de Gallay y Wayne (2005); **no es un nuevo descubrimiento de dinámica de fluidos**.

Pero **formar una forma global común ≠ sincronizar fases ≠ persistir como dos remolinos separados**. Una reducción de la diferencia a escala normalizada puede coexistir con información persistente en escalas físicas no normalizadas.

## 1. Contrato de la dinámica [D]

Consideramos Navier–Stokes incompresible 2D, con viscosidad `ν>0`, sin forzamiento, dominio `R²`, decaimiento adecuado y vorticidad suave inicialmente no negativa, `ω₀≥0`, `Γ=∫ω₀ dx>0`:

\[
\partial_t\omega+u\cdot\nabla\omega=\nu\Delta\omega,\qquad
\nu>0,\qquad\nabla\cdot u=0,\qquad u=K_{BS}*\omega,
\]

\[
K_{BS}(z)=\frac{z^\perp}{2\pi|z|^2}.
\]

Presuponemos momento espacial de primer orden finito y entropía relativa inicial finita para la cota cuantitativa. El centro global

\[
c=\Gamma^{-1}\int x\,\omega(x,t)dx
\]

es constante, por la antisimetría de Biot–Savart. Elegimos una referencia `t₀>0` arbitraria y fija **antes** de evaluar la trayectoria, no adaptada retrospectivamente:

\[
a(t)=\sqrt{4\nu(t+t_0)},\qquad\xi=\frac{x-c}{a(t)},\qquad
\tau=\ln\left(1+\frac{t}{t_0}\right),\qquad
F(\xi,\tau)=\frac{a(t)^2}{\Gamma}\omega(c+a(t)\xi,t).
\tag{1}
\]

Así `F≥0` y `∫F dξ=1`. La diferencia entre `a(t)` y los radios geométricos `√S_i` de O31–O32, o `R_i` modales de MF-43, es deliberada. No se supone `Rω=v_*` para los vórtices.

## 2. Transformación autosimilar exacta [T]

La homogeneidad `K_{BS}(a z)=a^{-1}K_{BS}(z)` conduce a

\[
\boxed{
\partial_\tau F
=\frac14\Delta_\xi F+\frac12\nabla_\xi\cdot(\xi F)
-\frac{\Gamma}{4\nu}\,(K_{BS}*F)\cdot\nabla_\xi F.
}\tag{2}
\]

La referencia gaussiana normalizada es

\[
\boxed{G(\xi)=\pi^{-1}e^{-|\xi|^2},\qquad\int G=1.}\tag{3}
\]

Es un punto fijo de (2): la parte de Ornstein–Uhlenbeck se anula en `G`, y la velocidad inducida `K*G` es tangencial a sus circunferencias, de modo que `(K*G)·∇G=0`. En variables físicas es el vórtice de Lamb–Oseen con tiempo desplazado:

\[
\omega_G(x,t)=\frac{\Gamma}{4\pi\nu(t+t_0)}
\exp\left(-\frac{|x-c|^2}{4\nu(t+t_0)}\right).
\tag{4}
\]

No es una forma estática en metros: se ensancha y decae en amplitud. Es estable como **forma bajo la transformación de escala**.

## 3. O34-T1 — Entropía decreciente por Navier–Stokes, sin `K` artificial [T/C]

Definamos la entropía relativa y la información de Fisher:

\[
\mathcal H(F\mid G)=\int F\ln(F/G)\,d\xi,
\qquad
\mathcal I(F\mid G)=\int F|\nabla\ln(F/G)|^2d\xi.
\tag{5}
\]

**Identidad:** para solución positiva regular e integraciones justificadas,

\[
\boxed{\frac{d}{d\tau}\mathcal H(F\mid G)=-\frac14\mathcal I(F\mid G)\le0.}\tag{6}
\]

**Demostración:** el operador disipativo de (2) es `1/4 ∇·[F ∇log(F/G)]`, que aporta `−I/4`. Sea `v=K*F`. Como `∇·v=0`, el término advectivo en la derivada de `H` se reduce a un múltiplo de `∫F v·ξ`. Este último se anula exactamente:

\[
\int F(\xi)\,v(\xi)\cdot\xi\,d\xi
=\frac12\iint F(\xi)F(\eta)
(\xi-\eta)\cdot K_{BS}(\xi-\eta)\,d\xi d\eta=0,
\]

pues `z·K_BS(z)=0`. Por tanto **la interacción no lineal del flujo no genera un término residual de entropía**. Es una cancelación exacta, no una suposición de que la no linealidad sea pequeña.

La desigualdad logarítmica de Sobolev gaussiana clásica para `G=π⁻¹e^{−|ξ|²}` indica `H≤I/4`. Junto con (6) y Grönwall:

\[
\boxed{\mathcal H(F(\tau)\mid G)\le e^{-\tau}\mathcal H(F(0)\mid G).}\tag{7}
\]

Por Pinsker, con `||.||₁=∫|.|`,

\[
\boxed{\|F(\tau)-G\|_1\le
\sqrt{2\mathcal H(F(0)\mid G)}e^{-\tau/2}.}\tag{8}
\]

**Supuestos del resultado (7)–(8):** vorticidad de un solo signo, circulación positiva, entropía relativa finita, regularidad/decadencia, 2D sin forzamiento en `R²`. No es un teorema para 3D ni para flujos de vorticidad con signo cambiante. La fuente clásica de la convergencia más general es Gallay–Wayne, no el presente suplemento.

## 4. O34-T2 — Dos formas inicialmente diferentes adquieren una proyección común [T]

Sean `F^A,F^B` dos soluciones normalizadas que parten de datos **diferentes** con entropías iniciales `H_A,H_B<∞`, permitiendo circulaciones originales diferentes, cada una con su propio centro y la **misma regla de escala** `a(t)` (igual `ν,t₀`). Por desigualdad triangular y (8):

\[
\boxed{
\|F^A(\tau)-F^B(\tau)\|_1
\le (\sqrt{2H_A}+\sqrt{2H_B})e^{-\tau/2}
\longrightarrow0.}\tag{9}
\]

Se trata de **dos evoluciones posibles, no de dos remolinos coexistentes en un mismo flujo**. La aproximación de formas entre evoluciones independientes nace de un atractor compartido. No constituye acoplamiento mutuo ni bloqueo de frecuencias.

Incluso si `F₀` no tiene simetría central, la conclusión vale. Ejemplo de mezcla de dos gaussianas en coordenadas `ξ`, con pesos `0.65`, `0.35`, centros `(0.7,0)` y `(−1.3,0)` y anchuras cuadráticas normalizadas `0.6`, `1.2`. Su centro de masa es cero y su tercer momento central en `ξ₁` no se anula. Por ello no posee simetría bajo media vuelta. Una cuadratura Gauss–Hermite estima `H(F₀|G)≈0.4845`: la referencia circular **no estaba impuesta en los datos iniciales**. La estimación numérica no sustituye la demostración universal (7).

## 5. O34-T3 — Dos componentes distintas *dentro del mismo flujo*: familia exacta [T/E]

Para evitar confundir un par de soluciones con un par de componentes simultáneas, damos un caso explícito en un **solo campo**. Sea

\[
\omega(x,0)=\omega_A(x,0)+\omega_B(x,0),\qquad
\omega_i(x,0)=\frac{\Gamma_i}{\pi a_0^2\beta_{i0}}
\exp\Bigl(-\frac{|x|^2}{a_0^2\beta_{i0}}\Bigr),
\]

con `Γ_i>0`, `a₀²=4νt₀` y `β_A0≠β_B0>0`. El campo de velocidades inducido por la **suma radial** es tangencial; la advección de cada componente radial es cero. Por tanto, ambas componentes evolucionan **exactamente bajo el mismo Navier–Stokes 2D** mediante difusión:

\[
\boxed{
\omega_i(x,t)=\frac{\Gamma_i}{\pi (a_0^2\beta_{i0}+4\nu t)}
\exp\left(-\frac{|x|^2}{a_0^2\beta_{i0}+4\nu t}\right).
}\tag{10}
\]

En la escala `a(t)` los perfiles normalizados son gaussianas de parámetro

\[
\boxed{\beta_i(\tau)=1+(\beta_{i0}-1)e^{-\tau}\to1.}\tag{11}
\]

Convergen hacia el mismo `G` aunque **sus circulaciones `Γ_i` sigan siendo distintas y constantes**. Es una construcción de **componentes concéntricas etiquetadas**, no de dos vórtices espacialmente separados. La descomposición en etiquetas no es canónica.

En particular para una gaussiana `G_β=(πβ)⁻¹e^{−|ξ|²/β}`:

\[
\boxed{\mathcal H(G_\beta\mid G)=\beta-1-\ln\beta,\qquad
\mathcal I(G_\beta\mid G)=\frac{4(\beta-1)^2}{\beta}.}\tag{12}
\]

Como `dβ/dτ=1−β`, la identidad (6) se verifica exactamente. La ejecución de `verificar_o34.py` comprueba estas igualdades y las cotas de forma analítica, sin simular numéricamente Navier–Stokes.

**Dato del ejemplo:** con `β_A0=0.55`, `β_B0=1.8`, la distancia `L¹` entre las dos gaussianas normalizadas vale aproximadamente `0.8243415` inicialmente y `0.0454008` en `τ=3`, es decir, `t/t₀=e³−1≈19.0855`.

## 6. O34-T4 — Un residuo que persiste aunque las formas normalizadas converjan [T/O]

Esta es la distinción central para el discurso del programa. En la familia exacta anterior, el **segundo momento físico central**, para cada etiqueta, es

\[
S_i(t)=\frac1{\Gamma_i}\int|x|^2\omega_i(x,t)dx
=a_0^2\beta_{i0}+4\nu t.
\tag{13}
\]

Por tanto, el residuo **en unidades físicas**, entre sus extensiones cuadráticas, persiste exactamente:

\[
\boxed{S_A(t)-S_B(t)=a_0^2(\beta_{A0}-\beta_{B0})\ne0.}\tag{14}
\]

Sin embargo, al dividir por la escala común `a(t)²`:

\[
\boxed{
\frac{S_A(t)-S_B(t)}{a(t)^2}=(\beta_{A0}-\beta_{B0})e^{-\tau}\to0.
}\tag{15}
\]

Así, **el mismo par de estructuras admite una diferencia constante al medir en su referente físico y una diferencia que tiende a cero al compararlo con la escala que crece**. No hay contradicción: son contratos de comparación distintos.

**Lectura [O]:** una proyección puede llegar a mostrar formas indistinguibles sin destruir toda la información que las diferenciaba. El residuo no es ruido ni voluntad ni una prueba de indeterminismo fundamental; es una diferencia que otra referencia todavía permite recuperar. Esta realización de comparación y residuo es consistente con el Núcleo Canónico, pero no demuestra que éste imponga la ley física gaussiana.

## 7. O34-T5 — Cierre propio como punto fijo *normalizado* y límite de esa afirmación [T/O]

La transformación de escala (1) convierte a la evolución en un semigrupo `\mathscr R_τ` sobre perfiles normalizados. Entonces

\[
\boxed{\mathscr R_\tau G=G,\qquad
\|\mathscr R_\tau F_0-G\|_1\to0.}\tag{16}
\]

Esto permite dar un significado operativo preciso a *cierre autosimilar de forma*: **un perfil que se reproduce bajo la regla de evolución y reescalado**. No requiere que el fluido piense, compare conscientemente o elija.

Pero `\mathscr R_τ` depende de la dinámica y de la referencia de escala ya seleccionadas. No es todavía el cierre ontológico primordial; es su posible **realización física**. Tampoco `\mathscr R_τG=G` quiere decir que toda la física se reduce a un único estado o que desaparece la microinformación.

## 8. Controles adversariales y límites [F/A]

1. **Sin viscosidad (`ν=0`)**: las dos gaussianas radiales concéntricas son soluciones estacionarias de Euler para la vorticidad radial; no se deduce convergencia hacia una forma gaussiana nueva por este mecanismo. El balance disipativo pierde su término motor.
2. **Simetría inicialmente impuesta**: el caso de O33 conserva una relación exacta de rotación si existe desde el inicio. El presente teorema no requiere esa simetría inicial: incluso distribuciones con tercer momento asimétrico convergen a `G`.
3. **Fases y frecuencias**: `G` tiene `Q=0` y carece de fase elíptica cuadrupolar. Convergencia a `G` no demuestra un ritmo `p:q`, bloqueo de fase, `R_iω_i=v_*` universal ni una regla de sincronización de remolinos.
4. **Identidades separadas**: en el régimen asintótico sobre todo `R²`, puede perderse la existencia de dos núcleos localizados separados. El atractor es una forma del **campo total**, no un teorema de supervivencia independiente de cada remolino.
5. **Datos con signos cambiantes**: la entropía probabilística no aplica. La convergencia de datos integrables generales en el plano se apoya en teoremas externos (Gallay–Wayne), con otras técnicas y calificaciones.
6. **3D, límites, fuerzas**: el término de estiramiento de vorticidad, los bordes, una fuerza externa o una geometría periódica requieren una nueva demostración.
7. **Radios y c**: `a(t)` es un radio difusivo escogido del NS; no es el radio del programa, ni un horizonte causal, ni deriva la velocidad de la luz.
8. **Originalidad**: las ecuaciones de vorticidad, el atractor de Oseen, el método de entropía y el criterio de normalización forman parte de conocimiento matemático establecido. La novedad que se investiga en el programa es la **articulación formal con la ontología de comparación y residuo**, no reclamar una nueva solución al problema de Navier–Stokes.

## 9. Obligación pendiente: dos núcleos separados que se acoplan sin fusionarse [A]

Para resolver el problema más fuerte que motivó O28–O33 habría que exhibir, para un sistema de dos vórtices no concéntricos e inicialmente incompatibles, una relación de fase o forma `ψ` cuyo campo inducido por Navier–Stokes exhiba contracción transversal y que además preserve una firma de identidad de **cada** núcleo en una ventana especificada. Debe incluir estabilidad bajo perturbaciones, sin postular una constante `K`, y comparar contra los casos que se mezclan hacia un solo Oseen. Las ecuaciones aquí no alcanzan esa meta.

En particular, un punto fijo gaussiano global **no sustituye** el teorema de persistencia separada de O31–O32. Son destinos dinámicos diferentes.

## 10. Antecedentes y bibliografía

- Programa de Geometría Relacional: Núcleo Generativo Canónico, comparación `C(a,b)=(q,r)`, complemento antes de ortogonalidad; MF-43 sobre modo y ritmo relacional.
- O26: limitación de interfaces espectrales truncadas para continuación futura.
- O28–O29: compatibilidad modular y acoplamiento endógeno; O30: balance de formas y centros; O31–O32: persistencia finita; O33: preservación de simetría estructural preexistente.
- **Gallay, T. y Wayne, C. E.** (2005), *Global stability of vortex solutions of the two-dimensional Navier–Stokes equation*, Communications in Mathematical Physics 255, 97–129. https://arxiv.org/abs/math/0402449 . **Fuente clásica principal** de convergencia al atractor de Oseen.
- **Gallay, T. y Maekawa, Y.** (2018), *Existence and stability of viscous vortices*, Handbook of Mathematical Analysis in Mechanics of Viscous Fluids. https://arxiv.org/abs/1610.08384 . Revisión sobre estabilidad, interacción y diferencias entre 2D/3D.
- Desigualdad logarítmica de Sobolev gaussiana y desigualdad de Pinsker: herramientas de análisis clásico, utilizadas como lemas externos, no resultados nuevos del programa.

**Tesis final O34:** la dinámica puede producir una forma común que no estaba impuesta por la simetría inicial. Esa normalización puede hacer indistinguible una diferencia que conserva valor en una escala anterior. La emergencia de una forma común no demuestra, por sí sola, que dos remolinos independientes hayan sincronizado sus ritmos o conservado sus identidades separadas.
