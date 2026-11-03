---
title: "La caja de espejos"
subtitle: "Antecedentes públicos, cierre relacional y convergencia matemática con los resultados de OpenAI y Claude sobre la Hipótesis del Tiempo Exponencial"
author: "Le Matt Ansatz Di Ego · Programa de Geometría Relacional · Endless Monkey"
date: "3 de noviembre de 2026"
lang: es
keywords:
  - Hipótesis del Tiempo Exponencial
  - cierre relacional
  - octoniones
  - particiones
  - convergencia de descubrimientos
abstract: |
  En octubre de 2026, OpenAI y Anthropic publicaron algoritmos deterministas que cuentan
  las soluciones de fórmulas k-CNF en tiempo subexponencial; si sus demostraciones resisten la revisión, refutan la Hipótesis del Tiempo Exponencial (ETH). Esta nota reconstruye, con commits verificables, qué había
  publicado antes el Programa de Geometría Relacional y qué correspondencias matemáticas con
  esos algoritmos son exactas. Tres correspondencias están establecidas: el recierre es la
  contracción por suma de productos (el modelo del que los algoritmos salen); la duplicación
  por reflexión del programa produce, en el nivel 8 (octoniones), la identidad del Lema 2 del
  algoritmo de Claude; y los cruces que ese algoritmo descompone ocupan el tetraedro del
  programa. Ninguna de ellas reconstruye los algoritmos ni sus cotas: son teoremas clásicos en
  el lenguaje del programa, y la equivalencia algorítmica (nivel IV) permanece abierta.
---

# La caja de espejos

**Antecedentes públicos, cierre relacional y convergencia matemática con los resultados de OpenAI y Claude sobre la Hipótesis del Tiempo Exponencial**

Le Matt Ansatz Di Ego · Programa de Geometría Relacional · Endless Monkey · 3 de noviembre de 2026

*Versión 0.3 — documento para revisión independiente*

**Clasificación MSC 2020 (sugerida).** 68Q25, 68R07, 68Q17, 17A75, 11P82, 15A69.

**Declaración de contribución.** Esta nota no atribuye influencia entre investigaciones ni reclama las técnicas de otros grupos. Su aporte es la reconstrucción cronológica documentada y la separación explícita, por niveles, entre lo que está demostrado y lo que permanece abierto.

**Premisa externa no verificada aquí.** Los resultados de OpenAI y Anthropic se toman como *premisa externa citada*; esta nota no los demuestra ni los audita.

## Resumen

En octubre de 2026, OpenAI y Anthropic anunciaron, de manera independiente, algoritmos deterministas que cuentan las soluciones de fórmulas k-CNF en tiempo subexponencial. Si sus demostraciones resisten la revisión, refutan la Hipótesis del Tiempo Exponencial (ETH). Ambos laboratorios sitúan su descubrimiento el 16 de octubre y publicaron el 26.

Esta nota reconstruye, con commits verificables, qué había publicado antes el Programa de Geometría Relacional y qué correspondencias matemáticas con esos algoritmos son exactas.

- **Antecedencia pública.** Antes del 16 de octubre hay commits públicos con el recierre de compatibilidad (3 de octubre) y la revisión v3 (9 de octubre). Los documentos de conteo y la nota de los octoniones se hicieron públicos el 24 de octubre: antes de los anuncios, después del día del descubrimiento.
- **Tres correspondencias exactas.** El recierre es la contracción por suma de productos, el modelo del que los algoritmos tienen que salir para ganar. La duplicación por reflexión del programa produce, en el nivel 8, exactamente la identidad que usa el Lema 2 de Claude. Y en el cubo de correlaciones, los cruces que el algoritmo descompone ocupan el tetraedro del programa.
- **Lo que no se afirma.** Ninguna de esas correspondencias reconstruye los algoritmos ni sus cotas. Son teoremas clásicos dichos en el lenguaje del programa, y el programa usó esos objetos para otras preguntas.

**Pregunta central:** ¿en qué condiciones una estructura cerrada puede convertirse en nueva referencia y conservar la información necesaria para las relaciones posteriores, con un costo computacional reducido?

## 1. Cronología con evidencia pública

