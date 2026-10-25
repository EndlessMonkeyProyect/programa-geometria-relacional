---
title: "Las cuatro referencias: lo escrito y lo que aún necesita una diferencia"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
editorial: "Depuración ontológica y tipado de la interpretación física de T8"
version: "2.8 — 2026-10-14"
status: "Geometría combinatoria demostrada; emergencia física abierta"
---

# T8: de las cuatro referencias al espacio de comparación

## 1. El hilo no empieza en un sistema de coordenadas `POSTULADO`

El programa parte de la diferencia y de qué puede distinguir y sostener un
lenguaje. Sólo después aparecen los números, las comparaciones y sus posibles
realizaciones geométricas. «Cuatro referencias al mismo radio» es primero una
propuesta **relacional**, no cuatro puntos ya puestos en un espacio físico.

El autor comenzó a formular que **mientras sean cuatro se pueden escribir**
las relaciones, pero dejó la frase sin completar. Tomamos esa intuición como
pregunta de investigación, **no como un enunciado ya establecido por el autor**.
La exigencia distinta que podría introducir una quinta referencia queda por
formular; no se sustituye el argumento por una geometría elegida de antemano.

## 2. Representación que sí está demostrada `DERIVADO`

Con n distinciones binarias independientes representamos los 2^n estados por
todas sus paridades no triviales (los 2^n−1 subconjuntos no vacíos de las n
coordenadas). Para dos estados diferentes, exactamente 2^(n−1) paridades los
separan. Es el código símplex binario. Para n=2:

- 4 estados, 3 paridades no triviales y distancia de Hamming 2 entre cualquier par.
- Con la inmersión de los bits en R³, los 4 vectores son vértices de un tetraedro
  regular; cuatro equidistantes son el máximo en R³.
- La suma XOR de los cuatro estados es cero: cualquiera de tres determina el cuarto;
  la identidad es simétrica y **no designa a una referencia privilegiada**.

### Familia T8(n), no sólo su caso preferido

| Distinciones n | Estados 2^n | Paridades 2^n−1 | Distancia Hamming |
|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 |
| 2 | 4 | 3 | 2 |
| 3 | 8 | 7 | 4 |
| 4 | 16 | 15 | 8 |

Este mismo método puede representar 8 estados como símplex en R⁷, o 16 en R¹⁵.
Por tanto, **n=2 no se deduce de la mera construcción del código**. El programa
requiere una regla ontológica adicional que seleccione exactamente esas dos
distinciones, o una prueba de que sólo n=2 satisface alguna condición independiente.

## 3. Quinta referencia: qué obliga y qué no `DERIVADO condicional`

Dados cuatro puntos afínmente independientes en R³, un quinto no puede ser
equidistante de todos ellos y de los demás con una distancia común positiva.
Las diez distancias entre cinco puntos en R³ satisfacen una relación de
compatibilidad (determinante de Cayley–Menger = 0). Cuatro puntos ya tienen
seis distancias y, localmente, no se exige una ecuación de ese tipo.

Eso prueba una restricción **una vez que se seleccionó R³**. No demuestra que
la quinta referencia cree la distancia física. De hecho, cinco puntos
equidistantes existen en R⁴: forman un símplex regular de dimensión cuatro.

Tampoco «no tener restricciones entre distancias» equivale a «no tener métrica»:
la distancia de Hamming ya es una métrica sobre palabras, y la realización en
R³ incorpora su métrica euclidiana. El momento en que el programa introduce
**distancia medible con unidades físicas** debe derivarse por otra regla.

## 4. Pregunta ontológica que preservamos `ABIERTO`

> ¿Cuál es la capacidad de descripción de un cierre de cuatro referencias y cuál
> es la primera relación adicional que obliga a refinar ese lenguaje cuando se
> pretende incorporar una quinta, sin presuponer ni R³ ni una unidad de longitud?

Esta pregunta tiene prioridad sobre seleccionar coordenadas o interpretar radios
como masas. Una vía verificable sería especificar:

1. Un lenguaje L₄ de relaciones representables con cuatro referencias, sin métrica.
2. Una nueva relación ρ₅ concreta y una prueba de que **no** es definible en L₄
   (por ejemplo, dos modelos indistinguibles en L₄ que ρ₅ sí distinga).
3. La extensión mínima de L₄ que permite describir ρ₅, y el número de nuevas
   comparaciones requeridas.
4. Sólo después, una construcción de métrica y un criterio externo para la
   dimensión espacial, la escala y los observables físicos.

Si se construyen dos realizaciones relacionales con iguales datos L₄ pero
comportamiento distinto de ρ₅, se demostraría que L₄ no alcanza. Si L₄ ya
determina ρ₅, la idea de que la quinta exige nueva información, tal como está
formulada, quedaría refutada o requeriría redefinición. Esta es una forma
operativa de aplicar la **regla R** del documento principal.

## 5. Etiquetas de continuidad

- `DERIVADO`: conteo 2^n, código símplex, distancias de Hamming, tetraedro
  **condicional** en R³, simetría de la relación de cuatro estados, restricciones
  euclidianas de Cayley–Menger.
- `POSTULADO`: cuatro como actualidad del cierre y la lectura del tres y uno
  sin escoger cuál; la quinta como evento de nueva distinción.
- `ABIERTO`: selección ontológica de n=2, demostración de necesidad de nueva
  información antes de una métrica, emergencia de tres dimensiones físicas,
  conversión a longitudes observables.

**Regla editorial:** no volver a llamar «demostrada» a la emergencia física en
base a identidades de representaciones elegidas. Esto precisa el alcance de la
nota `DEL_CUATRO_A_LA_DISTANCIA_Y_EL_TIEMPO_v2_7.md` sin borrar la formulación
del autor ni las construcciones matemáticas que sí son exactas.

## 6. Control reproducible

`experiments/t8_familia_v2_8.py`, `tests/test_t8_familia_v2_8.py` y
`results/t8_familia_v2_8.json` calculan T8(n) para n=1,2,3,4 y la pauta de
distancias [1,1,1,3] de las cuatro palabras exteriores al código de n=2.
Son controles de la representación elegida, no de la tesis física.
