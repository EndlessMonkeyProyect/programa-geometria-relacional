# R–03 · Spectral inheritance, normalization, and zero locations

**Continuation of R–01 / R–02 · Examination document, v0.3 · November 18, 2026**  
**Endless Monkey Project**  
Relational Geometry Program  
**Le Matt Ansatz Di Ego**

## Abstract

The Mellin transform of the sieve discrepancy preserves the zeros of the Riemann zeta function under every reference made of finitely many primes. The preservation is exact and reversible inside the open critical strip. This examination studies four consequences: normalization to a common reference, the stability of that recovery, the inversion cost at the pivot $s=\tfrac12$ when the reference includes all primes up to $X$, and the separation between symmetry and localization through two control models.

At the pivot, the inversion cost has an exact normalization that is equivalent to the Riemann hypothesis (Akatsuka, 2024). Written with the sieve discrepancy, the Riemann hypothesis becomes a lower bound for the complete discrepancy at the pivot. The laboratory follows that quantity up to $X=10^8$. The Riemann hypothesis remains open.

**Keywords:** sieve; inheritance; Mellin transform; zeta zeros; partial Euler product; Davenport–Heilbronn function; normalization.

## 1. Reference, discrepancy, and transform

Let $S$ be a finite set of primes, and define

$$
M_S=\prod_{p\in S}p,\qquad
\delta_S=\prod_{p\in S}\left(1-p^{-1}\right),\qquad
A_S(x)=\left|\lbrace 1\le n\le x:\ \gcd(n,M_S)=1\rbrace\right|,
$$

$$
E_S(x)=A_S(x)-x\,\delta_S,
\qquad
F_S(s)=\int_0^\infty E_S(x)\,x^{-s-1}\,dx.
$$

Proposition 1 in the [published formalization](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md) gives, for $0<\mathrm{Re}(s)<1$,

$$
F_S(s)=\frac{\zeta(s)}{s}\,P_S(s),\qquad
P_S(s)=\prod_{p\in S}\left(1-p^{-s}\right).\tag{R03.1}
$$

The inheritance operator $T_pf(x)=f(x)-f(x/p)$ corresponds under the Mellin transform to multiplication by $1-p^{-s}$.

## 2. Proposition 1 — Exact spectral inheritance

**For every finite $S$, $F_S$ and $\zeta$ have exactly the same zeros, with identical multiplicities, in $0<\mathrm{Re}(s)<1$.**

*Proof.* Write $s=\sigma+it$ with $0<\sigma<1$. Each factor satisfies $|p^{-s}|=p^{-\sigma}<1$, so $P_S(s)$ has no zeros in the strip. The factor $1/s$ has no zeros or poles there either. Equation (R03.1) expresses $F_S$ as $\zeta$ times a holomorphic nowhere-vanishing function, and local factorization preserves the orders of the zeros. $\square$

**Reading:** a finite reference preserves the zeros and supplies another way of observing them, at the same locations.

## 3. Proposition 2 — Normalization and a common reference

Define

$$
N_S(s)=\frac{F_S(s)}{P_S(s)}.\tag{R03.2}
$$

For every finite $S$ and $0<\mathrm{Re}(s)<1$,

$$
\boxed{N_S(s)=\frac{\zeta(s)}{s}.}\tag{R03.3}
$$

*Proof.* Divide (R03.1) by the nonzero factor $P_S(s)$. $\square$

The normalized reference is the same for every finite prime set. It is an exact invariance: evaluating $N_S$ still requires $F_S$ and $P_S$, or another representation with verified cost.

## 4. Proposition 3 — Inversion cost and stability

Fix $\sigma_0$ with $0<\sigma_0<1$. For $\mathrm{Re}(s)\ge\sigma_0$,

$$
\prod_{p\in S}\left(1-p^{-\sigma_0}\right)
\le |P_S(s)|
\le\prod_{p\in S}\left(1+p^{-\sigma_0}\right).\tag{R03.4}
$$

