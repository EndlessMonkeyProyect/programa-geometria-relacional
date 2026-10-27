# Beyond Yang–Mills: a relational framework for its emergence

**Author:** Le Matt Ansatz Di Ego (Relational Geometry Program)\
**Date:** October 27, 2026\
**Status:** draft for review. It is not a solution of the Clay Mathematics Institute mass gap problem, nor does it claim to be one.\
**Language:** English translation of *Más allá de Yang–Mills: un marco relacional de su emergencia*. The Spanish text is the reference version.

## Abstract

The Clay Institute Yang–Mills problem takes the theory as given and asks for a proof of the mass gap. This work asks a prior question: why that theory? We propose a framework in which Yang–Mills emerges from four relational principles: relations are transports between nodes; no local reference is privileged; independent things multiply; and each minimal closure is weighted by a local defect that is never negative and vanishes when the closure is perfect. We show that these principles generate a family of local gauge actions. If, in addition, the defect has a positive, non-degenerate quadratic term near the identity (an additional hypothesis), its classical limit for smooth fields has the Yang–Mills form. The Wilson action is the natural, standard particular choice, not the only one, and we verify numerically its classical limit, that of another choice, and that of a counterexample. We further show that the program's incompatibility observable, ν = 1 − ½ tr(UVU⁻¹V⁻¹), is the plaquette defect for constant transports. The full family of ν comparisons singles out the center of the algebra u(2) = su(2) ⊕ u(1): three references that compose without commuting, and one common phase. We state explicitly what the framework does not explain: the mass gap, the mechanism that gives mass to three electroweak modes, the physical identity of the photon, the value of the Weinberg angle, and the direction of the change of scale. All results come with reproducible scripts.

## 1. Motivation

Physics describes with enormous precision which gauge theories govern nature, but it rarely asks why those and not others. The Relational Geometry Program starts from an ontology in which what is primary are relations and their closure, not objects. If that ontology is fertile, it should be able to explain the form of known theories, not just reinterpret them. This article puts that capacity to the test with Yang–Mills.

We state the scope from the outset: explaining the emergence of a theory is not the same as solving it. The mass gap remains an open problem, and nothing that follows proves it.

## 2. Four relational principles

1. **Relations are transports between nodes.** Each relation is represented by a group element assigned to a link.
2. **No local reference is privileged.** The weight of a configuration can depend only on closed loops (gauge invariance), and each relation is weighted with the uniform measure of the group (Haar measure), the only one that favors no reference.
3. **Independent things multiply.** Novelty acts as a multiplicative factor; the weights of independent closures multiply, so the total weight is the exponential of a sum of local terms.
4. **The minimal closure is weighted by its defect.** The local term is a closure defect of the plaquette, d(U), which is never negative (nothing is compared negatively), is invariant under conjugation, and vanishes at the identity (a perfect closure carries no weight). Conjugation invariance is required by principle 2: changing the reference of the node from which the loop is traversed conjugates the plaquette.

## 3. Result 1: the principles generate a family of actions; with the quadratic condition, of Yang–Mills class

The four principles give a family of weights, one for each admissible defect:

dμ = Π dHaar · exp(−β Σ d(U\_plaquette)).

