---
title: "Memoria del bit, equilibrio periódico y trayectoria autorreferenciada"
subtitle: "Consecuencias exactas de la herencia por octavas en la aritmética de Riemann"
author: "Endless Monkey Project / Relational Geometry Program"
date: 2026-11-22
lang: es-CR
status: "Identidades y desigualdades demostradas; condición cuantitativa equivalente a RH identificada"
---

# Memoria del bit, equilibrio periódico y trayectoria autorreferenciada

**Nota de continuidad matemática · 22 de noviembre de 2026 · Texto para revisión**

## Resumen

La reflexión, la diferencia binaria y la herencia forman el orden conceptual de partida. En la realización aritmética estudiada, la duplicación transporta **exactamente** el acarreo de cada potencia de dos a la potencia inmediata superior, conservando la suma de esas contribuciones. En las demás referencias primas, las activaciones periódicas poseen correlaciones ya determinadas en trabajos previos. A partir de estas correlaciones se demuestra aquí una **cota cuadrática media** para el conjunto de ciclos con frontera fija: su desviación típica, dividida entre la escala, tiende a cero. También se cuantifica la singularidad *de muestreo* de la trayectoria autorreferenciada $t=X$: su separación respecto de la media del ciclo fijo es asintóticamente lineal y supera un número creciente de desviaciones típicas. La desviación normalizada de los retornos aritméticos reales tiende a cero por el teorema clásico de los números primos; el exponente requerido por Riemann exige una cota cuantitativa adicional. La presente nota reúne consecuencias algebraicas de resultados anteriores sin convertir los promedios de ciclos en una estimación sobre la trayectoria seleccionada.

## 1. Bit de acarreo y referencias

Para $q=p^a$, con $p$ primo y $a\ge1$, se define

\[
c_q(t)=\left\lfloor\frac{2t}{q}\right\rfloor-2\left\lfloor\frac tq\right\rfloor
=\mathbf1_{\{2(t\bmod q)\ge q\}}\in\{0,1\}.
\tag{1}
\]

Sea $L(X)=\operatorname{mcm}(1,\ldots,X)$. Para $X\ge2$ fijo, el observable de fases heredadas es

\[
H_X(t)=\sum_{p^a\le X}(\log p)c_{p^a}(t).
\tag{2}
\]

Tiene período $L(X)$. La esperanza $\mathbb E_X$ y la varianza $\operatorname{Var}_X$ designan exclusivamente **el promedio uniforme de los enteros $t=0,\ldots,L(X)-1$**; se trata de una medida finita de conteo, no de un supuesto de aleatoriedad en los primos.

### Proposición 1 — Transporte exacto del bit por duplicación

Para todo $m,a\ge1$,

\[
\boxed{c_{2^{a+1}}(2m)=c_{2^a}(m),\qquad c_2(2m)=0.}
\tag{3}
\]

En consecuencia, al sumar sobre todas las potencias de dos,

\[
\boxed{\sum_{a\ge1}c_{2^a}(2m)=\sum_{a\ge1}c_{2^a}(m)=s_2(m),}
\tag{4}
\]

donde $s_2(m)$ es la cantidad de dígitos uno en la escritura binaria de $m$; las sumas son finitas porque los indicadores se anulan cuando $2^a>2m$. La **parte heredada del coeficiente binomial central**, $B(m)$, tiene un corte distinto y satisface $v_2(B(m))=s_2(m)-1$.

**Demostración.** El indicador $c_{2^a}(m)$ lee el dígito binario de peso $2^{a-1}$ de $m$. Multiplicar $m$ por dos desplaza ese dígito exactamente una posición, lo que da (3). Como $2m$ es par, $c_2(2m)=0$, y la suma se transporta por un cambio de índice. La suma de los indicadores $c_{2^a}(m)$ sobre todas las potencias de dos registra exactamente todos los dígitos uno de $m$; de ahí (4). La propiedad de $B(m)$ procede de la separación de la potencia nueva en $(m,2m]$, demostrada anteriormente. $\square$

Este resultado precisa la expresión «se conserva el bit»: **se conserva por transporte entre referencias, no porque permanezca fijo el indicador de un módulo individual**.

## 2. Equilibrio cuadrático de un sistema de referencias fijadas

La media de un indicador es

\[
\alpha_q=\mathbb E_X[c_q]=\frac{\lfloor q/2\rfloor}{q}.
\]

