---
title: "O51 — ¿El avance axial compensa el desfase interior–exterior del aro?"
subtitle: "Anillo vorticial de Navier–Stokes 3D sin forzamiento: propagación, trazadores materiales y reloj del espejo"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-20"
status: "Experimento Galerkin 3D verificable, en tiempo finito; resultados condicionados por resolución; sin prueba de regularidad global"
parents: ["MF-43", "O25", "O27", "O39", "O41", "O43R", "O44", "O45", "O48", "O49", "O50"]
---

# O51 — El avance axial frente al desfase interior–exterior

## 0. Dictamen y alcance

**[RESULTADO NUMÉRICO]** Un anillo con campo inicial de vorticidad toroidal suave en una caja periódica se dejó evolucionar por una aproximación Galerkin tridimensional de Navier–Stokes **sin forzamiento externo**. Avanza axialmente con un centro de enstrofía que se desplaza aproximadamente `1.28156` en `T=1.20`; las partículas a distintas profundidades del núcleo acumulan diferencias de fase del orden `0.14` vueltas. El desfase no varía de modo monótono. Se controlaron errores espaciales y temporales en `N=32,40,48` y `dt=.004,.002`.

**[NO-GO]** El avance axial no fuerza una sincronización exacta entre todas las capas de un aro en este ensayo. Tampoco una ley universal puede expresar una velocidad de traslación *absoluta* `U` mediante exclusivamente desfases internos: `U` cambia bajo un boost galileano, pero los desfases internos no. Es imprescindible restar el movimiento del referente externo/fondo antes de contrastar una ecuación física.

**[ABIERTO]** No se demostraron tres vueltas de partículas, bloqueo asintótico, una desigualdad universal que controle el estiramiento en todos los flujos 3D, ni regularidad global NS. El ensayo incluye movimiento material real de un solver, pero no es una solución analítica exacta de NS en espacio abierto. El dominio periódico añade interacciones entre imágenes del aro y no constituye un anillo perfectamente aislado en R³. La malla cúbica solamente aproxima la axisimetría continua.

## 1. Narrativa ontológica → pregunta física

La unidad del aro puede permanecer reconocible mientras se transforma el foco de comparación. El avance abre una comparación entre ritmos: movimiento axial del núcleo, giro de partículas de la sección y diferencias de fase entre capas. O49 mostró el equilibrio de flujo relativo para anillos estacionarios en su marco; O50 mostró que ese equilibrio geométrico no impone isocronía por cinemática. Aquí preguntamos qué sucede si **la dinámica selecciona sus propias velocidades**.

No se confunde la singularidad ontológica del Programa con singularidad analítica de NS. El espejo es una referencia de comparación y no un espejo material.

## 2. Ecuaciones y preparación reproducible

Ecuaciones en `T³` de lado `2π`, sin fuerza:

`∂_t u + (u·∇)u = -∇p + νΔu`, `∇·u=0`, `ω=∇×u`.

Parámetros fijos: viscosidad `ν=0.025`, `R=1`, ancho nominal `a=0.35`, circulación nominal `Γ=6`, `T=1.20`, paso `dt=0.004`, mallas `32³,40³,48³`. Se verifica `40³` con `dt=0.002`.

Datos iniciales en cilíndricas `r=(x²+y²)^(1/2)`:

`ω(x,y,z)=(-y,x,0) f(r²,z)`, con

`f(r²,z) = Γ/(π a² R) exp(-((r²-R²)/(2Ra))² - (z/a)²)`.

Son aproximadamente un tubo toroidal de sección gaussiana, sin swirl y con vorticidad orientada azimutalmente. La expresión `(-y f,x f,0)` tiene divergencia exactamente nula en espacio euclídeo cuando `f` depende de `r²,z` y está localizada lejos de la frontera. En el cubo periódico se periodiza numéricamente (colas muy pequeñas, pero no exactamente cero). Se reconstruye `u` por inversión de curl en Fourier (proyección libre de divergencia).

Esquema numérico: 

`∂t û(k) = P_k F[u×ω](k) - ν|k|² û(k)` con `P_k=I-kkᵀ/|k|²`, filtro 2/3 y RK4. `u×ω` es la forma rotacional de la no linealidad: el gradiente de Bernoulli desaparece tras `P_k`. Se fija el modo medio a cero. El campo permanece libre de divergencia en la aproximación Galerkin.

