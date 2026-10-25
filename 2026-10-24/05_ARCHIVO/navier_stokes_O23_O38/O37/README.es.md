# O37 — Emergencia de una relación común de mezcla y persistencia de forma

**Estatus:** suplemento independiente del Programa de Geometría Relacional. No actualiza ni sustituye la Imagen Total, el Núcleo Canónico o la carpeta original del programa.

## Qué demuestra

Bajo Navier–Stokes 2D no forzado, viscosidad positiva, vorticidad total positiva y dos componentes iniciales de soporte disjunto, el funcional

`O(t) = integral omega_A omega_B / (omega_A+omega_B)`

cumple exactamente `O'(t)=2 nu integral omega |grad(omega_A/omega)|² >=0`.

Para un intervalo no nulo se conserva la separación de dos concentraciones etiquetadas y su anisotropía cuadrupolar, aplicando las cotas de O31 y O32. Una construcción elíptica compacta permite demostrar además, para una elección adecuada de orientación y suficiente separación inicial, que la diferencia de orientaciones **disminuye inicialmente** por la interacción de Biot–Savart.

**Advertencias:** esta relación común es **solapamiento por difusión**, no sincronización de frecuencias; la mezcla mantiene un historial de etiquetas, no un observable intrínseco de la fotografía de la vorticidad total; la prueba de acercamiento angular es local y no establece un atractor permanente. Ningún resultado resuelve el problema 3D de Navier–Stokes.

## Archivos

- `O37_MEZCLA_MONOTONA_Y_DIFERENCIA_PERSISTENTE_NS.es.md` — formulación completa, pruebas, limitaciones y condiciones.
- `verificar_o37.py` — cuadratura determinista del efecto angular inicial, control de la expansión lejana y soluciones radiales exactas de NS como prueba de la mezcla.
- `resultados_o37.json` — salida auditada.
- `ANTECEDENTE_O36_FORMALIZACION.es.md` — antecedente inmediatamente anterior; copia sin modificaciones.
- `MANIFEST_SHA256.txt` — integridad de los demás archivos del paquete.

## Cómo reproducir

```bash
python -m pip install numpy scipy
python verificar_o37.py
```

El programa imprime un objeto JSON con `status: PASS`. Los controles de cuadratura **no** integran el sistema PDE completo ni sustituyen una prueba con errores intervalares; el signo analítico para `d=4000` procede de la desigualdad del documento, no de extrapolar la cuadratura realizada para `d=12`.

## Precisión epistemológica

**[T]** Ley de mezcla exacta y condición de existencia de un intervalo de coexistencia de dos concentraciones diferenciadas.  
**[T, con contrato]** Acercamiento inicial de fase cuadrupolar por Biot–Savart para una familia explícita.  
**[E]** Controles numéricos de datos iniciales y soluciones radiales exactas.  
**[A]** Cierre dinámico de dos remolinos con sincronización de frecuencias, estable ante perturbaciones durante tiempos extensos, o reconstruible sin historial de componentes.
