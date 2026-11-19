# R–03 · Herencia espectral, normalización y ubicación de los ceros

**Continuación de R–01 / R–02 · Documento de examen, v0.4 · 18 de noviembre de 2026**<br>
**Endless Monkey Project**<br>
Relational Geometry Program<br>
**Le Matt Ansatz Di Ego**

## Resumen

La transformada de Mellin de la discrepancia de criba conserva los ceros de la función zeta bajo cualquier referencia formada por un número finito de primos. La conservación es exacta y reversible dentro de la franja crítica abierta. Este examen estudia cuatro consecuencias: la normalización que recupera la referencia común, la estabilidad de esa recuperación, el factor de amplificación de errores de la normalización en el pivote $s=\tfrac12$ cuando la referencia incorpora todos los primos hasta $X$, y la separación entre simetría y localización mediante tres modelos de control.

En el pivote, el factor de inversión admite una normalización exacta que equivale a la hipótesis de Riemann (Akatsuka, 2024). Escrita con la discrepancia de la criba, la hipótesis de Riemann es una cota inferior para la discrepancia completa en el pivote. El laboratorio sigue esa cantidad hasta $X=10^8$. La hipótesis de Riemann permanece abierta.

**Palabras clave:** criba; herencia; transformada de Mellin; ceros de zeta; producto de Euler parcial; función de Davenport–Heilbronn; normalización.


## Procedencia y alcance de las afirmaciones

| Resultado | Procedencia | Estado de esta edición |
|:--|:--|:--|
| Recurrencia de criba y forma de Mellin (R03.1) | Legendre, inclusión-exclusión; identidad clásica de Mellin | Conocido; reproducido |
| Conservación de ceros y multiplicidades para $S$ finito | Consecuencia inmediata de (R03.1) | Corolario demostrado aquí, no nueva localización |
| $F_S/P_S=\zeta/s$ y cotas de amplificación | Álgebra del producto finito y desigualdad triangular | Corolarios demostrados; complejidad no medida |
| Producto normalizado $E_1(X)$ y criterio RH | Akatsuka (2024), Teorema 3 | Conocido |
| Identidad de la discrepancia normalizada en $s=1/2$ | Sustitución exacta en Akatsuka | Reformulación demostrada; no criterio nuevo |
| Modelos de simetría y controles | Construcción polinomial; Davenport–Heilbronn; producto desplazado de $\xi$ | Controles, no pruebas de RH |
| Puente con Nyman–Beurling | Inclusión-exclusión, inversión $x\mapsto1/x$; criterio clásico (Báez-Duarte) | Correspondencia exacta explícita; suficiencia del subespacio restringido abierta |
| Cota inferior uniforme para la discrepancia normalizada | Equivalente a RH por Akatsuka | Abierto |

## 1. Referencia, discrepancia y transformada

Sea $S$ un conjunto finito de números primos y sean

$$
M_S=\prod_{p\in S}p,\qquad
\delta_S=\prod_{p\in S}\left(1-p^{-1}\right),\qquad
A_S(x)=\left|\lbrace 1\le n\le x:\ \gcd(n,M_S)=1\rbrace\right|,
$$

$$
E_S(x)=A_S(x)-x\,\delta_S,
\qquad
F_S(s)=\int_0^\infty E_S(x)\,x^{-s-1}\,dx.
$$

**Precisión de lenguaje.** $E_S$ es una discrepancia de conteo, no energía. La referencia modular distingue clases de residuos; la granularidad describe las distinciones accesibles bajo esa referencia. La medición cuadrática posterior no define la granularidad ni postula energía física.

La Proposición 1 de la [formalización publicada](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md) establece, en la franja $0<\mathrm{Re}(s)<1$,

$$
F_S(s)=\frac{\zeta(s)}{s}\,P_S(s),\qquad
P_S(s)=\prod_{p\in S}\left(1-p^{-s}\right).\tag{R03.1}
$$

El operador de herencia $T_pf(x)=f(x)-f(x/p)$ equivale, tras la transformada, a multiplicar por $1-p^{-s}$.

## 2. Proposición 1 — Herencia espectral exacta

