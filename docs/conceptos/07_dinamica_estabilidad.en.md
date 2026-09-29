# 7. Dynamics, stability, and holonomy

## Economy and motion

A quotient of maximal economy preserves the stated responses and removes irrelevant distinctions. It is idempotent. It does not determine a unique gradual trajectory: several mergers can preserve exactly the same invariants.

Version 0.74 introduces accessibility and proves confluence for contractions of edges that are already closable in a fixed graph. The process that makes an initially positive difference decrease remains separate.

## Variational dynamics

With fixed linear comparisons \(\partial:X\to Y\), pattern b, and defect

\[
D(x)=\tfrac12\|\partial x-b\|^2,
\]

adopting gradient descent with \(\kappa>0\) gives

\[
\dot x=-\kappa\partial^\ast(\partial x-b).
\]

On states, the operator is \(\Gamma_X=\kappa\partial^\ast\partial\); on residuals q = ∂x − b, with constant b, it is \(\Gamma_Y=\kappa\partial\partial^\ast\). These operators act on different spaces.

The descent principle, metric, and architecture are hypotheses of the realization. The term “economy” does not determine them by itself.

## Persistence

A module M invariant under U has exact resonant closure if \(U^p|_M=I\). In finite dimension, that return implies bounded powers on M. A frequency of unit modulus alone is insufficient: a Jordan block can grow.

Stability with respect to a fixed U does not prove robustness under changes in U or external couplings. Version 0.76 correctly distinguishes these regimes.

## Hodge

For an explicit complex with \(B_1B_2=0\),

\[
\Delta_1=B_1^\top B_1+B_2B_2^\top.
\]

Harmonic modes satisfy \(B_1h=0\) and \(B_2^\top h=0\). The combined dynamics of v0.77 is precise if the internal rotation and Hodge act on different factors:

\[
\dot a=(\omega I\otimes J-\gamma\Delta_1\otimes I)a.
\]

For each eigenmode with eigenvalue λ, the norm has decay factor \(e^{-\gamma\lambda s}\). λ = 0 protects the mode in this architecture; it does not identify the mode with a particle.

A triangle without a face has a harmonic cycle. Adding the face can eliminate it. A rule is needed to determine when that relation is added.

## Phase and holonomy — editorial review

If \(\Delta_{ij}=\theta_i-\theta_j\) for globally assigned phases, the sum around a cycle is zero modulo 2π. An independent connection on edges can have nontrivial holonomy; merely relabeling exact differences is insufficient.

Likewise, imposing \(g_{ik}=g_{jk}g_{ij}\) for all pairs and paths, with compatible identities and inverses, forces path-independent transport. To study holonomy, transport composed along a path is distinguished from the direct link, without identifying them universally.

Another limit: a flow h on a cycle does not necessarily arise from differences of nodal values. Gradients \(B_1^\top x\) are orthogonal to \(\ker B_1\). Moving from nodal variables to general cochains enlarges the space; that move must be stated.

## Sources

- [v0.74](../../fuentes/originales/ECONOMY_IDENTITY_LOCAL_REDUCTION_v0_74.md).
- [v0.75](../../fuentes/originales/PHASE_SYNCHRONIZATION_DYNAMICS_v0_75.md).
- [v0.76](../../fuentes/originales/RESONANT_MODULES_STABLE_CLOSURE_v0_76.md).
- [v0.77](../../fuentes/originales/DERIVED_OPERATOR_HODGE_HARMONICS_v0_77.md).
- [v0.89](../../fuentes/originales/GAMMA_DESDE_ARQUITECTURA_v0_89.md).

Next: [bits, weights, and scales](08_bits_pesos_escalas.en.md).
