---
title: "O47 — El espejo que continúa: información necesaria para actualizar el tiempo relacional"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-20"
status: "Resultados exactos sobre derivadas en el instante inicial; evolución Galerkin 3D de duración finita, trazadores; NO prueba de regularidad global"
parents: ["MF-43", "MF-86", "MF-97", "O25", "O39", "O40", "O41", "O42", "O43E", "O44", "O44N", "O45", "O46"]
---

# O47 — Continuidad de la unidad y suficiencia temporal de un espejo normalizado

## 0. Resultado

La ontología mantiene: una singularidad relacional es una totalidad que se sostiene por su cierre propio y una referencia normalizadora; el desplazamiento del espejo hace comparables ritmos del flujo, de su referente espacial y de una partícula. **Eso no equivale a afirmar que un MCM aritmético sea un invariante físico, ni que una fase aislada determine la evolución.**

**T1 (exacto en una familia de campos iniciales suaves de NS 3D).** Existen dos datos con el mismo mínimo común múltiplo de números de onda, la misma enstrofía `E`, palinstrofía `J`, escala espectral endógena `ell_omega=sqrt(2E/J)`, bispectro triádico de fase `beta`, y la misma derivada inicial de `E`, pero diferente derivada inicial de `J` y, por consiguiente, diferente derivada inicial de `ell_omega`. En el control adversarial B se iguala, además, la **energía cinética**. Hay estiramiento de vorticidad local no nulo en los datos. **Conclusión:** estas interfaces no son dinámicamente suficientes para predecir la siguiente escala del espejo en la familia ensayada.

**E1 (experimento reproducible).** Un solucionador pseudospectral Galerkin 3D, filtro 2/3, RK4, `nu=.03`, dominios periódicos `T^3`, para `T=.12`, confirma la divergencia de `ell_omega(t)`, del reloj de escala `s(t)=integral (1/ell_omega) dt` (`v_*=1` elegido) y de la evolución de marcadores materiales. Resoluciones 24³, 32³ y 48³; control temporal `dt=.004` frente a `.002` en 32³; segundo experimento 32³ y 48³. Esta evidencia NO controla el límite continuo de todos los datos ni tiempos ilimitados.

## 1. Vocabulario y jerarquía

- **[O] singularidad/cierre propio:** totalidad de relaciones normalizadas con indefiniciones contextuales pendientes; no es blow-up analítico.
- **[O/D] desplazamiento del espejo:** cambio de foco, radio u orientación que modifica comparaciones. Cambiar coordenadas no genera por sí una nueva fuerza física ni un tiempo absoluto.
- **[D] reloj de escala:** `s(t)=int v_*/ell_omega dt`; un parámetro operacional, **no** la demostración de un reloj físico universal de la singularidad.
- **[D] marcador material:** solución de `dot X=u(X,t)`; se compara contra otro marcador que hace de referente *explícitamente etiquetado*, no contra un foco ontológico único ya identificado.
- **[D] interfaz suficiente:** `C(u)=C(v)` obliga a `C(Phi_t(u))=C(Phi_t(v))` para todos los estados y tiempos admitidos, tal como exige O41-T1/MF-97. Si los derivados iniciales de una componente observada difieren, la suficiencia fracasa sin tener que esperar una simulación larga.

## 2. Familia tridimensional: forma inicial y pruebas

Sea `psi(x,y)=A cos x + D cos y + B cos(x-y)`, con `A=1`, `D=.7`, `B=.4`, y

`h(z)=sum_{k in K} (a_k/k) cos(k z)`.

Tomamos datos iniciales en `T^3`:

\[
 u_0=(\partial_y\psi,-\partial_x\psi+h(z),0),\qquad
 \omega_0=(f(z),0,W(x,y)),\quad f(z)=\sum_k a_k\sin(kz),\;W=-\Delta_{xy}\psi.
\]

Son suaves, libres de divergencia. El estiramiento `(omega·grad)u` **no es cero en general**; el integral de producción `P(0)=<omega·(omega·grad)u>` sí se anula por ortogonalidad en el plano. Se invoca existencia local clásica de solución suave a partir de esos datos, **sin imponer que el ansatz sobreviva tras `t=0`**.

Para promedio espacial y enstrofía `E=1/2<|omega|²>`:

\[
 E(0)=\tfrac14(A^2+D^2+4B^2+\sum a_k^2),\quad
 J(0)=\tfrac12(A^2+D^2)+4B^2+\tfrac12\sum k^2a_k^2,\quad
 \ell_\omega^2=\frac{2E}{J}.
\]

