# Laboratorio S–RA–01 — Semilla de Möbius por octavas

**Anexo técnico | 21 de noviembre de 2026**  
**Continuidad:** RA–01 (recuperación acumulada por semillas), R3 (recierre de focos al duplicar la escala), Teorema 4 de CR–6, registro numérico del Compendio CME §6.  
**Firma pública:** Le Matt Ansatz Di Ego  
**Identificación documental:** Endless Monkey Project / Relational Geometry Program

## 1. Qué se mide

En $H=L^2((0,\infty),dx)$, con $\chi=\mathbf 1_{(0,1]}$ y $f_n(x)=\{1/(nx)\}$, cada escala diádica hereda las referencias anteriores y agrega una octava nueva:

$$
W_j=\operatorname{span}\{f_n:\ n\le2^j,\ \mu(n)\ne0\},\qquad e_j^2=\operatorname{dist}(\chi,W_j)^2 .
$$

Para cada octava se miden tres cantidades:

- **Ganancia óptima** $\Delta_j=e_j^2-e_{j+1}^2$: lo que recupera la octava con todas sus referencias nuevas.
- **Ganancia de la semilla** $d_j=|\langle r_j,g_j\rangle|^2/\|u_j\|^2$, con la capa de Möbius $g_j=\sum_{2^j<n\le2^{j+1}}\mu(n)f_n$ usada como una sola dirección (definición y cota $d_j\le\Delta_j$ en RA–01, §2).
- **Proporción** $d_j/\Delta_j\in[0,1]$: la parte de la recuperación de la octava que lleva la semilla. Es el coseno cuadrado del ángulo entre la parte nueva de la semilla y la dirección óptima de la octava.
- **Comparación:** la mejor referencia nueva tomada sola, $\max_n$ de la misma proporción para $g=f_n$ con $n$ en la octava (columna «sola»).

## 2. Método

**Fórmula analítica de producto interno.** Para $h,k$ coprimos,

$$
\langle f_h,f_k\rangle=\frac{\log2\pi-\gamma}{2}\Big(\frac1h+\frac1k\Big)+\frac{k-h}{2hk}\log\frac hk-\frac{\pi}{2hk}\big(V(h,k)+V(k,h)\big),
$$

$$
V(h,k)=\sum_{m=1}^{k-1}\Big\{\frac{mh}{k}\Big\}\cot\frac{\pi m}{k},\qquad
\langle f_{dh},f_{dk}\rangle=\frac{\langle f_h,f_k\rangle}{d}.
$$

La fórmula analítica se contrasta con la integral $\int_0^\infty\{t/h\}\{t/k\}\,t^{-2}dt$. El contraste **integra por tramos hasta un corte finito** $T$ y **aproxima la cola** mediante la media periódica dividida por $T$; no es una integración exacta de toda la semirrecta. En ocho pares desde $(1,1)$ hasta $(210,221)$, la mayor discrepancia observada es inferior a $8\cdot10^{-10}$. Esta comparación es numérica y su error no constituye una cota certificada para todas las entradas.

**Consulta.** $\langle\chi,f_n\rangle=(1-\gamma+\log n)/n$ y $\|\chi\|^2=1$.

**Álgebra.** La matriz de Gram se escala por su diagonal; su condición crece de $14$ ($N=2$) a $1{,}6\cdot10^6$ ($N=2048$), por lo que las cifras mostradas son aproximaciones numéricas reproducibles, no intervalos certificados ni una garantía uniforme de precisión. Cada ganancia óptima se calcula por el complemento de Schur (identidad (5) de RA–01) y el script comprueba que coincide con $e_j^2-e_{j+1}^2$; también comprueba $0\le d_j\le\Delta_j$ en cada octava.

## 3. Resultados

| $j$ | $N=2^j$ | dim | $e_j^2$ | $\gamma_j=\Delta_j/e_j^2$ | $d_j/\Delta_j$ | $(j+1)\,d_j/e_j^2$ | sola$/\Delta_j$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 0,85821205 | 0,66213 | 1,0000 | 0,662 | 1,0000 |
| 1 | 2 | 2 | 0,28996457 | 0,67638 | 1,0000 | 1,353 | 1,0000 |
| 2 | 4 | 3 | 0,09383723 | 0,72416 | 0,9409 | 2,044 | 0,7930 |
| 3 | 8 | 6 | 0,02588376 | 0,24919 | 0,5068 | 0,505 | 0,3527 |
| 4 | 16 | 11 | 0,01943371 | 0,21725 | 0,7337 | 0,797 | 0,3810 |
| 5 | 32 | 20 | 0,01521182 | 0,22128 | 0,9016 | 1,197 | 0,3645 |
| 6 | 64 | 39 | 0,01184578 | 0,15775 | 0,9313 | 1,028 | 0,1058 |
| 7 | 128 | 78 | 0,00997716 | 0,15152 | 0,8826 | 1,070 | 0,0571 |
| 8 | 256 | 157 | 0,00846542 | 0,10460 | 0,7577 | 0,713 | 0,0612 |
| 9 | 512 | 314 | 0,00757996 | 0,11975 | 0,8249 | 0,988 | 0,1536 |
| 10 | 1024 | 624 | 0,00667226 | 0,06642 | 0,5975 | 0,437 | 0,2020 |
| 11 | 2048 | 1245 | 0,00622907 | — | — | — | — |