If a measurement $\widetilde F_S$ of $F_S$ has absolute error $\varepsilon(s)$, then

$$
\left|\frac{\widetilde F_S(s)}{P_S(s)}-\frac{\zeta(s)}{s}\right|
=\frac{|\varepsilon(s)|}{|P_S(s)|}
\le |\varepsilon(s)|\prod_{p\in S}\left(1-p^{-\sigma_0}\right)^{-1}.\tag{R03.5}
$$

*Proof.* Apply $1-|z|\le|1-z|\le1+|z|$ to each $z=p^{-s}$, multiply, and divide by $P_S(s)$. $\square$

**Asymptotic limitation.** For any $0<\sigma_0<1$, taking all primes up to $p_k$ gives $P_{S_k}(\sigma_0)=\prod_{j\le k}(1-p_j^{-\sigma_0})\to0$, since $\sum_p p^{-\sigma_0}$ diverges (it dominates $\sum_p 1/p$). Inversion can amplify measurement errors without a uniform bound as the reference grows.

This proposition measures one component of reconstruction cost. The next section evaluates it at the pivot, where that cost has an exact form.

## 5. Proposition 4 — Inversion cost at the pivot

Let $S_X$ be the set of primes $p\le X$ and $\vartheta(X)=\sum_{p\le X}\log p$. At the pivot $s=\tfrac12$ the inheritance factor is real and positive,

$$
P_{S_X}\!\left(\tfrac12\right)=\prod_{p\le X}\left(1-p^{-1/2}\right),
$$

and its inverse grows without bound (§4). Akatsuka measures that growth exactly. Let

$$
E_1(X)=\frac{P_{S_X}\!\left(\tfrac12\right)^{-1}}{\exp\!\left(\mathrm{li}\big(\vartheta(X)^{1/2}\big)\right)}.\tag{R03.11}
$$

**Theorem (Akatsuka, 2024, Theorem 3).** The following are equivalent:

1. the Riemann hypothesis;
2. $E_1(X)$ is bounded for $X\ge3$;
3. $E_1(X)\to-\sqrt2\,\zeta\!\left(\tfrac12\right)\approx 2.0653$ as $X\to\infty$.

*Known.*

**Proposition 4 (sieve reading).** For every $X\ge3$,

$$
\boxed{F_{S_X}\!\left(\tfrac12\right)\,e^{\mathrm{li}\left(\vartheta(X)^{1/2}\right)}=\frac{2\,\zeta\!\left(\tfrac12\right)}{E_1(X)}.}\tag{R03.12}
$$

Consequently, the Riemann hypothesis is equivalent to each of the following:

- $\left|F_{S_X}(\tfrac12)\right|\,e^{\mathrm{li}(\vartheta(X)^{1/2})}$ is bounded below by a positive constant for $X\ge3$;
- $F_{S_X}(\tfrac12)\,e^{\mathrm{li}(\vartheta(X)^{1/2})}\to-\sqrt2$.

*Proof.* The point $s=\tfrac12$ lies in the open strip, so (R03.1) gives $F_{S_X}(\tfrac12)=2\,\zeta(\tfrac12)\,P_{S_X}(\tfrac12)$. By (R03.11), $P_{S_X}(\tfrac12)=1/\big(E_1(X)\,e^{\mathrm{li}(\vartheta(X)^{1/2})}\big)$, which gives (R03.12). Since $\zeta(\tfrac12)\approx-1.4604$ is nonzero and $E_1(X)>0$, an upper bound for $E_1$ is equivalent to the lower bound in the first statement, and the limit of $E_1$ gives the limit $2\zeta(\tfrac12)/(-\sqrt2\,\zeta(\tfrac12))=-\sqrt2$. $\square$

**Reading.** $F_{S_X}(\tfrac12)$ is the sieve discrepancy with all primes up to $X$, integrated over all scales with the pivot weight $x^{-3/2}$. Proposition 4 says that this total discrepancy decays like $e^{-\mathrm{li}(\sqrt{\vartheta(X)})}$, with constant $-\sqrt2$, exactly when all zeros lie on the line. By the same theorem, a zero with real part greater than $\tfrac12$ makes $E_1$ unbounded.

