# De la primera aparición a la memoria aritmética entre escalas

**Formalización de continuidad · 21 de noviembre de 2026 · versión 1.0 (para revisión)**  
**Serie:** R–01 / R–02 → R–03 → HC–03 → aparición, herencia y acarreos  
**Objeto:** derivar las identidades de incorporación, reconstrucción, duplicación, memoria heredada y frecuencia de activaciones desde la factorización prima.  
**Estado:** proposiciones y cotas locales demostradas (hechos clásicos reorganizados); verificación finita reproducible; criterio global equivalente a la hipótesis de Riemann (RH) registrado mediante un resultado clásico; estimación global abierta.

## Resumen

Una referencia prima se incorpora cuando aparece una potencia prima. La factorización única conserva su genealogía en cada entero posterior. El mínimo común múltiplo hasta una escala codifica exactamente esas incorporaciones, y su logaritmo coincide con la función de Chebyshev \(\psi\). Al duplicar la escala \(m\to 2m\), el coeficiente binomial central se factoriza en un factor de incorporaciones \(A(m)\), libre de cuadrados, y un factor de memoria \(B(m)\), determinado por acarreos de potencias primas anteriores. La transición de \(B\) necesita únicamente dos consultas locales a potencias primas impares, además de un factor racional explícito. Las activaciones de diferentes primos se combinan exactamente por el teorema chino del resto sobre períodos completos; para cada potencia prima hay además una cota óptima de discrepancia en intervalos parciales. La estimación uniforme de la memoria con frontera creciente no se deduce de esas identidades; su forma equivalente a RH queda registrada con procedencia clásica.

**Criterio de conceptualización.** Las entidades del mecanismo son aparición, conservación, ampliación, combinación y herencia. Las diferencias con signo se emplean exclusivamente como instrumentos cuantitativos de comparación con una referencia declarada.

## 1. Definiciones

Sea \(\mathbb P\) el conjunto de los primos. Para \(n\ge1\) se definen

\[
L(0)=L(1)=1,\quad L(n)=\operatorname{mcm}(1,2,\ldots,n),\quad
r(n)=\frac{L(n)}{L(n-1)}.
\tag{1.1}
\]

Se adopta \(r(1)=1\). La función de von Mangoldt y la primera función de Chebyshev son

\[
\Lambda(n)=\begin{cases}\log p,&n=p^j,\ j\ge1,\\0,&\text{en otro caso},\end{cases}\qquad
\psi(x)=\sum_{n\le x}\Lambda(n).
\tag{1.2}
\]

Las funciones \(v_p\) representan la valuación prima habitual y \(s_2(n)\) el número de unos en la expansión binaria de \(n\).

## 2. Proposición 1 — Incorporación y reconstrucción

**Enunciado.** Para todo \(n\ge2\):

\[
\boxed{r(n)=\frac{n}{\gcd(n,L(n-1))}
=\begin{cases}p,&n=p^j,\ j\ge1,\\1,&\text{en los demás casos};\end{cases}}
\tag{2.1}
\]

\[
\boxed{n=\prod_{d\mid n}r(d)},\qquad
\boxed{\log L(n)=\sum_{d\le n}\log r(d)=\psi(n)}.
\tag{2.2}
\]

**Demostración.** La valuación \(v_p(L(n))\) es el mayor entero \(j\ge0\) que satisface \(p^j\le n\). Al avanzar de \(n-1\) a \(n\), la valuación aumenta una unidad únicamente si \(n=p^j\); por lo tanto el cociente de los m.c.m. es \(p\) en ese caso y 1 en los restantes. El cociente \(n/\gcd(n,L(n-1))\) tiene exactamente las mismas valuaciones. Para la reconstrucción, los divisores de \(n\) que aportan un factor \(p\) son \(p,p^2,\ldots,p^{v_p(n)}\); su producto aporta \(p^{v_p(n)}\). Finalmente, el producto telescópico de los \(r(d)\) es \(L(n)\), y \(\log r(d)=\Lambda(d)\). \(\square\)

**Corolario (acumulación factorial).** Para cada entero \(N\ge1\):

\[
\boxed{N!=\prod_{d=1}^{N}r(d)^{\lfloor N/d\rfloor}.}
\tag{2.3}
\]

En efecto, al multiplicar (2.2) para todos los enteros \(1\le n\le N\), el factor \(r(d)\) aparece una vez por cada múltiplo de \(d\) no mayor que \(N\). Esta fórmula es clásica y expresa exactamente la frecuencia de transmisión de una referencia.

