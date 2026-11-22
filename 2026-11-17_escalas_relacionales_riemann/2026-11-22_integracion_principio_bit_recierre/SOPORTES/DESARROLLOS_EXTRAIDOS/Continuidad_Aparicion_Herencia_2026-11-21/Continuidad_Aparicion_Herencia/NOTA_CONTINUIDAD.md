# Aparición, herencia y transmisión entre escalas

**Nota de continuidad de R–01/R–02, R–03 y HC–03 · 21 de noviembre de 2026**  
**Objeto:** seguir las propiedades fijadas por las primeras apariciones hasta su expresión en la duplicación de escala, sin introducir una ley de cancelación como hipótesis.  
**Estado:** identidades y descomposiciones **demostradas**; controles exactos **ejecutados**; caracterización cuantitativa equivalente a RH **establecida por reducción a un criterio clásico**; su estimación **abierta**.

## Resumen

Toda incorporación prima queda registrada por la sucesión de enteros positivos
\[
 L(n)=\operatorname{mcm}(1,\ldots,n),\qquad r(n)=L(n)/L(n-1).
\]
La regla local es \(r(n)=p\) exactamente cuando \(n=p^j\), y \(r(n)=1\) para los restantes enteros. La duplicación de escala admite una separación positiva exacta:
\[
 \binom{2m}{m}=A(m)B(m),\qquad A(m)=\frac{L(2m)}{L(m)},\qquad
 B(m)=\prod_{\substack{p^j\le m\\2(m\bmod p^j)\ge p^j}}p.
\]
El factor \(A(m)\) es **libre de cuadrados**, pues cada primo puede renovar su potencia a lo sumo una vez entre \(m\) y \(2m\). El factor \(B(m)\) cuenta con multiplicidad las intervenciones de referencias anteriores en la acumulación factorial; en particular, \(v_2(B(m))=s_2(m)-1\), donde \(s_2\) es el número de cifras binarias iguales a 1. Por logaritmos se obtiene una condición exacta de precisión sobre la memoria \(B(m)\) equivalente al criterio clásico de RH. **La reducción no demuestra la estimación de precisión.**

La formulación conceptual es afirmativa: **aparición, conservación, ampliación y combinación**. Los signos de una comparación numérica son herramientas de medición, no una entidad generadora.

## 1. Incorporación desde las primeras apariciones

Para cada entero \(n\ge2\):
\[
 \boxed{r(n)=\frac{n}{\gcd(n,L(n-1))}}
 \quad\text{y}\quad
 \boxed{L(n)=L(n-1)\,r(n)}.\tag{1}
\]

**Demostración.** Para cada primo \(p\), el exponente de \(p\) en \(L(n)\) es el máximo \(j\) con \(p^j\le n\). Al pasar de \(n-1\) a \(n\), cambia un exponente si y solo si \(n\) es una potencia de ese primo, en cuyo caso aumenta una unidad. El cociente de (1) reproduce exactamente ese incremento. \(\square\)

Para todo \(n\ge2\), las incorporaciones de sus divisores reconstruyen el entero:
\[
 \boxed{n=\prod_{d\mid n}r(d)}.\tag{2}
\]
La identidad procede de que los divisores que son potencias de \(p\) son \(p,p^2,\ldots,p^{v_p(n)}\): cada uno aporta un factor \(p\). Como consecuencia,
\[
 \boxed{n!=\prod_{d\le n}r(d)^{\lfloor n/d\rfloor}}.\tag{3}
\]
El peso \(\lfloor n/d\rfloor\) es exactamente la cantidad de múltiplos de \(d\) contenidos en la escala \(n\).

La segunda diferencia mínima de HC–03 también tiene la expresión exacta
\[
 \boxed{\Delta^2T(n)=\frac{\log r(n)}{n}=\frac{\Lambda(n)}{n}},\qquad n\ge2,\tag{4}
\]
para \(T(x)=\sum_{k\le x}\Lambda(k)(x/k-1)\) y \(\Delta^2T(n)=T(n+1)-2T(n)+T(n-1)\). La misma referencia se reconoce tanto por la incorporación multiplicativa como por la diferencia mínima.

## 2. Primera consecuencia en la duplicación: incorporación sin repetición

Defínase
\[
 \boxed{A(m)=\prod_{m<d\le2m}r(d)=\frac{L(2m)}{L(m)}}.\tag{5}
\]