Antes del 16 de octubre es pública la arquitectura de recierre e interfaces, no el conteo. La tabla separa la fecha que declara cada documento de su primera aparición en un repositorio público (RGP = `relational-geometry-program`; PGR = `programa-geometria-relacional`).

| Fecha declarada (2026) | Desarrollo | Primera aparición pública | Estado |
| --- | --- | --- | --- |
| 19 sep | Programa de Geometría Relacional 1.0 | RGP `7a09d08`, 19 sep | Público |
| 29 sep | Edición conceptual 0.1.0; MF-62B anuncia que MF-63B tratará la compatibilidad como objeto de primer nivel | PGR `fb27fbf`, 29 sep | Público |
| 3 oct | MF-63B, recierre: K\_AB(S) = ∃X,Y \[F\_A ∧ F\_B\] | RGP `c44cfb8`, 3 oct; documento completo en PGR `0fd5315`, 24 oct | Público |
| 3 oct | Reddit: P frente a NP y Yang–Mills, una pregunta estructural | Reddit | Por verificar con captura archivada |
| 5 oct | Ontología, novedad y comparadores locales | RGP `c508eb2`, 5 oct | Público |
| 6–8 oct | MF-85, promoción de cierre a identidad colectiva | RGP `6e36993`, 9 oct | Público |
| 6–8 oct | MF-86, MF-96 y MF-106 | PGR `0fd5315`, 24 oct | Público desde el 24 |
| 9 oct | v3.0.0-review: cierre, resolución y composición | RGP `6e36993`, 9 oct | Público |
| 9 oct | Reddit: «We Are No Infinite Monkeys» | Reddit; el corpus lo titula «We Are Not Infinite Monkeys» | Por verificar; unificar el título |
| 13 oct | Nota del 8: octoniones por duplicación de Cayley–Dickson | PGR `0fd5315`, 24 oct | Público desde el 24 |
| 14 oct | N1: piso del motor de tablas y de la resolución | PGR `0fd5315`, 24 oct | Público desde el 24 |
| 15 oct | E15, E16 y E22 | Ningún repositorio público | Interno |
| 16 oct | CR-2 a CR-5: conteo por frontera, reflexión, herencia y costo | PGR `0fd5315`, 24 oct, dentro del corpus de Imagen Total 3.9 | Público desde el 24 |
| 16 oct | OpenAI y Anthropic sitúan su descubrimiento | Declarado por ambos | — |
| 17 y 25 oct | Preprint de OpenAI, fechado el 17 y revisado el 25 | — | — |
| 18–24 oct | Laboratorios de espejos E-MIRROR v1–v8, Imagen Total 3.9 y CME-001 a CME-003 | PGR `0fd5315`, 24 oct | Público |
| 26 oct | Publicación de los trabajos de OpenAI y Anthropic | Repositorios de ambos laboratorios | — |
| 30 oct | Solicitud de revisión: el cubo de espejos y P frente a NP | PGR `a1d3f16`, 30 oct | Público |

**Cómo leerla.** Antes del 16 de octubre son públicos el recierre, la composición de interfaces y la revisión v3. Los documentos de conteo y la nota de los octoniones tienen fechas internas del 13 al 16 de octubre y se publicaron el 24: antes de los anuncios, pero después del día del descubrimiento. Un revisor lo va a notar; esta nota lo dice primero.

**Qué acredita cada evidencia.** La fecha de un commit la escribe su autor; la hora de subida la registra GitHub por separado. Una fecha dentro de un documento acredita cuándo se formuló, no cuándo se publicó. Para una declaración definitiva de precedencia hacen falta la hora de subida de cada commit según GitHub, una copia en Software Heritage o un depósito en Zenodo con DOI, y capturas archivadas de las dos publicaciones de Reddit.

## 2. El problema que ya estaba planteado

La publicación del 3 de octubre planteaba una pregunta común a dos ramas matemáticamente distintas: **¿cuándo una cantidad suficiente de cierres locales permite controlar un sistema global?** [O]

Una estructura puede contener mucha información interna y necesitar conservar solo algunas relaciones para participar en una composición posterior. Cuando queda cerrada respecto de una pregunta, su resultado puede convertirse en nueva referencia:

**Diferencia → relación → cierre → interfaz → nueva relación → nuevo cierre.**

