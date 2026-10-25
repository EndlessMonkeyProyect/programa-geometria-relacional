---
title: "¿Sobrevive una genealogía al cierre? Respuesta a ROSI y a la revisión externa"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
editorial: "Formalización asistida; suplemento de la v2.4"
version: "2.5 — 2026-10-13"
status: "Resultados exactos + estados ROSI propuestos + dos correcciones verificadas; ninguna derivación física"
---

# ¿Sobrevive una genealogía al cierre?

Dos revisiones evaluaron la formalización v1: ROSI, en formato de estados, y otro
modelo, con un laboratorio propio. Esta nota responde a ambas desde el estado v2.4,
contesta el discriminante que ROSI marcó como prioritario y precisa una lectura de la
v2.3. Código: `experiments/genealogia_y_cierre_v2_5.py`. Pruebas:
`tests/test_genealogia_y_cierre_v2_5.py`.

---

## 1. El discriminante prioritario

> **ROSI_SIGUIENTE_DISCRIMINANTE_PRIORITARIO.** ¿Puede una misma identidad numérica
> sostener diferencias relacionales operacionalmente distinguibles, separables sin
> preguntas artificiales y conservadas después del cierre?

**Criterio** `DEFINICIÓN`, desde T1 y P5. Dos historias son equivalentes respecto de un
lenguaje si ninguna continuación de ese lenguaje las separa. Una pregunta sobre la
historia es legítima en el lenguaje de valores sólo si desciende al cociente: si es
constante sobre cada clase de valor. Una pregunta que no desciende es justo lo que ROSI
llama «distinguir artificialmente».

### 1.1 En los enteros: no `DERIVADO`

Las cuatro genealogías del 9, 8+1, 3·3, 8² − 5·11 y 32 − 23, valen lo mismo, y la
evaluación es un homomorfismo: toda continuación aritmética ve sólo el valor. Se
comprobó con 1849 continuaciones de profundidad ≤ 2 con +, − y × (`test_ninguna_continuacion_separa_las_genealogias_del_9`).

La pregunta que propuso la revisión externa, «¿la expresión es m·m?», separa 3·3 de
8+1, pero no desciende al valor (`test_la_pregunta_sintactica_no_desciende_al_valor`).
Es una pregunta del lenguaje de historias, no del de valores. Por P5, no es una relación
del cociente.

**El 9 no guarda su historia.** En un álgebra asociativa y conmutativa, el cierre lo
borra todo: no hay dónde guardar cómo se llegó.

### 1.2 En el hilo del dos: sí, y con dos partes `DERIVADO`

Una historia de unidades tiene dos componentes: **el orden de los factores** (quién va
antes en la fila) y **la agrupación** (qué pareja se juntó primero). Sobre unidades
imaginarias distintas:

| Nivel | Pares en que el orden cambia el signo | Tríos en que la agrupación cambia el signo | Bits que deja una historia |
|---:|---:|---:|---:|
| 2 | — (una sola unidad imaginaria) | — | 0 |
| 4 | 6 de 6 | 0 de 6 | ≤ 1 |
| **8** | **42 de 42** | **168 de 210** | **≤ 1** |
| 16 | 210 de 210 | 1848 de 2730 | ≤ 1 (muestra de 420 tríos) |

Prueba: `test_orden_desde_el_4_agrupacion_desde_el_8`, `test_toda_historia_de_un_trio_deja_un_destino_y_a_lo_sumo_un_bit`.

En el 8, (e₁e₂)e₄ = e₇ y e₁(e₂e₄) = −e₇: mismo destino, valor distinto. La pregunta
«¿qué signo?» no desciende al cociente de destinos (`test_en_el_8_el_signo_no_desciende_al_destino`),
pero la contesta la evaluación misma del álgebra, sin ningún predicado añadido. Es
legítima en el lenguaje de historias del 8 y no en el de destinos: exactamente la
situación de T7.

**Respuesta.** Sí: el primer lugar del hilo donde la historia sobrevive al cierre por la
operación propia del álgebra es el 4, para el orden de los factores; el 8 agrega la
agrupación. En los enteros no sobrevive nada.

### 1.3 Precisión a la v2.3 `CORRECCIÓN`

La v2.3 decía «hasta el 4, una unidad cerrada olvida cómo se formó». Es cierto para la
agrupación, no para el orden de los factores: en el 4, e_i e_j = −e_j e_i. La lectura
precisa es:

- **Desde el 4**, lo compuesto recuerda **quién iba antes** en la fila.
- **Desde el 8**, recuerda además **qué se juntó primero**: el orden de los cierres.
- En ambos casos, para unidades, a lo sumo un bit.

La tesis del autor sobre el antes y el después (T7, lectura del orden) tiene ahora dos
candidatos: el orden de posición, que aparece en el 4, y el orden de los cierres, que
aparece en el 8. El texto de la v2.2, la v2.3 y el documento ya los distingue. Cuál de
los dos es el que la tesis del tiempo necesita queda para el autor `ABIERTO`.

## 2. Estados de ROSI, propuestos desde la v2.5

Los estados son una propuesta de actualización; ROSI debería reevaluarlos.

