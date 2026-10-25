---
title: "O50 — Desfase material, deformación del aro y sincronización de ritmos"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-20"
status: "Teoremas cinemáticos exactos con verificadores; no constituye solución no forzada de Euler/NS ni prueba de regularidad"
parents: ["MF-43", "O25", "O27", "O39", "O43R", "O44", "O45", "O47", "O48", "O49"]
---

# O50 — La comparación interior–exterior durante el avance y la deformación de un aro

## 0. Dictamen breve

**[T]** Construimos una familia explícita de campos axisimétricos incompresibles, suaves en un entorno toroidal, cuya sección se traslada y se deforma conservando las superficies materiales normalizadas. Dos trayectorias inicialmente situadas a diferentes radios de núcleo pueden estar encerradas en la *misma unidad geométrica* y acumular desfase material. **Cerrar la frontera no equivale a sincronizar todos los ritmos.**

**[T]** En la subfamilia de perfil lineal, todas las trayectorias tienen el mismo ritmo en la referencia normalizada incluso cuando se traslada o deforma la sección: existe un ejemplo exacto de **cierre dinámico por isocronía**, sin imponer velocidades instantáneas interiores y exteriores iguales.

**[F]** En una subfamilia ligeramente no lineal, permanecen cerradas todas las superficies materiales, pero el desfase aumenta linealmente con el conteo de vueltas de referencia. Es un contraejemplo a la implicación cinemática `frontera que se sostiene → sincronización de todas las fases`.

**[A]** No está demostrado que Navier–Stokes 3D seleccione universalmente el subrégimen isócrono, que la sincronización implique cotas de vorticidad ni que el avance axial compense todo desfase. La familia construida es **cinemática**, no una solución demostrada de las ecuaciones de momento de Euler ni de Navier–Stokes sin fuerza externa.

## 1. Narrativa, preservando la ontología

Una singularidad relacional puede sostener su unidad al cambiar el espejo, su escala o su foco. El desplazamiento habilita comparaciones entre ritmo del frente axial, giro de secciones materiales y diferencia entre sus partes. El modelo no convierte el foco interno en observador exterior ni confunde la singularidad ontológica con `blow-up` del PDE. La pregunta de O50 es qué comparador distingue la **continuidad de frontera** de la **sincronización de fases**.

**Definiciones:** `frontera cerrada` = una superficie material que no es atravesada por trazadores; `ciclo` = retorno de fase desenrollada a un múltiplo entero de `2π`; `sincronización` = diferencia de fases desenrolladas permanece constante o en una banda preregistrada (no simplemente fase módulo `2π`); `isocronía transversal` = un mismo período para todas las órbitas de una familia; `avance relativo` = desplazamiento axial menos un fondo físico definido, si existe.

## 2. Coordenadas naturales del anillo [T]

Para flujo suave axisimétrico sin swirl, con coordenadas cilíndricas `(r, φ, z)` y `r>0`, define la variable de área meridiana

\[
 w=\frac{r^2}{2},\qquad dw=r\,dr.
\]

La condición de incomprensibilidad es

\[
 \frac{1}{r}\partial_r(r u_r)+\partial_z u_z=0,
\]

que equivale a `∂_w(r u_r)+∂_z u_z=0`. Por ello existe función de corriente local `ψ(w,z,t)` tal que

\[
\boxed{\dot w=r u_r=-\partial_z\psi,\qquad \dot z=u_z=\partial_w\psi.}\tag{O50.1}
\]

Esta transformación identifica el plano meridiano como área canónica sin declarar que su coordenada `w` sea una dimensión física adicional.

## 3. Aro móvil y deformable [D/T]

Fijemos `R>0`, `w0=R²/2`, `a(t),b(t)>0` con `a(t)b(t)=C>0`; `Z(t)` es la posición axial de referencia, `U=dot Z` y `h=dot a/a=-dot b/b`. Para trayectorias de un entorno toroidal donde `w>0`, pongamos

\[
 s=\frac{(w-w_0)^2}{a(t)^2}+\frac{(z-Z(t))^2}{b(t)^2}, \quad
 \boxed{\psi=Uw-h(w-w_0)(z-Z)+C\,\Omega(t)\left(\frac{s}{2}+\frac{\varepsilon s^2}{4}\right).}\tag{O50.2}
\]

Aquí `ε≥0` es el parámetro de perfil radial, *no* la profundidad discreta `ε` de la ontología canónica. Se eligió el mismo símbolo sólo en la ecuación breve; en implementación se llama `eps_profile`, y en otros módulos debe distinguirse.

