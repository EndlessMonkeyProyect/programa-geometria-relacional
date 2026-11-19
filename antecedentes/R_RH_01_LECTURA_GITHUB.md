# R–RH–01 — Primos, reflexión y cierre: una ruta relacional hacia la hipótesis de Riemann

> **Edición de lectura para GitHub.** El [archivo fuente](R_RH_01_Primos_Reflexion_y_Cierre_2026-11-01.md) conserva sus bytes originales; aquí se adaptan la notación y la disposición de algunas fórmulas para visualización.


**Programa de Geometría Relacional · 1 de noviembre de 2026**
**Estado:** OPEN (puente matemático exacto; hipótesis de Riemann no demostrada).
**Naturaleza:** nota de investigación, distinción entre resultados clásicos, nuevas articulaciones del programa y objetivos abiertos.

## Resumen

El trabajo R–01 formaliza la incorporación de una referencia prima independiente y su normalización común; MF–69/MF–71 distinguen nuevos generadores primos de potencias heredadas y construyen comparadores de diferencias. R–RH–01 conecta esos elementos con la teoría analítica de números mediante dos modelos:

1. Un **laboratorio de desplazamientos primos** en $\ell^2(\mathbb N)$, cuyo vector de coeficientes $n^{-s}$ tiene norma finita exactamente para $\Re(s)>1/2$. Esta frontera es un hecho de sumabilidad, no una prueba sobre los ceros de la zeta.
2. Un **laboratorio de cierre funcional** en $L^2(0,\infty)$ basado en el teorema clásico de Nyman–Beurling, en la versión fortalecida de Báez-Duarte. La hipótesis de Riemann es equivalente a que una función de referencia pertenezca al cierre del espacio generado por las dilataciones aritméticas. Se obtiene un entrelazamiento exacto entre multiplicación prima y cambio de escala, y se calculan los primeros dos errores óptimos.

La conexión más útil es un **diagrama conmutativo explícito**: multiplicar la etiqueta de una referencia por un primo y luego transportarla equivale a transportar primero y dilatar después. La transformada de Mellin identifica además la imagen de cada referencia con un múltiplo explícito de la función zeta. El salto todavía abierto es demostrar que el espacio generado de este modo alcanza el objetivo en el límite infinito.

## 1. Proveniencia en el programa

| Nodo del programa | Contenido recuperado | Uso en R–RH–01 |
|---|---|---|
| R–01, 23/10/2026 | Firma módulo N, primo p que no divide a N, normalizador Np, compatibilidad operativa | Distinguir incorporación prima y permanencia de referencias anteriores |
| MF–69 / MF–71 | Valuaciones primas y operadores de comparación | Generadores independientes y modelo espectral |
| O40 / O58 | Conservación de relaciones bajo múltiplos comunes; distinta normalización de resto unitario | Evitar confundir cambio de referencia con una nueva ley dinámica |
| CME–002 | Plegado y pared móvil: una firma anterior puede ser insuficiente | Interpretación operativa de un cambio de escala |
| MF–43 / O45 | Fases, ritmos y recurrencias relativos a una referencia | Fases $e^{-it\log p}$, sin identificar ritmos discretos con períodos enteros |
| R–04 | Distinción entre control local e incompatibilidad global | Control adversarial: cierres de ventanas finitas no prueban un límite global |

Fuentes internas principales: `R01_PUENTE_NORMALIZACION_AUTORREFERENCIA_YM.es.md`, `MF71_K_incorporacion_novedad_REPO_READY.md`, `O58_FORMALIZACION.es.md`, `El_cubo_de_espejos.pdf`, `Programa_Geometria_Relacional_Manuscrito_Publico_2026-10-24.pdf`.

## 2. Contrato de la hipótesis de Riemann

Para $\Re(s)>1$,

$$
\zeta(s)=\sum_{n=1}^\infty n^{-s}=\prod_{p\ \mathrm{primo}}(1-p^{-s})^{-1}.
$$

Su continuación meromorfa y su ecuación funcional conducen a la función entera

$$
\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad \xi(1-s)=\xi(s).
$$

**RH:** todo cero de $\xi$ tiene parte real $1/2$. La ecuación funcional establece la simetría, pero no establece por sí sola la localización.

