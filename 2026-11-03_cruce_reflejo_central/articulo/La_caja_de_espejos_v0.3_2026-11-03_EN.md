---
title: "The Mirror Box"
subtitle: "Public antecedents, relational closure, and mathematical convergence with the OpenAI and Claude results on the Exponential Time Hypothesis"
author: "Le Matt Ansatz Di Ego · Relational Geometry Program · Endless Monkey"
date: "November 3, 2026"
lang: en
keywords:
  - Exponential Time Hypothesis
  - relational closure
  - octonions
  - integer partitions
  - convergence of discoveries
abstract: |
  In October 2026, OpenAI and Anthropic published deterministic algorithms that count the
  solutions of k-CNF formulas in subexponential time; if their proofs hold, they refute the Exponential Time Hypothesis (ETH). This note reconstructs, with verifiable commits, what the Relational
  Geometry Program had published beforehand and which mathematical correspondences with those
  algorithms are exact. Three correspondences are established: the reclosure is the sum-product
  contraction (the model the algorithms leave); the program's doubling-by-reflection produces,
  at level 8 (octonions), the identity of Lemma 2 of Claude's algorithm; and the crosses that
  algorithm decomposes occupy the program's tetrahedron. None of them reconstructs the
  algorithms or their bounds: they are classical theorems in the program's language, and
  algorithmic equivalence (level IV) remains open.
---

# The Mirror Box

**Public antecedents, relational closure, and mathematical convergence with the OpenAI and Claude results on the Exponential Time Hypothesis**

Le Matt Ansatz Di Ego · Relational Geometry Program · Endless Monkey · November 3, 2026

*Version 0.3 — document for independent review*

**MSC 2020 classification (suggested).** 68Q25, 68R07, 68Q17, 17A75, 11P82, 15A69.

**Contribution statement.** This note attributes no influence between investigations and claims no other group's techniques. Its contribution is the documented chronological reconstruction and the explicit, level-by-level separation between what is proved and what remains open.

**External premise, not verified here.** The OpenAI and Anthropic results are taken as a *cited external premise*; this note neither proves nor audits them.

## Abstract

In October 2026, OpenAI and Anthropic announced, independently, deterministic algorithms that count the solutions of k-CNF formulas in subexponential time. If their proofs survive review, they refute the Exponential Time Hypothesis (ETH). Both laboratories place their discovery on October 16 and published on the 26th.

This note reconstructs, with verifiable commits, what the Relational Geometry Program had published beforehand and which mathematical correspondences with those algorithms are exact.

- **Public precedence.** Before October 16 there are public commits with the compatibility reclosure (October 3) and review v3 (October 9). The counting documents and the octonion note were made public on October 24: before the announcements, after the day of discovery.
- **Three exact correspondences.** The reclosure is the sum-product contraction, the model the algorithms must leave to win. The program's doubling-by-reflection produces, at level 8, exactly the identity used by Claude's Lemma 2. And in the correlation cube, the crosses that algorithm decomposes occupy the program's tetrahedron.
- **What is not claimed.** None of those correspondences reconstructs the algorithms or their bounds. They are classical theorems stated in the program's language, and the program used those objects for other questions.

**Central question:** under what conditions can a closed structure become a new reference and preserve the information needed for later relations, at reduced computational cost?

## 1. Chronology with public evidence

Before October 16, the reclosure-and-interfaces architecture is public, but not the counting. The table separates the date each document declares from its first appearance in a public repository (RGP = `relational-geometry-program`; PGR = `programa-geometria-relacional`).