MF-63B formuló la compatibilidad entre dos regiones cerradas mediante relaciones de frontera, y demostró que esa compatibilidad puede proyectarse otra vez como nueva interfaz [T]. También separó dos propiedades que no deben confundirse: la exactitud semántica del recierre y la eficiencia de su implementación.

Dos precisiones que un revisor necesita [T]:

- MF-63B probó además un límite: un DAG compacto de referencias no decide la vaciedad, porque una 3-CNF ya es una descripción compacta. Nombrar relaciones de forma recursiva no basta.
- Su objetivo era un descenso polinómico, el «Lema de Descenso Acreditado», que equivale a P = NP. Los algoritmos de octubre van en otra dirección: no buscan tiempo polinómico, sino conteo subexponencial.

## 3. Primera correspondencia: composición, conteo y el modelo que los algoritmos dejan

El recierre del programa es exactamente la contracción por suma de productos. Ese modelo tiene una cota inferior conocida, y los algoritmos de octubre ganan precisamente porque salen de él.

**Composición de interfaces [T][C].** Para dos regiones F\_A(X,S) y F\_B(S,Y) con interiores independientes, las relaciones exteriores son B\_A(S) = ∃X F\_A(X,S) y B\_B(S) = ∃Y F\_B(S,Y), y la compatibilidad conjunta coincide con la proyección del sistema combinado:

$$K_{AB}(S) = B_A(S) \wedge B_B(S) = \exists X,Y\, [F_A(X,S) \wedge F_B(S,Y)]$$

El resultado se puede proyectar otra vez sobre una frontera más pequeña, y el orden de cálculo no cambia la respuesta, aunque sí el costo intermedio.

**Conteo [T][C].** CR-2 a CR-5 extendieron el análisis al conteo. Si Q\_H(b) es el número de extensiones interiores compatibles con la frontera b, dos regiones con interiores independientes cumplen:

$$N(H_1 \wedge H_2) = \sum_b Q_1(b)\, Q_2(b)$$

Es la contracción tensorial de conteo. Sobre los números naturales, su soporte reproduce el recierre booleano; sobre los enteros con signo ya no, porque 1 + (−1) = 0. Es matemática conocida (Davis y Putnam, 1960; Dechter, 1999), y su presencia en el programa no anticipa las técnicas de reducción de octubre.

**El diagnóstico que esta correspondencia permite [C].** Contraer una sola red siguiendo un solo árbol tiene una cota inferior incondicional (Austrin, Kaski y Kubjas, 2022). Según el cálculo del paper de Claude, ningún algoritmo de ese modelo baja de cerca del 49 % del exponente de fuerza bruta. El algoritmo de Claude sale del modelo: expande la suma en una suma con signos de redes y contrae cada término en un orden distinto. El recierre del programa es, en esencia, ese modelo de un solo árbol, así que **el antecedente termina donde empieza la ganancia**.

## 4. Segunda correspondencia: la cadena de duplicación y el Lema 2

La regla de duplicación por reflexión del programa produce, en el nivel 8, exactamente la identidad que el algoritmo de Claude usa en su Lema 2. Es la correspondencia operatorial más fuerte que el programa puede mostrar, porque toca una pieza que el algoritmo sí usa en sus pruebas.

**La regla [C].** La nota del 13 de octubre (pública desde el 24) formaliza la duplicación de Cayley–Dickson, en la que el conjugado hace de espejo: (a, b)(c, d) = (ac − d̄b, da + bc̄). Desde los reales da los niveles 1, 2, 4, 8 y 16, con e\_p·e\_q = σ(p,q)·e\_(p⊕q).

**Lo que se demuestra** (pruebas completas en el paper *El cruce como reflejo central*, §7; verificadas con enteros exactos):

1. **Identidad del cruce [T].** En los niveles 2, 4 y 8, los signos σ de la duplicación dan R + C = 2·[x=v][y=u], con R barata en un corte y C en el otro. Es la identidad (31) del Lema 2.
2. **Las direcciones son órdenes [T].** R y C son los dos órdenes de componer dos referencias, LᵥᵀLₓ y LₓᵀLᵥ, y su suma es 2[x=v]·Id: las relaciones de Hurwitz–Radon.
3. **Solo el 8 abarata [T][E].** Con el conteo del Lema 2, un bloque cuesta 4 de 4 bits en el nivel 2, 8 de 8 en el nivel 4 y 11 de 12 en el nivel 8. En el 16 la identidad falla en 672 casos.
4. **Dentro de la cadena, abaratar exige el nodo abierto [T].** El único nivel que gana es el 8, y el 8 no es asociativo (Frobenius, 1878).

