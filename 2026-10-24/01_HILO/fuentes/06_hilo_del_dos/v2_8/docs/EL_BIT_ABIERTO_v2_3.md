---
title: "El bit abierto del 8: real, relacional, latente y de orden"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
editorial: "Formalización asistida; suplemento de la v2.2"
version: "2.3 — 2026-10-13"
status: "Resultados exactos sobre unidades + lectura ontológica acordada con el autor; ninguna derivación física"
---

# El bit abierto del 8

> **Pregunta del autor (13-10-2026).** «¿Ese bit es relacionable? ¿Está disponible
> para resolver, o queda congelado en la eternidad sin comparación de tiempo?»
>
> **Respuesta, acordada con el autor.** Es relacionable y es resoluble. No queda
> congelado: es permanente como estructura y está disponible como relación.

Esta nota formaliza esa respuesta (T7) y la escribe en el lenguaje de la ontología:
postulados P0–P5, regla R y residuo. Código: `experiments/bit_abierto_v2_3.py`.
Pruebas: `tests/test_bit_abierto_v2_3.py`. Se apoya en la construcción exacta de la
v2.2 (`experiments/ocho_nodo_abierto_v2_2.py`).

**Alcance.** Todo lo que sigue vale para las **unidades**, es decir, para las
distinciones puras. Entre elementos generales del 8, la diferencia entre dos caminos
es un elemento completo (el asociador), no sólo un signo.

---

## 1. Los dos lenguajes `DEFINICIÓN`

Siguiendo P1, lo que hay es el cociente de un conjunto de casos bajo un lenguaje.

- **Distinciones.** Las siete unidades imaginarias e₁,…,e₇ del 8; su índice es un
  vector no nulo de GF(2)³. La unidad real e₀ = 1 es la referencia.
- **Historias.** Ω = sucesiones ordenadas de distinciones junto con una agrupación,
  es decir, un orden de composición. Para tres: (e_i e_j) e_k o e_i (e_j e_k).
- **Lenguaje de destinos L_D.** Pregunta «a qué unidad llega la historia».
- **Lenguaje de historias L_H.** Pregunta «a qué unidad llega y con qué signo».

L_H refina a L_D. **El bit abierto** es lo que L_H distingue y L_D no: en el lenguaje
de la v2 (§15), el residuo H(L_H | L_D).

## 2. Teorema T7 `DERIVADO`

En el álgebra de dimensión 8, para historias de unidades:

| | Enunciado | Comprobación exacta | Prueba |
|---|---|---|---|
| **(a) Real** | Ninguna convención de signos lo elimina | Las 2⁷ = 128 convenciones e_i → ±e_i dejan abiertos los mismos 168 de 210 tríos | `test_a_real_ninguna_convencion_lo_elimina` |
| **(b) Relacional** | No está en ningún camino; aparece al comparar dos | (e_i e_j) e_k − e_i (e_j e_k) = ±2·e_(i⊕j⊕k) si i, j, k son independientes, y 0 si están en una línea. Ejemplo: (1, 2, 4) da 2·e₇ | `test_b_relacional_la_comparacion_completa_el_cubo` |
| **(c) Latente** | Una unidad cerrada no lo muestra; reaparece al relacionarse | Para cada e_i e_j, 4 de las 5 unidades restantes lo reabren; sólo la de su propia línea, e_(i⊕j), lo deja cerrado | `test_c_latente_cuatro_terceras_reabren` |
| **(d) De orden** | Toda historia deja el mismo destino y a lo sumo un bit | Con 3 unidades distintas, abierto en 168 de 210 historias; con 4, en 840 de 840; con 5, en 2520 de 2520 | `test_d_a_lo_sumo_un_bit_para_cualquier_historia` |
| **(e) Con límite** | Sobre el 8 se conserva; sobre el 16 puede anularse | En el 16 hay 336 pares (e_a ± e_b)(e_c ± e_d) = 0: los signos opuestos se cancelan | `test_e_en_16_los_signos_se_cancelan` |

Control: en los cuaterniones, el 4, ningún trío abre el signo
(`test_cuaterniones_no_tienen_bit_abierto`).

**Sobre (b).** Tres unidades independientes generan las siete. Ellas mismas y sus
productos de a pares alcanzan seis: i, j, k, i⊕j, i⊕k, j⊕k. La comparación de los dos caminos
apunta exactamente a la séptima, i⊕j⊕k. El bit sólo se hace visible en el punto que
completa la relación entre las tres.

**Sobre (d).** Que haya a lo sumo un bit se sigue de e_i e_j = ± e_(i⊕j) (v2.2, §2):
el destino de una historia es la suma de sus índices y sólo el signo puede variar. Lo
que agrega la prueba es que, desde cuatro unidades, **toda** historia lo tiene abierto.

## 3. Las tres respuestas `DERIVADO` · `POSTULADO`

**¿Es relacionable?** Sí, y sólo así existe. Ningún camino aislado lo contiene; aparece
al compararlo con otro, por (b). Ésta es la forma del 8 de la tesis del programa:
lo que hay son relaciones entre construcciones, no propiedades de una sola.

**¿Está disponible para resolver?** Sí, de dos maneras, ambas dentro de la regla R:

1. **Refinar el lenguaje.** La relación «por qué camino se compuso» no desciende al
   cociente de L_D, y sí al de L_H. Por P5, en L_D no es representable; en L_H, sí.
   Resolver el bit es pasar a un lenguaje que conserve el orden de composición.
2. **Comparar.** Sin refinar el lenguaje, poner dos historias lado a lado lo
   determina: la diferencia vale 0 o ±2·e_(i⊕j⊕k).

**¿Queda congelado?** No. Por (a), no se puede quitar: es **permanente como
estructura**. Por (c), duerme en lo cerrado y despierta cuando lo cerrado entra en
relación con una tercera distinción independiente: está **disponible como relación**.
Por (d), no crece con la historia: una historia larga no acumula más que un bit de
orden.

## 4. En el lenguaje de la ontología `POSTULADO`, salvo donde se indica

| Postulado | Cómo aparece el bit |
|---|---|
| **P0 · unidad** | e₀ = 1 nunca abre el bit: un trío que incluye la referencia siempre cierra, y agregarla a una historia no cambia su bit. La unidad sostiene; el bit vive entre distinciones. `DERIVADO` |
| **P1 · describibilidad** | El bit no es un objeto nuevo: es la diferencia entre dos cocientes del mismo Ω, el de L_H y el de L_D. |
| **P2 · economía** | L_D es más barato y pierde a lo sumo un bit por historia. Un lenguaje económico elige L_D cuando el orden no importa y L_H cuando sí. |
| **P3 · hilo** | El 8 crece sobre el 4: cada una de sus siete líneas, con la unidad real, es una copia de los cuaterniones (v2.2). El 16 crece sobre el 8 y ahí el bit puede cancelarse, por (e). El hilo sigue; el bit tiene borde. |
| **P4 · reflexión** | T4 dice que un sistema reflexivo conserva siempre una pregunta abierta. El bit es la forma algebraica más chica conocida en el programa de algo permanente que, aun así, se responde caso por caso. Es una lectura, no una consecuencia de T4. |
| **P5 · regla R** | El orden de composición es representable en L_H y no en L_D (§3). `DERIVADO` |

**El orden como primer registro del antes y el después.** Hasta el 4, una unidad
cerrada olvida cómo se agrupó, es decir, qué pareja se juntó primero; el orden de los
factores ya cuenta desde el 4 (precisado en la v2.5). En el 8 guarda además un bit de
la agrupación. La
tesis del autor (T7, lectura del orden) es que ese bit es la forma mínima del antes y
el después: el lugar donde la comparación de ritmos, el tiempo del programa, encuentra
su forma más chica. **El paso al tiempo físico es hipótesis** `ABIERTO`.

## 5. Como residuo `DERIVADO`

Visto desde fuera, por L_D, el destino del 8 está fijado. Visto desde dentro, por L_H,
queda el bit. Con peso uniforme sobre los tríos y sus dos caminos, el residuo es de
1 bit por trío independiente y 0.8 bits en promedio (168/210; v2.2, §4). Es la primera
cápsula del programa con **residuo interior bajo cierre exterior**: el tipo de
estructura que nombra la hipótesis de masa como residuo, que sigue `CONTRASTE`
pendiente con el protocolo de la v2.1 (un parámetro fijado por μ/e, predicción de τ/e).

## 6. Lo que no se afirma

- Que el bit sea el tiempo físico.
- Que la masa sea este residuo; sólo que el 8 es la primera estructura del tipo.
- Que la excepción de Zsigmondy en el centro 8 y la no asociatividad del 8 respondan
  a un mismo mecanismo: coinciden en el número, sigue `ABIERTO`.
- Nada sobre elementos generales del 8 más allá de las unidades.

## 7. Adiciones a la matriz epistémica

| Enunciado | Etiqueta | Prueba |
|---|---|---|
| T7 (a) real: invariante bajo las 128 convenciones | DERIVADO | `test_a_real_ninguna_convencion_lo_elimina` |
| T7 (b) relacional: la comparación da ±2·e_(i⊕j⊕k) | DERIVADO | `test_b_relacional_la_comparacion_completa_el_cubo` |
| T7 (c) latente: 4 de 5 terceras unidades lo reabren | DERIVADO | `test_c_latente_cuatro_terceras_reabren` |
| T7 (d) de orden: mismo destino, a lo sumo un bit | DERIVADO | `test_d_a_lo_sumo_un_bit_para_cualquier_historia` |
| T7 (e) con límite: cancelación en el 16 | DERIVADO | `test_e_en_16_los_signos_se_cancelan` |
| La referencia e₀ nunca abre el bit (P0) | DERIVADO | `test_la_referencia_no_abre_el_bit` |
| El bit es relacionable, resoluble y no congelado | DERIVADO desde (a)–(d); acordado con el autor | — |
| El bit es la forma mínima del antes y el después | POSTULADO, del autor | — |
| El bit es el tiempo físico | ABIERTO | — |

## Reproducir

```bash
python -m unittest tests.test_bit_abierto_v2_3 -v
python experiments/bit_abierto_v2_3.py
```

## Fuentes

- John C. Baez, «The Octonions», *Bulletin of the AMS* 39 (2002): https://arxiv.org/abs/math/0105155
  (construcción de Cayley–Dickson, plano de Fano, teorema de Artin, divisores de cero
  en los sedeniones).
