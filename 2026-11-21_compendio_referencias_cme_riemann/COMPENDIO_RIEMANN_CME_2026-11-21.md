# Anexo consolidado: referencias, granularidad, focos de determinación y cierre funcional

**Fecha de consolidación:** 21 de noviembre de 2026<br>
**Ámbito:** R–01/R–02, R–03, R–RH–01, economía de consultas, G–01/O58, CME–002 y ensayos CME–RH–01/02/03<br>
**Estado:** identidades y controles aritméticos **demostrados**; errores óptimos hasta $m=2048$ **recalculados** en coma flotante doble; equivalencia de la familia libre de cuadrados con RH **clásica** (Báez-Duarte, 2002); condiciones de transferencia **condicionales**; la correspondencia geométrica con CME–002 y las hipótesis RH y GRH siguen **abiertas**.<br>
**Tipo de documento:** anexo de investigación verificable, con controles reproducibles en `scripts/`.

## Resumen y resultado central

La incorporación de referencias permite distinguir relaciones nuevas y recuperar diferencias pendientes. La pregunta funcional es de **reconstrucción**: fijada una clase de operaciones, se mide la convergencia en la norma correspondiente. Los experimentos con el cubo de espejos parten de sus *focos de determinación* —puntos de concurrencia de relaciones— en lugar de ángulos asignados a posteriori a funciones aritméticas.

El anexo distingue tres niveles de cierre:

1. **Recierre aritmético local.** En cada paso diádico $N\to2N$, los saltos de la combinación de Möbius en los puntos $x=1/n$, $N<n\le2N$, se cancelan exactamente al incorporar la referencia $n$. Para $N=1024$ se verificaron 621 focos no triviales.
2. **Recuperación por proyecciones.** Para espacios funcionales anidados, la diferencia de errores óptimos es exactamente la norma cuadrática del componente nuevo. Una reflexión ortogonal de Hilbert representa esa diferencia; su identificación con un espejo de CME–002 está abierta.
3. **Cierre global.** Para la familia de índices libres de cuadrados, $e_m\to0$ equivale a RH. Llegar a ese cierre exige controlar a la vez la acumulación cerca de cero, la región intermedia, la cola y la recuperación entre todas las escalas; las identidades de los niveles 1 y 2 son locales.

La aportación consiste en reunir esas identidades, dos tipos de obstrucción, el ensayo de focos, el recálculo de los errores óptimos hasta $m=2048$ y un **contrato falsable de transferencia**. La identidad de Möbius y la estructura booleana subyacente son clásicas; lo propio de este anexo es su organización como observable del laboratorio.

## 1. Objetos, procedencia y distinciones de tipo

### 1.1. Referencia aritmética de criba

Para un conjunto finito de primos $S$ se define

$$
M_S=\prod_{p\in S}p,\qquad
\delta_S=\prod_{p\in S}(1-p^{-1}),\qquad
A_S(x)=\operatorname{card}\lbrace 1\le n\le x:\gcd(n,M_S)=1\rbrace,\qquad
E_S(x)=A_S(x)-\delta_S x.
$$

La referencia cambia al añadir un primo; las propiedades de la nueva coordenada módulo $p$ vienen dadas por el teorema chino del resto:

$$
\mathbb Z/(M_Sp)\mathbb Z\simeq\mathbb Z/M_S\mathbb Z\times\mathbb Z/p\mathbb Z\qquad(p\notin S).
$$

El espacio de preguntas importa: esa coordenada nueva distingue residuos, y que mejore una consulta depende de la consulta.

### 1.2. Referencia funcional

En $H=L^2((0,\infty),dx)$, sean

$$
\chi(x)=\mathbf 1_{(0,1]}(x),\qquad
f_n(x)=\left\lbrace\frac{1}{nx}\right\rbrace,\qquad
W_m^{\mathrm{sf}}=\operatorname{span}\lbrace f_n:1\le n\le m,\ \mu(n)\ne0\rbrace .
$$

Con $P_m$ la proyección ortogonal sobre $W_m^{\mathrm{sf}}$:

$$
r_m=(I-P_m)\chi,\qquad e_m^2=\Vert r_m\Vert_2^2 .
$$

Todos los valores numéricos de $e_m$ de este anexo se refieren a esta **familia restringida a índices libres de cuadrados**. La combinación fija de criba $a_m=-\sum_{n\le m}\mu(n)f_n$ es un elemento de $W_m^{\mathrm{sf}}$ que en general difiere del aproximante óptimo $P_m\chi$; sus errores se reportan por separado.

