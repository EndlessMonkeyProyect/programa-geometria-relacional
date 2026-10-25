# Revisión de la rama P frente a NP · 24 de octubre de 2026

Notas de edición surgidas al revisar LAB-CONV v2. No modifican ningún documento original.

## Comprobado

- `laboratorio_v2.py` y `verificar_exhaustivo.py` regeneran sus JSON byte a byte.
- La eliminación coincide con un solucionador independiente en 300 grafos aleatorios de 10 a 14 vértices.
- T1–T4 y el falsador de cantidad y radio son correctos.

## Lo que mide el método

`escalado_cuadriculas_y_cubicos.py` usa el propio `eliminate` del laboratorio:

- En cuadrículas k×k (bipartitas, triviales) las evaluaciones pasan de 22 a 107.005 entre k = 3 y k = 9.
- En grafos 3-regulares aleatorios (3-coloreables por Brooks) pasan de 105 a 178.406 entre 16 y 56 vértices.

El costo sigue al ancho del grafo, no a la dificultad. Bajo la hipótesis SETH, ningún refinamiento exacto de las tablas de frontera baja la base 3 (Lokshtanov, Marx y Saurabh); la simetría S₃ solo ahorra un factor constante.

Uso: `python3 escalado_cuadriculas_y_cubicos.py ../VIGENTE_LAB_CONV_V2`

## Para la próxima edición

1. Nombrar los resultados establecidos: eliminación de variables, congruencia de Myhill–Nerode, simetría de valores y dureza del *backbone* (Kilby y otros, 2005).
2. Los scripts de `antecedentes/` escriben en una ruta fija `/mnt/data/...` y no corren fuera del entorno original.
3. **La cota propia ya está demostrada en el material.** `01_HILO/fuentes/06_hilo_del_dos/v2_8/docs/PISO_DEL_CAMINO_v2_7.md` (14 de octubre) prueba N1:
   - ningún orden baja el motor de tablas de 3^(tw+1);
   - con poda, toda corrida que concluye «no hay coloración» es una refutación por resolución, y por eso cuesta 2^Ω(n) en grafos aleatorios, con cualquier selector, incluso con oráculo (Beame, Culberson, Mitchell y Moore, 2005).

   Es más fuerte que la cota en cuadrículas que propuse en esta revisión, que queda superada.
4. **LAB‑CONV v2 no cita N1.** Su sección VII vuelve a pedir un «selector de convergencias» que N1 ya mostró imposible dentro de este motor. Conviene que lo cite y que el próximo paso se plantee fuera del motor de tablas.
