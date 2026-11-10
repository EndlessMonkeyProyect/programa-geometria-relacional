# What computation becomes unnecessary?
## Mirror Cube: minimal structures, reference discovery, and exact counting

**Endless Monkey Project**  
*Relational Geometry Program*  
**November 10, 2026 · Manuscript for independent review · version 0.2**

### Abstract

When can recognizing inherited relations and changing reference reduce the **total cost** of an exact computation? A *mirror cube* provides a conceptual laboratory for reference, reflection, closure, reopening, and cost. We do not derive mathematics from an optical metaphor: each result is stated under a verifiable contract. We connect three existing strands of the program. Reconstruction of the six binary edge labels of the four-vertex complete graph requires only three independent bits. A unique affine root may be recognized before closure, provided its residual state is retained. Recovering inherited parity relations can then support exact counting. For explicitly given XOR equations plus OR clauses, or for a family where the XOR reference can be extracted with a certified polynomial cost, we obtain an exact upper bound \(O(\operatorname{poly}(L)[1+2^{\min(t,d)}])\). Here \(L\) is the input length, \(d\) is affine free dimension, and \(t\) counts OR clauses not implied by the affine base. Experiments demonstrate favorable and unfavorable regimes against specific baselines. No general subexponential bound for 3-SAT, universal optimality, or algorithmic equivalence with external work is claimed.

**Keywords:** distinctions, inheritance, representation, reference recognition, affine spaces, XOR, CNF, exact counting, computational complexity.

## 1. The problem and four different costs

The program's November 8 paper, *Where does computation become cheaper?*, distinguished observable differences, exact representation, and operations needed to answer a query. We now make a fourth cost explicit: **discovering, validating, and updating the reference** that enables the other savings.

Let \(X\) be a finite state space and \(\mathcal Q\) a declared family of queries. Write \(x\sim_{\mathcal Q}y\) if all queries return identical answers. Then

\[
D_{\mathcal Q}=\log_2|X/\!\sim_{\mathcal Q}|
\]

measures the capacity to distinguish equivalence classes; it is **not Shannon entropy** without a probability distribution. A new constraint is inherited relative to a reference when it is already implied by its known relations. A constraint is genuinely restrictive when it excludes previously admissible realizations.

We distinguish **two structural measures**, \(D_{\rm obs}\) for observable distinctions and \(D_{\rm rep}\) for minimum size in a specified representation class, from **computational costs**, \(C_{\rm rec}\) for discovering and verifying the reference, \(C_{\rm calc}\) for counting and managing residues, and \(C_{\rm recon}\) for reconstructing the output. These quantities have different units and must not be added indiscriminately. A net advantage over baseline \(B\) requires

\[
C_{\rm rec}(F)+C_{\rm calc}(F)+C_{\rm recon}(F)< C_B(F)
\]

under the same cost model and exact task. Minimal representation does not automatically imply fastest computation.

## 2. Reconstructing the six edges of a tetrahedron from three bits

For \(K_4\), let \(s_i\in\mathbb F_2\) be vertex states and \(b_{ij}=s_i\oplus s_j\) the edge labels. From any focus \(f\), three star labels determine all six labels by
\(b_{ij}=b_{fi}\oplus b_{fj}\).

**Theorem 1.** There are precisely eight compatible edge patterns, and exactly three independent bits are necessary and sufficient to identify them. **Proof:** The linear map \(\delta:\mathbb F_2^4\to\mathbb F_2^6\) taking vertex labels to edge differences has kernel \(\{0000,1111\}\), hence rank three and image size eight. The three star labels achieve the encoding, and fewer than three bits cannot distinguish eight patterns. \(\square\)

The 16 vertex assignments yield eight observable edge patterns because global inversion preserves all edges. This is a minimum under the stated edge-reconstruction contract, not a general computational lower bound.

## 3. Early recognition of an affine root does not imply closure

Let \(S\subseteq\mathbb F_2^n\) be the admissible states. A dimension-\(d\) affine root is a set \(P=a+U\subseteq S\), with \(|P|=2^d\). Define \(\mathcal R_d(S)\) as all such roots.

**Theorem 2.** If \(|S|<3\cdot2^{d-1}\), then \(|\mathcal R_d(S)|\le1\). **Proof:** Two distinct affine \(d\)-flats intersect in at most \(2^{d-1}\) states, so their union has at least \(3\cdot2^{d-1}\) states. \(\square\)