## 3. Resultado A — laboratorio de desplazamientos primos

Sea $\mathcal H=\ell^2(\mathbb N)$ con base ortonormal $e_n$. Para cada primo $p$ definimos

$$
S_p e_n=e_{pn}.
$$

Cada $S_p$ es una isometría y los operadores conmutan: $S_pS_q=S_qS_p$. Los generadores primos alcanzan todas las etiquetas de la base desde $e_1$, por la factorización única.

**Lema A1 (frontera de normalización).** El vector formal

$$
\Psi_s=\sum_{n\ge1} n^{-s}e_n
$$

pertenece a $\mathcal H$ si y solo si $\Re(s)>1/2$. En ese dominio

$$
\|\Psi_s\|^2=\sum_{n\ge1} n^{-2\Re(s)}=\zeta(2\Re(s)).
$$

**Demostración.** Los $e_n$ son ortonormales; la suma de cuadrados coincide con una p-serie de exponente $2\Re(s)$, que converge precisamente cuando el exponente es mayor que uno. QED.

**Lema A2 (reconocimiento por cada primo).** Para $\Re(s)>1/2$:

$$
S_p^{\ast}\Psi_s=p^{-s}\Psi_s.
$$

**Demostración.** $S_p^{\ast}e_m=e_{m/p}$ si $p\mid m$, y es cero en otro caso. El coeficiente de $e_n$ en $S_p^{\ast}\Psi_s$ es $(pn)^{-s}=p^{-s}n^{-s}$. QED.

**Lema A3 (producto de factores como estado).** Si $\Re(s)>1/2$, el límite de los vectores con factores primos acotados existe en $\ell^2$ y

$$
\Psi_s=\lim_{P\to\infty}\left(\prod_{p\le P}(I-p^{-s}S_p)^{-1}\right)e_1,
$$

con convergencia en norma. Para $\Re(s)>0$, cada producto **finito** está definido y

$$
\|\Psi_{s,P}\|^2=\prod_{p\le P}(1-p^{-2\Re(s)})^{-1}.
$$

**Alcance.** La frontera $1/2$ es real y exacta, pero mide pertenencia de un vector a un espacio de Hilbert; no da la posición de los ceros de $\xi$. En particular, la expresión $\zeta(2\sigma)$ se identifica con esa norma únicamente para $\sigma>1/2$. No se debe sustituir la serie divergente por el valor de la continuación analítica y llamarlo una norma.

## 4. Resultado B — criterio clásico de cierre funcional

Escribamos $\{t\}=t-\lfloor t\rfloor$, sea

$$
\chi(x)=\mathbf 1_{(0,1]}(x),\qquad
f_k(x)=\left\{\frac1{kx}\right\},\quad k\ge1.
$$

Estas funciones pertenecen a $L^2((0,\infty),dx)$. Sea

$$
\mathcal V_m=\operatorname{span}\{f_1,\dots,f_m\},\quad
d_m=\inf_{v\in\mathcal V_m}\|\chi-v\|_{L^2}.
$$

**Teorema clásico (Nyman–Beurling, versión de Báez-Duarte):**

$$
\boxed{\mathrm{RH}\iff\chi\in\overline{\operatorname{span}\{f_k:k\in\mathbb N\}}^{L^2}
\iff \lim_{m\to\infty}d_m=0.}
$$

No es un teorema nuevo del programa; es el criterio previo que aporta un objetivo preciso de cierre.

### 4.1. Entrelazamiento exacto entre referencia prima y dilatación

Definamos $T$ en sucesiones de soporte finito por $T e_n=f_n$, y sobre funciones por $D_p h(x)=h(px)$. Entonces, para todo $n$,

$$
T S_p e_n =T e_{pn}=f_{pn}=D_p f_n=D_p T e_n,
$$

es decir:

$$
\boxed{T S_p=D_p T\quad\text{en el dominio de soporte finito}.}
$$

Aquí el transporte es **algebraicamente exacto**. No se ha probado que $T$ se extienda a un operador acotado entre los espacios de Hilbert completos.

Para normalizar las normas, sea $g_n=\sqrt n\,f_n$ y $U_p h(x)=\sqrt p\,h(px)$. Entonces

$$
\|U_ph\|_2=\|h\|_2,\qquad U_pg_n=g_{pn},
$$

