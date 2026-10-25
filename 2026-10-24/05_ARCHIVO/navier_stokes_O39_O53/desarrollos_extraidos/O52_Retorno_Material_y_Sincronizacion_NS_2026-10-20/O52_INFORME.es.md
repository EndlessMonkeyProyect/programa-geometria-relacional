---
title: "O52 — Primeros retornos de fase material en un anillo Navier–Stokes: avance axial y deslizamiento entre capas"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-20"
status: "Extensión temporal reproducible de O51; validación numérica exploratoria; sin demostración de regularidad NS general"
parents: ["MF-43", "O25", "O27", "O39", "O43R", "O45", "O49", "O50", "O51"]
---

# O52 — Cuando el aro completa las primeras vueltas: ¿el avance sincroniza sus capas?

## 0. Respuesta y alcance

**Resultado observado.** Al extender exactamente el mismo experimento espectral de O51 desde `T=1.20` hasta `T=2.40`, sin reajustar geometría inicial ni viscosidad, **cinco de seis trazadores cruzan por primera vez un cambio de fase meridiana de −2π** respecto al centro de enstrofía móvil. Los tiempos difieren según profundidad y orientación. El aro sigue avanzando y la diferencia de fases no desaparece tras los primeros cruces. La prueba se reproduce en mallas `40³` y `48³`, con una discrepancia espacial no despreciable pero suficiente para establecer el deslizamiento en ambas discretizaciones.

**Importante:** cruzar `−2π` de una *fase definida respecto de un centro móvil* **no prueba** retorno de Poincaré a la misma posición material ni que la frontera del núcleo sea material. Tampoco prueba que las trayectorias sean periódicas; exige comparar las demás coordenadas y retornar a una sección física predeclarada. Una vuelta de fase no equivale automáticamente a un ciclo completo de la estructura.

**Dictamen:** avance axial autogenerado y giro de las capas están acoplados por el mismo flujo, pero la compensación exacta del desfase **no** es una consecuencia universal de la forma del anillo. Sigue abierta una posible relación de *control acotado* del desfase, para regímenes definidos y mediante un mecanismo dinámico verificable.

## 1. Ontología y pregunta formal

El espejo móvil fija una referencia desde la cual el flujo, el centro del aro y las partículas son comparables. La continuidad de la unidad no exige que los tres ritmos coincidan. La hipótesis fuerte que se contrasta sería: **todo retorno de la sección de referencia obliga a restaurar un mismo estado de fase entre capas**. O52 muestra una situación numérica incompatible con esa lectura estricta.

La hipótesis más prudente y aún abierta es que haya relaciones de escala y orientación suficientes para mantener *acotados* los desfasajes mientras avance, transporte y difusión se reorganizan; esto requiere una desigualdad y un intervalo de validez definidos independientemente.

## 2. Contrato computacional previo

Usamos **el mismo código y los mismos datos iniciales de O51**, con `R=1`, `a=0.35`, circulación nominal `Γ=6`, `ν=0.025`, dominio cúbico periódico de lado `2π`, sin forzamiento, evolución Fourier–Galerkin 2/3 desaliasada con RK4 y trazadores advectados con interpolación trilineal. Se extendió el horizonte a `T=2.4`, con `dt=0.004`, y se registró un estado cada `0.02` unidades de tiempo (`sampler_every=5`). No se alteró la semilla ni los puntos iniciales. Resoluciones: `N=40` y `N=48`.

**No es solución analítica exacta de NS en espacio abierto.** El dominio periódico repite el anillo y el centro de enstrofía es no material; la simetría axial sólo es aproximada a través de la discretización cúbica. El núcleo inicial tiene `a/h ≈2.23` para `N=40` y `≈2.67` para `N=48`, por lo que la resolución transversal es modesta. Las cifras temporales deben considerarse orientativas, no convergencia PDE certificada.

## 3. Evento: primer cruce de una vuelta de fase

Para cada trazador definimos, como en O51,

\[
\theta_p(t)=\operatorname{unwrap}\operatorname{atan2}\bigl(z_p(t)-Z_c(t),\,r_p(t)-R_c(t)\bigr),\qquad
W_p(t)=\frac{\theta_p(t)-\theta_p(0)}{2\pi}.
\]

El evento observado es el primer `t>0` con `W_p(t)=-1`. La estimación del evento interpola linealmente entre muestras consecutivas separadas por `0.02`. Se registra simultáneamente `Z_c(t)-Z_c(0)`, pero **ese desplazamiento es del centro de enstrofía y no de una única partícula material**.

## 4. Resultados de los primeros retornos

| Trazador | `t` a −1 vuelta, 40³ | `t` a −1 vuelta, 48³ | Avance axial al cruce, 48³ |
|---|---:|---:|---:|
| exterior, `d=0.12` | 1.36194 | **1.35914** | 1.43082 |
| interior, `d=0.12` | 1.39872 | **1.38005** | 1.45017 |
| exterior, `d=0.26` | 1.81674 | **1.79534** | 1.82240 |
| interior, `d=0.26` | 1.76530 | **1.73303** | 1.76796 |
| exterior, `d=0.34` | Sin cruce en `[0,2.4]` | Sin cruce en `[0,2.4]` | — |
| interior, `d=0.34` | 2.05350 | **2.03023** | 2.02335 |

El trazador exterior `d=.34` termina cerca de `-0.9973` vueltas en `48³`, de modo que podría cruzar poco después de `T=2.4`; **no** declaramos ausencia perpetua de retorno.

El contraste más claro está entre los trazadores exteriores: `d=.12` completa su primera vuelta de fase unos `0.4362` antes que `d=.26` en `48³`. Sus avances axiales hasta esos eventos son `1.43082` y `1.82240`. Por tanto, **no hay una longitud axial única por vuelta material para todas las capas en este ensayo**, ni restitución instantánea de las fases cuando una capa completa su giro.

