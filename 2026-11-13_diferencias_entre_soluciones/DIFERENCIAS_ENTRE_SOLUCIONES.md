# Diferencias entre soluciones: medición, conservación y costo

*Borrador para revisión independiente · 13 de noviembre de 2026*

**Endless Monkey Project**  
*Relational Geometry Program*

**Autor:** Le Matt Ansatz Di Ego.

## Resumen sencillo

Una solución puede describirse por su posición respecto de una referencia sin identificarla individualmente. Un conjunto de soluciones admite tres medidas iniciales: cuántas hay, cuál es la suma de sus posiciones y cuál es la suma de los cuadrados de esas posiciones. Estas cantidades se calculan y se transportan mediante reglas exactas de suma y producto. En consecuencia, es posible estudiar diferencias entre sistemas sin producir una lista completa de sus soluciones.

Tres ensayos reproducibles examinan esa conservación en operaciones de conteo exacto. La contracción conjunta recupera conteo y momentos en ocho instancias; la agrupación por continuaciones y la recuperación por Hermite permiten comparar costos; y la descomposición tensorial con signos se verifica en 4.096 casos, con rangos 8 y 64 según el corte. En una recuperación polinómica se obtienen exactamente las medidas 18, 51 y 165 mediante seis datos de Hermite. La factorización tensorial muestra una reducción local de operaciones frente al comparador declarado.

El resultado de interés es una condición comprobable: las relaciones conservadas deben permitir recuperar las medidas exigidas por cada consulta, con un costo total menor que el de una alternativa igualmente exacta.

## 1. Definiciones

Sea $`F`$ un sistema finito de restricciones y sea $`K_F`$ su conjunto de soluciones. Se fija una referencia $`w:K_F\to\mathbb Z_{\ge0}`$, por ejemplo el peso $`w(x)=\sum_{i=1}^n x_i`$ de una asignación booleana. La referencia establece qué propiedad se compara; no representa una distancia física universal.

Se definen los momentos iniciales

```math
N=\sum_{x\in K_F}1,\qquad
S=\sum_{x\in K_F}w(x),\qquad
Q=\sum_{x\in K_F}w(x)^2.
```

Si $`N>0`$, el centro de la distribución respecto de la referencia es $`\mu=S/N`$, y la dispersión cuadrática media es $`V=Q/N-(S/N)^2`$. Si $`N=0`$, el sistema es incompatible y el centro queda indefinido.

**Diferencia:** variación entre los resultados de una comparación declarada. **Distinción:** diferencia que alguna consulta admitida puede detectar. **Herencia:** recuperación de una medida a partir de relaciones ya calculadas y de una regla de composición demostrada. **Cierre:** conservación exacta de las respuestas exigidas al transformar la representación. **Economía:** reducción de recursos bajo la misma tarea, dominio y exigencia de exactitud.

El conteo $`N`$ por sí solo no determina cómo se distribuyen las soluciones. Los momentos $`S,Q`$ agregan medidas colectivas, aunque tampoco determinan necesariamente toda la distribución.

## 2. Resultado de composición

**Proposición 1 (conservación de los dos primeros momentos).** Sean $`A,B`$ dos conjuntos de soluciones que se combinan por producto cartesiano, con posiciones aditivas $`w(a,b)=w_A(a)+w_B(b)`$. Para sus ternas $`(N,S,Q)`$ y $`(n,s,q)`$, la terna combinada satisface

```math
(N,S,Q)\otimes(n,s,q)=
\bigl(Nn,\;Sn+Ns,\;Qn+2Ss+Nq\bigr).
```

**Demostración.** Se suman, sobre todas las parejas, las identidades $`1=1`$, $`w_A+w_B`$ y $`(w_A+w_B)^2=w_A^2+2w_Aw_B+w_B^2`$. La factorización de cada suma produce las tres componentes. $`\square`$

Una realización equivalente utiliza el anillo truncado $`R=\mathbb Z[u]/(u^3)`$:

```math
J_F(u)=\sum_{x\models F}(1+u)^{w(x)}\pmod{u^3}
=N+Su+\frac{Q-S}{2}u^2.
```

La asociatividad y la distributividad garantizan que una red finita de sumas y productos preserve $`J_F`$ al cambiar el orden exacto de eliminación. Para factores con variables compartidas, la suma se efectúa sobre las asignaciones compatibles de la frontera; la fórmula de producto cartesiano se aplica solamente a las partes independizadas por ese condicionamiento.

