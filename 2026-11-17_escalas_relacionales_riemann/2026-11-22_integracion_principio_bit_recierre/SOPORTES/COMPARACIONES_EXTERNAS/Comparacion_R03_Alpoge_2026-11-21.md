# Correspondencia matemática entre R–03 y la demostración formal de Riemann

**Nota técnica de examen · 21 de noviembre de 2026**  
**Endless Monkey Project / Relational Geometry Program**  
**Objeto:** discrepancia de criba, derivada logarítmica de zeta, sumas ponderadas de von Mangoldt, criterio de ventanas y condiciones de transferencia.  
**Estado:** identidades del puente **demostradas por cálculo clásico**; verificación aritmética finita **reproducida**; teorema RH/GRH **certificado formalmente por Lean/Mathlib en la biblioteca de Alpöge**; interpretación de su prueba en lenguaje humano **preliminar**; transferencia de las estimaciones automórficas al sistema de discrepancias **no establecida**.

## 1. Procedencia documental y alcance

La rama principal del repositorio [programa-geometria-relacional](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional) conserva R–03 v0.3. La edición R–03 v0.4 está propuesta en [PR #9](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/9), todavía en borrador. El [PR #11](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/11), también en borrador, propone un compendio CME–RH: proyecciones, norma de cierre, discretización y ventanas. Esta nota no confunde el código de esas ramas con el contenido fusionado en `main`.

La [nota de Alpöge](https://alpo.ge/remark.pdf) anunció una demostración Lean el 20-XI-2026. La [declaración conjunta de Lean y Mathlib](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), 21-XI, informa la compilación, comparación del enunciado canónico y validación del término de prueba por verificadores distintos. El [repositorio comunitario de verificación](https://github.com/leanprover-community/riemann-hypothesis) organiza esos controles. Para reconstruir los mecanismos se consultó también la [nota preliminar de Robin Zhang](https://hexagonmath.org/pdf/2611.00809v1) y la [cartografía de pruebas](https://github.com/nasqret/riemann-rev). Esos textos explicativos tienen carácter preliminar: el control formal de Lean no significa que cada interpretación expositiva haya sido auditada contra los 17 millones de líneas.

**Objeto de comparación:** la demostración formal de *Levent Alpöge* —no la propuesta contemporánea de *Alessandro Masullo*. Ambas se anunciaron el 20-XI-2026 y son desarrollos distintos.

## 2. Punto de partida: discrepancia y Mellin (R–03)

Para un conjunto finito de primos \(S\), defínanse

\[
M_S=\prod_{p\in S}p,\qquad
\delta_S=\prod_{p\in S}(1-p^{-1}),\qquad
A_S(x)=\#\{1\le n\le x:\gcd(n,M_S)=1\},
\]

\[
E_S(x)=A_S(x)-\delta_S x,\qquad
F_S(s)=\int_0^\infty E_S(x)x^{-s-1}\,dx.
\]

Para \(0<\Re s<1\), el cálculo de R–01/R–03 da

\[
\boxed{F_S(s)=\frac{\zeta(s)}{s}P_S(s)},\qquad
P_S(s)=\prod_{p\in S}(1-p^{-s}).\tag{R03.1}
\]

En dicha franja \(P_S(s)\ne0\). Por eso \(F_S\) y \(\zeta\) comparten ceros y multiplicidades. Para derivar en \(\Re s>1\) se usa la **continuación meromorfa** del lado derecho de (R03.1), no la integral original fuera de su franja.

## 3. Proposición A: descomposición exacta de las potencias primas

La identidad de derivadas logarítmicas es

\[
\frac{F'_S}{F_S}=\frac{\zeta'}{\zeta}+\frac{P'_S}{P_S}-\frac1s,
\qquad
\frac{P'_S}{P_S}=\sum_{p\in S}\frac{\log p}{p^s-1}.
\]

Por tanto, para \(\Re s>1\),

\[
\boxed{-\frac{\zeta'(s)}{\zeta(s)}=-\frac{F'_S(s)}{F_S(s)}-\frac1s+\sum_{p\in S}\frac{\log p}{p^s-1}.}\tag{A1}
\]

Y, puesto que

\[
-\frac{\zeta'(s)}{\zeta(s)}=\sum_{p}\sum_{k\ge1}\frac{\log p}{p^{ks}},\qquad
\frac{\log p}{p^s-1}=\sum_{k\ge1}\frac{\log p}{p^{ks}},
\]

se obtiene la versión más operativa

\[
\boxed{-\frac{F'_S(s)}{F_S(s)}-\frac1s=
\sum_{p\notin S}\sum_{k\ge1}\frac{\log p}{p^{ks}}.}\tag{A2}
\]

**Interpretación precisa:** al incorporar un primo a la referencia \(S\), la derivada logarítmica de la transformada de discrepancia elimina exactamente la familia completa de sus potencias primas. Es una partición algebraica de la información aritmética; la fórmula procede de identidades clásicas del producto de Euler y no constituye un nuevo teorema sobre la localización de ceros.

La fórmula (A1) se prolonga meromórficamente allí donde las expresiones estén definidas. La serie de (A2) se usa exclusivamente en \(\Re s>1\).

## 4. Proposición B: correspondencia en la variable de escala

Para \(y\ge1\), considérese la suma de von Mangoldt ponderada

\[
T(y)=\sum_{n\le y}\Lambda(n)\left(\frac yn-1\right)
=\sum_p\sum_{\substack{k\ge1\\p^k\le y}}\log p\left(\frac y{p^k}-1\right).
\]

Descompóngase como \(T(y)=B_S(y)+R_S(y)\), con

\[
B_S(y)=\sum_{p\in S}\sum_{p^k\le y}\log p\left(\frac y{p^k}-1\right),\quad
R_S(y)=\sum_{p\notin S}\sum_{p^k\le y}\log p\left(\frac y{p^k}-1\right).
\tag{B1}
\]

El cálculo de la transformada para \(\Re s>1\) es

\[
\int_{n}^{\infty}\left(\frac yn-1\right)y^{-s-1}\,dy=\frac{n^{-s}}{s(s-1)}.
\tag{B2}
\]

Intercambiando suma e integral absolutamente,

\[
\boxed{\int_1^\infty R_S(y)y^{-s-1}\,dy
=\frac{-F'_S(s)/F_S(s)-1/s}{s(s-1)}},\qquad \Re s>1.\tag{B3}
\]

La identidad (B3) es el **puente exacto en el espacio de escalas**: la misma transformada de R–03 codifica, tras la derivada logarítmica, la suma ponderada de *las potencias primas todavía externas a la referencia*.

La cantidad centrada de Alpöge para el carácter principal es

\[
G(y)=T(y)-y(\log y-1-\gamma),\tag{B4}
\]

con \(\gamma\) constante de Euler. En consecuencia, R–03 recupera algebraicamente el observable mediante

\[
\boxed{G(y)=R_S(y)+B_S(y)-y(\log y-1-\gamma).}\tag{B5}
\]

Esta fórmula es exacta para cada \(y\ge1\) y cualquier \(S\) finito.

## 5. Una obstrucción cuantitativa instructiva: el término lineal

Para un primo fijo \(p\in S\), sea \(K=\lfloor\log_p y\rfloor\). Entonces

\[
B_{\{p\}}(y)=\log p\left[\frac{y(1-p^{-K})}{p-1}-K\right]
=\frac{\log p}{p-1}y+O_p(\log y).\tag{C1}
\]

Para \(S\) finito fijo,

\[
B_S(y)=y\sum_{p\in S}\frac{\log p}{p-1}+O_S(\log y).\tag{C2}
\]

Por tanto, **quitar las potencias primas heredadas introduce un término principal de orden \(y\)**. Para buscar una cota de orden \(y^{1/2+\varepsilon}\) hace falta un centrado coherente y controlar el resto uniformemente. La descomposición exacta no entrega por sí misma esa cancelación. Si \(S=S(y)\) crece con la escala, deben establecerse además cotas uniformes en \(S\).

## 6. El paso decisivo de la prueba formal: ventanas unilaterales

El análisis de la biblioteca Lean, expuesto provisionalmente en [Zhang, §1–2](https://hexagonmath.org/pdf/2611.00809v1) y en la [cartografía de la prueba](https://github.com/nasqret/riemann-rev), utiliza para cada carácter primitivo \(\psi\) una combinación **con coeficientes positivos** de \(G\) y de partes reales de \(G_\chi\), donde \(\chi\) recorre los caracteres primitivos asociados con las potencias de \(\psi\). La forma central de la estimación es

\[
\forall\varepsilon>0\ \text{(suficientemente pequeño)},\quad
\exists\text{ valores de }Y\text{ arbitrariamente grandes}:\qquad
G_\psi(y)\le y^{1/2+9\varepsilon}
\quad\forall y\in[Y,Y^{3/2}].\tag{D1}
\]

La positividad de las combinaciones evita que polos de derivadas logarítmicas correspondientes a ceros se cancelen. Un argumento localizado de tipo Landau vincula (D1) con la ausencia de ceros a la derecha de la línea crítica; la ecuación funcional traslada la exclusión al otro semiplano de la franja. La estimación (D1) surge de la parte aritmético-automórfica de la demostración, con cadenas de levantamientos theta, divisibilidad de períodos, desigualdades de pendientes, Galois e Iwasawa. La [comunidad Lean/Mathlib](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) certifica el teorema formal; la explicación de estas técnicas continúa en elaboración.

## 7. Comparación de obligaciones matemáticas

| Aspecto | R–03 y anexos de cierre | Demostración de Alpöge |
|:--|:--|:--|
| Dato inicial | Discrepancia de coprimalidad \(E_S(x)\) | Suma ponderada de von Mangoldt \(T(y)\) y versiones torcidas |
| Codificación espectral | \(F_S=\zeta P_S/s\) | \(-L'/L\) y transformada de Mellin de una rampa |
| Paso común exacto | (A1)–(B5): derivada logarítmica y partición de potencias primas | Mismo dato aritmético luego del cambio de representación |
| Cantidad crítica | Cota en el pivote \(s=1/2\) (Akatsuka); o convergencia en norma \(L^2\) (Báez-Duarte) | Cota superior unilateral en ventanas para combinaciones positivas |
| Fuente de la cota | Abierta en las propuestas del programa | Proporcionada por la construcción aritmética y automórfica formalizada |
| Estado | Identidades y equivalencias conocidas/corroboradas; transferencia pendiente | RH y GRH de Dirichlet certificados como teoremas Lean, con explicación humana en progreso |

**Separación esencial:** la condición equivalente a RH reformulada con Akatsuka en R–03 no es la estimación localizada (D1); comparten información sobre ceros, pero sus cuantificadores, variables, pesos y métodos de control son distintos. La regla de reducción del residuo en \(L^2\) de CME–RH tampoco se deduce de (A1)–(B5).

## 8. Extensión algebraica a caracteres

Para un carácter de Dirichlet \(\chi\), se puede **definir formalmente**

\[
F_{S,\chi}(s)=\frac{L(s,\chi)}s\prod_{p\in S}(1-\chi(p)p^{-s}).
\]

En \(\Re s>1\), la misma derivación da

\[
-\frac{F'_{S,\chi}(s)}{F_{S,\chi}(s)}-\frac1s
=\sum_{p\notin S}\sum_{k\ge1}\frac{\log p\,\chi(p)^k}{p^{ks}}.\tag{E1}
\]

Es una extensión algebraica exacta: **no** se ha demostrado aquí que esa función proceda de un observable geométrico de criba con todas las propiedades requeridas, ni que sus combinaciones ofrezcan cotas unilaterales. Para recuperar la prueba generalizada harían falta controles uniformes en conductores, caracteres, escalas y parámetros de las ventanas.

## 9. Laboratorio reproducible y resultado finito

El script adjunto `verificar_puente_R03_Alpoge.py` comprueba, para \(y=30\), que la partición de la suma ponderada por \(S=\{2,3\}\) coincide exactamente término a término en los coeficientes racionales de \(\log p\). En particular,

\[
B_{\{2,3\}}(30)=\frac{193}{8}\log2+\frac{103}{9}\log3,
\]

\[
R_{\{2,3\}}(30)=\frac{26}{5}\log5+\frac{23}{7}\log7
+\frac{19}{11}\log11+\frac{17}{13}\log13
+\frac{13}{17}\log17+\frac{11}{19}\log19
+\frac7{23}\log23+\frac1{29}\log29.
\]

La verificación también contrasta \(B_{\{p\}}\) con la forma cerrada (C1), para \(p=2,3\), y \(T=B_S+R_S\) a distintas escalas. Esto verifica una **identidad finita**, no una estimación asintótica ni una afirmación sobre ceros.

## 10. Dictamen y objetivo siguiente

**Demostrado en esta nota:** identidad (A2) de eliminación de potencias primas por referencia; identidad (B3) de Mellin para el resto; reconstrucción de \(G\) mediante (B5); término principal (C2); extensión algebraica (E1). Todo corresponde a consecuencias conocidas de Euler, Mellin y la derivada logarítmica.

**Correspondencia identificada:** R–03 y el argumento formal codifican el mismo flujo aritmético de potencias primas en representaciones distintas. El programa organiza esa codificación mediante referencia, herencia y normalización; la prueba formal añade una estimación cuantitativa unilateral cuya procedencia es automórfica y aritmética.

**Obligación precisa para avanzar:** formular y demostrar, sin emplear RH/GRH ni equivalentes como premisas, una regla que produzca desde las discrepancias \(E_S\), con elección explícita de \(S=S(y,\chi,\varepsilon)\) y control de los términos principales, una cota **uniforme** de tipo (D1), incluyendo las combinaciones positivas de caracteres. Una alternativa es demostrar directamente una cota en norma \(L^2\) suficiente para el criterio funcional, pero eso es otra ruta y requiere un puente cuantitativo separado.

**Resultado del examen:** correspondencia algebraica **exacta**; transferencia del mecanismo de demostración **no acreditada**; prioridad u originalidad de los ingredientes clásicos **no reivindicadas**.

---

**Endless Monkey Project / Relational Geometry Program**
