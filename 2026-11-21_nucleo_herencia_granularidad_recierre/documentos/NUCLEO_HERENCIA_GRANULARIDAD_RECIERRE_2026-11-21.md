# Núcleo persistente, herencia, granularidad y recierre

## Resultados formales y correspondencias entre escalas

**Fecha de consolidación:** 21 de noviembre de 2026  
**Versión de publicación:** 3.5  
**Destino:** incorporación aditiva al repositorio  
**Firma:** Endless Monkey Project / Relational Geometry Program

### Resumen

Un sistema relacional se desarrolla desde un núcleo persistente por ampliaciones compatibles de referencia. **Historia** identifica la procedencia y las dependencias de las distinciones; **herencia** designa la conservación operativa de las respuestas constituidas en una ampliación; **granularidad** cuantifica las distinciones accesibles bajo una referencia; **recierre** expresa la recuperación de una relación dentro de un contrato de consulta. Esta separación permite formular resultados exactos en aritmética, geometría de relaciones y espacios funcionales.

El conjunto de resultados aquí consolidado comprende el transporte exacto entre normalizadores, una ley algebraica de resto, la cancelación de saltos al duplicar cualquier escala entera, identidades de energía y de proyección, una fórmula exacta de costo periódico, una descomposición de la reconstrucción funcional en tres ventanas y una medición reproducible de la recuperación por octavas. Las conexiones se exponen mediante los objetos y operadores concretos que permiten compararlas.

## 1. Contrato fundacional

Sea una estructura de referencia en el nivel $k$, dada por $\mathcal S_k=(X_k,Q_k,\Phi_k,\mathcal A_k)$, donde $X_k$ es un conjunto de estados, $Q_k$ es la familia de preguntas, $\Phi_k$ es una representación observacional y $\mathcal A_k$ una familia de decodificadores admitidos. Una ampliación $\iota_k:\mathcal S_k\to\mathcal S_{k+1}$ **hereda** una consulta $q\in Q_k$ cuando la respuesta obtenida en la referencia nueva coincide con la respuesta previamente constituida, mediante el mapa de transporte declarado.

La historia es la estructura de procedencias $\mathcal H_k$ que permite reconstruir cómo se constituyeron las distinciones y de qué relaciones dependen. La herencia es la propiedad operativa de las ampliaciones compatibles. Una conserva **trazabilidad**; la otra conserva **capacidad de respuesta**. El núcleo no requiere desplazamiento para que la estructura incorpore nuevas distinciones: el crecimiento es una extensión de relaciones, que puede entenderse mediante la figura del tronco que crece desde una base persistente.

En ROSI, una diferencia se convierte en información operativa cuando existe una pregunta y un procedimiento que la distingue de forma recuperable. La suficiencia de una firma $\Phi$ para una consulta $q$ se expresa como

$$
q=\bar q\circ\Phi
$$

para un decodificador $\bar q$ admisible. Esta identidad, utilizada en MF-86 y CR-6, ofrece el contrato preciso para afirmar qué conserva cada interfaz.

## 2. Resultados exactos sobre escalas

### R1 — Transporte hereditario del valor racional (O40)

Para enteros $N,q\ge1$ y cualquier numerador entero $h$, el cambio de escala conserva la razón:

$$
\frac hN=\frac{qh}{qN}.
$$

El transporte de la referencia modifica la representación y conserva el valor. Las nuevas distinciones se organizan con un denominador común y se preserva la relación recuperable del nivel anterior. **Estado:** identidad algebraica exacta; formalización original: O40, 20-X-2026.

### R2 — Resto algebraico con granularidad decreciente (O58 / G-01)

Para enteros que satisfacen $a^2+b^2+1=N^2$, se tiene

$$
\frac{a^2+b^2}{N^2}+\frac1{N^2}=1.
$$

La granularidad $g_N=N^{-2}$ es positiva en cada nivel y tiende a cero en cualquier sucesión admisible con $N\to\infty$. Ejemplos exactos: $(a,b,N)=(2,2,3),(4,8,9),(12,12,17)$. **Estado:** identidad y límite algebraicos exactos. El parámetro $g_N$ pertenece al contrato de O58.