por lo que $T'e_n=g_n$ satisface $T'S_p=U_pT'$ sobre sucesiones de soporte finito. Los $U_p$ son operadores unitarios sobre $L^2(0,\infty)$; los $S_p$ son isometrías no sobreyectivas en $\ell^2(\mathbb N)$. Las $g_n$ tienen la misma norma, pero **no son ortogonales**. Igualdad de normas individuales no significa que $T'$ sea isométrico.

La equivalencia con RH puede escribirse como:

$$
\boxed{\mathrm{RH}\iff \chi\in\overline{\operatorname{span}\{U_n g_1:n\ge1\}}^{L^2}.}
$$

Es un problema de pertenencia a un subespacio cíclico generado mediante dilataciones por enteros, todos ellos productos de primos.

### 4.2. Gram y comparador

Para cada $m$, sea $T_m:\mathbb C^m\to L^2$ el operador $T_m c=\sum_{k=1}^m c_k f_k$. Defina

$$
G_m=T_m^*T_m,\quad (G_m)_{jk}=\langle f_j,f_k\rangle,\quad b_k=\langle\chi,f_k\rangle.
$$

El problema de mejor cierre es:

$$
d_m^2=1-b_m^*G_m^+b_m,
$$

con $G_m^+$ la pseudoinversa Moore–Penrose (si $G_m$ es invertible, es su inversa). Como $\mathcal V_m\subseteq\mathcal V_{m+1}$,

$$
0\le d_{m+1}\le d_m\le1.
$$

La positividad de $G_m=T_m^*T_m$ es **automática para cada m** y no demuestra RH. Lo que falta es $d_m\to0$.

### 4.3. La transformada de Mellin y la aparición exacta de zeta

Para $0<\Re(s)<1$, la identidad clásica de Mellin–parte fraccionaria es

$$
\boxed{\mathcal M f_1(s)=\int_0^\infty \left\{\frac1x\right\}x^{s-1}\,dx=-\frac{\zeta(s)}s.}
$$

Como $f_n(x)=f_1(nx)$, el cambio de escala produce

$$
\boxed{\mathcal M f_n(s)=-\frac{\zeta(s)}{s n^s},\quad 0<\Re(s)<1.}
$$

Por otra parte, $\mathcal M\chi(s)=1/s$. Escribiendo $A_m(s)=\sum_{k=1}^m a_k k^{-s}$ y $a_k=-c_k$, la transformada del residuo es

$$
\mathcal M\left\lbrack\chi-\sum_{k=1}^m c_kf_k\right\rbrack(s)
=\frac{1-\zeta(s)A_m(s)}s.
$$

La isometría de Mellin–Plancherel sobre $L^2((0,\infty),dx)$ identifica la norma de cierre con

$$
\boxed{d_m^2=\inf_{A_m}\frac1{2\pi}\int_{-\infty}^{\infty}
\frac{\big|1-\zeta(\tfrac12+it)A_m(\tfrac12+it)\big|^2}{\tfrac14+t^2}\,dt.}
$$

Se obtiene una cadena exacta y conmutativa:

$$
\text{multiplicación prima}\ \xrightarrow{T}\ \text{dilatación}
\ \xrightarrow{\mathcal M}\ \text{multiplicación por }p^{-s}
\ \xrightarrow{\mathrm{evaluación}}\ \text{forma con }\zeta(s).
$$

**Sentido de la frontera:** la recta $\Re(s)=1/2$ es la línea de Plancherel en esta realización de $L^2(dx)$; la localización de todos los ceros no se deduce de ese hecho. La equivalencia $d_m\to0\iff\mathrm{RH}$ continúa siendo el criterio profundo.

**Antecedentes directos:** Balazard–Saias, *The Nyman–Beurling equivalent form for the Riemann hypothesis* (1998/2000); y las exposiciones modernas del criterio de Báez-Duarte.

### 4.4. Barrera cuantitativa conocida

El descenso de $d_m$ no puede suponerse rápido. Resultados de Báez-Duarte, Balazard, Landreau y Saias, mejorados por Burnol, proporcionan cotas inferiores de orden $1/\log m$ para $d_m^2$ en sentido asintótico, con constantes expresadas mediante ceros de zeta en la línea crítica. Esta literatura constituye un control contra la extrapolación engañosa desde $m=1,2$. La tarea abierta de RH requiere cotas superiores que realmente impliquen $d_m\to0$, no solo la existencia de esos límites inferiores.

