# 10. Computation, certification, and coordination

## What is sought

The computational branch asks whether a sufficient representation can be constructed and updated without enumerating all alternatives. Length, certification, updating, and decision must be measured separately.

That SAT/UNSAT is one bit does not bound the work required to obtain it. MF-59B directly shows that deciding whether a clause is redundant can contain the difficulty of UNSAT: a formula G over original variables implies a clause over three fresh variables if and only if G is unsatisfiable.

## Positive controls and their limits

Horn admits propagation; XOR, linear elimination; 2-SAT, implications and strongly connected components. These are known algorithms, and the sources use them as controls.

A mixture of sectors does not automatically inherit their tractability. MF-62B partitions exact three-literal clauses into Horn and dual-Horn; coordinating both sectors contains the general problem even though each sector has a trivial witness.

## Capsules of futures

In v0.79, two prefixes belong to the same capsule if they induce the same function over all continuations. For an order π:

\[
W_\pi(k)=|\{F_\alpha:\alpha\in\{0,1\}^k\}|.
\]

This counts residual functions, not an orbit of four phases.

In \(F_m=\bigwedge_i(x_i\leftrightarrow y_i)\), fixing all x variables before the y variables generates \(2^m\) distinct futures. Interleaving pairs keeps the width small. A poor representation can grow exponentially even for an easy family.

Organizing W leaves in a tree of arity four requires at least \(\lceil(W-1)/3\rceil\) internal nodes. Reducing depth does not guarantee a reduction in total size.

## Reference selector v0.80

\(\Gamma_0\) is an ordering heuristic based on incidences and the boundary. It is not the relaxation operator of v0.89.

The attached results report 24 small planted instances and seven controls. On the 24 instances, \(\Gamma_0\) attains the reported optimal width on 14. These are finite controls, with no asymptotic guarantee and no generator code included in this corpus. The laboratory optimum uses an exact search over subsets; it is not part of the selector.

## Contract for a consequence about P versus NP

A general solution requires, uniformly:
- an exact representation of polynomial size;
- polynomial construction and updating;
- certification of the necessary equivalences;
- a polynomial number of steps;
- a correct decision of emptiness and recovery of the answer.

The sources do not jointly satisfy that contract for all 3-SAT. Nor do they prove that no method can. Obstacles for a particular representation do not establish that P differs from NP.

## Sources

- [MF-59B](../../fuentes/originales/MF59B_3SAT_ACCREDITATION_BARRIER.md).
- [MF-60B](../../fuentes/originales/MF60B_COMPOSABLE_LOCAL_CERTIFICATES.md).
- [MF-61B](../../fuentes/originales/MF61B_COORDINATION_AND_SHARED_BOUNDARY.md).
- [v0.79](../../fuentes/originales/CAPSULE_SAT_EXPERIMENT_v0_79.md).
- [v0.80](../../fuentes/originales/GAMMA_REFERENCE_OPERATOR_v0_80.md).
- [Data guide](../../datos/README.en.md).

Continue with [results and dependencies](../trazabilidad/RESULTADOS.en.md).
