---
title: "Generación, herencia y composición aritmética"
subtitle: "Puentes exactos entre R–03, HC–02/HC–03, los acarreos y dos enfoques analíticos de Riemann"
author: "Endless Monkey Project / Relational Geometry Program"
date: "22 de noviembre de 2026"
lang: es-CR
abstract: |
  Se integran resultados aritméticos y funcionales documentados entre el 20 y el 22 de noviembre de 2026. La suma ponderada de von Mangoldt permite recuperar cada incorporación prima mediante una segunda diferencia exacta. La factorización binomial transforma esas mismas incorporaciones en activaciones de acarreo y una desviación conjunta, ligada por identidad a dos escalas de la función de Chebyshev. Una identidad de ventanas conecta el observable ponderado con la integral de la discrepancia. Se cuantifica además el costo de recuperar coeficientes desde datos aproximados. La comparación con una prueba formal publicada en Lean y con una construcción de operadores espectrales conserva el alcance específico de cada procedimiento. Los resultados proceden de identidades clásicas y de nuevas formulaciones de correspondencia y condicionamiento dentro del marco de referencias.
---

**Nota técnica de integración · Versión 1.0 · Manuscrito para revisión matemática**

## 1. Objetivo y procedencia

La organización de *aparición $\to$ referencia $\to$ herencia $\to$ composición $\to$ residuo $\to$ control de escala* reúne cuatro expresiones aritméticas: (i) incorporación de potencias primas, (ii) sumas ponderadas de von Mangoldt, (iii) acarreos en coeficientes binomiales y (iv) transformadas de discrepancias de criba.

Se emplean como antecedentes los documentos R–01/R–02 (17-XI), R–03 (18-XI), HC–02 y HC–03 (21-XI), las comparaciones R–03/Alpöge (20–21-XI), la auditoría de correspondencias con Masullo (21-XI) y *Referencia, composición, residuo y control de escala* (22-XI). Las identidades clásicas se atribuyen a la teoría de números analítica y al álgebra de operadores; la aportación de esta nota consiste en fijar sus interfaces y la estabilidad de los cambios de representación.

La comunidad Lean/Mathlib certificó el 21 de noviembre de 2026 el enunciado y el término de prueba de RH publicado en la biblioteca Lean de Alpöge, según su declaración conjunta [A2]. Su explicación matemática convencional y la identificación del mecanismo concreto utilizado en cada módulo se estudian por separado. El manuscrito de Masullo es una propuesta espectral publicada para examen [M1].

## 2. Notación y sistema de observables

Para $n\ge2$ defínanse

$$
\Lambda(n)=\begin{cases}\log p,&n=p^j,\quad j\ge1,\\0,&\text{en otro caso},\end{cases}
\qquad
\psi(x)=\sum_{n\le x}\Lambda(n),\qquad E(x)=\psi(x)-x.
\tag{1}
$$

Para $x\ge1$, el observable ponderado y el centrado son

$$
T(x)=\sum_{n\le x}\Lambda(n)\left(\frac{x}{n}-1\right),\qquad
G(x)=T(x)-x(\log x-1-\gamma),
\tag{2}
$$

con $\gamma$ constante de Euler. La sumatoria incluye las potencias primas en el punto de entrada $n=p^j$ y la posterior contribución del peso de rampa $x/n-1$.

Para una potencia prima $q=p^j$, defínanse

$$
c_q(m)=\left\lfloor\frac{2m}{q}\right\rfloor-2\left\lfloor\frac mq\right\rfloor,
\quad \alpha_q=\frac{\lfloor q/2\rfloor}{q},\quad
S(m)=\sum_{p^j\le m}\big(c_{p^j}(m)-\alpha_{p^j}\big)\log p.
\tag{3}
$$

El número $c_q(m)$ es $0$ o $1$ y registra el acarreo de $m+m$ módulo $q$.

## 3. Incorporación local recuperada por diferencias

**Proposición 1 (recuperación local exacta).** Para cada entero $n\ge2$,

$$
\boxed{\Delta^2T(n):=T(n+1)-2T(n)+T(n-1)=\frac{\Lambda(n)}n.}
\tag{4}
$$

*Prueba.* Fijado $k$, la contribución de $\Lambda(k)$ a $T(x)$ es $\Lambda(k)\max\{x/k-1,0\}$. Para $k<n$ es lineal en los tres puntos $n-1,n,n+1$ y su segunda diferencia es cero; para $k>n$ es cero en los tres puntos, incluso cuando $k=n+1$; para $k=n$ las contribuciones son $0,0,\Lambda(n)/n$. La suma finita de segundas diferencias da (4). $\square$

