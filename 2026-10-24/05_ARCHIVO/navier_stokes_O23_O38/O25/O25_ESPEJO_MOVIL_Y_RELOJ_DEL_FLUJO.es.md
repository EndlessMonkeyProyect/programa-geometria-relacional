# O25 — El espejo móvil de Navier–Stokes: referencia endógena y reloj de escala

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 19 de octubre de 2026**  
**Estado:** suplemento formal de integración para evaluación, no modificación del Núcleo ni de la Imagen Total.  
**Etiquetas:** `[O]` lectura ontológica; `[D]` definición o contrato; `[T]` teorema exacto bajo hipótesis; `[E]` ensayo reproducible; `[F]` contraejemplo; `[H]` hipótesis puente; `[A]` abierto.

## 0. Resultado y alcance

[T1] Un radio móvil positivo y suave `ell(t)` y una velocidad de referencia `v_*>0` producen una descripción *exactamente equivalente* de una solución suave de Navier–Stokes incompresible por cambio invertible de espacio, tiempo, velocidad y presión. Ningún canal nuevo, límite causal ni regularidad se desprende de esa equivalencia.

[T2] La definición endógena `ell_omega=(||omega||_2^2/||grad omega||_2^2)^(1/2)`, con `omega=curl u`, transforma la libertad de elegir el espejo en una **regla operacional determinada por el propio flujo** en una caja periódica. La tasa de cambio de esa escala puede escribirse exactamente mediante integrales de vorticidad, estiramiento y disipación. La ecuación de Navier–Stokes sigue siendo la misma: escoger esta referencia no aporta nuevas soluciones ni una cota global a priori.

[T3] Al usar `ell=ell_omega`, la referencia queda normalizada por `||grad_y(curl_y V)||_2^2/||curl_y V||_2^2=1` en las coordenadas móviles, siempre que las integrales sean finitas y el denominador no se anule.

**Pregunta genuina [A]:** ¿se puede deducir del núcleo relacional, sin introducir una selección retrospectiva, una regla para la escala y un observable nuevo que distingan la dinámica propuesta de Navier–Stokes ordinario? También permanece abierta la identificación física `v_*=c`.

## 1. Antes de la matemática: correspondencia de vocabulario [O/D]

El `espejo` es **la operación de representar el mismo flujo desde un radio de referencia**; no una superficie física que se mueve necesariamente en el fluido. La `imagen` es el campo reexpresado en ese marco. El `referente` es la longitud `ell(t)` usada para medir posiciones. El `radio` es una escala observable, no necesariamente una frontera material. La `profundidad` `n=log2(L/ell)` cuenta octavas entre dos referencias; no segundos ni número de remolinos físicos. El `ritmo de lectura` se fija por `ds/dt=v_*/ell`. El `flujo` es `u(x,t)`, con una ley de evolución física independiente de nuestra elección de representación.

**Lo común** a dos imágenes con escalas diferentes es la solución física subyacente, con los observables transformados correctamente. **Cierre de representación** significa que se puede volver entre los dos marcos sin perder información bajo las hipótesis; no es automáticamente `cierre propio` de la ontología ni estabilidad de Navier–Stokes. **Indefinición** es la falta de una regla para seleccionar `ell`, no aleatoriedad del fluido. **Resolución de una diferencia** sería fijar una escala por una consulta reproducible sobre el propio estado `u`; aquí se propone la consulta de vorticidad. **Residuo** es todo lo que esta elección no determina: evolución global, velocidad característica `U_ell`, dinámica de memoria y comportamiento de singularidades.

No identificar el `espejo` de O19–O23 (reflexión geométrica) con la dilatación temporal O25 como una misma operación: son representaciones geométricas distintas hasta que exista un morfismo explícito.

### Concordancia documental preexistente