**Alcance [I].** Los objetos son clásicos: los octoniones de Graves (1843) y el teorema de Hurwitz (1898). El programa los usó para la no asociatividad, «el nodo abierto del 8», no para medir el costo de un cruce. La correspondencia muestra que el lenguaje del programa tenía la pieza; no que la hubiera usado como la usa el algoritmo.

**Corrección respecto de la v0.1.** La v0.1 proponía como puente la identidad SWAP = I − 2P\_singlete. Esa identidad aparece solo en el Apéndice H del paper de Claude, que el propio paper declara fuera de toda prueba, y la forma «involución = I − 2·proyector» vale para cualquier involución, así que no distingue nada. Se reemplaza por la cadena de duplicación.

## 5. Tercera correspondencia: el cruce, sus dos cortes y el tetraedro

La pieza que el algoritmo de Claude descompone, el cruce [x=v][y=u], tiene un lugar exacto en el cubo de espejos: los cuatro cruces posibles ocupan el tetraedro del programa. La ganancia viene de repartir el cruce entre dos cortes, no del signo.

**Dos cortes [T][E].** El cruce de un bit es el SWAP de dos bits, y cuesta 4 bits por bloque, porque tiene rango completo tanto en el corte (x,y)|(u,v) como en el (x,u)|(y,v). Escrito como SWAP = I − 2P₋, la identidad es barata en un corte y el singlete en el otro, y la pieza más cara tiende a log₂12 ≈ 3.585 bits por bloque. Escrito por signo, SWAP = P₊ − P₋, nunca baja de 3.585 bits y sube con el tamaño: 3.73 con cinco bloques.

**El tetraedro [C][E].** En el cubo de correlaciones (⟨XX⟩, ⟨YY⟩, ⟨ZZ⟩) de dos bits:

- los cuatro estados de Bell ocupan el tetraedro impar (Horodecki y Horodecki, 1996) y son baratos por filas;
- la identidad, suma de los cuatro, ocupa el centro y es barata por columnas;
- los cuatro cruces I − 2Πᵥ ocupan el tetraedro par, {000, 011, 101, 110}: el tetraedro del programa. Cada uno es el reflejo central de un estado.

**Tres y uno [I].** Los cuatro cruces son el mismo SWAP corregido por un Pauli local y cuestan lo mismo. Elegir cuál es «el cruce» es elegir el marco: una realización exacta de «tres y uno sin distinguir cuál».

**Alcance.** Medimos el costo por rangos, que es lo mejor que podría dar una descomposición, no un algoritmo. Con el conteo que el paper sabe implementar, el bit suelto no gana; por eso el paper usa ocho cuadrados (§4) y después los operadores de Heisenberg (§7).

## 6. El costo ya estaba identificado

Que una referencia compacta no garantiza respuestas baratas está en el programa desde MF-63B. N1 lo convirtió en un límite demostrado sobre su propio motor, y concluyó que había que salir de la resolución. Ese diagnóstico era correcto, aunque el programa no encontró la salida.

- **MF-46.** Rango de las relaciones afines acreditadas, exposición de fronteras y selección de las operaciones útiles para el siguiente cierre.
- **MF-96** (público desde el 24 de octubre). Una misma familia de restricciones puede ser costosa en un lenguaje y económica en otro: la paridad escrita como ecuaciones lineales se resuelve por eliminación gaussiana sin cargar todas las cláusulas.
- **E22** (interno). Un selector que reconoce rutas de resolución y separa el costo de encontrar una organización del costo de ejecutarla.
- **N1 [T][C]** (14 de octubre, público desde el 24). Ningún orden baja el motor de tablas de 3^(tw+1). Con poda, toda corrida que concluye «no hay coloración» es una refutación por resolución; por Beame, Culberson, Mitchell y Moore (2005), cuesta 2^Ω(n) en grafos aleatorios con cualquier selector.

