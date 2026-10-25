---
title: "Duplicar o recerrar, y cómo contrastar la masa como residuo"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
editorial: "Formalización asistida; suplemento de la v2"
version: "2.1 — 2026-10-13"
status: "Material para una decisión del autor + protocolo de contraste; no decide la ontología ni deriva masas"
---

# Duplicar o recerrar, y cómo contrastar la masa como residuo

Esta nota prepara los dos pasos que la v2 dejó abiertos. La parte A calcula qué
implica cada lectura de la reflexión, para que el autor decida. La parte B fija
cómo contrastar la hipótesis de masa como residuo sin caer en coincidencias, y
mide cuánto vale cada coincidencia conocida.

Código: `experiments/decision_y_contraste_v2_1.py`. Pruebas:
`tests/test_decision_y_contraste_v2_1.py`. Resultados:
`results/decision_y_contraste_v2_1.json`.

---

# A. Duplicar o recerrar

## A.1 Tres lecturas `DEFINICIÓN`

| Lectura | Centros | Qué hace la profundidad h |
|---|---|---|
| **Duplicar** | 2, 4, 8, 16, 32… (2^k) | Sube de a un nivel |
| **Recerrar** | 2, 4, 16, 256, 65536 (2^(2^m)) | Se duplica: cada paso cierra todo lo anterior |
| **Ambas, en planos distintos** | El hilo duplica; las cápsulas se cierran en h = 1, 2, 4, 8, 16 | Sube de a uno; los cierres caen en potencias de dos |

Los tres esquemas parten aquí del centro 2, con imágenes 1 y 3. Si se parte del 4, como en la v2, el 3 cuenta como nuevo en el 4 y nada más cambia.

## A.2 Consecuencias calculadas `DERIVADO`

| Criterio | Duplicar | Recerrar | Ambas |
|---|---|---|---|
| Radio de la clase | 2^(−k) | 2^(−2^m) | 2^(−h); en los cierres 2^(−2^m) |
| Imagen superior sin palabra nueva | Sólo el centro 8 | Nunca: los números de Fermat son coprimos | Sólo en h = 3, que no es un cierre |
| Imagen inferior heredada | Cuando k es par | Siempre: es el producto de todo lo anterior | En todo cierre con h ≥ 2 y en los pasos pares intermedios |
| Novedad de un solo primo | Varía por nivel | Pasos 0 a 4 (3, 5, 17, 257, 65537); en el paso 5 se parte: 641 · 6700417 | Igual que recerrar en los cierres |
| Qué es una cápsula | Cada nivel | Cada paso, como unidad de todo lo anterior | Sólo los niveles de cierre; los demás son refinamiento abierto |

Dato clásico sobre la columna de recerrar: no se conoce ningún primo de Fermat
después de 65537; todos los F_m comprobados desde m = 5 son compuestos. Bajo
recerrar, la novedad deja de ser una sola palabra desde el sexto paso.

## A.3 A qué compromete cada lectura `POSTULADO` · `ABIERTO`

**Duplicar.** Hay novedad en casi todo nivel y la anomalía del 8 es un hecho del
esquema. Todo nivel es cápsula, así que no hay puntos de cierre privilegiados: el
4 del programa sería un nivel más.

**Recerrar.** Es la separación más limpia entre herencia y novedad: cada paso es
todo lo anterior cerrado más algo coprimo. Pero los niveles 3, 5, 6 y 7 no existen,
el centro 8 no aparece, y la asimetría entre 7 y 9 queda fuera del esquema.

**Ambas.** Conserva los dos hechos. La anomalía del 8 ocurre en h = 3, entre los
cierres de h = 2 y h = 4: es refinamiento abierto, no una cápsula. El primer cierre
cuya unidad contiene más de una palabra es h = 4, con 15 = 3·5. Eso le da al 4 un
papel estructural en esta lectura: primer cierre compuesto. Es una lectura, no una
derivación física de q = 4.

**Compatibilidad con lo que el autor ya escribió.** Los textos usan centros que se
duplican (4 → (3, 5); 8 → (7, 9)) y también dicen que una cápsula cerrada participa
como unidad en una escala ulterior. Sólo la lectura «ambas» es compatible con las
dos afirmaciones a la vez. La decisión sigue siendo del autor.

## A.4 La pregunta que decide `ABIERTO`

> ¿El 8 es una cápsula cerrada o un paso intermedio del hilo?

Si es cápsula, la lectura es duplicar. Si sólo cierran 2, 4, 16 y 256, la lectura es
recerrar o ambas. Si el hilo pasa por el 8 sin cerrarlo, la lectura es ambas.

---

# B. Cómo contrastar la masa como residuo

## B.1 Lo que exigen los leptones `DERIVADO`

Si la masa creciera como 2 elevado al residuo, los residuos deberían diferir en:

| Cociente | Valor (PDG 2025) | Bits: log₂ del cociente |
|---|---:|---:|
| muón / electrón | 206.768 | 7.692 |
| tau / electrón | 3477.37 | 11.764 |
| tau / muón | 16.818 | 4.072 |