Las seis partículas se siguen con `ẋ_p=u(x_p,t)` usando RK4 con interpolación trilineal de `u` en cada subetapa. Se lanzan desde `(R±d,0,0)`, con `d=0.12,0.26,0.34`. No se impone el radio ni la velocidad de avance después del instante inicial.

## 3. Observable de avance y fases materiales

Se obtiene `R_c(t)` y `Z_c(t)` como promedios radial y axial ponderados por `|ω|²`. Para el eje axial periódico se usa media circular angular. Estos **centros de enstrofía no son partículas materiales** y pueden desplazarse por redistribución, no sólo por transporte de materia. Su rol se declara antes de mirar los resultados.

Para trazador `p`, definimos una fase meridiana desenrollada relativa al centro del aro:

`θ_p(t)=unwrap atan2(z_p(t)-Z_c(t), r_p(t)-R_c(t))`.

El desfase entre dos capas se mide por

`S_{p,q}(t) = [(θ_q(t)-θ_p(t)) - (θ_q(0)-θ_p(0))]/(2π)`.

**Sincronización estricta entre las capas en todo el intervalo** exigiría `S_{p,q}(t)=0` para todos `t`. Un retorno común tras vueltas enteras requiere eventos de retorno material real; no está demostrado aquí porque ningún trazador logró siquiera una vuelta durante `[0,1.2]`.

El signo de `θ` depende de la orientación del sistema, pero las magnitudes de desfase y la existencia de deslizamiento no.

## 4. Resultados y regresión

| Corrida | Despl. axial `Z_c` | `U_media` | Desfase exterior `d=.12` vs `.26` | Desfase interior correspondiente | Cambio energía | Cambio enstrofía |
|---|---:|---:|---:|---:|---:|---:|
| `32³`, `dt=.004` | 1.2809923 | 1.0674936 | 0.1017199 | 0.0839084 | −30.7938 % | −53.1599 % |
| `40³`, `dt=.004` | 1.2815320 | 1.0679433 | 0.1461909 | 0.1044085 | −30.7818 % | −53.2314 % |
| `40³`, `dt=.002` | 1.2815320 | 1.0679433 | 0.1461947 | 0.1044107 | −30.7818 % | −53.2314 % |
| `48³`, `dt=.004` | 1.2815628 | 1.0679690 | 0.1426899 | 0.1075818 | −30.7809 % | −53.2342 % |

La diferencia espacial de fase entre `40³` y `48³` es `0.0035010` vueltas en este observable (≈2.5 % de 48³): hay **convergencia orientativa, no demostración de convergencia asintótica**. `32³` es demasiado burda para usar su estimación de fase como valor final. El avance está considerablemente más convergido que el desfase.

Los valores temporales aproximados `S` en `48³`:

| `t` | Desfase `S` (vueltas) |
|---:|---:|
| 0.00 | 0.0000 |
| 0.24 | 0.0535 |
| 0.48 | 0.1171 |
| 0.72 | 0.1383 |
| 0.96 | 0.1062 |
| 1.20 | 0.1427 |

**Interpretación:** no se observa un bloqueo estricto de fase; tampoco se observa crecimiento monótono. El descenso entre `0.72` y `0.96` puede deberse a dinámica reorganizativa, pero por sí solo no prueba una fuerza restauradora universal ni retorno asintótico.

Máximo número de vueltas poloidales acumuladas por cualquier trazador en `48³` durante el intervalo: `0.894402`. **No se observó ninguna vuelta completa**; no adjudicar restitución de fase tras ciclos.

## 5. Controles físicos y numéricos

- `max |∇·u|` espectral en los datos finales: `~1e−15` (proyección).
- La energía disminuye y el balance NS `dE/dt=−2ν Enstrofía` se cumple al integrar por trapecios los registros con error absoluto relativo al `E(0)` de `3.7×10⁻⁵` (para `dt=.004`, muestras cada 10 pasos) y `9.4×10⁻⁶` cuando `dt=.002` (muestreo duplicado).
- Reducción del paso temporal en `40³`: diferencia axial `1.35×10⁻⁹`, desfase `3.74×10⁻⁶` vueltas.
- Contraste espacial `40³/48³` corroboró desplazamiento próximo y fases no idénticas, y diferencia material no nula.
- `validar_y_graficar.py` preserva **28 pruebas automatizadas** de rango/invariantes/convergencia; no equivalen a 28 leyes físicas independientes.
- Todo el código y los datos crudos están incluidos; es posible reproducir sin escoger velocidades de antemano.

