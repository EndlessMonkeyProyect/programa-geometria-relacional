# O85 — Escala crítica, concentración adversarial y límite del certificado recursivo

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**22 de octubre de 2026 · Continuación de O40/O58, O25/O45, O79–O84**  
**Estado:** `[O]` ontología/narrativa; `[T]` proposición analítica exacta en el contrato; `[E]` verificación reproducible; `[F]` prueba adversarial; `[A]` puente pendiente.

> **Alcance:** se prueban identidades de escala y se contrastan familias tridimensionales exactas/instantáneas. No se construye ninguna singularidad de Navier–Stokes, ni se demuestra regularidad global para todos los datos 3D. Las plantillas repetidas NO forman una sola solución del PDE.

## 0. La pregunta del programa, sin redefinir la ontología

La singularidad ontológica es la regla de **cierre propio y continuidad de referencia**, no una forma fija ni un `blow-up` de Navier–Stokes. O40/O58 demostraron transportabilidad aritmética y estela de múltiplos; O25/O45 la comparación de ritmos y escala/tiempo endógenos; O79 la participación decisiva de la fase; O80–O82 presupuestos dinámicos; O83 la mejora al absorber una interacción; O84 una **cuenta acumulada sin cobrar de nuevo el resto**. O85 pregunta qué ocurre cuando la siguiente configuración se concentra en escalas espaciales cada vez menores.

No se identifican por decreto los enteros normalizadores `(N)` de O58, las ramas por pares de la ontología, ni la escala geométrica de un anillo con el entero de dilatación `λ` utilizado aquí. Esta última es una **simetría exacta de la PDE en un toro periódico** cuando `λ` es entero.

## 1. Contrato y presupuesto de O84

Navier–Stokes 3D sin fuerza en `T³=(R/2πZ)³`, `ν>0`, media espacial cero:

\[
\partial_tu+\mathcal N(u)=\nu\Delta u,
\quad\mathcal N(u)=\mathbb P\nabla\cdot(u\otimes u),\quad\nabla\cdot u=0.
\]

Para campos solenoidales periódicos:

\[
R(f)=\sum_{k\ne0}\frac{|\hat f_k|}{|k|},\quad
S(f)=\sum_{k\ne0}|\hat f_k|,\quad
Q(f)=\sum_{k\ne0}|k|\,|\hat f_k|.
\]

Sea `U` una referencia suave **conocida sin usar la solución futura**, `v=u−U`, con defecto `F_U=∂_tU+N(U)−νΔU`. Poner `B=R(F_U)`, `g=(4/ν)S(U)^2`, `G(t)=∫₀ᵗg` y, para referencia sin saltos,

\[
\mathcal C(t)=R(v(0))+\int_0^t e^{-G(s)}B(s)ds.
\]

O84 probó bajo el bootstrap `R(v)≤ν/2`:

\[
\boxed{e^{-G(t)}R(v(t))+\frac\nu4\int_0^t e^{-G(s)}Q(v(s))ds\le\mathcal C(t).}\tag{85.1}
\]

Si los indicadores son conocidos a priori y `e^{G(T)}C(T)<ν/2`, hay continuación en `[0,T]`; para `T*<∞`, controlar también `∫₀^{T*}Q(U)` y mantener los indicadores uniformemente permite el criterio clásico `∫||∇u||∞<∞`. En referencias con saltos se añade su costo, como en O84. No se afirma universalidad de esas hipótesis.

## 2. O85-T1 — Covariancia exacta de todos los costos críticos [T]

Para cada entero `λ≥1` definimos la transformación de Navier–Stokes

\[
\boxed{u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),\quad
p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t).}\tag{85.2}
\]

La misma operación define `U_λ(x,t)=λU(λx,λ²t)` y `v_λ` asociado. Si `f_λ(x)=λf(λx)`, cada coeficiente de frecuencia `k` se traslada a `λk` y su amplitud se multiplica por `λ`. Por tanto:

\[
\boxed{R(f_\lambda)=R(f),\quad S(f_\lambda)=\lambda S(f),\quad Q(f_\lambda)=\lambda^2Q(f).}\tag{85.3}
\]

**Demostración.** En Fourier, `\hat f_λ(λk)=λ\hat f(k)`, y no hay otros modos no nulos. En `R`, el factor de amplitud `λ` se cancela con `|λk|`; en `S` y `Q` quedan `λ` y `λ²`. QED.

El defecto físico de la referencia escala con potencia tres: `F_{U_λ}(x,t)=λ³F_U(λx,λ²t)`, luego

\[
\boxed{B_\lambda(t)=\lambda^2B(\lambda^2t),\quad
G_\lambda(t)=G(\lambda^2t),\quad
\mathcal C_\lambda(t)=\mathcal C(\lambda^2t).}\tag{85.4}
\]

También `∫₀^{T/λ²}Q(U_λ)dt=∫₀^TQ(U)dτ`. Los costos de salto `J_j=R(U_{j-1}-U_j)` se conservan bajo escalado, y el factor integrante acumulado también. Por tanto **el certificado completo O84 es crítico**: conserva exactamente su margen si comprimimos conjuntamente espacio y tiempo.

