---
title: "El piso del camino: demostración inductiva y prioridad de resolución"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
editorial: "Extensión de prueba y alcance; no reescribe la ontología"
version: "2.8 — 2026-10-14"
status: "Teorema condicional para el motor O2c definido; puente a cotas externas sujeto a sus hipótesis"
---

# Del lenguaje de resolución al certificado: N1-B

## 1. Antes del cálculo: lo que expresa el programa `POSTULADO`

La solución no depende del orden en que se formulen las preguntas, pero el camino sí.
Una relación que excluye una posibilidad puede escribirse como una afirmación nueva;
la prioridad indica qué diferencias atender primero, **no modifica las reglas que
permiten acreditar una exclusión**. La prioridad fija propuesta por el autor
(14-10-2026) pertenece a este caso. Esta distinción entre respuesta y costo conserva
el lenguaje ontológico: diferencia → exclusión → recierre → certificado.

## 2. Objeto preciso `DEFINICIÓN`

Sea un grafo simple finito G=(V,E), con colores {0,1,2}; B ⊆ V es una frontera fija.
Partimos de la CNF F_G con variables booleanas x_(v,c):

- ALO(v): x_(v,0) ∨ x_(v,1) ∨ x_(v,2), para cada vértice v.
- EDGE(u,v,c): ¬x_(u,c) ∨ ¬x_(v,c), para cada arista {u,v} y cada color c.

No se necesita imponer exactamente un color por vértice: si una valoración satisface
esta CNF, elegimos para cada vértice cualquiera de sus colores verdaderos; por EDGE
los extremos de una arista nunca pueden elegir el mismo. Así, F_G es satisfacible
si y sólo si G es 3-coloreable.

El motor O2c v1.6 trabaja con factores extensionales (S, R), donde R ⊆ {0,1,2}^S.
En cada paso selecciona v ∉ B, reúne todos los factores que contienen v, enumera
las 3^|U| asignaciones de su unión de ámbitos U, proyecta v y guarda el factor
resultante sobre T = U sin {v}. Su normalización solamente suprime factores universalmente
verdaderos o duplicados, y convierte una tabla vacía en la contradicción global.
Al final, si no se detectó antes una tabla vacía, enumera las 3^|B| asignaciones
de frontera. `total_candidates` suma esos costos de enumeración de **tablas**, y no
contabiliza el tiempo del selector ni el coste total de implementar las tablas.

Una **prioridad fija por vértices**, caso simple del criterio propuesto, es una
permutación π de V: el selector toma el primer v pendiente fuera de B según π.
Una **regla fija de prioridad** puede asimismo recalcular qué factor ya tiene
exclusiones acreditadas, siempre que únicamente escoja el siguiente v. La prueba
cubre ambas: nada en la inducción depende de cómo se eligió v.

## 3. Invariante de las filas excluidas `DERIVADO`

Para toda fila a excluida por un factor de ámbito S existe una cláusula C_a
**derivada por resolución de F_G** que cumple:

    C_a ⊆ { ¬x_(u,a(u)) : u ∈ S }.

Esta inclusión es más fuerte que decir simplemente que C_a es válida: la propia
fila a falsifica C_a, y ninguna variable fuera de S aparece en ella.

### Base

En un factor de arista {u,v}, la única clase de filas excluidas es a(u)=a(v)=c.
La cláusula EDGE(u,v,c) pertenece a F_G y satisface la inclusión.

### Paso: eliminación de v

Sea b una fila de salida sobre T que no sobrevive. Para cada color c, la extensión
b∪{v↦c} viola alguno de los factores de entrada. Por inducción, disponemos de
C_c ⊆ {¬x_(u,b(u)):u∈T} ∪ {¬x_(v,c)}.

Si algún C_c carece del literal ¬x_(v,c), **ya es** testigo para b.
De lo contrario, resolvemos sucesivamente ALO(v) con C_0, C_1 y C_2, usando los
pivotes x_(v,0), x_(v,1), x_(v,2). El resultado contiene solamente negaciones
de literales de b, por lo que cumple el invariante. No aparecen tautologías:
los antecedentes sólo contienen los positivos restantes de ALO(v) y negativos
correspondientes a los colores ya eliminados. Son a lo sumo **tres** inferencias.

### Normalización y detención anticipada

Eliminar un factor universalmente verdadero no elimina testigos de filas
excluidas (no tiene ninguna); suprimir duplicados mantiene uno de los mismos
ámbitos/tablas con los mismos testigos. Si un factor tiene tabla vacía, sus
3^|S| filas están excluidas y tienen testigos. Al detenerse anticipadamente no se
necesita procesar factores posteriores.

