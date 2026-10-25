---
title: "El 8: la estructura sobre la que crece, con un nodo abierto"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
editorial: "Formalización asistida; suplemento de la v2.1"
version: "2.2 — 2026-10-13"
status: "Lectura del autor + resultados exactos verificados; ninguna derivación física"
---

# El 8: la estructura sobre la que crece, con un nodo abierto

> **Respuesta del autor (13-10-2026).** «El 8 pensaría que es la estructura sobre la
> que crece, pero su naturaleza tiene un nodo abierto.»

Esta respuesta descarta dos lecturas de la v2.1. No es recerrar puro, porque el 8
existe y es estructural. Tampoco es duplicar puro, porque el 8 no es una cápsula
cerrada como las anteriores. Queda una forma precisa de «ambas»: el 8 sostiene el
crecimiento y deja un nodo sin cerrar.

Esta nota muestra que existe un objeto matemático exacto con esa forma, y que ya
estaba latente en el programa. Código: `experiments/ocho_nodo_abierto_v2_2.py`.
Pruebas: `tests/test_ocho_nodo_abierto_v2_2.py`.

---

## 1. La duplicación por reflexión `DEFINICIÓN` · `DERIVADO`

La construcción de Cayley–Dickson duplica un álgebra reflejándola en su conjugación:
de un álgebra A se forman pares (a, b) con

```text
(a, b)(c, d) = (ac − d̄ b,  d a + b c̄)        (a, b)‾ = (ā, −b)
```

Empezando por los reales, cada duplicación pierde una propiedad:

| Dimensión | Álgebra | Qué conserva | Qué pierde |
|---:|---|---|---|
| 1 | Reales | Todo | — |
| 2 | Complejos | Conmutatividad, asociatividad, división | El orden |
| 4 | Cuaterniones | Asociatividad, división | La conmutatividad |
| **8** | **Octoniones** | **División y norma multiplicativa** | **La asociatividad** |
| 16 | Sedeniones | — | La división: (e₁ + e₁₀)(e₄ − e₁₅) = 0 |

**Teorema de Hurwitz** (1898): las únicas álgebras normadas de división son las de
dimensión 1, 2, 4 y 8. `DERIVADO`

**Lectura** `POSTULADO`: el 8 es la estructura sobre la que crece el 16, que se
construye como pares de octoniones, y es la última que conserva la división. Es
literalmente «la estructura sobre la que crece».

El programa ya tenía los niveles anteriores: J² = −I es el nivel 2, y el grupo de
cuaterniones Q₈ junto con su(2) son el nivel 4. El 8 es la continuación natural.

## 2. El 8 son 7 más 1 `DERIVADO`

Las unidades e₀,…,e₇ cumplen e_i · e_j = ± e_(i XOR j). El índice del producto es la
suma en GF(2)³: el destino de una composición lo fija un vector de tres bits.

- **e₀ = 1** es la unidad real: la referencia `1_ref`.
- **Las siete unidades imaginarias** son los siete vectores no nulos: los siete
  puntos del **plano de Fano**, el plano proyectivo más pequeño.
- **Sus siete líneas** son las tripletas con XOR cero:
  {1,2,3}, {1,4,5}, {1,6,7}, {2,4,6}, {2,5,7}, {3,4,7}, {3,5,6}.
- **Cada línea, con la unidad real, es una copia de los cuaterniones.**

En la genealogía del dos, la imagen inferior del centro 2^k cuenta las unidades
imaginarias del álgebra de dimensión 2^k: 1, 3, 7, 15. El 7 que aparece como palabra
nueva en el centro 8 son las siete unidades imaginarias del 8.

## 3. El nodo abierto `DERIVADO`

Tomemos tres unidades imaginarias y compongámoslas por los dos caminos posibles,
(e_i e_j) e_k y e_i (e_j e_k).

- **El destino se cierra siempre.** Ambos caminos llegan a la misma unidad, porque
  XOR es asociativo.
- **La orientación se cierra sólo sobre una línea.** Si k está en la línea de i y j,
  los dos caminos dan el mismo signo. Si los tres índices son independientes, dan
  signos opuestos:

```text
(e_i e_j) e_k = − e_i (e_j e_k)        cuando i, j, k no están en una línea de Fano
```

| Álgebra | Tríos ordenados de unidades imaginarias distintas | Signo cerrado | Signo abierto |
|---|---:|---:|---:|
| Cuaterniones (4) | 6 | 6 | 0 |
| **Octoniones (8)** | **210** | **42** | **168** |