Como $\log r(n)=\Lambda(n)$ para $r(n)=\operatorname{mcm}(1,\ldots,n)/\operatorname{mcm}(1,\ldots,n-1)$, la cadena de recuperación también admite la forma

$$
\boxed{n\Delta^2T(n)=\Lambda(n)=\log r(n).}
\tag{5}
$$

Esta identidad enlaza la regla de primera aparición de R–01/R–02 con la codificación analítica de HC–03.

**Proposición 2 (estabilidad de la recuperación).** Si $\widetilde T(k)$ aproxima a $T(k)$ con error absoluto a lo sumo $\varepsilon$ en $k=n-1,n,n+1$, entonces

$$
\boxed{\left|n\Delta^2\widetilde T(n)-\Lambda(n)\right|\le4n\varepsilon.}
\tag{6}
$$

La constante $4n$ es óptima frente a errores arbitrarios de magnitud $\varepsilon$ en esos tres puntos.

*Prueba.* La desigualdad triangular aplicada a los coeficientes $1,-2,1$ da $n(1+2+1)\varepsilon$. Se alcanza al tomar errores $+\varepsilon,-\varepsilon,+\varepsilon$. $\square$

La recuperación exacta es un operador local de tres muestras; su condicionamiento absoluto determina una exigencia cuantitativa de precisión cuando crece la escala.

## 4. Composición en dos escalas y desbalance de acarreos

Sea $C(m)=\binom{2m}{m}$ y $H_{\rm imp}(m)=\sum_{\substack{p\text{ impar},\,j\ge1\\ p^j\le m}}\log p/p^j$.

**Proposición 3 (puente exacto: observable local y acarreo global).** Para cada entero $m\ge1$,

$$
\boxed{\log C(m)=\sum_{n=2}^{2m}n\Delta^2T(n)\left(\left\lfloor\frac{2m}{n}\right\rfloor-2\left\lfloor\frac mn\right\rfloor\right).}
\tag{7}
$$

Además,

$$
\boxed{S(m)=\log C(m)-\psi(2m)+\frac12\psi(m)+\frac12H_{\rm imp}(m).}
\tag{8}
$$

En particular, (8) puede escribirse exclusivamente con segundas diferencias:

$$
\boxed{\begin{aligned}
S(m)={}&\log C(m)-\sum_{n=2}^{2m}n\Delta^2T(n)\\
&+\frac12\sum_{n=2}^{m}n\Delta^2T(n)
+\frac12\sum_{\substack{2\le n\le m\\n\text{ impar}}}\Delta^2T(n).
\end{aligned}}
\tag{9}
$$

*Prueba.* Por la fórmula de Legendre, el exponente de un primo $p$ en $C(m)$ es la suma de $\lfloor2m/p^j\rfloor-2\lfloor m/p^j\rfloor$ sobre sus potencias. La ecuación (5) sustituye cada $\log p$ por $n\Delta^2T(n)$, y demuestra (7). Para $p^j>m$ y $p^j\le2m$, el acarreo vale $1$; la contribución es $\psi(2m)-\psi(m)$. Para $p=2$, $\alpha_{2^j}=1/2$; para los primos impares, $\alpha_{p^j}=1/2-1/(2p^j)$. Restar las frecuencias $\alpha_{p^j}$ da (8). Sustituir de nuevo $\Lambda(n)=n\Delta^2T(n)$ da (9). $\square$

**Corolario 3.1 (drift y error de Chebyshev).** Cuando $m\to\infty$,

$$
\boxed{S(m)-\left(2\log2-\frac32\right)m
=-E(2m)+\frac12E(m)+O(1).}
\tag{10}
$$

*Prueba.* Stirling proporciona $\log C(m)=2m\log2-\frac12\log(\pi m)+O(m^{-1})$; la fórmula clásica de Mertens junto con la convergencia de las contribuciones de potencias superiores da $H_{\rm imp}(m)=\log m+O(1)$. Sustituir $\psi(x)=x+E(x)$ en (8) cancela los términos logarítmicos, resultando (10). $\square$

La identidad (10), junto al criterio clásico de von Koch y la iteración diádica de $E(2m)$, establece la equivalencia

$$
\boxed{\mathrm{RH}\iff
S(m)-\left(2\log2-\frac32\right)m=O(\sqrt m\log^2m).}
\tag{11}
$$