## 5. Resultados exactos m=1 y m=2

Sea $\gamma$ la constante de Euler–Mascheroni y $A=\log(2\pi)-\gamma$.

**Lema B1.** Para $k\ge1$:

$$
\boxed{\langle\chi,f_k\rangle=\frac{\log k+1-\gamma}{k},\quad
\|f_k\|_2^2=\frac{A}{k}.}
$$

**Prueba (esquema).** Con $t=1/(kx)$, la integral de $\chi f_k$ es
$k^{-1}\int_{1/k}^\infty\{t\}t^{-2}dt$. Su primer tramo es $\log k$, y la parte de $1$ a infinito es $1-\gamma$, al sumar sobre intervalos $[n,n+1)$. La relación $f_k(x)=f_1(kx)$ da $\|f_k\|^2=k^{-1}\|f_1\|^2$. Para $f_1$, la suma de integrales sobre intervalos y la fórmula de Stirling producen $\|f_1\|^2=\log(2\pi)-\gamma$. QED.

**Lema B2.** Se verifica exactamente

$$
\boxed{\langle f_1,f_2\rangle=\frac A2+\frac{\log\pi-\gamma}{4}.}
$$

**Prueba (esquema).** En la variable $t=1/x$:
$\{t/2\}=\tfrac12\{t\}+\tfrac12(\lfloor t\rfloor\bmod2)$. Así la correlación es $A/2$ más la mitad de la suma de integrales de $\{t\}/t^2$ sobre los intervalos $[2j+1,2j+2)$. Esas integrales suman $(\log\pi-\gamma)/2$ por el producto de Wallis y el límite de los números armónicos. QED.

Por tanto,

$$
G_2=\begin{pmatrix}A&B\\B&A/2\end{pmatrix},\qquad
b_2=\binom{1-\gamma}{(\log2+1-\gamma)/2},\quad B=A/2+(\log\pi-\gamma)/4.
$$

La proyección ortogonal da:

$$
d_1^2=1-\frac{(1-\gamma)^2}{A},\qquad
d_2^2=1-b_2^\top G_2^{-1}b_2.
$$

**Cálculos reproducibles:**

| Cantidad | Valor |
|---|---:|
| $G_{11}$ | 1.260661401508 |
| $G_{12}$ | 0.772209255991 |
| $G_{22}$ | 0.630330700754 |
| $d_1$ | 0.926397350706 |
| $d_2$ | 0.538483587254 |

Esta reducción es estricta; ninguna cantidad finita de distancias demuestra la condición global $d_m\to0$.

## 6. Tercera relación: la ventana móvil de Weil

El criterio de positividad de Weil, en su contrato de funciones de prueba adecuado, es equivalente a RH. Si una función de prueba está soportada en $[e^{-a},e^a]$, su convolución multiplicativa con la función invertida queda soportada en $[e^{-2a},e^{2a}]$. Por la fórmula explícita, los términos aritméticos de esa forma incluyen potencias primas $p^j$ que alcanzan el soporte, es decir, $\log(p^j)\le2a$. Al aumentar la ventana aparecen términos adicionales.

Esta es una versión **matemática y ya conocida** de una ventana que incorpora distinciones al ampliar su escala. Se diferencia de CME–002 porque la ventana es de funciones de prueba y la forma de Weil incluye contribuciones arquimedianas, polos y términos de borde que no pueden omitirse. Su positividad para todas las ventanas y todas las funciones admisibles es el paso profundo.

## 7. Controles adversariales

1. **Simetría no es localización.** La función entera $F(s)=((s-1/4)^2+9)((s-3/4)^2+9)$ satisface $F(1-s)=F(s)$ y tiene ceros con partes reales $1/4$ y $3/4$. La reflexión sola no obliga a los ceros a estar en el eje.
2. **Positividad de Gram no es RH.** Toda matriz $G_m=T_m^*T_m$ es positiva semidefinida; lo difícil es el límite $d_m\to0$.
3. **Producto de Euler finito no detecta ceros críticos.** $\prod_{p\le P}(1-p^{-s})^{-1}$ no se anula para $\Re(s)>0$ y no proporciona la continuación analítica relevante para RH.
4. **El umbral $1/2$ de la norma no es una afirmación sobre los ceros.** Es el límite de convergencia cuadrática del vector $\Psi_s$.
5. **Las aproximaciones finitas pueden ocultar el comportamiento del límite.** La positividad, la compatibilidad y el descenso inicial de errores no constituyen una cota uniforme.