Para módulos de bases primas diferentes, los indicadores son independientes sobre un período común, por el teorema chino del resto. Entre potencias distintas $2^a,2^b$ la covarianza es cero. Para $q=p^a<Q=p^b$ con $p$ impar, las correlaciones heredadas del análisis del 21 de noviembre satisfacen

\[
\boxed{\operatorname{Cov}_X(c_q,c_Q)=\frac{q^2-1}{4qQ}.}
\tag{5}
\]

Estas son identidades de conteo bajo la medida finita definida arriba.

### Proposición 2 — Cota exacta de segundo momento

Para todo entero $X\ge2$,

\[
\boxed{\operatorname{Var}_X(H_X)
\le\frac12\sum_{p^a\le X}(\log p)^2
\le\frac12\psi(X)\log X.}
\tag{6}
\]

**Demostración.** Escribimos $A_p=\max\{a:p^a\le X\}$. Los términos de varianza de cada indicador son $\alpha_q(1-\alpha_q)\le1/4$. Las covarianzas entre bases distintas son cero. Para una misma base impar $p$, usando (5) y $q=p^a,Q=p^b$,

\[
2\sum_{1\le a<b\le A_p}\!\operatorname{Cov}(c_{p^a},c_{p^b})
\le\frac12\sum_{1\le a<b\le A_p}p^{a-b}
\le\frac{A_p}{2(p-1)}.
\]

La contribución de la base $p$ queda acotada por $(\log p)^2 A_p(\frac14+\frac1{2(p-1)})\le\frac12 A_p(\log p)^2$ para $p$ impar. Para $p=2$, las covarianzas cruzadas son cero y la misma cota vale. Sumando sobre las bases primas se obtiene la primera desigualdad. Para cada $p^a\le X$, $\log p\le\log X$; por definición $\psi(X)=\sum_{p^a\le X}\log p$, de donde la segunda desigualdad. $\square$

**Corolario 2.1 — Unidad normalizada en promedio.** Sea $\sigma_X^2=\operatorname{Var}_X(H_X)$. Por el teorema clásico de los números primos, $\psi(X)\sim X$. Entonces

\[
\boxed{\frac{\sigma_X}{X}=O\!\left(\sqrt{\frac{\log X}{X}}\right)\to0.}
\tag{7}
\]

En un período completo de referencias **fijas**, la anchura cuadrática media relativa a la escala desaparece. Por la desigualdad de Chebyshev, para $\lambda>0$,

\[
\frac1{L(X)}\#\{0\le t<L(X):|H_X(t)-\mu_X|\ge\lambda X\}
\le\frac{\psi(X)\log X}{2\lambda^2X^2},
\tag{8}
\]

donde $\mu_X=\mathbb E_X[H_X]$. Esto cuantifica el equilibrio de los ciclos enteros mediante una desigualdad matemática explícita.

## 3. La trayectoria autorreferenciada es distinguible del ciclo fijo

El observable aritmético usado en la descomposición de los coeficientes binomiales es la **diagonal**

\[
H(X)=H_X(X)=\log\binom{2X}{X}-[\psi(2X)-\psi(X)].
\tag{9}
\]

Su media con referencias fijas vale

\[
\mu_X=\frac12\psi(X)
-\frac12\sum_{\substack{p^a\le X\\p\ \mathrm{impar}}}\frac{\log p}{p^a}.
\tag{10}
\]

### Proposición 3 — Separación lineal de la trayectoria seleccionada

Se cumple el límite incondicional

\[
\boxed{\lim_{X\to\infty}\frac{\mu_X-H_X(X)}{X}
=\frac32-2\log2=0.11370563888\ldots>0.}
\tag{11}
\]

En particular, si $\sigma_X>0$,

\[
\boxed{\frac{|H_X(X)-\mu_X|}{\sigma_X}\longrightarrow\infty.}
\tag{12}
\]

**Demostración.** Como $\sum_{p^a\le X,\,p\text{ impar}}(\log p)/p^a\le\sum_{n\le X}(\log n)/n=O(\log^2X)$, el teorema de los números primos implica $\mu_X=\frac12X+o(X)$. Por Stirling, $\log\binom{2X}{X}=2X\log2+O(\log X)$ y, por el mismo teorema de los números primos, $\psi(2X)-\psi(X)=X+o(X)$. Por tanto $H_X(X)=(2\log2-1)X+o(X)$. Restar da (11). La cota (6) implica $\sigma_X=O(\sqrt{X\log X})$; al dividir una cantidad asintóticamente lineal entre una de ese orden, se obtiene (12). $\square$