El bispectro planar, invariante por traslaciones, es `beta=Re(conj(psi_hat_(1,0))*psi_hat_(0,1)*psi_hat_(1,-1))=ADB/8=.035`. La energía cinética depende también de `sum a_k²/k²`.

## 3. Prueba A — tres modos con la misma interfaz O46 ampliada

Se usan `K={2,3,4}`, con dos repartos de amplitudes de vorticidad axial:

- I: `(a2²,a3²,a4²)=(.36,.16,.16)`.
- II: `(a2²,a3²,a4²)=(.402,.088,.19)`.

Las diferencias de cuadrados `(0.042,-0.072,0.030)` satisfacen simultáneamente:

\[
 \sum\Delta a_k^2=0,\qquad\sum k^2\Delta a_k^2=0,\qquad\sum k^4\Delta a_k^2=2.52.
\]

Por tanto, los dos campos comparten `N_arit=mcm(2,3,4)=12`, `E=.7025`, `J=4.105`, `ell_omega=.58503464`, `beta=.035`, `P(0)=0`, y `dot E(0)=-nu J`. **No comparten toda su energía cinética**; esa objeción se controla por separado en la prueba B.

### Derivada exacta de J

La identidad periódica general, conocida de Navier–Stokes 3D, es:

\[
 \dot J=-2\langle\partial_i\omega_a\,\partial_i u_b\,\partial_b\omega_a\rangle
 +2\langle\nabla\omega:\nabla((\omega\cdot\nabla)u)\rangle
 -2\nu\langle|\Delta\omega|^2\rangle.
\]

**En los datos iniciales de esta familia**, las contribuciones no viscosas axiales promedian cero: la derivada de `f(z)` está en `z`, el factor axial de estiramiento es `f(z) B cos(x-y)` y su promedio planar es cero; `h(z) partial_y W` tiene promedio axial cero; la interacción estrictamente planar de `psi` es idéntica en ambos campos. Así, **la diferencia** de la derivada se reduce exactamente al momento axial de orden cuatro:

\[
 \boxed{\dot J_{II}(0)-\dot J_I(0)=-\nu\sum k^4\Delta a_k^2=-.03(2.52)=-0.0756.}
\]

Como `dot ell/ell=1/2(dot E/E -dot J/J)` y `E,J,dot E` coinciden,

\[
 \boxed{\left(\frac{\dot\ell}{\ell}\right)_{II}
 -\left(\frac{\dot\ell}{\ell}\right)_{I}
 =\frac{.03(2.52)}{2(4.105)}\simeq0.00920828.}
\]

El defecto se encuentra en la **primera derivada de un observable de la interfaz**, lo que prueba su insuficiencia predictiva bajo O41-T1 para cualquier intervalo común de solución suave local.

## 4. Evolución temporal E1: prueba A

Pseudospectral Galerkin 2/3 y RK4, dominio `[0,2pi)^3`, `nu=.03`, duración `.12`, paso `.004`. Diagnósticos para resolución 48³:

| t | E I | E II | ell I | ell II | P I | P II |
|---:|---:|---:|---:|---:|---:|---:|
| 0.00 | 0.702500000 | 0.702500000 | 0.585034640 | 0.585034640 | 0 | 0 |
| 0.06 | 0.695446058 | 0.695450028 | 0.589820125 | 0.590140069 | 0.007702194 | 0.007703463 |
| 0.12 | 0.689001749 | 0.689017242 | 0.594006172 | 0.594638693 | 0.014363587 | 0.014369331 |

En `t=.12`: `delta ell=ell_II-ell_I=0.0006325213`; `delta E=+1.54935e-5`; `delta J=-0.0082164044`. Inicialmente los `P` globales son 0, pero **durante la evolución aparece producción global no nula por estiramiento**: no se simuló solamente una cizalla lineal que apaga la no linealidad. El balance temporal de `E` con la regla Simpson usando `t=0,.06,.12` coincide con `E(T)-E(0)` a aprox. `1.1e-8` por caso; no es una certificación de error PDE.

Control espacial: `delta ell(t=.12)` en 24³ es `0.0006325434`, en 32³ `0.0006325213102` y en 48³ `0.0006325213115`. Control temporal 32³ `dt=.004` frente a `.002` modifica `delta ell` por menos de `2e-15`. La divergencia de la velocidad resuelta es cercana a `5e-16` en norma RMS discreta. **Esto confirma convergencia práctica de los observables registrados en este intervalo**; no demuestra convergencia matemática uniforme en todo NS 3D.

