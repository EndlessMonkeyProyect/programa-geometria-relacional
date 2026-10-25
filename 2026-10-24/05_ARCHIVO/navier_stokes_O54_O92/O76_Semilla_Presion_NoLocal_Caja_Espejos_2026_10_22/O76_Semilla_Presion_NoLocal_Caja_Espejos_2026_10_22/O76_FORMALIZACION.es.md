# O76 — Semilla suficiente, cuatro cápsulas y presión no local

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**22 de octubre de 2026** · suplemento aditivo O76, continúa O70–O75 · español

**Estado epistemológico:** `[O]` ontología propuesta, `[N]` narrativa interpretativa, `[D]` identidad o construcción demostrada, `[E]` comprobación numérica reproducible, `[H]` hipótesis por estudiar, `[F]` falsador delimitado. **No constituye una solución del problema de regularidad de Navier–Stokes 3D.**

## 0. Prioridad: la relación, no la energía [O]

La unidad se sostiene en un cierre propio cuando las diferencias encuentran una referencia común. El múltiplo que hizo posible su normalización se transporta como referente; no se identifica automáticamente ni con el número de reflejos de la caja ni con una magnitud energética. La novedad puede habitar relaciones disponibles sin destruir el cierre resuelto. La proyección tetraedro→anillo coplanar puede dejar enlaces sin participar del circuito; la alternancia de los giros permite un grado de libertad cinemático en el modelo de engranajes, pero no obliga al campo fluido a sincronizarse.

**Pregunta O76:** ¿una semilla calculada con cuatro enlaces, sus radios, frecuencias y la proyección de los ocho espejos puede predecir de modo autónomo la transformación siguiente? ¿Qué relación omitida puede causar una diferencia dinámica verificable?

## 1. Caja apagada: dos nociones distintas [N]

La caja *computa* coincidencias de un campo observado; «apagar» los espejos elimina la operación exterior de reflexión, pero no la dinámica ni la interacción entre regiones del fluido. Una semilla que continúe debe tener suficiente información para reconstruir su siguiente referencia sin volver a solicitar datos que descartó. 

La prueba adversarial será particularmente exigente: los cuatro nodos verán idénticas velocidades y derivadas locales hasta orden dos, pero su evolución no será idéntica. Así evitamos confundir una mera diferencia de radios observados con la insuficiencia real del dato relacional.

## 2. Ecuación que conecta las cuatro cápsulas con el resto del campo [D]

En el toro periódico tridimensional `T³=(R/2πZ)³`, con viscosidad `ν>0`, consideremos NS incompresible sin fuerza:

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,\quad\nabla\cdot u=0.
\tag{76.1}
\]

Al tomar divergencia se obtiene la ecuación elíptica exacta

\[
\boxed{-\Delta p=\partial_i u_j\,\partial_j u_i.}\tag{76.2}
\]

La presión es una función **no local** del campo espacial de velocidades, mediante la solución periódica de (76.2). El valor de `∇p` en un nodo no está determinado en general por la velocidad ni por un número finito de derivadas evaluadas únicamente en ese nodo. Esta no localidad matemática procede de la restricción de incompresibilidad: no es una afirmación de propagación física superlumínica para líquidos compresibles.

## 3. Teorema O76.1 — Mismas cuatro cápsulas y jets de orden dos, distinta aceleración [D]

Elijamos cuatro esquinas coplanares del dominio:

\[
X_1=(0,0,0),\ X_2=(\pi/2,0,0),\ X_3=(\pi/2,\pi/2,0),\ X_4=(0,\pi/2,0).
\tag{76.3}
\]

Comparemos dos datos iniciales suaves y solenoidales, uno en reposo `u^{(0)}=0`, y otro, para `c≠0`, dado por

\[
\boxed{u^{(c)}(x,y,z)=c\big[\sin^3(2y),\ \sin^3(2x)+\sin^4(2x),\ 0\big].}\tag{76.4}
\]

La divergencia es exactamente cero porque el primer componente depende sólo de `y`, el segundo sólo de `x` y el tercero es nulo. En cada una de las cuatro esquinas, tanto `u^{(c)}` como **todas sus derivadas espaciales de orden ≤2** son nulas. Por tanto, los cuatro nodos tienen **las mismas muestras locales hasta orden dos** para todas las amplitudes `c` y para el campo en reposo. Esto también iguala al inicio la deformación infinitesimal `F_i(0)=I`, la referencia local `H_F(0)=1` de O75 y la tasa de cambio `\dot H_F(0)=0`.

La presión *no* es equivalente. Escribamos `f(y)=sin³(2y)`, `g(x)=sin³(2x)+sin⁴(2x)`. En este caso:

