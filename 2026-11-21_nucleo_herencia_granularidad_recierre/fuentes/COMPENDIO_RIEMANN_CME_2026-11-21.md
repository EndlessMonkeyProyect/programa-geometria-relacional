# Anexo consolidado: referencias, granularidad, focos de determinación y cierre funcional

**Fecha de consolidación:** 21 de noviembre de 2026  
**Ámbito:** R–01/R–02, R–03, R–RH–01, economía de consultas, G–01/O58, CME–002 y ensayos CME–RH–01/02/03  
**Estado de revisión:** identidades y controles aritméticos **DEMOSTRADOS**; resultados computacionales **VERIFICADOS EN INSTANCIAS FINITAS**; condiciones de transferencia **CONDICIONALES**; equivalencia geométrica y consecuencia sobre RH **ABIERTAS**.  
**Alcance:** documento de investigación verificable; no demuestra la hipótesis de Riemann (RH) ni la hipótesis generalizada (GRH).

## Resumen y resultado central

La incorporación de referencias permite distinguir relaciones nuevas y recuperar algunas diferencias previamente pendientes. La pregunta funcional, sin embargo, exige **reconstrucción bajo una clase de operaciones fijada y convergencia en la norma correspondiente**. Los experimentos con el cubo de espejos deben comenzar por sus *focos de determinación* —puntos de concurrencia de relaciones— y no por ángulos asignados a posteriori a funciones aritméticas.

Quedan establecidos tres niveles diferentes de cierre:

1. **Recierre aritmético local:** en cada paso diádico `N → 2N`, los saltos de la combinación de Möbius en los puntos `x=1/n`, `N<n≤2N`, se cancelan exactamente al incorporar la referencia `n`. Se verificaron 621 focos no triviales para `N=1024`.
2. **Recuperación por proyecciones:** para espacios funcionales anidados, la diferencia de errores óptimos es exactamente la norma cuadrática del componente nuevo; una reflexión ortogonal de Hilbert representa esa diferencia, pero **no se ha identificado con un espejo original de CME–002**.
3. **Cierre global:** demostrar que los errores óptimos tienden a cero requiere controlar la acumulación cerca de cero, la región intermedia, la cola y la recuperación entre todas las escalas. Las identidades anteriores no implican ese control.

La aportación concreta consiste en reunir las identidades, dos tipos de obstrucción, el ensayo de focos y un **contrato falsable de transferencia**. La novedad del recierre aritmético es su aplicación y organización como observable del laboratorio; la identidad de Möbius y la estructura booleana subyacente son clásicas. Ningún resultado se presenta como prueba de RH.

## 1. Objetos, procedencia y distinciones de tipo

### 1.1. Referencia aritmética de criba

Para un conjunto finito de primos `S`, se define

\[
M_S=\prod_{p\in S}p,\qquad
\delta_S=\prod_{p\in S}(1-p^{-1}),\qquad
A_S(x)=\#\{1\le n\le x:\gcd(n,M_S)=1\},\quad
E_S(x)=A_S(x)-\delta_Sx.
\]

La referencia cambia al añadir un primo; las propiedades de la nueva coordenada módulo `p` vienen dadas por el teorema chino del resto:

\[
\mathbb Z/(M_Sp)\mathbb Z\simeq
\mathbb Z/M_S\mathbb Z\times\mathbb Z/p\mathbb Z\quad(p\notin S).
\]

El espacio de preguntas importa: esa coordenada nueva distingue residuos, pero no supone una mejora estricta para **toda** consulta posible.

### 1.2. Referencia funcional

En `H=L²((0,∞),dx)`, sean

\[
\chi(x)=\mathbf1_{(0,1]}(x),\qquad
f_n(x)=\left\{\frac1{nx}\right\},\qquad
W_m^{\mathrm{sf}}=\operatorname{span}\{f_n:1\le n\le m,\ \mu(n)\ne0\}.
\]

Con `P_m` la proyección ortogonal sobre `W_m^{sf}` se define

\[
r_m=(I-P_m)\chi,\qquad e_m^2=\|r_m\|_2^2.
\]

Los resultados numéricos de los archivos aportados para `e_m` se refieren a **esta familia restringida a índices libres de cuadrados**. La combinación fija de criba `a_m=-\sum_{n\le m}\mu(n)f_n` no coincide, en general, con el aproximante óptimo `P_m\chi`; sus errores deben mantenerse separados.

