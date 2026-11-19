# R–03 v0.4 and the configuration-measurement Gram bridge

**19 November 2026 · Bilingual editorial proposal, subject to PR approval**<br>
Le Matt Ansatz Di Ego<br>
Endless Monkey Project<br>
Relational Geometry Program

This is a **new versioned directory**. Preserve the published R–03 v0.3 and historical R–01/R–02 files unchanged. The quadratic forms measure configuration-counting discrepancies; they are not statements of physical energy.

## Documents

- [R–03 — Spanish](R03_HERENCIA_Y_LOCALIZACION_ES.md)
- [R–03 — English](R03_SPECTRAL_INHERITANCE_EN.md)
- [Weighted Gram measurement — Spanish](PUENTE_GRAM_MEDICION_ES.md)
- [Weighted Gram measurement — English](GRAM_BRIDGE_MEASUREMENT_EN.md)
- [Provenance and scope (Spanish)](PROCEDENCIA_Y_LIMITES.md)
- [Changes (Spanish)](CHANGELOG.md)

## Verification

```bash
python -m pip install mpmath
python verificacion_R03.py --hasta 6
python verificacion_puente_y_control.py
python verificacion_puente_gram_v1_1.py --N 3000 --dps 45
sha256sum -c SHA256SUMS.txt
```

The full R–03 $10^8$ verification may require substantial memory. Audit logs from prior sessions are included separately, **not** as proof of a fresh run. The R–RH–01 file supplied on 19 November 2026 (SHA-256 `cba927f6532471cd8aee14f0dbc96ae2b1bfe3137d4910b2813ef72fe42feedf`) matches the reading transcription apart from a final newline. The manuscript is not included here; a public link remains pending. RH remains open.
