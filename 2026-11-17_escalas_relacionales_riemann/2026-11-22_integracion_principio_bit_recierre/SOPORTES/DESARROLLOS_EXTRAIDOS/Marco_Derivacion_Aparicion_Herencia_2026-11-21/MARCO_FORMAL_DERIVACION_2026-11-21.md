# Marco formal de derivación: aparición, herencia, acarreos y acumulación

**Continuidad:** R–01/R–02 → R–03 → HC–03 → Aparición y transmisión entre escalas → Acarreos y herencia  
**Fecha:** 21 de noviembre de 2026  
**Tipo:** nota de demostración, con verificador independiente  
**Estado:** proposiciones D1–D7 demostradas; condición cuantitativa vinculada a RH caracterizada mediante un criterio clásico; la estimación sigue abierta.  
**Firma:** Endless Monkey Project / Relational Geometry Program

## Resumen

Se formaliza una sola cadena de implicaciones desde la aparición de la primera referencia prima hasta las relaciones de acumulación. Se parte exclusivamente de factorización única y divisibilidad: la incorporación local queda codificada por el cociente del mínimo común múltiplo; la acumulación por sus logaritmos; la comparación entre escalas por los coeficientes binomiales; las referencias anteriores por los acarreos; y la actualización por una transición exacta entre dos posiciones impares. Una proposición complementaria demuestra la **mejor cota universal de discrepancia de frecuencia para una referencia fija** observada en cualquier ventana entera. Las identidades son clásicos de aritmética y combinatoria reordenados en un mismo marco; no se declara una prueba de RH.

## 1. Contrato de aparición

Se define, para enteros \(n\ge1\),

\[
L(0)=1,\qquad L(n)=\operatorname{mcm}(1,\dots,n),\qquad
r(n)=\frac{L(n)}{L(n-1)}.
\]

Una referencia prima \(p\) se incorpora a potencia \(j\) cuando el índice \(n\) alcanza \(p^j\). Su conservación se expresa por divisibilidad. El cociente \(r(n)\) mide exactamente la incorporación en ese instante.

### Proposición D1 — Regla local de incorporación

Para todo \(n\ge2\),

\[
\boxed{r(n)=\frac{n}{\gcd(n,L(n-1))}=\begin{cases}p,&n=p^j\ (j\ge1),\\1,&\text{en los demás casos}.\end{cases}}
\]

**Demostración.** El exponente de un primo \(p\) en \(L(n)\) es \(e_p(n)=\max\{j:p^j\le n\}\). Entre \(n-1\) y \(n\), este exponente aumenta exactamente si \(n=p^j\); aumenta entonces una unidad. En el cociente \(n/\gcd(n,L(n-1))\), la valuación de \(p\) es \(\max(0,v_p(n)-e_p(n-1))\). Solo vale uno si \(n=p^j\), y cero en otro caso. Ambas expresiones tienen, por tanto, la misma valuación para todo \(p\). \(\square\)

### Proposición D2 — Reconstrucción y herencia de múltiplos

Para todo \(n\ge2\),

\[
\boxed{n=\prod_{d\mid n}r(d)},\qquad
\boxed{n!=\prod_{d=1}^n r(d)^{\lfloor n/d\rfloor}},\qquad
\boxed{\log L(n)=\sum_{d\le n}\Lambda(d)=\psi(n)}.
\]

**Demostración.** Los divisores \(d\) de \(n\) que aportan un factor mayor que uno son exactamente las potencias \(p,p^2,\ldots,p^{v_p(n)}\), cada una con factor \(r(d)=p\). Esto reproduce \(n\) por factorización única. Multiplicar la primera identidad para \(1\le k\le n\) registra cada divisor \(d\) exactamente \(\lfloor n/d\rfloor\) veces. Tomar logaritmos de \(L(n)=\prod_{d\le n}r(d)\), usando \(\log r(d)=\Lambda(d)\), da la última identidad. \(\square\)

### Proposición D3 — El paso mínimo recupera cada incorporación

Defínase para \(x\ge1\):

\[
T(x)=\sum_{k\le x}\Lambda(k)\left(\frac{x}{k}-1\right).
\]

Para todo entero \(n\ge2\),

\[
\boxed{T(n+1)-2T(n)+T(n-1)=\frac{\Lambda(n)}n=\frac{\log r(n)}n}.
\]

**Demostración.** El sumando asociado a \(k\) vale cero hasta el índice \(x=k\); a partir de allí es una rampa lineal con pendiente \(\Lambda(k)/k\). La segunda diferencia centrada de una rampa es cero salvo en el punto de incorporación \(n=k\), donde vale su pendiente. Sumar en \(k\) produce la fórmula. El \(-1\) del peso establece que el valor en el instante de aparición es cero. \(\square\)