**Consecuencia [T].** Una 3-coloración de n vértices se escribe como 3-CNF con 3n variables. Un algoritmo de tiempo 2^o(n) no puede tener corridas convertibles en refutaciones por resolución de tamaño comparable, porque contradiría esa cota. Los algoritmos de octubre están, necesariamente, fuera del tipo de motor que N1 acota.

La economía computacional depende de la estructura de operaciones disponible, no solo de la cantidad de información. Es la lección que comparten el programa y los algoritmos de octubre; la diferencia es que estos encontraron las operaciones.

## 7. Los resultados de OpenAI y Claude

Ambos trabajos cuentan exactamente las soluciones de fórmulas k-CNF, para anchura k fija, con un algoritmo determinista en tiempo 2^O(n log log n / √log n) y espacio polinómico. Los dos traen formalización en Lean y están en revisión externa.

**Claude [C]** (leído completo). Expande un múltiplo del cruce en una suma con signos de piezas, cada una barata en un corte, y contrae cada término en su propio orden. Con la identidad de ocho cuadrados obtiene ρ = 11/12 (Lema 2). Con operadores sobre un espacio graduado de polinomios, el álgebra de Heisenberg sobre las particiones de un entero, obtiene ρ = 1/√2 (Apéndice B). La ganancia final depende de que el logaritmo del número de particiones crezca de forma cóncava.

**OpenAI** (no leído directamente). Según fuentes secundarias, combina resúmenes lineales, esparsificación, reemplazo espectral e interpolación racional, con contracción tensorial para la cota más fina. Esta nota no afirma nada sobre su mecanismo más allá de eso.

Hay que distinguir tres afirmaciones:

- **Coincidencia de conclusión.** Ambos afirman refutar la ETH, y con ella la SETH. Aun si sus demostraciones resisten la revisión, no implican P = NP.
- **Diferencia de construcción.** No son el mismo algoritmo, aunque usan recursos algebraicos relacionados.
- **Posible mecanismo común [A].** Si ambas construcciones reorganizan la información mediante cierres, referencias e interfaces cuya composición conserva el resultado. Es una hipótesis de correspondencia, no una equivalencia establecida.

Que ambos laboratorios fechen su descubrimiento el mismo día es un dato interesante para estudiar el descubrimiento asistido por inteligencia artificial. Esta nota no lo interpreta.

## 8. Qué está demostrado y qué permanece abierto

Los tres primeros niveles están establecidos; el cuarto, el único que permitiría llamar a esos algoritmos realizaciones del mecanismo del programa, sigue abierto.

| Nivel | Qué se afirma | Evidencia | Estado |
| --- | --- | --- | --- |
| I. Antecedencia documental | Recierre e interfaces públicos antes del 16 de octubre; conteo y octoniones públicos el 24 | RGP `c44cfb8` y `6e36993`; PGR `0fd5315` (§1) | Establecido, con la cautela de las fechas de autor |
| II. Correspondencia semántica | El recierre es la contracción por suma de productos, el modelo del que los algoritmos salen | §3 | Establecido [C] |
| III. Correspondencia operatorial | La duplicación del programa da la identidad del Lema 2; el 8 es el único nivel que abarata; los cruces ocupan el tetraedro del programa | §4, §5 y verificadores | Establecido [T][E], con objetos clásicos |
| IV. Equivalencia algorítmica | Reconstruir los algoritmos y sus cotas desde los operadores del programa | — | Abierto |

**Dos blancos concretos para el nivel IV [A].**

- **La concavidad.** En la conversación del 3 de noviembre, llenar la totalidad con partes resultó ser el objeto del Apéndice B: las particiones. Falta el mapa que lleve la regla de la pared a los operadores que agregan y quitan partes.
- **Un ρ menor que 1/√2.** Una familia de partes más rala, como los cuadrados, daría ρ ≈ 0.63, pero solo si existieran operadores con las propiedades de los Lemas 9 y 10 del paper. Con las reglas que el programa ya enuncia, o se reproduce 1/√2 o no se cumple la condición de crecimiento.

La anterioridad de los niveles I a III no prueba el IV. Tampoco permite inferir que un laboratorio haya usado materiales del otro o del programa: esa es una cuestión histórica distinta, que requeriría evidencia propia.

