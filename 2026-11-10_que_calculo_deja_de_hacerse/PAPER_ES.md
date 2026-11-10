# ¿Qué cálculo deja de hacerse?
## La caja de espejos: incertidumbre, reconocimiento y cierre

**Endless Monkey Project**  
*Relational Geometry Program*  
10 de noviembre de 2026 · manuscrito para revisión independiente · versión 0.3

### Resumen

Cuando una parte de la incertidumbre ya está resuelta por relaciones heredadas, reconocerla ahorra cálculo, y reconocerla también cuesta. Este manuscrito sigue esa cuenta en la caja de espejos, en cuatro pasos. En el tetraedro, seis comparaciones entre cuatro estados se reconstruyen desde tres, porque la comparación no tiene dirección. Mientras la incertidumbre se reduce, con cinco de ocho estados ya se reconoce el único cierre de cuatro que cabe, y un estado queda pendiente; la exclusión siguiente cierra o deshace lo reconocido. Cuando los reflejos están dados como ecuaciones de paridad, el número exacto de soluciones sale con costo $O(\operatorname{poly}(L)(1+2^{\min(t,d)}))$, donde $d$ es la incertidumbre que el cierre deja libre y $t$ la novedad que queda. Y cuando los reflejos llegan escondidos en compuertas lógicas, reconocerlos tiene un costo propio. Lo medimos contra un DPLL que enumera y contra la eliminación de variables sobre la fórmula tal como llega, aumentando el tamaño. En fórmulas de ancho constante, las dos rutas exactas crecen de forma polinómica y se separan por un factor constante. En fórmulas con conexiones largas, la tabla mayor de la eliminación crece de $2^{6}$ a $2^{58}$, mientras el reconocimiento cuenta 256 variables primarias en 58 ms. Cada resultado vale para la familia que define su sección; la pregunta para fórmulas de tres literales sin plantillas reconocibles queda abierta en el §12.

**Palabras clave:** incertidumbre, comparación, reflejo, cierre, herencia, novedad, reconocimiento, conteo exacto.

## 1. La pregunta

La publicación del 8 de noviembre, «¿Dónde se ahorra el cálculo?», separó tres cosas: cuántas diferencias ve una consulta, cuántas hay que guardar para reconstruir la respuesta y cuántas operaciones cuesta darla. Este manuscrito la continúa con una cuarta: cuánto cuesta reconocer qué parte de la incertidumbre ya estaba resuelta.

La caja de espejos es el laboratorio conceptual. Un espejo refleja un estado en otro. Un cierre es un conjunto que contiene el reflejo de sus propias combinaciones. Una restricción nueva corre la pared: o cae sobre un reflejo que ya estaba, y entonces es herencia, o abre una comparación que no tenía con qué compararse, y entonces es novedad. Cada imagen se traduce a una definición y a una cuenta verificable antes de hablar de ahorro.

Los resultados son de cuatro tipos: teoremas bajo hipótesis escritas, controles finitos exhaustivos, mediciones sobre implementaciones concretas y preguntas abiertas.

## 2. Incertidumbre, herencia y novedad

Sea $X$ un conjunto finito de estados y $\mathcal Q$ una familia de consultas. Dos estados son indistinguibles, $x\sim_{\mathcal Q}y$, cuando toda consulta da la misma respuesta sobre ambos. La resolución de la consulta es

$$
D_{\mathcal Q}=\log_2\lvert X/{\sim_{\mathcal Q}}\rvert ,
$$

el número de bits de diferencia que la consulta alcanza a ver. Es un conteo de clases, sin distribución de probabilidad.

Una relación es **heredada** cuando ya es consecuencia de lo fijado. Una restricción es **novedad** cuando excluye estados que lo fijado todavía admitía. Las dos palabras se refieren siempre a una referencia y a una consulta.

La economía tiene dos medidas de estructura y tres de trabajo:

1. $D_{\mathrm{obs}}$: lo que la consulta necesita distinguir.
2. $D_{\mathrm{rep}}$: lo mínimo que hay que guardar para reconstruirlo, dentro de una clase de representaciones declarada.
3. $C_{\mathrm{rec}}$: reconocer, comprobar y mantener la referencia.
4. $C_{\mathrm{calc}}$: contar sobre esa referencia y llevar lo pendiente.
5. $C_{\mathrm{recon}}$: reconstruir la respuesta.

