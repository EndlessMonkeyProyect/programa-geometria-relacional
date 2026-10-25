# O49 — Balance del anillo móvil

Suplemento autónomo aditivo para el Programa de Geometría Relacional.

- `O49_AVANCE_CIERRE_INNER_OUTER.es.md`: análisis, demostraciones, controles adversariales, fuentes y límites.
- `verificar_o49.py`: verificador reproducible con `sympy` y `numpy`. No es un solucionador de Euler/Navier–Stokes.
- `resultados_o49.json`: valores comprobados.
- `relacion_giro_avance.png`: comparación ilustrativa bajo hipótesis del núcleo delgado uniforme.
- `SHA256SUMS`: integridad del paquete.

Ejecutar: `python verificar_o49.py`

Se diferencia estrictamente entre cierre de flujo relativo para un anillo estacionario ideal, retorno material de fases y regularidad global de Navier–Stokes.
