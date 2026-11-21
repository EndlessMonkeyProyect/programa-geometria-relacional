# Resolución entre escalas, granularidad y resto funcional
## Puente verificable entre herencia, economía de consultas y la vía aritmética a Riemann

**20 de noviembre de 2026 · Anexo de revisión matemática**  
**Estado ROSI:** resultados exactos y controles adversariales **RESOLVED** en sus contratos; transferencia a la hipótesis de Riemann **OPEN**.  
**Alcance:** no contiene ni anuncia una demostración de la hipótesis de Riemann (RH).

## Resumen

Una referencia puede resolver una pregunta sin reconstruir su interior; una nueva referencia puede conservar la identidad anterior y añadir distinciones. Esta estructura aparece en los contratos de cierre propio y economía computacional (MF–86, CR–6), en el normalizador con resolución finita y el hiperboloide de O58 (G–01, v1.3) y en la criba e interfaz funcional de R–01/R–03. **La coincidencia de operaciones no establece identidad de errores.** Se precisa aquí el tipo de mapeo que permitiría trasladar una ley de granularidad al error funcional de Báez-Duarte y se muestran controles que impiden inferencias automáticas.

Las contribuciones de esta nota son una **tabla tipada de correspondencias**, un **certificado de tres ventanas para controlar la norma**, un **teorema de transferencia condicional con cuantificadores**, dos **obstrucciones explícitas a la transferencia automática**, un **criterio finito por proyecciones de Gram**, y controles reproducibles. Las equivalencias con RH y las barreras conocidas de aproximación pertenecen a la literatura clásica.

## 1. Procedencia y contratos que no deben confundirse

| Rama | Referencia y observable | Grano o resto | Resultado exacto disponible | No se deduce |
|---|---|---|---|---|
| G–01 §2B | Razones `α`, precisión `ε`, menor denominador admisible `q_ε(α)` | Resolución de consulta `ε` | `q_ε(α) ≤ ⌈1/ε⌉` por Dirichlet | Un error `L²` sobre funciones de zeta |
| O58 / G–01 §2D | Enteros `a,b,N` con `a²+b²+1=N²` | `r_N=1/N²`, unidad pendiente cuadrática | Para cualquier sucesión válida `N_k→∞`, `r_{N_k}→0`; hiperboloide y continuaciones enteras | Elección única del sucesor o cota del error de Riemann |
| Cierre propio, E9, MF–86 y CR–6 | Firma `Φ`, preguntas `Q` y continuaciones | Una nueva clase distinguible; interfaz suficiente | `q=\bar q∘Φ` caracteriza suficiencia; composición exacta bajo fronteras declaradas | Densidad de un **espacio lineal** de funciones arbitrario |
| Economía 19-XI | Referencias primas; consulta `q` | Diferencia nueva relativa a la consulta | CRT: nueva coordenada módulo `p`; la misma novedad puede ser redundante para otra consulta | Que cada primo reduzca la distancia funcional |
| R–01/R–02 y R–03 | Criba finita `S`, discrepancia `E_S` y transformada `F_S` | Resto de criba, no resto de O58 | `F_{S∪{p}}=(1-p^{-s})F_S`, factor sin ceros para `0<Re(s)<1` | Ubicación de ceros en `Re(s)=1/2` |
| R–RH–01 | `χ=1_(0,1]`, `f_n(x)={1/(nx)}` y `W_m` | `e_m²=dist_{L²}(χ,W_m)²` | Monotonía, balance de proyecciones; criterio RH de Báez-Duarte | `lim e_m=0` sin una cota global adicional |

**Precisión física:** `C` en G–01 es un horizonte de comparación en un contrato geométrico; no es la línea crítica de la zeta. `ε` es una tolerancia de consulta, `1/N²` una fracción algebraica y `e_m²` un error integral. No comparten unidades ni operaciones por definición.

## 2. Un contrato común de resolución (definición; no teorema de equivalencia)

Una instancia de resolución se declara mediante `\mathcal R=(X,Q,Φ_λ,\mathcal A_λ,\nu, T_λ)`:

