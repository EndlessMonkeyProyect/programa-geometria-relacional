# Registro de integración: T-EXT-01

Fecha: 30 de octubre de 2026. Documento base: SOLICITUD_REVISION_INTEGRAL_AJUSTADA.md.

## Incorporación

- Se añade T-EXT-01 a la sección 5, inmediatamente después de R5 y R6.
- Se declara la familia bipartita etiquetada con todas las posibles aristas entre dos partes equilibradas.
- La continuación exterior D_uv consiste exactamente en dos vértices nuevos y cinco aristas (ab,au,av,bu,bv).
- La interfaz contiene los n vértices originales; las consultas pueden acceder a cualquier par cruzado.
- La equivalencia H_E unión D_uv 3-coloreable si y solo si uv está ausente se prueba por K4 y por una coloración constructiva.
- Se deduce por indistinguibilidad que cualquier firma autosuficiente necesita al menos 2^floor(n²/4) estados y floor(n²/4) bits en codificación fija. La matriz de aristas alcanza la cota de almacenamiento en esta familia.
- Se incorpora un ensayo independiente de 4.672 consultas y el anexo técnico autosuficiente.
- Se agrega la pregunta 13 de revisión, manteniendo las doce originales.
- El resumen ejecutivo se actualiza y se conserva en una página.

## Límites y precisión

- El resultado es de información, no de tiempo ni de separación P/NP.
- No establece la misma cota para interfaces parciales arbitrarias.
- Cualquier acceso persistente al grafo original debe contarse en el estado autosuficiente si se pretende aplicar la cota.
- R6 estudia inserciones sobre los mismos vértices; T-EXT-01 permite nuevos vértices. Los contratos no se confunden.
- La bibliografía y originalidad de T-EXT-01 quedan abiertas a evaluación independiente.

## Reproducción

Ejecutar: `python3 verificar_T_EXT_01.py` en esta carpeta. Se genera `RESULTADOS_T_EXT_01.json`.

Se preservan las fuentes técnicas históricas sin reescribir sus resultados.
