# O54 — Primera verificación analítica de la condición relacional toroidal

**Fecha:** 21 de octubre de 2026. **Alcance:** modelo ideal, tres dimensiones, densidad constante, viscosidad cinemática positiva, sin fuerza volumétrica, toro sólido con frontera impermeable. No constituye una demostración de regularidad global de Navier–Stokes.

## 1. Hipótesis del programa y distinción entre niveles

O54 propone que dos recorridos del toroide conservan una identidad relacional mediante una referencia perpendicular común y la renovación de un múltiplo normalizador, cuya novedad permitiría continuidad de una configuración a la siguiente. Se trata de un **principio ontológico propuesto**, no de una ley dinámica deducida.

La relación geométrica local satisface Pitágoras; **la geometría no implica por sí misma incomprensibilidad, ecuación de momentum, condiciones de contorno ni regularidad global**. Un múltiplo de normalización elegido libremente tampoco equivale a demostrar conservación dinámica.

## 2. Geometría exacta

Parametrizamos el toro sólido con `0 ≤ ρ < a < R`, `θ, φ` angulares:

\[
X(\rho,\theta,\phi)=((R+\rho\cos\theta)\cos\phi,(R+\rho\cos\theta)\sin\phi,\rho\sin\theta).
\]

Con `s=R+ρ cosθ`, las direcciones `∂θ X` y `∂φ X` son ortogonales, y

\[
d\ell^2=d\rho^2+\rho^2d\theta^2+s^2d\phi^2,\qquad J=\rho s.
\]

Sobre una superficie `ρ=a`, la identidad pitagórica es `dℓ²=a²dθ²+s²dφ²`. Adviértase que la longitud de arco toroidal local usa `s`, no siempre `R`.

## 3. Prueba negativa: geometría no garantiza incomprensibilidad

Si se imponen dos velocidades angulares constantes `θ̇=α`, `φ̇=β`, con `ρ̇=0`, la divergencia es

\[
\nabla\!\cdot u=\frac{1}{J}\partial_\theta(J\alpha)= -\frac{\rho\alpha\sin\theta}{R+\rho\cos\theta}.
\]

Es no nula en general. Por ejemplo, con `ρ=R/4`, `θ=π/2` y `α=1 s⁻¹`, da `−0.25 s⁻¹`. Se mantienen ortogonalidad, toroide y posibilidad de normalizar, pero **falla la primera ecuación de Navier–Stokes incompresible**.

## 4. Prueba de reparación parcial: divergencia cero, pero momentum falla

Corrijamos a `θ̇=K/s`, `φ̇=Ω`, `ρ̇=0`, donde `K` tiene unidades de longitud/tiempo y `Ω` de 1/tiempo. Entonces `J θ̇=ρ K` y `∇·u=0`. En coordenadas cilíndricas `(s,z,φ)`, con `z=ρ sinθ`, esto equivale a

\[
u_s=-Kz/s,\quad u_z=K(s-R)/s,\quad u_\phi=\Omega s.
\]

Para flujo estacionario, `Δu_φ=0` pero la componente azimutal de aceleración convectiva es

\[
[(u\cdot\nabla)u]_\phi=-\frac{2K\Omega z}{s}.
\]

La ecuación azimutal de Navier–Stokes sin forzamiento exigiría

\[
\partial_\phi p=2K\Omega z.
\]

Si `K Ω ≠ 0` y `z ≠ 0`, esta derivada es constante no nula en `φ`, **imposible para una presión monovaluada y periódica al dar una vuelta completa**. Por ello este **ansatz particular** con ambos recorridos y esos ritmos no es una solución estacionaria sin fuerza, aunque su divergencia sea cero. Esto **no** descarta otras leyes de ritmo, flujos no estacionarios o la idea relacional general.

## 5. Control positivo de consistencia

Con `K=0`, `u=Ω s e_φ`, `p=Ω²s²/2` (densidad unitaria), se satisfacen exactamente `∇·u=0` y `∂_t u+(u·∇)u=−∇p+νΔu`. Es rotación rígida azimutal, suave en el toro sólido alejado del eje, con condición impermeable y contorno deslizante; **no** incluye el segundo recorrido dinámico y no resuelve el problema general en 3D.

## 6. Resultado, no extrapolación

**Resultado demostrado en este modelo:** referencia geométrica perpendicular y un normalizador común no bastan para las ecuaciones del flujo. Puede construirse un campo con dos recorridos y divergencia cero, pero el candidato sencillo falla momentum.

**Próximo paso interno a O54:** derivar —no suponer— una ley de evolución para el normalizador y sus novedades compatible simultáneamente con incomprensibilidad, ecuación de momentum, periodicidad, contorno y los tres ritmos del programa. Distinguir continuamente: geometría, representación normalizada, ley física y control de regularidad.
