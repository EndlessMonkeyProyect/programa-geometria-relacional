# O57 — La superficie completa del toroide: normalizador común y novedad de forma

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego**  
**21 de octubre de 2026 · Suplemento candidato aditivo sobre O40, O44N, O45, O53, O54, O55 y O56.**  
**Estatutos:** [O] ontología; [D] definición; [T] resultado matemático exacto bajo hipótesis; [E] ensayo numérico; [F] contraejemplo o límite; [A] abierto.

## 0. Resultado y posición dentro del hilo

La propuesta original no considera el vórtice un objeto inmóvil cuyo radio exterior necesariamente aumente. Distingue la *unidad con cierre propio*, sus dos recorridos internos, la referencia que los hace comparables y el *espejo móvil* (cambio de foco, orientación o escala para comparar). El múltiplo que normalizó una relación es el portador **propuesto** de continuidad; una nueva diferencia puede exigir ampliar la familia de relaciones acreditadas. El flujo se mueve y puede deformar las relaciones internas, pero cambiar solo el espejo no altera el fluido.

O54 propuso sostener un plano relacional mediante una perpendicularidad común. O56 encontró la tasa `d(a·b)/dt=2aᵀSb` y dos orientaciones de una perturbación que dan respuestas locales distintas. **O57 descubre una distinción necesaria:** poder escoger ejes perpendiculares *en* un plano no prueba que las relaciones materiales que definen ese plano hayan sido conservadas. Toda métrica positiva de dimensión dos admite bases ortogonales. Debemos comparar las relaciones *antes y después* del transporte, no buscar un par de ejes perpendiculares a posteriori.

El candidato geométrico más fuerte es conservar la **métrica de la superficie material hasta un factor común de escala**; lo que esa normalización no explica queda registrado como *novedad de forma*. Bajo esa definición no se exige que la nueva forma sea igual para toda clase de cierre propio ni que la novedad destruya la singularidad. Se trata de un contrato de comparación más exigente, no de un nuevo axioma del programa.

El experimento [E] muestra que el anillo no perturbado conserva muy bien la perpendicularidad de sus coordenadas materiales, pero **no** conserva su métrica salvo escala. Este resultado prohíbe identificar los 90° con la identidad geométrica completa.

## 1. Desde la narrativa hasta el objeto matemático

**[O]** El toroide dispone de dos ciclos distinguibles: toroidal (recorre el anillo) y poloidal/meridiano (recorre el ducto). La referencia común permite expresar sus relaciones. Si el espejo cambia, se reexpresan las mismas relaciones; si el flujo físicamente deforma la superficie, cambia la estructura de relaciones que debe transportar el siguiente cierre.

**[D]** Tomamos una superficie inicialmente toroidal regular `X₀(φ,θ)` con `0<r<R`, donde

\[
X_0(\phi,\theta)=((R+r\cos\theta)\cos\phi,\,(R+r\cos\theta)\sin\phi,\,r\sin\theta).
\tag{O57.1}
\]

La superficie **material** en el tiempo `t` es `X(φ,θ,t)=F_t(X₀(φ,θ))`, donde `F_t` es el flujo lagrangiano de un campo suave `u`.

Sus tangentes transportadas son `a=∂φX`, `b=∂θX`; su métrica inducida en la superficie es

\[
G_t=\begin{pmatrix}a\cdot a&a\cdot b\\a\cdot b&b\cdot b\end{pmatrix};\qquad G_0>0.
\tag{O57.2}
\]

La perpendicularidad de las líneas originalmente etiquetadas exige `a·b=0` pero no determina `|a|/|b|` ni, por ello, toda la métrica.

## 2. Teorema de deformación métrica material [T]

Sean `u` de clase `C¹` espacial y `X` transportado por `∂t X=u(X,t)`. Defina `S=(∇u+∇uᵀ)/2`. Entonces

