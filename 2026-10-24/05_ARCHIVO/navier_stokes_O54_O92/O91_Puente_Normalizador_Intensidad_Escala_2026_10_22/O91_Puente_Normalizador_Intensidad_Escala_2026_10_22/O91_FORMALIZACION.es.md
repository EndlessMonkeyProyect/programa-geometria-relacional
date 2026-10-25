# O91 — El múltiplo, la intensidad y la escala: prueba exacta de suficiencia dinámica

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 22 de octubre de 2026**  
**Continuidad:** O40, O44-N, O25, O39, O45, O66, O79, O88–O90.  
**Clasificación:** [O] interpretación ontológica; [D] definición; [T] teorema demostrado en contrato explícito; [F] falsador; [A] problema físico abierto.

## 0. Resultado terminado — sin confundir la prueba con la regularidad universal

**[F/T]** Existen dos soluciones *exactas, globalmente suaves, sin fuerza externa* de Navier–Stokes sobre el toro periódico que poseen en el instante inicial:

- el mismo soporte armónico `k=1,2,3,4`, fases sinusoidales y normalizador aritmético `N=mcm(1,2,3,4)=12`;
- idéntica intensidad cuadrática de velocidad, idéntica enstrofía e idéntica escala física de vorticidad;
- pero **tasas opuestas de cambio** del cociente entre intensidad, escala y viscosidad.

Esto falsifica la tesis de que dichos datos de cierre determinen por sí solos el comportamiento dinámico. Falsifica **esa interfaz**, no el principio ontológico general de cierre propio.

**[T]** En esta familia de **cuatro armónicos**, incluir una cuarta información —un momento espectral adicional, relacionado con `||Δω||²`— **sí** produce una interfaz dinámicamente suficiente: permite reconstruir exactamente las cuatro amplitudes modales y la evolución para todo tiempo. Se demuestra por matriz invertible y un sistema cerrado de cuatro ecuaciones.

**[F/T]** El cociente global `U_rms·ell_omega/nu` tampoco detecta por sí mismo concentración localizada: existe una familia de campos suaves, solenoidales y de energía decreciente hacia cero cuya norma crítica local diverge mientras ese cociente global tiende a cero. Es un **falsador cinemático**, no una trayectoria PDE.

**[A]** No se demuestra que esa interfaz finita controle un vórtice tridimensional no lineal general; no se demuestra ni se presupone regularidad global de Navier–Stokes 3D sin fuerza.

## 1. Ontología y contrato físico separados [O/D]

En el programa, el **múltiplo que normalizó** un valor referenciado permite su reconstrucción bajo refinamiento. Este hecho aritmético ya está probado en O40 y no se vuelve a postular. En O88–O90 vimos que la sincronización rígida 2:1 de cuatro nodos no es condición universal de continuidad.

Para preguntar si la continuidad de representación **controla** la física, debemos fijar observables antes de examinar la evolución. Elegimos una intensidad y una escala internas físicamente mensurables:

\[
U(t)^2=\langle |u|^2\rangle,\qquad
A(t)=\langle |\omega|^2\rangle,\qquad
B(t)=\langle |\nabla\omega|^2\rangle,
\]
\[
\boxed{\ell_\omega(t)^2=A(t)/B(t),\qquad
\mathcal K(t)=U(t)\ell_\omega(t)/\nu.}\tag{91.1}
\]

Los promedios `⟨·⟩` son volumen normalizado de `T³=(R/2πZ)³`; `ω=curl u`, `ν>0`. Se exige `U,A,B>0`. `\mathcal K` es adimensional (una medida tipo Reynolds). **No es el número entero `N`**. Para dilataciones enteras de Navier–Stokes `u_λ(x,t)=λu(λx,λ²t)` en este toro, `U_λ=λU`, `ℓ_{ω,λ}=ℓ_ω/λ`, `\mathcal K_λ=\mathcal K`; cambiar etiqueta o radio no lo hace pequeño automáticamente.

Para flujo general suave, derivar la definición da la identidad:

