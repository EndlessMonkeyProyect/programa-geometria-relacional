# Persistent Core, Inheritance, Granularity, and Reclosure

## Formal Results and Correspondences Across Scales

**Consolidated:** November 21, 2026  
**Publication version:** 3.5  
**Destination:** additive contribution to the repository  
**Public signature:** Le Matt Ansatz Di Ego · Endless Monkey Project / Relational Geometry Program

### Abstract

A relational system develops from a persistent core through compatible extensions of reference. **History** identifies the provenance and dependencies of distinctions; **inheritance** denotes the operational preservation of established answers under an extension; **granularity** quantifies the distinctions accessible under a reference; **reclosure** expresses the recovery of a relation within a query contract. This separation supports exact results in arithmetic, relational geometry, and function spaces.

The results consolidated here comprise exact transport between normalizers, an algebraic remainder law, cancellation of jumps when any integer scale is doubled, energy and projection identities, an exact formula for periodic cost, a three-window decomposition of functional reconstruction, and a reproducible measurement of recovery by dyadic blocks. Each connection is stated through the concrete objects and operators that make comparison possible.

## 1. Foundational Contract

Let a reference structure at level $k$ be $\mathcal S_k=(X_k,Q_k,\Phi_k,\mathcal A_k)$, where $X_k$ is a set of states, $Q_k$ is the family of questions, $\Phi_k$ is an observational representation, and $\mathcal A_k$ is a family of admissible decoders. An extension $\iota_k:\mathcal S_k\to\mathcal S_{k+1}$ **inherits** a query $q\in Q_k$ when the answer obtained in the new reference agrees with the previously established answer through the declared transport map.

History is the provenance structure $\mathcal H_k$ that reconstructs how distinctions were established and which relations they depend on. Inheritance is the operational property of compatible extensions. The former preserves **traceability**; the latter preserves **the ability to answer**. The core need not be displaced for the structure to incorporate new distinctions: growth extends relations, as illustrated by a trunk growing from a persistent base.

In ROSI, a difference becomes operational information when a question and a procedure distinguish it in a recoverable way. The sufficiency of a signature $\Phi$ for a query $q$ is expressed by

$$
q=\bar q\circ\Phi
$$

for an admissible decoder $\bar q$. This identity, used in MF-86 and CR-6, gives a precise contract for stating what each interface preserves.

## 2. Exact Results Across Scales

### R1 — Inherited Transport of a Rational Value (O40)

For integers $N,q\ge1$ and any integer numerator $h$, a change of scale preserves the ratio:

$$
\frac hN=\frac{qh}{qN}.
$$

Transport of the reference changes the representation and preserves the value. New distinctions are organized with a common denominator, while the recoverable relation from the previous level is retained. **Status:** exact algebraic identity; original formalization: O40, October 20, 2026.

### R2 — Algebraic Remainder with Decreasing Granularity (O58 / G-01)

For integers satisfying $a^2+b^2+1=N^2$, one has

$$
\frac{a^2+b^2}{N^2}+\frac1{N^2}=1.
$$

Granularity $g_N=N^{-2}$ is positive at each level and tends to zero along any admissible sequence with $N\to\infty$. Exact examples are $(a,b,N)=(2,2,3),(4,8,9),(12,12,17)$. **Status:** exact algebraic identity and limit. The parameter $g_N$ belongs to the O58 contract.

### R3 — Arithmetic Reclosure on Doubling the Scale

Let $\mu$ be the Möbius function, and define

$$
J_N(n)=\sum_{\substack{d\mid n\\d\le N}}\mu(d).
$$

**Identity.** For all integers $N\ge1$ and $N<n\le2N$,

$$
\boxed{J_N(n)=-\mu(n),\qquad J_{2N}(n)=0.}
$$

**Proof.** Every proper divisor $d$ of $n$ satisfies $d\le n/2\le N$. Thus $J_N(n)$ contains all proper divisors. Since $n>1$, the identity $\sum_{d\mid n}\mu(d)=0$ yields $J_N(n)=-\mu(n)$. At scale $2N$, the divisor $d=n$ is included as well, and the sum vanishes. $\square$

This is the identity $\sum_{d\mid n}\mu(d)=0$ ($n>1$) read between two scales: in the interval $(N,2N]$, the only missing divisor is $n$ itself, and the statement holds for every integer scale $N$. The moving-wall picture in laboratory CME-002 illustrates the addition of the missing reference; the identity itself concerns the divisor system exactly.

