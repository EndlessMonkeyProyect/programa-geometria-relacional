# El hilo del dos — Formalización consolidada v2.8

**Autor del programa:** Le Matt Ansatz Di Ego  
**Edición:** 14 de octubre de 2026  
**Método editorial:** conservación de ontología y lenguaje; extensiones aditivas y límites explícitos.

## Principio de lectura

La pregunta ontológica conduce al lenguaje; el lenguaje permite expresar reglas
lógicas; la matemática deriva consecuencias condicionales; el código contrasta
implementaciones; la física exige predicciones y observables independientes.
**No se invierte ese orden para presentar una representación como necesidad física.**

## Ruta recomendada

1. `docs/HILO_DEL_DOS_FORMALIZACION_v2.md`: texto principal, **sin reescribir**.
2. `docs/CONTINUIDAD_ONTOLOGICA_Y_ESTADOS_v2_8.md`: mapa de correspondencias,
   preguntas y estados de cierre.
3. `docs/N1_B_CERTIFICADOS_Y_PRIORIDAD_v2_8.md`: invariante, inducción y
   cota reforzada para cualquier prioridad permitida del motor O2c.
4. `docs/T8_DEL_LENGUAJE_AL_ESPACIO_v2_8.md`: familia T8(n), distinciones y
   frontera entre construcción matemática y espacio físico.
5. Documentos v2.1–v2.7: siguen intactos como historial técnico y ontológico.
   Donde alguna frase anterior excede su demostración, **rige el alcance v2.8**,
   sin borrar su formulación original.

## Dos resultados depurados

| Tema | Cierre ganado | Límite abierto |
|---|---|---|
| N1-B | Toda ejecución insatisfacible de O2c v1.6 con Join/Project/Normalize tiene refutación por resolución, con `pasos ≤ 1.5 × total_candidates`, independiente de la prioridad | No cubre otros sistemas de prueba o todo algoritmo de 3-coloración; el selector puede tener costo adicional |
| T8 | Paridades de n distinciones, código símplex, dimensión representacional `2^n−1`; n=2 produce cuatro estados y tres ejes | No demuestra por qué n=2 ni que los tres ejes sean el espacio físico; falta definir el nuevo enunciado de la quinta referencia sin presuponer métrica |

## Archivos añadidos en v2.8

- `docs/CONTINUIDAD_ONTOLOGICA_Y_ESTADOS_v2_8.md`
- `docs/N1_B_CERTIFICADOS_Y_PRIORIDAD_v2_8.md`
- `docs/T8_DEL_LENGUAJE_AL_ESPACIO_v2_8.md`
- `experiments/prioridad_fija_v2_8.py` — ejecuta prioridades prefijadas y un
  control independiente del contador para grafos pequeños no coloreables.
- `experiments/t8_familia_v2_8.py` — verifica paridades y rangos afines para n=1..4.
- `tests/test_prioridad_fija_v2_8.py`
- `tests/test_t8_familia_v2_8.py`
- `results/prioridad_fija_v2_8.json`
- `results/t8_familia_v2_8.json`
- `auditorias/AUDITORIA_PREVIA_N1B_T8_2026-10-14.md` — auditoría previa
  conservada; su obligación inductiva queda atendida en la nueva nota N1-B.
- `antecedentes/README_v2_7.md` — índice original v2.7, preservado.

## Verificaciones efectuadas

Desde la raíz del ZIP extraído:

```bash
python -m unittest discover -s tests -q
python experiments/prioridad_fija_v2_8.py
python experiments/t8_familia_v2_8.py
```

- **89 pruebas unitarias satisfactorias** (85 originales, 4 añadidas).
- **1488 ejecuciones** de prioridades prefijadas: todas las permutaciones de K4
  (24) y rueda de 6 vértices (720), cada una con frontera vacía y frontera de 2.
- Todas obtuvieron refutaciones verificadas y concordaron con una segunda
  implementación del contador; no se encontraron infracciones de la cota 3/2.
- T8(1..4) verificó los conteos y la pauta [1,1,1,3] de la quinta palabra.

**Advertencia epistémica:** estas pruebas son controles finitos. La afirmación
universal N1-B se justifica por la inducción escrita en el suplemento, dentro de
las hipótesis de O2c. El texto sigue siendo una formalización susceptible de
revisión matemática externa; no equivale a una solución de P frente a NP.

## Integridad y antecedentes

- `SHA256_MANIFEST.json` contiene las huellas de todos los archivos del paquete,
  excepto el propio manifiesto, y la huella del ZIP v2.7 de origen.
- Los dos motores fuente en `experiments/o2c_v1_6/` son idénticos al original.
- Los documentos preexistentes de `docs/` no se alteraron, incluyendo sus
  enunciados históricos. Los nuevos suplementos precisan el alcance sin
  reescribirlos.
