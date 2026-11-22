---
title: "Reflexión, unidad conservada y precisión del retorno"
subtitle: "Auditoría de transferencia desde el bit relacional y las octavas hasta la desviación aritmética"
author: "Endless Monkey Project / Relational Geometry Program"
date: 2026-11-22
lang: es-CR
status: "Identidades exactas y ejemplo de control demostrados; transferencia aritmética cuantitativa en investigación"
---

# Reflexión, unidad conservada y precisión del retorno

**Nota de continuidad · 22 de noviembre de 2026 · Para revisión matemática**

## Resumen

La unidad normalizada constituye una referencia común para las reflexiones, las identidades heredadas y las nuevas distinciones. En sus realizaciones matemáticas, una reflexión isométrica conserva la norma y una proyección ortogonal distribuye exactamente la energía entre componente reconocida y residuo. La rama aritmética permite expresar el retorno entre las escalas $m$ y $2m$ mediante la memoria de acarreos. El análisis distingue dos magnitudes diferentes: la *fracción normalizada* de una desviación y su *tasa de decrecimiento entre octavas*. Un ejemplo constructivo demuestra que una familia de ciclos con compensación periódica exacta, herencia íntegra y amplitud normalizada acotada puede presentar un desbalance no normalizado de orden lineal. El contrato matemático para la hipótesis de Riemann queda localizado en la tasa cuantitativa de la desviación aritmética del retorno.

## 1. Orden de procedencia

La formulación se obtiene por lectura de los antecedentes, en este orden:

1. **Reflexión e incertidumbre** (*La reflexión*, septiembre de 2026; *El hilo*, octubre de 2026): la primera diferencia abierta precede a su magnitud; la orientación binaria es una realización de la distinción mínima.
2. **Octavas** (*Incertidumbre orientacional y octavas relacionales en el espectro de Mersenne*, mayo de 2026): $M_{2k}=M_k(2^k+1)$, con $\gcd(M_k,2^k+1)=1$; herencia y complemento aparecen juntos en cada factorización.
3. **Granularidad y cierre** (20–21 de noviembre de 2026): el transporte de normalizadores, la conservación de consultas y las identidades de proyección tienen contratos específicos.
4. **Acarreos y retorno** (21–22 de noviembre de 2026): $B(m)$, las fases $c_q(m)$, la identidad $H(2m)-H(m)$ y el criterio diádico equivalente a Riemann están demostrados como identidades y equivalencias, respectivamente.

En este texto **reflexión geométrica**, **cambio de módulo** y **duplicación del argumento** siguen siendo operaciones matemáticas distintas. Se comparan mediante invariantes expresamente indicados.

## 2. La unidad y sus reflejos: ley exacta

**Proposición 1 — Conservación y reparto.** En un espacio de Hilbert $\mathcal H$, sean $R$ una isometría y $P$ un proyector ortogonal. Para todo $v\in\mathcal H$:

\[
\boxed{\|Rv\|^2=\|v\|^2,\qquad
\|Pv\|^2+\|(I-P)v\|^2=\|v\|^2.}\tag{1}
\]

**Prueba.** La primera igualdad es la definición de isometría. La segunda resulta de la ortogonalidad $Pv\perp(I-P)v$ y el teorema de Pitágoras. $\square$

Bajo $\|v\|=1$, todas las componentes proyectadas quedan dentro de esa unidad. Una nueva referencia puede aumentar la parte reconocida y disminuir el resto, conservando la suma cuadrática. Esta es una realización precisa de la normalización y de la información referenciada.

Una identidad que se sostiene por referencias internas puede conservar diferencias aun cuando se represente exteriormente como una sola unidad. La información disponible para una consulta exterior depende de qué relaciones preserva su interfaz. Esta observación recupera el sentido ontológico de *singularidad* sin identificarlo con un punto singular de una función analítica.

**Corolario — Reflexión recuperadora.** Sean $W_m\subset W_n$ espacios anidados, $r_m=(I-P_m)\chi$, $Q=P_n-P_m$ y $\mathscr R=I-2Q$. Entonces

\[
\boxed{\|r_m\|^2-\|r_n\|^2
=\|Qr_m\|^2=\tfrac14\|r_m-\mathscr Rr_m\|^2.}\tag{2}
\]

La identidad coincide con el lema de *CME–RH–01* (21-XI-2026). Mide exactamente la fracción de la diferencia pendiente que una nueva referencia alcanza a distinguir.