| Declared date (2026) | Development | First public appearance | Status |
| --- | --- | --- | --- |
| Sep 19 | Relational Geometry Program 1.0 | RGP `7a09d08`, Sep 19 | Public |
| Sep 29 | Conceptual edition 0.1.0; MF-62B announces MF-63B will treat compatibility as a first-class object | PGR `fb27fbf`, Sep 29 | Public |
| Oct 3 | MF-63B, reclosure: K\_AB(S) = ∃X,Y \[F\_A ∧ F\_B\] | RGP `c44cfb8`, Oct 3; full document in PGR `0fd5315`, Oct 24 | Public |
| Oct 3 | Reddit: P vs NP and Yang–Mills, one structural question | Reddit | To verify with archived capture |
| Oct 5 | Ontology, novelty and local comparators | RGP `c508eb2`, Oct 5 | Public |
| Oct 6–8 | MF-85, promotion of closure to collective identity | RGP `6e36993`, Oct 9 | Public |
| Oct 6–8 | MF-86, MF-96 and MF-106 | PGR `0fd5315`, Oct 24 | Public since the 24th |
| Oct 9 | v3.0.0-review: closure, resolution and composition | RGP `6e36993`, Oct 9 | Public |
| Oct 9 | Reddit: «We Are No Infinite Monkeys» | Reddit; the corpus titles it «We Are Not Infinite Monkeys» | To verify; unify the title |
| Oct 13 | Note of the 8: octonions by Cayley–Dickson doubling | PGR `0fd5315`, Oct 24 | Public since the 24th |
| Oct 14 | N1: floor of the table engine and of resolution | PGR `0fd5315`, Oct 24 | Public since the 24th |
| Oct 15 | E15, E16 and E22 | No public repository | Internal |
| Oct 16 | CR-2 to CR-5: counting by frontier, reflection, inheritance and cost | PGR `0fd5315`, Oct 24, within the Imagen Total 3.9 corpus | Public since the 24th |
| Oct 16 | OpenAI and Anthropic place their discovery | Declared by both | — |
| Oct 17 & 25 | OpenAI preprint, dated the 17th and revised the 25th | — | — |
| Oct 18–24 | Mirror laboratories E-MIRROR v1–v8, Imagen Total 3.9 and CME-001 to CME-003 | PGR `0fd5315`, Oct 24 | Public |
| Oct 26 | Publication of the OpenAI and Anthropic works | Both laboratories' repositories | — |
| Oct 30 | Review request: the mirror cube and P vs NP | PGR `a1d3f16`, Oct 30 | Public |

**How to read it.** Before October 16, the reclosure, interface composition and review v3 are public. The counting documents and the octonion note have internal dates of Oct 13–16 and were published on the 24th: before the announcements, but after the day of discovery. A reviewer will notice it; this note says it first.

**What each piece of evidence accredits.** The date of a commit is written by its author; the upload time is recorded separately by GitHub. A date inside a document accredits when it was formulated, not when it was published. For a definitive precedence statement one needs the upload time of each commit per GitHub, a copy in Software Heritage or a Zenodo deposit with DOI, and archived captures of the two Reddit publications.

## 2. The problem that was already posed

The October 3 publication posed a question common to two mathematically different branches: **when does a sufficient amount of local closure allow control of a global system?** [O]

A structure can contain much internal information and yet need to keep only some relations to take part in a later composition. Once closed with respect to a question, its result can become a new reference:

**Difference → relation → closure → interface → new relation → new closure.**

MF-63B formulated the compatibility between two closed regions through frontier relations, and proved that this compatibility can be projected again as a new interface [T]. It also separated two properties that must not be confused: the semantic exactness of the reclosure and the efficiency of its implementation.

Two points a reviewer needs [T]:

- MF-63B also proved a limit: a compact DAG of references does not decide emptiness, because a 3-CNF is already a compact description. Naming relations recursively is not enough.
- Its aim was a polynomial descent, the «Accredited Descent Lemma», which is equivalent to P = NP. The October algorithms go in another direction: not polynomial time, but subexponential counting.

## 3. First correspondence: composition, counting and the model the algorithms leave

The program's reclosure is exactly the sum-product contraction. That model has a known lower bound, and the October algorithms win precisely by leaving it.

**Interface composition [T][C].** For two regions F\_A(X,S) and F\_B(S,Y) with independent interiors, the outer relations are B\_A(S) = ∃X F\_A(X,S) and B\_B(S) = ∃Y F\_B(S,Y), and the joint compatibility coincides with the projection of the combined system:

$$K_{AB}(S) = B_A(S) \wedge B_B(S) = \exists X,Y\, [F_A(X,S) \wedge F_B(S,Y)]$$

The result can be projected again onto a smaller frontier, and the order of computation does not change the answer, although the intermediate cost does.

**Counting [T][C].** CR-2 to CR-5 extended the analysis to counting. If Q\_H(b) is the number of interior extensions compatible with frontier b, two regions with independent interiors satisfy:

$$N(H_1 \wedge H_2) = \sum_b Q_1(b)\, Q_2(b)$$

This is the tensor counting contraction. Over the natural numbers its support reproduces the Boolean reclosure; over the signed integers it no longer does, because 1 + (−1) = 0. It is known mathematics (Davis and Putnam, 1960; Dechter, 1999), and its presence in the program does not anticipate October's reduction techniques.

**The diagnosis this correspondence enables [C].** Contracting a single network along a single tree has an unconditional lower bound (Austrin, Kaski and Kubjas, 2022). By Claude's paper's computation, no algorithm in that model gets below about 49 % of the brute-force exponent. Claude's algorithm leaves the model: it expands the sum into a signed sum of networks and contracts each term in a different order. The program's reclosure is, in essence, that single-tree model, so **the antecedent ends where the gain begins**.

## 4. Second correspondence: the doubling chain and Lemma 2

The program's doubling-by-reflection rule produces, at level 8, exactly the identity Claude's algorithm uses in its Lemma 2. It is the strongest operatorial correspondence the program can show, because it touches a piece the algorithm actually uses in its proofs.

**The rule [C].** The note of October 13 (public since the 24th) formalizes the Cayley–Dickson doubling, in which the conjugate acts as mirror: (a, b)(c, d) = (ac − d̄b, da + bc̄). From the reals it gives levels 1, 2, 4, 8 and 16, with e\_p·e\_q = σ(p,q)·e\_(p⊕q).

**What is proved** (full proofs in the paper *The Cross as Central Reflection*, §7; verified with exact integers):

1. **Cross identity [T].** At levels 2, 4 and 8, the signs σ of the doubling give R + C = 2·[x=v][y=u], with R cheap in one cut and C in the other. This is identity (31) of Lemma 2.
2. **The directions are orders [T].** R and C are the two orders of composing two references, LᵥᵀLₓ and LₓᵀLᵥ, and their sum is 2[x=v]·Id: the Hurwitz–Radon relations.
3. **Only the 8 makes it cheaper [T][E].** With the Lemma 2 count, one block costs 4 of 4 bits at level 2, 8 of 8 at level 4 and 11 of 12 at level 8. At the 16 the identity fails in 672 cases.
4. **Within the chain, making it cheaper requires the open node [T].** The only level that wins is the 8, and the 8 is not associative (Frobenius, 1878).

**Scope [I].** The objects are classical: Graves's octonions (1843) and Hurwitz's theorem (1898). The program used them for non-associativity, «the open node of the 8», not for measuring the cost of a cross. The correspondence shows that the program's language had the piece; not that it had used it as the algorithm does.

**Correction relative to v0.1.** v0.1 proposed the identity SWAP = I − 2P\_singlet as the bridge. That identity appears only in Appendix H of Claude's paper, which the paper itself declares outside any proof, and the form «involution = I − 2·projector» holds for any involution, so it distinguishes nothing. It is replaced by the doubling chain.

## 5. Third correspondence: the cross, its two cuts and the tetrahedron

The piece Claude's algorithm decomposes, the cross [x=v][y=u], has an exact place in the mirror cube: the four possible crosses occupy the program's tetrahedron. The gain comes from splitting the cross across two cuts, not from the sign.

