# Instrucciones para integrar el marco de derivación

**Repositorio destino:** https://github.com/EndlessMonkeyProyect/programa-geometria-relacional  
**Fecha del expediente:** 21-XI-2026

## Alcance del cambio

Agregar la nueva carpeta:

`2026-11-17_escalas_relacionales_riemann/2026-11-21_aparicion_herencia_acarreos/`

Contiene un informe académico formal en Markdown, dos verificadores de Python, su salida JSON, README y manifiesto SHA-256. **No reemplazar** `FORMALIZACION_R01_R02_ES.md`, ni R–03, ni el contenido de los PR abiertos (#9 y #11). Crear una rama específica; comprobar conflictos y mantener los artefactos originales sin modificaciones.

## Protocolo de integración

1. Extraer el ZIP **en la raíz del repositorio** para conservar las rutas.
2. Ejecutar desde la carpeta nueva `python3 verificar_marco.py --max-m 1024` (o `py -3` en Windows).
3. Ejecutar `python3 verificar_manifest.py`. El manifiesto corresponde a la ejecución de referencia incluida; si se vuelven a generar archivos, se deben regenerar explícitamente las huellas antes de la revisión.
4. Revisar fórmulas renderizadas en GitHub, en especial (4.2), (5.1), (7.2) y (8.4).
5. Abrir un **pull request en revisión**. Solicitar examen matemático de la regla de acarreos y el alcance lógico del criterio equivalente a RH.
6. Integrar únicamente tras la revisión técnica y la validación de todos los controles.

## Título sugerido del PR

`Formalizar aparición, herencia y acarreos: identidad de memoria y cotas por referencia`

## Descripción sugerida del PR

Se incorpora una formalización de continuidad que parte de la incorporación por potencias primas y deriva la reconstrucción multiplicativa, la descomposición exacta de la duplicación de escala y la actualización unitaria del factor de memoria `B(m)`. Se demuestra una cota óptima de activación para cada potencia prima sobre ventanas enteras y se distingue de una estimación uniforme con frontera creciente. La relación con la hipótesis de Riemann se presenta como **reformulación de un criterio clásico**, no como una nueva prueba. Se adjuntan controles exactos y manifiesto de integridad.

## Criterio editorial

Presentar primero definiciones, mecanismos y resultados demostrados. La ontología se mantiene afirmativa: aparición, conservación, ampliación, combinación y herencia. Emplear los signos únicamente en mediciones matemáticas. Mantener la procedencia explícita de factorización única, Legendre, Kummer, CRT y von Koch.

**Endless Monkey Project / Relational Geometry Program**
