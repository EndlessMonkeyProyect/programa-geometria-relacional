# O36 — Comparación modular, acercamiento unilateral y límite del cierre atractor

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**Fecha:** 20 de octubre de 2026  
**Estatus:** suplemento independiente y reproducible. NO modifica el Núcleo Canónico, los suplementos O24–O35 ni la Imagen Total.  
**Etiquetas:** [D] definición/contrato; [T] teorema con hipótesis; [E] verificación numérica puntual; [F] contraejemplo/no-go; [O] interpretación ontológica; [A] pregunta abierta.

## 0. Alcance

O35 demostró, para gaussianas elípticas positivas inicialmente separadas, que el flujo de Navier–Stokes bidimensional puede reducir **instantáneamente** una diferencia de orientación de formas, sin coeficiente de sincronización elegido. O36 precisa exactamente qué puede inferirse: una relación invariante de marco, un testigo de acercamiento unilateral, la existencia de **un intervalo finito** para un conjunto abierto de datos y un obstáculo a proclamar atracción exponencial uniforme cerca de la alineación. No se demuestra un atractor para el PDE, bloqueo persistente, dos remolinos físicos separados eternamente, frecuencia universal ni regularidad 3D.

La noción de *módulo* sigue significando comparación estructural. No se atribuyen a los remolinos reconocimiento, elección ni conciencia.

## 1. Contrato de Navier–Stokes [D]

En el plano completo, \(\nu>0\) y sin forzamiento:

\[
\partial_t\omega+u\cdot\nabla\omega=\nu\Delta\omega,\qquad
\nabla\cdot u=0,\quad u=K_{BS}*\omega,\quad
K_{BS}(x)=\frac{Jx}{2\pi|x|^2}.
\]

Se distinguen dos etiquetas \(\omega_A,\omega_B\ge0\) en el dato inicial, transportadas y difundidas por el **mismo** campo total \(u\). Se presupone localización, regularidad y momentos suficientes para las integraciones. Cada \(\Gamma_i=\int\omega_i>0\) es constante. Etiquetas difusas no equivalen a fronteras materiales únicas.

Definimos \(c_i=\Gamma_i^{-1}\int x\omega_i\), \(S_i=\Gamma_i^{-1}\int|x-c_i|^2\omega_i\) y el cuadrupolo complejo:

\[
Q_i=\frac1{\Gamma_i}\int(z-C_i)^2\omega_i\,dA,\quad z=x+iy,\quad C_i=c_{ix}+ic_{iy}.
\]

En el dominio \(Q_AQ_Br\ne0\), con \(r=C_A-C_B\), la fase de cada forma es \(\phi_i=\arg Q_i\). El eje geométrico es \(\phi_i/2\pmod\pi\); **no** es la frecuencia de giro de partículas del fluido. Los vórtices circulares, con \(Q=0\), quedan fuera de esta carta, no fuera del conjunto de remolinos físicos.

La identidad exacta de O29–O32 es

\[
\boxed{\dot Q_i=\frac2{\Gamma_i}\int(z-C_i)(u_x+iu_y)\omega_i\,dA.}\tag{1}
\]

## 2. Módulo relacional independiente del marco [D/T]

Para \(p,q\in\mathbb N\), definimos el observable unitario

\[
\boxed{Z_{p:q}=
\left(\frac{Q_A}{|Q_A|}\right)^q
\left(\frac{\overline{Q_B}}{|Q_B|}\right)^p
\left(\frac{\overline r}{|r|}\right)^{2(q-p)}\in U(1).}\tag{2}
\]

**Teorema O36-T1.** \(Z_{p:q}\) es invariante bajo una traslación global, una rotación global del plano y una dilatación espacial positiva aplicada a todas las configuraciones. Bajo rotación \(z\mapsto e^{i\beta}z\): \(Q_i\mapsto e^{2i\beta}Q_i\), \(r\mapsto e^{i\beta}r\). Los exponentes de fase suman \(2q-2p-2(q-p)=0\). Bajo dilatación positiva, los cocientes unitarios no cambian. QED.

Al escribir \(Z_{p:q}=e^{i\Psi_{p:q}}\) se obtiene la **ley exacta**

\[
\boxed{\dot Z_{p:q}=iZ_{p:q}\dot\Psi_{p:q},\quad
\dot\Psi_{p:q}=q\Im\frac{\dot Q_A}{Q_A}-p\Im\frac{\dot Q_B}{Q_B}-2(q-p)\Im\frac{\dot r}{r}.}\tag{3}
\]

