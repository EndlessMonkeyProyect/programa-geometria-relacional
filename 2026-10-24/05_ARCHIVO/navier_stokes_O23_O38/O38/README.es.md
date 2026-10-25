# O38 — Cambio intrínseco de foco en Navier–Stokes 2D

**Estado:** suplemento independiente del Programa de Geometría Relacional. **No modifica** el Núcleo Canónico ni la Imagen Total.

## Objetivo

Probar la existencia de una transición geométrica observable usando **solo el campo de vorticidad total instantáneo**, sin etiquetas de vórtices en el futuro, un coeficiente de sincronización elegido ni la interpretación cognitiva de «reconocimiento».

## Archivos

- `O38_CRITERIO_INTRINSECO_Y_CAMBIO_DE_FOCO_NS.es.md`: contrato, teorema condicionado de NS 2D, prueba, banco exacto de calor, contraejemplo de solapamiento etiquetado y límites.
- `verificar_o38.py`: controles ejecutables sobre la solución exacta de calor, curvatura central, invariancias y ambigüedad del solapamiento etiquetado.
- `resultados_o38.json`: salida reproducible.
- `MANIFEST_SHA256.txt`: integridad de los contenidos.

## Reproducción

```bash
python verificar_o38.py
```

Se requiere Python con `numpy` y `scipy`.

## Resultado condicionado y límites

En NS 2D no forzado con viscosidad fija y dos gaussianas de igual circulación inicial `gamma` centradas en `+/-a`, con `a>sigma`, existe un `gamma_*>0` tal que para `0<gamma<gamma_*` la curvatura intrínseca del centro cambia de silla a máximo local estricto en un horizonte finito. Este resultado se deduce de la continuidad de soluciones suaves de la ecuación no lineal con el parámetro de amplitud, **no** de una simulación de NS ni de una demostración del valor explícito de `gamma_*`.

La solución exacta del **calor** tiene un tiempo crítico `T=(a²−sigma²)/(2nu)`; no asumir que el mismo tiempo sea exacto para la NS no lineal.

**No se acredita:** un único máximo global para NS arbitraria, sincronización de frecuencias, persistencia de dos identidades tras la reorganización, una ley física nueva, ni regularidad global 3D.

## Bibliografía de contexto

Gallay & Wayne, *Global stability of vortex solutions of the two-dimensional Navier–Stokes equation*, CMP 255 (2005), 97–129. DOI 10.1007/s00220-004-1254-9. https://arxiv.org/abs/math/0402449
