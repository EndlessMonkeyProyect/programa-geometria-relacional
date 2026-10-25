# El hilo del dos — Formalización v2

**Autor del programa:** Le Matt Ansatz Di Ego
**Versión:** 2.7 · 14 de octubre de 2026
**Integra:** formalización v1 (13-10-2026), propuesta v4 «El hilo y el lenguaje» y laboratorio R14.1.

## Qué contiene

- `docs/HILO_DEL_DOS_FORMALIZACION_v2.md` — documento principal.
- `docs/DUPLICAR_O_RECERRAR_Y_CONTRASTE_DE_MASA_v2_1.md` — suplemento v2.1: material para decidir la lectura de la reflexión y protocolo para contrastar la masa como residuo.
- `docs/EL_OCHO_NODO_ABIERTO_v2_2.md` — suplemento v2.2: la respuesta del autor sobre el 8 y su formalización exacta.
- `docs/EL_BIT_ABIERTO_v2_3.md` — suplemento v2.3: el bit abierto del 8 (T7), escrito en el lenguaje de la ontología.
- `docs/MAPA_DE_ALGORITMOS_Y_FALSADOR_v2_4.md` — suplemento v2.4: dónde está cada algoritmo de la rama de cómputo y el falsador de MF-46 §14 corrido.
- `docs/GENEALOGIA_Y_CIERRE_v2_5.md` — suplemento v2.5: respuesta a ROSI y a la revisión externa; cuándo una genealogía sobrevive al cierre.
- `docs/MASA_COMO_COMPLEMENTO_v2_6.md` — nota v2.6: el modelo fundacional de masa en su texto, qué es exacto, qué se falsó y qué falta.
- `docs/DEL_CUATRO_A_LA_DISTANCIA_Y_EL_TIEMPO_v2_7.md` — nota v2.7: cómo nace la distancia en el paso del cuatro al cinco (T8), la decisión «tres y uno sin distinguir cuál» y las lecturas del tiempo, tipadas.
- `docs/PISO_DEL_CAMINO_v2_7.md` — nota v2.7: ningún selector hace polinómico al motor de tablas O2/O2c (no-go N1).
- `experiments/laboratorio_hilo_v2.py` — laboratorio exacto, sólo biblioteca estándar.
- `experiments/decision_y_contraste_v2_1.py` — esquemas duplicar/recerrar/ambos y calibrador de coincidencias.
- `experiments/ocho_nodo_abierto_v2_2.py` — construcción de Cayley–Dickson exacta y el nodo abierto del 8.
- `experiments/bit_abierto_v2_3.py` — T7: el bit abierto es real, relacional, latente, de orden y con límite.
- `experiments/falsador_v2_4.py` — reglas compartidas del 8 y arnés del falsador con cuatro familias y cuatro métodos.
- `experiments/genealogia_y_cierre_v2_5.py` — genealogías del 9 en los enteros, orden y agrupación en el hilo del dos, correcciones verificadas.
- `experiments/del_cuatro_a_la_distancia_v2_7.py` — T8: referencias, tres y uno, la quinta, Cayley–Menger y el 8; identidades del tiempo.
- `experiments/piso_del_camino_v2_7.py` — N1: el piso 3^(tw+1) y la corrida como refutación por resolución, verificada.
- `experiments/o2c_v1_6/` — los motores O2 y O2c del paquete O2C v1.6, copiados sin cambios.
- `tests/` — 85 pruebas (26 de la v2, 11 de la v2.1, 10 de la v2.2, 7 de la v2.3, 10 de la v2.4, 7 de la v2.5, 3 de la v2.6 y 11 de la v2.7).
- `results/` — tablas generadas por el laboratorio.
- `antecedentes/FORMALIZACION_CANONICA_REFLEXION_CARDINALIDAD_CAPSULAS_MASA_v1.md` — la v1, sin modificar.
- `SHA256_MANIFEST.json` — huellas de todos los archivos.

## Reproducir

```bash
python -m unittest discover -s tests -v
python experiments/laboratorio_hilo_v2.py
python experiments/decision_y_contraste_v2_1.py
python experiments/ocho_nodo_abierto_v2_2.py
python experiments/bit_abierto_v2_3.py
python experiments/falsador_v2_4.py   # unos 10 minutos
python experiments/genealogia_y_cierre_v2_5.py
python experiments/del_cuatro_a_la_distancia_v2_7.py
python experiments/piso_del_camino_v2_7.py   # medio minuto; la parte a escala usa numpy si está
```

## Lo principal en una tabla