**Precisión necesaria sobre el criterio clásico:** Báez-Duarte establece la equivalencia con RH para el cierre generado por las dilataciones de **índices enteros**. El cierre de la familia restringida a índices libres de cuadrados implica el cierre de la familia completa y por tanto implica RH. Los documentos cotejados no aportan una demostración autónoma de la implicación recíproca para el subespacio restringido; por eso **no se declara aquí** `RH ⇔ e_m→0` para esa familia. Toda aparición previa de esa equivalencia restringida requiere una cita o demostración adicional antes de su publicación como tal. Esta cautela no afecta las identidades finitas de proyección ni las condiciones suficientes formuladas a continuación.

### 1.3. Granularidad, economía y promoción

Una interfaz observacional `Φ_λ` es suficiente para una pregunta `q` si existe un decodificador permitido con `q=\bar q\circ Φ_λ`. Aun siendo inyectiva, `Φ_λ` puede no permitir reconstrucción usando exclusivamente **combinaciones lineales**. Ejemplo exacto: en `X={0,1,2}` con medida uniforme, `Φ(x)=x` y `q(x)=x²`, la consulta se responde con `Φ²`, pero el mejor ajuste en `span{1,Φ}` deja error cuadrático `2/9`.

En G–01/O58, `a²+b²+1=N²` implica el resto algebraico `1/N²→0` a lo largo de sucesiones admisibles `N→∞`. Este resto **no es** el error `e_m²` de `L²`. Tampoco hay una selección única de sucesor: `(2,2,3)` admite, entre otras, `(4,8,9)` y `(12,12,17)`. La promoción de una clase cerrada al nivel siguiente proporciona una estructura de herencia, no una cota funcional sin un mapa explícito.

## 2. Correspondencias exactas de criba y transformación

### 2.1. Mellin y factores finitos de Euler

Para `0<Re(s)<1`, la integral de Mellin de la discrepancia finita converge absolutamente y satisface, con la convención indicada,

\[
F_S(s)=\int_0^\infty E_S(x)x^{-s-1}\,dx
=\frac{\zeta(s)}{s}\prod_{p\in S}(1-p^{-s}).\tag{M}
\]

En efecto, `E_S` es acotada para `x≥1`; para `0<x<1`, `E_S(x)=-\delta_Sx`, lo que justifica ambos extremos de convergencia. La identidad se obtiene por inclusión-exclusión y la transformada clásica de `\lfloor x\rfloor-x` en la misma franja. Para `p∉S`,

\[
F_{S\cup\{p\}}(s)=(1-p^{-s})F_S(s).
\]

Como `1-p^{-s}` no se anula cuando `Re(s)>0`, los factores finitos conservan posiciones y multiplicidades de ceros dentro de la franja crítica. **Conservar ceros no determina su ubicación.** Bajo la especialización racional y carácter trivial de un producto de Euler incompleto, puede escribirse `L^S(s,1)=sF_S(s)` si se adoptan esas mismas convenciones; no es una equivalencia global de teorías.

### 2.2. Inversión y funciones de partes fraccionarias

Aplicando inclusión-exclusión a `A_S`:

\[
\boxed{G_S(t):=-E_S(1/t)=\sum_{d\mid M_S}\mu(d)f_d(t).}\tag{F}
\]

Esta es una **igualdad lineal exacta** y un puente natural con el sistema de funciones fraccionarias. Cada divisor `d|M_S` es libre de cuadrados. La inversión de Möbius sobre el retículo de subconjuntos recupera esas funciones **dentro del sistema de índices libres de cuadrados**; no recupera por ese solo argumento las dilataciones `f_{p²}`, por ejemplo.

### 2.3. Conjugación de operadores

Sean `T_pf(x)=f(x)-f(x/p)`, `P_pφ(x)=φ(x)-φ(px)` y `Jf(x)=f(1/x)`. Entonces

\[
\boxed{JT_pJ=P_p}\tag{O}
\]