Derivando la función de corriente:

\[
 \boxed{\begin{aligned}
 \dot w&=h(w-w_0)-\frac{C\Omega(t)}{b^2}(1+\varepsilon s)(z-Z),\\
 \dot z&=U-h(z-Z)+\frac{C\Omega(t)}{a^2}(1+\varepsilon s)(w-w_0).
 \end{aligned}}\tag{O50.3}
\]

No existe fuente de compresión: `∂_w dot w+∂_z dot z=0` exactamente. Las identidades `a'=ha`, `b'=-hb`, `Z'=U` dan

\[
\boxed{\frac{ds}{dt}=0.}\tag{O50.4}
\]

Todas las secciones `s=const` son superficies materiales móviles y deformables. El volumen del toroide `s≤s0` vale `2π² R?` sólo para secciones circulares en `(r,z)`, no para nuestras elipses exactas en `(w,z)`. En nuestro contrato la medida espacial exacta del tubo es `2π·(π a b s0)=2π² C s0`, constante: `dV=2π dw dz`. No sustituir esta geometría de áreas por `2π² R a²` sin conversión correcta entre radios.

**Extensión física global cinemática:** se puede multiplicar la función de corriente anterior por una función de corte suave de `s` igual a uno en `s≤1` y cero en `s≥3/2`. Escogiendo `w0>a(t)√(3/2)`, el soporte queda lejos del eje `r=0`, y el campo inducido es suave, axisimétrico, de divergencia cero y de soporte compacto en cada instante. Esta extensión coincide exactamente con (O50.2) en las trayectorias ensayadas `s≤0.81`. Sigue sin demostrar la ecuación de momento no forzada.

## 4. Teorema de sincronización y su contraejemplo [T/F]

En coordenadas normalizadas `q=(w-w0)/a`, `p=(z-Z)/b`, escribimos `q=√s cos θ`, `p=√s sin θ`. De (O50.3) se obtiene

\[
\boxed{\dot\theta=\Omega(t)(1+\varepsilon s),\qquad\dot s=0.}\tag{O50.5}
\]

Una vuelta de referencia está definida por `∫Ω(t)dt=2π`. Para dos trazadores con radios materiales `s_1,s_2` y fases iniciales iguales:

\[
\boxed{\Delta\theta(t)=\varepsilon(s_2-s_1)\int_0^t\Omega(\tau)d\tau.}\tag{O50.6}
\]

A las `N` vueltas de referencia:

\[
\boxed{\frac{\Delta\theta_N}{2\pi}=N\varepsilon(s_2-s_1).}\tag{O50.7}
\]

Consecuencias:

- **Isocronía (`ε=0`):** todas las órbitas regresan juntas, aun con avance `U(t)` variable y deformación `a,b` variables.
- **Desfase (`ε≠0`, `s1≠s2`):** la misma superficie global permanece material y cerrada, pero los ritmos de dos capas son distintos.
- **Misma capa, lados opuestos:** dos partículas con fases iniciales separadas por `π` mantienen exactamente ese desfase en coordenadas normalizadas. El interior y exterior *de una misma órbita* pasan sucesivamente por los dos lados y comparten el período; no confundirlas con dos capas diferentes del núcleo.
- **No-go de sincronización automática:** si el reloj acumula vueltas ilimitadas, `Δθ` desenrollada permanece acotada para todas las capas ensayadas únicamente si el perfil `Ω(1+ε s)` no depende de `s`. Puede haber retornos de fase módulo `2π` ocasionales para razones racionales, sin bloqueo continuo de fase.

**Corolario:** `cierre geométrico`, `cierre de flujo`, `retorno de fase`, `sincronización de capas` y `regularidad de PDE` son cinco predicados no equivalentes. O49 establece una identidad de frontera estacionaria; O50 distingue cómo evolucionan sus trayectorias materiales.

## 5. Laboratorio numérico reproducible [E]

El verificador usa `R=1.5`, `w0=R²/2`, `a0=0.20`, `b0=0.24`, `a=a0 exp(0.18 sin(0.9t))`, `b=b0 exp(-0.18 sin(0.9t))`, `Ω=2π(1+0.12 cos(0.7t))`, `U=0.32+0.04 sin(0.65t)` y `Z=∫Udt`.

