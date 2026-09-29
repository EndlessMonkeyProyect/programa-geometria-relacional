# 3. Novelty, resolution, and a new reference

## Two changes

Novelty expands the comparisons; resolution restricts realizations. Given an event e with comparisons D and restriction Y:

\[
X'=X\cap Y,\qquad C'=C\cup D,\qquad K'=X'/{\sim_{C'}}.
\]

The rule determines the state conditioned on the event. It does not determine which event occurs. If X' is empty, the result is contradiction \(\bot\); no logarithm of zero is calculated.

## Exact criterion

A new comparison c is redundant if a function on the previous closure reconstructs its response:

\[
Q_c=\bar Q_c\circ q_C.
\]

In finite nonempty systems, this is equivalent to c splitting no class. Novelty is

\[
\nu(c\mid C)=\log_2\frac{|K_{C+c}|}{|K_C|}.
\]

For a binary comparison, if N previous classes include s split classes, \(N'=N+s\); hence \(0\le\nu\le1\). One bit is the maximum opening capacity of that comparison, not a mandatory increase in every context.

## Full independence and partial novelty

MF-58 uses the image of the signature \(\Phi_C\). Support independence requires

\[
\operatorname{im}\Phi_{C+c}
=\operatorname{im}\Phi_C\times\operatorname{im}Q_c.
\]

This is stronger than non-factorization. It is not probabilistic independence without a distribution.

For s = 0011, x = 0101, and y = 0001:
- x adds one bit to s;
- y adds \(\log_2(3/2)\) bits to s;
- y is redundant once s and x are known, because y = s AND x.

Functional dependence does not generally satisfy the matroid exchange property. There is therefore no universal “linear basis” of comparisons.

## Scope of a new reference

Non-factorization requires enriching the description if one wants to answer the new question. It does not determine a unique geometric operator, a spatial direction, or the algebraic relation between two generators.

MF-57 expresses the extension as \(\mathcal A_{k+1}=\langle\mathcal A_k,R_{k+1}\rangle\), but leaves cross-relations between references open.

## Sources

- [MF-55](../../fuentes/originales/MF55_ONTOLOGICAL_TRANSITION_RULE.md).
- [MF-58](../../fuentes/originales/MF58_RELATIONAL_INDEPENDENCE_AND_RANK.md).
- [New difference, new reference](../../fuentes/originales/NEW_DIFFERENCE_NEW_REFERENCE_ES.md).
- [Independent difference and dimension](../../fuentes/originales/INDEPENDENT_DIFFERENCE_AND_DIMENSION_ES.md).

Next: [relations between closures](04_dependencia_composicion.en.md).