en un dominio común estable bajo estas operaciones. En `L²((0,∞),dx/x)`, `J` es unitario y las dilataciones son unitarias; allí los operadores son acotados. No se infiere de ello que las completaciones, rangos cerrados o contratos topológicos de otros espacios (por ejemplo, ciertos espacios de funciones de prueba) sean equivalentes. Este es el límite de la comparación preliminar con el marco de Masullo: **las correspondencias algebraicas están delimitadas, la transferencia funcional sigue abierta y no valida GRH**.

## 3. Identidad de recuperación y reflexión operativa

Para `m<n`:

\[
U_{m,n}=W_n^{\mathrm{sf}}\cap(W_m^{\mathrm{sf}})^\perp,
\quad Q_{m,n}=P_n-P_m,
\quad \mathscr R_{m,n}=I-2Q_{m,n}.
\]

`Q_{m,n}` es una proyección ortogonal y `\mathscr R_{m,n}` es una involución. Por Pitágoras:

\[
\boxed{e_m²-e_n²=\|Q_{m,n}r_m\|²
=\tfrac14\|r_m-\mathscr R_{m,n}r_m\|².}\tag{R}
\]

Para una semilla `g∈W_n^{sf}` con `h=(I-P_m)g≠0`, el certificado elemental de recuperación es

\[
\frac{|\langle r_m,g\rangle|²}{\|h\|²}\le e_m²-e_n².
\]

Esto reproduce, con operadores de reflexión, la estructura del certificado de semilla y de la matriz de Gram; **no** establece que `\mathscr R_{m,n}` sea una reflexión original del recinto CME–002.

Cuando `e_m>0`, la esfera unitaria del complemento de lo heredado define el coeficiente

\[
\gamma_m=\frac{\|Q_{m,2m}r_m\|²}{e_m²}\in[0,1],
\quad e_{2m}²=e_m²(1-\gamma_m).
\]

Por telescopaje:

\[
\boxed{e_{2^J}²=e_1²\prod_{j=0}^{J-1}(1-\gamma_{2^j}).}\tag{A}
\]

Si ningún factor llega a cero, `e_{2^J}→0` equivale a `\sum_j\gamma_{2^j}=∞`; si alguna `\gamma` vale uno, el cierre se obtiene en ese paso. Esta es una condición **equivalente a la convergencia de la familia restringida**, no una demostración de que ocurra.

**Contrapruebas geométricas.** Tres reflectores que generan el grupo `B₃` de 48 simetrías pueden actuar sobre las tres primeras coordenadas de `\mathbb R^4` y dejar invisible la cuarta. A la inversa, dos reflexiones de producto de orden infinito pueden tener normales que abarquen `\mathbb R²` y recuperen toda consulta en ese espacio. Por tanto, **finitud del grupo, cierre del recinto y recuperabilidad de una pregunta son propiedades lógicamente distintas**. Ambos controles se verifican con aritmética racional en `scripts/verificar_reflexiones.py`.

## 4. Focos de determinación: cruce, herencia y recierre aritmético

### 4.1. Definición operativa y lema universal

Un *foco aritmético candidato* para el sistema `f_d` es un punto `x=1/n` donde concurren discontinuidades de varias referencias, etiquetado por la relación de divisibilidad. Se trata de un candidato **aritmético**; todavía no se ha probado que sea una intersección de rayos del laboratorio óptico.

En la combinación

\[
G_N(x)=\sum_{1\le d\le N}\mu(d)f_d(x),
\]

cada `f_d` salta `+1` al aumentar `x` a través de `1/n` si `d|n`, y no salta allí en caso contrario. El salto de `G_N` es

\[
J_N(n)=\sum_{\substack{d\mid n\\d\le N}}\mu(d).
\]

**Proposición F (demostrada).** Para todo entero `N≥1` y cada entero `N<n≤2N`,

\[
\boxed{J_N(n)=-\mu(n),\qquad J_{2N}(n)=0.}\tag{C}
\]

**Prueba.** Todo divisor propio `d` de `n` satisface `d≤n/2≤N`. Por tanto, antes de ampliar la pared estaban presentes todos los divisores propios; solo faltaba el término `d=n`. Como `n>1`, la identidad clásica `\sum_{d|n}\mu(d)=0` implica `J_N(n)=-\mu(n)`. Al añadir `n`, la suma queda completa y vale cero. `□`