**Implicación rigurosa:** pasar de `λ=1` a `λ≫1` no mejora automáticamente el margen del certificado ni lo empeora. Cambia la ventana de tiempo físico de `δ` a `δ/λ²`. Ésta es una obstrucción a la propuesta de resolver el régimen difícil mediante un *simple cambio de múltiplo*; no descarta una referencia físicamente nueva que aproveche cancelaciones o nuevas restricciones.

## 3. O85-T2 — Un campo helicoidal grande y globalmente suave [T]

Definimos el campo ABC con coeficientes iguales:

\[
 b(x,y,z)=(\sin z+\cos y,\ \sin x+\cos z,\ \sin y+\cos x).
\]

Verificación directa:

\[
\nabla\cdot b=0,\quad\nabla\times b=b,\quad\Delta b=-b.
\]

**Precisión de norma Fourier:** en cada frecuencia axial aparecen simultáneamente componentes seno y coseno en direcciones vectoriales ortogonales. La norma euclidiana del **coeficiente vectorial** es `a/√2` en cada uno de los dos signos, y las tres parejas suman `3√2 a`. No hay que sumar esas componentes como seis normas escalares independientes.

La identidad vectorial `(b·∇)b=∇|b|²/2−b×(∇×b)` implica que la no linealidad de `b` es un gradiente puro y su proyección solenoidal es nula. Por ello **para cualquier amplitud `a>0` e entero `λ≥1`**

\[
\boxed{u_{a,\lambda}(x,t)=\lambda a e^{-\nu\lambda^2t}b(\lambda x)}\tag{85.5}
\]

es solución exacta suave de NS sin fuerza, con presión `p=−|u|²/2` hasta función de tiempo. Sus presupuestos son:

\[
 R(u(0))=3\sqrt2\,a,\quad
 S(u(t))=3\sqrt2\,a\lambda e^{-\nu\lambda^2t},\quad
 Q(u(t))=3\sqrt2\,a\lambda^2e^{-\nu\lambda^2t}.
\]

En particular,

\[
\boxed{\int_0^\infty Q(u(t))dt=\frac{3\sqrt2\,a}{\nu},\quad
\frac4\nu\int_0^\infty S(u)^2dt=\frac{36a^2}{\nu^2}.}\tag{85.6}
\]

Podemos escoger `a` de manera que `R(u₀)=3√2 a≫ν`, y `λ` arbitrariamente grande. La vorticidad inicial crece como `λ²`, **sin singularidad dinámica**, porque la disipación también se intensifica según `λ²`. Si usamos `U=u` como control exacto de esta **familia explícita**, entonces `v=0` y el defecto es cero. Ello demuestra que el criterio pequeño aplicado a todo el campo no es necesario. No ofrece un método universal para encontrar una referencia exacta a partir de datos arbitrarios.

## 4. O85-T3 — Campo 3D no-Beltrami: mismo margen, tiempo cada vez menor [T/E]

Retomamos el dato de O84 con `ν=1`:

\[
u_0(x,y,z)=(4\sin y,\ \sin z,\ \sin x),
\quad W=\mathcal N(u_0)=(4\sin z\cos y,\ \sin x\cos z,\ 4\sin y\cos x).
\]

Su referencia inicial es `U⁰=e^{-t}u₀`. La primera actualización que incorpora los doce modos nuevos es:

\[
\boxed{U^1(t)=e^{-t}u_0-te^{-2t}W.}\tag{85.7}
\]

Sobre el intervalo `δ=9/500=0,018`, O84 prueba exactamente:

\[
M_0=0.519488712836\ldots>\tfrac12,
\quad M_1\le0.271724746561\ldots<\tfrac12.
\]

Escalamos el **mismo campo inicial** con cada entero `λ`: `u_{0,λ}(x)=λu₀(λx)`, y sus dos referencias correspondientes, a viscosidad fija `ν=1`. De (85.3)–(85.4), los presupuestos son **idénticos** en `δ_λ=δ/λ²`.

| `λ` | `δ_λ` | `M₀` | `M₁` (cota) |
|--:|--:|--:|--:|
|1|0.018|0.5194887|0.2717247|
|2|0.0045|0.5194887|0.2717247|
|4|0.001125|0.5194887|0.2717247|
|8|0.00028125|0.5194887|0.2717247|
|16|0.0000703125|0.5194887|0.2717247|

**Control de costo no despreciable.** El soporte de Fourier de `U⁰` (ondas base de frecuencia 1) es disjunto del de `D=U¹−U⁰=−te^{-2t}W` (frecuencias de magnitud `√2`). Por ello **la norma de Wiener `Q` suma sin cancelación entre ambas partes**:

\[
\int_0^\delta Q(U^1)dt=6(1-e^{-\delta})+
9\sqrt2\frac{1-(1+2\delta)e^{-2\delta}}4
\approx 0.10904690476.\tag{85.8}
\]

Esta cantidad, como el margen del certificado, es independiente de `λ` bajo la compresión física del intervalo. Cada plantilla concentrada puede pasar el certificado y, sin embargo, tener un **costo positivo por bloque** que no se hace más pequeño con el radio espacial.