## 8. Programa experimental mínimo

**Control I (resuelto):** verificar la firma CRT del puente R–01 para $N=6,p=5$. Exactamente 30 clases nuevas y cinco refinamientos por clase antigua.

**Control II (resuelto):** calcular $\|\Psi_{s,P}\|^2$ con primos hasta $P=10,100,1000,10000$. Se observa crecimiento en $\sigma\le1/2$ y aproximación a un valor finito para $\sigma>1/2$, de acuerdo con el teorema de convergencia.

**Control III (resuelto):** reconstruir $d_1,d_2$ con expresiones exactas, sin extrapolaciones.

**Control IV (resuelto):** exhibir $F(s)$ simétrica con ceros fuera del eje.

**Control V (pendiente):** construir cotas certificadas para las matrices Gram $G_m$, al menos para $m=3,\ldots,20$, evitando cuadraturas sin control de los saltos de la parte fraccionaria. Registrar límites inferior y superior verificables para $d_m$.

**Control VI (abierto):** identificar alguna estructura relacional que **imponga una cota global nueva** sobre $d_m$, o una forma de positividad de Weil, sin introducir como supuesto lo equivalente a RH.

## 9. Dictamen ROSI

- **RESOLVED:** multiplicación prima; entrelazamiento $T S_p=D_p T$ sobre soporte finito; umbral de $\ell^2$; cálculos $m=1,2$; control simétrico adversarial.
- **OPEN:** demostrar $d_m\to0$, establecer la positividad de Weil para todas las funciones admisibles, o construir un operador autoadjunto con correspondencia espectral completa con los ceros.
- **FALSO / DESCARTADO:** inferir RH de simetría, de una norma positiva arbitraria, de descenso observado en una ventana finita o de coincidencia del número $1/2$ en dos modelos diferentes.
- **Hipótesis fértil de trabajo:** buscar una propiedad adicional, verificable y no circular, que vincule la conservación de referencias bajo dilataciones primas con la completitud del subespacio cíclico que aproxima $\chi$.

**Pregunta central R–RH–01:** ¿qué condición estructural, expresada en el lenguaje de referencias, transporte y cierre, puede garantizar que la distancia $d_m$ tienda a cero para la familia aritmética de Báez-Duarte?

## 10. Bibliografía externa contrastada

- NIST Digital Library of Mathematical Functions, sección 27.4 (producto de Euler): https://dlmf.nist.gov/27.4
- NIST DLMF, sección 25.4 (ecuación funcional): https://dlmf.nist.gov/25.4
- L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann Hypothesis* (2002): https://arxiv.org/abs/math/0202141
- J. C. Lagarias, *The Riemann Hypothesis: Arithmetic and Geometry*: https://dept.math.lsa.umich.edu/~lagarias/doc/mt-holyoke-rev.pdf
- J. Arias de Reyna, *La hipótesis de Riemann y la Física*, Instituto de Matemáticas, Universidad de Sevilla (2022): https://institucional.us.es/blogimus/2022/11/la-hipotesis-de-riemann-y-la-fisica/
- E. Bombieri y J. C. Lagarias, *Li’s criterion for the Riemann hypothesis*, discusión de la positividad de Weil: https://websites.umich.edu/~lagarias/doc/bombieri.pdf
- M. Balazard y É. Saias, *The Nyman-Beurling equivalent form for the Riemann hypothesis* (1998): https://www.esi.ac.at/preprints/esi623.pdf
- J.-F. Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta function* (2002): https://arxiv.org/abs/math/0103058

## 11. Reproducción

Ejecutar:

```bash
python3 R_RH_01_verificador.py
```

El código utiliza la biblioteca estándar y verifica las identidades y controles numéricos declarados. **La ejecución de pruebas no demuestra la hipótesis de Riemann.**