| Fuente anterior | Resultado a reutilizar | Precisión para O25 |
|---|---|---|
| Núcleo Generativo Canónico; Nota de cierre propio, E9 y MF-86 | comparación, residuo, normalización, suficiencia para preguntas y composición | la normalización de unidades no equivale a control dinámico |
| `ritmo_radio_relatividad_relacional_v0_1.md` | `R_i omega_i=v_*` bajo radio espectral y dinámica oscilatoria declarada | el mismo símbolo `v_*` sólo es una *referencia candidata* en NS, no una velocidad luminosa demostrada |
| `incertidumbre_radio_pseudoinversa_v0_1.md` | otra normalización: `v_*^2=Gamma/beta`; `unidad_minima_incertidumbre_por_direccion` usa `Gamma q0` | no borrar factores de normalización entre los dos convenios |
| `MF43_INTRINSIC_RELATIONAL_CLOCK.md` | orden de actualización, ritmo relativo y tiempo físico distintos | `s(t)` es un tiempo reparametrizado, no el propio tiempo ontológico universal |
| `MF44B_normalizacion_causal_cierre_global_v1.md` | cota causal de red local normalizada, `c_rel=1` | no adjudicar propagación a velocidad finita al PDE parabólico-incompresible |
| `O24_RITMOS_ESPEJO_Y_NAVIER_STOKES.es.md` | tres tasas `v_*/ell`, `U_ell/ell`, `nu/ell²`; octavas no equivalen a ciclos acumulados | se reutilizan definiciones; O25 construye una escala endógena |
| `O23_CONTRATO_MINIMO_DE_INTERFAZ.es.md` | información suficiente depende de preguntas futuras | una escala sola no reconstruye el campo completo ni la memoria |
| `navier_stokes__redistribution_v2.pdf` (junio) | `D_t=P`, Navier–Stokes en `c_DRD=lambda=0`, balance conservativo de memoria | `c_DRD` no se identifica con `v_*` ni con velocidad luminosa |
| `O18` canales por octava | hiperviscosidad requiere crecimiento real del símbolo disipativo | el coeficiente viscoso reescalado `nu/(v_* ell)` no crea hiperviscosidad |

## 2. Teorema O25-T1: equivalencia por representación móvil [T]

Sea `u,p` solución suave sobre `R³` (o un dominio adecuadamente transformado) de

\[
\partial_tu+(u\cdot\nabla_x)u=-\nabla_xp+\nu\Delta_xu+f,\qquad \nabla_x\cdot u=0.
\]

Con densidad constante absorbida en la presión, `nu>0`, una longitud **arbitraria** `ell in C¹`, `ell(t)>0`, y velocidad de referencia fija `v_*>0`, elegir `s(t0)=0` y

\[
 y=\frac{x}{\ell(t)},\qquad \frac{ds}{dt}=\frac{v_*}{\ell(t)}>0,\qquad
 u(x,t)=v_*V(y,s),\quad p(x,t)=v_*^2\Pi(y,s).
\]

Para fuerza original `f(x,t)` definimos `F(y,s)=ell(t) f(ell(t)y,t)/v_*²`. Regla de cadena:

\[
\partial_tu=\frac{v_*^2}{\ell}\,\partial_sV
 -\frac{v_*\dot\ell}{\ell}\, y\cdot\nabla_y V,\quad
(u\cdot\nabla_x)u=\frac{v_*^2}{\ell}(V\cdot\nabla_y)V,
\quad \Delta_xu=\frac{v_*}{\ell^2}\Delta_yV.
\]

Sustituir da exactamente

\[
\boxed{\partial_sV+
\left(V-\frac{\dot\ell}{v_*}y\right)\cdot\nabla_yV
=-\nabla_y\Pi+\frac{\nu}{v_*\ell}\Delta_yV+F,\quad \nabla_y\cdot V=0.}
\tag{O25.1}
\]

La inversa existe mientras `ell>0` y `s` sea estrictamente creciente. El término `-(dot ell/v_*)y·grad V` representa la deriva **de las coordenadas**, no una fuerza descubierta.

**Corrección de dominio necesaria:** si la caja física es el toro periódico de lado fijo `L_box`, el dominio en `y` tiene lado `L_box/ell(t)` y por tanto es **móvil**. El factor `y·grad V` no es un campo periódico global sobre un toro fijo. Se debe trabajar en `R³`, en un mapa local o mantener el toro móvil y sus condiciones de empalme. No es legítimo integrar allí por partes como si las fronteras permanecieran fijas.

La ecuación de presión sigue siendo elíptica: para fuerza con divergencia conocida,

\[
\Delta_y\Pi=-\partial_{y_i}V_j\,\partial_{y_j}V_i+\nabla_y\cdot F.
\]

No se obtiene propagación física de velocidad finita ni desaparece el estiramiento de vorticidad.

## 3. Profundidad, ritmo y movimiento de espejo [T]

Para referente mayor `L(t)>0`, sea

\[
n(t)=\log_2\frac{L(t)}{\ell(t)}.
\]

Se deduce

\[
\boxed{\dot n=\frac1{\ln2}\left(\frac{\dot L}{L}-\frac{\dot\ell}{\ell}\right),\qquad
\frac{dn}{ds}=\frac{\ell}{v_*\ln2}\left(\frac{\dot L}{L}-\frac{\dot\ell}{\ell}\right).}
\tag{O25.2}
\]

Los cocientes adimensionales de O24-R permanecen:

\[
 B_\ell=\frac{U_\ell}{v_*},\qquad D_\ell=\frac{\nu}{v_*\ell},\qquad
\mathrm{Re}_\ell=\frac{B_\ell}{D_\ell}=\frac{U_\ell\ell}{\nu}.
\]

