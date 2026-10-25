# Experimento: densidad de indefinición, marco de comparación y recierre

**Programa Relacional · Ejercicio exploratorio · 14 de octubre de 2026**

## Pregunta

¿El costo de resolución se explica mejor por la cantidad bruta de posibilidades, por la disposición relacional y por la pregunta desde la cual se observa el sistema que por un tiempo o número de ciclos descontextualizado?

## Protocolo

- **81 grafos de 8 vértices**, usados como instancias de 3-coloración; 72 muestras pseudoaleatorias (18 por densidad generadora 0,15; 0,30; 0,45; 0,60) más 9 casos estructurados.
- **Frontera fija:** tres vértices, 0, 1 y 2; 27 asignaciones posibles antes de considerar restricciones.
- Para cada grafo se calculó el número de coloraciones globales y el conjunto de asignaciones de frontera compatibles. Se verificó **independientemente por enumeración exhaustiva** el tamaño de la interfaz para los 81 casos.
- Se ejecutó el motor O2c de v2.7 con selector `min_fill` y con selector `relacional`. Ambos produjeron la misma interfaz en todos los casos.
- Costo comparado (un **proxy de trabajo**, no segundos ni operaciones elementales uniformes de máquina): **candidatos examinados + lecturas de factores para seleccionar + comprobaciones de normalización**. Sirve para comparar este motor implementado y estos casos, no constituye una cota de complejidad general.
- En control adicional, sobre los mismos 81 grafos y la misma frontera, se variaron las preguntas sobre pares (0,1), (0,2) y (1,2), que influyen en el selector `relacional`.

## Resultados

| Grupo de 18 grafos | Media de asignaciones compatibles en frontera (máx. 27) | Mediana del proxy de trabajo `relacional` |
|---|---:|---:|
| Probabilidad generadora de arista 0,15 | 23,5 | 64 |
| Probabilidad generadora de arista 0,30 | 17,0 | 202 |
| Probabilidad generadora de arista 0,45 | 7,8 | 313 |
| Probabilidad generadora de arista 0,60 | 2,0 | 756 |

Con más restricciones, en esta muestra **disminuye el número de soluciones sobrevivientes**, mientras el trabajo requerido por el motor suele aumentar. Por tanto, **menos indefinición final no equivale automáticamente a menor costo de resolverla**.

**Control de disposición:** los casos `random_p30_s00` y `random_p45_s15` tienen ambos 8 vértices, 13 aristas, 12 soluciones globales y 6 asignaciones admisibles de frontera, pero su proxy de trabajo `relacional` fue de **481 frente a 314** (53 % más en el primero). Así, igual tamaño, igual cantidad de restricciones e igual número de soluciones no determinan por sí solos el costo de este motor: la **topología y el recorrido** importan.

**Control de punto de vista:** al mantener el grafo y la frontera y cambiar solo qué par de vértices se pregunta, el costo del selector `relacional` cambió en **20 de 81** casos. En `random_p60_s14`, la pregunta (0,1) produjo un costo de **418**, mientras las preguntas (0,2) o (1,2) produjeron **581** (39 % más). Esta diferencia es efecto de la **política heurística dependiente de la pregunta**; no prueba que el costo óptimo intrínseco de la pregunta cambie en igual proporción.

**Control adversarial:** contando el costo del selector, `relacional` obtuvo un proxy menor que `min_fill` en **2 de 81** casos, igual en uno y mayor en 78. El selector ensayado **no demuestra** en este experimento ser una política superior de recierre. **No se ejecutó ROSI completo**: solo el modo `relacional` del motor O2c v2.7.

## Lectura desde la ontología

La propuesta «la densidad de indefinición es el marco» puede definirse inicialmente como un **perfil contextual**, no como un único escalar:

\[
M(F,Q,B) = \bigl(\sigma(F),\ |I_B(F)|/3^{|B|},\ \mathcal{D}(F,B),\ C(F,\pi,Q)\bigr),
\]

donde `I_B(F)` es el conjunto de asignaciones de frontera realizables, `σ` registra satisfacibilidad/contradicción, `𝓓` describe las dependencias estructurales (p. ej., ancho efectivo del recierre), y `C` es el costo acreditado de la política especificada, incluida la selección. La fracción de asignaciones supervivientes es una **densidad de posibilidades**, no una medida completa de dificultad.

Una hipótesis falsable para ROSI sería: **entre instancias cuyos perfiles estructurales y preguntas sean comparables, una política de cierre sensible a esos perfiles debe predecir y/o reducir el costo mejor que una prioridad que ignore la información relacional**. Esa hipótesis requiere ensayar el algoritmo ROSI propiamente dicho, distintas escalas, instancias adversarias y verificaciones de costo de selector, memoria y certificación.

## Límites

- Muestra exploratoria, tamaño fijo y pequeño (8 vértices); las 72 muestras aleatorias siguen probabilidades generadoras, no una estratificación controlada por cada magnitud.
- La cantidad de soluciones globales y las asignaciones de frontera se calcularon exhaustivamente **solo para medir**; esa información no fue suministrada al selector.
- Un proxy suma tipos distintos de operación, lo que no equivale a medir tiempo real o costo asintótico; el resultado depende del motor y la política usados.
- La densidad de aristas no equivale a densidad de indefinición. También influyen ubicación de aristas y pregunta.
- Los datos **no demuestran** P=NP ni P≠NP, ni confirman que siempre exista un cierre de costo polinómico.

**Archivos:** `mediciones.csv`, `trazas.json`; script reproducible `../experimento_densidad_relacional.py`.
