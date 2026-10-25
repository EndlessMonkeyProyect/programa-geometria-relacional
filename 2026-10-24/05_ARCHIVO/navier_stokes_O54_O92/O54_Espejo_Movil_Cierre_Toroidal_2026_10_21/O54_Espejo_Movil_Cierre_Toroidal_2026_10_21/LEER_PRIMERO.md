# O54 — Formalización autónoma, candidata para incorporar a Imagen Total

**Autor del Programa de Geometría Relacional:** Le Matt Ansatz Di Ego
**Fecha:** 21 de octubre de 2026
**Base:** Imagen Total v3.8.1 candidata, sin cambiar ni sobrescribir los originales.

## Orden de lectura

1. `O54_FORMALIZACION.es.md`: narrativa original, contrato, identidad geométrica, transformación de espejo, leyes de transporte material, normalizador y novedad, límites de Navier–Stokes.
2. `codigo/verificar_o54.py`: 12 controles de identidades y contraejemplos usando sólo la biblioteca estándar de Python.
3. `resultados/verificacion_o54.json`: resultados exactos/rango de tolerancias generados por el código.

## Ejecutar

```bash
python3 codigo/verificar_o54.py
```

La formulación es aditiva y **no es una nueva versión integral ya fusionada**. Para incorporarla a una siguiente versión, proponer ubicación `25_dinamica_y_tiempo/.../O54/` o en una nueva capa de suplementos y actualizar entonces los manifiestos. La base v3.8.1 sigue intacta.

## Conclusión principal

En un toroide regular, dos direcciones paramétricas son perpendiculares. Para que **esas mismas direcciones materiales** permanezcan perpendiculares durante un flujo, debe anularse su tasa de cizalla cruzada: `a·S b=0`. Para preservar además su razón local de longitudes, las tasas longitudinales de deformación han de coincidir. El cambio de escala exterior deja el cociente `r/R` idéntico, sin imponer dinámica física. El normalizador aritmético permite extensiones exactas; no prueba que el toroide real sobreviva. Esa consecuencia física sigue pendiente.