\(\dot Q_i\) y \(\dot r\) provienen del campo NS; no aparece una constante de sincronización arbitraria. **Suficiencia instantánea:** \((Q_A,Q_B,r,\dot Q_A,\dot Q_B,\dot r)\) determina \(\dot Z\), pero no acredita una interfaz finita suficiente para todas las continuaciones.

La discrepancia respecto del módulo elegido es

\[
\boxed{E_{p:q}=1-\Re Z_{p:q}=1-\cos\Psi_{p:q},\qquad
\dot E_{p:q}=\sin\Psi_{p:q}\dot\Psi_{p:q}.}\tag{4}
\]

## 3. Familia adversarial de dos gaussianas elípticas [D]

Fijamos \(a>b>0\), \(\gamma>0\), \(d>0\), dos centros \((-d/2,0),(d/2,0)\), y gaussianas con matrices de covarianza

\[
\Sigma_{\theta}=R_\theta\begin{pmatrix}a^2&0\\0&b^2\end{pmatrix}R_\theta^\top,
\qquad\theta_A=0,\quad\theta_B=\theta.
\]

Entonces \(\Gamma_A=\Gamma_B=\gamma\), \(S=a^2+b^2\), \(Q_A=D_Q=a^2-b^2>0\), \(Q_B=D_Qe^{2i\theta}\), \(\Psi_{1:1}=-2\theta\pmod {2\pi}\). Los datos generan soluciones 2D lisas para \(t>0\); **las gaussianas no se suponen gaussianas durante toda la evolución no lineal**.

Denotemos por

\[
f_d(\theta):=\dot\Psi_{1:1}(0;\theta,d)
=\Im\left(\frac{\dot Q_A(0)}{Q_A(0)}-\frac{\dot Q_B(0)}{Q_B(0)}\right)
\]

la derivada **exacta instantánea** de la fase producida por el campo NS.

## 4. Paridad, simetría y semiestabilidad [T]

**Teorema O36-T2 (paridad).** En esta familia:

\[
\boxed{f_d(-\theta)=f_d(\theta),\qquad f_d(0)=0.}\tag{5}
\]

*Prueba.* La reflexión \((x,y)\mapsto(x,-y)\) transforma la gaussiana de orientación \(\theta\) en la de orientación \(-\theta\), sin cambiar las dos circulaciones positivas. El núcleo de Biot–Savart transforma la velocidad compleja como \(U(\bar z)\mapsto-\overline{U(z)}\) cuando se conservan los signos escalares de vorticidad. Por (1), \(Q_i\mapsto\overline{Q_i}\) y \(\dot Q_i\mapsto-\overline{\dot Q_i}\); por tanto \(\Im(\dot Q_i/Q_i)\) es idéntico en ambas configuraciones. La diferencia de tasas conserva el signo. En \(\theta=0\), la media vuelta alrededor del origen intercambia las dos etiquetas y sus momentos, por lo que sus tasas de fase coinciden. QED.

Para \(a>b>0\), la función \(f_d\) es lisa y analítica localmente en \(\theta\), porque las matrices de covarianza permanecen definidas positivas y las integrales gaussianas del núcleo localmente integrable admiten derivación respecto de \(\theta\). Al ser par y anularse en cero:

\[
\boxed{f_d(\theta)=O(\theta^2)\quad (\theta\to0).}\tag{6}
\]

Para el canal 1:1:

\[
\boxed{\dot E_{1:1}(0;\theta,d)=-\sin(2\theta)f_d(\theta).}\tag{7}
\]

**Consecuencia:** si \(f_d(\theta)<0\) para ángulos pequeños de ambos signos, entonces para \(\theta<0\), \(\dot E<0\) (acercamiento), mientras que para \(\theta>0\), \(\dot E>0\) (alejamiento). El mismo mecanismo es **unilateral**, no bilateralmente atractor.

## 5. Interacción lejana y coeficiente de orden [T]

El cálculo O35 de Biot–Savart para gaussianas elípticas da, con \(S=a^2+b^2\), \(D_Q=a^2-b^2\):

\[
\boxed{f_d(\theta)=
-\frac{\gamma S}{\pi D_Q d^2}\left(1-\cos2\theta\right)
+o(d^{-2}),\qquad d\to\infty.}\tag{8}
\]

El error puede hacerse uniforme para \(\theta\) en un compacto, incluso tras derivadas angulares hasta segundo orden, por localización gaussiana y la expansión del núcleo en regiones separadas; el complemento se controla mediante las colas gaussianas. El autoacoplamiento se cancela en la diferencia de fases debido a que ambos núcleos tienen los mismos semiejes y circulación. **No usar (8) como igualdad a distancia finita.**

