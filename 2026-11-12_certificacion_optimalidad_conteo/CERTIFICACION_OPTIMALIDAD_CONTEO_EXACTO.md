---
title: "Certificación de optimalidad local y composición de cotas en conteo exacto"
subtitle: "Propuesta metodológica para contracciones tensoriales e interpolación de Hermite en los algoritmos de Anthropic y OpenAI"
date: "12 de noviembre de 2026 · Propuesta académica · versión 2.0"
lang: es-CR
---

**Autor:** Le Matt Ansatz Di Ego  
**Programa:** Endless Monkey Project · Relational Geometry Program

**Propuesta de investigación para revisión por especialistas · Complejidad computacional, álgebra multilineal y cómputo simbólico**  
**Aplicaciones examinadas:** algoritmos de conteo exacto de Anthropic y OpenAI (octubre de 2026).  
**Estado:** resultados locales demostrados; examen de su composición como certificado global.

## Resumen

Se propone un **marco de certificación de optimalidad relativa** para procedimientos de conteo exacto. El problema consiste en determinar, para una familia de entradas, una clase de transformaciones admisibles y un modelo de recursos explícito, el mínimo costo de producir una representación que permita recuperar exactamente el conteo. La metodología exige dos certificados sobre el mismo recurso: una construcción exacta que proporcione una cota superior y una cota inferior válida para toda estrategia de la clase. Como casos de control se estudian dos operaciones presentes en los enfoques publicados por Anthropic y OpenAI para $`\#\mathrm{SAT}`$: la descomposición separable de un tensor de cruce bajo un corte fijado y la recuperación de un valor polinómico mediante datos de Hermite en nodos auxiliares. Se obtienen mínimos locales de $`q^2`$ y $`1`$ términos para dos cortes del cruce, y de $`d+1`$ observaciones para el espacio completo de polinomios de grado a lo sumo $`d`$. Para subespacios polinómicos estructurados se formula además un criterio exacto de recuperabilidad mediante núcleo y espacio fila. La propuesta académica es estudiar qué hipótesis permiten **componer** esas cotas locales, contabilizando la selección de representaciones, su construcción, la reutilización de datos y la reconstrucción final, hasta obtener certificados de costo para clases completas de estrategias.

**Contribución propuesta.** Un contrato común de optimalidad auditable, dos casos de prueba con cotas coincidentes, un criterio de recuperación para familias polinómicas estructuradas y un programa explícito de revisión sobre la composición de certificados. Las pruebas de rango e interpolación utilizan resultados clásicos; el objetivo de investigación es su integración en límites de costo para clases algorítmicas concretas.

**Palabras clave:** conteo exacto; $`\#\mathrm{SAT}`$; optimalidad relativa; cotas inferiores; complejidad de contracción; rango de aplanamiento; interpolación de Hermite; certificación de recursos.

**Abstract (English).** We propose a framework for certifying relative optimality in exact counting algorithms. Given an input family, an admissible class of transformations, and an explicit cost model, the objective is to bound the minimum cost of an exact representation-and-recovery procedure. The framework pairs an exact upper-bound construction with a lower bound applicable to every strategy in the declared class. Two local test cases motivated by the Anthropic and OpenAI counting approaches are established: optimal separable decompositions of a crossing tensor under fixed flattenings ($`q^2`$ versus $`1`$ terms), and exact Hermite recovery of the value at zero of any degree-$`d`$ polynomial from nonzero nodes ($`d+1`$ observations). For structured polynomial subspaces, a kernel/row-space condition characterizes exact recovery and may yield smaller data requirements. The research proposal asks when local certificates can be composed into meaningful lower bounds for full strategies, including representation selection, data generation, reuse, arithmetic precision, and final reconstruction.

## 1. Objeto de la revisión y contribuciones

El objeto de consulta es el número exacto de asignaciones que satisfacen una fórmula $`F`$ sobre $`n`$ variables:

```math
Z(F)=\sum_{x\in\lbrace0,1\rbrace^n}\mathbf1[F(x)=1]. \tag{1}
```

El procedimiento que se propone separa **exactitud de recuperación**, **mínimo de un recurso local** y **mínimo del costo total**. La separación resulta necesaria cuando una representación reduce una dimensión lineal pero introduce más términos, evaluaciones o precisión aritmética.

