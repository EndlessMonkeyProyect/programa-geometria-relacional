---
title: "O53 — Perturbación tridimensional del anillo, avance axial y desfase material"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-20"
status: "Laboratorio numérico Fourier–Galerkin de Navier–Stokes 3D; verificación exploratoria, no prueba de regularidad global"
parents: ["MF-43", "O25", "O27", "O39", "O42", "O45", "O49", "O50", "O51", "O52"]
---

# O53 — El espejo al perder simetría: avance y diferencia de ritmos en un anillo NS 3D

## 0. Respuesta y genealogía

**Pregunta:** ¿al introducir una diferencia verdaderamente tridimensional en el aro, su avance axial obliga a compensar o sincronizar los ritmos materiales del interior y exterior? ¿Sobrevive la relación cuando igualamos la energía inicial y comprobamos la resolución?

**Resultado de este ensayo:** NO se observa una regla universal de restauración de fase determinada por el avance axial. A `T=2.4`, una perturbación solenoidal del 14 % aumenta el desfase exterior respecto al control si se conserva su amplitud sin renormalizar; **al igualar la energía cinética inicial**, una perturbación con la misma forma lo reduce. Ambos signos de la respuesta se reproducen cualitativamente en `N=40` y `N=48`. La relación `R_c (dΔθ/dt)/U_rel` cambia durante la evolución y atraviesa valores positivos y negativos. Un patrón no equivale a una ley de compensación universal.

**Continuidad:** O49 encontró la condición estacionaria de frontera de un anillo ideal, O50 distinguió cierre de frontera y sincronización material mediante flujos cinemáticos, O51–O52 hicieron evolucionar el aro axisimétrico aproximado de Navier–Stokes y registraron los primeros cruces de fase. O53 conserva íntegros esos datos iniciales de control y agrega una perturbación no axisimétrica reproducible, una fuente de giro azimutal, un balance de estiramiento y un control de energía inicial.

**Estatutos:** `[O]` interpretación ontológica; `[D]` definición; `[T]` identidad exacta de NS para soluciones suaves; `[E]` observación numérica Galerkin; `[F]` falsación del comparador simple *en esta clase numérica*; `[A]` pregunta abierta.

## 1. Ontología, lenguaje y discriminación

Un anillo que se desplaza puede mantener reconocible una unidad geométrica mientras sus partes internas giran con diferentes ritmos. El espejo móvil (referencia en `Z_c(t),R_c(t)`) hace comparables los movimientos materiales, pero no crea una fuerza restauradora. Hay tres cierres distintos: (i) contorno/flujo relativo compatible con una frontera, (ii) retorno de una fase meridiana medida, (iii) regularidad matemática uniforme de las derivadas del campo. No se sigue (iii) de (i) o (ii).

Una **perturbación perpendicular** o una fase distinta no implica control de amplificación, ni el retorno de fase implica retorno a la misma posición material. El significado de *sincronización* debe ser una condición predictiva declarada, no una reconstrucción retrospectiva del desfase observado.

## 2. Datos y perturbación solenoidal [D/T]

En el dominio periódico `[-π,π)^3`, resolvemos una aproximación espectral Galerkin sin fuerza de Navier–Stokes incompresible con viscosidad `ν=0.025`, radio base `R=1`, radio del núcleo `a=0.35`, circulación **nominal** del perfil inicial `Γ=6`, tiempo final `T=2.4` y paso RK4 `dt=0.004`:

\[
\partial_tu+P_\sigma[(u\cdot\nabla)u]=\nu\Delta u,\quad \nabla\cdot u=0.
\]

Partimos del perfil O51–O52, obtenido al invertir el rotacional de una distribución anular localizada

\[
\omega_0=(-y f,x f,0),\quad
 f=\frac{\Gamma}{\pi a^2R}\exp\!\left[-\left(\frac{r^2-R^2}{2Ra}\right)^2-\left(\frac z a\right)^2\right].
\]

Sea `g` el factor exponencial. Definimos el potencial vectorial no axisimétrico

\[
\mathcal A(x,y,z)=\left(0,\frac xR g,\frac yR g\right),\qquad
v=P_{2/3}(\nabla\times\mathcal A).
\]

Por construcción `∇·v=0`. Después de truncar en `2/3` espectral y quitar el modo de media, iniciamos

\[
 u_{\epsilon}(0)=c_\epsilon\Big(u_0(0)+\epsilon\frac{\|u_0(0)\|_2}{\|v\|_2}\,v\Big).
\]

En el ensayo de energía libre `c_ε=1`; en el **ensayo de energía igualada** elegimos

\[
 c_\epsilon=\frac{\|u_0(0)\|_2}
 {\|u_0(0)+\epsilon\|u_0(0)\|_2 v/\|v\|_2\|_2}.
\]

Se probaron `ε=0`, `0.07`, `0.14`; la condición de energía igualada se repitió con `ε=0.14`. La renormalización ajusta toda la velocidad y **no** iguala simultáneamente la enstrofía, la palinstrofía, el perfil de circulación o la escala del espejo. Este límite es relevante: el control separa el efecto de energía cinética inicial, pero no todas las demás causas.