## 5. Partículas y reloj del espejo

Se integran cuatro trazadores por campo resolviendo `dot X_p=u(X_p,t)` mediante RK4 con velocidades interpoladas trilinealmente de las etapas RK4 de la PDE. Se etiqueta uno como **referente material operativo** `X_s`, y se observa otro `X_p` desde `zeta=(X_p-X_s)/ell_omega`. Se mide la fase de orientación plana de `zeta` sólo mientras la separación planar no sea cero. No se postula que el referente trazador **sea** la singularidad ontológica.

El reloj nominal de escala es `s(t)=int_0^t (v_*/ell_omega)dt` con `v_*=1` adimensional declarado. Para 48³, a `t=.12`:

- Caso I: `s=0.203490340784`.
- Caso II: `s=0.203380993978`.
- Diferencia: `s_II-s_I=-0.0001093468053`.
- El cambio del ángulo relativo plano de un trazador frente a `X_s` es `0.042116 rad` en I y `0.043156 rad` en II, valores **sensibles a la interpolación de la trayectoria**, menos convergidos que los balances globales.

Convergencia temporal del reloj: en 32³, al reducir el paso de `.004` a `.002`, la diferencia entre relojes cambia cerca de `1.6e-9`, consistente con el orden de la cuadratura temporal empleada. Ningún marcador seguido presentó retorno completo bajo **la orientación angular relativa aquí declarada**; el «resto después de una vuelta» permanece indefinido. No se infiere ausencia universal de vueltas en otros flujos o tiempos.

### Lectura exacta del comienzo de los relojes

`dot s=v_*/ell`. Como `ell_I(0)=ell_II(0)`, los relojes empiezan con la **misma primera tasa**. Pero `ell'_I!=ell'_II` implica:

\[
 \boxed{\ddot s_{II}(0)-\ddot s_I(0)
 =-\frac{v_*}{\ell(0)}\,
 \left[\left(\frac{\dot\ell}{\ell}\right)_{II}
 -\left(\frac{\dot\ell}{\ell}\right)_{I}\right] \neq0.}
\]

La diferencia de reloj surge de la información interna necesaria para actualizar la **referencia del espejo**, aunque la referencia inicial y su primera tasa coincidan. Esto es una conclusión matemática para un reloj de escala definido, **no una derivación del tiempo propio relativista ni de una singularidad física**.

## 6. Control adversarial B — también idéntica energía cinética

Se amplía a cuatro bandas axiales `K={2,3,4,5}`, con MCM `60`. Tomamos I con `a_k²=.25` para los cuatro modos. II difiere según:

\[
\Delta (a_2^2,a_3^2,a_4^2,a_5^2)=.03\,(-48/125,243/125,-64/25,1).
\]

Por construcción exacta:

\[
\sum\Delta a_k^2=0,\quad
\sum k^2\Delta a_k^2=0,\quad
\sum \Delta a_k^2/k^2=0,
\quad \sum k^4\Delta a_k^2=3.6288.
\]

Así I y II comparten desde `t=0` no sólo `(N,E,J,ell,beta,P,dot E)`, sino también la **energía cinética total**. Sin embargo,

\[
\boxed{\dot J_{II}(0)-\dot J_I(0)=-.03(3.6288)=-0.108864.}
\]

Los verificadores reproducen el resultado en 32³ y 48³. La integración a `t=.12` produce `delta ell≈0.0003399978` y un reloj de escala diferente. Los cambios pueden estar ligados a interacciones que se desarrollan durante la evolución; el resultado exacto se refiere a la diferencia de primera derivada en `t=0`.

**Esto elimina la objeción más inmediata de la prueba A:** la pérdida de suficiencia **no** se debe simplemente a que un estado tenga mayor energía cinética inicial.

## 7. Qué sabemos ahora sobre suficiencia dinámica

