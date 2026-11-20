# Active distinctions, cycles and minimal recurrences

**Mathematical appendix to the review request “Where does computation become cheaper?”**

19 November 2026 · Technical revision for the repository

[Español](ANEXO_ECONOMIA_ES.md)

## Summary

Two questions from the 8 November 2026 publication become sharper after an external mathematical review:

1. **Partitions (Q2).** The bipartite intersection graph gives an exact identity with the cycle rank and extends the original covariance identity to every pair of partitions through a nonnegative defect. The product law is equivalent to `k·Cov = δ`. Example B satisfies it without permuting, on six elements, which is the minimum size.
2. **Grids (Q1).** The number of orbits under colour permutation and reflection has a closed form by Burnside. The minimal recurrence order is the number of distinct eigenvalues that touch the counting vector. Exact computation for widths 1 to 10 gives the shape of that recurrence: its polynomial is irreducible over `ℚ`, of degree `d_w`, and the difference with the number of orbits splits between the kernel and a second irreducible factor. For width 10: `136 = 51 + 40 + 45`.

The text separates three levels: proven identities, exact computations for `w ≤ 10`, and the question of a general law.

---

## Q2. Intersections of partitions

### Definitions

Let `X` be a finite nonempty set, and let `P` and `Q` be partitions of `X`.

- `P ∧ Q` is the fine partition whose blocks are the **nonempty** intersections `B ∩ C` with `B ∈ P`, `C ∈ Q`.
- `P ∨ Q` is the coarse partition of the smallest equivalence relation containing both equivalence relations.
- Let `𝒥 = P ∨ Q` and `k = |𝒥| ≥ 1`. For each `J ∈ 𝒥`, `p_J` and `q_J` count the blocks of `P` and `Q`, respectively, contained in `J`.
- `e_J` is the number of pairs `(B,C)` of blocks of `P` and `Q` contained in `J` with `B ∩ C ≠ ∅`.

The covariance is taken **uniformly over the `k` join blocks**:

$$
\operatorname{Cov}_{\mathcal J}(p,q)
=\frac1k\sum_{J\in\mathcal J}p_Jq_J
-\frac{|P||Q|}{k^2}.
$$

The simple bipartite graph `G(P,Q)` has one vertex per block of `P`, one vertex per block of `Q`, and one edge per nonempty intersection. Its connected components are exactly the blocks of `P ∨ Q`.

### Proposition 1. Cycle identity and sharp bounds

If `β₁(G)` is the cyclomatic number (dimension of the cycle space over `𝔽₂`), then

$$
\boxed{|P\wedge Q|=|P|+|Q|-|P\vee Q|+\beta_1(G).}\tag{1}
$$

Moreover,

$$
\boxed{|P|+|Q|-k\;\leq\;|P\wedge Q|\;\leq\;\sum_{J\in\mathcal J}p_Jq_J.}\tag{2}
$$

The lower bound is an equality if and only if `G` is a forest. The upper bound is an equality if and only if every component `G[J]` is the complete bipartite graph `K_{p_J,q_J}`.

**Proof.** The graph has `|P|+|Q|` vertices, `|P ∧ Q|` edges and `k` components. For every finite graph the cycle space has dimension `E−V+k`, which gives (1). Each component is connected, so `e_J ≥ p_J+q_J−1`, with equality exactly for a tree. There is at most one edge per pair of blocks, so `e_J ≤ p_Jq_J`, with equality exactly when every pair intersects. Summing over `J` gives (2). `□`

### Proposition 2. Permutability and bipartite completeness

The following conditions are equivalent:

1. The equivalence relations of `P` and `Q` permute: `R_P ∘ R_Q = R_Q ∘ R_P`.
2. `R_P ∘ R_Q = R_{P∨Q}`.
3. Inside each `J ∈ P∨Q`, **every** block of `P` meets **every** block of `Q`.
4. `G[J]` is `K_{p_J,q_J}` for each `J`.
5. `|P∧Q| = Σ_J p_Jq_J`.

**Proof.** Conditions 3, 4 and 5 are equivalent by the definition of the edges and the upper bound of Proposition 1. If the relations permute, their composition is an equivalence relation containing both, hence their join `R_{P∨Q}`: given `x` and `z` in the same `J`, there is `y` with `x R_P y R_Q z`, so the `P`-block of `x` meets the `Q`-block of `z`. Conversely, if all such pairs of blocks meet, that `y` exists for any `x,z ∈ J`, so `R_{P∨Q} ⊆ R_P ∘ R_Q`. The reverse inclusion is immediate. Exchanging `P,Q` gives `R_P ∘ R_Q = R_Q ∘ R_P`. `□`