Si `\mu(n)=0`, el salto ya era cero antes del avance. Así, **no todo entero del intervalo corresponde a un foco no trivial**. El lema es uniforme en `N` para saltos, **no para normas de aproximación**.

### 4.2. Ejemplo exacto: 1030

`1030=2·5·103` es libre de cuadrados. En el nivel `N=1024`, el punto `x=1/1030` contiene discontinuidades de las referencias

\[
\{1,2,5,10,103,206,515\},
\]

con signos de Möbius, respectivamente, `(+1,−1,−1,+1,−1,+1,+1)`. Su suma es `+1`. En `N=2048`, entra `1030`, con `\mu(1030)=−1`, y el salto total se cancela:

\[
1-1-1+1-1+1+1-1=0.
\]

Los ocho divisores de `1030` corresponden a los ocho subconjuntos de `{2,5,103}`. Alternar la presencia de un primo es una involución binaria `T_p` y `T_pT_q=T_qT_p`; la estructura combinatoria es `\mathbb F_2^3`, con suma alternada `(1-1)^3=0`. Es **una realización exacta de relaciones de divisores**, no una realización demostrada de las reflexiones angulares de CME–002, cuyos productos pueden tener orden `3` o `k`.

### 4.3. Conteo de focos y falsación cuantitativa

Para la transición `1024→2048`, `scripts/verificar_focos.py` recorre **todos los enteros** `1025≤n≤2048` con aritmética exacta:

| Estado del salto en el foco `x=1/n` | Casos |
|---|---:|
| `\mu(n)≠0`: foco no trivial cancelado por la nueva referencia | **621** |
| `\mu(n)=0`: salto ya nulo | **403** |
| Total | **1024** |

Entre los 621 casos no triviales hay 137 con un factor primo distinto, 282 con dos, 168 con tres y 34 con cuatro. **No se necesita la llegada de un primo nuevo:** `1030` es una combinación nueva de factores previamente presentes.

El control adversarial es indispensable. Entre `N=16` y `N=32` se cierran **nueve** focos no triviales, pero para el aproximante *de coeficientes fijos* `a_N=-G_N` el error cuadrático global **crece**:

\[
\|\chi-a_{16}\|²\approx0.106470,
\qquad \|\chi-a_{32}\|²\approx0.186754.
\]

No hay contradicción con la monotonía del **óptimo** `e_N²`: este mide la mejor combinación del espacio ampliado y necesariamente no crece. El control prueba que **cancelación de saltos locales ≠ disminución universal del error de una combinación fijada**, y mucho menos cierre global de los óptimos.

### 4.4. Contrastación con el cubo óptico

En CME–002, las relaciones de grupos triangulares `(2,3,k)` cierran para `k=2,3,4,5`, presentan el caso euclídeo en `k=6` y se abren para `k≥7`; en cambio, la familia `(2,2,k)` cierra para cualquier `k`. El laboratorio usa las composiciones de reflexiones como criterio operativo, no solamente el número de referencias.

La asignación tentativa `f_n` como normal a un espejo se falsó en un ejemplo: las normales funcionales elegidas `f_1027`, `f_1030` forman aproximadamente `6.512951°` en su métrica de Gram, mientras la regla angular `π/1027` da `0.175268°`. **El ensayo descarta esa asignación concreta, no otros entrelazadores aún no definidos**. La prueba posterior por focos reemplaza esa comparación angular arbitraria por una investigación de las relaciones que concurren primero.

## 5. Economía de reconstrucción: certificado de tres ventanas

Para cualquier aproximante finito `a_m=\sum_{n≤m}c_{m,n}f_n`, se definen

\[
B_m=\chi-a_m,\quad L_m=\sum_{n≤m}|c_{m,n}|,
\quad C_m=\sum_{n≤m}\frac{c_{m,n}}{n}.
\]

**Proposición V (exacta).** Para todo `0<δ≤1≤R`,

\[
\boxed{\|B_m\|_2²\le
\delta(1+L_m)^2+\int_\delta^R|B_m(x)|²dx+
\frac{|C_m|²}{R}.}\tag{V}
\]

**Prueba.** Para `0<x<δ`, `|B_m(x)|≤1+L_m`, por ser `0≤f_n(x)<1`. Para `x>R≥1`, vale exactamente `B_m(x)=-C_m/x` y su contribución es `|C_m|²/R`. La integral central se deja sin alterar. `□`