**Interpretación matemática.** La configuración $t=X$ es una posición especial seleccionada simultáneamente con la frontera de referencias. El equilibrio de un período completo y el comportamiento de esta posición coexisten en la misma aritmética: el primero mide la distribución sobre todas las fases, mientras que el segundo sigue la **memoria autorreferenciada de cada nueva escala**. La palabra «singularidad» se conserva para su definición ontológica previa; el hecho aquí demostrado es la atipicidad **de muestreo** de una trayectoria aritmética, sin atribuirle singularidad analítica o física.

## 4. Retorno entre octavas y desviación aritmética

Sea $a=2\log2-1$ y

\[
\mathfrak D(m)=H(2m)-H(m)-am,
\qquad E(x)=\psi(x)-x.
\]

La identidad exacta es

\[
\boxed{\mathfrak D(m)=-E(4m)+2E(2m)-E(m)+\varepsilon_m,}
\tag{13}
\]

con término explícito

\[
\varepsilon_m=\log\frac{\binom{4m}{2m}}{\binom{2m}{m}}-2m\log2
=-\frac12\log2+O(m^{-1}).
\tag{14}
\]

La estimación clásica de von Koch, junto con la iteración diádica de la segunda diferencia, ofrece el criterio

\[
\boxed{\mathrm{RH}\iff\mathfrak D(m)=O(\sqrt m\log^2m).}
\tag{15}
\]

De modo incondicional, el teorema clásico de los números primos ya da

\[
\boxed{\frac{\mathfrak D(m)}m\longrightarrow0.}
\tag{16}
\]

Este último límite establece que la **diferencia normalizada del retorno efectivamente se agota**. La precisión exigida en (15) especifica la tasa de agotamiento. La reflexión geométrica conserva la norma en su propio contrato; las identidades (3), (6) y (13) expresan distintas leyes matemáticas de herencia, promedio y retorno en la aritmética.

## 5. Próximo contrato verificable

La siguiente investigación debe analizar la **trayectoria con frontera móvil** usando la herencia completa de las activaciones: las nuevas potencias primas, los cambios de fase de potencias impares, y el traslado exacto de los bits binarios. El resultado buscado es una cota uniforme para el término de la segunda diferencia en (13), obtenida de desigualdades aritméticas comprobables y sin suponer previamente su conclusión.

Una cota promedio como (6) proporciona control de ciclos enteros. Para transportar esa información a la trayectoria $t=X$ se necesita una **estimación determinista de muestreo** que respete la dependencia entre fase y frontera. El sesgo lineal demostrado en (11) fija un control adversarial específico para esa estimación: cualquier candidato debe reproducir primero ese término y luego controlar su fluctuación sublineal.

El programa conserva así una secuencia única de trabajo: **reflexión → distinción mínima → herencia → repetición → normalización → estimación del retorno**. Las proposiciones 1–3 y la ley (16) son resultados exactos o consecuencias de teoremas clásicos; (15) es una equivalencia a una condición global que requiere demostración aritmética independiente.

## Procedencia y control

- *Incertidumbre orientacional y octavas relacionales en el espectro de Mersenne*, mayo de 2026; $M_{2k}=M_k(2^k+1)$ y bits orientacionales bajo un postulado declarado.
- *La reflexión*, septiembre de 2026; *El hilo*, octubre de 2026.
- *NOTA_DE_CONTINUIDAD.md*, 21-XI-2026: periodicidad, correlaciones exactas, memoria prima y frontera móvil.
- *MARCO_FORMAL_DERIVACION_2026-11-21.md*, proposiciones D1–D7.
- *Reflexión, unidad conservada y precisión del retorno*, 22-XI-2026, ecuaciones (1)–(11).
- Resultados clásicos usados: teorema chino del resto, fórmula de Legendre, teorema de los números primos, fórmula de Stirling y criterio de von Koch.

**Reproducibilidad.** `verificar_memoria.py` comprueba con fracciones racionales las covarianzas para pares de potencias primas, el desplazamiento binario entre octavas y la desigualdad (6) en escalas finitas; muestra también la separación diagonal y contrasta momentos teóricos con promedios sobre períodos completos pequeños. `RESULTADOS.txt` contiene la ejecución. Las proposiciones universales se justifican por las demostraciones anteriores.

---

Endless Monkey Project / Relational Geometry Program
