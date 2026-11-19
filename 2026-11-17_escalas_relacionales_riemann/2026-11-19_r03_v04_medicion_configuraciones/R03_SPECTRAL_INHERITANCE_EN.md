# R–03 · Spectral inheritance, normalization, and zero locations

**Continuation of R–01 / R–02 · Examination document, v0.4 · November 18, 2026**<br>
**Endless Monkey Project**<br>
Relational Geometry Program<br>
**Le Matt Ansatz Di Ego**

## Abstract

The Mellin transform of the sieve discrepancy preserves the zeros of the Riemann zeta function under every reference made of finitely many primes. The preservation is exact and reversible inside the open critical strip. This examination studies four consequences: normalization to a common reference, the stability of that recovery, the absolute-error amplification factor under normalization at the pivot $s=\tfrac12$ when the reference includes all primes up to $X$, and the separation between symmetry and localization through three control models.

At the pivot, the inversion factor admits an exact normalization that is equivalent to the Riemann hypothesis (Akatsuka, 2024). Written with the sieve discrepancy, the Riemann hypothesis becomes a lower bound for the complete discrepancy at the pivot. The laboratory follows that quantity up to $X=10^8$. The Riemann hypothesis remains open.

**Keywords:** sieve; inheritance; Mellin transform; zeta zeros; partial Euler product; Davenport–Heilbronn function; normalization.


## Provenance and scope

| Statement | Origin | Status in this edition |
|:--|:--|:--|
| Sieve recurrence and Mellin identity (R03.1) | Legendre, inclusion–exclusion, classical Mellin identity | Known, reproduced |
| Same zeros and multiplicities for finite $S$ | Immediate consequence of (R03.1) | Proved corollary, not new localization |
| $F_S/P_S=\zeta/s$ and amplification bounds | Finite-product algebra and triangle inequality | Proved corollaries; no complexity bound |
| Normalized product $E_1(X)$ and RH criterion | Akatsuka (2024), Theorem 3 | Known |
| Normalized discrepancy identity at $s=1/2$ | Exact substitution into Akatsuka | Proved restatement, not a new criterion |
| Symmetry controls | Elementary polynomial; Davenport–Heilbronn; shifted completed zeta product | Controls, not proofs of RH |
| Nyman–Beurling connection | Inclusion–exclusion, inversion $x\mapsto1/x$; classical criterion (Báez-Duarte) | Exact correspondence; density of restricted span remains open |
| Uniform lower bound for normalized discrepancy | Equivalent to RH by Akatsuka | Open |

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

**Terminological precision.** $E_S$ is a counting discrepancy, not energy. A modular reference distinguishes residue classes; granularity describes which differences are accessible under that reference. A subsequent quadratic measurement neither defines granularity nor postulates physical energy.

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

The normalized reference is the same for every finite prime set. It is an exact algebraic invariance, not a computational complexity bound: evaluating $N_S$ still requires $F_S$ and $P_S$, or another representation with verified cost.

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

This proposition measures an **absolute-error conditioning factor**, not runtime or memory complexity. The next section evaluates it at the pivot, where that cost has an exact form.

## 5. Proposition 4 — Normalizing the inversion factor at the pivot

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

## 6. Proposition 5 — Symmetry and localization: three controls

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

**Conclusion of the controls.** The minimal control shows that both symmetries and finite filters leave the location of the zeros of a holomorphic function free. The standard control shows the same for a Dirichlet series with a functional equation of the type of $\zeta$ and with zeros on the line. An Euler product is one difference between $\zeta$ and $f$; the stronger control in §6.3 shows why this difference alone still does not localize zeros. Proposition 4 adds a much more specific global condition.


### 6.3 Stronger control: an Euler product and symmetry without zero localization

One structural difference between the Davenport–Heilbronn function and $\zeta$ is an Euler product. **The mere existence of an Euler product, even together with reflection symmetry, does not force all zeros onto $\operatorname{Re}(s)=1/2$.**

For real $0<a<1/2$, let $\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ and define

$$
\boxed{\mathcal H_a(s)=\xi(s+a)\,\xi(s-a).}\tag{R03.14}
$$

The function $\mathcal H_a$ is entire, and $\mathcal H_a(1-s)=\mathcal H_a(s)$ as well as $\mathcal H_a(\overline{s})=\overline{\mathcal H_a(s)}$. Its arithmetic factor has a **genuine Euler product** when $\operatorname{Re}(s)>1+a$:

$$
\zeta(s+a)\zeta(s-a)=\prod_p(1-p^{-s-a})^{-1}(1-p^{-s+a})^{-1}.\tag{R03.15}
$$

If $\rho=1/2+i\gamma$ is a known zero of $\xi$, then $\mathcal H_a(\rho-a)=\mathcal H_a(\rho+a)=0$. With $a=1/5$ and the first zeta zero $\gamma\approx14.1347251417$, $\mathcal H_a$ has zeros at $0.3+i\gamma$ and $0.7+i\gamma$, and at their conjugates: **off the critical line**.

*Proof.* The functional equation interchanges the two factors when $s\mapsto1-s$, while conjugation preserves the completed zeta function. The two zeta factors have their stated Euler products in the common half-plane of absolute convergence. At $s=\rho-a$ the first completed zeta factor vanishes, and at $s=\rho+a$ the second vanishes. $\square$

**Scope:** this is a product of two *shifted* zeta functions with shifted gamma factors; it does not meet every axiom for a normalized primitive $L$-function (in particular the Ramanujan condition on local parameters). It defeats the general inference “symmetry + Euler product $\Rightarrow$ all zeros on the line,” **not** RH or a theorem about a narrower standard $L$-function class.

**Revised interpretation.** Euler products, reflection symmetry and finite-filter inheritance are distinct properties. None individually, nor the above unrestricted combination, forces zero localization. Akatsuka's criterion imposes a specific global arithmetic bound; proving it remains equivalent to RH.

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

**Scope of “radius.”** In (R03.9), $r_p$ denotes the modulus of $p^{-\rho}$ in the complex plane; it is not the relational accessibility radius used in the gravity or computation laboratories, nor an energy quantity.

The radius $r_p$ and the modulus $|\lambda_p|$ are different quantities. For any fixed prime $p$, the statement “$r_p(\rho)=p^{-1/2}$ for every nontrivial zero $\rho$” is equivalent to $\mathrm{Re}(\rho)=\tfrac12$ for all of them: it is a restatement of the Riemann hypothesis.

The phrase “one number per zero” refers to the number of **real parameters needed to describe the symmetric orbit**: on the line the height $\gamma$ suffices; off the line one also needs $\beta$. It is a count of continuous parameters; its relation to a count of bits or to a computational cost remains to be established.

## 8. The mathematical obligation, made precise

Version 0.2 asked for a functional $Q$, built from the discrepancies $E_S$, that excludes off-line modes. Proposition 4 gives an exact form of that functional: the complete discrepancy at the pivot, normalized by $e^{\mathrm{li}(\sqrt{\vartheta(X)})}$. The obligation becomes:

> Prove, without assuming the Riemann hypothesis, a constant $c>0$ such that $\left|F_{S_X}(\tfrac12)\right|\,e^{\mathrm{li}(\vartheta(X)^{1/2})}\ge c$ for every $X\ge3$.

By Proposition 4 this statement is equivalent to the Riemann hypothesis: the restatement places the problem on the program's own object, with the same difficulty. In terms of primes, it asks to control $\sum_{p\le X}-\log(1-p^{-1/2})$ against $\mathrm{li}(\vartheta(X)^{1/2})$ with an error bounded above.

The **quadratic dispersion over a full period** in R–01/R–02 —called “period energy” there by mathematical analogy—is

$$
\langle E_k^2\rangle=\frac{2^k\delta_k}{12},
\qquad
\langle E_k(x)\,E_k(x/p)\rangle=\frac1p\,\langle E_k^2\rangle.
$$

These are discrepancy dispersion and correlation measurements over complete periods; they define neither physical energy nor granularity. Granularity concerns distinctions accessible under a reference; a radius delimits an observational domain. Proposition 4 instead uses a Mellin transform at the pivot $s=1/2$, whose integrand carries the weight $x^{-3/2}$.

The **separate configuration measurement laboratory** uses

$$
G_{S,T}=\int_0^\infty\frac{E_S(x)E_T(x)}{x^2}\,dx
=\int_0^\infty h_S(t)h_T(t)\,dt,
\qquad h_S(t)=-E_S(1/t).
$$