Las dos primeras se miden en bits; las otras tres, en operaciones. Frente a una ruta de comparación $B$, con el mismo problema, la misma respuesta y el mismo modelo de costo, hay economía neta cuando

$$
C_{\mathrm{rec}}(F)+C_{\mathrm{calc}}(F)+C_{\mathrm{recon}}(F)<C_B(F).
$$

Guardar poco y calcular poco son dos cosas distintas: la representación más corta puede salir cara de encontrar.

## 3. El tetraedro: la comparación sin dirección

Cuatro estados $s_0,s_1,s_2,s_3\in\mathbb F_2$ ocupan los vértices de un tetraedro. Cada arista lleva la comparación entre sus dos extremos, el reflejo de un estado en el otro:

$$
b_{ij}=s_i\oplus s_j .
$$

Desde cualquier vértice $f$, las tres comparaciones que salen de él reconstruyen las seis: $b_{ij}=b_{fi}\oplus b_{fj}$.

**Teorema 1.** Las seis comparaciones compatibles forman ocho patrones. Tres bits los codifican exactamente, y tres es el mínimo de cualquier código binario inyectivo.

**Prueba.** La aplicación lineal $\delta:\mathbb F_2^4\to\mathbb F_2^6$, $\delta(s)_{ij}=s_i\oplus s_j$, tiene núcleo $\lbrace 0000,1111\rbrace$. Por rango y nulidad, su imagen tiene dimensión 3: son $2^3=8$ patrones. Las tres comparaciones desde un vértice los distinguen todos, y dos bits distinguen a lo sumo cuatro. $\square$

Invertir los cuatro estados a la vez deja intactas las seis comparaciones: la comparación registra la diferencia, no el lado desde el que se comparó. Por eso las 16 configuraciones de vértices dan 8 patrones, y un bit —la orientación del conjunto— queda fuera de lo que las aristas ven. La economía aquí es de representación: tres bits sostienen seis comparaciones.

## 4. La incertidumbre se reduce: reconocer antes de cerrar

Trabajamos en $\mathbb F_2^n$, los $2^n$ estados de $n$ bits. Un **cierre** de dimensión $d$ es un conjunto $P$ de $2^d$ estados que contiene el reflejo de sus propias combinaciones: si $a,b,c\in P$, entonces $a\oplus b\oplus c\in P$. Sea $S$ el conjunto de estados que siguen admitidos.

**Teorema 2 (un solo cierre cabe).** Si $\lvert S\rvert<3\cdot2^{d-1}$, entonces $S$ contiene a lo sumo un cierre de dimensión $d$.

**Prueba.** Dos cierres distintos de dimensión $d$ comparten a lo sumo $2^{d-1}$ estados, así que juntos ocupan al menos $2^{d+1}-2^{d-1}=3\cdot2^{d-1}$. $\square$

El teorema da unicidad cuando el cierre existe; que exista depende de $S$.

En $\mathbb F_2^3$ hay ocho estados: tres bits de incertidumbre. Cada exclusión resuelve una parte. Tras tres exclusiones quedan cinco estados, y en los 56 casos posibles cuatro de ellos forman el único cierre que cabe; el quinto es la incertidumbre que sigue abierta. El cierre ya se reconoce, con un estado todavía pendiente.

La cuarta exclusión decide. Si resuelve el estado pendiente, quedan los cuatro del cierre: cierra. Si quita un estado del cierre reconocido, ese cierre deja de caber: lo reconocido se retrae. El recorrido exhaustivo de las 336 secuencias ordenadas de tres exclusiones y sus 1.680 continuaciones da 336 cierres y 1.344 retracciones.

La cuenta de incertidumbre es exacta. Pasar de ocho estados a cuatro resuelve un bit:

$$
\log_2\frac{8}{5}+\log_2\frac{5}{4}=1 .
$$

