# Alcance y criterios de la edición

## Corpus

Esta edición preserva 79 adjuntos: 72 Markdown, cinco JSON, un CSV y un ZIP. Del ZIP se extraen tres miembros; dos repiten exactamente documentos ya adjuntos y uno es el manifiesto interno de v0.91. Se mantienen ambas procedencias.

El inventario se limita a esta conversación. Los textos remiten a desarrollos, datos y códigos anteriores que no están incluidos. Una referencia a ellos no equivale a disponer de ellos. El [catálogo](../fuentes/CATALOGO.md) y el [manifiesto](../fuentes/MANIFIESTO.json) identifican el contenido efectivamente preservado.

## Niveles de lectura

- **Fuente histórica:** afirmación tal como fue aportada, conservada literalmente.
- **Síntesis editorial:** explicación reorganizada que enlaza las fuentes.
- **Revisión editorial:** evaluación matemática de la integración, identificada expresamente.
- **Ejemplo editorial:** cálculo nuevo de alcance limitado; no reemplaza los experimentos históricos.
- **Pendiente:** construcción o demostración que no se encontró en el corpus revisado.

La autoría del programa se conserva como Le Matt Ansatz Di Ego, según las fuentes. Las correcciones propuestas por esta edición no se atribuyen automáticamente al autor.

## Etiquetas epistemológicas

| Etiqueta | Significado |
|---|---|
| DEFINICIÓN | Elección de un objeto y su significado. |
| POSTULADO | Condición adoptada como punto de partida. |
| DERIVADO CONDICIONAL | Consecuencia de hipótesis indicadas; no prueba esas hipótesis. |
| CONTROL REPORTADO | Resultado numérico consignado en una fuente, sin reproducción integral aquí. |
| COMPROBADO EN ESTA EDICIÓN | Ejemplo o verificación efectivamente ejecutado en esta entrega. |
| CORRESPONDENCIA | Interpretación entre ramas que necesita un puente adicional. |
| ABIERTO | Falta un procedimiento, una prueba o una identificación. |
| CORRECCIÓN | Formulación que debe sustituirse o acotarse, manteniendo el original. |

## Reglas de fidelidad

1. Una versión posterior no elimina automáticamente todos los resultados anteriores.
2. Una auditoría que afirma «cerrado» se lee junto con sus hipótesis y demostraciones.
3. Un mismo símbolo no establece identidad entre objetos de tipos distintos.
4. Un resultado sobre un modelo finito no se traslada automáticamente a física o complejidad general.
5. «Sin pérdida» describe la conservación de las fuentes; no certifica exhaustividad del archivo histórico ni validez universal de sus afirmaciones.
6. Los originales pueden contener errores de escape en LaTeX o texto de control. Se preservan los bytes; la síntesis reescribe las expresiones necesarias de forma legible.
7. No se asigna una licencia de reutilización sin decisión del titular. La preparación del repositorio no cambia los derechos de las fuentes.

## Verificación

Se comprueban hashes, presencia de cada original, coincidencia del paquete con su extracción, sintaxis JSON, estructura CSV y enlaces locales de la documentación editorial. Se ejecutan ejemplos exactos sin dependencias externas. Los informes históricos de miles de pruebas se conservan como reportados, no como pruebas rerrealizadas.