**Quadratic condition.** Recovering the classical Yang–Mills form requires one more condition, which does not follow from the principles: near the identity the defect must have a positive, non-degenerate quadratic term, d(e^{iεX}) = κε²|x|² + O(ε³) with κ > 0 for X = x·σ/2, together with symmetry, locality, and a normalization that fixes κ relative to β. In SU(2), conjugation invariance forces that term to be the same in the three directions of the algebra (Schur's lemma), so κ only fixes the normalization of the coupling. With this, for smooth fields, the sum of defects tends to 8κ times (a⁴/8) Σ F².

**The Wilson choice.** d\_W(U) = 1 − ½ Re tr U, with κ = 1/8, is the natural, standard particular choice, but not the only one. Checks: a random change of all local references leaves the action identical; all defects lie between 0 and 2; and for a smooth field the ratio between the sum of defects and (a⁴/8) Σ F² tends to 1 (0.988; 0.997; 0.9993; 0.9998 for lattices from 16 to 128).

**Another choice and a counterexample.** The Manton action, d = θ²/8 with θ the rotation angle of U, has the same quadratic term and the same limit (0.989 → 0.9998). By contrast, d(U) = [1 − ½ Re tr U]² is non-negative, invariant, and vanishes only at the identity, but starts at fourth order. It does not reproduce the classical quadratic term: its ratio tends to zero as a⁴ (1.4·10⁻³ → 3.4·10⁻⁷).

**Scope.** The principles do not determine the action: they define a family, and Wilson is one choice within it. The quadratic condition is an additional hypothesis, and the counterexample shows that it is needed. The continuum-limit checks are classical, for smooth fields: they prove neither universality nor the existence of the quantum theory. That the coefficient 22/3 of the SU(2) beta function is common to the whole family is a universality result of quantum field theory, not of the program.

## 4. Result 2: ν is the defect of the minimal closure

When the transports do not vary from point to point, the plaquette coincides with the commutator UVU⁻¹V⁻¹, and its Wilson defect is exactly ν(U,V). Verified on 2000 pairs with zero error. With another choice in the family, the defect of the commutator is a function of ν, because in SU(2) every conjugation-invariant function depends only on the trace. Thus ν is the form of the general dynamical defect in the case of constant transports, and the full dynamical object is the plaquette defect.

## 5. Result 3: three references and one common phase

If relations are general 2×2 unitary transports (a quaternion plus a phase), the group is U(2), and the decomposition of its algebra, u(2) = su(2) ⊕ u(1), is exact and coincides with that of the electroweak sector. We write the generators as X = (cI + x·σ)/2 and Y = (dI + y·σ)/2. Then:

- ν is exactly insensitive to the phase: ν(e^{iφ}U, e^{iψ}V) = ν(U,V).
- For small transports, ν(e^{iεX}, e^{iεY}) = ε⁴|x×y|²/8 + O(ε⁶): it depends only on the su(2) parts.
- A single comparison does not single out the center: two aligned non-central transports (y parallel to x) give ν = 0. What singles it out is the full family of comparisons: a direction is invisible to all of them if and only if its component x vanishes, that is, if it is central, because the only directions that commute with all others are the central ones.

Verified numerically: the expansion, with remainder of order ε⁶, and the control, in which two aligned non-central transports give ν = 0 exactly and two non-aligned ones give 0.2331.

In the language of the program: a particle has three references by which to orient itself, three spaces of comparison that, once disentangled, stand at 90 degrees to one another (the i, j, k of the quaternion), and between any pair of them the order of comparison matters. The fourth component is not one more reference, but the common phase they share without distinguishing them.

**The program's reading (interpretation, not derivation).** The author identifies this common phase with time: the void being progressively covered, the moving mirror, the changing relation between the size of the universe and that of the particle. We note both the support for and the limit of this reading: in quantum mechanics time evolution acts as a phase, e^{−iEt}; but the u(1) phase is internal and is not the time of spacetime.

**Control.** A 3+1 obtained by counting four references in a graph is trivial: any connected graph with N nodes gives one null mode and N−1 positive ones, and its null mode is the uniform mixture, which never coincides with the photon. The 3+1 of this work, by contrast, lives in the space of generators and is not chosen by hand.

**Scope.** The 3+1 separation is algebraic. By itself it does not prove the electroweak mass mechanism, the physical identity of the photon, or the Weinberg angle. Moreover, in U(2) the invariant quadratic term of the defect has two independent constants, one for su(2) and one for u(1); the principles do not fix their ratio, which is what distinguishes the two couplings.

## 6. The Weinberg angle as a comparison

In the Standard Model, the photon is a mixture of the common phase and one of the three references. The fraction of its weight in the su(2) part is exactly sin²θ\_W = g′²/(g² + g′²): a comparison between the part of one coupling and the whole of the two. In SU(5) unification this fraction equals 3/8 at the unification scale and then runs with scale, because the inverse of each coupling acquires a term proportional to its logarithm. With the Standard Model content alone, this running does not reproduce the value measured at the Z boson scale (about 0.231); with supersymmetry the agreement improves.

In the framework, this fraction depends on the ratio between the two quadratic constants of the defect in U(2), which the principles leave free. The author proposes that the fraction is inherited from scale to scale and that, upon normalizing, the scale ends up in the denominator as a relation. This agrees in form with the known running. What the framework still has to show is quantitative: which inheritance coefficients correspond to the three references and to the common phase, and whether they reproduce the measured value without fitting, starting from an initial fraction fixed by the framework itself.

## 7. What the framework does not explain

- **The mass gap.** If the emergent dynamics is Yang–Mills, the gap is exactly the open problem. Complementary calculations in Ising models (packages PR-05 and PR-06, which reproduce known results) show that the language of closure supports real proofs where the tools exist, and that the missing piece for non-abelian gauge theory is a Simon–Lieb-type inequality.
- **The direction of scale.** In pure SU(2), non-abelian effects grow at large distances; they do not fade into U(1).
- **The mass mechanism.** In the Standard Model, three modes acquire mass through the Higgs field, observed at 125 GeV. The framework does not yet reproduce or replace it.
- **The physical identity of the photon.** The direction blind to ν is the u(1) center; that the observed photon is the mixture it is comes from the Standard Model.
- **The value of θ\_W.**
- **Why the group is U(2).** This requires checking whether the program's hypotheses PC1–PC5 force relations to carry a phase.

## 8. Falsifiers

1. If some action in the family with a positive, non-degenerate quadratic term had a smooth classical limit that is not of Yang–Mills form, the claim of Section 3 would fail.
2. If the program's relations did not carry a phase, there would be no common phase and the 3+1 separation would disappear.
3. Any 3+1 claim based only on counting references is empty.
4. If the proposed inheritance rule does not reproduce, without fitting, the measured value of sin²θ\_W at the Z scale (about 0.231), the reading of the mixing angle is refuted.

## 9. Conclusion

This work does not solve Yang–Mills. It proposes a framework for its emergence: the relational principles generate a family of gauge actions that, with the quadratic condition, is of Yang–Mills class, and the family of ν comparisons distinguishes in the electroweak algebra three references and one common phase.

The axis of the next stage of research is the gap, not the action, and the path already has its links. The table shows which are theorems and which are missing.

| Link | Statement | Status |
| --- | --- | --- |
| Criterion (PR-04) | The gap is uniform if and only if the logarithmic loss accumulated across scales is bounded | Exact identity |
| Boundary closure (PR-06) | If the correlation flux leaving through the boundary of a window is less than one, correlations decay exponentially | Theorem in Ising, with the Simon–Lieb lemma cited |
| From decay to gap (YM-R3B) | A common exponential decay of gauge-invariant correlators gives a spectral gap | Spectral theorem, already in the Yang–Mills branch; requires reflection positivity |
| Boundary inequality for gauge theory | A Simon–Lieb-type bound for gauge loops | Open. First natural case: Z₂, where the Griffiths inequalities hold; for SU(2) no analogue is known |
| Continuum | That the control holds uniformly in physical units as the lattice is removed | Open |

The next step is to formulate the boundary flux for Z₂ gauge theory, check whether it closes, and identify which part of the mechanism survives or fails when passing to SU(2).

## 10. Request for review

We request critical review in particular of: (a) the construction of the family of actions from the four principles and the role of the quadratic condition; (b) the proposition of the 3+1 separation by the family of ν comparisons; (c) the relevance of reading the common phase as time; and (d) the feasibility of an inheritance rule that fixes the mixing angle.

## Reproducible material

Everything stated here is regenerated by the packages of October 26 and 27, 2026, in the folder `2026-10-27_mas_alla_de_yang_mills` of the repository [github.com/EndlessMonkeyProyect/programa-geometria-relacional](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional). Each package includes a README, a verification script, results, and a SHA-256 manifest. The package documentation is in Spanish.

| Package | What it establishes | Status |
| --- | --- | --- |
| PR-01 | The residue of the unit vector is preserved if the projection respects duplication | Elementary theorem; says nothing about the gap |
| PR-02 | Where the gap lives under duplication: inherited versus new modes | Exact lemma; controls on graphs |
| PR-03 | Ising chain growing in volume: the gap survives interaction | Exact measurement; its summability argument is corrected in PR-04 |
| PR-04 | Correct criterion: logarithmic loss per scale; 2D Ising with and without gap | Structural measures do not decide the gap |
| PR-05 | Uniform gap of 2D Ising at high temperature: local resolution versus influence | Known theorem, reproduced; β < 0.3322 |
| PR-06 | Positive mass by closing windows: the correlation flux through the boundary | Theorem with one cited lemma; β < 0.4067 |
| PR-07 | From the principles to the family of actions, with Wilson as a particular choice; 3+1 separation by ν; controls | Supports Sections 3 to 6 |

## Main references

Wilson (1974); Osterwalder and Seiler (1978); Gross and Wilczek (1973); Politzer (1973); Georgi and Glashow (1974); Glashow (1961), Weinberg (1967), Salam (1968); Elitzur (1975); Simon (1980); Lieb (1980); Duminil-Copin and Tassion (2016); Bałaban (1980s); Fricke–Vogt and Procesi for the invariants of SU(2).
