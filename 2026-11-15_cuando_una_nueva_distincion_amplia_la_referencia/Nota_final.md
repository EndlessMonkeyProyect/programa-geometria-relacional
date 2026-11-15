---
title: "Cuándo una nueva distinción amplía la referencia"
subtitle: "Semilla, radio y normalización común: consecuencias exactas y tres laboratorios"
date: 2026-11-15
version: "1.0 — texto para examen editorial"
author: "Le Matt Ansatz Di Ego"
lang: es-CR
status: "Resultados algebraicos cerrados; aplicación global a Goldbach, Navier–Stokes y Yang–Mills abierta"
---

# Cuándo una nueva distinción amplía la referencia

**Semilla, radio y normalización común: consecuencias exactas y tres laboratorios**<br>
**15 de noviembre de 2026 · Nota para examen editorial**

**Le Matt Ansatz Di Ego**

**Endless Monkey Project**<br>
*Relational Geometry Program*

## Resumen

Una referencia conserva las relaciones que puede reconocer. Cuando una nueva operación distingue estados que esa referencia reunía, la descripción debe ampliarse para expresar la diferencia. En una grilla aritmética, el mínimo común múltiplo proporciona exactamente esa referencia conjunta: conserva la granularidad anterior y agrega clases distinguibles cuando el denominador incorporado no divide al anterior. La posibilidad nueva pertenece al espacio antes indefinido respecto de la consulta; su existencia como **solución** exige, además, cumplir una condición de compatibilidad.

Este mecanismo se formaliza mediante fibras de comparación y proyecciones ortogonales. La parte heredada y la nueva pueden separarse sin confundir su independencia representacional con perpendicularidad física. En la correlación ponderada de Goldbach, una reflexión permite una identidad y un criterio condicional exactos para certificar parejas de primos. Navier–Stokes y Yang–Mills aportan controles distintos: las fases de una tríada y el orden de los transportes muestran por qué conservar etiquetas no determina las interacciones. El radio se mantiene como alcance de distinguibilidad y el momento como relación respecto de una referencia; ninguna norma cuadrática del laboratorio sustituye esa ontología.

**Palabras clave:** normalización; mínimo común múltiplo; semilla; novedad; reflexión; correlación de Goldbach; fase; holonomía.

## 1. De la indefinición a la distinción

Una *referencia* es una regla de comparación. Una *semilla* es el conjunto de relaciones que puede transportarse y reconstruirse bajo continuaciones declaradas. Una *singularidad relacional* es un cierre que conserva su distinguibilidad como unidad. Su *radio* delimita el alcance de las comparaciones que permanecen acreditables; fuera de ese alcance quedan posibilidades que todavía no separa la referencia. La indefinición, por tanto, describe una relación no resuelta **respecto de una consulta**, no una falta de existencia.

Sea $X$ un conjunto de estados, $\Phi:X\to Y$ una firma y $d:X\to D$ una consulta nueva. La consulta introduce una distinción genuina respecto de la firma precisamente cuando

$$\exists x,y\in X:\quad \Phi(x)=\Phi(y),\qquad d(x)\ne d(y).$$

Equivalentemente, $d$ no factoriza por $\Phi$. La misma fibra de la referencia previa contiene ahora dos respuestas posibles. Una extensión $\Psi=(\Phi,d)$ conserva la información anterior y reconoce esa diferencia. Si una continuación $F:X\to X$ debe poder actualizarse sin reabrir el interior, su condición exacta es

$$\Phi(x)=\Phi(y)\ \Longrightarrow\ \Phi(Fx)=\Phi(Fy).$$

Las dos condiciones anteriores distinguen *apertura de una nueva comparación* de *cierre suficiente para continuar*. Una nueva distinción no equivale automáticamente a una solución admisible.

## 2. El nuevo denominador y la totalidad normalizada

Para $N\ge1$, considérese la grilla racional de fases

$$H_N=\left\{\frac{j}{N}\bmod1:0\le j<N\right\}\subset\mathbb R/\mathbb Z.$$

**Proposición 1 — Herencia y granularidad [EXACTA].** Si $L=\operatorname{mcm}(N,m)$, entonces