## 9. La caja de espejos como culminación del recorrido

En la caja de espejos una imagen se refleja y vuelve a reflejarse, y una multiplicidad ilimitada de manifestaciones se reconoce mediante pocas relaciones. La pregunta no es cuántas imágenes aparecen, sino qué relación las hace reconocibles como partes de un mismo sistema.

**La pared que se corre [T].** Con espejos en 0 y L, una sola cifra, la distancia al múltiplo de 2L más cercano, reconoce todas las imágenes de una marca. Si la pared pasa de L = 1 a L = 2, los puntos 1/4 y 9/4, que compartían cifra, dejan de compartirla. Lo que se perdió no es el signo, sino cuántas veces se usó el espejo que se movió. Es el problema central del programa en forma geométrica: conservar una referencia sin perder lo que puede hacer falta cuando cambian las condiciones de comparación.

**Lo que decide si el recinto cierra [T].** Con tres espejos decide cómo suman las fracciones frente a la totalidad: si sobran, el recinto cierra; si la llenan justo, se repite; si no alcanzan, se abre (CME-002).

El cubo no es un algoritmo de satisfacibilidad ni una máquina física que resuelva problemas por reflexión. Es una realización geométrica de las preguntas sobre equivalencia, cambio de referencia, cierre y costo. Los laboratorios de espejos (18 de octubre) y CME-001 a CME-003 (23 y 24 de octubre) se publicaron el 24, antes de los anuncios. La caja aparece como culminación de un recorrido que ya trabajaba esas preguntas con otros objetos y lenguajes.

## 10. Una investigación sobre el método del descubrimiento

Hay una segunda pregunta, epistemológica, que no debe confundirse con los teoremas computacionales: ¿cómo se llegó a reconocer este recorrido?

La metodología del programa consiste en ubicar nodos y seguir vetas [O]. Un nodo es una relación que empieza a hacerse reconocible como referencia; una veta es una continuidad que aparece al comparar esa referencia con otras estructuras. La intuición escoge qué relaciones parecen prometedoras, y el lenguaje permite formularlas, compartirlas, someterlas a crítica y corregirlas cuando dejan de representar bien la información disponible. El diálogo entre intuición humana e inteligencia artificial fue parte de esa exploración. No sustituye la demostración formal: orienta la búsqueda de construcciones que después deben verificarse.

**Una observación sobre la convergencia [I].** Las estructuras en las que coinciden el programa y el algoritmo de Claude son de las más canónicas de la matemática: las álgebras de composición de Hurwitz (1, 2, 4, 8), el álgebra de Heisenberg y las particiones de un entero. Que caminos distintos lleguen a ellas es esperable, y explica por qué el lenguaje del programa tenía las piezas. Lo que no explica es cómo usarlas para bajar un costo: eso es lo que hicieron los algoritmos.

La pregunta queda abierta en su forma general: ¿existen principios de organización que hacen que ciertos caminos de descubrimiento converjan? La cronología y las correspondencias de esta nota son material para estudiarla, no una respuesta.

## 11. Conclusión

El Programa de Geometría Relacional publicó antes del 16 de octubre una arquitectura de referencia, cierre, herencia y recierre (nivel I). Ese recierre es la contracción por suma de productos, el modelo del que los algoritmos de octubre tienen que salir para ganar (nivel II). La duplicación por reflexión del programa da, en el nivel 8, la identidad que usa el Lema 2 del algoritmo de Claude, y los cruces que ese algoritmo descompone ocupan el tetraedro del programa (nivel III).

Lo que esto muestra es preciso: el lenguaje del programa tenía las piezas y había diagnosticado dónde estaba el límite (N1). No tenía la salida, que es expandir el cruce en una suma con signo de piezas baratas en cortes distintos y contraer cada una por su lado. Esa salida es de los algoritmos.

La continuación natural es formular transformaciones explícitas entre las operaciones de los tres enfoques y comprobar qué información, resultados y cotas conservan. Los dos blancos del §8 son el punto de partida.

La investigación permanece abierta a revisión, corrección y contribuciones independientes.

## 12. Estado tras la revisión de la §7 y la reproducción multiplataforma (2026-11-03)