## 3. El retorno aritmético: memoria conservada y diferencia normalizada

Sean $L(n)=\operatorname{mcm}(1,\dots,n)$, $\psi(x)=\sum_{n\le x}\Lambda(n)$ y $E(x)=\psi(x)-x$. Para $m\ge1$ se definen

\[
B(m)=\frac{\binom{2m}{m}}{L(2m)/L(m)},\quad H(m)=\log B(m),\quad a=2\log2-1.
\]

El **desbalance de retorno** es

\[
\boxed{\mathfrak D(m)=H(2m)-H(m)-am.}\tag{3}
\]

Por Legendre, $H(m)$ es una suma ponderada de bits de acarreo asociados a las potencias primas hasta $m$. En el retorno $m\mapsto2m$, los bits de potencias de dos se transportan exactamente; los cambios proceden de las fases de potencias impares ya heredadas y de las nuevas referencias impares.

Defínase $F(m)=H(m)-am$ y la **desviación normalizada por la unidad de escala**

\[
u(m)=\frac{F(m)}m.
\]

**Proposición 2 — Ecuación exacta de herencia normalizada.** Para todo $m\ge1$,

\[
\boxed{F(2m)=F(m)+\mathfrak D(m),\qquad
u(2m)=\frac12u(m)+\frac{\mathfrak D(m)}{2m}.}\tag{4}
\]

**Prueba.** La primera identidad es (3) reorganizada; dividir por $2m$ produce la segunda. $\square$

La ecuación (4) exhibe los dos componentes del retorno: el efecto de la **memoria heredada**, cuya fracción se divide entre dos al duplicar la referencia, y la **aportación del nuevo ciclo**, $\mathfrak D(m)/(2m)$. El límite relevante para Riemann es la tasa cuantitativa de esa aportación.

## 4. Qué se obtiene de una cota de unidad

**Proposición 3 — Alcance exacto de una amplitud normalizada.** Si $|\nu(m)|\le K$ para todas las escalas consideradas, entonces

\[
\boxed{|\mathfrak D(m)|\le3Km.}\tag{5}
\]

**Prueba.** Por (4), $\mathfrak D(m)=m\,[2u(2m)-u(m)]$; aplicar la desigualdad triangular demuestra (5). $\square$

La conservación geométrica de la unidad determina, en este tipo de medición, una escala lineal de control. La precisión requerida por la hipótesis de Riemann es más fina: $\sqrt m\log^2m$. Esta distinción permite localizar el dato cuantitativo que debe transmitir una ley de herencia.

**Proposición 4 — Ciclos equilibrados y herencia exacta con desbalance lineal.** Para cada $k\ge1$ se define una función periódica de período $2^k$:

\[
h_k(t)=\mathbf 1_{\{t\equiv0\pmod{2^k}\}}-\mathbf 1_{\{t\equiv1\pmod{2^k}\}}.
\]

Cada ciclo tiene suma **exactamente cero** en su período completo. Para $t\ge2$ entero, sean

\[
D_*(t)=\sum_{2^k\le t}2^{k-2}h_k(t),\qquad u_*(t)=\frac{D_*(t)}t.
\]

Se cumplen

\[
\boxed{|u_*(t)|<\tfrac12\quad\text{para todo }t\ge2,\qquad
D_*(2^K)=\frac{2^K-1}{2}\quad(K\ge1).}\tag{6}
\]

**Prueba.** Hay una contribución $+1$ y otra $-1$ por ciclo. Por la desigualdad triangular, si $2^K\le t<2^{K+1}$,
$|D_*(t)|\le\sum_{k=1}^K2^{k-2}=(2^K-1)/2<t/2$. Si $t=2^K$, para todos $1\le k\le K$ se verifica $h_k(t)=1$, y la suma alcanza $(2^K-1)/2$. $\square$

Esta familia transporta íntegramente las referencias anteriores y agrega una sola referencia nueva en cada duplicación relevante. Cada ciclo está perfectamente compensado en un período completo, y el observable total permanece dentro de su unidad normalizada. Sin embargo, sobre la trayectoria de retorno $t=2^K$ su diferencia alcanza orden $t$. La construcción es un **control lógico de los supuestos de conservación y periodicidad**: no representa la distribución efectiva de las potencias primas ni invalida las identidades aritméticas documentadas.

## 5. Condición aritmética que determina la velocidad del retorno

