# R–03 · Spectral inheritance, normalization, and zero locations

**Continuation of R–01 / R–02 · Examination document, v0.2 · November 18, 2026**  
**Endless Monkey Project**  
Relational Geometry Program  
**Le Matt Ansatz Di Ego**

## Abstract

The Mellin transform of sieve discrepancy inherits the zeros of the Riemann zeta function under every reference involving finitely many primes. This preservation is exact and reversible inside the open critical strip. Three consequences are examined: normalization to a common reference, the quantitative stability of this recovery, and the inability of finite zero-preserving operations by themselves to force the zeros onto `Re(s)=1/2`. A control counterexample separates symmetry from localization. The Riemann hypothesis remains open.

**Keywords:** sieve; inheritance; Mellin transform; zeta zeros; normalization; discrepancy; information economy.

## 1. Reference, discrepancy, and transform

Let `S` be a finite set of primes, and define

\[
M_S=\prod_{p\in S}p,\qquad
\delta_S=\prod_{p\in S}(1-p^{-1}),\qquad
A_S(x)=\#\{1\le n\le x:\gcd(n,M_S)=1\},
\]

\[
E_S(x)=A_S(x)-x\delta_S,
\quad
F_S(s)=\int_0^\infty E_S(x)x^{-s-1}\,dx.
\]

Proposition 1 in the [published formalization](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md) gives, for `0<Re(s)<1`,

\[
F_S(s)=\frac{\zeta(s)}s P_S(s),\qquad
P_S(s)=\prod_{p\in S}(1-p^{-s}).\tag{R03.1}
\]

The inheritance operator `T_p f(x)=f(x)-f(x/p)` corresponds under the Mellin transform to multiplication by `1-p^{-s}`.

## 2. Proposition 1 — Exact spectral inheritance

**For every finite S, F_S and ζ have exactly the same zeros, with identical multiplicities, in 0<Re(s)<1.**

*Proof.* Write `s=σ+it` with `0<σ<1`. Each factor satisfies `|p^{-s}|=p^{-σ}<1`; thus `P_S(s)` has no zeros in the strip. The factor `1/s` also has no zeros or poles there. Equation (R03.1) therefore expresses `F_S` as `ζ` multiplied by a holomorphic nowhere-zero function. Local holomorphic factorization preserves zeros and their orders. □

**Interpretation:** a finite reference preserves the zeros and supplies a different way of observing them, without changing their locations.

## 3. Proposition 2 — Normalization and a common reference

Define

\[
N_S(s)=\frac{F_S(s)}{P_S(s)}.\tag{R03.2}
\]

For every finite `S` and `0<Re(s)<1`,

\[
\boxed{N_S(s)=\frac{\zeta(s)}s.}\tag{R03.3}
\]

*Proof.* Divide (R03.1) by the nonzero factor `P_S(s)`. □

The normalized reference is the same for every finite prime set. This is an exact invariance, **not** a demonstrated computational compression: evaluating `N_S` still requires knowledge of `F_S` and `P_S`, or some other representation with verified cost.

## 4. Proposition 3 — Inversion cost and stability

Fix `σ₀` with `0<σ₀<1`. For `Re(s)≥σ₀`,

\[
\prod_{p\in S}(1-p^{-\sigma_0})
\le |P_S(s)|
\le\prod_{p\in S}(1+p^{-\sigma_0}).\tag{R03.4}
\]

If a measurement $\widetilde F_S$ of $F_S$ has absolute error $\varepsilon(s)$, then

\[
\left|\frac{\widetilde F_S(s)}{P_S(s)}-\frac{\zeta(s)}s\right|
=\frac{|\varepsilon(s)|}{|P_S(s)|}
\le |\varepsilon(s)|\prod_{p\in S}(1-p^{-\sigma_0})^{-1}.\tag{R03.5}
\]