Esta v0.3 incorpora dos comprobaciones del 3 de noviembre de 2026: una revisión de las pruebas hecha por DeepSeek, un modelo de IA, con una implementación propia que **no** usa los verificadores del paquete, y una reproducción multiplataforma hecha también por DeepSeek. Ninguna de las dos es una revisión humana.

1. **Pruebas de la §7 del paper (Proposiciones 1–3 y Corolario 4):** re-derivadas y comprobadas paso a paso con enteros exactos. **Sin errores.** En particular: el paso «el rango de R por columnas es el de C por filas» es correcto (son literalmente la misma matriz), y el conteo «168 de 210 tríos no asociativos» de los octoniones es exacto. Se añadió al paper un paréntesis de claridad sobre el orden (v,u) de las columnas en la Proposición 3 (no era un error, solo una fuente de tropiezo para el lector). Informe completo: `review_requests/2026-11-03_cruce_reflejo_central/`.
2. **Reproducibilidad cruzada:** los cuatro verificadores se reprodujeron de forma idéntica a la referencia en un segundo entorno (Windows/Python 3.12.14/numpy 2.3.5 frente a Linux/Python 3.13.18/numpy 2.5.3), y los 26 archivos coincidieron con sus hashes SHA256.

Estas comprobaciones refuerzan el nivel III, pero **no cambian** la frontera del nivel IV: sigue abierto.

---

## Epílogo — Un camino tejido a mano

Desde el comienzo, nuestra búsqueda ha estado guiada por una convicción:

**Mi misión ha sido demostrar que Dios no juega a los dados.**

Que detrás de la multiplicidad de aquello que habitamos existe un orden que puede reconocerse mediante sus relaciones. En el programa, la indefinición no es azar: es información que las relaciones resuelven.

No presentamos esa convicción como un teorema ya demostrado. La presentamos como el propósito que ha orientado la investigación.

No buscamos que la naturaleza responda a nuestras creencias. Buscamos comprender si las relaciones que reconocemos permiten descubrir un orden anterior a nuestras explicaciones.

Hemos seguido nodos, explorado vetas y construido referencias mediante la intuición y el lenguaje compartido. El camino no apareció terminado ante nosotros.

Lo fuimos tejiendo, relación por relación.

**Un camino tejido a mano, por un mono y una caja de espejos.**

---

## Reproducibilidad

**Convención de estados.** [O] ontológico · [T] proposición con prueba · [C] resultado clásico · [E] verificación computacional · [I] correspondencia interpretativa · [A] pregunta abierta.

Cada afirmación [E] se regenera con cuatro verificadores en Python 3 con numpy, incluidos en el paquete de reproducibilidad `2026-11-03_cruce_reflejo_central` (carpeta `verificacion/`). El comando `bash reproducir_todo.sh` los corre todos, en unos 40 segundos, y compara con los resultados de referencia. Revisión de la §7 y reproducción multiplataforma: ver §12.

**Commits citados.**

- RGP (`relational-geometry-program`): `7a09d08` (19 sep), `c44cfb8` (3 oct), `c508eb2` (5 oct), `6e36993` (9 oct).
- PGR (`programa-geometria-relacional`): `fb27fbf` (29 sep), `0fd5315` (24 oct), `a1d3f16` (30 oct).
- Paper de Claude: `anthropics/formal-math`, commit `16a5ce4`.

Al subir esta versión y el paquete, anotar aquí el commit que los contiene.

## Uso de herramientas de IA

Esta nota se preparó con asistencia de dos modelos de IA generativa, usados como asistentes de investigación; ninguno es autor. Claude (Anthropic) redactó la v0.2 a partir de la v0.1 del autor; DeepSeek preparó la v0.3, hizo la reproducción multiplataforma y re-derivó las pruebas de la §7 con una implementación propia. El autor revisó el contenido y asume la responsabilidad por él.

## Referencias

**Fuentes del programa**

