# Reading map

## Conceptual route

| Question | Chapter | Main sources |
|---|---|---|
| What makes a difference visible? | [1. Comparison](conceptos/01_comparacion_informacion.en.md) | MF-54, v0.72, v0.78 |
| What does a closed identity preserve? | [2. Boundary](conceptos/02_frontera_cierre.en.md) | MF-54, MF-60B, v0.87 |
| When is a new reference required? | [3. Novelty](conceptos/03_novedad_resolucion.en.md) | MF-55, MF-57–58 |
| What belongs to the joint relation? | [4. Composition](conceptos/04_dependencia_composicion.en.md) | MF-56, MF-61B–62B |
| What has been proven about four? | [5. Geometry](conceptos/05_reflexion_geometria.en.md) | MF-57, v0.83–84, v0.90 |
| How is one layer preserved while another is generated? | [6. Inheritance](conceptos/06_capas_y_nuevo_operador.en.md) | v0.87, v0.91 |
| What makes a closure stable? | [7. Dynamics](conceptos/07_dinamica_estabilidad.en.md) | v0.74–77, v0.89 |
| Where do 16, 15, and octaves come from? | [8. Weights](conceptos/08_bits_pesos_escalas.en.md) | v0.81, v0.84–86, v0.90 |
| What does relational time mean? | [9. Totality](conceptos/09_totalidad_tiempo_fisica.en.md) | v0.72–78 |
| What is missing for a general algorithm? | [10. Computation](conceptos/10_computacion_acreditacion.en.md) | MF-59B–62B, v0.79–80 |

## Three routes

**First reading:** the synthesis, chapters 1–4 and 6, and the record of open work. This conveys the proposal and its limits without reconstructing every version.

**Mathematical review:** chapters 3–8, results, corrections, and linked sources. Check the hypotheses against the originals; editorial labels do not replace proofs.

**Reproduction:** the data guide, editorial examples, and verification. Several scripts and datasets cited by the historical experiments are absent here; the edition identifies that limitation.

## Dependency map

~~~mermaid
flowchart TD
 A["Comparisons and responses"] --> B["Quotient and sufficient boundary"]
 B --> C["Novelty by non-factorization"]
 B --> D["Joint compatibility"]
 C --> E["Extended description"]
 D --> E
 F["Local metric postulates"] --> G["Four-phase orbit"]
 E -. "bridge still open" .-> H["New geometric operator"]
 G -. "inheritance to justify" .-> H
 H --> I["Stability under coupling"]
 J["Specified architecture and dynamics"] --> I
~~~

The dotted arrows mark open work; the others describe conceptual dependencies and do not establish physical universality.

## Reference tools

- [Glossary](GLOSARIO.en.md).
- [Notation crosswalk](NOTACION.en.md).
- [Results](trazabilidad/RESULTADOS.en.md).
- [Document lineage](trazabilidad/LINAJE.en.md).
- [Corrections and open work](trazabilidad/CORRECCIONES_Y_PENDIENTES.en.md).
- [Complete catalog](../fuentes/CATALOGO.en.md).
