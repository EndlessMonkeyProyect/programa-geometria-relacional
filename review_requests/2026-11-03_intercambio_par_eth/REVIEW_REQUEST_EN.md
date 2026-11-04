---
title: "Request for Independent Review"
subtitle: "Documentary precedence and correspondences with the ETH refutations · Relational Geometry Program"
author: "Le Matt Ansatz Di Ego"
date: "November 3, 2026"
lang: en
---

# Request for Independent Review

**Documentary precedence and correspondences with the ETH refutations**

Le Matt Ansatz Di Ego · Relational Geometry Program · November 3, 2026

[Español](SOLICITUD_REVISION.md)

---

## Summary

We request review of two separable questions: which formulations of the Relational Geometry Program were public and verifiable before October 16, 2026, and whether certain operations of the program coincide with pieces of the two algorithms that refute the Exponential Time Hypothesis (ETH), OpenAI's and Anthropic's. The main result is an exact local coincidence, measured on November 3: the pair swap appears as the same operator in the constructions of both algorithms. In addition, related sums of the same binomial multiplicities give the ranks of Anthropic's one-bit split and the number of rows in OpenAI's explicit measurement construction; the formulas are proved in general, but they have not been shown to affect either bound. It is not an identity between the algorithms.

We claim no algorithmic equivalence, no influence between groups and no anticipation of the algorithms, and the validity of the two refutations is taken as an external premise. The chronology rests on commit metadata, which the author controls, and still has to be confirmed with independent timestamps. Five hypotheses (H1 to H5) come with explicit refutation criteria, so that a reviewer can decide where the framework explains and where it only interprets.

## 1. Scope and review questions

**Review priority · November 4, 2026.** We first request a human assessment of Propositions 1, 2, 4 and 5 and Corollary 3 of the proof note: correctness and faithful correspondence with the sources. The second question is bibliographic: precedents for the formulas or comparison. Replies can be collected in the [dedicated thread](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/4); documentary chronology is a separate question.

Each question states what evidence would settle it and where it stands today.

| # | Question | Evidence that settles it | Status |
| --- | --- | --- | --- |
| Q1 | What was public before October 16? | Independently dated push events, snapshots, DOIs or archived captures that contain the relevant content | Partial: commit metadata is consistent, independent timestamps are missing (Section 2) |
| Q2 | Do the operations coincide algebraically? | Identities in standard notation and a verifier | One exact local coincidence between the two algorithms (3.3); the rest is classical or analogy |
| Q3 | Does the framework derive the result without postulating it? | Explicit deduction from the program's principles | Open (H3) |
| Q4 | Is there historical dependence between groups? | Independent external evidence | Out of scope (H4) |
| Q5 | Has it been noted that both algorithms share the pair swap? | Literature or public discussion of the two papers | Open (H2 and H5) |

**Terminology.** "OpenAI" and "Anthropic" name the laboratories. Anthropic's paper is signed by Claude, its model, and is cited that way in the references.

## 2. Verifiable chronology

The request cites commits dated before October 16 for the interface composition (MF-60B to MF-62B), the core of the MF-63B reclosure, MF-85 and the v3 review; independent evidence of when these versions became public is still needed. The cited records for the counting documents, the octonion note and the floor N1 are dated October 24, before the announcements but after the reported day of the discovery. An internal date does not establish precedence by itself. PGR is this repository, programa-geometria-relacional, and RGP is [Relational-Geometry-program](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program).

