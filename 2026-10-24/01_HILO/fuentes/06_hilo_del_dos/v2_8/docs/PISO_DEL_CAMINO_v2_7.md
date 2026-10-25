---
title: "El piso del camino: ningún selector hace polinómico al motor de tablas"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
editorial: "Formalización asistida; respuesta a «¿podrías demostrarlo desde esta perspectiva?» (13-10-2026)"
version: "2.7 — 2026-10-14"
status: "No-go N1 demostrado y verificado sobre los motores O2/O2c v1.6 sin cambios"
---

# El piso del camino

El paquete O2C v1.6 mostró que la pregunta y la disposición cambian el camino y su
costo, aunque la respuesta sea la misma. Esta nota demuestra que **el camino tiene un
piso que ningún selector baja**. Lo fija la relación misma, no el selector ni la
pregunta.

Los motores se copiaron sin cambios en `experiments/o2c_v1_6/`, con sus huellas en el
manifiesto.

- Experimento: `experiments/piso_del_camino_v2_7.py`.
- Pruebas: `tests/test_piso_del_camino_v2_7.py`.
- Resultados: `results/piso_del_camino_v2_7.json`.

## N1-A — Motor O2, sin poda, cualquier orden `DERIVADO`

Para todo grafo G, frontera B y orden σ de los vértices internos:

```text
total_candidates(σ) = Σᵥ 3^(grado_H(v) + 1) + 3^|B|  ≥  3^(tw(G) + 1)
```

H es el grafo de eliminación y tw es el ancho de árbol.

*Prueba.*

1. O2 no borra factores. Al eliminar v saca los factores que lo contienen y agrega uno
   sobre sus vecinos. Eso es exactamente quitar v y unir a sus vecinos entre sí, así que
   la bolsa de v es v junto con sus vecinos en H. La suma es lo que cuenta el motor.
2. Si se completa σ eliminando B al final, la bolsa máxima de todo el recorrido es al
   menos tw(G).
3. Si esa bolsa cae en σ, aporta un término de al menos 3^(tw+1). Si no, entonces
   tw ≤ |B| − 1, y 3^|B| ya alcanza. ∎

Con el mejor orden, el costo es a lo sumo n·3^(tw+|B|+1) + 3^|B|. **Con |B| fija, el
motor es polinómico exactamente cuando tw = O(log n).** Esa es la clase explícita que
pedía O2c §7.

**En el lenguaje del programa:** tw + 1 es la cápsula más grande que hay que sostener a
la vez, minimizando sobre todos los cierres posibles.

## N1-B — Motor O2c, con poda, cualquier selector `DERIVADO`

Si una corrida de O2c concluye que no hay coloración, da una **refutación por
resolución** de la CNF directa de G con a lo sumo 2·total_candidates pasos. La CNF tiene
la cláusula «cada vértice tiene un color» y, por cada arista, «no comparten color».

*Prueba.*

1. Cada fila excluida de cada factor tiene una cláusula derivada que la excluye.
2. Una fila de salida queda excluida sólo si sus tres extensiones violan algún factor.
   Tres resoluciones con «v tiene un color» dan la cláusula de esa fila.
3. Quitar tautologías o duplicados no pierde filas excluidas.
4. Cuando una tabla o la interfaz queda vacía, se resuelve variable por variable hasta
   la cláusula vacía.

El selector no aparece en ningún paso, así que vale para cualquier regla, aun una con
oráculo. ∎

## Corolarios `DERIVADO` (con resultados publicados)

- **Grafos 3-regulares aleatorios.** La cota espectral da tw ≥ nλ₂/(3+λ₂) − 1. Por
  Friedman, λ₂ ≥ 3 − 2√2 − ε casi seguramente, así que tw ≥ 0.054·n − 1. Con N1-A,
  **cualquier orden** cuesta al menos 3^(0.054n).
- **Grafos aleatorios no 3-coloreables con un número lineal de aristas.** Toda
  refutación por resolución tiene tamaño 2^Ω(n) (Beame, Culberson, Mitchell, Moore 2005).
  Con N1-B, **toda corrida de O2c, con cualquier selector,** cuesta 2^Ω(n).

## Lo verificado

| Comprobación | Resultado |
|---|---|
| Igualdad de la fórmula con el contador del motor O2 | exacta, también con B = {0,1} |
| Orden óptimo por programación dinámica (un selector con oráculo), n ≤ 18 | nunca baja de 3^(tw+1); min-fill lo iguala |
| Piso certificado para n = 1600 | 3^90 ≈ 10^42.9 candidatos, cualquier selector |
| Refutaciones construidas desde O2c | 36, comprobadas línea por línea; la réplica coincide con `run()` en orden y costo |

Con n ≤ 18, tw se queda en 3 o 4 y el crecimiento exponencial todavía no se ve. Aparece
con n en los cientos. La parte a escala usa numpy solamente para el autovalor; sin
numpy, se omite.

## Qué significa para P frente a NP

O2 y O2c están en las zonas 2 y 3 del mapa de la v2.4: costo exponencial en el ancho y
búsqueda que hereda las cotas de la resolución.

Para acercarse a P = NP, un motor de cápsulas tendría que producir certificados que
escapen de la resolución y también del álgebra de grado acotado. Para 3-coloración en
grafos aleatorios, Nullstellensatz y el cálculo polinomial necesitan grado lineal
(Conneryd, de Rezende, Nordström, Pang y Risse; Lauria y Nordström 2017).

Más arriba están sistemas sin cotas inferiores conocidas, como Frege. Un algoritmo
polinómico para 3-coloración daría un sistema de pruebas polinómico (Cook–Reckhow).

**Esta nota no decide P frente a NP. Cierra la línea «un selector mejor».**

## Fuentes

- P. Beame, J. Culberson, D. Mitchell, C. Moore, «The resolution complexity of random
  graph k-colorability», *Discrete Applied Math.* 153 (2005); ECCC TR04-012.
- J. Conneryd, S. F. de Rezende, J. Nordström, S. Pang, K. Risse, «Graph colouring is
  hard on average for polynomial calculus and Nullstellensatz», arXiv:2503.17022.
- M. Lauria, J. Nordström, «Graph colouring is hard for algorithms based on Hilbert's
  Nullstellensatz and Gröbner bases», CCC 2017.
- «An improved spectral lower bound of treewidth», arXiv:2404.08520; L. S. Chandran,
  C. R. Subramanian (2003).
- J. Friedman, «A proof of Alon's second eigenvalue conjecture», *Memoirs AMS* (2008).
- S. A. Cook, R. A. Reckhow, «The relative efficiency of propositional proof systems»,
  *J. Symbolic Logic* 44 (1979).
