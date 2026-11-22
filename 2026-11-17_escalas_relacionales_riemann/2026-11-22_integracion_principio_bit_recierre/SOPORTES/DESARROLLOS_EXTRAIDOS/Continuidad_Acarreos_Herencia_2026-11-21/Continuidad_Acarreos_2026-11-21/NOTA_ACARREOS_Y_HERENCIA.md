# Aparición, herencia y acarreos: transición unitaria y organización por períodos

**Fecha:** 21 de noviembre de 2026  
**Tipo:** nota de continuidad técnica de R–01/R–02 → R–03 → HC–03 → *Aparición, herencia y transmisión entre escalas*.  
**Estado:** identidades de incorporación y transición **demostradas**; independencia en períodos completos y ley binaria **demostradas**; controles computacionales exactos **superados**; control global de fluctuaciones en escalas parciales **abierto**.

## Resumen

Las referencias primas aparecen como potencias primas y se conservan por divisibilidad. La duplicación de una escala separa las incorporaciones del intervalo y las intervenciones de referencias anteriores. Se deducen tres resultados precisos: (i) una transición exacta de la memoria heredada que necesita dos posiciones de prueba de potencia prima impar; (ii) independencia exacta, por el teorema chino del resto, entre las activaciones de referencias primas distintas cuando se promedia sobre un período común completo; y (iii) una ley binomial exacta para el número de activaciones de la referencia 2 en un bloque de escalas. La dimensión cuantitativa pendiente es transferir estas propiedades desde ciclos completos a las ventanas de escala que intervienen en las discrepancias de los primos.

La terminología conceptual es **aparición, incorporación, conservación, herencia y combinación**. Las comparaciones con signo se reservan para medidas matemáticas.

## 1. Referencias desde la primera aparición

Se definen, para enteros \(n\ge1\),

\[
L(n)=\operatorname{mcm}(1,\ldots,n),\qquad L(0)=1,\qquad
r(n)=L(n)/L(n-1).
\]

La factorización única establece

\[
r(n)=\begin{cases}p,&n=p^j\text{ con }j\ge1,\\1,&\text{en otro caso},\end{cases}
\qquad
\log r(n)=\Lambda(n).
\tag{1}
\]

La acumulación hasta \(n\) es \(\log L(n)=\psi(n)\). Si

\[
A(m)=\frac{L(2m)}{L(m)},\quad C(m)=\binom{2m}{m},\quad
B(m)=\frac{C(m)}{A(m)},
\tag{2}
\]

entonces \(A(m)\) y \(B(m)\) son enteros positivos, \(C(m)=A(m)B(m)\), y \(A(m)\) es libre de cuadrados. Estas identidades constan en la nota de continuidad precedente.

## 2. Proposición 1: transición de la memoria en dos posiciones

**Enunciado.** Defínase

\[
r_{\rm impar}(n)=\begin{cases}p,&n=p^j\text{ para un primo impar }p,\\1,&\text{en los demás casos}.\end{cases}
\]

Para todo \(m\ge1\),

\[
\boxed{\frac{B(m+1)}{B(m)}=
\frac{2(2m+1)}{m+1}\,
\frac{r_{\rm impar}(m+1)}{r(2m+1)}.}
\tag{3}
\]

Equivalente en logaritmos,

\[
\boxed{\log B(m+1)-\log B(m)=
\log\frac{2(2m+1)}{m+1}
+\log r_{\rm impar}(m+1)-\log r(2m+1).}
\tag{4}
\]

**Prueba.** De \(A(m)=L(2m)/L(m)\),

\[
\frac{A(m+1)}{A(m)}=
\frac{r(2m+1)r(2m+2)}{r(m+1)}.
\]

Además,

\[
\frac{C(m+1)}{C(m)}=\frac{2(2m+1)}{m+1}.
\]

Como \(B=C/A\), el cociente de estas expresiones da

\[
\frac{B(m+1)}{B(m)}=
\frac{2(2m+1)}{m+1}\,
\frac{r(m+1)}{r(2m+1)r(2m+2)}.
\]

La cantidad \(2m+2=2(m+1)\) es una potencia prima exactamente cuando \(m+1\) es potencia de 2. En ese caso, tanto \(r(m+1)\) como \(r(2m+2)\) valen 2; en otro caso \(r(2m+2)=1\). Por lo tanto, su cociente es \(r_{\rm impar}(m+1)\), y se obtiene (3). \(\square\)

**Lectura.** La transmisión de la referencia 2 está incorporada en ambos lados de la duplicación. La variación del factor de memoria necesita, además del factor de escala conocido, solo las apariciones de potencias primas impares en \(m+1\) y \(2m+1\). La fórmula es exacta y determinista. Es una reorganización algebraica de propiedades clásicas de factoriales y m.c.m.; su interés aquí es el enlace explícito con el mecanismo de herencia.

