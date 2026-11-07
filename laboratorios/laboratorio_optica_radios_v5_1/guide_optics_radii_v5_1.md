# Lab v5.1 — Radii, a moving wall and the appearance of new references

**Endless Monkey Project** · *Relational Geometry Program*
Le Matt Asantz Di Ego · November 7, 2026

*Versión en español: [guia_optica_radios_v5_1.md](guia_optica_radios_v5_1.md)*

## The question

From a given reference, an extended structure can look like a single blur. That reduction depends on the distance, the scale of the structure, and the observer's aperture and wavelength; the internal structure still exists. The spectrum keeps frequency distinctions that the spatial image no longer separates.

The lab measures three things:

1. when a distinction disappears or reappears as the reference moves;
2. when a phase observation with a new period adds distinctions to the inherited ones;
3. how many distinctions the observer obtains and what they cost (the economy).

In A, B and C the observer sees classes of configurations equivalent under the declared observables. Moving the reference splits or merges those classes.

| Part | What moves | What looks identical | Is information lost? |
| --- | --- | --- | --- |
| A — mirrors | The wall L | Points in the same orbit | The scene is kept; the signature gives the orbit, not the point |
| B — resolution | The distance D | Sources closer than the angular threshold | Yes; the far scene is irreversible (E) |
| C — phase | The set of wavelengths | Positions that differ by a multiple of H | No within the period; ambiguous beyond it |

## A — Parallel mirrors

- s₀(x) = −x and s_L(x) = 2L − x are involutions; s_L(s₀(x)) = x + 2L.
- The orbit signature F_L(x) = L − |(x mod 2L) − L| maps each point to its representative in [0, L] within the orbit {±x + 2kL}. The code checks this invariance for k = −3 … 3.
- With L = 1, the points 0.25 and 1.75 both have signature 0.25: same orbit. With L = 2 their signatures are 0.25 and 1.75: different orbits.

Moving the wall changes the partition into orbits.

## B — Radii, distance and resolution

**Scene.** Five sources on a section perpendicular to the line of sight, at −R, −R+s, 0, R−s and R, with R = 5×10⁸ m and s = 10⁷ m. Bands 450, 450, 550, 650 and 650 nm; weights 1.0, 1.2, 2.0, 1.3 and 1.0. Aperture radius r₀ = 0.25 m. Distance D(t) = 10¹⁵ − 2×10⁶·t m (|v|/c ≈ 0.0067, approaching).

**Per-band threshold** (Rayleigh, circular aperture, one-way relativistic Doppler, β = v/c < 0):

```
θ_R(λ) = 1.22 · λ_obs / (2 r₀),   λ_obs = λ · √((1+β)/(1−β))
```

Values while approaching: 1.091×10⁻⁶ rad (450 nm), 1.333×10⁻⁶ rad (550 nm) and 1.575×10⁻⁶ rad (650 nm).

**Components.** Two neighboring sources fall into different components when their angular separation reaches the threshold of the longer wavelength of the pair (the wider blur). This is a discrete resolution model, without noise, interference or a sensitivity threshold.

**Extent.** Total angular size divided by the 550 nm threshold. Below 1: point-like image; above 1: extended image.

| t (s) | D (m) | Components | Extent | Image |
| ---: | ---: | ---: | ---: | --- |
| 0 | 1×10¹⁵ | 1 | 0.75 | point-like |
| 2×10⁸ | 6×10¹⁴ | 1 | 1.25 | extended |
| 3.3×10⁸ | 3.4×10¹⁴ | 2 | 2.21 | extended |
| 4×10⁸ | 2×10¹⁴ | 3 | 3.75 | extended |
| 4.9×10⁸ | 2×10¹³ | 3 | 37.5 | extended |
| 4.96×10⁸ | 8×10¹² | 4 | 93.8 | extended |
| 4.99×10⁸ | 2×10¹² | 5 | 375 | extended |

**Exact transitions.** Each gap gᵢ between neighbors opens at the distance Dᵢ = gᵢ / θᵢ. The code checks each jump by evaluating the count at Dᵢ·(1 ± 10⁻⁶).

| Transition | Gap | Threshold band | Dᵢ (m) | As D increases |
| --- | --- | --- | ---: | --- |
| D₁ | red pair (R−s, R), 10⁷ m | 650 nm | 6.35×10¹² | 5 → 4 |
| D₂ | blue pair (−R, −R+s), 10⁷ m | 450 nm | 9.17×10¹² | 4 → 3 |
| D₃ | center – (R−s), 4.9×10⁸ m | 650 nm | 3.11×10¹⁴ | 3 → 2 |
| D₄ | (−R+s) – center, 4.9×10⁸ m | 550 nm | 3.68×10¹⁴ | 2 → 1 |

Results:

- The full ladder is 5 → 4 → 3 → 2 → 1 and it is asymmetric: the blue side separates before the red side, because its threshold is smaller.
- One component and one point are different things: at D = 6×10¹⁴ m there is a single component and the image spans 1.25 times the threshold.
- Reversed motion: with v = +2×10⁶ m/s (receding) the threshold grows through Doppler and each Dᵢ is multiplied by 0.9867. The sequence traversed is 5-4-3-3-2-1-1, the reverse of the approach.
- Ideal receiver spectrum: weights 2.2 (450 nm), 2.0 (550 nm) and 2.3 (650 nm). The three bands are distinguishable at every instant and do not depend on the positions.
- Total flux follows the 1/D² law.

**Check against an idealized physical image** (`contraste_airy.py`): incoherent sum of Airy patterns, one per source at its own wavelength, noiseless panchromatic receiver; local maxima are counted. The Airy ranges come from a sweep over 3000 distances, with a resolution of about 0.2%.

| Components | Lab criterion | Airy image |
| ---: | --- | --- |
| 5 | D < 6.35×10¹² m | D < 7.28×10¹² m |
| 4 | 6.35×10¹² – 9.17×10¹² m | 7.28×10¹² – 1.07×10¹³ m |
| 3 | 9.17×10¹² – 3.11×10¹⁴ m | 1.07×10¹³ – 4.08×10¹⁴ m |
| 2 | 3.11×10¹⁴ – 3.68×10¹⁴ m | 4.08×10¹⁴ – 6.02×10¹⁴ m |
| 1 | D > 3.68×10¹⁴ m | D > 6.02×10¹⁴ m |

The Airy image reproduces the same ladder in the same order. Each transition occurs at a distance 1.1 to 1.6 times greater, because a dip between two maxima appears before the Rayleigh separation. At D = 6×10¹⁴ m the Airy image sits on the edge: two maxima with a 0.01% dip and a width 2.35 times that of a point source.

## C — Reflection phase: periods and new referents

In an ideal interferometer, light of wavelength λ that travels to the mirror at distance D and back has phase

```
φ(D) = 4π·D / λ   (mod 2π)
```

The phase identifies positions separated by λ/2: φ(D) = φ(D + λ/2).

With unit u = 100 nm and periods p = 3, 5, 7 and 9 (λ = 600, 1000, 1400 and 1800 nm; from 1000 nm on it is near infrared), two integer positions D/u share the same collection of phases exactly when their difference is a multiple of H = lcm(P). A new observation of period m gives the combined period H′ = lcm(H, m) and splits each inherited class into H′/H = m / gcd(H, m) classes. A new referent appears exactly when m does not divide H.

This construction is the integer idealization of the method of excess (or exact) fractions of multi-wavelength interferometry, used in gauge-block calibration since the 1890s (see References). It assumes coherent noiseless phase, commensurate periods and integer positions.

| Inherited (H) | New m | H′ | Classes per inherited class | Bits it costs | Bits it adds | Efficiency |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| {3} (3) | 5 | 15 | 5 | 2.32 | 2.32 | 100% |
| {3,5} (15) | 9 | 45 | 3 | 3.17 | 1.58 | 50% |
| {3,5,9} (45) | 7 | 315 | 7 | 2.81 | 2.81 | 100% |
| {3,5,7} (105) | 9 | 315 | 3 | 3.17 | 1.58 | 50% |
| {3,5,7,9} (315) | 9 | 315 | 1 | 3.17 | 0 | 0% |
| {3,5} (15) | 5 | 15 | 1 | 2.32 | 0 | 0% |

The case of 9: 15 contains the factor 3 but not 3², so the period-9 phase separates positions that were previously equivalent. What changes is the collection of observables; the uncertainty in this section is the phase ambiguity over the position D.

## D — Economy

The economy is measured as the number of classes the observer distinguishes (in bits, log₂ of the number of classes) against the number of states that exist.

**B saves because it forgets.** The number of components is a step function of distance:

```
N(D) = 1 + #{ i : gᵢ ≥ θ_R(λᵢ) · D }
```

Each distinction appears at its own distance, and the order of appearance is set by the hierarchy of gaps in the structure: it is a single-linkage dendrogram (the H₀ barcode of persistent homology). From far away the description is minimal (one component, its extent and three bands), and section E shows that this description corresponds to more than one structure. Producing the image requires summing the n sources: the saving is in what is distinguished, and the computational cost stays.

**C saves because it reuses.** An observation of period m costs log₂ m bits, the size of its outcome, and adds log₂(m / gcd(H, m)) bits (table in C). It pays off fully when it brings a new prime power. The residues of {3, 5, 7, 9} take 9.88 bits and distinguish 315 classes (8.30 bits): the residue mod 3 is redundant because mod 9 contains it. The minimal basis is the set of maximal prime powers of H: {5, 7, 9}.