### R3 — Recierre aritmético al duplicar la escala

Sea $\mu$ la función de Möbius y

$$
J_N(n)=\sum_{\substack{d\mid n\\d\le N}}\mu(d).
$$

**Identidad.** Para todos los enteros $N\ge1$ y $N<n\le2N$,

$$
\boxed{J_N(n)=-\mu(n),\qquad J_{2N}(n)=0.}
$$

**Prueba.** Cada divisor propio $d$ de $n$ verifica $d\le n/2\le N$. La suma en $J_N(n)$ contiene todos los divisores propios. Como $n>1$, la identidad $\sum_{d\mid n}\mu(d)=0$ da $J_N(n)=-\mu(n)$. Al pasar a $2N$, se incorpora también $d=n$; la suma es entonces nula. $\square$

Es la identidad $\sum_{d\mid n}\mu(d)=0$ ($n>1$) leída entre dos escalas: en la ventana $(N,2N]$ el único divisor que falta es el propio $n$, y vale para toda escala entera $N$. La figura del avance de la pared en el laboratorio CME-002 permite visualizar la incorporación de la referencia faltante; la identidad se refiere exactamente al sistema de divisores.

**Instancia de control.** En $1024\to2048$, los $1024$ enteros nuevos se distribuyen en $621$ con $\mu(n)\ne0$ (saltos activos cancelados) y $403$ con $\mu(n)=0$ (saltos ya nulos). El recuento se verifica exactamente con `scripts/verificar_resultados.py`.

**Ejemplo.** Para $n=1030=2\cdot5\cdot103$, los siete divisores propios son $1,2,5,10,103,206,515$, cuya suma de Möbius es $+1$; al incorporar el divisor $1030$, con $\mu(1030)=-1$, el salto se anula.

## 3. Laboratorios: equivalencias operativas

**ROSI — Diferencia recuperable.** Los observables se especifican por preguntas y procedimientos; la herencia mantiene los resultados de consultas acreditadas al ampliar referencias.

**Caja de espejos / CME-002 — Reflexión y recierre.** Los experimentos de pared móvil distinguen continuidad de una relación, apertura de nuevas configuraciones y cierre bajo composición. El paralelo aritmético exacto se expresa mediante $J_N$ y la suma de Möbius. La correspondencia con la óptica se registra como analogía estructurada hasta disponer de una transformación que preserve todos los operadores.

**Esferas, tetraedro y referencias.** El agregado de una referencia amplía la colección de comparaciones. En el modelo $\mathbb F_2^4$, la firma de comparaciones por pares $\Phi(x)=(x_i\oplus x_j)_{i<j}$ satisface $\Phi(x)=\Phi(y)$ exactamente cuando $y=x$ o $y=x\oplus1111$. El modelo exhibe una equivalencia observacional exacta de dos configuraciones y permite estudiar el costo de una referencia adicional.

**Normalizadores y economía de consultas (O40, O58, MF-86, CR-6).** La granularidad especifica una resolución; la suficiencia especifica las preguntas respondibles; el costo caracteriza el procedimiento de reconstrucción. Cada resultado tiene un contrato propio, y la comparación entre contratos se efectúa por una transformación explícita de observables.

## 4. Recuperación funcional como ampliación de relaciones

Sea $H=L^2((0,\infty),dx)$, $\chi=\mathbf1_{(0,1]}$, $f_n(x)=\{1/(nx)\}$ y $W_m=\operatorname{span}\{f_n:1\le n\le m,\ \mu(n)\ne0\}$. Si $P_m$ es la proyección ortogonal sobre $W_m$ y $e_m=\|\chi-P_m\chi\|_2$, entonces para $m<n$:

$$
\boxed{e_m^2-e_n^2=\|(P_n-P_m)\chi\|_2^2.}
$$

**Prueba.** Los espacios $W_m\subseteq W_n$ son anidados. Los componentes $P_m\chi$, $(P_n-P_m)\chi$ y $\chi-P_n\chi$ son ortogonales; por Pitágoras, la diferencia de errores cuadrados coincide con la energía de la dirección recién incorporada. $\square$