**Criterio para la familia restringida.** Báez-Duarte demostró que RH equivale a que $\chi$ pertenezca al cierre de $\operatorname{span}\lbrace f_n:n\in\mathbb N\rbrace$. En la segunda versión del trabajo, la Proposición 3.1 (atribuida a M. Balazard) establece que, bajo RH, existe $c>0$ con

$$
\Bigl\Vert\chi+\sum_{a\le n}\mu(a)\,e^{-c\log a/\log\log n}\,f_a\Bigr\Vert_2\ll(\log\log n)^{-1/3}.
$$

Los coeficientes se anulan cuando $\mu(a)=0$, de modo que ese aproximante pertenece a $W_n^{\mathrm{sf}}$ y acota $e_n$. La implicación recíproca se obtiene por inclusión: el cierre de la familia restringida está contenido en el de la familia entera. Por tanto

$$
\mathrm{RH}\iff e_m\to0\quad\text{(familia libre de cuadrados)}.\qquad\text{(BD)}
$$

Con esta referencia, la equivalencia restringida queda respaldada donde se haya usado en documentos previos del programa.

### 1.3. Granularidad, economía y promoción

Una interfaz observacional $\Phi_\lambda$ es suficiente para una pregunta $q$ si existe un decodificador permitido con $q=\bar q\circ\Phi_\lambda$. Aun siendo inyectiva, $\Phi_\lambda$ puede dejar la pregunta fuera del alcance de las **combinaciones lineales**. Ejemplo exacto: en $X=\lbrace0,1,2\rbrace$ con medida uniforme, $\Phi(x)=x$ y $q(x)=x^2$; la consulta se responde con $\Phi^2$, pero el mejor ajuste en $\operatorname{span}\lbrace1,\Phi\rbrace$ deja error cuadrático $2/9$.

En G–01/O58, $a^2+b^2+1=N^2$ implica el resto algebraico $1/N^2\to0$ a lo largo de sucesiones admisibles $N\to\infty$. Ese resto es algebraico y distinto del error $e_m^2$ de $L^2$. El sucesor admite varias elecciones: $(2,2,3)$ admite, entre otras, $(4,8,9)$ y $(12,12,17)$. La promoción de una clase cerrada al nivel siguiente proporciona una estructura de herencia; convertirla en una cota funcional requiere un mapa explícito.

## 2. Correspondencias exactas de criba y transformación

### 2.1. Mellin y factores finitos de Euler

Para $0<\operatorname{Re}(s)<1$, la integral de Mellin de la discrepancia finita converge absolutamente y satisface

$$
F_S(s)=\int_0^\infty E_S(x)\,x^{-s-1}\,dx=\frac{\zeta(s)}{s}\prod_{p\in S}(1-p^{-s}).\qquad\text{(M)}
$$

$E_S$ es acotada para $x\ge1$ y vale $-\delta_Sx$ para $0<x<1$, lo que da la convergencia en ambos extremos. La identidad se obtiene por inclusión-exclusión y la transformada clásica de $\lfloor x\rfloor-x$ en la misma franja. Para $p\notin S$,

$$
F_{S\cup\lbrace p\rbrace}(s)=(1-p^{-s})F_S(s).
$$

Como $1-p^{-s}$ no se anula en $\operatorname{Re}(s)>0$, los factores finitos conservan posiciones y multiplicidades de los ceros dentro de la franja crítica: la identidad transporta los ceros sin fijar su ubicación. Con carácter trivial, $sF_S(s)=L^S(s,1)$, el producto de Euler incompleto sin los factores de $S$; es una identificación de funciones bajo estas convenciones.

### 2.2. Inversión y funciones de partes fraccionarias

Aplicando inclusión-exclusión a $A_S$:

$$
G_S(t):=-E_S(1/t)=\sum_{d\mid M_S}\mu(d)\,f_d(t).\qquad\text{(F)}
$$

Es una **igualdad lineal exacta** y un puente natural con el sistema de funciones fraccionarias. Cada divisor $d\mid M_S$ es libre de cuadrados. La inversión de Möbius sobre el retículo de subconjuntos recupera esas funciones dentro del sistema de índices libres de cuadrados; las dilataciones con índice no libre de cuadrados, como $f_{p^2}$, quedan fuera de ese argumento.

