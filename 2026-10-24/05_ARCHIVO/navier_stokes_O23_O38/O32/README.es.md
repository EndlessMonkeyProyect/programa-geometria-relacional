# O32 — Certificado de continuidad de la forma propia

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego**

Este paquete complementa O31 y *no* modifica la Imagen Total ni el Núcleo Canónico.

## Contenido

- `O32_FORMA_PROPIA_Y_CONTINUIDAD_VORTICIAL.es.md`: formalización y prueba de las identidades y condiciones suficientes.
- `verificar_o32.py`: 2715 controles numéricos/algebraicos con un ejemplo gaussiano predefinido.
- `ANTECEDENTE_O31_2026-10-19.zip`: la versión antecedente que contiene el criterio de concentración.
- `MANIFIESTO_SHA256.txt`: hashes de todos los archivos principales anteriores.

## Reproducibilidad

```bash
python verificar_o32.py
```

Requiere Python 3 y `scipy` (prueba de integración, ODE y cuadratura). El teorema se prueba en el documento; estas comprobaciones NO son una simulación de Navier–Stokes ni una prueba experimental.

## Resultado

En Navier–Stokes bidimensional no forzado, para dos etiquetas de vorticidad positiva y observables iniciales explícitos, se garantiza durante un intervalo finito la separación de dos concentraciones y la permanencia de anisotropía de segundo momento en cada una, siempre que se satisfaga el criterio T4. La orientación cuadrupolar no es la fase material del fluido.

## Precauciones

- No hay teoría general de identificación de vórtices no etiquetados.
- No hay teorema de sincronización física o fusión a partir de la desigualdad.
- No hay extensión a vorticidad 3D ni solución del problema global de regularidad.
- `U_0` es una cota dependiente de los datos iniciales, no la velocidad universal `c`.
- El certificado puede no cumplirse aunque los vórtices persistan: es suficiente, nunca necesario.
