# ROSI — matriz de resolución, relaciones y obligaciones

**Uso propuesto:** verificación argumental y trazabilidad editorial del Programa. Los estados indican el grado de cierre **de una afirmación bajo su contrato**, nunca una certificación de verdad por autoridad. Esta matriz se ha preparado manualmente; no equivale a una evaluación automatizada externa.

## Convención

- **RESOLVED:** demostración o testigo exacto que cierra la afirmación en su alcance.
- **OPEN:** se conoce la pregunta y la evidencia discriminante pendiente.
- **SUPERPOSED:** dos o más rutas permanecen compatibles con lo medido; registrar qué dato las separaría.
- **COLLAPSED:** se enuncia un cierre sin los discriminantes requeridos; debe corregirse antes de publicar.

## Registros

| ID | Referencia y determinante | Estado | Evidencia / obligación que lo separa | Novedad operacional |
|---|---|---|---|---|
| R-E01 | Firma `Φ`, consulta `q` | RESOLVED | prueba de factorización; testigo de falla | criterio verificable |
| R-E02 | Fibra antigua, nueva consulta | RESOLVED | `ceil(log2 max_s |q(Φ^-1(s))|)` en X finito; **no incluye tiempo de construir código** | cuantificación de suplemento |
| R-E03 | Ampliar familia de consultas | RESOLVED | inclusión de equivalencias; referencia fija | monotonicidad tipada |
| R-E04 | Pared `L=1` → `L=2` | RESOLVED | dos racionales exactos; nueva lectura los separa | testigo de reapertura |
| R-E05 | Cuatro puntos con orientación | RESOLVED | distancias cuadradas idénticas y volúmenes orientados opuestos | bit sujeto a etiqueta |
| R-E06 | Cuatro bits y seis XOR | RESOLVED | ocho patrones / tres grados relativos | distinción algebraica |
| R-E07 | `Z_6` con referencia nueva `Z_10` | RESOLVED | cinco valores por fibra antigua y tres bits suplementarios | normalización |
| R-E08 | Cierre propio autorreferenciado | OPEN | especificar operador interno, invariantes y falsador independiente de consulta exterior | condición por construir |
| R-E09 | Reconocimiento universal de estructura oculta | OPEN | algoritmo uniforme, certificados y familias adversariales no construidas para el reconocedor | costo de descubrimiento |
| R-E10 | Transferir economía a 3-SAT general | OPEN | cota uniforme de extractor+certificador+consulta y reducción completa | implicación no demostrada |
| R-E11 | Puente óptico → algebraico | OPEN | mapa que preserve operaciones y error; prueba de conmutatividad | equivalencia pendiente |
| R-E12 | Puente holonomía/Yang–Mills → economía | OPEN | modelo, evolución, observable físico y predicción | interpretación por contrastar |
| R-E13 | «Herencia» vs «novedad» de cláusulas | RESOLVED bajo contrato general | `F⊨C`: coNP-completo; `F⊭C`: NP-completo; reportar corrección editorial donde se invirtieron | corrección semántica |
| R-E14 | Economía neta | RESOLVED como regla de contabilidad | `H + mR < mD` con mismo contrato; medir H,R,D para cada familia | umbral condicionado |
| R-E15 | Comparación con contadores especializados | OPEN | mismo DIMACS, exactitud, recursos, seeds, hardware y certificados | resultado por medir |

## Regla editorial de cierre

Cada vez que se declare un resultado, registrar: 1) la versión comprobada, 2) el enunciado exacto, 3) el código o argumento, 4) el falsador más próximo, 5) si el resultado cambia la interpretación de un concepto anterior. Una equivalencia no demostrada conserva **OPEN** aun cuando el experimento sea favorable.

## Corrección prioritaria

En las solicitudes de revisión y el material del 8-XI, se debe evitar mezclar las decisiones `F⊨C` y `F⊭C`. Para cláusula `C` y 3-CNF general `F` con un universo de variables declarado, la primera es coNP-completa y la segunda NP-completa. La distinción preserva la pregunta original: **qué relación se heredó y qué novedad queda pendiente**.
