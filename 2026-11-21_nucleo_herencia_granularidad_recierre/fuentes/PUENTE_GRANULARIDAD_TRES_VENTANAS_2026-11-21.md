# Granularidad y cierre funcional: examen de tres ventanas

**Nota técnica de actualización · 21 de noviembre de 2026**  
**Endless Monkey Project / Relational Geometry Program**  
**Estado:** identidades y controles exactos; transferencia a RH **ABIERTA**.  
**Función editorial:** complemento puntual del `COMPENDIO_RIEMANN_ECONOMIA_2026-11-21.md`. No sustituye R–RH–01, R–01/R–02, R–03 ni los anexos históricos. No constituye una prueba de RH o GRH.

## 1. Contrato ya establecido

En el Hilbert de Báez-Duarte,

\[
H=L^2((0,\infty),dx),\qquad \chi(x)=\mathbf1_{(0,1]}(x),\qquad
f_n(x)=\left\{\frac1{nx}\right\},
\]

\[
W_m=\operatorname{span}\{f_n:n\le m,\ \mu(n)\ne0\},\qquad
e_m=\operatorname{dist}(\chi,W_m).
\]

La equivalencia **clásica** `RH ⇔ e_m→0`, bajo la versión libre de cuadrados de las referencias, es el contrato que debe alcanzarse. Las identidades de herencia y Mellin preservan los ceros bajo referencias primas finitas, pero no implican ese límite.

El teorema V del anexo del 20-XI, para un aproximante finito `a=Σ_{n∈I}c_nf_n`, `B=χ−a`, `L=Σ|c_n|` y `C=Σc_n/n`, da, para `0<ε≤1≤R`,

\[
\tag{V}
\|B\|_2^2\le\varepsilon(1+L)^2+
\int_{\varepsilon}^R|B(x)|^2\,dx+\frac{|C|^2}{R}.
\]

La última contribución es, de hecho, **exacta**: `∫_R^∞|B|²dx=|C|²/R`. La primera es sólo una cota gruesa. La cuestión examinada aquí es si se puede calcular mejor el costo de la ventana fina y si el mecanismo de herencia lo controla automáticamente.

## 2. Resultado I — costo periódico exacto de la granularidad fina

Sea `I` un conjunto **finito** de enteros positivos, con coeficientes reales o complejos `c_n`. En la variable invertida `u=1/x`, la expresión válida para `0<x<1` es

\[
1-a(1/u)=1-\sum_{n\in I}c_n\{u/n\}.
\]

Esta expresión es periódica en `u` con período común `M=\operatorname{mcm}(I)`. Defínase la energía de un período

\[
Q_I(c)=\frac1M\int_0^M\left|1-\sum_{n\in I}c_n\{u/n\}\right|^2du.
\]

**Proposición 1 (identidad exacta).** Se cumple

\[
\boxed{Q_I(c)=\left|1-\frac12\sum_n c_n\right|^2+
\frac1{12}\sum_{n,m\in I}c_n\overline{c_m}\frac{\gcd(n,m)^2}{nm}.}\tag{1}
\]

**Prueba.** Cada `{u/n}` tiene media `1/2` sobre el período común. Escribiendo `\varphi_n(u)={u/n}−1/2`, la media de `\varphi_n` es cero y

\[
\frac1M\int_0^M \varphi_n(u)\varphi_m(u)\,du
=\frac{\gcd(n,m)^2}{12nm}.
\]

Esta última igualdad se obtiene integrando por tramos o mediante la serie de Fourier de la función diente de sierra y `Σ_{r≥1}r^{-2}=π²/6`. La expansión del cuadrado proporciona (1). `□`

**Proposición 2 (relación con la ventana física).** Para `0<ε≤1`,

\[
\boxed{
\left|\int_0^\varepsilon|B(x)|^2dx-\varepsilon Q_I(c)\right|
\le 2\varepsilon^2\left(
\sum_n n|c_n|+
\sum_{n,m}\operatorname{mcm}(n,m)|c_n|\,|c_m|
\right).}\tag{2}
\]