The equivalence is the classical characterization of permuting equivalence relations (Ore, 1942; Birkhoff, 1948).

### Theorem 3. General covariance–defect identity

Define the **intersection defect**

$$
\delta(P,Q)=\sum_{J\in\mathcal J}(p_Jq_J-e_J)
=\sum_{J\in\mathcal J}p_Jq_J-|P\wedge Q|.
$$

Then `δ(P,Q) ≥ 0` and

$$
\boxed{\;k|P\wedge Q|
=|P||Q|+k^2\operatorname{Cov}_{\mathcal J}(p,q)-k\delta(P,Q).\;}\tag{3}
$$

Also

$$
\boxed{\;\beta_1(G)=\sum_{J\in\mathcal J}(p_J-1)(q_J-1)-\delta(P,Q).\;}\tag{4}
$$

`δ(P,Q)=0` if and only if `P` and `Q` permute.

**Proof.** By the definition of the covariance,

$$
k^2\operatorname{Cov}_{\mathcal J}(p,q)
=k\sum_Jp_Jq_J-|P||Q|.
$$

Substituting `Σ_Jp_Jq_J = |P∧Q|+δ(P,Q)` and rearranging gives (3). By (1),

$$
\begin{aligned}
\beta_1(G)
&=|P\wedge Q|-|P|-|Q|+k\\
&=\sum_J[p_Jq_J-p_J-q_J+1]-\delta(P,Q),
\end{aligned}
$$

which is (4). The equivalence `δ=0 ⇔` permutability follows from Proposition 2. `□`

**Consequence.** The product law

$$
|P\wedge Q|\,|P\vee Q|=|P|\,|Q|
$$

holds exactly when

$$
\boxed{\;k\operatorname{Cov}_{\mathcal J}(p,q)=\delta(P,Q).\;}\tag{5}
$$

Permutability with zero covariance is one way to satisfy (5). The other is a positive defect balancing a positive covariance. This corrects claim 1 of the review request, which required permutability and zero covariance.

### Two checkable examples

**Example A: the single cycle of the external comment.** Take

- `P = {{a,b},{c,d},{e}}`;
- `Q = {{a,c},{b,d},{e}}`.

Here `|P|=|Q|=3`, `k=2`, `|P∧Q|=5`, `p=(2,1)`, `q=(2,1)`, `Cov=1/4`, `δ=0`, `β₁=1`. Thus `5·2=9+4·(1/4)=10`. The first component is `K₂,₂`, with one independent cycle.

**Example B: product law without permutability.** Take

- `X={a,b,c,d,e,f}`;
- `P={{a},{b,c,d},{e,f}}`;
- `Q={{a},{b,e},{c,f},{d}}`.

Here `|P|=3`, `|Q|=4`, `k=2`, `|P∧Q|=6`, `p=(1,2)`, `q=(1,3)`, `Cov=1/2`, `δ=1` and `β₁=1`. Hence

$$
6\cdot2=3\cdot4+4\cdot\tfrac12-2\cdot1=12.
$$

The product law holds; the second component is `K₂,₃` with one edge missing, and the relations **do not permute**.

Six elements is the minimum size: on sets of up to five elements, every pair of partitions satisfying the product law permutes (exhaustive search). On a six-element set there are 720 ordered pairs that satisfy it without permuting.

---

## Q1. Colourings and minimal recurrence order

### Definitions

Let `X_w` be the set of proper three-colourings of a column of height `w`. Then

$$
|X_w|=3\cdot2^{w-1}\quad(w\ge1).
$$

For `x,y ∈ X_w`, define the symmetric transfer matrix

$$
(T_w)_{xy}=\begin{cases}1,&x_i\ne y_i\text{ for all }i,\\0,&\text{otherwise.}\end{cases}
$$

The number of proper colourings of the grid `P_w □ P_m`, with free boundaries, is

$$
a_w(m)=\mathbf1^\top T_w^{m-1}\mathbf1,\qquad m\ge1.\tag{6}
$$

The group `S₃ × C₂` acts by global colour permutation and vertical reflection of the column. Let `o_w` be the number of orbits.

### Proposition 4. Closed orbit formula

For `w=1`, `o₁=1`. For `w≥2`, with `n=w−1`,