$$H_N+H_m=H_L,\qquad H_N,H_m\subseteq H_L.$$

La nueva grilla agrega posiciones si y solo si $m\nmid N$. La reducción $\pi:\mathbb Z/L\mathbb Z\to\mathbb Z/N\mathbb Z$ tiene fibras de tamaño $q=L/N$; conserva las clases anteriores y permite distinguir hasta $q$ alternativas por clase anterior.

**Demostración.** El subgrupo generado por $1/N$ y $1/m$ es el generado por $1/L$, pues $L/N$ y $L/m$ son coprimos. Como $N\mid L$, la reducción módulo $N$ está definida y cada fibra tiene $L/N$ representantes. Si $m\mid N$, entonces $L=N$; en otro caso, $L>N$. $\square$

**Ejemplo.** Los denominadores $6$ y $4$ producen $L=12$. Las posiciones $0$ y $6$ pertenecen a una misma clase módulo $6$, pero tienen restos distintos módulo $4$. La nueva comparación cabe en la grilla de $12$. Esto introduce una potencia prima mayor del factor $2$; **no requiere que aparezca un primo nuevo**.

**Proposición 2 — La diferencia como complemento [EXACTA].** En $\mathcal H_L=\ell^2(\mathbb Z/L\mathbb Z)$ defínase el levantamiento isométrico

$$(If)(z)=q^{-1/2}f(z\bmod N).$$

Sea $V_N$ el subespacio de funciones levantadas y $P$ su proyector ortogonal. Entonces

$$\mathcal H_L=V_N\oplus\ker P,$$

$Pf$ es el promedio de $f$ sobre cada fibra de $\pi$, y $(I-P)f$ es la diferencia que la grilla anterior no podía reconstruir. Para la reflexión $J_Lf(z)=f(-z)$,

$$PJ_L=J_LP.$$

Por consiguiente, para cualquier $a\in\mathcal H_L$,

$$\langle a,J_La\rangle=\langle Pa,J_LPa\rangle+\langle (I-P)a,J_L(I-P)a\rangle,$$

$$\left|\langle a,J_La\rangle-\langle Pa,J_LPa\rangle\right|\le\|(I-P)a\|^2.$$

**Demostración.** El levantamiento constante en cada fibra preserva el producto interno por el factor $q^{-1/2}$. Su proyector promedia fibras. Como $\pi(-z)=-\pi(z)$, la reflexión preserva el subespacio levantado y su complemento, por lo que conmutan. La ortogonalidad elimina términos cruzados en la identidad de correlación, y $\|J_L\|=1$ da la cota. $\square$

Estas identidades muestran cómo *puede representarse* ortogonalmente lo heredado y lo nuevo. La perpendicularidad es propia de este espacio de funciones: la coprimalidad, el radio geométrico y el momento físico son conceptos distintos. La compatibilidad con una restricción concreta sigue siendo una consulta adicional.

## 3. Qué constituye una solución nueva

Sea $A\subseteq\mathbb Z/L\mathbb Z$ el conjunto de estados admitidos por una operación. Una **posibilidad abierta** es una clase de $\pi^{-1}(r)$ que la referencia antigua aún no distinguía. Una **solución realizada** es un $z\in A$ que satisface las restricciones declaradas. Una **solución nueva relativa** exige además que la consulta que reconoce a $z$ no se recupere de la firma anterior.

Por tanto, $m\nmid N$ implica una ampliación demostrable de granularidad; **no** implica por sí solo $A\ne\varnothing$. Esa separación mantiene el significado de la incertidumbre: una región de posibilidades aún no resueltas, y no un error que deba suprimirse.

## 4. Goldbach: reflexión y certificado condicional

Fíjese un entero par $N\ge4$ y su grupo de unidades $U_N=(\mathbb Z/N\mathbb Z)^\times$. En $\mathscr H_N=\ell^2(U_N)$, la reflexión es $(J_Na)(r)=a(-r)$. Sea $\varphi\ge0$ una función simétrica respecto de $1/2$, acotada por $1$, con soporte en $[1/3,2/3]$. Defínase

