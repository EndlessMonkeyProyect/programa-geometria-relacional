# Relational scales and the Riemann hypothesis

**Public author:** Le Matt Ansatz Di Ego<br>
Endless Monkey Project · Relational Geometry Program<br>
November 17, 2026 · Version 1.0

This delivery contains two Spanish papers and their reproducible checks. [The sieve formalization](FORMALIZACION_R01_R02_ES.md) develops an exact discrepancy inheritance law, its Mellin transform and period energy, and a scale table for exact prime counting. [The accompanying reflection](REFLEXION_UN_NUMERO_POR_CERO_ES.md) follows the prime-counting fluctuation to the zeros of $\zeta$, the symmetry about $\operatorname{Re}s=\tfrac12$, and a comparison with Mersenne octaves.

The papers distinguish proved identities, finite computations, and the open Riemann hypothesis. The PDF editions are [formalization](FORMALIZACION_R01_R02_ES.pdf) and [reflection](REFLEXION_UN_NUMERO_POR_CERO_ES.pdf). The two Python verifiers and their figures are in this folder.

## Bilingual R–03 supplement · November 18, 2026

[R–03 in English](2026-11-18_r03_herencia_espectral/R03_SPECTRAL_INHERITANCE_EN.md) · [R–03 en español](2026-11-18_r03_herencia_espectral/R03_HERENCIA_Y_LOCALIZACION_ES.md) · [Short English addendum](2026-11-18_r03_herencia_espectral/ADDENDUM_V1_1_ZERO_PRESERVATION_EN.md) · [Guide and verification](2026-11-18_r03_herencia_espectral/README.md).

The supplement (v0.3) proves zero preservation under finite prime filters and quantifies normalization stability. At the pivot $s=\tfrac12$ it writes a known equivalent with the sieve discrepancy: the Riemann hypothesis is equivalent to a lower bound for the complete discrepancy normalized by $e^{\mathrm{li}(\sqrt{\vartheta(X)})}$ (Akatsuka, 2024), with a laboratory up to $X=10^8$. With the Davenport–Heilbronn function it separates symmetry from localization: what distinguishes $\zeta$ is the Euler product, inheritance over all primes. The Riemann hypothesis remains open.

## Reproduction

```sh
pip install numpy mpmath sympy matplotlib
python verificacion_R01_R02.py
python verificacion_un_numero_por_cero.py
```

The published edition aligns the public author name with the repository and clarifies the Conrad reference, the finite collection in the Kronecker–Weyl statement, and sign crossings for simple zeros. [Rights and use](RIGHTS.md) · [Guía en español](README.md).