*Proof.* Apply `1−|z|≤|1−z|≤1+|z|` to `z=p^{-s}`, multiply the inequalities, and divide by `P_S(s)`. □

**Asymptotic limitation.** For any fixed `0<σ₀<1`, taking the first `k` primes gives $P_{S_k}(\sigma_0)=\prod_{j\le k}(1-p_j^{-\sigma_0})\to0$, since $\sum_p p^{-\sigma_0}$ diverges (it dominates $\sum_p 1/p$). Inversion can therefore amplify measurement errors without a uniform bound as the reference grows.

This result measures **one component of reconstruction cost**; it does not alone determine total transform-evaluation cost or zero locations.

## 5. Proposition 4 — Preservation and reflection do not determine the line

Set `a=1/5+i`, `z=s−1/2`, and consider

\[
H(s)=(z^2-a^2)(z^2-\overline a^{\,2}).\tag{R03.6}
\]

It obeys the symmetries

\[
H(1-s)=H(s),\qquad
H(\overline s)=\overline{H(s)}.\tag{R03.7}
\]

Its four zeros are

\[
\boxed{\,3/10\pm i,\qquad 7/10\pm i\,}.\tag{R03.8}
\]

For any finite prime set `S`, the family `H_S(s)=H(s)P_S(s)` retains the four zeros in the open strip. **This family does not, in general, retain reflection symmetry under `s↦1−s`** because typically `P_S(1−s)≠P_S(s)`. It retains conjugation symmetry.

To retain **both symmetries at every finite reference**, use the symmetrized filter:

\[
\boxed{\widehat H_S(s)=H(s)P_S(s)P_S(1-s).}\tag{R03.8a}
\]

For every `s`,

\[
\widehat H_S(1-s)=\widehat H_S(s),\qquad
\widehat H_S(\overline s)=\overline{\widehat H_S(s)}.\tag{R03.8b}
\]

In `0<Re(s)<1`, neither `P_S(s)` nor `P_S(1−s)` vanishes. Hence the **only zeros inside the open strip** of `\widehat H_S` are the four zeros of `H`, with the same multiplicities.

*Proof.* The reflection `s↦1−s` maps `z↦−z`; `H` depends only on `z²`. Conjugation symmetry follows from the paired conjugate coefficients. Its zeros satisfy `z=±a` or `z=±\bar a`, giving real parts `1/2±1/5`. Multiplication by `P_S(s)` or by `P_S(s)P_S(1−s)` adds no zeros in the strip, because those factors are nonvanishing there. The symmetrized product is invariant under `s↦1−s`, and its factors also respect conjugation. □

**Logical conclusion of the control.** Reflection symmetry, conjugation symmetry, and multiplication by finite filters are **not sufficient on their own** to force every zero of an arbitrary holomorphic function onto a fixed line. The example neither replaces the additional analytic properties of `ζ` nor supplies a counterexample to RH; it only tests the implications of the mechanisms formalized here.

## 6. Radius, phase, and supplementary data

For a hypothetical zero `ρ=β+iτ`, the inheritance multiplier is

\[
\lambda_p(\rho)=1-p^{-\rho},\qquad
r_p(\rho)=|p^{-\rho}|=p^{-\beta}.\tag{R03.9}
\]

The magnitude of the **full multiplier** also depends on phase:

\[
|\lambda_p(\rho)|^2
=1+p^{-2\beta}-2p^{-\beta}\cos(\tau\log p).\tag{R03.10}
\]

The radius `r_p` and `|λ_p|` are different quantities. For any single fixed prime `p>1`, the statement

\[
\forall\rho:\ \ r_p(\rho)=p^{-1/2}
\]

is equivalent to `Re(ρ)=1/2` for every nontrivial zero. **It restates the Riemann hypothesis and does not follow from (R03.9).**

The phrase “one number per zero” refers to the number of **real parameters required to describe a symmetry orbit**: the height `τ` suffices on the line; off the line one also needs `β`. Counting continuous parameters is not automatically counting bits or proving a smaller computational cost.

