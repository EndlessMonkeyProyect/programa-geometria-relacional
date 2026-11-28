# Anexo T.1 — Herencia local, defectos de reflexión y cierre autónomo

**Complemento de investigación de T.1 v1.4 · 28 de noviembre de 2026**  
Endless Monkey Project / Relational Geometry Program

## Estatuto

Se desarrolla una equivalencia interna por defectos locales de herencia, una ley de variación absoluta de los coeficientes óptimos, una obstrucción local de referencias ausentes y una cota de recuperación para una referencia lejana. Se amplía el laboratorio a 448 transiciones y se certifica por intervalos una violación de la cota universal por primo, incluso con profundidad ilimitada. No se presupone RH en los lemas internos. La identificación final con RH utiliza la Proposición 8 de T.1 v1.4 (Báez-Duarte). La anulación general de los defectos permanece abierta: el complemento no constituye una prueba autónoma de RH. No se reclama prioridad frente a otras formulaciones de convergencia de coeficientes.

## 1. Convenio y continuidad de los focos

En $H=L^2((0,\infty),dt/t^2)$, $e_d(t)=\{t/d\}$, $\chi=1_{[1,\infty)}$. Para $S$ finito, $P_S=\prod_{p\in S}p$, $V_S=\operatorname{span}\{e_d:d\mid P_S\}$. Sean $a_S=\Pi_S\chi=\sum_{d\mid P_S}c_S(d)e_d$, $u_S=\chi-a_S$, $Q_S=\|u_S\|^2$. Los coeficientes se extienden por cero a los demás enteros. Se escribirá $\mu$ para Möbius y $\mu_p$ para la cota del espejo de T.1.

Sea $\mathcal A$ el espacio de funciones que son afines en cada intervalo $(n,n+1)$, $n\ge0$, con pendiente común $s(f)$ y con $f(t)=s(f)t$ en $(0,1)$. Se consideran representantes afines en intervalos abiertos. Es un subespacio cerrado de $H$: la pendiente es el funcional continuo $s(f)=\langle f,g_0\rangle$, con $g_0=t1_{(0,1)}$, $\|g_0\|=1$; y los promedios $M_n(f)=\int_n^{n+1}f(t)dt$ son continuos por Cauchy–Schwarz, con representantes $t^2 1_{(n,n+1)}$. En el intervalo $(n,n+1)$ la función queda fijada por $s(f)(t-n-1/2)+M_n(f)$. Las restricciones convergen localmente en $H$, por lo que la estructura persiste al tomar límites. $\chi$ y todas las referencias están en $\mathcal A$.

**Lema A1 (focos continuos).** Para $n\ge1$ el salto ascendente $J_n(f)=f(n+)-f(n-)$ tiene la fórmula

$$J_n(f)=M_n(f)-M_{n-1}(f)-s(f)=\langle f,g_n\rangle,$$

$$g_n=t^2(1_{(n,n+1)}-1_{(n-1,n)})-g_0.$$

Por inversión de Möbius se define el funcional continuo

$$C_d(f)=-\sum_{k\mid d}\mu(d/k)J_k(f)=\langle f,h_d\rangle,\qquad h_d=-\sum_{k\mid d}\mu(d/k)g_k.$$

Aquí el producto interno es real. Como $J_n(e_d)=-1_{d\mid n}$ y $J_n(\chi)=1_{n=1}$, se tiene $C_d(e_e)=1_{d=e}$, $C_d(a_S)=c_S(d)$, $C_d(\chi)=-\mu(d)$. En particular la base finita es linealmente independiente. Se obtiene sin estimar el condicionamiento global:

$$|c_S(d)+\mu(d)|\le\|h_d\|\sqrt{Q_S}. \tag{A1}$$

El término $d=1$ conserva la pendiente común; en $d>1$ la suma de los coeficientes de Möbius es cero y el término de pendiente se cancela. El certificado utiliza solamente los intervalos hasta $d+1$.

## 2. Convergencia y variación absoluta