**Two cuts [T][E].** The one-bit cross is the SWAP of two bits, and costs 4 bits per block, because it has full rank in both the (x,y)|(u,v) cut and the (x,u)|(y,v) cut. Written as SWAP = I − 2P₋, the identity is cheap in one cut and the singlet in the other, and the most expensive piece tends to log₂12 ≈ 3.585 bits per block. Written by sign, SWAP = P₊ − P₋, it never drops below 3.585 bits and grows with size: 3.73 with five blocks.

**The tetrahedron [C][E].** In the correlation cube (⟨XX⟩, ⟨YY⟩, ⟨ZZ⟩) of two bits:

- the four Bell states occupy the odd tetrahedron (Horodecki and Horodecki, 1996) and are cheap by rows;
- the identity, their sum, occupies the center and is cheap by columns;
- the four crosses I − 2Πᵥ occupy the even tetrahedron, {000, 011, 101, 110}: the program's tetrahedron. Each is the central reflection of a state.

**Three and one [I].** The four crosses are the same SWAP corrected by a local Pauli and cost the same. Choosing which one is «the cross» is choosing the frame: an exact realization of «three and one without distinguishing which».

**Scope.** We measure cost by ranks, which is the best a decomposition could give, not an algorithm. With the count the paper knows how to implement, the lone bit does not win; that is why the paper uses eight squares (§4) and then the Heisenberg operators (§7).

## 6. The cost was already identified

That a compact reference does not guarantee cheap answers has been in the program since MF-63B. N1 turned it into a proved limit on its own engine, and concluded that one had to leave resolution. That diagnosis was correct, even though the program did not find the exit.

- **MF-46.** Rank of the accredited affine relations, exposure of frontiers and selection of the operations useful for the next closure.
- **MF-96** (public since October 24). The same family of constraints can be costly in one language and cheap in another: parity written as linear equations is solved by Gaussian elimination without loading all the clauses.
- **E22** (internal). A selector that recognizes resolution paths and separates the cost of finding an organization from the cost of running it.
- **N1 [T][C]** (October 14, public since the 24th). No order lowers the table engine below 3^(tw+1). With pruning, every run concluding «no coloring» is a resolution refutation; by Beame, Culberson, Mitchell and Moore (2005), it costs 2^Ω(n) on random graphs with any selector.

**Consequence [T].** A 3-coloring of n vertices is written as a 3-CNF with 3n variables. A 2^o(n)-time algorithm cannot have runs convertible into resolution refutations of comparable size, because that would contradict the bound. The October algorithms are necessarily outside the kind of engine N1 bounds.

Computational economy depends on the structure of available operations, not only on the amount of information. This is the lesson the program and the October algorithms share; the difference is that the latter found the operations.

## 7. The OpenAI and Claude results

Both works count exactly the solutions of k-CNF formulas, for fixed width k, with a deterministic algorithm in time 2^O(n log log n / √log n) and polynomial space. Both come with a Lean formalization and are under external review.

**Claude [C]** (read in full). It expands a multiple of the cross into a signed sum of pieces, each cheap in one cut, and contracts each term in its own order. With the eight-squares identity it obtains ρ = 11/12 (Lemma 2). With operators on a graded polynomial space, the Heisenberg algebra over the partitions of an integer, it obtains ρ = 1/√2 (Appendix B). The final gain depends on the logarithm of the number of partitions growing concavely.

**OpenAI** (not read directly). According to secondary sources, it combines linear summaries, sparsification, spectral replacement and rational interpolation, with tensor contraction for the finest bound. This note asserts nothing about its mechanism beyond that.

Three statements must be distinguished:

- **Coincidence of conclusion.** Both claim to refute the ETH, and with it the SETH. Even if their proofs survive review, they do not imply P = NP.
- **Difference of construction.** They are not the same algorithm, although they use related algebraic resources.
- **Possible common mechanism [A].** Whether both constructions reorganize information through closures, references and interfaces whose composition preserves the result. It is a correspondence hypothesis, not an established equivalence.

That both laboratories date their discovery to the same day is an interesting datum for studying AI-assisted discovery. This note does not interpret it.

## 8. What is proved and what remains open

