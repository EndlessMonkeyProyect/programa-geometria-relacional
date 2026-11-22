# Generación, herencia y control de los primos

**Correspondencias formales entre R–03 / HC–02 / HC–03 y el argumento de Alpöge**  
**Nota técnica de comparación · 21 de noviembre de 2026 · Versión 1.0**

## Resumen

El estudio conjunto de la criba relacional R–01/R–03, los laboratorios HC–01/HC–02 y la propuesta de diferencia mínima HC–03 permite reconocer una interfaz aritmética exacta con la reconstrucción publicada del argumento formal de Levent Alpöge para RH y GRH. El observable común es la suma centrada de von Mangoldt con peso de rampa \((x/n-1)\). La presentación por herencia aporta una descomposición explícita de primos ordinarios y potencias heredadas, una cota uniforme para estas últimas y una operación local que recupera los coeficientes individuales. El argumento de Alpöge aporta, en su exposición técnica disponible, estimaciones aritméticas para combinaciones de sumas modificadas por caracteres de Dirichlet y un criterio analítico de localización de ceros. El encaje demostrado es el de los observables y las identidades; la transferencia de estimaciones constituye una tarea matemática específica.

**Palabras clave:** hipótesis de Riemann, von Mangoldt, criba, herencia, diferencias finitas, caracteres de Dirichlet, Mellin, cotas en ventanas.

## 1. La interfaz aritmética compartida

Sea \(\Lambda(n)=\log p\) cuando \(n=p^k\) para algún primo \(p\) y \(k\ge1\), y \(0\) en otro caso. La suma ponderada es

\[
T(x)=\sum_{n\le x}\Lambda(n)\left(\frac{x}{n}-1\right),
\qquad
G(x)=T(x)-x(\log x-1-\gamma).
\tag{1}
\]

La función \(G\) coincide literalmente con el observable destacado en la reconstrucción publicada del argumento de Alpöge, incluida la normalización mediante la constante de Euler \(\gamma\) [3, 5]. La coincidencia identifica una **interfaz matemática común**; no establece por sí sola una equivalencia de procedimientos de demostración.

El peso \(x/n-1\) vale cero al alcanzar \(x=n\). Al avanzar la escala, incorpora de manera continua la contribución de cada potencia prima, lo que vincula el punto de entrada de la información con su acumulación posterior.

## 2. Herencia, localización espectral y escala

En R–03, para un conjunto finito de primos \(S\), la transformada de la discrepancia de criba está representada por

\[
F_S(s)=\frac{\zeta(s)}{s}\prod_{p\in S}(1-p^{-s}),
\qquad 0<\operatorname{Re}s<1.
\tag{2}
\]

Cada factor \(1-p^{-s}\) es distinto de cero en la franja indicada. Por tanto, la multiplicación conserva exactamente los ceros de \(\zeta\) y sus multiplicidades. Esta relación distingue la **representación espectral** del problema de la **estimación de tamaños** requerida para localizar los ceros [1].

El laboratorio HC–02 emplea las funciones de Chebyshev

\[
\vartheta(x)=\sum_{p\le x}\log p,\qquad
\psi(x)=\sum_{n\le x}\Lambda(n),\qquad
U(x)=\psi(x)-\vartheta(x)
=\sum_{k\ge2}\vartheta(x^{1/k}).
\tag{3}
\]

Su identidad de transferencia global es

\[
G(x)=Q(x)-B(x),\quad
Q(x)=-x\int_x^\infty\frac{\vartheta(t)-t}{t^2}\,dt,\quad
B(x)=x\int_x^\infty\frac{U(t)}{t^2}\,dt.
\tag{4}
\]

El resultado probado en HC–02, mediante estimaciones clásicas, es

\[
0\le B(x)<24\sqrt{x}\qquad(x\ge4).
\tag{5}
\]

De este modo, la parte heredada queda controlada cuantitativamente; la estimación de \(Q\) es el objetivo adicional que conecta con la distribución de los primos ordinarios [2].

## 3. La diferencia mínima: recuperación local exacta

Para enteros \(m\ge2\), se define la segunda diferencia centrada

\[
\Delta^2 f(m)=f(m+1)-2f(m)+f(m-1).
\]

La linealidad del peso de rampa en cada intervalo \(x\ge n\) conduce a la identidad exacta

\[
\boxed{\Delta^2 T(m)=\frac{\Lambda(m)}m.}
\tag{6}
\]

La centración de (1) aporta

\[
\boxed{\Delta^2 G(m)=\frac{\Lambda(m)}m
-\bigl[(m+1)\log(m+1)-2m\log m+(m-1)\log(m-1)\bigr].}
\tag{7}
\]

La expresión entre corchetes es \(1/m+O(m^{-3})\). La segunda diferencia aísla, por tanto, la contribución exacta de cada potencia prima, y la acumulación de estas diferencias reconstruye el observable global con las condiciones iniciales correspondientes. Se trata de una identidad elemental comprobable de forma independiente; su uso sistemático como registro de generación, herencia y costo constituye la orientación de HC–03.

## 4. Extensión exacta a caracteres de Dirichlet

Sea \(\chi\) un carácter de Dirichlet. Defínase

\[
T_\chi(x)=\sum_{n\le x}\Lambda(n)\chi(n)
\left(\frac{x}{n}-1\right),\qquad
\vartheta_\chi(x)=\sum_{p\le x}\chi(p)\log p.
\tag{8}
\]

La misma operación local funciona con coeficientes complejos:

\[
\boxed{\Delta^2 T_\chi(m)=\frac{\Lambda(m)\chi(m)}m.}
\tag{9}
\]

La parte heredada admite la identidad