### 2.3. Conjugación de operadores

Sean $T_pf(x)=f(x)-f(x/p)$, $P_p\varphi(x)=\varphi(x)-\varphi(px)$ y $Jf(x)=f(1/x)$. Entonces

$$
JT_pJ=P_p\qquad\text{(O)}
$$

en un dominio común estable bajo estas operaciones. En $L^2((0,\infty),dx/x)$, $J$ y las dilataciones son unitarios y los operadores son acotados. La conjugación es algebraica; la equivalencia de completaciones, rangos cerrados o contratos topológicos de otros espacios (por ejemplo, ciertos espacios de funciones de prueba) requiere un argumento propio. Ese es el alcance de la comparación preliminar con el marco de Masullo: las correspondencias algebraicas están delimitadas y la transferencia funcional sigue abierta.

## 3. Identidad de recuperación y reflexión operativa

Para $m<n$:

$$
U_{m,n}=W_n^{\mathrm{sf}}\cap\bigl(W_m^{\mathrm{sf}}\bigr)^{\perp},\qquad
Q_{m,n}=P_n-P_m,\qquad
\mathcal R_{m,n}=I-2Q_{m,n}.
$$

$Q_{m,n}$ es una proyección ortogonal y $\mathcal R_{m,n}$ una involución. Por Pitágoras:

$$
e_m^2-e_n^2=\Vert Q_{m,n}r_m\Vert^2=\tfrac14\Vert r_m-\mathcal R_{m,n}r_m\Vert^2.\qquad\text{(R)}
$$

Para una semilla $g\in W_n^{\mathrm{sf}}$ con $h=(I-P_m)g\ne0$, el certificado elemental de recuperación es

$$
\frac{\vert\langle r_m,g\rangle\vert^2}{\Vert h\Vert^2}\le e_m^2-e_n^2 .
$$

Esto reproduce, con operadores de reflexión, la estructura del certificado de semilla y de la matriz de Gram. La identificación de $\mathcal R_{m,n}$ con una reflexión original del recinto CME–002 forma parte del contrato de §8.

**Positividad del error.** $e_m>0$ para todo $m$. Si $\chi=\sum_{n\le m}c_nf_n$ en $L^2$, la transformada de Mellin en $0<\operatorname{Re}(s)<1$ daría $1+\zeta(s)\sum_{n\le m}c_nn^{-s}=0$; por continuación, $1/\zeta(s)=-\sum_{n\le m}c_nn^{-s}$ en $\operatorname{Re}(s)>1$, y por unicidad de los coeficientes de Dirichlet $\mu(n)=-c_n$ para todo $n$, lo cual es imposible porque $\mu(n)\ne0$ para infinitos $n$.

Se define entonces

$$
\gamma_m=\frac{\Vert Q_{m,2m}r_m\Vert^2}{e_m^2}\in[0,1),\qquad e_{2m}^2=e_m^2(1-\gamma_m).
$$

Por telescopaje:

$$
e_{2^J}^2=e_1^2\prod_{j=0}^{J-1}\bigl(1-\gamma_{2^j}\bigr).\qquad\text{(A)}
$$

Como cada factor es positivo y $e_m$ no crece, $e_m\to0$ equivale a $\sum_j\gamma_{2^j}=\infty$. Junto con (BD):

$$
\mathrm{RH}\iff\sum_{j\ge0}\gamma_{2^j}=\infty .
$$

Es una reformulación equivalente: la divergencia de la serie es la obligación pendiente.

**Contraejemplos geométricos.** Tres reflectores que generan el grupo $B_3$ de 48 simetrías pueden actuar sobre las tres primeras coordenadas de $\mathbb R^4$ y dejar invisible la cuarta. A la inversa, dos reflexiones cuyo producto tiene orden infinito pueden tener normales que abarcan $\mathbb R^2$ y recuperar toda consulta en ese espacio. **Finitud del grupo, cierre del recinto y recuperabilidad de una pregunta son, por tanto, propiedades lógicamente distintas.** Ambos controles se verifican con aritmética racional en `scripts/verificar_reflexiones.py`.

## 4. Focos de determinación: cruce, herencia y recierre aritmético

### 4.1. Definición operativa y lema universal

Un *foco aritmético candidato* para el sistema $f_d$ es un punto $x=1/n$ donde concurren discontinuidades de varias referencias, etiquetado por la relación de divisibilidad. Es un objeto **aritmético**; su correspondencia con intersecciones de rayos del laboratorio óptico es parte del contrato de §8.

