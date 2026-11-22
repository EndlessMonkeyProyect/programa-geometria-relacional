---
title: "Retorno de escala, reflexión y herencia aritmética"
subtitle: "Del bit modular y las octavas de Mersenne a una condición diádica equivalente a Riemann"
author: "Endless Monkey Project / Relational Geometry Program"
date: "22 de noviembre de 2026"
lang: es-CR
abstract: |
  Se formaliza la repetición relacional como retorno de una firma bajo una transformación de escala, manteniendo separados los índices de las octavas de Mersenne y los argumentos de las sumas de Chebyshev. Una reflexión sobre los residuos produce el bit de acarreo y un defecto de conmutación de exactamente una unidad modular al duplicar. Para módulos impares las trayectorias de duplicación son periódicas; las potencias de dos trasladan exactamente su contribución a la siguiente escala. Esta herencia conduce a una identidad de transición que distingue las fases antiguas de las nuevas potencias primas. Como resultado, la cota asociada con Riemann se expresa de manera equivalente mediante una sola desviación del retorno diádico de los acarreos impares. Se exhibe también un ciclo módulo siete que impide inferir cancelación a partir de la periodicidad por sí sola. Las identidades se prueban para todos los índices indicados y se contrastan con controles finitos exactos; la estimación uniforme requerida no se deduce de la periodicidad.
---

**Nota de formalización y continuidad · Versión 1.0 · Para revisión matemática**

## 1. Planteamiento: qué significa que una estructura se repita

El punto de partida es el principio relacional de *La reflexión* (septiembre de 2026) y de *El hilo* (octubre de 2026): una reflexión introduce una posibilidad de comparación, y una distinción mínima constituye un bit bajo un contrato definido. La nota de *Incertidumbre orientacional y octavas relacionales en el espectro de Mersenne* (mayo de 2026) contiene la identidad de herencia $M_{2k}=M_k(2^k+1)$. Se investigan **retornos de relaciones**, con conservación y actualización de las referencias, en lugar de identificar repetición con igualdad numérica.

Se mantendrán dos transformaciones diferentes: (i) la duplicación $m\mapsto2m$ del argumento de los observables aritméticos, y (ii) la secuencia de niveles de Mersenne $M_k=2^k-1$, cuyo índice $k$ se puede desplazar o duplicar. Ambas poseen una estructura binaria, pero cada una tiene su propia ecuación.

Para todo entero $q\ge2$ y residuo $r\in\{0,\ldots,q-1\}$, se definen

\[
R_q(r)=q-1-r,\qquad D_q(r)=(2r)\bmod q,\qquad
c_q(r)=\left\lfloor\frac{2r}{q}\right\rfloor\in\{0,1\}.
\tag{1}
\]

La reflexión $R_q$ organiza las imágenes de una comparación en pares; $c_q$ distingue los dos miembros cuando el par contiene dos puntos. Se trata de una **realización aritmética** del bit discriminante, definida por una consulta de acarreo. El grano del espacio normalizado de residuos es $1/q$.

**Proposición 1 (reflexión, bit y punto fijo).** Para todos $q,r$ anteriores,

\[
\boxed{R_q^2(r)=r,\qquad
c_q(r)+c_q(R_qr)=1-\mathbf1_{\{q\text{ impar},\,2r=q-1\}}.}
\tag{2}
\]

*Prueba.* El primer enunciado resulta de $q-1-(q-1-r)=r$. Si $q=2h$, la reflexión intercambia los residuos inferiores a $h$ con los superiores o iguales a $h$. Si $q=2h+1$, intercambia $\{0,\ldots,h-1\}$ con $\{h+1,\ldots,2h\}$ y fija $h$, cuyo acarreo es cero. $\square$

La incertidumbre asociada al par es binaria en las órbitas de dos elementos. El punto fijo impar tiene una respuesta de acarreo ya determinada; su papel aritmético se estudió en la nota *Del bit fundamental a la desviación aritmética* (22-XI-2026).

## 2. El retorno y su diferencia mínima

**Proposición 2 (defecto exacto de composición).** La duplicación de residuo y la reflexión cumplen, como aplicaciones módulo $q$,

\[
\boxed{R_qD_q(r)\equiv D_qR_q(r)+1\pmod q.}
\tag{3}
\]

*Prueba.* Por definición $R_qD_q(r)\equiv-1-2r\pmod q$, mientras $D_qR_q(r)\equiv-2-2r\pmod q$. La diferencia es $1\pmod q$. $\square$

