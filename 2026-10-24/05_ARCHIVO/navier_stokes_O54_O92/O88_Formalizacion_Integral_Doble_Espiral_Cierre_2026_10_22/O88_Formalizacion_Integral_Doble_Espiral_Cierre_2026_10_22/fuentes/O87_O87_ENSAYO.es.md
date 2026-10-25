# O87 — Doble espiral, nodos móviles y desfase normalizado

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego** · 22 de octubre de 2026  
**Estado:** `[O]` lectura ontológica, `[T]` resultado exacto del modelo, `[E]` comprobación numérica, `[F]` falsador, `[A]` puente físico abierto.  
**Alcance:** modelo cinemático de transporte tangente sobre una superficie toroidal incomprensible **en dos dimensiones**. No se afirma que estos campos resuelvan Navier–Stokes 3D, ni que existan cuatro cápsulas materiales mínimas universales.

## 1. Planteamiento ontológico [O]

El usuario propone un aro que no gira en bloque: hay un recorrido alrededor del tubo (poloidal), un recorrido alrededor del aro (toroidal) y nodos que avanzan, con desfases internos entre vueltas como un resorte que arrastra la siguiente. La **identidad del cierre** podría residir en una referencia de fase compartida y transportable, no en la igualdad de los ángulos visibles ni en que cuatro partículas permanezcan en las mismas posiciones. El «múltiplo que normalizó» conserva relaciones acreditadas; **no identificarlo por definición** con los números de enrollamiento del presente ensayo.

## 2. Geometría y fase [D]

La superficie del toro se parametriza por

\[
X(\theta,\varphi)=((R+a\cos\theta)\cos\varphi,(R+a\cos\theta)\sin\varphi,a\sin\theta),\quad R>a>0.
\]

La métrica es `ds²=a²dθ²+(R+a cosθ)²dφ²`, con densidad superficial `J=a(R+a cosθ)`.

Sean `p,q` enteros primos entre sí; `p` es el número de vueltas alrededor del aro y `q` el número de vueltas alrededor del tubo de la curva parametrizada

\[
\varphi=p\chi,\qquad \theta=q\chi.
\]

La condición de cierre de la curva es `χ→χ+2π`, con `(Δφ,Δθ)=(2πp,2πq)`. La combinación

\[
\boxed{\Psi=p\theta-q\varphi}
\]

es constante sobre esta curva. Este hecho es cinemático/topológico; no fuerza a un flujo de Navier–Stokes a seguir la curva.

## 3. Una familia exacta de transporte de nodos [T]

Elegimos las velocidades angulares tangenciales

\[
\boxed{\dot\theta=\frac{q\kappa}{R+a\cos\theta},\quad
\dot\varphi=\frac{p\kappa}{R+a\cos\theta}.}
\]

**Incompresibilidad de superficie:** la divergencia intrínseca es

\[
\frac1J[\partial_\theta(J\dot\theta)+\partial_\varphi(J\dot\varphi)]=0,
\]

porque `J dotθ=aqκ` y `J dotφ=apκ` son constantes. No es un argumento de incomprensibilidad de una extensión tridimensional arbitraria.

Dado `θ=qχ`, `φ=pχ`, se deduce `dotχ=κ/(R+a cos(qχ))`; por tanto **los nodos no tienen velocidad angular constante**. Definimos la fase normalizada

\[
\boxed{\gamma=\chi+\frac{a}{qR}\sin(q\chi),\quad\dot\gamma=\frac\kappa R.}\tag{87.1}
\]

Para `R>a`, `dγ/dχ=1+(a/R)cos(qχ)>0`, de modo que la referencia es invertible y conserva información. **La fase uniforme es la referencia normalizada, no el ángulo geométrico `χ`.**

Tomando cuatro nodos con `γ_i(0)=γ_0+iπ/2`, obtenemos para todo instante:

\[
\boxed{\gamma_{i+1}(t)-\gamma_i(t)=\frac\pi2,\qquad p\theta_i-q\varphi_i=0.}\tag{87.2}
\]

Con `p=1`, `q=2`, además `γ(χ+π)=γ(χ)+π`; al invertir, se obtiene **dos parejas opuestas**:

\[
\boxed{\chi_3-\chi_1=\pi,\quad \chi_4-\chi_2=\pi,}\tag{87.3}
\]

mientras los espaciamientos **entre vecinos** `χ_2-χ_1` sí varían. Esto realiza exactamente el enunciado "nodos móviles, fase heredable, cierre por pares" **dentro del modelo elegido**.

