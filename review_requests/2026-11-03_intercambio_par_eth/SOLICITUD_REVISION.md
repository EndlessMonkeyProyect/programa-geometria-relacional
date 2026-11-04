---
title: "Solicitud de revisión independiente"
subtitle: "Precedencia documental y correspondencias con las refutaciones de la ETH · Programa de Geometría Relacional"
author: "Le Matt Ansatz Di Ego"
date: "3 de noviembre de 2026"
lang: es
---

# Solicitud de revisión independiente

**Precedencia documental y correspondencias con las refutaciones de la ETH**

Le Matt Ansatz Di Ego · Programa de Geometría Relacional · 3 de noviembre de 2026

[English](REVIEW_REQUEST_EN.md)

---

## Resumen

Se pide revisar dos cuestiones separables: qué formulaciones del Programa de Geometría Relacional eran públicas y verificables antes del 16 de octubre de 2026, y si ciertas operaciones del programa coinciden con piezas de los dos algoritmos que refutan la Hipótesis del Tiempo Exponencial (ETH), el de OpenAI y el de Anthropic. El resultado principal es una coincidencia exacta y local, medida el 3 de noviembre: el intercambio de un par aparece como el mismo operador en las construcciones de ambos algoritmos. Además, sumas relacionadas de las mismas multiplicidades binomiales dan los rangos de la división de un bit de Anthropic y el número de filas de la construcción explícita de mediciones de OpenAI; las fórmulas se prueban en general, pero no se ha mostrado que influyan en ninguna de las dos cotas. No es una identidad entre los algoritmos.

No se reclama equivalencia algorítmica, influencia entre grupos ni anticipación de los algoritmos, y la validez de las dos refutaciones se toma como premisa externa. La cronología se apoya en metadatos de commit, que controla el autor, y falta confirmarla con sellos de tiempo independientes. Se presentan cinco hipótesis (H1 a H5) con criterios explícitos de refutación, para que quien revise pueda decidir dónde el marco explica y dónde solo interpreta.

## 1. Alcance y preguntas de revisión

**Prioridad de revisión · 4 de noviembre de 2026.** Se pide primero un dictamen humano sobre las proposiciones 1, 2, 4 y 5 y el corolario 3 de la nota de prueba: corrección y fidelidad a las fuentes. La segunda pregunta es bibliográfica: antecedentes de las fórmulas o de la comparación. Las respuestas se reúnen en el [hilo específico](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/4); la cronología documental es una consulta separada.

Cada pregunta dice qué evidencia la resolvería y en qué estado está hoy.

| # | Pregunta | Evidencia que la resuelve | Estado |
| --- | --- | --- | --- |
| Q1 | ¿Qué era público antes del 16 de octubre? | Eventos de subida, capturas, DOI o archivos con fecha independiente que contengan el material pertinente | Parcial: los metadatos de commit son consistentes, faltan sellos de tiempo independientes (sección 2) |
| Q2 | ¿Coinciden algebraicamente las operaciones? | Identidades en notación estándar y un verificador | Una coincidencia exacta y local entre los dos algoritmos (3.3); lo demás es clásico o analogía |
| Q3 | ¿El marco deriva el resultado sin postularlo? | Deducción explícita desde los principios del programa | Abierta (H3) |
| Q4 | ¿Hay dependencia histórica entre grupos? | Evidencia externa independiente | Fuera de alcance (H4) |
| Q5 | ¿Ya se señaló que los dos algoritmos comparten el intercambio de un par? | Literatura o discusión pública de los dos papers | Abierta (H2 y H5) |

**Terminología.** «OpenAI» y «Anthropic» designan a los laboratorios. El paper de Anthropic está firmado por Claude, su modelo, y así se cita en las referencias.

## 2. Cronología verificable

La solicitud cita commits fechados antes del 16 de octubre para la composición de interfaces (MF-60B a MF-62B), el núcleo del recierre MF-63B, MF-85 y la revisión v3; todavía falta evidencia independiente de cuándo esas versiones quedaron públicas. Los registros citados de los documentos de conteo, la nota de los octoniones y el piso N1 están fechados el 24 de octubre, antes de los anuncios pero después del día declarado del descubrimiento. Una fecha interna no acredita precedencia por sí sola. PGR es este repositorio, programa-geometria-relacional, y RGP es [Relational-Geometry-program](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program).

