# O24-R — Espejo en movimiento, ritmos de escala y Navier–Stokes

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 19 de octubre de 2026**  
**Tipo:** suplemento exploratorio independiente para la Imagen Total. No modifica la versión canónica ni sustituye la rama geométrica O24.  
**Claves epistémicas:** [O] ontología; [D] contrato/hipótesis; [T] deducción exacta bajo contrato; [E] ejemplo numérico; [F] falsador o contraejemplo; [A] puente abierto.

## 1. Narrativa antes de las ecuaciones [O]

El cubo de espejos no sirve aquí como reloj absoluto sino como una arquitectura de referencias: una imagen reconocible puede reconstituirse a diferentes radios. El remolino transportado por un fluido puede cambiar de escala local a la vez que se cambia la escala de observación. La *profundidad relacional* mide la distancia entre esas escalas; el *ritmo* mide una tasa de evolución declarada. El primero no equivale automáticamente al segundo.

## 2. Antecedentes auditables: NO derivar c de nuevo [D/T]

- `ritmo_radio_relatividad_relacional_v0_1.md`, septiembre: para el comparador métrico con autovalores positivos `lambda_i`, `R_i=lambda_i^(-1/2)`, `omega_i=sqrt(Gamma lambda_i)`, entonces `R_i omega_i=sqrt(Gamma)=v_*` (realización exacta con estas definiciones).
- `incertidumbre_radio_pseudoinversa_v0_1.md` y `unidad_minima_incertidumbre_por_direccion_v0_1.md`: con otra normalización, `R_i=sqrt(q0/lambda_i)`, `omega_i=sqrt(Gamma lambda_i)`, de donde `v_*=sqrt(Gamma q0)`. Estas dos definiciones de radio NO se deben fusionar olvidando q0.
- `MF44B_normalizacion_causal_cierre_global_v1.md`: localidad de radio uno da `c_rel=1` en enlaces/actualización; identificar su conversión dimensional con velocidad luminosa física c es puente abierto.
- La realización espectral fija una velocidad *común entre modos*, si Gamma y q0 son comunes. Identificarla con la luz requiere causalidad física universal y Lorentz, no obtenidas aquí.
- Navier–Stokes continuo incompresible es parabólico y su presión satisface una restricción elíptica global; NO hereda automáticamente una cota causal finita de MF44.

## 3. Teorema de cociente de ritmos de dos escalas [T]

Supóngase que en un mismo instante `t` la escala global `L(t)>0` y la local `ell(t)>0` pertenecen a una misma familia espectral con `v_*(t)>0` independiente del modo y frecuencias adiabáticas o nominales `omega_L=v_*/L`, `omega_ell=v_*/ell`.

Definir profundidad:

`n(t) = log_2(L(t)/ell(t))`.

Entonces, exactamente para las frecuencias nominales,

`omega_ell/omega_L = L/ell = 2^n`.

Y si `L,ell` son diferenciables:

`dn/dt = (dot L/L - dot ell/ell)/ln 2`.

La igualdad entre frecuencias **instantáneas** no garantiza que las fases de dos osciladores no autónomos satisfagan `dot phi=omega`: el parámetro de frecuencia instantánea es exacto en la ecuación congelada, pero su interpretación como ciclos observables necesita evolución dinámica y, usualmente, régimen adiabático `|dot ell|/v_* << 1` y `|dot L|/v_* <<1` (más condiciones si v_* varía).

## 4. Tres relojes locales que hay que mantener distintos [D/T]

Para viscosidad cinemática `nu>0`, escala `ell>0` y velocidad típica de fluctuación `U_ell>0`, declaramos tasas de orden de magnitud (no todas son frecuencias oscilatorias):

- `omega_* = v_*/ell`: ritmo de propagación de la familia relacional hipotética.
- `omega_adv = U_ell/ell`: tasa advectiva / de recambio del remolino.
- `omega_nu = nu/ell^2`: tasa de difusión viscosa.

Sus cocientes adimensionales exactos **por definición de estas tasas características** son:

`B = omega_adv / omega_* = U_ell/v_*`;

`D = omega_nu / omega_* = nu/(v_* ell)`;

`Re_ell = omega_adv/omega_nu = U_ell ell/nu = B/D`.

No existe una sola 'sincronización': `B=1` compara advectivo con propagación, `D=1` compara viscosa con propagación y `Re_ell=1` compara advectivo con viscoso. Estas superficies son diferentes.

**Falsador directo de una equiparación de relojes:** elegir `U_ell=v_*/100`, `nu=v_*ell/100` produce `B=D=0.01`, `Re_ell=1`: advección y viscosidad están sincronizadas, pero ninguna con la escala propagativa. El modelo debe distinguirlo.

## 5. Qué ocurre en cada octava [T]

Para `ell_j=L/2^j` y v_*, nu constantes:

