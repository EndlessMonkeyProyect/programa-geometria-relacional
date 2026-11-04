---
title: "Proof note for Section 3.3"
subtitle: "The pair swap and related binomial counts · Relational Geometry Program"
author: "Le Matt Ansatz Di Ego"
date: "November 3, 2026"
lang: en
---

# Proof note for Section 3.3

**The pair swap and related binomial counts**

[Español](NOTA_PRUEBA_3_3.md) · [Review request](REVIEW_REQUEST_EN.md)

**Fixed sources · editorial update of November 4, 2026:** [OpenAI, §§2.7 and 4.2, commit `42907c9`](https://github.com/openai/math/blob/42907c9e999cc00d6abe7a50bfc1023250edd1b9/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) · [Anthropic, Appendix H, commit `16a5ce4`](https://github.com/anthropics/formal-math/blob/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/eth/paper.pdf). [Review thread](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/4).

This note proves the formulas of Section 3.3 for every t and Q in their respective settings: the one-bit crossing is S = I − 2P₋; in OpenAI's explicit construction the number of measurement rows is the count outside a window of antisymmetric factors; and in the one-bit split the ranks of each piece, by rows and by columns, are upper tails of the same binomial multiplicities at r = 2. It does not prove that this coincidence plays any role in either algorithm's bound.

## 1. Definitions

Let r ≥ 2 and $V=\mathbb{R}^r\otimes\mathbb{R}^r$, with basis $e_a\otimes e_b$. The swap is $S(e_a\otimes e_b)=e_b\otimes e_a$. Since $S^2=I$ and $S$ is symmetric, $P_\pm=\tfrac12(I\pm S)$ are orthogonal projectors with $P_++P_-=I$ and

$$S=P_+-P_-=I-2P_-.$$

The antisymmetric subspace has basis $e_a\otimes e_b-e_b\otimes e_a$ with $a<b$, of dimension $a_r=r(r-1)/2$; the symmetric one has dimension $s_r=r(r+1)/2$.

**Cuts.** For a four-index function F(x, y, u, v), the row cut is the matrix with rows (x, y) and columns (u, v); the column cut is the matrix with rows (x, u) and columns (y, v). Ranks are over ℝ. For block products, each cut is the Kronecker product of the blocks' cuts, up to a permutation of rows and columns.

## 2. The one-bit crossing

**Proposition 1.** In the row cut, [x=v][y=u] is the matrix of S and [x=u][y=v] is the identity. At r = 2, the entries of 2P₋ are $[x\neq y]\,(-1)^x\,[u\neq v]\,(-1)^u$, so S = I − 2P₋ is exactly the identity of Appendix H of Anthropic's paper.

*Proof.* The (x, y), (u, v) entry of S is $\langle e_x\otimes e_y,\,e_v\otimes e_u\rangle$, which is [x=v][y=u]. At r = 2 the antisymmetric subspace is spanned by $\psi=(e_0\otimes e_1-e_1\otimes e_0)/\sqrt2$, whose entries are $\psi(x,y)=[x\neq y]\,(-1)^x/\sqrt2$. Since $P_-=\psi\psi^{\mathsf T}$, the entry of $2P_-$ is the stated product. ∎

## 3. OpenAI's construction

On $V^{\otimes Q}$, let $\Pi_s$ be the swap acting on factor s (§2.7, Step 2 of the preprint). The $\Pi_s$ commute, satisfy $\Pi_s^2=I$, and $\Pi_s=I-2P_-^{(s)}$.

**Proposition 2.** Let $W_0=\tfrac12\sum_s(I-\Pi_s)=\sum_s P_-^{(s)}$ and $V_0=\prod_s\Pi_s$. In the product basis $\psi=\psi_1\otimes\cdots\otimes\psi_Q$, with each $\psi_s$ an eigenvector of S, $W_0\psi=j\,\psi$ and $V_0\psi=(-1)^j\psi$, where j is the number of antisymmetric factors. Hence $V_0=(-1)^{W_0}$, and the eigenvalue j of $W_0$ has multiplicity

$$m_r(Q,j)=\binom{Q}{j}\,a_r^{\,j}\,s_r^{\,Q-j}.$$

*Proof.* $P_-^{(s)}\psi$ is ψ if $\psi_s$ is antisymmetric and 0 otherwise; $\Pi_s\psi=\pm\psi$ by the same criterion. The multiplicity counts the ways to choose which j factors are antisymmetric and one vector from each subspace. ∎

**Corollary 3.** With $M_0=V_0\,f(W_0)$ and $f(j)=(-1)^j$ on the window I, $M_0\psi=(-1)^j f(j)\,\psi=\psi$ when j ∈ I. In OpenAI's explicit choice, the measurement rows are the basis vectors with j ∉ I, so their number is

$$c=\sum_{j\notin I}m_r(Q,j)=r^{2Q}\,\Pr[W\notin I],\qquad W\sim\mathrm{Bin}\!\left(Q,\tfrac{r-1}{2r}\right),$$

which is the preprint's expression for that choice. Its lemma states an upper bound on the number of rows; this equality does not assert that the count is minimal. ∎

## 4. The one-bit split

At r = 2, on $V^{\otimes t}$, expand $S^{\otimes t}=\prod_s(I-2P_-^{(s)})$ by the number of factors I. The piece $A_i$ collects the terms with i factors I and t − i factors −2P₋, so that $S^{\otimes t}=\sum_i A_i$.

**Proposition 4 (rows).** $\operatorname{rank}_{\text{rows}}(A_i)=\sum_{j\ge t-i}\binom{t}{j}3^{\,t-j}$.

*Proof.* In the row cut, $A_i$ is the operator itself, and it is diagonal in the product basis. Let ψ have antisymmetric set J of size j. The term with factors I on the set T is nonzero exactly when the complement of T is contained in J, and then equals $(-2)^{t-i}\psi$. There are $\binom{j}{t-i}$ such terms, so $A_i\psi=\binom{j}{t-i}(-2)^{t-i}\psi$, nonzero if and only if j ≥ t − i. The rank is the number of basis vectors with j ≥ t − i, that is $\sum_{j\ge t-i}m_2(t,j)$ with $m_2(t,j)=\binom{t}{j}3^{t-j}$. ∎

**Proposition 5 (columns).** $\operatorname{rank}_{\text{columns}}(A_i)=\sum_{j\ge i}\binom{t}{j}3^{\,t-j}$.

*Proof.* The column cut of one block is the realignment $R(F)(x,u;\,y,v)=F(x,y,u,v)$. With $\Phi=e_0\otimes e_0+e_1\otimes e_1$, $R(I)=\Phi\Phi^{\mathsf T}$ and $R(S)=S$, so $R(-2P_-)=R(S-I)=S-\Phi\Phi^{\mathsf T}$. Since $S\Phi=\Phi$, the two commute and share the basis formed by $\phi^+=\Phi/\sqrt2$, two symmetric vectors orthogonal to Φ, and the singlet. In it, $R(I)$ has eigenvalues (2, 0, 0, 0) and $R(-2P_-)$ has (−1, 1, 1, −1), none of them zero.

Realignment is multiplicative over blocks. On a product vector with k factors equal to $\phi^+$ (set K), the term with factors R(I) on T is nonzero exactly when T ⊆ K. All such terms have the same value, $2^i(-1)^{k-i}\prod_{s\notin K}\lambda_s$, so the sum is $\binom{k}{i}$ times that value and is nonzero if and only if k ≥ i. Since $\phi^+$ is one of four vectors per block, the number of vectors with k ≥ i is $\sum_{k\ge i}\binom{t}{k}3^{t-k}$. ∎

## 5. Consequence and limits

At r = 2, let $W_m\sim\mathrm{Bin}(m,1/4)$ for each nonnegative integer m. The three counts use the same binomial weights with different summation ranges:

$$\operatorname{rank}_{\text{rows}}(A_i)=4^t\Pr[W_t\ge t-i],\qquad \operatorname{rank}_{\text{columns}}(A_i)=4^t\Pr[W_t\ge i],\qquad c=4^Q\Pr[W_Q\notin I].$$

For example, with t = 4 and i = 2, and with Q = 4 and I = {0, 1}, both equal $4^4\Pr[W_4\ge2]=67$. In general, the complement of I can consist of both a lower and an upper tail.

**What is not proved.** That this coincidence plays any role in the bounds. In Anthropic's paper the one-bit split is in Appendix H, which no proof uses; Lemma 2 uses the eight-square identity. In OpenAI's, c does enter the cost of the measurements, but it has not been shown that its coincidence with the ranks of the one-bit split has consequences. The value 67 depends on the choice of parameters and is not, on its own, evidence of a common mechanism.

## 6. Numerical verification

`verificar_pieza_compartida.py` checks Propositions 1 and 2 numerically for r = 2 to 5, Corollary 3 for (r, Q) = (2, 3), (2, 4) and (3, 3), the realignment facts of Proposition 5, and the ranks of Propositions 4 and 5 for t = 3, 4 and 5 with explicit Kronecker products. Its output and environment are in `salida_verificador_2026-11-03.txt`. These are numerical checks, not formal proofs.