* `X`: estados o funciones admisibles;
* `Q`: preguntas observables;
* `Φ_λ`: representación disponible a resolución `λ`;
* `\mathcal A_λ`: decodificadores permitidos para responder desde esa representación;
* `ν`: noción explícita de error/costo;
* `T_λ`: regla de continuación, con dominio y garantías de conservación declarados.

Una firma es **suficiente** para `q∈Q` cuando `q=\bar q∘Φ_λ` para algún decodificador permitido. Al restringir decodificadores a combinaciones lineales, el criterio es más exigente que permitir todas las funciones de la firma. La herencia se acredita mostrando mapas y conmutatividad de las continuaciones; la convergencia de los errores exige además uniformidad respecto de `λ`.

### Ejemplo exacto: suficiencia no equivale a cierre lineal

Sea `X={0,1,2}` con medida uniforme, `Φ(x)=x`, y `q(x)=x²`. Toda la respuesta se reconstruye **exactamente** mediante `q=Φ²`; la interfaz es suficiente. Pero el mejor aproximante a `q` en `span{1,Φ}` es `a(x)=2x−1/3`, y su error cuadrático es

\[
\frac13\sum_{x=0}^{2}(q(x)-a(x))^2=\frac{2}{9}>0.
\]

La representación distingue cada estado, pero la clase **lineal** de operaciones permitidas no reconstruye la pregunta. Esta es una obstrucción directa a trasladar suficiencia de CR–6 a la distancia en el span lineal de R–RH–01 sin mostrar un entrelazador que preserve la clase de operadores.

## 3. El límite algebraico exacto de G–01/O58

Las ternas `(2,2,3)`, `(4,8,9)` y `(12,12,17)` cumplen `a²+b²+1=N²`. En particular,

\[
\frac{a^2+b^2}{N^2}+\frac1{N^2}=1,
\qquad
\text{y, si }N_k\to\infty,\quad \frac1{N_k^2}\to0.
\]

**Control sobre el «único camino».** Desde `(2,2,3)` hay al menos dos sucesores distintos en el árbol documentado de G–01: `(4,8,9)` y `(12,12,17)`. **Un padre recuperable de manera única no equivale a una continuación futura única.** La solución nueva no puede ser cualquier número, pero las restricciones aritméticas admiten ramificaciones. La unicidad requerida por una aplicación concreta debe probarse bajo su propio contrato de selección.

El normalizador de G–01 con precisión `ε` también tiene una cota finita `q_ε(α)≤⌈1/ε⌉`. No hay en ese teorema una relación entre `ε`, `N_k` y el índice `m` de la aproximación funcional a RH.

## 4. Aritmética prima: novedad e invariancia son observables distintos

Para un conjunto finito de primos `S`, sea `M_S=∏_{p∈S}p`. Añadir `p∉S` produce por CRT

\[
\mathbb Z/(M_Sp)\mathbb Z\cong\mathbb Z/M_S\mathbb Z\times\mathbb Z/p\mathbb Z.
\]

La nueva coordenada módulo `p` no está determinada por la anterior. En cambio, para la transformada de Mellin de la discrepancia de criba,

\[
F_S(s)=\frac{\zeta(s)}s\prod_{p\in S}(1-p^{-s}),
\quad F_{S\cup\{p\}}(s)=(1-p^{-s})F_S(s).
\]

El factor nuevo no se anula en `0<Re(s)<1`. Por tanto **las posiciones y multiplicidades de los ceros no cambian al añadir ese primo**. La novedad de la referencia es real respecto de los residuos, pero su acción sobre el observable «conjunto de ceros» es invariante. Se evita así la inferencia «primo nuevo ⇒ toda pregunta obtiene una reducción estricta del error».

### Puente con las funciones fraccionarias

Sea `A_S(x)=#{1≤n≤x:(n,M_S)=1}`, `δ_S=∏_{p∈S}(1-1/p)` y `E_S(x)=A_S(x)-δ_Sx`. Con `f_d(t)={1/(dt)}` se obtiene por inclusión-exclusión

\[
G_S(t):=-E_S(1/t)=\sum_{d\mid M_S}\mu(d)f_d(t).
\]

