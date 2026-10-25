# O37 — De dos formas separadas a una relación común persistente: mezcla, orientación y diferencia

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**20 de octubre de 2026 · Suplemento independiente, sin modificación de la Imagen Total**  
**Leyenda:** [D] contrato; [T] teorema condicionado; [E] comprobación reproducible; [O] correspondencia ontológica; [F] contraejemplo; [A] abierto.

## 0. Pregunta que efectivamente se intenta resolver

¿Podemos comenzar con dos concentraciones inicialmente separadas, diferentes en orientación, y demostrar **en la dinámica no forzada de Navier–Stokes 2D** que (i) aparece una relación compartida ausente al inicio, (ii) esa relación no desaparece posteriormente, y (iii) durante un intervalo ambas concentraciones conservan información propia y continúan espacialmente distinguibles?

**Respuesta [T]: sí, si la relación común se define explícitamente como solapamiento relacional de componentes de vorticidad etiquetadas** y «distinguible» se define mediante concentración de circulación y un cuadrupolo no degenerado. Se obtiene además una familia en que la diferencia de orientación disminuye inicialmente por el acoplamiento de Biot–Savart. **No** se obtiene sincronización de frecuencia estable de largo plazo, fusión, autorreferencia física universal o regularidad global 3D. La relación de solapamiento es un observable histórico de la descomposición inicial, **no** una función intrínseca de la vorticidad total en un instante.

## 1. Contrato [D]

En el plano completo, con viscosidad ν>0, sin forzamiento, un campo de vorticidad total no negativa y suficientemente regular:

\[
\partial_t\omega+u\cdot\nabla\omega=\nu\Delta\omega,\qquad
u>0,\quad \nabla\cdot u=0,\qquad
u=K_{BS}*\omega,\qquad K_{BS}(r)=\frac{Jr}{2\pi|r|^2}.
\]

**Nota de notación:** la última ecuación debe leerse **\(u=K_{BS}*\omega\)** (el símbolo `u` representa velocidad; **ν** representa viscosidad). No se debe confundir el campo con el coeficiente de difusión.

La vorticidad inicial es suma de **dos componentes de signo positivo** y soportes conexos disjuntos, fijadas **por las dos componentes conexas del soporte inicial**:

\[
\omega_0=\omega_{A0}+\omega_{B0},\qquad
\omega_{i0}\ge 0,\quad \Gamma_i=\int\omega_{i0}>0,
\quad \operatorname{supp}\omega_{A0}\cap\operatorname{supp}\omega_{B0}=\varnothing.
\]

Su evolución etiquetada está determinada unívocamente por el campo **total**:

\[
\partial_t\omega_i+u\cdot\nabla\omega_i=\nu\Delta\omega_i,\qquad
\omega=\omega_A+\omega_B,
\quad i=A,B.
\tag{1}
\]

Las etiquetas son un historial matemático determinado por el dato inicial. Tras difundirse, **no** se recuperan de forma única mirando solo \(\omega(\cdot,t)\). Las circulaciones \(\Gamma_i\) se conservan. Al crecer en espacio por difusión, el soporte de cada \(\omega_i(t)\) deja de ser compacto para \(t>0\).

En los cocientes siguientes se entiende \(t>0\), cuando \(\omega>0\) bajo el principio fuerte del máximo. Para \(t=0\) se define el integrando por continuidad igual a cero donde \(\omega=0\).

## 2. Teorema O37-T1 — Una relación de mezcla que aparece y no disminuye [T]

Defina la composición local adimensional de las etiquetas:

\[
 f(x,t)=\frac{\omega_A(x,t)}{\omega_A(x,t)+\omega_B(x,t)}\in[0,1]
\]

y el **solapamiento relacional**:

\[
\boxed{\mathcal O(t)=\int \frac{\omega_A\omega_B}{\omega_A+\omega_B}\,dx
=\int \omega f(1-f)\,dx.}\tag{2}
\]

Esta expresión es invariante ante intercambiar etiquetas, traslaciones o rotaciones de la misma configuración. **No** es una energía, entropía termodinámica ni frecuencia. Para soportes inicialmente disjuntos, \(\mathcal O(0)=0\).

**Identidad de producción [T]:**

\[
\boxed{
\frac{d\mathcal O}{dt}
=2\nu\int\omega\,\left|\nabla\left(\frac{\omega_A}{\omega}\right)\right|^2\,dx\ge0.
}\tag{3}
\]

Con datos iniciales no triviales de soportes disjuntos, existe \(T_*>0\) tal que \(\mathcal O(t)>0\) y \(\dot{\mathcal O}(t)>0\) para todo \(0<t<T_*\). El solapamiento \(\mathcal O\) permanece **no decreciente en todo el horizonte de existencia regular**, no solo en esta ventana.

