# Laboratorio S–RA–01 — Semilla de Möbius por octavas

Medición reproducible de la semilla propuesta en RA–01: cuánto de la recuperación óptima de cada octava lleva la capa nueva de Möbius, para los índices libres de cuadrados hasta 2048. Reproduce además el registro archivado del paso 1024→2048.

## Archivos

- `documentos/LAB_RA01_SEMILLA_MOBIUS_2026-11-21.md` — objetos, método, validación, resultados y lectura.
- `scripts/medir_semilla_mobius.py` — cálculo completo con comprobaciones internas.
- `RESULTADOS_VERIFICACION.txt` — salida del script.

## Reproducción

Requiere `numpy`. Desde la raíz del paquete:

```bash
python3 laboratorios/2026-11-21_RA01_semilla_mobius/scripts/medir_semilla_mobius.py
```

Tiempo aproximado: 15 s. Un argumento opcional `J` fija la escala `2^J` (por defecto `J=11`).

**Endless Monkey Project / Relational Geometry Program**