En particular:

\[
\frac{\partial^2 f_d}{\partial\theta^2}(0)
=-\frac{4\gamma S}{\pi D_Q d^2}+o(d^{-2}).\tag{9}
\]

Para todo \(d\) suficientemente grande, \(f_d''(0)<0\), por lo que existe \(\varepsilon_d>0\) con \(f_d(\theta)<0\) cuando \(0<|\theta|<\varepsilon_d\). Se acredita, así, una **región abierta unilateral de acercamiento** y otra de alejamiento, sin imponer un \(K\).

## 6. O36-T3: no-go de tasa exponencial uniforme cerca de la coincidencia [T/F]

Como \(E_{1:1}(0;\theta)=1-\cos(2\theta)=2\theta^2+O(\theta^4)\) y \(f_d(\theta)=O(\theta^2)\), entonces

\[
\dot E(0;\theta,d)=O(\theta^3),\qquad
\boxed{\frac{\dot E(0;\theta,d)}{E(0;\theta)}=O(|\theta|)\longrightarrow0.}\tag{10}
\]

**No-go O36-F1.** En un intervalo de parámetros de acercamiento que incluya ángulos \(\theta<0\) arbitrariamente próximos a \(0\), **no existe** una constante \(\lambda>0\) independiente de \(\theta\) para la que todos esos estados satisfagan ya en \(t=0\)

\[
\dot E(0;\theta,d)\le-\lambda E(0;\theta).
\]

Esto no prohíbe tasas dependientes del estado, ni atractores en otra configuración o clase de formas, ni una condición integral de convergencia más débil. Refuta únicamente esta **pretensión de atracción exponencial uniforme** para la familia y el observable declarados.

Al combinar (8) con \(\theta\to0\), la tasa relativa formal de primer orden del mecanismo unilateral cumple

\[
\frac{\dot E}{E}\sim
\frac{2\gamma S}{\pi D_Qd^2}\theta,
\]

negativa desde \(\theta<0\), positiva desde \(\theta>0\). El orden de los límites se controla mediante la expansión uniforme en \(\theta\), no mediante una extrapolación de la tabla numérica.

## 7. O36-T4: contracción finita y robusta, sin atractor global [T]

Sea un conjunto compacto de parámetros iniciales \(K\) en una región de datos lisos donde (i) \(E(0)>0\); (ii) \(\dot E(0)<0\); (iii) \(Q_i(0)\ne0\); (iv) \(d(0)>2(\sqrt{S_A(0)}+\sqrt{S_B(0)})\). Estas desigualdades estrictas definen un abierto; el teorema O36-T2/T3 y la interacción lejana garantizan que existen ejemplos y compactos no vacíos \(K\) contenidos en él.

Como \(E,\dot E,Q_i,d,S_i\) varían continuamente respecto de tiempo y datos iniciales para NS 2D suave, hay \(T_K>0\), \(\lambda_K>0\) tales que, para todos los datos de \(K\) y \(0\le t\le T_K\),

\[
\boxed{\dot E(t)\le-\lambda_K E(t),\qquad Q_i(t)\ne0.}\tag{11}
\]

Además, al escoger \(T_K\) menor que el horizonte de O31, cada una de las etiquetas conserva al menos \(75\%\) de su circulación en dos discos disjuntos. Se deduce \(E(t)\le E(0)e^{-\lambda_K t}\) **solo dentro de esa ventana temporal**.

*Demostración.* Por compacidad, \(\sigma:=\min_K[-\dot E(0)]>0\), \(E_{\max}:=\max_K E(0)>0\). Continuidad uniforme de los campos y de la evolución PDE sobre el compacto da un \(T_1>0\) en que \(\dot E(t)\le-\sigma/2\) y \(E(t)\le2E_{\max}\). Por tanto \(\dot E(t)\le-(\sigma/(4E_{\max}))E(t)\). Los no-ceros de \(Q\) y las desigualdades de concentración estrictas persisten en un intervalo común, que se intersecta con \(T_1\). QED.

**Advertencia epistemológica.** \(T_K\) y \(\lambda_K\) son existenciales, no límites numéricos a priori evaluados para todos los parámetros. Este teorema demuestra robustez de *acercamiento finito*, no atracción asintótica a la misma fase, ni identidad física común indefinida. Evitar llamar «atractor de sincronización» al resultado.

## 8. Horizonte de separación computable sin certificación de fase [T/E]

Para el ejemplo de O35 \(a=0.9,b=0.5,\gamma=1,\nu=0.02,d_0=6\), usamos la cota inicial de vorticidad