**Prueba.** De (1) para \(\omega\) y \(\omega f\) resulta

\[
(\partial_t+u\cdot\nabla)f
=\nu\Delta f+2\nu\nabla\log\omega\cdot\nabla f.
\tag{4}
\]

Para cualquier \(h\in C^2([0,1])\), una regla de la cadena directa da

\[
\partial_t[\omega h(f)]+\nabla\cdot[u\omega h(f)]
=\nu\Delta[\omega h(f)]-\nu\omega h''(f)|\nabla f|^2.
\tag{5}
\]

Al integrar en todo \(\mathbb R^2\), los flujos de frontera se anulan por localización, quedando \(d\int\omega h(f)/dt=-\nu\int\omega h''(f)|\nabla f|^2\). Para \(h(f)=f(1-f)\), se tiene \(h''=-2\), y obtenemos (3). Como ambas componentes son positivas para \(t>0\) por difusión, \(\mathcal O(t)>0\). El hecho de que al comienzo sean realmente diferentes implica que \(f(\cdot,t)\) no puede ser constante en todo un intervalo inicial; su derivada es entonces estrictamente positiva en una ventana temporal positiva, por la continuidad de soluciones. □

La ley anterior incluye el caso sin advección. **La creación de solapamiento es un efecto de difusión compartida, no una prueba de sincronización vorticial inducida por la parte no lineal.** La advección incomprensible no contribuye al signo de (3), aunque sí determina las formas y la posición de las regiones donde la mezcla tiene lugar.

**Cota universal exacta:** para \(\Gamma=\Gamma_A+\Gamma_B\),

\[
\boxed{0\le\mathcal O(t)\le\frac{\Gamma_A\Gamma_B}{\Gamma}.}\tag{6}
\]

Prueba: con \(\alpha=\Gamma_A/\Gamma\), la cantidad \(\mathcal D(t)=\int\omega(f-\alpha)^2 dx\) satisface

\[
\boxed{\mathcal D(t)=\frac{\Gamma_A\Gamma_B}{\Gamma}-\mathcal O(t),\qquad
\dot{\mathcal D}=-2\nu\int\omega|\nabla f|^2 dx.}\tag{7}
\]

Así, la relación creciente también se entiende como disminución de la **diferencia de composición** bajo un comparador declarado. Si alguna vez \(\mathcal D=0\), las etiquetas serían proporcionales espacialmente, pero esto no se exige ni se afirma en tiempo finito.

**Generalización [T]:** la ecuación (5) da una familia de funciones de comparación; para \(h\) convexa, \(\int\omega h(f)\) es no creciente. La derivación no depende de ajustar coeficientes ni de observar el resultado final.

## 3. Teorema O37-T2 — Las dos identidades pueden persistir mientras surge el solapamiento [T]

Sea \(c_i=\Gamma_i^{-1}\int x\omega_i\), \(S_i=\Gamma_i^{-1}\int|x-c_i|^2\omega_i\), \(d_0=|c_A(0)-c_B(0)|\). Para \(M_0=\|\omega_0\|_\infty\), \(\Gamma=\Gamma_A+\Gamma_B\), O31 demuestra con \(U_0=\sqrt{2\Gamma M_0/\pi}\):

\[
\sqrt{S_i(t)}\le\underbrace{\sqrt{S_i(0)+4\nu t}+U_0t}_{a_i^{\rm sup}(t)},
\quad d(t)\ge d_0-2U_0t.
\tag{8}
\]

Si para cierto \(T>0\)

\[
\boxed{2[a_A^{\rm sup}(T)+a_B^{\rm sup}(T)]<d_0-2U_0T,}\tag{9}
\]

entonces las dos etiquetas conservan por lo menos el **75 % de su circulación individual en discos separados** para todo \(t\le T\).

Defina el cuadrupolo de cada forma en notación compleja \(z=x+iy\):

\[
Q_i(t)=\Gamma_i^{-1}\int(z-C_i)^2\omega_i(z,t)\,dA.
\tag{10}
\]

El resultado O32 proporciona

\[
 |Q_i(t)|\ge|Q_i(0)|-H_i(t),\qquad
H_i(t)=\frac{U_0}{3\nu}\bigl[(S_i(0)+4\nu t)^{3/2}-S_i(0)^{3/2}\bigr]+U_0^2t^2.
\tag{11}
\]

Si \(|Q_i(0)|>H_i(T)\), ambas formas conservan una **anisotropía de segundo orden no nula** en la ventana \([0,T]\).

