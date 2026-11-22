# HC–02 · Transferencia entre escalas y cota de herencia

**Documento principal:** `INFORME_LAB_HC02.md`.

## Reproducción

En Python 3.9+:

```bash
python laboratorio_hc02.py
```

Solo requiere la biblioteca estándar. Produce `escalas.csv`, `frontera.csv`, `cortes.csv`, `metadatos.json` y registra 1.352 controles de coeficientes racionales, 307 pruebas numéricas de la identidad finita y cuatro verificaciones de frontera.

Opcionalmente:

```bash
python graficos_hc02.py
```

Requiere `matplotlib`, y genera `transferencia_normalizada.png` y `frontera_cuadratica.png`.

## Resultado y estado

La desigualdad uniforme HC02.1 se demuestra **sin RH** con sumación de Abel y una cota elemental de Chebyshev sobre potencias primas heredadas. Su centro contiene una integral de la discrepancia de los primos ordinarios y un dato de borde. La desigualdad no resuelve la hipótesis de Riemann y no acredita que la integral restante tenga tamaño de raíz cuadrada.

## Archivos y procedencia

- `INFORME_LAB_HC02.md`: desarrollo, pruebas, contexto y condiciones abiertas.
- `laboratorio_hc02.py`: controles y tablas reproducibles.
- `graficos_hc02.py`: figuras opcionales.
- `ejecucion.txt`: salida de la ejecución incluida en el paquete.
- `escalas.csv`, `frontera.csv`, `cortes.csv`: resultados numéricos.
- `metadatos.json`: resumen legible por máquina.
- `SHA256SUMS.txt`: huellas de archivos del paquete, sin incluirse a sí mismo.

**Endless Monkey Project / Relational Geometry Program**
