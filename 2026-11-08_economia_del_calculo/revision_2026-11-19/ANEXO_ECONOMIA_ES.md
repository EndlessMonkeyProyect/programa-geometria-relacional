# Distinciones activas, ciclos y recurrencias mínimas

**Anexo matemático a la solicitud de revisión «¿Dónde se ahorra el cálculo?»**

19 de noviembre de 2026 · Revisión técnica para el repositorio

[English](APPENDIX_ECONOMY_EN.md)

## Resumen

Dos preguntas de la publicación del 8 de noviembre de 2026 quedan más precisas tras una revisión matemática externa:

1. **Particiones (Q2).** El grafo bipartito de intersecciones da una identidad exacta con el rango de ciclos y extiende la identidad de covarianza original a cualquier par de particiones mediante un defecto no negativo. La ley de producto equivale a `k·Cov = δ`. El Ejemplo B la cumple sin permutar, con seis elementos, que es el tamaño mínimo.
2. **Cuadrículas (Q1).** El número de órbitas bajo permutación de colores y reflexión tiene fórmula cerrada por Burnside. El orden mínimo de la recurrencia es el número de autovalores distintos que tocan al vector de conteo. El cálculo exacto para los anchos 1 a 10 da la forma de esa recurrencia: su polinomio es irreducible sobre `ℚ`, de grado `d_w`, y la diferencia con el número de órbitas se reparte entre el núcleo y un segundo factor irreducible. Para el ancho 10: `136 = 51 + 40 + 45`.

El texto distingue tres niveles: identidades demostradas, cálculos exactos para `w ≤ 10` y la pregunta por una ley general.

---

## Q2. Intersecciones de particiones

### Definiciones

Sea `X` un conjunto finito no vacío, y sean `P` y `Q` particiones de `X`.

- `P ∧ Q` es la partición fina cuyos bloques son las intersecciones **no vacías** `B ∩ C` con `B ∈ P`, `C ∈ Q`.
- `P ∨ Q` es la partición gruesa correspondiente a la menor relación de equivalencia que contiene ambas relaciones de equivalencia.
- Sea `𝒥 = P ∨ Q` y `k = |𝒥| ≥ 1`. Para cada `J ∈ 𝒥`, `p_J` y `q_J` son las cantidades de bloques de `P` y `Q`, respectivamente, contenidos en `J`.
- `e_J` es el número de pares `(B,C)` de bloques de `P` y `Q` contenidos en `J` con `B ∩ C ≠ ∅`.

La covarianza se define **uniformemente sobre los `k` bloques de la unión**:

$$
\operatorname{Cov}_{\mathcal J}(p,q)
=\frac1k\sum_{J\in\mathcal J}p_Jq_J
-\frac{|P||Q|}{k^2}.
$$

Se construye el grafo bipartito simple `G(P,Q)` con un vértice por bloque de `P`, un vértice por bloque de `Q` y una arista por intersección no vacía. Sus componentes conexas son exactamente los bloques de `P ∨ Q`.

### Proposición 1. Identidad de ciclos y cotas extremas

Si `β₁(G)` denota el número ciclomático (dimensión del espacio de ciclos sobre `𝔽₂`), entonces

$$
\boxed{|P\wedge Q|=|P|+|Q|-|P\vee Q|+\beta_1(G).}\tag{1}
$$

Además,

$$
\boxed{|P|+|Q|-k\;\leq\;|P\wedge Q|\;\leq\;\sum_{J\in\mathcal J}p_Jq_J.}\tag{2}
$$

La cota inferior es una igualdad si y solo si `G` es un bosque. La superior es una igualdad si y solo si cada componente `G[J]` es un bipartito completo `K_{p_J,q_J}`.

**Demostración.** El grafo tiene `|P|+|Q|` vértices, `|P ∧ Q|` aristas y `k` componentes. Para todo grafo finito, la dimensión del espacio de ciclos es `E−V+k`, que da (1). Toda componente es conexa, por lo que `e_J ≥ p_J+q_J−1`, con igualdad exactamente cuando es un árbol. Como hay a lo sumo una arista por par de bloques, `e_J ≤ p_Jq_J`, con igualdad exactamente cuando cada par se intersecta. Sumando sobre `J` se obtiene (2). `□`

### Proposición 2. Permutabilidad y completitud bipartita

Las siguientes condiciones son equivalentes:

1. Las relaciones de equivalencia asociadas a `P` y `Q` permutan: `R_P ∘ R_Q = R_Q ∘ R_P`.
2. `R_P ∘ R_Q = R_{P∨Q}`.
3. Dentro de cada `J ∈ P∨Q`, **todo** bloque de `P` intersecta **todo** bloque de `Q`.
4. `G[J]` es `K_{p_J,q_J}` para cada `J`.
5. `|P∧Q| = Σ_J p_Jq_J`.

**Demostración.** Las condiciones 3, 4 y 5 son equivalentes por la definición de las aristas y la cota superior de la Proposición 1. Si las relaciones permutan, su composición es una relación de equivalencia que contiene ambas y coincide con su unión `R_{P∨Q}`: así, dados `x` y `z` en un mismo `J`, existe `y` con `x R_P y R_Q z`, de modo que el bloque `P` de `x` intersecta el bloque `Q` de `z`. Recíprocamente, si todos esos pares de bloques se intersectan, para cualquier `x,z ∈ J` existe ese `y`, por lo que `R_{P∨Q} ⊆ R_P ∘ R_Q`. La inclusión inversa es inmediata. Intercambiando `P,Q` se obtiene `R_P ∘ R_Q = R_Q ∘ R_P`. `□`

La equivalencia es la caracterización clásica de las relaciones de equivalencia permutables (Ore, 1942; Birkhoff, 1948).

### Teorema 3. Identidad general de covarianza y defecto

Defínase el **defecto de intersecciones**

$$
\delta(P,Q)=\sum_{J\in\mathcal J}(p_Jq_J-e_J)
=\sum_{J\in\mathcal J}p_Jq_J-|P\wedge Q|.
$$

Entonces `δ(P,Q) ≥ 0` y

$$
\boxed{\;k|P\wedge Q|
=|P||Q|+k^2\operatorname{Cov}_{\mathcal J}(p,q)-k\delta(P,Q).\;}\tag{3}
$$

También

$$
\boxed{\;\beta_1(G)=\sum_{J\in\mathcal J}(p_J-1)(q_J-1)-\delta(P,Q).\;}\tag{4}
$$

Se tiene `δ(P,Q)=0` si y solo si `P` y `Q` permutan.

**Demostración.** Por definición de la covarianza,

$$
k^2\operatorname{Cov}_{\mathcal J}(p,q)
=k\sum_Jp_Jq_J-|P||Q|.
$$

Sustituir `Σ_Jp_Jq_J = |P∧Q|+δ(P,Q)` y despejar da (3). Por (1),

$$
\begin{aligned}
\beta_1(G)
&=|P\wedge Q|-|P|-|Q|+k\\
&=\sum_J[p_Jq_J-p_J-q_J+1]-\delta(P,Q),
\end{aligned}
$$

que es (4). La equivalencia `δ=0 ⇔` permutabilidad sigue de la Proposición 2. `□`

**Consecuencia.** La ley de producto

$$
|P\wedge Q|\,|P\vee Q|=|P|\,|Q|
$$

se cumple exactamente cuando

$$
\boxed{\;k\operatorname{Cov}_{\mathcal J}(p,q)=\delta(P,Q).\;}\tag{5}
$$

Permutabilidad con covarianza nula es una manera de cumplir (5). La otra es que un defecto positivo compense una covarianza positiva. Esto corrige la afirmación 1 de la solicitud, que pedía permutabilidad y covarianza nula.

### Dos ejemplos comprobables

**Ejemplo A: el ciclo único del comentario externo.** Tomar

- `P = {{a,b},{c,d},{e}}`;
- `Q = {{a,c},{b,d},{e}}`.

Aquí `|P|=|Q|=3`, `k=2`, `|P∧Q|=5`, `p=(2,1)`, `q=(2,1)`, `Cov=1/4`, `δ=0`, `β₁=1`. Resulta `5·2=9+4·(1/4)=10`. La primera componente es `K₂,₂`, con un ciclo independiente.

**Ejemplo B: igualdad de producto sin permutabilidad.** Tomar

- `X={a,b,c,d,e,f}`;
- `P={{a},{b,c,d},{e,f}}`;
- `Q={{a},{b,e},{c,f},{d}}`.

Aquí `|P|=3`, `|Q|=4`, `k=2`, `|P∧Q|=6`, `p=(1,2)`, `q=(1,3)`, `Cov=1/2`, `δ=1` y `β₁=1`. Por tanto,

