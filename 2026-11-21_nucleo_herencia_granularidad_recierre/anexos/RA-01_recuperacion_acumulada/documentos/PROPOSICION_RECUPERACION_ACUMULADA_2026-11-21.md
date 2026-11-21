# Proposición RA–01 · Certificado de recuperación acumulada por herencia y referencias nuevas

**Fecha:** 21 de noviembre de 2026  
**Ámbito:** ROSI · O40/O58 · R–03 · R–RH–01 · CR–6 · laboratorio armónico MF–69 · focos de Möbius · recuperación funcional · laboratorio S–RA–01.  
**Tipo:** proposición matemática demostrada bajo un certificado cuantitativo explícito; programa de verificación aritmética.

## 1. Contrato funcional

En el espacio de Hilbert real $H=L^2((0,\infty),dx)$, se fijan

$$
\chi(x)=\mathbf 1_{(0,1]}(x), \qquad f_n(x)=\left\{\frac{1}{nx}\right\},
$$

$$
W_j=\operatorname{span}\{f_n:n\le 2^j,\ \mu(n)\ne0\},\quad
P_j=P_{W_j},\quad r_j=\chi-P_j\chi,\quad e_j^2=\|r_j\|_2^2.
$$

La ampliación $W_j\subseteq W_{j+1}$ formaliza la herencia. La normalización armónica y la granularidad permiten formular consultas sobre escalas; el error funcional se mide en la norma indicada.

## 2. Proposición de recuperación por semillas (RA–01)

La implicación de suma divergente es el Teorema 4 de CR–6 (`fuentes/ANEXO_CR6_RH_CONSULTA_UNITARIA_Y_RESIDUO_2026-11-21.md`, §5), demostrado allí para una cadena anidada de referencias. RA–01 la aplica a la cadena diádica y le agrega la cota por semilla (1): la ganancia de cada octava se acredita con una función explícita de la octava nueva.

Para cada $j$ con $e_j>0$, elíjase una **semilla explícita** $g_j\in W_{j+1}$, y defínase su parte novedosa

$$
u_j=(I-P_j)g_j.
$$

Si $u_j\ne0$, defínase

$$
d_j=\frac{|\langle r_j,g_j\rangle|^2}{\|u_j\|_2^2};
$$

y si $u_j=0$, tómese $d_j=0$.

**Identidad y cota demostradas** (para cada escala):

$$
0\le d_j\le e_j^2-e_{j+1}^2,
\qquad
 e_{j+1}^2\le e_j^2-d_j.
\tag{1}
$$

**Certificado suficiente.** Supóngase que para cada $j$ se obtienen, a partir de cálculos aritméticos finitos y estimaciones demostradas independientemente de RH, números $E_j>0$, $a_j\ge0$ tales que

$$
e_j^2\le E_j,\qquad d_j\ge a_j,
\qquad\sum_{j=0}^\infty\frac{a_j}{E_j}=\infty.
\tag{2}
$$

Entonces

$$
\boxed{\lim_{j\to\infty}e_j=0.}
\tag{3}
$$

En particular, al tratarse de una familia de funciones contenida en el sistema de índices enteros del criterio clásico de Báez-Duarte, (3) implica la **hipótesis de Riemann**. La recíproca para la familia restringida a índices libres de cuadrados no se presupone.

### Demostración

Sea $U_j=W_{j+1}\cap W_j^\perp$. Por ortogonalidad, $P_{j+1}-P_j$ es la proyección sobre $U_j$, mientras $u_j\in U_j$. La proyección del resto $r_j$ sobre la recta $\mathbb Ru_j$ tiene norma cuadrática $d_j$. Por tanto,

$$
e_j^2-e_{j+1}^2=\|(P_{j+1}-P_j)r_j\|_2^2\ge d_j.
$$

Si $e_j>0$, de (2) y (1) resulta

$$
e_{j+1}^2\le e_j^2\left(1-\frac{a_j}{E_j}\right),
\qquad 0\le\frac{a_j}{E_j}\le1.
$$

Iterando y usando $1-t\le e^{-t}$,

$$
0\le e_J^2\le e_0^2\exp\left(-\sum_{j=0}^{J-1}\frac{a_j}{E_j}\right)\longrightarrow0.
$$

Si algún $e_j=0$, el cierre ya se obtuvo y persiste por anidación. $\square$

### Tamaño y alcance del certificado

**Criterio exacto para las ganancias óptimas.** Escribiendo

$$
\Delta_j=e_j^2-e_{j+1}^2,\qquad
\gamma_j=\frac{\Delta_j}{e_j^2}
\quad(e_j>0),
$$

si todos los errores son positivos, la identidad telescópica da