\[
U_\chi(x)=\sum_{k\ge2}\sum_{p^k\le x}(\log p)\chi(p)^k
=\sum_{k\ge2}\vartheta_{\chi^k}(x^{1/k}),
\quad |U_\chi(x)|\le U(x).
\tag{10}
\]

Así, para
\(B_\chi(x)=x\int_x^\infty U_\chi(t)t^{-2}\,dt\), resulta

\[
|B_\chi(x)|\le B(x)<24\sqrt x\qquad(x\ge4).
\tag{11}
\]

Esta extensión es una consecuencia directa de la multiplicatividad de \(\chi\) y la cota de HC–02; proporciona una componente heredada controlada de manera uniforme también en la versión torcida. Para un carácter primitivo no principal, la exposición de Alpöge utiliza el observable centrado

\[
g_\chi(x)=T_\chi(x)+x\frac{L'}{L}(1,\chi).
\tag{12}
\]

Como el término de centración es lineal en \(x\), se conserva exactamente \(\Delta^2g_\chi(m)=\Lambda(m)\chi(m)/m\). Las expresiones (9)–(12) son el **puente algebraico verificable** entre HC–03 y las sumas torcidas que aparecen en la otra construcción [5].

## 5. Encaje de las construcciones y diferencia de alcance

| Capa matemática | R–03 / HC–02 / HC–03 | Argumento de Alpöge | Estado de la relación |
|---|---|---|---|
| Generación aritmética | Criba, nuevas referencias y potencias heredadas | Primos y potencias en sumas ponderadas | Identidades clásicas compartidas |
| Observable principal | \(G(x)\) en (1) | El mismo \(G(x)\) | Coincidencia exacta |
| Observación local | \(\Delta^2T(m)=\Lambda(m)/m\) | Peso de rampa y transformada de Mellin | Interfaz derivada exactamente |
| Caracteres | (8)–(11), extensión algebraica | \(g_\chi\) y familias positivas de caracteres | Comparación técnicamente disponible |
| Control cuantitativo | \(B(x)=O(\sqrt x)\) | Cotas de sumas combinadas en ventanas mediante aritmética automórfica | Mecanismos complementarios |
| Localización de ceros | Conservación de ceros por factores finitos | Exclusión de ceros por criterio analítico y ecuación funcional | Alcances distintos |

La relación se representa por una **inclusión de observables**, seguida de un **acoplamiento de técnicas**: la generación y la herencia ofrecen una realización microscópica de las sumas, mientras que el argumento aritmético-analítico añade las estimaciones para familias de caracteres necesarias para localizar ceros.

La certificación formal de Lean/Mathlib del 21 de noviembre de 2026 se refiere a la prueba presentada por Alpöge. Las ecuaciones (6)–(11) de esta nota son derivaciones separadas, no parte de esa certificación [3].

## 6. Condición para una integración más profunda

La arquitectura publicada del argumento de Alpöge utiliza una combinación positiva \(G_{\mathcal F}(x)\) de sumas centradas \(G\) y \(\operatorname{Re}g_\chi\), y un criterio de ventanas del tipo

\[
G_{\mathcal F}(x)\le C_\eta x^{1/2+\eta}
\quad\text{para todo }x\in[Y,Y^{3/2}],
\tag{13}
\]

para ventanas \(Y\) arbitrariamente grandes y exponentes \(\eta>0\) adecuados. Las cotas del argumento se obtienen mediante estructuras automórficas y levantamientos theta; la implicación analítica hacia la localización de ceros utiliza Mellin, positividad y un razonamiento de tipo Landau [4, 5].

El ensayo siguiente queda formulado con precisión: construir \(G_{\mathcal F}\) a partir de las diferencias mínimas (9), descomponer cada término en aportes ordinarios y heredados mediante (10)–(11), y buscar una desigualdad sobre la **parte ordinaria combinada** que sea suficientemente fuerte en esas ventanas. El éxito matemático no sería la reconstrucción exacta —que ya se dispone— sino la obtención de una cota nueva sin introducirla como premisa.

## Conclusión

La coincidencia del observable \(G(x)\), de su peso de rampa y de sus extensiones a caracteres ofrece una articulación exacta entre ambas propuestas. La diferencia mínima da una lectura local de los coeficientes; la herencia proporciona un control uniforme de las potencias primas; el argumento de Alpöge aporta herramientas aritméticas para las cotas combinadas que conducen a RH/GRH. La estructura conjunta constituye un programa de comparación reproducible con una condición matemática pendiente y explícita: el control de la contribución ordinaria en familias de caracteres.

## Referencias y procedencia

1. **R–03**, *Herencia espectral, normalización y ubicación de los ceros*, v0.2, 18 de noviembre de 2026. [Repositorio del programa](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional).
2. **LAB–HC–02**, *Herencia de potencias primas y certificado de transferencia entre escalas*, expediente v1.0, 21 de noviembre de 2026, archivo `INFORME_LAB_HC02.md`.
3. Lean and Mathlib communities, [*Lean verification of the Riemann Hypothesis*](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), declaración conjunta, 21 de noviembre de 2026.
4. Levent Alpöge, [*Remark*](https://alpo.ge/remark.pdf), comunicación de cuatro páginas, 20 de noviembre de 2026.
5. [*The proof of the Riemann hypothesis announced by L. Alpöge: a guide to its architecture*](https://nasqret.github.io/riemann-rev/guide/proof-guide.pdf), guía técnica de lectura del archivo Lean, consultada el 21 de noviembre de 2026. La guía es una reconstrucción independiente de la arquitectura, no la transcripción completa de un manuscrito del autor.

*Endless Monkey Project / Relational Geometry Program*
