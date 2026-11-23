# Edición bilingüe | Bilingual edition — 2.1-BI

**Fecha / Date:** 2026-11-22  
**Firma / Signature:** Endless Monkey Project / Relational Geometry Program

## Archivos / Files

- `DEMOSTRACION_HILADA_BILINGUE_v2_1.pdf`: portada y manuscrito completo en español seguido de la traducción completa en inglés (19 páginas en total).
- `DEMOSTRACION_HILADA_ES_v2_1.pdf`: versión autónoma en español (9 páginas).
- `CHAINED_DEMONSTRATION_EN_v2_1.pdf`: full independent English version (9 pages).
- `src/`: fuentes LaTeX de las dos ediciones y de la portada.
- `proofs/VERIFICAR_CADENA_O58_MOBIUS.py`: laboratorio original de comprobaciones exactas.
- `proofs/RESULTADOS_VERIFICACION.txt`: ejecución local del laboratorio.
- `CONCORDANCIA_BILINGUE.md`: correspondencia de secciones y precisiones editoriales.
- `MANIFIESTO_SHA256.txt`: huellas de integridad del paquete.

## Alcance / Scope

La cadena demuestra la existencia de referencias aritméticas, su cobertura de índices libres de cuadrados, identidades de inversión y el presupuesto de recuperación funcional. La equivalencia `RH <=> lim U_j = 1` usa resultados clásicos de Báez-Duarte. **No contiene una demostración incondicional de RH**.

The chain proves arithmetic reference coverage, subset-lattice inversion, and a functional recovery budget. The equivalence `RH <=> lim U_j = 1` relies on Báez-Duarte's classical theorem. **This is not an unconditional proof of RH**.

## Reproducibilidad / Reproduction

```sh
python3 proofs/VERIFICAR_CADENA_O58_MOBIUS.py
sha256sum -c MANIFIESTO_SHA256.txt
```

Las 1.648 comprobaciones son **finitas y exactas**; no deciden la convergencia global.
The 1,648 checks are **finite and exact**; they do not decide global convergence.

## Nota editorial / Editorial note

Las identidades, la secuencia de pruebas y los resultados se conservan en ambos idiomas. Se corrigió una transición tipográfica de la versión española y se aclaró que las mediciones por octavas provienen del laboratorio diádico S--RA--01, no de la cadena de Pell `W_j`. Los títulos de archivos documentales españoles se mantienen en la bibliografía inglesa con traducciones descriptivas entre corchetes.

The identities, proof sequence, and results are preserved in both languages. A Spanish typographical transition was corrected, and the octave measurements are explicitly described as coming from the separate dyadic S--RA--01 laboratory rather than the Pell-indexed `W_j` sequence. Spanish source titles remain in the English bibliography with descriptive translations in brackets.