Dos capas materiales `ρ1=0.38`, `ρ2=0.90`, `s_i=ρ_i²`; se comparan `ε=0` y `ε=0.20`. El integrador `solve_ivp` valida las soluciones cerradas analíticas y desenrolla las fases materiales a cada vuelta del reloj de referencia.

| Vueltas de referencia | ε=0: desfase en vueltas | ε=0.20: desfase en vueltas |
|---:|---:|---:|
| 1 | 0 | 0.13312 |
| 2 | 0 | 0.26624 |
| 3 | 0 | 0.39936 |

**48/48 comprobaciones superadas**: divergencia simbólica, conservación material de `s`, evolución analítica de fase, reloj monótono, área exacta, `w>0`, error ODE vs solución cerrada, control de órbitas antipodales, invariancia galileana del avance de fondo y diferencia de velocidades instantáneas interior/exterior. En `resultados_o50.json` se preservan diagnósticos de residuo y tiempos medidos.

Control regresivo **O49** vuelto a ejecutar: `PASS 7 grupos algebraicos/modelo + 3 cuadraturas`. Se reutiliza su conclusión, no se modifica.

## 6. Respuesta al planteamiento del autor

**Sí puede existir una sincronización en la que el desplazamiento del frente, la sección que gira y sus escalas distintas sean compatibles en una unidad móvil.** O50 exhibe una realización cinemática explícita con deformación continua e isocronía (`ε=0`). **Pero ni avance axial ni incomprensibilidad obligan a esa isocronía:** cambiar `ε` mantiene cerradas las superficies y produce desfase, y modificar `U` sin modificar las fases no altera su sincronización relativa dentro del modelo cinemático. Una relación física entre `U` y el giro debe surgir de la ley de movimiento (Biot–Savart/presión/viscosidad), no de escoger coordenadas.

Por ello la frase defendible es: *la regularidad del mecanismo relacional es compatible con una sincronización transversal de fases, pero la sincronización debe demostrarse como una consecuencia, o establecerse como una hipótesis física falsable, y además controlar la vorticidad*. El propio contraejemplo cinemático es suave y libre de divergencia aun con desincronización: no debe confundirse isocronía con necesidad de regularidad de todos los campos.

## 7. Siguiente prueba física que realmente cerraría el puente [A]

1. Definir una familia **no forzada** de anillos Navier–Stokes 3D a partir de un campo inicial suave, aislado, y aplicar convergencia espacial-temporal. No sustituir por una función de corriente elegida.
2. Extraer la velocidad del frente `U_rel` respecto del fluido lejano, radio/sección del núcleo y presión; no elegir `U` para forzar cierre después de observar trazadores.
3. Sembrar marcadores pasivos en capas de vorticidad bien definidas y seguir **al menos tres vueltas materiales completas** o declarar el evento ausente. En viscosidad, la superficie de nivel de vorticidad no es automáticamente material.
4. Medir `Ω(ρ,t)` con fases desenrolladas en un marco corregido por traslación y deformación; registrar si la deriva de fase entre capas crece.
5. Comparar `Δθ`, transferencia, producción de vorticidad `P` y disipación `D` para comprobar si el bloqueo de fases impone alguna cota uniforme nueva.
6. Probar adversarialmente que dos condiciones iniciales indistinguibles por el comparador tienen o no la misma evolución, según O41-T1. El criterio final de regularidad necesita un control a priori aplicable a la clase declarada, no retornos visuales.

## 8. Genealogía y bibliografía

Internos: O39 (balance estiramiento/disipación/foco móvil y falsadores), O43R (mapa de retorno de Poincaré de fase), O44 (trazadores sin vueltas completas), O45 (relación tres ritmos y reloj de referencia), O47/O48 (cierre de observables y contraejemplos), O49 (frontera de corriente y avance axial).

Externo: Masroor, E. & Stremler, M. A., *On the Topology of the Atmosphere Advected by a Periodic Array of Axisymmetric Thin-cored Vortex Rings*, Regular and Chaotic Dynamics 27 (2022), 183–197, DOI `10.1134/S1560354722020046`: estudia trayectorias de partículas en el marco de anillos Euler y cambios topológicos del conjunto atrapado. No prueba ni afirma el teorema de O50.

**Estado O50:** teorema cinemático sectorial exacto; validación numérica de ecuaciones cerradas; contraste adversarial positivo/negativo; puente específico a anillo NS no forzado todavía abierto. **No es una solución de la regularidad global de Navier–Stokes 3D.**
