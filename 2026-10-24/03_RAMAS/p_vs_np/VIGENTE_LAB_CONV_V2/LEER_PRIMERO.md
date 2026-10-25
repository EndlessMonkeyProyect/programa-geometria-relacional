# LAB-CONV v2 — guía de reproducción

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 2026-10-22**

**Resultado:** normalización exacta de interfaces de 3-coloración por renombramiento S3, cierre certificado por diamante, obstrucción de ciclo impar en vecindad, falsador conjunto de cantidad+radio, comparación de órdenes de eliminación. Ninguna prueba de P=NP.

## Archivos

- `LAB_CONV_V2_NODOS_Y_FRONTERAS.md`: narrativa → ontología → lenguaje → matemáticas → mediciones → límite.
- `laboratorio_v2.py`: experimento completo reproducible (Python estándar, sin SAT, sin redes).
- `verificar_exhaustivo.py`: enumeración independiente para 1.338 grafos pequeños y verificación de fusiones.
- `resultados_v2.json`: cada traza, cada orden y cada cuenta de tablas, con límites de ejecución.
- `controles_exhaustivos.json`: resumen de controles exhaustivos y aleatorios.
- `tabla_resumen.csv`: resumen compacto de los ensayos.
- `antecedentes/`: copias inalteradas de los documentos y scripts usados inmediatamente antes de este nuevo ensayo.

## Ejecutar

```bash
python3 laboratorio_v2.py
python3 verificar_exhaustivo.py
```

La ejecución puede reemplazar los JSON con el mismo contenido determinista. El parámetro interno `cap=130000` corta una orden de eliminación que requiera examinar más estados; en tal caso **no hay veredicto** para esa corrida. La prueba de exhaustividad comprueba n=4,5 (todos los grafos etiquetados) y 250 grafos de n=6 generados con semilla fija `20261022`.

## Interpretación

Las cifras son **evaluaciones de frontera**, no duración de CPU ni cotas de complejidad general. Toda equivalencia de color empleada aquí depende de NO tener colores nombrados por anclajes absolutos. La preservación de historias adicionales no está garantizada por una firma de existencia.