**Para todo conjunto finito $S$, $F_S$ y $\zeta$ tienen los mismos ceros, con las mismas multiplicidades, dentro de $0<\mathrm{Re}(s)<1$.**

*Demostración.* Para $s=\sigma+it$ con $0<\sigma<1$, cada factor cumple $|p^{-s}|=p^{-\sigma}<1$, así que $P_S(s)$ no se anula. El factor $1/s$ tampoco se anula ni tiene polos en la franja. Por (R03.1), $F_S$ es $\zeta$ multiplicada por una función holomorfa sin ceros, y la factorización local preserva los órdenes de anulación. $\square$

**Lectura:** una referencia finita conserva los ceros y aporta otra forma de observarlos, con las mismas posiciones.

## 3. Proposición 2 — Normalización y referencia común

Defínase

$$
N_S(s)=\frac{F_S(s)}{P_S(s)}.\tag{R03.2}
$$

Para cada $S$ finito y $0<\mathrm{Re}(s)<1$,

$$
\boxed{N_S(s)=\frac{\zeta(s)}{s}.}\tag{R03.3}
$$

*Demostración.* Dividir (R03.1) entre el factor no nulo $P_S(s)$. $\square$

La referencia normalizada es la misma para todas las colecciones finitas de primos. Se trata de una identidad algebraica, no de una cota de recursos computacionales. Es una invariancia exacta: evaluar $N_S$ sigue pidiendo conocer $F_S$ y $P_S$, u otra representación de costo verificable.

## 4. Proposición 3 — Costo de la inversión y estabilidad

Fijado $\sigma_0$ con $0<\sigma_0<1$, para $\mathrm{Re}(s)\ge\sigma_0$ se cumple

$$
\prod_{p\in S}\left(1-p^{-\sigma_0}\right)
\le |P_S(s)|
\le\prod_{p\in S}\left(1+p^{-\sigma_0}\right).\tag{R03.4}
$$

Si una medición $\widetilde F_S$ de $F_S$ introduce un error absoluto $\varepsilon(s)$, la normalización satisface

$$
\left|\frac{\widetilde F_S(s)}{P_S(s)}-\frac{\zeta(s)}{s}\right|
=\frac{|\varepsilon(s)|}{|P_S(s)|}
\le |\varepsilon(s)|\prod_{p\in S}\left(1-p^{-\sigma_0}\right)^{-1}.\tag{R03.5}
$$

*Demostración.* Aplicar $1-|z|\le|1-z|\le1+|z|$ a cada $z=p^{-s}$, multiplicar y dividir entre $P_S(s)$. $\square$

**Límite asintótico.** Para cualquier $0<\sigma_0<1$, al incorporar todos los primos hasta $p_k$, el valor real $P_{S_k}(\sigma_0)=\prod_{j\le k}(1-p_j^{-\sigma_0})$ tiende a cero, porque $\sum_p p^{-\sigma_0}$ diverge (domina a $\sum_p 1/p$). La inversión puede amplificar los errores de medición sin una cota uniforme al crecer la referencia.

Esta proposición mide un **factor de acondicionamiento del error absoluto**, no el tiempo ni la memoria del cómputo. La sección siguiente la evalúa en el pivote, donde ese costo tiene una forma exacta.

## 5. Proposición 4 — Normalización del factor de inversión en el pivote

Sea $S_X$ el conjunto de los primos $p\le X$ y sea $\vartheta(X)=\sum_{p\le X}\log p$. En el pivote $s=\tfrac12$ el factor de herencia es real y positivo,

$$
P_{S_X}\!\left(\tfrac12\right)=\prod_{p\le X}\left(1-p^{-1/2}\right),
$$

y su inverso crece sin cota (§4). Akatsuka mide ese crecimiento con exactitud. Sea

$$
E_1(X)=\frac{P_{S_X}\!\left(\tfrac12\right)^{-1}}{\exp\!\left(\mathrm{li}\big(\vartheta(X)^{1/2}\big)\right)}.\tag{R03.11}
$$

**Teorema (Akatsuka, 2024, Teorema 3).** Son equivalentes:

1. la hipótesis de Riemann;
2. $E_1(X)$ está acotada para $X\ge3$;
3. $E_1(X)\to-\sqrt2\,\zeta\!\left(\tfrac12\right)\approx 2{,}0653$ cuando $X\to\infty$.

*Conocido.*

**Proposición 4 (lectura en la criba).** Para todo $X\ge3$,

$$
\boxed{F_{S_X}\!\left(\tfrac12\right)\,e^{\mathrm{li}\left(\vartheta(X)^{1/2}\right)}=\frac{2\,\zeta\!\left(\tfrac12\right)}{E_1(X)}.}\tag{R03.12}
$$

En consecuencia, la hipótesis de Riemann equivale a cada uno de estos enunciados:

- $\left|F_{S_X}(\tfrac12)\right|\,e^{\mathrm{li}(\vartheta(X)^{1/2})}$ está acotada inferiormente por una constante positiva para $X\ge3$;
- $F_{S_X}(\tfrac12)\,e^{\mathrm{li}(\vartheta(X)^{1/2})}\to-\sqrt2$.

*Demostración.* El punto $s=\tfrac12$ está en la franja abierta, así que (R03.1) da $F_{S_X}(\tfrac12)=2\,\zeta(\tfrac12)\,P_{S_X}(\tfrac12)$. Por (R03.11), $P_{S_X}(\tfrac12)=1/\big(E_1(X)\,e^{\mathrm{li}(\vartheta(X)^{1/2})}\big)$, lo que da (R03.12). Como $\zeta(\tfrac12)\approx-1{,}4604$ es distinto de cero y $E_1(X)>0$, la cota superior de $E_1$ equivale a la cota inferior del primer enunciado, y el límite de $E_1$ da el límite $2\zeta(\tfrac12)/(-\sqrt2\,\zeta(\tfrac12))=-\sqrt2$. $\square$

**Lectura.** $F_{S_X}(\tfrac12)$ es la discrepancia de la criba con todos los primos hasta $X$, integrada sobre todas las escalas con el peso $x^{-3/2}$ del pivote. La Proposición 4 dice que esa discrepancia total decae como $e^{-\mathrm{li}(\sqrt{\vartheta(X)})}$, con constante $-\sqrt2$, exactamente cuando todos los ceros están en la línea. Por el mismo teorema, un cero con parte real mayor que $\tfrac12$ hace que $E_1$ no esté acotada.

**Laboratorio.** *Verificado* con `verificacion_R03.py`:

| $X$ | $P_{S_X}(\tfrac12)^{-1}$ | $E_1(X)$ | $F_{S_X}(\tfrac12)\,e^{\mathrm{li}}$ |
|:-:|:-:|:-:|:-:|
| $10^2$ | $e^{6{,}95}$ | $3{,}1875$ | $-0{,}9163$ |
| $10^4$ | $e^{30{,}91}$ | $2{,}4439$ | $-1{,}1951$ |
| $10^6$ | $e^{178{,}32}$ | $2{,}2643$ | $-1{,}2899$ |
| $10^7$ | $e^{463{,}67}$ | $2{,}2229$ | $-1{,}3139$ |
| $10^8$ | $e^{1246{,}86}$ | $2{,}1945$ | $-1{,}3309$ |
| límite bajo RH | — | $2{,}0653$ | $-1{,}4142$ |

El inverso del factor crece hasta $e^{1247}$, y la cantidad normalizada se mantiene acotada y se acerca despacio a su límite. Es una observación compatible con la hipótesis de Riemann en ese rango; la tabla no demuestra la cota.

## 6. Proposición 5 — Simetría y localización: tres controles

### 6.1 Control mínimo

Sea $a=\tfrac15+i$, $z=s-\tfrac12$, y

$$
H(s)=\left(z^2-a^2\right)\left(z^2-\overline a^{\,2}\right).\tag{R03.6}
$$

Satisface $H(1-s)=H(s)$ y $H(\overline s)=\overline{H(s)}$, y sus cuatro ceros son $\tfrac{3}{10}\pm i$ y $\tfrac{7}{10}\pm i$. Para cada $S$ finito, la familia $H_S=H\,P_S$ conserva esos ceros dentro de la franja y la simetría conjugada; la simetría $s\mapsto1-s$ se pierde en general, porque $P_S(1-s)\neq P_S(s)$. El filtro simetrizado