En la combinación

$$
G_N(x)=\sum_{1\le d\le N}\mu(d)\,f_d(x),
$$

cada $f_d$ salta $+1$ al aumentar $x$ a través de $1/n$ si $d\mid n$, y es continua allí en caso contrario. El salto de $G_N$ es

$$
J_N(n)=\sum_{\substack{d\mid n\\ d\le N}}\mu(d).
$$

**Proposición F.** Para todo entero $N\ge1$ y cada entero $N<n\le2N$,

$$
J_N(n)=-\mu(n),\qquad J_{2N}(n)=0.\qquad\text{(C)}
$$

*Prueba.* Todo divisor propio $d$ de $n$ satisface $d\le n/2\le N$. Antes de ampliar la pared estaban presentes todos los divisores propios y faltaba solo $d=n$. Como $n>1$, la identidad clásica $\sum_{d\mid n}\mu(d)=0$ da $J_N(n)=-\mu(n)$. Al añadir $n$, la suma queda completa y vale cero. $\square$

Si $\mu(n)=0$, el salto ya era cero antes del avance: los focos no triviales del intervalo son exactamente los $n$ libres de cuadrados. El lema es uniforme en $N$ para saltos; las normas de aproximación se tratan en §5–§7.

### 4.2. Ejemplo exacto: 1030

$1030=2\cdot5\cdot103$ es libre de cuadrados. En el nivel $N=1024$, el punto $x=1/1030$ contiene discontinuidades de las referencias

$$
\lbrace1,2,5,10,103,206,515\rbrace,
$$

con signos de Möbius $(+1,-1,-1,+1,-1,+1,+1)$. Su suma es $+1$. En $N=2048$ entra $1030$, con $\mu(1030)=-1$, y el salto total se cancela:

$$
1-1-1+1-1+1+1-1=0.
$$

Los ocho divisores de $1030$ corresponden a los ocho subconjuntos de $\lbrace2,5,103\rbrace$. Alternar la presencia de un primo es una involución binaria $T_p$, con $T_pT_q=T_qT_p$; la estructura combinatoria es $\mathbb F_2^3$ y la suma alternada es $(1-1)^3=0$. Es una realización exacta de relaciones de divisores mediante involuciones que conmutan, cuyos productos tienen orden $2$. Las reflexiones angulares de CME–002 tienen productos de orden $3$ o $k$; la relación entre ambas estructuras está abierta.

### 4.3. Conteo de focos y falsación cuantitativa

Para la transición $1024\to2048$, `scripts/verificar_focos.py` recorre **todos los enteros** $1025\le n\le2048$ con aritmética exacta:

| Estado del salto en el foco $x=1/n$ | Casos |
|---|---:|
| $\mu(n)\ne0$: foco no trivial cancelado por la nueva referencia | **621** |
| $\mu(n)=0$: salto ya nulo | **403** |
| Total | **1024** |

Entre los 621 casos no triviales hay 137 con un factor primo, 282 con dos, 168 con tres y 34 con cuatro. Los 137 primeros son los primos de $(1024,2048]$; los 484 restantes son combinaciones nuevas de factores ya presentes, como $1030$.

El control adversarial es indispensable. Entre $N=16$ y $N=32$ se cierran **nueve** focos no triviales, y el error cuadrático de la combinación *de coeficientes fijos* $a_N=-G_N$ **crece**:

$$
\Vert\chi-a_{16}\Vert^2\approx0.106470,\qquad\Vert\chi-a_{32}\Vert^2\approx0.186754.
$$

En el mismo paso, el óptimo baja de $e_{16}^2=0.019434$ a $e_{32}^2=0.015212$ (§6), como corresponde a la mejor combinación de un espacio ampliado. El control separa dos cantidades: la cancelación de saltos locales y el error de una combinación fijada, que puede crecer.

### 4.4. Contrastación con el cubo óptico

En CME–002, los grupos triangulares $(2,3,k)$ cierran para $k=2,3,4,5$, presentan el caso euclídeo en $k=6$ y se abren para $k\ge7$; la familia $(2,2,k)$ cierra para todo $k$. El laboratorio usa como criterio operativo las composiciones de reflexiones, además del número de referencias.