## 5. O85-F1 — El escenario Zeno que la escala por sí sola no prohíbe [F]

Consideremos **plantillas independientes**, cada una igual a la referencia anterior escalada por `λ_j=2^j`, con intervalos de duración `δ/4^j`. La suma formal de duraciones es

\[
\boxed{\sum_{j=0}^\infty\frac\delta{4^j}=\frac{4\delta}{3}<\infty,}
\]

mientras la suma de los costos de referencia de (85.8) diverge porque cada bloque aporta la misma cantidad positiva:

\[
\boxed{\sum_{j=0}^\infty\int_{I_j}Q(U^1_{2^j})dt=+\infty.}\tag{85.9}
\]

**Límite lógico esencial:** estas referencias reescaladas son **problemas iniciales diferentes**. Concatenarlas no construye una trayectoria suave de NS y mucho menos un blow-up. Las diferencias entre campos en las transiciones no están controladas ni son nulas. La construcción sólo refuta la inferencia «un margen crítico idéntico en cada escala basta para que el costo total de una cadena sea finito». En O84 la suma de costos y los eventuales saltos deben controlarse realmente en **la misma evolución**.

## 6. O85-T4 — Fases adversas sobreviven al escalado [T]

O79 construyó datos de cuatro ondas que dependen genuinamente de las tres coordenadas, con un receptor `m=k+l` y fase relativa `c=±1/4`. A viscosidad `ν=0.01`, para `λ=1` sus transferencias no lineales al modo receptor son `±0.125`, aunque comparten sus módulos de Fourier. Aplicando (85.2) con factor entero `λ`:

\[
\boxed{T_{m,\lambda}^{(\pm)}=\pm0.125\lambda^4,\quad
D_{m,\lambda}=-0.005625\lambda^4.}\tag{85.10}
\]

El escalado no borra la información de fase: aumenta simultáneamente la rapidez de las transferencias y de la disipación. Las transferencias de signo contrario siguen siendo diferentes aun si sus **magnitudes iniciales normalizadas** y su estructura de escala coinciden. No basta trasladar el entero normalizador para predecir cuál de esas orientaciones de transferencia se realiza.

## 7. La proposición que requeriría O86 [A]

El resultado adversarial muestra por qué es necesaria una **ley real de ganancia entre cierres**. Un objetivo que sí implicaría continuación para datos suaves 3D periódicos es construir, **sólo desde el dato inicial y actualizaciones explícitas que no dependan de conocer el futuro de `u`**, referencias sobre cada tiempo finito `T` tales que:

\[
\boxed{\sup_{t<T}e^{G(t)}\mathcal C(t)<\nu/2,
\qquad \int_0^T Q(U(t))dt<\infty.}\tag{85.11}
\]

La cuenta `C` y `G` son las de O84 e incorporan costos de saltos si existen. Para todo `T` finito, estas dos cotas permitirían el criterio conocido `∫₀ᵀ ||∇u||_∞dt<∞`, sin presuponer suavidad global. **No hemos demostrado que referencias con esas propiedades puedan construirse para todo dato suave 3D.** Conseguirlo en esa generalidad sería un teorema mayor, no una mera normalización aritmética.

O86 debería enfrentar **una evolución única** con fases y escalas acopladas, proponiendo una desigualdad que haga decrecer el costo físico de los nuevos cierres, o que encuentre una cancelación a priori justificada por la propia PDE. Debe medir tanto los nuevos modos como la intensidad que transportan; debe tratar `λ` como variable física solo cuando se derive una regla observable que lo vincule al normalizador cardinal del programa.

## 8. Registro epistemológico y reproducción

| Enunciado | Clasificación |
|---|---|
| `R,S,Q,B,G,C` transforman según (85.3)–(85.4) | `[T]` Exacto |
| Beltrami ABC da soluciones 3D de amplitud arbitraria y regularidad global | `[T]` Exacto |
| La actualización 3D O84 conserva margen bajo reescala entera | `[T]` Exacto |
| Dos fases con mismas magnitudes transfieren en sentidos opuestos | `[T]` Instante inicial de O79 |
| Plantillas reescaladas permiten tiempo acumulado finito y costo formal infinito | `[F]` Ejemplo de presupuestos separados, **no solución NS** |
| Referencias O84 uniformes para todo dato y todo tiempo físico | `[A]` Abierto |
| Singularidad ontológica = blow-up de NS | `[F]` Identificación inválida sin puente |

Ejecutar `python3 codigo/verificar_o85.py` para las identidades, escalado y contrastes; genera `resultados/verificacion.json`. `python3 codigo/graficar_o85.py` genera las figuras (NumPy y Matplotlib). **Las identidades y cotas se prueban analíticamente; los controles digitales son auxiliares.**

**Interpretación final:** el eco puede conservar perfectamente la referencia mientras la intensidad y la tasa del cambio de escala se reorganizan. La prueba relevante para regularidad no es la existencia de la cadena aritmética, sino que la dinámica de una misma solución impida que el costo de concentraciones sucesivas deje de ser integrable en tiempo finito.