Este certificado separa **granularidad fina**, **región intermedia** y **cola**. Si se construyen `a_m`, `δ_m↓0`, `R_m↑∞` para los cuales los **tres términos del lado derecho** tienden a cero, se tendrá `e_m→0` para la familia restringida y, por inclusión en la familia entera, RH. **Es una condición suficiente, no obtenida de las reglas existentes.** La identidad `1/N²→0` de G–01 no implica por sí sola esas tres estimaciones.

Otra vía de formulación, igualmente condicional, consiste en relacionar una sucesión geométrica `N_k` con índices funcionales `m(k)` y aproximantes `a_k`, mediante una cota demostrada independientemente de RH:

\[
\|\chi-a_k\|²\le A_k N_k^{-2}+B_k,
\qquad A_k/N_k²+B_k\to0.
\]

Si se prueban estas hipótesis y `m(k)→∞`, se obtiene RH. La cota global es, precisamente, **la obligación no resuelta**; elegir `A_k` después de conocer el error sería circular. Las cotas inferiores clásicas del problema de aproximación (orden `1/\log m`) descartan identificar directamente `e_m²` con `1/m²`.

## 6. Recuperación por escalas, condiciones propuestas y resultados numéricos

La matriz de Gram `G=(\langle f_i,f_j\rangle)` y el vector `b=(\langle\chi,f_i\rangle)` permiten calcular errores óptimos finitos. Para índices heredados `A` y nuevos `B`, cuando las matrices relevantes son invertibles:

\[
S=G_{BB}-G_{BA}G_{AA}^{-1}G_{AB},\qquad
h=b_B-G_{BA}G_{AA}^{-1}b_A,
\qquad
\boxed{e_A²-e_{A\cup B}²=h^*S^{-1}h.}\tag{S}
\]

La igualdad es un objetivo para obtener **cotas inferiores no circulares**, no un teorema de reducción uniforme por sí sola.

La ley candidata del 20-XI, que exigía para todo `j`

\[
\gamma_{2^j}\ge\frac1{j+2},
\]

es **falsa como afirmación universal**: los registros del paso `1024→2048` dan `\gamma_{1024}≈0.0664`, menor que `1/12≈0.083333`. No debe publicarse como teorema ni describirse como resultado pendiente de generalización; es un **intento refutado por el control disponible**. Esto no refuta RH.

Los datos aportados, procedentes de la resolución numérica de matrices grandes de Gram, indican:

| Indicador del paso `1024→2048` | Resultado reportado |
|---|---:|
| Referencias libres de cuadrados hasta 1024 | 624 |
| Referencias nuevas hasta 2048 | 621 |
| Referencias acumuladas hasta 2048 | 1245 |
| Error óptimo restringido `e_{1024}²` | ≈ 0.006672 |
| Error óptimo restringido `e_{2048}²` | ≈ 0.006229 |
| Fracción recuperada `\gamma_{1024}` | ≈ 6.64 % |
| Ángulo entre resto y subespacio nuevo, `arccos√γ` | ≈ 75.07° |

**Calificación:** las cantidades enteras y el lema de focos se verifican exactamente; los errores óptimos grandes y el ángulo derivan de registros numéricos del trabajo previo, no de certificados de aritmética exacta para una matriz `1245×1245` en esta entrega. No es un ángulo entre espejos físicos.

La comparación de recetas para `N=2048` informa un error cuadrático aproximado de `0.067054` con pesos `w_n=1-\log n/\log N`, `0.084783` para coeficientes de corte abrupto y `0.006229` para el óptimo restringido. El comportamiento observado no demuestra un límite. El teorema asintótico citado de Bettin–Conrey–Farmer para pesos logarítmicos se formula bajo **RH e hipótesis adicionales sobre `ζ′`**, y no puede utilizarse como demostración independiente del cierre.

## 7. Dos obstrucciones adicionales: lo local no controla lo global

**Obstrucción por interfaz insuficiente.** Una firma puede distinguir cada estado pero no permitir responder una consulta cuando los decodificadores se restringen a un subespacio lineal (ejemplo `q=Φ²` con error `2/9`). Por ello una nueva relación determinable no implica una nueva dirección de reconstrucción admitida.