| Tema | Resultado | Etiqueta |
|---|---|---|
| 7 frente a 9 | El centro 8 es la única excepción de Zsigmondy para la imagen superior: 9 = 3² es pura herencia | DERIVADO |
| Recierre | En los centros 2, 4, 16, 256, 65536 la imagen inferior es el producto de todo lo anterior y la superior es coprima con todo | DERIVADO |
| Genealogía aditiva de la v1 | Su primera aparición es sólo el tamaño del número; se archiva | DERIVADO |
| §25 | r_V = 2^(−h) es el radio de la propia clase y baja; r_m = 1 − 2^(−h) es la fracción ya distinguida y sube | DERIVADO |
| Información sostenida | Resolución, indeterminación y residuo interior, con Res + Ind = total | DERIVADO |
| Masa como complemento de la proyección | Definición exacta del modelo fundacional: coincide con E² = (pc)² + (mc²)²; no predice razones de masa por sí sola | DERIVADO |
| Complemento con una sola escala | Dos masas difieren a lo sumo √2; muón/electrón = 206.8: falsado | CONTRASTE falsado |
| Masa como residuo interior | Hipótesis nueva, bien tipada | CONTRASTE pendiente |
| Cápsulas fuera del sector afín para NP-completos | Por Schaefer, equivale a P = NP | DERIVADO |
| Duplicar, recerrar o ambas | El autor: el 8 es la estructura sobre la que crece, con un nodo abierto | POSTULADO |
| El 8 con nodo abierto | Octoniones: última álgebra de división; el destino de una composición se cierra y la orientación queda abierta, un bit, fuera de las líneas de Fano | DERIVADO |
| El bit abierto (T7) | Real (ninguna convención lo quita), relacional (aparece al comparar dos caminos, en ±2·e_(i⊕j⊕k)), latente (una unidad cerrada lo reabre con 4 de 5 terceras), de orden (a lo sumo un bit por historia) y con límite (se cancela en el 16) | DERIVADO |
| El bit como forma mínima del antes y el después | Lectura del autor; el puente al tiempo físico es hipótesis | POSTULADO |
| Reglas compartidas del 8 | El destino conserva x ⊕ y ⊕ z; el bit abierto sólo admite proyecciones, como 3-SAT | DERIVADO |
| Mapa de algoritmos | Cuatro zonas: lo que cierra el lenguaje de destinos, lo que paga por el residuo con un parámetro, búsqueda con aprendizaje y el blanco universal | Ubicación |
| Falsador de MF-46 §14 | Dispara para {DPLL, CAG afín, Davis–Putnam, tablas} en palomar y 3-CNF aleatoria; en la familia del 8, CAG absorbe los destinos pero las bifurcaciones se siguen duplicando | CONTRASTE, tamaños chicos |
| Genealogía y cierre | En los enteros, las genealogías del 9 no sobreviven al cierre; en el hilo del dos, el orden de los factores sobrevive desde el 4 y la agrupación desde el 8, a lo sumo un bit | DERIVADO |
| Revisión externa | Su tabla de herencia es «cuadrado impar sí o no»; la cobertura afín mínima de dos cláusulas es 6, no 9 | CORRECCIÓN |
| Del cuatro a la distancia (T8) | Dos distinciones dan cuatro referencias a igual distancia en 2² − 1 = 3 ejes; cumplen a⊕b⊕c⊕d = 0 sin que ninguna sea distinta; una quinta no cabe igual y señala a una; con cinco aparece la primera relación obligada entre comparaciones (Cayley–Menger): ahí nace la distancia | DERIVADO |
| Tres y uno sin distinguir cuál | Decisión del autor (14-10-2026); su contenido exacto es T8b | POSTULADO + DERIVADO |
| El tiempo como comparación de ritmos y la flecha como resolución | Lecturas del autor; exactos: compás = MCM, reloj propio = √r_m, OP¹ ≅ S⁸ | POSTULADO + DERIVADO |
| «Hacia el uno» universal | Choca con la expansión observada; en sistemas ligados queda abierto | CONTRASTE |
| El piso del camino (N1) | Todo orden del motor O2 cuesta ≥ 3^(tw+1); toda corrida no coloreable de O2c es una refutación por resolución: ningún selector lo hace polinómico | DERIVADO |
| Coincidencia del protón con 4 | Improbable por la fórmula (≈ 0.7 %); falta descontar la elección de cantidades | CONTRASTE |
| Coincidencias simples con leptones | Cualquier objetivo al azar las tiene | CONTRASTE sin valor |

## Estado

Resultados exactos en sus sectores; hipótesis físicas con falsador declarado. No se
deriva ninguna masa física ni se decide P frente a NP.