\[
\boxed{\partial_t(G_t)_{ij}=2\,(\partial_iX)^\top S(X,t)(\partial_jX),\qquad i,j\in\{\phi,\theta\}.}
\tag{O57.T1}
\]

**Prueba.** `∂t(∂iX)=∂i(∂tX)=(∇u)(∂iX)`. Derivar `∂iX·∂jX`; la parte antisimétrica de `∇u` se cancela al sumar el producto y su transpuesto. ∎

Esto generaliza O54/O56: la evolución de `a·b` es un componente de una ecuación para *toda* la métrica, no un argumento independiente sobre la supervivencia de una singularidad.

## 3. Separación exacta de escala compartida y forma residual [D/T]

Respecto a la métrica inicial, construimos el operador positivo

\[
C=G_0^{-1/2}\,G_t\,G_0^{-1/2} \quad (>0),\qquad
\sigma=(\det C)^{1/4}>0,\qquad
D=\frac{C}{\sqrt{\det C}}.\tag{O57.3}
\]

Entonces, **exactamente**,

\[
\boxed{C=\sigma^2D,\qquad \det D=1.}\tag{O57.T2}
\]

- `σ` es un **normalizador geométrico local de longitud**: factor de escala común extraído de la deformación.
- `D` conserva únicamente la **forma residual** de la transformación de la métrica; es simétrico positivo y tiene determinante uno.
- `D=I` equivale a `G_t=σ²G₀` (*deformación conforme local*, sin anisotropía de la métrica inicial). No exige que `σ` sea el mismo en todos los puntos de la superficie.
- `D≠I` es una diferencia en las relaciones de longitud/ángulo que no se elimina multiplicando toda la geometría local por un mismo número. **Es novedad relativa a ese comparador**, no creación de materia ni pérdida necesaria de identidad.

Esta separación no postula que `σ` sea el **entero `N` o el MCM** de O40/O44N; ambos poseen contratos distintos. `σ` pertenece a la geometría continua y `N` a una familia discreta de fracciones/fases. Un puente entre ellos debe derivarse, no introducirse por semejanza del nombre «normalizador».

Sea `λ₊≥λ₋>0` el espectro de `C`. Como medida adimensional de la diferencia residual definimos

\[
\boxed{\eta=\frac{\lambda_+-\lambda_-}{\lambda_++\lambda_-}\in[0,1),\qquad \eta=0\iff D=I.}\tag{O57.4}
\]

Los autovalores de `C` son independientes de la base ortonormal elegida en el plano inicial; `η` no depende de girar el toroide o renumerar sus direcciones materiales mediante un cambio regular de coordenadas. En el muestreo del laboratorio usamos derivadas centradas de la malla material para estimarlo.

**[T] Espejo de escala exterior.** Sean coordenadas vistas `Y=X/L(t)` con `L(t)>0`, sin deformar la superficie material. Entonces `G_t^{obs}=G_t/L(t)^2` y, al contrastar con `G_0^{obs}`, el operador `C` se multiplica por un único escalar `(L(0)/L(t))²`. Por tanto `σ^{obs}=(L(0)/L(t))σ`, mientras **`D^{obs}=D` y `η^{obs}=η`**. Traslaciones y rotaciones rígidas del espejo dejan `G_t` sin cambios. Son resultados de representación, no nuevas fuerzas ni soluciones físicas.

## 3.1. El complemento perpendicular exigido por la incompresibilidad [T]

Aquí aparece el enlace más directo con la intuición original: el área del plano material y su dirección normal **no evolucionan arbitrariamente de manera independiente** si el fluido es incompresible.

Sea `n` la normal unitaria de la superficie material, `S_T` la restricción de la deformación a sus dos direcciones tangentes, y `J_2=\sqrt{\det C}=\sigma^2` el factor de área de un parche material respecto del instante inicial. La derivada exacta de la métrica y de su determinante da

\[
\boxed{\frac{D}{Dt}\log J_2=\operatorname{tr}S_T.}
\tag{O57.T4a}
\]