**Control instance.** In the transition $1024\to2048$, the $1024$ new integers comprise $621$ with $\mu(n)\ne0$ (active jumps that cancel) and $403$ with $\mu(n)=0$ (jumps already zero). The exact count is checked by `scripts/verificar_resultados.py`.

**Example.** For $n=1030=2\cdot5\cdot103$, the seven proper divisors are $1,2,5,10,103,206,515$, whose Möbius values sum to $+1$. Including the divisor $1030$, with $\mu(1030)=-1$, cancels the jump.

## 3. Laboratories: Operational Correspondences

**ROSI — Recoverable difference.** Observables are specified by questions and procedures; inheritance preserves the results of certified queries when references are extended.

**Mirror box / CME-002 — Reflection and reclosure.** The moving-wall experiments distinguish the continuity of a relation, the opening of new configurations, and closure under composition. The exact arithmetic parallel is expressed through $J_N$ and the Möbius sum. Its correspondence with optics is recorded as a structured analogy pending a transformation that preserves all operators.

**Spheres, tetrahedron, and references.** Adding a reference expands the collection of comparisons. In the model $\mathbb F_2^4$, the pairwise-comparison signature $\Phi(x)=(x_i\oplus x_j)_{i<j}$ satisfies $\Phi(x)=\Phi(y)$ exactly when $y=x$ or $y=x\oplus1111$. The model exhibits an exact observational equivalence between two configurations and supports a study of the cost of an additional reference.

**Normalizers and query economy (O40, O58, MF-86, CR-6).** Granularity specifies a resolution; sufficiency specifies which questions can be answered; cost characterizes the reconstruction procedure. Each result has its own contract, and contracts are compared through an explicit transformation of observables.

## 4. Functional Recovery as an Extension of Relations

Let $H=L^2((0,\infty),dx)$, $\chi=\mathbf1_{(0,1]}$, $f_n(x)=\{1/(nx)\}$, and $W_m=\operatorname{span}\{f_n:1\le n\le m,\ \mu(n)\ne0\}$. If $P_m$ is the orthogonal projection onto $W_m$ and $e_m=\|\chi-P_m\chi\|_2$, then, for $m<n$,

$$
\boxed{e_m^2-e_n^2=\|(P_n-P_m)\chi\|_2^2.}
$$

**Proof.** The spaces $W_m\subseteq W_n$ are nested. The components $P_m\chi$, $(P_n-P_m)\chi$, and $\chi-P_n\chi$ are orthogonal. By the Pythagorean theorem, the difference of squared errors equals the energy of the newly added direction. $\square$

This identity gives an **exact accounting** of recovery through inheritance in Hilbert spaces. The reflection $\mathscr R_{m,n}=I-2(P_n-P_m)$ represents the gain algebraically:

$$
 e_m^2-e_n^2=\tfrac14\|r_m-\mathscr R_{m,n}r_m\|_2^2,\qquad r_m=(I-P_m)\chi.
$$

With $\gamma_m=(e_m^2-e_{2m}^2)/e_m^2$ for $e_m>0$, continuity across scales has the exact multiplicative form

$$
\boxed{e_{2^J}^2=e_1^2\prod_{j=0}^{J-1}(1-\gamma_{2^j}).}
$$

This multiplicative form is the accounting used in RA–01 (§5).

### Reproduced Numerical Measurements

For squarefree references, laboratory S–RA–01 reproduces the Gram-matrix record: $e_{1024}^2=0{,}0066723$, $e_{2048}^2=0{,}0062291$, and a recovered fraction of $6{,}64\,\%$. The calculation uses an exact formula for the inner products $\langle f_n,f_m\rangle$, numerically checked against integration over intervals with an approximate tail, and double precision with condition number $1{,}6\cdot10^6$ after diagonal scaling. These are reproducible measurements; the R3 identities are exact.

## 5. Granularity and a Reconstruction Certificate

For an admissible approximant $a(x)=\sum_{n\in I}c_nf_n(x)$, let $B(x)=\chi(x)-a(x)$, $L=\sum|c_n|$, and $C=\sum c_n/n$. If $0<\varepsilon\le1\le R$, then

$$
\boxed{\|B\|_2^2\le \varepsilon(1+L)^2+\int_\varepsilon^R|B(x)|^2\,dx+\frac{|C|^2}{R}.}
$$

**Proof.** On $(0,\varepsilon)$, each $f_n$ lies in $[0,1)$, so $|B|\le1+L$. On $(R,\infty)$, $f_n(x)=1/(nx)$ and $\chi(x)=0$, hence $B(x)=-C/x$ and the final integral equals $|C|^2/R$ exactly. The middle region remains an explicit integral. $\square$