**The limit.** Locating a position among 630 requires log₂ 630 = 9.30 bits, and no representation goes below that bound.

| Periods | Signatures in [0, 630) | Positions per signature | Bits distinguished | Bits stored | Redundant bits |
| --- | ---: | ---: | ---: | ---: | ---: |
| {3, 5} | 15 | 42 | 3.91 | 3.91 | 0 |
| {3, 5, 9} | 45 | 14 | 5.49 | 7.08 | 1.58 |
| {5, 7, 9} | 315 | 2 | 8.30 | 8.30 | 0 |
| {3, 5, 7, 9} | 315 | 2 | 8.30 | 9.88 | 1.58 |

- The modular signature is a change of coordinates: the Chinese remainder theorem is a one-to-one correspondence.
- The real economy is incremental. With {3, 5, 9} (H = 45), the queries x mod 3, 9, 15 and 45 are answered from the inherited signature; x mod 2 and x mod 7 require a new observation. In general, x mod m is answered from what is inherited exactly when m divides H.
- Adding an observation costs only its residue.

**What the bits measure.** They count distinguishable classes and redundancy in the representation; the physical cost of measuring and the computing time are assessed separately. The optical formulas and thresholds are approximations within the idealized model.

## E — Reopening and the limit of inheritance

Two scenes with the same bands and the same weights: A, with five distinct positions, and B = (−R, −R, 0, R, R), with three distinct positions (coincident sources).

- At 10¹⁵ m both have one component, extent 0.75 and the same spectrum.
- At 2×10¹² m, A has five components and B three.
- In an ideal noiseless image, their weighted centroids at 10¹⁵ m differ by 1.54×10⁻¹⁰ rad, that is 1.15×10⁻⁴ times the 550 nm threshold.

The far observable (component count, extent and spectrum) is the same for two different distributions: that signal determines the class, and the distribution of sources remains undetermined. Recovering it requires changing the observation (moving closer, another band, another observable) or having kept more relations.

## Verified in this implementation

Each item corresponds to assertions in the code and to computed values in the CSV.

1. **A:** involutions, composition equal to the translation by 2L, invariance of the signature over the whole orbit, and the change of partition when L moves.
2. **B:** the ladder 5 → 4 → 3 → 2 → 1 with four exact transitions Dᵢ = gᵢ/θᵢ; one extended component at D = 6×10¹⁴ m; reversal with real receding motion (v > 0); three spectral bands at every instant.
3. **B, optional check:** the Airy image gives the same ladder in the same order, with transitions at distances 1.1 to 1.6 times greater.
4. **C:** λ/2 periodicity, the lcm criterion, a new referent exactly when m does not divide H, and the bits each observation costs and adds.
5. **D:** classes of exact size in [0, 630); minimal basis {5, 7, 9}; redundancy of the residue mod 3; queries x mod m answered from what is inherited exactly when m divides H.
6. **E:** the same far observable for two different distributions, and the computed centroid difference.

## Open

- Demonstrate a computational economy greater than that of existing methods in algebra, dynamic programming, the Chinese remainder theorem, compression and inference.
- Find a family of problems in which inherited structure lets you skip work rather than merely reorder it; this is where the SAT question comes in.
- Demonstrate an equivalent link with the OpenAI/Anthropic algorithms.
- Carry this idealized realization over to highly complex physical observations.
- Add noise, finite coherence, time delay and full relativity in B; non-commensurate periods, continuous distances and noisy phase in C.

## Reproduce

```bash
python3 laboratorio_optica_radios_v5_1.py   # standard library only, under 1 s
python3 contraste_airy.py                   # optional; numpy and scipy, about 5–10 s
```

The first verifies sections A–E and writes `resultados_optica_v5_1.csv`. The second prints the tables of the Airy check in section B.

This lab complements the v4 protocol, "Open call for review: reflection, inheritance and computational economy", which defines the normalization singularity and measures the economy of interfaces; that protocol is published separately.

## References

- M. Wengierow, L. Salbut, Z. Ramotowski, R. Szumski and K. Szykiedans, ["Measurement system based on multi-wavelength interferometry for long gauge block calibration"](https://journals.pan.pl//Content/90167/PDF/Journal10178-VolumeXX%20Issue3_14.pdf), Polish Academy of Sciences, vol. XX, no. 3, 2013.
- ["Method of excess fractions with application to absolute distance metrology: wavelength selection and the effects of common error sources"](https://doi.org/10.1364/AO.51.006471), *Applied Optics* 51, 6471 (2012).
- ["Phase-step calibration extends 19th century standard into 21st"](https://www.laserfocusworld.com/test-measurement/test-measurement/article/16549948/phasestep-calibration-extends-19th-century-standard-into-21st), *Laser Focus World*.