En el 8 queda abierto **exactamente un bit**: la orientación, que depende del camino.
Los 168 tríos abiertos son exactamente los de índices independientes.

**Teorema de Artin.** Dos octoniones cualesquiera generan un subálgebra asociativa.
`DERIVADO` Con dos, la estructura cierra; con un tercero independiente, el nodo
queda abierto.

## 4. El nodo abierto como residuo `DERIVADO`

En el lenguaje de la v2 (§15), sea Ω el conjunto de tríos con sus dos caminos. La
pregunta exterior es «a qué unidad llega». La interior es «a qué unidad y con qué
signo».

| Álgebra | Residuo interior por trío independiente | Residuo medio sobre todos los tríos |
|---|---:|---:|
| Cuaterniones (4) | — | 0 bits |
| **Octoniones (8)** | **1 bit** | **0.8 bits** |

El 8 es una cápsula que el exterior ve cerrada, porque el destino está fijado, con un
residuo interior de un bit, porque la orientación guarda el camino. Ésa es la forma
exacta de «una estructura con un nodo abierto».

## 5. Qué cambia en el programa

**La decisión pendiente queda resuelta así** `POSTULADO`, a confirmar por el autor:

| Nivel | Qué cierra | Estado |
|---:|---|---|
| 1, 2, 4 | Destino y orientación | Cápsulas cerradas |
| **8** | **El destino; la orientación queda abierta** | **Estructura de crecimiento con un nodo abierto** |
| 16 | Ni la división | Crece sobre el 8 y se rompe |

**Dos hechos en el mismo lugar, sin mecanismo común demostrado** `ABIERTO`. En la
genealogía multiplicativa, el centro 8 es la única excepción de Zsigmondy: el 9 no
trae palabra nueva. En el álgebra, el 8 es el primer nivel no asociativo. Coinciden
en el número; que respondan al mismo mecanismo está por demostrar y no se afirma.

**La hipótesis de masa como residuo** `CONTRASTE` pendiente. Si la masa es residuo
interior bajo cierre exterior, la primera estructura que lo tiene es la del 8. Esto
compromete al programa con una línea ya existente en física teórica, la de los
octoniones y el Modelo Estándar, frente a la cual debe posicionarse antes de afirmar
nada. La puerta de entrada a esa literatura es la revisión de Baez.

## 6. Pregunta para el autor `ABIERTO`

> ¿El nodo abierto del 8 es la orientación que depende del camino, es decir, que en
> el 8 la historia de la composición importa?

Si la respuesta es sí, el programa obtiene una tesis precisa: hasta el 4, una unidad
cerrada olvida cómo se agrupó; en el 8, conserva un bit de esa agrupación. (El orden de
los factores ya cuenta desde el 4; precisado en la v2.5.)

> **Respondida en la v2.3.** El autor lo acepta y pregunta si ese bit es relacionable
> o queda congelado. La respuesta, con el teorema T7, está en `docs/EL_BIT_ABIERTO_v2_3.md`.

## 7. Adiciones a la matriz epistémica

| Enunciado | Etiqueta | Prueba |
|---|---|---|
| Cada duplicación pierde una propiedad; el 16 tiene divisores de cero | DERIVADO | `test_cada_duplicacion_pierde_una_propiedad`, `test_divisores_de_cero_solo_en_16` |
| e_i e_j = ± e_(i XOR j) | DERIVADO | `test_el_indice_es_xor` |
| Siete líneas de Fano; cada una es una copia de los cuaterniones | DERIVADO | `test_siete_lineas_de_fano`, `test_lineas_son_cuaterniones_y_pares_cierran` |
| En el 8 el signo queda abierto exactamente fuera de las líneas | DERIVADO | `test_ocho_deja_abierto_el_signo_fuera_de_las_lineas` |
| Residuo de un bit por trío independiente | DERIVADO | `test_un_bit_por_trio_independiente` |
| El 8 como estructura de crecimiento con nodo abierto | POSTULADO, del autor | — |
| Zsigmondy y no asociatividad en el 8 responden a un mismo mecanismo | ABIERTO | — |
| Masa como residuo del tipo del 8 | CONTRASTE pendiente | — |

## Fuentes

- John C. Baez, «The Octonions», *Bulletin of the AMS* 39 (2002): https://arxiv.org/abs/math/0105155
  (construcción de Cayley–Dickson, teorema de Hurwitz, plano de Fano y teorema de Artin).