| Internal date (2026) | Document | Cited record | Public before Oct 16? |
| --- | --- | --- | --- |
| Sep 19 | Relational Geometry Program 1.0 | RGP [`7a09d08`](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/commit/7a09d08), Sep 19 | Unverified; commit date only |
| Sep 29 | Conceptual edition 0.1.0: MF-60B to MF-62B; MF-62B announces that MF-63B will treat compatibility | PGR [`fb27fbf`](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/commit/fb27fbf), Sep 29 | Unverified; commit date only |
| Oct 3 | MF-63B, compatibility reclosure | Core in RGP [`c44cfb8`](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/commit/c44cfb8), Oct 3; full document in PGR `0fd5315`, Oct 24 | Core unverified; full document not in cited record until Oct 24 |
| Oct 3 | Reddit: "P vs NP and Yang–Mills: Two Problems, One Structural Question" | Reddit, with its own timestamp | Platform timestamp to verify; archived capture missing |
| Oct 5 | Ontology, novelty and local comparators | RGP [`c508eb2`](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/commit/c508eb2), Oct 5 | Unverified; commit date only |
| Oct 6–8 | MF-85, promotion of closure to collective identity | RGP [`6e36993`](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/commit/6e36993), Oct 9 | Unverified; commit date only |
| Oct 6–8 | MF-86, MF-96 and MF-106 | PGR `0fd5315`, Oct 24; MF-96 is only cited on Oct 9 | No |
| Oct 9 | v3.0.0-review: closure, resolution and composition; involution H = 2P − I and the Walsh basis | RGP `6e36993`, Oct 9 | Unverified; commit date only |
| Oct 9 | Reddit: "We Are No Infinite Monkeys" (r/epistemology) | Reddit; date not verified; the corpus titles it "Not" | To be verified |
| Oct 13 | Note on the 8: octonions by Cayley–Dickson doubling | PGR [`0fd5315`](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/commit/0fd5315), Oct 24 | No |
| Oct 14 | N1: floor of the table engine and of resolution | PGR `0fd5315`, Oct 24 | No |
| Oct 15 | E15, E16 and E22 | No public repository | No, internal |
| Oct 16 | CR-2 to CR-5: frontier counting, reflection, inheritance and cost | PGR `0fd5315`, Oct 24, inside Imagen Total 3.9 | No |
| Oct 16 | Anthropic: its paper places the finding of the core algorithm on that day | Anthropic's paper, §1 | — |
| Oct 17 | OpenAI preprint, revised Oct 25; it states no discovery date | openai/math | — |
| Oct 18–24 | Mirror laboratories E-MIRROR v1 to v8, Imagen Total 3.9, CME-001 to CME-003 | PGR `0fd5315`, Oct 24 | No |
| Oct 26 | Date of Anthropic's paper; both results announced | Both laboratories' repositories | — |
| Oct 30 | Review request: the mirror cube and P versus NP | PGR [`a1d3f16`](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/commit/a1d3f16), Oct 30 | — |
| Nov 3 | The Cross as Central Reflection | PGR [`a630cff`](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/commit/a630cff); DOI 10.5281/zenodo.23932854 | — |