Las tres primeras exclusiones resuelven 0,678 bits y ya permiten reconocer el cierre; la cuarta resuelve los 0,322 restantes y lo confirma. Reconocer ocurre antes que cerrar. El estado pendiente se conserva hasta que una exclusión lo resuelva, porque descartarlo antes cambiaría la respuesta de toda consulta que lo distinga.

## 5. Tres cláusulas: un cierre y un estado pendiente

Una cláusula de tres literales sobre tres variables distintas excluye uno de los ocho estados de esas variables. Sean $a,b,c\in\mathbb F_2^3$ tres estados distintos excluidos por tres cláusulas. Su propio cierre y su complemento son

$$
L=\lbrace a,b,c,a\oplus b\oplus c\rbrace ,\qquad P=\mathbb F_2^3\setminus L .
$$

**Teorema 3.** Los estados que admiten las tres cláusulas son $P\cup\lbrace a\oplus b\oplus c\rbrace$: un cierre de cuatro estados y un estado pendiente. $P$ es el único cierre de dimensión 2 contenido en ellos.

**Prueba.** Tres estados distintos de $\mathbb F_2^3$ generan el cierre de cuatro estados $L$. Los cinco admitidos son el complemento de $L$, que también es un cierre, más el cuarto estado de $L$. La unicidad sigue del Teorema 2 con $d=2$ y $\lvert S\rvert=5<6$. $\square$

Una cuarta cláusula que excluye exactamente el estado pendiente cierra $P$; una que excluye un estado de $P$ lo retrae. Así, una fórmula de cláusulas de tres literales produce un cierre local sin que ninguna ecuación de paridad aparezca escrita. Según la terna, ese cierre fija una variable (24 de las 56 ternas), iguala o separa dos (24) o es una paridad de las tres (8).

Reconocer el mismo cierre cuando la relación está repartida entre muchas cláusulas es otro problema, con su propio costo: el tema del §7.

## 6. Contar cuando los reflejos están dados

Sea $F$ la conjunción de ecuaciones de paridad $Ax=b$ sobre $\mathbb F_2$, con $n$ variables, y de cláusulas disyuntivas $C_1,\dots,C_k$. En el hilo:

- las ecuaciones son el cierre heredado; si son consistentes y de rango $r$, dejan $d=n-r$ bits de incertidumbre libre;
- cada cláusula corre la pared. Si el cierre ya la cumple ($Ax=b\models C_j$), es herencia y se retira sin cambiar las soluciones; si no, es novedad. Quedan $t\le k$ cláusulas de novedad.

Que una cláusula sea herencia se comprueba por eliminación gaussiana: $Ax=b\land\lnot C_j$ es inconsistente. Negar una cláusula equivale a fijar sus literales en falso, así que cada término de la inclusión–exclusión es otro sistema de paridad. Escribimos $N(\cdot)$ para el número de soluciones:

$$
N(F)=\sum_{J\subseteq\lbrace 1,\dots,k\rbrace}(-1)^{\lvert J\rvert}N\Big(Ax=b\land\bigwedge_{j\in J}\lnot C_j\Big).
$$

Cada sumando vale $0$ si el sistema ampliado es inconsistente, y $2^{n-r_J}$ si no, con $r_J$ su rango.

**Teorema 4 (dos rutas exactas).** Con las ecuaciones de paridad dadas, el número de soluciones se calcula en tiempo

$$
O\big(\operatorname{poly}(L)\cdot(1+2^{\min(t,d)})\big),
$$

con $L$ la longitud de la entrada, incluyendo la construcción de la base y la retirada de las cláusulas heredadas, en el modelo usual de operaciones sobre palabras de tamaño polinómico. Si el sistema de paridad es inconsistente, el número es cero.

**Prueba.** La eliminación gaussiana construye la base y prueba cada cláusula en tiempo polinómico. Quedan $t$ cláusulas: la inclusión–exclusión visita a lo sumo $2^t$ subconjuntos, cada uno un sistema lineal. Alternativamente, se recorren los $2^d$ valores de los parámetros libres y se prueba cada cláusula. Se toma la ruta menor. $\square$

