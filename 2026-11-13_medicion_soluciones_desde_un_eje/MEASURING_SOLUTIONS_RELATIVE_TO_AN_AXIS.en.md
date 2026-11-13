---
title: "Measuring solutions relative to an axis"
subtitle: "Moments, restricted counts, and Hankel rank for minimal representations"
author: "Le Matt Ansatz Di Ego — Endless Monkey Project · Relational Geometry Program"
date: "November 13, 2026"
lang: en
---

**Mathematical research note — version 0.2 for technical review**

## Abstract

This note measures distributions of solutions projected onto a line of values and compared with a scalar reference. In the polynomial laboratory, Newton's identities recover moments of real roots from coefficients, and Sturm's theorem counts roots in intervals. In the Boolean laboratory, exact counts with fixed variables recover the moments of orders zero, one, and two. The Hankel–Vandermonde factorization certifies the minimum number of positions of a positive atomic measure from a sufficient sequence of moments. Two pairs of examples verify these identities. The note organizes a research agenda on reusing queries and measuring reconstruction costs in exact counting algorithms.

**Question:** Which quantities of a solution distribution can be recovered from a scalar reference, which queries distinguish such distributions, and which sequence of moments certifies the minimum number of positions in their representation?

## 1. Reference, object, and scope

The *reference* fixes the comparison, and the projection $w$ assigns a real value to each solution. A *difference* expresses variation among these values; a *distinction* is established by the first moment query that separates two distributions, as defined in Section 2. *Inheritance* describes the logical provenance of the restricted counts in Section 4. *Conservation* expresses the recovery of a quantity from declared relations. *Economy* compares resources used by procedures that perform the same task with the same exactness requirement.

In this note, $w$ defines the line of projected values, and $a$ is a scalar reference on that line. In the polynomial laboratory, each real root is indexed according to its multiplicity; in the Boolean laboratory, each satisfying assignment appears once. This convention makes the same moment formulas applicable to both classes of solutions.

## 2. An axis for quantifying a distribution of solutions

Let $K$ be a finite, nonempty set of solution indices, and let $w:K\to\mathbb R$ be a projection defined by the system's relations. The indices count repeated roots with their multiplicity. Let $a\in\mathbb R$ be the chosen scalar reference. Define the moments

$$M_j(K,w)=\sum_{x\in K} w(x)^j,\qquad j\ge0,$$

with $M_0=|K|$. The dispersion measure relative to the axis $a$ is

$$J_K(a)=\frac1{M_0}\sum_{x\in K}(w(x)-a)^2
=\frac{M_2}{M_0}-2a\frac{M_1}{M_0}+a^2.$$

**Proposition 1 (optimal quadratic axis).** The value minimizing $J_K(a)$ is

$$a_* =\frac{M_1}{M_0},\qquad
J_K(a_*)=\frac{M_2}{M_0}-\left(\frac{M_1}{M_0}\right)^2.$$

**Proof.** Completing the square gives $J_K(a)=J_K(a_*)+(a-a_*)^2$. $\square$

The minimum describes the **dispersion of positions** for the chosen projection. Its computational cost is determined for each concrete procedure.

Two systems can share their initial moments and differ at higher orders. For two distributions $A$ and $B$ with the same reference, define the *first order of distinction by moments* as

$$\delta_w(A,B)=\min\{j\ge0:M_j(A,w)\ne M_j(B,w)\},$$

when the set is nonempty. If the atomic measures are identical, write $\delta_w=\infty$. This quantity records the **first moment order** that distinguishes the projected distributions.

## 3. Real roots through Newton and Sturm

Let $P(z)=z^d+c_1z^{d-1}+c_2z^{d-2}+\dots+c_d$ be monic, with all its roots **real** and counted with multiplicity. Their power sums $p_j=\sum_{i=1}^d r_i^j$ are obtained from the coefficients through Newton's identities. In particular,

$$p_1=-c_1,\qquad p_2=c_1^2-2c_2.$$

The axis of least quadratic dispersion for the roots is $a_*=-c_1/d$, and their sum of squared distances is

$$\sum_i(r_i-a_*)^2=p_2-\frac{p_1^2}{d}.$$

For complex roots, the algebraic sum $(r_i-a)^2$ and the sum of squared Euclidean distances $|r_i-a|^2$ express different quantities. The quadratic-dispersion interpretation in this section applies to real roots.