This proves **at most one** root of fixed dimension, not its existence, and must not be conflated with a maximum-cardinality `Core` defined under a different contract. In \(\mathbb F_2^3\), every five-element subset contains a unique four-element affine plane and one residual point. Exhaustive affine-root and residual controls confirm all 336 ordered sequences of three exclusions. Of the 1,680 fourth-exclusion extensions, 336 close the root and 1,344 invalidate it. A residual state must not be discarded before it is excluded.

## 4. An affine root and a residual state from three clauses

A three-literal clause over three distinct variables forbids one of eight assignments. Let \(a,b,c\) be three distinct excluded assignments. The affine span is \(L=\{a,b,c,a\oplus b\oplus c\}\); its complement \(P=\mathbb F_2^3\setminus L\) is also an affine plane.

**Theorem 3.** The allowed set is precisely \(P\cup\{a\oplus b\oplus c\}\): a unique affine plane of size four and a disjoint residual point. **Proof:** The three excluded states lie in the uniquely generated four-point plane \(L\). The five permitted states comprise its four-point complement and its remaining fourth point. Uniqueness follows from Theorem 2. \(\square\)

A fourth clause excluding that residual point closes the plane. If instead it excludes a point in \(P\), the previously recognized root must be retracted. This is an exact relationship discovered without an explicit XOR equation in that local 3-CNF, **not a general method for arbitrarily obscured parity**.

## 5. Exact counting with parity equations and disjunctive clauses

Let \(F=(Ax=b)\land C_1\land\cdots\land C_k\), where \(Ax=b\) is over \(\mathbb F_2\), consistent of rank \(r\), and each \(C_j\) is an OR clause. The affine dimension is \(d=n-r\). Inclusion-exclusion yields

\[
\#F=\sum_{J\subseteq[k]}(-1)^{|J|}\,#\!\left(Ax=b\land\bigwedge_{j\in J}\neg C_j\right).
\]

Every negated clause is a set of unit equations; Gaussian elimination gives zero for inconsistent extensions and \(2^{n-r_J}\) otherwise. A clause already implied by \(Ax=b\) can be deleted after testing the inconsistency of \(Ax=b\land\neg C_j\). Let \(t\le k\) be the remaining clause count.

**Theorem 4.** With an explicit affine reference, exact counting takes

\[
O(\operatorname{poly}(L)[1+2^{\min(t,d)}]).
\]

**Proof:** Construct the affine basis and remove clauses implied by it in polynomial time. Inclusion-exclusion then visits at most \(2^t\) terms, each solvable by Gaussian elimination. Alternatively, enumerate \(2^d\) free affine parameters and verify every OR clause. Choose the cheaper route. \(\square\)

This bound is polynomial for \(\min(t,d)=O(\log L)\) and can be exponential otherwise. Any extraction from an input that does not explicitly expose the XOR constraints **adds a recognition and validation cost**. A polynomial bound on that extra step is a separate assumption that must be proved for each recognizable encoding family.

## 6. Recognition: the other component of economy

A reference extractor may output \(E(F)=(R,\Delta,\pi)\), with reference \(R\), residual information \(\Delta\), and a certificate \(\pi\) allowing exact recovery of the requested answer. The total cost is

\[
C_{\rm total}=C_E+C_V+C_{R,\Delta}+C_{\rm recon}.
\]

**Conditional transfer proposition.** If a family admits a correct extractor, a sound verifier, exact and non-overlapping (or properly inclusion-exclusion corrected) decomposition, and an exact counter for its outputs, the family can be counted at the combined cost of those operations. Net economy holds only where that combined cost is lower than a stated baseline. This criterion is not itself a new complexity upper bound.

A mirror cube's precise methodological role is to ask which changes of reference conserve the answer, which differences are inherited, which reopen the state space, and how expensive every operation is. Discovering the optimal reference for unrestricted CNF may be difficult; it is never assumed free.

## 7. Reproducible controls and negative cases

The bundled exchange-and-convergence laboratory and its unchanged results file report:

| Control | Observation |
|---|---|
| swap decomposition and tensor ranks | Local swap identities and matrix-rank formula checks; representational facts, not end-to-end time bounds. |
| local swap comparison | Local SWAP-bit correspondence between studied OpenAI and Anthropic constructions for \(r=2\); no algorithm-wide equivalence established. |
| common modular reference | LCM(12,18)=36 and an explicit uniqueness-vs-construction control. |
| affine-root and residual controls | Five-state affine root plus residual; 336 closure extensions and 1,344 retractions. |
| parity-plus-disjunction counting controls favorable | 96 variables, 81 XOR equations, eight OR clauses: **10,656** models with both algorithms; **0.0015 s** for affine inclusion-exclusion vs **0.385 s** for the included variable-elimination baseline. |
| parity-plus-disjunction counting controls unfavorable | 32 variables, 16 XOR equations, 20 OR clauses: **5,220** models with both algorithms, but **0.0378 s** for affine inclusion-exclusion vs **0.0021 s** for variable elimination. |
| interpolation-window control | An excessively narrow interpolation window fails to capture most of the weight in some tested regimes. |