## 2. Duplicación y separación positiva

Para cada \(m\ge1\) se definen

\[
A(m)=\frac{L(2m)}{L(m)},\qquad
C(m)=\binom{2m}{m},\qquad
B(m)=\frac{C(m)}{A(m)}.
\]

### Proposición D4 — Aportaciones del intervalo y memoria de acarreos

\[
\boxed{A(m)=\prod_{m<d\le2m}r(d)},\qquad
\boxed{C(m)=A(m)B(m)},
\]

con \(A(m)\) entero libre de cuadrados, y

\[
\boxed{B(m)=\prod_{\substack{p^j\le m\\2(m\bmod p^j)\ge p^j}}p}. 
\]

**Demostración.** La primera identidad telescopa desde la definición de \(r\). Dos potencias consecutivas de un mismo \(p\) tienen cociente \(p\ge2\); por ello en \((m,2m]\) cabe a lo sumo una de ellas, y \(A(m)\) es libre de cuadrados. Por la fórmula de Legendre,

\[
v_p(C(m))=\sum_{j\ge1}\left(\left\lfloor\frac{2m}{p^j}\right\rfloor-2\left\lfloor\frac{m}{p^j}\right\rfloor\right).
\]

Escribiendo \(m=ap^j+t\), \(0\le t<p^j\), el sumando se convierte en \(\lfloor2t/p^j\rfloor\), que vale uno cuando \(2t\ge p^j\). Para \(m<p^j\le2m\) este factor pertenece exactamente a \(A(m)\); para \(p^j\le m\) pertenece a \(B(m)\). Se obtiene el producto indicado, demostrando además que \(B(m)\) es entero positivo. \(\square\)

### Proposición D5 — Transición unitaria del factor heredado

Sea \(r_{\rm impar}(n)=p\) si \(n=p^j\) con \(p\) primo impar, y \(r_{\rm impar}(n)=1\) en los demás casos. Entonces

\[
\boxed{\frac{A(m+1)}{A(m)}=\frac{r(2m+1)r(2m+2)}{r(m+1)}},
\]

\[
\boxed{\frac{B(m+1)}{B(m)}=
\frac{2(2m+1)}{m+1}\,\frac{r_{\rm impar}(m+1)}{r(2m+1)}}.
\]

**Demostración.** La primera igualdad resulta del telescopaje de \(L(2m+2)/L(m+1)\) frente a \(L(2m)/L(m)\). Por factoriales,
\(C(m+1)/C(m)=2(2m+1)/(m+1)\). Al dividir este cociente por el de \(A\), aparece el factor \(r(m+1)/r(2m+2)\). Dado que \(2m+2=2(m+1)\), ambos factores son 2 exactamente cuando \(m+1\) es potencia de 2, y fuera de ese caso el factor inferior vale 1. Así, el cociente es precisamente \(r_{\rm impar}(m+1)\). \(\square\)

**Comprobación ilustrativa.** \(A(5)=42, B(5)=6\) y \(A(6)=462, B(6)=2\). La actualización da \(B(6)/B(5)=2/6=1/3\).

## 3. Combinación de referencias y mejor cota de ventana para una referencia

Para una potencia prima \(q=p^j\) definimos su indicador de acarreo

\[
c_q(m)={\bf1}_{\{m\bmod q\ge\lceil q/2\rceil\}}.
\]

El indicador está definido para todos los enteros a efectos de estudiar sus períodos; en el factor hereditario \(B(m)\) la referencia \(q\) interviene únicamente cuando \(q\le m\). Su período es \(q\), con exactamente \(h_q=\lfloor q/2\rfloor\) activaciones por período. Si \(q=p^j\) y \(r=\ell^k\) tienen primos base distintos, el teorema chino del resto da, sobre el período completo \(qr\),

\[
\boxed{\sum_{m=0}^{qr-1}c_q(m)c_r(m)=h_qh_r}.
\]

La independencia es **exacta para períodos completos y referencias base distintas**. Las potencias de un mismo primo pueden conservar dependencia entre sus indicadores.

### Proposición D6 — Cota óptima en cualquier intervalo consecutivo (refinamiento)

Para todo entero \(a\), \(N\ge1\) y \(q\ge2\), sea

\[
D_q(a,N)=\sum_{m=a}^{a+N-1}c_q(m)-\frac{N h_q}{q}.
\]

Se tiene la desigualdad uniforme

\[
\boxed{|D_q(a,N)|\le \frac{h_q(q-h_q)}{q}=\frac{\lfloor q^2/4\rfloor}{q}\le\frac q4.}
\]

**La primera constante es la mejor posible para cada \(q\).**