$$
\boxed{\widehat H_S(s)=H(s)\,P_S(s)\,P_S(1-s)}\tag{R03.8}
$$

conserva las dos simetrías, y dentro de $0<\mathrm{Re}(s)<1$ sus únicos ceros son los cuatro de $H$, con las mismas multiplicidades.

*Prueba.* El cambio $s\mapsto1-s$ envía $z\mapsto-z$, y $H$ depende de $z^2$; sus coeficientes en $z$ son reales. Los ceros cumplen $z=\pm a$ o $z=\pm\overline a$, con partes reales $\tfrac12\pm\tfrac15$. En la franja, $P_S(s)$ y $P_S(1-s)$ son holomorfos y no nulos, y su producto es invariante bajo $s\mapsto1-s$ y respeta la conjugación. $\square$

### 6.2 Control estándar: Davenport–Heilbronn

Sea $\tau=\dfrac{\sqrt{10-2\sqrt5}-2}{\sqrt5-1}\approx0{,}2841$ y sea $a(n)$ periódica de período $5$ con $a(1)=1$, $a(2)=\tau$, $a(3)=-\tau$, $a(4)=-1$, $a(5)=0$. La función de Davenport–Heilbronn (también llamada contraejemplo de Titchmarsh) es

$$
f(s)=\sum_{n\ge1}\frac{a(n)}{n^s}=5^{-s}\sum_{j=1}^{4}a(j)\,\zeta\!\left(s,\tfrac{j}{5}\right),
\qquad
\Lambda(s)=\left(\frac{5}{\pi}\right)^{(s+1)/2}\,\Gamma\!\left(\frac{s+1}{2}\right)f(s).\tag{R03.13}
$$

Cumple la ecuación funcional $\Lambda(s)=\Lambda(1-s)$, del tipo de las funciones $L$ de Dirichlet impares módulo $5$; como sus coeficientes son reales, $\Lambda$ es real sobre la línea. Tiene ceros sobre la línea, el primero en $\tfrac12+5{,}0941598446\,i$, y ceros fuera de ella, el primero en $0{,}8085171825+85{,}6993484854\,i$ (Spira, 1994), con su espejo en $0{,}1914828175+85{,}6993484854\,i$. Sus coeficientes no son multiplicativos: $a(2)\,a(3)=-\tau^2\approx-0{,}0807$, mientras que $a(6)=a(1)=1$. Por eso $f$ no tiene producto de Euler. *Conocido* (Davenport y Heilbronn, 1936); *verificado* con `verificacion_R03.py`.

**Conclusión de los controles.** El control mínimo muestra que las dos simetrías y los filtros finitos dejan libre la ubicación de los ceros de una función holomorfa. El control estándar muestra lo mismo para una serie de Dirichlet con ecuación funcional del tipo de $\zeta$ y con ceros sobre la línea. Una diferencia entre $\zeta$ y $f$ es el producto de Euler; el control reforzado de §6.3 muestra por qué esta diferencia, aislada, tampoco basta para localizar los ceros. La Proposición 4 incorpora una condición global mucho más específica.


### 6.3 Control reforzado: producto de Euler y simetría sin localización

Una diferencia estructural entre la función de Davenport–Heilbronn y $\zeta$ es la existencia del producto de Euler. **Su mera existencia, aun combinada con simetría funcional, tampoco obliga a todos los ceros a quedar sobre $\operatorname{Re}(s)=1/2$.**

Sea $0<a<1/2$ real y sea $\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$. Definimos

$$
\boxed{\mathcal H_a(s)=\xi(s+a)\,\xi(s-a).}\tag{R03.14}
$$

La función $\mathcal H_a$ es entera, cumple $\mathcal H_a(1-s)=\mathcal H_a(s)$ y $\mathcal H_a(\overline{s})=\overline{\mathcal H_a(s)}$. Su parte aritmética tiene **producto de Euler genuino** en $\operatorname{Re}(s)>1+a$:

