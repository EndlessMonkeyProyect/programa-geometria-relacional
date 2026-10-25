# O50 — Desfase material, deformación del aro, sincronización

Autor: Le Matt Ansatz Di Ego — Programa de Geometría Relacional (20-10-2026).

Pruebas reproducibles de un **modelo cinemático axisimétrico incompresible** con geometría toroidal trasladada y deformada. No se presenta como solución libre de fuerza de Euler ni Navier–Stokes.

- `O50_INFORME.es.md`: desarrollo ontología → matemática → pruebas → falsadores.
- `verificar_o50.py`: demuestra simbólicamente divergencia nula y etiqueta material constante, integra trazadores y verifica fases vs solución analítica.
- `resultados_o50.json`: 48 diagnósticos y registros de fase y trayectorias.
- `graficos_o50.png`: fase diferencial vs vueltas de referencia.
- `REGRESION_ANTECEDENTES.md`: comprobación de continuidad con O49.
- `MANIFEST.sha256`: verificación de integridad.

Reproducir desde esta carpeta:

```bash
python verificar_o50.py
```

Dependencias: Python 3, numpy, scipy, sympy. Los gráficos usan matplotlib, solo para visualización.