**Cambio de referencia.** Una traslación $`w\mapsto w-a`$ transforma las medidas mediante

```math
N_a=N,\qquad S_a=S-aN,\qquad Q_a=Q-2aS+a^2N.
```

La comparación puede desplazarse sin recuperar las soluciones una por una.

## 3. Primer ensayo: cortes tensoriales y signos

La identidad de ocho cuadrados empleada en una construcción de conteo exacto descompone una condición de cruce como suma de dos piezas firmadas, $`R+C=2[x=v][y=u]`$, con cuatro bloques $`x,y,u,v\in\lbrace0,1\rbrace^3`$. Los signos proceden de la multiplicación octoniónica y son parte indispensable de la identidad [1].

El verificador del ensayo C [5] examinó exhaustivamente las $`8^4=4.096`$ cuádruplas. La igualdad se mantuvo al añadir la referencia $`w=|x|+|y|+|u|+|v|`$, donde $`|\cdot|`$ es el peso de Hamming. Los momentos firmados fueron:

| Contribución | $`N`$ | $`S`$ | $`Q`$ |
|---|---:|---:|---:|
| $`2[x=v][y=u]`$ | 128 | 768 | 5.376 |
| Pieza $`R`$ | 64 | 384 | 2.688 |
| Pieza $`C`$ | 64 | 384 | 2.688 |

El valor 128 incluye la multiplicidad 2 de la identidad; corresponde a 64 parejas compatibles. Cada pieza incorpora 224 contribuciones negativas entre sus 512 entradas no nulas. La recuperación exige conservar los signos hasta el cierre.

Los rangos exactos de las matrices de $`64\times64`$, sobre $`\mathbb Q`$, dependen del corte:

| Pieza | Corte $`(x,y)\mid(u,v)`$ | Corte $`(x,u)\mid(y,v)`$ |
|---|---:|---:|
| $`R`$ | 8 | 64 |
| $`C`$ | 64 | 8 |

Así, el rango 8 certifica el número mínimo de términos separados dentro del corte y del modelo lineal correspondiente. El cambio de orientación altera ese mínimo local; la igualdad del conteo final permanece.

En el comparador aritmético del ensayo, una evaluación directa con filtro de paridad requirió 12.288 sumas y multiplicaciones escalares, mientras que la factorización por los cortes favorables requirió 960: una razón de 12,8. Son cuentas de operaciones enteras bajo reglas explícitas, no tiempos de ejecución ni costos completos. Se excluyeron búsquedas, construcción de tablas, gestión de memoria y costos binarios. La identidad y su factorización son antecedentes conocidos; el ensayo acredita el transporte exacto de las medidas durante esa operación.

## 4. Segundo ensayo: recuperación mediante Hermite

El ensayo C [5] examinó una interfaz de interpolación con valores y primeras derivadas de Hasse en $`T=1,2,3`$. Para una fórmula booleana de cinco variables se definió el polinomio de control

```math
H_F(T,u)=\sum_{x\models F}(1+u)^{w(x)}
\prod_{i=1}^{5}(1+Tx_i)\pmod{u^3}.
```

Este polinomio tiene grado a lo sumo cinco en $`T`$; en $`T=0`$ codifica los momentos buscados. Mediante los seis datos seleccionados se obtuvo exactamente

```math
H_F(0,u)=18+51u+57u^2,
\qquad (N,S,Q)=(18,51,165).
```

Para un polinomio arbitrario de grado $`\le5`$ sobre $`\mathbb Q`$, los datos de valor y derivada primera en los tres puntos forman un sistema de Hermite invertible. En ese **conjunto fijo de seis mediciones**, el funcional de recuperación tiene la forma

```math
H(0)=-18H(1)-9D H(1)+9H(2)-18D H(2)+10H(3)-3D H(3),
```

con $`DH(a)=[z]H(a+z)`$. Los seis coeficientes son distintos de cero. Por consiguiente, omitir cualquiera de esos datos impide recuperar $`H(0)`$ para **toda** la familia de polinomios de grado $`\le5`$ empleando exclusivamente los cinco datos restantes. Esta necesidad es relativa a la familia general y a las observaciones fijadas: no establece un mínimo universal para cualquier esquema de medición.