**Exact check.** Consider

$$P_1(z)=z^4-10z^2+9,\qquad P_2(z)=z^4-10z^2+16.$$

| Quantity obtained without listing roots | $P_1$ | $P_2$ |
|:--|--:|--:|
| Number of real roots (with multiplicity) | 4 | 4 |
| Axis $a_*$ | 0 | 0 |
| $p_2$ | 20 | 20 |
| $p_4=200-4c_4$ | 164 | 136 |
| Roots in $(-5/4,5/4)$, by Sturm | 2 | 0 |

Thus $\delta(P_1,P_2)=4$: the distributions agree at moment orders $0,1,2,3$ and differ at the fourth. Counting roots inside a specified radius also distinguishes them. Newton's identities and Sturm's theorem provide these measurements without explicitly calculating the roots.

## 4. Boolean moments through restricted counts

Let $F$ be a Boolean formula with $n$ variables, and let $K_F=\{x\in\{0,1\}^n:F(x)=1\}$. Choose the comparison axis

$$w(x)=\sum_{i=1}^n \alpha_i x_i,\qquad \alpha_i\in\mathbb Z,$$

which measures a declared property of each solution. For Hamming weight, $\alpha_i=1$. Define the restricted counts

$$N=\#F,\quad A_i=\#(F\wedge x_i),\quad B_{ij}=\#(F\wedge x_i\wedge x_j).$$

In this restriction notation, $x_i$ means $x_i=1$; $B_{ij}$ is used only for $i<j$.

**Proposition 2 (the first two moments without enumeration).** For $w(x)=\sum_i\alpha_ix_i$,

$$M_0=N,\quad M_1=\sum_i\alpha_i A_i,$$

$$M_2=\sum_i\alpha_i^2 A_i+2\sum_{i<j}\alpha_i\alpha_jB_{ij}.$$

Consequently, if $N>0$, the axis $a_*=M_1/N$ and the minimum dispersion $J_K(a_*)$ are obtained with at most

$$1+n+\binom n2$$

exact counting queries on restricted formulas, plus rational arithmetic.

**Proof.** In every Boolean assignment, $x_i^2=x_i$. Expanding $w(x)$ and $w(x)^2$ and interchanging the sums over solutions yields the two equalities. $\square$

These identities reduce the recovery of the first three moments to exact counting queries and rational arithmetic. The total cost includes each query and the arithmetic. If $N=0$, the count certifies unsatisfiability; for $N>0$, the normalized axis and dispersion are defined.

**Checked examples.** On $x_1,x_2,x_3$:

$$F_A=(x_1\oplus x_2\oplus x_3=0)\land(x_1\lor x_2\lor x_3),$$

$$F_B=(\neg x_1)\land(\neg x_2\lor x_3).$$

Both have three solutions. Project using $w=x_1+x_2+x_3$.

| Measure | $F_A$ | $F_B$ |
|:--|--:|--:|
| $M_0$ (solutions) | 3 | 3 |
| $M_1$ | 6 | 3 |
| $M_2$ | 12 | 5 |
| Optimal axis $a_*$ | 2 | 1 |
| Minimum dispersion $J(a_*)$ | 0 | $2/3$ |
| Distinct observed positions | 1 | 3 |

The position-generating functions are

$$G_A(t)=3t^2,\qquad G_B(t)=1+t+t^2.$$

The **coefficients** of $G$ record the multiplicities at each position $w$. The roots of $G(t)$ characterize the generating polynomial; in the first laboratory, the roots of $P(z)$ are the solutions of the equation.

## 5. An exact minimum through moment rank

Group solutions by their real position $v_j=w(x)$; suppose there are $s$ distinct positions $v_1,\dots,v_s$ with positive multiplicities $m_j$. Then

$$M_k=\sum_{j=1}^s m_jv_j^k.$$

Form the Hankel matrix of size $r$:

$$\mathcal H_r=(M_{i+j})_{0\le i,j<r}.$$

**Theorem 3 (minimum number of positions).** For a finite real atomic distribution with positive multiplicities and $s$ distinct positions,

$$\operatorname{rank}(\mathcal H_r)=\min(r,s).$$

Consequently, $s$ is the **minimum number of atomic positions** in any representation that reproduces all the moments of the distribution.

**Proof.** Let $V_r$ be the Vandermonde matrix with entries $(V_r)_{ij}=v_j^i$. Then

