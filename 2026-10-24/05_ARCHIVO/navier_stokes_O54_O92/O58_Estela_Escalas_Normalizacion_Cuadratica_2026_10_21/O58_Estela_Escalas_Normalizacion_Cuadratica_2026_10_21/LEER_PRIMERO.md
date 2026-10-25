# O58 — Estela de escalas, cuadrados y unidad pendiente

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 21 octubre 2026**

## Qué contiene

Un suplemento aditivo que retoma la corrección ontológica después de O57: no tomar el ángulo entre tangentes como condición ontológica fundamental; investigar el transporte del **múltiplo normalizador de dos relaciones cuadráticas** y la **unidad de resto**.

El análisis mantiene dos operaciones aritméticas distintas:

1. Identidad bilateral canónica: `N²−(N−1)(N+1)=1`, válida para todo entero N.
2. Hipótesis fuerte de dos cuadrados: `a²+b²+1=N²`, que sólo admite determinadas ternas enteras. **Se solicita confirmar que ésta es la lectura buscada**.

### Qué está demostrado

La familia `N²−2m²=1` admite infinitas soluciones exactas: `3,17,99,577,...` para N. Existe una cadena compatible por múltiplos `3→99→3880899→...`. Una transición de escala pura transforma el resto bruto 1 en `q²`; si se exige volver a resto 1 con otro N, los canales normalizados deben cambiar. El balance de esa reorganización queda demostrado y puede reconstruirse con la referencia anterior.

### Qué NO está demostrado

No hay regla física deducida de Navier–Stokes que obligue a seleccionar esos múltiplos; la aritmética muestra **ramificación**. La identidad no demuestra estabilidad de anillo vorticial, regularidad global, tiempo físico ni ninguna ley cosmológica.

## Archivos

- `O58_FORMALIZACION.es.md`: relato ontológico → contratos → teoremas → estela → condiciones para el puente de NS.
- `codigo/o58_verificar.py`: pruebas con enteros exactos y `fractions.Fraction`, Python estándar.
- `resultados/soluciones_hasta_200.csv`: censo limitado de pares positivos enteros, sin duplicar por permutación.
- `resultados/estela_pell.csv`: familia infinita representada por primeros ocho elementos.
- `resultados/estela_anidada.csv`: primeros cinco elementos de cadena con divisibilidad explícita.
- `resultados/ramas_compatibles_hasta_200.csv`: aristas de divisibilidad y variación de pesos normalizados.
- `resultados/verificacion.json`: registro de comprobaciones.
- `MANIFEST_SHA256.json` y `verificar_integridad.py`: integridad de archivos.

**Reproducir:** `python3 codigo/o58_verificar.py && python3 verificar_integridad.py`.

**Integración:** suplemento autónomo, **sin modificar** la Imagen Total candidata v3.8.1 ni versiones previas O40–O57.
