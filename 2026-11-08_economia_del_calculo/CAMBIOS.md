# Cambios · Changes

Endless Monkey Project  
Relational Geometry Program

[Español](#español) · [English](#english)

---

## Español

**Versión 2 · 8 de noviembre de 2026.** Respecto de la etiqueta `2026-11-08-economia-del-calculo` (commit `552aa0b`). Las cuatro primeras filas responden a una revisión externa del mismo día, y la quinta a una segunda lectura de la versión 2; las demás vienen de la preparación de la solicitud de revisión.

| Sección | Cambio | Justificación |
| --- | --- | --- |
| §2, cor. 2.2 | Con permutación, \|P ∧ Q\|·\|P ∨ Q\| = \|P\|·\|Q\| + k²·Cov_J(p_J, q_J). La ley del producto pide permutación y covarianza nula. Nuevo contraejemplo: {12 \| 34 \| 5} y {13 \| 24 \| 5} permutan y dan 10 frente a 9. | La permutación sola no fija la ley. E1: de 334 pares que permutan, 176 cumplen la ley, y la ley vale exactamente cuando la covarianza es nula en los 334. |
| §6, teo. 6.1 | «Para todo orden y todo campo, algún corte tiene rango 2^Ω(n)». | Es lo que prueba el argumento: el corte del medio de cada orden. Un corte cualquiera puede tener rango bajo (E2: rango mínimo de 4 a 10 sobre cortes balanceados, n = 8…16). |
| §6, teo. 6.2 | El rango de corte de Tseitin es 2^λ(A), con λ la función de conectividad del matroide gráfico, para cualquier carga satisfacible. Prueba por bloques de unos. Antecedentes: teorema del espacio de estados de Forney (1994) y Kashyap (2008). La cota exponencial se atribuye a familias satisfacibles sobre expansores; un árbol da rango 1. | La versión 1 contaba filas distintas y solo trataba la carga nula. E3b ahora calcula el rango directamente: 3003 cortes con carga nula, 3003 con carga aleatoria y 216 en grafos aleatorios. |
| §5.5 | El orden 51 queda certificado: det H_51 ≠ 0, det H_52 = 0 y Hankel desplazado no singular (sin raíz nula). Tabla de órdenes para anchos 1 a 10: 1, 1, 2, 3, 5, 7, 13, 19, 35, 51. Los anchos 6 y 7 coinciden con OEIS A207995 y A207996. | La versión 1 apoyaba el orden en el rango de Hankel módulo un primo. Nuevo experimento E5c. |
| Resumen, §5.5, solicitud | El 51 se enuncia como la dimensión de la representación lineal mínima de la cuenta sobre los racionales. La solicitud separa lo demostrado de lo que se pregunta y empieza por la pregunta concreta. | El 51 caracteriza esa representación lineal del conteo. La pregunta por sus antecedentes es distinta del cálculo certificado. |
| §5.5 y solicitud, referencia OEIS | A207997 contiene conteos para anchos mayores que 7; no se presenta como una tabla de órdenes mínimos de recurrencia. | Corrección bibliográfica en la revisión previa a la publicación de v2. |
| §10 | Nueva fila resuelta (Tseitin y el matroide gráfico); la pregunta abierta de la rejilla pasa a ser la sucesión de órdenes. Once relaciones resueltas. | Consecuencia de los cambios anteriores. |
| §10, ruta del signo | Se acota el costo total: cuántos términos, cómo se hallan, cuánto cuesta evaluarlos y recombinarlos, y exactitud para toda la familia. | Bajar el rango de cada término es trivial con términos de rango uno. |
| §11 | Filas de E1, E3b y E5c actualizadas; comando `E5 E5x E5c`. | Reproducción de los cambios. |
| §12 | Párrafo «Revisión posterior». | Registro de la revisión externa. |
| Resumen, §2, §7, §8, §10 | Frases que describían lo que el texto no es, reescritas por lo que es. Firma: Endless Monkey Project · Relational Geometry Program. | Criterio editorial del programa. |
| Laboratorio | Nuevos `E5c`, `bareiss_det`, `rejilla_cociente`, `conectividad_matroide_grafico`; E1 y E3b ampliados. Corrida completa: 250 s, sin errores. | Reproducibilidad de cada número nuevo. |

---

## English

**Version 2 · November 8, 2026.** Relative to the tag `2026-11-08-economia-del-calculo` (commit `552aa0b`). The first four rows answer an external review of the same day, and the fifth a second reading of version 2; the rest come from preparing the review request.

| Section | Change | Reasoning |
| --- | --- | --- |
| §2, Cor. 2.2 | Under permutation, \|P ∧ Q\|·\|P ∨ Q\| = \|P\|·\|Q\| + k²·Cov_J(p_J, q_J). The product law requires permutation and zero covariance. New counterexample: {12 \| 34 \| 5} and {13 \| 24 \| 5} permute and give 10 against 9. | Permutation alone does not fix the law. E1: of 334 permuting pairs, 176 satisfy the law, and the law holds exactly when the covariance vanishes in all 334. |
| §6, Thm. 6.1 | "For every order and every field, some cut has rank 2^Ω(n)." | That is what the argument proves: the middle cut of each order. An arbitrary cut can have low rank (E2: minimum rank 4 to 10 over balanced cuts, n = 8…16). |
| §6, Thm. 6.2 | The Tseitin cut rank is 2^λ(A), with λ the connectivity function of the graphic matroid, for any satisfiable charge. Proof by all-ones blocks. Antecedents: Forney's state space theorem (1994) and Kashyap (2008). The exponential bound is attributed to satisfiable families on expanders; a tree gives rank 1. | Version 1 counted distinct rows and only treated zero charge. E3b now computes the rank directly: 3003 cuts with zero charge, 3003 with random charge and 216 on random graphs. |
| §5.5 | Order 51 is certified: det H_51 ≠ 0, det H_52 = 0 and a nonsingular shifted Hankel matrix (no zero root). Table of orders for widths 1 to 10: 1, 1, 2, 3, 5, 7, 13, 19, 35, 51. Widths 6 and 7 match OEIS A207995 and A207996. | Version 1 based the order on the Hankel rank modulo a prime. New experiment E5c. |
| Summary, §5.5, request | The 51 is stated as the dimension of the minimal linear representation of the count over the rationals. The request separates what is proven from what is asked and opens with the concrete question. | The 51 characterizes that linear representation of the count. The question of its antecedents is distinct from the certified computation. |
| §5.5 and review request, OEIS reference | A207997 contains counts for widths beyond 7; it is not presented as a table of minimal recurrence orders. | Bibliographic correction during the prepublication review of v2. |
| §10 | New resolved row (Tseitin and the graphic matroid); the grid's open question becomes the sequence of orders. Eleven resolved relations. | Follows from the changes above. |
| §10, sign route | Total cost is bounded: how many terms, how they are found, what evaluating and recombining them costs, and exactness for the whole family. | Lowering each term's rank is trivial with rank-one terms. |
| §11 | Rows for E1, E3b and E5c updated; command `E5 E5x E5c`. | Reproduction of the changes. |
| §12 | "Later review" paragraph. | Record of the external review. |
| Summary, §2, §7, §8, §10 | Sentences that described what the text is not, rewritten as what it is. Signature: Endless Monkey Project · Relational Geometry Program. | Editorial standard of the program. |
| Lab | New `E5c`, `bareiss_det`, `rejilla_cociente`, `conectividad_matroide_grafico`; E1 and E3b extended. Full run: 250 s, no errors. | Reproducibility of every new number. |
