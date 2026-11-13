---
title: "Medición de soluciones respecto de un eje"
subtitle: "Momentos, conteos restringidos y rango de Hankel para representaciones mínimas"
author: "Le Matt Ansatz Di Ego — Endless Monkey Project · Relational Geometry Program"
date: "13 de noviembre de 2026"
lang: es-CR
---

**Nota matemática de investigación — versión 0.2 para revisión técnica**

## Resumen

Esta nota mide distribuciones de soluciones proyectadas sobre una recta de valores y comparadas con una referencia escalar. En el laboratorio polinómico, las identidades de Newton recuperan momentos de raíces reales a partir de coeficientes y el teorema de Sturm cuenta raíces en intervalos. En el laboratorio booleano, conteos exactos con variables fijadas recuperan los momentos de órdenes cero, uno y dos. La factorización de Hankel–Vandermonde certifica el mínimo de posiciones de una medida atómica positiva a partir de una secuencia suficiente de momentos. Dos pares de ejemplos verifican estas identidades. La nota organiza una agenda de investigación sobre reutilización de consultas y costos de reconstrucción en algoritmos de conteo exacto.

**Pregunta:** ¿qué magnitudes de una distribución de soluciones se recuperan desde una referencia escalar, qué consultas las distinguen y qué secuencia de momentos certifica el mínimo de posiciones de su representación?

## 1. Referencia, objeto y alcance

La *referencia* fija la comparación y la proyección $w$ asigna un valor real a cada solución. La *diferencia* expresa la variación de esos valores; la *distinción* se acredita mediante la primera consulta de momentos que separa dos distribuciones, definida en la sección 2. La *herencia* describe la procedencia lógica de los conteos restringidos de la sección 4. La *conservación* expresa la recuperación de una magnitud a partir de relaciones declaradas. La *economía* compara recursos entre procedimientos que cumplen la misma tarea y el mismo requisito de exactitud.

En esta nota $w$ define la recta de valores de la proyección, y $a$ es una referencia escalar en esa recta. En el laboratorio polinómico, cada raíz real se indexa según su multiplicidad; en el booleano, cada asignación satisfactoria aparece una vez. Esta convención permite emplear las mismas fórmulas de momentos para ambas clases de soluciones.

## 2. Un eje para cuantificar una distribución de soluciones

Sea $K$ un conjunto finito y no vacío de índices de soluciones, y $w:K\to\mathbb R$ una proyección definida por las relaciones del sistema. Los índices permiten contar raíces repetidas con su multiplicidad. Sea $a\in\mathbb R$ la referencia escalar escogida. Definimos los momentos

$$M_j(K,w)=\sum_{x\in K} w(x)^j,\qquad j\ge0,$$

con $M_0=|K|$. La medida de dispersión respecto del eje $a$ es

$$J_K(a)=\frac1{M_0}\sum_{x\in K}(w(x)-a)^2
=\frac{M_2}{M_0}-2a\frac{M_1}{M_0}+a^2.$$

**Proposición 1 (eje cuadrático óptimo).** El valor que minimiza $J_K(a)$ es

$$a_* =\frac{M_1}{M_0},\qquad
J_K(a_*)=\frac{M_2}{M_0}-\left(\frac{M_1}{M_0}\right)^2.$$

**Prueba.** Completar el cuadrado da $J_K(a)=J_K(a_*)+(a-a_*)^2$. $\square$

El mínimo describe la **dispersión de las posiciones** para la proyección elegida. Su costo de cálculo se determina para cada procedimiento concreto.

Dos sistemas pueden compartir los primeros momentos y distinguirse en órdenes superiores. Para dos distribuciones $A$ y $B$ con la misma referencia, definimos el *primer orden de distinción por momentos* como

$$\delta_w(A,B)=\min\{j\ge0:M_j(A,w)\ne M_j(B,w)\},$$

cuando el conjunto no está vacío. Si las medidas atómicas son idénticas, escribimos $\delta_w=\infty$. Esta cantidad registra el **primer orden de momento** que distingue las distribuciones proyectadas.

## 3. Raíces reales mediante Newton y Sturm

Sea $P(z)=z^d+c_1z^{d-1}+c_2z^{d-2}+\dots+c_d$ mónico, con todas sus raíces **reales**, contadas con multiplicidad. Sus sumas de potencias $p_j=\sum_{i=1}^d r_i^j$ se obtienen de los coeficientes mediante las identidades de Newton. En particular,

$$p_1=-c_1,\qquad p_2=c_1^2-2c_2.$$

El eje de menor dispersión cuadrática de las raíces es $a_*=-c_1/d$, y su suma de distancias cuadráticas es

$$\sum_i(r_i-a_*)^2=p_2-\frac{p_1^2}{d}.$$

Para raíces complejas, la suma algebraica $(r_i-a)^2$ y la suma de distancias euclidianas $|r_i-a|^2$ expresan magnitudes diferentes. La lectura de dispersión cuadrática de esta sección corresponde a raíces reales.

**Control exacto.** Consideramos

