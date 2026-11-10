# Imagen Total 4.0

**Endless Monkey Project**  
*Relational Geometry Program*  
10 de noviembre de 2026 · [English](README.en.md)

La imagen del programa a hoy, en un solo texto. Sigue el hilo acordado el 24 de octubre: la totalidad y su indeterminación, la reflexión, abrir o cerrar según los ángulos, y las ramas. Reúne el desarrollo completo de la Imagen Total 3.9 y las entregas del 27 de octubre al 10 de noviembre: *Más allá de Yang–Mills*, T-EXT-01, G–01, *El cruce como reflejo central*, el laboratorio óptico v5.1, *La economía del cálculo*, *¿Qué cálculo deja de hacerse?* y las notas del 10 de noviembre sobre cuatro cápsulas en Navier–Stokes, el mecanismo P/NP y el recierre en Yang–Mills.

## Contenido

- [`Imagen_Total_4_0.md`](Imagen_Total_4_0.md) y [`Imagen_Total_4_0.pdf`](Imagen_Total_4_0.pdf): el documento.
- [`verificadores/ns_c4/`](verificadores/ns_c4/): cuatro cápsulas en Navier–Stokes, C4‑E1 y C4‑E3, con su archivo de resultados.
- [`verificadores/ym_z2/`](verificadores/ym_z2/): recierre exacto de dos plaquetas $\mathbb Z_2$.
- [`SHA256SUMS.txt`](SHA256SUMS.txt): sumas de todos los archivos.

## Partes

I. El lenguaje · II. El hilo · III. Palabras · IV. Núcleo formal · V. Realizaciones · VI. Ramas (Navier–Stokes, P frente a NP, Yang–Mills) · VII. Masa, tiempo y gravedad · VIII. El lenguaje en operación · IX. Matriz · X. Procedencia y verificación · XI. Capa de enlaces.

## Verificación inmediata

```bash
python3 -I verificadores/ns_c4/verificar_ns_c4.py
python3 -I verificadores/ym_z2/verificar_recierre_Z2.py
```

Biblioteca estándar de Python 3.9 o posterior. El primero reescribe `verificadores/ns_c4/datos/resultados_ns_c4.json`.

## Ediciones anteriores

La Imagen Total 3.9 sigue íntegra en [`../2026-10-24/01_HILO/imagen_total_3_9/`](../2026-10-24/01_HILO/imagen_total_3_9/), y el hilo ontológico integrado del 24 de octubre en [`../2026-10-24/01_HILO/`](../2026-10-24/01_HILO/).
