# R–03 · Herencia espectral, normalización y ubicación de los ceros

**Continuación de R–01 / R–02 · Documento de examen, v0.3 · 18 de noviembre de 2026**  
**Endless Monkey Project**  
Relational Geometry Program  
**Le Matt Ansatz Di Ego**

## Resumen

La transformada de Mellin de la discrepancia de criba conserva los ceros de la función zeta bajo cualquier referencia formada por un número finito de primos. La conservación es exacta y reversible dentro de la franja crítica abierta. Este examen estudia cuatro consecuencias: la normalización que recupera la referencia común, la estabilidad de esa recuperación, el costo de la inversión en el pivote $s=\tfrac12$ cuando la referencia incorpora todos los primos hasta $X$, y la separación entre simetría y localización mediante dos modelos de control.

En el pivote, el costo de la inversión tiene una normalización exacta que equivale a la hipótesis de Riemann (Akatsuka, 2024). Escrita con la discrepancia de la criba, la hipótesis de Riemann es una cota inferior para la discrepancia completa en el pivote. El laboratorio sigue esa cantidad hasta $X=10^8$. La hipótesis de Riemann permanece abierta.

**Palabras clave:** criba; herencia; transformada de Mellin; ceros de zeta; producto de Euler parcial; función de Davenport–Heilbronn; normalización.

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

La referencia normalizada es la misma para todas las colecciones finitas de primos. Es una invariancia exacta: evaluar $N_S$ sigue pidiendo conocer $F_S$ y $P_S$, u otra representación de costo verificable.

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

Esta proposición mide una parte del costo de reconstrucción. La sección siguiente la evalúa en el pivote, donde ese costo tiene una forma exacta.

## 5. Proposición 4 — El costo de la inversión en el pivote

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

## 6. Proposición 5 — Simetría y localización: dos controles

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

**Conclusión de los controles.** El control mínimo muestra que las dos simetrías y los filtros finitos dejan libre la ubicación de los ceros de una función holomorfa. El control estándar muestra lo mismo para una serie de Dirichlet con ecuación funcional del tipo de $\zeta$ y con ceros sobre la línea. Entre esos ingredientes, lo que separa a $\zeta$ de $f$ es el producto de Euler: en el programa, la herencia sobre **todos** los primos. La Proposición 4 es justamente un enunciado sobre la herencia completa en el pivote.

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

El radio $r_p$ y el módulo $|\lambda_p|$ son objetos diferentes. Para cualquier primo fijo $p$, el enunciado «$r_p(\rho)=p^{-1/2}$ para todo cero no trivial $\rho$» equivale a $\mathrm{Re}(\rho)=\tfrac12$ para todos ellos: es una reformulación de la hipótesis de Riemann.

La frase «un número por cero» se refiere al número de **parámetros reales necesarios para describir la órbita simétrica**: en la línea basta la altura $\gamma$; fuera de ella hace falta también $\beta$. Es un conteo de parámetros continuos; su relación con un conteo de bits o con un costo de cómputo queda por establecer.

## 8. La obligación matemática, precisada

La versión 0.2 pedía un funcional $Q$, construido con las discrepancias $E_S$, que excluyera los modos fuera de la línea. La Proposición 4 da una forma exacta de ese funcional: la discrepancia completa en el pivote, normalizada por $e^{\mathrm{li}(\sqrt{\vartheta(X)})}$. La obligación queda así:

> Demostrar, sin suponer la hipótesis de Riemann, una constante $c>0$ tal que $\left|F_{S_X}(\tfrac12)\right|\,e^{\mathrm{li}(\vartheta(X)^{1/2})}\ge c$ para todo $X\ge3$.

Por la Proposición 4, ese enunciado es equivalente a la hipótesis de Riemann: la reformulación ubica el problema en el objeto del programa, con la misma dificultad. En términos de primos, pide controlar $\sum_{p\le X}-\log(1-p^{-1/2})$ frente a $\mathrm{li}(\vartheta(X)^{1/2})$ con un error acotado superiormente.

La energía por período de R–01/R–02,

$$
\langle E_k^2\rangle=\frac{2^k\delta_k}{12},
\qquad
\langle E_k(x)\,E_k(x/p)\rangle=\frac1p\,\langle E_k^2\rangle,
$$