La asignación tentativa de $f_n$ como normal a un espejo se falsó en un ejemplo: las normales funcionales $f_{1027}$ y $f_{1030}$ forman aproximadamente $6.512951^\circ$ en su métrica de Gram, mientras la regla angular $\pi/1027$ da $0.175268^\circ$ (`scripts/ensayo_angulos.py`). El ensayo descarta esa asignación concreta; otros entrelazadores quedan por definir. La prueba por focos reemplaza esa comparación angular arbitraria por el estudio de las relaciones que concurren primero.

## 5. Economía de reconstrucción: certificado de tres ventanas

Para cualquier aproximante finito $a_m=\sum_{n\le m}c_{m,n}f_n$ se definen

$$
B_m=\chi-a_m,\qquad L_m=\sum_{n\le m}\vert c_{m,n}\vert,\qquad C_m=\sum_{n\le m}\frac{c_{m,n}}{n}.
$$

**Proposición V.** Para todo $0<\delta\le1\le R$,

$$
\Vert B_m\Vert_2^2\le\delta(1+L_m)^2+\int_\delta^R\vert B_m(x)\vert^2\,dx+\frac{\vert C_m\vert^2}{R}.\qquad\text{(V)}
$$

*Prueba.* Para $0<x<\delta$, $\vert B_m(x)\vert\le1+L_m$ porque $0\le f_n(x)<1$. Para $x>R\ge1$ vale exactamente $B_m(x)=-C_m/x$, cuya contribución es $\vert C_m\vert^2/R$. La integral central queda sin alterar. $\square$

El certificado separa **granularidad fina**, **región intermedia** y **cola**. Si se construyen $a_m\in W_m^{\mathrm{sf}}$ y parámetros $0<\delta_m\le1\le R_m$ con los tres términos del lado derecho tendiendo a cero, entonces $e_m\to0$ y, por (BD), RH. La condición también es necesaria: bajo RH, los aproximantes de (BD) cumplen $\Vert B_m\Vert_2\to0$, y basta tomar $\delta_m=\min\lbrace1,\ m^{-1}(1+L_m)^{-2}\rbrace$ y $R_m=\max\lbrace1,\ m\vert C_m\vert^2\rbrace$, porque la integral central no supera $\Vert B_m\Vert_2^2$. El certificado es así otra reformulación equivalente; su valor está en separar las tres obligaciones. La identidad $1/N^2\to0$ de G–01 controla un resto algebraico, y las tres estimaciones de (V) son una obligación aparte.

Otra formulación, igualmente condicional, relaciona una sucesión geométrica $N_k$ con índices funcionales $m(k)$ y aproximantes $a_k\in W_{m(k)}^{\mathrm{sf}}$ mediante una cota demostrada independientemente de RH:

$$
\Vert\chi-a_k\Vert^2\le A_kN_k^{-2}+B_k,\qquad A_k/N_k^2+B_k\to0.
$$

Si se prueban estas hipótesis con $m(k)\to\infty$, se obtiene RH. La cota global es precisamente **la obligación pendiente**; elegir $A_k$ después de conocer el error sería circular. La cota inferior de Burnol, de orden $1/\log m$, impide identificar $e_m^2$ con $1/m^2$: el término $B_k$ debe absorber al menos ese orden.

## 6. Recuperación por escalas, condiciones propuestas y resultados numéricos

La matriz de Gram $G=(\langle f_i,f_j\rangle)$ y el vector $b=(\langle\chi,f_i\rangle)$, con $\langle\chi,f_n\rangle=(\log n+1-\gamma_{\mathrm E})/n$ y $\gamma_{\mathrm E}$ la constante de Euler, permiten calcular errores óptimos finitos. Para índices heredados $A$ y nuevos $B$, cuando las matrices relevantes son invertibles:

$$
S=G_{BB}-G_{BA}G_{AA}^{-1}G_{AB},\qquad
h=b_B-G_{BA}G_{AA}^{-1}b_A,\qquad
e_A^2-e_{A\cup B}^2=h^{\top}S^{-1}h.\qquad\text{(S)}
$$

La igualdad (S) es la vía para obtener **cotas inferiores no circulares** de la recuperación; por sí sola es una identidad, sin reducción uniforme.

La ley candidata del 20 XI, que exigía para todo $j$

$$
\gamma_{2^j}\ge\frac{1}{j+2},
$$

