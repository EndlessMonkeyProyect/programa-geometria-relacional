---
title: "Revisión de las pruebas de la §7 con implementación propia"
subtitle: "El cruce como reflejo central · Proposiciones 1–3 y Corolario 4"
author: "DeepSeek, modelo de IA (2026-11-03)"
lang: es
---

# Revisión de las pruebas de la §7 con implementación propia

**Paper:** «El cruce como reflejo central» · §7 *La cadena de duplicación: por qué el 8*
**Revisor:** DeepSeek, modelo de IA · 3 de noviembre de 2026
**Método:** reimplementación independiente de la duplicación de Cayley–Dickson (sin usar los verificadores del paquete) y comprobación paso a paso con enteros exactos y rangos de matrices.

## Veredicto

**Las cuatro pruebas son correctas.** Cada paso de las Proposiciones 1–3 y del Corolario 4 fue re-derivado y verificado numéricamente para los niveles N = 2, 4, 8, 16. No se encontró ningún error matemático. Hay **una** observación de claridad (no un error) en la Proposición 3.

---

## Proposición 1 — La duplicación da la identidad del cruce [correcta]

Afirma: en los niveles 2, 4 y 8, R + C = 2·[x=v][y=u].

**Pasos verificados:**

1. **Multiplicatividad de la norma** (Hurwitz 1898) ⇒ (Σa²)(Σb²) = Σ_k (Σ_{p⊕q=k} σ a_p b_q)². Verificado: es exactamente la propiedad de composición en N = 1, 2, 4, 8.
2. **Identidad (28):** el coeficiente del monomio a_p a_p′ b_q b_q′ es 2[σ(p,q)σ(p′,q′) + σ(p,q′)σ(p′,q)] y debe anularse. Verificado: el número de violaciones de (28) es **0** en N = 2, 4, 8 y **672** en N = 16.
3. **R = [x⊕y=v⊕u] σ(x,y)σ(v,u)** y **C = [x⊕u=v⊕y] σ(x,u)σ(v,y)**: verificado entrada a entrada.
4. Casos y = u (⇒ x = v, R = C = 1) e y ≠ u (⇒ R + C = 0 por (28)): verificado exhaustivamente en N = 2, 4, 8.

---

## Proposición 2 — Las direcciones son órdenes [correcta]

Afirma: R = (LᵥᵀLₓ)ᵤ,ᵧ, C = (LₓᵀLᵥ)ᵤ,ᵧ, y LᵥᵀLₓ + LₓᵀLᵥ = 2[x=v]·Id.

**Pasos verificados:**

1. (LᵥᵀLₓ)ᵤ,ᵧ = Σ_k ψ_k(v,u)ψ_k(x,y) = R: verificado.
2. (LₓᵀLᵥ)ᵤ,ᵧ = Σ_k ψ_k(x,u)ψ_k(v,y) = C: verificado.
3. Relación de Hurwitz–Radon LᵥᵀLₓ + LₓᵀLᵥ = 2[x=v]·Id: **verificada** para todo x, v en N = 2, 4, 8 (y, correctamente, **falla** en N = 16).

---

## Proposición 3 — Solo el 8 abarata [correcta]

Afirma: rangos de R (filas, columnas) = (2,2), (4,16), (8,64) para N = 2, 4, 8; costo 4/4, 8/8, 11/12; en N = 16 la identidad (28) falla en 672 casos.

**Pasos verificados:**

1. **ΦΦᵀ = N·Id**: con Φ[k,(x,y)] = ψ_k(x,y), cada (x,y) cae en un único k ⇒ ΦΦᵀ = N·Id. Verificado.
2. **R = ΦᵀΦ, R² = N·R, rango por filas = N**: verificado en la matricización correcta. Ver nota ⚠ abajo.
3. **C = 2·Id − R** (cruce = identidad en esa matricización) y sus autovalores 2−N (multiplicidad N) y 2 (multiplicidad N²−N): verificado ⇒ rango de C por filas = N² (N ≠ 2) o 2 (N = 2).
4. **Paso delicado — «el rango de R por columnas es el de C por filas, porque C(x,y,u,v) = R(x,u,y,v)»**: verificado entrada a entrada. **R por columnas y C por filas son literalmente la misma matriz** (R_cols[(x,u),(y,v)] = C_filas[(x,y),(u,v)] = R(x,y,u,v) bajo el mismo etiquetado (p,q)×(r,s)). El paso es correcto.
5. **Rangos finales** (filas, columnas): (2,2), (4,16), (8,64) — verificados. **Costos** 4, 8, 11 frente a 4, 8, 12 — verificados.
6. **N = 16**: (28) falla en 672 casos; R + C deja de ser múltiplo del cruce — verificado.

⚠ **Observación de claridad (no es error).** En «R = ΦᵀΦ», la matriz usa **columnas indexadas por (v,u)**, no por (u,v). El paper lo dice («Con columnas indexadas por (v, u)»), pero un revisor puede tropezar: en el corte por filas convencional las columnas son (u,v), y con ese orden R² = N·R **no** vale literalmente (vale con columnas (v,u)). Sugerencia: añadir un paréntesis explícito, p. ej. «nótese el orden (v,u) de las columnas, distinto del corte por filas habitual (u,v)». El rango es invariante bajo permutación de columnas, así que la conclusión (rango N por filas) no se ve afectada.

---

## Corolario 4 — Abaratar exige el nodo abierto [correcta]

Afirma: el único nivel que abarata es el 8, y el 8 no es asociativo.

**Pasos verificados:**

1. La ganancia exige N > 4 y que valga (28): verificado (solo N = 8 gana en la tabla).
2. Todo nivel posterior contiene al 16 como subálgebra con la misma tabla de signos ⇒ también falla: correcto (la duplicación de nivel 2k contiene al nivel k como primer componente).
3. **Asociatividad**: N = 2, 4 asociativos; N = 8 no asociativo (Frobenius 1878). Verificado.
4. **Conteo «168 de 210»**: verificado de forma independiente — exactamente **168 de los 210 tríos** de unidades no nulas y distintas de los octoniones son no asociativos. La afirmación de la nota del 13 de octubre es correcta.

---

## Tabla de verificación

| Afirmación | N = 2 | N = 4 | N = 8 | N = 16 |
|---|---|---|---|---|
| e_p e_q = σ e_{p⊕q} | ✓ | ✓ | ✓ | ✓ |
| R + C = 2·cruce | ✓ | ✓ | ✓ | ✗ (correcto) |
| identidad (28): 0 violaciones | ✓ | ✓ | ✓ | ✗ (672, correcto) |
| Hurwitz–Radon | ✓ | ✓ | ✓ | ✗ (correcto) |
| R² = N·R (matriz (v,u)) | ✓ | ✓ | ✓ | ✓ (estructural) |
| R por columnas = C por filas | ✓ | ✓ | ✓ | ✓ (estructural) |
| rangos (filas, columnas) | (2,2) | (4,16) | (8,64) | (16,256) |
| costo bloque / cruce | 4/4 | 8/8 | 11/12 | — |
| asociatividad | ✓ | ✓ | ✗ | ✗ |

**Conclusión: sin errores. Recomendado añadir un paréntesis sobre el orden (v,u) de las columnas en la Proposición 3.**

---

*Esta revisión la hizo DeepSeek, un modelo de IA, con una implementación propia; no es una revisión humana y no sustituye la revisión por pares externa. El script de la revisión está en `review_pruebas_sec7.py`.*