La contribución de esta propuesta es una **formulación auditable del contrato de minimalidad** y dos aplicaciones concretas con prueba de cotas iguales. Las cotas de rango y el teorema de interpolación pertenecen a resultados clásicos de álgebra lineal e interpolación; aquí se utilizan como certificados particulares para examinar las construcciones referidas. La novedad eventualmente atribuible al protocolo deberá evaluarse en función de su capacidad para obtener cotas adicionales en clases algorítmicas efectivas.

### 1.1. Pregunta y programa de investigación

La pregunta central es: **¿bajo qué condiciones se pueden transformar mínimos locales certificados en cotas inferiores sobre el costo total de estrategias exactas de conteo?** La propuesta adopta cuatro obligaciones formales:

1. **Contrato de algoritmos:** especificar qué transformaciones, cortes, observaciones, recomposiciones y formas de reutilización pertenecen a la clase admisible.
2. **Exactitud:** establecer una identidad de recuperación de la consulta para toda entrada de la familia.
3. **Certificados locales:** exhibir una construcción y una obstrucción que coincidan para la misma magnitud y el mismo contrato.
4. **Composición:** demostrar una desigualdad que relacione los certificados locales con el costo total, considerando la posible compartición de subresultados y los recursos aritméticos.

La aplicación a Anthropic estudia rangos por cortes y el costo de reorganizar contracciones; la aplicación a OpenAI estudia el espacio efectivo de polinomios auxiliares, sus observaciones necesarias y el costo de producirlas con precisión. **Un certificado global será una consecuencia de hipótesis de composición verificadas**, no de sumar automáticamente cotas calculadas en representaciones diferentes.

## 2. Contrato formal de economía mínima

**Definición 1 (algoritmos admisibles).** Fijados una familia $`\mathcal F_N`$ de entradas, una clase $`\mathcal A_N`$ de procedimientos y una consulta $`Z`$, cada $`A\in\mathcal A_N`$ consta de una construcción de datos auxiliares $`R_A`$ y un recuperador $`D_A`$, y es *exacto* cuando

```math
D_A(R_A(F))=Z(F)\quad\text{para toda }F\in\mathcal F_N. \tag{2}
```

**Definición 2 (costo).** Un modelo $`\mathcal M`$ especifica operaciones elementales, tamaño de representación, precisión y convención de conteo. Para una unidad común de recursos, $`C_{\mathcal M}(A;F)`$ incorpora la construcción, acreditación de exactitud cuando corresponda, preparación de datos, evaluación, recomposición y lectura final. El costo de peor caso y el óptimo relativo a la clase son

```math
B_{\mathcal M}(A,N)=\sup_{F\in\mathcal F_N} C_{\mathcal M}(A;F),\qquad
C^*_{\mathcal A,\mathcal M}(N)=\inf_{A\in\mathcal A_N^{\mathrm{exactos}}}B_{\mathcal M}(A,N). \tag{3}
```

Para múltiples recursos (por ejemplo, tiempo y espacio) se fija una restricción presupuestaria o una relación de Pareto. El costo de encontrar el mejor procedimiento también se contabiliza cuando la selección forma parte del algoritmo anunciado.

**Proposición 1 (certificado relativo de optimalidad).** Si $`A_0`$ es exacto y tiene costo de peor caso a lo sumo $`U(N)`$, y toda construcción exacta de $`\mathcal A_N`$ requiere un costo de peor caso al menos $`L(N)`$, entonces

```math
L(N)\le C^*_{\mathcal A,\mathcal M}(N)\le U(N). \tag{4}
```

Para $`L(N)=U(N)`$, la clase posee un mínimo certificado. La demostración sigue directamente de las definiciones del ínfimo y del supremo. $`\square`$

**Condición de aplicación.** Una desigualdad de rango sólo es una cota de *rango* hasta que se demuestre una relación con el recurso $`C_{\mathcal M}`$. De forma análoga, una cota sobre cantidad de condiciones algebraicas sólo se transforma en una cota de operaciones cuando se modela el costo de producirlas y utilizarlas.

## 3. Aplicación A: tensor de cruce y elección del corte (Anthropic)

El trabajo *A $`2^{o(n)}`$ Time Algorithm for 3-SAT* presenta algoritmos de conteo basados en contracciones de redes tensoriales e identidades de cruce [1, 2]. El examen local considera el tensor, independientemente de la recursión que rodea la contracción.