$$
\frac{e_J^2}{e_0^2}=\prod_{j<J}(1-\gamma_j),
\qquad e_J\to0\ \Longleftrightarrow\ \sum_{j\ge0}\gamma_j=\infty.
$$

Si en alguna escala el error es exactamente cero, el cierre ya se obtiene en ese paso y persiste por anidación. Estas son condiciones **necesarias y suficientes para las ganancias óptimas exactas**.

**Criterio certificado por semillas.** Para una selección fijada de semillas $g_j$, (2) es una **condición suficiente**, no necesaria: puede ocurrir $e_j\to0$ mientras $d_j=0$ para todas esas semillas. Incluso cuando $d_j>0$, la semilla puede recuperar solo una parte de la ganancia óptima. Por tanto, la equivalencia anterior no se atribuye a la capa de Möbius ni a un certificado arbitrario.

**Control exacto de la distinción.** En $H=\ell^2(\mathbb N)$, con base ortonormal $(v_k)$, tómense

$$
\chi=\sum_{k=0}^{\infty}2^{-(k+1)}v_{2k+1},\qquad
W_j=\operatorname{span}\{v_1,\ldots,v_{2j}\},\qquad
 g_j=v_{2j+2}.
$$

Entonces $g_j\in W_{j+1}\cap W_j^\perp$, $g_j\ne0$, pero $\langle r_j,g_j\rangle=0$, así que $d_j=0$. No obstante,

$$
e_j^2=\frac{4^{-j}}{3}\longrightarrow0,\qquad
\Delta_j=4^{-(j+1)}>0.
$$

La familia heredada cierra globalmente y la semilla elegida no detecta sus mejoras. El verificador RA–01 añade un control racional de este contraejemplo.

Para cualquier certificado, mientras todos los errores sean positivos,

$$
\frac{a_j}{E_j}\le\gamma_j,
\qquad
\sum_{j<J}\frac{a_j}{E_j}\le\sum_{j<J}\gamma_j\le\log\frac{e_0^2}{e_J^2}.
$$

La cota inferior de aproximación de Burnol para $D(\lambda)=\operatorname{dist}(\chi,\mathcal B_\lambda)$, con $\mathcal B_\lambda=\operatorname{span}\{x\mapsto\{\theta/x\}:\lambda\le\theta\le1\}$, da $D(2^{-j})^2\ge c/\log(2^j)$ para $j$ suficientemente grande, con alguna constante $c>0$. Puesto que $W_j\subseteq\mathcal B_{2^{-j}}$, también $e_j^2\ge c/\log(2^j)$ (bajo RH, la constante explícita del teorema depende de la suma de $m_\rho^2/|\rho|^2$; si RH falla, el límite inferior de Burnol es infinito). Esta desigualdad concierne la **distancia clásica y el error óptimo**, no la ganancia por semilla $d_j$, y implica $\sum_{j<J}a_j/E_j\le\log J+C$ para alguna constante $C$. Esta es una **restricción sobre el crecimiento acumulado** del certificado, no una exigencia de cotas punto a punto de orden $1/j$. Son posibles distribuciones intermitentes de ganancias cuya suma diverja.

## 3. Semilla aritmética concreta y lectura del laboratorio

Una primera selección completamente explícita es la **capa nueva de Möbius**:

$$
g_j(x)=\sum_{2^j<n\le2^{j+1}}\mu(n)f_n(x).
\tag{4}
$$

Esta suma solo incorpora índices libres de cuadrados y pertenece a $W_{j+1}$. La identidad universal de focos

$$
J_{2^j}(n)=-\mu(n),\qquad J_{2^{j+1}}(n)=0
\quad (2^j<n\le2^{j+1})
$$

documenta el efecto exacto de esa capa sobre los saltos aritméticos. La cantidad $d_j$ de (1) mide **cuánto de esa incorporación llega efectivamente a la consulta funcional $\chi$**.

**Medición (laboratorio S–RA–01).** Para $j=0,\dots,10$ la semilla (4) recupera entre el $51\,\%$ y el $100\,\%$ de la ganancia óptima de la octava ($60\,\%$ en 1024→2048). En las octavas $j=0,1$ la semilla iguala a la mejor referencia nueva tomada sola; en las octavas $j=2,\dots,10$ la supera. Para $j=3,\dots,10$, el indicador $(j+1)d_j/e_j^2$ toma valores observados entre aproximadamente $0{,}437$ y $1{,}197$, compatibles solamente en esa muestra con un orden $1/(j+1)$, **sin establecer una cota asintótica**. Ver `laboratorios/2026-11-21_RA01_semilla_mobius/`.

La indistinguibilidad armónica bajo una consulta de granularidad define un cierre *observacional*. RA–01 proporciona el contrato complementario para medir recuperación *en norma*: la granularidad dirige la búsqueda de semillas; las correlaciones con $r_j$ certifican la ganancia real.

