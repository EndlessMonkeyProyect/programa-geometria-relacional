# 2. Sufficient boundary, identity, and closure

## Concept

A boundary preserves the differences that can still modify admissible responses. A closure organizes interior and interface; it does not amount to immobility.

If a summary \(s:X\to S\) allows every response Q to be reconstructed, then

\[
s(x)=s(y)\Rightarrow x\sim_C y.
\]

It therefore needs at least as many labels as there are contextual classes. The quotient attains this bound: for that contract, it is the minimum exact deterministic summary by number of states.

This semantic minimality does not claim that the quotient is cheap to compute or that it minimizes every storage format.

## Identity and interior

The closure can operate through a small interface while its context remains in the layer that supports it. Version 0.87 represents inheritance by an inclusion with recovery:

\[
i_k:L_k\hookrightarrow L_{k+1},\qquad p_ki_k=I.
\]

If \(L_{k+1}=L_k\oplus N_{k+1}\), projection onto the first summand recovers the previous layer. This preserves represented information; it does not prove that every physical history is stored in an isolated identity.

## Relative sufficiency

In the threshold example, a future question is \(Q(p,s)=1[|p|+|s|\le k]\). If r future bits remain, the minimum summary of a prefix p is

\[
\theta(p)=\operatorname{clip}(k-|p|,-1,r).
\]

Distinct counts may be equivalent because no available future distinguishes them. MF-54 corrected a counter that was sufficient but not always minimal.

If the context expands, the old interface may cease to suffice. Retaining the interior may allow the interface to be recomputed; using only the earlier summary does not guarantee recovery of distinctions already omitted.

## Certifiable closure

MF-60B adds a witness of sufficiency: state and certificate. The existence of a certificate, its verification, its generation, and its updating must be distinguished. None of these operations becomes efficient merely by defining a quotient.

## Sources

- [MF-54, §§8–14](../../fuentes/originales/MF54_LOCAL_INFORMATION_REFLECTION_AND_BOUNDARY_STATE.md).
- [Certifiable closure](../../fuentes/originales/ACCREDITABLE_CLOSURE_ES.md).
- [MF-60B](../../fuentes/originales/MF60B_COMPOSABLE_LOCAL_CERTIFICATES.md).
- [Inheritance v0.87](../../fuentes/originales/AUTORRECURRENCIA_CAPAS_HERENCIA_v0_87.md).

Next: [novelty and resolution](03_novedad_resolucion.en.md).
