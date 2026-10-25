# Contrato de continuidad O22 — evaluación por otro agente

## Qué hay que reproducir

1. Leer `O22_CONTINUIDAD_Relleno_Y_FOCO.es.md` y distinguir hipótesis geométricas [D], resultados [T], ensayos [E], e interpretaciones [O].
2. Ejecutar `python laboratorio_o22.py` y verificar su salida y manifiesto.
3. Derivar independientemente que \(\Lambda=\{(i,j,k)\in\mathbb Z^3:i+j+k\equiv 0\;(2)\}\) produce un tetraedro de cuatro vértices pares dentro de cada cubo entero y un octaedro en cada esquina impar; demostrar por desigualdades el recubrimiento interior disjunto.
4. Verificar que el vértice especular \(q=(4/3,4/3,4/3)\) de \(T_0\) es centroide de la cara opuesta del octaedro, y por qué esa igualdad **no** convierte a \(q\) en un vértice nuevo de la teselación.
5. Verificar la regla de incidencia local 8T+6O por vértice y 2T+2O por arista.
6. Buscar otros rellenos o continuaciones bajo contratos más débiles para medir qué tan específica es la elección de la red par; **no** declarar su unicidad a partir del ejemplo construido.

## Falsadores prioritarios

- Si se logra demostrar que un K4 combinatorio con solo su automorfismo S4 ya determina una única métrica y orientación sin hipótesis adicional, hay que revisar D1 (pero K4 desnudo normalmente permite numerosas métricas invariantes solo bajo un subgrupo).
- El octaedro de puntos medios de O21 tiene arista \(a/2\); el octaedro global de O22 tiene arista \(a\). Mezclar ambos destruye la comparación de escalas.
- Cualquier derivación de un único centro inmóvil para toda la red infinita translacional debe especificar qué rompe o restringe esa invariancia.
- No confundir un número de relaciones o volúmenes geométricos con bits físicos, masa, entropía o una ley gravitacional. Se necesitarían observables independientes.

## Lo que se abre

O23: ¿qué contratos de consulta permiten distinguir una continuación especular de una extensión octaédrica desde la misma cara, y cuál es el costo de transmitir tal elección entre octavas o escalas? Enlaces con O14/O16/O17 (contención) y O18 (canal espectral) requieren construcción explícita; el empalme del espacio no da por sí mismo un operador disipativo.