Esta identidad es una **contabilidad exacta** de la recuperación por herencia en espacios de Hilbert. La reflexión $\mathscr R_{m,n}=I-2(P_n-P_m)$ ofrece una representación algebraica de la ganancia, mediante

$$
 e_m^2-e_n^2=\tfrac14\|r_m-\mathscr R_{m,n}r_m\|_2^2,\qquad r_m=(I-P_m)\chi.
$$

Con $\gamma_m=(e_m^2-e_{2m}^2)/e_m^2$ para $e_m>0$, la continuidad entre escalas tiene una forma multiplicativa exacta:

$$
\boxed{e_{2^J}^2=e_1^2\prod_{j=0}^{J-1}(1-\gamma_{2^j}).}
$$

Esta forma multiplicativa es la contabilidad sobre la que se formula RA–01 (§5).

### Medidas numéricas reproducidas

Para las referencias libres de cuadrados, el laboratorio S–RA–01 reproduce el registro de matrices de Gram: $e_{1024}^2=0{,}0066723$, $e_{2048}^2=0{,}0062291$ y una fracción recuperada de $6{,}64\,\%$. El cálculo usa una fórmula exacta para los productos internos $\langle f_n,f_m\rangle$, contrastada numéricamente con integración por tramos y cola aproximada, y doble precisión con condición $1{,}6\cdot10^6$ tras escalado diagonal. Son mediciones reproducibles; las identidades de R3 son exactas.

## 5. Granularidad y certificado de reconstrucción

Para un aproximante admisible $a(x)=\sum_{n\in I}c_nf_n(x)$, sea $B(x)=\chi(x)-a(x)$, $L=\sum|c_n|$, $C=\sum c_n/n$. Si $0<\varepsilon\le1\le R$, entonces

$$
\boxed{\|B\|_2^2\le \varepsilon(1+L)^2+\int_\varepsilon^R|B(x)|^2\,dx+\frac{|C|^2}{R}.}
$$

**Prueba.** En $(0,\varepsilon)$, cada $f_n$ está en $[0,1)$, luego $|B|\le1+L$. En $(R,\infty)$, $f_n(x)=1/(nx)$ y $\chi(x)=0$, por lo que $B(x)=-C/x$ y la última integral vale exactamente $|C|^2/R$. La franja intermedia se conserva como integral explícita. $\square$

La desigualdad es una **descomposición en tres ventanas**: cota exacta cerca de cero (granularidad $\varepsilon$ y costo $L$), integral explícita en la ventana intermedia y cola exacta ($C$). La recuperación de la consulta ocurre en la ventana intermedia. Una familia de coeficientes y ventanas para la que los tres términos tienden a cero da aproximación global en $L^2$.

### Energía periódica exacta de la ventana fina

Sea $M=\operatorname{mcm}(I)$. La energía de un período es

$$
Q_I(c)=\frac1M\int_0^M\left|1-\sum_{n\in I}c_n\{u/n\}\right|^2du.
$$

Para coeficientes reales (y por extensión con conjugados para complejos),

$$
\boxed{Q_I(c)=\left(1-\tfrac12\sum_nc_n\right)^2+\frac1{12}\sum_{n,m\in I}c_nc_m\frac{\gcd(n,m)^2}{nm}.}
$$

La fórmula da una métrica aritmética explícita para el costo de oscilación interior. El verificador incluido compara la fórmula con la integración exacta, por tramos racionales, para familias finitas de coeficientes.

### Regla de transferencia certificable

Dada una familia de normalizadores $N_k\to\infty$, se eligen aproximantes $a_k\in W_{m(k)}$, con $m(k)\to\infty$, y se documentan controles $A_k,B_k\ge0$ tales que

$$
\|\chi-a_k\|_2^2\le A_kN_k^{-2}+B_k,\qquad A_kN_k^{-2}+B_k\to0.
$$

Entonces $e_{m(k)}\to0$. Esta implicación está demostrada por la optimalidad de las proyecciones. El criterio funcional clásico de Nyman–Beurling / Báez-Duarte permite utilizar la convergencia de la familia completa de dilataciones enteras para estudiar RH. La convergencia de la familia libre de cuadrados es una condición suficiente para la familia completa. La construcción explícita y las cotas uniformes se registran como **condiciones de aplicación** del certificado.

