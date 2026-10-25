# O38 — Bifurcación intrínseca de una referencia de vorticidad en Navier–Stokes 2D

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**20 de octubre de 2026 · Suplemento de investigación independiente**  
**Política:** no modifica el Núcleo Canónico, O24–O37 ni la Imagen Total.

**Leyenda:** [D] definición; [T] identidad/teorema bajo hipótesis; [E] control ejecutable; [O] interpretación ontológica; [F] falsador; [A] abierto.

## 0. Juicio resumido

**[T]** Para dos núcleos gaussianos idénticos y espacialmente separados, el dato inicial de Navier–Stokes bidimensional posee dos máximos locales y un punto central tipo silla. Para cada viscosidad fija y una elección explícita de la separación mayor que la anchura, existe una circulación positiva suficientemente pequeña de ambos núcleos tal que el punto central, que permanece crítico por simetría rotacional de media vuelta, se convierte en un máximo local estricto en un tiempo finito y conserva esa condición en una ventana posterior. Por continuidad, en el intervalo ocurre al menos una degeneración de la curvatura central. El testigo se computa a partir de **la vorticidad total instantánea**, sin etiquetas históricas ni coeficiente artificial de sincronización.

**[A]** No se demuestra fusión topológica global en un único máximo para todo flujo; no se demuestra retención de ambas identidades durante la transición, cierre propio autosostenido, sincronización de fases, derivación del programa desde NS ni regularidad NS 3D. El mecanismo está dominado por difusión cuando la circulación es pequeña.

## 1. Contrato físico [D]

En el plano completo, con viscosidad ν>0 y sin fuerza externa:

\[
\partial_t\omega+u\cdot\nabla\omega=\nu\Delta\omega,\qquad
u=K_{BS}*\omega,\qquad K_{BS}(x)=\frac{Jx}{2\pi|x|^2}.
\]

En la segunda fórmula, el símbolo **\(u\)** indica el campo de velocidades inducidas y **\(\nu\)** la viscosidad. El dato es suave, positivo, de caída gaussiana; se usa la teoría clásica de existencia, unicidad y dependencia continua en amplitud para Navier–Stokes 2D.

Se toman \(a>\sigma>0\), \(\gamma>0\), \(e_1=(1,0)\), y

\[
\boxed{\omega^\gamma_0(x)=
\frac{\gamma}{2\pi\sigma^2}
\left[e^{-|x-ae_1|^2/(2\sigma^2)}+
 e^{-|x+ae_1|^2/(2\sigma^2)}\right].}\tag{1}
\]

La circulación de cada gaussiana inicial es \(\gamma\); la total es \(2\gamma\). No se exige que cada componente siga siendo gaussiana después de \(t=0\).

## 2. Testigo geométrico instantáneo sin etiquetas [D/T]

Definimos, únicamente desde la vorticidad total instantánea:

\[
\Gamma=\int\omega\,dx,\quad
C=\Gamma^{-1}\int x\omega\,dx,\quad
R^2=\Gamma^{-1}\int|x-C|^2\omega\,dx.
\]

Si \(\omega(C,t)>0\), defínase el módulo adimensional

\[
\boxed{\mathscr B[\omega(t)]
=R(t)^2\lambda_{\max}\!\left(\nabla^2\log\omega(C(t),t)\right).}\tag{2}
\]

Si \(C(t)\) es un punto crítico, \(\mathscr B<0\) garantiza un máximo local estricto; \(\mathscr B>0\) dice que existe una dirección de curvatura positiva pero no determina por sí sola la signatura completa. En nuestro ejemplo el otro autovalor es negativo inicialmente; el centro es una silla.