\[
M_0\le\frac{2\gamma}{2\pi ab},\qquad
\Gamma=2\gamma,\qquad U_0=\sqrt{\frac{2\Gamma M_{0,\mathrm{sup}}}{\pi}}=\frac2{\pi\sqrt{ab}}\approx0.94901672.
\]

O31 con \(k=2\), \(S_A(0)=S_B(0)=S=1.06\), acredita **concentración separada** mientras

\[
\boxed{4\sqrt{S+4\nu T}+6U_0T<d_0.}\tag{12}
\]

La raíz de igualdad es aproximadamente \(T_{\mathrm{geom}}=0.3217447464\) (unidades del modelo). Todo \(0\le T<T_{\mathrm{geom}}\) está garantizado por esta cota para conservar dos discos etiquetados disjuntos con \(75\%\) de circulación propia en cada uno.

**No** se concluye que \(\dot E<0\) en todo ese intervalo. Su horizonte debe calcularse por separado, mediante integración de NS con control de error o cotas independientes para la segunda derivada del observable.

## 9. Verificación numérica y falsadores [E/F]

Reutilizamos la integración exacta instantánea de O35 mediante (i) una integral unidimensional por transformada de Laplace y (ii) cuadratura Gauss–Hermite en dos dimensiones. Para \(d=6,a=0.9,b=0.5,\gamma=1\):

- \(\theta_B=-0.35\): \(\Psi=+0.70\), \(\dot\Psi\simeq-0.004750381\), \(\dot E\simeq-0.003060279\).
- \(\theta_B=+0.35\): \(\Psi=-0.70\), \(\dot\Psi\simeq-0.004750381\), \(\dot E\simeq+0.003060279\).
- Cuando \(|\theta_B|\to0\) a distancia fija, \(\dot\Psi\propto\theta_B^2\) y \(\dot E/E\to0\).

Estas cifras son **cuadraturas numéricas de la derivada inicial**, no una simulación temporal completa y no poseen certificación formal de error intervalar. El signo para separación suficientemente grande está cubierto por el teorema asintótico.

Falsadores obligatorios para una futura tesis de cierre estable: (a) fase cuadrupolar indefinida \(Q=0\); (b) orientación reflejada con alejamiento; (c) igualdad de radios y circulaciones con dinámica relativa distinta; (d) persistencia de fase sin persistencia de forma; (e) imposibilidad de repetición rígida exacta de toda vorticidad positiva viscosa, pues el segundo momento total crece \(4\nu\Gamma t\); (f) posibles momentos de orden superior que separan formas con igual cuadrupolo.

## 10. Juicio ontológico y obligación matemática [O/A]

**[O]** La diferencia propia puede reducirse mediante la comparación efectiva de estructuras dentro del flujo sin que ninguna de ellas «reconozca» a la otra. El marco común no borra las diferencias. Pero un **acercamiento unilateral** todavía no representa un **cierre propio autónomo**: debemos demostrar que una nueva relación es preservada o estabilizada por la evolución ante perturbaciones admisibles.

**[A]** Próxima prueba que realmente falta: hallar una región invariante de estados o una estructura de Lyapunov/contracción que permita continuar el acercamiento sin perder \(Q_i\ne0\) y separación distinguible durante un horizonte declarado, idealmente más allá de la existencia local. Alternativamente, establecer un no-go físico para tal región bajo el tipo de flujo y fronteras declarados. Explorar firmas de forma superiores, no solamente \(Q\), y comparar con DNS controlado de NS 2D. Nada de esto implica resolución de la regularidad 3D.

## 11. Antecedentes y bibliografía

- O28–O35: comparación modular, forma cuadrupolar, balances, certificados de concentración, simetrías, atractor de forma normalizada, acercamiento instantáneo.
- Núcleo Generativo Canónico: diferencia/comparación/residuo, complemento antes de ortogonalidad, no atribuir voluntad a una operación.
- Gallay, *Interaction of vortices in viscous planar flows*, arXiv:0908.2518, https://arxiv.org/abs/0908.2518.
- Gallay y Wayne, *Invariant manifolds and the long-time asymptotics of the Navier–Stokes and vorticity equations on R²*, arXiv:math/0102197, https://arxiv.org/abs/math/0102197.

**Estado final:** formalización matemática condicionada de *acercamiento unilateral robusto en tiempo finito*, más un obstáculo para la atracción exponencial uniforme alrededor de la fase idéntica, dentro de una familia explícita. No afirmar sincronización global ni descubrimiento físico original.
