# Corrections and open issues

## Historical corrections already recorded

| ID | Correction | Source and scope |
|---|---|---|
| H01 | The threshold counter is capped according to what the remaining future can distinguish. | MF-54 and VALIDATION v0.62.1. |
| H02 | The double-closure sign is fixed at −1 under the metric postulates. | MF-57; consolidated invariance proof in v0.84. |
| H03 | The former identity U = V + m with m perpendicular to V is incompatible with the stated iteration. | MF-57 and v0.84. The scalar partition is retained separately. |
| H04 | Iterating a single axis does not generate directions indefinitely. | MF-57 and v0.84. |
| H05 | Functional dependence does not guarantee exchange or a basis of unique size. | MF-58 and v0.73. |
| H06 | Monotonicity, confluence, or four local states do not imply polynomial time. | MF-59B–62B and v0.73–80. |
| H07 | Four-state phase order does not imply four independent bits. | v0.81–86 and v0.90. |

## Observations from this editorial review

These observations do not replace the originals and are not attributed to the author without review.

### E01. A residue that cannot leave the subspace

In v0.91, §§4–6, if x_i and x_j belong to L and T_ij preserves L, then x_j − T_ij x_i belongs to L, and (I − P_L) annihilates it.

**Required repair:** specify the joint space and the operation that contains information not representable by the prior interface. MF-61B provides an exact semantic reference, not an automatic vector identification.

### E02. Parallel axis and seed

V0.91 takes R = q/||q|| and then uses q as the seed of J. If J is the product associated with R, then q × R = 0. The v0.84 theorem applies only when q is perpendicular to R.

**Required repair:** define a different axis or a new J and justify it. If J is abstract, state the additional structure.

### E03. Orbital and linear novelty are different

An intermediate phase is outside the four-state orbit but inside its plane. Nonfactorization, membership in an orbit, and a component outside a subspace are different tests.

**Required repair:** state a bridge theorem with explicit representations and observables.

### E04. Mixed state and uniform vector

V0.86, §9, incorrectly equates a uniform superposition with I/D. They agree on probabilities in the chosen basis, but not on all projectors. A vector in the same space is not a purification of I/D.

**Required repair:** restrict equivalence to diagonal observables or use a purification in a larger space. This does not affect the mixed-state invariance theorem.

### E05. Holonomy and exact differences

In v0.72, differences of global phases sum to zero around cycles. In v0.91, universally requiring path-independent composition with compatible identities and inverses rules out nontrivial holonomy.

**Required repair:** distinguish a connection on edges from exact differences; do not identify a direct link with every composed transport.

### E06. Enlargement when moving from nodes to relations

The gradients B_1^T x are orthogonal to cycles in ker B_1. A general harmonic flow need not arise from those gradients. V0.77–89 allow general cochains, but the integration must state that enlargement.

### E07. Two uses of 1:3 and the Clifford choice

Counting three distinct roles of a reference in C4 is not the same construction as the three nonscalar channels of the two-projective-role book. Clifford completion of independent roles is an additional choice, not a consequence of support independence.

### E08. Nonempty domains and amplitudes

Logarithmic cardinality measures require nonempty sets. The closure T of an empty contract is not the state ⊥. A real amplitude r sqrt(1−r²) requires 0≤r≤1.

### E09. Trivial channel

The intertwining equation admits the zero map. To infer an operational channel, additional appropriate properties are needed, such as nontriviality and observables it actually transports.

## Prioritized open issues

| ID | Question | Evidence needed to close it |
|---|---|---|
| P01 | What data of a joint relation constitute the new reference? | Construct an interface and prove its sufficiency for the stated futures. |
| P02 | How does contextual novelty translate into geometric residue? | Explicit maps and proof of which distinctions they preserve. |
| P03 | What determines J at the new level? | An operator constructed from composition; domain, metric, and proof that J² = −I. |
| P04 | How are different generators related? | Derived laws or clearly stated and tested postulates. |
| P05 | When does composite closure persist? | Joint dynamics and a stability criterion; separate state stability from operator robustness. |
| P06 | What selects events and active relations? | A rule independent of knowing the desired outcome. |
| P07 | How are scales connected with physical observables? | Units, measurements, and predictions without circular calibration. |
| P08 | Is there a general computational consequence? | A complete accuracy contract and worst-case costs. |

## Next concrete test

Use two small closures with a shared boundary. Construct their relation by union and projection. Identify a comparison that does not factor through the previous summary. Then propose its geometric realization and assess whether a new J can be derived or must be adopted as a postulate.

A negative result must be acceptable: contextual composition could work without requiring any new C4 orbit. A good example should not build the four into its definition and then announce it as a result.

## Traceability

See the [results](RESULTADOS.en.md), [lineage](LINAJE.en.md), [MF-57](../../fuentes/originales/MF57_GENERATOR_AUDIT_AND_NEW_REFERENCE_RULE.md), [MF-61B](../../fuentes/originales/MF61B_COORDINATION_AND_SHARED_BOUNDARY.md), and [v0.91](../../fuentes/originales/COMPOSICION_RECURSIVA_CAPSULAS_v0_91.md).