Hay tres tasas diferentes: `ds/dt=v_*/ell` (reparametrización), `dot n` (cambio de profundidad), `U_ell/ell` (recambio advectivo); la tasa viscosa `nu/ell²` agrega una cuarta. Una sin otra no implica sincronización. En particular una evolución con `dot n=0` puede tener `ds/dt>0` y `nu/ell²>0`.

## 4. Teorema O25-T2: seleccionar el espejo mediante vorticidad [D/T]

En el toro físico fijo `T³` supongamos `u` suave, periódico, divergencia cero y `omega=curl u` no idénticamente nula en el intervalo. Definimos

\[
A(t)=\int_{T^3}|\omega|^2dx,\qquad
B(t)=\int_{T^3}|\nabla\omega|^2dx>0,\qquad
\boxed{\ell_\omega(t)=\sqrt{\frac{A(t)}{B(t)}}.}
\tag{O25.3}
\]

`ell_omega` es longitud; por Parseval, `1/ell_omega²` es el promedio de `|k|²` ponderado por `|omega_hat(k)|²`: una medida de escala espectral **sin elegir un único remolino**. En un único modo `|k|`, se reduce a `ell_omega=1/|k|`.

Esta regla usa observables del propio flujo. La transformación (O25.1) con `ell=ell_omega(u)` es todavía un cambio de representación de NS; ahora la escala está fijada por una **condición de normalización** en vez de por gusto del observador. Es global en la caja, no una ley local de seguimiento de cada vórtice.

Sea `S=omega·grad u`, `g=curl f`. Usando `partial_t omega+u·grad omega=S+nu Delta omega+g`, la identidad periódica exacta de producción de enstrofía es

\[
\boxed{\dot A=2\int\omega\cdot S\,dx-2\nu B+2\int\omega\cdot g\,dx.}
\tag{O25.4}
\]

La identidad de palinstrofía es

\[
\boxed{\begin{aligned}
\dot B={}&-2\int (\partial_i\omega_a)(\partial_i u_b)(\partial_b\omega_a)\,dx
+2\int \nabla\omega:\nabla S\,dx\\
&-2\nu\int|\Delta\omega|^2dx
+2\int\nabla\omega:\nabla g\,dx.
\end{aligned}}
\tag{O25.5}
\]

Bajo las hipótesis de suavidad y periodicidad no hay términos de frontera. Por derivación logarítmica:

\[
\boxed{\frac{\dot\ell_\omega}{\ell_\omega}=
\frac12\left(\frac{\dot A}{A}-\frac{\dot B}{B}\right).}
\tag{O25.6}
\]

Para `L` fijo,

\[
\boxed{\dot n_\omega=\frac1{2\ln2}\left(\frac{\dot B}{B}-\frac{\dot A}{A}\right),\quad
\frac{dn_\omega}{ds}=\frac{\ell_\omega}{2v_*\ln2}\left(\frac{\dot B}{B}-\frac{\dot A}{A}\right).}
\tag{O25.7}
\]

**Esto responde al encargo de buscar la velocidad del espejo en el flujo:** está dada por integrales dinámicas de Navier–Stokes. Es una identidad calculable a partir de una solución suave. **No** constituye estimación a priori que garantice que esas integrales permanezcan controladas globalmente.

## 5. Teorema O25-T3: el foco como normalización espectral [T]

Con `u=v_*V`, `x=ell y`, `omega_y=curl_y V`, `omega_x=(v_*/ell) omega_y`, y `dx=ell³dy`, resultan

\[
A_x=v_*^2\ell\,A_y,\qquad B_x=\frac{v_*^2}{\ell} B_y.
\]

Por tanto si `ell=ell_omega=sqrt(A_x/B_x)`, necesariamente

\[
\boxed{\frac{B_y}{A_y}=1.}
\tag{O25.8}
\]

Esta es una **calibración del referente**: el número de onda cuadrático medio ponderado por la vorticidad vale uno en las coordenadas del espejo. No obliga a una partícula central, a una singularidad focal ni al módulo tetraédrico. La información física no se pierde en el cambio de variables; el campo completo y la escala siguen siendo necesarios para reconstrucción inversa.

## 6. Contraejemplo y prueba adversarial [F/T]

En un flujo de cizalla de Navier–Stokes no forzado en un toro, `u=(a e^{-nu k²t}sin(kx₂),0,0)`, el término advectivo es cero. Sus normas `A,B` decrecen, pero `ell_omega=1/k` **permanece fija**, por tanto `dot n=0` si `L` es fijo, a pesar de que el tiempo transcurre y el fluido disipa energía. El reloj `s` sigue avanzando. **El tiempo físico no es idéntico al número de octavas.**

