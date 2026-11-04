---
title: "Nota de prueba de la sección 3.3"
subtitle: "El intercambio de un par y conteos binomiales relacionados · Programa de Geometría Relacional"
author: "Le Matt Ansatz Di Ego"
date: "3 de noviembre de 2026"
lang: es
---

# Nota de prueba de la sección 3.3

**El intercambio de un par y conteos binomiales relacionados**

[English](PROOF_NOTE_3_3_EN.md) · [Solicitud de revisión](SOLICITUD_REVISION.md)

Esta nota prueba las fórmulas de la sección 3.3 para todo t y Q en sus respectivos contextos: el cruce de un bit es S = I − 2P₋; en la construcción explícita de OpenAI el número de filas de medición cuenta los factores antisimétricos fuera de una ventana; y en la división de un bit los rangos de cada pieza, por filas y por columnas, son colas superiores de las mismas multiplicidades binomiales con r = 2. No prueba que esta coincidencia cumpla algún papel en las cotas de ninguno de los dos algoritmos.

## 1. Definiciones

Sea r ≥ 2 y $V=\mathbb{R}^r\otimes\mathbb{R}^r$, con base $e_a\otimes e_b$. El intercambio es $S(e_a\otimes e_b)=e_b\otimes e_a$. Como $S^2=I$ y $S$ es simétrica, $P_\pm=\tfrac12(I\pm S)$ son proyectores ortogonales con $P_++P_-=I$ y

$$S=P_+-P_-=I-2P_-.$$

El subespacio antisimétrico tiene base $e_a\otimes e_b-e_b\otimes e_a$ con $a<b$, de dimensión $a_r=r(r-1)/2$; el simétrico tiene dimensión $s_r=r(r+1)/2$.

**Cortes.** Para una función de cuatro índices F(x, y, u, v), el corte por filas es la matriz con filas (x, y) y columnas (u, v); el corte por columnas, la matriz con filas (x, u) y columnas (y, v). Los rangos son sobre ℝ. Para productos por bloques, cada corte es el producto de Kronecker de los cortes de los bloques, salvo permutación de filas y columnas.

## 2. El cruce de un bit

**Proposición 1.** En el corte por filas, [x=v][y=u] es la matriz de S y [x=u][y=v] es la identidad. Con r = 2, las entradas de 2P₋ son $[x\neq y]\,(-1)^x\,[u\neq v]\,(-1)^u$, así que S = I − 2P₋ es exactamente la identidad del Apéndice H del paper de Anthropic.

*Prueba.* La entrada (x, y), (u, v) de S es $\langle e_x\otimes e_y,\,e_v\otimes e_u\rangle$, que vale [x=v][y=u]. Con r = 2 el subespacio antisimétrico está generado por $\psi=(e_0\otimes e_1-e_1\otimes e_0)/\sqrt2$, cuyas entradas son $\psi(x,y)=[x\neq y]\,(-1)^x/\sqrt2$. Como $P_-=\psi\psi^{\mathsf T}$, la entrada de $2P_-$ es el producto indicado. ∎

## 3. La construcción de OpenAI

Sobre $V^{\otimes Q}$, sea $\Pi_s$ el intercambio que actúa en el factor s (§2.7, paso 2 del preprint). Los $\Pi_s$ conmutan, cumplen $\Pi_s^2=I$ y $\Pi_s=I-2P_-^{(s)}$.

**Proposición 2.** Sean $W_0=\tfrac12\sum_s(I-\Pi_s)=\sum_s P_-^{(s)}$ y $V_0=\prod_s\Pi_s$. En la base producto $\psi=\psi_1\otimes\cdots\otimes\psi_Q$, con cada $\psi_s$ vector propio de S, se tiene $W_0\psi=j\,\psi$ y $V_0\psi=(-1)^j\psi$, donde j es el número de factores antisimétricos. Por tanto $V_0=(-1)^{W_0}$, y el valor propio j de $W_0$ tiene multiplicidad

$$m_r(Q,j)=\binom{Q}{j}\,a_r^{\,j}\,s_r^{\,Q-j}.$$

*Prueba.* $P_-^{(s)}\psi$ vale ψ si $\psi_s$ es antisimétrico y 0 si no; $\Pi_s\psi=\pm\psi$ con el mismo criterio. La multiplicidad cuenta las maneras de elegir qué j factores son antisimétricos y un vector de cada subespacio. ∎

**Corolario 3.** Con $M_0=V_0\,f(W_0)$ y $f(j)=(-1)^j$ en la ventana I, $M_0\psi=(-1)^j f(j)\,\psi=\psi$ si j ∈ I. En la elección explícita de OpenAI, las filas de medición son los vectores de la base con j ∉ I, así que su número es

$$c=\sum_{j\notin I}m_r(Q,j)=r^{2Q}\,\Pr[W\notin I],\qquad W\sim\mathrm{Bin}\!\left(Q,\tfrac{r-1}{2r}\right),$$