$$P_1(z)=z^4-10z^2+9,\qquad P_2(z)=z^4-10z^2+16.$$

| Magnitud obtenida sin listar raíces | $P_1$ | $P_2$ |
|:--|--:|--:|
| Número de raíces reales (con multiplicidad) | 4 | 4 |
| Eje $a_*$ | 0 | 0 |
| $p_2$ | 20 | 20 |
| $p_4=200-4c_4$ | 164 | 136 |
| Raíces en $(-5/4,5/4)$, por Sturm | 2 | 0 |

Así, $\delta(P_1,P_2)=4$: coinciden en los momentos de orden $0,1,2,3$ y se distinguen en el cuarto. El conteo de raíces dentro de un radio concreto también distingue las distribuciones. Las identidades de Newton y el teorema de Sturm proporcionan estas medidas sin calcular explícitamente las raíces.

## 4. Momentos booleanos mediante conteos restringidos

Sea $F$ una fórmula booleana con $n$ variables y $K_F=\{x\in\{0,1\}^n:F(x)=1\}$. Elegimos el eje de comparación

$$w(x)=\sum_{i=1}^n \alpha_i x_i,\qquad \alpha_i\in\mathbb Z,$$

que mide una propiedad declarada de cada solución. Para el peso de Hamming, $\alpha_i=1$. Definimos los conteos restringidos

$$N=\#F,\quad A_i=\#(F\wedge x_i),\quad B_{ij}=\#(F\wedge x_i\wedge x_j).$$

En notación de restricciones, $x_i$ significa $x_i=1$; $B_{ij}$ solo se usa para $i<j$.

**Proposición 2 (primeros dos momentos sin enumeración).** Para $w(x)=\sum_i\alpha_ix_i$ se tiene

$$M_0=N,\quad M_1=\sum_i\alpha_i A_i,$$

$$M_2=\sum_i\alpha_i^2 A_i+2\sum_{i<j}\alpha_i\alpha_jB_{ij}.$$

Por tanto, si $N>0$, el eje $a_*=M_1/N$ y la dispersión mínima $J_K(a_*)$ se obtienen con a lo sumo

$$1+n+\binom n2$$

consultas de conteo exacto de fórmulas restringidas, más aritmética racional.

**Prueba.** En cada asignación booleana, $x_i^2=x_i$. Expandir $w(x)$ y $w(x)^2$ e intercambiar las sumas sobre soluciones produce las dos igualdades. $\square$

Estas identidades reducen la obtención de los tres primeros momentos a consultas de conteo exacto y aritmética racional. El costo total incorpora cada consulta y la aritmética. Si $N=0$, el conteo certifica incompatibilidad; para $N>0$, se definen el eje normalizado y la dispersión.

**Ejemplos comprobados.** Sobre $x_1,x_2,x_3$:

$$F_A=(x_1\oplus x_2\oplus x_3=0)\land(x_1\lor x_2\lor x_3),$$

$$F_B=(\neg x_1)\land(\neg x_2\lor x_3).$$

Ambas admiten tres soluciones. Proyectamos mediante $w=x_1+x_2+x_3$.

| Medida | $F_A$ | $F_B$ |
|:--|--:|--:|
| $M_0$ (soluciones) | 3 | 3 |
| $M_1$ | 6 | 3 |
| $M_2$ | 12 | 5 |
| Eje óptimo $a_*$ | 2 | 1 |
| Dispersión mínima $J(a_*)$ | 0 | $2/3$ |
| Posiciones distintas observadas | 1 | 3 |

Las funciones generadoras de posiciones son

$$G_A(t)=3t^2,\qquad G_B(t)=1+t+t^2.$$

Los **coeficientes** de $G$ registran multiplicidades en cada posición $w$. Las raíces de $G(t)$ caracterizan el polinomio generador; en el primer laboratorio, las raíces de $P(z)$ son las soluciones de la ecuación.

## 5. Un mínimo exacto: el rango de momentos

Agrupemos las soluciones por su posición real $v_j=w(x)$; supongamos $s$ posiciones distintas $v_1,\dots,v_s$ con multiplicidades positivas $m_j$. Entonces

$$M_k=\sum_{j=1}^s m_jv_j^k.$$

Formamos la matriz de Hankel de tamaño $r$:

$$\mathcal H_r=(M_{i+j})_{0\le i,j<r}.$$

**Teorema 3 (mínimo de posiciones).** Para una distribución atómica real finita con multiplicidades positivas y $s$ posiciones distintas,

$$\operatorname{rango}(\mathcal H_r)=\min(r,s).$$

En consecuencia, $s$ es el **número mínimo de posiciones atómicas** de cualquier representación que reproduzca todos los momentos de la distribución.

**Demostración.** Sea $V_r$ la matriz de Vandermonde con entradas $(V_r)_{ij}=v_j^i$. Entonces

$$\mathcal H_r=V_r\,\operatorname{diag}(m_1,\dots,m_s)\,V_r^{\mathsf T}.$$