$$
6\cdot2=3\cdot4+4\cdot\tfrac12-2\cdot1=12.
$$

La ley de producto se cumple; el segundo componente es `K₂,₃` con una arista ausente, y las relaciones **no permutan**.

Seis elementos es el tamaño mínimo: en conjuntos de hasta cinco elementos, todo par de particiones que cumple la ley de producto permuta (búsqueda exhaustiva). En un conjunto de seis elementos hay 720 pares ordenados que la cumplen sin permutar.

---

## Q1. Coloraciones y orden mínimo de recurrencia

### Definiciones

Sea `X_w` el conjunto de coloraciones propias de una columna de altura `w` con tres colores. Entonces

$$
|X_w|=3\cdot2^{w-1}\quad(w\ge1).
$$

Para `x,y ∈ X_w`, defínase la matriz simétrica de transferencia

$$
(T_w)_{xy}=\begin{cases}1,&x_i\ne y_i\text{ para todo }i,\\0,&\text{en otro caso.}\end{cases}
$$

El número de coloraciones propias de la cuadrícula `P_w □ P_m`, con bordes libres, es

$$
a_w(m)=\mathbf1^\top T_w^{m-1}\mathbf1,\qquad m\ge1.\tag{6}
$$

Actúa el grupo `S₃ × C₂`: permutación global de colores y reflexión vertical de la columna. Sea `o_w` el número de órbitas.

### Proposición 4. Fórmula cerrada de órbitas

Para `w=1`, `o₁=1`. Para `w≥2`, con `n=w−1`,

$$
\boxed{\;o_w=\frac{2^n+2^{\lceil n/2\rceil}+\mathbf1_{2\mid n}\,2^{n/2}}4.\;}\tag{7}
$$

**Demostración.** Una columna queda determinada por su primer color y los incrementos `s_i = x_{i+1}-x_i ∈ {+1,-1}` en `ℤ/3ℤ`, `1≤i≤n`. Las seis permutaciones de `ℤ/3ℤ` son las aplicaciones afines `x ↦ ±x+b`: actúan transitivamente sobre el color inicial y, sobre la palabra de incrementos, inducen la identidad o el cambio global de signo. La reflexión invierte el orden de los incrementos y su signo. Por tanto, las órbitas de columnas corresponden a las órbitas de palabras en `{±1}^n` bajo el grupo de cuatro aplicaciones `id`, `negación`, `reversión` y `negación◦reversión`.

Para `n≥1`, las cantidades de palabras fijas son, en ese orden,

$$
2^n,\quad 0,\quad 2^{\lceil n/2\rceil},\quad
\begin{cases}2^{n/2},&n\text{ par},\\0,&n\text{ impar}.\end{cases}
$$

Burnside da (7). Para `w=1`, las tres coloraciones son equivalentes por permutación de colores. `□`

### Teorema 5. Soporte espectral y recurrencia mínima

Sea `b_k=1ᵀT_w^k1` (`k≥0`). Sea `Λ_w` el conjunto de autovalores **distintos** de `T_w` y `Π_λ` la proyección ortogonal sobre el autoespacio de `λ`. Entonces

$$
\boxed{\;d_w
=\#\{\lambda\in\Lambda_w:\Pi_\lambda\mathbf1\ne0\}
=\operatorname{rank}_{\mathbb Q}(b_{i+j})_{i,j\ge0}
=\dim_{\mathbb Q}\operatorname{span}\{T_w^j\mathbf1:j\ge0\}.\;}\tag{8}
$$

Aquí `d_w` es el orden mínimo de una recurrencia lineal homogénea válida desde `k=0` para la sucesión `b_k`.

**Demostración.** Como `T_w` es real y simétrica, admite descomposición espectral ortogonal. Se sigue que

$$
b_k=\sum_{\lambda\in\Lambda_w}
\underbrace{\|\Pi_\lambda\mathbf1\|^2}_{c_\lambda\ge0}\lambda^k.
$$

Sean `λ₁,…,λ_d` los valores distintos con `c_{λ_j}>0`. Sus potencias definen `d` sucesiones geométricas linealmente independientes (Vandermonde). El polinomio `∏_{j=1}^d(t−λ_j)` anula la sucesión; ningún polinomio de grado menor lo hace desde `k=0`. Además,

$$
H_N=(b_{i+j})_{0\le i,j<N}
=V_N\operatorname{diag}(c_{\lambda_1},\ldots,c_{\lambda_d})V_N^\top
$$