$$
\zeta(s+a)\zeta(s-a)=\prod_p(1-p^{-s-a})^{-1}(1-p^{-s+a})^{-1}.\tag{R03.15}
$$

Si $\rho=1/2+i\gamma$ es uno de los ceros conocidos de $\xi$, entonces $\mathcal H_a(\rho-a)=\mathcal H_a(\rho+a)=0$. Para $a=1/5$ y el primer cero $\gamma\approx14.1347251417$, aparecen ceros de $\mathcal H_a$ en $0.3+i\gamma$ y $0.7+i\gamma$, y sus conjugados: **fuera de la línea**.

*Demostración.* La ecuación funcional da $\xi(1-(s\pm a))=\xi(s\mp a)$, que intercambia los factores; la realidad de $\xi$ respecto de la conjugación da la segunda simetría. El producto de Euler procede de los dos factores de zeta en su semiplano común de convergencia. Finalmente, en $s=\rho-a$ se anula $\xi(s+a)$, y en $s=\rho+a$ se anula $\xi(s-a)$. $\square$

**Alcance:** el producto es de dos funciones de zeta desplazadas, con factores gamma desplazados; no satisface todas las restricciones de una función $L$ primitiva normalizada (en particular, la condición de Ramanujan para los parámetros locales). Es un contraejemplo a la inferencia general «simetría + Euler product $\Rightarrow$ ubicación», **no** un contraejemplo a RH ni a un resultado estándar sobre una clase $L$ más restringida.

**Conclusión revisada de los controles.** El producto de Euler, la simetría y la conservación bajo filtros finitos son propiedades distintas. Ninguna de ellas, por separado ni bajo el conjunto amplio de hipótesis anterior, determina la línea crítica. La condición aritmética particular de Akatsuka exige controlar una magnitud infinita específica; demostrar esa cota sigue siendo equivalente a RH.

## 7. Radio, fase y dato suplementario

Para un cero hipotético $\rho=\beta+i\gamma$, el multiplicador de herencia es

$$
\lambda_p(\rho)=1-p^{-\rho},\qquad
r_p(\rho)=\left|p^{-\rho}\right|=p^{-\beta}.\tag{R03.9}
$$

La amplitud del multiplicador completo depende también de la fase:

$$
\left|\lambda_p(\rho)\right|^2
=1+p^{-2\beta}-2p^{-\beta}\cos(\gamma\log p).\tag{R03.10}
$$

**Alcance de «radio».** En (R03.9), $r_p$ es el módulo de $p^{-\rho}$ en el plano complejo, no el radio relacional de accesibilidad de los laboratorios de gravedad o computación. Tampoco define una magnitud energética.

El radio $r_p$ y el módulo $|\lambda_p|$ son objetos diferentes. Para cualquier primo fijo $p$, el enunciado «$r_p(\rho)=p^{-1/2}$ para todo cero no trivial $\rho$» equivale a $\mathrm{Re}(\rho)=\tfrac12$ para todos ellos: es una reformulación de la hipótesis de Riemann.

La frase «un número por cero» se refiere al número de **parámetros reales necesarios para describir la órbita simétrica**: en la línea basta la altura $\gamma$; fuera de ella hace falta también $\beta$. Es un conteo de parámetros continuos; su relación con un conteo de bits o con un costo de cómputo queda por establecer.

## 8. La obligación matemática, precisada

La versión 0.2 pedía un funcional $Q$, construido con las discrepancias $E_S$, que excluyera los modos fuera de la línea. La Proposición 4 da una forma exacta de ese funcional: la discrepancia completa en el pivote, normalizada por $e^{\mathrm{li}(\sqrt{\vartheta(X)})}$. La obligación queda así:

> Demostrar, sin suponer la hipótesis de Riemann, una constante $c>0$ tal que $\left|F_{S_X}(\tfrac12)\right|\,e^{\mathrm{li}(\vartheta(X)^{1/2})}\ge c$ para todo $X\ge3$.

