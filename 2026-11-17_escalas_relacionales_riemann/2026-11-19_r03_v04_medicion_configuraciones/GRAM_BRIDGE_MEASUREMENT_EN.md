# Weighted Gram bridge — revision 1.1

**19 November 2026 · Status: an exact bridge among known results, with a reproducible finite computation.**

## Finding

Three corrections are integrated: documentary identification of R–RH–01, pending comparison with the original; a projection computed independently from truncated integrals **both for the Gram matrix and the target vector**; and explicit separation of the families of approximating functions.

### Source and public-link requirement

The antecedent is **R–RH–01 — Primos, reflexión y cierre: una ruta relacional hacia la hipótesis de Riemann** (1 November 2026), identified in the program archive under `R_RH_01_Primos_Reflexion_y_Cierre_2026-11-01.md` and PDF. It contains the classical Nyman–Beurling/Báez-Duarte criterion, its Gram matrix, and the closed-form finite `d_2` calculation. **No public GitHub URL or authenticated original bytes for this manuscript have been verified.** The original should be compared and linked by a stable relative path or commit before merging. The package includes a reading transcription for comparison only, outside the integration folder.

Background source: L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, 2003, [arXiv:math/0202141](https://arxiv.org/abs/math/0202141).

## Exact bridge

For a finite set of primes `S`, write `M_S=∏_{p∈S}p` and `δ_S=∏_{p∈S}(1−1/p)`. Define

$$
E_S(y)=\sum_{1\le n\le y}\mathbf1_{\gcd(n,M_S)=1}-y\delta_S,
\quad f_d(t)=\{1/(dt)\},\quad h_S(t)=-E_S(1/t).
$$

Then elementary inclusion-exclusion gives

$$
h_S(t)=\sum_{d\mid M_S}\mu(d) f_d(t).
$$

Under `y=1/t` the weighted Gram matrix and target become

$$
G_{S,T}=\int_0^\infty E_S(y)E_T(y)y^{-2}\,dy,
\qquad b_S=-\int_1^\infty E_S(y)y^{-2}\,dy.
$$

For a finite family, the optimal squared distance is the standard projection formula `d²=1−b*G⁺b`. No novelty is claimed for this formula or the criterion.

## Independent truncated projection and tail enclosure

Take `S=∅` and `{2}`; these span the **same** space as `f_1,f_2`. On each interval `[n,n+1)`, compute `E_j(y)=A_j(n)−δ_j y` with `A_∅(n)=n` and `A_{2}(n)=⌈n/2⌉`. Compute both `G^(N)` over `(0,N)` and `b^(N)` over `(1,N)` by direct piecewise integration. Set `c_N=(G^(N))^{-1}b^(N)`. Since the restricted target norm is `1−1/N`, the restricted error is

$$
d_N^2=1-1/N-(b^{(N)})^*c_N.
$$

At `N=3000`, using `mpmath` with `45` digits: `d_N = 0.538346614598845...`. Closed-form constants are **not** used in that projection; they are used independently afterwards to obtain `d_2=0.538483587254247...`.

For `y≥N`, `|E_∅(y)|≤1` and `|E_{2}(y)|≤1/2`. Evaluating the full objective at the truncated minimizer provides the analytic enclosure

$$
d_N^2\le d_2^2\le d_N^2+
\frac{(1+|c_{N,0}|+|c_{N,1}|/2)^2}{N}.
$$

This yields `[0.538346614598845..., 0.541166573542464...]`. The truncation inequalities are rigorous in exact arithmetic, but the printed decimal endpoints are **not** directed-rounding interval certificates.

## Function families: do not conflate

| Family | Span | Interpretation |
|---|---|---|
| Two sieve references | `span(h_∅, h_{2})=span(f_1,f_2)` | Direct comparison with the finite `d_2` in R–RH–01 |
| All sieve subsets of a finite prime set `P` | `span{h_S:S⊆P}=span{f_d:d\mid\prod_{p∈P}p}` | Exactly `2^|P|` squarefree divisor indices |
| Integer-dilation Béz-Duarte truncation `m` | `span{f_n:1≤n≤m}` | Includes indices with repeated prime factors; `m` and `|P|` are different parameters |

Special Möbius-coefficient trial approximants are not interchangeable with optimal Gram projections. Inversion on the subset lattice proves the second span equality.

## Contribution and scope

This supplies a traceable **integration** between finite prime-reference discrepancies, weighted Gram measurement, and an established closure criterion. It is mathematically exact and independently testable. RH remains open.

Reproduce in an environment with `mpmath>=1.3` using `python verificacion_puente_gram_v1_1.py --N 3000 --dps 45`. No random seeds are used. `EJECUCION_LOCAL_2026-11-19.txt` records an earlier package run; current branch results are documented in the PR. Comparing and linking the original R–RH–01 remains a prerequisite before merging.

**Endless Monkey Project**<br>
Relational Geometry Program<br>
Le Matt Ansatz Di Ego