con `V_N=(λ_j^i)`, luego `rank(H_∞)=d`, `det H_d>0` y `det H_{d+1}=0`. Por simetría, `H_N` es la matriz de Gram de `1,T1,…,T^{N−1}1`, y su rango es la dimensión de Krylov. Las matrices son racionales, así que el rango es el mismo sobre `ℚ` y `ℝ`. `□`

**Raíz cero y desfase.** Para el Hankel desplazado `H_d^{(1)}=(b_{1+i+j})_{0≤i,j<d}`,

$$
\det H_d^{(1)}=\left(\prod_{j=1}^{d}\lambda_j\right)\det H_d.
$$

Por tanto, `det H_d^{(1)}≠0` equivale a que ninguno de los autovalores activos sea cero. Es la hipótesis que permite conservar el mismo orden mínimo al iniciar la recurrencia una posición después.

**Certificado con dos determinantes.** Como `H_N` es una matriz de Gram, `det H_d ≠ 0` dice que `1, T1, …, T^{d−1}1` son independientes, y `det H_{d+1} = 0` dice que `T^d1` depende de ellos. El espacio de Krylov tiene entonces dimensión `d` y la recurrencia de orden `d` vale para todo `k`. Por eso los determinantes del experimento E5c (`det H_d ≠ 0`, `det H_{d+1} = 0`, `det H_d^{(1)} ≠ 0`) certifican `d_w` y la ausencia de raíz nula.

### Proposición 6. La reducción por órbitas no agota el ahorro lineal

Sea `G=S₃×C₂`, y `V_w^G ⊆ ℝ^{X_w}` el subespacio de vectores constantes en cada órbita. Como `T_w` conmuta con `G` y `1∈V_w^G`,

$$
d_w\le \dim V_w^G=o_w\le |X_w|.
$$

Sea `r_w` el número de autovalores distintos de `T_w` restringida a `V_w^G`, y `m_λ` la multiplicidad de cada uno en ese subespacio. Entonces