**Laboratory.** *Verified* with `verificacion_R03.py`:

| $X$ | $P_{S_X}(\tfrac12)^{-1}$ | $E_1(X)$ | $F_{S_X}(\tfrac12)\,e^{\mathrm{li}}$ |
|:-:|:-:|:-:|:-:|
| $10^2$ | $e^{6.95}$ | $3.1875$ | $-0.9163$ |
| $10^4$ | $e^{30.91}$ | $2.4439$ | $-1.1951$ |
| $10^6$ | $e^{178.32}$ | $2.2643$ | $-1.2899$ |
| $10^7$ | $e^{463.67}$ | $2.2229$ | $-1.3139$ |
| $10^8$ | $e^{1246.86}$ | $2.1945$ | $-1.3309$ |
| limit under RH | — | $2.0653$ | $-1.4142$ |

The inverse factor grows to $e^{1247}$, while the normalized quantity stays bounded and slowly approaches its limit. This is an observation compatible with the Riemann hypothesis in that range; the table does not prove the bound.

## 6. Proposition 5 — Symmetry and localization: two controls

### 6.1 Minimal control

Let $a=\tfrac15+i$, $z=s-\tfrac12$, and

$$
H(s)=\left(z^2-a^2\right)\left(z^2-\overline a^{\,2}\right).\tag{R03.6}
$$

It satisfies $H(1-s)=H(s)$ and $H(\overline s)=\overline{H(s)}$, and its four zeros are $\tfrac{3}{10}\pm i$ and $\tfrac{7}{10}\pm i$. For each finite $S$, the family $H_S=H\,P_S$ keeps those zeros inside the strip and keeps conjugation symmetry; reflection $s\mapsto1-s$ is lost in general, because $P_S(1-s)\neq P_S(s)$. The symmetrized filter

$$
\boxed{\widehat H_S(s)=H(s)\,P_S(s)\,P_S(1-s)}\tag{R03.8}
$$

keeps both symmetries, and inside $0<\mathrm{Re}(s)<1$ its only zeros are the four zeros of $H$, with the same multiplicities.

*Proof.* The map $s\mapsto1-s$ sends $z\mapsto-z$, and $H$ depends on $z^2$ with real coefficients. The zeros satisfy $z=\pm a$ or $z=\pm\overline a$, with real parts $\tfrac12\pm\tfrac15$. In the strip, $P_S(s)$ and $P_S(1-s)$ are holomorphic and nonvanishing, and their product is invariant under $s\mapsto1-s$ and respects conjugation. $\square$

### 6.2 Standard control: Davenport–Heilbronn