### RA–01 — Recuperación acumulada certificable por semillas

RA–01 es el Teorema 4 de CR–6 (implicación de ganancia relativa acumulada) aplicado a la cadena diádica, con una cota por semilla explícita. Para cada escala diádica $j$, el incremento heredado es $W_{j+1}\supseteq W_j$. Con $r_j=\chi-P_j\chi$, una semilla explícita $g_j\in W_{j+1}$ y su parte nueva $u_j=(I-P_j)g_j$, se acredita la ganancia

$$
d_j=\frac{|\langle r_j,g_j\rangle|^2}{\|u_j\|^2}
\le e_j^2-e_{j+1}^2
\qquad (u_j\ne0).
$$

**Teorema RA–01 (implicación demostrada).** Si se certifican $a_j\ge0$ y $E_j>0$ tales que $d_j\ge a_j$, $e_j^2\le E_j$ y $\sum_j a_j/E_j=\infty$, entonces $e_j\to0$. La demostración aplica la proyección ortogonal y el producto de reducciones:

$$
e_J^2\le e_0^2\exp\!\left(-\sum_{j<J}\frac{a_j}{E_j}\right).
$$

**Distinción entre exactitud y suficiencia.** La suma divergente de las **ganancias óptimas relativas** $\gamma_j=(e_j^2-e_{j+1}^2)/e_j^2$ es necesaria y suficiente para el cierre cuando todos los errores son positivos (o se produce cierre exacto en un paso). Para las **ganancias de una semilla fijada**, la divergencia de $\sum a_j/E_j$ es únicamente suficiente. Una semilla puede ser ortogonal al residuo aun cuando el espacio ampliado lo aproxime completamente; el anexo incluye un contraejemplo exacto. La cota clásica $e_j^2\gtrsim1/j$ limita las sumas parciales de certificados por $\sum_{j<J}a_j/E_j\le\log J+C$, sin imponer una tasa por octava de $1/j$.

La capa aritmética propuesta como semilla es $g_j=\sum_{2^j<n\le2^{j+1}}\mu(n)f_n$. Su recierre de saltos está certificado por R3. En el laboratorio S–RA–01 esta semilla recupera entre el 51 % y el 100 % de la ganancia óptima de cada octava para $j\le10$ (60 % en 1024→2048) y en el intervalo estudiado el indicador $(j+1)d_j/e_j^2$ toma valores aproximados entre $0{,}437$ y $1{,}197$ para $j=3,\dots,10$. En las dos primeras octavas la semilla empata con la mejor referencia individual, y en las posteriores la supera. Es una pauta finita compatible con $1/(j+1)$, sin constituir una ley asintótica; la condición de aplicación del teorema requiere demostrar la divergencia de las ganancias certificadas para todas las escalas. Se adjuntan [demostración y protocolo RA–01](../anexos/RA-01_recuperacion_acumulada/documentos/PROPOSICION_RECUPERACION_ACUMULADA_2026-11-21.md), [verificador exacto de controles finitos](../scripts/verificar_ra01.py) y [laboratorio S–RA–01](../laboratorios/2026-11-21_RA01_semilla_mobius/documentos/LAB_RA01_SEMILLA_MOBIUS_2026-11-21.md).

## 6. Trazabilidad y estado verificable de los resultados

| Código | Resultado | Alcance certificado | Fuente principal |
|---|---|---|---|
| R1 | Herencia racional $h/N=qh/(qN)$ | Identidad exacta | O40; Granularidad y resto |
| R2 | Ley $1/N^2$ de O58 | Identidad y límite en sucesiones admisibles | G-01/O58; anexo técnico |
| R3 | $J_N(n)=-\mu(n)$, $J_{2N}(n)=0$ | Identidad exacta, todo $N\ge1$ y $N<n\le2N$ | Compendio CME, §4 |
| V1 | Conteo de 621 focos activos y 403 nulos | Exacto para 1024→2048 | Verificador incluido |
| R4 | Balance de proyecciones y reflexión | Identidad en Hilbert | Compendio CME, §3 |
| R5 | Descomposición en tres ventanas | Desigualdad exacta | Anexo técnico, §5 |
| R6 | Fórmula periódica de energía $Q_I(c)$ | Identidad finita | Puente de tres ventanas, §2 |
| O1 | Recuperación funcional hasta m=2048 | Reproducida, doble precisión | Compendio CME, §6; laboratorio S–RA–01 |
| T1 | Transferencia por cota uniforme | Teorema de implicación con condiciones explícitas | Anexo técnico, §5 |
| RA–01 | Recuperación certificable por semillas y suma de ganancias | Implicación suficiente por semillas; equivalencia solo para ganancias óptimas | Anexo RA–01, §2–§4; CR–6, Teorema 4 |
| S1 | Semilla de Möbius por octavas | 51–100 % de la ganancia óptima, $j\le10$; medición reproducible | Laboratorio S–RA–01 |

