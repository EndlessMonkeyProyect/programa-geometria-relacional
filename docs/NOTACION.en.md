# Notation and object types

This table suggests reading names to avoid collisions. It does not modify the originals.

| Historical symbol | Use | Recommended name when integrating |
|---|---|---|
| J in v0.73–74 | Invariant identity function. | \(\mathcal I\) |
| J or J_R from MF-57 onward | Transverse linear operator whose square is −I. | \(J_R\), with its domain specified |
| Γ in v0.80 | Heuristic selector of the next variable/reference. | \(\mathrm{Sel}_{\rm frontera}\) |
| Γ* in v0.81 | New coset in a binary affine extension. | \(\mathrm{Ext}_{\rm afin}\) |
| Γ in v0.82 and v0.87 | Idempotent closure operator. | \(\mathrm{Cl}_k\) |
| Γ in v0.89–91 | Positive relaxation operator. | \(\Gamma_X\) or \(\Gamma_Y\) |
| Γ_AB in MF-56 | Subset of allowed pairs. | \(\mathcal R_{AB}\) |
| C | Family of comparisons or constraint matrix, depending on the source. | \(\mathcal C\) for questions; ∂ for the operator |
| c | Individual comparison or physical constant/scale. | \(c_{\rm obs}\) or \(c_{\rm fis}\), according to domain |
| R | Reference vector, its magnitude, radius, or relation. | R for the vector; r = ||R||; subscripted radii |
| q_C | Quotient map to contextual classes. | \(\pi_C\) |
| q_ij in v0.91 | Projection residual of a difference between interfaces. | \(r^{\rm geom}_{ij}\) |
| q = Cx − b in v0.89 | Constraint defect. | \(q^{\rm restr}\in Y\) |
| ρ in v0.86 | Normalized positive state. | \(\rho_{\rm estado}\) |
| ρ in other branches | Resolution, scale, norm, or rhythm ratio. | Explicit type-specific subscript |
| V | Second application of the generator or historical modal channel. | \(V_{\rm iter}\), \(V_{\rm modal}\) |
| I | Linear identity or informational measure. | \(\mathrm{Id}\), \(I_{\rm dist}\) |
| k, s, t | Depth, step, or evolution parameter. | State whether these are indices or continuous variables |
| K | Contextual quotient, topological complex, or computational representation. | \(K_C\), \(\mathscr K_{\rm top}\), \(K_F\) |

## Two required type checks

**States and residuals:** ∂ maps X to Y; ∂*∂ acts on X and ∂∂* acts on Y. They must not be applied to the same vector without an explicit identification.

**Axis and seed:** J_R is proven on the space perpendicular to R. If the seed is parallel to the axis, the antisymmetric product annihilates it.

## Distinct extension operations

- Refining a partition adds distinctions.
- Adding a summand adds linear directions.
- Introducing a face in a complex changes topological relations.
- Adding a generator to an algebra requires its relations to be specified.
- Changing variable order can change the representation without changing the Boolean function.

These operations may model related aspects; sharing the name “new layer” does not imply that any two are equivalent.
