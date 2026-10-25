# O77 — Semilla finita y cierre dinámico de un perfil toroidal

**Programa de Geometría Relacional** — Le Matt Ansatz Di Ego  
**22 de octubre de 2026** · suplemento independiente posterior a O76  
**Estatus:** `[O]` ontología del programa, `[N]` narrativa, `[D]` resultado exacto demostrado, `[E]` comprobación computacional, `[H]` hipótesis abierta, `[F]` criterio adversarial. **No se ha demostrado la regularidad global de Navier–Stokes 3D.**

## 0. El orden del programa: no partir de energía [O/N]

La unidad se propone como una relación que consigue cierre propio; la proyección exterior permite reconocer comunes y diferencias, pero suprimir la caja no significa suprimir las interacciones físicas. Los radios y las frecuencias son manifestaciones geométricas y dinámicas de la relación, no una definición inicial mediante energía. El múltiplo normalizador entero y la diferencia pendiente son conceptos propios de la ontología; **no identificarlos a posteriori** con el número de parámetros de un perfil gaussiano, con el orden del grupo de espejos, ni con la viscosidad.

**Pregunta O77:** ¿puede una semilla pequeña compuesta de radios, ancho del núcleo, amplitud y posición determinar **exactamente** el siguiente estado de un anillo de Navier–Stokes? Para probar una proposición positiva se necesita una familia invariante; para refutar la suficiencia de una familia concreta basta demostrar que el vector de evolución de la ecuación sale de su espacio tangente en un instante.

## 1. La clase física: anillo axisimétrico sin giro azimutal [D]

Trabajamos en todo el espacio tridimensional, con coordenadas cilíndricas `(r,θ,z)` y campo

\[
u=u^r(r,z,t)e_r+u^z(r,z,t)e_z,\quad u^\theta\equiv0,\quad\nabla\cdot u=0.
\]

Esto **no** significa que no haya rotación: las partículas giran en la sección meridiana del toroide; lo ausente es el desplazamiento alrededor del eje azimutal `e_θ`. La vorticidad es toroidal `ω=ω^θ e_θ` y la variable exacta de O73 es

\[
\eta=\frac{\omega^\theta}{r},\qquad
\partial_t\eta+u^r\partial_r\eta+u^z\partial_z\eta
=\nu\left(\partial_{rr}+\frac3r\partial_r+\partial_{zz}\right)\eta.
\tag{77.1}
\]

Este sector es dinámicamente invariante y su regularidad global, bajo condiciones usuales de suavidad y decaimiento, es un resultado clásico. **Que la clase sea invariante no implica que una subfamilia de cinco números lo sea.** Véanse Ladyzhenskaya y Ukhovskii–Yudovich, y síntesis en Gallay–Šverák y Hmidi–Rousset.

## 2. Una semilla toroidal suave de cinco parámetros [D]

Elijamos `A≠0`, `α>0`, `β>0`, `b>0` y centro `z₀` (trasladaremos a `z₀=0` para el cálculo). Con `y=r²`, sea

\[
Q=\alpha(y-b)^2+\beta(z-z_0)^2,\quad
\phi=Ae^{-Q},\quad \Psi=r^2\phi.
\tag{77.2}
\]

Definimos el campo por la función de corriente:

\[
u^r=-\frac1r\partial_z\Psi=2\beta r(z-z_0)\phi,\qquad
u^z=\frac1r\partial_r\Psi=\bigl(2-4\alpha y(y-b)\bigr)\phi.
\tag{77.3}
\]

Las identidades `∂_r u^r + u^r/r +∂_z u^z=0`, suavidad en el eje y decaimiento rápido son exactas. La familia constituye datos iniciales físicos admisibles en `R³` de un flujo localizado. Al escoger `b=R²`, `α=1/(4R²a²)` y `β=1/a²`, su función de corriente se concentra en la vecindad de un toroide de radio mayor `R` y ancho `a`. **No es un anillo de circulación exclusivamente de un signo; la vorticidad puede tener lóbulos secundarios de signo contrario.** Se usa como familia adversarial de perfiles toroidales suaves, no como perfil universal de todos los anillos.

En estas variables, la vorticidad normalizada se escribe

\[
\eta=Ae^{-Q}P(y,z),\tag{77.4}
\]

\[
P=2\beta-4\beta^2 z^2+24\alpha y-16\alpha b-16\alpha^2y(y-b)^2.
\tag{77.5}
\]

