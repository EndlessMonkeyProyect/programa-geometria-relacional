# Relational scales and the Riemann hypothesis

**Public author:** Le Matt Ansatz Di Ego<br>
Endless Monkey Project · Relational Geometry Program<br>
November 17, 2026 · Version 1.0

This delivery contains two Spanish papers and their reproducible checks. [The sieve formalization](FORMALIZACION_R01_R02_ES.md) develops an exact discrepancy inheritance law, its Mellin transform and period energy, and a scale table for exact prime counting. [The accompanying reflection](REFLEXION_UN_NUMERO_POR_CERO_ES.md) follows the prime-counting fluctuation to the zeros of $\zeta$, the symmetry about $\operatorname{Re}s=\tfrac12$, and a comparison with Mersenne octaves.

The papers distinguish proved identities, finite computations, and the open Riemann hypothesis. The PDF editions are [formalization](FORMALIZACION_R01_R02_ES.pdf) and [reflection](REFLEXION_UN_NUMERO_POR_CERO_ES.pdf). The two Python verifiers and their figures are in this folder.

## Reproduction

```sh
pip install numpy mpmath sympy matplotlib
python verificacion_R01_R02.py
python verificacion_un_numero_por_cero.py
```

The published edition aligns the public author name with the repository and clarifies the Conrad reference, the finite collection in the Kronecker–Weyl statement, and sign crossings for simple zeros. [Rights and use](RIGHTS.md) · [Guía en español](README.md).
