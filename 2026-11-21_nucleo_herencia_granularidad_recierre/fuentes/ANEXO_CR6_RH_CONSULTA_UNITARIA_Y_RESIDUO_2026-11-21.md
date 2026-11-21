# Suficiencia de la consulta unitaria y agotamiento del residuo

**Anexo de formalización — 21 de noviembre de 2026**  
**Continuidad:** CR–6 · G–01 · R–RH–01 · R–03 (v0.4) · auditoría de herencia prima del 20-XI-2026  
**Estado:** identidades funcionales y teoremas condicionales **DEMOSTRADOS**; cobertura de referencias **RECUPERADA DE DOCUMENTOS PREVIOS**; recuperación global incondicional **ABIERTA**.

## Resumen

La incorporación de referencias primas y la construcción de interfaces funcionales están formalizadas en documentos anteriores. Este anexo fija una consulta escalar que mide **exactamente** el residuo de la proyección ortogonal en la norma relevante para el criterio de Nyman–Beurling/Báez-Duarte. Se demuestra que la consulta unitaria coincide con la energía residual, que la incorporación de nuevas referencias produce una contabilidad telescópica exacta y que una condición explícita de ganancia relativa acumulada es suficiente para agotar el residuo. La condición universal de ganancia **no se deriva** de la mera cobertura de referencias ni de CR–6.

El resultado **no demuestra la hipótesis de Riemann**. Aísla una obligación cuantitativa concreta equivalente o suficiente para el cierre funcional exigido por el criterio clásico.

## 1. Contrato funcional

Sea el espacio de Hilbert real

\[
H=L^2((0,\infty),dx),\qquad
\chi(x)=\mathbf 1_{(0,1]}(x),\qquad \|\chi\|_2^2=1.
\]

Para cada entero positivo \(d\), defínase

\[
f_d(x)=\left\{\frac{1}{dx}\right\}, \qquad x>0,
\]

donde \(\{t\}=t-\lfloor t\rfloor\). Cada \(f_d\) pertenece a \(H\).

Se utiliza la cadena creciente de índices libres de cuadrados \(D_j\) ya definida por la interfaz de referencias primas de la auditoría de Pell del 20-XI-2026. Para fijar notación, allí se toma

\[
N_k+a_k\sqrt 2=(3+2\sqrt 2)^k,\qquad
\kappa_j=\operatorname{mcm}(1,\dots,j),\qquad
A_j=a_{\kappa_j},
\]

\[
S_j=\{p\text{ primo}:p\mid A_j\},\qquad
D_j=\{d:d\mid A_j,\ \mu(d)\ne0\}.
\]

La construcción previa demuestra que \(D_j\subseteq D_{j+1}\) y que cualquier entero positivo libre de cuadrados pertenece a \(D_j\) desde alguna etapa. Se definen los subespacios cerrados de dimensión finita

\[
W_j=\operatorname{span}\{f_d:d\in D_j\},
\]

y sus proyecciones ortogonales \(P_j:H\to W_j\). El residuo y su energía son

\[
r_j=\chi-P_j\chi,\qquad Q_j=\|r_j\|_2^2.
\]

**Distinción de contratos.** El resto geométrico de Pell \(N_k^{-2}\) y el error funcional \(Q_j\) son magnitudes diferentes. Ninguna identidad de este anexo los iguala.

## 2. Teorema 1 — Consulta unitaria exacta

**Enunciado.** En toda etapa \(j\), se cumple

\[
\boxed{\displaystyle Q_j=\|r_j\|_2^2=\int_0^1 r_j(x)\,dx.} \tag{1}
\]

**Demostración.** La definición de proyección ortogonal implica \(r_j\perp W_j\), mientras que \(P_j\chi\in W_j\). Por consiguiente,

\[
\begin{aligned}
\|r_j\|_2^2
&=\langle r_j,r_j\rangle\\
&=\langle r_j,\chi-P_j\chi\rangle\\
&=\langle r_j,\chi\rangle\\
&=\int_0^1 r_j(x)\,dx.
\end{aligned}
\]

La integral existe por Cauchy–Schwarz, porque \(r_j\in L^2(0,\infty)\) y el intervalo tiene medida finita. \(\square\)

**Alcance.** Aunque \(r_j\) pueda cambiar de signo, la consulta firmada sobre \((0,1]\) no pierde la magnitud del error cuadrático **cuando \(r_j\) es precisamente el residuo de la proyección ortogonal de \(\chi\)**. Esta identidad no se extiende sin más a errores de aproximantes arbitrarios.

## 3. Teorema 2 — Contabilidad exacta de herencia y recuperación

