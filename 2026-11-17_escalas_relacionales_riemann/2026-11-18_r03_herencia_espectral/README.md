# R–03 · Revisión bilingüe / Bilingual revised package

**v0.3 · 18 de noviembre de 2026 / November 18, 2026**  
**Endless Monkey Project**  
Relational Geometry Program  
**Le Matt Ansatz Di Ego**

Adiciones y correcciones que acompañan la [publicación R–01/R–02 v1.0](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann). La edición v1.0 se conserva tal cual; la hipótesis de Riemann permanece abierta.

Additions and corrections accompanying the [published Spanish R–01/R–02 v1.0](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann). The v1.0 edition is kept as published; the Riemann hypothesis remains open.

| Archivo / File | Función / Purpose |
|:--|:--|
| `R03_HERENCIA_Y_LOCALIZACION_ES.md` | Formalización R–03 completa en español |
| `R03_SPECTRAL_INHERITANCE_EN.md` | Complete R–03 formalization in English |
| `ANEXO_V1_1_CONSERVACION_CEROS_ES.md` | Inserción breve con enlace a las pruebas completas |
| `ADDENDUM_V1_1_ZERO_PRESERVATION_EN.md` | Short insertion linking to the full proofs |
| `verificacion_R03.py` | Controles numéricos, cuadratura independiente de Mellin, Davenport–Heilbronn y laboratorio del pivote / Numerical checks, independent sieve quadrature, Davenport–Heilbronn, and pivot laboratory |
| `RESULTADOS_R03_v03.txt` | Registro reproducible de ejecución / Recorded verification output |
| `R03_Anexo_Bilingue.docx` | Lectura unificada ES/EN / Combined Word edition |
| `build_word.py` | Reconstrucción local del Word (requiere `pandoc`, `python-docx`) |
| `CHANGELOG.md` | Cambios / Changes |
| `SHA256SUMS.txt` | Sumas de los archivos distribuidos / Checksums |

## Lo nuevo en v0.3 / What is new in v0.3

- **El costo de la inversión en el pivote (Proposición 4).** Con la identidad de R–01, $F_{S_X}(\tfrac12)\,e^{\mathrm{li}(\vartheta(X)^{1/2})}=2\zeta(\tfrac12)/E_1(X)$. Por el Teorema 3 de Akatsuka (2024), la hipótesis de Riemann equivale a que esa cantidad se mantenga lejos de cero, con límite $-\sqrt2$. Laboratorio hasta $X=10^8$: $E_1$ baja de $3{,}19$ a $2{,}19$, hacia $2{,}0653$. / *Inversion cost at the pivot:* with R–01's identity, RH is equivalent to a positive lower bound for the normalized complete discrepancy at $s=\tfrac12$, with limit $-\sqrt2$.
- **Control estándar de Davenport–Heilbronn.** Serie de Dirichlet con ecuación funcional, ceros sobre la línea y fuera de ella ($0{,}8085171825+85{,}6993484854\,i$), sin producto de Euler. Localiza el ingrediente que falta: la herencia sobre todos los primos. / *Standard control:* the Davenport–Heilbronn function isolates the Euler product as the missing ingredient.
- **Cuadratura afinada.** La diferencia de la cuadratura independiente es exactamente el término principal de la cola, $\langle G\rangle N^{-s-1}$; al restarlo, la coincidencia pasa a $\le 9\cdot10^{-15}$. / *Sharpened quadrature:* the residual is the leading tail term; subtracting it gives agreement to $\le 9\cdot10^{-15}$.
- **Matemática visible en GitHub.** Las ecuaciones usan `$…$` y `$$…$$`. / *Math now renders on GitHub.*

## Reproducibilidad / Reproduction

```bash
python -m pip install mpmath
python verificacion_R03.py            # ~10 s; laboratorio del pivote hasta 1e8
python verificacion_R03.py --hasta 7  # ejecución liviana, hasta 1e7
```

Para generar el DOCX / To rebuild the DOCX: `python build_word.py` (requires `pandoc` and `python-docx`).

**Estado matemático / Mathematical status:** herencia finita y conservación de ceros demostradas; equivalencia de la hipótesis de Riemann con la cota inferior de la discrepancia completa en el pivote demostrada a partir de Akatsuka (2024); la cota misma, como la hipótesis de Riemann, **abierta**. / Finite inheritance and zero preservation are proved; the pivot equivalence is proved from Akatsuka (2024); the bound itself, like the Riemann hypothesis, is **open**.