**Obstrucción por acumulación cerca de cero.** En la criba por un bloque finito de primos `S_y={p≤y}`, sea `q_y` el primo siguiente y `δ_y=∏_{p≤y}(1-1/p)`. Para `t>1/q_y` se obtiene `\chi(t)+G_{S_y}(t)=\delta_y/t`, y de ahí

\[
\|\chi+G_{S_y}\|_2²\ge q_y\delta_y²,
\]

cantidad que crece sin cota al aumentar `y`, por las estimaciones clásicas de primos. Entretanto, para cada `t>0` fijo, `G_{S_y}(t)→-\chi(t)`. **La recuperación puntual de cada ventana fija no garantiza control global en norma.** Es un control sobre la *criba directa*, no sobre el aproximante óptimo.

### Oscilación media en un período completo de la criba

Además del control cerca de `t=0`, existe una fórmula exacta para la **magnitud cuadrática media** de la combinación aritmética en la variable inversa `u=1/t`. Sea `S` un conjunto **no vacío** de `k` primos, `M=∏_{p∈S}p`, `ρ=∏_{p∈S}(1-1/p)` y

\[
H_S(u)=\sum_{d\mid M}\mu(d)\left\{\frac{u}{d}\right\},
\qquad Q_S=\frac1M\int_0^M(1+H_S(u))^2\,du.
\]

El promedio de `H_S` en ese período es cero, porque `∑_{d|M}μ(d)=0`. La identidad clásica para la covarianza de dos funciones fraccionarias con períodos enteros da

\[
\frac1M\int_0^M
\left(\left\{\frac{u}{d}\right\}-\frac12\right)
\left(\left\{\frac{u}{e}\right\}-\frac12\right)du
=\frac{\gcd(d,e)^2}{12de}.
\]

Al expandir `H_S²`, la suma factoriza primo a primo:

\[
\boxed{Q_S=1+\frac1{12}\prod_{p\in S}2(1-p^{-1})
=1+\frac{2^k\rho}{12}.}\tag{P}
\]

Esta igualdad explica por qué el recierre de saltos discretos puede coexistir con oscilaciones cuadráticas persistentes o crecientes en la representación invertida. **No es la norma óptima `e_m²` ni implica una ubicación de ceros**. `scripts/verificar_periodos.py` verifica la fórmula por integración racional exacta para pequeños conjuntos de primos.

## 8. Contrato exacto de transferencia CME → RH y estado de las esferas

Para declarar una correspondencia geométrica genuina debe especificarse, **antes de medir mejoras**, una familia de representaciones `ρ_m` de los generadores originales de CME–002 y mapas `T_m` al sistema funcional que satisfagan simultáneamente:

1. **Composición:** las identidades, órdenes e involuciones originales se preservan; donde el recinto exige `(s_is_j)^k=I`, su imagen cumple esa relación sin colapsar artificialmente los generadores.
2. **Focos:** las intersecciones geométricas se corresponden con focos aritméticos mediante una regla explícita, no simplemente por semejanza de vocabulario.
3. **Consulta:** se conserva la pregunta `\chi`, la clase permitida de reconstrucciones y la información heredada al mover la pared.
4. **Alcance:** se demuestra que las operaciones acceden a componentes de `U_{m,2m}`, y se identifica cualquier complemento invisible.
5. **Uniformidad:** se obtiene una estimación no circular que controle la recuperación acumulada (por ejemplo, `\gamma_{2^j}≥c_j≥0` con `\sum c_j=∞`), compatible con las barreras conocidas de aproximación.

Las *esferas* utilizadas en las pruebas funcionales son esferas unitarias de direcciones en Hilbert. No se han identificado con las esferas físicas o geométricas originales; **esa correspondencia también está abierta**.

## 9. Tabla de procedencia y dictamen editorial

