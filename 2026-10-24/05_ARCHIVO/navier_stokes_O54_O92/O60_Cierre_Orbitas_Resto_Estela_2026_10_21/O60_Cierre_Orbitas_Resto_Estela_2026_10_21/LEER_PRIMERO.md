# O60 — Autorreferencia, sectores pendientes y estela cuadrática

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego · 21 de octubre de 2026**

Suplemento aditivo y candidato después de O59. No reemplaza la Imagen Total v3.8.1 ni los registros O40–O59.

## Conclusión

Se realiza *condicionalmente* la regla `a²+b²+1=N²` mediante una partición D4-invariante de una cuadrícula `N×N`: dos canales ocupan `a²` y `b²` posiciones y un centro queda aún deshabitado. Toda solución entera positiva de esa regla se puede representar así. La continuidad hacia `N'=mN` mediante **ocupación sin borrado** existe dentro del modelo si y sólo si `a'²−m²a² ≥0` y `b'²−m²b² ≥0`; ejemplos `3→51`, `3→99`, pero no `3→9`. La familia Pell permite una cadena infinita anidada con un único centro pendiente en cada resolución.

**No confundir:** la cuadrícula con el cubo físico de espejos; las cardinalidades cuadráticas con dos cuadrados geométricos contiguos; el centro pendiente con un blow-up de Navier–Stokes; la partición aritmética con una ley física; el nuevo modelo de simetría D4 con el grupo de espejos enfrentados de O59.

## Archivos

- `O60_FORMALIZACION.es.md`: planteamiento completo, demostraciones, límites, próximo puente físico O61.
- `codigo/verificar_o60.py`: reconstrucción reproducible (Python 3 puro).
- `resultados/resumen_o60.json`: hechos exactos de prueba y contrafactuales.
- `resultados/patron_3x3.txt`: primera unidad `4+4+1`.
- `resultados/configuraciones_revisadas.csv`: muestra de soluciones confirmadas.
- `MANIFEST_SHA256.json`: integridad de los archivos del suplemento.

Ejecutar desde esta carpeta: `python codigo/verificar_o60.py`.