Una familia adicionalmente restringida puede admitir menos datos. Por ejemplo, si $`H(T)=A+BT^2+CT^4`$, entonces

```math
H(0)=\frac32H(1)-\frac35H(2)+\frac1{10}H(3).
```

La reducción requiere demostrar que las relaciones restrictivas son satisfechas por los polinomios producidos por la construcción que se pretende optimizar. El ensayo no acredita esa propiedad para la familia completa de OpenAI, ni reproduce sus sustituciones, módulos, truncamientos y requisitos de precisión [2].

## 5. Condiciones de recuperabilidad y economía

Una representación reducida es válida respecto de una familia de consultas $`\mathcal C`$ cuando las configuraciones que agrupa tienen contribuciones iguales para cada continuación admitida, o cuando la operación de agrupamiento conserva explícitamente la suma firmada o la multiplicidad necesaria para reconstruirlas. Para observaciones lineales $`E`$ y una respuesta lineal $`\ell`$, esta exigencia se expresa mediante

```math
\ker(E|_V)\subseteq\ker(\ell|_V),
```

siendo $`V`$ el espacio de representaciones admitidas. La condición caracteriza la recuperación exacta; reconocer y utilizar las clases puede tener un costo propio.

**Cotas bajo un modelo aritmético.** Si un circuito de tamaño $`T`$ usa únicamente sumas y productos compatibles con el anillo truncado y la referencia se factoriza localmente, su levantamiento de escalares a ternas emplea $`O(T)`$ operaciones escalares, con una constante adicional por operación. En cambio, calcular $`N,S,Q`$ mediante los conteos condicionados $`\#F`$, $`\#(F\land x_i)`$ y $`\#(F\land x_i\land x_j)`$ requiere a lo sumo $`1+n+\binom n2`$ llamadas, además de las sumas para reconstruir los momentos. La comparación $`O(T)`$ frente a $`O(n^2T)`$ se refiere a **esa referencia de llamadas separadas sin reutilización**; no establece una ventaja frente a un contador optimizado que comparta trabajo.

En los ocho ensayos de contracción elemental [3], las medidas se recuperaron exactamente. Para una cadena de diez variables, el transporte conjunto utilizó 1.560 operaciones escalares, frente a 12.320 de las consultas condicionadas contabilizadas de forma independiente, y requirió más componentes simultáneas de memoria. En una deformación cúbica con datos de Hermite, la recuperación de las mismas medidas costó entre 6,35 y 6,52 veces las operaciones de la contracción directa [4]. Estas cifras corresponden a modelos reducidos y no reproducen las recursiones completas de las publicaciones.

La minimización debe incluir operaciones aritméticas, crecimiento del tamaño de los enteros, precisión, tablas de frontera, identificación de equivalencias, memoria y tiempo. Un menor rango o un menor número de posiciones no equivale por sí mismo al menor costo computacional.

## 6. Certificación de posiciones diferentes

Si la proyección produce $`s`$ valores reales distintos $`v_1,\ldots,v_s`$ con multiplicidades positivas $`m_i`$, los momentos completos cumplen $`M_k=\sum_{i=1}^{s}m_iv_i^k`$. La matriz $`\mathcal H_r=(M_{i+j})_{0\le i,j<r}`$ satisface

```math
\operatorname{rango}(\mathcal H_r)=\min(r,s).
```

La factorización de Vandermonde demuestra esa identidad [6], y permite certificar el mínimo número de posiciones de una representación atómica que reproduce todos los momentos. La positividad de las multiplicidades importa: las contribuciones tensoriales intermedias con signo pueden cancelarse, por lo que esta conclusión se aplica directamente a la distribución final no negativa, no a cada término firmado aislado. Los tres primeros momentos, por sí solos, tampoco determinan siempre $`s`$.

## 7. Alcance de los resultados

**Demostrado algebraicamente:** conservación de $`N,S,Q`$ bajo las operaciones compatibles; transformación exacta por cambio de referencia; recuperabilidad mediante seis datos de Hermite para la familia general ensayada; rangos de las dos piezas según el corte; mínimo de posiciones por rango de momentos bajo sus hipótesis.

**Verificado computacionalmente:** 4.096 casos de la identidad firmada, rangos racionales de las cuatro matrices y recuperación exacta de $`(18,51,165)`$. El verificador es reproducible con Python estándar.