**Ejemplo:** \(m=5\): \(A(5)=42\), \(B(5)=6\); \(m=6\): \(A(6)=462\), \(B(6)=2\). La fórmula (3) produce \(B(6)/B(5)=\frac{2\cdot11}{6\cdot11}=1/3\).

## 3. Proposición 2: activación de cada potencia heredada

Para una potencia prima \(q=p^j\), defínase

\[
c_q(m)=\mathbf 1_{\{2(m\bmod q)\ge q\}}.
\tag{5}
\]

Por Legendre/Kummer,

\[
\boxed{B(m)=\prod_{p^j\le m}p^{c_{p^j}(m)},\qquad
\log B(m)=\sum_{p^j\le m}(\log p)c_{p^j}(m).}
\tag{6}
\]

Cada función \(c_q\) es periódica de período \(q\). A lo largo de un ciclo de \(q\) residuos enteros aparecen exactamente \(\lfloor q/2\rfloor\) activaciones:

\[
\frac1q\sum_{m=0}^{q-1}c_q(m)=\frac{\lfloor q/2\rfloor}{q}.
\tag{7}
\]

**Prueba.** Los residuos activados son \(\lceil q/2\rceil,\ldots,q-1\), cuyo número es \(\lfloor q/2\rfloor\). \(\square\)

## 4. Proposición 3: combinación exacta de referencias primas distintas

**Enunciado.** Sean \(q=p^a\) y \(r=\ell^b\), con primos distintos \(p\ne\ell\). En un período completo \(qr\),

\[
\boxed{\sum_{m=0}^{qr-1}c_q(m)c_r(m)
=\lfloor q/2\rfloor\lfloor r/2\rfloor.}
\tag{8}
\]

En consecuencia, si \(m\) se toma uniformemente entre los \(qr\) residuos, ambas activaciones son estadísticamente independientes **bajo ese promedio finito**.

**Prueba.** Como \(\gcd(q,r)=1\), el teorema chino del resto establece una biyección
\(\mathbb Z/(qr)\mathbb Z\cong\mathbb Z/q\mathbb Z\times\mathbb Z/r\mathbb Z\). Para cada residuo activado módulo \(q\) y cada residuo activado módulo \(r\) existe exactamente una posición del período con esos dos residuos. El conteo resulta del producto de las dos cantidades (7). \(\square\)

**Extensión a familias.** Para una frontera finita fija \(Q\), defínase

\[
X_{p,Q}(m)=\sum_{j:p^j\le Q}c_{p^j}(m),\qquad
W_Q(m)=\sum_{p\le Q}(\log p)X_{p,Q}(m).
\tag{9}
\]

Si \(m\) recorre un período completo \(P_Q=\operatorname{mcm}(1,\ldots,Q)\), las variables \(X_{p,Q}\) para **primos distintos** son mutuamente independientes por CRT. Por tanto, los promedios finitos satisfacen las identidades exactas

\[
\boxed{\mathbb E W_Q=\sum_{p^j\le Q}(\log p)\frac{\lfloor p^j/2\rfloor}{p^j},}
\tag{10}
\]

\[
\boxed{\operatorname{Var}(W_Q)=\sum_{p\le Q}(\log p)^2\operatorname{Var}(X_{p,Q}).}
\tag{11}
\]

Estas igualdades son para el **modelo con frontera fija \(Q\)** observado en su ciclo completo. Para \(m\ge Q\), \(W_Q(m)\) recoge parte de \(\log B(m)\); la parte restante corresponde a potencias primas \(Q<p^j\le m\). La propia \(B(m)\) tiene una frontera móvil \(Q=m\).

**Ejemplo 1 (primos distintos).** \(q=8\), \(r=9\), período \(72\). Se dan \(4\) activaciones de \(c_8\) y \(4\) de \(c_9\) por sus períodos; en el ciclo común coinciden exactamente \(4\cdot4=16\) veces.

**Ejemplo 2 (la misma referencia).** En los nueve residuos, \(c_3\) se activa tres veces y \(c_9\) cuatro; ambas lo hacen conjuntamente dos veces. Su covarianza uniforme es

\[
\frac{2}{9}-\frac13\frac49=\boxed{\frac{2}{27}}.
\tag{12}
\]

Así, dentro de una misma genealogía pueden existir dependencias exactas entre niveles de potencia. La independencia de (8) se aplica a **primos diferentes**.

## 5. Proposición 4: ley binaria exacta en una escala

Para \(2^J\le m<2^{J+1}\), el intervalo \((m,2m]\) contiene una potencia de 2, por lo que

\[
\boxed{v_2(B(m))=s_2(m)-1.}
\tag{13}
\]

Aquí \(s_2(m)\) es el número de unos de su expresión binaria. En ese bloque, el bit principal es fijo (igual a 1) y los \(J\) bits restantes recorren todas sus combinaciones. Por tanto, para \(k=0,\ldots,J\),

