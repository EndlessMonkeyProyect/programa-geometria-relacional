# Independencia relacional, suficiencia y radio de cierre

**El hilo del dos · laboratorio exploratorio · 14 de octubre de 2026**

## Pregunta ontológica

No basta contar relaciones o soluciones. Importa cuáles diferencias conservan información propia, cuáles dependen de otras y cuál es el conjunto suficiente para una pregunta formulada desde una frontera. El radio que mide la resolución debe depender de esa pregunta y del alcance relacional de la información necesaria.

## Propuesta matemática (operacional, relativa a una pregunta)

Sea `E` un conjunto de relaciones binarias entre ocho variables de tres valores (restricciones de desigualdad de color), `B=(0,1,2)` la frontera y

`I_B(E) = { a|_B : a satisface todas las restricciones de E }`.

Esta representación es un laboratorio particular, no una identificación general de lo relacional con la 3-coloración.

1. **Indispensabilidad individual para la pregunta**: una relación `e` es indispensable si `I_B(E \ {e}) != I_B(E)`. Como quitar restricciones no elimina respuestas, el cambio solamente puede agregar respuestas en la frontera. Esta noción es *marginal y contextual*; no equivale a independencia estadística o algebraica.
2. **Sinergia de pares**: `e1` y `e2` son conjuntamente relevantes aunque individualmente no lo sean cuando quitar cada una por separado deja la interfaz intacta, pero quitar ambas la modifica. No todas las sinergias tienen que ser de tamaño dos.
3. **Núcleo suficiente mínimo**: `S* ⊆ E` de mínima cardinalidad con `I_B(S*)=I_B(E)`. Encontrar este núcleo constituye otro problema computacional; enumerarlo fuera del selector no lo vuelve eficiente.
4. **Radio de cierre**: con distancia de grafo desde `B`, sea `B_r` el conjunto de vértices hasta `r` enlaces de la frontera y `E_r` las relaciones cuyos dos extremos están en `B_r`. Se define `R*(E,B)= min { r : I_B(E_r)=I_B(E) }` en estas instancias finitas. El radio se mide en *saltos relacionales*, no en distancia física ni tiempo.

## Método y control

Se reutilizaron las 81 instancias del experimento de densidad (8 vértices, 3 colores, frontera fija B=(0,1,2)). Las soluciones admisibles se calcularon exactamente por intersección de bitsets correspondientes a las `3^8=6561` asignaciones posibles. Para cada arista se quitó la restricción y se comparó `I_B`. Para todos los pares de aristas individualmente no indispensables se comprobó el efecto conjunto. Para las dos instancias comparables se recorrieron subconjuntos de aristas de menor a mayor cardinalidad hasta hallar el núcleo mínimo; sus respuestas se verificaron también mediante una segunda enumeración directa de coloraciones.

## Resultado comparativo decisivo

| Medida | `random_p30_s00` (A) | `random_p45_s15` (B) |
|---|---:|---:|
| Vértices | 8 | 8 |
| Aristas / relaciones | 13 | 13 |
| Coloraciones completas | 12 | 12 |
| Respuestas compatibles en frontera | 6 | 6 |
| Aristas individualmente indispensables en la frontera | **10** | **5** |
| Mínimo de aristas suficiente para conservar la respuesta | **11** | **5** |
| Radio relacional de cierre `R*` | **2** | **1** |
| Indicador de trabajo del selector `relacional` de O2c | 481 | 314 |

En A el radio 0 permite 18 respuestas en frontera, el radio 1 permite 12, y el radio 2 deja 6. En B el radio 0 permite 12 y el radio 1 ya deja las 6 definitivas. La diferencia de costo entre estas dos ejecuciones del motor acompaña una diferencia en suficiencia y radio, sin demostrar causalidad ni una relación universal.

Para A, quitar individualmente las relaciones `(4,5)` o `(4,6)` no cambia la interfaz, pero quitar **ambas** sí la cambia: son un ejemplo de dependencia conjunta. Por ello, las diez relaciones individualmente indispensables no bastan; el núcleo mínimo tiene once. En B, las cinco individualmente indispensables forman directamente un núcleo mínimo.

## Vista de las 81 instancias

- En **55/81** instancias se encontró al menos una arista individualmente indispensable para la frontera.
- En **22/81** apareció por lo menos un par de aristas no indispensables individualmente cuya eliminación conjunta cambia la respuesta.
- En **8/81** la interfaz estaba restringida sin tener ninguna arista individualmente indispensable: resulta especialmente importante evaluar dependencias de conjuntos y no solo relaciones aisladas.
- La correlación descriptiva lineal, en esta muestra y con este indicador de trabajo, fue `r=0.880` para el número total de aristas, `r=0.925` para el rango ciclomático del grafo (`m-n+componentes`), y `r=0.140` para el conteo de aristas individualmente indispensables en la frontera. **No** se puede concluir de ello que el rango ciclomático sea independencia de información ni que determine costos en general; todas son medidas confundidas por la estructura, el tamaño y el motor usado.

## Interpretación para el programa

Este ensayo apoya distinguir **cantidad**, **indispensabilidad contextual**, **interdependencia** y **suficiencia**, cada una relativa a la pregunta y a la escala. El centro no es un tiempo absoluto: la evaluación del costo se formula desde la frontera y las relaciones necesarias para resolverla. Una misma cantidad de respuestas finales puede requerir distinto radio de cierre.

## Límites de resolución

- Son instancias pequeñas y especiales de 3-coloración. El cálculo usa enumeración exhaustiva de asignaciones y subconjuntos; **no** establece un algoritmo general eficiente.
- La selección retrospectiva de dos casos de igual tamaño y solución permite explicar diferencias, **no** predecir la dificultad de nuevos casos sin calcular primero los núcleos.
- El indicador de trabajo `relacional` ya definido mezcla varias operaciones y no equivale a una medida formal de tiempo o a un tiempo físico.
- El `R*` elegido depende de la definición de frontera y de distancia en el grafo; no deriva un radio geométrico físico.
- Estos resultados no deciden `P=NP` ni `P≠NP`.

## Siguiente discriminante propuesto

Construir una estimación **previa** de independencia, sin enumerar respuestas ni probar todos los subconjuntos, que seleccione prioridades mejores que `min_fill` bajo el mismo contador de trabajo total, con validación de instancias nuevas, diversas y adversarias. Diferenciar la búsqueda de un núcleo de su verificación y declarar el costo de ambas.

**Datos y reproducción:** `independencia_81.csv`, `mediciones.csv`, `medir_independencia.py` en esta carpeta.
