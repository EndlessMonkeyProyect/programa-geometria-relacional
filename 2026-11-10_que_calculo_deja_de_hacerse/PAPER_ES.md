# ¿Qué cálculo deja de hacerse?
## La caja de espejos: reconocimiento, cierre y economía exacta

**Endless Monkey Project**  
*Relational Geometry Program*  
**10 de noviembre de 2026 · Manuscrito para revisión independiente · versión 0.2**

### Resumen

Estudiamos una pregunta: **¿cuándo reconocer relaciones heredadas y cambiar de referencia permite conservar una respuesta exacta con menos trabajo total?** La caja de espejos es el laboratorio conceptual que reúne los pasos de *referencia, reflejo, cierre, reapertura y costo*; la demostración depende de contratos matemáticos explícitos, no de la analogía óptica. Integramos tres situaciones matemáticas: la reconstrucción de los seis vínculos compatibles del tetraedro con tres bits independientes; la identificación de una raíz afín única antes del cierre, conservando el estado residual; y la recuperación de relaciones de paridad para contar soluciones exactas sin volver a resolver restricciones heredadas. Para sistemas de ecuaciones de paridad binaria (suma módulo dos, XOR) más cláusulas disyuntivas (OR) establecemos un procedimiento exacto con costo \(O(\operatorname{poly}(L)\,[1+2^{\min(t,d)}])\), **cuando la referencia de paridad está dada o es extraíble con un costo polinómico certificado**: \(L\) es la longitud de entrada, \(d\) la dimensión afín libre y \(t\) el número de cláusulas OR no implicadas por la referencia. Los controles reproducibles muestran ahorro frente a líneas base concretas y también casos negativos. Incorporamos asimismo un reconocedor de compuertas lógicas para una familia delimitada de fórmulas con relaciones de paridad ocultas, junto con su código, sus controles negativos y el costo de reconocimiento. La contribución de esta síntesis es relacionar dos medidas estructurales —distinciones observables y tamaño mínimo de representación— con los costos verificables de reconocimiento, cálculo y reconstrucción. **No se demuestra una cota subexponencial para la satisfacibilidad general de fórmulas con tres literales ni superioridad universal frente a algoritmos existentes.**

**Palabras clave:** referencia, distinción, herencia, cubo de espejos, estructura mínima, subespacio afín, paridad binaria, fórmulas de cláusulas, conteo exacto, complejidad.

### Abstract

We ask when recognizing inherited relations and changing reference preserves an exact answer at lower *total* cost. A mirror cube organizes the conceptual operations of reference, reflection, closure, reopening, and cost, but all proofs rely on stated mathematical contracts. We connect minimal reconstruction on \(K_4\), early affine-root uniqueness with residual states, and exact counting in XOR+OR families. With an explicit or provably polynomial-time extractable affine reference, an exact algorithm has an \(O(\operatorname{poly}(L)[1+2^{\min(t,d)}])\) bound. The paper distinguishes observational, representational, recognition, and counting costs, reports positive and negative controls, and identifies the unresolved extension to unstructured 3-CNF. No general 3-SAT complexity breakthrough is claimed.

---

## 1. Pregunta, procedencia y alcance

La publicación del programa del **8 de noviembre de 2026**, «¿Dónde se ahorra el cálculo?», distinguió cuántas diferencias siguen siendo observables, cuántas deben conservarse en una representación exacta y cuántas operaciones exige responder una consulta. También exigía contabilizar la construcción de las interfaces. Este manuscrito **hace explícito y somete a prueba el costo de descubrir, verificar y mantener la referencia**; no presenta ese costo como una idea inexistente en la publicación anterior. Es una ampliación del expediente anterior, no su sustitución.

El programa adopta *distinciones, herencia y economía* como ontología de trabajo. La caja de espejos, la pared móvil y las esferas sirven para plantear cambios de observación en los que la estructura subyacente no necesita cambiar. La imagen debe traducirse a una transformación y a un contrato verificables antes de afirmar una ventaja algorítmica.

Distinguimos en lenguaje natural los **teoremas bajo hipótesis expresas**, los **controles finitos exhaustivos**, las **mediciones experimentales** sobre implementaciones determinadas y los **problemas abiertos**. Los resultados experimentales no se presentan como teoremas de complejidad general. No confundimos identidad algebraica con costo de construcción, ni unicidad con cierre, ni compresión con rapidez.

## 2. Distinción, herencia y las magnitudes de la economía