$$a_N(r)=\frac{\Lambda(r)\varphi(r/N)}{\sqrt N},\quad 1\le r<N,\ r\in U_N,$$

con $\Lambda$ la función de von Mangoldt. La correlación ponderada es

$$G_N=\langle a_N,J_Na_N\rangle=\frac1N\sum_{r\in U_N}\Lambda(r)\Lambda(N-r)\varphi(r/N)^2.$$

La operación de reflexión identifica las *parejas posibles*. Los pesos $\Lambda$ registran cuáles están ocupadas por primos o sus potencias. Esta es una identidad clásica de representación, no una cota nueva sobre la distribución de primos.

Sean $E_{\mathrm{par}}=(I+J_N)/2$ y $E_{\mathrm{impar}}=(I-J_N)/2$. Se cumple exactamente

$$G_N=\|E_{\mathrm{par}}a_N\|^2-\|E_{\mathrm{impar}}a_N\|^2=2\|E_{\mathrm{par}}a_N\|^2-\|a_N\|^2.$$

**Proposición 3 — Certificado de una semilla [EXACTA, CONDICIÓN ABIERTA].** Sea $S_N$ un subespacio del sector simétrico $E_{\mathrm{par}}\mathscr H_N$ elegido por reglas independientes de conocer previamente las parejas, y $P_{S_N}$ su proyector ortogonal. Entonces

$$G_N\ge 2\|P_{S_N}a_N\|^2-\|a_N\|^2.$$

Más concretamente, para cualquier $g_N\in S_N,\ g_N\ne0$,

$$G_N\ge \frac{2|\langle a_N,g_N\rangle|^2}{\|g_N\|^2}-\|a_N\|^2.$$

**Demostración.** La descomposición ortogonal $E_{\mathrm{par}}a_N=P_{S_N}a_N+(E_{\mathrm{par}}-P_{S_N})a_N$ da la primera desigualdad. La desigualdad de Cauchy–Schwarz aplicada a $P_{S_N}a_N$ y $g_N$ da la segunda desigualdad. $\square$

Para inferir una **pareja de primos ordinarios** dentro de la ventana es preciso separar las potencias primas propias. Con $0\le\varphi\le1$, una cota elemental para sus contribuciones es

$$0\le G_N^{\mathrm{pot}}\le B_N:=\frac{2(\log N)^3}{\sqrt N\log2}.$$

Así, la condición verificable

$$\boxed{\frac{2|\langle a_N,g_N\rangle|^2}{\|g_N\|^2}-\|a_N\|^2>B_N}$$

acreditaría la existencia de al menos una pareja de primos ordinarios en la ventana. Las cotas inferiores del numerador y superiores del denominador aritmético deben obtenerse **sin conocer previamente la pareja buscada**. En particular, tomar $S_N=E_{\mathrm{par}}\mathscr H_N$ reproduce la pregunta inicial: es una identidad, no una solución.

Si se construye una regla uniforme para todos los pares suficientemente grandes y se verifica por separado el conjunto finito restante, podría obtenerse una demostración de Goldbach. **Esa regla y sus estimaciones no están demostradas en esta nota.** La construcción espectral condicional de Li–Liu utiliza hipótesis adicionales y otro espacio de operadores; no se afirma equivalencia de normas entre ambas.

## 5. Qué muestran Navier–Stokes y Yang–Mills

**Navier–Stokes: una interacción necesita fase.** En Fourier, la no linealidad involucra triples $k+l=m$ y productos $(\widehat u_k\cdot l)\widehat u_l$, seguidos de proyección solenoidal. O79 exhibe datos suaves con iguales frecuencias y módulos, pero transferencias iniciales distintas al cambiar el signo de una amplitud. La subred se hereda, mientras que la fase de la tríada puede introducir una distinción que no cabe en una firma hecha solo de etiquetas y tamaños. El mismo documento muestra que puede aparecer un modo nuevo $k-l$ sin aumentar su módulo de frecuencia. La *novedad no equivale a un radio mayor*.

**Yang–Mills: una interacción necesita orden.** En una plaqueta con transportes $SU(2)$, el producto ordenado $W_\square$ da el defecto