$$
\boxed{\;o_w-d_w
=\underbrace{\sum_{\lambda}(m_\lambda-1)}_{o_w-r_w}
+\underbrace{\#\{\lambda:\Pi_\lambda\mathbf1=0\text{ en }V_w^G\}}_{r_w-d_w}.\;}\tag{9}
$$

**Demostración.** La simetría de `T_w` preserva el subespacio fijo. El espacio tiene una base de indicadores de las órbitas y, por tanto, dimensión `o_w`. La descomposición ortogonal en autoespacios de la restricción da `o_w=Σ_λm_λ`, con `r_w` sumandos. Cada `Π_λ1` está en `V_w^G`, porque `Π_λ` es un polinomio en `T_w`; solo los valores con proyección no nula contribuyen a `d_w` por el Teorema 5. Restar da (9). `□`

### Proposición 7. La actividad va por factores irreducibles

Sea `χ_w` el polinomio característico de `T_w` restringida a `V_w^G`. Si `f` es un factor irreducible de `χ_w` sobre `ℚ`, o todas sus raíces son activas (`Π_λ1 ≠ 0`) o ninguna lo es. En consecuencia, el polinomio mínimo de la sucesión `b_k` es el producto de los factores irreducibles activos, cada uno con exponente 1, y `d_w` es la suma de sus grados.

**Demostración.** `Π_λ = ∏_{μ≠λ}(T_w−μ)/(λ−μ)`, con `μ` en los autovalores distintos de la restricción. Si `σ` es un automorfismo del cuerpo de descomposición de `χ_w`, como `T_w` y `1` tienen entradas racionales, `σ(Π_λ1)=Π_{σ(λ)}1`. Así `Π_λ1≠0` si y solo si `Π_{σ(λ)}1≠0`, y las raíces de un factor irreducible forman una sola órbita de Galois. El polinomio mínimo de la sucesión es `∏_{λ activo}(t−λ)`. `□`

### Una matriz cociente verificable

Elíjase un representante `x_i` de cada órbita `O_i`, y defínase

$$
A_{ij}=\#\{y\in O_j:T_w(x_i,y)=1\},\qquad D=\operatorname{diag}(|O_i|).
$$

En la base de indicadores de las órbitas, `A` es la matriz de `T_w` restringida a `V_w^G`; su polinomio característico es `χ_w`. La equivariancia da `|O_i|A_{ij}=|O_j|A_{ji}`. Por consiguiente, `B=D^{1/2}AD^{-1/2}` es simétrica y, con `z=D^{1/2}1`,

$$
\boxed{\;b_k=\mathbf1^\top D A^k\mathbf1=z^\top B^kz.\;}\tag{10}
$$

Esto permite estudiar la descomposición espectral y los espacios de Krylov con una matriz de orden `o_w`, en lugar de `3·2^{w−1}`.

### Cálculo exacto de la brecha para `w ≤ 10`

Con aritmética entera exacta sobre `A` se calculan, para cada ancho, el rango de Krylov sobre `ℚ`, el polinomio `χ_w`, su factorización en irreducibles sobre `ℚ` y qué factores son activos (`brecha_exacta.py`).

| Ancho `w` | Estados | Órbitas `o_w`, ec. (7) | Orden `d_w` | Distintos `r_w` | Núcleo | Factor inactivo `≠0` (grado) | `o_w−d_w = (o_w−r_w)+(r_w−d_w)` |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 3 | 1 | 1 | 1 | 0 | — | 0 = 0 + 0 |
| 2 | 6 | 1 | 1 | 1 | 0 | — | 0 = 0 + 0 |
| 3 | 12 | 2 | 2 | 2 | 0 | — | 0 = 0 + 0 |
| 4 | 24 | 3 | 3 | 3 | 0 | — | 0 = 0 + 0 |
| 5 | 48 | 6 | 5 | 6 | 0 | 1 (`t+1`) | 1 = 0 + 1 |
| 6 | 96 | 10 | 7 | 8 | 3 | — | 3 = 2 + 1 |
| 7 | 192 | 20 | 13 | 20 | 0 | 7 | 7 = 0 + 7 |
| 8 | 384 | 36 | 19 | 28 | 9 | 8 | 17 = 8 + 9 |
| 9 | 768 | 72 | 35 | 72 | 0 | 37 | 37 = 0 + 37 |
| 10 | 1536 | 136 | 51 | 92 | 45 | 40 | 85 = 44 + 41 |

En los diez anchos:

1. **La parte activa es un solo factor irreducible de grado `d_w`.** El polinomio mínimo de la recurrencia es irreducible sobre `ℚ`: los `d_w` autovalores activos forman una sola órbita de Galois.
2. **Los autovalores distintos de cero son simples en `V_w^G`.** Toda la multiplicidad está en el núcleo, que aparece en los anchos pares desde `w = 6`, con dimensiones 3, 9 y 45.
3. **Lo inactivo distinto de cero es un solo factor irreducible**, de grados 1, 7, 8, 37 y 40 para `w = 5, 7, 8, 9, 10`. En `w = 6` no hay.

Es decir, para `1 ≤ w ≤ 10`,

$$
\chi_w(t)=t^{\,z_w}\,f_w(t)\,g_w(t),
$$

con `f_w` irreducible, activo y de grado `d_w`; `g_w` irreducible e inactivo, o igual a 1; y `z_w` la dimensión del núcleo. Para el ancho 10: `136 = 51 + 40 + 45`. En la ecuación (9), la brecha `85` se reparte en `44` (multiplicidad del cero) y `41` (el cero y las 40 raíces de `g₁₀`).

### Pregunta abierta concreta

¿Vale `χ_w = t^{z_w} f_w g_w`, con `f_w` y `g_w` irreducibles, para todo `w`? ¿Qué fija los grados `d_w = deg f_w`, `deg g_w` y la dimensión del núcleo `z_w`? Una explicación de esa factorización daría `d_w` sin calcular rangos de Hankel.

La correspondencia de Lenard entre coloraciones de tres estados y el modelo de seis vértices, el trabajo de Lieb (1967) sobre el hielo cuadrado y las simetrías de grupos cuánticos en modelos XXZ estudiadas por Pasquier y Saleur (1990) son la dirección para contrastar. Para usarla hace falta establecer, para esta matriz con bordes libres, la equivalencia exacta de matrices, las condiciones de borde, el espacio de estados y las simetrías conservadas. Lieb resolvió el hielo cuadrado con bordes periódicos.

---

## Reproducción y estado de verificación

**Verificador sin dependencias externas** (unos segundos):

```bash
python3 -I verificar_revision.py
```

Comprueba las identidades de Q2 para todas las parejas de particiones de conjuntos de tamaños `1,…,5`; verifica los dos ejemplos; confirma que seis elementos es el tamaño mínimo del Ejemplo B; construye las órbitas de coloraciones de ancho `1,…,10` y las compara con (7); comprueba la reversibilidad ponderada de la matriz cociente, y calcula rangos de Krylov **módulo 1 000 000 007**, que son cotas inferiores del rango racional.

**Cálculo exacto sobre `ℚ`** (requiere `sympy`; unos segundos):

```bash
python3 -I brecha_exacta.py
```

Calcula `d_w` como rango exacto, el polinomio característico de `A`, su factorización y los factores activos; comprueba que `A` es diagonalizable y produce la tabla anterior.

**Certificados racionales originales** (desde `2026-11-08_economia_del_calculo/`):

```bash
python3 -I laboratorio_economia_relacional.py E5 E5x E5c
```

Certifican `d_1, …, d_10` con determinantes de Hankel exactos. El registro de las tres corridas está en `registro_verificacion.txt`.

### Estado de las afirmaciones

| Afirmación | Estado |
|---|---|
| Q2: fórmula de ciclos, cotas y equivalencia de permutabilidad | Demostrada; caracterización clásica de Ore y Birkhoff |
| Q2: identidad (3) con defecto y condición (5) | Demostrada |
| Q2: ley de producto sin permutabilidad | Ejemplo B, verificado; tamaño mínimo seis, por búsqueda exhaustiva |
| Q1: fórmula de órbitas (7) | Demostrada por Burnside |
| Q1: soporte espectral (8), brecha (9) y actividad por factores (Prop. 7) | Demostradas por álgebra lineal |
| Q1: valores `d_w` hasta 10 | Certificados por E5c y por el rango exacto de `brecha_exacta.py` |
| Q1: factorización `t^{z_w} f_w g_w` y reparto de la brecha, `w ≤ 10` | Cálculo exacto |
| Q1: forma general de `χ_w` y fórmula para `d_w` | Pregunta abierta |
| Q1: relación con XXZ y grupos cuánticos | Dirección por contrastar |

## Referencias y procedencia

1. **Publicación y certificados originales:** [La economía del cálculo desde las relaciones entre referencias y la solicitud «¿Dónde se ahorra el cálculo?», versión 2 (8 nov 2026)](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/2026-11-08-economia-del-calculo-v2/2026-11-08_economia_del_calculo).
2. **Revisión externa recibida el 19 nov 2026:** [u/DifficultAvocado6185](https://www.reddit.com/r/combinatorics/comments/1xrkk9h/comment/19sw59dkcp4io/). Aportó el grafo de intersecciones, el rango de ciclos, la cuenta por Burnside y las pistas espectrales. La formalización, el Ejemplo B y el cálculo exacto de la brecha son desarrollos posteriores de esa revisión.
3. Ø. Ore, *Theory of Equivalence Relations*, Duke Mathematical Journal **9** (1942), 573–627.
4. G. Birkhoff, [*Lattice Theory*, edición revisada](https://math.chapman.edu/~jipsen/summerschool/Birkhoff%201948%20Lattice%20Theory%20Revised%20Edition.pdf), AMS Colloquium Publications **25** (1948).
5. OEIS: [A207995](https://oeis.org/A207995) (coloraciones de ancho 6 salvo permutación de colores; recurrencia de orden 7), [A207996](https://oeis.org/A207996) (ancho 7) y [A207997](https://oeis.org/A207997) (la tabla completa `T(n,k)`).
6. [Pregunta técnica pública sobre los órdenes mínimos](https://cstheory.stackexchange.com/questions/57333/minimal-order-of-the-linear-recurrence-counting-3-colourings-of-w-%C3%97-m-grids-is).
7. [V. Pasquier y H. Saleur, *Common structures between finite systems and conformal field theories through quantum groups*, Nuclear Physics B **330** (1990), 523–556](https://inspirehep.net/literature/25720).
8. E. H. Lieb, [*Residual entropy of square ice*](https://doi.org/10.1103/PhysRev.162.162), Physical Review **162** (1967), 162–172.
9. J. Lamers, [*On elliptic quantum integrability: vertex models, solid-on-solid models and spin chains*](https://research-portal.uu.nl/ws/files/21138055/Lamers.pdf), tesis doctoral, Universidad de Utrecht (2016); §2.1, «Three-colourings», expone la correspondencia de Lenard.

---

**Le Matt Ansatz Di Ego** · Endless Monkey Project · Relational Geometry Program