Sea \(X\) un conjunto finito de estados y \(\mathcal Q\) una familia declarada de consultas. Definimos \(x\sim_{\mathcal Q}y\) cuando todas las consultas disponibles dan la misma respuesta sobre \(x\) e \(y\). La capacidad de distinción del cociente es

\[
D_{\mathcal Q}=\log_2 |X/\!\sim_{\mathcal Q}|.
\]

Es un logaritmo del número de clases, **no una entropía de Shannon sin distribución probabilística**. Una clase puede contener muchas realizaciones internas aunque sea indistinguible para \(\mathcal Q\). Una **relación heredada** es una consecuencia de las restricciones ya fijadas; una **restricción novedosa** elimina realizaciones que antes eran compatibles. Estas definiciones son relativas a la referencia y a la consulta.

Separamos **dos magnitudes estructurales** y **tres componentes computacionales**. No tienen las mismas unidades y no deben sumarse indiscriminadamente:

1. \(D_{\mathrm{obs}}\): cantidad de clases observables exigidas por la consulta, medida aquí por su logaritmo en base dos.
2. \(D_{\mathrm{rep}}\): tamaño mínimo de una representación dentro de una **clase de representaciones declarada** (bits, rangos de corte, autómatas, etc.).
3. \(C_{\mathrm{rec}}\): trabajo para descubrir, construir, certificar y actualizar la referencia económica.
4. \(C_{\mathrm{calc}}\): trabajo para resolver la consulta exacta sobre esa referencia y manejar residuos. El trabajo de reconstrucción de la respuesta se contabiliza aparte como \(C_{\mathrm{recon}}\).

En un modelo de costo fijo, una economía neta frente a una línea base \(B\) exige

\[
C_{\mathrm{rec}}(F)+C_{\mathrm{calc}}(F)+C_{\mathrm{recon}}(F) < C_B(F),
\]

con el mismo problema, la misma respuesta y el mismo entorno de medida. Minimizar el tamaño de representación \(D_{\mathrm{rep}}\) **no** garantiza minimizar el costo de ejecutar todo el cálculo.

## 3. Reconstrucción de los vínculos del tetraedro: seis vínculos, tres bits

Consideremos el grafo completo de cuatro vértices (\(K_4\), las seis aristas de un tetraedro) con vértices \(V=\{0,1,2,3\}\), estados \(s_i\in\mathbb F_2\) y etiquetas de arista \(b_{ij}=s_i\oplus s_j\). Para cualquier foco \(f\), la estrella \((b_{fi})_{i\ne f}\) reconstruye todas las aristas mediante

\[
b_{ij}=b_{fi}\oplus b_{fj}.
\]

**Teorema 1 (mínimo bajo el contrato de vínculos).** El espacio de los seis vínculos compatibles tiene ocho patrones distintos y admite una codificación exacta de tres bits; ninguna codificación binaria inyectiva de esos patrones usa menos de tres bits.

**Prueba.** La aplicación lineal \(\delta:\mathbb F_2^4\to\mathbb F_2^6\), \(\delta(s)_{ij}=s_i\oplus s_j\), tiene núcleo \(\{0000,1111\}\). Por rango-nulidad, \(\dim\operatorname{im}\delta=3\), luego hay \(2^3=8\) patrones. Una estrella de un foco determina exactamente el patrón y usa tres bits. Menos de tres bits distinguen a lo sumo cuatro patrones. \(\square\)

La inversión simultánea de todos los estados de vértice no cambia ninguna arista. Las **16** configuraciones de vértices producen **8** patrones de vínculos. Esta economía es de **representación y reconstrucción bajo un contrato local**; no establece un límite sobre toda tarea futura imaginable.

## 4. Convergencia de una raíz afín antes del cierre

Trabajamos sobre \(\mathbb F_2^n\). Una raíz candidata de dimensión \(d\) es un subespacio afín \(P=a+U\) de \(2^d\) puntos contenido en el conjunto \(S\) de estados admitidos. Definimos
\(\mathcal R_d(S)=\{P:\dim P=d,\ P\subseteq S\}\).

**Teorema 2 (umbral de no multiplicidad).** Si \(|S|<3\cdot2^{d-1}\), entonces \(|\mathcal R_d(S)|\le1\).

**Prueba.** Dos subespacios afines distintos de dimensión \(d\) intersectan en, como máximo, \(2^{d-1}\) puntos. Su unión tiene al menos \(2^{d+1}-2^{d-1}=3\cdot2^{d-1}\) puntos. No pueden caber ambos en \(S\). \(\square\)