\[
\boxed{\frac{d}{dt}\log\mathcal K
=\tfrac12\left[\frac{(U^2)'}{U^2}+\frac{A'}A-\frac{B'}B\right].}\tag{91.2}
\]

En el caso **no forzado**, `\frac12(U²)'=-νA` y `\frac12A'=P-νB`, donde `P=⟨ω·Sω⟩` es estiramiento. `B'` contiene derivadas y transferencias adicionales (O25); ninguna depende exclusivamente del entero `N`. **Con fuerza externa**, aparecen términos adicionales `⟨f·u⟩` y `⟨ω·curl f⟩`: no omitirlos cuando se compare con la construcción forzada anunciada por OpenAI en septiembre de 2026.

## 2. Una familia de soluciones exactas, sin error numérico [T]

En el toro periódico, para `w_k>0`, `k∈{1,2,3,4}`, defina:

\[
\boxed{
 u_w(x,y,z,t)=
 \left(\sum_{k=1}^4\frac{\sqrt{w_k}}k e^{-νk^2t}\sin(ky),\ 0,\ 0\right).
}\tag{91.3}
\]

El campo es solenoidal, `(u·∇)u=0` por independencia de `x`, satisface `∂_t u=νΔu` y admite presión constante. Por tanto es solución **exacta y globalmente suave de NS 3D**, aunque pertenece a la clase degenerada de cizallas, no es un anillo tridimensional genérico.

La vorticidad es `ω_z=-Σ√w_k e^{-νk²t}cos ky`. Por ortogonalidad, con

\[
m_j(t)=\sum_{k=1}^4k^{2j}w_k e^{-2νk^2t},\qquad j=-1,0,1,2,\ldots,
\tag{91.4}
\]

se deduce exactamente:

\[
\boxed{U²=m_{-1}/2,\quad A=m_0/2,\quad B=m_1/2,\quad C:=\langle|Δω|²\rangle=m_2/2,\quad \ell_\omega²=m_0/m_1,\quad \mathcal K²=\frac{m_{-1}m_0}{2ν²m_1}.}\tag{91.5}
\]

La dinámica modal y de momentos está enteramente determinada:

\[
\boxed{w_k(t)=w_k(0)e^{-2νk^2t},\qquad m_j'=-2νm_{j+1}.}\tag{91.6}
\]

Por derivación de (91.5):

\[
\boxed{\frac{d}{dt}\log\mathcal K
=ν\left(\frac{m_2}{m_1}-\frac{m_1}{m_0}-\frac{m_0}{m_{-1}}\right).}\tag{91.7}
\]

El primer par de términos es no negativo por Cauchy–Schwarz, pero el último es estrictamente negativo. **No hay signo universal** para la evolución de `\mathcal K` siquiera en una cizalla suave exacta.

## 3. Falsador fuerte: mismas tres medidas, signos opuestos [T/F]

Con `ν=1`, fijamos dos vectores de pesos racionales positivos:

\[
 w^{(C)}=(7/12,\ 539/150,\ 1/20,\ 817/300),
\]
\[
 w^{(D)}=(203/300,\ 427/150,\ 113/100,\ 689/300).
\tag{91.8}
\]

Ambos tienen **todas** las frecuencias `1,2,3,4` activas con la misma fase seno; `N=mcm(1,2,3,4)=12`. Tienen exactamente los mismos tres momentos iniciales:

\[
\boxed{m_{-1}=23867/14400,\quad m_0=139/20,\quad m_1=2949/50.}\tag{91.9}
\]

Por tanto `U²`, `A`, `B`, `ℓ²` y `\mathcal K` **coinciden inicialmente**. La diferencia está en el siguiente momento:

\[
\boxed{m_2^{(C)}=7593/10,\qquad m_2^{(D)}=7257/10.}\tag{91.10}
\]

Al sustituir en (91.7), se obtienen **signos contrarios**:

\[
\boxed{\left.\frac d{dt}\log\mathcal K_C\right|_{0}
=\frac{3167962897}{16305576395}\approx+0.1942871,}\tag{91.11}
\]
\[
\boxed{\left.\frac d{dt}\log\mathcal K_D\right|_{0}
=-\frac{6121073503}{16305576395}\approx-0.3753976.}\tag{91.12}
\]

**Conclusión demostrada:** la interfaz `(N, U², A, ℓ²)` y el patrón de fases de seno **no determina ni siquiera el signo de la evolución inmediata** de la relación intensidad–escala. En particular la palabra «múltiplo» no puede sustituir la distribución de amplitudes entre las escalas físicas.

Como control adicional más simple, los pesos `(93,156,19,132)/100` y `(107,44,181,68)/100` tienen `N=12`, `U²=205/288`, `A=2`, `B=15`, `ℓ²=2/15` y `\mathcal K²=41/432` (con `ν=1`), pero sus derivadas logarítmicas de `\mathcal K` difieren **exactamente** en `42/25=1.68`. Dos pares independientes confirman la insuficiencia.

## 4. El resultado positivo: cuarto observable y cierre dinámico para estos cuatro modos [T]

El número físico adicional es

\[
\boxed{C=\langle|Δω|²\rangle=m_2/2.}\tag{91.13}
\]

Con frecuencias *conocidas* `1,2,3,4`, los cuatro pesos desconocidos `w=(w_1,\ldots,w_4)` quedan determinados por

\[
\begin{pmatrix}m_{-1}\\m_0\\m_1\\m_2\end{pmatrix}=
\underbrace{\begin{pmatrix}
1&1/4&1/9&1/16\\
1&1&1&1\\
1&4&9&16\\
1&16&81&256
\end{pmatrix}}_{\mathsf M}\begin{pmatrix}w_1\\w_2\\w_3\\w_4\end{pmatrix},
\quad\boxed{\det\mathsf M=525/2\ne0.}\tag{91.14}
\]

La inversión de esta matriz reconstruye los pesos iniciales. Con (91.6) reconstruye toda la evolución de la familia. Incluso puede escribirse una **dinámica cerrada de cuatro momentos**:

\[
\begin{aligned}
\dot m_{-1}&=-2ν m_0,\\
\dot m_0&=-2νm_1,\\
\dot m_1&=-2νm_2,\\
\dot m_2&=-2ν(30m_2-273m_1+820m_0-576m_{-1}).
\end{aligned}\tag{91.15}
\]

La cuarta ecuación se deduce de la identidad polinómica verdadera en `x∈{1,4,9,16}`:

\[
 x^4-30x^3+273x^2-820x+576=0.
\]

Multiplicar por `w_k/x` y sumar produce `m_3=30m_2-273m_1+820m_0-576m_{-1}`.

**Esta sí es una interfaz suficiente** para el contrato restringido: cuatro frecuencias conocidas, fase seno, cizalla lineal por estructura convectiva nula. **No se presume** que una interfaz de cuatro números cierre la dinámica general tridimensional. Los «cuatro modos» de esta prueba no son automáticamente las «cuatro partículas» ontológicas del nodo.

## 5. Otro falsador: puede aumentar \(\mathcal K\) sin singularidad [T/F]

Tome ahora solamente `k=1,3`, ambos de peso uno en (91.3). En `t=0`:

\[
\mathcal K(0)=1/(3ν),\qquad
\boxed{\left.\frac d{dt}\log\mathcal K\right|_0=7ν/5>0.}\tag{91.16}
\]

Aun así la solución es explícita, suave para todo tiempo y se apaga por disipación. El aumento inicial surge porque las frecuencias altas decaen más rápido: crece `ℓω` lo suficiente para que el producto `Uℓω` aumente a pesar de que `U` disminuye. **Aumento del cociente crítico local/medio no equivale a colapso.**

## 6. Falsador de concentración: el promedio global puede ocultar el núcleo [F/T]

No basta pasar del múltiplo entero a `\mathcal K=U_rms ell_omega/nu` y declararlo criterio universal. El promedio `U_rms` mide **toda la caja**, mientras una concentración puede ocupar un volumen diminuto. Probamos su limitación sin usar simulaciones.

Sea `V=\nabla\times(\psi e_3)` un campo no nulo, suave, solenoidal y de soporte compacto dentro de la bola unidad `B_1⊂R³`, con `\psi` suave y compactamente soportada. Sea `x_0` interior al toro y, para `0<ell≪1`, defina el **dato suave**

\[
\boxed{u_ell(x)=ell^{-\beta}V((x-x_0)/ell),\qquad \beta=6/5.}\tag{91.17}
\]

Todo `u_ell` es solenoidal y suave. La familia `ell→0` **NO es una trayectoria de una sola solución de Navier–Stokes**. Por sustitución de variable y derivación, obtenemos **escalados exactos** de magnitudes para esta familia, con constantes positivas dependientes de `V`:

\[
\|u_ell\|_2^2\asymp ell^{3-2\beta}=ell^{3/5}\to0,\quad
U_{rms}(u_ell)\asymp ell^{3/2-\beta}=ell^{3/10}\to0,
\]
\[
\ell_\omega(u_ell)\asymp ell,\quad
\boxed{\mathcal K_{global}(u_ell)\asymp ell^{5/2-\beta}=ell^{13/10}\to0.}\tag{91.18}
\]

**Al mismo tiempo**,

\[
\boxed{\|u_ell\|_{L^3}\asymp ell^{1-\beta}=ell^{-1/5}\to\infty.}\tag{91.19}
\]

Por tanto, **energía pequeña, `\mathcal K_global` pequeño y cociente creciente/no creciente no son por sí solos un detector de concentraciones locales**.

Un comparador local de velocidad, definido antes del ejemplo y sin usar el resultado futuro, es

\[
\boxed{\mathcal K_{local}(u;x,r)=\frac r\nu
\left(\fint_{B_r(x)}|u-u_{B_r(x)}|^3dy\right)^{1/3}.}\tag{91.20}
\]

En `x=x_0`, `r=ell`, la media del campo construido es cero por ser `V` un rizo compacto, y se obtiene `\mathcal K_local\asymp ell^{1-\beta}=ell^{-1/5}\to∞`. Además, este comparador es invariante bajo la escala crítica de Navier–Stokes cuando el radio y las coordenadas se transforman juntos; está ligado a una medida local de `L³`, no a `U_rms` global.

**Resultado:** una prueba de concentración necesita al menos un observable *local* y no solo un promedio sobre la caja. El perfil kinemático aquí empleado sirve para refutar la suficiencia del observable propuesto, **no para afirmar que existe blow-up en un flujo sin fuerzas**.

## 7. La información que realmente falta en Navier–Stokes 3D [A]

En esta prueba la cascada no lineal es nula. En el caso general, las transferencias dependen de fases, proyección de presión, orientaciones y amplitudes (`O79`, `O86`); una sucesión de momentos derivaría nuevas cantidades y no se cerraría simplemente como (91.15). El cierre espectral finito es especial de las cuatro frecuencias y no una demostración universal.

Para contrastar reorganización regular con un vórtice singular forzado como el anunciado por OpenAI, habrá que añadir a la ley (91.2) los **términos de fuerza** y medir sin reajuste retrospectivo la evolución de `U`, `ℓω`, la redistribución/modalidad y la presión. El contraste válido no es afirmar que `\mathcal K` tiene signo opuesto en todos los casos, sino preguntar si la interfaz propuesta predice la tasa con el mismo contrato.

**Posible pregunta fuerte para crítica externa:** «¿Existe una regla intrínseca de normalización relacional, independiente de la solución futura, que reduzca la jerarquía no lineal de transferencias a una cota dinámica suficiente para toda solución admisible?» O91 prueba que **tres momentos más un entero no bastan**, y da una versión **positiva** sobre una familia exacta de cuatro modos. No responde afirmativamente la pregunta general.

## 8. Reproducibilidad y trazabilidad

Ejecutar `python codigo/verificar_o91.py` (Python estándar, `matplotlib` opcional). La prueba de momentos, signos, determinante y recurrencia utiliza `fractions.Fraction` para comparaciones exactas. `resultados/verificacion.json` registra fracciones y estatus; `resultados/trayectorias.csv` y el gráfico ilustran sus trayectorias analíticas; **no se ejecuta una simulación de Navier–Stokes**. El script imprime 44 grupos de controles superados. El argumento físico de (91.3) es exacto por sustitución en la PDE.

**Procedencia ontológica:** conceptos de cierre, múltiplo y referencia del programa; ecuaciones de NS y herramientas de Fourier/energía son matemáticas conocidas usadas para contrastarlas. No atribuir automáticamente al programa esas herramientas externas ni reclamar este ejemplo como demostración global.

**Referencia externa sólo comparativa:** [OpenAI, *On the Navier–Stokes Millennium Prize Problem*, 8-IX-2026](https://openai.com/index/navier-stokes-solution/): anuncio de singularidad tridimensional **forzada**; no confundirlo con los resultados no forzados particulares aquí demostrados.