**Lema A2.** Para una cadena creciente $S_j$, las diferencias $w_j=a_{S_{j+1}}-a_{S_j}$ son ortogonales entre sí, y $\|w_j\|^2=Q_{S_j}-Q_{S_{j+1}}$. Por telescopaje $a_{S_j}$ converge fuertemente a $a_\infty=\Pi_{V_\infty}\chi$, donde $V_\infty=\overline{\bigcup_j V_{S_j}}$. El límite $Q_\infty\in[0,Q_{S_0}]$ existe sin RH. Para todo $d$ fijo, $c_{S_j}(d)$ converge a $C_d(a_\infty)$.

Más generalmente, para cualquier $h\in H$, si $Z_j=V_{S_{j+1}}\cap V_{S_j}^\perp$, entonces

$$\sum_{j\ge m}|\langle w_j,h\rangle|\le\sqrt{Q_{S_m}-Q_\infty}\left(\sum_{j\ge m}\|\Pi_{Z_j}h\|^2\right)^{1/2}\le\|h\|\sqrt{Q_{S_m}-Q_\infty}. \tag{A2}$$

Demostración: $w_j\in Z_j$, los $Z_j$ son mutuamente ortogonales, y se aplica Cauchy–Schwarz a la serie de productos de normas. Con $h=h_d$ resulta variación absoluta finita para cada coeficiente. Con $h=h_d+h_{pd}$ resulta variación absoluta finita para el defecto de herencia $D_S(d,p)=c_S(d)+c_S(pd)$, para todo $d$ libre de cuadrados y $p\nmid d$.

Al añadir un primo $q$ se dispone también de la actualización exacta del anexo T.1: en la ordenación de los bloques antiguos y nuevos, $y=S_q^{-1}v$, $c'=(c-G^{-1}Cy,y)$. Para una pareja ya presente en el bloque antiguo, el cambio del defecto es la suma de las dos coordenadas correspondientes de $-G^{-1}Cy$. La fórmula convierte la anulación del defecto en un problema de cancelación de una serie absolutamente convergente. La convergencia por sí sola no fija su suma.

## 3. Coherencia hereditaria: equivalencia interna

**Teorema A3.** Sea la cadena cofinal en los conjuntos finitos de primos. Son equivalentes:

(i) $Q_{S_j}\to0$.

(ii) $c_{S_j}(d)\to-\mu(d)$ para cada $d$ libre de cuadrados.

(iii) $D_{S_j}(d,p)\to0$ para cada $d$ libre de cuadrados y cada primo $p\nmid d$.

(iv) $J_n(u_{S_j})\to0$ para cada entero $n\ge1$.

Demostración. (i) implica (ii) por (A1) e implica (iv) por continuidad de $J_n$. (ii) implica (iii) por multiplicatividad de Möbius. Para (iii), el lema A2 da límites $c_\infty(d)$; por inducción sobre el número de factores primos, $c_\infty(d)=c_\infty(1)\mu(d)$ en el diccionario libre de cuadrados. En los índices no libres de cuadrados, $C_d(a_\infty)=0$ por continuidad. Por inversión, $J_n(a_\infty)=-\sum_{d\mid n}C_d(a_\infty)=-c_\infty(1)1_{n=1}$. Por ello $a_\infty+c_\infty(1)\chi$ tiene todos sus saltos nulos y pertenece a $\mathcal A$. Una función de $\mathcal A$ sin saltos es $st$ en toda la semirrecta; la condición $L^2(dt/t^2)$ obliga a $s=0$. Así $a_\infty=\lambda\chi$. Como $a_\infty$ es una proyección de $\chi$, $\lambda=\lambda^2$, y $\lambda\ne0$ porque $e_1\in V_\infty$ y $\langle\chi,e_1\rangle=1-\gamma>0$. Luego $\lambda=1$. Finalmente, (iv) implica que $u_\infty\in\mathcal A$ tiene todos sus saltos nulos, y el mismo argumento da $u_\infty=0$.