Por la Proposición 4, ese enunciado es equivalente a la hipótesis de Riemann: la reformulación ubica el problema en el objeto del programa, con la misma dificultad. En términos de primos, pide controlar $\sum_{p\le X}-\log(1-p^{-1/2})$ frente a $\mathrm{li}(\vartheta(X)^{1/2})$ con un error acotado superiormente.

La **dispersión cuadrática por período** de R–01/R–02 —denominada allí «energía por período» por analogía matemática— se expresa por

$$
\langle E_k^2\rangle=\frac{2^k\delta_k}{12},
\qquad
\langle E_k(x)\,E_k(x/p)\rangle=\frac1p\,\langle E_k^2\rangle.
$$

Estas son mediciones de dispersión y correlación sobre períodos completos; no definen energía física ni granularidad. La granularidad pertenece a las distinciones accesibles bajo una referencia; el radio delimita un dominio de observación. La Proposición 4, en cambio, se apoya en una transformada de Mellin en el pivote $s=1/2$, cuyo integrando lleva el peso $x^{-3/2}$.

El **laboratorio separado de medición entre configuraciones** usa

$$
G_{S,T}=\int_0^\infty\frac{E_S(x)E_T(x)}{x^2}\,dx
=\int_0^\infty h_S(t)h_T(t)\,dt,
\qquad h_S(t)=-E_S(1/t).
$$

Este peso $x^{-2}$ proviene del cambio de variable $t=1/x$; **no es el peso del pivote** ni una ley física. La interpretación, procedencia y las verificaciones del laboratorio se documentan en el archivo complementario `PUENTE_GRAM_MEDICION_ES.md`.

### Protocolo de verificación

1. Integrar independientemente $E_S(x)$ sobre intervalos de longitud uno, acotar la cola y contrastar con (R03.1); calcular el término principal de la cola y restarlo.
2. Verificar el factor no nulo en ceros conocidos; esta comprobación es ilustrativa.
3. Verificar las simetrías y los ceros de $H$ y de $\widehat H_S$, y la pérdida de reflexión de $H\,P_S$.
4. Verificar la ecuación funcional de Davenport–Heilbronn, sus ceros sobre y fuera de la línea y la no multiplicatividad de sus coeficientes.
5. Medir $|P_S(\sigma)|^{-1}$ al crecer $S$, y $E_1(X)$ en el pivote hasta $X=10^8$.
6. Mantener separadas la prueba simbólica, el control numérico y el problema abierto.

### Resultado de la integración independiente

El script calcula $A_S(n)$ directamente por coprimalidad, integra exactamente en cada tramo entero la función lineal $E_S(x)=A_S(n)-\delta_S x$ (en punto flotante) y acota la cola por periodicidad y media cero. Se evaluaron $S=\lbrace2\rbrace$, $\lbrace2,3\rbrace$ y $\lbrace2,3,5\rbrace$ en $s=0{,}7$ y $s=0{,}7+2{,}4i$, con corte $N=240\,000$, múltiplo de los tres períodos.

La diferencia frente a la expresión de Mellin tiene como término principal de la cola, $\langle G\rangle N^{-s-1}$, donde $\langle G\rangle$ es la media sobre un período de $G(y)=\int_0^y E_S$; por eso el módulo observado es prácticamente igual en los dos valores de $s$ ($5{,}95\cdot10^{-11}$, $1{,}19\cdot10^{-10}$ y $4{,}76\cdot10^{-10}$). El script calcula $\langle G\rangle$ en aritmética racional y lo resta: la diferencia restante es a lo sumo $9\cdot10^{-15}$ en los seis casos, por debajo de la cota analítica del resto de segundo orden más un margen de $10^{-13}$ para el redondeo. La comprobación es independiente del cálculo de $F_S$ por el lado derecho de (R03.1) y acompaña a la demostración de la identidad.

## 9. Registro de resultados