**Demostración.** Escribimos \(N=tq+s\), \(0\le s<q\). Los \(t\) períodos completos tienen exactamente \(th_q\) activaciones y contribución neta cero en \(D_q\). En la sección restante de longitud \(s\), el número \(u\) de activaciones satisface

\[
\max(0,s-(q-h_q))\le u\le\min(s,h_q).
\]

De aquí,
\(u-sh_q/q\le h_q(q-h_q)/q\): para \(s\le h_q\) usar \(u\le s\), y para \(s\ge h_q\), usar \(u\le h_q\). Del mismo modo,
\(sh_q/q-u\le h_q(q-h_q)/q\) usando los dos tramos delimitados por \(q-h_q\). La cota es alcanzable: seleccionar una ventana formada exactamente por las \(h_q\) posiciones activas consecutivas da \(u=h_q\), \(s=h_q\), y \(D_q=h_q(q-h_q)/q\). \(\square\)

**Alcance.** Para una referencia fija, la frecuencia por ventanas está completamente controlada mediante una constante óptima. Sin embargo, la suma sobre un número creciente de referencias conduce, por desigualdad triangular, a una cota de orden \(\sum_{p^j\le Q}p^j\log p\); ese control puede ser demasiado amplio para deducir una estimación de tipo RH. La independencia de períodos completos tampoco sustituye una cota uniforme para ventanas parciales con frontera móvil.

### Proposición D7 — Memoria binaria exacta

Para todo \(m\ge1\), si \(s_2(m)\) es la cantidad de unos de su representación binaria,

\[
\boxed{v_2(B(m))=s_2(m)-1}.
\]

Para \(2^J\le m<2^{J+1}\), se cumple

\[
\boxed{\#\{m:v_2(B(m))=k\}=\binom Jk}\quad (0\le k\le J).
\]

**Demostración.** La fórmula de Legendre \(v_2(n!)=n-s_2(n)\) da \(v_2(C(m))=s_2(m)\). Como \((m,2m]\) contiene exactamente una potencia de dos, \(v_2(A(m))=1\); de aquí la primera identidad. Dentro del bloque dyádico, el primer bit es uno y los \(J\) bits restantes recorren todas las combinaciones. Elegir \(k\) unos entre esos \(J\) bits produce exactamente \(\binom Jk\) casos. \(\square\)

## 4. Qué está demostrado y qué queda por derivar

La estructura completa satisface

\[
\boxed{\log A(m)=\psi(2m)-\psi(m)},\qquad
\boxed{\log B(m)=\log\binom{2m}{m}-\psi(2m)+\psi(m)}.
\]

Por el criterio clásico de von Koch, RH es equivalente a \(\psi(x)=x+O(\sqrt x\log^2 x)\). En el lenguaje de la herencia, se puede definir

\[
J(m)=\log\binom{2m}{m}-\log B(m)-m.
\]

Entonces \(J(m)=\psi(2m)-\psi(m)-m\). Se deduce **por equivalencia clásica**

\[
\mathrm{RH}\quad\Longleftrightarrow\quad
J(m)=O(\sqrt m\log^2 m)
\quad(m\to\infty).
\]

La dirección inversa se demuestra iterando \(E(2m)=E(m)+J(m)\), donde \(E(n)=\psi(n)-n\), y para los impares \(E(2m+1)=E(m)+J(m)+\Lambda(2m+1)-1\). Como \(|\Lambda(n)|\le\log n\), la suma sobre escalas sucesivamente divididas por dos resulta \(O(\sqrt n\log^2 n)\). Esta deducción identifica la **condición**, no establece la cota.

El resultado demostrado D6 es un refinamiento incondicional de la estimación por una referencia en ventanas: el error absoluto es como máximo \(q/4\), con constante óptima exacta. Sigue pendiente una desigualdad conjunta que controle el total de las referencias de frontera creciente con precisión suficiente. La formulación mantiene separados mecanismo, identidad, consecuencia y cuestión abierta.

## 5. Procedencia y reproducción

**Base matemática clásica:** factorización única, mínimo común múltiplo, función de von Mangoldt, fórmula de Legendre, teorema de Kummer, teorema chino del resto, combinatoria binaria y criterio de von Koch. Las demostraciones D1–D7 son deducciones explícitas dentro de un marco unificado de aparición, herencia y combinación; no atribuyen originalidad a la teoría base.

**Verificador:** `verificar_marco.py`; usa solo biblioteca estándar de Python y compara las identidades por enteros exactos, además de las cotas de ventana con fracciones racionales. La prueba de D6 es algebraica; las comprobaciones finitas son controles adicionales.

**Fuentes de continuidad:** `NOTA_CONTINUIDAD.md` y `NOTA_ACARREOS_Y_HERENCIA.md` (21-XI-2026), R–01/R–02 y R–03 del repositorio público.

Endless Monkey Project / Relational Geometry Program