Leído en el hilo: el costo se paga en la menor de dos incertidumbres, recorrer lo que el cierre dejó libre o desplegar la novedad que queda. Es polinómico cuando una de las dos es $O(\log L)$ y exponencial cuando las dos crecen linealmente. Cuando la entrada trae los reflejos escondidos, a la cuenta se suma el costo de reconocerlos.

## 7. El costo de reconocer lo heredado

La publicación del 8 de noviembre ya medía la economía de observar, de representar y de ejecutar. Aquí la pregunta previa tiene lugar propio: ¿cuánto cuesta saber qué estaba heredado antes de volver a calcularlo?

Un reconocedor $E$ lee la fórmula y devuelve $E(F)=(R,\Delta,\pi)$: la referencia reconocida $R$, lo pendiente $\Delta$ y una constancia $\pi$ con la que se comprueba que la respuesta se reconstruye exacta. Un comprobador $V$ la revisa. El costo total es

$$
C_{\mathrm{total}}=C_E+C_V+C_{R,\Delta}+C_{\mathrm{recon}} .
$$

**Proposición de transferencia (condicional).** Supongamos que una familia $\mathcal F$ admite un reconocedor y un comprobador correctos, de costos $T_E(L)$ y $T_V(L)$; una descomposición exacta de cada fórmula en referencia y pendiente, disjunta o corregida por inclusión–exclusión; y un contador sobre $(R,\Delta)$ de costo $T_C(L,t,d)$. Entonces cada $F\in\mathcal F$ se cuenta con costo $O(T_E+T_V+T_C+T_{\mathrm{recon}})$. Hay economía neta frente a $B$ cuando esa suma es menor que el costo de $B$ en la misma familia y con el mismo modelo.

La proposición es un criterio para demostrar ahorros familia por familia. En una fórmula de tres literales cualquiera, encontrar la mejor referencia puede exigir inferencias difíciles, y ese costo entra completo en la cuenta.

La función de la caja de espejos es concreta: proponer cambios de referencia que conservan la respuesta, separar los reflejos heredados de las diferencias nuevas y llevar la cuenta de lo que se reabre.

## 8. Controles con los reflejos dados

Los controles de esta sección están en `experimentos/intercambio_y_convergencia/`. Los tiempos son los del archivo de resultados, medidos con implementaciones en Python.

| Control | Resultado |
|---|---|
| Unicidad del referente y su construcción (C5) | Los restos módulo 12 y 18 determinan un entero dentro de un ciclo de 36, su mínimo común múltiplo: en $[0,72)$ cada par de restos aparece dos veces, y solo existen 36 de los 216 pares posibles. Saber que la referencia es única y construirla son dos trabajos distintos. |
| Reconocer antes de cerrar (C6) | Cinco de ocho estados: un cierre de cuatro y un estado pendiente; 336 continuaciones cierran y 1.344 retraen. |
| Reflejos dados, caso favorable (C7) | 96 variables, 81 ecuaciones de paridad y 8 cláusulas: ambas rutas cuentan 10.656. La inclusión–exclusión visita 39 términos en 0,0015 s; la eliminación de variables forma una tabla de $2^{24}$ y tarda 0,385 s. |
| Reflejos dados, caso contrario (C7) | 32 variables, 16 ecuaciones y 20 cláusulas: ambas cuentan 5.220; inclusión–exclusión 0,0378 s, eliminación 0,0021 s. |
| Mucha novedad, poco cierre (C7) | 24 variables, 2 ecuaciones y 48 cláusulas: la inclusión–exclusión pasa el tope de dos millones de términos; la eliminación cuenta 4.672, igual que la fuerza bruta. |
| Ventana de interpolación (C8) | Con $Q=400$, una ventana de ancho $\sqrt Q$ deja fuera el 24,8 % del peso; de ancho $2\sqrt Q$, el 2,1 %; de ancho $3\sqrt Q$, el 0,06 %. Una referencia demasiado estrecha encarece la reconstrucción. |

## 9. Reflejos escondidos en compuertas

Aquí la fórmula llega solo como cláusulas de hasta tres literales. Los reflejos, que son relaciones de paridad entre variables primarias, están construidos con compuertas de conjunción y disyunción de dos entradas y sus variables auxiliares. Los nombres de las variables se permutan y el orden de las cláusulas se mezcla. Algunos reflejos llegan como cierre con un estado pendiente. El reconocedor identifica compuertas completas, reconstruye las paridades y conserva los estados pendientes.