es **falsa como afirmación universal**. El recálculo da $\gamma_{1024}=0.06642<1/12\approx0.08333$; entre $j=0$ y $j=10$ es el único paso donde falla. Queda registrada como intento refutado. La refutación afecta a esa cota particular: para la divergencia de $\sum_j\gamma_{2^j}$ bastaría, por ejemplo, una cota inferior del orden de $c/(j\log j)$.

Valores recalculados con `scripts/recalcular_gram.py`:

| Indicador del paso $1024\to2048$ | Valor |
|---|---:|
| Referencias libres de cuadrados hasta 1024 | 624 |
| Referencias nuevas hasta 2048 | 621 |
| Referencias acumuladas hasta 2048 | 1245 |
| Error óptimo restringido $e_{1024}^2$ | 0.006672 |
| Error óptimo restringido $e_{2048}^2$ | 0.006229 |
| Fracción recuperada $\gamma_{1024}$ | 0.06642 (6.64 %) |
| Ángulo entre resto y subespacio nuevo, $\arccos\sqrt{\gamma_{1024}}$ | 75.065° |
| Número de condición de Gram, dimensión 1245 | $8.6\times10^{6}$ |

**Calificación.** Las cantidades enteras y el lema de focos son exactos. Los errores óptimos se calculan en coma flotante doble con un paso de refinamiento iterativo, después de contrastar la fórmula de Gram con integración directa en seis pares (diferencias del orden de $10^{-10}$). Con número de condición $\approx8.6\times10^{6}$, la estimación estándar del error de redondeo en $e_m^2$ es del orden de $10^{-9}$, por debajo de las seis cifras decimales reportadas. Los valores coinciden en todas las cifras con el registro previo `resultados/registro_mecanismos_original.txt`. El ángulo es un ángulo de Hilbert entre el resto $r_{1024}$ y $U_{1024,2048}$.

Para $N=2048$, el error cuadrático es $0.067054$ con pesos $w_n=1-\log n/\log N$, $0.084783$ con coeficientes de corte abrupto y $0.006229$ para el óptimo restringido. Los productos $e_m^2\log m$ valen $0.0462$ en $m=1024$ y $0.0475$ en $m=2048$, del orden de la constante $C_0=2+\gamma_{\mathrm E}-\log4\pi\approx0.0462$. Esa constante aparece en la cota inferior de Burnol (bajo RH con ceros simples) y en la asintótica de Bettin–Conrey–Farmer para pesos logarítmicos, formulada bajo RH e hipótesis adicionales sobre $\zeta'$. Es una comparación de magnitud a escala finita: esos teoremas quedan como referencia externa, no como premisa, y los datos indican que los pesos logarítmicos se acercan al óptimo lentamente.

## 7. Dos obstrucciones adicionales: lo local frente a lo global

**Obstrucción por interfaz insuficiente.** Una firma puede distinguir cada estado y aun así dejar una consulta sin respuesta cuando los decodificadores se restringen a un subespacio lineal (ejemplo $q=\Phi^2$, error $2/9$). Una relación nueva determinable y una dirección nueva de reconstrucción admitida son, por tanto, objetos distintos.

**Obstrucción por acumulación cerca de cero.** En la criba por un bloque finito de primos $S_y=\lbrace p\le y\rbrace$, sea $q_y$ el primo siguiente y $\delta_y=\prod_{p\le y}(1-1/p)$. Para $t>1/q_y$ se obtiene $\chi(t)+G_{S_y}(t)=\delta_y/t$, y de ahí

$$
\Vert\chi+G_{S_y}\Vert_2^2\ge q_y\,\delta_y^2,
$$

cantidad que crece sin cota al aumentar $y$: por el producto de Mertens y el teorema de los números primos, $q_y\delta_y^2\asymp y/\log^2y$. Al mismo tiempo, para cada $t>0$ fijo, $G_{S_y}(t)\to-\chi(t)$. La recuperación puntual en cada ventana fija coexiste con una norma que crece sin cota. El control se refiere a la criba directa; el aproximante óptimo se trata en §3 y §6.

### 7.1. Oscilación media en un período completo de la criba

Además del control cerca de $t=0$, existe una fórmula exacta para la **magnitud cuadrática media** de la combinación aritmética en la variable inversa $u=1/t$. Sea $S$ un conjunto **no vacío** de $k$ primos, $M=\prod_{p\in S}p$, $\rho=\prod_{p\in S}(1-1/p)$ y

$$
H_S(u)=\sum_{d\mid M}\mu(d)\left\lbrace\frac{u}{d}\right\rbrace,\qquad
Q_S=\frac1M\int_0^M\bigl(1+H_S(u)\bigr)^2\,du.
$$

