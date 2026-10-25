---
title: "O49 — Avance axial del anillo, diferencia interior–exterior y cierre en el espejo móvil"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-20"
status: "Análisis físico-matemático documentado: cierre exacto bajo régimen estacionario ideal; no-go de compensación universal; puente NS general abierto"
parents: ["O25", "O39", "O41", "O43R", "O44", "O45", "O47", "O48"]
---

# O49 — ¿El avance axial compensa la diferencia entre el interior y el exterior del aro?

## 0. Respuesta falsable

**Resultado principal [T, bajo hipótesis].** Sí existe una condición *exacta de equilibrio de flujo* para un anillo axisimétrico de Euler que se traslada sin cambiar de forma: la función de corriente en el marco del anillo es constante en la frontera cerrada de su núcleo. Si dos puntos de esa misma frontera están en el lado interior y exterior de una sección meridiana,

\[
U = \frac{2(\psi_e-\psi_i)}{r_e^2-r_i^2},\qquad
\int_{r_i}^{r_e}r(u_z-U)\,dr=0.
\]

La velocidad de avance es el promedio radial ponderado de la velocidad axial entre los puntos de frontera. **Ésta es una forma precisa de 'compensación' de flujo relativo**, no de velocidades de giro o fases iguales. La relación es necesaria para un núcleo de frontera estacionaria en el marco que traslada al aro y no selecciona por sí sola cuál es el valor de U: hay que resolver el campo y su distribución de vorticidad.

**No-go [F].** Ni las circunferencias interior/exterior ni los radios R,a obligan a una ley universal de sincronización poloidal, ni a una razón fija entre traslación y giro de la sección. La velocidad autoinducida depende del perfil del núcleo. En Euler axisimétrico sin giro azimutal pueden aparecer estiramientos/filamentos debidos a la diferencia de velocidades núcleo-periferia: *ninguna compensación universal recupera automáticamente la forma*. Incluso cuando hay regularidad global en una subclase, puede existir reorganización geométrica.

**Abierto [A].** Un teorema que fuerce este cierre para *Navier–Stokes viscoso general* y que de ahí produzca una cota de regularidad global no se ha demostrado. Un anillo no es una superficie material exacta para la vorticidad cuando ν>0 porque ésta difunde.

## 1. Ontología, lenguaje y tres nociones distintas

El espejo móvil es una *referencia de comparación*, no una superficie física adicional. La singularidad ontológica del programa no es una singularidad analítica. Separar: (1) avance axial del anillo; (2) recirculación del fluido en planos meridianos, que atraviesa las zonas interior y exterior; (3) flujo azimutal alrededor del eje de simetría (*swirl*), que puede ser cero mientras el anillo avanza. No deducir una diferencia de períodos materiales simplemente de longitudes 2π(R±a): sin giro azimutal u_θ=0 y las partículas mantienen su ángulo azimutal.

El objetivo relacional es evaluar si el movimiento relativo en el marco del aro posee un cierre definido, y si ese cierre está asociado con controles físicos cuantitativos.

## 2. Teorema de cierre de flujo en el marco del aro [T]

En coordenadas cilíndricas (r,θ,z), para un flujo suave axisimétrico incompresible con u_θ=0, existe la función de corriente de Stokes ψ tal que

\[
 u_r=-\frac1r\,\partial_z\psi,\qquad u_z=\frac1r\,\partial_r\psi.
\]

Si el anillo se traslada sin cambiar su estructura meridiana con velocidad constante U en la dirección z, en z'=z−Ut el flujo relativo es (u_r,u_z−U), generado por