## 3. Proposición 2 — La duplicación incorpora cada referencia a lo sumo una vez

Para \(m\ge1\), defínanse

\[
A(m)=\frac{L(2m)}{L(m)}=\prod_{m<d\le2m}r(d),\quad
C(m)=\binom{2m}{m},\quad B(m)=\frac{C(m)}{A(m)}.
\tag{3.1}
\]

**Enunciado.** \(A(m)\) es entero libre de cuadrados y satisface

\[
\boxed{\frac{A(m+1)}{A(m)}
=\frac{r(2m+1)r(2m+2)}{r(m+1)}}.
\tag{3.2}
\]

**Demostración.** Dos potencias consecutivas de un mismo primo tienen cociente \(p\ge2\), de modo que el intervalo \((m,2m]\) contiene como máximo una. Así, en el producto (3.1) cada primo tiene exponente 0 o 1. La fórmula de transición resulta al cancelar los factores de \(L(2m+2)/L(m+1)\) frente a \(L(2m)/L(m)\). \(\square\)

## 4. Proposición 3 — Factor heredado y acarreos

Para cada potencia prima \(q=p^j\) se define el indicador de activación

\[
c_q(m)=\mathbf1_{\{2(m\bmod q)\ge q\}}.
\tag{4.1}
\]

**Enunciado.** Para todo \(m\ge1\), \(B(m)\) es un entero positivo, y

\[
\boxed{C(m)=A(m)B(m)},\qquad
\boxed{B(m)=\prod_{p^j\le m}p^{c_{p^j}(m)}}.
\tag{4.2}
\]

**Demostración.** La fórmula de Legendre da

\[
v_p(C(m))=\sum_{j\ge1}\left(
\left\lfloor\frac{2m}{p^j}\right\rfloor
-2\left\lfloor\frac{m}{p^j}\right\rfloor\right).
\tag{4.3}
\]

Cada sumando es 0 o 1. Si \(p^j>m\), el sumando vale 1 exactamente cuando \(m<p^j\le 2m\), lo que corresponde al exponente aportado por \(A(m)\). Si \(p^j\le m\), escribir \(m=k p^j+t\), \(0\le t<p^j\), convierte el sumando en \(\lfloor 2t/p^j\rfloor=c_{p^j}(m)\). La diferencia de valuaciones entre \(C\) y \(A\) es, por tanto, el exponente del producto expresado en (4.2). Es un entero no negativo para todo \(p\), lo cual demuestra ambas afirmaciones. \(\square\)

**Corolario binario.** En todo \(m\ge1\),

\[
\boxed{v_2(B(m))=s_2(m)-1.}
\tag{4.4}
\]

La identidad de Legendre \(v_2(n!)=n-s_2(n)\) da \(v_2(C(m))=s_2(m)\), y \((m,2m]\) contiene exactamente una potencia de 2, por lo que \(v_2(A(m))=1\). Para \(2^J\le m<2^{J+1}\), se sigue el conteo exacto

\[
\#\{m:v_2(B(m))=k\}=\binom Jk,\quad 0\le k\le J.
\tag{4.5}
\]

## 5. Proposición 4 — Actualización unitaria de la memoria

Defínase \(r_{\mathrm{impar}}(n)=p\) si \(n\) es una potencia de un primo impar, y 1 en los demás casos.

**Enunciado.** Para cada \(m\ge1\),

\[
\boxed{\frac{B(m+1)}{B(m)}=
\frac{2(2m+1)}{m+1}\;
\frac{r_{\mathrm{impar}}(m+1)}{r(2m+1)}.}
\tag{5.1}
\]

**Demostración.** La identidad de factoriales da \(C(m+1)/C(m)=2(2m+1)/(m+1)\). Por (3.2),

\[
\frac{B(m+1)}{B(m)}=
\frac{2(2m+1)}{m+1}\cdot
\frac{r(m+1)}{r(2m+1)r(2m+2)}.
\]

La posición \(2m+2=2(m+1)\) es una potencia prima si y solo si \(m+1\) es una potencia de 2. En ese caso tanto \(r(m+1)\) como \(r(2m+2)\) son 2; en los demás casos \(r(2m+2)=1\). Por consiguiente, \(r(m+1)/r(2m+2)=r_{\mathrm{impar}}(m+1)\). \(\square\)

