# What computation becomes unnecessary?

**Endless Monkey Project**  
*Relational Geometry Program*  
November 10, 2026 · manuscript for independent review · version 0.3 · [Español](README.md)

When part of the uncertainty is already resolved by inherited relations, recognizing it saves computation, and recognizing it also costs something. The manuscript follows that account inside the mirror box: the tetrahedron and comparison without direction, the closure recognized before it closes, exact counting when the reflections are given, and the cost of recognizing them when they arrive hidden in gates. The measurements compare recognition with a DPLL that enumerates and with variable elimination on the formula as it arrives, up to 256 primary variables.

It continues [*Where does computation become cheaper?*](../2026-11-08_economia_del_calculo) (November 8, 2026).

## Contents

- [`PAPER_EN.md`](PAPER_EN.md) and [`PAPER_EN.pdf`](PAPER_EN.pdf): paper in English.
- [`PAPER_ES.md`](PAPER_ES.md) and [`PAPER_ES.pdf`](PAPER_ES.pdf): paper in Spanish.
- [`EVIDENCE.en.md`](EVIDENCE.en.md): what each folder holds, how to reproduce, and the reproduction record.
- [`experimentos/`](experimentos/): standalone verifier, two laboratories, generic baseline and their results.
- [`SHA256SUMS.txt`](SHA256SUMS.txt): checksums of every file.

## Quick check

```bash
python3 -I experimentos/verificar_reconstruccion_y_convergencia.py
```

No dependencies. The laboratories use NumPy; instructions are in `EVIDENCE.en.md`.
