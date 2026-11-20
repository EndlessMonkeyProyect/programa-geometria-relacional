# Cambios · Changes

Endless Monkey Project  
Relational Geometry Program

[Español](#español) · [English](#english)

---

## Español

**Revisión · 19 de noviembre de 2026.** Respecto de la etiqueta `2026-11-08-economia-del-calculo-v2`. Responde a una revisión matemática externa del 19 de noviembre ([u/DifficultAvocado6185](https://www.reddit.com/r/combinatorics/comments/1xrkk9h/comment/19sw59dkcp4io/)); el detalle está en el [anexo](revision_2026-11-19/ANEXO_ECONOMIA_ES.md).

| Sección | Cambio | Justificación |
| --- | --- | --- |
| Anexo, Q2 | Identidad de ciclos del grafo de intersecciones y teorema 3: k·\|P ∧ Q\| = \|P\|·\|Q\| + k²·Cov_J − k·δ para cualquier par de particiones, con δ el defecto de intersecciones. La ley del producto vale exactamente cuando k·Cov_J = δ. Ejemplo B: {a \| bcd \| ef} y {a \| be \| cf \| d} cumplen la ley sin permutar. | Corrige la afirmación 1 de la solicitud, que pedía permutación y covarianza nula. Búsqueda exhaustiva: ningún ejemplo con cinco elementos o menos; con seis, 720 pares ordenados. La equivalencia entre permutación y completitud bipartita es la de Ore (1942) y Birkhoff (1948). |
| Anexo, Q1 | Fórmula de Burnside para las órbitas. El orden mínimo es el número de autovalores distintos que tocan al vector de unos, y la actividad va por factores irreducibles. | Lee la tabla de órdenes en términos espectrales y muestra por qué bastan los determinantes de E5c (matriz de Gram). |
| Anexo, Q1 | Cálculo exacto para w = 1…10: el polinomio característico del cociente es t^z·f·g, con f irreducible, activo y de grado d_w. En el ancho 10, 136 = 51 + 40 + 45. | Reparte la brecha o_w − d_w de la ecuación (9) del anexo. La forma general y la relación con XXZ quedan como preguntas abiertas. |
| README, §12, solicitud (afirmaciones 1 y 7) | Enlaces al anexo y redacción de la ley del producto. | Consecuencia de las filas anteriores. |
| Verificación | `verificar_revision.py` (sin dependencias), `brecha_exacta.py` (sympy) y nueva corrida de E5, E5x y E5c; registro en `registro_verificacion.txt`. | Reproducibilidad de cada número nuevo. |

**Versión 2 · 8 de noviembre de 2026.** Respecto de la etiqueta `2026-11-08-economia-del-calculo` (commit `552aa0b`). Las cuatro primeras filas responden a una revisión externa del mismo día, y la quinta a una segunda lectura de la versión 2; las demás vienen de la preparación de la solicitud de revisión.

| Sección | Cambio | Justificación |
| --- | --- | --- |
| §2, cor. 2.2 | Con permutación, \|P ∧ Q\|·\|P ∨ Q\| = \|P\|·\|Q\| + k²·Cov_J(p_J, q_J). Dentro de la clase de pares que permutan, la ley del producto equivale a covarianza nula. Contraejemplo a que baste la permutación: {12 \| 34 \| 5} y {13 \| 24 \| 5} permutan y dan 10 frente a 9. | La permutación sola no fija la ley. E1: de 334 pares que permutan, 176 cumplen la ley, y la ley vale exactamente cuando la covarianza es nula en los 334. |
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

**Revision · November 19, 2026.** Relative to the tag `2026-11-08-economia-del-calculo-v2`. It answers an external mathematical review of November 19 ([u/DifficultAvocado6185](https://www.reddit.com/r/combinatorics/comments/1xrkk9h/comment/19sw59dkcp4io/)); details are in the [appendix](revision_2026-11-19/APPENDIX_ECONOMY_EN.md).

| Section | Change | Reasoning |
| --- | --- | --- |
| Appendix, Q2 | Cycle identity of the intersection graph and Theorem 3: k·\|P ∧ Q\| = \|P\|·\|Q\| + k²·Cov_J − k·δ for every pair of partitions, with δ the intersection defect. The product law holds exactly when k·Cov_J = δ. Example B: {a \| bcd \| ef} and {a \| be \| cf \| d} satisfy the law without permuting. | Corrects claim 1 of the request, which required permutation and zero covariance. Exhaustive search: no example on five elements or fewer; on six, 720 ordered pairs. The equivalence between permutation and bipartite completeness is that of Ore (1942) and Birkhoff (1948). |
| Appendix, Q1 | Burnside formula for the orbits. The minimal order is the number of distinct eigenvalues that touch the all-ones vector, and activity goes by irreducible factors. | Reads the table of orders in spectral terms and shows why the E5c determinants suffice (Gram matrix). |
| Appendix, Q1 | Exact computation for w = 1…10: the characteristic polynomial of the quotient is t^z·f·g, with f irreducible, active and of degree d_w. At width 10, 136 = 51 + 40 + 45. | Splits the gap o_w − d_w of equation (9) of the appendix. The general form and the relation to XXZ remain open questions. |
| README, §12, request (claims 1 and 7) | Links to the appendix and wording of the product law. | Follows from the rows above. |
| Verification | `verificar_revision.py` (no dependencies), `brecha_exacta.py` (sympy) and a new run of E5, E5x and E5c; log in `registro_verificacion.txt`. | Reproducibility of every new number. |

**Version 2 · November 8, 2026.** Relative to the tag `2026-11-08-economia-del-calculo` (commit `552aa0b`). The first four rows answer an external review of the same day, and the fifth a second reading of version 2; the rest come from preparing the review request.

| Section | Change | Reasoning |
| --- | --- | --- |
| §2, Cor. 2.2 | Under permutation, \|P ∧ Q\|·\|P ∨ Q\| = \|P\|·\|Q\| + k²·Cov_J(p_J, q_J). Within the class of permuting pairs, the product law is equivalent to zero covariance. Counterexample to permutation alone: {12 \| 34 \| 5} and {13 \| 24 \| 5} permute and give 10 against 9. | Permutation alone does not fix the law. E1: of 334 permuting pairs, 176 satisfy the law, and the law holds exactly when the covariance vanishes in all 334. |
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