## 6. Resultado exacto previo que este ensayo no debe confundir: ecuación de q=ωθ/r

En NS axisimétrico *continuo sin swirl*, con `ω=ωθ eθ`, se obtiene exactamente:

`D_t ωθ = (u_r/r) ωθ + ν (∂_rr + (1/r)∂_r + ∂_zz -1/r²) ωθ`.

Para `q=ωθ/r`, siempre que los campos sean suaves,

`(∂_t+u_r∂_r+u_z∂_z) q = ν(∂_rr+(3/r)∂_r+∂_zz)q`.

En Euler (`ν=0`) la relación `q` es materialmente conservada. En Navier–Stokes (`ν>0`) se difunde: no es una igualdad de frecuencias ni un mecanismo automático de sincronización, pero es un puente matemático exacto entre radio, flujo y reorganización de vorticidad. El anillo computado en cubo periódico se aproxima a la clase axisimétrica, pero no se proclama su simetría exacta global.

## 7. NO-GO exacto de velocidad absoluta y reloj

La transformación galileana

`u^V(x,t)=u(x−V t,t)+V`, `x^V_p(t)=x_p(t)+Vt`,

con `V` vector axial constante, preserva NS sin forzamiento (adaptando correctamente la presión) y las diferencias de fase relativas si se transforma simultáneamente el centro del aro. Sin embargo, el avance medido en el laboratorio cambia: `U^V=U+V_z`.

**Por tanto** ninguna ley física objetiva puede determinar `U` *absoluta* sólo desde diferencias de fase internas. Debe compararse `U_rel=U−u_fondo,z`, donde `u_fondo` se fija operacionalmente. En un toro periódico puede fijarse como velocidad media del fluido; un boost cambia conjuntamente ambos sumandos y preserva `U_rel`. Esta corrección mejora el comparador `K=R ΔΩ_io/U` previamente propuesto.

Se propone `K_obj = R_c ΔΩ_io / U_rel`, cuando `U_rel≠0`, usando diferencias de fases desenrolladas y una referencia consistente. **No se ha demostrado `d K_obj/dt=0` ni que controle enstrofía.**

## 8. Consecuencia para la conjetura de sincronización y regularidad

**Rechazada en su versión universal estricta:** todo anillo NS sin forzamiento con frontera/coherencia y avance axial mantiene todas las capas perfectamente sincronizadas. Este ensayo exhibe deslizamiento de fase en una aproximación dinámica.

**Sigue abierta una versión precisa:** el avance relativo y la interacción interior–exterior pueden inducir respuestas geométricas que *moderen* el deslizamiento en ciertos regímenes. Habría que demostrarlo mediante una cota dinámica, no mediante el mero cierre geométrico ni la igualdad de fases a un instante.

**La regularidad global de NS 3D general NO está demostrada.** Los datos axisimétricos sin swirl son una clase especial donde ya hay teoría matemática favorable; resolverla en un simulador no resuelve el problema de Clay.

## 9. Próxima obligación reproducible

1. Aumentar la resolución del núcleo hasta tener al menos 8–12 celdas a lo ancho y hacer estudio de convergencia de desfase.
2. Extender el tiempo mientras se controla que la interacción con copias periódicas no domina y registrar retornos materiales completos o su ausencia.
3. Comparar dos perfiles de núcleo con la misma circulación y radio, pero distinta distribución de vorticidad, manteniendo `ν` fijo; no confundir cambio de perfil con cambio de fase.
4. Medir en un marco objetivo `U_rel`, `ΔΩ_io` y los términos de estiramiento y difusión en la ecuación de `q`.
5. Formular por anticipado una ley o cota para `K_obj` y buscar soluciones que la falsen. Sólo entonces contrastar si ese control implica regularidad dentro de la clase examinada.

## 10. Rastro documental y genealogía

Antecedentes internos: O25 (espejo y reloj), O27 (canales ortogonales), O39 (balance de estiramiento, difusión y ventanas móviles), O43R (mapa de retorno material), O44 (falta de vueltas completas), O45 (tres ritmos), O49 (equilibrio de flujo en marco móvil), O50 (isocronía y deslizamiento cinemáticos). O51 añade exclusivamente la **evolución Galerkin NS 3D no forzada del anillo** y la comparativa de fases con regresión, y señala la necesidad de objetividad galileana. No reetiquetar identidades clásicas como teoremas originales.