$$
\boxed{\;o_w=\frac{2^n+2^{\lceil n/2\rceil}+\mathbf1_{2\mid n}\,2^{n/2}}4.\;}\tag{7}
$$

**Proof.** A column is determined by its first colour and the steps `s_i = x_{i+1}-x_i ∈ {+1,-1}` in `ℤ/3ℤ`, `1≤i≤n`. The six permutations of `ℤ/3ℤ` are the affine maps `x ↦ ±x+b`: they act transitively on the first colour and, on the step word, induce the identity or global negation. Reflection reverses the order of the steps and negates them. So orbits of columns correspond to orbits of words in `{±1}^n` under the four maps `id`, `negation`, `reversal` and `negation◦reversal`.

For `n≥1`, the numbers of fixed words are, in that order,

$$
2^n,\quad 0,\quad 2^{\lceil n/2\rceil},\quad
\begin{cases}2^{n/2},&n\text{ even},\\0,&n\text{ odd}.\end{cases}
$$

Burnside gives (7). For `w=1`, the three colourings are equivalent under colour permutation. `□`

### Theorem 5. Spectral support and minimal recurrence

Let `b_k=1ᵀT_w^k1` (`k≥0`). Let `Λ_w` be the set of **distinct** eigenvalues of `T_w` and `Π_λ` the orthogonal projection onto the eigenspace of `λ`. Then

$$
\boxed{\;d_w
=\#\{\lambda\in\Lambda_w:\Pi_\lambda\mathbf1\ne0\}
=\operatorname{rank}_{\mathbb Q}(b_{i+j})_{i,j\ge0}
=\dim_{\mathbb Q}\operatorname{span}\{T_w^j\mathbf1:j\ge0\}.\;}\tag{8}
$$

Here `d_w` is the minimal order of a homogeneous linear recurrence valid from `k=0` for the sequence `b_k`.

**Proof.** `T_w` is real and symmetric, so it has an orthogonal spectral decomposition. Hence

$$
b_k=\sum_{\lambda\in\Lambda_w}
\underbrace{\|\Pi_\lambda\mathbf1\|^2}_{c_\lambda\ge0}\lambda^k.
$$

Let `λ₁,…,λ_d` be the distinct values with `c_{λ_j}>0`. Their powers give `d` linearly independent geometric sequences (Vandermonde). The polynomial `∏_{j=1}^d(t−λ_j)` annihilates the sequence; no polynomial of lower degree does so from `k=0`. Moreover,

$$
H_N=(b_{i+j})_{0\le i,j<N}
=V_N\operatorname{diag}(c_{\lambda_1},\ldots,c_{\lambda_d})V_N^\top
$$

with `V_N=(λ_j^i)`, so `rank(H_∞)=d`, `det H_d>0` and `det H_{d+1}=0`. By symmetry, `H_N` is the Gram matrix of `1,T1,…,T^{N−1}1`, and its rank is the Krylov dimension. The matrices are rational, so the rank is the same over `ℚ` and `ℝ`. `□`

**Zero root and shift.** For the shifted Hankel matrix `H_d^{(1)}=(b_{1+i+j})_{0≤i,j<d}`,

$$
\det H_d^{(1)}=\left(\prod_{j=1}^{d}\lambda_j\right)\det H_d.
$$

So `det H_d^{(1)}≠0` means that no active eigenvalue is zero. This is what keeps the same minimal order when the recurrence starts one position later.

**Certificate by two determinants.** Since `H_N` is a Gram matrix, `det H_d ≠ 0` says that `1, T1, …, T^{d−1}1` are independent, and `det H_{d+1} = 0` says that `T^d1` depends on them. The Krylov space then has dimension `d`, and the order-`d` recurrence holds for every `k`. This is why the determinants of experiment E5c (`det H_d ≠ 0`, `det H_{d+1} = 0`, `det H_d^{(1)} ≠ 0`) certify `d_w` and the absence of a zero root.

### Proposition 6. The orbit reduction does not exhaust the linear saving

Let `G=S₃×C₂`, and let `V_w^G ⊆ ℝ^{X_w}` be the subspace of vectors constant on each orbit. Since `T_w` commutes with `G` and `1∈V_w^G`,

$$
d_w\le \dim V_w^G=o_w\le |X_w|.
$$

Let `r_w` be the number of distinct eigenvalues of `T_w` restricted to `V_w^G`, and `m_λ` the multiplicity of each in that subspace. Then