## 7. The next mathematical obligation

A new restriction on zero locations requires a verifiable condition `Q`, beyond (R03.1), that excludes off-line modes. A falsifiable formulation is:

> Find a functional `Q`, defined from the sieve discrepancies `E_S` and their relationships on incomplete windows, such that (i) it satisfies a demonstrable identity or inequality not assuming RH; (ii) it controls the spectral component after removal of the structural term at closure; and (iii) it implies a pointwise bound sufficient for `π(x)−li(x)=O(√x log x)`, or yields a counterexample to the proposed criterion.

The complete-period energy identity from R–01/R–02,

\[
\langle E_k^2\rangle=\frac{2^k\delta_k}{12},
\qquad
\langle E_k(x)E_k(x/p)\rangle=\frac1p\langle E_k^2\rangle,
\]

does **not yet** satisfy (ii): these are averages over complete periods, whereas sieve closure concerns windows much shorter than `M_k`. It remains a **candidate for testing**, not a proof of a stronger bound.

### Verification protocol

1. Integrate the discrepancy `E_S(x)` **independently** across unit intervals with an explicit tail bound, compare with (R03.1), and check normalized recovery (R03.3).
2. Check the nonzero factor at known zeros; this cannot certify all zeros.
3. Test `H` symmetry, exhibit reflection failure for `H_S=H P_S`, and verify both symmetries and four zeros of `\widehat H_S=H P_S(s)P_S(1−s)`.
4. Measure `|P_S(σ)|^{-1}` as `S` grows.
5. Keep symbolic proofs, finite computations, and open claims separate.

### Independent integration results

The `verificacion_R03.py` script computes `A_S(n)` directly from coprimality, integrates the piecewise-linear function `E_S(x)=A_S(n)−δ_S x` analytically on each unit interval (using floating-point arithmetic), and controls the remaining tail using periodicity and zero mean. The six cases use `S={2}`, `{2,3}`, `{2,3,5}` at `s=0.7` and `s=0.7+2.4i`, with cutoff `N=240000`, divisible by all three periods. The largest observed mismatch with the Mellin expression was under `4.8×10^−10`; the largest analytic tail bound was below `1.5×10^−7`. An additional `2×10^−8` allowance covers floating-point rounding, without claiming a rigorous machine-arithmetic error enclosure. This is computationally independent of constructing `F_S` from the right-hand side of (R03.1), but does not replace the proof of the identity.

## 8. Results register

| Statement | Status |
|:--|:--|
| `F_S` and `ζ` have the same zeros and multiplicities for finite S | **Proved**, Mellin corollary |
| Normalized recovery `F_S/P_S=ζ/s` | **Proved** |
| Stability bounds and loss of uniformity as S grows | **Proved** |
| Symmetry plus finite inheritance alone cannot localize zeros | **Proved by symmetrized control model** |
| Independent Mellin integration with tail bound | **Numerical verification**, not a proof of RH |
| All zeros of `ζ` lie on `Re(s)=1/2` | **Open**, Riemann hypothesis |
| A reduction in total cost for recognizing those zeros | **Open** |

## References and provenance

- [R–01/R–02, *Relational scales of the sieve*, published Spanish edition of Nov. 17, 2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md), §3, Proposition 1; §5, Proposition 2; §7, explicit formula.
- [*One number per zero*, published Spanish reflection](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/REFLEXION_UN_NUMERO_POR_CERO_ES.md), §§4–8, 11–13: radius, reflection, and the supplementary datum interpretation.
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, §2.1, for the classical Mellin identity.
- H. Davenport, *Multiplicative Number Theory*, for properties of the zeta function and Euler products.

**Public signature:** Le Matt Ansatz Di Ego.

**Scope note.** R–03 makes explicit and tests mechanisms from the preceding publication. It claims neither a proof of RH nor originality for the classical identities.