### Vaciamiento global

Para un ámbito S con todas las filas excluidas, se elimina sucesivamente cada
variable con el mismo argumento de ALO. Por inducción sobre |S| se llega a una
cláusula sobre el ámbito vacío, que sólo puede ser la cláusula vacía. La misma
construcción aplica a una frontera completamente descartada.

**Conclusión:** cualquier corrida de O2c que responde «sin coloración» se convierte
en una refutación por resolución de F_G, sin importar qué variable elegía el
selector (prioridad fija, min-fill, relacional o incluso un orden proporcionado
externamente), *siempre que sólo elija v y conserve Join/Project/Normalize*.

## 4. Contabilidad mejorada `DERIVADO`

Sea C_i=3^|U_i| el número de candidatos enumerados en una proyección sobre U_i,
con |U_i|=|T_i|+1.

- Cada fila b rechazada de T_i cuesta como máximo 3 resoluciones; hay a lo sumo
  3^|T_i| filas. Por tanto, **pasos de proyección ≤ 3·3^|T_i| = C_i**.
- Vaciar un factor sobre k variables cuesta a lo sumo
  3·(1+3+⋯+3^(k−1)) = 3(3^k−1)/2 pasos.
- Si la detención es temprana porque una proyección produjo tabla vacía, el
  vaciamiento adicional cuesta menos de 3^(k+1)/2 = C_última/2.
- Si se llega a la frontera B sin factor vacío y todas sus filas están excluidas,
  el vaciamiento cuesta menos de (3/2)·3^|B|, y esa enumeración de frontera está
  incluida en `total_candidates`.

Por lo tanto, para toda ejecución que concluya insatisfacibilidad:

    #resoluciones ≤ (3/2) · total_candidates.

La anterior cota `2·total_candidates` de v2.7 es correcta pero no óptima bajo
este conteo. La demostración cuenta inferencias de resolución; los axiomas de
entrada no se cuentan como inferencias. Si una convención de bibliografía mide
número de líneas incluyendo axiomas, se añaden los |V|+3|E| axiomas iniciales.

## 5. Transferencia de las cotas inferiores `DERIVADO condicional`

Si una familia de grafos exige un mínimo R(G) de pasos de resolución (o líneas,
ajustando el costo de axiomas) para refutar F_G, cualquier corrida insatisfacible
O2c de esa familia cumple:

    total_candidates ≥ (2/3)·R(G)   [para R medido en pasos de inferencia].

Por tanto, una cota inferior R(G)=2^{Ω(n)} se transfiere a `total_candidates`
para esa familia y **ese motor**. No se transfieren sin más cotas de una codificación
diferente, un régimen de densidades diferente o un sistema de pruebas más fuerte.

El trabajo Beame–Culberson–Mitchell–Moore (2005) demuestra cotas exponenciales
de resolución para coloración de grafos aleatorios con número lineal de aristas.
Antes de afirmar parámetros o constantes exactas para nuestras instancias hay
que emparejar el régimen de G, las cláusulas iniciales y la convención de tamaño
con sus teoremas. La cota para familias concretas **no es** una cota universal
para todos los grafos no 3-coloreables (K4 admite refutaciones pequeñas).

## 6. Qué se cierra y qué no `ALCANCE`

**Cerrado dentro de O2c:** la simulación por resolución y la cota 3/2 para toda
corrida insatisfacible, independiente de la prioridad (y también de selectores
que inspeccionan información extra, siempre que no alteren las reglas del motor).

**No demostrado:** que cualquier algoritmo posible de 3-coloración deba operar
por O2c o simularse eficientemente por resolución; que el tiempo para **calcular**
un selector arbitrario esté acotado por `total_candidates`; que P≠NP; o que
el criterio ontológico determine por sí solo un selector computacional óptimo.

## 7. Reproducción y controles

- Fuente histórica del motor: `experiments/o2c_v1_6/` (sin modificaciones).
- Constructor y verificador de pruebas: `experiments/piso_del_camino_v2_7.py`.
- Prioridades deterministas prefijadas y contraprueba por enumeración directa:
  `experiments/prioridad_fija_v2_8.py` y `tests/test_prioridad_fija_v2_8.py`.
- La demostración general es la inducción anterior; probar un conjunto finito de
  prioridades solamente contrasta la implementación, no demuestra el teorema.

## 8. Referencia externa

Paul Beame, Joseph Culberson, David Mitchell, Cristopher Moore, *The resolution
complexity of random graph k-colorability*, Discrete Applied Mathematics 153
(2005), pp. 25–47. https://doi.org/10.1016/j.dam.2005.05.004