Como los $v_j$ son distintos y todos los $m_j>0$, la matriz tiene rango $\min(r,s)$. Cualquier representación mediante $s'$ posiciones produce matrices de Hankel de rango a lo sumo $s'$; por tanto requiere $s'\ge s$. Las $s$ posiciones originales alcanzan esa cota. $\square$

La factorización clásica de Hankel–Vandermonde proporciona un certificado del **mínimo de posiciones de la distribución proyectada**. La referencia escalar organiza la medida de dispersión.

Para certificar $s$ con una secuencia finita de momentos se forman matrices de Hankel de tamaño creciente hasta observar rango menor que el tamaño, o se usa una cota superior conocida para $s$. La Proposición 2 proporciona $M_0,M_1,M_2$; la certificación general incorpora los momentos de orden superior que requiera la distribución.

**Comprobación.** Para $F_A$, los momentos $M_0,\dots,M_4$ son $(3,6,12,24,48)$ y la matriz $\mathcal H_3$ tiene rango $1$. Para $F_B$ son $(3,3,5,9,17)$ y

$$\mathcal H_3(F_B)=\begin{pmatrix}3&3&5\\3&5&9\\5&9&17\end{pmatrix},\quad
\det\mathcal H_3(F_B)=4,\quad \operatorname{rango}=3.$$

Por tanto, las soluciones del primer sistema se representan mediante una posición de la proyección con multiplicidad tres, mientras que el segundo requiere tres posiciones distintas para reproducir todos sus momentos. El valor $s$ mide el tamaño mínimo del soporte de la **distribución proyectada**. El costo de un algoritmo de conteo se evalúa por sus consultas, aritmética y reconstrucción.

## 6. Aplicaciones a algoritmos de conteo exacto

La Proposición 2 emplea consultas de conteo $\#(F\wedge C)$, donde $C$ fija una o dos variables. Esas restricciones producen instancias compatibles con cualquier contador exacto de #SAT que las admita. Los preprints citados de Anthropic y OpenAI describen, bajo sus hipótesis, contadores para fórmulas de anchura fija. Si cada consulta tiene cota $T(n,m)$ en la familia considerada, la recuperación de $M_0,M_1,M_2$ utiliza a lo sumo $O(n^2)$ llamadas y aritmética racional. Cuando $T(n,m)=2^{o(n)}$, el total conserva una cota subexponencial.

Una línea de trabajo examina la reutilización de contracciones parciales en la construcción tensorial de Anthropic. Otra estudia qué datos auxiliares de una construcción por interpolación de OpenAI permiten recuperar momentos de consultas relacionadas. La comparación medirá el costo de reconocimiento, consultas, reutilización y reconstrucción.

El polinomio generador $G_F(t)$ codifica multiplicidades por posición. El polinomio auxiliar $H(T)$ de una construcción por interpolación de OpenAI codifica una deformación algebraica. Una conexión formal entre ambos se expresará mediante una transformación explícita y un teorema de recuperación. El polinomio del primer laboratorio representa soluciones como **raíces** de una ecuación.

## 7. Resultados demostrados y programa de investigación

**Resultados exactos:** centro y dispersión óptimos desde momentos; identidades de Newton para raíces reales; conteos de intervalos mediante Sturm; recuperación de los primeros dos momentos booleanos por conteos restringidos; mínimo de posiciones desde el rango de Hankel. Los ejemplos y las cuentas se comprobaron con aritmética exacta.

**Programa de investigación:** identificar familias concretas de #SAT en las que una secuencia de momentos se obtenga y actualice mediante consultas reutilizables. La comparación de procedimientos incluirá el costo de reconocer relaciones, las consultas auxiliares, la precisión requerida y la reconstrucción. Se registrará el orden de momento necesario para certificar cada soporte.

**Pregunta para revisión técnica.** Para clases concretas de #SAT, ¿qué subespacios de momentos se recuperan con una familia suficiente de consultas y cuál es el costo total de reconocerla y mantenerla bajo nuevas restricciones?

## Fuentes y verificación

- *¿Cómo se cuantifica la información de un sistema?* Documento rector, 12-XI-2026.
- *Una misma pregunta, tres mecanismos*. Comparación entre representaciones, 12-XI-2026.
- Anthropic, *A $2^{o(n)}$ Time Algorithm for 3-SAT* (preprint v1, 2026), [texto](https://hexagonmath.org/pdf/2610.00577v1).
- OpenAI, *The Exponential Time Hypothesis is False* (preprint, 25-X-2026), [repositorio](https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026).
- Antecedentes matemáticos: identidades de Newton, teorema de Sturm, matrices de momentos de Hankel y factorización de Vandermonde.
- Verificador adjunto `verificar_eje.py`: identidades exactas de Newton, conteos de Sturm, conteos restringidos, dispersión y rangos de Hankel. La enumeración de ocho asignaciones audita las fórmulas de los ejemplos booleanos.

**Le Matt Ansatz Di Ego**  
*Endless Monkey Project · Relational Geometry Program*