**Method caveat.** A commit date is written by its author and can be rewritten. GitHub push events have server timestamps when available, but GitHub does not provide a permanent per-commit upload timestamp; its public Events API retains only recent events. A version visible today does not prove that its files existed in an earlier version. A claim of precedence needs independently dated push events or archival snapshots containing the exact commits and content, and independently dated copies of the two Reddit posts. [GitHub event retention](https://docs.github.com/en/rest/activity/events) · [Software Heritage origin visits](https://docs.softwareheritage.org/devel/swh-web/uri-scheme-browse-snapshot.html)

## 3. Mathematical correspondences

There is one exact local coincidence between the two algorithms; the program's correspondences with them are well-placed classical mathematics or analogies. Each carries its type: (A) algebraic identity, exact and verifiable; (B) structural analogy, same form in another space or role; (C) interpretive reading, not falsifiable on its own.

### 3.1 Interface composition — type A, classical

For two regions $F_A(X,S)$ and $F_B(S,Y)$ with common frontier $S$ and disjoint interiors:

$$K_{AB}(S)=\exists X\,F_A(X,S)\wedge\exists Y\,F_B(S,Y)=\exists X,Y\,[F_A\wedge F_B]$$

This is the variable elimination of Davis and Putnam (1960) and of Dechter (1999): a factor contraction in the Boolean semiring. The criterion $B_A \cap B_B \neq \emptyset$ is public in MF-61B (Sep 29) and the core of the reclosure in MF-63B (Oct 3).

### 3.2 Frontier counting — type A, classical

With $Q_H(b)$ the number of interior extensions compatible with frontier $b$, $N(H_1 \wedge H_2) = \sum_b Q_1(b)\,Q_2(b)$: a contraction in the counting semiring. The map from ℕ to 𝔹 preserves the structure; the one from ℤ to 𝔹 does not, because 1 + (−1) = 0, so a sum with cancellations cannot be followed by the Boolean reclosure. In the 21-solution pilot, with frontier {x₂, x₃}, N₁ = [2, 1, 2, 2] and N₂ = [4, 3, 2, 3] give 21. Public since October 24 (CR-2).

### 3.3 The pair swap in both algorithms — type A, local coincidence measured November 3

Let $S$ be the swap on $\mathbb{R}^r \otimes \mathbb{R}^r$ and $P_-$ its antisymmetric projector, so that $S = I - 2P_-$.

- **Anthropic.** The crossing [x=v][y=u] is $S$. Lemma 2 decomposes it with the eight-square identity (ρ = 11/12). Appendix H records the one-bit version, and the paper states that no proof uses it:

$$[x=v][y=u]=[x=u][y=v]-[x\neq y]\,(-1)^{x}\,[u\neq v]\,(-1)^{u}$$

- **OpenAI.** Πₛ swaps pair $s$ (§2.7, Step 2). With $W_0$ counting antisymmetric factors:

$$V_0=\prod_{s=1}^{Q}\Pi_s,\qquad W_0=\sum_{s=1}^{Q}P_-^{(s)},\qquad V_0=(-1)^{W_0},\qquad M_0=V_0\,f(W_0)$$

Here $f$ interpolates $(-1)^j$ on a window. This step is inside the proof (§4.2).

- **Coincidence.** At r = 2, Πₛ equals the one-bit crossing entry by entry. The same binomial multiplicities also enter two different counts:

$$\operatorname{rank}_{\text{rows}}(A_i)=\sum_{j\ge t-i}\binom{t}{j}3^{\,t-j},\qquad c=\sum_{j\notin I}\binom{Q}{j}\left(\tfrac{r(r-1)}{2}\right)^{j}\left(\tfrac{r(r+1)}{2}\right)^{Q-j}$$

On the left is an upper tail giving the row ranks of the one-bit pieces. On the right is the complement of OpenAI's interpolation window, which can include both a lower and an upper tail; $c$ counts rows in the explicit measurement matrix constructed in the preprint, not a proved minimum. With t = 4, i = 2, r = 2, Q = 4 and I = {0, 1}, both counts equal 67. [`verificar_pieza_compartida.py`](verificar_pieza_compartida.py) checks this small instance. This is a comparison between the two external papers made by the program, not an antecedent. The [proof note](PROOF_NOTE_3_3_EN.md) proves the formulas for every t and Q in their respective settings; the value 67 only illustrates them and is not, on its own, evidence of a common mechanism.

### 3.4 The program's reflections versus the swap — type B

The program's binary reflection, ρᵢ(x) = x ⊕ eᵢ, is not the same operator as the swap. Flipping a bit acts as X on one coordinate; on two bits its trace is 0 and the swap's is 2, and their antisymmetric projectors have rank 2 and 1. No isomorphism carries one to the other.

What does correspond are the mirror-cube reflections that exchange two coordinates, across the planes xᵢ = xⱼ. They belong to the symmetry group of the tetrahedron, S₄, and on the cube's vertices they are exactly the swap of two bits. The program treats that group in the mirror-cube documents published on October 24 (O21), but we found no place where it identifies those reflections with the swap of two bits. It is a type B analogy: the same operator plays another role, symmetry of the tetrahedron rather than cost reduction. The involution H = 2P − I of October 9 is a different reflection, through the uniform vector.

### 3.5 Measurements of the November 3 package — type A, classical theorems

- **Two cuts.** S = I − 2P₋ lowers the crossing to log₂ 12 ≈ 3.585 bits per block (ρ ≈ 0.896); the split by sign never drops below that value.
- **Tetrahedron.** The four crossings occupy the even class {000, 011, 101, 110} of the correlation cube; each is the central reflection of a Bell state.
- **Doubling.** Cayley–Dickson gives R + C = 2·crossing at 2, 4 and 8; under Lemma 2's count only the 8 gains (11 of 12 bits), and that requires losing associativity.

These are classical theorems stated in the program's language; five verifiers reproduce them ([November 3 delivery](../../2026-11-03_cruce_reflejo_central/READ_FIRST.en.md)), and the values are in its `referencia_resultados/*.json` files.

## 4. Hypotheses and refutation criteria

Each hypothesis states what would prove it, what would refute it and where it stands. H1 and H2 are close to confirmed, but as known mathematics; H3 is the one that would decide whether the framework explains.

| Hypothesis | Expected proof | Refutation | Status |
| --- | --- | --- | --- |
| **H1, contraction.** The program's reclosure and counting are factor contractions, in the Boolean and counting semirings | Explicit identity in standard notation (3.1 and 3.2) | A closure operation of the program that is not a contraction, or is one only by rewriting definitions (type C) | Identities given; classical, no novelty |
| **H2, operator.** The pair swap is the same local operator in both algorithms and in the transposition reflections of the program's cube, with a different role in each | Entry-by-entry equality and a comparison of its role in each construction | A differing entry, or a program operator that is not a transposition, such as ρᵢ(x) = x ⊕ eᵢ (3.4) | Equality verified (3.3); the role differs in each case (3.4) |
| **H3, explanatory power.** The framework derives a bound or an exponent ρ without postulating it, for example ρ < 11/12 or 1/√2 | Step-by-step derivation from the program's principles | The bound or the doubling enters as an additional condition | Open; no derivation today |
| **H4, historical dependence.** There was dependence between groups | Independent external evidence | — | Out of scope |
| **H5, related binomial counts.** The related sums of antisymmetric-factor multiplicities that count the one-bit ranks and OpenAI's chosen measurement rows have consequences for either bound | The formulas, already proved in the [proof note](PROOF_NOTE_3_3_EN.md), plus an argument that this relationship enters one of the bounds | The shared weights arise only from using the same involution, with no effect on the bounds | Formulas proved for every t and Q in their respective settings; their role in the bounds is open |

## 5. Known mathematics versus possible contribution

Almost all of the mathematics is known. What may be a contribution is the measurement and the observation about the two papers, and that is what we ask reviewers to judge.

| Element | Status |
| --- | --- |
| Factor contraction and sum of products over the frontier | Known mathematics |
| Antisymmetric projector of an involution, S = I − 2P₋ | Known mathematics |
| Doubling by reflection (Cayley–Dickson) and the eight-square identity (Hurwitz) | Known; the program takes it as a postulate |
| The pair swap as a piece shared by the two algorithms | Observation about two external papers; whether it has been noted is to be assessed (Q5) |
| Related binomial counts for one-bit ranks and OpenAI's chosen measurement rows | Proved in the proof note; their relevance is to be assessed (H5) |
| Explicit finite-t rank formulas for the one-bit split | Derived here from the one- and three-dimensional eigenspaces already described in Anthropic's Appendix H; any novelty remains to be assessed |
| Architecture reference → closure → interface → reclosure | Conceptual reorganization; novelty to be assessed |
| AI-assisted intuition-and-language methodology | Epistemological, not mathematical |
| Derivation of complexity bounds from the framework | Open (H3) |

## 6. Reproducible material and formalization status

Everything marked as measured is regenerated by Python verifiers; these are numerical checks, not formal proofs, and nothing is formalized in Lean or Coq.

| Type | What it includes | Status |
| --- | --- | --- |
| Computational verifiers | The five of the November 3 package and `verificar_pieza_compartida.py` (Section 3.3) | Run on Nov 3: they match the reference in about 37 s (Python 3.13.18, numpy 2.5.3). DeepSeek repeated the five on Windows. The output of `verificar_pieza_compartida.py` and its environment are in `salida_verificador_2026-11-03.txt` |
| Proofs in prose | Propositions 1 to 3 and Corollary 4 of the November 3 paper; identities of 3.1 and 3.2; [proof note](PROOF_NOTE_3_3_EN.md) for 3.3 | DeepSeek re-derived those of the paper; this is an AI review, not a human one. The note for 3.3 has no external review |
| Formalization in Lean or Coq | — | None in the program's three repositories |

**Rerun the measurements.**

```bash
git clone https://github.com/EndlessMonkeyProyect/programa-geometria-relacional
cd programa-geometria-relacional
git checkout --detach 46e47274e9e573b9c91da1516d067c4f49c289f9
cd 2026-11-03_cruce_reflejo_central
python3 -m pip install -r requirements.txt   # numpy>=1.24
bash reproducir_todo.sh            # regenerates and compares all results
cd ../review_requests/2026-11-03_intercambio_par_eth
python3 verificar_pieza_compartida.py   # Section 3.3, under a second
```

The fixed commit corresponds to tag `2026-11-03-pair-swap-review`, avoiding future changes to `main`. The full block requires Bash and `python3` on `PATH`, because `reproducir_todo.sh` calls it internally. On Windows, Git Bash can be used with that command configured. To run only the Section 3.3 verifier with PowerShell, see the [package guide](README.md). Dependencies retain their declared range; this is not a frozen environment. Source versions: OpenAI, commit `42907c9e999cc00d6abe7a50bfc1023250edd1b9`, and Anthropic, commit `16a5ce41304fcdaea4e0be7c132e1c361dc26da5`.

**Links.**

- Mathematical core: [Relational-Geometry-program](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program)
- Ontological model: [relational-geometry-Model](https://github.com/EndlessMonkeyProyect/relational-geometry-Model)
- November 3 package: [folder](../../2026-11-03_cruce_reflejo_central/READ_FIRST.en.md), [release 2026-11-03](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/releases/tag/2026-11-03), [DOI 10.5281/zenodo.23932854](https://doi.org/10.5281/zenodo.23932854)
- DeepSeek's review: [review_requests/2026-11-03_cruce_reflejo_central](../2026-11-03_cruce_reflejo_central/README.md)

## 7. Conclusion

Commit metadata is consistent with, but does not establish, public availability of the interface composition, the core of the reclosure, MF-85 and the v3 review before October 16. Independent timestamps for the relevant content are still needed. In addition, measured afterwards, there is one exact local coincidence between the two algorithms: the pair swap. Related sums of its binomial multiplicities count the one-bit ranks and the rows of OpenAI's explicit measurement matrix.

It does not establish that the program discovered the algorithms, that there was influence between groups, or that the correspondences imply the same mechanism. The distance between correspondence and equivalence is precisely what this review is about. We welcome correspondences, contradictions or more precise formulations, above all on H2, H3 and H5, as [issues in this repository](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/4).

## Annex — Motivation of the program

The program grew out of a personal conviction: that behind the multiplicity we inhabit there is an order recognizable through its relations. That conviction is not presented as a theorem or a mathematical result; it is declared here as motivation, separate from the testable hypotheses of Sections 3 and 4. The work developed as a dialogue between human intuition and AI systems, and this is documented as method, not as validation.

**Use of AI.** This document was prepared with assistance from Claude (Anthropic) and DeepSeek. One of the assistants comes from the same company as one of the algorithms analyzed. The questions, the framework and the decisions on scope are the author's.

## References

- Claude (Anthropic). [A 2^o(n) Time Algorithm for 3-SAT](https://github.com/anthropics/formal-math/blob/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/eth/paper.pdf). October 26, 2026, commit `16a5ce4`.
- OpenAI. [The Exponential Time Hypothesis is False](https://github.com/openai/math/blob/42907c9e999cc00d6abe7a50bfc1023250edd1b9/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf). October 17, 2026, revised October 25.
- Relational Geometry Program. MF-61B and MF-62B, September 29, 2026 (`fb27fbf`); MF-63B, accredited compatibility reclosure, October 3, 2026 (`c44cfb8`; full in `0fd5315`); v3.0.0-review, October 9, 2026 (`6e36993`).
- Le Matt Ansatz Di Ego. The Cross as Central Reflection. November 3, 2026. [DOI 10.5281/zenodo.23932854](https://doi.org/10.5281/zenodo.23932854).
- Endless-monkey. [P vs NP and Yang–Mills: Two Problems, One Structural Question](https://www.reddit.com/user/Endless-monkey/comments/1wwk0xh/p_vs_np_and_yangmills_two_problems_one_structural/). Reddit, October 3, 2026.
- Endless-monkey. [We Are No Infinite Monkeys](https://www.reddit.com/r/epistemology/comments/1x1fls2/we_are_no_infinite_monkeys/). Reddit, r/epistemology; date to be verified.
- Davis and Putnam. A computing procedure for quantification theory. *Journal of the ACM* 7 (1960).
- Dechter. Bucket elimination: a unifying framework for reasoning. *Artificial Intelligence* 113 (1999).
- Hurwitz (1898): sums of squares with bilinear composition exist only in dimensions 1, 2, 4 and 8.
