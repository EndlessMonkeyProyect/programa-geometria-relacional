# 8. Bits, weights, and scales

## Four states and four roles

An orbit with four states requires two bits to identify a state. To obtain sixteen configurations, another construction is needed: recording the independent presence or absence of four roles, or an equivalent structure that justifies that repertoire.

Version 0.85 states the Boolean bridge: all subsets of n roles. Its cardinality is \(2^n\). The free space on roles distinguishes labels whose images can be linearly dependent in the geometric plane; this does not automatically add physical dimensions.

## Exterior and Clifford algebras

\(\Lambda^\bullet F_n\) has dimension \(2^n\). Version 0.86 uses the Clifford completion of a formal quadratic space with n generators. Choosing that space of roles, its quadratic form, and its relevance are additional conditions.

Support independence of observables does not by itself imply Clifford relations. MF-57 already warned against imposing cross-relations between generators without a derivation. The construction can be adopted as a conditional model, but cannot be presented as an inevitable consequence of non-factorization.

## Uniform weight

In a coefficient space of dimension D = \(2^n\), a positive trace-one operator invariant under all permutations and independent sign changes of the basis must be

\[
\rho_0=I/D.
\]

Then \(w(P)=\operatorname{Tr}(\rho_0P)=\operatorname{rank}(P)/D\). A rank-one sector has weight \(2^{-n}\); its complement has weight \(1-2^{-n}\).

This symmetry over all channels is stronger than permuting the generators. Nor is it automatically a symmetry of automorphisms of the Clifford algebra, which preserve the unit. Homogeneity must justify which transformations it permits and which structure it retains.

## Correction of v0.86, §9 — editorial review

The uniform vector \(|\Omega\rangle=D^{-1/2}\sum_i|i\rangle\) and the mixed state I/D agree for diagonal measurements in that basis, but not for all projectors. The former is pure; it is not a purification of the latter within the same space.

On \(P_\Omega=|\Omega\rangle\langle\Omega|\), their weights are respectively 1 and 1/D. The uniformity theorem for the mixed state remains valid under its hypotheses. A purification requires an auxiliary space and a partial reduction.

## Scale and physical correspondence

The octave bridge of v0.84 adopts a faithful identification \(C_4\to\mathbb R/\mathbb Z\) on a binary logarithmic scale. Under that choice, the generator corresponds to ±1/4 of an octave, with factor \(2^{\pm1/4}\). It does not derive base two from the orbit.

If a weight is identified with \(\omega_V^2/\omega^2=2^{-n}\), it follows that \(R_V/R_U=2^{n/2}\) for radii defined as c/frequency. The physical interpretation of those radii, the integer n, and the measured observable remain bridges.

The 1:3 of v0.85 comes from the ledger of two projective roles. The 1:3 of v0.90 counts one reference and the three remaining states of C4. The same numerical ratio does not prove that the two constructions are identical.

## Sources

- [v0.81](../../fuentes/originales/REFLEXION_ESCALA_BIT_v0_81.md).
- [v0.84](../../fuentes/originales/CIERRE_ALGEBRAICO_MINIMO_v0_84.md).
- [v0.85](../../fuentes/originales/PUENTE_BOOLEANO_C2_C4_v0_85.md).
- [v0.86](../../fuentes/originales/MEDIDA_INVARIANTE_PESO_BINARIO_v0_86.md).
- [v0.90](../../fuentes/originales/REFLEXION_CIERRE_CUATRO_v0_90.md).

Next: [totality and time](09_totalidad_tiempo_fisica.en.md).
