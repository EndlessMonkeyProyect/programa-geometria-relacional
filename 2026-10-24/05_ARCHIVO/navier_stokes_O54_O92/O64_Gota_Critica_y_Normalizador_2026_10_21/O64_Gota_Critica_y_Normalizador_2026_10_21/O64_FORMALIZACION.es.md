---
title: "O64 — Gota mínima, interfaz y referencia normalizadora"
subtitle: "Dos curvaturas, continuidad relacional y escala crítica de fragmentación"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-21"
status: "Suplemento autónomo: identidades capilares exactas y estimación de Hinze condicionada; puente al programa pendiente"
parents: ["O40", "O45", "O53", "O58", "O60", "O61", "O62", "O63", "Imagen Total v3.8.1"]
---

# O64 — La gota y la escala a la que una unidad puede mantenerse

## 0. Qué estamos preguntando

La pregunta del autor es si la información relacional mínima requerida para que una unidad continúe —investigada en O63, a partir de los ritmos del anillo vorticial— podría asociarse con el **tamaño de una gota mínima**. La pregunta es fértil, pero exige aclarar el significado de «mínima» **antes** de escoger un mecanismo. No confundiremos:

1. tamaño absoluto más pequeño que puede existir;
2. tamaño mínimo que un flujo turbulento puede fragmentar eficazmente bajo un régimen declarado;
3. tamaño físico más pequeño que una interfaz puede describir bajo un modelo continuo dado;
4. cantidad mínima de información relacional suficiente para anticipar un observable.

Estas cuatro nociones no son equivalentes. La segunda conduce a un umbral de fragmentación; la cuarta es la cuestión del programa. Se requiere un puente no circular entre ambas.

### Contrato epistemológico

- **[O] Narrativa del programa.** Una unidad sostiene un cierre propio a través del normalizador que permitió comparar sus relaciones; lo posible no está necesariamente habitado; la novedad se acredita por una diferencia antes no realizada. La dirección es consecuencia, no premisa de constitución. El espejo que cambia escala no modifica automáticamente la unidad física.
- **[D] Modelo añadido.** Una gota introduce **dos fases** y una interfaz con tensión superficial `σ>0`; ésta es física adicional respecto de Navier–Stokes monofásico de O53.
- **[T] Resultado exacto.** Young–Laplace, el costo de área de fragmentar una esfera en esferas menores y la variación de curvatura de un toroide circular, bajo hipótesis definidas.
- **[M] Estimación de régimen.** Diámetro de Hinze para turbulencia homogénea e isotrópica en rango inercial; su coeficiente empírico no es una ley universal.
- **[A] Abierto.** No existe identificación derivada entre el múltiplo entero cuadrático de O58 y el umbral capilar, ni prueba de un tamaño universal de gota, ni cierre predictivo general de NS 3D.

## 1. Narrativa → ontología → contrato físico

La imagen de la gota no es simplemente otra figura: representa la diferencia entre interior y exterior en una **interfaz reconocible**. Puede conservar su identidad como región material aun cuando su contorno cambie de escala o de forma; el conjunto de preguntas al que responde nuestro comparador decide qué se considera la «misma» unidad. A diferencia del anillo vorticial sin interfaz material, una gota ordinaria tiene una condición de frontera física cuya curvatura genera un salto de esfuerzo. No convertir ese salto en el múltiplo ontológico por decreto.

El contacto con O63 es doble: (i) **el mapa de fases/ritmos del flujo** determina esfuerzos instantáneos y su evolución; (ii) **la respuesta de la interfaz** depende de dos curvaturas y de las propiedades de ambas fases. Compartir energías por banda o `A₂` no fija estas propiedades; por eso no determina el tamaño de una gota sin datos adicionales.

## 2. Dos radios principales de curvatura

Sea `Γ` una interfaz lisa con tensiones isotrópicas y `κ₁=1/R₁`, `κ₂=1/R₂` las curvaturas principales firmadas según orientación. En equilibrio estático, sin esfuerzos viscosos ni otros esfuerzos interfaciales:

\[
\boxed{\Delta p=\sigma(\kappa_1+\kappa_2)
=\sigma\left(\frac1{R_1}+\frac1{R_2}\right).}\tag{64.1}
\]

**Importante:** las curvaturas pueden tener signo, y los radios principales **no** son los dos ciclos globales `R,r` del toroide. Tampoco satisfacen automáticamente la identidad de O58 `a²+b²+1=N²`, donde `a,b,N` eran enteros que contaban relaciones.

Para una **gota esférica** de radio `s`:

\[
\boxed{\Delta p=2\sigma/s,\quad A=4\pi s^2,\quad V=4\pi s^3/3.}\tag{64.2}
\]

