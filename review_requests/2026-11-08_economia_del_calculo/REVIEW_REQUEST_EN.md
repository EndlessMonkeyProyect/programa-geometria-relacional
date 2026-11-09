# Where does computation become cheaper?

**Independent review request**  
**Endless Monkey Project**  
*Relational Geometry Program*

November 8, 2026 · version 2

**Reviewed version:** [tag `2026-11-08-economia-del-calculo-v2`](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/2026-11-08-economia-del-calculo-v2/2026-11-08_economia_del_calculo) · [report](../../2026-11-08_economia_del_calculo/report.md) · [lab](../../2026-11-08_economia_del_calculo/laboratorio_economia_relacional.py) · [changes](../../2026-11-08_economia_del_calculo/CAMBIOS.md) · [Español](SOLICITUD_REVISION.md)

---

## A concrete question

Proper 3-colourings of the w × m grid with free boundaries satisfy a linear recurrence in m. For each width, the symmetry S₃ × Z₂ (permuting colours, reversing the column) groups the columns into orbits. The minimal order of the recurrence is the dimension of the minimal linear representation of the counting sequence:

| Width w | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Columns | 3 | 6 | 12 | 24 | 48 | 96 | 192 | 384 | 768 | 1536 |
| Orbits | 1 | 1 | 2 | 3 | 6 | 10 | 20 | 36 | 72 | 136 |
| Minimal order | 1 | 1 | 2 | 3 | 5 | 7 | 13 | 19 | 35 | 51 |

**Does the sequence of orders 1, 1, 2, 3, 5, 7, 13, 19, 35, 51 have a known explanation? Do the orders for widths 8 to 10 appear in the transfer-matrix literature?**

**What is proven.** Every order in the table is certified in exact arithmetic (next section). At w = 10, symmetry groups 1536 columns into 136 orbits, and the sequence admits a minimal linear representation of dimension 51 over the rationals.