**Definición 3 (cruce).** Sea $`K`$ un campo y $`q\ge1`$. Definimos $`X\in K^{q\times q\times q\times q}`$ por

```math
X_{ijuv}=\delta_{iv}\delta_{ju},\qquad i,j,u,v\in\lbrace1,\dots,q\rbrace. \tag{5}
```

Para una partición de índices $`P\mid Q`$, $`\mathrm{Flat}_{P\mid Q}(X)`$ denota el aplanamiento matricial que agrupa los índices de $`P`$ en filas y los de $`Q`$ en columnas.

**Lema 1 (rangos de los dos cortes).** Los aplanamientos

```math
A_{(i,u),(j,v)}=\delta_{iv}\delta_{ju},\qquad
B_{(i,v),(j,u)}=\delta_{iv}\delta_{ju} \tag{6}
```

satisfacen

```math
\operatorname{rank}_K A=q^2,\qquad \operatorname{rank}_K B=1. \tag{7}
```

**Demostración.** Cada fila $`(i,u)`$ de $`A`$ contiene exactamente un $`1`$, situado en la columna $`(j=u,v=i)`$, y cada columna exactamente uno: $`A`$ es una matriz de permutación $`q^2\times q^2`$, invertible sobre cualquier campo. En $`B`$ se tiene $`B_{(i,v),(j,u)}=a_{(i,v)}b_{(j,u)}`$, donde $`a_{(i,v)}=\delta_{iv}`$ y $`b_{(j,u)}=\delta_{ju}`$ son vectores no nulos. Por tanto, $`B=ab^\top`$ y su rango es uno. $`\square`$

**Proposición 2 (longitud separable óptima para un corte fijado).** En la clase de representaciones

```math
X_{ijuv}=\sum_{h=1}^{r} a_h(i,u)\,b_h(j,v), \tag{8}
```

la longitud mínima es $`r^*_{(i,u)\mid(j,v)}=q^2`$. Para la clase análoga relativa al corte $`(i,v)\mid(j,u)`$, la longitud mínima es $`1`$.

**Demostración.** Cada sumando de (8) tiene aplanamiento matricial de rango a lo sumo uno. La subaditividad del rango y el Lema 1 dan $`r\ge q^2`$. Una expansión por columnas de la matriz de permutación tiene $`q^2`$ sumandos, por lo que la cota es alcanzable. El corte alineado ya es un producto exterior no nulo. $`\square`$

| Dimensión de índice $`q`$ | Corte $`(i,u)\mid(j,v)`$ | Corte $`(i,v)\mid(j,u)`$ | Cociente de rangos |
|:--:|--:|--:|--:|
| 2 | 4 | 1 | 4 |
| 4 | 16 | 1 | 16 |
| 8 | 64 | 1 | 64 |

La identidad del operador de intercambio por bit, $`\mathrm{SWAP}=I-2P_-`$ con $`P_-=(I-\mathrm{SWAP})/2`$, constituye una operación exacta de descomposición que aparece en la documentación de Anthropic [2]. **La Proposición 2 se refiere a sumandos separables para un corte fijo**, mientras que el procedimiento publicado permite expresiones con signos, cortes alternados y recursión. Su análisis exige un contrato más amplio.

**Condición para trasladar la cota a recursos computacionales.** Sea $`\pi`$ una estrategia que selecciona cortes y descomposiciones y sea $`C_{\mathrm{redes}}(\pi)`$ la suma de construcción de términos, contracciones parciales, cambios de organización y recomposición. Un mínimo de rango local sólo se convierte en mínimo de $`C_{\mathrm{redes}}`$ si se establece una desigualdad válida para toda la clase de estrategias admitidas. En particular, la reducción de $`q^2`$ a $`1`$ cambia el corte; el costo de efectuar y mantener ese cambio depende de las conexiones del resto de la red.

## 4. Aplicación B: datos auxiliares e interpolación de Hermite (OpenAI)

En *The Exponential Time Hypothesis is False*, el valor original del conteo se codifica en una familia polinómica y se reconstruye a partir de datos calculados en puntos auxiliares [3]. Su tratamiento cuantitativo también controla precisión y recursión de contracciones [4]. Formulamos aquí el problema algebraico de recuperación que ese procedimiento utiliza.