\[
\Delta p=-2c^2f'(y)g'(x).\tag{76.5}
\]

La parte `g_o=sin³(2x)` es impar y aporta gradiente de presión `∂_x p(0,0)=0`; la parte `g_e=sin⁴(2x)` es par y genera la contribución no nula. Sus derivadas trigonométricas son

\[
f'(y)=\frac32(\cos2y-\cos6y),\qquad g_e'(x)=2\sin4x-\sin8x.
\tag{76.6}
\]

Por inversión explícita del laplaciano en los cuatro modos `sin(kx)cos(ly)` relevantes:

\[
\begin{aligned}
\partial_xp^{(c)}(0,0,0)&=
3c^2\left(\frac8{20}-\frac8{68}-\frac8{52}+\frac8{100}\right)\\
&=\boxed{c^2\frac{3456}{5525}}.
\end{aligned}\tag{76.7}
\]

En `X_1`, el término convectivo y el laplaciano local de la velocidad se anulan porque las derivadas hasta orden dos son cero. Por NS:

\[
\boxed{\partial_t u_x^{(c)}(X_1,0)=-c^2\frac{3456}{5525},\quad
\partial_t u_x^{(c)}(X_4,0)=+c^2\frac{3456}{5525}.}\tag{76.8}
\]

Así, la aceleración **relativa** entre dos de las cápsulas es

\[
\boxed{\partial_t[u_x(X_4)-u_x(X_1)]\big|_{t=0}=
 c^2\frac{6912}{5525}\approx1.251040724\,c^2.}\tag{76.9}
\]

Esta diferencia no se elimina trasladando o acelerando uniformemente el marco exterior. Es un observable diferencial entre nodos. En el campo en reposo ese valor es cero. Ambos datos dan lugar a soluciones clásicas locales; de hecho, la construcción es bidimensional embebida en 3D y pertenece a una clase globalmente regular. **No es un ejemplo de singularidad de NS.** QED.

**Alcance preciso de la negación:** una regla determinista que use solamente las posiciones de las cuatro cápsulas y los jets de velocidad hasta orden dos en ellas no puede predecir en general sus aceleraciones relativas. No se ha demostrado que *toda* compresión finita del campo sea imposible, ni que toda referencia ontológica deba ser infinita.

**Precisión sobre las frecuencias:** en el instante elegido las velocidades locales son cero y un cociente de frecuencias angulares de esos nodos puede ser **indefinido**, no lo postulamos igual a un valor racional. Lo que se ha igualado rigurosamente son las muestras del campo y sus dos primeras derivadas; los parámetros adicionales del normalizador no quedan automáticamente fijados.

## 4. Caja D₄ y relación dinámica no visible en la media [D/E]

Tomamos el grupo de ocho simetrías del cuadrado `D₄` sobre el plano `xy`. Definimos

\[
\mathcal P u=\frac18\sum_{g\in D_4}g\,u(g^{-1}x),\qquad
m=\mathcal Pu,\quad w=u-m.
\tag{76.10}
\]

Este modelo de ocho operaciones es una **elección de laboratorio**, no idéntica a la caja óptica de reflexiones infinitas de O59 ni al múltiplo entero ontológico de O40/O68.

Para el campo (76.4) se verifica por paridad **exactamente** `m(0)=0`: su promedio vectorial sobre el grupo es el mismo que para la configuración en reposo.

Sin embargo, para la elección con la suma de potencias cúbica y cuarta en el segundo componente, el promedio de su **derivada temporal inicial** no es cero. En unidades RMS del laboratorio:

\[
\boxed{\|\mathcal P\partial_tu^{(c)}(0)\|_{\rm RMS}=
0.4743416490\,c^2}\quad(c\ge0),\tag{76.11}
\]

valor verificado por cálculo espectral en dos resoluciones. La no linealidad cuadrática transmite al común información que la operación inicial de promediar había eliminado. Este cálculo numérico **no demuestra una regla nueva de acoplamiento de radios**, aunque sí comprueba la identidad exacta siguiente:

\[
\boxed{\partial_t m=F(m)-\mathbb L\nabla\cdot\tau,\qquad
\tau=\mathcal P^{(2)}(w\otimes w),}\tag{76.12}
\]

siendo `\mathbb L` la proyección de Leray y `F(m)=-\mathbb L\nabla\cdot(m\otimes m)+\nu\Delta m`. En este caso `m=0`, de modo que `\partial_tm=-\mathbb L\nabla\cdot\tau` en el instante inicial.