**Enunciado.** Como \(W_j\subseteq W_{j+1}\), la ganancia de proyección

\[
\Delta_j:=\|(P_{j+1}-P_j)\chi\|_2^2\ge0
\]

satisface

\[
\boxed{Q_j=Q_{j+1}+\Delta_j.} \tag{2}
\]

Para cualquier \(J>1\),

\[
\boxed{Q_1=\sum_{j=1}^{J-1}\Delta_j+Q_J.} \tag{3}
\]

**Demostración.** Al estar anidados los subespacios, \(P_{j+1}-P_j\) es la proyección ortogonal sobre \(W_{j+1}\cap W_j^\perp\). Además,

\[
r_j=r_{j+1}+(P_{j+1}-P_j)\chi,
\]

y ambos sumandos son ortogonales. Pitágoras da (2); sumando (2) de \(j=1\) a \(J-1\) se obtiene (3). \(\square\)

**Corolario.** \((Q_j)\) es decreciente, \(0\le Q_j\le1\), y por tanto \(Q_\infty:=\lim_{j\to\infty}Q_j\) existe.

## 4. Teorema 3 — Identificación del límite

Defínase el subespacio cerrado

\[
W_\infty=\overline{\bigcup_{j\ge1}W_j}^{\,H}.
\]

**Enunciado.**

\[
\boxed{Q_\infty=\operatorname{dist}(\chi,W_\infty)^2.} \tag{4}
\]

En consecuencia,

\[
\boxed{Q_\infty=0\iff\chi\in W_\infty.} \tag{5}
\]

**Demostración.** El teorema estándar de convergencia fuerte de proyecciones ortogonales sobre subespacios cerrados crecientes establece \(P_j\chi\to P_\infty\chi\) en \(H\), donde \(P_\infty\) proyecta sobre \(W_\infty\). Por continuidad de la norma, \(Q_j\to\|\chi-P_\infty\chi\|_2^2\), que es la distancia al cuadrado. La equivalencia (5) se sigue porque \(W_\infty\) es cerrado. \(\square\)

La cobertura aritmética previa identifica

\[
\bigcup_jW_j=\operatorname{span}\{f_d:\mu(d)\ne0\}.
\]

Con la versión del criterio clásico de Báez-Duarte para índices libres de cuadrados utilizada en R–03 v0.4, se tiene la **equivalencia conocida**

\[
\boxed{\mathrm{RH}\iff Q_\infty=0.} \tag{6}
\]

Esta equivalencia **no establece** por sí sola que \(Q_\infty=0\).

## 5. Teorema 4 — Condición suficiente de ganancia relativa

**Enunciado condicional.** Supóngase que existen números reales \(\eta_j\) tales que

\[
0\le\eta_j<1,\qquad
\Delta_j\ge\eta_jQ_j\quad\text{para todo }j\ge1,
\qquad\sum_{j=1}^\infty\eta_j=\infty.
\tag{7}
\]

Entonces \(Q_j\to0\); por (6), bajo el criterio funcional citado, se cumple RH.

**Demostración.** La ecuación (2) da

\[
Q_{j+1}=Q_j-\Delta_j\le(1-\eta_j)Q_j.
\]

Por inducción,

\[
Q_J\le Q_1\prod_{j=1}^{J-1}(1-\eta_j)
\le Q_1\exp\!\left(-\sum_{j=1}^{J-1}\eta_j\right).
\]

La suma divergente del exponente fuerza el límite cero. \(\square\)

**Importante.** (7) es una condición **suficiente, no un hecho demostrado de la familia aritmética**. Una condición particular considerada anteriormente, para etapas diádicas, es \(\eta_j=1/(j+2)\); los cálculos finitos favorables no garantizan su validez universal.

## 6. Matrices de Gram: expresión calculable de la consulta

Para una enumeración de \(D_j\), sean

\[
(G_j)_{de}=\langle f_d,f_e\rangle_H,
\qquad(b_j)_d=\langle\chi,f_d\rangle_H
=\frac{\log d+1-\gamma}{d}.
\]

Entonces la fórmula de proyección en subespacios de dimensión finita es

\[
\boxed{Q_j=1-b_j^{\!*}G_j^+b_j,} \tag{8}
\]

con \(G_j^+\) la pseudoinversa de Moore–Penrose. No depende de suponer que los vectores elegidos sean linealmente independientes.

La fórmula (8) es exacta; evaluaciones decimales con matrices mal condicionadas necesitan análisis de error o aritmética certificada para producir cotas rigurosas.

## 7. Relación con la suficiencia de CR–6

