# Publicación técnica — 13 de noviembre de 2026

**Endless Monkey Project**  
*Relational Geometry Program*

**Autor:** Le Matt Ansatz Di Ego.

*Cuatro referencias, paridad y reconstrucción de un teseracto* · Versión 1.1

## Archivos

- `CUATRO_REFERENCIAS_TESERACTO_2026-11-13.md`: artículo completo editable, con ecuaciones en LaTeX, demostraciones y referencias.
- `CUATRO_REFERENCIAS_TESERACTO_2026-11-13.pdf`: versión de lectura y archivo.
- `verificar.py`: comprobaciones finitas con aritmética exacta y solo la biblioteca estándar de Python.

## Reproducción

```bash
python3 verificar.py
```

Salida esperada en la última línea: `TODAS LAS COMPROBACIONES FINITAS PASARON.` (unos dos segundos).

El programa enumera el grafo $`Q_4`$, las dos 16-celdas con sus 16 celdas, las fibras de las comparaciones por pares, la paridad para $`n=2,\ldots,7`$, los 15 patrones de regiones y la coincidencia de $`S_iS_j`$ con $`S_jS_i`$ solo sobre la arista común. Comprueba además el lema 1 en las 118 096 palabras reducidas de longitud 1 a 10, la distinción de los 118 097 puntos de esa porción de la órbita del centroide y la ecuación $`F(S_iz)=F(z)\oplus e_i`$ de la etiqueta del teorema 6. La finitud de órbitas, la dimensión mínima, el criterio de cociente y el teorema 6 completo se demuestran en el artículo.

## Ubicación en el repositorio

`2026-11-13_cuatro_referencias_teseracto/`, con los tres archivos anteriores y este README.

Los enunciados clásicos se citan con su fuente: Hinton, con Boole y Falk, para el *tetra-tessaract*; Świerczkowski, Dekker y Stewart para el producto libre de las reflexiones de las caras.