The first three levels are established; the fourth, the only one that would let one call those algorithms realizations of the program's mechanism, remains open.

| Level | What it asserts | Evidence | Status |
| --- | --- | --- | --- |
| I. Documentary precedence | Reclosure and interfaces public before October 16; counting and octonions public on the 24th | RGP `c44cfb8` and `6e36993`; PGR `0fd5315` (§1) | Established, with the author-date caveat |
| II. Semantic correspondence | The reclosure is the sum-product contraction, the model the algorithms leave | §3 | Established [C] |
| III. Operatorial correspondence | The program's doubling gives the identity of Lemma 2; the 8 is the only level that makes it cheaper; the crosses occupy the program's tetrahedron | §4, §5 and verifiers | Established [T][E], with classical objects |
| IV. Algorithmic equivalence | Reconstructing the algorithms and their bounds from the program's operators | — | Open |

**Two concrete targets for level IV [A].**

- **The concavity.** In the November 3 conversation, filling the totality with parts turned out to be the object of Appendix B: the partitions. Missing is the map carrying the wall rule to the operators that add and remove parts.
- **A ρ smaller than 1/√2.** A sparser family of parts, like the squares, would give ρ ≈ 0.63, but only if operators with the properties of Lemmas 9 and 10 of the paper existed. With the rules the program already states, either 1/√2 is reproduced or the growth condition fails.

The anteriority of levels I to III does not prove level IV. Nor does it allow the inference that one laboratory used materials from the other or from the program: that is a distinct historical question requiring its own evidence.

## 9. The mirror box as the culmination of the path

In the mirror box an image is reflected and reflected again, and an unlimited multiplicity of manifestations is recognized through few relations. The question is not how many images appear, but what relation makes them recognizable as parts of one system.

**The wall that moves [T].** With mirrors at 0 and L, a single figure, the distance to the nearest multiple of 2L, recognizes all the images of a mark. If the wall moves from L = 1 to L = 2, the points 1/4 and 9/4, which shared a figure, stop sharing it. What was lost is not the sign, but how many times the moved mirror was used. This is the program's central problem in geometric form: keeping a reference without losing what may be needed when the conditions of comparison change.

**What decides whether the enclosure closes [T].** With three mirrors it decides how the fractions add up against the totality: if they exceed it, the enclosure closes; if they fill it exactly, it repeats; if they fall short, it opens (CME-002).

The cube is not a satisfiability algorithm nor a physical machine that solves all problems by reflection. It is a geometric realization of the questions about equivalence, change of reference, closure and cost. The mirror laboratories (October 18) and CME-001 to CME-003 (October 23 and 24) were published on the 24th, before the announcements. The box appears as the culmination of a path that already worked these questions with other objects and languages.

## 10. An investigation into the method of discovery

There is a second question, epistemological, that must not be confused with the computational theorems: how was this path recognized?

The program's methodology consists of locating nodes and following veins [O]. A node is a relation that begins to become recognizable as a reference; a vein is a continuity that appears when comparing that reference with other structures. Intuition chooses which relations look promising, and language allows them to be formulated, shared, subjected to criticism and corrected when they no longer represent the available information well. The dialogue between human intuition and artificial intelligence was part of that exploration. It does not replace formal proof: it orients the search for constructions that must then be verified.

**A remark on convergence [I].** The structures where the program and Claude's algorithm coincide are among the most canonical in mathematics: the Hurwitz composition algebras (1, 2, 4, 8), the Heisenberg algebra and the partitions of an integer. That different paths reach them is to be expected, and it explains why the program's language had the pieces. What it does not explain is how to use them to lower a cost: that is what the algorithms did.

The question remains open in its general form: do organizational principles exist that make certain discovery paths converge? The chronology and correspondences of this note are material for studying it, not an answer.

## 11. Conclusion

