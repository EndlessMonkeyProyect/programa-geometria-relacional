# Cómo continuar el repositorio

## Preservar la historia

No editar fuentes/originales ni sustituir una fuente por una versión corregida. Incorporar una nueva versión con nombre distinto, registrar su procedencia y actualizar el manifiesto. Conservar las auditorías anteriores.

## Añadir un resultado

Cada resultado nuevo debe indicar:
1. pregunta;
2. objetos, dominios e hipótesis;
3. afirmación;
4. demostración o procedimiento;
5. ejemplo y contraejemplo relevante;
6. alcance y dependencias;
7. fuentes o archivos que modifica conceptualmente.

Un control numérico se etiqueta como control, no como demostración general. Una definición nueva no se describe como derivación de su necesidad física.

## Actualizar síntesis

Identificar el resultado del registro al que afecta. Explicar si corrige, restringe, generaliza o reemplaza una formulación. Verificar que no cambia inadvertidamente el significado de cápsula, referencia, residuo, dimensión o cierre.

## Comprobar

~~~bash
python3 herramientas/verificar.py
python3 ejemplos/comprobaciones.py
~~~

Los comandos usan la biblioteca estándar de Python. Sus informes van a la salida estándar; guardar resultados sólo cuando se quiera registrar una nueva revisión.

## Publicación

El repositorio de esta edición se publica en [EndlessMonkeyProyect/programa-geometria-relacional](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional). La edición no atribuye una licencia abierta por defecto. El primer commit es de organización editorial, no acredita la fecha original de descubrimiento de los resultados.