Con dos frecuencias en el mismo perfil de cizalla, `u_1=a e^{-nu k_1²t} sin(k_1x₂)+b e^{-nu k_2²t} sin(k_2x₂)`, el sistema sigue siendo una solución exacta. Para `k1 != k2` y amplitudes no nulas, los modos altos se disipan más rápido, `ell_omega` generalmente aumenta y `n_omega` disminuye si `L` es fijo. No existe una ley universal de aumento de profundidad.

Un mismo `u` puede reescribirse con cualquier `ell(t)>0`; el simple término de deriva no predice algo nuevo. Sólo la elección espectral (O25.3) hace **reproducible** la referencia, no prueba una causalidad física adicional. Si la solución pierde suavidad, las integrales pueden dejar de estar definidas como aquí: la prueba no descarta singularidades.

## 7. Confrontación con DRD, O18 y la regularidad [A]

DRD del preprint de junio usa `partial_t D=P`, `partial_t P+(P·grad)P=-grad Pi+nu Delta P+c_DRD² Delta D-lambda P+S`; la reducción `c_DRD=lambda=0` da NS en `P`. Su término `c_DRD² Delta D` es conservativo para el balance de energía declarado, no equivale a la variación `ell(t)` ni a un canal hiperviscoso.

O18 estudia una **ecuación modificada** con símbolo disipativo por octavas. Reescalar coordenadas no agrega su disipación de alta frecuencia. En (O25.1), `nu/(v_*ell)` aumenta cuando `ell` disminuye, pero eso es sólo su valor **relativo a un reloj más rápido**: en variables originales sigue siendo `nu Delta u`.

Para alcanzar una afirmación de regularidad global habría que obtener, para datos suaves arbitrarios, estimaciones a priori que controlen derivadas pertinentes uniformemente hasta cualquier tiempo. Ni `ell_omega` ni (O25.7) lo hacen por sí solas. El modelo no resuelve Clay.

En particular, **velocidad relacional común** `v_*` no implica una cota `|u|<=v_*`: amplitudes arbitrariamente grandes de una cizalla suave son compatibles con NS matemático. Tampoco se permite identificar `v_*` con `c` luz sin el puente independiente de universalidad y Lorentz.

## 8. Prueba prospectiva y condiciones de integración

1. [D] Fijar `ell_omega` antes de consultar DNS, conservar la elección; comparar con la escala `ell` por gradiente de velocidad o espectro de energía como **alternativas declaradas**, no cambios silenciosos.
2. [E] Calcular `A,B,dot A,dot B` y residuo de (O25.7) con DNS de O17-F y con flujos sintéticos de control. Con una instantánea sola no se estima bien la derivada temporal: usar secuencia con resolución convergente.
3. [F] Control negativo de un modo de cizalla con `dot n=0`; control de dos modos con `dot n<0`; régimen de estiramiento con `dot n` potencialmente positivo.
4. [F] Verificar si el nuevo observable aporta información fuera de la ya contenida en enstrofía y palinstrofía; por ser función exacta de `A,B`, no constituye predicción independiente por sí solo.
5. [H] Para afirmar física nueva, el núcleo debe predecir una relación adicional **no contenida** en NS, por ejemplo una cota o restricción calibrable previamente sobre `dot ell_omega` o sobre transferencia espectral, y contrastarla con casos adversariales.
6. [A] Una vinculación entre este espejo espectral global y los módulos tetraédricos requiere una operación explícita compatible con ambas representaciones. La analogía sola no identifica sus focos.

## 9. Falsadores internos y estados ROSI

- `[RESOLVED | T]` derivación de (O25.1) y (O25.2), inversa bajo condiciones, escala endógena (O25.3) y sus identidades (O25.4)–(O25.8).
- `[RESOLVED | F]` contraejemplo a `tiempo = número de octavas` y a `v_*` como límite automático de NS.
- `[OPEN | H]` equivalencia ontológica física, regla del espejo desde cierre propio, velocidad universal `v_*=c`, cota nueva sobre estiramiento de vorticidad, regularidad global.
- `[NO-GO]` deducir nueva disipación, freno de singularidad o ley cosmológica de un cambio de unidades; confundir coordenada móvil y movimiento real de frontera; colapsar `c_DRD`, `c_rel`, `v_*`, `c` luz.

**Conclusión canónica propuesta:** *Navier–Stokes admite una reconstrucción exacta en un reloj de escala móvil. Si la escala se fija mediante el espectro de vorticidad, el movimiento del espejo es un observable determinado por el propio flujo. El resultado formaliza la comparación de ritmos sin generar una ley física nueva; la hipótesis relacional empieza donde se proponga y pruebe una restricción adicional independiente del cambio de representación.*