CR–6 demuestra que una interfaz \(Q_A(b)\) es suficiente **para una familia declarada de consultas de conteo** sobre una frontera finita: las respuestas se reconstruyen mediante \(\sum_bQ_A(b)G(b)\). También demuestra que una consulta que accede a variables internas puede exigir una interfaz más rica.

En el presente contrato, la consulta

\[
\mathcal C_{\chi}(h):=\langle h,\chi\rangle_H=\int_0^1h(x)\,dx
\]

es un funcional lineal continuo y el residuo \(r_j\) es específico de la proyección. El Teorema 1 prueba que \(\mathcal C_\chi(r_j)=Q_j\). Este hecho no equivale a extender automáticamente CR–6 de fronteras finitas al espacio \(L^2\).

La traducción matemática todavía necesaria es una ley **cuantitativa y uniforme** que vincule las operaciones aritméticas de recierre con \(\Delta_j\), de manera que se pueda verificar (7) u otro criterio suficiente de agotamiento. La mera presencia eventual de cada primo no obliga a esa ley.

### Control adversarial

En \(H_0=\ell^2(\{0,1,2,\ldots\})\), sea \(W_j^0=\operatorname{span}\{e_1,\ldots,e_j\}\) y objetivo \(\chi_0=e_0\). Aunque la unión contiene todos los generadores \(e_n\), \(n\ge1\), se tiene \(\operatorname{dist}(\chi_0,W_j^0)=1\) en cada etapa. Por tanto, **cobertura de generadores** no implica **suficiencia para un objetivo externo al cierre de su espacio generado**. El ejemplo no decide el caso particular de las funciones aritméticas.

Además, las cotas inferiores clásicas de Burnol impiden inferir, para esta cadena de Pell, una estimación general del tipo \(Q_j\le C/N_{\kappa_j}^2\) con \(C\) fijo. No debe confundirse el resto geométrico con la norma funcional.

## 8. Tabla de procedencia y estado

| Enunciado | Procedencia | Estado |
|---|---|---|
| Cadena de Pell, herencia y cobertura de primos | G–01; auditoría Pell/RH 20-XI-2026 | Demostrado previamente |
| Interfaz con índices libres de cuadrados | R–03 v0.4; auditoría Pell/RH | Correspondencia algebraica previa |
| Identidad de consulta (1) | Ortogonalidad de \(P_j\) | Demostrado en este anexo |
| Identidades de ganancias (2)–(3) | Pitágoras en espacios anidados | Demostradas en este anexo |
| Límite (4)–(5) | Convergencia de proyecciones | Teorema funcional estándar |
| Relación (6) | Criterio Nyman–Beurling/Báez-Duarte | Equivalencia clásica aplicada |
| Implicación (7) \(\Rightarrow Q_j\to0\) | Producto telescópico/exponencial | Teorema condicional demostrado |
| Validez de (7) en la cadena aritmética concreta | — | **Abierta** |
| Extensión de suficiencia CR–6 a consultas funcionales completas | — | **Abierta** |

## 9. Obligación matemática precisa

Construir, a partir de propiedades **demostradas** de los espacios aritméticos \(W_j\), una cota para \(\Delta_j\) suficientemente fuerte para implicar \(Q_j\to0\), **sin utilizar RH ni otra afirmación equivalente como premisa**. El resultado debe especificar cuantificadores, dependencia de constantes, dominio funcional y tratamiento uniforme del límite.

Este enunciado ubica la obligación lógica dentro de la formulación existente; no constituye una prueba incondicional de RH.

## Referencias documentales

- `CR6_Economia_Herencia_2026-10-16.pdf` — CR–6.1–6.5 (biblioteca de trabajo).
- `G01_Mecanismo_de_la_Gravedad_Programa_Relacional_v1.3_2026-11-01.docx` — rama Pell y recierre.
- `R_RH_01_Primos_Reflexion_y_Cierre_2026-11-01.md` — proyecciones, Gram, criterio de Báez-Duarte.
- `R03_v04_BILINGUE.docx` — interfaz libre de cuadrados y herencia espectral.
- `AUDITORIA_UNA_ESCALA_PELL_PRIMOS_RH_2026-11-20.md` — cobertura de generadores y control de tasas.
- `INTENTO_DE_PRUEBA_RESTO_RIEMANN.md` — experimento por bloques y criterio condicional.
- L. Báez-Duarte, [*A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis*](https://arxiv.org/abs/math/0202141).
- J.-F. Burnol, [*A lower bound in an approximation problem involving the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/0103058).

---

Endless Monkey Project / Relational Geometry Program