**Definición 4 (modelo de observaciones auxiliares).** Sea $`K`$ un campo de característica cero, $`d\ge0`$ y $`H\in K[T]`$ con $`\deg H\le d`$. Se permite conocer, en nodos distintos $`a_1,\ldots,a_k\in K\setminus\lbrace0\rbrace`$, los datos

```math
H^{(j)}(a_i),\qquad 0\le j<m_i,\quad m_i\ge1;\qquad s=\sum_{i=1}^k m_i. \tag{9}
```

La consulta consiste en determinar $`H(0)`$ para **todo** polinomio del espacio $`K[T]_{\le d}`$. El punto $`0`$ está excluido de las observaciones permitidas.

**Proposición 3 (mínimo de condiciones de Hermite).** Para los datos descritos en la Definición 4, la determinación de $`H(0)`$ para todo $`H\in K[T]_{\le d}`$ exige $`s\ge d+1`$. Un conjunto de $`d+1`$ condiciones de Hermite con nodos distintos determina el polinomio y permite recuperar $`H(0)`$ de forma exacta.

**Demostración.** Supóngase $`s\le d`$. El polinomio

```math
P(T)=\prod_{i=1}^{k}(T-a_i)^{m_i} \tag{10}
```

tiene grado $`s\le d`$. Todas las observaciones (9) de $`P`$ y del polinomio cero coinciden, mientras que $`P(0)=\prod_i(-a_i)^{m_i}\ne0`$. Por consiguiente, las observaciones no determinan $`H(0)`$. Con $`s=d+1`$, la matriz confluente de Vandermonde de interpolación de Hermite es invertible sobre $`K`$, pues los nodos son distintos; recupera $`H`$ y en particular $`H(0)`$. $`\square`$

**Corolario 1 (datos homogeneizados).** Si $`Q`$ nodos auxiliares aportan $`J`$ derivadas consecutivas (contando el valor, orden cero), el total de condiciones es $`QJ`$ y la recuperación de toda la clase de grado $`d`$ es posible precisamente cuando $`QJ\ge d+1`$. La elección mínima por cantidad de condiciones requiere $`QJ=d+1`$ cuando existen tales enteros y el contrato permite esa distribución.

**Proposición 4 (recuperabilidad en una familia polinómica estructurada).** Sea $`V\subseteq K[T]_{\le d}`$ un subespacio vectorial de dimensión finita, $`E:V\to K^s`$ el operador lineal que reúne observaciones de valor y derivadas en nodos auxiliares, y $`\ell_0:V\to K`$, $`\ell_0(H)=H(0)`$. Las observaciones determinan $`H(0)`$ para todo $`H\in V`$ si y solo si

```math
\ker E\subseteq\ker\ell_0
\quad\Longleftrightarrow\quad
\ell_0\in\operatorname{im}(E^*). \tag{R}
```

En ese caso existe un vector de coeficientes $`w\in K^s`$ con $`H(0)=w^\top E(H)`$ para todo $`H\in V`$.

**Demostración.** Si $`E(H_1)=E(H_2)`$, el valor en cero queda determinado exactamente cuando $`\ell_0(H_1-H_2)=0`$; esto es la inclusión de núcleos. En dimensión finita, un funcional se anula sobre $`\ker E`$ precisamente cuando pertenece al espacio fila de $`E`$. Por tanto, existe un recuperador lineal $`w^\top E`$. $`\square`$

**Control de alcance.** Para $`V=K[T]_{\le d}`$ y observaciones de Hermite en nodos distintos de cero, la Proposición 3 fija el mínimo $`d+1`$. Para $`V=\mathrm{span}\lbrace1,T(T-1)\rbrace`$, basta una observación en $`T=1`$: todo $`H\in V`$ satisface $`H(0)=H(1)`$. Este ejemplo de grado máximo dos muestra que la estructura de la familia puede modificar el número mínimo de datos. El criterio de núcleo permite calcular ese mínimo una vez determinada la subfamilia efectiva generada por una deformación concreta.

**Ejemplo comprobable.** Sea $`H(T)=3(1+T)^2`$. La terna de datos en el nodo no nulo $`T=1`$ es

```math
H(1)=12,\qquad H'(1)=12,\qquad H''(1)=6. \tag{11}
```

