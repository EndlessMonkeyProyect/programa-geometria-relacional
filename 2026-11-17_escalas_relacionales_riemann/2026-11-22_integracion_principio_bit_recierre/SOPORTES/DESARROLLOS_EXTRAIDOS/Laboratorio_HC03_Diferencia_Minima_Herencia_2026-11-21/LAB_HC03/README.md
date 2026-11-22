# LAB–HC–03 — Diferencia mínima, aparición y herencia

**Fecha:** 21-XI-2026. **Estado:** identidades y controles finitos verificados; cota global pendiente en HC-03.

## Contenido

- `INFORME_LAB_HC03.md`: artículo académico y demostraciones con estados de procedencia.
- `laboratorio_hc03.py`: cómputo y pruebas reproducibles (solo biblioteca estándar Python 3.10+).
- `graficos_hc03.py`: generación de figuras opcional (`matplotlib`).
- `resumen.json` / `ejecucion.txt`: indicadores, controles y puntos de referencia.
- `escalas.csv`: datos en escalas señaladas.
- `bloques_diadicos.csv`: máximos por bloque de escala.
- `control_pesos.csv`: cambio de pesos sobre las mismas posiciones de potencias primas.
- `certificado_bloques.png`, `control_genealogia.png`: gráficos ilustrativos de una muestra finita.
- `SHA256SUMS.txt`: huellas de integridad, sin incluirse a sí mismo.
- `verificar_integridad.py`: verificador multiplataforma de huellas SHA-256 (solo biblioteca estándar).

## Reproducir

```bash
cd LAB_HC03
python laboratorio_hc03.py > ejecucion.txt
python graficos_hc03.py
```

Comprobar integridad en Linux/macOS: `sha256sum -c SHA256SUMS.txt`. Comprobar integridad en cualquier plataforma: `python verificar_integridad.py` (Windows: `py -3 verificar_integridad.py`). El verificador imprime solamente caracteres ASCII para funcionar con consolas de Windows sin modo UTF-8.

La reproducción puede cambiar las últimas cifras de los CSV por versiones de Python y redondeos. En ese caso regenerar el manifiesto. No se equiparan redondeos de coma flotante a certificados matemáticos rigurosos.

## Criterio de lectura

La herencia y las apariciones son objetos positivos. La diferencia con signo cuantifica la separación respecto de una referencia de consulta. El laboratorio **no demuestra RH**: la cota del certificado sobre todos los bloques diádicos es un requisito equivalente a una de las formulaciones clásicas de RH.

**Endless Monkey Project / Relational Geometry Program**