## 5. Desfase y balances físicos

Definimos la diferencia entre las dos capas exteriores:

\[
S(t)=\frac{[\theta_{0.26,ext}(t)-\theta_{0.12,ext}(t)]-[\theta_{0.26,ext}(0)-\theta_{0.12,ext}(0)]}{2\pi}.
\]

En `48³`: `S(1.2)=0.14269`, máximo observado `S≈0.31504` cerca de `t=1.58`, y `S(2.4)=0.22575` vueltas. En `40³`: `S(2.4)=0.22515`, máximo `≈0.32507`. El desfase **aumenta y disminuye**, pero no regresa a cero al final del ensayo ni al producirse el primer retorno de las partículas.

| Indicador final | 40³ | 48³ |
|---|---:|---:|
| Desplazamiento del centro del aro | 2.326749 | 2.326685 |
| Desfase exterior `S(2.4)` | 0.225148 | 0.225754 |
| Cambio relativo de energía | −47.4642 % | −47.4641 % |
| Cambio relativo de enstrofía | −71.1836 % | −71.1846 % |
| Residuo relativo balance energía (trapecios) | `1.10e−5` | `1.10e−5` |
| Cruces completos de fase | 5/6 | 5/6 |

El balance de energía se comprueba contra `d E/dt = −2ν Enstrofía` con campos espectrales periódicos; el residuo numérico incluye error de cuadratura temporal.

## 6. Criterio objetivo de comparación y su límite

Un desplazamiento galileano común cambia la velocidad axial absoluta pero no las fases relativas definidas respecto del aro. Es obligatorio usar `U_rel=U_c−U_fondo` al construir una comparación objetiva. Siempre que `U_rel ≠ 0`, por regla de la cadena:

\[
\frac{d\Delta\theta}{d Z_{rel}}=\frac{\Delta\dot\theta}{U_{rel}},\qquad
\mathcal K_{obj}=\frac{R_c\,\Delta\dot\theta}{U_{rel}}.
\]

Esta igualdad **no es una ley restauradora**: define la razón local y puede variar con tiempo, perfil de núcleo y fase. Su existencia no prueba `d\mathcal K/dt=0`, ni una cota de la vorticidad.

## 7. Regularidad: el contraste que evita una confusión

Para soluciones suaves **exactamente axisimétricas sin swirl** en el dominio físico apropiado, la cantidad `q=ω_θ/r` satisface

\[
D_t q=\nu(\partial_{rr}q+3r^{-1}\partial_rq+\partial_{zz}q).
\]

El segundo miembro es un operador difusivo comparable al laplaciano radial de dimensión cinco. Bajo hipótesis estándar se dispone de principios del máximo sobre `q`, y la **regularidad global de esta subclase** es clásica (Ladyzhenskaya; Ukhovskii–Yudovich). La regularidad no requiere postular igualdad de períodos meridianos para todas las partículas del anillo. La prueba O52 es una aproximación periódica cúbica y no hereda automáticamente todas las hipótesis de ese teorema, pero es relevante como ensayo físico de una región vorticial.

No inferir que el máximo de `q` por sí solo prueba regularidad de *todo* NS 3D: con swirl y en dinámica 3D sin simetrías aparecen fuentes adicionales y estiramiento no controlado por esta identidad.

La hipótesis de «regularidad por sincronización» aún podría producir un teorema útil **si se deriva** una regla cuantitativa que controle los términos peligrosos de NS general sin restringir los datos a una clase ya regular. Este trabajo no deriva tal regla.

## 8. Conclusiones y experimentos prioritarios

- **Resuelto en O52 (numérico):** alcanzar un evento de fase de una vuelta en cinco trazadores y distinguir tiempos de retorno por capa; el aro avanza sin restaurar necesariamente los desfases.
- **Confirmado con dos discretizaciones:** los tiempos individuales de primer cruce difieren `0.003–0.032`, y el desfase final difiere ~`0.00061` vueltas. No se afirma convergencia matemática del esquema.
- **Abierto:** retorno de Poincaré real, período tras dos o más vueltas, efecto de modificar el perfil de vorticidad, tiempo prolongado sin interacción significativa de copias periódicas, control espacial convergente y relación causal avance–sincronización.
- **Falsador futuro predeclarable:** comparar dos perfiles de núcleo con mismo `R,Γ,ν`, medir `U_rel`, tiempos de primer cruce y evolución de `S`; luego introducir perturbación tridimensional con swirl o asimetría controlada. Para regularidad general se requiere demostrar una cota relevante a priori, no un patrón gráfico.

**Cierre conceptual:** *La unidad del aro puede reconocerse mientras sus partículas poseen ritmos distintos. La compatibilidad de ritmos no equivale a identidad de períodos ni a retorno geométrico total. Para demostrar regularidad, un cierre relacional debe controlar cuantitativamente las transferencias y el estiramiento que las diferencias de fase producen o permiten.*

## 9. Fuentes

**Internas:** O25, O39, O43R, O45 y O49–O51. Códigos O51 y O52 incluidos.

**Externas (teoría de regularidad clásica):** artículo *Global axisymmetric solution to the 3D incompressible anisotropic Navier–Stokes equations* (antecedentes históricos sobre NS clásica, 2026), https://www.sciencedirect.com/science/article/pii/S0021782425001515 ; artículo *Solving the axisymmetric Navier-Stokes equations in critical spaces (I): The case with small swirl component* (2022), https://www.sciencedirect.com/science/article/abs/pii/S0022039622000171 . Son referencias al estado conocido, no validación independiente de nuestras simulaciones.