| Afirmación | Estado |
|:--|:--|
| Ceros de $F_S$ y $\zeta$ idénticos, con multiplicidades, para $S$ finito | **Demostrado**, corolario de Mellin |
| Recuperación normalizada $F_S/P_S=\zeta/s$ | **Demostrado** |
| Cotas de estabilidad y pérdida de uniformidad al crecer $S$ | **Demostrado** |
| RH equivale a que $E_1$ esté acotada, y a $E_1\to-\sqrt2\,\zeta(\tfrac12)$ | **Conocido** (Akatsuka, 2024, Teorema 3) |
| RH equivale a la cota inferior de la discrepancia completa en el pivote, con límite $-\sqrt2$ | **Demostrado** (Proposición 4) |
| $E_1(X)$ decrece de $3{,}19$ a $2{,}19$ entre $X=10^2$ y $10^8$ | **Verificado**; compatible con RH en ese rango |
| Las dos simetrías y los filtros finitos dejan libre la ubicación de los ceros | **Demostrado** (control mínimo) |
| Serie de Dirichlet con ecuación funcional y ceros fuera de la línea, sin producto de Euler | **Conocido** (Davenport–Heilbronn; Spira); **verificado** |
| Control reforzado: simetría y producto de Euler no bastan sin hipótesis adicionales | **Demostrado** por construcción desplazada, no prueba de RH |
| Puente exacto a Nyman–Beurling con índices libres de cuadrados | **Demostrado**; criterio RH equivalente conocido por Báez-Duarte (2003) |
| Integración independiente de Mellin; término principal asintótico de la cola | **Verificado** |
| Todos los ceros de $\zeta$ en la línea $\mathrm{Re}(s)=\tfrac12$ | **Abierto**, hipótesis de Riemann |
| Cota inferior de la Proposición 4 sin suponer RH | **Abierto**, equivalente a RH |
| Reducción demostrada del costo total de reconocer los ceros | **Abierto** |


## 10. Puente exacto con el criterio funcional del 1 de noviembre

La transcripción de lectura de la nota previa *R–RH–01 — Primos, reflexión y cierre* emplea las funciones $f_n(t)=\{1/(nt)\}$ y el criterio de Nyman–Beurling/Báez-Duarte, cuyo cierre completo equivale a RH. La discrepancia de la criba es una combinación **exacta** de esas funciones cuando se invierte la referencia.

**Proposición 6 (puente de inversión).** Para cada conjunto finito $S$ de primos, incluido $S=\varnothing$, si $M_S=\prod_{p\in S}p$ y $h_S(t)=-E_S(1/t)$, entonces

$$
\boxed{h_S(t)=\sum_{d\mid M_S}\mu(d)f_d(t).}\tag{R03.16}
$$

En consecuencia,

$$
\boxed{\|h_S\|_{L^2(0,\infty)}^2=\int_0^\infty\frac{|E_S(y)|^2}{y^2}\,dy.}\tag{R03.17}
$$

*Demostración.* La identidad de inclusión-exclusión es $A_S(y)=\sum_{d\mid M_S}\mu(d)\lfloor y/d\rfloor$ y $\delta_S=\sum_{d\mid M_S}\mu(d)/d$. Por tanto $E_S(y)=-\sum_{d\mid M_S}\mu(d)\{y/d\}$. Sustituyendo $y=1/t$ resulta (R03.16). El cambio de variable $y=1/t$ en la norma prueba (R03.17), y la convergencia sigue de $E_S(y)=O_S(1)$ al infinito y $E_S(y)=-y\delta_S$ cerca de cero. $\square$

**Corolario 6.1 (alcance exacto de las firmas).** Al variar $S$ entre conjuntos finitos de primos, el espacio vectorial **algebraico** generado por $h_S$ es exactamente el generado por $f_d$ con $d$ libre de cuadrados. En efecto, la inversión sobre el retículo de subconjuntos proporciona, para cada producto $d_S=\prod_{p\in S}p$,

$$
f_{d_S}(t)=\sum_{T\subseteq S}(-1)^{|T|}h_T(t).\tag{R03.18}
$$

La familia de todas las $f_n$ contiene además índices con potencias primas repetidas, por ejemplo $f_4$. **El cierre de la familia libre de cuadrados puede ser diferente del cierre completo; aquí no se demuestra su igualdad.** Más aún, $f_{p^2}$ no es una combinación **finita** de las $f_d$ de índice libre de cuadrados: bajo Mellin ello exigiría que la función $p^{-2s}$ fuera un polinomio de Dirichlet finito con exponentes $\log d$ distintos, lo que contradice la independencia lineal de las funciones exponenciales.