\[
\boxed{\#\{m\in[2^J,2^{J+1}):v_2(B(m))=k\}=\binom Jk.}
\tag{14}
\]

En particular, para el promedio uniforme del bloque,

\[
\boxed{\mathbb E\,v_2(B)=J/2,\qquad\operatorname{Var}(v_2(B))=J/4.}
\tag{15}
\]

Esta ley es exacta, sin modelos probabilísticos añadidos. La distribución binomial es un modo compacto de contar los \(2^J\) estados posibles. Para \(J=8\), el intervalo \([256,512)\) tiene 256 valores y las multiplicidades son \(1,8,28,56,70,56,28,8,1\).

## 6. Alcance de la transferencia entre ciclos y ventanas

Para cualquier potencia prima fija \(q\), cualquier inicio entero \(a\) y cualquier longitud \(N\ge1\), descomponer \([a,a+N)\) en ciclos completos de longitud \(q\) y un fragmento restante da

\[
\boxed{\left|\sum_{m=a}^{a+N-1}c_q(m)-N\frac{\lfloor q/2\rfloor}{q}\right|<q.}
\tag{16}
\]

Para potencias primas coprimas \(q,r\), análogamente,

\[
\boxed{\left|\sum_{m=a}^{a+N-1}c_q(m)c_r(m)
-N\frac{\lfloor q/2\rfloor\lfloor r/2\rfloor}{qr}\right|<qr.}
\tag{17}
\]

La demostración consiste en restar el promedio exacto de cada ciclo completo; la discrepancia del fragmento final es inferior a su longitud. Estas desigualdades son incondicionales, pero su precisión depende de la razón entre el período y el tamaño de la ventana.

Para la suma de frontera fija (9) se obtiene, por desigualdad triangular,

\[
\left|\sum_{m=a}^{a+N-1}W_Q(m)-N\mathbb EW_Q\right|
\le \sum_{p^j\le Q}p^j\log p.
\tag{18}
\]

La cota (18) no aprovecha correlaciones entre períodos distintos y puede alcanzar orden \(Q^2\) mediante cotas clásicas, mientras que las ventanas relevantes pueden tener longitud del orden de \(Q\). De forma similar, el ciclo conjunto \(P_Q\) crece con rapidez; por ejemplo \(P_{12}=27720\), mucho mayor que 12. **La independencia en ciclos completos establece una propiedad estructural exacta, pero todavía se necesita una estimación de correlaciones válida en ventanas parciales con frontera creciente para controlar la discrepancia global de los primos.**

Esta es la obligación matemática que emerge de las relaciones originales: conectar las frecuencias de activación de distintas referencias en ventanas observables, con una cota uniforme cuando la frontera se amplía. No se introduce esa cota como supuesto de los teoremas anteriores.

## 7. Reproducción, controles y límites

`python verificar_herencia_acarreos.py` ejecuta el verificador principal con \(m\le2048\) y biblioteca estándar:

- \(r(n)\) por potencias primas y de modo independiente con \(n/\gcd(n,L(n-1))\).
- \(C(m)=A(m)B(m)\) y \(B(m)\) por productos de activaciones; carácter libre de cuadrados de \(A\).
- Transición (3) por igualdad entera cruzada, además de la transición general de tres posiciones.
- Identidad binaria, ley binomial en bloques y ejemplo de dependencia dentro de una misma genealogía.
- Independencia CRT de 139 parejas de potencias primas de distinto primo y 10 parejas de bloques de primos en el período \(P_{12}=27720\).

**Resultado de ejecución:** 14.548 comprobaciones exactas superadas, sin depender de redondeos de logaritmos, generación aleatoria ni supuestos sobre ceros de zeta. Se incluyen `muestras.csv`, `crt_pares.csv`, `binario_hist.csv` y `resultado.json`.

**Procedencia:** la ley de apariciones por potencias primas, Legendre, Kummer, CRT y los hechos de dígitos binarios son matemáticas clásicas. Las proposiciones de esta nota dan una organización conjunta y pruebas explícitas en términos de aparición y herencia. El control global de tipo Riemann permanece abierto; los promedios uniformes de ciclos completos no deben interpretarse como una demostración de independencia estadística de los primos sobre escalas ordinarias.

## Referencias de continuidad

- [R–01/R–02 — las escalas relacionales de la criba](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md).
- [R–03 — herencia espectral y localización](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/2026-11-18_r03_herencia_espectral/R03_HERENCIA_Y_LOCALIZACION_ES.md).
- Nota anterior: `Continuidad_Aparicion_Herencia/NOTA_CONTINUIDAD.md`.
- Fórmulas de Legendre y Kummer (teoría aritmética clásica); teorema chino del resto; combinatoria binaria elemental.

**Endless Monkey Project / Relational Geometry Program**