Sus cambios infinitesimales de amplitud, radios (`b,α,β`) y posición `z₀` pertenecen al espacio tangente de funciones de la forma `e^{-Q}` multiplicada por polinomios en `y,z`.

## 3. Teorema O77.1: la semilla gaussiana NO es una familia NS invariante [D]

**Proposición:** para `A≠0`, `α>0`, `β>0`, `b>0`, no existe una evolución diferenciable de esos cinco parámetros que satisfaga exactamente (77.1) en todo un intervalo temporal alrededor del instante inicial, para ninguna viscosidad finita `ν≥0`.

**Prueba.** Partiendo de (77.3) y (77.4), el transporte no lineal tiene la forma

\[
u^r\partial_r\eta+u^z\partial_z\eta=A^2e^{-2Q}\,\mathcal N(y,z),\tag{77.6}
\]

con el polinomio explícito

\[
\mathcal N=
4\beta yz\,[\partial_yP-2\alpha(y-b)P]
+[2-4\alpha y(y-b)]\,[\partial_zP-2\beta zP].
\tag{77.7}
\]

Al expandirlo en potencias de `z`, su coeficiente de `z³` es exactamente

\[
\boxed{[z^3]\mathcal N=16\beta^3\ne0.}\tag{77.8}
\]

Por otro lado, `∂t η` a lo largo de cualquier trayectoria diferenciable de cinco parámetros es `e^{-Q}` por un polinomio, y `νΔ₅η` es igualmente `e^{-Q}` por un polinomio. Para satisfacer (77.1) sería necesario que, en cada `y>0` fijo,

\[
P_1(z)=A^2 e^{-Q(y,z)}\mathcal N(y,z)\tag{77.9}
\]

para algún polinomio `P₁`. Cuando `|z|→∞`, el miembro derecho converge a cero; por tanto, el polinomio `P₁` tendría que ser idénticamente cero. Pero (77.8) prueba que el miembro derecho no lo es. Contradicción. **QED.**

El argumento es exacto y muestra **no invarianza de esta familia gaussiana concreta**, no imposibilidad de todas las familias finitas imaginables. El mismo argumento impide un cierre por simple traslación axial uniforme: la traslación sólo modifica la derivada tangente `∂_{z₀}η`.

Una instancia algebraica verificable es `α=1/4, β=1, b=y=1, z=1/2`, para la que `\mathcal N=-2`.

## 4. Prueba numérica del defecto de cierre [E]

Escogimos `R=1`, `a=0.32`, `A=0.24`, `b=1`, `α=1/(4a²)`, `β=1/a²`. Medimos la tasa exigida por (77.1) y su proyección ortogonal ponderada sobre el espacio tangente de cinco parámetros. Peso `r dr dz`, integrado en `r∈[0.001,2.35]` y `z∈[-1.2,1.2]`. La región es truncada para el cálculo, no la prueba matemática. Como el peso constante `2π` cancela, no aparece en el cociente.

| Puntos radiales | ν | Residuo relativo del transporte no lineal | Residuo relativo de todo `∂tη` |
|---:|---:|---:|---:|
|100|0|0.7989230|0.7989230|
|160|0|0.7989230|0.7989230|
|100|0.025|0.7989230|0.3223736|
|160|0.025|0.7989230|0.3223740|

**Interpretación:** en el ejemplo escogido, casi el 80% de la norma del transporte no lineal cae fuera de las direcciones infinitesimales que esta semilla de cinco parámetros puede cambiar. Para ν=.025, el residuo de toda la tasa equivale aproximadamente a 32.24% de su norma. **No son errores de solución numérica ni una simulación temporal:** son residuos instantáneos de aproximación del vector de evolución. El teorema no depende de esos porcentajes. El valor de los residuos depende del perfil, parámetros y dominio de integración.

## 5. Control positivo: el vórtice de Lamb–Oseen [D]

Es posible una semilla finita exacta si la dinámica respeta su familia. Para un vórtice plano axisimétrico en rotación, extendido como una **columna** en la dirección `z`, considérese

\[
\omega_z(r,t)=\frac{\Gamma}{\pi w(t)}e^{-r^2/w(t)},\quad
u_\theta(r,t)=\frac{\Gamma}{2\pi r}(1-e^{-r^2/w(t)}),\quad
\boxed{w(t)=w_0+4\nu t}.\tag{77.10}
\]

La relación `w'=4ν`, junto con `Γ` constante, satisface exactamente la ecuación de vorticidad de este flujo (la presión radial equilibra la aceleración centrípeta). Para `w₀>0`, la solución es suave desde el inicio. El script verifica simbólicamente su ecuación de difusión.