**Teorema conjunto:** datos iniciales con dos soportes disjuntos, forma cuadrupolar no nula y desigualdad estricta de concentración al tiempo cero admiten algún \(T>0\) en el que simultáneamente:

1. \(\mathcal O(0)=0<\mathcal O(t)\), y \(\dot{\mathcal O}(t)>0\) para \(0<t<T\);
2. se conserva \(\ge75\%\) de la circulación de cada etiqueta en dos discos disjuntos;
3. \(Q_A(t),Q_B(t)\ne0\), por lo que ambas conservan información propia de forma.

**Prueba:** T1, las cotas (8)–(11), y continuidad de las desigualdades estrictas en \(t=0\). El intervalo es la intersección de las ventanas de cada garantía. □

**Importante:** el solapamiento matemático de dos etiquetas aumenta incluso mientras los discos principales permanecen disjuntos. Positividad de las colas difundidas no elimina las concentraciones independientes. Esto distingue *relación creciente* de *fusión total*.

## 4. Teorema O37-T3 — También es posible acercar dos fases de forma por Biot–Savart [T]

El resultado anterior usa difusión, pero no exige que la parte no lineal acerque las orientaciones. Para acreditar **ambos canales en un mismo dato inicial** construiremos ahora dos concentraciones elípticas positivas y compactamente soportadas, de la misma intensidad y forma, pero orientadas distinto.

Sean \(a>b>0\), \(\theta_A=0\), \(\theta_B=\theta<0\), centros \(c_A=(-d/2,0),c_B=(d/2,0)\), y \(\rho\) una densidad radial suave o \(C^k\), positiva dentro del disco unidad y nula fuera. Con \(T_\theta=R_\theta\mathrm{diag}(a,b)\), tome

\[
\omega_{i0}(x)=\frac{\gamma}{ab}\rho(T_{\theta_i}^{-1}(x-c_i)),\qquad
\int_{|s|\le1}\rho(s)ds=1.
\tag{12}
\]

Para \(d>2a\), los soportes son disjuntos; la separación mayor necesaria en O31 se impone por separado. Como \(\rho\) es radial, los valores \(S_i(0)=S\) y \(|Q_i(0)|=D>0\) coinciden, pero \(Q_A=D\), \(Q_B=De^{2i\theta}\).

La diferencia de fases \(\Psi=\arg Q_A-\arg Q_B=-2\theta\) es invariante bajo giro simultáneo del par, y \(E=1-\cos\Psi\). Para cada \(Q\ne0\), la ley de cambio de orientación es la identidad de NS:

\[
\dot\phi_i=\operatorname{Im}\frac{\dot Q_i}{Q_i},\quad
\dot Q_i=\frac2{\Gamma_i}\int(z-C_i)U(z)\omega_i(z)dx.
\tag{13}
\]

El aporte de cada remolino a su propia \(\dot\phi_i\) es igual en los dos por invariancia rotacional y formas congruentes; al restarlos, se cancela. Los términos cruzados vienen **directamente** de Biot–Savart.

**Cálculo de interacción lejana [T].** Para \(d\to\infty\) con \(a,b,\theta\) fijos, la expansión del núcleo en el soporte de cada remolino da

\[
\boxed{
\dot\Psi(0)
=-\frac{\gamma S}{\pi D d^2}(1-\cos2\theta)+O(d^{-3}).
}\tag{14}
\]

En consecuencia, para \(\theta<0\) y separación suficientemente grande, \(\dot\Psi(0)<0\) y \(\Psi(0)>0\); así \(\dot E(0)=\sin\Psi(0)\dot\Psi(0)<0\) si \(0<-2\theta<\pi\).

**Prueba del coeficiente.** En el centro opuesto del par \(r=(\pm d,0)\),

