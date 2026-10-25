# O35 — Comparación modular de dos formas vorticiales

Suplemento **independiente** de O34, de investigación del Programa de Geometría Relacional. **No modifica la Imagen Total.**

## Resultado

Prueba analítica asintótica de que existen dos gaussianas elípticas de vorticidad positiva, separadas, con los mismos radios y circulación, para las que la ecuación de Navier–Stokes 2D reduce inicialmente la diferencia de fase cuadrupolar. El ejemplo espejo aumenta esa diferencia. Por continuidad y por el criterio O31, hay una ventana no vacía con acercamiento de fase, formas anisótropas y dos concentraciones distinguibles.

## Precisión

- **No es** prueba de sincronización a largo plazo ni de cierre físico permanente.
- La fase considerada corresponde a la **orientación de la forma**, no al giro material de las partículas.
- Los números se obtienen de derivadas instantáneas de Navier–Stokes evaluadas por cuadratura; no se ejecuta la PDE en el tiempo.
- El no-go de periodicidad rígida sigue del incremento de segundo momento en NS 2D viscoso.

## Contenido

- `O35_COMPARACION_ENDOGENA_Y_APROXIMACION_MODULAR_NS.es.md`: definiciones, pruebas, condiciones, no-go, adversarios, límites.
- `verificar_o35.py`: dos integrales alternativas (Laplace / Gauss-Hermite), comprobación de signos y asintótica; requiere `numpy` y `scipy`.
- `VALIDACION_O35.json`: resultados reproducibles y aserciones ejecutadas.
- `ANTECEDENTE_O34_2026-10-20.zip`: suplemento anterior inalterado.
- `MANIFIESTO_SHA256.txt`: digests de los archivos del suplemento.

## Ejecutar

```bash
python verificar_o35.py
```

Los controles no prueban regularidad 3D, no certifican con aritmética de intervalos el signo del caso finito `d=6`, y no prueban sincronización atractora.