$$
\boxed{\;o_w-d_w
=\underbrace{\sum_{\lambda}(m_\lambda-1)}_{o_w-r_w}
+\underbrace{\#\{\lambda:\Pi_\lambda\mathbf1=0\text{ in }V_w^G\}}_{r_w-d_w}.\;}\tag{9}
$$

**Proof.** The symmetry of `T_w` preserves the fixed subspace. It has a basis of orbit indicators, hence dimension `o_w`. The orthogonal eigenspace decomposition of the restriction gives `o_w=Σ_λm_λ`, with `r_w` terms. Each `Π_λ1` lies in `V_w^G`, because `Π_λ` is a polynomial in `T_w`; only values with nonzero projection contribute to `d_w` by Theorem 5. Subtracting gives (9). `□`

### Proposition 7. Activity goes by irreducible factors

Let `χ_w` be the characteristic polynomial of `T_w` restricted to `V_w^G`. If `f` is an irreducible factor of `χ_w` over `ℚ`, either all its roots are active (`Π_λ1 ≠ 0`) or none is. Consequently, the minimal polynomial of the sequence `b_k` is the product of the active irreducible factors, each with exponent 1, and `d_w` is the sum of their degrees.

**Proof.** `Π_λ = ∏_{μ≠λ}(T_w−μ)/(λ−μ)`, with `μ` over the distinct eigenvalues of the restriction. If `σ` is an automorphism of the splitting field of `χ_w`, then, since `T_w` and `1` have rational entries, `σ(Π_λ1)=Π_{σ(λ)}1`. So `Π_λ1≠0` if and only if `Π_{σ(λ)}1≠0`, and the roots of an irreducible factor form one Galois orbit. The minimal polynomial of the sequence is `∏_{λ active}(t−λ)`. `□`

### A checkable quotient matrix

Choose a representative `x_i` of each orbit `O_i`, and define

$$
A_{ij}=\#\{y\in O_j:T_w(x_i,y)=1\},\qquad D=\operatorname{diag}(|O_i|).
$$

In the basis of orbit indicators, `A` is the matrix of `T_w` restricted to `V_w^G`; its characteristic polynomial is `χ_w`. Equivariance gives `|O_i|A_{ij}=|O_j|A_{ji}`. Hence `B=D^{1/2}AD^{-1/2}` is symmetric and, with `z=D^{1/2}1`,

$$
\boxed{\;b_k=\mathbf1^\top D A^k\mathbf1=z^\top B^kz.\;}\tag{10}
$$

Spectral decomposition and Krylov spaces can thus be studied with a matrix of order `o_w` instead of `3·2^{w−1}`.

### Exact computation of the gap for `w ≤ 10`

Exact integer arithmetic on `A` gives, for each width, the Krylov rank over `ℚ`, the polynomial `χ_w`, its factorization into irreducibles over `ℚ`, and which factors are active (`brecha_exacta.py`).

| Width `w` | States | Orbits `o_w`, eq. (7) | Order `d_w` | Distinct `r_w` | Kernel | Inactive factor `≠0` (degree) | `o_w−d_w = (o_w−r_w)+(r_w−d_w)` |
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

In all ten widths:

1. **The active part is a single irreducible factor of degree `d_w`.** The minimal polynomial of the recurrence is irreducible over `ℚ`: the `d_w` active eigenvalues form one Galois orbit.
2. **Nonzero eigenvalues are simple in `V_w^G`.** All multiplicity sits in the kernel, which appears in even widths from `w = 6` on, with dimensions 3, 9 and 45.
3. **The inactive nonzero part is a single irreducible factor**, of degrees 1, 7, 8, 37 and 40 for `w = 5, 7, 8, 9, 10`. At `w = 6` there is none.

That is, for `1 ≤ w ≤ 10`,

$$
\chi_w(t)=t^{\,z_w}\,f_w(t)\,g_w(t),
$$

with `f_w` irreducible, active and of degree `d_w`; `g_w` irreducible and inactive, or equal to 1; and `z_w` the kernel dimension. For width 10: `136 = 51 + 40 + 45`. In equation (9), the gap `85` splits into `44` (multiplicity of zero) and `41` (zero and the 40 roots of `g₁₀`).

### A concrete open question

Does `χ_w = t^{z_w} f_w g_w`, with `f_w` and `g_w` irreducible, hold for every `w`? What fixes the degrees `d_w = deg f_w`, `deg g_w` and the kernel dimension `z_w`? An explanation of this factorization would give `d_w` without computing Hankel ranks.

Lenard's correspondence between three-state colourings and the six-vertex model, Lieb's 1967 work on square ice, and the quantum-group symmetries of XXZ models studied by Pasquier and Saleur (1990) are the direction to test. Using it requires establishing, for this free-boundary matrix, the exact matrix equivalence, the boundary conditions, the state space and the conserved symmetries. Lieb solved square ice with periodic boundaries.

---

## Reproduction and verification status

**Verifier without external dependencies** (a few seconds):

```bash
python3 -I verificar_revision.py
```

It checks the Q2 identities for every pair of set partitions of sizes `1,…,5`; checks both examples; confirms that six elements is the minimum size for Example B; builds the colouring orbits for widths `1,…,10` and compares them with (7); checks the weighted symmetry of the quotient matrix; and computes Krylov ranks **modulo 1,000,000,007**, which are lower bounds for the rational rank.

**Exact computation over `ℚ`** (requires `sympy`; a few seconds):

```bash
python3 -I brecha_exacta.py
```

It computes `d_w` as an exact rank, the characteristic polynomial of `A`, its factorization and the active factors; it checks that `A` is diagonalizable and produces the table above.

**Original rational certificates** (from `2026-11-08_economia_del_calculo/`):

```bash
python3 -I laboratorio_economia_relacional.py E5 E5x E5c
```

They certify `d_1, …, d_10` with exact Hankel determinants. The log of the three runs is in `registro_verificacion.txt`.

### Claim status

| Claim | Status |
|---|---|
| Q2: cycle formula, bounds and permutability equivalence | Proven; classical characterization by Ore and Birkhoff |
| Q2: defect identity (3) and condition (5) | Proven |
| Q2: product law without permutability | Example B, checked; minimum size six by exhaustive search |
| Q1: orbit formula (7) | Proven by Burnside |
| Q1: spectral support (8), gap (9) and activity by factors (Prop. 7) | Proven by linear algebra |
| Q1: values `d_w` up to 10 | Certified by E5c and by the exact rank in `brecha_exacta.py` |
| Q1: factorization `t^{z_w} f_w g_w` and split of the gap, `w ≤ 10` | Exact computation |
| Q1: general form of `χ_w` and a formula for `d_w` | Open question |
| Q1: relation to XXZ and quantum groups | Direction to test |

## References and provenance

1. **Original publication and certificates:** [The economy of computation from relations between references and the request “Where does computation become cheaper?”, version 2 (8 Nov 2026)](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/2026-11-08-economia-del-calculo-v2/2026-11-08_economia_del_calculo).
2. **External review received 19 Nov 2026:** [u/DifficultAvocado6185](https://www.reddit.com/r/combinatorics/comments/1xrkk9h/comment/19sw59dkcp4io/). It contributed the intersection graph, the cycle rank, the Burnside count and the spectral leads. The formalization, Example B and the exact computation of the gap are later developments of that review.
3. Ø. Ore, *Theory of Equivalence Relations*, Duke Mathematical Journal **9** (1942), 573–627.
4. G. Birkhoff, [*Lattice Theory*, revised edition](https://math.chapman.edu/~jipsen/summerschool/Birkhoff%201948%20Lattice%20Theory%20Revised%20Edition.pdf), AMS Colloquium Publications **25** (1948).
5. OEIS: [A207995](https://oeis.org/A207995) (width-6 colourings up to colour permutation; order-7 recurrence), [A207996](https://oeis.org/A207996) (width 7) and [A207997](https://oeis.org/A207997) (the full table `T(n,k)`).
6. [Public technical question on the minimal orders](https://cstheory.stackexchange.com/questions/57333/minimal-order-of-the-linear-recurrence-counting-3-colourings-of-w-%C3%97-m-grids-is).
7. [V. Pasquier and H. Saleur, *Common structures between finite systems and conformal field theories through quantum groups*, Nuclear Physics B **330** (1990), 523–556](https://inspirehep.net/literature/25720).
8. E. H. Lieb, [*Residual entropy of square ice*](https://doi.org/10.1103/PhysRev.162.162), Physical Review **162** (1967), 162–172.
9. J. Lamers, [*On elliptic quantum integrability: vertex models, solid-on-solid models and spin chains*](https://research-portal.uu.nl/ws/files/21138055/Lamers.pdf), PhD thesis, Utrecht University (2016); §2.1, “Three-colourings”, presents Lenard's correspondence.

---

**Le Matt Ansatz Di Ego** · Endless Monkey Project · Relational Geometry Program