| Fecha interna (2026) | Documento | Registro citado | ¿Público antes del 16 oct? |
| --- | --- | --- | --- |
| 19 sep | Programa de Geometría Relacional 1.0 | RGP [`7a09d08`](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/commit/7a09d08), 19 sep | Sin verificar; solo fecha del commit |
| 29 sep | Edición conceptual 0.1.0: MF-60B a MF-62B; MF-62B anuncia que MF-63B tratará la compatibilidad | PGR [`fb27fbf`](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/commit/fb27fbf), 29 sep | Sin verificar; solo fecha del commit |
| 3 oct | MF-63B, recierre de compatibilidad | Núcleo en RGP [`c44cfb8`](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/commit/c44cfb8), 3 oct; completo en PGR `0fd5315`, 24 oct | Núcleo sin verificar; documento completo en el registro citado desde el 24 oct |
| 3 oct | Reddit: «P vs NP and Yang–Mills: Two Problems, One Structural Question» | Reddit, con su propia marca de tiempo | Falta verificar la fecha de la plataforma y archivar una captura |
| 5 oct | Ontología, novedad y comparadores locales | RGP [`c508eb2`](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/commit/c508eb2), 5 oct | Sin verificar; solo fecha del commit |
| 6–8 oct | MF-85, promoción de cierre a identidad colectiva | RGP [`6e36993`](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/commit/6e36993), 9 oct | Sin verificar; solo fecha del commit |
| 6–8 oct | MF-86, MF-96 y MF-106 | PGR `0fd5315`, 24 oct; MF-96 solo aparece citada el 9 oct | No |
| 9 oct | v3.0.0-review: cierre, resolución y composición; involución H = 2P − I y base de Walsh | RGP `6e36993`, 9 oct | Sin verificar; solo fecha del commit |
| 9 oct | Reddit: «We Are No Infinite Monkeys» (r/epistemology) | Reddit; fecha sin verificar; el corpus lo titula «Not» | Por verificar |
| 13 oct | Nota del 8: octoniones por duplicación de Cayley–Dickson | PGR [`0fd5315`](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/commit/0fd5315), 24 oct | No |
| 14 oct | N1: piso del motor de tablas y de la resolución | PGR `0fd5315`, 24 oct | No |
| 15 oct | E15, E16 y E22 | Ningún repositorio público | No, internos |
| 16 oct | CR-2 a CR-5: conteo por frontera, reflexión, herencia y costo | PGR `0fd5315`, 24 oct, dentro de Imagen Total 3.9 | No |
| 16 oct | Anthropic: su paper sitúa ese día el hallazgo del algoritmo central | Paper de Anthropic, §1 | — |
| 17 oct | Preprint de OpenAI, revisado el 25; no declara fecha de descubrimiento | openai/math | — |
| 18–24 oct | Laboratorios E-MIRROR v1 a v8, Imagen Total 3.9, CME-001 a CME-003 | PGR `0fd5315`, 24 oct | No |
| 26 oct | Fecha del paper de Anthropic; anuncio de ambos resultados | Repositorios de ambos laboratorios | — |
| 30 oct | Solicitud de revisión: el cubo de espejos y P frente a NP | PGR [`a1d3f16`](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/commit/a1d3f16), 30 oct | — |
| 3 nov | El cruce como reflejo central | PGR [`a630cff`](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/commit/a630cff); DOI 10.5281/zenodo.23932854 | — |