El promedio de $H_S$ en ese período es cero, porque $\sum_{d\mid M}\mu(d)=0$. La identidad clásica de Franel para la covarianza de dos funciones fraccionarias con períodos enteros da

$$
\frac1M\int_0^M\left(\left\lbrace\frac{u}{d}\right\rbrace-\frac12\right)\left(\left\lbrace\frac{u}{e}\right\rbrace-\frac12\right)du=\frac{\gcd(d,e)^2}{12\,de}.
$$

Al expandir $H_S^2$, la suma factoriza primo a primo:

$$
Q_S=1+\frac1{12}\prod_{p\in S}2(1-p^{-1})=1+\frac{2^k\rho}{12}.\qquad\text{(P)}
$$

Cada primo añadido multiplica $Q_S-1$ por $2(1-1/p)$, factor que vale $1$ para $p=2$ y supera $1$ para todo $p\ge3$. El recierre de saltos discretos coexiste así con oscilaciones cuadráticas medias crecientes en la variable $u=1/t$. $Q_S$ es un promedio periódico de la criba, distinto de la norma óptima $e_m^2$. `scripts/verificar_periodos.py` verifica la fórmula por integración racional exacta para $S=\lbrace2\rbrace$, $\lbrace2,3\rbrace$, $\lbrace2,3,5\rbrace$ y $\lbrace2,3,5,7\rbrace$.

## 8. Contrato de transferencia CME → RH y estado de las esferas

Para declarar una correspondencia geométrica genuina debe especificarse, **antes de medir mejoras**, una familia de representaciones $\rho_m$ de los generadores originales de CME–002 y mapas $T_m$ al sistema funcional que satisfagan simultáneamente:

1. **Composición:** las identidades, órdenes e involuciones originales se preservan; donde el recinto exige $(s_is_j)^k=I$, su imagen cumple esa relación sin colapsar artificialmente los generadores.
2. **Focos:** las intersecciones geométricas se corresponden con focos aritméticos mediante una regla explícita, más allá de la semejanza de vocabulario.
3. **Consulta:** se conservan la pregunta $\chi$, la clase permitida de reconstrucciones y la información heredada al mover la pared.
4. **Alcance:** se demuestra que las operaciones acceden a componentes de $U_{m,2m}$ y se identifica cualquier complemento invisible.
5. **Uniformidad:** se obtiene una estimación no circular que controle la recuperación acumulada, por ejemplo $\gamma_{2^j}\ge c_j\ge0$ con $\sum_jc_j=\infty$, compatible con la cota inferior de Burnol. Por §3, esa estimación equivale a RH.

Las *esferas* de las pruebas funcionales son esferas unitarias de direcciones en Hilbert. Su identificación con las esferas físicas o geométricas originales está **abierta**.

## 9. Tabla de procedencia y estado

| Afirmación | Estado | Procedencia o prueba |
|---|---|---|
| CRT, inclusión-exclusión, transformada de Mellin finita, saltos de Möbius | Clásica / demostración directa | R–01/R–03; §2 y §4 |
| Recierre $J_N(n)=-\mu(n)$, $J_{2N}(n)=0$ | Demostrado | Proposición F; `scripts/verificar_focos.py` |
| Conteo de 621 focos; ejemplo 1030 | Verificación finita exacta | `scripts/verificar_focos.py` |
| El error de la criba fija crece de 16 a 32 | Control numérico reproducido | `scripts/verificar_focos.py` |
| Identidad (R) y reflexión asociada | Demostrado en Hilbert | §3; ejemplos finitos en `scripts/verificar_reflexiones.py` |
| Grupo finito o infinito frente a recuperabilidad | Contraejemplos demostrados | §3; `scripts/verificar_reflexiones.py` |
| RH ⇔ $e_m\to0$ en la familia libre de cuadrados | Clásica | Báez-Duarte (2002), Proposición 3.1 de la segunda versión; §1.2 |
| RH ⇔ $\sum_j\gamma_{2^j}=\infty$ | Demostrado a partir de (BD) | §3 |
| Certificado de tres ventanas | Demostrado; equivalente a RH a partir de (BD) | §5; controles auxiliares en `scripts/verificar_puentes.py` |
| Oscilación media periódica $Q_S$ | Demostrado | Fórmula (P); `scripts/verificar_periodos.py` |
| $e_m^2$ hasta 2048 y $\gamma_{1024}$ ≈ 6.64 % | Recalculado en coma flotante doble | `scripts/recalcular_gram.py`; coincide con `resultados/registro_mecanismos_original.txt` |
| Ley $\gamma_{2^j}\ge1/(j+2)$ | Refutada en $j=10$ | §6; `scripts/recalcular_gram.py` |
| Asignación de $f_n$ como normal de espejo | Descartada en el ejemplo 1027/1030 | §4.4; `scripts/ensayo_angulos.py` |
| Entrecruzamiento CME–002 con el criterio funcional | Abierto | §8 |
| RH | Abierta | Reformulada como $\sum_j\gamma_{2^j}=\infty$ (§3) |
| GRH | Abierta | Comparación algebraica con el marco de Masullo en §2.3 |

