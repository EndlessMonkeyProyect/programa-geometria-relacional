# O90 — El anillo vorticial: cuatro nodos, dos giros y la fragilidad del múltiplo fijo

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 22 octubre 2026**  
**Continuidad:** O68, O69, O88, O89. **Estatus:** `[O]` hipótesis ontológica, `[T]` cálculo analítico exacto, `[E]` ensayo numérico, `[F]` falsador, `[A]` puente pendiente. 

## 0. Resultado en dos frases

**[T]** Existe un campo inicial liso, solenoidal, de soporte toroidal, con *ambos giros* y cuatro nodos materiales, para el cual una perturbación arbitrariamente pequeña destruye el acoplamiento primitivo común `2:1` entre los giros de los cuatro nodos. Las soluciones de Navier–Stokes correspondientes tienen una evolución suave local; por tanto, **la falta de un múltiplo entero fijo no implica ruptura física inmediata**.

**[E]** En el ensayo tridimensional Fourier–Galerkin O53/O69, los cuatro nodos pierden **coherencia relativa** con perturbación azimutal, pero siguen siendo cuatro trayectorias materiales distintas durante la ventana medida. En ausencia de perturbación, su fase colectiva se desplaza y la coherencia relativa permanece: **deriva común ≠ pérdida de cierre relativo**.

**No se demuestra** regularidad global 3D, ni que toda singularidad física sea un anillo, ni la imposibilidad de otro normalizador más general. La primera afirmación es un contraejemplo matemático **a la necesidad del mismo múltiplo rígido**, no al conjunto abierto de hipótesis del programa.

## 1. El objeto ontológico que sometemos a prueba [O/D]

Un nodo se considera una unidad desde fuera y admite una lectura interna de relaciones. La realización del anillo tiene cuatro marcas materiales alrededor del aro, no cuatro partículas físicas privilegiadas ni un tetraedro fijo. Un giro recorre la sección del tubo (meridional/poloidal, fase `θ`); otro recorre el aro (azimutal/toroidal, fase `φ`). El par entero primitivo `(q,p)=(2,1)` expresa el **candidato** de cierre de O68/O88:

\[
\Psi_i=\theta_i-2\varphi_i,\qquad \dot\Psi_i=\dot\theta_i-2\dot\varphi_i.
\tag{90.1}
\]

Dos tipos de información diferentes: la **deriva común** `\overline{\Delta\Psi}` y la **coherencia entre nodos**, medida mediante

\[
\delta_i(t)=\Psi_i(t)-\Psi_i(0),\quad
\widetilde\delta_i=\delta_i-\frac14\sum_j\delta_j,\quad
\boxed{\mathcal C_4(t)=\left|\frac14\sum_{i=1}^4 e^{\mathrm i\delta_i(t)}\right|.}
\tag{90.2}
\]

`C4=1` si las cuatro fases incrementales coinciden módulo `2π`; `C4<1` si hay dispersión. La deriva uniforme puede ser absorbida al transportar la referencia; la dispersión relativa no puede eliminarse con **una sola fase común**. La elección de cuatro nodos y del centro toroidal sigue siendo parte del protocolo: no se reivindica un observable universal extraído canónicamente del flujo.

## 2. Teorema O90-T1: datos exactos con estructura vorticial toroidal [T/F]

Trabajamos en `T³=(-π,π]^3` con viscosidad constante `ν>0` y sin fuerza. Coordenadas cilíndricas `(r,φ,z)`. Elegimos `R=1.4`, `a=0.6`, `d=0.3`, `c=1` y `ε` real de módulo arbitrariamente pequeño. Definimos

\[
Q(r,z)=\frac{(r-R)^2+z^2}{a^2},\quad
\chi(r,z)=\begin{cases}
\exp\{-Q/(1-Q)\},&Q<1,\\0,&Q\ge 1.
\end{cases}
\tag{90.3}
\]

`χ` es suave, no nula, soportada en un **toro sólido** que no toca el eje `r=0` ni las caras del dominio periódico. Para `Q_*=d²/a²=1/4` escogemos

\[
 b=\frac{c\,\partial_r\chi(R+d,0)}{2d\,\chi(R+d,0)}=-\frac{c}{a^2(1-Q_*)^2}=-\frac{400}{81}.
\tag{90.4}
\]

Construimos un campo real suave en las tres coordenadas:

\[
\boxed{\begin{aligned}
u_r&=-\frac{c\chi_z}{r}-\frac{2\varepsilon\chi\sin2\varphi}{r},\\
u_\varphi&=b\chi-\varepsilon\chi_r\cos2\varphi,\\
u_z&=\frac{c\chi_r}{r}.
\end{aligned}}
\tag{90.5}
\]

La notación `u_r,u_φ,u_z` de (90.5) denota componentes de velocidad y **no** la viscosidad `ν`.

**Incompresibilidad exacta:** en coordenadas cilíndricas,

\[
\nabla\cdot u=\frac1r\partial_r(ru_r)+\frac1r\partial_\varphi u_\varphi+\partial_z u_z
=\frac{-c\chi_{zr}-2\varepsilon\chi_r\sin2\varphi+2\varepsilon\chi_r\sin2\varphi+c\chi_{rz}}r=0.
\tag{90.6}
\]

Ambos giros están activos: `u_z` proporciona movimiento meridional y `u_φ` movimiento alrededor del eje. El vórtice tiene distribución localizada en la región toroidal; no se supone un tubo de vorticidad congelado materialmente.

Colocamos cuatro nodos iniciales en `(r,φ,z)=(R+d,jπ/2,0)`, `j=0,1,2,3`. Sean `θ=atan2(z,r-R)` y `φ` la fase azimutal. Por derivación cinemática exacta en `t=0`:

\[
\dot\theta_j(0)=\frac{c\chi_r}{(R+d)d},\qquad
\dot\varphi_j(0)=\frac{b\chi-\varepsilon\chi_r(-1)^j}{R+d}.
\tag{90.7}
\]

Todos los valores de `χ` y `χ_r` de ahora en adelante se evalúan en `(R+d,0)`. Por la elección de `b`, con `ε=0` hay cierre instantáneo **2:1** para los cuatro nodos. Con `ε≠0`:

\[
\boxed{\dot\Psi_j(0)=\frac{2\varepsilon\chi_r}{R+d}(-1)^j.}
\tag{90.8}
\]

Numéricamente, para `ε=0.04`, los nodos alternan

\[
(-0.0999085052,\,+0.0999085052,\,-0.0999085052,\,+0.0999085052)
\quad \text{rad/tiempo}.
\tag{90.9}
\]

Como `χ_r≠0`, estos dos pares **no** admiten simultáneamente el mismo entero primitivo no trivial `(q,p)` para los cocientes instantáneos de sus giros: si `pθ̇=qφ̇` valiera en ambos pares, restar las identidades forzaría `q=0`, y entonces `p=0`, incompatible con primitivdad. Este argumento vale para todo `ε≠0`, por pequeño que sea.

**Interpretación rigurosa:** se comparan dos condiciones iniciales distintas y arbitrariamente próximas: la configuración `ε=0`, sincronizada en esos cuatro puntos al inicio, y la `ε≠0`, no sincronizada. **No se afirma** que la solución `ε=0` conserve ese bloqueo durante toda su evolución ni que un mismo flujo primero lo conserve y después lo pierda por el mecanismo exacto aquí construido.

**No colapso local:** el teorema clásico de existencia local para Navier–Stokes en `T³` con datos suaves y solenoidales garantiza una solución suave durante cierto intervalo `[0,T_ε]`. Para cada `t` en ese intervalo, su mapa material `X_t` es un difeomorfismo que preserva volumen, puesto que

\[
\det \nabla X_t(x)=\exp\int_0^t(\nabla\cdot u)(X_s(x),s)ds=1.
\tag{90.10}
\]

La imagen del **toro material inicial** conserva topología y los cuatro nodos no se fusionan. Esto **no implica** que el soporte de vorticidad sea ese mismo toro material: la viscosidad difunde vorticidad a través de su frontera.

## 3. Comprobación O90-E1: cuatro nodos en el anillo numérico de O69 [E]

Usamos los operadores originales de O62/O63 y el estado inicial del anillo O53, con `ν=0.025`, caja periódica, resolución Fourier–Galerkin `N=32,40`, desaliasado `2/3`, Runge–Kutta cuarto orden, `dt=0.004`, `T=0.08`. Elegimos los mismos cuatro azimuts `0°,90°,180°,270°`, todos inicialmente en el exterior del núcleo a profundidad `d=0.12`, y calculamos ambas fases materiales desde el **campo simulado**, no imponiendo su razón. El centro meridional se lee de la distribución de enstrofía de O63.

