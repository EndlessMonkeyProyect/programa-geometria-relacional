# O89 — La pérdida del múltiplo entero no es la pérdida de continuidad

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**22 de octubre de 2026 · Suplemento crítico tras O88**  
**Estatus:** [O] hipótesis ontológica, [T] prueba exacta, [E] comprobación reproducible, [F] refutación de una implicación concreta, [A] puente pendiente.

## 0. Tesis que se somete a ataque

La **tesis fuerte atacada** es «cuando dos canales de vorticidad dejan de admitir cualquier múltiplo entero exacto de sus ritmos, un fluido homogéneo necesariamente pierde continuidad y colapsa». Ésta es una interpretación física extrema de la intuición del usuario, **no** un teorema del núcleo ontológico ni una atribución obligatoria al autor.

Una formulación universal tendría que valer para toda solución suave de Navier–Stokes sin fuerzas. Mostraremos un contraejemplo *exacto* a esa formulación, con viscosidad uniforme y cuatro marcas materiales. El contraejemplo **no** desmiente el principio más amplio de reconstruibilidad relacional; muestra que un acoplamiento racional persistente no puede imponerse como condición necesaria para regularidad.

## 1. Campo exacto en un medio homogéneo [T]

En el toro tridimensional \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), con viscosidad constante \(\nu=1\), media cero y sin fuerza, tomamos

\[
\boxed{u(x,y,z,t)=\bigl(2e^{-t}\sin y+e^{-4t}\sin 2z,\;0,\;0\bigr).}\tag{89.1}
\]

Es incompresible: \(\nabla\cdot u=\partial_x u_x=0\). El término convectivo \((u\cdot\nabla)u=u_x\partial_xu=0\). Además, \(\partial_tu=\Delta u\), término a término. Por tanto satisface exactamente Navier–Stokes 3D para **todo** \(t\ge0\), con presión espacialmente constante. No es un cálculo de Galerkin ni una hipótesis de evolución.

Su vorticidad física es

\[
\boxed{\omega=\nabla\times u=(0,2e^{-4t}\cos 2z,-2e^{-t}\cos y).}\tag{89.2}
\]

Los dos canales de vorticidad, reconocibles por su dirección y su frecuencia espacial, tienen magnitudes máximas

\[
a(t)=2e^{-4t},\quad b(t)=2e^{-t},\quad \rho(t)=\frac{b(t)}{a(t)}=e^{3t}.
\tag{89.3}
\]

Así, \(\rho(0)=1\) y al tiempo

\[
\boxed{t_*=\frac{\ln 2}{6},\qquad\rho(t_*)=\sqrt2\notin\mathbb Q.}\tag{89.4}
\]

**Consecuencia exacta:** dos canales que al inicio admiten la referencia entera primitiva \(1:1\) dejan de admitir cualquier proporción de **enteros positivos** en ese instante. El medio sigue siendo uniforme y la solución es completamente regular. No ha ocurrido una singularidad. **Importante:** no se pierde el ritmo físico: cada canal sigue una ley exponencial exacta y su relación \(\rho(t)=e^{3t}\) permite reconstruir ambos. Lo que falla es la exigencia de *un múltiplo entero fijo*, no la posibilidad de comparar o transportar la información.

Como \(\rho(t)\) varía estrictamente, no existen dos enteros fijos positivos \(p,q\) tales que \(p\,a(t)=q\,b(t)\) en ningún intervalo abierto. Esto refuta una condición de *acoplamiento racional exacto persistente* impuesta a todos los canales de vorticidad.

## 2. Cuatro nodos transportados por el mismo flujo [T]

Para evitar que la comparación sean solamente amplitudes espectrales, elegimos cuatro **marcas materiales**, dos parejas antipodales en la dirección periódica \(x\):

\[
A_0(0)=(0,\pi/2,0),\ A_1(0)=(\pi,\pi/2,0),
\]
\[
B_0(0)=(0,0,\pi/4),\ B_1(0)=(\pi,0,\pi/4).
\tag{89.5}
\]

Como \(u_y=u_z=0\), las posiciones \(y,z\) de cada marca permanecen fijas y las fases **levantadas** de los desplazamientos en \(x\) son

\[
\theta_A(t)=2(1-e^{-t}),\qquad
\theta_B(t)=\frac{1-e^{-4t}}4.
\tag{89.6}
\]

Las velocidades iniciales guardan la razón \(2:1\), pero

\[
\frac{\dot\theta_A(t)}{\dot\theta_B(t)}=2e^{3t},
\quad\Psi(t)=\theta_A(t)-2\theta_B(t)
=2(1-e^{-t})-\frac12(1-e^{-4t}).\tag{89.7}
\]

\(\Psi(0)=\dot\Psi(0)=0\) y \(\dot\Psi(t)=2(e^{-t}-e^{-4t})>0\) para \(t>0\): el acoplamiento inicial \(2:1\) se pierde inmediatamente, sin romper la continuidad de las trayectorias. En \(t_*\), la razón instantánea es \(2\sqrt2\), irracional.