**Prueba de la dirección de recuperación.** La cota sobre $S$ y (10) implican $E(2m)=\frac12E(m)+O(\sqrt m\log^2m)$. La diferencia $E(2m+1)-E(2m)=\Lambda(2m+1)-1=O(\log m)$ lleva la misma recurrencia a índices impares. Iterar a través de $\lfloor n/2\rfloor$ produce una serie geométrica, dominada por $O(\sqrt n\log^2n)$; la extensión de enteros a reales utiliza $\psi(x)=\psi(\lfloor x\rfloor)$. Von Koch concluye la dirección inversa. La dirección RH hacia la cota se sigue directamente del mismo criterio aplicado a (10). $\square$

La ecuación (11) fija de forma precisa el objetivo de control global de las activaciones: una desviación centrada que se mide a la escala $\sqrt m\log^2m$.

## 5. Ventanas de escala como observables integrados

**Proposición 4 (identidad exacta de ventanas).** Para $1\le a<b$,

$$
\boxed{\frac{T(b)}b-\frac{T(a)}a
=\int_a^b\frac{\psi(t)}{t^2}\,dt.}
\tag{12}
$$

De manera equivalente,

$$
\boxed{\frac{T(b)}b-\frac{T(a)}a-\log\frac ba
=\int_a^b\frac{E(t)}{t^2}\,dt.}
\tag{13}
$$

*Prueba.* La contribución de $\Lambda(n)$ a $T(x)/x$ es $\Lambda(n)(1/n-1/x)$ para $x\ge n$, que coincide con $\Lambda(n)\int_n^x t^{-2}dt$. Al sumar y permutar la suma finita con la integral, se obtiene $T(x)/x=\int_1^x\psi(t)t^{-2}dt$. Restar los valores en $b$ y $a$ da (12); descomponer $\psi(t)=t+E(t)$ da (13). $\square$

Las ecuaciones (4), (10) y (13) proporcionan tres niveles enlazados: **coeficiente individual**, **discrepancia entre dos escalas** y **promedio ponderado sobre una ventana**. La formulación local recupera toda la información discreta; la ventana ofrece una consulta integrada que responde a una ley de conservación distinta.

### 5.1. Correspondencia con la prueba formal de Alpöge

El observable de (2) es el mismo $T$ usado en las comparaciones R–03/Alpöge y su versión centrada $G$ [D2, D3]. Sus extensiones a caracteres de Dirichlet son

$$
T_\chi(x)=\sum_{n\le x}\Lambda(n)\chi(n)\left(\frac xn-1\right),\qquad
\boxed{\Delta^2T_\chi(n)=\frac{\Lambda(n)\chi(n)}n.}
\tag{14}
$$

Las descomposiciones en primos ordinarios y potencias superiores se heredan término a término; las estimaciones en caracteres exigen las normas y los cuantificadores del argumento correspondiente. Las notas técnicas previas [D2, D3] describen una cota superior unilateral en familias de ventanas $[Y,Y^{3/2}]$ para combinaciones positivas de funciones centradas y torcidas. La construcción formal que suministra esa cota utiliza técnicas aritméticas y automórficas cuyo alcance es adicional a las identidades (4)–(14). El certificado computacional de Lean [A2] corresponde a esa biblioteca externa.

## 6. Transformada de Mellin de la discrepancia (R–03)

Sea $P$ un conjunto *finito* de primos, $M_P=\prod_{p\in P}p$, $\delta_P=\prod_{p\in P}(1-1/p)$, $A_P(x)=\#\{1\le n\le x:(n,M_P)=1\}$ y $D_P(x)=A_P(x)-\delta_P x$.

Para $0<\Re s<1$, la integral

$$
F_P(s)=\int_0^\infty D_P(x)x^{-s-1}\,dx
=\frac{\zeta(s)}s\prod_{p\in P}(1-p^{-s})
\tag{15}
$$

converge absolutamente. En la franja crítica los factores $1-p^{-s}$ son no nulos y conservan los ceros y multiplicidades de $\zeta$. Para $\Re s>1$ se utiliza la continuación meromorfa del miembro derecho. Por diferenciación logarítmica,

