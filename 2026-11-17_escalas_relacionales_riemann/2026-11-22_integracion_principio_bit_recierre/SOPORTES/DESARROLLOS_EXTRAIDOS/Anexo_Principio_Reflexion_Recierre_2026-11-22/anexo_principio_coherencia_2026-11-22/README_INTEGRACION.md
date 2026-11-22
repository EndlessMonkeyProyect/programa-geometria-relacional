# Instrucciones de integración — anexo de correspondencias

**Destino propuesto:** directorio de anexos de Riemann existente, manteniendo el orden documental R–01/R–02 → R–03 → HC–02/03 → RA–01 → Compendio Riemann–CME. El archivo es complementario; no sustituye ni reescribe los teoremas previos.

## Archivos

- `ANEXO_CORRESPONDENCIAS_RECIERRE_Y_FRONTERA_ES.md`: nota de formalización, pruebas y dictamen.
- `scripts/verificar_coherencia.py`: control entero finito.
- `datos_octavas.csv`: salida reproducible.
- `MANIFIESTO_SHA256.txt`: huellas de los archivos precedentes.

## Reproducción

```bash
python3 scripts/verificar_coherencia.py --max-j 17 --salida datos_octavas.csv
sha256sum -c MANIFIESTO_SHA256.txt
```

El verificador utiliza exclusivamente la biblioteca estándar de Python 3. La reproducibilidad de los cálculos finitos no acredita la desigualdad asintótica equivalente a RH.

## Precisión editorial

1. Conservar la Proposición F de 21-XI como resultado previo, no como resultado independiente nuevo.
2. Clasificar como derivados elementales la involución de factores primos, la conservación de la norma y la identidad de frontera.
3. Mantener la Proposición 5 como reformulación exacta de la equivalencia clásica de Mertens con RH.
4. Incorporar el vínculo al índice del repositorio solo después de cotejar el destino en la rama activa; no hay publicación automática desde este ZIP.

**Endless Monkey Project / Relational Geometry Program**