**Corolario 6.2 (criterio de cierre escrito con la criba; conocido por reducción).** Sea $\chi=\mathbf1_{(0,1]}$. Entonces

$$
\boxed{\mathrm{RH}\iff \chi\in\overline{\operatorname{span}\{h_S:S\subset\mathbb P\text{ finito}\}}^{L^2(0,\infty)}.}\tag{R03.19}
$$

*Demostración.* Báez-Duarte (2002, segunda nota, Proposición 3.1, atribuida a M. Balazard) muestra que, **bajo RH**, existen aproximaciones a $\chi$ con coeficientes proporcionales a $\mu(n)\exp[-c\log n/\log\log N]$ y error $O((\log\log N)^{-1/3})$ en $L^2$. Los términos con $\mu(n)\ne0$ tienen índices libres de cuadrados y, por el Corolario 6.1, cada suma finita pertenece a $\operatorname{span}\{h_S\}$. En sentido inverso, el cierre de esos $h_S$ está contenido en el generado por **todas** las $f_n$; el Teorema 1.1 de Báez-Duarte (2002/2003) implica RH si $\chi$ pertenece a ese cierre. $\square$

El corolario **no es una nueva caracterización original**: presenta en el lenguaje de la discrepancia una consecuencia del criterio y de sus aproximantes de Möbius ya publicados. Puede estudiarse por separado si los dos **espacios completos** (libres de cuadrados y todos los índices) coinciden; esa igualdad no es necesaria para el corolario y no se demuestra aquí. No se obtiene incondicionalmente la convergencia ni el costo de construir sus aproximaciones.

**Aporte para el programa:** el puente alinea exactamente discrepancia, referencia inversa y el criterio de cierre ya presente en R–RH–01. El objetivo ya identificado no necesita volver a formularse: **demostrar sin suponer RH que la distancia de $\chi$ a ese espacio tienda a cero**. Ese paso sigue abierto.

## Referencias y procedencia

- [R–01/R–02, «Las escalas relacionales de la criba», edición publicada del 17-XI-2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md), §3, Proposición 1; §5, Proposición 2; §7, fórmula explícita.
- [«Un número por cero», edición publicada](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/REFLEXION_UN_NUMERO_POR_CERO_ES.md), §§4–8 y 11–13: radio, espejo y lectura del dato suplementario.
- H. Akatsuka (2024). *Maximal order for divisor functions and zeros of the Riemann zeta-function.* [arXiv:2411.19259](https://arxiv.org/abs/2411.19259), Teorema 3.
- H. Akatsuka (2017). *The Euler product for the Riemann zeta-function in the critical strip.* Kodai Math. J. 40, 79–101.
- H. Davenport y H. Heilbronn (1936). *On the zeros of certain Dirichlet series.* J. London Math. Soc. 11.
- R. Spira (1994). *Some zeros of the Titchmarsh counterexample.* Math. Comp. 63, 747–748.
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, §2.1, para la identidad clásica de Mellin.
- H. Davenport, *Multiplicative Number Theory*, para las propiedades de la función zeta y el producto de Euler.

- L. Báez-Duarte (2003), [*A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis*](https://arxiv.org/abs/math/0202141), Teorema 1.1 (criterio de cierre).
- L. Báez-Duarte (2002), [*A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis, 2*](https://arxiv.org/abs/math/0205003), Proposición 3.1 de M. Balazard (aproximantes ponderados y cota condicional).
- R–RH–01 (1-XI-2026), *Primos, reflexión y cierre* (nota anterior del programa; transcripción de lectura, original pendiente de cotejo).

**Firma pública:** Le Matt Ansatz Di Ego.

**Nota de alcance.** R–03 explicita y controla los mecanismos de la publicación anterior, y escribe con sus objetos una equivalencia conocida de la hipótesis de Riemann. Las identidades y los teoremas citados son clásicos o de sus autores; la hipótesis de Riemann permanece abierta.
