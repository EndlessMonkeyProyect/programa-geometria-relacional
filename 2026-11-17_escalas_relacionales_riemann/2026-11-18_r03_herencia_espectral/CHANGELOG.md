# Registro de revisión / Revision log

**R–03 v0.3 · 18-XI-2026 / Nov 18, 2026**

- **Pivote / Pivot.** Nueva Proposición 4: con (R03.1) en $s=\tfrac12$ y el Teorema 3 de Akatsuka (2024), la hipótesis de Riemann equivale a una cota inferior positiva para $\lvert F_{S_X}(\tfrac12)\rvert\,e^{\mathrm{li}(\vartheta(X)^{1/2})}$, con límite $-\sqrt2$. La obligación $Q$ de §8 queda escrita con esa cantidad. Laboratorio hasta $X=10^8$. / New Proposition 4 and a precise form of the §8 obligation.
- **Davenport–Heilbronn.** Control estándar añadido en §6.2, con ecuación funcional, ceros sobre y fuera de la línea y coeficientes no multiplicativos, verificados en el script. El control polinomial pasa a §6.1. / Standard control added; the polynomial control becomes §6.1.
- **Cuadratura / Quadrature.** El término principal de la cola $\langle G\rangle N^{-s-1}$ se calcula en aritmética racional y se resta; la coincidencia pasa de $\sim10^{-10}$ a $\le 9\cdot10^{-15}$. / Leading tail term computed exactly and subtracted.
- **Formato / Format.** Ecuaciones con `$…$` y `$$…$$`, que GitHub renderiza (los delimitadores `\[ \]` de v0.2 aparecían como texto). Proposiciones renumeradas: la antigua Proposición 4 es ahora la 5. / GitHub-rendered math; old Proposition 4 is now Proposition 5.
- **Alcance / Scope.** Sin cambios en la edición v1.0 de R–01/R–02.


**R–03 v0.2 · 18-XI-2026 / Nov 18, 2026**

- **Control de simetría / Symmetry control.** Se reconoce expresamente la pérdida general de simetría funcional de `H P_S` y se prueba que `H P_S(s)P_S(1-s)` conserva ambas simetrías, y los ceros originales dentro de la franja crítica abierta.
- **Mellin independiente / Independent Mellin check.** El nuevo programa calcula e integra `E_S(x)` por tramos, sin construir el integrando desde `ζ(s)P_S(s)/s`. La cola se acota por la periodicidad y el promedio nulo de `E_S` para `S` no vacío. La precisión de máquina se controla mediante una tolerancia explícita, sin certificación intervalar.
- **Sin repeticiones / No duplicated propositions.** El anexo 1.1 enlaza las Proposiciones 1 y 2 de R–03, sin reproducir sus pruebas.
- **Firma pública / Public signature.** `Le Matt Ansatz Di Ego` figura junto a la firma institucional existente.
- **Alcance / Scope.** Este paquete no es la traducción completa de R–01/R–02 ni una prueba de la hipótesis de Riemann.