- **Ya resuelto en MF-86/MF-97/O41-T1:** definición algebraica/semántica de normalización suficientemente composicional y criterio de dinámica que desciende a un cociente.
- **Ya resuelto en O41-T2:** interfaces de Fourier autónomas para cizallas lineales particulares.
- **Ya probado en O46:** `(E,ell)` recupera la derivada inicial `dot E` si además `P(0)=0` en una familia tridimensional concreta, y un bispectro determinado recupera otra derivada modal.
- **Nuevo O47:** aun conservando `(E,ell,beta)` y la energía cinética, una interfaz puede perder información necesaria para determinar **su siguiente velocidad de escala**: `dot J` exige al menos el momento axial de orden cuatro en esta clase de datos iniciales. En el campo 3D general también necesita controlar sus términos de transferencia no lineal.
- **No probado:** que añadir un momento más garantice cierre para todo tiempo. La cadena de derivadas y las interacciones no lineales podrían requerir una interfaz mucho más rica o un teorema especial de reducción; cualquier afirmación de tamaño finito/universal sería prematura.

### Lección metodológica

**Suficiencia instantánea para una pregunta** es distinta de **suficiencia temporal para todas las continuaciones admitidas**. El normalizador ontológico no se refuta porque un catálogo particular de observables sea insuficiente. El falsador especifica precisamente qué diferencia faltó en ese catálogo.

## 8. Regresión de investigaciones previas

Conservadas, no reclamadas como nuevas:

| Fuente | Hallazgo/comprobación anterior | Alcance |
|---|---|---|
| MF-43 | Fase de actualización, ritmo relativo, no-go del segundo absoluto | Recurrencia de red condicional |
| O25 | Espejo espectral `ell_omega`, evolución de `A,B`, cambio de marco móvil | Identidades exactas para soluciones suaves |
| O39 | `E'=P-Damp-Dang`, flujo por referencias móviles, no-go de giro compensatorio obligatorio | Balance PDE exacto; control global abierto |
| O41 | Cizallas de Fourier dinámicamente suficientes y falsadores de fase 3D | Familias declaradas |
| O42 | Dependencia triádica de transferencia instantánea | Tubo axial 3D; alcance instantáneo |
| O43E | **103 comprobaciones** reportadas en regresión O46 | Anillo 3D Galerkin, tiempo corto |
| O43R | **10.100 comprobaciones** reportadas en regresión O46 | Identidades aritméticas/cinemáticas, no retorno físico |
| O44 | **114 comprobaciones** reportadas en regresión O46 | Anillos finitos, sin vueltas materiales completas |
| O45 | **10 pruebas ejecutadas de nuevo** | Cinemática, gauge, marco NS |
| O46 | **66 controles ejecutados de nuevo** | Derivadas iniciales exactas y FFT |

O47 añade pares de datos preparados **antes de medir el resultado**, verificadores exactos de derivadas y evolución corta con controles espaciales/temporales. No agrega ninguna solución del problema Clay.

## 9. Próximo falsador legítimo

Definir una consulta Q explícita de continuación física (p. ej. `J(t+delta)`, transferencia de un conjunto de tríadas o fase relativa material) y una interfaz candidata que no contenga por definición toda la solución; comprobar su derivada inducida a lo largo de sus fibras. Si falla, identificar el observable mínimo cuya ausencia explica un par indistinguible. Si pasa en una subclase, demostrar por qué la dinámica mantiene esa subclase.

La pregunta ontológica que permanece es si existe una operación de recierre suficientemente económica que capture esas dependencias sin imponer de antemano toda la historia de un flujo. Para el problema de regularidad 3D, aun esa suficiencia deberá combinarse con una **estimación a priori** cuantitativa que controle el estiramiento en todas las escalas pertinentes.

## 10. Reproducción

```sh
python verificar_O47.py --N 24 32 48 --T .12 --dt .004
python verificar_O47.py --N 32 --T .12 --dt .002
python verificar_O47_control_energia.py
```

- `O47_RESULTADOS_N24_N32_N48.json`: evolución principal de los tres tamaños.
- `O47_RESULTADOS_N32_dtmitad.json`: control temporal.
- `O47_CONTROL_ENERGIA.json`: segundo experimento que iguala además energía cinética.
- `verificar_O47.py` y `verificar_O47_control_energia.py`: implementación NumPy.
- `REGRESION_ANTECEDENTES.md`: procedencia y estatus de ensayos anteriores.
- `MANIFEST_SHA256.json`: hashes de los archivos del suplemento.

**Estado general:** demostración exacta de un defecto de suficiencia temporal para una interfaz especificada; pruebas numéricas convergentes en un horizonte corto para los observables globales; origen físico del reloj de singularidad, cierre completo NS 3D y regularidad global abiertos.