El algoritmo usa velocidades espectrales sin divergencia, desaliasado de los modos retenidos por la regla `2/3`, no linealidad en forma `u×ω`, RK4 y trazadores advectados por interpolación trilineal. Es solución del sistema de Galerkin discretizado, **no solución exacta del PDE continuo** ni un cálculo DNS certificado.

## 3. Observables preregistrados y balances [D/T]

Se mantienen los seis marcadores de O52, inicialmente situados a profundidades meridianas `d=0.12,0.26,0.34` y en lados interior/exterior. Con radio de enstrofía `R_c(t)` y centro axial circular `Z_c(t)`, definimos

\[
\theta_j(t)=\operatorname{unwrap}\operatorname{atan2}(z_j(t)-Z_c(t),r_j(t)-R_c(t)),
\]
\[
 S(t)=\frac{[\theta_{0.26,ext}(t)-\theta_{0.12,ext}(t)]-[\theta_{0.26,ext}(0)-\theta_{0.12,ext}(0)]}{2\pi}.
\]

`S` es desfase de marcadores respecto de un centro de **enstrofía no material**; un cruce de `−1` vuelta no es retorno espacial a una sección de Poincaré. Durante la perturbación los marcadores pueden adquirir movimiento azimutal: se conserva la definición de O52 para comparabilidad, con su límite explícito.

En el caso numérico la velocidad media de fondo es cero (modo de Fourier `k=0` suprimido), por lo que el desplazamiento medido de `Z_c` es relativo a ese fondo. Una transformación galileana uniforme no puede modificar `S`.

La cantidad candidata de acoplamiento instantáneo es

\[
\mathcal K(t)=\frac{R_c(t)}{U_{rel}(t)}\frac{d\Delta\theta}{dt}
=R_c(t)\frac{d\Delta\theta}{dZ_{rel}},
\]

si `U_rel≠0`. Es identidad de regla de cadena, **no ley conservativa**. Se evalúa con derivadas temporales de las muestras y se declara sensible a la elección de centro y a la diferenciación numérica.

Para soluciones suaves incompresibles de NS sin fuerza, con promedios espaciales `⟨·⟩`:

\[
 E_\omega=\tfrac12\langle|\omega|^2\rangle,\quad
 J=\langle|\nabla\omega|^2\rangle,\quad
 \ell_\omega=\sqrt{2E_\omega/J},
\]
\[
\boxed{\dot E_\omega=P-D,\quad
P=\langle\omega\cdot(\omega\cdot\nabla)u\rangle,\quad D=\nu J,}
\]
\[
\boxed{\dot E_{kin}=-2\nu E_\omega,\quad E_{kin}=\tfrac12\langle|u|^2\rangle.}
\]

O53 computa `P`, `D`, la variación de `Ekin` y sus residuos de cuadratura. En el flujo axisimétrico sin *swirl* también puede existir **estiramiento 3D de vorticidad**; la perturbación no lo crea desde cero, sino que rompe simetría e introduce componentes y acoplamientos adicionales.

## 4. Resultados cuantitativos [E]

Todos los resultados siguientes se refieren al mismo `T=2.4`, `ν=0.025` y trazadores iniciales. Las unidades son las de la simulación periódica.

| Caso | `N` | `Ekin(0)` | Avance axial `ΔZ` | Desfase `S(T)` (vueltas) | Pico de producción `P` |
|---|---:|---:|---:|---:|---:|
| Control original | 40 | 0.07788157 | 2.326749 | 0.225148 | 0.07123 |
| Perturbación 7 % | 40 | 0.08230622 | 2.360544 | 0.242793 | 0.08265 |
| Perturbación 14 % | 40 | 0.08749412 | 2.384592 | 0.290501 | 0.11741 |
| Perturbación 14 %, energía igualada | 40 | 0.07788157 | 2.258945 | 0.168686 | 0.09438 |
| Control original | 48 | 0.07788169 | 2.326685 | 0.225754 | 0.07119 |
| Perturbación 14 % | 48 | 0.08749141 | 2.384608 | 0.292658 | 0.11804 |
| Perturbación 14 %, energía igualada | 48 | 0.07788169 | 2.258996 | 0.165097 | 0.09481 |

**Contraste decisivo:** conservar `c_ε=1` hace que el perfil perturbado tenga **mayor energía cinética inicial**; el desfase crece. Cuando se fuerza `Ekin_ε(0)=Ekin_0(0)`, el desfase **disminuye** respecto del control, en las dos resoluciones. La diferencia entre estos resultados prohíbe interpretar el primer aumento como efecto aislado de la ruptura de simetría.

**Escala del espejo:** en `N=48`, el control comienza con `ℓ_ω≈0.22752` y termina con `≈0.32922`. Ambos casos perturbados de 14 % parten de `ℓ_ω≈0.19437`; terminan con `≈0.31522` sin igualación y `≈0.31691` con igualación energética. Aun cuando la energía cinética inicial se iguala, la información de gradientes difiere entre comparadores: un mismo `Ekin` no implica misma `ℓ_ω`.