\[
\psi_U(r,z')=\psi(r,z)-\frac12Ur^2.
\]

Sobre cualquier línea de corriente cerrada **fija en ese marco**, ψ_U es constante. Sean (r_i,z_0), (r_e,z_0) dos intersecciones interior y exterior de **la misma** línea de corriente con el mismo plano meridiano z'=z_0. Entonces ψ_U(r_i,z_0)=ψ_U(r_e,z_0), y

\[
\boxed{U=\frac{2(\psi_e-\psi_i)}{r_e^2-r_i^2}}.\tag{O49.1}
\]

Como ψ_e−ψ_i=∫_{r_i}^{r_e}r u_z(r,z_0)dr, equivale a

\[
\boxed{\int_{r_i}^{r_e} r(u_z-U)\,dr=0,\qquad
U=\frac{\int_{r_i}^{r_e} r u_z\,dr}{\int_{r_i}^{r_e}r\,dr}.}\tag{O49.2}
\]

Ésta es la anulación exacta del flujo **axial relativo total**, ponderado por el Jacobiano cilíndrico, a través de la banda radial limitada por los dos puntos. Es balance firmado: el flujo positivo en una parte se compensa con flujo negativo en otra *en el marco que se mueve con el anillo*. Si r_i=R−a y r_e=R+a, la identidad se reduce a

\[
\boxed{U=\frac{\psi_e-\psi_i}{2Ra}.}\tag{O49.3}
\]

**No interpretar:** (O49.1) no expresa el mismo tiempo de vuelta de dos partículas ni que el transporte vórtice/fluido sea idéntico. Las partículas que dan vueltas meridianas recorren sucesivamente posiciones interiores y exteriores; sus fases deben medirse con trazadores. Tampoco la condición de contorno y la incomprensibilidad sustituyen la ecuación de Euler para seleccionar una solución física. Las construcciones estacionarias de Fraenkel–Berger y su marco móvil usan exactamente este tipo de función de corriente.

**Objetividad galileana.** Si el sistema entero recibe una traslación axial uniforme V, ψ↦ψ+V r²/2 y U↦U+V; ψ_U no cambia. Por ello una ley en términos de U sin sustraer la velocidad del fluido lejano es dependiente del observador. Para ensayos físicos emplear U_rel=U−u_∞.

## 3. Equilibrio cinemático no implica ecuación del fluido [E]

Control ilustrativo (NO solución afirmada de Euler/NS):

\[
\psi=\tfrac12Ur^2+A[(r-R)^2+z^2].
\]

Las curvas (r−R)²+z²=a² son cerradas en el marco móvil. Se obtiene

\[
 u_r=-2Az/r,\qquad u_z=U+2A(r−R)/r.
\]

En la intersección interior r_i=R−a se tiene u_z−U<0 y en la exterior r_e=R+a, u_z−U>0 para A>0. Su balance ponderado es cero exactamente. La prueba por cuadratura reproduce 0 para 17, 257 y 8193 puntos; es comprobación de la identidad cinemática, no validación física de esta ψ como solución estacionaria de la ecuación de impulso.

## 4. Cuánto se sincronizan avance y giro en un anillo de núcleo delgado [F/modelo]

Para el modelo clásico de anillo delgado con núcleo de vorticidad aproximadamente uniforme (a/R≪1), circulación Γ y radio mayor R, la expresión asintótica es

\[
U_{\rm sol}\simeq\frac{\Gamma}{4\pi R}\left(\log\frac{8R}{a}-\frac14\right).
\]

Para el modelo de núcleo hueco, Fetter obtiene

\[
U_{\rm hueco}\simeq\frac{\Gamma}{4\pi R}\left(\log\frac{8R}{a}-\frac12\right),
\quad U_{\rm sol}-U_{\rm hueco}=\frac{\Gamma}{16\pi R}.
\]

Así, la velocidad NO depende exclusivamente de la diferencia de circunferencias interior–exterior: el perfil del núcleo modifica la velocidad, incluso a R,a,Γ fijados.

En la aproximación del núcleo uniforme y plano, la velocidad angular poloidal representativa en el borde del núcleo es Ω_p≈Γ/(2πa²). Por tanto

\[
\boxed{\frac{U_{\rm sol}}{a\Omega_p}\simeq\frac{a}{2R}\left(\log\frac{8R}{a}-\frac14\right).}\tag{O49.4}
\]

Éste es un comparador concreto **avance vs velocidad tangencial poloidal de referencia**, NO el diferencial de fases entre dos partículas interior/exterior. Depende del adelgazamiento ε=a/R; tiende a cero al estrecharse el núcleo. No hay igualdad universal U=aΩ_p.

| a/R | U/(aΩ_p), núcleo uniforme |
|---:|---:|
| 0.02 | 0.057415 |
| 0.05 | 0.120629 |
| 0.10 | 0.206601 |
| 0.15 | 0.279492 |
| 0.20 | 0.343888 |

Para ε≥0.15 la expansión asintótica del núcleo delgado es menos confiable cuantitativamente; la tendencia no debe presentarse como comparación exacta con anillos de núcleo grueso.

## 5. La relación material auténtica interior–exterior [T]

Para un flujo axisimétrico **sin swirl** con ω=ω_θ e_θ:

\[
D_t\omega_\theta=\frac{u_r}{r}\omega_\theta+\nu\left(\partial_{rr}+\frac1r\partial_r+\partial_{zz}-\frac1{r^2}\right)\omega_\theta.
\]

Definiendo η=ω_θ/r y aplicando la regla del producto se obtiene exactamente

\[
\boxed{D_t\eta=\nu\left(\partial_{rr}+\frac3r\partial_r+\partial_{zz}\right)\eta.}\tag{O49.5}
\]

En el caso ideal ν=0, D_tη=0: a lo largo de una trayectoria material que pase de r_i a r_e, ω_{θ,e}/ω_{θ,i}=r_e/r_i si el mismo trazador mantiene η. Esto **no** dice que dos partículas distintas, situadas a lados distintos del aro, tengan ω_θ/r idéntica ni que giren a la misma frecuencia. Con ν>0 existe transporte más difusión. Es una vía exacta para el ajuste radial, distinta del balance axial de (O49.2).

**Regularidad.** Para clases regulares de NS axisimétrico sin swirl se conoce regularidad global. Ello no demuestra una ley de compensación universal interior–exterior para NS 3D sin simetría. La circulación con swirl azimutal uθ≠0 agrega fuentes y estructura distintas.

## 6. Prueba adversarial de 2026: el núcleo puede superar a su periferia [F/evidencia externa]

Guo, Jeong y Zhao, *Global dynamics of a single vortex ring*, prepublicación de 2026, estudian Euler axisimétrico sin swirl. Los autores prueban movimiento axial de anillos concentrados con velocidad principal Kelvin–Hicks y describen un mecanismo de filamentación: la región concentrada puede avanzar más rápido que partes periféricas de la misma vorticidad, estirando el soporte axialmente en tiempo largo. Es una **contraprueba a la lectura fuerte** "toda diferencia de velocidad se compensa restaurando automáticamente la forma". No equivale a una singularidad en tiempo finito ni a una demostración de NS 3D general. Como prepublicación, conservar su estatus y no presentarla como validación editorial definitiva.

## 7. Separar tres criterios de cierre

1. [T geométrico/marco] Misma ψ_U en frontera de anillo estacionario ⇒ (O49.1–3). **Demostrado**.
2. [A dinámico/material] Tríada de fases de partícula, fluido y foco con retorno y diferencia interior/exterior acotada ⇒ registrar vueltas poloidales reales y secciones de Poincaré; no deducido de (1). **Abierto**.
3. [A regularidad] La sincronización de ritmos impone una estimación uniforme a priori sobre producción de vorticidad versus disipación, o un criterio equivalente que excluye concentración finita. **No demostrado**.

La condición de cierre de flux en marco móvil puede existir en un anillo sin que cada partícula regrese exactamente a su punto de partida en un tiempo común. La regularidad no equivale a tener forma estacionaria. Un anillo viscoso puede conservar regularidad mientras cambia su núcleo por difusión.

## 8. Protocolo de próximo laboratorio material

En una simulación tridimensional de anillo axisimétrico bien resuelta: (a) fijar circulación Γ, geometría, perfil radial y velocidad ambiente; (b) seleccionar velocidad de avance U_rel desde el centroide del vórtice sin ajustar retrospectivamente; (c) reconstruir ψ_U y medir variación de ψ_U en el contorno elegido; (d) medir el residuo de flujo \(F=\int r(u_z-U)dr\) y contrastarlo contra deformación del contorno; (e) sembrar partículas interiores/exteriores *etiquetadas por trayectoria*, registrar dθ en vueltas completas sin asumir que permanecen siempre en el interior/exterior; (f) comparar cambios con transporte de η=ωθ/r y fuentes viscosas; (g) repetir con perfiles de núcleo distintos y viscosidades distintas. Falsadores: velocidad inferida dependiente del marco galileano, líneas que no retornan, residuos grandes cuando se presupone estado estacionario, correlación sin control de perfil inicial, o crecimiento sin sincronización. Sin vuelta material, no asignar período o resto de Poincaré.

## 9. Fuentes externas consultadas

- L. E. Fraenkel y M. S. Berger, *A Global Theory of Steady Vortex Rings in an Ideal Fluid*, Acta Mathematica 132 (1974). https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6160-11511_2006_Article_BF02392107.pdf
- A. L. Fetter, *Translational velocity of a classical vortex ring*, Phys. Rev. A 10 (1974) 1724. https://doi.org/10.1103/PhysRevA.10.1724
- P. G. Saffman, *The Velocity of Viscous Vortex Rings*, Studies in Applied Mathematics 49 (1970) 371–380. https://doi.org/10.1002/sapm1970494371
- D. Guo, I.-J. Jeong, L. Zhao, *Global dynamics of a single vortex ring*, arXiv:2602.20131 (2026, preprint). https://arxiv.org/html/2602.20131v1
- P. Buttà et al., *Global time evolution of concentrated vortex rings*, ZAMP (2022). https://link.springer.com/article/10.1007/s00033-022-01708-w
- Basilisk, *Axisymmetric stream function*. https://basilisk.fr/src/axistream.h
- J. Rencławowicz y W. M. Zajączkowski, *On Some Regularity Criteria for Axisymmetric Navier–Stokes Equations*, J. Math. Fluid Mech. 21 (2019). https://link.springer.com/article/10.1007/s00021-019-0447-0

## 10. Conclusión para la imagen total

Se conserva el hilo ontológico: el avance genera un marco donde se reconocen relaciones de las partes, sin imponer un reloj exterior. Una traducción física **exacta y localizable** de ese cierre es la constancia de la corriente relativa sobre una sección cerrada del aro y su equivalencia con el balance ponderado de flujo axial. Esto confirma un acoplamiento interno entre traslación y sección, pero **no** una compensación universal de desfases ni regularidad NS general. La tarea científica siguiente consiste en hacer corresponder este cierre estacionario de corriente con un cierre material de fases, medir si persiste al difundirse/deformarse, y recién después investigar si hay estimaciones cuantitativas de regularidad que se desprendan.
