# O56 — Normalizador, novedad y perpendicularidad material

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 21 oct 2026**

Continuación de O54, O55, O45 y O40; **suplemento aditivo** a la Imagen Total v3.8.1. No reemplaza archivos históricos ni afirma solución global de Navier–Stokes.

## Hallazgo

Dos soluciones exactas de Navier–Stokes con **iguales** escala, energía y enstrofía inicial pueden transportar dos tangentes marcadas de un mismo toroide inicial hasta **ángulos diferentes**, conservando su normalizador aritmético. En la cizalla X la perpendicularidad se conserva (90°); en la cizalla Y termina en **81.633°**. La diferencia predictiva *a primer orden* es `K = aᵀ S b`, una relación nueva de orientación/gradiente que no contiene el múltiplo por sí solo.

En un ensayo numérico de anillo vorticial NS con el mismo perfil inicial y cizallas X/Y (malla 32³) obtuvimos ángulos **91.106°** y **81.796°**, respectivamente, con energía, enstrofía y geometría inicial global iguales. La posición de la marca material importa; los campos X/Y son equivalentes bajo una rotación física si se gira también el observador y su marca.

**Otro resultado importante:** la pérdida de perpendicularidad local no equivale a desaparición topológica del toroide; existe un contraejemplo exacto de volumen constante. La propia regularidad de Navier–Stokes no se deduce de ese comparador.

## Orden de lectura

- `O56_FORMALIZACION.es.md`: ontología, derivaciones exactas, testigos, resultados y límites.
- `codigo/ensayo_o56.py`: flujo NS exacto, comparador y 21 controles.
- `codigo/simulacion_toroide_O56.py`: continuación directa del motor numérico de O55 con perturbaciones X e Y, sin fuerza exterior.
- `resultados/`: series de tiempo, resúmenes JSON y observaciones del O55 histórico para contraste.
- `graficos/`: ángulo material y cociente global, distinguiendo ambas escalas.
- `fuentes/`: script y serie original de O55 (fuentes preservadas sin cambios).
- `MANIFEST_SHA256.json` / `verificar_paquete.py`: integridad de esta edición.

## Alcance epistemológico

Demostrado en un modelo exacto, observado en una simulación numérica corta, **no** prueba de estabilidad global, de novedad física universal o de una ley de actualización del múltiplo. La rejilla aritmética `10→20` es *declarada como comparación*, nunca determinada por la ecuación de NS.

La bibliografía externa, cuando se use, es comparación crítica y no fundamento constitutivo de la ontología.