Ninguno es entero: 2^7 = 128 y 2^8 = 256 encierran a 206.8. Con pesos uniformes y
residuos en bits enteros, ese mapa no reproduce los cocientes. Cualquier mapa
candidato debe declararse antes de mirar estos números.

## B.2 Calibrador de coincidencias `DEFINICIÓN` · `DERIVADO`

Una coincidencia vale tanto como su improbabilidad. El calibrador toma una familia
de fórmulas declarada, aquí 2^a · 3^b · 5^c · π^d con exponentes entre −4 y 4 (6561
fórmulas), y mide:

- **Aciertos:** fórmulas dentro de la tolerancia del objetivo.
- **Tasa base:** probabilidad de que un objetivo al azar, en una década alrededor,
  tenga al menos un acierto.
- **Tasa base igual de simple:** la misma probabilidad usando sólo fórmulas tan
  cortas como el acierto más corto (complejidad = suma de exponentes en valor
  absoluto).

| Caso | Tolerancia | Acierto más simple | Tasa base | Tasa igual de simple | Lectura |
|---|---|---|---:|---:|---|
| Protón: r_p / λ̄_p = 3.9977 | 1σ (7.6·10⁻⁴) | 4 = 2² | 51 % | 0.65 % | No es barata por la fórmula; falta descontar la elección de cantidades |
| Muón / electrón = 206.768 | 10⁻³ | 2²·5·π³/3 = 206.71 | 49 % | 18 % | Sin valor |
| Tau / muón = 16.818 | 10⁻² | 2·5²/3 = 16.67 | 100 % | 46 % | Sin valor |
| Tau / muón frente a potencias de 2 | 6 % | 16 = 2⁴ | 15 % | 10 % | Sin valor: «tau/muón ≈ 16» es una coincidencia de 1 en 7 a 10 |

**Lectura del protón** `CONTRASTE`. Dentro de esta familia, encontrar al azar un
acierto tan simple como el 4 a 1σ tiene una probabilidad cercana a 0.7 %. La
coincidencia que el programa comparte con Trinhammer y Bohr no se explica por la
libertad de fórmula. Sí quedan tres libertades sin descontar: elegir qué longitudes
comparar (radio de carga o magnético; λ̄ o λ = 2πλ̄), cuántas cantidades se
revisaron antes de encontrar ésta, y que el valor del hidrógeno muónico queda a
1.6σ. Es una pista que merece mecanismo, no una evidencia.

**Lectura de los leptones.** Las coincidencias simples con los cocientes leptónicos
no valen nada: cualquier objetivo al azar las tiene. Por eso la hipótesis de masa
como residuo sólo puede contrastarse con una predicción declarada de antemano.

## B.3 Protocolo `DEFINICIÓN`

1. Declarar antes de mirar los datos la familia de mapas residuo → masa y su
   número de parámetros libres.
2. Fijar los parámetros con a lo sumo un cociente; predecir el otro sin reajustar.
3. Reportar la tasa base del calibrador para la familia y la tolerancia usadas.
4. Contar un acierto como evidencia sólo si la tasa base es pequeña, por ejemplo
   menor que 1 %.
5. Publicar con fecha antes de contrastar con datos no usados. Koide no sirve como
   predicción: ya es conocido.

## B.4 Siguiente paso `ABIERTO`

Escribir el mapa residuo → masa que el autor considere natural, con un parámetro a
lo sumo, fijarlo con muón/electrón y predecir tau/electrón. Si acierta con tasa base
pequeña, la hipótesis gana su primer contraste; si no, queda falsada en esa forma.

---

# C. Adiciones a la matriz epistémica

| Enunciado | Etiqueta | Prueba |
|---|---|---|
| Recerrar: herencia completa y novedad coprima en cada paso | DERIVADO | `test_recerrar_hereda_todo_y_trae_novedad_coprima` |
| F_5 = 641 · 6700417: la novedad se parte | DERIVADO | `test_fermat_cinco_es_compuesto` |
| Ambas: cierres en h = 1, 2, 4, 8, 16; el 8 no es cierre | DERIVADO | `test_ambos_cierres_en_potencias_de_dos`, `test_ambos_la_anomalia_del_ocho_no_es_cierre` |
| Elección entre duplicar, recerrar o ambas | ABIERTO, decisión del autor | — |
| Cocientes leptónicos exigen residuos no enteros en bits | DERIVADO | `test_bits_requeridos` |
| Coincidencia del protón: improbable por la fórmula (≈ 0.7 %) | CONTRASTE pendiente de mecanismo | `test_casos_reportan_complejidad` |
| Coincidencias simples con leptones | CONTRASTE, sin valor | `test_casos_reportan_complejidad` |
| Masa como residuo con un parámetro | ABIERTO, protocolo B.3 | — |

## Fuentes

- Particle Data Group 2025, tabla de leptones: https://pdg.lbl.gov/2025/tables/rpp2025-sum-leptons.pdf
- CODATA 2022: radio de carga del protón 0.84075(64) fm (ver la nota del protón del repositorio v3.1).
- Números de Fermat y su factorización: resultado clásico (Euler, 1732, para F_5).