\[
DK_{BS}(r)=-\frac{1}{2\pi d^2}
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

La traslación inducida (término constante en el campo externo) no contribuye a \(\dot Q_i\) porque \(\int(z-C_i)\omega_i=0\). La parte lineal induce \(\dot Q_i^{\times}=-i\gamma S/(\pi d^2)\) y una tasa angular \(-\gamma S\cos(2\theta_i)/(\pi Dd^2)\). Su resta da (14). Las correcciones provienen de la segunda derivada del núcleo y de la extensión finita de ambos soportes.

**Cota explícita suficiente [T].** Para soportes contenidos en discos de radio \(a\) alrededor de sus centros, el error total en \(\dot\Psi\) de (14) obedece la estimación conservadora

\[
\left|\dot\Psi(0)+\frac{\gamma S}{\pi Dd^2}(1-\cos2\theta)\right|
\le \frac{56\gamma a^3}{\pi D(d-2a)^3}.
\tag{15}
\]

En efecto, \(|D^2 K_{BS}(r)[h,h]|\le7|h|^2/(\pi|r|^3)\). El resto de Taylor de orden uno es a lo sumo \(7|h|^2/(2\pi(d-2a)^3)\), con \(|h|\le2a\). En cada \(\dot Q_i^{\times}\) el resto queda acotado por \(28\gamma a^3/(\pi(d-2a)^3)\), y la suma de los errores de fase introduce el factor \(2/D\). Por tanto un criterio **evaluado solo con datos iniciales** para \(\dot E(0)<0\) es

\[
\boxed{\frac{56a^3}{(d-2a)^3}<\frac{S}{d^2}(1-\cos2\theta),\qquad -\frac\pi2<\theta<0.}\tag{16}
\]

Esta desigualdad es deliberadamente muy conservadora. No debe emplearse para concluir que una pareja a distancia moderada carece de acercamiento si no la satisface.

**Ejemplo de prueba con momentos exactamente conocidos [T].** Use en el disco unidad la densidad

\[
\rho(s)=\frac{k+1}{\pi}(1-|s|^2)^k_+,\qquad k=8.
\]

Es \(C^7\), de soporte compacto y positiva en el interior; la solución viscosa es suave para \(t>0\). Por integración beta:

\[
S=\frac{a^2+b^2}{2(k+2)},\qquad D=\frac{a^2-b^2}{2(k+2)}.
\]

Con \(a=0.9\), \(b=0.5\), \(\gamma=1\), \(\theta=-0.35\), \(d=4000\): \(S=0.053\), \(D=0.028\); el lado izquierdo de (16) es aproximadamente \(6.39\cdot10^{-10}\), menor que el derecho \(7.79\cdot10^{-10}\). Por tanto **el signo del acercamiento inicial está garantizado por una desigualdad analítica**, aunque la magnitud del efecto es diminuta para tan gran separación.

**Consecuencia temporal [T].** Por continuidad de las soluciones 2D y de \(\dot E\), existe \(T_\phi>0\) tal que \(\dot E(t)<0\) para \(0\le t\le T_\phi\). Intersectando con el intervalo T2, hay una ventana \(0<T<\min(T_\phi,T_{\rm forma},T_{\rm sep})\) en la que ocurren simultáneamente:

\[
\boxed{
\mathcal O(t)>\mathcal O(0)=0,\quad
\dot{\mathcal O}(t)>0,\quad
\dot E(t)<0,\quad
Q_AQ_B\ne0,\quad
\text{dos concentraciones espacialmente distinguibles}.
}\tag{17}
\]

La afirmación es **existencial y rigurosa**, pero no proporciona una duración numérica explícita para \(\dot E<0\) en la evolución completa.

## 5. Ejemplo cuantitativo de las ventanas O31–O32 y verificación del signo [E]

Para la densidad compacta \(C^\infty\) \(\rho(s)\propto\exp[-1/(1-|s|^2)]\) en el disco, \(a=0.9,b=0.5,\gamma=1,\nu=0.02,\theta=-0.35,d=12\): cuadratura radial determina \(S\approx0.13849494\), \(D\approx0.07316714\). Utilizando la cota conservadora \(\|\omega_0\|_\infty\le2\gamma/(ab)\) (válida para esta densidad, cuya normalización da máximo menor que \(1\) en el disco) se obtiene \(U_0\approx2.37883215\). Entonces:

- el horizonte O31 de concentración por el criterio \(k=2\) permite \(T<0.71672968\);
- el horizonte O32 para conservar \(|Q_i|>0\) permite \(T<0.03680093\);
- la cuadratura inicial completa de Biot–Savart da \(\dot\Psi(0)\approx-0.00098791\), \(\dot E(0)\approx-0.00063643\).

**Precaución:** las cifras de Biot–Savart a \(d=12\) son diagnósticos numéricos de tiempo cero, no pruebas con intervalos certificados ni demostración de que \(\dot E<0\) hasta \(T=0.0368\). La condición suficiente (16) proporciona una construcción analítica con separación mucho mayor; mejorar su conservadurismo es una tarea independiente.

El código adjunto también evalúa la ley de mezcla en **soluciones exactas de NS 2D radiales concéntricas**, para las cuales la advección tangencial no modifica las distribuciones radiales y cada gaussiana evoluciona por difusión. Estas comprueban el mecanismo de mezcla, **pero no constituyen dos remolinos separados**.

## 6. Contraejemplos y límites [F/A]

1. **No hay sincronización universal.** En la familia de forma elíptica, cambiar \(\theta<0\) por \(\theta>0\) invierte el signo de \(\dot E\), aunque el solapamiento \(\mathcal O\) siga siendo monótono. Mezcla y sincronización son propiedades diferentes.
2. **La viscosidad es esencial para (3).** Si \(\nu=0\) (Euler 2D), \(\dot{\mathcal O}=0\). Un transporte incomprensible común sin difusión no produce esta novedad de solapamiento. La advección por sí sola sí puede cambiar \(E\) y deformar las formas.
3. **No hay identidad intrínseca de etiquetas en una foto del futuro.** Dos descomposiciones \(\omega_A+\omega_B=\omega\) de la misma vorticidad instantánea pueden tener valores diferentes de \(\mathcal O\). La selección inicial por soportes separados reduce esa arbitrariedad, pero el observable sigue siendo **histórico**.
4. **No hay persistencia eterna de dos identidades.** Las cotas O31 y O32 garantizan un intervalo finito; el solapamiento positivo no garantiza que las formas continúen separadas a tiempos grandes.
5. **No hay sincronización de frecuencias.** \(\dot E<0\) significa acercamiento inicial de orientaciones de **segundos momentos**; no prueba bloqueo de fases ni relación \(R_i\omega_i=v_*\) para la rotación material de vórtices.
6. **No hay transferencia automática a 3D.** En 3D, la vorticidad vectorial obedece estiramiento, puede cambiar de dirección, y esta ley para dos vorticidades escalares positivas no se exporta sin reformular el sistema.
7. **No hay descubrimiento original de una ley de fluidos.** (3) es una identidad clásica de disipación de funcionales convexos para dos soluciones de transporte-difusión común, aplicada aquí a la vorticidad positiva. Su papel nuevo **dentro del programa** consiste en ofrecer una realización operativa y falsable del par `comparación / residuo`.

## 7. Interpretación ontológica controlada [O]

- **Forma propia:** \(Q_i,S_i\) y una distribución de vorticidad que puede conservar diferencias medibles.
- **Comparación modular:** \(f=\omega_A/(\omega_A+\omega_B)\) mide cómo contribuye cada forma a la referencia común donde coincide con la otra.
- **Relación nueva:** \(\mathcal O\) es inicialmente cero para soportes separados, después positivo y no decreciente.
- **Resto:** \(\mathcal D\), más diferencias geométricas que la mezcla no agota. **No es azar ni una voluntad del sistema.**
- **Cierre propio relativo:** durante una ventana, dos concentraciones mantienen una interfaz diferenciadora mientras una relación de mezcla compartida se construye y persiste.
- **Límite ontológico:** no se ha demostrado que toda forma de cierre propio deba realizarse físicamente como disipación de mezcla. Lo resuelto por este contrato no agota las posibilidades del núcleo.

La frase de alcance preciso es:

> **En Navier–Stokes bidimensional viscoso existen datos con dos formas inicialmente disjuntas y distintas para los que aparece una relación creciente de mezcla, mientras cada forma conserva una diferencia geométrica y ambas permanecen distinguibles durante un intervalo no nulo; podemos escoger además orientaciones para que su desacuerdo cuadrupolar disminuya inicialmente por la interacción de Biot–Savart.**

Esta afirmación es un resultado físico-matemático condicionado para un caso particular; no es la solución global del problema de Navier–Stokes ni una ley universal de sincronización.

## 8. Próxima obligación

La búsqueda más exigente queda bien definida: encontrar un observable **intrínseco al campo total instantáneo**, o una firma histórica reconstruible sin etiquetas impuestas, cuyo cierre conjunto sea dinámicamente estable bajo perturbaciones durante una ventana cuantitativa extensa. Una candidata distinta al solapamiento es una función de los conjuntos de nivel de vorticidad y su persistencia topológica, con un criterio que identifique nuevos máximos, bifurcaciones o conectividad. No se declara demostrado.

## 9. Antecedentes

- O28–O36: comparación modular, formas y fases de cuadrupolo, interacción exacta, persistencia, simetrías, atractores, acercamiento unilateral.
- O31 y O32: cotas de concentración y anisotropía a priori.
- Núcleo Generativo Canónico: comparación \(\mathcal C(a,b)=(q,r)\); la novedad no debe imponerse al resultado.
- Gallay, *Interaction of vortices in viscous planar flows*, arXiv:0908.2518; Gallay & Wayne, *Invariant manifolds and the long-time asymptotics of the Navier–Stokes and vorticity equations on R²*, arXiv:math/0102197.

**Política de integración:** este suplemento no modifica ningún archivo canónico ni la Imagen Total.
