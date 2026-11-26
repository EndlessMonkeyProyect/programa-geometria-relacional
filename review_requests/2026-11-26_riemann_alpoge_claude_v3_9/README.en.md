# Independent review request · Riemann–Alpöge–Claude v3.9

**Le Matt Ansatz Di Ego** · Endless Monkey Project · Relational Geometry Program · November 26, 2026

This dossier invites independent examination of successive arithmetic references, functional approximation, and recovery cost. It states identities and equivalences under their hypotheses and poses **Problem T** on quantitative transfer between the constructions. The English review edition adapts the complete Spanish original for examination; it is not a page-for-page translation.

## Documents

- [English review request](english/Independent_Review_Request_EN.md) and [English technical note](english/Riemann_Alpoge_Claude_Independent_Review_EN_v3_9.pdf).
- [English presentation](english/Riemann_Alpoge_Claude_Review_Presentation_EN_v3_9.pdf).
- [Spanish original](original_spanish/Equivalencias_Riemann_Alpoge_Claude_v3_9.pdf) and [Spanish presentation](original_spanish/Presentacion_Riemann_Alpoge_Claude_v3_9.pdf).
- [English LaTeX sources](english/) and [original Spanish sources and verifiers](original_spanish/Equivalencias_v3_9_fuente_y_verificacion.zip).
- [Original reproduction guide](README_EN.txt), [delivery checksums](SHA256SUMS.txt), and [publication checksums](MANIFIESTO_PUBLICACION_SHA256.txt).
- [Bilingual editorial note](NOTA_EDITORIAL_ES_EN.md) on reference [15] and the provenance of the Lean reports.

The original archive preserves nine scripts, reports, and Spanish source materials. The English edition checks file integrity and documents earlier numerical results; it does not report a new execution of the nine scripts or an independent Lean audit. The request identifies formulas, sources, hypotheses, and transfer estimates for review.

On Python 3.12 with current NumPy and mpmath, `checks.py` needs [an explicit `numpy.int64` to `int` conversion](compat/checks_numpy_int.patch) before constructing `mp.mpf`. Apply the patch to an **extracted working copy** of the Spanish ZIP; original files and hashes remain intact. On a Windows cp1252 console, set `PYTHONIOENCODING=utf-8` to print the report's integral symbol. These execution compatibility changes leave the formulas unchanged.

**Audit for this preparation:** with Python 3.12.14, NumPy 2.3.5, and mpmath 1.3.0, the patched working copy of `checks.py` completed sections (a)–(g); `vasyunin.py` and `cadena_lc.py` also completed. The other six scripts and the Lean development were not run in this review.

The [R–03/Alpöge comparison materials](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/13) and [O58 v2.1](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/14) remain in separate PRs outside `main`. This dossier cites those antecedents without copying them.

No general reuse license is granted; rights associated with each file and its cited sources are retained.