**Teorema O64-T1 — ausencia de tamaño mínimo geométrico en este continuo.** Para cada `s>0`, el campo estacionario `u=0` en ambas fases con presiones constantes `p_in=p_out+2σ/s` y geometría esférica satisface formalmente la condición de salto capilar e incomprensibilidad, bajo condiciones de frontera compatibles y sin fuerzas externas. Por tanto, ninguna identidad (64.1) o condición monofásica de incompresibilidad selecciona una longitud universal positiva `s_min`.

*Demostración.* `∇·0=0` y los términos temporales, convectivos y viscosos de cada fase se anulan. Los gradientes de presión son cero dentro de cada región. El salto `p_in-p_out` compensa la curvatura de la esfera mediante (64.2) para cualquier `s>0`. **Límite:** cuando `s` es molecular, la descripción continua y la hipótesis de `σ` constante dejan de estar garantizadas. ∎

## 3. Volver al toroide: diferencia local de la misma totalidad

La superficie circular ideal de radio mayor `R` y radio de tubo `r`, con `R>r>0`, tiene parametrización

\[
X(\theta,\phi)=((R+r\cos\theta)\cos\phi,(R+r\cos\theta)\sin\phi,r\sin\theta).
\]

Sus curvaturas principales (convención de normales compatible con la curvatura positiva de la esfera) son

\[
\boxed{\kappa_{\rm merid}=\frac1r,\qquad
\kappa_{\rm toro}=\frac{\cos\theta}{R+r\cos\theta}.}\tag{64.3}
\]

Así, la suma que una interfaz capilar leería cambia con el recorrido:

\[
K(0)=\frac1r+\frac1{R+r},\qquad
K(\pi)=\frac1r-\frac1{R-r},\qquad
K(0)-K(\pi)=\frac{2R}{R^2-r^2}>0.\tag{64.4}
\]

**Teorema O64-T2.** Un toroide circular de `R>r>0` no puede satisfacer una condición estática de salto de presión **constante** con `σ` constante en ambas fases sin esfuerzos adicionales; el salto capilar requerido por (64.1) depende de `θ`. Esto no demuestra que un anillo vorticial en movimiento no pueda persistir: los esfuerzos dinámicos y presiones variables son precisamente la física que habría que resolver.

*Demostración.* La fórmula (64.4) da dos curvaturas medias diferentes en puntos distintos, y una presión uniforme a cada lado de la interfaz da un salto constante. Contradicción. ∎

Por eso la geometría misma enseña a distinguir continuidad de una configuración dinámica frente a equilibrio estático de una gota.

## 4. La «gota mínima» como umbral de fragmentación, no radio ontológico

Una interfaz requiere esfuerzo para aumentar su área. Dividir una gota esférica de radio `s` en `m≥2` gotas esféricas de igual volumen total produce radios `s_m=s m^{-1/3}` y área total `A_m=m^{1/3}A_1`. El incremento energético capilar es

\[
\boxed{\Delta E_\sigma=4\pi\sigma s^2(m^{1/3}-1)>0.}\tag{64.5}
\]

**Teorema O64-T3.** Dentro del contrato de volumen fijo y estados inicial/final esféricos, la fragmentación aumenta el área y necesita un aporte neto de energía superficial. Esto no es una cota universal sobre el trabajo externo, ni asegura imposibilidad de ruptura bajo dinámica real.

En turbulencia con tasa de disipación de energía cinética por masa `ε`, densidad de fase continua `ρ_c`, tensión interfacial `σ` y escala `d` **dentro del rango inercial**, la estimación de velocidades relativas `δu_d~(ε d)^{1/3}` da

\[
We_d\sim\frac{\rho_c(\delta u_d)^2d}{\sigma}
\sim\frac{\rho_c\varepsilon^{2/3}d^{5/3}}{\sigma}.\tag{64.6}
\]

Al igualar con un umbral crítico `We_cr` surge la escala Kolmogorov–Hinze:

\[
\boxed{d_H\simeq C_H\left(\frac{\sigma}{\rho_c}\right)^{3/5}\varepsilon^{-2/5},\qquad C_H\approx0.725\ \text{(régimen/fuente empírica).}}\tag{64.7}
\]

**Interpretación rigurosa:** `d_H` aproxima el *máximo diámetro estable frente a ese mecanismo de fragmentación turbulenta*; equivalentemente, el umbral inferior de tamaño al que ese mecanismo suele empezar a ser eficaz. **No** es el diámetro mínimo físicamente existente. Para escalas fuera del rango inercial, fluidos muy viscosos, surfactantes o coalescencia importante, (64.7) puede fallar o requerir correcciones.