La ecuación (3) cuantifica un **desfase de una celda modular**; respecto de la normalización $r/q$, su amplitud algebraica es $1/q$ sobre el círculo de residuos. La diferencia entre las *respuestas binarias* de $c_q$ puede ser cero o una unidad y depende de si se cruza el umbral. El desfase no se identifica con una probabilidad física ni con un error analítico acumulado.

**Proposición 3 (retornos para una referencia fija).** Si $q$ es impar y $d=\gcd(m,q)$, la trayectoria de $m$ bajo duplicaciones,

\[
m,\ 2m,\ 4m,\ldots\pmod q,
\]

es periódica, de período $\operatorname{ord}_{q/d}(2)$, con el convenio $\operatorname{ord}_{1}(2)=1$. Por tanto, $c_q(2^jm)$ también es periódico en $j$. Si $q=2^a$, la trayectoria modular llega a cero en a lo sumo $a$ duplicaciones.

*Prueba.* La igualdad $2^\ell m\equiv m\pmod q$ equivale a $2^\ell\equiv1\pmod{q/d}$, pues $m/d$ es coprimo con $q/d$. Para $q$ impar, $2$ es invertible y su orden multiplicativo es finito. Para $q=2^a$, $2^am\equiv0\pmod{2^a}$. $\square$

La periodicidad es **relativa a un módulo fijo**. En las sumas de acarreos, la familia de módulos activos cambia cuando aparece una nueva potencia prima.

**Testigo de sesgo de fase.** Para $q=7$, la órbita $1\to2\to4\to1$ tiene bits $(0,0,1)$, con media $1/3$; la órbita $3\to6\to5\to3$ tiene bits $(0,1,1)$, con media $2/3$. La media uniforme de los siete residuos es $3/7$. Los tres valores son distintos: un retorno periódico exacto admite diferentes desbalances según la órbita seleccionada.

## 3. Herencia bajo duplicación del argumento

Sean $L(n)=\operatorname{mcm}(1,\ldots,n)$, $\Lambda$ la función de von Mangoldt y $\psi(x)=\sum_{n\le x}\Lambda(n)$. Defínanse

\[
B(m)=\frac{\binom{2m}{m}}{L(2m)/L(m)},\quad
H(m)=\log B(m)=\sum_{p^j\le m}(\log p)c_{p^j}(m),
\quad m\ge1.
\tag{4}
\]

La identidad de $H(m)$ es exacta por la fórmula clásica de Legendre, y quedó demostrada en las notas aritméticas del 21–22 de noviembre. La familia activa incluye las potencias primas $p^j\le m$.

**Proposición 4 (conservación de los bits de base dos).** Para todo $a\ge2$,

\[
\boxed{c_{2^a}(2m)=c_{2^{a-1}}(m),\qquad c_2(2m)=0.}
\tag{5}
\]

Consecuentemente,

\[
\boxed{\sum_{2^a\le2m}(\log2)c_{2^a}(2m)
=\sum_{2^a\le m}(\log2)c_{2^a}(m).}
\tag{6}
\]

*Prueba.* La primera igualdad se obtiene directamente de las partes enteras que definen el acarreo. La segunda surge de $2m\equiv0\pmod2$. Al desplazar el índice $a\mapsto a-1$ en la suma de la izquierda, cada potencia $2^{a-1}\le m$ encuentra exactamente su contribución anterior; el término $a=1$ vale cero. $\square$

**Proposición 5 (identidad completa de retorno con herencia y novedad).** Para todo $m\ge1$,

\[
\boxed{\begin{aligned}
H(2m)-H(m)={}&\sum_{\substack{p\ \mathrm{impar},\,j\ge1\\p^j\le m}}
(\log p)\,[c_{p^j}(2m)-c_{p^j}(m)]\\
&+\sum_{\substack{p\ \mathrm{impar},\,j\ge1\\m<p^j\le2m}}
(\log p)\,c_{p^j}(2m).
\end{aligned}}
\tag{7}
\]

*Prueba.* Se resta la suma de (4) en $m$ de su valor en $2m$. Las referencias impares ya activas aportan la diferencia de sus fases; las potencias primas impares incorporadas entre $m$ y $2m$ aportan el segundo sumando. Los términos de base dos se cancelan exactamente por (6). $\square$

Esta igualdad **define sin ambigüedad lo que retorna y lo que se incorpora**: el mismo umbral impar puede cambiar su bit por reflexión/duplicación, y las nuevas referencias entran con su propia fase. Toda contribución de base dos se transporta de escala en escala sin cambio en el peso total.

## 4. Las octavas de Mersenne como trayectoria especial

Sea $M_k=2^k-1$. La factorización heredada del antecedente de mayo es