que es la expresión del preprint para esa elección. Su lema enuncia una cota superior para el número de filas; esta igualdad no afirma que el conteo sea mínimo. ∎

## 4. La división de un bit

Con r = 2, sobre $V^{\otimes t}$, se desarrolla $S^{\otimes t}=\prod_s(I-2P_-^{(s)})$ según el número de factores I. La pieza $A_i$ reúne los términos con i factores I y t − i factores −2P₋, de modo que $S^{\otimes t}=\sum_i A_i$.

**Proposición 4 (filas).** $\operatorname{rank}_{\text{filas}}(A_i)=\sum_{j\ge t-i}\binom{t}{j}3^{\,t-j}$.

*Prueba.* En el corte por filas, $A_i$ es el operador mismo, y es diagonal en la base producto. Sea ψ con conjunto antisimétrico J, de tamaño j. El término con factores I en el conjunto T no se anula exactamente cuando el complemento de T está contenido en J, y entonces vale $(-2)^{t-i}\psi$. Hay $\binom{j}{t-i}$ términos así, de modo que $A_i\psi=\binom{j}{t-i}(-2)^{t-i}\psi$, distinto de cero si y solo si j ≥ t − i. El rango es el número de vectores de la base con j ≥ t − i, es decir $\sum_{j\ge t-i}m_2(t,j)$ con $m_2(t,j)=\binom{t}{j}3^{t-j}$. ∎

**Proposición 5 (columnas).** $\operatorname{rank}_{\text{columnas}}(A_i)=\sum_{j\ge i}\binom{t}{j}3^{\,t-j}$.

*Prueba.* El corte por columnas de un bloque es el reordenamiento $R(F)(x,u;\,y,v)=F(x,y,u,v)$. Con $\Phi=e_0\otimes e_0+e_1\otimes e_1$ se tiene $R(I)=\Phi\Phi^{\mathsf T}$ y $R(S)=S$, de modo que $R(-2P_-)=R(S-I)=S-\Phi\Phi^{\mathsf T}$. Como $S\Phi=\Phi$, los dos conmutan y comparten la base formada por $\phi^+=\Phi/\sqrt2$, dos vectores simétricos ortogonales a Φ y el singlete. En ella, $R(I)$ tiene valores propios (2, 0, 0, 0) y $R(-2P_-)$ tiene (−1, 1, 1, −1), ninguno nulo.

El reordenamiento es multiplicativo por bloques. Sobre un vector producto con k factores iguales a $\phi^+$ (conjunto K), el término con factores R(I) en T no se anula exactamente cuando T ⊆ K. Todos esos términos valen lo mismo, $2^i(-1)^{k-i}\prod_{s\notin K}\lambda_s$, así que la suma es $\binom{k}{i}$ veces ese valor y no se anula si y solo si k ≥ i. Como $\phi^+$ es uno de cuatro vectores por bloque, el número de vectores con k ≥ i es $\sum_{k\ge i}\binom{t}{k}3^{t-k}$. ∎

## 5. Consecuencia y límites

Con r = 2, sea $W_m\sim\mathrm{Bin}(m,1/4)$ para cada entero no negativo m. Los tres conteos usan los mismos pesos binomiales con distintos rangos de suma:

$$\operatorname{rank}_{\text{filas}}(A_i)=4^t\Pr[W_t\ge t-i],\qquad \operatorname{rank}_{\text{columnas}}(A_i)=4^t\Pr[W_t\ge i],\qquad c=4^Q\Pr[W_Q\notin I].$$

Por ejemplo, con t = 4 e i = 2, y con Q = 4 e I = {0, 1}, ambos valen $4^4\Pr[W_4\ge2]=67$. En general, el complemento de I puede reunir una cola inferior y otra superior.

**Lo que no se prueba.** Que esta coincidencia cumpla algún papel en las cotas. En el paper de Anthropic, la división de un bit está en el Apéndice H, que ninguna prueba usa; el Lema 2 usa la identidad de los ocho cuadrados. En el de OpenAI, c sí entra en el costo de las mediciones, pero no se ha mostrado que su coincidencia con los rangos de la división de un bit tenga consecuencias. El valor 67 depende de la elección de parámetros y, por sí solo, no es evidencia de un mecanismo común.

## 6. Verificación numérica

`verificar_pieza_compartida.py` comprueba numéricamente las proposiciones 1 y 2 para r = 2 a 5, el corolario 3 para (r, Q) = (2, 3), (2, 4) y (3, 3), los hechos del reordenamiento de la proposición 5, y los rangos de las proposiciones 4 y 5 para t = 3, 4 y 5 con productos de Kronecker explícitos. La salida y el entorno están en `salida_verificador_2026-11-03.txt`. Son comprobaciones numéricas, no pruebas formales.