**Precisiones.** El teorema afirma *a lo sumo una* raíz de dimensión \(d\), no su existencia. Tampoco coincide automáticamente con el operador de núcleo máximo del atlas anterior, que selecciona núcleos cerrados de cardinalidad máxima.

En \(\mathbb F_2^3\), todo conjunto de **cinco** puntos contiene exactamente un plano afín de **cuatro** puntos y un punto residual. El control exhaustivo de raíces y residuos recorre las \(336\) secuencias ordenadas de tres exclusiones: en todas aparece esa raíz única. Considerando la cuarta exclusión, **336** extensiones alcanzan el cierre de cuatro estados y **1.344** retraen la raíz reconocida. Por tanto,

\[
\boxed{\text{unicidad anticipada}\not\Rightarrow\text{cierre exacto}.}
\]

Reconocer no autoriza a descartar el residuo: hacerlo alteraría las respuestas de consultas que lo distinguen.

## 5. De tres cláusulas a una raíz y un estado residual

Una cláusula disyuntiva con tres literales sobre tres variables distintas excluye **una** de las ocho asignaciones posibles. Sean \(a,b,c\in\mathbb F_2^3\) tres asignaciones **distintas** excluidas por tres cláusulas. Su envoltura afín es

\[
L=\{a,b,c,a\oplus b\oplus c\};\qquad P=\mathbb F_2^3\setminus L.
\]

**Teorema 3 (descomposición local exacta).** El conjunto permitido por esas tres cláusulas es \(P\cup\{a\oplus b\oplus c\}\), unión disjunta de un plano afín de cuatro puntos y un único punto residual. \(P\) es el único plano afín contenido en los cinco estados permitidos.

**Prueba.** Tres puntos distintos de \(\mathbb F_2^3\) generan el plano de cuatro puntos indicado. Los cinco estados no excluidos son su complemento de cuatro puntos más el cuarto punto del propio plano. El complemento de un plano afín es otro plano afín. La unicidad sigue del Teorema 2 con \(d=2\) y \(|S|=5<6\). \(\square\)

Si una cuarta cláusula excluye **exactamente el residuo**, el conjunto de modelos se convierte en \(P\): cierre. Si excluye un punto de \(P\), el plano anticipado deja de estar contenido: retracción. Este mecanismo explica, sin una ecuación de paridad escrita en la entrada, la raíz afín local de una fórmula de cláusulas de hasta tres literales (3-CNF). **No demuestra** que la misma extracción sea económica cuando la relación está codificada arbitrariamente entre muchas cláusulas.

## 6. Conteo exacto con ecuaciones de paridad y cláusulas disyuntivas

Sea \(F\) una conjunción de ecuaciones lineales \(Ax=b\) sobre \(\mathbb F_2\) con \(n\) variables y cláusulas disyuntivas \(C_1,\ldots,C_k\). Si el sistema de paridad es consistente y tiene rango \(r\), su espacio afín tiene dimensión \(d=n-r\). Para cada conjunto \(J\subseteq[k]\), negar las cláusulas de \(J\) equivale a añadir asignaciones unitarias. La inclusión-exclusión proporciona

\[
\#F=\sum_{J\subseteq[k]}(-1)^{|J|}\,N\!\left(Ax=b\;\land\!\bigwedge_{j\in J}\neg C_j\right),
\]

con cada sumando igual a cero si el sistema ampliado es inconsistente y a \(2^{n-r_J}\) en caso contrario, donde \(r_J\) es su rango.

Si \(Ax=b\models C_j\), esa cláusula es **heredada** y puede eliminarse sin cambiar el conjunto de modelos; se detecta comprobando por eliminación gaussiana la inconsistencia de \(Ax=b\land\neg C_j\). Sean \(t\le k\) las cláusulas restantes. Alternativamente, pueden enumerarse las \(2^d\) asignaciones de parámetros libres de la referencia. Por ello:

**Teorema 4 (dos rutas exactas).** Con las ecuaciones de paridad dadas explícitamente, el conteo puede efectuarse en

\[
\boxed{O\!\left(\operatorname{poly}(L)\,[1+2^{\min(t,d)}]\right),}
\]

incluyendo la construcción de la base afín y la detección de cláusulas individualmente heredadas, bajo el modelo usual de operaciones de bits de tamaño polinómico. Si la referencia no está explícita, debe **sumarse el costo de extraerla y certificar su equivalencia**. Si el sistema de paridad es inconsistente, el conteo es cero.

