# Aparición, herencia y acarreos — marco de derivación

**21 de noviembre de 2026 · versión 1.0 · revisión técnica**

Esta carpeta documenta una formalización de continuidad a partir de las primeras apariciones de potencias primas, la herencia por divisibilidad y la acumulación en el m.c.m. Se integra en la línea **R–01/R–02 → R–03 → HC–03** y no reemplaza esos documentos.

## Documentos

- [`MARCO_DERIVACION_ES.md`](MARCO_DERIVACION_ES.md): siete proposiciones con hipótesis, demostraciones, procedencia y límite de las conclusiones.
- [`verificar_marco.py`](verificar_marco.py): verificación con enteros y fracciones exactas; únicamente biblioteca estándar de Python 3.9+.
- [`resultado_verificacion.json`](resultado_verificacion.json): resultado de ejecución de referencia con `--max-m 1024`.
- [`verificar_manifest.py`](verificar_manifest.py): comprobación de las huellas de integridad.
- [`INSTRUCCIONES_INTEGRACION.md`](INSTRUCCIONES_INTEGRACION.md): procedimiento para incorporar este anexo en GitHub.
- [`MANIFEST.sha256`](MANIFEST.sha256): hashes de los archivos de esta entrega, excepto el propio manifiesto.

## Ejecutar

Desde esta carpeta:

```bash
python3 verificar_marco.py --max-m 1024
python3 verificar_manifest.py
```

En Windows se puede utilizar `py -3` en lugar de `python3`.

El script principal imprime una línea `OK` en ASCII y genera `resultado_verificacion.json` en UTF-8. La salida contiene el número de controles exactos, los rangos y casos de comparación. Para un rango mayor se puede usar, por ejemplo, `--max-m 2048` y después regenerar el manifiesto antes de publicarlo. La ejecución de referencia evita dependencias de coma flotante.

## Resultado y alcance

La regla exacta de incorporación es `r(n)=L(n)/L(n-1)` y el factor de memoria en una duplicación satisface `binom(2m,m)=A(m)B(m)`. El documento demuestra una actualización local de `B(m)`, la organización por acarreos y una cota óptima para las activaciones de una potencia prima en una ventana cualquiera.

La conexión a RH se limita a reescribir una equivalencia clásica de von Koch en términos de `B(m)`: **no se ha demostrado la estimación global correspondiente ni una prueba nueva de RH**. Los fundamentos son factorización única, Legendre, Kummer, teorema chino del resto y Stirling.

## Procedencia y continuidad

- [R–01/R–02: criba y escalas](../FORMALIZACION_R01_R02_ES.md).
- [R–03: herencia espectral](../2026-11-18_r03_herencia_espectral/R03_HERENCIA_Y_LOCALIZACION_ES.md).
- HC–03 y las notas de continuidad del 21-XI-2026 son el antecedente inmediato; sus artefactos no se duplican en esta entrega.

La exposición conserva la ontología afirmativa: aparición, incorporación, conservación, combinación y herencia. Las comparaciones con signo son operaciones matemáticas para medir un error, no entidades del mecanismo.

**Endless Monkey Project / Relational Geometry Program**