La inversión sobre subconjuntos de primos permite recuperar los `f_d` con índice libre de cuadrados a partir de los `G_S`; este es un puente **lineal exacto** con la familia aritmética de R–RH–01, no una cota de error. La versión de trabajo R–03 v0.4 expone este puente; no reemplazarla automáticamente por la v0.3 pública.

## 5. Contrato funcional de Riemann y el error pendiente

En `H=L²((0,∞),dx)`, defínanse

\[
\chi(x)=\mathbf 1_{(0,1]}(x),\quad f_n(x)=\left\{\frac1{nx}\right\},\quad
W_m=\operatorname{span}\{f_n:1\le n\le m,\ \mu(n)\ne0\},\quad
 e_m=\operatorname{dist}(\chi,W_m).
\]

Por el criterio clásico de Báez-Duarte y el puente de índices libres de cuadrados utilizado en R–03 v0.4,

\[
\boxed{\mathrm{RH}\iff\lim_{m\to\infty}e_m=0.}
\]

Las proyecciones `P_m` permiten escribir para `m<n`:

\[
e_m^2-e_n^2=\|(P_n-P_m)\chi\|^2\ge0.
\]

La igualdad es exacta para los subespacios anidados, sin apelar a RH. No proporciona por sí misma una cota inferior positiva proporcional a `e_m²`.

### Teorema V — Certificado de tres ventanas (exacto; nuevo contrato de prueba)

Sean `a_m(x)=∑_{n≤m} c_{m,n} f_n(x)` y `B_m(x)=χ(x)−a_m(x)`. Defínanse los dos costos observables de la representación

\[
L_m=\sum_{n\le m}|c_{m,n}|,\qquad
C_m=\sum_{n\le m}\frac{c_{m,n}}n.
\]

**Proposición V.** Para cualquier `0<δ≤1≤R`,

\[
\boxed{
\|B_m\|_2^2\le
\delta(1+L_m)^2+
\int_\delta^R|B_m(x)|^2\,dx+
\frac{|C_m|^2}{R}.}
\tag{V}
\]

*Prueba.* En `0<x<δ`, la desigualdad `0≤f_n(x)<1` implica `|B_m(x)|≤1+L_m`; por tanto la integral de ese sector no excede `δ(1+L_m)^2`. Para `x>R≥1`, la identidad exacta `f_n(x)=1/(nx)` y `χ(x)=0` da `B_m(x)=−C_m/x`, cuya integral cuadrática es `|C_m|²/R`. El sector central se deja intacto. La suma de las tres integrales da (V). `□`

**Corolario V.1 (objetivo con granularidad controlada).** Si existen coeficientes construibles y ventanas `δ_m↓0`, `R_m↑∞` tales que

\[
\delta_m(1+L_m)^2\to0,\quad
\int_{\delta_m}^{R_m}|B_m(x)|²dx\to0,\quad
|C_m|²/R_m\to0,
\]

entonces `||B_m||_2→0` y RH. Este criterio **no se ha satisfecho** para una familia aritmética general: hay que demostrar sus tres estimaciones. Sin embargo proporciona un lugar explícito donde la granularidad (`δ_m`), la economía de la representación (`L_m`) y la herencia de la cola (`C_m`) se encuentran en **una misma desigualdad de norma**, sin confundir contratos físicos y funcionales.

**Control de escala:** elegir `δ_m` pequeño no basta si `L_m` crece demasiado. Una familia que cierra cada ventana fija pero desplaza masa hacia cero puede violar el primer requisito, como hace la aproximación directa por criba.

### Teorema de transferencia (condicional, demostración completa)

**Proposición T.** Sean `N_k→∞` normalizadores de una sucesión admisible en O58, `m(k)→∞` índices, y `a_k∈W_{m(k)}` aproximantes explícitos. Si existen números `A_k,B_k≥0` certificados **sin suponer RH** tales que

\[
\|\chi-a_k\|_{L²}^2\le A_k\,N_k^{-2}+B_k,\qquad
A_k/N_k^2+B_k\xrightarrow[k\to\infty]{}0,
\tag{T}
\]

entonces **RH es verdadera**.