**Prueba.** La sustitución `u=1/x` convierte la integral en `∫_{1/ε}^∞ |1−Σc_n{u/n}|²u^{-2}du`. Si `h` es periódica de período `T`, tiene media cero y `|h|≤A`, una integración por partes de su primitiva periódica da

\[
\left|\int_U^\infty\frac{h(u)}{u^2}du\right|\le\frac{2TA}{U^2}.
\]

Se aplica por separado a cada `{u/n}−1/2`, de período `n` y módulo ≤`1/2`, y a los productos `{u/n}{u/m}` menos su media, de período `mcm(n,m)` y módulo ≤1. El término constante se integra exactamente. `□`

**Alcance:** (1) reemplaza las oscilaciones de una ventana muy fina por una matriz aritmética de máximos comunes divisores; (2) controla el error de ese reemplazo. Son identidades y cotas *finitas*: no garantizan una cota uniforme al crecer el número de referencias. En particular, el segundo miembro de (2) puede volverse muy grande.

## 3. Resultado II — el intercambio exacto entre cola y oscilación en la criba directa

Sea `S` un conjunto finito **no vacío** de `k` primos; `M_S=∏_{p∈S}p`, `ρ_S=∏_{p∈S}(1−1/p)`. La criba directa usa `a_S=−G_S`, con `G_S(t)=−E_S(1/t)=Σ_{d|M_S} μ(d)f_d(t)`. Sus coeficientes son `c_d=−μ(d)`.

Por Möbius y por la ley de energía por período de R–01/R–02,

\[
\boxed{L_S=2^k,\qquad C_S=-\rho_S,\qquad
Q_S=1+\frac{2^k\rho_S}{12}.}\tag{3}
\]

**Prueba.** Los divisores de `M_S` son libres de cuadrados, `Σ_{d|M_S} μ(d)=0` y `Σ_{d|M_S} μ(d)/d=ρ_S`. Además, `E_S(u)=−Σ_{d|M_S} μ(d){u/d}` tiene media cero sobre un período y energía media `2^kρ_S/12`. Para la expresión de la ventana fina `1−a_S(1/u)=1−E_S(u)`, la media cuadrática es `1+2^kρ_S/12`. `□`

**Interpretación precisa:** al incorporar un primo nuevo `p`, el término oscilatorio `Q_S−1` se multiplica por `2(1−1/p)`, mientras que `|C_S|` se multiplica por `1−1/p`. En esta regla **particular** de herencia, una cola exterior cada vez menor coexiste con una energía periódica interior creciente. No cabe inferir de ello que todo aproximante óptimo tenga ese comportamiento.

## 4. Resultado III — localización exacta de la masa que se escapa

Para `S_y={p\le y}` y `q_y` primer primo mayor que `y`, no existe entero entre `2` y `q_y−1` coprimo con `M_{S_y}`. Por consiguiente, para `x>1/q_y`,

\[
A_{S_y}(1/x)=\chi(x),\qquad
B_y(x):=\chi(x)+G_{S_y}(x)=\frac{\rho_y}{x}.
\]

Para cada `0<ε<1` **fijo**, y `q_y>1/ε`, se sigue exactamente que

\[
\boxed{\int_\varepsilon^\infty|B_y(x)|^2dx=\frac{\rho_y^2}{\varepsilon}\longrightarrow0,}\tag{4}
\]

mientras que

\[
\boxed{\int_0^\varepsilon|B_y(x)|^2dx\ge
\rho_y^2\left(q_y-\frac1\varepsilon\right)\longrightarrow\infty.}\tag{5}
\]

La divergencia utiliza `ρ_y∼e^{-γ}/log y` (Mertens) y `q_y>y`. Así queda localizada la obstrucción: el error de la criba directa desaparece en cualquier región alejada de cero, **pero se concentra en una ventana que se desplaza hacia cero**. Es un control negativo exacto de *convergencia local* versus *convergencia global en norma*. La conclusión se refiere a `a_y=−G_{S_y}`, no a la mejor proyección en `W_m`.

## 5. Obligación de transferencia y límite de la granularidad de O58

Un criterio suficiente inmediato del teorema V es el siguiente. Si una sucesión admisible de normalizadores `N_k→∞` se relaciona **mediante un mapa explícito** con `a_k∈W_{m(k)}`, y se puede probar sin RH que