$$
\boxed{-\frac{\zeta'(s)}{\zeta(s)}
=-\frac{F_P'(s)}{F_P(s)}-\frac1s
+\sum_{p\in P}\frac{\log p}{p^s-1}.}
\tag{16}
$$

La parte restante es

$$
-\frac{F_P'}{F_P}-\frac1s
=\sum_{p\notin P}\sum_{j\ge1}\frac{\log p}{p^{js}},\qquad \Re s>1.
\tag{17}
$$

La relación entre (17), las potencias primas que aparecen en $T(x)$ y los acarreos de (7) es una identidad de datos aritméticos bajo representaciones diferentes. El cambio de representación se compone de operaciones explícitas: producto de Euler, derivada logarítmica, suma de von Mangoldt, diferencia finita y activación modular.

## 7. Contraste operatorio con la propuesta de Masullo

En $H_0=L^2((0,\infty),dx/x)$, sea $Jf(x)=f(1/x)$ y $T_p f(x)=f(x)-f(x/p)$, $P_p f(x)=f(x)-f(px)$ para $p>1$.

**Proposición 5 (conjugación y estructura espectral).** Se cumple

$$
\boxed{J^2=I,\qquad JT_pJ=P_p.}
\tag{18}
$$

El operador $J$ es unitario en $H_0$. Los operadores $T_p$ y $P_p$ tienen núcleo trivial e imagen densa, pero no cerrada en $H_0$.

*Prueba.* La sustitución $x\mapsto1/x$ preserva la medida $dx/x$ y establece (18). Bajo $u=\log x$, $T_p$ corresponde al multiplicador de Fourier $1-e^{-i\xi\log p}$ (según la convención de signos). Sus ceros forman un conjunto discreto, de medida cero; por ello el núcleo es trivial y la imagen es densa. El multiplicador se aproxima a cero en entornos de esos puntos, de modo que el operador no está acotado inferiormente. La imagen de un operador inyectivo y acotado de Hilbert sería cerrada solamente si su inversa en esa imagen fuera acotada; por tanto, la imagen no es cerrada. La conjugación traslada la conclusión a $P_p$. $\square$

Esta proposición fija una correspondencia exacta entre operadores de diferencia. Para el espacio $L^2(dt)$ del criterio funcional de Báez-Duarte, el operador unitario adaptado es $Uf(t)=t^{-1}f(1/t)$; en esa norma la transformación de $T_p$ adquiere un factor de dilatación. Por eso el análisis comparativo con espacios de Hardy–Sobolev y espacios localmente convexos de la propuesta espectral [M1, D4] se formula junto con su topología.

## 8. Contrato de composición y economía de información

Sea $X$ un monoide, $O:X\to Y$ una consulta y $x\sim_O y$ cuando $O(uxv)=O(uyv)$ para todos los contextos $u,v\in X$. Esta relación es una congruencia; el cociente conserva exactamente las distinciones recuperables mediante continuaciones. La formulación se utiliza en la línea de recierre contextual asociada a P frente a NP y proporciona un patrón de comparación:

- **Consulta:** coeficiente $\Lambda(n)$, error $E(x)$, cero espectral o respuesta de una instancia.
- **Referencia:** lista de potencias primas, conjunto finito $P$, observables $T,F_P$ o firma de frontera.
- **Composición:** ampliación de la escala, multiplicación, operación de diferencia o continuación.
- **Residuo:** acarreo modular, discrepancia, información contextual adicional.
- **Costo:** tamaño de referencia, estabilidad de inversión, norma y costo de actualizar la respuesta.

Las fórmulas (6) y (18) muestran que una igualdad estructural puede coexistir con un condicionamiento cuantitativo específico del espacio y la escala. Esta es la conexión operativa con los estudios sobre P vs NP y Yang–Mills documentados en el marco transversal [D5].

### 8.1. Continuaciones y congruencia observacional

**Proposición 6 (estabilidad de las clases de referencia).** La equivalencia $x\sim_O y$ definida por la igualdad de observaciones en todos los contextos es una congruencia: si $x\sim_O y$, entonces $axb\sim_O ayb$ para cualquier $a,b\in X$.

*Prueba.* Para todo $u,v\in X$, por asociatividad, $O(u(axb)v)=O((ua)x(bv))=O((ua)y(bv))=O(u(ayb)v)$. La igualdad demuestra la compatibilidad de la relación con la composición. $\square$

Esta propiedad aporta una referencia suficiente respecto de una familia declarada de consultas; su costo operativo se determina mediante el algoritmo que construye y actualiza las clases.

### 8.2. Un residuo de composición en $SU(2)$

Para $U,V\in SU(2)$, sea $C(U,V)=UVU^{-1}V^{-1}$ y $\nu(U,V)=1-\frac12\operatorname{ReTr}C(U,V)$.

**Proposición 7 (observable exacto de conmutación).** Con la norma de Frobenius,

$$
\boxed{\nu(U,V)=\frac14\|UV-VU\|_F^2,\qquad 0\le\nu(U,V)\le2.}
\tag{20}
$$

Además, $\nu(gUg^{-1},gVg^{-1})=\nu(U,V)$ para todo $g\in SU(2)$.

*Prueba.* La expansión de $\|UV-VU\|_F^2$ mediante $U^*=U^{-1}$ y $V^*=V^{-1}$ da $4-2\operatorname{ReTr}(UVU^{-1}V^{-1})$. La traza de un elemento de $SU(2)$ pertenece a $[-2,2]$ y la traza es invariante bajo conjugación. $\square$

El acarreo aritmético de (3) es un residuo entero de suma; $\nu$ es un defecto cuadrático de conmutación. Las dos operaciones admiten una descripción común por composición y actualización de información, con métricas y leyes propias de cada dominio.

## 9. Tabla de resultados y reproducibilidad

| Fórmula o mecanismo | Procedencia | Tipo de comprobación |
|:--|:--|:--|
| Aparición $\log r(n)=\Lambda(n)$ y diferencia (4) | R–01/R–02, HC–03 | Demostración directa; coeficientes racionales |
| Estabilidad de recuperación (6) | Análisis de condicionamiento de esta nota | Desigualdad aguda; prueba algebraica |
| Legendre y acarreos (7)–(9) | Identidades clásicas, marco del 22-XI | Prueba por exponentes primos; control racional |
| Relación con Chebyshev (10) y RH (11) | Stirling, Mertens, von Koch | Reducción analítica y equivalencia |
| Ventanas (12)–(13) | Sumas ponderadas, integración | Prueba directa; control racional de ventanas |
| Producto de Euler, Mellin (15)–(17) | R–03, comparaciones 20–21-XI | Cálculo analítico exacto en dominios indicados |
| Conjugación e imagen (18) | Auditoría Masullo, análisis de Fourier | Prueba de operadores en $H_0$ |
| Congruencia contextual y defecto $SU(2)$ (20) | Marco transversal P vs NP / Yang–Mills | Pruebas algebraicas directas |
| Extensión a caracteres (14) | HC–03, comparación Alpöge | Identidad por linealidad |

**Programa de control.** `scripts/verificar_integracion.py` usa `fractions.Fraction` y compara coeficientes racionales de cada símbolo formal $\log p$; los controles incluyen la recuperación por $\Delta^2T$, la fórmula de Legendre, la identidad de $S$, ventanas, periodicidad coprima y una dependencia explícita entre los módulos $3$ y $9$. La aritmética finita verifica los casos enumerados y permite detectar regresiones de implementación. Los enunciados de alcance infinito se justifican por sus pruebas textuales y fuentes analíticas.

## 10. Programa matemático de transferencia

La formulación cuantitativa natural es hallar, mediante hipótesis explícitas sobre familias de referencias y su composición, una estimación para la desviación conjunta centrada

$$
\mathcal R(m)=S(m)-\left(2\log2-\frac32\right)m.
\tag{19}
$$

El puente con observables $T_\chi$ permite comparar esta tarea con desigualdades de ventanas para combinaciones positivas de caracteres. El puente operatorio permite, por su parte, evaluar el efecto de la norma y de la inversión de referencias en la recuperación. Una transferencia matemática concreta se expresará como una aplicación explícita entre espacios, una desigualdad cuantitativa y los cuantificadores de uniformidad de cada escala.

## Bibliografía documental

- **[D1]** R–01/R–02, *Escalas relacionales de la criba*, 17-XI-2026, [repositorio público](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/2026-11-17_escalas_relacionales_riemann).
- **[D2]** `Comparacion_R03_Alpoge_2026-11-21.md`, nota técnica de correspondencia exacta y ventanas, 21-XI-2026, biblioteca de investigación.
- **[D3]** `nota_comparativa_R03_HC03_Alpoge_2026-11-21.pdf`, *Generación, herencia y control de los primos*, 21-XI-2026, biblioteca de investigación.
- **[D4]** `AUDITORIA_CORRESPONDENCIAS_ECONOMIA_2026-11-21.md`, auditoría de operadores y topologías, 21-XI-2026, biblioteca de investigación.
- **[D5]** `MARCO_COMUN_ES.md`, *Referencia, composición, residuo y control de escala*, 22-XI-2026, archivo de trabajo.
- **[A1]** L. Alpöge, *Remark*, 20-XI-2026, [anuncio original](https://alpo.ge/remark.pdf).
- **[A2]** Lean/Mathlib, *Lean verification of the Riemann Hypothesis*, 21-XI-2026, [declaración conjunta](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/).
- **[M1]** A. M. Masullo, *The Music of the Primes*, borrador difundido 20-XI-2026, [manuscrito](https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf); R. Vakil, [anuncio y actualización](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/).
- **[C1]** Criterios clásicos de Mertens, von Koch, Nyman–Beurling y Báez-Duarte, según se aplican en la bibliografía matemática citada en D1–D4.

---

*Endless Monkey Project / Relational Geometry Program*