**Invariancia exacta:** bajo traslación, rotación y dilatación positiva conjunta \(x\mapsto b+\ell Rx\), el nuevo radio es \(R'^2=\ell^2R^2\); la Hessiana logarítmica pasa a \(\ell^{-2}R(\nabla^2\log\omega)R^T\), y los autovalores escalan por \(\ell^{-2}\). Por tanto \(\mathscr B\) es invariante. Multiplicar la vorticidad por una constante positiva también conserva \(\mathscr B\), porque el logaritmo solo cambia en una constante. **No es necesario identificar un remolino A o B en el tiempo futuro.**

Además, la simetría \(\omega_0(-x)=\omega_0(x)\) se conserva por unicidad de la ecuación ante rotación de 180 grados. Por tanto \(C(t)=0\) y \(\nabla\omega(0,t)=0\) para todos los tiempos regulares. La rotación de 180° es una simetría orientada de NS; no se requiere invariancia ante reflexión axial.

## 3. Referencia exacta de difusión [T]

Al retirar el transporte no lineal, el dato (1) evoluciona por el calor con

\[
 s^2(t)=\sigma^2+2\nu t,\qquad
h(x,t)=\frac{1}{2\pi s^2(t)}
\left[e^{-|x-ae_1|^2/(2s^2(t))}+e^{-|x+ae_1|^2/(2s^2(t))}\right].
\tag{3}
\]

Su logaritmo puede escribirse como

\[
\log h(x,y,t)=\mathrm{const}-\frac{x^2+y^2+a^2}{2s^2}
+\log\cosh\!\left(\frac{ax}{s^2}\right).
\]

La Hessiana central es diagonal, con

\[
\boxed{\lambda_x(t)=\frac{a^2-s^2(t)}{s^4(t)},\qquad
\lambda_y(t)=-\frac1{s^2(t)}.}\tag{4}
\]

Si \(a>\sigma\), inicialmente \(\lambda_x(0)>0>\lambda_y(0)\): silla. Si \(s(t)>a\), ambos autovalores son negativos: máximo local estricto. La transición de referencia sucede en

\[
\boxed{T_c^{\mathrm{calor}}=\frac{a^2-\sigma^2}{2\nu}.}\tag{5}
\]

En la referencia de calor, la ecuación de puntos críticos sobre el eje x es \(x=a\tanh(ax/s^2)\). Cuando \(a>s\), tiene dos soluciones no nulas simétricas, que corresponden a los dos máximos; cuando \(a<s\), únicamente x=0 es crítico y es un máximo estricto. Esto demuestra una reorganización real de la **forma total** en el sistema lineal de referencia.

## 4. Teorema O38-T1 — La transición existe en Navier–Stokes 2D [T]

**Enunciado.** Fijados \(a>\sigma>0\), \(\nu>0\) y un tiempo \(T>T_c^{\mathrm{calor}}\), existe \(\gamma_*(a,\sigma,\nu,T)>0\) tal que para cualquier circulación inicial \(0<\gamma<\gamma_*\), la solución de Navier–Stokes 2D de (1) satisface:

1. el centro de vorticidad y el punto crítico central coinciden exactamente en el origen;
2. inicialmente la Hessiana de \(\log\omega^\gamma(0,0)\) es indefinida y hay dos máximos no centrales;
3. en tiempo \(T\), la Hessiana logarítmica central es definida negativa: existe un **nuevo máximo local estricto en el centro**;
4. existe \(t_*\in(0,T)\) con \(\mathscr B(t_*)=0\); para cada \(\gamma\) suficientemente pequeña, \(t_*\) puede localizarse arbitrariamente cerca de \(T_c^{\mathrm{calor}}\), aunque sin cota numérica explícita para \(\gamma_*\);
5. en una ventana abierta alrededor de \(T\), persiste la condición de máximo local central, por continuidad y estrictez de la Hessiana.

**Prueba.** Escriba \(\omega^\gamma=\gamma w^\gamma\). Biot–Savart es lineal, por lo que \(u^\gamma=\gamma K_{BS}*w^\gamma\). El campo normalizado cumple

\[
\boxed{\partial_t w^\gamma
=\nu\Delta w^\gamma
-\gamma (K_{BS}*w^\gamma)\cdot\nabla w^\gamma,}
\quad
w^\gamma(0)=h(0).\tag{6}
\]

Para datos gaussianos suaves y cualquier \(T<\infty\), la teoría de soluciones parabólicas 2D y su dependencia continua en el parámetro de la no linealidad implican \(w^\gamma\to h\) en \(C([0,T];C^2(K))\) para cada compacto K; incluso puede tomarse una clase de mayor regularidad apropiada para estos datos. Se necesita asimismo que \(w^\gamma(0,t)\) permanezca positiva y que \(\nabla w^\gamma\to\nabla h\), propiedades que cumplen estos datos positivos y las soluciones suaves.

En \(t=0\), los signos de la Hessiana central son estrictos y **no dependen de \(\gamma\)**, porque \(\log(\gamma h)=\log\gamma+\log h\). En \(T>T_c\), los dos autovalores de la Hessiana central de \(\log h\) son estrictamente negativos. La dependencia continua preserva ambos signos para \(\gamma\) bastante pequeña. La simetría de media vuelta preserva la condición \(\nabla\omega(0,t)=0\). Por continuidad en tiempo de los autovalores y del módulo (2), al menos uno de ellos debe anularse en un \(t_*\in(0,T)\). La localización de \(t_*\) cerca de \(T_c\) se deduce de la convergencia uniforme en subintervalos cerrados que excluyen \(T_c\). La Hessiana negativa estricta también se conserva para tiempos próximos a \(T\). □

**Importante:** el teorema garantiza una **transición geométrica central**; no demuestra que no aparezcan otros máximos alejados del centro, ni que dos remolinos inicialmente separados hayan persistido como identidades independientes hasta \(T\). El ejemplo no necesita etiquetas históricas, pero tampoco demuestra una nueva simetría rotacional exacta.

## 5. Ejemplo con valores evaluados [E]

Tomar \(\sigma^2=1\), \(a=2\), \(\nu=0.5\). Para calor:

\[
T_c=3,\quad R^2(t)=2s^2(t)+a^2=6+2t,\quad
\mathscr B(0)=18,\quad\mathscr B(3)=0,\quad\mathscr B(6)=-54/49\approx-1.102040816.
\]

La ley \(R^2(t)=R^2(0)+4\nu t\) **también es exacta para la solución no lineal NS 2D**, porque la auto-advección total no modifica el segundo momento central global. No se ha calculado un valor numérico de \(\gamma_*\), ni se ha ejecutado una simulación NS completa; los números exhibidos pertenecen a la solución exacta de calor, mientras que la existencia de una solución NS con cambio de signo se obtiene por perturbación rigurosa.

## 6. Prueba adversarial O38-F1 — La mezcla etiquetada no es un criterio intrínseco [T/F]

Sea la misma vorticidad total \(\omega=\omega_A+\omega_B\). O37 definió \(\mathcal O=\int \omega_A\omega_B/(\omega_A+\omega_B)\), monótona para etiquetas que siguen el mismo transporte-difusión. Pero puede elegirse, en un instante, \(\omega'_A=\omega/2\) y \(\omega'_B=\omega/2\), lo que produce \(\mathcal O'=\Gamma/4\) para **la misma configuración total**; la separación natural en las dos gaussianas tiene \(\mathcal O<\Gamma/4\). Por tanto no existe una función \(F\) del campo total instantáneo que reproduzca el solapamiento de toda descomposición admisible: \(\mathcal O\) es una **firma histórica de la etiqueta**, no un observable intrínseco al flujo.

El indicador \(\mathscr B\) sí es intrínseco al campo instantáneo. Esto no lo hace automáticamente un índice universal de identidad: debe especificarse la positividad, regularidad, existencia del centro y significado de su curvatura.

## 7. Contrato epistemológico y conexión con el programa [O/A]

- **[D/T] Comparador interno:** el centro, radio global y curvatura del logaritmo salen del propio campo de vorticidad; no hay observador físico ni voluntariedad en la comparación.
- **[T] Novedad relativa al comparador:** en una ventana finita el punto central cambia de silla a máximo de la vorticidad, una distinción del flujo total y no de etiquetas de origen. La nueva propiedad persiste en un intervalo abierto posterior.
- **[F] No es nuevo principio físico universal:** el proceso es una consecuencia clásica de difusión y de la estabilidad de NS 2D cerca de ese régimen, no un descubrimiento inédito de mecánica de fluidos.
- **[A] No conserva necesariamente dos identidades:** precisamente el nuevo foco central puede acompañarse de la pérdida de dos máximos individuales. Este es un discriminante contra una noción de cierre que exija coexistencia permanente de dos formas separadas.
- **[A] No es aún cierre propio autosostenido:** un máximo local no garantiza estabilidad ante perturbaciones grandes, un atractor ni una interfaz suficiente para predecir futuras evoluciones.
- **[A] No prueba sincronización de frecuencias** \(R_i\omega_i=v_*\), ni regularidad 3D, ni un puente necesario de los postulados ontológicos a Navier–Stokes.

**Siguiente problema concreto:** estimar \(\gamma_*\) o certificar una ventana temporal amplia mediante cotas cuantitativas del operador no lineal; comparar con simulación NS 2D que identifique máximos y su estructura de nivel. Si se desea conservar dos identidades, construir un comparador intrínseco de par que siga siendo definible después de la difusión, sin depender de etiquetas iniciales.

## 8. Bibliografía

- Thierry Gallay y C. Eugene Wayne, *Global stability of vortex solutions of the two-dimensional Navier–Stokes equation*, Comm. Math. Phys. 255 (2005), 97–129, DOI 10.1007/s00220-004-1254-9, arXiv:math/0402449. Resultados de convergencia global a vórtice Oseen; **no atribuimos nuestro módulo de curvatura a este trabajo**.
- Programa de Geometría Relacional, suplementos O31–O37 y Núcleo Generativo Canónico. Las identidades sobre vorticidad y la estabilidad parabólica son matemáticas conocidas; la interpretación relacional es un encuadre de investigación, no una validación de la ontología.