La reconstrucción exacta se expresa mediante el desarrollo de Taylor:

```math
H(0)=H(1)-H'(1)+\tfrac12H''(1)=12-12+3=3. \tag{12}
```

Esta identidad demuestra la recuperación algebraica para un polinomio ilustrativo construido a partir de una fórmula de tres variables con tres soluciones; su evaluación no reproduce las sustituciones del artículo de OpenAI ni mide sus costos asintóticos.

**Condiciones del modelo publicado.** El análisis de OpenAI utiliza familias polinómicas estructuradas, datos de Taylor, operaciones en anillos y requisitos de precisión. La Proposición 3 ofrece la cota de número de datos bajo el espacio completo $`K[T]_{\le d}`$ y observaciones de Hermite permitidas. Para una subfamilia estructurada, la cota puede cambiar; el criterio de la Proposición 4 permite examinarla a partir de su espacio efectivo de polinomios. En un anillo no corporal o bajo precisión finita también se examinan invertibilidad, altura y pérdida de precisión [3, 4].

## 5. Qué puede componerse y qué debe medirse

Las Proposiciones 2 y 3 producen **certificados de optimalidad local** con dos unidades diferentes: número de términos separables y número de condiciones auxiliares. Un certificado global de economía de un algoritmo de conteo exige fijar una clase de estrategias completas, incluyendo cambios de corte, recursión, selección de parámetros, generación de datos, evaluación y recuperación.

Consideremos, por ejemplo, las dos funciones de costo esquemáticas

```math
C_A(\pi)=C_{\mathrm{construcción}}(\pi)+C_{\mathrm{contracción}}(\pi)+C_{\mathrm{recomposición}}(\pi), \tag{13}
```

```math
C_O(\theta)=C_{\mathrm{deformación}}(\theta)+C_{\mathrm{datos}}(\theta)+C_{\mathrm{interpolación}}(\theta)+C_{\mathrm{precisión}}(\theta). \tag{14}
```

La determinación de mínimos globales dentro de clases admisibles $`\Pi,\Theta`$ requiere cotas inferiores sobre **todos** los términos pertinentes o argumentos que los relacionen. Las cotas locales $`r\ge q^2`$ y $`s\ge d+1`$ se transportan a (13)-(14) mediante desigualdades justificadas por el modelo. En especial, no se suman cotas de pasos independientes si los procedimientos pueden compartir resultados intermedios o reutilizar datos.

**Observación de comparabilidad.** Ambos preprints proponen algoritmos de conteo exacto de $`k`$-CNF para $`k`$ fijo; el mismo objetivo $`Z(F)`$ permite comparar corrección. Sus mínimos locales se refieren a objetos distintos y no producen por sí solos una clasificación de cuál algoritmo es más rápido. Un contraste computacional requiere la misma familia de entradas, protocolos y unidades de recursos, y declarar si se mide costo en peor caso, promedio sobre una distribución o una instancia concreta.

### 5.1. Resultado esperado de la propuesta

Un resultado evaluable para cada clase de estrategias consistirá en un cuádruple $`(\mathcal A_N,\mathcal M,L,U)`$: clase admisible, modelo de recursos, cota inferior demostrada y procedimiento exacto con cota superior. La brecha $`U/L`$ —cuando $`L>0`$— permitirá registrar la precisión del certificado. Los casos locales de este artículo tienen brecha $`1`$ para sus recursos propios. Para estrategias completas, la brecha se determinará mediante una desigualdad de composición que tenga en cuenta reutilización de intermedios, cambio de corte, multiplicidad de evaluaciones y precisión aritmética.

La primera línea de examen será **clasificar los datos realmente accesibles** por los algoritmos publicados, en lugar de tomar como modelo todas las descomposiciones o todos los polinomios abstractos. La segunda será demostrar si la estructura restringida permite mejorar las cotas locales y cómo se refleja en operaciones elementales. La tercera será confrontar los certificados de peor caso con implementaciones exactas sobre familias reproducibles de fórmulas.

## 6. Control reproducible y trazabilidad