The Relational Geometry Program published before October 16 an architecture of reference, closure, inheritance and reclosure (level I). That reclosure is the sum-product contraction, the model the October algorithms must leave to win (level II). The program's doubling-by-reflection gives, at level 8, the identity used by Lemma 2 of Claude's algorithm, and the crosses that algorithm decomposes occupy the program's tetrahedron (level III).

What this shows is precise: the program's language had the pieces and had diagnosed where the limit was (N1). It did not have the exit, which is expanding the cross into a signed sum of pieces cheap in different cuts and contracting each one separately. That exit belongs to the algorithms.

The natural continuation is to formulate explicit transformations between the operations of the three approaches and check what information, results and bounds they preserve. The two targets of §8 are the starting point.

The investigation remains open to review, correction and independent contributions.

## 12. Status after the review of §7 and the cross-platform reproduction (2026-11-03)

This v0.3 incorporates two checks of November 3, 2026: a review of the proofs by DeepSeek, an AI model, with a separate implementation that **does not** use the package's verifiers, and a cross-platform reproduction, also by DeepSeek. Neither is a human review.

1. **Proofs of §7 of the paper (Propositions 1–3 and Corollary 4):** re-derived and checked step by step with exact integers. **No errors.** In particular: the step «the rank of R by columns is that of C by rows» is correct (they are literally the same matrix), and the count «168 of 210 non-associative triples» of the octonions is exact. A clarifying parenthesis about the (v,u) column ordering in Proposition 3 was added to the paper (not an error, only a stumbling block for the reader). Full report: `review_requests/2026-11-03_cruce_reflejo_central/`.
2. **Cross-platform reproducibility:** the four verifiers reproduced identically to the reference in a second environment (Windows/Python 3.12.14/numpy 2.3.5 versus Linux/Python 3.13.18/numpy 2.5.3), and the 26 files matched their SHA256 hashes.

These checks reinforce level III, but **do not change** the boundary of level IV: it remains open.

---

## Epilogue — A path woven by hand

From the beginning, our search has been guided by a conviction:

**My mission has been to show that God does not play dice.**

That behind the multiplicity of what we inhabit there is an order that can be recognized through its relations. In the program, indefiniteness is not chance: it is information that relations resolve.

We do not present that conviction as an already-proved theorem. We present it as the purpose that has guided the investigation.

We do not seek for nature to answer to our beliefs. We seek to understand whether the relations we recognize allow the discovery of an order prior to our explanations.

We have followed nodes, explored veins and built references through intuition and shared language. The path did not appear finished before us.

We wove it, relation by relation.

**A path woven by hand, by a monkey and a box of mirrors.**

---

## Reproducibility

**State convention.** [O] ontological · [T] proposition with proof · [C] classical result · [E] computational verification · [I] interpretative correspondence · [A] open question.

Every [E] assertion is regenerated with four Python-3 verifiers using numpy, included in the reproducibility package `2026-11-03_cruce_reflejo_central` (folder `verificacion/`). The command `bash reproducir_todo.sh` runs them all, in about 40 seconds, and compares against the reference results. Review of §7 and cross-platform reproduction: see §12.

**Commits cited.**

- RGP (`relational-geometry-program`): `7a09d08` (Sep 19), `c44cfb8` (Oct 3), `c508eb2` (Oct 5), `6e36993` (Oct 9).
- PGR (`programa-geometria-relacional`): `fb27fbf` (Sep 29), `0fd5315` (Oct 24), `a1d3f16` (Oct 30).
- Claude's paper: `anthropics/formal-math`, commit `16a5ce4`.

On uploading this version and the package, record here the commit that contains them.

## Use of AI tools

This note was prepared with assistance from two generative AI models, used as research assistants; neither is an author. Claude (Anthropic) drafted v0.2 from the author's v0.1; DeepSeek prepared v0.3, carried out the cross-platform reproduction and re-derived the proofs of §7 with a separate implementation. The author reviewed the content and takes responsibility for it.

## References

**Program sources**