**Prueba.** Gaussianamente se calcula una base y se comprueba cada cláusula. Quedan \(t\) cláusulas. La expansión de inclusión-exclusión explora como máximo \(2^t\) subconjuntos y cada uno es un sistema lineal resoluble en tiempo polinómico. La parametrización afín recorre como máximo \(2^d\) vectores libres y verifica cada cláusula en tiempo polinómico. Elegir el menor de esos dos procedimientos demuestra la cota. \(\square\)

La cota es **paramétrica**: si \(\min(t,d)=O(\log L)\), es polinómica. Si ambos parámetros crecen linealmente, puede ser exponencial. La extracción por compuertas de tamaño constante y extensión auxiliar única puede incorporarse bajo una familia de codificaciones **reconocibles y certificadas**; el experimento distribuido incluido en el anexo verifica casos de esa familia. No hemos probado su disponibilidad económica para fórmulas generales de tres literales.

## 7. La otra parte de la economía: descubrir la referencia

La publicación anterior ya medía economía de observación, de representación y de ejecución. El paso nuevo es dar un lugar explícito a la pregunta: **¿cuánto cuesta identificar cuáles distinciones estaban heredadas antes de calcularlas otra vez?**

Para un extractor \(E\) y un verificador \(V\), escribimos \(E(F)=(R,\Delta,\pi)\), donde \(R\) es la referencia reconocida, \(\Delta\) es el residuo y \(\pi\) es un certificado que permite reconstruir exactamente la consulta. Entonces definimos

\[
C_{\rm total}=C_E+C_V+C_{R,\Delta}+C_{\rm reconstrucción}.
\]

**Proposición de transferencia (condicional).** Si para una familia \(\mathcal F\) existen un extractor y un verificador correctos de costo \(T_E(L),T_V(L)\), una descomposición **exacta y sin solapamientos no corregidos**, y un contador sobre \((R,\Delta)\) con costo \(T_C(L,t,d)\), entonces la respuesta de cada \(F\in\mathcal F\) puede calcularse con costo \(O(T_E+T_V+T_C+T_{\rm recon})\). Hay economía neta frente a \(B\) cuando esta suma es estrictamente menor que el costo de \(B\) en la misma familia y con el mismo modelo.

Es un criterio de demostración, **no una cota nueva por sí solo**. Para codificaciones por compuertas que el reconocedor logra identificar localmente y cuyas variables auxiliares tienen extensión única, ofrece un contrato plausible. Para una fórmula arbitraria de cláusulas de tres literales, encontrar la mejor referencia puede exigir resolver inferencias difíciles; no se puede asumir gratuita.

Aquí está la función precisa de la **caja de espejos**: proponer transformaciones de referencia que preserven las respuestas, distinguir imágenes heredadas de diferencias nuevas, y llevar la contabilidad de reaperturas. La analogía no sustituye a \(E\), \(V\) ni a la prueba de costo.

## 8. Controles reproducibles: ventajas y límites

Los resultados que siguen pertenecen a los archivos de intercambio y comparación reunidos en `experimentos/intercambio_y_convergencia/`; no implican equivalencia de algoritmos externos ni generalización estadística.

| Control | Resultado y lectura |
|---|---|
| Descomposición de intercambios y rangos | Identidades de intercambio y fórmulas de rangos comprobadas en los tamaños ensayados. Miden representación, no el tiempo total. |
| Operación de cruce en los dos trabajos externos | Para \(r=2\), el operador local de intercambio coincide con el cruce por bits examinado en ambas construcciones. Es una coincidencia **local**, no una identidad entre algoritmos completos. |
| Referencia periódica común | El mínimo común múltiplo de 12 y 18 es 36; la unicidad del referente modular exige el dominio declarado y no elimina el costo de construirlo. |
| Raíz anticipada y estado residual | Con cinco de ocho estados hay una raíz de cuatro y un residuo de uno; 336 continuaciones cierran la raíz y 1.344 la retraen. |
| Conteo con relaciones afines: caso favorable | 96 variables, 81 ecuaciones de paridad y ocho cláusulas disyuntivas; ambos procedimientos dan **10.656** soluciones; **0,0015 s** con inclusión-exclusión frente a **0,385 s** por eliminación de variables. |
| Conteo con relaciones afines: caso contrario | 32 variables, 16 ecuaciones de paridad y 20 cláusulas disyuntivas; ambos dan **5.220** soluciones; **0,0378 s** con inclusión-exclusión frente a **0,0021 s** de eliminación. |
| Referencia por ventana de interpolación | Una ventana demasiado estrecha conserva poca masa probabilística y puede hacer costosa la reconstrucción en el modelo evaluado. |