**Paridad y enrollamiento no son lo mismo:** cuatro nodos corresponde a nuestra construcción C4; números `p,q` son vueltas topológicas y no se deduce que ambos deban ser pares. La alternancia de engranajes exteriores de O72 necesita un circuito par bajo *ese* contrato de acoplamiento, no bajo cualquier campo fluido.

## 4. Control adversarial: desacoplamiento SIN ruptura del fluido [T/F]

Alteremos sólo el ritmo poloidal:

\[
\boxed{\dot\theta=\frac{q[\kappa+\varepsilon\sin\varphi]}{R+a\cos\theta},\quad
\dot\varphi=\frac{p\kappa}{R+a\cos\theta}.}\tag{87.4}
\]

La divergencia superficial permanece exactamente cero: `J dotθ=aq(κ+εsinφ)` no depende de θ y `J dotφ=apκ` no depende de φ. Sin embargo,

\[
\boxed{\dot\Psi=p\dot\theta-q\dot\varphi
=\frac{pq\varepsilon\sin\varphi}{R+a\cos\theta},}
\tag{87.5}
\]

que en general no es cero. El cierre de fases `pθ−qφ=const` se pierde, **aunque el flujo sobre la superficie siga siendo suave, incompresible y las trayectorias existan para todo tiempo** (campo liso sobre toro compacto).

Esta es la distinción necesaria: **desacoplamiento de una referencia no equivale por sí mismo a ruptura material, desaparición de la unidad ontológica ni explosión matemática de Navier–Stokes**.

## 5. Comprobación reproducible [E]

Con `R=2`, `a=0.6`, `κ=0.8`, `p=1`, `q=2`, cuatro nodos de desfases normalizados consecutivos π/2, y perturbación ε=0.25, un integrador adaptativo y la inversión de (87.1) verifican:

- error de inversión de γ: < `2·10⁻¹⁵`;
- error respecto de la solución diferencial del modelo coherente: < `3·10⁻¹³`;
- error de desfases γ y de parejas opuestas: < `5·10⁻¹⁵`;
- variación máxima del desfase vecino geométrico `χ₂−χ₁−π/2`: aproximadamente `0.287672` rad (16.48°);
- en el modelo adversarial, deriva máxima de `Ψ` durante 14 unidades de tiempo: aproximadamente `1.25` rad;
- divergencia superficial cero por derivación; diferencia finita secundaria en 200 pares angulares < `10⁻⁹`.

Los resultados, trayectorias y gráficos están en `resultados/` y `graficos/`. Se regeneran mediante `python codigo/o87_verificar.py` con NumPy, SciPy y Matplotlib.

## 6. Puente medible hacia Navier–Stokes 3D [A]

Para una partícula realmente seguida en la superficie de un tubo aproximadamente toroidal de radios fijos, escribimos las **componentes físicas tangenciales** `v_pol` y `v_tor`. Entonces

\[
\boxed{\dot\Psi=p\frac{v_{\rm pol}}a-q\frac{v_{\rm tor}}{R+a\cos\theta}.}\tag{87.6}
\]

En un toro de radio variable, centro móvil y sección deformable aparecen términos geométricos adicionales; se necesitan definiciones de centro, eje, nodos y superficie transportada consistentes con los datos. En los ensayos O69, las razones de dos ritmos materiales no estuvieron exactamente bloqueadas. **No imponer que un vórtice genérico satisfaga (87.6)=0.**

Prueba física siguiente: extraer fases poloidal/toroidal de trazadores 3D, medir el defecto de cierre `Ψ(t)−Ψ(0)` y sus saltos, detectar desplazamiento de nodos como máximos de fase o regiones de interacción, y contrastar ese defecto con la vorticidad/estiramiento reales. Para afirmar regularidad universal, además debería derivarse una desigualdad de control dinámico que no se sigue de la conservación topológica de enrollamientos.

## 7. Resultado ontológico del ensayo

**Aceptable dentro del contrato:** el desfase coherente puede residir en una **fase normalizada común** y sus parejas, aunque las separaciones visibles y las velocidades de los nodos cambien. Esto materializa una parte de la narrativa "espiral sobre espiral" sin exigir unísono.

**No acreditado:** que todos los vórtices 3D sostengan la misma relación, que su pérdida produzca singularidad de NS, o que la regla de cuatro nodos sea físicamente mínima universal.