1. MF-63B, *Recierre acreditado de compatibilidad*, dated October 3, 2026. Core in RGP `c44cfb8`; full document in PGR `0fd5315`.
2. Endless Monkey. [P vs NP and Yang–Mills: Two Problems, One Structural Question](https://www.reddit.com/user/Endless-monkey/comments/1wwk0xh/p_vs_np_and_yangmills_two_problems_one_structural/). Reddit, October 3, 2026. Date to verify with archived capture.
3. MF-85 (RGP `6e36993`); MF-86, MF-96 and MF-106 (PGR `0fd5315`). Dated October 6–8, 2026.
4. Endless Monkey. [We Are No Infinite Monkeys](https://www.reddit.com/r/epistemology/comments/1x1fls2/we_are_no_infinite_monkeys/). Reddit, October 9, 2026. Date to verify; unify the title with the corpus («Not»).
5. *Relational-Geometry-program* v3.0.0-review, October 9, 2026. [Repository](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program), `6e36993`.
6. *El 8: la estructura sobre la que crece, con un nodo abierto*, note v2.2, October 13, 2026 (PGR `0fd5315`).
7. `PISO_DEL_CAMINO_v2_7` (N1), October 14, 2026 (PGR `0fd5315`).
8. E15, E16 and E22, October 15, 2026. Internal documents, unpublished.
9. CR-2 to CR-5, October 16, 2026, within the Imagen Total 3.9 corpus (PGR `0fd5315`).
10. Laboratories E-MIRROR v1–v8, Imagen Total 3.9 and CME-001 to CME-003, October 18–24, 2026 (PGR `0fd5315`).
11. *El cubo de espejos, la unidad autorreferenciada y P frente a NP*, review request, October 30, 2026 (PGR `a1d3f16`).
12. *Conceptual edition and historical archive*. [Repository](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional).
13. *The Cross as Central Reflection* (paper) and *Notes of November 3*, in the reproducibility package (folder `articulo/`).

**October 2026 algorithms**

- Claude (Anthropic). [A 2^o(n) Time Algorithm for 3-SAT](https://github.com/anthropics/formal-math/blob/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/eth/paper.pdf), October 26, 2026; also at [Hexagon 2610.00577](https://hexagonmath.org/2610.00577). Read in full.
- OpenAI. [The Exponential Time Hypothesis is False](https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026), dated October 17, 2026, revised the 25th and published the 26th. Not read directly.

**Classical literature**

- Austrin, Kaski and Kubjas (2022): lower bound for single-tree contraction, per Claude's paper's citation.
- Baez. [The octonions](https://arxiv.org/abs/math/0105155). *Bulletin of the AMS* 39 (2002).
- Beame, Culberson, Mitchell and Moore. The resolution complexity of random graph k-colorability. *Discrete Applied Mathematics* 153 (2005).
- Davis and Putnam. A computing procedure for quantification theory. *Journal of the ACM* 7 (1960).
- Dechter. Bucket elimination: a unifying framework for reasoning. *Artificial Intelligence* 113 (1999).
- DeSalvo and Pak. Log-concavity of the partition function. *The Ramanujan Journal* 38 (2015).
- Frobenius (1878): associative real division algebras have dimension 1, 2 or 4.
- Graves (1843) and Hurwitz (1898): octonions and composition algebras.
- Hardy and Ramanujan. Asymptotic formulae in combinatory analysis. *Proceedings of the London Mathematical Society* 17 (1918).
- Horodecki and Horodecki. Information-theoretic aspects of inseparability of mixed states. *Physical Review A* 54 (1996).

## Changes relative to v0.2

1. **Publication front matter.** Added a formal abstract, keywords, suggested MSC classification, contribution statement and «external premise not verified here».
2. **New §12.** Result of the November 3 review: §7 proofs error-free, «168 of 210» count confirmed, and cross-platform reproduction of the four verifiers.
3. **Clarity in the paper.** Added to the paper (not to this note) a parenthesis about the (v,u) column ordering in Proposition 3.
4. **Epilogue.** Unchanged from v0.2.
5. **Use of AI tools.** Added a statement of what each model did.