Por T.1 v1.4, Proposición 8, las cuatro condiciones equivalen a RH. La equivalencia con (iii) requiere solamente el defecto límite de cada pareja fija, sin uniformidad simultánea ni velocidad de convergencia. La prueba autónoma necesitaría demostrar la anulación de esos límites, no solo su existencia.

**Determinante operativo:** el defecto no es la diferencia de dos cantidades arbitrarias; es la falta de coherencia entre dos referencias ligadas por una incorporación prima. La interpretación del espejo es aritmética y no una identidad con una reflexión óptica física.

## 4. Referencia ausente y cobertura local

**Lema A4.** Si $p\notin S$, para todo $e_d\in V_S$ se cumple $J_p(e_d)=J_1(e_d)$, porque el único divisor de $p$ presente en el diccionario es 1. En cambio $J_p(\chi)-J_1(\chi)=-1$. Por tanto

$$Q_S\ge\frac{1}{\|g_p-g_1\|^2}=\begin{cases}1/16,&p=2,\\1/(2p^2+10/3),&p\ge3.\end{cases} \tag{A3}$$

La norma se calcula integrando $t^2$ en los intervalos de los representantes, con coeficiente -2 en $(1,2)$ si $p=2$. Para $p\ge3$ los dos pares de intervalos son disjuntos. Se obtiene una obstrucción local explícita mientras falta una referencia prima, independiente de la cantidad de primos mayores incorporados. Esta cota inferior desaparece al agotar los primos y no constituye una cota superior del resto global.

## 5. Recuperación en una referencia lejana

**Lema A5.** Fijado $S$, sean $s=\sum c_S(d)/d$, $m=1-\tfrac12\sum c_S(d)$, $A=\|e_1\|^2=\log(2\pi)-\gamma$, $F=1-a_S$. $F$ es periódica de período $P_S$ y media $m$, y $u_S(t)=F(t)$ para $t\ge1$, $u_S(t)=-st$ para $t<1$. Se tiene

$$|x\langle u_S,e_x\rangle-m\log x|\le C_S:=|s|+\tfrac18\sum_{d\mid P_S}d|c_S(d)|+(1-\gamma)(1+\sum_{d\mid P_S}|c_S(d)|),\qquad x\ge1. \tag{A4}$$

Aquí $e_x=\{t/x\}$ también para parámetros reales. Prueba: para $t<x$, $e_x=t/x$. Se divide $x\langle u_S,e_x\rangle$ en $(0,1)$, $(1,x)$ y $(x,\infty)$. La primera contribución es $-s$. En la segunda se separa $m\log x$ y se integra por partes el término de media cero; su primitiva desde 1 tiene módulo a lo sumo $\sum d|c_S(d)|/8$, pues una primitiva periódica de $e_d-1/2$ tiene oscilación $d/8$. La última contribución tiene módulo a lo sumo $\|F\|_\infty\int_1^\infty\{y\}dy/y^2=(1-\gamma)\|F\|_\infty$. Se usa $\|F\|_\infty\le1+\sum|c_S(d)|$.

En particular, para un primo $p\notin S$,

$$\eta_p\ge\mu_p\ge\frac{(|m|\log p-C_S)_+^2}{p A Q_S}. \tag{A5}$$

Se usa el testigo individual $e_p$ en el bloque dilatado, cuya norma al cuadrado es $A/p$. Si $m\ne0$, $p\mu_p\to\infty$ para $S$ fijo y $p\to\infty$. Más precisamente, con $\ell=(1/d)_{d\mid P_S}$ y el Gram $G$ heredado, (A4) aplicado a $x=pd$ da

$$p\mu_p=\frac{m^2\ell^*G^{-1}\ell}{Q_S}(\log p)^2+O_S(\log p+1).$$

La estimación tiene dependencia explícita de la totalidad fija y no es uniforme cuando $S$ crece. Tampoco permite sumar recuperaciones calculadas con el mismo resto congelado como si fueran incrementos ortogonales. En la cadena natural, la media cambia de signo y las constantes de (A4) pueden crecer; este mecanismo no cierra la divergencia por sí solo.