**Advertencia de método.** La fecha de un commit la escribe su autor y se puede reescribir. Los eventos de subida de GitHub tienen fecha del servidor cuando están disponibles, pero GitHub no ofrece una fecha permanente de subida para cada commit; su API pública de eventos conserva solo los recientes. Una versión visible hoy no prueba que sus archivos existieran en una versión anterior. Para alegar precedencia hacen falta eventos de subida o capturas archivadas con fecha independiente que incluyan los commits y el contenido exacto, y copias fechadas independientemente de las dos publicaciones de Reddit. [Retención de eventos en GitHub](https://docs.github.com/en/rest/activity/events) · [Visitas de origen en Software Heritage](https://docs.softwareheritage.org/devel/swh-web/uri-scheme-browse-snapshot.html)

## 3. Correspondencias matemáticas

Hay una coincidencia exacta y local entre los dos algoritmos; las del programa con ellos son matemática clásica bien ubicada o analogías. Cada una lleva su tipo: (A) identidad algebraica, exacta y verificable; (B) analogía estructural, misma forma con otro espacio o función; (C) lectura interpretativa, no falsable por sí sola.

### 3.1 Composición de interfaces — tipo A, clásica

Para dos regiones $F_A(X,S)$ y $F_B(S,Y)$ con frontera común $S$ e interiores disjuntos:

$$K_{AB}(S)=\exists X\,F_A(X,S)\wedge\exists Y\,F_B(S,Y)=\exists X,Y\,[F_A\wedge F_B]$$

Es la eliminación de variables de Davis y Putnam (1960) y de Dechter (1999): una contracción de factores en el semianillo booleano. El criterio $B_A \cap B_B \neq \emptyset$ es público en MF-61B (29 sep) y el núcleo del recierre, en MF-63B (3 oct).

### 3.2 Conteo por frontera — tipo A, clásica

Con $Q_H(b)$, el número de extensiones interiores compatibles con la frontera $b$, se cumple $N(H_1 \wedge H_2) = \sum_b Q_1(b)\,Q_2(b)$: una contracción en el semianillo de conteo. El paso de ℕ a 𝔹 conserva la estructura; el de ℤ a 𝔹 no, porque 1 + (−1) = 0, así que una suma con cancelaciones no admite después el recierre booleano. En el piloto de 21 soluciones, con frontera {x₂, x₃}, N₁ = [2, 1, 2, 2] y N₂ = [4, 3, 2, 3] dan 21. Es público desde el 24 de octubre (CR-2).

### 3.3 El intercambio de un par en los dos algoritmos — tipo A, coincidencia local medida el 3 de noviembre

Sea $S$ el intercambio en $\mathbb{R}^r \otimes \mathbb{R}^r$ y $P_-$ su proyector antisimétrico, de modo que $S = I - 2P_-$.

- **Anthropic.** El cruce [x=v][y=u] es $S$. El Lema 2 lo descompone con la identidad de los ocho cuadrados (ρ = 11/12). El Apéndice H registra la versión de un bit, y el paper declara que ninguna prueba lo usa:

$$[x=v][y=u]=[x=u][y=v]-[x\neq y]\,(-1)^{x}\,[u\neq v]\,(-1)^{u}$$

- **OpenAI.** Πₛ intercambia el par $s$ (§2.7, paso 2). Con $W_0$, que cuenta los factores antisimétricos, se tiene:

$$V_0=\prod_{s=1}^{Q}\Pi_s,\qquad W_0=\sum_{s=1}^{Q}P_-^{(s)},\qquad V_0=(-1)^{W_0},\qquad M_0=V_0\,f(W_0)$$

Aquí $f$ interpola $(-1)^j$ en una ventana. Este paso está dentro de la prueba (§4.2).

- **Coincidencia.** Con r = 2, Πₛ es el cruce de un bit entrada por entrada. Las mismas multiplicidades binomiales entran además en dos conteos distintos:

$$\operatorname{rank}_{\text{filas}}(A_i)=\sum_{j\ge t-i}\binom{t}{j}3^{\,t-j},\qquad c=\sum_{j\notin I}\binom{Q}{j}\left(\tfrac{r(r-1)}{2}\right)^{j}\left(\tfrac{r(r+1)}{2}\right)^{Q-j}$$

A la izquierda hay una cola superior que da los rangos por filas de las piezas de un bit. A la derecha está el complemento de la ventana de interpolación de OpenAI, que puede incluir una cola inferior y otra superior; $c$ cuenta las filas de la matriz explícita de mediciones construida en el preprint, no un mínimo demostrado. Con t = 4, i = 2, r = 2, Q = 4 e I = {0, 1}, ambos conteos valen 67. [`verificar_pieza_compartida.py`](verificar_pieza_compartida.py) comprueba este caso pequeño. Es una comparación entre los dos papers externos hecha por el programa, no un antecedente. La [nota de prueba](NOTA_PRUEBA_3_3.md) demuestra las fórmulas para todo t y Q en sus respectivos contextos; el valor 67 solo las ilustra y, por sí solo, no es evidencia de un mecanismo común.

### 3.4 Reflexiones del programa frente al intercambio — tipo B

La reflexión binaria del programa, ρᵢ(x) = x ⊕ eᵢ, no es el mismo operador que el intercambio. Voltear un bit actúa como X sobre una coordenada; en dos bits su traza es 0 y la del intercambio es 2, y sus proyectores antisimétricos tienen rango 2 y 1. Ningún isomorfismo lleva uno al otro.

Lo que sí corresponde son las reflexiones del cubo de espejos que intercambian dos coordenadas, por los planos xᵢ = xⱼ. Pertenecen al grupo de simetrías del tetraedro, S₄, y sobre los vértices del cubo son exactamente el intercambio de dos bits. El programa trata ese grupo en los documentos del cubo de espejos publicados el 24 de octubre (O21), pero no se encontró que identifique esas reflexiones con el intercambio de dos bits. Es una analogía de tipo B: el mismo operador cumple otra función, simetría del tetraedro en lugar de rebaja de costo. La involución H = 2P − I del 9 de octubre es una reflexión distinta, a través del vector uniforme.

### 3.5 Mediciones del paquete del 3 de noviembre — tipo A, teoremas clásicos

- **Dos cortes.** S = I − 2P₋ rebaja el cruce a log₂ 12 ≈ 3,585 bits por bloque (ρ ≈ 0,896); la división por signo nunca baja de ese valor.
- **Tetraedro.** Los cuatro cruces ocupan la clase par {000, 011, 101, 110} del cubo de correlaciones; cada uno es la reflexión central de un estado de Bell.
- **Duplicación.** Cayley–Dickson da R + C = 2·cruce en 2, 4 y 8; con la cuenta del Lema 2 solo el 8 gana (11 de 12 bits), y eso exige perder la asociatividad.

Son teoremas clásicos dichos en el lenguaje del programa; cinco verificadores los reproducen ([entrega del 3 de noviembre](../../2026-11-03_cruce_reflejo_central/LEER_PRIMERO.md)), y los valores están en sus archivos `referencia_resultados/*.json`.

## 4. Hipótesis y criterios de refutación

Cada hipótesis dice qué la probaría, qué la refutaría y dónde está hoy. H1 y H2 están cerca de confirmarse, pero como matemática conocida; H3 es la que decidiría si el marco explica.

| Hipótesis | Prueba esperada | Refutación | Estado |
| --- | --- | --- | --- |
| **H1, contracción.** El recierre y el conteo del programa son contracciones de factores, en los semianillos booleano y de conteo | Identidad explícita en notación estándar (3.1 y 3.2) | Una operación de cierre del programa que no sea contracción, o que solo lo sea reescribiendo definiciones (tipo C) | Identidades dadas; clásico, sin novedad |
| **H2, operador.** El intercambio de un par es el mismo operador local en los dos algoritmos y en las reflexiones de transposición del cubo del programa, con un papel distinto en cada uno | Igualdad entrada por entrada y comparación de su función en cada construcción | Una entrada distinta, o un operador del programa que no sea transposición, como ρᵢ(x) = x ⊕ eᵢ (3.4) | Igualdad verificada (3.3); la función difiere en cada caso (3.4) |
| **H3, capacidad explicativa.** El marco deriva una cota o un exponente ρ sin postularlo, por ejemplo ρ < 11/12 o 1/√2 | Derivación paso a paso desde los principios del programa | Que la cota o la duplicación entren como condición adicional | Abierta; hoy no hay derivación |
| **H4, dependencia histórica.** Hubo dependencia entre grupos | Evidencia externa independiente | — | Fuera de alcance |
| **H5, conteos binomiales relacionados.** Las sumas relacionadas de multiplicidades de factores antisimétricos que cuentan los rangos de un bit y las filas de medición elegidas por OpenAI tienen consecuencias para alguna de las dos cotas | Las fórmulas, ya probadas en la [nota de prueba](NOTA_PRUEBA_3_3.md), más un argumento de que esa relación entra en una de las cotas | Que los pesos compartidos surjan solo de usar la misma involución, sin efecto en las cotas | Fórmulas probadas para todo t y Q en sus respectivos contextos; su papel en las cotas, abierto |

## 5. Matemática conocida frente a posible aporte

Casi todo lo matemático es conocido. Lo que puede ser aporte es la medición y la observación sobre los dos papers, y eso es lo que se pide juzgar.

| Elemento | Estatus |
| --- | --- |
| Contracción de factores y suma de productos sobre la frontera | Matemática conocida |
| Proyector antisimétrico de una involución, S = I − 2P₋ | Matemática conocida |
| Duplicación por reflexión (Cayley–Dickson) e identidad de los ocho cuadrados (Hurwitz) | Conocida; el programa la toma como postulado |
| El intercambio de un par como pieza común de los dos algoritmos | Observación sobre dos papers externos; por evaluar si ya se señaló (Q5) |
| Conteos binomiales relacionados para los rangos de un bit y las filas de medición elegidas por OpenAI | Probados en la nota de prueba; su relevancia, por evaluar (H5) |
| Fórmulas explícitas de rango para t finito en la división de un bit | Se derivan aquí de los espacios propios de dimensiones uno y tres ya descritos en el Apéndice H de Anthropic; falta evaluar cualquier novedad |
| Arquitectura referencia → cierre → interfaz → recierre | Reorganización conceptual; novedad por evaluar |
| Metodología de intuición y lenguaje asistida por IA | Epistemológica, no matemática |
| Derivación de cotas de complejidad desde el marco | Abierta (H3) |

## 6. Material reproducible y estado de formalización

Todo lo marcado como medido se regenera con verificadores en Python; son comprobaciones numéricas, no pruebas formales, y nada está formalizado en Lean ni en Coq.

| Tipo | Qué incluye | Estado |
| --- | --- | --- |
| Verificadores computacionales | Los cinco del paquete del 3 de noviembre y `verificar_pieza_compartida.py` (sección 3.3) | Corridos el 3 nov: coinciden con la referencia en unos 37 s (Python 3.13.18, numpy 2.5.3). DeepSeek repitió los cinco en Windows. La salida de `verificar_pieza_compartida.py` y su entorno están en `salida_verificador_2026-11-03.txt` |
| Pruebas en prosa | Proposiciones 1 a 3 y corolario 4 del paper del 3 de noviembre; identidades de 3.1 y 3.2; [nota de prueba](NOTA_PRUEBA_3_3.md) de 3.3 | DeepSeek re-derivó las del paper; es revisión de IA, no humana. La nota de 3.3 no tiene revisión externa |
| Formalización en Lean o Coq | — | Ninguna en los tres repositorios del programa |

**Repetir las mediciones.**

```bash
git clone https://github.com/EndlessMonkeyProyect/programa-geometria-relacional
cd programa-geometria-relacional
git checkout --detach 46e47274e9e573b9c91da1516d067c4f49c289f9
cd 2026-11-03_cruce_reflejo_central
python3 -m pip install -r requirements.txt   # numpy>=1.24
bash reproducir_todo.sh            # regenera y compara todos los resultados
cd ../review_requests/2026-11-03_intercambio_par_eth
python3 verificar_pieza_compartida.py   # sección 3.3, menos de un segundo
```

El commit fijado corresponde a la etiqueta `2026-11-03-pair-swap-review`; evita depender de futuros cambios de `main`. El bloque completo requiere Bash y el comando `python3` en `PATH`, porque `reproducir_todo.sh` lo invoca internamente. En Windows puede usarse Git Bash con ese comando configurado. Para ejecutar solo el verificador de la sección 3.3 con PowerShell, véase [LEER_PRIMERO](LEER_PRIMERO.md). Las dependencias conservan el rango declarado; no se afirma un entorno congelado. Fuentes contrastadas: OpenAI, commit `42907c9e999cc00d6abe7a50bfc1023250edd1b9`, y Anthropic, commit `16a5ce41304fcdaea4e0be7c132e1c361dc26da5`.

**Enlaces.**

- Núcleo matemático: [Relational-Geometry-program](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program)
- Modelo ontológico: [relational-geometry-Model](https://github.com/EndlessMonkeyProyect/relational-geometry-Model)
- Paquete del 3 de noviembre: [carpeta](../../2026-11-03_cruce_reflejo_central/LEER_PRIMERO.md), [versión 2026-11-03](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/releases/tag/2026-11-03), [DOI 10.5281/zenodo.23932854](https://doi.org/10.5281/zenodo.23932854)
- Revisión de DeepSeek: [review_requests/2026-11-03_cruce_reflejo_central](../2026-11-03_cruce_reflejo_central/LEER_PRIMERO.md)

## 7. Conclusión

Los metadatos de commit son consistentes con que la composición de interfaces, el núcleo del recierre, MF-85 y la revisión v3 fueran públicos antes del 16 de octubre, pero no lo acreditan. Siguen faltando sellos de tiempo independientes del contenido pertinente. Además se identifica, medida después, una coincidencia exacta y local entre los dos algoritmos: el intercambio de un par. Sumas relacionadas de sus multiplicidades binomiales cuentan los rangos de la división de un bit y las filas de la matriz explícita de mediciones de OpenAI.

No acredita que el programa descubriera los algoritmos, que hubiera influencia entre grupos ni que las correspondencias impliquen el mismo mecanismo. La distancia entre correspondencia y equivalencia es, precisamente, el objeto de esta revisión. Se invita a señalar correspondencias, contradicciones o formulaciones más precisas, sobre todo en H2, H3 y H5, como [issues en este repositorio](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/4).

## Anexo — Motivación del programa

El programa nació de una convicción personal: que detrás de la multiplicidad de lo que habitamos hay un orden reconocible por sus relaciones. Esa convicción no se presenta como teorema ni como resultado matemático; se declara aquí como motivación, separada de las hipótesis evaluables de las secciones 3 y 4. El recorrido se desarrolló en diálogo entre la intuición humana y sistemas de IA, y eso se documenta como método, no como validación.

**Uso de IA.** Este documento se preparó con asistencia de Claude (Anthropic) y de DeepSeek. Uno de los asistentes viene de la misma empresa que uno de los algoritmos analizados. Las preguntas, el marco y las decisiones de alcance son del autor.

## Referencias

- Claude (Anthropic). [A 2^o(n) Time Algorithm for 3-SAT](https://github.com/anthropics/formal-math/blob/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/eth/paper.pdf). 26 de octubre de 2026, commit `16a5ce4`.
- OpenAI. [The Exponential Time Hypothesis is False](https://github.com/openai/math/blob/42907c9e999cc00d6abe7a50bfc1023250edd1b9/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf). 17 de octubre de 2026, revisado el 25.
- Programa de Geometría Relacional. MF-61B y MF-62B, 29 de septiembre de 2026 (`fb27fbf`); MF-63B, recierre acreditado de compatibilidad, 3 de octubre de 2026 (`c44cfb8`; completo en `0fd5315`); v3.0.0-review, 9 de octubre de 2026 (`6e36993`).
- Le Matt Ansatz Di Ego. El cruce como reflejo central. 3 de noviembre de 2026. [DOI 10.5281/zenodo.23932854](https://doi.org/10.5281/zenodo.23932854).
- Endless-monkey. [P vs NP and Yang–Mills: Two Problems, One Structural Question](https://www.reddit.com/user/Endless-monkey/comments/1wwk0xh/p_vs_np_and_yangmills_two_problems_one_structural/). Reddit, 3 de octubre de 2026.
- Endless-monkey. [We Are No Infinite Monkeys](https://www.reddit.com/r/epistemology/comments/1x1fls2/we_are_no_infinite_monkeys/). Reddit, r/epistemology; fecha por verificar.
- Davis y Putnam. A computing procedure for quantification theory. *Journal of the ACM* 7 (1960).
- Dechter. Bucket elimination: a unifying framework for reasoning. *Artificial Intelligence* 113 (1999).
- Hurwitz (1898): sumas de cuadrados con composición bilineal, solo en dimensiones 1, 2, 4 y 8.