## 10. Fuentes

**Notas de trabajo consolidadas (20–21 XI 2026).** Sus huellas SHA-256 figuran en `PROCEDENCIA_Y_HUELLAS.md`.

- Anexo técnico del 20 XI (`ANEXO_TECNICO_ES.md`, entrega `2026-11-20_resolucion_granularidad_riemann`): fuente del certificado de tres ventanas.
- Nota *Mecanismos del programa frente a la regla de eliminación entre escalas*, con el script `scripts/prueba_reglas_de_peso.py` y los registros `resultados/registro_mecanismos_original.txt`, `resultados/registro_bloques_primos_original.txt` y `resultados/salida_prueba_reglas_de_peso_original.txt`.
- Notas del 21 XI `CME_RH_PUENTE_REFLEXIONES_Y_CIERRE_2026-11-21.md`, `ENSAYO_CME_ARIT_1024_2048_2026-11-21.md` y `FOCOS_DETERMINACION_CME_RH_2026-11-21.md`; sus verificadores están en `scripts/`.
- Auditoría preliminar de las correspondencias con el marco de Masullo (nota de trabajo); los problemas de normalización, convergencia y dominios se tratan en §2.

**Documentos del programa.**

- [R–01/R–02 — *Las escalas relacionales de la criba*, v1.0, 17 XI 2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/FORMALIZACION_R01_R02_ES.md)
- [R–03 — *Herencia espectral, normalización y ubicación de los ceros*, v0.3, 18 XI 2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-11-17_escalas_relacionales_riemann/2026-11-18_r03_herencia_espectral/R03_HERENCIA_Y_LOCALIZACION_ES.md)
- [R–RH–01 — *Primos, reflexión y cierre*, manuscrito fuente del 1 XI 2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/791defa354a636067e3f36aa4543af993a79e7bb/antecedentes/R_RH_01_Primos_Reflexion_y_Cierre_2026-11-01.md): antecedente en el PR #9, en borrador al 21 XI 2026.
- [CME–002 — *La pared que se corre: ángulos e identidades*, 24 X 2026](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/2026-10-24/02_REALIZACIONES/01_cubo_de_espejos/CME-002_pared_que_se_corre/CME-002_Pared_que_se_corre.md)
- [Laboratorio de radios y pared móvil — v5.1](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/main/laboratorios/laboratorio_optica_radios_v5_1/README.md)
- [Identidad contextual y promoción de escala](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/blob/main/02_formal_core/contextual_identity_and_scale_promotion.es.md)
- [Cierre relativo y control uniforme](https://github.com/EndlessMonkeyProyect/Relational-Geometry-program/blob/main/02_formal_core/relative_closure_and_uniform_control.es.md)

**Literatura.**

- L. Báez-Duarte, [*A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*](https://arxiv.org/abs/math/0202141): equivalencia con RH para los índices enteros.
- L. Báez-Duarte, [*A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis, 2*](https://arxiv.org/abs/math/0205003): Proposición 3.1 (M. Balazard), aproximantes con coeficientes de Möbius bajo RH.
- J.-F. Burnol, [cota inferior en el problema de aproximación de Nyman–Beurling](https://arxiv.org/abs/math/0103058).
- S. Bettin, J. B. Conrey y D. W. Farmer, [*An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion*](https://arxiv.org/abs/1211.5191) (hipótesis: RH y una condición sobre $\zeta'$).
- Masullo, [*The Music of the Primes*](https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf): marco externo de comparación.

**Le Matt Ansatz Di Ego** · Endless Monkey Project · Relational Geometry Program
