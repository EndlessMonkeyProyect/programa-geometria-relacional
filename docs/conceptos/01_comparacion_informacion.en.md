# 1. Comparison and local information

## Concept

A difference acquires content for a framework if at least one comparison admits different responses. Information is contextual: it is not assigned here as an absolute quantity to an isolated thing.

For a nonempty set X, a family of comparisons C, and responses Q, we define

\[
x\sim_C y\iff Q(x,c)=Q(y,c)\quad\forall c\in C.
\]

The complete signature is \(\mathfrak R_C(x)=(Q(x,c))_{c\in C}\). The quotient \(K_C=X/{\sim_C}\) collects the classes distinguished by that language. In the finite case,

\[
I_{\rm dist}(X\mid C)=\log_2|K_C|.
\]

This measures the cardinality of the classes; it is not Shannon entropy unless a distribution is added and the identification is justified.

## Result

If C is contained in C', the second context refines the partition. It may separate realizations that were previously indistinguishable; it does not merge those already separated. Therefore \(I_{\rm dist}(X\mid C')\ge I_{\rm dist}(X\mid C)\).

With empty C and nonempty X there is a single class. This does not imply that the interior lacks structure. It means only that the contract does not distinguish its realizations.

## Example

In X = {00,01,10,11}, observing the first bit produces two classes. Observing both produces four. Observing only parity again produces two, but they are different classes. The number of classes alone does not determine the content of the comparisons.

## Uncertainty and distinguishability

Hartley uncertainty within a finite capsule C is \(U_H(C)=\log_2|C|\). The distinguishability of the set of classes is \(\log_2|K|\). Enriching the questions can increase the latter and decrease the sizes of the classes. These two quantities must not be interchanged just because both use a logarithm.

## Sources

- [MF-54, §§2–9](../../fuentes/originales/MF54_LOCAL_INFORMATION_REFLECTION_AND_BOUNDARY_STATE.md).
- [Language as reflection](../../fuentes/originales/LANGUAGE_AS_REFLECTION_LOCAL_INFORMATION_ES.md).
- [Core v0.78, §§II–III](../../fuentes/originales/NUCLEO_INTEGRADO_v0_78.md).

Next: [boundary and closure](02_frontera_cierre.en.md).
