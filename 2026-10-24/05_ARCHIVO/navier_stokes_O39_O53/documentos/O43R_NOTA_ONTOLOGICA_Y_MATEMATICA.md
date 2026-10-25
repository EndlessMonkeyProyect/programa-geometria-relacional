# O43R — Resto heredado, vueltas del toroide y suficiencia dinámica
**Programa de Geometría Relacional · suplemento independiente · 20 de octubre de 2026**

## 1. Punto de partida ontológico

La unidad del anillo no es una imagen congelada. Cada vuelta vuelve a comparar sus relaciones con una referencia compartida. Una vuelta puede completar una unidad de referencia y dejar un segmento pendiente, que orienta la siguiente vuelta. La expresión «el resto es uno» se interpreta, aquí, como **un segmento de una partición normalizada**, es decir, `1/N` de la unidad, y no como una unidad completa.

El normalizador heredado expresa la escala en la que ese resto se puede comparar con relaciones anteriores. La hipótesis física —aún abierta— es que existe un observable del flujo que porta esa memoria relacional.

## 2. Solo dos radios geométricos

Para un toroide de sección circular, `R > a > 0`, con `R` radio mayor y `a` radio del tubo, la superficie se parametriza por dos ángulos (no son radios adicionales):

\[
\mathbf{x}(\theta,\varphi)=((R+a\cos\theta)\cos\varphi,(R+a\cos\theta)\sin\varphi,a\sin\theta).
\]

`φ` recorre el anillo mayor (dirección toroidal) y `θ` la circunferencia del tubo (dirección poloidal). La métrica sobre esa superficie es

\[
 ds^2=a^2\,d\theta^2+(R+a\cos\theta)^2\,d\varphi^2.
\]

No puede obtenerse **una ley de velocidades o fases** solo de `R` y `a`. Las velocidades angulares requieren datos dinámicos.

## 3. Resto discreto heredado: definición y teorema

Escogida una partición en `N` segmentos, se describe el resto por

\[
 \rho_n = \frac{r_n}{N},\qquad r_n\in\{0,1,\ldots,N-1\}.
\]

Si cada vuelta adelanta `k_n` segmentos en la referencia del tubo, la recurrencia puramente aritmética es

\[
\boxed{r_{n+1}=(r_n+k_n)\bmod N.}
\]

Con incremento fijo `k`, se cierra el resto después de `q=N/gcd(N,k)` vueltas (período mínimo del estado de resto). Si `r_0=1`, el resto inicial es `1/N`: esta es una posible traducción precisa de «queda uno».

**Ejemplo exacto:** `N=5`, `r_0=1`, `k=2`: los residuos son `1,3,0,2,4,1`, con período 5. El paso por `0` expresa cierre en esa partición, no una singularidad física ni destrucción del flujo.

### Cambio de normalizador

Si surge otro denominador `m`, la extensión racional mínima común es `N'=mcm(N,m)`. El resto antiguo se **transporta exactamente** como

\[
 r'=(N'/N)r,\quad r'/N'=r/N.
\]

Ejemplo: `1/5=6/30` al ampliar desde `N=5` a `N'=mcm(5,6)=30`. Una nueva contribución de `1/6=5/30` da `(6+5)/30=11/30` antes de tomar el módulo. **Conservar la referencia no exige que el numerador heredado continúe siendo uno**.

## 4. Versión continua: retorno de Poincaré

Para una trayectoria del flujo cuya coordenada toroidal avanza una vuelta y puede seguirse sin ambigüedad, sean `t_n` los instantes en que el ángulo toroidal desenrollado `φ` crece `2π` desde la sección anterior. Definimos

\[
\alpha_n=\frac1{2\pi}\int_{t_n}^{t_{n+1}}\dot\theta(t)\,dt,\qquad
\boxed{\rho_{n+1}=\{\rho_n+\alpha_n\}},
\]

donde `{x}=x-floor(x)` es la parte fraccionaria y `ρ` representa el resto de fase poloidal. Esta es una **definición cinemática** de un resto transportado: no demuestra que un campo de Navier–Stokes mantenga una partición fija ni un cierre estable.