Como `∇·u=tr S=0` en Navier–Stokes incompresible,

\[
\boxed{\operatorname{tr}S_T=-n^\top S n,\qquad
\frac{D}{Dt}\log\sigma=-\tfrac12 n^\top S n.}
\tag{O57.T4b}
\]

Además, si una pequeña separación material inicial en dirección transversal se transporta mediante la matriz de deformación `F`, su **componente proyectada sobre la normal actual** cambia por el factor `h_\perp=1/J_2` cuando `det F=1`. Así, en ese contrato local,

\[
\boxed{J_2\,h_\perp=1.}
\tag{O57.T4c}
\]

**Prueba.** En un marco ortonormal tangencial actual, `tr S = tr S_T+n^TSn=0`. El transporte del elemento de área de una superficie material da `D_t\log J_2=tr S_T`, ya sea por la regla de Jacobi aplicada a `det G` y O57.T1 o derivando `|a×b|`. Para un par tangente inicial `a₀,b₀` y una normal `n₀`, el volumen orientado transformado es `det F·det(a₀,b₀,n₀)`; al dividir por el área transformada `|Fa₀×Fb₀|`, la componente normal de `Fn₀` es `det F/J_2=1/J_2`. ∎

**Alcance:** esta es una identidad *local de geometría material y conservación de volumen*, no una fuerza perpendicular adicional ni una garantía de que `D=I`. El factor `h_\perp` no debe confundirse con el radio `r` del ducto ni con un múltiplo entero del programa. El plano tangente puede deformarse anisotrópicamente aun cuando el volumen tridimensional sea constante. La expresión ayuda a identificar **qué relación perpendicular se necesita conservar** sin apelar a una dimensión exterior al sistema.

**[F] Los 90° no bastan.** Con `C=diag(4,1)` se conserva `a·b=0` y, aun así, `η=(4−1)/(4+1)=3/5`; la métrica no es conforme. Una medición del ángulo sola omite parte de la novedad.

**[T, en sentido inverso]** Si durante un intervalo el tensor de deformación restringido al plano material cumple `S|_{T\Sigma}=\alpha I` como forma bilineal (α puede depender de la marca y del tiempo), entonces `∂tG=2αG` y `G_t=e^{2∫α}G_0`. Se conserva `D=I`, mientras puede cambiar la escala. No afirma que Navier–Stokes obligue a cumplir esta condición.

## 4. Predicción local desde la estructura actual [T]

Al inicio `C(0)=I`. En una base tangencial inicialmente ortonormal, denotamos `S_T` la restricción bidimensional de `S`. Por (O57.T1):

\[
C(t)=I+2t S_T(0)+O(t^2),
\tag{O57.5}
\]

si el campo y las trayectorias son suficientemente regulares. Si `s₊≥s₋` son los autovalores de `S_T(0)`, para `t\downarrow0`:

\[
\boxed{\eta(t)=t(s_+-s_-)+O(t^2),\quad
s_+-s_- = \sqrt{(S_{11}-S_{22})^2+4S_{12}^2}.}\tag{O57.T3}
\]

Este **predictor se calcula en el estado inicial**, a partir de la deformación tangencial, y no se ajusta retrospectivamente a `η(t)`. La tasa `s₊−s₋` es escalar y no cambia al rotar simultáneamente el campo y la unidad. En cambio, el valor de la cizalla `S12` por sí solo depende de qué direcciones elegimos.

**Límite:** conservar la tasa inicial no basta para predecir todo el intervalo, pues evoluciona `S_T(t)` y sus componentes, así como la geometría de las trayectorias materiales. Tampoco se ha demostrado un sistema finito autónomo para `(σ,D)` en Navier–Stokes general.

## 5. Simulación de la superficie completa [E]