*Prueba.* Por optimalidad, `0≤e_{m(k)}²≤||χ−a_k||²≤A_k/N_k²+B_k→0`. Como los subespacios `W_m` son anidados y `m(k)→∞`, para todo `m≥m(k)` se tiene `e_m≤e_{m(k)}`. Así `e_m→0`. La equivalencia clásica anterior concluye RH. `□`

**Alcance epistémico:** la proposición es un criterio de **certificación de transferencia**, no su prueba. Su hipótesis (T) contiene el control global pendiente. Reescribir `e_m²` como una granularidad o elegir `A_k` después de medir el error sería circular. Para obtener un resultado nuevo se necesita construir los `a_k` y acotar `A_k,B_k` independientemente.

### Barrera conocida de escala

La teoría de aproximación Nyman–Beurling proporciona, para índices suficientemente grandes, una cota inferior `e_m²≥c/\log m` con alguna constante `c>0` (Báez-Duarte–Balazard–Landreau–Saias; Burnol). Si se pretende `e_{m(k)}²≤C/N_k²` con `C` fijo, necesariamente `m(k)` debe satisfacer `\log m(k)≥(c/C)N_k²` para índices grandes. **Una identificación directa `e_m²≈1/m²` contradice esa barrera.** La escala de referencia no puede asociarse al índice `m` sin verificar este requisito.

## 6. Ley de reducción por bloques: dónde está la obligación universal

Para `m=2^j`, sea `\Delta_j=e_{2^j}²-e_{2^{j+1}}²`. La ley candidata examinada el 20-XI es

\[
\boxed{\forall j\ge0:\quad \Delta_j\ge\frac{e_{2^j}²}{j+2}.}\tag{L}
\]

**Proposición L (condicional).** Si (L) vale para todo `j`, entonces

\[
e_{2^J}²\le \frac{e_1²}{J+1}\longrightarrow0,
\]

y, en consecuencia, RH. La prueba es la multiplicación telescópica de `e_{2^{j+1}}²≤(j+1)e_{2^j}²/(j+2)`.

Esta ley es **suficiente, no está probada y puede ser más fuerte que RH**. El ensayo previo comprobó aproximadamente seis bloques (`m≤64`); son cálculos exploratorios sensibles al condicionamiento de las matrices de Gram, no certificados universales. Un solo `j` que viole (L) la refuta **sin refutar RH**.

Con bloques de Gram `G_{AA}`, `G_{AB}`, `G_{BB}` e índices nuevos `B`, la ganancia exacta, cuando las inversas existen, es

\[
\Delta_j=h^*S^{-1}h,
\quad S=G_{BB}-G_{BA}G_{AA}^{-1}G_{AB},\quad
h=b_B-G_{BA}G_{AA}^{-1}b_A,
\]

con `b_n=⟨χ,f_n⟩`. El siguiente contrato de investigación consiste en deducir de la estructura de los primos **una cota inferior para esa expresión**, no únicamente su no negatividad.

## 7. Dos controles adversariales que impiden declarar el cierre global

### Control A. Cada primo reduce el resto y puede sobrevivir una componente fija

En `H=\ell²(\{0\}\cup\mathbb P)` con base ortonormal `u_0,u_{p_1},u_{p_2},…`, sea

\[
\psi=\frac{1}{\sqrt2}u_0+\sum_{j\ge1}2^{-(j+1)/2}u_{p_j},\quad
V_m=\operatorname{span}\{u_{p_1},\dots,u_{p_m}\}.
\]

Todos los generadores son **primos distintos**. Sin embargo,

\[
\|\psi\|²=1,\qquad
\operatorname{dist}(\psi,V_m)²=\tfrac12+2^{-(m+1)}\to\tfrac12.
\]

Cada primo aporta una dirección nueva **y cada paso reduce estrictamente el error**; queda una componente invisible para todas esas direcciones. Es un contraejemplo a la inferencia lógica general, **no** un contraejemplo a RH ni a la familia especial `f_n`.

### Control B. Cierre puntual de la criba no da cierre en norma

