# T.1 — herencia, recuperación y transferencia métrica (v1.4 + T.1.5)

**Le Matt Ansatz Di Ego** · Endless Monkey Project · Relational Geometry Program · 28 de noviembre de 2026

Esta actualización amplía el [expediente de revisión Riemann–Alpöge–Claude v3.9](../README.md) y su [issue #16](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/16). Reúne el anexo T.1 v1.4, los complementos de cierre global y herencia local, una auditoría Arb y la cota finita de T.1.5.

## Documentos

- [Anexo T.1 v1.4 en español](01_T1_v1_4/Anexo_T1_Herencia_y_transferencia_v1_4.pdf) · [English reading copy](01_T1_v1_4/Annex_T1_Inheritance_and_Metric_Transfer_v1_4_EN.pdf) · [fuente TeX](01_T1_v1_4/Anexo_T1_Herencia_y_transferencia_v1_4.tex) · [guía y verificadores](01_T1_v1_4/README.md).
- [Cierre global, lemas B1–B4](02_cierre_global/Anexo_T1_complemento_cierre_global.md) · [PDF español](02_cierre_global/Anexo_T1_complemento_cierre_global_ES.pdf).
- [Herencia local, criterios A1–A5](03_herencia_local/Anexo_T1_Herencia_local.md) · [laboratorio y contraejemplo intervalar](03_herencia_local/README.md).
- [Auditoría Arb recibida](04_auditoria_Arb/README.md) y [T.1.5: cota de Jensen](05_T1_5/Anexo_T1_5_Jensen_y_Arb.md).
- [Reproducción de esta revisión](REPRODUCCION_ES_EN.md) · [certificado Arb nuevo hasta p=19](05_T1_5/certificado_jensen_arb_p19.json) · [manifiesto de publicación](MANIFIESTO_PUBLICACION_SHA256.txt).

La ejecución independiente del verificador Arb de T.1.5 certifica ocho etapas finitas hasta $p=19$. El cierre global utiliza el resultado externo citado de Báez-Duarte. La divergencia asintótica, la transferencia aritmética directa y la certificación de extremos espectrales permanecen como preguntas de investigación.

## Procedencia y derechos

Las carpetas `01_T1_v1_4` a `05_T1_5` conservan los 34 archivos de la entrega original sin cambios. Se añadieron el PDF inglés de v1.4, el PDF español de cierre global y el certificado generado en esta revisión. El PDF español v1.4 adjunto por separado coincide byte por byte con el incluido en la entrega. Los ZIP v1.2 y v1.3 de `00_antecedentes` se reservaron para cotejo histórico. Las frases sobre el estado del repositorio en las guías originales describen la instantánea anterior a este PR. SHA-256 del ZIP recibido: `2425dca17b7079d2d9fe7a4f09d64323894bce2a57936c9d4a070c9446ce93a5`.

Sin licencia general de reutilización; se conservan los derechos correspondientes a cada archivo y a sus fuentes citadas.