es una media sobre períodos completos, mientras que la Proposición 4 integra la discrepancia sobre todas las escalas con el peso del pivote. Relacionar ambas es un **candidato de laboratorio**.

### Protocolo de verificación

1. Integrar independientemente $E_S(x)$ sobre intervalos de longitud uno, acotar la cola y contrastar con (R03.1); calcular el término principal de la cola y restarlo.
2. Verificar el factor no nulo en ceros conocidos; esta comprobación es ilustrativa.
3. Verificar las simetrías y los ceros de $H$ y de $\widehat H_S$, y la pérdida de reflexión de $H\,P_S$.
4. Verificar la ecuación funcional de Davenport–Heilbronn, sus ceros sobre y fuera de la línea y la no multiplicatividad de sus coeficientes.
5. Medir $|P_S(\sigma)|^{-1}$ al crecer $S$, y $E_1(X)$ en el pivote hasta $X=10^8$.
6. Mantener separadas la prueba simbólica, el control numérico y el problema abierto.

### Resultado de la integración independiente

El script calcula $A_S(n)$ directamente por coprimalidad, integra exactamente en cada tramo entero la función lineal $E_S(x)=A_S(n)-\delta_S x$ (en punto flotante) y acota la cola por periodicidad y media cero. Se evaluaron $S=\lbrace2\rbrace$, $\lbrace2,3\rbrace$ y $\lbrace2,3,5\rbrace$ en $s=0{,}7$ y $s=0{,}7+2{,}4i$, con corte $N=240\,000$, múltiplo de los tres períodos.

La diferencia frente a la expresión de Mellin es exactamente el término principal de la cola, $\langle G\rangle N^{-s-1}$, donde $\langle G\rangle$ es la media sobre un período de $G(y)=\int_0^y E_S$; por eso la diferencia tiene el mismo módulo en los dos valores de $s$ ($5{,}95\cdot10^{-11}$, $1{,}19\cdot10^{-10}$ y $4{,}76\cdot10^{-10}$). El script calcula $\langle G\rangle$ en aritmética racional y lo resta: la diferencia restante es a lo sumo $9\cdot10^{-15}$ en los seis casos, por debajo de la cota analítica del resto de segundo orden más un margen de $10^{-13}$ para el redondeo. La comprobación es independiente del cálculo de $F_S$ por el lado derecho de (R03.1) y acompaña a la demostración de la identidad.

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
| Integración independiente de Mellin; la diferencia es el término principal de la cola | **Verificado** |
| Todos los ceros de $\zeta$ en la línea $\mathrm{Re}(s)=\tfrac12$ | **Abierto**, hipótesis de Riemann |
| Cota inferior de la Proposición 4 sin suponer RH | **Abierto**, equivalente a RH |
| Reducción demostrada del costo total de reconocer los ceros | **Abierto** |

## Referencias y procedencia

- [R–01/R–02, «Las escalas relacionales de la criba», edición publicada del 17-XI-2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md), §3, Proposición 1; §5, Proposición 2; §7, fórmula explícita.
- [«Un número por cero», edición publicada](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-17-escalas-relacionales-riemann-v1/2026-11-17_escalas_relacionales_riemann/REFLEXION_UN_NUMERO_POR_CERO_ES.md), §§4–8 y 11–13: radio, espejo y lectura del dato suplementario.
- H. Akatsuka (2024). *Maximal order for divisor functions and zeros of the Riemann zeta-function.* [arXiv:2411.19259](https://arxiv.org/abs/2411.19259), Teorema 3.
- H. Akatsuka (2017). *The Euler product for the Riemann zeta-function in the critical strip.* Kodai Math. J. 40, 79–101.
- H. Davenport y H. Heilbronn (1936). *On the zeros of certain Dirichlet series.* J. London Math. Soc. 11.
- R. Spira (1994). *Some zeros of the Titchmarsh counterexample.* Math. Comp. 63, 747–748.
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, §2.1, para la identidad clásica de Mellin.
- H. Davenport, *Multiplicative Number Theory*, para las propiedades de la función zeta y el producto de Euler.

**Firma pública:** Le Matt Ansatz Di Ego.

**Nota de alcance.** R–03 explicita y controla los mecanismos de la publicación anterior, y escribe con sus objetos una equivalencia conocida de la hipótesis de Riemann. Las identidades y los teoremas citados son clásicos o de sus autores; la hipótesis de Riemann permanece abierta.