Con `S_y={p≤y}`, `q_y` el primer primo `>y`, `δ_y=∏_{p≤y}(1−1/p)`, `G_y=-E_{S_y}(1/t)`, se prueba en el informe de granularidad previo que para `t>1/q_y`

\[
\chi(t)+G_y(t)=\frac{\delta_y}{t},
\qquad\|\chi+G_y\|_2²\ge q_y\delta_y²\to\infty
\]

por el producto de Mertens. Sin embargo `G_y(t)→−χ(t)` para cada `t>0` fijo. Así, una identidad que resuelve cada comparación puntual puede omitir masa que se desplaza hacia escalas más pequeñas. Cualquier teorema de transferencia debe controlar **la norma integral y las ventanas móviles**, no solo una granularidad local.

## 8. Dictamen y prueba decisiva para la próxima revisión

**DEMOSTRADO EN EL CONTRATO:** equivalencia entre consulta y factorización, composición contextual CR–6, aritmética CRT, ramificación admisible O58, identidades de herencia/Mellin, algebra de proyecciones, controles A y ejemplo de suficiencia versus linealidad.

**CLÁSICO:** criterio de Báez-Duarte, cotas inferiores de aproximación, producto de Mertens.

**DEMOSTRADO (lema operativo):** proposición V, desigualdad de tres ventanas para todo aproximante finito. **CONDICIONAL:** corolario V.1, proposición T, proposición L y forma Schur como objetivo de cota universal.

**ABIERTO:** obtener un mapeo que preserve la clase de decodificadores entre los modelos y certificar (T) o una cota global equivalente. No existe en el corpus auditado un teorema que deduzca esa norma únicamente de la existencia de nuevos primos, el recierre o la unidad `1/N²`.

**Pregunta técnica publicada:** ¿puede deducirse del recierre heredado y la economía de consultas una desigualdad no circular sobre la expresión de Schur, válida para toda incorporación diádica de referencias libres de cuadrados?

### Criterios para acreditar un cierre futuro

1. Identificar explícitamente `N_k`, `m(k)`, `a_k`, el dominio y el observable preservado.
2. Demostrar sin RH la desigualdad de error **en `L²((0,∞),dx)`**, incluida la ventana `x→0`.
3. Acreditar uniformidad para todo `k`, con constantes y condiciones de escala compatibles con Burnol.
4. Verificar la conexión exacta con las `f_n`; no sustituir el espacio lineal por todas las funciones de la firma.
5. Someter el argumento al falsador prime-indexado y a controles adversariales del laboratorio anterior.

## 9. Procedencia y fuentes

- **Programa, antecedentes:** `O40_NORMALIZADOR_HEREDADO_RESTO_Y_REORGANIZACION.es.md` (20-X); `O58_FORMALIZACION.es.md` (21-X); `G01_Mecanismo_de_la_Gravedad_Programa_Relacional_v1.3_2026-11-01.docx` (§§2B–2D, B18–B21); `Programa_Relacional_Cierre_Propio_Diferencia_Minima_2026-10-16.docx` (T1–T2); `CR6_Economia_Herencia_2026-10-16.pdf` (CR-6.1–6.6); `ANEXO_ECONOMIA_MATRIZ_PRIMOS_R03_2026-11-19.md`; R–01/R–02 y R–03; `R_RH_01_Primos_Reflexion_y_Cierre_2026-11-01.md`; `GRANULARIDAD_RESTO_Y_CIERRE_RH.md` e `INTENTO_DE_PRUEBA_RESTO_RIEMANN.md` (20-XI).
- **L. Báez-Duarte (2002):** [A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis](https://arxiv.org/abs/math/0202141), teorema 1.1.
- **J.-F. Burnol (2002):** [A lower bound in an approximation problem involving the zeros of the Riemann zeta function](https://arxiv.org/abs/math/0103058).
- **Teoremas clásicos adicionales:** Dirichlet, CRT, Möbius y Mertens, según el contexto.

**Alcance documental:** esta nota revisa los documentos indicados y el laboratorio previo; no equivale a una auditoría de cada rama, commit o anexo histórico. No se han compilado archivos Lean de terceros. Mantener el estado RH **OPEN**.

---

Endless Monkey Project / Relational Geometry Program