| Afirmación | Estado | Procedencia o prueba |
|---|---|---|
| CRT, inclusión-exclusión, transformada Mellin finita, saltos de Möbius | Clásica / demostración directa | R–01/R–03; §2 y §4 de este anexo |
| Recierre `J_N(n)=-μ(n)`, `J_{2N}(n)=0` | Demostrado | Proposición F; verificador entero |
| Conteo de 621 focos; ejemplo 1030 | Verificación finita exacta | `scripts/verificar_focos.py` |
| Error de criba fija aumenta de 16 a 32 | Control numérico reproducido | Gram del archivo suministrado; `scripts/verificar_focos.py` |
| `e_m²-e_n²=\|Q r_m\|²` y reflexión asociada | Demostrado en Hilbert | §3; `scripts/verificar_reflexiones.py` controla ejemplos finitos |
| Grupos finito/infinito no deciden recuperación | Contraejemplos demostrados | §3; verificación racional |
| Tres ventanas y criterio condicional | Demostrado / condicional | §5; `scripts/verificar_puentes.py` aporta controles auxiliares |
| Oscilación media periódica `Q_S` | Demostrado | Fórmula (P) y `scripts/verificar_periodos.py` |
| Mejora óptima de 6.64 % en la última escala | Registro numérico previo | `registro_mecanismos..txt`; no rehacer prueba de alta precisión aquí |
| Ley `\gamma_j≥1/(j+2)` | Refutada por resultado numérico de control | §6; debe excluirse de hipótesis demostradas |
| Entrecruzamiento CME–002 con el criterio funcional | Abierto | §8 |
| RH/GRH | Abierto | No hay estimación universal acreditada |

### Dictamen

Se recomienda incorporar este compendio como **anexo único de síntesis**, conservando la cronología de R–01/R–03, economía de información, G–01, y CME–002 mediante referencias, sin sustituir archivos previos ni duplicar sus demostraciones históricas. Las pruebas reproducibles y los controles se empaquetan por separado. Los resultados de esta entrega **no acreditan** una demostración de RH ni equivalencia completa con los métodos externos.

## 10. Fuentes primarias y literatura de comparación

**Documentos utilizados en la consolidación (archivos entregados y notas de investigación del 20–21 XI):**

- `ANEXO_TECNICO_ES(1).md` y anexo equivalente dentro de `ACTUALIZACION_PUENTE_RESOLUCION_RIEMANN_2026-11-20(1).zip` (**contenido redundante**; fuente base de tres ventanas).
- `Mecanismos del programa frente a la regla de eliminación entre escalas.md`, `registro_mecanismos..txt`, `registro_bloques_primos..txt`, `prueba_reglas_de_peso.py`.
- `CME_RH_PUENTE_REFLEXIONES_Y_CIERRE_2026-11-21.md`, `ENSAYO_CME_ARIT_1024_2048_2026-11-21.md`, `FOCOS_DETERMINACION_CME_RH_2026-11-21.md` y sus verificadores.
- `Texto pegado(5).txt`: auditoría preliminar de las correspondencias con Masullo; los problemas de normalización, convergencia y dominios se tratan separadamente en §2.

**Repositorios y referencias documentales:**

- [R–01/R–02 — criba y herencia](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md).
- [R–03 — herencia y localización](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/2026-11-18_r03_herencia_espectral/R03_HERENCIA_Y_LOCALIZACION_ES.md). **Advertencia editorial:** el puente lineal completo figura en la copia de trabajo v0.4; comprobar la revisión pública efectiva antes de citarlo como publicado.
- [CME–002 — pared que se corre](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-10-24/02_REALIZACIONES/01_cubo_de_espejos/CME-002_pared_que_se_corre/CME-002_Pared_que_se_corre.md).
- [Laboratorio de óptica y radios v5.1](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/laboratorios/laboratorio_optica_radios_v5_1/README.md).
- [Identidad contextual y promoción de escala](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/blob/main/02_formal_core/contextual_identity_and_scale_promotion.es.md).
- [Cierre relativo y control uniforme](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/blob/main/02_formal_core/relative_closure_and_uniform_control.es.md).
- [Báez-Duarte — fortalecimiento de Nyman–Beurling](https://arxiv.org/abs/math/0202141) (índices enteros).
- [Burnol — cota inferior de aproximación](https://arxiv.org/abs/math/0103058).
- [Bettin–Conrey–Farmer — polinomios óptimos](https://arxiv.org/abs/1211.5191) (revisar cuidadosamente las hipótesis).
- [Masullo — *The Music of the Primes*](https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf) (solo marco externo de comparación, no validación).

**Endless Monkey Project / Relational Geometry Program**