The weight $x^{-2}$ comes from the substitution $t=1/x$; **it is not the pivot weight**, nor a physical energy law. See the accompanying `GRAM_BRIDGE_MEASUREMENT_EN.md` for provenance and verification.

### Verification protocol

1. Integrate $E_S(x)$ independently over unit intervals, bound the tail, and compare with (R03.1); compute the leading tail term and subtract it.
2. Check the nonzero factor at known zeros; this check is illustrative.
3. Check the symmetries and zeros of $H$ and $\widehat H_S$, and the loss of reflection for $H\,P_S$.
4. Check the Davenport–Heilbronn functional equation, its zeros on and off the line, and the non-multiplicativity of its coefficients.
5. Measure $|P_S(\sigma)|^{-1}$ as $S$ grows, and $E_1(X)$ at the pivot up to $X=10^8$.
6. Keep symbolic proof, numerical control, and open problem separate.

### Independent integration results

The script computes $A_S(n)$ directly from coprimality, integrates the piecewise-linear $E_S(x)=A_S(n)-\delta_S x$ exactly on each unit interval (in floating point), and bounds the tail by periodicity and zero mean. The cases are $S=\lbrace2\rbrace$, $\lbrace2,3\rbrace$, and $\lbrace2,3,5\rbrace$ at $s=0.7$ and $s=0.7+2.4i$, with cutoff $N=240\,000$, a multiple of the three periods.

The difference from the Mellin expression has leading tail term $\langle G\rangle N^{-s-1}$, where $\langle G\rangle$ is the period mean of $G(y)=\int_0^y E_S$; this is why its observed modulus is practically the same at the two values of $s$ ($5.95\cdot10^{-11}$, $1.19\cdot10^{-10}$, and $4.76\cdot10^{-10}$). The script computes $\langle G\rangle$ in rational arithmetic and subtracts it: the remaining difference is at most $9\cdot10^{-15}$ in all six cases, below the analytic second-order remainder bound plus a $10^{-13}$ allowance for rounding. The check is independent of computing $F_S$ from the right-hand side of (R03.1) and accompanies the proof of the identity.

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
| Stronger control: symmetry and Euler product alone do not suffice | **Proved** by shifted construction; not an RH counterexample |
| Exact Nyman–Beurling bridge with squarefree indices | **Proved**; RH-equivalent target follows from Báez-Duarte (2003) |
| Independent Mellin integration; leading asymptotic tail term | **Verified** |
| All zeros of $\zeta$ on the line $\mathrm{Re}(s)=\tfrac12$ | **Open**, Riemann hypothesis |
| Lower bound of Proposition 4 without assuming RH | **Open**, equivalent to RH |
| A proved reduction in the total cost of recognizing the zeros | **Open** |


## 10. Exact bridge to the functional criterion from November 1

The compared text of the earlier note *R–RH–01 — Primes, reflection, and closure* uses $f_n(t)=\{1/(nt)\}$ and the classical Nyman–Beurling/Báez-Duarte criterion, in which density of the full family is equivalent to RH. The sieve discrepancy becomes an **exact** linear combination of those functions after reference inversion.

**Proposition 6 (inversion bridge).** For any finite prime set $S$, including $S=\varnothing$, put $M_S=\prod_{p\in S}p$ and $h_S(t)=-E_S(1/t)$. Then

$$
\boxed{h_S(t)=\sum_{d\mid M_S}\mu(d)f_d(t).}\tag{R03.16}
$$

Consequently,

$$
\boxed{\|h_S\|_{L^2(0,\infty)}^2=\int_0^\infty\frac{|E_S(y)|^2}{y^2}\,dy.}\tag{R03.17}
$$

*Proof.* Inclusion–exclusion gives $A_S(y)=\sum_{d\mid M_S}\mu(d)\lfloor y/d\rfloor$ and $\delta_S=\sum_{d\mid M_S}\mu(d)/d$. Hence $E_S(y)=-\sum_{d\mid M_S}\mu(d)\{y/d\}$. Substitute $y=1/t$ to obtain (R03.16), and change variables in the $L^2$ norm to obtain (R03.17). Convergence follows from bounded $E_S$ at infinity and $E_S(y)=-y\delta_S$ near zero. $\square$

**Corollary 6.1 (exact scope of the signatures).** As $S$ runs through finite prime sets, the **algebraic** span of $h_S$ equals that of all $f_d$ with squarefree indices $d$. Boolean-lattice inversion gives