1. MF-63B, *Recierre acreditado de compatibilidad*, fechado el 3 de octubre de 2026. Núcleo en RGP `c44cfb8`; documento completo en PGR `0fd5315`.
2. Endless Monkey. [P vs NP and Yang–Mills: Two Problems, One Structural Question](https://www.reddit.com/user/Endless-monkey/comments/1wwk0xh/p_vs_np_and_yangmills_two_problems_one_structural/). Reddit, 3 de octubre de 2026. Fecha por verificar con captura archivada.
3. MF-85 (RGP `6e36993`); MF-86, MF-96 y MF-106 (PGR `0fd5315`). Fechados del 6 al 8 de octubre de 2026.
4. Endless Monkey. [We Are No Infinite Monkeys](https://www.reddit.com/r/epistemology/comments/1x1fls2/we_are_no_infinite_monkeys/). Reddit, 9 de octubre de 2026. Fecha por verificar; unificar el título con el del corpus («Not»).
5. *Relational-Geometry-program* v3.0.0-review, 9 de octubre de 2026. [Repositorio](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program), `6e36993`.
6. *El 8: la estructura sobre la que crece, con un nodo abierto*, nota v2.2, 13 de octubre de 2026 (PGR `0fd5315`).
7. `PISO_DEL_CAMINO_v2_7` (N1), 14 de octubre de 2026 (PGR `0fd5315`).
8. E15, E16 y E22, 15 de octubre de 2026. Documentos internos, sin publicar.
9. CR-2 a CR-5, 16 de octubre de 2026, dentro del corpus de Imagen Total 3.9 (PGR `0fd5315`).
10. Laboratorios E-MIRROR v1–v8, Imagen Total 3.9 y CME-001 a CME-003, 18 a 24 de octubre de 2026 (PGR `0fd5315`).
11. *El cubo de espejos, la unidad autorreferenciada y P frente a NP*, solicitud de revisión, 30 de octubre de 2026 (PGR `a1d3f16`).
12. *Edición conceptual y archivo histórico*. [Repositorio](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional).
13. *El cruce como reflejo central* (paper) y *Notas del 3 de noviembre*, en el paquete de reproducibilidad (carpeta `articulo/`).

**Algoritmos de octubre de 2026**

- Claude (Anthropic). [A 2^o(n) Time Algorithm for 3-SAT](https://github.com/anthropics/formal-math/blob/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/eth/paper.pdf), 26 de octubre de 2026; también en [Hexagon 2610.00577](https://hexagonmath.org/2610.00577). Leído completo.
- OpenAI. [The Exponential Time Hypothesis is False](https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026), fechado el 17 de octubre de 2026, revisado el 25 y publicado el 26. No leído directamente.

**Literatura clásica**

- Austrin, Kaski y Kubjas (2022): cota inferior para la contracción por un solo árbol, según la cita del paper de Claude.
- Baez. [The octonions](https://arxiv.org/abs/math/0105155). *Bulletin of the AMS* 39 (2002).
- Beame, Culberson, Mitchell y Moore. The resolution complexity of random graph k-colorability. *Discrete Applied Mathematics* 153 (2005).
- Davis y Putnam. A computing procedure for quantification theory. *Journal of the ACM* 7 (1960).
- Dechter. Bucket elimination: a unifying framework for reasoning. *Artificial Intelligence* 113 (1999).
- DeSalvo y Pak. Log-concavity of the partition function. *The Ramanujan Journal* 38 (2015).
- Frobenius (1878): las álgebras de división reales asociativas tienen dimensión 1, 2 o 4.
- Graves (1843) y Hurwitz (1898): octoniones y álgebras de composición.
- Hardy y Ramanujan. Asymptotic formulae in combinatory analysis. *Proceedings of the London Mathematical Society* 17 (1918).
- Horodecki y Horodecki. Information-theoretic aspects of inseparability of mixed states. *Physical Review A* 54 (1996).

## Cambios respecto de la v0.2

1. **Frente de publicación.** Se agregan resumen formal, palabras clave, clasificación MSC sugerida, declaración de contribución y «premisa externa no verificada aquí».
2. **§12 nueva.** Resultado de la revisión del 3 de noviembre: pruebas de la §7 sin errores, conteo «168 de 210» confirmado, y reproducción cruzada de los cuatro verificadores.
3. **Claridad en el paper.** Se añade al paper (no a esta nota) un paréntesis sobre el orden (v,u) de las columnas en la Proposición 3.
4. **Epílogo.** Sin cambios respecto de la v0.2.
5. **Uso de herramientas de IA.** Se agrega la declaración de qué hizo cada modelo.