Esta identidad reduce la actualización de la memoria a un factor de escala y dos apariciones locales. Es una actualización exacta, sin que ello imponga una cota global de fluctuaciones.

## 6. Proposición 5 — Organización de las referencias por períodos

**Enunciado.** Para \(q=p^j\), la activación \(c_q(m)\) es periódica módulo \(q\), con exactamente \(a_q=\lfloor q/2\rfloor\) activaciones por período. Su promedio uniforme es

\[
\boxed{\mu_q=\frac{a_q}{q}}.
\tag{6.1}
\]

Si \(q=p^j\) y \(t=\ell^k\), con \(p\ne\ell\), entonces sobre un ciclo de \(qt\):

\[
\boxed{\sum_{m=0}^{qt-1}c_q(m)c_t(m)=a_q a_t.}
\tag{6.2}
\]

**Demostración.** Los residuos activados de \(c_q\) son \(\lceil q/2\rceil,\ldots,q-1\), que suman \(\lfloor q/2\rfloor\) posiciones. Para potencias de primos distintos, el teorema chino del resto da una biyección entre residuos módulo \(qt\) y parejas de residuos módulo \(q\) y \(t\); cada pareja de posiciones activas se presenta una sola vez. \(\square\)

La independencia obtenida es una propiedad de un **promedio finito en un ciclo completo**. Los niveles de potencia de un mismo primo pueden presentar dependencias: por ejemplo, el promedio de \(c_3c_9\) en los nueve residuos es \(2/9\), mientras que el producto de sus promedios es \(4/27\).

## 7. Proposición 6 — Discrepancia óptima para una referencia en una ventana

Para cualquier inicio entero \(u\), longitud entera \(N\ge0\) y potencia prima \(q\), se define

\[
D_q(u,N)=\sum_{m=u}^{u+N-1}c_q(m)-N\mu_q.
\tag{7.1}
\]

**Enunciado.** Sea \(a=\lfloor q/2\rfloor\), \(b=\lceil q/2\rceil\). Entonces

\[
\boxed{\left|D_q(u,N)\right|\le\frac{ab}{q}\le\frac q4.}
\tag{7.2}
\]

La constante \(ab/q\) es óptima para \(q\) fijo.

**Demostración.** En cada período hay un tramo consecutivo de \(b\) ceros seguido de uno de \(a\) unos. Al centrar respecto de \(\mu_q=a/q\), las sumas parciales en el tramo de ceros decrecen desde 0 hasta \(-ab/q\); en el tramo de unos vuelven desde \(-ab/q\) a 0. Todas las sumas parciales centradas de un período se hallan, por tanto, en \([-ab/q,0]\). La suma sobre cualquier intervalo es la diferencia de dos de esas sumas parciales, puesto que los períodos completos tienen suma centrada cero. De ahí (7.2). Tomar un intervalo formado exactamente por el tramo de \(b\) ceros alcanza el valor absoluto \(ab/q\). \(\square\)

**Consecuencia para frontera fija.** Sea \(Q\ge2\) y \(W_Q(m)=\sum_{p^j\le Q}(\log p)c_{p^j}(m)\). Con el promedio de ciclo completo \(\bar W_Q=\sum_{p^j\le Q}(\log p)\mu_{p^j}\), vale

\[
\boxed{\left|\sum_{m=u}^{u+N-1}W_Q(m)-N\bar W_Q\right|
\le\sum_{p^j\le Q}(\log p)
\frac{\lfloor p^j/2\rfloor\lceil p^j/2\rceil}{p^j}.}
\tag{7.3}
\]

**Demostración.** Aplicar (7.2) por separado a cada sumando y la desigualdad triangular. \(\square\)

La desigualdad (7.3) es incondicional pero puede ser amplia cuando \(Q\) crece: no prueba una ley de cancelación entre referencias. Además, en \(\log B(m)\) la frontera de potencias primas cambia con \(m\), mientras que \(W_Q\) utiliza una frontera fija.

## 8. Proposición 7 — Condición de precisión y vínculo clásico con RH

De (3.1) y (4.2) se obtiene la identidad exacta

\[
\boxed{\psi(2m)-\psi(m)=\log\binom{2m}{m}-\log B(m).}
\tag{8.1}
\]

Defínase la comparación de precisión del intervalo

\[
J(m)=\log\binom{2m}{m}-\log B(m)-m.
\tag{8.2}
\]