$$
f_{d_S}(t)=\sum_{T\subseteq S}(-1)^{|T|}h_T(t),\qquad d_S=\prod_{p\in S}p.\tag{R03.18}
$$

The full Nyman–Beurling family also contains indices with repeated prime factors, e.g. $f_4$. **Equality of the two Hilbert-space closures is not proved here.** Indeed, $f_{p^2}$ cannot be a **finite** linear combination of squarefree-indexed $f_d$: Mellin transformation would identify $p^{-2s}$ with a Dirichlet polynomial supported on distinct squarefree indices, contradicting linear independence of distinct exponentials.

**Corollary 6.2 (the functional criterion in sieve-discrepancy notation; known by reduction).** Let $\chi=\mathbf1_{(0,1]}$. Then

$$
\boxed{\mathrm{RH}\iff \chi\in\overline{\operatorname{span}\{h_S:S\subset\mathbb P\text{ finite}\}}^{L^2(0,\infty)}.}\tag{R03.19}
$$

*Proof.* Báez-Duarte (2002, second paper, Proposition 3.1, credited to M. Balazard) constructs, **assuming RH**, approximations to $\chi$ with coefficients proportional to $\mu(n)\exp[-c\log n/\log\log N]$ and $L^2$ error $O((\log\log N)^{-1/3})$. All nonzero terms have squarefree indices, and by Corollary 6.1 every finite such sum belongs to $\operatorname{span}\{h_S\}$. Conversely, this span is contained in the span of **all** $f_n$, and Báez-Duarte's Theorem 1.1 (2002/2003) implies RH if $\chi$ belongs to its closure. $\square$

This is **not a new original characterization**: it is a translation into sieve-discrepancy notation of an implication already accessible from the published Möbius-based approximants. Whether the **full closed subspaces** generated by squarefree versus all indices coincide is a separate question, unnecessary for this corollary and not proved here. No unconditional convergence or computational cost bound has been obtained.

**Contribution to the program:** the bridge connects sieve discrepancy, inverse reference, and the closure criterion previously used in R–RH–01. The obligation is now explicit: **prove without assuming RH that the distance of $\chi$ to this space tends to zero**. That step remains open.

## References and provenance

- [R–01/R–02, *Relational scales of the sieve*, published Spanish edition of Nov. 17, 2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md), §3, Proposition 1; §5, Proposition 2; §7, explicit formula.
- [*One number per zero*, published Spanish reflection](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/REFLEXION_UN_NUMERO_POR_CERO_ES.md), §§4–8 and 11–13: radius, reflection, and the supplementary datum.
- H. Akatsuka (2024). *Maximal order for divisor functions and zeros of the Riemann zeta-function.* [arXiv:2411.19259](https://arxiv.org/abs/2411.19259), Theorem 3.
- H. Akatsuka (2017). *The Euler product for the Riemann zeta-function in the critical strip.* Kodai Math. J. 40, 79–101.
- H. Davenport and H. Heilbronn (1936). *On the zeros of certain Dirichlet series.* J. London Math. Soc. 11.
- R. Spira (1994). *Some zeros of the Titchmarsh counterexample.* Math. Comp. 63, 747–748.
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, §2.1, for the classical Mellin identity.
- H. Davenport, *Multiplicative Number Theory*, for properties of the zeta function and Euler products.

- L. Báez-Duarte (2003), [*A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis*](https://arxiv.org/abs/math/0202141), Theorem 1.1 (closure criterion).
- L. Báez-Duarte (2002), [*A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis, 2*](https://arxiv.org/abs/math/0205003), M. Balazard's Proposition 3.1 (conditional weighted approximants and bound).
- [R–RH–01, *Primes, reflection, and closure* (Spanish source)](../../antecedentes/R_RH_01_Primos_Reflexion_y_Cierre_2026-11-01.md) (stated date: Nov. 1, 2026; supplied text compared; [provenance record, in Spanish](PROCEDENCIA_Y_LIMITES.md)).

**Public signature:** Le Matt Ansatz Di Ego.

**Scope note.** R–03 makes explicit and tests the mechanisms of the preceding publication, and writes a known equivalent of the Riemann hypothesis with its objects. The identities and theorems cited are classical or belong to their authors; the Riemann hypothesis remains open.