## 4. Forma matriz de Gram: cálculo finito

Sean $A_j$ los índices heredados y $B_j$ los nuevos. Para los bloques de la matriz $G_{nm}=\langle f_n,f_m\rangle$ y $b_n=\langle\chi,f_n\rangle$, si $G_{AA}$ y el complemento de Schur son invertibles,

$$
S_j=G_{BB}-G_{BA}G_{AA}^{-1}G_{AB},\quad
h_j=b_B-G_{BA}G_{AA}^{-1}b_A,
$$

$$
\boxed{e_j^2-e_{j+1}^2=h_j^{\!T}S_j^{-1}h_j.}
\tag{5}
$$

Esta identidad permite contrastar la semilla (4) con la recuperación óptima. Para bloques singulares se trabaja directamente con las proyecciones ortogonales (o con la pseudoinversa, justificando compatibilidad de rangos).

Un límite superior $E_j$ puede obtenerse de cualquier combinación explícita $a_j^*\in W_j$ mediante $E_j=\|\chi-a_j^*\|_2^2$; un límite inferior certificado $a_j\le d_j$ puede provenir de cotas de productos internos y normas del bloque. Ambos se deben estimar sin usar como hipótesis el cierre que se intenta deducir.

## 5. Protocolo de examen

1. Construir la capa (4) y los bloques de Gram en cada octava; conservar identidades de focos exactas.
2. Obtener intervalos rigurosos para $e_j^2$, $d_j$, $E_j$ y $a_j$; usar los ensayos numéricos como orientación, no como cota universal.
3. Investigar una estimación aritmética verificable que haga divergir $\sum a_j/E_j$. Se admiten recuperaciones variables, intermitentes o agrupadas en bloques: no se impone una cota uniforme por octava.
4. Si la semilla (4) resulta débil, explorar semillas explícitas alternativas en el mismo subespacio nuevo y verificar la desigualdad (1).
5. Documentar cada desigualdad con rango de índices, constantes, prueba y estado de verificación.

**Estado al 21 de noviembre de 2026:** las identidades (1), (5) y la implicación (2) ⇒ (3) están demostradas; el puente de Möbius para los focos es exacto. El certificado aritmético (2) para todas las escalas queda formulado como objetivo verificable. El laboratorio S–RA–01 reproduce el registro $1024\to2048$ ($e^2_{1024}=0{,}0066723$, $e^2_{2048}=0{,}0062291$, recuperación $6{,}64\,\%$) y mide la semilla (4) en doble precisión; para usar esos valores como cotas $E_j,a_j$ se requiere aritmética de intervalos.

## 6. Procedencia documental

- `fuentes/ANEXO_CR6_RH_CONSULTA_UNITARIA_Y_RESIDUO_2026-11-21.md`: Teorema 4, implicación de ganancia relativa acumulada.
- `fuentes/COMPENDIO_RIEMANN_CME_2026-11-21.md`: apartados 3–6, recuperación, focos y control por tres ventanas.
- `fuentes/COMPENDIO_RIEMANN_ECONOMIA_2026-11-21.md`: contraste de cotas por octavas y condición de cierre.
- `fuentes/ANEXO_TECNICO_ES.md`, §5, y `fuentes/PUENTE_GRANULARIDAD_TRES_VENTANAS_2026-11-21.md`: contrato de tres ventanas.
- `laboratorios/2026-11-21_armonicos_granularidad/documentos/LAB_ARMONICOS_GRANULARIDAD_Y_RECIERRE_2026-11-21.md`: indistinguibilidad por consultas de celda.
- `laboratorios/2026-11-21_RA01_semilla_mobius/`: medición de la semilla (4) y reproducción del registro 1024→2048.
- Báez-Duarte (2002), criterio clásico sobre el cierre por dilataciones de índices enteros; Báez-Duarte, Balazard, Landreau y Saias (2000) y Burnol (2002), Teorema 1.3, distancia clásica $D(\lambda)$ y límite inferior con multiplicidades al cuadrado [texto completo](https://arxiv.org/html/math/0103058v2); distinción de $d_j$ como ganancia por semilla.



## Referencias vivas y procedencia de revisión

La copia `fuentes/COMPENDIO_RIEMANN_CME_2026-11-21.md` documenta un **estado anterior** al texto revisado en [PR #11 — CME–RH](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/11) (en borrador al 21-XI-2026). La edición R–03 v0.4 pertenece al [PR #9 — R–03 y Gram](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/9), también en borrador; no se presenta como texto ya fusionado en `main`. Se conservan los archivos de `fuentes/` como antecedentes íntegros; la integración debe enlazar el estado vigente de cada PR y cotejar sus cambios al fusionar.

**Le Matt Ansatz Di Ego**  
Endless Monkey Project / Relational Geometry Program
