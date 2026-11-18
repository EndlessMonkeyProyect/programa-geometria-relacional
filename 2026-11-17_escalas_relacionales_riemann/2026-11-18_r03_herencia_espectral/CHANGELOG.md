# Registro de revisión / Revision log

**R–03 v0.2 · 18-XI-2026 / Nov 18, 2026**

- **Control de simetría / Symmetry control.** Se reconoce expresamente la pérdida general de simetría funcional de `H P_S` y se prueba que `H P_S(s)P_S(1-s)` conserva ambas simetrías, y los ceros originales dentro de la franja crítica abierta.
- **Mellin independiente / Independent Mellin check.** El nuevo programa calcula e integra `E_S(x)` por tramos, sin construir el integrando desde `ζ(s)P_S(s)/s`. La cola se acota por la periodicidad y el promedio nulo de `E_S` para `S` no vacío. La precisión de máquina se controla mediante una tolerancia explícita, sin certificación intervalar.
- **Sin repeticiones / No duplicated propositions.** El anexo 1.1 enlaza las Proposiciones 1 y 2 de R–03, sin reproducir sus pruebas.
- **Firma pública / Public signature.** `Le Matt Ansatz Di Ego` figura junto a la firma institucional existente.
- **Alcance / Scope.** Este paquete no es la traducción completa de R–01/R–02 ni una prueba de la hipótesis de Riemann.