| Ítem | Estado en la v1 | Estado propuesto | Por qué |
|---|---|---|---|
| EVALUACION_GLOBAL | OPEN | OPEN | Siguen abiertos el radio relacional completo y los observables físicos |
| INTEGRIDAD_REPRODUCCION | RESOLVED | RESOLVED | 71 pruebas en verde sobre extracción limpia |
| REFLEXION_RESIDUO_T1_T2 | RESOLVED | RESOLVED | Sin cambios |
| GENEALOGIA_CARDINAL_T3 | RESOLVED | RESOLVED | Exacto, pero su contenido es sólo el tamaño del número (v2) |
| ORIGEN_NECESARIO_REGLA_PG | OPEN | **TRANSFERRED** | La v2 archivó la genealogía aditiva y pasó a la multiplicativa (2^k ± 1, Zsigmondy). Que los centros sean potencias de dos queda como postulado del dos |
| CIERRE_CARDINALIDAD_INTERFAZ | RESOLVED | RESOLVED | Sin cambios |
| RADIO_ESCALAR_F1 | RESOLVED | RESOLVED | Sin cambios |
| RADIO_RELACIONAL_UNIVERSAL | SUPERPOSED | SUPERPOSED, acotado | Radio estructural = clase en el retículo (T5); escalar = radio de la propia clase (T6, §25 corregido). El radio físico sigue superpuesto |
| INFORMACION_GENEALOGICA_NUEVE | OPEN | **RESOLVED** | §1: en los enteros ninguna pregunta legítima separa las genealogías; la equivalencia es la de T1 |
| MASA_LEY_MODAL_CONDICIONAL | RESOLVED | RESOLVED | La v2 lo contrastó con el PDG: falsado para una sola escala |
| INFORMACION_COMO_MASA_FISICA | OPEN | OPEN | Falta correr el protocolo de la v2.1 |
| CAPSULAS_GF2_Y_P_NP | OPEN | OPEN, localizado | Es P vs NP (v2, Schaefer); el repertorio declarado quedó falsado (v2.4) |
| SIGUIENTE_DISCRIMINANTE_PRIORITARIO | OPEN | **RESOLVED** | §1: no en los enteros; sí en el hilo del dos, desde el 4 por orden y desde el 8 por agrupación |

**Siguiente discriminante propuesto.** Cuál de los dos órdenes, el de posición o el de
los cierres, es el que la tesis del tiempo necesita, y qué observable lo distinguiría.

## 3. Correcciones verificadas a la revisión externa

| Afirmación | Verificación | Prueba |
|---|---|---|
| «Herencia» = 9, 25, 49, 81…; «novedad pura» = 7, 11, 13… | Su «herencia» es exactamente la lista de cuadrados impares. Su «novedad pura» incluye 15 compuestos hasta 81: 15, 21, 27 = 3³, 33, 35, 39, 45, … | `test_la_herencia_de_la_revision_son_los_cuadrados_impares` |
| Componer k cláusulas OR₃ exige 3^k componentes afines | Falso como mínimo. Búsqueda exhaustiva: 3 con una cláusula y **6, no 9**, con dos. Sigue siendo exponencial por conteo, al menos (7/4)^k, pero sólo en el lenguaje «uniones de subespacios afines»; la CNF misma usa k cláusulas (MF-14) | `test_cobertura_afin_minima_no_es_tres_a_la_k` |
| ¿Existe un lenguaje cerrado bajo proyección, polinómico, fuera del sector afín? | Sí, trivialmente: 2-CNF. La versión no trivial, para una familia NP-completa, es P = NP (v2, O5) | Comprobación en la conversación; resultado clásico |
| «O1 cerrada» con `es_autorreflexion_cuadratica` | La pregunta no desciende al valor (§1.1): reformula la O1, no la cierra | `test_la_pregunta_sintactica_no_desciende_al_valor` |

El laboratorio de la revisión externa no venía adjunto y, según su propio informe, quedó
con cuatro pruebas fallando y correcciones sin ejecutar. No se integra.

## 4. Adiciones a la matriz epistémica

| Enunciado | Etiqueta | Prueba |
|---|---|---|
| Las genealogías del 9 no sobreviven al cierre en los enteros | DERIVADO | `test_ninguna_continuacion_separa_las_genealogias_del_9` |
| «¿Es m·m?» no desciende al valor | DERIVADO | `test_la_pregunta_sintactica_no_desciende_al_valor` |
| El orden sobrevive desde el 4; la agrupación, desde el 8 | DERIVADO | `test_orden_desde_el_4_agrupacion_desde_el_8` |
| Toda historia de unidades deja un destino y a lo sumo un bit | DERIVADO | `test_toda_historia_de_un_trio_deja_un_destino_y_a_lo_sumo_un_bit` |
| En el 8, el signo no desciende al destino | DERIVADO | `test_en_el_8_el_signo_no_desciende_al_destino` |
| La tabla de herencia externa es «cuadrado impar sí o no» | CORRECCIÓN | `test_la_herencia_de_la_revision_son_los_cuadrados_impares` |
| Cobertura afín mínima: 3 y 6, no 3^k | CORRECCIÓN | `test_cobertura_afin_minima_no_es_tres_a_la_k` |
| Qué orden necesita la tesis del tiempo | ABIERTO, del autor | — |

## Reproducir

```bash
python -m unittest discover -s tests -p "test_genealogia_y_cierre_v2_5.py" -v
python experiments/genealogia_y_cierre_v2_5.py
```