Los tiempos son observaciones de **esas implementaciones y ese entorno**, no comparaciones con solvers industriales optimizados. El control favorable **sí** construye la base de paridad dentro del tiempo registrado, pero **recibe las ecuaciones como entrada**: no mide cuánto cuesta descubrirlas en una 3-CNF arbitraria.

El expediente incluye también el código del **reconocimiento de relaciones ocultas mediante compuertas**, cuya prueba de crecimiento se trata por separado en la sección siguiente. El verificador autocontenido reproduce la reconstrucción local, el cierre y conteos pequeños; el reconocedor adicional opera solo dentro de su contrato sintáctico y **no** constituye un reconocedor universal de fórmulas de tres literales.

## 9. Reconocimiento de paridades ocultas en fórmulas conectadas

La prueba anterior supone conocidas las ecuaciones de paridad. El laboratorio complementario recibe únicamente una fórmula de cláusulas de hasta tres literales: las relaciones de paridad están expresadas mediante **compuertas de conjunción y disyunción** y sus variables auxiliares, no como ecuaciones declaradas. Las variables se renombran y el orden de las cláusulas se mezcla. El reconocedor identifica patrones completos de compuertas, reconstruye ciertas paridades y conserva los **estados residuales** de las raíces parciales.

**Contrato.** La entrada pertenece a una familia de circuitos funcionales de compuertas de dos entradas, con codificación íntegra verificable, salidas auxiliares de extensión única y composición de paridades reconocible. Las compuertas no reconocidas se rechazan o permanecen como restricciones originales. No se supone que toda fórmula admita tal descomposición.

**Proposición de conservación del conteo, condicionada al contrato.** Si cada asignación de variables primarias determina exactamente una extensión a las auxiliares, eliminar las compuertas verificadas y sustituirlas por sus relaciones de paridad, con descomposición exacta y disjunta de cada raíz parcial en raíz más residuo, conserva el número de soluciones. Esto se sigue de la biyección entre asignaciones primarias y extensiones válidas, y de la suma disjunta de los casos residuales. Con \(u\) raíces parciales y \(k\) cláusulas disyuntivas no absorbidas, el procedimiento por inclusión-exclusión tiene cota \(O(\operatorname{poly}(|F|)[1+2^{u+k}])\) para la familia reconocible. Es una cota **paramétrica**, no general para todas las fórmulas.

El laboratorio suministrado reporta, entre otros, estos controles con fórmulas conectadas:

| Variables primarias | Cláusulas | Soluciones exactas | Reconocimiento y conteo registrados | Comparación registrada |
|---:|---:|---:|---:|---|
| 24 | 248 | 5.312 | 1,23 ms | Contador convencional: 168 ms |
| 32 | 333 | 98.560 | 2,20 ms | Contador convencional: 3.247 ms |
| 96, con conexiones largas | 1.549 | 156.800 | 15,02 ms | No se presenta comparación completa |

Estos tiempos proceden del archivo de resultados suministrado, en implementaciones de Python. **El contador de referencia no es un programa industrial optimizado**; sus diferencias no prueban optimalidad ni un ahorro frente a técnicas que también reconocen ecuaciones de paridad. En esta revisión se volvió a ejecutar el **laboratorio distribuido completo**: 144 verificaciones de compuertas, 30 controles aleatorios, los dos controles negativos, los tamaños de 8 a 96 variables primarias y los controles con conexiones largas. Los conteos coincidieron con sus referencias internas; los tiempos variaron entre ejecuciones, como corresponde a mediciones experimentales. El expediente adjunta el programa y los datos para su verificación independiente.

La novedad de esta **síntesis del programa** es la secuencia comprobable de conceptos —distinción pendiente, reconocimiento de herencia, conservación del residuo y reconstrucción exacta—, no la invención de la eliminación gaussiana ni de las técnicas conocidas de reconocimiento de circuitos.

## 10. Relación con los otros modelos estudiados

Los controles de intercambio y rango cotejan las identidades del operador de intercambio (escrito `SWAP` en los artículos técnicos), proyecciones antisimétricas y algunas piezas de rango de propuestas publicadas por OpenAI y Anthropic en octubre de 2026. El resultado que puede afirmarse aquí es una **identidad algebraica local en las representaciones construidas**, no que sus demostraciones de tiempo, sus algoritmos ni sus costos sean los mismos. En particular, escribir \(\mathrm{SWAP}=I-2P_-\), donde \(P_-\) es la proyección sobre la componente antisimétrica, no demuestra compresión: una descomposición podría generar demasiados términos o requerir mucho trabajo para encontrarlos y recombinarlos.