**Cociente de avance y diferencia angular:** con `N=48`, el cociente instantáneo `\mathcal K`, discretizado mediante derivadas de registros, presenta valores de ambos signos. En la porción interior de registros, para el control su rango aproximado fue `[-3.02,5.00]`, para la perturbación 14 % `[-2.65,5.30]` y para energía igualada `[-2.60,2.48]`. En esta simulación **no se conserva como constante de sincronización**. Estos rangos son descriptivos y no establecen cotas universales.

**Retornos:** se cuantificaron los primeros cruces de fase de cada marcador. El número y los tiempos dependen del perfil y no establecen órbitas materiales periódicas. Los tiempos y etiquetas están en `O53_RESUMEN.json`.

## 5. Controles, regresión y precisión [E]

`52/52` controles automáticos del posprocesado **PASS**: divergencia, energía decreciente, balances de energía/enstrofía, trayectorias finitas, reproducción O52 para ambos `N`, efecto de perturbación, comparación `N=40/48`, igualdad de energía inicial y cambio de fase aun con energía igualada.

- `max |div u|` es aproximadamente `1.2–1.4×10⁻¹⁵` en todos los ensayos.
- Residuo relativo del balance de energía mediante cuadratura temporal: `~1.1–1.9×10⁻⁵`.
- Residuo del balance de enstrofía mediante cuadratura: `~0.8–1.2×10⁻⁴`.
- Comparación `N=40` vs `N=48` de la perturbación del 14 %: diferencias de avance de aproximadamente `0.000016`, y de desfase `0.002157` vueltas.
- Para el caso de energía igualada: diferencias de avance `0.000051` y de desfase `0.003589` vueltas.
- Los dos controles sin perturbación reproducen las cifras O52 de avance y desfase con tolerancia `10⁻⁵`.

**Advertencia de resolución:** con radio inicial `a=0.35` y `N=48`, el núcleo solo tiene `a/h≈2.67` celdas por radio. Las coincidencias entre mallas son indicios de robustez del observable concreto, **no certificación de convergencia del PDE ni de dinámica a pequeñas escalas**. No se hizo un control explícito de error local del trazador por interpolación ni un régimen de tiempo arbitrariamente grande.

## 6. Falsador de sincronización simple y nueva frontera [F/A]

**Falsación numérica del comparador simple:** la tesis «el avance axial por sí solo reduce cualquier desfase radial producido por perturbaciones 3D» no es compatible con esta familia: el aumento de avance acompaña un aumento de desfase en un grupo de datos; tras igualar energía, el avance y desfase cambian juntos en dirección opuesta. Ningún cociente axial-rotación único describe todas las continuaciones.

Esto **no** refuta la posibilidad de que exista un cierre de sincronización de mayor dimensión o una condición de balance que modere estiramiento bajo hipótesis concretas. Tampoco prueba regularidad general NS 3D.

**Condición pendiente:** identificar una firma `C[u]` invariante frente a observadores permitidos que contenga suficientes relaciones de geometría, dirección, fases y transferencia para determinar la respuesta material de la clase propuesta. Debe demostrarse que las fibras de `C` son invariantes bajo NS o proporcionar una cota certificada del residuo de cierre, y contrastar contra datos adversariales con misma `C` y distinto futuro.

**Siguiente prueba prioritaria:** construir un par de anillos con **igual energía cinética, enstrofía, palinstrofía y geometría inicial**, pero con distinta fase/dirección de modos tridimensionales. Medir `P`, `S(t)` y la transferencia residual. Eso distinguiría si el ritmo y la orientación añaden información predictiva genuina más allá de la escala del espejo. Otra prioridad es definir fases materiales robustas ante deformación no axisimétrica y disponer de mayor resolución en el núcleo.

### Lectura ontológica final

La perpendicularidad permite distinguir relaciones; la sincronización exige una regla dinámica que conserve su compatibilidad en el tiempo. El avance axial está unido al giro por la misma dinámica de vorticidad, pero no se revela como el compensador universal de las diferencias interior/exterior. El cierre de la unidad es una **condición de continuidad de las relaciones suficientes**, no una imposición de igualdad de períodos ni garantía directa de regularidad.

## 7. Reproducibilidad y fuentes

- `o53_perturbed_ring.py`: solver Galerkin NS y marcadores materiales.
- `ejecutar_o53.py`, `ejecutar_control_energia.py`: corridas y controles.
- `analizar_o53.py`: casos, eventos, balances, regresiones, gráficos y 52 afirmaciones comprobables.
- `NS_N*.json`: series originales, con condiciones iniciales, 121 muestras temporales por corrida, marcadores y magnitudes.
- `O53_RESUMEN.json`: resultados y pruebas.
- `o53_desfase_perturbacion.png`, `o53_avance.png`, `o53_estiramiento.png`: figuras.

**Antecedentes internos:** O25, O27, O39, O41–O42, O45–O52, manuscrito de septiembre sobre cierre ortogonal. Los resultados clásicos de regularidad axisimétrica sin *swirl* no deben promocionarse como demostración nueva del problema general tridimensional.