**Enunciado (equivalencia clásica reescrita).** La hipótesis de Riemann es equivalente a

\[
\boxed{J(m)=O(\sqrt m\log^2m)\quad (m\to\infty).}
\tag{8.3}
\]

Por la fórmula de Stirling para el binomial central, también equivale a

\[
\boxed{\log B(m)=(2\log2-1)m-\tfrac12\log(\pi m)
+O(\sqrt m\log^2m).}
\tag{8.4}
\]

**Demostración de equivalencia, no de la cota.** El criterio clásico de von Koch afirma \(\mathrm{RH}\iff\psi(x)=x+O(\sqrt{x}\log^2x)\). La dirección directa proporciona (8.3) al restar \(\psi(2m)\) y \(\psi(m)\). Para la recíproca, defínase \(E(n)=\psi(n)-n\). Si \(n=2m\), la identidad (8.2) da \(E(n)=E(m)+J(m)\); si \(n=2m+1\), da \(E(n)=E(m)+J(m)+\Lambda(n)-1\). Al iterar \(n\mapsto\lfloor n/2\rfloor\), se acumula una serie geométrica de términos \(O(\sqrt{n/2^j}\log^2n)\) y contribuciones de orden \(O(\log^2n)\), porque \(\Lambda(n)\le\log n\). Por tanto \(E(n)=O(\sqrt n\log^2n)\). Pasar de enteros a reales agrega a lo sumo \(O(\log x)\), y el criterio clásico implica RH. Finalmente, Stirling da \(\log\binom{2m}{m}=2m\log2-\tfrac12\log(\pi m)+O(m^{-1})\), lo cual convierte (8.3) en (8.4). \(\square\)

**Alcance.** Las proposiciones 1–6 demuestran identidades y controles aritméticos clásicos. La proposición 7 demuestra la **equivalencia lógica** entre una condición de precisión sobre \(B\) y un criterio clásico de RH. La estimación (8.3)/(8.4) **no ha sido obtenida** a partir de las proposiciones anteriores.

## 9. Procedencia, estado y falsadores

| Afirmación | Fundamento | Estado |
|:--|:--|:--|
| Incorporación \(r(n)\), reconstrucción de \(n\), factorial y \(\psi\) | Factorización prima, von Mangoldt, m.c.m. | Clásico, demostrado aquí |
| \(A(m)\) libre de cuadrados; actualización unitaria | Propiedades de las potencias primas | Demostrado aquí |
| \(B(m)\) y fórmula por acarreos | Fórmulas de Legendre y Kummer | Clásico, explicitado aquí |
| Distribuciones de activación sobre ciclos y fórmula binaria | Congruencias, CRT, identidad de Legendre | Clásico, demostrado aquí |
| Cota óptima de una referencia y cota por frontera fija | Tramos de activación, suma parcial, triangular | Demostrado aquí; local |
| Condición sobre \(B\) equivalente a RH | Von Koch y Stirling | Equivalencia, estimación abierta |
| Control uniforme de acarreos con frontera creciente | Requiere argumento aritmético adicional | **Abierto** |

**Control conceptual:** la independencia sobre ciclos completos no implica independencia dentro de una ventana parcial. La cota óptima por referencia tampoco determina el orden de una suma con número creciente de referencias. Los ejemplos finitos verifican igualdades, no cuantificadores infinitos ni la hipótesis de Riemann.

## 10. Reproducibilidad y continuidad

El script `verificar_marco.py` utiliza únicamente la biblioteca estándar de Python; contrasta por vías separadas las identidades (2.1)–(8.2), casos de la cota óptima (7.2), la activación conjunta CRT y el factor binario. La verificación numérica es un control de implementación de las fórmulas, no sustituye las demostraciones anteriores. El archivo `README.md` fija la ejecución y `MANIFEST.sha256` las huellas de entrega.

**Continuidad documental (sin sustitución de originales):**

- [R–01/R–02: escalas relacionales de la criba](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md).
- [R–03 v0.3: herencia espectral y localización](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/2026-11-18_r03_herencia_espectral/R03_HERENCIA_Y_LOCALIZACION_ES.md).
- HC–03 y notas de continuidad (21-XI-2026): documentos de laboratorio de los que se integran las definiciones y las identidades.
- Legendre; Kummer; teorema chino del resto; criterio clásico de von Koch para la hipótesis de Riemann.

**Endless Monkey Project / Relational Geometry Program**
