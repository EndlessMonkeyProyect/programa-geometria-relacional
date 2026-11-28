# Anexo T.1 — Complemento de cierre global y transferencia analítica

**Nota técnica 01 v3.9 / Anexo T.1 v1.4 — Propuesta de extensión**  
28 de noviembre de 2026 · Endless Monkey Project / Relational Geometry Program

## 1. Estatuto y alcance

Se conservan el diccionario libre de cuadrados, la métrica funcional y las identidades de T.1 v1.4. Se demuestran un criterio de recuperación por bloques, una dirección de obstrucción asociada a un cero y una cota direccional óptima de segundo momento. La divergencia global se deduce utilizando RH como teorema externo formalmente verificado según las fuentes citadas, o utilizando la interfaz analítica de la prueba externa. La demostración autónoma de la divergencia, la condición por primo y el entrelazamiento directo de operadores permanecen como problemas de investigación. No se ha ejecutado una compilación Lean en esta revisión.

## 2. Recuperación por bloques (lema B1)

En $H=L^2((0,\infty),dt/t^2)$, sean $e_d(t)=\{t/d\}$, $\chi=1_{[1,\infty)}$, $V_S=\operatorname{span}\{e_d:d\mid\prod_{p\in S}p\}$, $u_S=(I-\Pi_S)\chi$ y $Q_S=\|u_S\|^2$. Sea $S\subset S'$, y $Z=V_{S'}\cap V_S^\perp$.

La identidad de Pitágoras da

