# 5. Reflection, geometry, and the four-state orbit

## The local realization

Version 0.84 starts with a real space with a positive inner product, a nonzero reference R, and an antisymmetric bilinear operation. For A perpendicular to R, it requires norm compatibility, transversality, and double closure. It does not start from contextual distinguishability alone.

With \(r=\|R\|\), \(T_R(A)=A\times R\), and \(E_R=R^\perp\), antisymmetry and double closure allow one to prove that E_R is invariant. On E_R,

\[
J_R=T_R/r,\quad J_R^\ast=-J_R,\quad J_R^\ast J_R=I,
\quad J_R^2=-I.
\]

Thus the positive-sign branch of double closure is excluded. For nonzero A:

\[
A,\ J_RA,\ -A,\ -J_RA,\ A.
\]

There are four different states and a fifth occurrence that returns to the first.

## What four means

It is the order of the discrete orbit of that seed. The real plane spanned by A and JA has dimension two and contains infinitely many vectors. It has not been shown that the plane can contain only four arbitrary identities.

An additional phase can lie outside the discrete orbit while remaining in the same plane. For example, \((A+JA)/\sqrt2\). That parameter novelty is not a new linear direction.

J² = −I without metric compatibility also does not imply perpendicularity with respect to a previously fixed metric. The program's proof uses its additional hypotheses; those must accompany any citation of the result.

## Historical correction

MF-57 and v0.84 show that iterating the same axis produces

\[
V=-r^2A,\qquad a=-r^2U.
\]

It does not generate independent directions indefinitely. It is also inconsistent to assert simultaneously V = T_R U, U = V + m, and m perpendicular to V for the nontrivial normalized seed.

The amplitude identity \(\mu^2=r^2(1-r^2)\) can be retained as a separate partition, with \(0\le r\le1\) for a real amplitude. It does not reconstruct the former vector identity.

## Novelty in a geometric module

If W is J-invariant, J is orthogonal, and y belongs to the ambient space already equipped with J, the residual \(r_y=(I-P_W)y\ne0\) generates the minimum J-invariant extension

\[
W'=W\oplus\operatorname{span}_{\mathbb R}\{r_y,Jr_y\}.
\]

This proves how to incorporate a given novelty in that realization. It does not show how the interaction of two capsules produces y or how a new J is chosen if the ambient space does not already contain it.

## Sources

- [MF-57](../../fuentes/originales/MF57_GENERATOR_AUDIT_AND_NEW_REFERENCE_RULE.md).
- [v0.84](../../fuentes/originales/CIERRE_ALGEBRAICO_MINIMO_v0_84.md).
- [v0.83](../../fuentes/originales/TEOREMA_ORBITAS_4_8_v0_83.md).
- [v0.90](../../fuentes/originales/REFLEXION_CIERRE_CUATRO_v0_90.md).

Next: [layers and geometric composition](06_capas_y_nuevo_operador.en.md).