**What we ask.** Whether the sequence of orders has an explanation and whether it is already published. In the sources consulted, the cited recurrences reach width 7: the OEIS gives recurrences of order 7 and 13 for widths 6 and 7 ([A207995](https://oeis.org/A207995), [A207996](https://oeis.org/A207996)). The counting table [A207997](https://oeis.org/A207997) includes larger widths, but does not by itself give the minimal orders for widths 8 to 10. The transfer-matrix literature remains to be checked.

## The reproducible evidence

Let b_k = 1ᵀ·T^k·1, with T the transfer matrix between columns; b_k counts the colourings of k + 1 columns. Since T is symmetric, the Hankel matrix H_N with entries b_(i+j) is the Gram matrix of the first N Krylov vectors T^i·1. Then det H_d ≠ 0 and det H_(d+1) = 0 fix the order d of the minimal recurrence valid for every m ≥ 1, which is the dimension of the minimal linear representation (Kronecker). The shifted Hankel matrix b_(1+i+j) is also nonsingular: the recurrence has no zero root, and no shorter one holds from m = 2 on.

A determinant that is nonzero modulo a prime is nonzero over the integers; the vanishing determinant is computed exactly. For w = 10 the recurrence has integer coefficients and order 51. The 51 is a property of the counting sequence and of its linear representations.

```bash
python3 -I laboratorio_economia_relacional.py E5 E5x E5c
```

E5 checks the ranks modulo two primes, E5x computes the exact Krylov dimension over the rationals, and E5c certifies the order for each width.

## The economy between references

### The general question

Can a better economy of computation arise from relations between references without losing the answer we seek?

Our starting point is **distinctions, inheritance, and economy**. A reference groups configurations that appear identical from its viewpoint; another relation may inherit, distinguish, or reopen what was grouped. The laboratory of **a mirror cube, a moving wall, and spheres** makes such changes of reference visible without changing the observed structure.

We ask **what can be proved**, under which assumptions, where the approach fails, and which results already exist. An impossibility theorem or a counterexample is also a result.

More precisely, three costs must be distinguished: **(i)** the differences that remain observable, **(ii)** those that must remain active to represent all possible futures exactly, and **(iii)** the operations needed to answer a query. They are three distinct, though related, costs. Any claim of *economy* should specify the query, the representation, and the baseline against which cost is measured.

The grid is a case of this question: symmetry groups 1536 columns into 136 orbits, and the counting query allows a further reduction, from 136 to 51 dimensions.

### Two controls separating the costs

Experiment **E9** keeps the same function and exact count (**6561**) but changes the maximum cut rank from **256 to 2** simply by changing variable order: the reference makes a large difference to the cost of a sequential representation. Satisfiable **Tseitin** formulas on expanders require exponential ordered representations yet are counted in polynomial time by Gaussian elimination (§6). These two cases separate **representation width** from **the cost of solving**.

### The mechanism we want to explore

In **a mirror cube**, moving the reference wall may group or separate images without modifying the underlying objects. With **spheres**, distance and a threshold determine which distinctions remain observable. The computational question is whether this picture suggests an exact **reflection, closure, or reopening** operation that lowers the work needed to answer a query.

Section **§10** of the report suggests looking for signed identities of the form

`X = Σ_j s_j c_j O_j`, with `s_j ∈ {−1,+1}`,

related to the involution `SWAP = I − 2P₋`, where `P₋` projects onto the antisymmetric subspace. Lower cut rank for each term is easy to achieve: every matrix decomposes into rank-one terms, sometimes too many. Real economy also requires bounds on **the number of terms, the cost of finding, evaluating, and recombining them, and exactness across the entire input family**.

This is the open challenge: exhibit a family with a proved saving, establish a no-go theorem for such decompositions, or give a counterexample.

## Nine claims and their status

Each item points to its proof in the report and, where applicable, a reproducible experiment. The status says what review is requested.

1. **Inheritance between partitions.** For partitions P and Q of a finite set, let J range over blocks of P ∨ Q and let p_J and q_J count the P- and Q-blocks inside J. Then `|P ∧ Q| ≤ Σ_J p_J q_J`, with equality exactly when P and Q permute. Under permutation and with k = |P ∨ Q|, `|P ∧ Q|·|P ∨ Q| = |P|·|Q| + k²·Cov_J(p_J, q_J)`: the product law requires permutation and zero covariance, for example homogeneous blocks. For residue classes this yields `lcm(H,m)·gcd(H,m) = Hm`. *Status:* to review; the modular identity is classical and we seek prior formulations for general partitions. **§2, Prop. 2.1, Cor. 2.2–2.3; E1.**
2. **Active distinctions and cut rank.** For a **linear sequential representation over a field**, minimum width at each past–future cut equals the matrix rank. For deterministic equivalence of futures, the criterion is Myhill–Nerode. *Status:* with antecedent: the theorem of Fliess (1974) and Carlyle–Paz (1971). **§3, Thm. 3.1 and 3.3.**
3. **Limit on universal reduction.** If `L: K^X → K^r` is linear and its induced equivalence is compatible with multiplication by **every** constraint indicator, its kernel is an ideal of the function algebra. If the exact count of every function must also be recoverable, `r ≥ |X|` (for Boolean assignments, `2^n`). *Status:* to review, especially the universality and count-recovery assumptions. **§4, Thm. 4.1.**
4. **Cost of identifying the minimal reference.** For a 3-CNF, deciding whether two past assignments admit exactly the same future is coNP-complete. So is deciding whether an added clause is **logically redundant** (`F ⊨ C`). *Status:* with antecedent: both reduce from unsatisfiability. **§4, Prop. 4.2–4.3.**
5. **Variable-order representations on expanders.** For monotone 2-CNFs from bounded-degree expander families, in **every variable order and over every field**, some cut has rank `2^Ω(n)`. The proof uses induced matchings and a **set-disjointness** submatrix. *Status:* to review; the rectangle technique is that of Bova, Capelli, Mengel and Slivovsky (2016). **§6, Thm. 6.1; E2, E2b.**
6. **Tseitin cuts.** For a connected G, any satisfiable charge and an edge partition `(A,B)`, `rank M_{A,B} = 2^λ(A)`, where `λ(A) = r(A) + r(B) − r(E)` is the connectivity function of the graphic matroid. In graph terms, `λ(A) = β + 1 − c_A − c_B`, with β the vertices incident to edges on both sides and c_A, c_B the components of the graph on each side. *Status:* with antecedent: with zero charge it is Forney's state space theorem (1994) for the cycle code, and λ is the function Kashyap (2008) uses for trellis-width. The rank was checked directly on 3003 cuts with zero charge, 3003 with random charge and 216 on random graphs. **§6, Thm. 6.2; E3b.**
7. **Three-colour grid, width 10.** 1536 columns, 136 orbits under `S₃ × Z₂`, and a minimal linear representation of dimension **51** over the rationals: the minimal recurrence has order 51. *Status:* certified by exact computation (det H_51 ≠ 0, det H_52 = 0, no zero root). What is open is the opening question. **§5.5; E5, E5x, E5c.**
8. **Optical fusion in a specified model.** For five sources and the observation operator in E6, `R_ℓ ≈ r(c_ℓ/ε)^(1/ℓ)` is the distance at which a distinction falls below relative threshold ε. In the symmetric example, the last surviving mode is the odd dipole. *Status:* its conditions are to review. **§7, Prop. 7.1–7.2; E6.**
9. **Comparison with the October 2026 papers.** OpenAI and Anthropic report exact-counting algorithms in `2^o(n)` time for fixed `k`, including `k = 2`. **If those results and their applicability to this family hold**, claim 5 illustrates a gap between the cost of every variable-order representation and that of an algorithm using other operations. The proposed readings are deformation with interpolation and signed cancellation. *Status:* conditional on those papers. **§8.**

## Review questions

- **Proofs:** Does any claim fail, need an additional hypothesis, or conflate rank, representation width, operation count, and construction time? Claims 1, 3, 5 and 8 in particular.
- **Prior art:** Where have equivalent versions of claims 1 or 3 appeared? Is there an explanation of the grid's sequence of orders, or an earlier publication of the orders 19, 35 and 51? Precise references are welcome.
- **Mechanism:** Do exact reflection or signed-cancellation transformations exist with **lower total cost**? What necessary or sufficient conditions could establish or rule them out?
- **Correspondences:** Which links to OpenAI and Anthropic are verifiable mathematical identities, which are analogies, and which remain conditional?

## Reproduction

The report contains the proofs, counterexamples, experiments E1–E12 (plus E5x and E5c), and a review-status table.

```bash
pip install -r requirements.txt
python3 -I laboratorio_economia_relacional.py                # everything, about 4 minutes
python3 -I laboratorio_economia_relacional.py E5 E5x E5c     # the grid and its certificate
python3 -I laboratorio_economia_relacional.py E1 E3b         # partitions and Tseitin, about 30 s
```

**Sources:** [report and lab, version 2](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/2026-11-08-economia-del-calculo-v2/2026-11-08_economia_del_calculo) · [OpenAI preprint](https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026) · [Anthropic paper](https://hexagonmath.org/2610.00577) · OEIS [A207995](https://oeis.org/A207995), [A207996](https://oeis.org/A207996), [A207997](https://oeis.org/A207997) · G. D. Forney, *Dimension/length profiles and trellis complexity of linear block codes*, IEEE Trans. Inf. Theory 40(6), 1994 · [N. Kashyap, *Matroid pathwidth and code trellis complexity*, arXiv:0705.1384](https://arxiv.org/pdf/0705.1384).

**How to respond:** open a repository issue or comment here, identifying the **claim number, hypothesis, proof step, experiment, or earlier reference**. Corrections are published in [`CAMBIOS.md`](../../2026-11-08_economia_del_calculo/CAMBIOS.md) with their reasoning.