En las octavas $j=0$ y $j=1$ entra una sola referencia nueva ($n=2$ y $n=3$), y la proporción vale 1 por construcción.

$e_j^2\log N$ para $N=64,\dots,2048$: $0{,}0493;\ 0{,}0484;\ 0{,}0469;\ 0{,}0473;\ 0{,}0463;\ 0{,}0475$.

## 4. Lectura

1. **Registro reproducido.** El paso 1024→2048 tiene $624+621=1245$ referencias, $e_{1024}^2=0{,}0066723$, $e_{2048}^2=0{,}0062291$ y $\gamma_{10}=6{,}64\,\%$: coincide con el registro archivado en todas las cifras reportadas.
2. **La capa de Möbius lleva la mayor parte de cada octava.** La semilla recupera entre el $51\,\%$ y el $94\,\%$ de la ganancia óptima en las octavas con varias referencias nuevas, y el $60\,\%$ en 1024→2048. En todas esas octavas supera a la mejor referencia nueva tomada sola (entre $6\,\%$ y $79\,\%$): la misma capa cuyos saltos cierra R3, sumada con sus signos, es una dirección de recuperación para la consulta $\chi$ mejor que cualquiera de sus partes.
3. **Escala relativa observada en la muestra.** $(j+1)\,d_j/e_j^2$ se sitúa aproximadamente entre $0{,}437$ y $1{,}197$ para $j=3,\dots,10$. Son datos compatibles, **solo en ese intervalo finito**, con una tasa cercana a $1/(j+1)$; no proporcionan una cota para todas las octavas, ni RA–01 exige una tasa punto a punto. La última octava medida da el valor más bajo; establecer o descartar una cota asintótica es la cuestión de investigación.
4. **Escala del error.** $e_j^2\log N$ se mantiene entre $0{,}046$ y $0{,}049$ en el rango medido, junto a la constante $2+\gamma-\log4\pi\approx0{,}0462$ de la cota inferior asintótica para la familia completa de dilataciones enteras. Se observa una proximidad numérica en el rango estudiado; no se deduce igualdad de constantes asintóticas ni convergencia del error.

## 5. Estado y siguiente medición

**Estado:** mediciones reproducibles en doble precisión, contrastadas con integración por tramos y cola aproximada, además de verificaciones internas; pendientes de certificación rigurosa de errores. La necesidad y suficiencia de la acumulación se refieren a ganancias óptimas; para esta semilla concreta RA–01 da una condición suficiente.

**Siguiente medición:** extender a $J=12,13$ y recalcular $e_j^2$, $\Delta_j$ y $d_j$ con aritmética de intervalos, para que $E_j$ y $a_j$ puedan entrar como cotas en el certificado (2) de RA–01.

## Puente con la literatura

La fórmula analítica de productos internos corresponde a Vasyunin (1995). Burnol (2002), Teorema 1.3, estudia **otra magnitud**: la distancia clásica $D(\lambda)=\operatorname{dist}(\chi,\mathcal B_\lambda)$, donde $\mathcal B_\lambda$ es el espacio generado por $x\mapsto\{\theta/x\}$, con $\lambda\le\theta\le1$. Su resultado es

$$
\liminf_{\lambda\downarrow0}D(\lambda)^2\log(1/\lambda)
\ge\sum_\rho\frac{m_\rho^2}{|\rho|^2}.
$$

La suma incorpora los ceros no triviales con el **cuadrado de sus multiplicidades**; en el caso de fallo de RH, el propio artículo observa que la cota resulta trivial porque el límite inferior es infinito. Si RH es cierta y todos los ceros son simples, la suma se reduce a $2+\gamma_E-\log(4\pi)$; en general no se afirma esa igualdad sin las hipótesis pertinentes. Como $W_j\subseteq\mathcal B_{2^{-j}}$, la distancia discreta $e_j$ es al menos $D(2^{-j})$. **La ganancia de una semilla $d_j$ es distinta de esa distancia clásica**, y la constante de Burnol no proporciona una cota inferior directa para ella. Fuente: [Burnol, Teorema 1.3](https://arxiv.org/html/math/0103058v2).

**Le Matt Ansatz Di Ego**  
Endless Monkey Project / Relational Geometry Program