El ensayo reutiliza, **sin editar**, el resolvedor exploratorio O56 (perfil vorticial de anillo O55): caja periódica de lado `8`, `N=32³`, viscosidad `ν=0.025`, `dt=0.014`, 90 pasos RK2, tiempo final `1.26`. La superficie material está representada por `24×16=384` trazadores sobre un toroide inicial `R₀=1.60`, `r₀=0.48`. Se transportan junto a una marca local adicional de O56. Las tangentes se aproximan mediante diferencias centrales de etiquetas periódicas. El promedio de `η` utiliza el área material inicial como peso. El espejo puramente observacional `L(t)=e^{0.23t}` **no** se realimenta en la PDE.

Se comparan el control sin cizalla y dos perturbaciones solenoidales de igual amplitud `A=0.22`, dirigidas sobre `X` y `Y`, con el mismo perfil sinusoidal vertical. Las preparaciones `X` y `Y` están relacionadas por una rotación de 90° del sistema completo. **Ese parentesco exige igualdad de todos los escalares globales objetivos de la superficie**; no constituye dos experimentos físicamente distintos de ruptura global.

| Observable al tiempo final `t=1.26` | Sin perturbación | Cizalla X | Cizalla Y |
|---|---:|---:|---:|
| `η` media ponderada (anisotropía) | `0.119566` | `0.173516` | `0.173516` |
| RMS de coseno entre tangentes | `0.002693` | `0.103706` | `0.103706` |
| Relación de área superficial material | `1.001660` | `1.005716` | `1.005716` |
| Energía cinética final (promedio) | `0.00270398` | `0.01434113` | `0.01434113` |
| Enstrofía final (promedio) | `0.00728668` | `0.01453421` | `0.01453421` |

**Observación que nos obliga a corregir el criterio anterior.** En el control sin perturbación el RMS del coseno es `0.00269` (casi perpendicularidad), pero la anisotropía media `η=0.11957` **no es pequeña en la misma proporción**. Por tanto el flujo conserva prácticamente las etiquetas ortogonales mientras modifica la relación de longitudes. Esto descarta «se conservan los 90°» como criterio suficiente de reproducción de toda la métrica del toroide.

**Compensación perpendicular:** en las tres preparaciones, se verificó en la superficie inicial `tr S_T + nᵀ S n=0` con error máximo inferior a `2.3×10⁻¹⁶`. Al comparar la tasa de cambio de área medida al primer paso contra la predicción discreta calculada antes de evolucionar (usando la misma aproximación de tangentes por cuerdas), los errores RMS relativos son `1.19%` en el control y `1.17%` en X/Y. No se trata de una prueba de conservación exacta de volumen del *esquema de trazadores*, sino de una comprobación de consistencia a corto plazo.

**Control global de orientación.** Las series `X` e `Y` coinciden en `η` media, percentil 95, máximo, coseno RMS, energía, enstrofía y razón de área dentro de errores de redondeo (`< 5×10⁻¹⁵` en las cifras principales). Tras desplazar el índice toroidal exactamente un cuarto de vuelta, las matrices de `η` sobre la superficie también coinciden con diferencia máxima `1.85×10⁻¹³`. En una marca **sin rotar** se distinguen, como había observado O56: la diferencia local procede de la elección del punto de comparación, no de una nueva identidad física del flujo total.

**Predicción objetiva de corto plazo.** La tasa inicial media calculada antes de simular es `0.1133569` en el control y `0.1560218` en las perturbaciones. El valor observado `η(t)/t` después del primer paso (`t=0.014`) es, respectivamente, `0.1112096` y `0.1553986`, con errores relativos aproximados de `1.9%` y `0.4%`. La predicción es local en tiempo y el error incluye discretización espacial, interpolación y el integrador. Es una comprobación del teorema cinemático en este ensayo, no un nuevo invariante global.

**Importante:** estas cifras provienen de un campo de velocidad pseudoespectral Galerkin con resolución `32³` y trazadores de superficie discretos. No se ha demostrado convergencia de malla para O57, ni se ha acreditado estabilidad del vórtice a tiempos largos o para datos tridimensionales generales. **La superficie rastreada es material, no automáticamente una superficie de vorticidad ni un tubo vorticial material exacto.**

