# 6. Inheritance and geometric composition of capsules

## What is established

The direct sum preserves the previous layer. If \(J_{k+1}=J_k\oplus J_N\) is constructed with a suitable J_N, its restriction to the inherited sector retains its law. The intertwining equation is

\[
J_{k+1}i_k=i_kJ_k.
\]

This does not derive the choice of J_N from relational information.

For a general idempotent closure C, preserving fixed points also requires \(C_{k+1}i_k=i_kC_k\). An interaction may fail to satisfy this compatibility and may reconfigure the closure.

## The v0.91 proposal

The source proposes:

\[
d_{ij}=x_j-T_{ij}x_i,\qquad q_{ij}=(I-P_k)d_{ij},
\]

and, if q is nonzero, a new capsule \(\{q,Jq,-q,-Jq\}\).

Operational definitions are needed for the interface S_k, transport T_ij, the comparison space, the projected subspace, and the new J. Writing the names of those maps does not demonstrate that they exist with all the required properties.

## Two integration obstacles — editorial review

**Zero residual under linear closure.** If both interfaces lie in L_k and the transport preserves L_k, their difference also lies there; then q = 0. A broader joint representation, a different operation, or a justification for transport that introduces outside information is needed.

**Axis and seed.** If R = q/||q|| and \(J_R(v)=v\times R/\|R\|\) is reused, q is parallel to the axis, lies outside the transverse sector, and \(q\times R=0\). Generating the orbit of q requires specifying another operator or a different axis. Adopting an abstract J is possible as an assumption; it is not equivalent to deriving J through that formula.

## What construction is missing

1. Give two closures and their interfaces with a sufficiency contract.
2. Construct joint compatibility, using MF-56 or MF-61B.
3. Identify novelty through non-factorization.
4. Define a geometric realization that preserves those distinctions.
5. Construct J for the new level and prove its domain, metric compatibility, and square.
6. Verify stability under the chosen dynamics and recovery of inherited information.

This is a proof program, not a proof completed by this edition.

## Caution about self-similarity

Preserving order four in existing sectors is not equivalent to proving that every composition has order four. Self-recurrence can be stated as a structural principle. Deriving it requires a law for relations between generators, the matter left open in MF-57.

## Sources

- [Inheritance v0.87](../../fuentes/originales/AUTORRECURRENCIA_CAPAS_HERENCIA_v0_87.md).
- [Composition v0.91](../../fuentes/originales/COMPOSICION_RECURSIVA_CAPSULAS_v0_91.md).
- [Audit v0.91](../../fuentes/originales/AUDITORIA_v0_91.md).
- [MF-57, §§9–15](../../fuentes/originales/MF57_GENERATOR_AUDIT_AND_NEW_REFERENCE_RULE.md).

Next: [dynamics and stability](07_dinamica_estabilidad.en.md).