**Contrato.** La fórmula es un circuito funcional de compuertas de dos entradas, cada asignación de las variables primarias determina una sola extensión a las auxiliares, y las paridades se componen de forma reconocible. Lo que sale del contrato se rechaza.

**Proposición de conservación del conteo (bajo el contrato).** Sustituir las compuertas verificadas por sus relaciones de paridad, y cada cierre parcial por su cierre más su estado pendiente, conserva el número de soluciones: las asignaciones primarias y sus extensiones están en biyección, y los casos pendientes se suman por separado. Con $u$ cierres parciales y $k$ cláusulas de novedad, el conteo cuesta $O(\operatorname{poly}(\lvert F\rvert)\cdot(1+2^{u+k}))$ en la familia.

**Medición.** El script `experimentos/linea_base_generica/comparacion_y_escala.py` mide todas las rutas sobre las mismas fórmulas ya generadas, en la misma ejecución:

- reconocer y contar, mediana de 7;
- eliminación de variables sobre la fórmula tal como llega, sin reconocer nada, mediana de 3, cuando su tabla mayor es de hasta $2^{24}$;
- el DPLL del laboratorio, mediana de 3, hasta 32 variables primarias en el ciclo y 24 en conexiones largas.

Los conteos completados coinciden en todas las filas. La familia de conexiones largas se extiende hasta 256 variables primarias.

| Familia | Primarias | Cláusulas | Soluciones | Reconocer y contar | Eliminación genérica | Tabla mayor de la eliminación | DPLL |
|-------|---------:|---------:|--------------------:|----------:|----------:|----------:|---------:|
| ciclo | 24 | 248 | 5.312 | 1,4 ms | 6,6 ms | $2^{6}$ | 227,7 ms |
| ciclo | 32 | 333 | 98.560 | 2,4 ms | 9,4 ms | $2^{5}$ | 4.662 ms |
| ciclo | 96 | 941 | 420.906.795.008.000 | 12,9 ms | 45,8 ms | $2^{6}$ | — |
| largas | 24 | 409 | 26 | 2,6 ms | 11,6 ms | $2^{9}$ | 19,6 ms |
| largas | 48 | 789 | 364 | 6,5 ms | 27,8 ms | $2^{13}$ | — |
| largas | 64 | 1.036 | 3.084 | 8,4 ms | 54,9 ms | $2^{18}$ | — |
| largas | 96 | 1.549 | 156.800 | 12,8 ms | 247,0 ms | $2^{21}$ | — |
| largas | 128 | 2.043 | 6.272.000 | 22,4 ms | — | $2^{29}$ | — |
| largas | 200 | 3.183 | 25.690.112.000 | 41,3 ms | — | $2^{40}$ | — |
| largas | 256 | 4.076 | 13.153.337.344.000 | 58,0 ms | — | $2^{58}$ | — |

Las 23 fórmulas medidas están en `RESULTADOS_COMPARACION.json`; la tabla muestra diez.

**Ciclo de ternas.** Cada reflejo toca solo a sus vecinos y el ancho es constante: la eliminación forma tablas de a lo sumo $2^{6}$. Las dos rutas exactas crecen de forma polinómica y se separan por un factor de 3,5 a 5. El DPLL recorre dos nodos por solución (10.623 nodos para 5.312 soluciones; 197.119 para 98.560): su tiempo sigue al número de soluciones. En esta familia, la ventaja frente al DPLL viene de contar sin enumerar, y eso lo hacen las dos rutas exactas.

**Conexiones largas.** Un tercio de los reflejos une variables lejanas. El ancho de la eliminación crece con el tamaño: $2^{6}$ con 12 primarias, $2^{21}$ con 96 y $2^{58}$ con 256. Una segunda ordenación, de relleno mínimo, da $2^{19}$ y $2^{54}$. La eliminación cuenta hasta 96 primarias, en 247 ms; desde 128 necesita tablas de $2^{29}$ o mayores. El reconocimiento cuenta las 256 primarias y 4.076 cláusulas en 58 ms. Aquí reconocer lo heredado paga: la eliminación guarda como tablas completas relaciones que el reconocimiento resuelve como ecuaciones de paridad.

