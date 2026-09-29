# Datos y experimentos

Los archivos de resultados se conservan en fuentes/originales para mantener una única copia de referencia por adjunto. Los siguientes enlaces apuntan a los bytes recibidos.

| Datos | Qué contienen | Límite |
|---|---|---|
| [mf53_obdd_normalization_summary.json](../fuentes/originales/mf53_obdd_normalization_summary.json) | Controles de umbral, paridad, HWB y orden de igualdades. | No se incluye el código original ni el manuscrito MF-53. |
| [mf53_equality_order.csv](../fuentes/originales/mf53_equality_order.csv) | Ocho filas de tamaños OBDD para dos órdenes. | Un orden malo no es cota inferior para todos los métodos. |
| [mf54_local_information_summary.json](../fuentes/originales/mf54_local_information_summary.json) | Clases contextuales, umbral corregido, paridad y controles reportados. | Los conteos de pruebas no se regeneran desde semillas en esta entrega. |
| [mf55_transition_rule_summary.json](../fuentes/originales/mf55_transition_rule_summary.json) | Novedad, resolución y transición de ejemplos finitos. | No selecciona eventos físicos. |
| [capsule_width_results_v0_79.json](../fuentes/originales/capsule_width_results_v0_79.json) | Anchos residuales de controles y 3-CNF plantadas. | Ensayos pequeños; no garantía asintótica. |
| [gamma_reference_results_v0_80.json](../fuentes/originales/gamma_reference_results_v0_80.json) | Siete controles y 24 instancias de estrés. | El óptimo de laboratorio no es el costo del selector. |

## Validaciones históricas

Los 14 archivos VALIDATION disponibles permanecen en el [catálogo](../fuentes/CATALOGO.md). Incluyen pruebas reportadas de algoritmos conocidos, identidades finitas, contraejemplos y controles numéricos. «PASS» es el estado declarado por la fuente, no una validación física ni una reproducción nueva de todos los ensayos.

## Verificación de esta edición

El script de integridad analiza JSON y CSV y compara las filas comunes de MF-53. Recalcula los 14 aciertos respecto del óptimo reportado de v0.80. No reconstruye fórmulas ausentes ni certifica por sí mismo los óptimos almacenados.

Los [ejemplos editoriales](../ejemplos/README.md) son pequeños controles independientes que sí se ejecutan en esta edición. No se presentan como código histórico recuperado.

## Para una reproducción completa futura

Incorporar con procedencia: scripts originales, versiones de dependencias, semillas, instancias completas, parámetros, criterios de tolerancia y comandos de ejecución. Algunas fuentes remiten a results/computation; esos archivos no fueron adjuntados y se registran como faltantes.