## 6. Laboratorio y contraejemplo certificado

Se recorren todas las parejas $(S,p)$ con $S\subseteq\{2,3,5,7,11,13,17\}\setminus\{p\}$. Total $7\cdot2^6=448$. Con la métrica funcional de T.1 v1.4 se obtienen 208 valores $pR_{p,4}<1$ en doble precisión. Ejemplos:

| S | p | p R4 | p eta |
|---|---:|---:|---:|
| 2,3,5,7,11 | 13 | 1.12373 | 1.63726 |
| 11 | 13 | 0.50765 | 0.70262 |
| 7,11 | 13 | 0.05114 | 0.06621 |
| 5,7,11,17 | 13 | 0.01230 | 0.01840 |

Para $S=\{11\}$, $p=13$, se repite el cálculo de $Q_S$ y $Q_{S+p}$ por eliminación gaussiana con intervalos de mpmath.iv (50 cifras, datos enteros y funciones intervalares, fórmula de Vasyunin del anexo). Se obtiene $0.70261<13\eta_{13}<0.70263<1$. Como $R_{p,k}\le\eta_p$ para todo $k$, ninguna profundidad cumple $R_{13,k}\ge1/13$ en esa transición. La certificación se refiere a la fórmula analítica de Gram y al backend de intervalos empleado; no es una formalización Lean. No refuta la conjetura eventual específica de la cadena natural, ni una cota universal con una constante positiva menor desconocida.

El segundo control extrae coeficientes por saltos y los compara con las ecuaciones normales, verifica ortogonalidad de los incrementos y las cotas (A1)–(A2) en los casos finitos. Ejemplos de la cadena natural:

| Último primo | c(1) | c(2) | c(3) | c(6) | D(1,2) | D(1,3) |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | -0.922685 | 1.022286 | 1.035642 | 0.588756 | 0.099601 | 0.112957 |
| 7 | -0.949177 | 0.950772 | 0.932509 | -0.416682 | 0.001595 | -0.016668 |
| 13 | -0.962104 | 0.967688 | 0.936075 | -0.587815 | 0.005583 | -0.026029 |
| 17 | -0.970748 | 0.970043 | 0.956175 | -0.718021 | -0.000705 | -0.014574 |

Los defectos pueden cambiar de signo y magnitud. Estos resultados no determinan el límite. Los JSON contienen todas las transiciones y los coeficientes seleccionados. Las siete etapas de v1.4 siguen intactas.

## 7. Obligación pendiente y decisión editorial

La ruta propuesta es demostrar una propiedad de cancelación de las correcciones de un par fijo: después de que $d,pd$ estén presentes, la suma de sus correcciones por todos los primos posteriores debe ser exactamente el defecto inicial con signo opuesto. El lema A2 garantiza existencia absoluta de esa suma, pero no su valor. Un argumento aritmético que fuerce esa cancelación para toda pareja establecería la condición (iii) del Teorema A3. Otra ruta consiste en probar que todos los saltos del resto límite se anulan.

No se sustituye T.1 v1.4 ni el complemento de transferencia externa. Incorporar este documento como investigación autónoma, mantener abiertos la anulación de defectos y el entrelazamiento directo con los operadores automorfos. El control por intervalos corrige cualquier lectura de la cota $1/p$ como propiedad universal de la herencia sin restricciones sobre la cadena. No se modifica el repositorio remoto.

## Referencias

- Anexo T.1 v1.4, Proposición 8 y §8; complemento de cierre global y transferencia analítica, 28 nov. 2026.
- L. Báez-Duarte, [A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis](https://arxiv.org/abs/math/0202141), 2002/2003; la restricción libre de cuadrados se deduce de sus aproximantes con Möbius como en T.1 v1.4.
- L. Báez-Duarte, [Arithmetical Aspects of Beurling's Real Variable Reformulation of the Riemann Hypothesis](https://arxiv.org/abs/math/0011254), 2000. Antecedente sobre convergencias aritméticas; no se afirma novedad bibliográfica de los criterios de coeficientes.