$$\mathcal H_r=V_r\,\operatorname{diag}(m_1,\dots,m_s)\,V_r^{\mathsf T}.$$

Because the $v_j$ are distinct and all $m_j>0$, the matrix has rank $\min(r,s)$. Any representation using $s'$ positions produces Hankel matrices with rank at most $s'$; it therefore requires $s'\ge s$. The original $s$ positions attain this bound. $\square$

The classical Hankel–Vandermonde factorization provides a certificate of the **minimum number of positions in the distribution defined by the projection $w$**. The scalar reference $a$ organizes the dispersion measurement.

To certify $s$ from a finite sequence of moments, form Hankel matrices of increasing size until their rank is smaller than their size, or use a known upper bound on $s$. Proposition 2 provides $M_0,M_1,M_2$; the general certificate incorporates the higher-order moments required by the distribution.

**Check.** For $F_A$, the moments $M_0,\dots,M_4$ are $(3,6,12,24,48)$ and the matrix $\mathcal H_3$ has rank $1$. For $F_B$, they are $(3,3,5,9,17)$ and

$$\mathcal H_3(F_B)=\begin{pmatrix}3&3&5\\3&5&9\\5&9&17\end{pmatrix},\quad
\det\mathcal H_3(F_B)=4,\quad \operatorname{rank}=3.$$

Thus the solutions of the first system are represented by one projected position with multiplicity three, while the second requires three distinct positions to reproduce all its moments. The value $s$ measures the minimum support size of the **projected distribution**. The cost of a counting algorithm is assessed through its queries, arithmetic, and reconstruction.

## 6. Applications to exact counting algorithms

Proposition 2 uses counting queries $\#(F\wedge C)$, where $C$ fixes one or two variables. These restrictions produce instances compatible with any exact #SAT counter that accepts them. The cited preprints by Anthropic and OpenAI describe counters for fixed-width formulas under their stated hypotheses. If each query has bound $T(n,m)$ on the family under consideration, recovering $M_0,M_1,M_2$ uses at most $O(n^2)$ calls and rational arithmetic. When $T(n,m)=2^{o(n)}$, the total retains a subexponential bound.

One line of work examines the reuse of partial contractions in Anthropic's tensor construction. Another studies which auxiliary data from an interpolation construction by OpenAI allow moments of related queries to be recovered. The comparison will measure the costs of recognition, queries, reuse, and reconstruction.

The generating polynomial $G_F(t)$ encodes multiplicities by position. The auxiliary polynomial $H(T)$ in an interpolation construction by OpenAI encodes an algebraic deformation. A formal connection between them would consist of an explicit transformation and a recovery theorem. The polynomial in the first laboratory represents solutions as **roots** of an equation.

## 7. Established results and research program

**Exact results:** optimal center and dispersion from moments; Newton's identities for real roots; interval counts by Sturm; recovery of the first two Boolean moments from restricted counts; minimum number of positions from Hankel rank. The examples and calculations were checked with exact arithmetic.

**Research program:** identify concrete #SAT families in which a sequence of moments can be obtained and updated through reusable queries. The comparison of procedures will include the costs of recognizing relations, auxiliary queries, required precision, and reconstruction. It will record the moment order needed to certify each support.

**Question for technical review.** For concrete classes of #SAT, which moment subspaces can be recovered with a sufficient family of queries, and what is the total cost of recognizing and maintaining that family under new restrictions?

## Sources and verification

- *¿Cómo se cuantifica la información de un sistema?* Governing document, November 12, 2026.
- *Una misma pregunta, tres mecanismos*. Comparison between representations, November 12, 2026.
- Anthropic, *A $2^{o(n)}$ Time Algorithm for 3-SAT* (preprint v1, 2026), [text](https://hexagonmath.org/pdf/2610.00577v1).
- OpenAI, *The Exponential Time Hypothesis is False* (preprint, October 25, 2026), [repository](https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026).
- Mathematical background: Newton's identities, Sturm's theorem, Hankel moment matrices, and Vandermonde factorization.
- The accompanying verifier `verificar_eje.py` checks exact Newton identities, Sturm counts, restricted counts, dispersion, and Hankel ranks. Enumeration of eight assignments audits the formulas in the Boolean examples.

**Le Matt Ansatz Di Ego**  
*Endless Monkey Project · Relational Geometry Program*
