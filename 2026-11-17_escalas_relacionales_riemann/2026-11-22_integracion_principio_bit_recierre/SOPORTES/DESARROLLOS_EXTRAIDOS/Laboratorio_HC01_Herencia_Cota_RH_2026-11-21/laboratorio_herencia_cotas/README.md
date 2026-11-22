# Laboratorio HC–01

Estudio reproducible de la separación exacta entre contribuciones heredadas y primos nuevos en una suma ponderada de von Mangoldt.

**Documento principal:** `INFORME_LAB_HC_01.md`.

**Ejecutar (solo Python 3):**

```bash
python laboratorio.py
```

Crea `resumen.csv` y `resultados.csv`; valida identidades racionales, la ley de energía, el conteo por criba y la separación de la suma ponderada hasta un millón.

**Gráfica opcional (requiere matplotlib):**

```bash
python graficos.py
```

Crea `serie_normalizada.csv` y `comparacion_escalas.png`.

**Resultado:** La corrección heredada tiene término principal `2*theta(sqrt(x))`, cuyo orden es `2*sqrt(x)` por el teorema clásico de los números primos. La estimación de la discrepancia restante no se demuestra con los controles de este laboratorio.

Endless Monkey Project / Relational Geometry Program