`omega_*,j= (v_*/L) 2^j`;

`omega_nu,j = (nu/L^2) 4^j`;

`D_j = (nu/(v_* L)) 2^j`;

`B_j = U_j / v_*` (sin regla para U_j, no hay ley del flujo);

`Re_j = (U_j L/nu) 2^(-j)`.

Si como experimento adicional `U_j=U_0 2^(-h j)`, `Re_j=Re_0 2^(-(h+1)j)` y `B_j=B_0 2^(-hj)`. El exponente h viene del escenario dinámico, no de la ontología. **El hecho que D_j se duplique no es la ganancia disipativa sqrt(2) exigida en el canal hiperviscoso O18**: aquella requiere una modificación real del símbolo disipativo, no cambiar unidades de comparación.

Existe una longitud de igualdad entre tasas `ell_*=nu/v_*`. **No es** una longitud fundamental: puede estar fuera del régimen donde Navier–Stokes incompresible o el modelo de propagación sea físico.

## 6. Teorema de no equivalencia: octavas infinitas ≠ ciclos infinitos [T/F]

Sea T finito, `ell(t)=a sqrt(nu(T-t))`, `a>0`, y L positivo constante. La ley de escala se adopta como **escenario hipotético de concentración**, no como un teorema general de Navier–Stokes.

Cuando `t->T^-`:

`n(t)=log_2[L/(a sqrt(nu(T-t)))] -> +infinito`.

`omega_*(t)=v_*/(a sqrt(nu(T-t)))`.

La acumulación formal de fase propagativa en `[t0,T)` es **finita**:

`int_(t0)^T omega_* dt = [2 v_*/(a sqrt(nu))] sqrt(T-t0) < infinito`.

Por el contrario, la acumulación de unidades de difusión viscosa **diverge**:

`int_(t0)^(T-eps) omega_nu dt = (1/a^2) ln[(T-t0)/eps] -> infinito`.

Si la velocidad local estuviese además uniformemente acotada `U_ell(t)<=v_*`, la fase advectiva característica `int omega_adv dt` también estaría acotada por la fase propagativa finita. **Pero no se ha demostrado U_ell<=v_* para Navier–Stokes.** En el escenario autosimilar de velocidad `U_ell ~ nu/ell`, el número formal de recambios advectivos diverge logarítmicamente, y `U_ell/v_*` diverge también.

Aún más: `|dot ell|/v_* = a sqrt(nu)/[2 v_* sqrt(T-t)] -> infinito`. La hipótesis de adiabaticidad falla antes de T, por lo que el integral de `omega_*` sólo debe leerse como *conteo nominal por una familia congelada*, no necesariamente como ciclos reales del oscilador dinámico no autónomo.

**Moraleja formal:** `n -> infinito` no implica `int omega_* dt -> infinito`. La 'infinitud de octavas' y la 'infinitud del tiempo vivido' NO son equivalentes. Este es un discriminante preciso para el lenguaje ontológico.

## 7. Relación con DRD y Navier–Stokes [A]

El preprint «Incompressible flow as redistribution of accumulated difference» (v2, junio de 2026) usa memoria `D` con `P=partial_t D`, advección y viscosidad para P, restitución conservativa `c_DRD^2 Delta D` y fricción `-lambda P`; si c_DRD=lambda=0 se recupera Navier–Stokes exacto en P. El c_DRD **no es** el c de luz ni `v_*`, salvo un puente adicional. La restitución del campo acumulado NO representa automáticamente disipación hiperviscosa ni regularidad.

Posible experimento futuro, por declarar: definir una escala local observable `ell(x,t)` a partir de espectro o vorticidad, una escala referente `L(t)`, un ritmo `v_*/ell`, y contrastar en datos DNS los cocientes B, D y Re. Para un puente dinámico verdadero, construir una ley de transporte/evolución de la escala con balance de energía, contrastarla frente a Navier–Stokes convencional y evitar reintroducir U_ell como resultado supuesto.

## 8. Falsadores y siguiente decisión

[F1] Las escalas L y ell no pertenecen a la misma familia espectral con una velocidad común: la razón de ritmos deja de ser L/ell. [F2] Los datos no sostienen el vínculo entre escala geométrica y el radio espectral adoptado. [F3] Las frecuencias nominales no predicen fases medibles de la evolución no autónoma. [F4] Una ley propuesta para U_ell contradice el balance de energía o la dinámica NS. [F5] La longitud ell_* queda fuera de dominio de la descripción continua. [F6] La supuesta velocidad física universal no resulta invariante tras la calibración.

**Estado final:** teorema geométrico-espectral y comparaciones dimensionales `[T]`, lectura de reloj `[O]` y puentes Navier–Stokes/relatividad `[A]`. No se deriva c física, un tiempo absoluto, una fuerza, una nueva disipación, ni regularidad global de NS.