**Observado en un comparador definido:** reducción local de 12.288 a 960 operaciones al utilizar la factorización conocida. La relación de costo no constituye una cota de la implementación completa.

**Pendiente de demostración:** preservación de las medidas en cada transformación y en todos los niveles recursivos de los algoritmos publicados, con un análisis de costo de bits y memoria; reducción de datos para las familias efectivamente generadas por la interpolación; identificación eficiente de equivalencias que conserve todas las consultas requeridas.

La extensión de conteos exactos a pesos en álgebras conmutativas, incluidos polinomios generadores, cuenta con un antecedente explícito publicado en octubre de 2026 [7]. Las identidades octoniónicas, la interpolación de Hermite y la factorización de Hankel–Vandermonde también son herramientas anteriores. La contribución sometida a revisión es la **articulación de una referencia, medidas recuperables y certificados de costo bajo condiciones declaradas**, no la atribución de novedad a esas herramientas.

## 8. Pregunta para revisión independiente

**¿Para qué familias de restricciones y qué transformaciones concretas puede certificarse que conservar las diferencias cuantificables respecto de una referencia —incluidos los signos, las multiplicidades y las continuaciones admisibles— reduce el costo total de recuperación, una vez incorporados el reconocimiento de equivalencias, la memoria y la precisión, frente a los mejores procedimientos comparables?**

## 9. Reproducción y fuentes

La carpeta reúne el artículo y los tres ensayos. La nota base revisada v0.2 se conserva en su [entrega propia](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/2026-11-13-medicion-soluciones-eje-v0.2/2026-11-13_medicion_soluciones_desde_un_eje):

| Pieza | Verificador | Qué comprueba |
|---|---|---|
| [Nota base v0.2: medición respecto de un eje](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-13-medicion-soluciones-eje-v0.2/2026-11-13_medicion_soluciones_desde_un_eje/MEDICION_SOLUCIONES_DESDE_UN_EJE.md) | [Verificador](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-13-medicion-soluciones-eje-v0.2/2026-11-13_medicion_soluciones_desde_un_eje/verificar_eje.py) (SymPy) | Newton, Sturm, conteos restringidos y rango de Hankel |
| [Ensayo A: contracción y momentos](ensayo_A_contraccion_y_momentos/INFORME.md) | `ensayo_momentos.py` | Ocho instancias, tres rutas de recuperación y costos |
| [Ensayo B: continuaciones y Hermite](ensayo_B_continuaciones_y_hermite/INFORME.md) | `verificar_paralelo.py` | Clases de continuación, Hermite cúbico y tabla de costos |
| [Ensayo C: cortes y datos de Hasse](ensayo_C_cortes_y_hasse/INFORME.md) | `verificar_transformaciones.py` | 4.096 casos de la identidad firmada, rangos, Hermite de seis datos |

La enumeración exhaustiva aparece como auditoría de identidades o casos reducidos.

[1] Anthropic, *A $`2^{o(n)}`$ Time Algorithm for 3-SAT*, Hexagon, versión 1, 27 de octubre de 2026; identidad de ocho cuadrados en §2.4, ec. (12); piezas $`R`$ y $`C`$ en §4, ecs. (30)–(31); lema 2. https://hexagonmath.org/pdf/2610.00577v1

[2] OpenAI, *The Exponential Time Hypothesis is False*, manuscrito y fuente TeX, revisión del 25 de octubre de 2026; sustituciones e interpolación de Hermite. https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/main_full_version.tex

[3] Ensayo A, *Conservar diferencias entre soluciones: prueba algebraica y ensayo de costo*, 13 de noviembre de 2026, en esta carpeta.

[4] Ensayo B, *Pruebas paralelas: continuaciones y recuperación por Hermite*, 13 de noviembre de 2026, en esta carpeta.

[5] Ensayo C, *Conservar diferencias bajo cambios de corte y recuperación de Hermite*, 13 de noviembre de 2026, en esta carpeta.

[6] Le Matt Ansatz Di Ego, [*Medición de soluciones respecto de un eje* v0.2](https://doi.org/10.5281/zenodo.24213729), 13 de noviembre de 2026.

[7] Deep Bhattacharjee, *Subexponential Weighted Counting and Exact Optimisation*, Hexagon, versión 1, 29 de octubre de 2026; extensión a álgebras conmutativas. https://hexagonmath.org/2610.00594v1

---

**Endless Monkey Project**  
*Relational Geometry Program*