These are implementation-level measurements, not benchmarks against industrial solvers. In parity-plus-disjunction counting controls, constructing the affine basis from **explicit XOR input** is timed; discovering such equations from arbitrary CNF is not. The included circuit-gate recognizer and its original results are separately documented below; its tests do not establish general hidden-parity extraction. The lightweight independent verifier included in this bundle checks the local tetrahedral reconstruction and affine-root bridge and small XOR+OR counts, not arbitrary hidden-gadget discovery.

## 8. Recognizing distributed parity relations in connected formulas

The complementary experiment receives formulas of clauses with at most three literals. Parity relations are encoded via fully defined two-input conjunction and disjunction gates, not written as parity equations. Auxiliary variables are uniquely determined by the primary variables; all identifiers and the ordering of the clauses are permuted. The recognizer validates the complete gate templates, reconstructs selected parity relations and retains the residual states of partial affine roots.

**Scope of the proposition.** When a formula belongs to this recognizable family of functional circuits and each primary assignment has a unique auxiliary extension, removing the validated gates and replacing them by their exact parity relation preserves the solution count. Each partial root is partitioned into a disjoint affine root and its residual state. If there are \(u\) such partial roots and \(k\) remaining disjunctions, the corresponding inclusion–exclusion procedure has cost \(O(\operatorname{poly}(|F|)[1+2^{u+k}])\). This is **not** a guaranteed polynomial-time extractor for arbitrary formulas.

In the supplied experiment data, a connected instance with 24 primary variables and 248 clauses has **5,312** exact solutions; a 32-primary-variable instance with 333 clauses has **98,560** solutions. A 96-primary-variable case with long-distance constraints and 1,549 clauses has **156,800** solutions. Reported timings are comparisons between specific Python implementations, not against modern optimized counting tools. As an independent editorial check, we reran **the entire distributed-relation laboratory**: 144 gate truth-table checks, two negative tests, 30 additional random controls, all primary-variable sizes from 8 to 96, and all long-distance tests. The exact counts agreed with their internal reference values. Recorded execution times vary between runs. The complete code and supplied results are included for further verification.

## 9. Comparison, open problems, and scope

The exchange-and-rank controls test local algebraic correspondences involving a swap operator and antisymmetric projections in external constructions. The identity \(\mathrm{SWAP}=I-2P_-\) is not enough for algorithmic efficiency: the number of terms, their discovery, evaluation, and recombination costs matter. The program does **not** claim to reproduce, supersede, or improve the whole OpenAI or Anthropic algorithms.

**Open problem.** Is there a nontrivial family of 3-CNF encodings with no obvious local gadgets in which a verifiable reference transformation yields a better end-to-end exact counting cost than the compared methods? A negative result or a lower bound on recognition would also settle a useful part of this question.

**Status:** K4 reconstruction, fixed-dimension affine uniqueness, local three-clause decomposition, and the explicit XOR+OR counting bound are proved under their hypotheses. Finite experiments support and limit specific implementations. A general recognition economy and any broad complexity advantage remain open.

## References and reproducibility

- Endless Monkey Project, [Where does computation become cheaper? / ¿Dónde se ahorra el cálculo?](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/2026-11-08_economia_del_calculo), November 8, 2026.
- Endless Monkey Project, [El cruce como reflejo central](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/2026-11-03_cruce_reflejo_central), November 3, 2026.
- Focal reconstruction of the six edges of a tetrahedron (historical supplement), October 18, 2026; the atlas of affine-root convergence and residual states, and the exact counting laboratory as specified in the local verification bundle.
- OpenAI, [The Exponential Time Hypothesis is False](https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026); Anthropic, [Hexagon Math preprint 2610.00577](https://hexagonmath.org/2610.00577). External references serve as comparison, not evidence of a universal advantage.

Editorial note: this manuscript consolidates independently stated results and scopes; it does not silently replace prior sources or upgrade unsupported claims. Independent proof and complexity review is requested.
