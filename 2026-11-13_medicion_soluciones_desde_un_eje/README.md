# Medición de soluciones respecto de un eje

**Nota matemática de investigación v0.2 · 13 de noviembre de 2026**  
**Autor público:** Le Matt Ansatz Di Ego  
**Programa:** Endless Monkey Project · Relational Geometry Program

Esta entrega estudia distribuciones de soluciones proyectadas sobre una recta de valores. Obtiene momentos de raíces reales a partir de coeficientes, recupera los tres primeros momentos de soluciones booleanas mediante conteos restringidos y usa el rango de Hankel para certificar el mínimo de posiciones de una distribución atómica positiva. El manuscrito presenta dos pares de ejemplos y una agenda para estudiar el costo de las consultas y su reutilización.

## Lectura

- [Manuscrito en español](MEDICION_SOLUCIONES_DESDE_UN_EJE.md) · [PDF](MEDICION_SOLUCIONES_DESDE_UN_EJE.pdf)
- [English manuscript](MEASURING_SOLUTIONS_RELATIVE_TO_AN_AXIS.en.md) · [PDF](MEASURING_SOLUTIONS_RELATIVE_TO_AN_AXIS.en.pdf)

El manuscrito en español es la referencia para la notación y las afirmaciones matemáticas.

## Verificación

Con Python 3.12 y la dependencia declarada en `requirements.txt`:

```bash
python -m pip install -r requirements.txt
python verificar_eje.py
```

La ejecución imprime `TODAS LAS PRUEBAS EXACTAS: OK` cuando coinciden los momentos, los conteos de Sturm, los conteos restringidos, la dispersión y los rangos de Hankel. [Resultados de referencia](RESULTADOS_VERIFICACION.txt).

## Derechos

[Declaración de derechos de esta entrega](RIGHTS.md). Cada archivo conserva sus condiciones de uso.