**Alcance de la medición.** En todas estas fórmulas $u\le 3$ y $k\le 3$, así que $2^{u+k}\le 64$: la medición sigue la parte polinómica de la cota. Los pasos siguientes son hacer crecer $u+k$ y comparar con contadores dedicados que también reconocen compuertas o usan descomposiciones en árbol (§13). Con `--dimacs`, el script escribe cada fórmula en formato DIMACS con su conteo esperado, lista para esos contadores.

**Contrato bajo prueba.** `prueba_adversarial.py` toma fórmulas válidas, les aplica al azar una de siete mutaciones (cambiar un signo, quitar o añadir una cláusula, reconectar un literal, fijar una variable, intercambiar o identificar variables) y añade ocho casos construidos fuera de la familia. De 5.889 fórmulas, el reconocedor rechaza 4.444 y acepta 1.445, y las 1.445 aceptadas dan el mismo conteo que la eliminación genérica. El laboratorio original verifica además 144 tablas de verdad de compuertas, 30 fórmulas aleatorias contra enumeración y dos controles fuera de contrato.

## 10. Relación con los preprints de octubre

Los controles C1–C4 cotejan, en representaciones construidas en el laboratorio, piezas de dos preprints de octubre de 2026, uno de OpenAI y otro de Anthropic. El operador de intercambio cumple $\mathrm{SWAP}=I-2P_-$, con $P_-$ la proyección sobre la parte antisimétrica. Con $r=2$, la matriz $V_0$ del preprint de OpenAI coincide con el cruce por bits del de Anthropic para $\lambda=1,\dots,5$, y las fórmulas de rango por pieza coinciden con los rangos medidos en todos los tamaños ensayados.

Es una identidad local entre representaciones. Que una descomposición ahorre depende además de cuántos términos genera y de cuánto cuesta encontrarlos y recombinarlos: la misma cuenta del §2.

La pregunta del programa es otra y los complementa: cuándo la referencia y la herencia permiten dejar de recalcular diferencias ya resueltas, conservando lo pendiente.

## 11. Estado de los resultados

| Resultado | Estado |
|---|---|
| Tetraedro: seis comparaciones desde tres bits | Teorema 1 |
| A lo sumo un cierre de dimensión $d$ bajo el umbral $3\cdot2^{d-1}$ | Teorema 2; existencia comprobada para cinco estados en $\mathbb F_2^3$ |
| Tres cláusulas: un cierre de cuatro y un estado pendiente | Teorema 3 |
| Conteo con reflejos dados en $O(\operatorname{poly}(L)(1+2^{\min(t,d)}))$ | Teorema 4 |
| Conteo con reflejos escondidos en compuertas | Proposición bajo contrato; 23 fórmulas medidas; 5.889 fórmulas en la prueba de contrato |
| Ahorro frente a rutas concretas | Medido: casos favorables y contrarios con reflejos dados (§8); factor constante con ancho constante y ventaja creciente con conexiones largas (§9) |
| Contadores dedicados, crecimiento en $u+k$, cota inferior para $C_{\mathrm{rec}}$ | Abierto |
| Economía neta en fórmulas de tres literales sin plantillas reconocibles | Abierto: pregunta central (§12) |

## 12. Preguntas para la revisión

1. Refutar alguna prueba local con un estado no considerado.
2. Exigir constancias semánticas del reconocimiento cuando los reflejos están repartidos.
3. Encontrar cotas inferiores para $C_{\mathrm{rec}}$.
4. Contar las fórmulas exportadas con contadores dedicados (GANAK, SharpSAT-TD) y con preprocesado por definibilidad (B+E).
5. Construir familias donde reconocer la referencia mínima cueste más que contar directamente.

**Pregunta central.** ¿Existe una familia no trivial de fórmulas de tres literales, sin plantillas locales reconocibles, en la que un cambio de referencia verificable recupere una representación exacta más barata que las rutas comparadas? Un contraejemplo a cualquier mecanismo propuesto también delimita su alcance.