## 7. Integración de la versión

Este documento se incorpora como síntesis adicional, conservando íntegros los manuscritos históricos. Los laboratorios ROSI, CME-002, esferas y el normalizador O40/O58 se indexan desde sus propias rutas; los laboratorios A–G–01 (armónicos y granularidad) y S–RA–01 (semilla de Möbius) viajan en `laboratorios/` dentro de este paquete. Los anexos funcionales y aritméticos se conservan como fuentes de prueba, instancias reproducibles y trazabilidad. El `README.md` de integración contiene la inserción sugerida para el índice principal; `integracion/INSTRUCCIONES_ADMIN.md` establece la secuencia de publicación.

## 8. Procedencia y bibliografía de contraste

Anexo incorporado: `anexos/RA-01_recuperacion_acumulada/documentos/PROPOSICION_RECUPERACION_ACUMULADA_2026-11-21.md`.

Laboratorios incorporados: `laboratorios/2026-11-21_armonicos_granularidad/` y `laboratorios/2026-11-21_RA01_semilla_mobius/`.

Fuentes archivadas dentro del paquete:

- `fuentes/COMPENDIO_RIEMANN_CME_2026-11-21.md` — recierre por focos, transformadas, proyecciones, registro m=2048.
- `fuentes/COMPENDIO_RIEMANN_ECONOMIA_2026-11-21.md` — síntesis por economía de consultas.
- `fuentes/ANEXO_TECNICO_ES.md` — contratos entre escalas y descomposición en tres ventanas.
- `fuentes/PUENTE_GRANULARIDAD_TRES_VENTANAS_2026-11-21.md` — energía periódica y ventana fina.
- `fuentes/ANEXO_CR6_RH_CONSULTA_UNITARIA_Y_RESIDUO_2026-11-21.md` — consulta unitaria, balance exacto de residuo y Teorema 4 de ganancia relativa acumulada.
- `fuentes/GRANULARIDAD_RESTO_Y_CIERRE_RH.md` — leyes de granularidad y pruebas sobre cierres finitos.

Antecedentes documentales: O40 (20-X), O58 (21-X), MF-86, CR-6, CME-002, R–01/R–02, R–03 v0.4 (propuesta en PR #9), R–RH–01 (manuscrito de 1-XI; archivo cotejado en PR #9), ROSI y ROS–1 Lite. Las versiones de trabajo siguen enlazadas a sus respectivos PR y sus fechas se registran como procedencia documental.

Referencias clásicas: L. Báez-Duarte (2002), *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, https://arxiv.org/abs/math/0202141; L. Báez-Duarte, M. Balazard, B. Landreau y É. Saias (2000) y J.-F. Burnol (2002), cota inferior del error de aproximación; V. I. Vasyunin (1995), fórmula de los productos internos.

---



## Referencias vivas y procedencia de revisión

La copia `fuentes/COMPENDIO_RIEMANN_CME_2026-11-21.md` documenta un **estado anterior** al texto revisado en [PR #11 — CME–RH](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/11) (en borrador al 21-XI-2026). La edición R–03 v0.4 pertenece al [PR #9 — R–03 y Gram](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/9), también en borrador; no se presenta como texto ya fusionado en `main`. Se conservan los archivos de `fuentes/` como antecedentes íntegros; la integración debe enlazar el estado vigente de cada PR y cotejar sus cambios al fusionar.

**Le Matt Ansatz Di Ego**  
Endless Monkey Project / Relational Geometry Program