**No es un anillo vorticial tridimensional localizado:** es una columna con la misma sección para todo `z` y no está en la clase de energía finita del problema Clay en `R³`. Sirve únicamente como control matemático positivo de **semilla finita dinámica suficiente**. La existencia de esta familia no resuelve el cierre del anillo.

## 6. El espejo y el anillo: simetría no equivale a compresión [D/N]

El grupo `D₄` de O70/O76 rota y refleja el plano `(x,y)`. Todo campo de la forma (77.3) es **invariante como campo vectorial** bajo esas operaciones: `g u(g⁻¹x)=u(x)` (actúan sólo sobre el plano transversal). Por tanto

\[
\mathcal P_{D_4}u=u.\tag{77.11}
\]

La caja conserva, en este caso, toda la **simetría angular**; pero no comprime el perfil meridiano arbitrario `η(r,z)` en cinco parámetros. El cierre por grupo de simetría es exacto y aun así su clase es infinita-dimensional. Ésta es la diferencia entre **una familia cerrada por sus comunes** y **una semilla que determine todo su siguiente estado**.

También la literatura de anillos viscosos usa perfiles gaussianos y traslación como aproximaciones controladas en ciertos regímenes, no como familias universales exactas: Gallay y Šverák, *Vanishing viscosity limit for axisymmetric vortex rings*, 2024.

## 7. Ontología, interpretación y falsadores [O/H/F]

- `[O]` «Apagar la caja» puede representar dejar de calcular proyecciones exteriores. El sistema físico sigue transportando y generando relaciones.
- `[D]` En esta familia suave los cambios de `A,R,a,z₀` no pueden absorber el término `e^{-2Q}` generado por las interacciones. El múltiplo normalizador **no fue derivado** de tal término.
- `[H]` Una semilla dinámica ampliada podría incorporar perfiles secundarios, tensores o funciones de memoria. No está probado que exista un cierre autónomo **finito** que reconstruya un anillo viscoso genérico.
- `[F]` Cualquier propuesta de evolución autónoma de los cinco parámetros para esta familia debe reproducir en el instante inicial todo el miembro derecho de (77.1); ya sabemos que no puede hacerlo exactamente.
- `[F]` Una propuesta que agregue un solo perfil `e^{-2Q}` debe volver a ser sometida al vector de evolución. Nada garantiza que sus nuevas interacciones dejen de generar otros perfiles.
- `[H]` Una ruta práctica es construir una **jerarquía de términos con errores certificados** e investigar si el resto se controla por la regla de referencia. Éste es un problema distinto de afirmar un teorema global para NS 3D.

**Resultado central:** una caja puede aislar un común verdadero y una semilla puede describir un radio y un ritmo, sin que esos datos sean dinámicamente suficientes. O77 exhibe un término exacto que no cabe en esa semilla y un control exacto positivo donde sí cabe. Para O78, investigar una semilla ampliada con un segundo perfil y cuantificar si el defecto decrece de manera controlable, sin hacer pasar una expansión infinita por un múltiplo finito derivado.

## 8. Reproducción, documentos y antecedentes

- Script: `codigo/verificar_o77.py`, usa `sympy`, `numpy`, `matplotlib`; ejecuta las pruebas algebraicas, proyección tangente ponderada y dos figuras.
- `datos/resultados_o77.json`, `datos/residuos_o77.csv` contienen los valores.
- Las pruebas ejecutadas son de **identidad simbólica y consistencia numérica**, no una integración 3D con garantías de convergencia PDE.
- Referencias comparativas externas (no fundamentos ontológicos):
  - Gallay y Šverák, *Vanishing viscosity limit for axisymmetric vortex rings*, versión 2024: https://www-fourier.univ-grenoble-alpes.fr/~gallay/Vanishing.pdf
  - *Global well-posedness for the Navier–Stokes–Boussinesq system with axisymmetric data*, sección sobre Navier–Stokes sin giro azimutal y variable `ωθ/r`: https://www.numdam.org/article/AIHPC_2010__27_5_1227_0.pdf
  - Descripción de solución Lamb–Oseen en literatura técnica: https://escholarship.org/uc/item/19q6q8rf

**Estado de la pregunta Clay:** abierto para datos tridimensionales suaves generales sin forzamiento; O77 no es una demostración de regularidad ni de explosión en tiempo finito.