**Otras escalas, no equivalentes:** Kolmogorov `η=(ν³/ε)^{1/4}` mide la escala disipativa viscosa del flujo, no el tamaño mínimo de una gota. Para cizalla externa de tasa `γdot`, `Ca=μ_c γdot d/σ` compara esfuerzo viscoso con tensión y puede organizar un umbral de rotura, **pero el `Ca` crítico depende de la configuración y de la razón de viscosidades**.

## 5. Cálculo de ejemplo, no medición del anillo O53

Se toman valores ilustrativos `ρ_c=1000 kg/m³`, `μ_c=0.001 Pa·s`, `σ=0.072 N/m`. Estos datos no describen automáticamente las fases del experimento monofásico O53, que usa parámetros adimensionales. La estimación de (64.7) produce:

| ε [m²/s³] | d_H [mm] | η de Kolmogorov [mm] |
|---:|---:|---:|
| 0.001 | 37.5610 | 0.1778 |
| 0.01 | 14.9533 | 0.1000 |
| 0.1 | 5.9530 | 0.0562 |
| 1 | 2.3699 | 0.0316 |
| 10 | 0.9435 | 0.0178 |

Son **escalas modelo**, no diámetros predichos de una gota individual de O53. Las cifras finas provienen de constantes elegidas y no representan precisión experimental.

## 6. Una firma relacional para O64: qué incluye y qué excluye

**Propuesta [H64].** Para una interfaz y pregunta explícita de continuidad/fragmentación, considerar una firma de referencia que incluya al menos:

\[
\mathscr C_{\partial U}=\big(\text{clase de interfaz},\ \sigma,\ \rho_{1,2},\ \mu_{1,2},\ \kappa_1,\kappa_2,\ \text{ritmos relativos},\ \text{esfuerzos interfaciales}\big).\tag{64.8}
\]

Esta lista es **candidata y no probada mínima o suficiente**. La continuidad relacional requeriría especificar qué preguntas admite y verificar si dos estados que comparten la firma tienen la misma respuesta futura. El cierre semántico de O45 no se deduce de registrar solamente esas variables.

La firma de O63 `A₂`, que detecta diferencias angulares de fase en un *anillo monofásico*, no contiene `σ`, ni la geometría y densidades de una interfaz adicional. Por tanto, **no puede determinar ella sola `d_H`**. En particular, variar `σ` manteniendo los datos de O63 no cambia `A₂` por definición, pero altera `d_H` conforme a `σ^{3/5}`. Es un falsador simple de una identificación inmediata entre firma angular y tamaño de gota.

### El normalizador y la estela

El programa propone que la referencia que normalizó una unidad transporte las relaciones acreditadas hacia otra escala. En el caso físico de gotas, el parámetro `d_H` es una escala de comparación **dependiente del contexto** (`σ, ρ_c, ε`), no un entero. La normalización adimensional `d/d_H` permite comparar condiciones experimentales distintas **siempre que ambas pertenezcan al régimen de validez**. No representa por sí sola la herencia o novedad aritmética de `a²+b²+1=N²`; trasladar el resto `1` requeriría una regla física y un observable que no tenemos.

**Observación central:** si una escala deja de fragmentarse, esto puede ser porque el esfuerzo del flujo ya no alcanza el costo de interfaz, sin que la gota haya perdido su identidad. La pérdida de condición de fragmentación y la pérdida de cierre propio son proposiciones diferentes.


### 6.1. Puente discreto condicional: dos áreas cuadráticas y una celda pendiente [H/T]

Podemos realizar **sin contradicción algebraica** el cierre de O58 como partición de una superficie, pero solo bajo una **hipótesis explícita de discretización**. Sea `A₀>0` una unidad de área **elegida**, y supongamos una interfaz con

\[
A_A=a^2 A_0,\qquad A_B=b^2 A_0,\qquad
A_{\rm pend}=A_0,\qquad A_{\rm total}=N^2A_0.
\]

La condición de partición `A_A+A_B+A_pend=A_total` se convierte **exactamente** en

\[
\boxed{a^2+b^2+1=N^2.}\tag{64.8a}
\]

Para una esfera cuya superficie se supone subdividida así, `4πs²=N²A₀` da

\[
\boxed{s=N\sqrt{\frac{A_0}{4\pi}}.}\tag{64.8b}
\]

En el **modelo entero con `a,b>0`**, la solución positiva más pequeña es `(a,b,N)=(2,2,3)`. En él aparece un tamaño inferior **dependiente de `A₀`**, `s_{\rm min,modelo}=3√(A₀/(4π))`. **Esto no es un tamaño mínimo físico**: basta cambiar el área postulada `A₀` para cambiarlo; ninguna ley de Navier–Stokes, Young–Laplace o O63 ha seleccionado `A₀`.