De la identidad exacta

\[
H(m)=\log\binom{2m}{m}-\psi(2m)+\psi(m)
\]

y de Stirling se deduce

\[
\boxed{\mathfrak D(m)
=-E(4m)+2E(2m)-E(m)-\frac12\log2+O(m^{-1}).}\tag{7}
\]

Esta es una **segunda diferencia entre escalas diádicas** del error de Chebyshev. La equivalencia clásica de von Koch, junto con la regla de actualización aritmética entre enteros vecinos, da

\[
\boxed{\mathrm{RH}\iff
\mathfrak D(m)=O(\sqrt m\log^2m).}\tag{8}
\]

En términos de la fracción normalizada $\rho(m)=\mathfrak D(m)/m$, la condición es

\[
\boxed{|\rho(m)|\le C\,m^{-1/2}\log^2m}\tag{9}
\]

para alguna constante $C$ y toda escala suficientemente grande. Así, **el valor uno es el referente de conservación; la tasa $m^{-1/2}\log^2m$ es la precisión de retorno requerida**.

La expresión (9) debe deducirse de una propiedad aritmética verificable que vincule simultáneamente la herencia de las potencias primas y las fases de los acarreos, con frontera móvil. La ley de reflexión de módulos individuales y la igualdad de energía (1) ya proporcionan dos identidades del marco; (9) identifica la restricción cuantitativa adicional que debe estar acreditada para la familia aritmética completa.

## 6. Segunda representación de la unidad: la vía funcional

El contrato de aproximación de R–RH–01 emplea $\chi=\mathbf 1_{(0,1]}$ en $L^2(0,\infty)$, cuya norma cuadrática es exactamente $1$. Sean $W_j$ los subespacios anidados del criterio de Báez-Duarte, $P_j$ sus proyecciones y $e_j^2=\|(I-P_j)\chi\|_2^2$. En cada ampliación se cumple

\[
\boxed{1=\sum_{j=0}^{J-1}(e_j^2-e_{j+1}^2)+e_J^2}\tag{10}
\]

si $W_0=\{0\}$. La identidad conserva la unidad y reparte exactamente la información recuperada y la diferencia pendiente.

Para las escalas $2^j$, el coeficiente de recuperación definido en *CME–RH–01* satisface

\[
\gamma_j=\frac{e_{2^j}^2-e_{2^{j+1}}^2}{e_{2^j}^2}\in[0,1],\qquad
e_{2^J}^2=e_1^2\prod_{j=0}^{J-1}(1-\gamma_j).
\tag{11}
\]

Demostrar $\sum_j\gamma_j=\infty$ (o una recuperación completa en algún paso) sería una condición suficiente para que $e_j\to0$, equivalente a RH por el criterio clásico. En esta segunda representación, **la cuestión cuantitativa es qué fracción del resto alcanza a reconocer cada nueva referencia**, y su acumulación efectiva.

Las dos representaciones, (8) y (11), constituyen criterios clásicos de RH reexpresados mediante operaciones que aparecen en la investigación. Su equivalencia lógica respecto de RH no constituye por sí misma un morfismo entre operadores geométricos, bits aritméticos y proyectores funcionales; un mapa que conserve las consultas y sus normas es objeto de examen separado.

## 7. Síntesis técnica

Las identidades de reflexión y de proyección fijan la conservación de la unidad. Las octavas y los acarreos fijan qué referencias se heredan y cómo se incorporan diferencias. El control de la desviación aritmética requiere acreditar una **tasa de contracción de la diferencia normalizada** —o su equivalente funcional en ganancia acumulada— específica de la familia de referencias de los primos. Con ello el mecanismo fundacional y la condición matemática quedan conectados mediante una pregunta cuantitativa precisa, sin alterar los resultados anteriores.

### Procedencia

- *Incertidumbre orientacional y octavas relacionales en el espectro de Mersenne*, mayo de 2026.
- *La reflexión*, versión 0.2, septiembre de 2026.
- *El hilo*, octubre de 2026.
- *CME–RH–01*, *Granularidad, referencia y agotamiento del resto* y *Granularidad heredada y condición de cierre funcional*, 20–21-XI-2026.
- *Marco formal de derivación: aparición, herencia, acarreos y acumulación*, 21-XI-2026.
- *Retorno de escala, reflexión y herencia aritmética*, 22-XI-2026.

Endless Monkey Project / Relational Geometry Program