**Proposición 1 (una ampliación por referencia).** Para cada primo \(p\) y cada entero \(m\ge1\), en el intervalo \((m,2m]\) puede haber a lo sumo una potencia de \(p\). Por tanto, \(A(m)\) es libre de cuadrados.

**Demostración.** Si dos potencias consecutivas de \(p\) estuvieran dentro de \((m,2m]\), su cociente sería \(p\ge2\), y la segunda superaría \(2m\). Al registrar solo una posible incorporación \(r(p^j)=p\) de cada primo, todos los exponentes de \(A(m)\) son 0 o 1. \(\square\)

**Proposición 2 (transición de una unidad).** Para todo \(m\ge1\),
\[
 \boxed{\frac{A(m+1)}{A(m)}=
 \frac{r(2m+1)\,r(2m+2)}{r(m+1)}}.\tag{6}
\]

**Demostración.** Sustituir \(A(m)=L(2m)/L(m)\) y usar tres veces la regla (1). \(\square\)

La ecuación (6) determina la actualización de un intervalo completo a partir de tres posiciones locales. Es una identidad de transmisión, no una cota de fluctuación.

## 3. Segunda consecuencia: memoria combinatoria de las referencias anteriores

Sea \(C(m)=\binom{2m}{m}\), y defínase \(B(m)=C(m)/A(m)\).

**Proposición 3 (descomposición positiva exacta).** Para todo \(m\ge1\), \(B(m)\) es un entero positivo y
\[
 \boxed{B(m)=\prod_{\substack{p^j\le m\\2(m\bmod p^j)\ge p^j}}p}.\tag{7}
\]
En particular, todos sus factores son referencias ya presentes hasta la escala \(m\).

**Demostración.** Por la fórmula de Legendre, para cada primo \(p\),
\[
 v_p\!\binom{2m}{m}
 =\sum_{j\ge1}\left(\Big\lfloor\frac{2m}{p^j}\Big\rfloor
 -2\Big\lfloor\frac{m}{p^j}\Big\rfloor\right).
\]
Cada sumando es 0 o 1. Si \(p^j>m\), es 1 exactamente cuando \(m<p^j\le2m\); esto es el exponente de \(p\) que aporta \(A(m)\). Si \(p^j\le m\), la identidad \(m=q p^j+t\) con \(0\le t<p^j\) muestra que el sumando es 1 exactamente cuando \(2t\ge p^j\). Son los factores de (7). De aquí \(C(m)=A(m)B(m)\) con \(A,B\in\mathbb Z_{>0}\). \(\square\)

La regla de activación en (7) es la formulación por residuos de los **acarreos de Kummer** al sumar \(m+m\) en base \(p\). Describe las relaciones de la referencia anterior que participan en el nuevo conteo.

**Corolario 3.1 (memoria binaria).** Si \(s_2(m)\) es el número de unos de \(m\) en base 2, entonces
\[
 \boxed{v_2(B(m))=s_2(m)-1}.\tag{8}
\]

**Demostración.** La identidad de Legendre \(v_2(n!)=n-s_2(n)\) da \(v_2(C(m))=s_2(m)\). El intervalo \((m,2m]\) contiene exactamente una potencia de 2; luego \(v_2(A(m))=1\). Restar exponentes en la factorización positiva \(C=AB\) produce (8). \(\square\)

**Ejemplo.** En \(m=5\), \(A(5)=42\), \(B(5)=6\) y \(C(5)=252\). En \(m=6\), \(A(6)=462\), \(B(6)=2\) y \(C(6)=924\). Ambas transiciones cumplen (6); las dos capas de acumulación se reconstruyen exactamente.

## 4. La precisión global traducida a la memoria positiva

Tomar logaritmos en la igualdad \(C=AB\) da
\[
 \underbrace{\psi(2m)-\psi(m)}_{\log A(m)}
 =\log\binom{2m}{m}-\log B(m).\tag{9}
\]
Se registra como observable de precisión del intervalo
\[
 \boxed{J(m):=\log\binom{2m}{m}-\log B(m)-m}.\tag{10}
\]
Esta expresión compara dos acumulaciones positivas y la escala; no postula una parte negativa en la descripción de las referencias.

**Proposición 4 (criterio de precisión; reducción a von Koch).** La hipótesis de Riemann es equivalente a la existencia de una constante \(K\) tal que
\[
 \boxed{|J(m)|\le K\sqrt m\,\log^2(2m)}\qquad(m\ge2).\tag{11}
\]
De modo equivalente,
\[
 \boxed{
 \log B(m)=(2\log2-1)m-\tfrac12\log(\pi m)
 +O(\sqrt m\,\log^2m)}.\tag{12}
\]