El término «celda deshabitada» se refiere aquí a una **clase de relaciones etiquetadas**, no a un agujero material en la gota ni a ausencia de líquido. La partición no necesita formar dos cuadrados geométricos disjuntos sobre la superficie: los cuadrados son números de celdas en un contrato combinatorio.

Un **límite por el total** puede formularse si además declaramos un presupuesto capilar fijo `E_*` que efectivamente limite `σ A_total`: entonces `σN² A₀≤E_*` implica

\[
\boxed{N\le\sqrt{\frac{E_*}{\sigma A_0}}.}\tag{64.8c}
\]

Es una implicación algebraica **condicional al presupuesto**, no una cota universal de Navier–Stokes. La energía cinética puede convertirse en energía superficial, de modo que no puede suponerse un tope `E_*` disponible sin especificar el sistema y las condiciones de contorno.

**Falsador interno:** en el límite de refinamiento `A₀→0` y `N→∞` manteniendo `N²A₀=A_total` constante, `A_pend/A_total=1/N²→0`. Por tanto, «queda una unidad» en cada rejilla **no proporciona** por sí mismo ni una longitud mínima positiva ni una tensión física nueva. El mecanismo solo se vuelve predictivo si `A₀` o una regla de selección viene de un observable dinámico independiente.

## 7. Conservación energética de dos fases: relación física que evita metáforas

Para Navier–Stokes incompresible de **dos fases** con tensión superficial constante, densidades y viscosidades por fase constantes, interfaz lisa transportada por la velocidad, sin fuerzas exteriores, trabajo en frontera, surfactantes ni cambios topológicos, la identidad formal de energía es

\[
\boxed{\frac{d}{dt}\left[\sum_{i=1}^2\int_{\Omega_i(t)}\frac12\rho_i|u|^2\,dV+\sigma\operatorname{Área}(\Gamma(t))\right]
=-\sum_{i=1}^2\int_{\Omega_i(t)}2\mu_i|D(u)|^2\,dV.}\tag{64.9}
\]

Esta identidad **sí** contiene un presupuesto de energía interfacial y disipación. Pero **no obliga** a que la superficie conserve una normalización cuadrática con resto unitario, ni evita por sí sola rotura, coalescencia o singularidad. Una condición topológica de ruptura exige mayor análisis.

## 8. Resultado de contraste y próximos pasos

**[T]** Hay dos radios de curvatura y una relación de presión para cada punto de una interfaz; los resultados (64.1)–(64.5) son exactos bajo hipótesis. En el continuo no surge tamaño absoluto mínimo. **[M]** Hinze da un umbral de fragmentación contextual, con exponente escalado verificable. **[H]** El tamaño crítico podría servir de **escala física de referencia** para las relaciones del anillo, sólo tras introducir y medir una interfaz y demostrar compatibilidad de comparadores. **[F]** La firma de O63 no basta para fijar un diámetro de gota si no conoce propiedades interfaciales.

**O65 propuesto, si decidimos avanzar:** construir dos preparaciones físicas **con idéntico flujo** y distinta `σ`, calcular el umbral de fragmentación antes de evolucionarlas y exigir que cualquier normalizador candidato distinga sus respuestas; luego introducir dos fases de forma controlada, sin adjudicar carácter de gota a estructuras monofásicas. La transición discreta del múltiplo no debe definirse después de observar los resultados.

## Fuentes externas solo para contraste físico

- Journal of Fluid Mechanics, *Morphology of clean and surfactant-laden droplets in homogeneous isotropic turbulence*. https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/morphology-of-clean-and-surfactantladen-droplets-in-homogeneous-isotropic-turbulence/4D73AA84DA6451E44774F5D67F8767F7
- Journal of Fluid Mechanics, *Droplet–turbulence interactions and quasi-equilibrium dynamics in turbulent emulsions*. https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/dropletturbulence-interactions-and-quasiequilibrium-dynamics-in-turbulent-emulsions/02D6429A447BB860DA3615E0D76A062A
- Physics Today, *Your wetting day* (Young–Laplace). https://physicstoday.aip.org/quick-study/your-wetting-day
- SIAM Review, *Energy Considerations for Multiphase Fluids with Variable Density and Surface Tension*. https://epubs.siam.org/doi/10.1137/070694880

La bibliografía no es fuente de ontología ni autoría del programa; sirve para verificar hechos físicos y distinguir contenido clásico del desarrollo relacional.