Let $\tau=\dfrac{\sqrt{10-2\sqrt5}-2}{\sqrt5-1}\approx0.2841$, and let $a(n)$ be periodic with period $5$, with $a(1)=1$, $a(2)=\tau$, $a(3)=-\tau$, $a(4)=-1$, $a(5)=0$. The Davenport–Heilbronn function (also called Titchmarsh's counterexample) is

$$
f(s)=\sum_{n\ge1}\frac{a(n)}{n^s}=5^{-s}\sum_{j=1}^{4}a(j)\,\zeta\!\left(s,\tfrac{j}{5}\right),
\qquad
\Lambda(s)=\left(\frac{5}{\pi}\right)^{(s+1)/2}\,\Gamma\!\left(\frac{s+1}{2}\right)f(s).\tag{R03.13}
$$

It satisfies the functional equation $\Lambda(s)=\Lambda(1-s)$, of the type of odd Dirichlet $L$-functions modulo $5$; since its coefficients are real, $\Lambda$ is real on the line. It has zeros on the line, the first at $\tfrac12+5.0941598446\,i$, and zeros off it, the first at $0.8085171825+85.6993484854\,i$ (Spira, 1994), with its mirror at $0.1914828175+85.6993484854\,i$. Its coefficients are not multiplicative: $a(2)\,a(3)=-\tau^2\approx-0.0807$, while $a(6)=a(1)=1$. Hence $f$ has no Euler product. *Known* (Davenport and Heilbronn, 1936); *verified* with `verificacion_R03.py`.

**Conclusion of the controls.** The minimal control shows that both symmetries and finite filters leave the location of the zeros of a holomorphic function free. The standard control shows the same for a Dirichlet series with a functional equation of the type of $\zeta$ and with zeros on the line. Among those ingredients, what separates $\zeta$ from $f$ is the Euler product: in the program, inheritance over **all** primes. Proposition 4 is precisely a statement about complete inheritance at the pivot.

## 7. Radius, phase, and supplementary datum

For a hypothetical zero $\rho=\beta+i\gamma$, the inheritance multiplier is

$$
\lambda_p(\rho)=1-p^{-\rho},\qquad
r_p(\rho)=\left|p^{-\rho}\right|=p^{-\beta}.\tag{R03.9}
$$

The magnitude of the full multiplier also depends on phase:

$$
\left|\lambda_p(\rho)\right|^2
=1+p^{-2\beta}-2p^{-\beta}\cos(\gamma\log p).\tag{R03.10}
$$

The radius $r_p$ and the modulus $|\lambda_p|$ are different quantities. For any fixed prime $p$, the statement “$r_p(\rho)=p^{-1/2}$ for every nontrivial zero $\rho$” is equivalent to $\mathrm{Re}(\rho)=\tfrac12$ for all of them: it is a restatement of the Riemann hypothesis.

The phrase “one number per zero” refers to the number of **real parameters needed to describe the symmetric orbit**: on the line the height $\gamma$ suffices; off the line one also needs $\beta$. It is a count of continuous parameters; its relation to a count of bits or to a computational cost remains to be established.

## 8. The mathematical obligation, made precise

Version 0.2 asked for a functional $Q$, built from the discrepancies $E_S$, that excludes off-line modes. Proposition 4 gives an exact form of that functional: the complete discrepancy at the pivot, normalized by $e^{\mathrm{li}(\sqrt{\vartheta(X)})}$. The obligation becomes:

> Prove, without assuming the Riemann hypothesis, a constant $c>0$ such that $\left|F_{S_X}(\tfrac12)\right|\,e^{\mathrm{li}(\vartheta(X)^{1/2})}\ge c$ for every $X\ge3$.

By Proposition 4 this statement is equivalent to the Riemann hypothesis: the restatement places the problem on the program's own object, with the same difficulty. In terms of primes, it asks to control $\sum_{p\le X}-\log(1-p^{-1/2})$ against $\mathrm{li}(\vartheta(X)^{1/2})$ with an error bounded above.

The period energy of R–01/R–02,

$$
\langle E_k^2\rangle=\frac{2^k\delta_k}{12},
\qquad
\langle E_k(x)\,E_k(x/p)\rangle=\frac1p\,\langle E_k^2\rangle,
$$

is an average over complete periods, whereas Proposition 4 integrates the discrepancy over all scales with the pivot weight. Relating the two is a **laboratory candidate**.

### Verification protocol

1. Integrate $E_S(x)$ independently over unit intervals, bound the tail, and compare with (R03.1); compute the leading tail term and subtract it.
2. Check the nonzero factor at known zeros; this check is illustrative.
3. Check the symmetries and zeros of $H$ and $\widehat H_S$, and the loss of reflection for $H\,P_S$.
4. Check the Davenport–Heilbronn functional equation, its zeros on and off the line, and the non-multiplicativity of its coefficients.
5. Measure $|P_S(\sigma)|^{-1}$ as $S$ grows, and $E_1(X)$ at the pivot up to $X=10^8$.
6. Keep symbolic proof, numerical control, and open problem separate.

### Independent integration results

The script computes $A_S(n)$ directly from coprimality, integrates the piecewise-linear $E_S(x)=A_S(n)-\delta_S x$ exactly on each unit interval (in floating point), and bounds the tail by periodicity and zero mean. The cases are $S=\lbrace2\rbrace$, $\lbrace2,3\rbrace$, and $\lbrace2,3,5\rbrace$ at $s=0.7$ and $s=0.7+2.4i$, with cutoff $N=240\,000$, a multiple of the three periods.

The difference from the Mellin expression is exactly the leading tail term $\langle G\rangle N^{-s-1}$, where $\langle G\rangle$ is the period mean of $G(y)=\int_0^y E_S$; this is why the difference has the same modulus at both values of $s$ ($5.95\cdot10^{-11}$, $1.19\cdot10^{-10}$, and $4.76\cdot10^{-10}$). The script computes $\langle G\rangle$ in rational arithmetic and subtracts it: the remaining difference is at most $9\cdot10^{-15}$ in all six cases, below the analytic second-order remainder bound plus a $10^{-13}$ allowance for rounding. The check is independent of computing $F_S$ from the right-hand side of (R03.1) and accompanies the proof of the identity.

## 9. Results register

| Statement | Status |
|:--|:--|
| $F_S$ and $\zeta$ have the same zeros and multiplicities for finite $S$ | **Proved**, Mellin corollary |
| Normalized recovery $F_S/P_S=\zeta/s$ | **Proved** |
| Stability bounds and loss of uniformity as $S$ grows | **Proved** |
| RH is equivalent to $E_1$ bounded, and to $E_1\to-\sqrt2\,\zeta(\tfrac12)$ | **Known** (Akatsuka, 2024, Theorem 3) |
| RH is equivalent to the lower bound for the complete discrepancy at the pivot, with limit $-\sqrt2$ | **Proved** (Proposition 4) |
| $E_1(X)$ decreases from $3.19$ to $2.19$ between $X=10^2$ and $10^8$ | **Verified**; compatible with RH in that range |
| Both symmetries and finite filters leave zero locations free | **Proved** (minimal control) |
| Dirichlet series with functional equation and off-line zeros, without Euler product | **Known** (Davenport–Heilbronn; Spira); **verified** |
| Independent Mellin integration; the difference is the leading tail term | **Verified** |
| All zeros of $\zeta$ on the line $\mathrm{Re}(s)=\tfrac12$ | **Open**, Riemann hypothesis |
| Lower bound of Proposition 4 without assuming RH | **Open**, equivalent to RH |
| A proved reduction in the total cost of recognizing the zeros | **Open** |

## References and provenance

- [R–01/R–02, *Relational scales of the sieve*, published Spanish edition of Nov. 17, 2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md), §3, Proposition 1; §5, Proposition 2; §7, explicit formula.
- [*One number per zero*, published Spanish reflection](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/REFLEXION_UN_NUMERO_POR_CERO_ES.md), §§4–8 and 11–13: radius, reflection, and the supplementary datum.
- H. Akatsuka (2024). *Maximal order for divisor functions and zeros of the Riemann zeta-function.* [arXiv:2411.19259](https://arxiv.org/abs/2411.19259), Theorem 3.
- H. Akatsuka (2017). *The Euler product for the Riemann zeta-function in the critical strip.* Kodai Math. J. 40, 79–101.
- H. Davenport and H. Heilbronn (1936). *On the zeros of certain Dirichlet series.* J. London Math. Soc. 11.
- R. Spira (1994). *Some zeros of the Titchmarsh counterexample.* Math. Comp. 63, 747–748.
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, §2.1, for the classical Mellin identity.
- H. Davenport, *Multiplicative Number Theory*, for properties of the zeta function and Euler products.

**Public signature:** Le Matt Ansatz Di Ego.

**Scope note.** R–03 makes explicit and tests the mechanisms of the preceding publication, and writes a known equivalent of the Riemann hypothesis with its objects. The identities and theorems cited are classical or belong to their authors; the Riemann hypothesis remains open.