**Demostración de la equivalencia.** La condición clásica de von Koch establece
\(\mathrm{RH}\iff\psi(x)=x+O(\sqrt x\,\log^2 x)\). De ella se obtiene inmediatamente (11), pues \(J(m)=\psi(2m)-\psi(m)-m\). Recíprocamente, sea \(E(n)=\psi(n)-n\). Para \(n=2m\), \(E(n)=E(m)+J(m)\); para \(n=2m+1\),
\[
 E(n)=E(m)+J(m)+\Lambda(n)-1.
\]
Como \(|\Lambda(n)|\le\log n\), la iteración a través de los cocientes enteros \(\lfloor n/2\rfloor\) acota \(E(n)\) por una serie geométrica de términos \(O(\sqrt{n/2^j}\log^2 n)\) más \(O(\log^2 n)\), y resulta \(E(n)=O(\sqrt n\log^2 n)\). La extensión de enteros a reales cuesta a lo sumo \(O(\log x)\). Esto recupera RH mediante el criterio clásico. Finalmente, Stirling da \(\log\binom{2m}{m}=2m\log2-\tfrac12\log(\pi m)+O(1/m)\), y (12) es equivalente a (11). \(\square\)

**Alcance.** La proposición 4 reorganiza un criterio clásico sobre \(\psi\) como una estimación de la memoria de acarreos \(B(m)\). Las identidades (1)–(10) demuestran la reconstrucción y las correspondencias; **no prueban (11) ni (12)**. La dificultad cuantitativa de RH permanece concentrada en el control uniforme de los acarreos ponderados.

## 5. Verificación computacional y controles adversariales

El archivo `verificar_transicion.py` ejecuta controles íntegros sobre enteros, sin evaluar ni asumir ceros de \(\zeta\). Alcanza \(m\le2048\), calcula \(L(n)\) hasta \(n=4098\) y comprueba por rutas independientes:

1. Regla local \(r(n)=n/\gcd(n,L(n-1))\) y reconstrucción multiplicativa por divisores.
2. Transición exacta (6), carácter libre de cuadrados de \(A(m)\) y reconstrucción directa por prime powers en \((m,2m]\).
3. Integridad de \(B(m)\) calculado como \(\binom{2m}{m}/A(m)\) y por el producto de acarreos (7).
4. Identidad binaria (8).

El verificador emite `muestras.csv` y `verificacion.json`. Los números finitos permiten auditar identidades; no verifican cuantificadores infinitos ni la condición (11).

## 6. Registro de procedencia

| Afirmación | Origen | Estado |
|---|---|---|
| Aparición \(r(n)\), m.c.m., factorial, \(\Lambda\) | Factorización única y divisibilidad clásicas; estructura R–01/HC–03 | Demostrado |
| \(A(m)\) libre de cuadrados y transición (6) | Comparación directa de potencias primas | Demostrado |
| Factor positivo \(B(m)\) por residuos y acarreos | Legendre / Kummer | Conocido; deducción explícita |
| \(v_2(B)=s_2-1\) | Legendre y acumulación binaria | Demostrado, corolario clásico |
| Criterio (11) y (12) | Equivalencia de von Koch para RH | Reformulación demostrada; cota abierta |

**Lectura conceptual:** las primeras apariciones contienen las reglas de conservación y ampliación, y las identidades muestran cómo se transmiten entre escalas. La precisión aritmética necesaria para controlar la acumulación está expresada como una condición concreta sobre el factor de memoria heredada. El análisis mantiene separados mecanismo, demostración y condición abierta.

## Fuentes

- R–01/R–02, [Las escalas relacionales de la criba](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md).
- R–03, [Herencia espectral, normalización y ubicación de los ceros](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/2026-11-18_r03_herencia_espectral/R03_HERENCIA_Y_LOCALIZACION_ES.md).
- HC–03, `LAB_HC03/INFORME_LAB_HC03.md`, nota del 21-XI-2026.
- Kummer (1852), enunciado de acarreos documentado en [T. Lengyel, *Annales Mathematicae et Informaticae*](https://real-j.mtak.hu/22311/1/AnnMathInf_41_2013.pdf), teorema 3.1.
- [Mathematical Association of America, *Equivalents of the Riemann Hypothesis*, volumen dos](https://old.maa.org/node/1401175), equivalencia clásica \(\psi(x)-x=O(\sqrt x\log^2 x)\).

**Endless Monkey Project / Relational Geometry Program**