The inequality is a **three-window decomposition**: an exact bound near zero (granularity $\varepsilon$ and cost $L$), an explicit integral over the middle window, and an exact tail ($C$). Recovery of the query occurs in the middle window. A family of coefficients and windows for which all three terms tend to zero gives global approximation in $L^2$.

### Exact Periodic Energy of the Fine Window

Let $M=\operatorname{lcm}(I)$. The energy of one period is

$$
Q_I(c)=\frac1M\int_0^M\left|1-\sum_{n\in I}c_n\{u/n\}\right|^2du.
$$

For real coefficients (and, by extension, with conjugates for complex coefficients),

$$
\boxed{Q_I(c)=\left(1-\tfrac12\sum_nc_n\right)^2+\frac1{12}\sum_{n,m\in I}c_nc_m\frac{\gcd(n,m)^2}{nm}.}
$$

The formula gives an explicit arithmetic measure of interior oscillation cost. The included verifier compares it with exact integration over rational intervals for finite families of coefficients.

### Certifiable Transfer Rule

Given a family of normalizers $N_k\to\infty$, choose approximants $a_k\in W_{m(k)}$, with $m(k)\to\infty$, and document bounds $A_k,B_k\ge0$ such that

$$
\|\chi-a_k\|_2^2\le A_kN_k^{-2}+B_k,\qquad A_kN_k^{-2}+B_k\to0.
$$

Then $e_{m(k)}\to0$. This implication follows from the optimality of orthogonal projections. The classical Nyman–Beurling / Báez-Duarte functional criterion uses convergence of the full family of integer dilations in the study of RH. Convergence of the squarefree subfamily is sufficient for convergence of the full family. The explicit construction and uniform bounds are stated as **conditions for applying** the certificate.

### RA–01 — Certifiable Accumulated Recovery by Seeds

RA–01 applies Theorem 4 of CR-6 (the implication from accumulated relative gain) to the dyadic chain, with an explicit per-seed bound. At each dyadic scale $j$, the inherited increment is $W_{j+1}\supseteq W_j$. With $r_j=\chi-P_j\chi$, an explicit seed $g_j\in W_{j+1}$, and its new part $u_j=(I-P_j)g_j$, the certified gain is

$$
d_j=\frac{|\langle r_j,g_j\rangle|^2}{\|u_j\|^2}
\le e_j^2-e_{j+1}^2
\qquad (u_j\ne0).
$$

**Theorem RA–01 (proved implication).** If one certifies $a_j\ge0$ and $E_j>0$ such that $d_j\ge a_j$, $e_j^2\le E_j$, and $\sum_j a_j/E_j=\infty$, then $e_j\to0$. The proof uses orthogonal projection and the product of reductions:

$$
e_J^2\le e_0^2\exp\!\left(-\sum_{j<J}\frac{a_j}{E_j}\right).
$$

**Exactness and sufficiency.** Divergence of the sum of **optimal relative gains** $\gamma_j=(e_j^2-e_{j+1}^2)/e_j^2$ is necessary and sufficient for closure when all errors are positive (or exact closure occurs in one step). For the **gains of a fixed seed**, divergence of $\sum a_j/E_j$ is only sufficient. A seed can be orthogonal to the residual even when the enlarged space approximates it completely; the appendix gives an exact counterexample. The classical bound $e_j^2\gtrsim1/j$ limits partial sums of certificates by $\sum_{j<J}a_j/E_j\le\log J+C$, without imposing a per-block rate of $1/j$.

The proposed arithmetic seed is $g_j=\sum_{2^j<n\le2^{j+1}}\mu(n)f_n$. Its jump reclosure is certified by R3. In laboratory S–RA–01, this seed recovers between 51% and 100% of the optimal gain in each block for $j\le10$ (60% in 1024→2048). Over the interval studied, $(j+1)d_j/e_j^2$ takes approximate values from $0{,}437$ to $1{,}197$ for $j=3,\dots,10$. In the first two blocks, the seed matches the best individual reference; in later blocks, it exceeds it. This finite pattern is compatible with $1/(j+1)$; applying the theorem requires proof that the certified gains diverge over all scales. See the [RA–01 proof and protocol](../anexos/RA-01_recuperacion_acumulada/documentos/PROPOSICION_RECUPERACION_ACUMULADA_2026-11-21.md), the [exact finite-control verifier](../scripts/verificar_ra01.py), and [laboratory S–RA–01](../laboratorios/2026-11-21_RA01_semilla_mobius/documentos/LAB_RA01_SEMILLA_MOBIUS_2026-11-21.md).

