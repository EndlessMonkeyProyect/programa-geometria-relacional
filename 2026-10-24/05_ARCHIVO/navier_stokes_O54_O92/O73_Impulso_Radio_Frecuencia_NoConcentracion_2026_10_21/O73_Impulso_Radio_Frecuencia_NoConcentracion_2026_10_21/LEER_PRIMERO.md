# O73 — Impulso y normalización del anillo vorticial

**Suplemento aditivo; no integrado en la Imagen Total v3.8.1.**

## Resultado central

1. **No basta el impulso para sostener un grosor mínimo:** familia analítica de datos iniciales axisimétricos y suaves con la misma circulación, el mismo impulso hidrodinámico y el mismo radio efectivo, pero núcleo arbitrariamente fino y máximo de vorticidad arbitrariamente alto. Es una obstrucción a la suficiencia de esas referencias, no un ejemplo de blow-up temporal.
2. **Sí existe una relación normalizada controlada por Navier–Stokes en una subclase:** sin giro azimutal, `η=ωθ/r` satisface una ecuación de transporte-difusión con operador radial de 5D, y por máximo `||η(t)||∞≤||η(0)||∞`.
3. **Activar el giro azimutal agrega una fuente:** este mecanismo deja de cerrarse automáticamente y constituye la obligación del siguiente paso.

El trabajo parte de relaciones de radio, circulación y orientación, no de energía como principio ontológico. Incluye pruebas analíticas y verificaciones computacionales. **No resuelve Navier–Stokes 3D general.**

## Reproducir

Desde la raíz del suplemento:

```bash
python codigo/verificar_o73.py
```

Dependencias `numpy`, `scipy`, `sympy`, `matplotlib`.

- `O73_FORMALIZACION.es.md` — demostraciones, distinción ontológica/física y fuentes.
- `codigo/verificar_o73.py` — reconstruye datos, gráficos y pruebas.
- `datos/resultados_o73.json` — datos numéricos del ensayo.
- `datos/controles_o73.json` — detalle de controles.
- `graficos/` — perfiles meridianos, pico de vorticidad y radios.
- `REGISTRO_AFIRMACIONES.csv` — tipado epistemológico.
- `MANIFIESTO_SHA256.txt` — huellas de los archivos.
