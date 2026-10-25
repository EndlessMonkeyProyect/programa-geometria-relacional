# O61 — Relaciones habitadas en un flujo de Navier–Stokes

**Le Matt Ansatz Di Ego · Programa de Geometría Relacional · 21 de octubre de 2026**

Este suplemento parte de O59–O60 y propone un primer puente dinámico verificable: *relaciones disponibles* como tríadas de Fourier y *relaciones activas* como transferencias no nulas. Conserva sin modificaciones la Imagen Total v3.8.1 y los documentos anteriores.

- `O61_FORMALIZACION.es.md`: ontología → clase invariante exacta NS → demostración de activación → numerización convergente → límites.
- `codigo/verificar_o61.py`: reconstruye la solución reducida, comprueba balances, convergencia, invariancia rotacional del acoplamiento y límites del total.
- `resultados/resumen_o61.json` y `resultados/series_o61.csv`: resultados numéricos.
- `graficos/o61_modo_nuevo_y_energia.png`: representación.
- `verificar_integridad.py`: verifica huellas del suplemento contra manifiesto.

**Hallazgo:** dos datos NS 3D tienen el mismo soporte Fourier inicial, energía y enstrofía pero difieren en la primera transferencia hacia un modo anteriormente vacío. La relación de acoplamiento de las componentes del flujo es información necesaria para esa pregunta.

**Límites:** clase particular global suave, no el anillo de O53; los cuadráticos con `+1` de O60 no están derivados de NS, no se ha demostrado regularidad global.
