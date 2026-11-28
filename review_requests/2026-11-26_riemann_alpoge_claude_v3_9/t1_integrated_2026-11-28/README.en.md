# T.1 — inheritance, recovery, and metric transfer (v1.4 + T.1.5)

**Le Matt Ansatz Di Ego** · Endless Monkey Project · Relational Geometry Program · November 28, 2026

This update extends the [Riemann–Alpöge–Claude v3.9 review dossier](../README.en.md) and its [issue #16](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/16). It brings together the T.1 v1.4 annex, supplements on global closure and local inheritance, an Arb audit, and the finite T.1.5 bound.

## Documents

- [T.1 v1.4 annex in English](01_T1_v1_4/Annex_T1_Inheritance_and_Metric_Transfer_v1_4_EN.pdf) · [Spanish reference PDF](01_T1_v1_4/Anexo_T1_Herencia_y_transferencia_v1_4.pdf) · [TeX source](01_T1_v1_4/Anexo_T1_Herencia_y_transferencia_v1_4.tex) · [guide and verifiers](01_T1_v1_4/README.md).
- [Global closure, lemmas B1–B4](02_cierre_global/Anexo_T1_complemento_cierre_global.md) · [Spanish PDF](02_cierre_global/Anexo_T1_complemento_cierre_global_ES.pdf).
- [Local inheritance, criteria A1–A5](03_herencia_local/Anexo_T1_Herencia_local.md) · [laboratory and interval counterexample](03_herencia_local/README.md).
- [Supplied Arb audit](04_auditoria_Arb/README.md) and [T.1.5: Jensen bound](05_T1_5/Anexo_T1_5_Jensen_y_Arb.md).
- [Reproduction record](REPRODUCCION_ES_EN.md) · [new Arb certificate through p=19](05_T1_5/certificado_jensen_arb_p19.json) · [publication checksums](MANIFIESTO_PUBLICACION_SHA256.txt).

The independent Arb run of the T.1.5 verifier certifies eight finite stages through $p=19$. Global closure invokes the cited external result of Báez-Duarte. Asymptotic divergence, direct arithmetic transfer, and certification of spectral endpoints remain research questions.

## Provenance and rights

Folders `01_T1_v1_4` through `05_T1_5` preserve the 34 files of the supplied delivery byte for byte. The English v1.4 PDF, Spanish global-closure PDF, and certificate generated during this review were added. The separately attached Spanish v1.4 PDF matches the copy in the delivery byte for byte. The v1.2 and v1.3 ZIPs in `00_antecedentes` remain historical comparison materials. Statements about repository status in the original guides describe the snapshot before this PR. SHA-256 of the supplied ZIP: `2425dca17b7079d2d9fe7a4f09d64323894bce2a57936c9d4a070c9446ce93a5`.

No general reuse license is granted; rights associated with each file and its cited sources are retained.