$$d_W(W_\square)=1-\tfrac12\operatorname{Re}\operatorname{tr}(W_\square).$$

Con transportes constantes $U,V$, el lazo es $UVU^{-1}V^{-1}$. Su defecto distingue relaciones que no conmutan. Compartir un marco o cerrar un lazo no determina por sí solo las comparaciones con todos los transportes disponibles, ni demuestra una brecha de masa. La familia de acciones discutida el 27 de octubre precisa hipótesis adicionales para recuperar el límite clásico de Yang–Mills.

**Correspondencia transversal.** En los tres casos aparecen referencias heredadas y comparaciones que pueden separar respuestas previamente reunidas. El normalizador, la proyección de Leray, la reflexión modular y la holonomía son operaciones matemáticas distintas; el vínculo entre ellas es una arquitectura de *preguntas, nuevas distinciones y condiciones de cierre*, no una identidad entre teorías.

## 6. Radio y momento: qué se conserva en el lenguaje

El punto de partida ontológico es **un momento referido a un radio relacional**, no energía como magnitud inicial. El radio establece el alcance de una diferencia acreditable. «Momento» requiere una operación y una referencia declaradas; no significa por definición un instante de reloj. En una realización espacial particular, con $\mathbf R_C=\mathbf x-\mathbf x_C$ y momento lineal $\mathbf p$, se obtiene

$$\mathbf L_C=\mathbf R_C\times\mathbf p,\qquad \frac{\|\mathbf L_C\|}{\|\mathbf R_C\|}=p_\perp\quad(\|\mathbf R_C\|>0).$$

Es una identidad mecánica bajo ese contrato. Una interpretación en términos de energía exige además unidades, dinámica y observables. Asimismo, $\|a_N\|^2$ en la sección 4 es una **norma auxiliar de un vector aritmético**, no el radio de la singularidad ni la energía ontológica. Su presencia en un certificado matemático no cambia la prioridad de la referencia, el radio y la comparación.

## 7. Resultado y obligación restante

La ampliación de una grilla reconoce nuevas diferencias exactamente cuando cambia el normalizador. El MCM transporta la herencia; la condición de no factorización identifica una novedad respecto de la firma; el complemento ortogonal permite representarla cuando existe un espacio con producto interno. La aparición de una solución añade una condición distinta: **un estado admisible debe ocupar alguna de las posibilidades abiertas**.

En Goldbach, la reflexión organiza esas posibilidades y la condición encuadrada de la sección 4 proporciona un certificado condicional exacto. Lo pendiente es construir una semilla y demostrar estimaciones uniformes independientes del conteo buscado. En Navier–Stokes falta controlar las interacciones de fase a todas las escalas pertinentes; en Yang–Mills, las relaciones gauge-invariantes y los límites espectrales requieren pruebas propias.

**Estado para revisión:** identidades de referencia, proyección y certificado **demostradas bajo sus hipótesis**; interpretación semilla–radio–momento **ontológica**; regla aritmética suficiente y consecuencias globales **abiertas**.

## Fuentes principales

1. *Momento, radio cuantificado y traducción a energía* (11-X-2026); O40 y O58 (normalización); MF–72 (incorporación de novedad).
2. [O79, *Eco de escala, relación de fase y generación de novedad en Navier–Stokes*](../2026-10-24/05_ARCHIVO/navier_stokes_O54_O92/O79_Triadas_Fases_Eco_Escalas_2026_10_22/O79_Triadas_Fases_Eco_Escalas_2026_10_22/O79_FORMALIZACION.es.md) (22-X-2026).
3. [*Más allá de Yang–Mills*](../2026-10-27_mas_alla_de_yang_mills/articulo/Mas_alla_de_Yang_Mills_2026-10-27.md) (27-X-2026).
4. *Semilla, radio y reflexión*, versión 0.3 (15-XI-2026), y antecedentes de primos y cierre.
5. Jiamin Li y Jianya Liu, [*A Conditional Proof of the Goldbach Conjecture*](https://mrc.sdu.edu.cn/info/1018/2193.htm) (13-XI-2026), como contraste de una ruta espectral condicional.