En un modelo ilustrativo con velocidades angulares constantes `dot φ=Ω_t>0` y `dot θ=Ω_p`, cada vuelta da `α=Ω_p/Ω_t`. Si `α=p/q` irreducible hay retorno exacto de fase al cabo de `q` vueltas; si `α` es irracional, no hay retorno exacto para ningún número finito de vueltas, aunque el resto siempre queda definido.

**Contraejemplo de suficiencia geométrica:** manteniendo idénticos `R,a`, podemos elegir `Ω_p/Ω_t=2/5` o `Ω_p/Ω_t=1/√2`. Cambia el mapa de retorno aunque la geometría sea idéntica. Esta demostración es cinemática, no dos soluciones verificadas de Navier–Stokes.

## 5. Estiramiento y comparación con O43

Bajo hipótesis de un tubo material ideal, incompresible, con sección aproximadamente circular y volumen constante:

\[
 V=2\pi^2Ra^2\quad\Rightarrow\quad Ra^2=C,\qquad
 \frac{\dot a}{a}=-\tfrac12\frac{\dot R}{R}.
\]

Si además la circulación `Γ` del mismo tubo material se conserva y se usa una vorticidad media de sección `\bar\omega=Γ/(πa²)`, entonces

\[
\frac{\dot{\bar\omega}}{\bar\omega}=\frac{\dot R}{R}.
\]

Son identidades **condicionales**; no modelan por sí solas la difusión viscosa, la sección deformada, mezcla entre tubos ni concentración máxima. La variable de resto `ρ` no aparece en estas identidades. Para demostrar que `ρ` modera el estiramiento hace falta derivar una ley de acoplamiento desde las ecuaciones de movimiento y contrastarla.

Atención: el desfase espectral `δ=arg(c₂)-2arg(c₁)` de dos armónicos azimutales —invariante frente a cambios del origen angular— **no es automáticamente el mismo objeto** que el resto de fase de una trayectoria `ρ` en un retorno de Poincaré. Esta identificación necesita una función de observación y una prueba.

## 6. Ensayo falsable propuesto

1. En datos tridimensionales de un anillo vorticial, estimar `R(t),a(t)` y definir una sección de retorno robusta para trayectorias materiales cerca del núcleo.
2. Medir `ρ_n` de cada trayectoria usando fases **desenrolladas**, y por separado el desfase espectral `δ(t)`; no confundirlos.
3. Comparar dos campos iniciales suaves y libres de divergencia, con igual `R,a`, energía y distribución de magnitudes modales cuando sea posible, pero distinta fase relativa. Mantener controles de resolución espacial, paso temporal, conservación de masa y balances de energía y enstrofía.
4. Medir la producción vorticial `P(t)=\int \omega\cdot(\omega\cdot\nabla)u\,dV` y la disipación viscosa `D(t)=\nu\int |\nabla\omega|^2\,dV` (sobre un dominio periódico o con condiciones de frontera compatibles), junto con cambios de `R,a,ρ,δ`.
5. Falsador A: si el supuesto resto físico no puede definirse de modo robusto ante cambios de sección/origen o resolución, falla la correspondencia propuesta. Falsador B: si estados con los mismos comparadores propuestos exhiben evoluciones distintas de la cantidad que se pretende predecir, el comparador no es dinámicamente suficiente.

## 7. Estado epistemológico

- **Derivado:** regla de resto módulo `N`, transporte por `mcm`, geometría de los dos radios y condicional de volumen-circulación.
- **Definido:** retorno de Poincaré de fase poloidal en cada vuelta toroidal.
- **Contraejemplo cinemático:** dos movimientos con idénticos radios pueden tener restos distintos; los radios solos no fijan la dinámica.
- **Hipótesis por comprobar:** el resto ontológico se observa como fase transportada en el anillo; ese dato contribuye a predecir la producción vorticial; existe un mecanismo de redistribución que evita concentraciones ilimitadas.
- **No demostrado:** evolución temporal de un anillo Navier–Stokes concreto, ruptura/reconexión topológica, control universal del estiramiento, regularidad global 3D.

Este suplemento es **independiente**. No modifica O39–O43 ni la Imagen Total.