Las parejas \((A_0,A_1)\) y \((B_0,B_1)\) **siguen separadas por** \(\pi\) en la coordenada periódica. Hay pérdida de una sincronización entre parejas y conservación de otra relación dentro de cada pareja.

**Restricción de interpretación:** las marcas son *trazadores* de un flujo de cizalla; no son los cuatro nodos constitutivos de un tubo vorticial toroidal ni un resorte de dos giros. El ejemplo refuta la pretensión universal «toda sincronización entera rota provoca singularidad». **No refuta** un teorema futuro que se formule exclusivamente para una clase de estructuras realmente toroidales y cuyas hipótesis se comprueben en la velocidad y la vorticidad.

## 3. Cota física exacta [T]

Con promedio espacial normalizado,

\[
\langle|\omega|^2\rangle=2e^{-2t}+2e^{-8t},\qquad
\langle|\nabla\omega|^2\rangle=2e^{-2t}+8e^{-8t}.
\tag{89.8}
\]

Aquí \(\omega\cdot S\omega\equiv0\), por lo que

\[
\frac12\frac d{dt}\langle|\omega|^2\rangle
=-\langle|\nabla\omega|^2\rangle.
\tag{89.9}
\]

Incluso la condición de continuación por gradiente está verificada explícitamente:

\[
\|\nabla u(t)\|_{L^\infty,\mathrm{op}}
\le 2e^{-t}+2e^{-4t},\qquad
\boxed{\int_0^\infty\|\nabla u(t)\|_\infty dt\le\frac52<\infty.}\tag{89.10}
\]

Por tanto, el ejemplo no contiene colapso de velocidad, vorticidad ni del mapa material.

## 4. Qué hay que conservar del planteamiento ontológico [O/A]

1. **Dos giros y cuatro nodos:** O88 define y reconstruye una realización toroidal con movimiento de nodos y diferencia de fase. Eso está demostrado **dentro de esa realización**.
2. **Una proporción entera no es una relación universal:** (89.4) y (89.7) demuestran que la ley viscosa puede disolver una proporción entera sin producir singularidad.
3. **El «uno» aritmético no es regularidad física:** \(\gcd(p,q)=1\) expresa primitividad de una pareja de enteros; no impone retorno físico, ni crecimiento controlado de \(\omega\).
4. **La pérdida de un canal no exige pérdida de reconstruibilidad:** el flujo (89.1) evoluciona mediante una regla continua y exactamente invertible sobre cualquier tiempo finito, aunque la referencia entera original no permanezca sincronizada.
5. **No definamos «cierre» como «cualquier información suficiente para reconstruir la solución»:** esa definición haría imposible refutar el programa y no generaría cotas independientes. Definir previamente un observable \(H[u]\) y su falla medible es esencial.

## 5. Dos preguntas con poder real de refutación [F/A]

**Prueba F89-1 (necesidad del cierre):** definir, antes de resolver la PDE, un cierre propio observable \(C[u]\) en una unidad vorticial concreta; comprobar si existe solución suave en la que \(C\) falle y aun así la velocidad conserve regularidad. El ejemplo (89.1) ya refuta \(C=\) «todas las razones entre canales son racionales», pero no cualquier otro \(C\).

**Prueba F89-2 (suficiencia del cierre):** demostrar o refutar que \(C[u]\) fuerza una cota física \(\int_0^T\|\nabla u\|_\infty dt<\infty\). No basta asegurar la identidad de \(C\): se necesita la desigualdad.

**Próximo ensayo O90, sin introducir nueva ontología:** definir nodos como subconjuntos de vorticidad de un mismo tubo material, elegir una diferencia de fase medible y una holonomía de la doble espiral, y comparar con los datos de O69. Aceptar la hipótesis únicamente si ese observable se deriva de la dinámica y su control implica una norma de continuación; rechazar la versión fuerte si aparece pérdida de cierre y evolución regular.

## 6. Alcance lógico y antecedentes

La existencia de un caso suave con pérdida de una sincronización 1:1/2:1 demuestra que **sincronía racional fija no es necesaria** para la regularidad de Navier–Stokes 3D. No demuestra que las singularidades 3D sean posibles o imposibles. El flujo de cizalla tiene dinámica espacial de menor complejidad que un vórtice toroidal con estiramiento, precisamente por eso ofrece un falsador limpio de afirmaciones *universales* pero no del modelo geométrico especializado.

Fuentes internas pertinentes: O68 (normalizador de dos giros, matrices unimodulares), O69 (dos giros trazados en flujo viscosa, razones no rígidas), O79 (fases y transferencias), O86 (balance de enstrofía), O88 (doble espiral, nodos móviles y reconstrucción). No se sustituye ni reescribe ninguna de ellas.