## 13. Puentes con lo conocido

El hilo de este manuscrito está escrito en el vocabulario del programa. Esta tabla lo enlaza con el vocabulario técnico.

| En el hilo | En la literatura |
|---|---|
| comparación sin dirección en el tetraedro | espacio de cortes (cociclos) de $K_4$, de dimensión 3 |
| cierre | subespacio afín de $\mathbb F_2^n$ |
| cierre con un estado pendiente | raíz afín más residuo; bloque de paridad con tres de sus cuatro cláusulas |
| reflejos dados | sistema de ecuaciones XOR; eliminación gaussiana |
| herencia de una cláusula | implicación $Ax=b\models C_j$ |
| novedad que queda | cláusulas OR no implicadas |
| desplegar la novedad | inclusión–exclusión sobre cláusulas [Iwama 1989] |
| reconocer lo heredado | detección de compuertas y definibilidad [Lagniez y Marquis 2014; Lagniez, Lonca y Marquis 2016] |
| reconocedor, comprobador y constancia | extractor, verificador y certificado |
| eliminación genérica | eliminación de variables; conteo exponencial en el ancho de árbol [Samer y Szeider 2010] |
| reflejos dentro de un resolvedor | XOR nativo con eliminación gaussiana [Soos, Nohl y Castelluccia 2009] |
| contadores dedicados | GANAK [Sharma et al. 2019]; SharpSAT-TD [Korhonen y Järvisalo 2021] |

La conservación del conteo al sustituir compuertas reconocidas (§9) tiene antecedente directo en B+E, que elimina salidas de compuertas definidas y conserva el número de modelos. Lo propio de esta síntesis es la secuencia del hilo, sobre técnicas conocidas: incertidumbre que se reduce, reconocimiento antes del cierre, conservación de lo pendiente y cuenta completa del costo de reconocer.

### Referencias

**Del programa**

- Endless Monkey Project, «[¿Dónde se ahorra el cálculo?](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/2026-11-08_economia_del_calculo)», 8 de noviembre de 2026.
- Endless Monkey Project, «[El cruce como reflejo central](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/2026-11-03_cruce_reflejo_central)», 3 de noviembre de 2026.
- Programa de Geometría Relacional, «Reconstrucción focal de los vínculos del tetraedro», 18 de octubre de 2026.

**Externas**

- K. Iwama, «CNF-satisfiability test by counting and polynomial average time», *SIAM Journal on Computing* 18(2), 385–391, 1989.
- J.-M. Lagniez y P. Marquis, «Preprocessing for Propositional Model Counting», AAAI 2014, 2688–2694.
- J.-M. Lagniez, E. Lonca y P. Marquis, «Improving Model Counting by Leveraging Definability», IJCAI 2016, 751–757; «Definability for model counting», *Artificial Intelligence* 281, 2020.
- M. Samer y S. Szeider, «Algorithms for propositional model counting», *Journal of Discrete Algorithms* 8, 2010.
- M. Soos, K. Nohl y C. Castelluccia, «Extending SAT Solvers to Cryptographic Problems», SAT 2009, LNCS 5584, 244–257.
- S. Sharma, S. Roy, M. Soos y K. S. Meel, «GANAK: A Scalable Probabilistic Exact Model Counter», IJCAI 2019, 1169–1176.
- T. Korhonen y M. Järvisalo, «Integrating Tree Decompositions into Decision Heuristics of Propositional Model Counters», CP 2021, LIPIcs 210, 8:1–8:11.
- OpenAI, «[The Exponential Time Hypothesis is False](https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026)», preprint, 25 de octubre de 2026.
- Anthropic, «[A $2^{o(n)}$ Time Algorithm for 3-SAT](https://hexagonmath.org/2610.00577)», Hexagon 2610.00577, 27 de octubre de 2026.

## 14. Reproducción

```bash
python3 -I experimentos/verificar_reconstruccion_y_convergencia.py
```

Comprueba los teoremas 1 a 4 en tamaños pequeños, sin dependencias. Las demás instrucciones y el registro de reproducción están en [`ANEXO_EVIDENCIAS.md`](ANEXO_EVIDENCIAS.md).