## 6. Traceability and Verifiable Status of Results

| Code | Result | Certified scope | Main source |
|---|---|---|---|
| R1 | Rational inheritance $h/N=qh/(qN)$ | Exact identity | O40; Granularity and Remainder |
| R2 | O58 law $1/N^2$ | Identity and limit along admissible sequences | G-01/O58; technical appendix |
| R3 | $J_N(n)=-\mu(n)$, $J_{2N}(n)=0$ | Exact identity for every $N\ge1$ and $N<n\le2N$ | CME Compendium, §4 |
| V1 | Count of 621 active and 403 zero foci | Exact for 1024→2048 | Included verifier |
| R4 | Projection balance and reflection | Identity in Hilbert space | CME Compendium, §3 |
| R5 | Three-window decomposition | Exact inequality | Technical appendix, §5 |
| R6 | Periodic energy formula $Q_I(c)$ | Finite identity | Three-Window Bridge, §2 |
| O1 | Functional recovery through m=2048 | Reproduced in double precision | CME Compendium, §6; laboratory S–RA–01 |
| T1 | Transfer under a uniform bound | Implication theorem with explicit conditions | Technical appendix, §5 |
| RA–01 | Certifiable recovery by seeds and summed gains | Sufficient implication for seeds; equivalence only for optimal gains | RA–01 appendix, §§2–4; CR-6, Theorem 4 |
| S1 | Möbius seed by dyadic blocks | 51–100% of optimal gain, $j\le10$; reproducible measurement | Laboratory S–RA–01 |

## 7. Version Integration

This document joins the repository as an additional synthesis while preserving the historical manuscripts. The ROSI, CME-002, spheres, and O40/O58 normalizer laboratories remain indexed at their own paths. Laboratories A–G–01 (harmonics and granularity) and S–RA–01 (Möbius seed) are included under `laboratorios/` in this package. The functional and arithmetic appendices serve as proof sources, reproducible instances, and provenance. The integration `README.md` contains a proposed entry for the main index; `integracion/INSTRUCCIONES_ADMIN.md` records the publication sequence.

## 8. Provenance and Comparative Bibliography

Included appendix: `anexos/RA-01_recuperacion_acumulada/documentos/PROPOSICION_RECUPERACION_ACUMULADA_2026-11-21.md`.

Included laboratories: `laboratorios/2026-11-21_armonicos_granularidad/` and `laboratorios/2026-11-21_RA01_semilla_mobius/`.

Source documents archived in the package:

- `fuentes/COMPENDIO_RIEMANN_CME_2026-11-21.md` — reclosure by foci, transforms, projections, and the m=2048 record.
- `fuentes/COMPENDIO_RIEMANN_ECONOMIA_2026-11-21.md` — synthesis by query economy.
- `fuentes/ANEXO_TECNICO_ES.md` — contracts across scales and the three-window decomposition.
- `fuentes/PUENTE_GRANULARIDAD_TRES_VENTANAS_2026-11-21.md` — periodic energy and the fine window.
- `fuentes/ANEXO_CR6_RH_CONSULTA_UNITARIA_Y_RESIDUO_2026-11-21.md` — unit query, exact residual balance, and Theorem 4 on accumulated relative gain.
- `fuentes/GRANULARIDAD_RESTO_Y_CIERRE_RH.md` — granularity laws and proofs for finite closures.

Documentary antecedents: O40 (October 20), O58 (October 21), MF-86, CR-6, CME-002, R–01/R–02, R–03 v0.4 (proposed in PR #9), R–RH–01 (November 1 manuscript; source collated in PR #9), ROSI, and ROS–1 Lite. The working versions are linked from their respective pull requests; their dates provide documentary provenance.

Classical references: L. Báez-Duarte (2002), *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, https://arxiv.org/abs/math/0202141; L. Báez-Duarte, M. Balazard, B. Landreau, and É. Saias (2000), and J.-F. Burnol (2002), lower bounds for approximation error; V. I. Vasyunin (1995), inner-product formula.

---

## Current References and Review Provenance

The copy `fuentes/COMPENDIO_RIEMANN_CME_2026-11-21.md` records an **earlier state** of the text revised in [PR #11 — CME–RH](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/11) (draft as of November 21, 2026). The R–03 v0.4 edition belongs to [PR #9 — R–03 and Gram](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/9), also in draft; it is not presented as already merged into `main`. The files under `fuentes/` are retained as complete antecedents. Integration should link the current state of each pull request and compare its changes before merging.

**Le Matt Ansatz Di Ego**  
Endless Monkey Project / Relational Geometry Program