\[
\boxed{M_{2k}=M_k(2^k+1),\qquad
\gcd(M_k,2^k+1)=1.}
\tag{8}
\]

**Proposición 6 (retorno exacto en el índice de octava).** Para todo módulo impar $q\ge3$, escribiendo $d_q=\operatorname{ord}_q(2)$,

\[
\boxed{c_q(M_{k+d_q})=c_q(M_k)\qquad(k\ge1).}
\tag{9}
\]

Para cada $a\ge1$, se cumple también

\[
\boxed{c_{2^a}(M_k)=\mathbf1_{\{k\ge a\}}.}
\tag{10}
\]

En particular, los módulos de base dos que efectivamente intervienen en $H(M_k)$ son $2^a$ con $1\le a\le k-1$, y todos tienen bit $1$:

\[
\boxed{v_2(B(M_k))=k-1.}
\tag{11}
\]

*Prueba.* De $2^{d_q}\equiv1\pmod q$ se obtiene $M_{k+d_q}\equiv M_k\pmod q$; el bit depende exclusivamente del residuo. Para la potencia de dos, si $k<a$, $0\le M_k=2^k-1<2^{a-1}$; su bit es cero. Si $k\ge a$, $M_k\equiv-1\pmod{2^a}$ y su bit es uno. Sumando las potencias activas se obtiene (11). $\square$

**Proposición 6.1 (módulo de Mersenne silencioso).** Para cualesquiera $d\ge2$ y $k\ge1$,

\[
\boxed{c_{M_d}(M_k)=0.}
\tag{12}
\]

*Prueba.* La relación $2^d\equiv1\pmod{M_d}$ permite escribir $M_k\bmod M_d=2^r-1$ para algún $0\le r<d$. Por tanto, $0\le2^r-1\le2^{d-1}-1<M_d/2$, y el acarreo es cero. $\square$

En particular, los módulos $3=M_2$, $7=M_3$ y $31=M_5$ tienen bit siempre nulo sobre la sucesión $M_k$. El módulo $9$ presenta un patrón diferente: al recorrer $k=1,\ldots,6$, sus bits son $(0,0,1,1,0,0)$ y vuelven a repetirse. La familia de fases presenta **retorno exacto, herencia y sesgos de trayectoria**. Cuando $M_d$ no es potencia prima, (12) es un hecho modular de prueba y no introduce por sí mismo un término adicional en la suma (4), cuyos índices son únicamente potencias primas.

## 5. De los retornos a la desviación global

Por la identidad (4) y la función $E(x)=\psi(x)-x$,

\[
\boxed{H(m)=\log\binom{2m}{m}-\psi(2m)+\psi(m).}
\tag{13}
\]

Defínase $a=2\log2-1$ y el **desfase acumulado de un retorno**

\[
\boxed{\mathfrak D(m)=H(2m)-H(m)-am.}
\tag{14}
\]

Por (7), $\mathfrak D(m)$ se expresa únicamente mediante cambios de bits impares heredados, activaciones de potencias primas impares nuevas y el centrado lineal $am$. Este es el observable preciso que permite examinar la hipótesis de que la repetición relacional limite la desviación.

**Teorema 7 (criterio diádico de retorno; equivalencia clásica reformulada).** Con $\mathfrak D$ de (14), se cumple

\[
\boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
\mathfrak D(m)=O(\sqrt m\,\log^2m)\quad(m\to\infty).}
\tag{15}
\]

*Prueba.* Por Stirling y (13),

\[
H(m)=am-\tfrac12\log(\pi m)-J(m)+O(m^{-1}),
\qquad J(m)=E(2m)-E(m).
\tag{16}
\]

La estimación clásica de von Koch expresa RH de modo equivalente a $E(x)=O(\sqrt x\log^2x)$; de ahí, por (16), $H(m)-am=O(\sqrt m\log^2m)$ y por diferencia de escalas la misma cota para $\mathfrak D(m)$.

Para la implicación inversa, póngase $F(m)=H(m)-am$. La hipótesis es

\[
F(2m)-F(m)=O(\sqrt m\log^2m).
\tag{17}
\]

La ley local exacta de actualización de la nota del 21-XI-2026 es

\[
\log\frac{B(m+1)}{B(m)}
=\log\frac{2(2m+1)}{m+1}
+\Lambda(m+1)-\Lambda(2m+1)-\Lambda(2m+2).
\tag{18}
\]

Como $0\le\Lambda(n)\le\log n$, esta variación es $O(\log(m+2))$. Por tanto $F(2m+1)=F(2m)+O(\log(m+2))$. Se obtiene para cualquier entero $n\ge2$