$$Q_S-Q_{S'}=\|\Pi_Zu_S\|^2.$$

Si $a\in V_{S'}$ satisface $\|\chi-a\|^2\leq\theta Q_S$, con $0<\theta<1$, entonces $w=(I-\Pi_S)a\in Z$ y

$$\|u_S-w\|^2=\|(I-\Pi_S)(\chi-a)\|^2\leq\theta Q_S.$$

Por optimalidad de la proyección, $Q_{S'}\leq\theta Q_S$. Además, $w\neq0$ y la proyección sobre la recta $\mathbb Rw$ es al menos tan eficaz como el vector $w$:

$$\frac{|\langle u_S,w\rangle|^2}{\|w\|^2}\geq(1-\theta)Q_S.$$

Es decir, un aproximante global genera un testigo de recuperación en la dirección fija del resto heredado, dentro del diccionario original.

Para una cadena de adiciones individuales, en cada bloque $B$,

$$1-\prod_{p\in B}(1-\eta_p)=1-Q_{S'}/Q_S\leq\sum_{p\in B}\eta_p.$$

Si cada bloque reduce $Q$ a la mitad, la suma de las $\eta_p$ en cada bloque es al menos $1/2$. La elección adaptada de profundidad $k_p$ del Teorema 3 de v1.4 asegura $R_{p,k_p}\geq\eta_p/2$; por tanto cada bloque aporta al menos $1/4$ a la serie de reflexiones. Una sucesión infinita de tales bloques equivale a $Q_S\to0$ y a RH por la Proposición 8 de v1.4. En particular, esta es una reformulación y no una demostración autónoma de RH.

## 3. Existencia de bloques por aproximación aritmética (proposición B2)

El resultado de Balazard (Proposición 3.1 en Báez-Duarte, arXiv:math/0205003) da, bajo RH, constantes $c,C>0$ tales que, para $n$ suficientemente grande,

$$a_n=-\sum_{d\leq n}\mu(d)\exp(-c\log d/\log\log n)e_d,\qquad \|\chi-a_n\|^2\leq C(\log\log n)^{-2/3}.$$

Todo coeficiente no nulo tiene índice libre de cuadrados. El aproximante pertenece a $V_{S'}$ en cuanto $S'$ contiene los primos hasta $n$. Para $Q_S>0$, basta escoger $n$ suficientemente grande con $\log\log n\geq(2C/Q_S)^{3/2}$ y alcanzar esa etapa. Las constantes y el umbral asintótico no se han explicitado aquí; la fórmula es una condición suficiente, no un costo computacional certificado.

Se deduce $Q_{S_j}\leq2^{-j}Q_{S_0}$ a lo largo de una subsecuencia adaptada, y la divergencia de $\sum_p\eta_p$ y $\sum_p R_{p,k_p}$. Para la cadena usual ordenada por tamaño, la misma cota implica $\sum_{q\leq p}-\log(1-\eta_q)\geq \tfrac23\log\log\log p-O(1)$. No se deduce de aquí una cota para $R_{p,4}$ por primo ni una tasa uniforme de profundidad.

## 4. Dirección invisible de un cero (proposición B3)

Trabájese en la complexificación de $H$, con producto interno lineal en la primera variable. Sea $\rho=\beta+i\gamma$ un cero de $\zeta$ con $1/2<\beta<1$. Defínase

$$h_\rho(t)=\begin{cases}t/(1-\overline\rho),&0<t<1,\\ t^{1-\overline\rho},&t\geq1.\end{cases}$$

La norma es finita y vale $\|h_\rho\|^2=|1-\rho|^{-2}+(2\beta-1)^{-1}$. Para toda función del diccionario y para $\chi$, lineales en $(0,1)$ (con pendiente cero en el caso de $\chi$), se cumple

$$\langle f,h_\rho\rangle=\int_0^\infty f(t)t^{-\rho-1}\,dt.$$

La identidad clásica de Mellin $\int_0^\infty\{t/d\}t^{-s-1}dt=-d^{-s}\zeta(s)/s$, válida para $0<\Re s<1$, implica $\langle e_d,h_\rho\rangle=0$. En cambio $\langle\chi,h_\rho\rangle=1/\rho$. Así, para todo $S$,

$$\langle u_S,h_\rho\rangle=1/\rho,\qquad Q_S\geq\frac{1/|\rho|^2}{|1-\rho|^{-2}+(2\beta-1)^{-1}}=\frac{(2\beta-1)|1-\rho|^2}{|\rho|^4}>0.$$

La conclusión es una obstrucción direccional explícita. Se trata de una aplicación del mecanismo clásico de Nyman–Beurling/Mellin, sin reclamo de prioridad. La ausencia de estos ceros permite la aproximación de B2 mediante el teorema de Báez-Duarte, no por la sola ausencia de los vectores exhibidos.

## 5. Transferencia analítica externa

La exposición de Rubinstein (v1.5, 27 de noviembre, ecuación 2.9, Teoremas 3.2, 4.1 y 10.3) identifica una interfaz escalar en la versión abreviada de la prueba de Alpöge–Claude. Para evitar confundir su módulo con $Q_S$, escribimos $M=18480$. Para los primos $d\equiv9239\pmod M$, la suma ponderada es

$$F_d(y)=\sum_{n\leq y,\ n\equiv1\ (\mathrm{mod}\ M)}\Lambda(n)(1-\chi_d(n))(1/n-1/y).$$

Con la constante $c_d$ especificada en esa fuente, el resto es $E_d(y)=F_d(y)-\log(y)/\varphi(M)-c_d$. La entrada externa es la cota unilateral $E_d(y)\leq y^{-1/2+\epsilon}$ eventualmente para cada $d,\epsilon>0$, junto con la elección de un twist auxiliar sin ceros en una caja fija a la derecha de la línea crítica. El argumento de Landau y la reducción analítica de Rubinstein excluyen un cero de $\zeta$ en esa caja. La ecuación funcional da RH. Aplicando B2 se obtienen los testigos aritméticos por bloques y la divergencia adaptada de T.1.

La cadena es: insumos automorfos externos → desigualdad escalar → exclusión de ceros → aproximación libre de cuadrados → testigo de bloque → divergencia. El resultado formal externo RH tiene verificaciones públicas; la exposición clásica consultada todavía remite los teoremas automorfos A, B y C a la prueba formal. No se ha reconstruido aquí dicha prueba. Esta transferencia es de consecuencias matemáticas, no una identificación de operadores o de retículos.

## 6. Precisión del problema de segundo momento (lema B4)

Sea $A\geq0$ sobre un espacio de dimensión $D\geq2$, $s=\operatorname{tr}A>0$, $\delta=D\operatorname{tr}(A^2)/s^2-1$. Para todo vector unitario $y$, con $B=A-(s/D)I$, se tiene

$$|\langle y,By\rangle|\leq\|B\|_{HS}\,\|yy^*-I/D\|_{HS}=\frac{s}{D}\sqrt{(D-1)\delta}.$$

Aquí se usa $\operatorname{tr}B=0$ y Cauchy–Schwarz de Hilbert–Schmidt. En consecuencia, la cota inferior para $\langle y,Ay\rangle$ es $(s/D)\max(0,1-\sqrt{(D-1)\delta})$, y la superior es $(s/D)(1+\sqrt{(D-1)\delta})$. Para $D=1$ la forma es escalar exacta.

El umbral de positividad es óptimo en general: $A=\operatorname{diag}(0,D/(D-1),\ldots,D/(D-1))$ tiene $s=D$, $\delta=1/(D-1)$ y anula $y=e_1$, aunque su corango relativo es $1/D$. Esto delimita por qué un control medio de rango/segundo momento no garantiza por sí solo la dirección del resto.

Con las notaciones de §5 de v1.4, basta una comparación escalar en $y=Uc$ (no es necesario el orden de Loewner global): $\langle y,Ay\rangle\leq\langle c,M^{-1}c\rangle$ para la ruta inversa, o $\langle c,Mc\rangle\leq\langle y,Ay\rangle$ para la ruta directa. En la segunda, la cota testigo da $\Delta Q\geq\|c\|^4/\langle y,Ay\rangle$. La construcción aritmética de tal mapa y las constantes requeridas para una suma divergente son todavía una obligación distinta de la transferencia analítica de §5.

## 7. Control finito y decisión editorial

Usando los valores de Q del JSON de v1.4 y formando bloques en el primer momento en que Q cae a la mitad, se obtienen cuatro bloques completos:

| Inicio | Fin | Q final / Q inicial | Suma de eta |
|---|---:|---:|---:|
| vacío | 2 | 0.337871 | 0.662129 |
| 2 | 3 | 0.266187 | 0.733813 |
| 3 | 5 | 0.482780 | 0.517220 |
| 5 | 13 | 0.483395 | 0.632633 |

El bloque que comienza después de 13 está incompleto en 17 (cociente 0.729224). Los valores son una relectura de los resultados en doble precisión; no son un certificado asintótico.

**Incorporación propuesta:** añadir este complemento junto a v1.4; no sustituir el expediente ni marcar la transferencia directa de operadores o una prueba autónoma como completadas. Distinguir: (a) identidades y lemas demostrados; (b) cierre por transferencia de un resultado externo; (c) estimaciones internas por etapa y mapa automorfo específico pendientes.

## Referencias

- Anexo T.1 v1.4, §§5, 7–8, Proposición 8 y Teorema 3, paquete del programa (28 nov. 2026).
- L. Báez-Duarte, [A strengthening of the Nyman-Beurling criterion](https://arxiv.org/abs/math/0202141), 2002/2003.
- L. Báez-Duarte, [A strengthening …, 2](https://arxiv.org/abs/math/0205003), 2002, Proposición 3.1 (M. Balazard).
- M. O. Rubinstein, [An outline of the shortened proof of the Riemann hypothesis](https://math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/rh-outline.pdf), v1.5, 27 nov. 2026; [página de seguimiento](https://math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/).
- Lean/Mathlib, [verificación comunitaria](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), 21 nov. 2026.
- A. Sutherland, MIT, [verificación original](https://math.mit.edu/~drew/grh/) y [versión abreviada](https://math.mit.edu/~drew/shortgrh/), consultadas el 28 nov. 2026. Versión abreviada: commit 72fead102f663d5c7a407964a13dc0cf9d977207, Lean 4.35.0, según el registro externo.