\[
L_k=o(N_k),\qquad
\int_{N_k^{-2}}^{N_k^2}|\chi-a_k|^2dx\longrightarrow0,
\]

entonces `||χ−a_k||²→0` porque `|C_k|≤L_k`, aplicando (V) con `ε=N_k^{-2}`, `R=N_k^2`. Si también `m(k)→∞`, se deduce RH por el criterio clásico. **Éste es un teorema condicional, no una verificación de sus hipótesis.** Escoger `ε=N^{-2}` es una prueba de compatibilidad sugerida por O58, no una identificación previa de errores.

**Barrera cuantitativa.** La cota inferior clásica de Burnol proporciona `e_m²≥c/log m` para `m` grande (con `c>0` adecuado). Si se intenta transferir un error cuadrático `O(N^{-2})` mediante una asignación `m(N)≤N^K` para algún `K` fijo, se obtiene la contradicción

\[
\frac{c}{\log m(N)}\le e_{m(N)}^2\le\frac C{N^2},\qquad
\frac{c}{K\log N}\le\frac C{N^2}
\]

para `N→∞`. Por tanto, **no puede existir tal cota `O(N^{-2})` con crecimiento polinómico del índice de referencias**. Esto no excluye un cierre más lento `e_m→0`, ni excluye un vínculo con una cantidad auxiliar que no sea la distancia `e_m`.

El contrato general de suficiencia `q=\bar q\circ\Phi` de CR–6 tampoco fuerza un cierre mediante *combinaciones lineales*: la clase de decodificadores permitidos debe preservarse en la transferencia. Es una obstrucción previa e independiente del número de subdivisiones.

## 6. Dictamen de actualización

| Pregunta | Resultado |
|---|---|
| ¿Se conserva la estructura de los ceros bajo una referencia prima finita? | Sí, por el puente Mellin ya establecido |
| ¿Hay un costo aritmético exacto para la ventana fina? | **Sí: (1)–(3), con prueba y control racional** |
| ¿La herencia directa garantiza cierre funcional? | **No: (4)–(5) muestran concentración divergente** |
| ¿La granularidad geométrica `1/N²→0` impone `e_m→0`? | No se deduce sin un mapa de observables y cotas uniformes |
| ¿Se demuestra RH o GRH? | **No** |

**Próxima obligación concreta:** buscar, dentro de las reglas ya formalizadas, una construcción de coeficientes `c_{k,n}` con control simultáneo de (a) el costo aritmético `Q_I(c)` o la norma real de la ventana fina, (b) el error de la ventana central, (c) el coeficiente de cola `C_k`, y (d) el crecimiento de `m(k)` compatible con la barrera `1/log m`. Las identidades de herencia y suficiencia son herramientas disponibles; ninguna proporciona por sí sola estos cuatro controles.

### Verificación reproducible

`verificar_tres_ventanas_2026-11-21.py` utiliza sólo la biblioteca estándar: compara la fórmula mcd con una integración exacta por fracciones racionales sobre períodos, verifica los términos móviles de la criba y comprueba la ley `Q_S=1+2^kρ_S/12` en cuatro conjuntos finitos. `REGISTRO_TRES_VENTANAS_2026-11-21.txt` contiene los resultados. Las pruebas computacionales **no certifican límites infinitos ni RH**.

### Fuentes mínimas

- `ANEXO_TECNICO_ES.md`, 20-XI-2026, teorema V y controles A/B (origen del contrato de tres ventanas).
- `R_RH_01_Primos_Reflexion_y_Cierre_2026-11-01.md`, §§4–5 (criterio clásico, matrices de Gram).
- [R–01/R–02 — criba, herencia y energía](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md).
- [R–03 — herencia espectral y normalización](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/2026-11-18_r03_herencia_espectral/R03_HERENCIA_Y_LOCALIZACION_ES.md).
- [Báez-Duarte, criterio clásico](https://arxiv.org/abs/math/0202141); [Burnol, barrera de aproximación](https://arxiv.org/abs/math/0103058).

---

Endless Monkey Project / Relational Geometry Program