## 6. Novedad, múltiplo y criterio de suficiencia [O/D/F/A]

La descomposición `C=σ²D` muestra *cómo* separar una escala compartida de lo que la escala no resuelve. Sin embargo, no determina un entero nuevo `N'`: el MCM `L=mcm(N,m)` puede refinar rejillas racionales de O40 sin seleccionar una trayectoria física.

Con el mismo toroide inicial y `η(0)=0`, los casos control y perturbado poseen distintas tasas de anisotropía inicial (`0.11336` y `0.15602`). Por ello **una interfaz que recuerde sólo radio, proporción, fase discreta y métrica inicial no predice siquiera la primera tasa de deformación de toda la superficie**. La nueva relación requerida es al menos el tensor de deformación tangencial (o alguna información equivalente para esta consulta). La tasa escalar `s₊−s₋` basta para la *primera derivada derecha de η en un punto inicialmente conforme*, pero no se ha probado que baste para su futuro completo.

**[F] La pérdida de conformalidad no implica desintegración.** Mientras `u` sea suave y el flujo lagrangiano `F_t` sea difeomorfismo, la imagen de una superficie toroidal embebida sigue siendo topológicamente un toroide (aunque su métrica haya cambiado); ello no implica que la vorticidad continúe concentrada sobre ese tubo ni que el campo tenga regularidad global a priori. Así, tres cierres deben quedar distinguidos: métrica conforme, topología material y coherencia física de vorticidad.

**[A] Formulación del puente que falta:** buscar un operador dinámico `\mathcal N` derivado del flujo que actualice `σ` y `D` y conserve una interfaz suficiente para una clase fija de consultas del programa, sin asignar un nuevo múltiplo aritmético a posteriori. Sólo después se podrá preguntar si un control de `D` contribuye a una desigualdad no circular sobre estiramiento o disipación en NS 3D. La lectura de Yang–Mills es una comparación metodológica entre suficiencia, novedad y dinámica; no identifica deformación de superficie con curvatura gauge ni produce gap.

## 7. Registro de estatus

- **[T]** `Ġ=2TᵀST` y la separación `C=σ²D`, `det D=1`, para superficie material suave.
- **[T]** La forma residual `D` es un tensor geométrico: su representación matricial cambia al cambiar de base, pero su espectro y `η` son invariantes. `D` no cambia bajo una escala uniforme del espejo ni una rotación rígida de toda la configuración.
- **[T]** `η(t)/t → s₊−s₋` localmente bajo condiciones suaves y métrica inicial normalizada.
- **[T]** La incompresibilidad obliga a compensar las tasas de área material y de estiramiento normal, sin obligar a que se conserve la forma conforme.
- **[E]** Cálculo `32³`, 384 marcas, 11 verificaciones automáticas y mapas de superficie; resultados limitados por resolución.
- **[F]** Perpendicularidad material no implica métrica preservada hasta escala: contraejemplo algebraico y resultado numérico del control.
- **[F]** Comparadores de métricas iniciales sin gradiente no predicen la evolución de `η` en esta familia.
- **[A]** Normalizador entero dinámico derivado, interfaz suficiente del flujo 3D, estabilidad física del tubo vorticial, regularidad global.

## 8. Instrucciones y archivos

```bash
python codigo/o57_superficie.py
python verificar_integridad.py
```

`resultados/series_o57.csv` registra cada instante de control y los observables globales; `resultados/mapas_superficie_o57.npz` guarda matrices completas de `η` y cosenos para cuatro tiempos representativos; `resultados/resumen_o57.json` resume predictores, comparadores y falsadores. Los gráficos muestran anisotropía global, comparación con predicción temprana y distribución de deformación sobre la superficie.

**Continuidad editorial:** este suplemento se agrega sobre O56. No altera Imagen Total v3.8.1 ni crea una prueba de Navier–Stokes, Yang–Mills o P versus NP.