\[
F(n)=F(\lfloor n/2\rfloor)
+O(\sqrt n\log^2(n+1)),
\tag{19}
\]

incluso al pasar por índices impares. La iteración de (19) hasta el índice $1$ suma una serie geométrica de términos $\sqrt{n/2^j}\log^2(n+1)$ y da $F(n)=O(\sqrt n\log^2n)$. La ecuación (16) recupera $J(m)=O(\sqrt m\log^2m)$. Finalmente, como

\[
E(2m)=E(m)+J(m),\qquad
E(2m+1)=E(2m)+\Lambda(2m+1)-1,
\tag{20}
\]

la misma iteración diádica da $E(n)=O(\sqrt n\log^2n)$. El criterio clásico de von Koch concluye RH. $\square$

**Forma íntegramente en bits impares.** Sustituyendo (7) en (14), la condición equivalente de (15) consiste exactamente en demostrar que

\[
\boxed{\begin{aligned}
&\sum_{\substack{p\ \mathrm{impar},j\ge1\\p^j\le m}}
(\log p)\,[c_{p^j}(2m)-c_{p^j}(m)]\\
&\quad+\sum_{\substack{p\ \mathrm{impar},j\ge1\\m<p^j\le2m}}
(\log p)\,c_{p^j}(2m)-am
=O(\sqrt m\log^2m).
\end{aligned}}
\tag{21}
\]

La identidad es **exacta**, y la cota es el **objetivo cuantitativo**. La equivalencia (15) es una caracterización bajo el criterio clásico; todavía no se dispone en este marco de una estimación independiente que establezca (21) para todas las escalas.

## 6. Qué garantiza el ciclo y qué debe probarse

Un bit asociado a un módulo impar fijo se repite tras un número finito de duplicaciones. En cambio, la suma (21) comprende un conjunto móvil de módulos y sigue una trayectoria aritmética específica. Los ciclos módulo siete de la sección 2 dan un testigo preciso: la periodicidad de cada referencia no fuerza que su contribución centrada tenga promedio cero sobre esa trayectoria. Del mismo modo, la igualdad de posición normalizada $\theta(2x)=\theta(x)$ en una octava logarítmica y la herencia $M_{2k}=M_k(2^k+1)$ describen retornos de escala, sin fijar por sí solos la distribución de los bits asociados a todas las potencias primas.

La condición de (21) es el contrato matemático de transferencia: una ley de **balance uniforme de fases heredadas y referencias nuevas**, con precisión $O(\sqrt m\log^2m)$, válida para cada escala. Puede contrastarse con registros exactos y estudiarse mediante dinámica modular o estimaciones analíticas; los controles finitos no establecen sus cuantificadores infinitos.

## 7. Registro de procedencia y verificación

| Resultado | Procedencia | Estado |
|:--|:--|:--|
| Bit de reflexión y punto fijo, (2) | *Del bit fundamental a la desviación*, 22-XI | Identidad exacta |
| Defecto modular de una celda, (3) | Composición explícita $R_q,D_q$ | Identidad exacta |
| Ciclos impares y extinción en $2^a$, sección 2 | Orden multiplicativo | Teorema elemental |
| Transporte de base dos, (5)–(6) | Acarreos y reindexación | Identidad exacta |
| Herencia + incorporación impares, (7) | Legendre y $B(m)$ | Identidad exacta |
| Octavas de Mersenne, (8) | Nota de mayo de 2026 | Identidad clásica |
| Bit sobre niveles $M_k$, (9)–(12) | Períodos y desigualdad del umbral | Identidades exactas |
| Criterio de retorno, (15)–(21) | Stirling, von Koch y transición de $B$ | Equivalencia condicional a una cota no establecida |

**Verificación independiente.** `scripts/verificar_octavas.py` utiliza exclusivamente aritmética entera y la biblioteca estándar de Python. Controla involuciones, defectos, períodos, módulos de Mersenne, transporte de potencias de dos, factorización de Legendre, descomposición de transición y los ciclos de $3$, $7$ y $9$. Su alcance es finito; los teoremas generales se justifican por las pruebas anteriores.

**Fuentes internas cotejadas.** *Incertidumbre orientacional y octavas relacionales en el espectro de Mersenne* (mayo de 2026); *La reflexión* v0.2 (septiembre de 2026); *El hilo* (octubre de 2026); *Aparición, herencia y acarreos: correlación de referencias y frontera móvil* (21-XI-2026); *CME–RH–01* (21-XI-2026); *Del bit fundamental a la desviación aritmética* (22-XI-2026); *Generación, herencia y composición aritmética* (22-XI-2026).

---

*Endless Monkey Project / Relational Geometry Program*
