# R–03 · Revisión bilingüe / Bilingual revised package

**18 de noviembre de 2026 / November 18, 2026**  
**Endless Monkey Project**  
Relational Geometry Program  
**Le Matt Ansatz Di Ego**

Adiciones y correcciones para acompañar la [publicación pública R–01/R–02 v1.0](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann). El paquete no modifica GitHub ni presenta una demostración de la hipótesis de Riemann.

Additions and corrections accompanying the [published Spanish R–01/R–02 v1.0](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann). This package does not modify GitHub and does not claim to prove the Riemann hypothesis.

| Archivo / File | Función / Purpose |
|:--|:--|
| `ANEXO_V1_1_CONSERVACION_CEROS_ES.md` | Inserción breve con enlace a las pruebas completas / Short insertion linking to full proofs |
| `ADDENDUM_V1_1_ZERO_PRESERVATION_EN.md` | English short insertion |
| `R03_HERENCIA_Y_LOCALIZACION_ES.md` | Formalización R–03 completa en español |
| `R03_SPECTRAL_INHERITANCE_EN.md` | Complete R–03 formalization in English |
| `verificacion_R03.py` | Controles numéricos + cuadratura independiente de Mellin / Independent sieve quadrature |
| `RESULTADOS_R03_v02.txt` | Registro reproducible de ejecución / Recorded verification output |
| `R03_Anexo_Bilingue.docx` | Lectura unificada ES/EN / Combined Word edition |
| `build_word.py` | Script local de reconstrucción de Word (requiere `pandoc`, `python-docx`) |
| `CHANGELOG.md` | Cambios y limitaciones / Changes and limitations |
| `SHA256SUMS.txt` | Sumas de los archivos distribuidos / Checksums |

## Correcciones / Corrections

- `H_S=H P_S` conserva los ceros en la franja, pero generalmente **no** conserva la simetría `s↦1−s`. La familia `H(s)P_S(s)P_S(1-s)` conserva ambas simetrías y los mismos ceros en `0<Re(s)<1`. / The symmetrized family restores reflection and conjugation symmetries without new zeros inside the strip.
- Se añaden seis integraciones independientes de `E_S` directamente desde la criba, con cota analítica explícita de la cola y margen declarado de redondeo. / Six independent sieve-based numerical Mellin integrals are added.
- El anexo 1.1 ahora **remite** a las proposiciones de R–03 sin duplicarlas. / The v1.1 insertion links to R–03 rather than duplicating its propositions.
- Firma pública incorporada / Public signature added: **Le Matt Ansatz Di Ego**.

## Alcance lingüístico / Translation scope

Las versiones ES/EN incluyen **R–03 y su anexo 1.1**. **No** son traducciones íntegras de R–01/R–02 ni de «Un número por cero». / The Spanish and English files cover **R–03 and its v1.1 insertion** only; they are **not** full translations of R–01/R–02 or *One number per zero*.

## Reproducibilidad / Reproduction

```bash
python -m pip install mpmath
python verificacion_R03.py
```

Para generar el DOCX / To rebuild the DOCX: `python build_word.py` (requires `pandoc` and `python-docx`).

**Estado matemático / Mathematical status:** herencia finita demostrada; preservación de ceros demostrada en la franja; localización universal de ceros sobre `Re(s)=1/2` **abierta**. / Finite inheritance and zero preservation are proved; the Riemann hypothesis remains **open**.