| Resolución | Perturbación angular | Rango del desfase relativo al tiempo 0.08 (rad) | `C4` final | Distancia mínima entre nodos al final |
|---|---:|---:|---:|---:|
| 32³ | 0 | `≈0` | `1.000000` | `1.5642` |
| 32³ | 0.14 | `0.521416` | `0.978958` | `1.5347` |
| 40³ | 0 | `≈0` | `1.000000` | `1.5628` |
| 40³ | 0.14 | `0.589640` | `0.973436` | `1.5300` |

El modelo sin perturbación tiene **deriva común** significativa: `ΔΨ≈−0.77` a `−0.79` rad. Por tanto, mantener `C4=1` **no significa** conservar `Ψ` fijo. Es justamente la separación entre ritmo transportado y sincronía entre ramas. La perturbación rompe esa coincidencia entre los cuatro nodos, no las trayectorias en la ventana observada.

**Limitaciones:** es una integración finito-dimensional, no una solución analítica del continuo; dos mallas no certifican convergencia, ni descartan singularidades tardías; los cuatro puntos son marcas materiales arbitrarias y los ángulos dependen de la lectura geométrica del anillo. Los datos iniciales de este ensayo son distintos de los datos exactos de §2.

## 4. Segundo teorema útil: circulación ≠ múltiplo entero [T]

Para un lazo **material** cerrado `C_t` transportado por una solución suave de Navier–Stokes, la evolución de la circulación obedece exactamente

\[
\boxed{\frac d{dt}\oint_{C_t}u\cdot d\ell=\nu\oint_{C_t}\Delta u\cdot d\ell.}
\tag{90.11}
\]

A diferencia del caso de Euler ideal, la circulación material puede variar por difusión viscosa. El hecho de que una curva cerrada siga siendo cerrada como objeto material **no** implica que su circulación, giros o normalizador entero sean invariantes.

**Consecuencia ontológica:** «se conserva la unidad», «se conserva una fase relativa», «se conserva un entero primitivo» y «se conserva la circulación» son contratos diferentes. Llamarlos a todos *cierre* sin distinguirlos hace que la hipótesis sea imposible de atacar.

## 5. ¿Qué quedó falsado y qué queda vivo?

| Proposición | Estado |
|---|---|
| Hay campos vorticiales toroidales suaves con ambos giros y cuatro nodos | **[T] Sí**; construcción explícita §2 |
| En todos ellos los nodos necesariamente comparten un entero primitivo fijo de giro | **[F] No**; perturbación arbitrariamente pequeña §2 |
| Se puede perder coherencia relativa durante un ensayo sin que los nodos colapsen en la ventana | **[E] Sí**; §3 |
| Una pérdida de sincronía entre giros es equivalente a una singularidad matemática de NS | **[F] Falso como requisito general**; local existencia y difeomorfismo material |
| La identidad ontológica del nodo es exactamente una marca material | **[A] No establecido** |
| Toda estructura vorticial regular admite una referencia relacional reconstructible **no trivial** | **[A] Abierto; requiere definición independiente** |
| La referencia relacional obliga a una cota global sobre `∫||∇u||∞` | **[A] Abierto** |

### Tesis O90 para crítica externa

> **Hipótesis fuerte y refutable:** existe una regla canónica —calculada de la distribución tridimensional de vorticidad, sin escoger cuatro partículas ni reajustar retrospectivamente la referencia— que transporta la identidad del cierre propio entre configuraciones y produce una desigualdad suficiente para controlar la concentración a cualquier escala.

**Ataque decisivo:** exhibir un campo suave cuyo cierre canónico, definido antes del ejemplo, sea imposible de transportar; o exhibir un campo donde el cierre se conserve pero no aporte ninguna cota dinámica adicional. Si el «normalizador» se permite redefinir para reconstruir arbitrariamente cualquier campo suave, la hipótesis se vuelve tautológica y deja de explicar regularidad.

## 6. Reproducibilidad y trazabilidad

`OPENBLAS_NUM_THREADS=1 python codigo/verificar_o90.py`. Incluye operadores originales O63/O62 (copia, no resultado nuevo), ensayos `N=32` y `N=40`, código del campo exacto, CSV, gráficos y JSON de verificaciones. **14 verificaciones superadas**, incluidos 36 puntos de diferencia finita sobre la divergencia. Las pruebas `[T]` se sostienen por las identidades escritas y existencia local clásica; los cálculos `[E]` comprueban, pero no sustituyen, una prueba de convergencia del continuo.