El control adjunto, `verificar_certificacion.py`, efectúa operaciones racionales exactas: verifica que los aplanamientos del tensor para $`q=2,4,8`$ son, respectivamente, una permutación de orden $`q^2`$ y un producto exterior, y construye la descomposición de $`q^2`$ términos; comprueba la identidad $`\mathrm{SWAP}=I-2P_-`$ para $`q=2`$; contrasta la Proposición 3 en 200 configuraciones aleatorias de nodos y multiplicidades (con $`s\le d`$ el polinomio de la demostración anula los datos; con $`s=d+1`$ la recuperación es exacta) y el Corolario 1 para $`d\le6`$; comprueba el ejemplo de la Proposición 4; enumera las ocho asignaciones de la fórmula de control con tres soluciones; y verifica (11)-(12). Las demostraciones de los lemas son generales; los controles finitos examinan la implementación de sus casos pequeños.

Para reproducir: `python3 verificar_certificacion.py`. La última línea de salida es `TODAS LAS COMPROBACIONES PASARON.` El código utiliza solo la biblioteca estándar de Python, con fracciones exactas.

## 7. Preguntas precisas para el examen independiente

1. **Clase tensorial.** ¿Qué clase de contracciones, permutaciones y descomposiciones admite una cota inferior global que incorpore los rangos locales y el número de subproblemas en la recursión de Anthropic?
2. **Clase polinómica.** ¿Cuál es el espacio lineal efectivo de los polinomios generados por las deformaciones de OpenAI y qué cota de datos auxiliares corresponde a ese espacio, considerando la precisión requerida?
3. **Composición de cotas.** ¿Bajo qué condiciones de independencia, reutilización o suma directa pueden combinarse certificados locales de rango, datos e intermedios para obtener una cota sobre $`C_{\mathcal M}`$?
4. **Comparación reproducible.** ¿Qué familia de entradas y qué modelo de costo permiten contrastar las estrategias completas, incluidas sus transformaciones y recuperadores, sin identificar rango con tiempo ni condiciones de interpolación con operaciones binarias?
5. **Antecedentes y originalidad.** ¿Qué formulaciones existentes de optimalidad relativa y certificación de recursos cubren el protocolo de las Definiciones 1-2 y la Proposición 4, y qué extensión matemática aportaría una cota global nueva?

## 8. Conclusión y solicitud de evaluación

La propuesta establece un **método de certificación de economía mínima relativa** mediante cotas superior e inferior sobre una clase definida de algoritmos y una misma magnitud de recursos. Las demostraciones de control fijan dos mínimos locales exactos: $`q^2`$ frente a $`1`$ término separable para los cortes examinados del tensor de cruce, y $`d+1`$ condiciones auxiliares de Hermite para recuperar $`H(0)`$ en el espacio completo $`K[T]_{\le d}`$. Para familias estructuradas, la Proposición 4 proporciona una prueba de recuperabilidad que permite identificar cuántas condiciones resultan necesarias bajo un contrato más fino.

Se invita a especialistas en complejidad, redes tensoriales, álgebra computacional e interpolación a examinar la pertinencia de las clases admisibles, la completitud de las cotas locales y las condiciones de composición necesarias para derivar límites sobre estrategias de conteo exacto. La evaluación externa deberá identificar antecedentes equivalentes y, cuando proceda, una familia concreta en la que el marco produzca una cota global nueva, un límite demostrado o un contraejemplo.

## Referencias

[1] Anthropic (2026). *A $`2^{o(n)}`$ Time Algorithm for 3-SAT*. Hexagon, versión 1, 27-X-2026. <https://hexagonmath.org/2610.00577>.

[2] Anthropic (2026). *formal-math/eth*, README y archivos de formalización Lean 4. <https://github.com/anthropics/formal-math/blob/main/eth/README.md>.

[3] OpenAI (2026). *The Exponential Time Hypothesis is False*, preprint revisado el 25-X-2026; apartados de deformación, evaluación de datos auxiliares e interpolación. <https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/main_full_version.tex>.

[4] OpenAI (2026). *quantitative-contraction.tex*, apéndice técnico sobre contracción, recuperación y precisión. <https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-contraction.tex>.

[5] Referencias clásicas: rango y factorizaciones de matrices; interpolación confluente de Hermite; métodos de cotas superior e inferior en complejidad computacional. Las Proposiciones 1-3 son explicitaciones o especializaciones de estos fundamentos y se ofrecen para evaluación de su utilidad como herramienta de examen.

---

**Endless Monkey Project**  
*Relational Geometry Program*