**Demostración de (76.12):** como `m` es invariante bajo todas las transformaciones, la media de los términos cruzados `m⊗w` y `w⊗m` es cero, mientras `\mathcal P^{(2)}(u⊗u)=m⊗m+\mathcal P^{(2)}(w⊗w)`. Aplicar `\mathcal P` a NS proyectada por Leray. QED.

Esta relación es una versión formal del mensaje O70: **el común no transporta automáticamente la información que lo hizo posible**.

## 5. Prueba positiva: existen semillas finitas *cuando hay una subfamilia dinámica exacta* [D]

No todo cierre comprimido es imposible. Consideremos en el toro tridimensional el campo ABC de Beltrami

\[
\begin{aligned}
U_x&=A\sin z+C\cos y,\\
U_y&=B\sin x+A\cos z,\\
U_z&=C\sin y+B\cos x.
\end{aligned}\tag{76.13}
\]

Verificaciones exactas: `∇·U=0`, `∇×U=U`, `ΔU=-U`. Como

\[
(U\cdot\nabla)U=\nabla(|U|^2/2)-U\times(\nabla\times U)
=\nabla(|U|^2/2),
\]

la solución sin forzamiento es

\[
\boxed{u(x,t)=e^{-\nu t}U(x),\qquad
p(x,t)=-\tfrac12e^{-2\nu t}|U(x)|^2.}\tag{76.14}
\]

Para esta familia, **los tres coeficientes `(A,B,C)`, el sistema de coordenadas y la viscosidad** determinan toda la evolución: una semilla finita físicamente suficiente. La cancelación de la parte solenoidal de la no linealidad es un resultado exacto, no impuesto mediante sincronización artificial.

**Advertencias:** ABC no es una construcción mínima de cuatro cápsulas, no describe nuestro anillo material como cuatro engranajes, y no demuestra regularidad tridimensional para datos generales. Prueba únicamente que las semillas finitas son posibles en **familias dinámicas cerradas**.

## 6. ¿Qué aporta O76 a la noción de identidad? [O/H]

Queda una distinción más afinada:

- **Coincidencia local:** cuatro cápsulas comparten ciertas muestras o un producto de enlace; puede ser insuficiente aun si incluye gradientes y curvaturas de segundo orden.
- **Coincidencia de reflejos:** `\mathcal P u` aisla un común, pero puede ocultar relaciones que influyen en su siguiente evolución.
- **Suficiencia dinámica:** una semilla debe incluir exactamente la información con la cual se determina su próxima referencia, o demostrar una ley interna que haga irrelevante lo omitido.
- **Cierre propio:** la descripción ontológica de continuidad sólo se vuelve una afirmación física si las relaciones de transición son consecuencias verificables de la dinámica y no ajustes retrospectivos.

El puente que corresponde investigar en O77 no es agregar un número a posteriori para forzar coincidencia: es **encontrar subfamilias invariantes** donde un conjunto pequeño de proporciones, fases y tensores de interacción tenga evolución autónoma. La familia ABC da un ejemplo positivo pero no representa todavía al anillo; el testigo O76 impide afirmar autonomía para el dato puramente local de cuatro cápsulas.

La presión no local y la viscosidad no se identifican con «información inmaterial» literal; son mecanismos físicos matemáticamente definidos que permiten estudiar qué información de una configuración influye sobre otra.

## 7. Reproducción y límites [E]

- Script `codigo/verificar_o76.py` (NumPy; Matplotlib opcional para gráfico).
- Correr `python codigo/verificar_o76.py --N 64` y `python codigo/verificar_o76.py --N 96`.
- Los campos son polinomios trigonométricos de modos resueltos exactamente por Fourier sobre `T²`, embebidos en `T³`; el cómputo no depende de integrar temporalmente Navier–Stokes.
- Salidas: `datos/resumen.json`, `datos/resumen_N64.json`, `datos/o76_contraste.csv`, `datos/controles.json` y `graficos/o76_presion_no_local.png`.
- La derivación racional `3456/5525` es **analítica**; su comparación con FFT es una comprobación de implementación.
- El contraste ABC es también analítico, y se prueban directamente sus identidades diferenciales.
- Ninguno de los resultados de O76 establece un tamaño físico mínimo de gota, el múltiplo entero del programa, ni una cota a priori universal de Navier–Stokes 3D.

**Resultado:** O76 construye un falsador explícito de suficiencia de cuatro enlaces locales, vincula el defecto de información con la presión no local y con el residuo de la caja de espejos, y aporta una familia positiva de soluciones NS donde sí existe una semilla finita exacta. La cuestión pendiente es **derivar una semilla autónoma para una familia física de anillos y demostrar después su alcance**.