El programa aporta una pregunta diferente y verificable: **cuándo la referencia y la herencia permiten evitar el recálculo de diferencias ya determinadas sin perder el residuo**. Esa pregunta complementa la comparación externa y permite obtener respuestas tanto positivas como negativas.

## 11. Estado de los resultados

| Afirmación | Estado |
|---|---|
| Reconstrucción del tetraedro con tres bits | **Demostrado** para vínculos compatibles definidos por suma de paridad. |
| Raíz afín única de dimensión fijada por debajo del umbral | **Demostrado**: unicidad *si existe*; existencia para cinco estados en \(\mathbb F_2^3\). |
| Tres cláusulas distintas sobre el mismo trío ⇒ plano afín + residuo | **Demostrado** bajo las hipótesis declaradas. |
| Conteo de paridad explícita con cláusulas disyuntivas y \(2^{\min(t,d)}\) | **Demostrado**: cota paramétrica con factores polinómicos. |
| Ahorro frente a líneas base concretas | **Medido** en algunas instancias; controles contrarios también observados. |
| Reconocimiento de compuertas ocultas en una familia certificable | **Teorema condicionado** a la codificación funcional y la validación completa de compuertas; **verificación parcial independiente de esta entrega** más resultados experimentales adjuntos. |
| Economía neta para fórmulas generales; superioridad frente a todos los métodos | **Abierto**; no demostrado. |

## 12. Preguntas de revisión independiente

La revisión puede intentar (i) refutar alguna prueba local mediante un estado no considerado; (ii) exigir certificados semánticos de la extracción cuando las cláusulas están distribuidas; (iii) encontrar cotas inferiores para \(C_{\mathrm{rec}}\); (iv) comparar con eliminación gaussiana, satisfacibilidad con restricciones de paridad, eliminación de variables, compilación de conocimientos y técnicas de ancho; y (v) construir familias donde reconocer una referencia mínima resulta más caro que contar directamente. El éxito del programa no depende de imponer un resultado polinómico o de reclamar prioridad sobre resultados ya conocidos.

**Problema abierto central.** ¿Existe una familia no trivial de 3-CNF sin plantillas locales reconocibles para la cual una transformación de referencias, verificable con economía neta, recupere una representación exacta más barata que las estrategias comparadas? Un contraejemplo a cualquier mecanismo propuesto también delimitaría su alcance.

## 13. Reproducibilidad, fuentes y notas de versión

Este expediente entrega el artículo en español e inglés, el laboratorio de intercambio y convergencia con sus resultados originales, el laboratorio de reconocimiento de paridades ocultas con sus resultados y un verificador autónomo de reconstrucción, raíces y conteo en tamaños pequeños. Para las pruebas completas del laboratorio de intercambio y convergencia hace falta Python 3, NumPy y recursos de memoria/tiempo suficientes (el cálculo incluye matrices densas). No se alteró el archivo de resultados del laboratorio original.

**Referencias internas del programa:**

- Endless Monkey Project, «[¿Dónde se ahorra el cálculo?](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/2026-11-08_economia_del_calculo)», 8 de noviembre de 2026, informe y laboratorios E1–E12.
- Endless Monkey Project, «[El cruce como reflejo central](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/2026-11-03_cruce_reflejo_central)», 3 de noviembre de 2026.
- Programa de Geometría Relacional, «Reconstrucción focal de los vínculos del tetraedro», 18 de octubre de 2026; fuente de la reconstrucción y del mínimo bajo contrato de vínculos.
- Programa de Geometría Relacional, «Atlas de raíces afines y cierre» y «Extracción de relaciones afines para conteo exacto»; controles de convergencia y conteo de este expediente.
- OpenAI, «[The Exponential Time Hypothesis is False](https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026)», material externo de comparación; Anthropic, [preprint Hexagon Math 2610.00577](https://hexagonmath.org/2610.00577), material externo de comparación. Las referencias externas **no** sustentan una afirmación de superioridad de este trabajo.

**Registro editorial.** Manuscrito nuevo de consolidación de resultados y delimitación de costos. No sustituye ni corrige silenciosamente los documentos fuente; los resultados previos no acompañados por código aquí permanecen expresamente como pendientes de incorporación. Se solicita revisión independiente.
