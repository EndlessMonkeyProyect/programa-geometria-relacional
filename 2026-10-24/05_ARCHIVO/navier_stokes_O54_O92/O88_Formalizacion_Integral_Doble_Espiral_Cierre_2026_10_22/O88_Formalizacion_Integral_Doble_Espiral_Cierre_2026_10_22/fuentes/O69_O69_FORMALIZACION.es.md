# O69 — Dos giros medidos en el anillo; coincidencia y renovación del normalizador

**Programa de Geometría Relacional** · **Le Matt Ansatz Di Ego** · **21 de octubre de 2026**  
**Estado:** suplemento aditivo; datos de una aproximación Fourier–Galerkin de Navier–Stokes tridimensional, identidades cinemáticas exactas y un teorema aritmético/topológico auxiliar. **No** constituye una solución del problema de regularidad global.

## 0. Ontología y motivo de la prueba

**[O]** La singularidad conserva su identidad mientras sus diferencias de giro, radios y frecuencias continúen admitiendo la referencia normalizadora que sostiene el cierre propio. La «semilla» no es una partícula fija ni una copia íntegra de la estructura anterior: es una relación que puede realizarse en nuevas circunstancias; el múltiplo normalizador representa continuidad aritmética. La totalidad contiene relaciones todavía no habitadas. La indefinición restante puede expresarse como grados de libertad de la familia de soluciones.

**[N]** «Apagar los espejos» significa comprobar si la relación continúa cuando dejamos de sostenerla como condición exterior. En este laboratorio el campo evoluciona **sin forzamiento externo** sobre un dominio periódico. No se han retirado físicamente paredes; no hay una caja reflectante en la simulación. Una relación de coordenadas no es una nueva fuerza.

**[H]** O68 propuso que, para dos fases materiales independientes, una clase entera primitiva `(q,p)` podría definir un cierre exacto `Psi = p theta1 - q theta2` con `dot Psi=0`. O69 pregunta si la dinámica real del modelo la conserva **sin introducir dicha igualdad en las ecuaciones**.

## 1. Las dos lecturas físicas del anillo

**[D]** El toroide posee dos ciclos geométricos: (i) el recorrido *meridional* alrededor de su sección; y (ii) el *azimutal* alrededor de su eje central. Poseer esos ciclos geométricos NO obliga a que cada partícula circule en ambos. Un anillo vorticial axisimétrico sin componente `u_phi` puede avanzar axialmente con `dot phi =0` para una partícula; su avance no es un segundo ciclo periódico.

En coordenadas cilíndricas `(rho,phi,z)` medimos directamente para cada trazador material `X_p(t)`:

\[
\theta_p=\operatorname{atan2}(z_p-Z_c,\rho_p-R_c),\quad
\varphi_p=\operatorname{atan2}(y_p,x_p).
\]

Aquí `R_c(t), Z_c(t)` son el radio y el centro axial *de enstrofía* del laboratorio O53, calculados del campo; NO son un foco ontológico ni una partícula identificada. Las derivadas, válidas cuando los denominadores no se anulan, son:

\[
\dot\theta_p=\frac{(\rho_p-R_c)(u_z-\dot Z_c)-(z_p-Z_c)(\dot\rho_p-\dot R_c)}{(\rho_p-R_c)^2+(z_p-Z_c)^2},\quad
\dot\rho_p=\frac{x_pu_x+y_pu_y}{\rho_p},
\quad
\boxed{\dot\varphi_p=\frac{x_pu_y-y_pu_x}{\rho_p^2}=\frac{u_\varphi}{\rho_p}.}
\]

El código deduce `dot R_c`, `dot Z_c` a partir de la ecuación semidiscreta del campo, y utiliza interpolación trilineal para evaluar `u(X_p)`. No se ajusta una fórmula de sincronía al resultado observado.

Distinguimos cuidadosamente estos observables:

- **Ciclos toroidales:** `theta` y `phi` de **una misma** partícula. Es la prueba de dos giros geométricamente diferentes.
- **Diferencia meridional:** `theta_1`, `theta_2` de dos partículas ubicadas inicialmente a profundidades `d=0.12` y `d=0.26` respecto del centro, en la cara exterior. Sirve para probar si dos ritmos interiores comparten una relación fija; NO debe presentarse como si fueran los dos ciclos topológicos del toroide.

En fluidos viscosos las partículas materiales no están obligadas a seguir líneas de vorticidad, ya que la vorticidad también se difunde. Por eso el transporte de un trazador no equivale a conservar la «semilla» del vórtice.

## 2. Acoplamiento exacto y su prueba

**[T, condicional]** Si el par de fases admite una relación primitiva `(q,p)`, con `gcd(p,q)=1`, entonces

\[
\Psi=p\theta_1-q\theta_2,\qquad
\boxed{\dot\Psi=p\omega_1-q\omega_2}.
\]

La coincidencia exacta en un intervalo exige `dot Psi=0` allí. La identidad de Bézout de O68 garantiza una transformación unimodular cuando **la razón entera ya existe**; no impone que la dinámica satisfaga esa razón. La coordinación de frecuencias no equivale a continuidad de identidad física, y la persistencia del vórtice no obliga a mantener el mismo par `(p,q)`.

**[T, teorema elemental de no recierre instantáneo racional]** Sean `omega1,omega2` funciones continuas sobre un intervalo conexo, con `omega2` distinto de cero. Supongamos que para todo instante `t` existen enteros `p(t),q(t)` no nulos tales que `p(t) omega1(t) = q(t) omega2(t)`. Entonces `omega1/omega2` es continuo y toma valores **sólo en Q**. La imagen continua de un intervalo es conexa; los únicos subconjuntos conexos de los racionales son puntos. En consecuencia, `omega1/omega2` debe ser **constante**. No se permite cambiar continuamente de razones enteras exactas instante a instante cuando la razón de frecuencias realmente varía. Este teorema no prohíbe: encuentros periódicos, razones aproximadas, fases bloqueadas en ventanas, ni una referencia relacional no reducible a un par fijo de enteros.

**[A]** Para construir un normalizador dinámico que absorba cambios de razón hace falta una ley más rica: memoria de fase, acoplamiento de varios recorridos, o estados de coincidencia definidos sobre intervalos/órbitas, no simplemente una selección racional posterior.

## 3. Contrato de datos y resolución

**[E]** Se reutilizan sin modificación los cuatro archivos de trayectorias del ensayo O53 (`N=40,48`, perturbación `epsilon=0` y `0.14`, `T=2.4`), inicialmente `R=1`, espesor `a=.35`, circulación nominal `Gamma=6`, viscosidad `nu=.025`, dominio periódico `[-pi,pi)^3`, método Fourier–Galerkin con máscara de desaliasado `2/3` y RK4. Los archivos originales de O53 suministran posiciones de partículas y fases del centro.

Adicionalmente se integraron **nuevas partículas fuera del plano inicial**, a azimutes `0°`, `45°`, `90°`, durante `T=.08`, `dt=.004`, en `N=32,40`, para evaluar las dos fases desde el mismo campo. Se reutilizaron los operadores de O63/O62 —incluidos con el código— para evitar imponer manualmente una frecuencia angular.

**Límite de validación:** el núcleo `a=.35` es relativamente delgado para estas mallas; la resolución no certifica convergencia de la ecuación diferencial en el continuo. Los cuatro cálculos de fase larga proceden de los datos históricos O53 y no son cuatro experimentos independientes recién integrados.

## 4. Resultado A: un ciclo material puede no estar habitado

Para una marca a `45°` alrededor del anillo, en `N=40`, profundidad `d=.12`, el cálculo directo de la velocidad inicial entrega:

| Preparación | `dot theta` [rad/tiempo] | `dot phi` [rad/tiempo] |
|---|---:|---:|
| Sin perturbación | −11.31653 | `≈0` |
| Perturbación `epsilon=.14` | −13.60046 | +0.18967 |

En `N=32`, respectivamente, los datos son `−11.47719`, `≈0` y `−14.31366`, `+0.20532`.

**[E]** La perturbación activa un movimiento azimutal detectable para estas marcas, sin que el par quede sincronizado automáticamente. Para una marca a `0°`, el cálculo perturbado da `dot phi≈0` por la simetría del plano de observación. Por eso una observación en un solo plano puede ocultar relaciones activas en otros azimutes. Los valores no son universales ni garantizan persistencia del giro azimutal a largo plazo.

## 5. Resultado B: dos velocidades meridionales no conservan razón exacta fija

Para las fases de **dos trazadores** del exterior `d=.12` y `d=.26`, las razones de velocidades iniciales y finales calculadas por diferencias temporales de O53 son:

| Malla | Perturbación | `omega_1/omega_2` al inicio | Al final `T=2.4` |
|---|---|---:|---:|
| 40³ | No | 1.3152 | 2.0126 |
| 40³ | Sí | 1.4060 | 3.9518 |
| 48³ | No | 1.3658 | 2.0629 |
| 48³ | Sí | 1.4837 | 3.7137 |

**[E]** Estos valores difieren sustancialmente; por tanto, en el **modelo numérico medido**, no hay un par primitivo constante `(p,q)` que imponga `p omega_1-q omega_2=0` durante toda la evolución: cualquier tal par impondría una razón constante.

El contrato auxiliar preconcebido `(p,q)=(3,4)` de O68 prueba `Psi=3theta_1-4theta_2`. Aunque el inicio se acerca en algunos casos, al final su deriva acumulada es:

| Malla | Perturbación | `(Psi(T)-Psi(0))/(2pi)` [vueltas] |
|---|---|---:|
| 40³ | No | +0.55697 |
| 40³ | Sí | +0.40677 |
| 48³ | No | +0.56067 |
| 48³ | Sí | +0.41158 |

**[F]** Estos resultados falsan la conservación exacta de ESA relación rígida para los trazadores de O53, no la persistencia del anillo, no cualquier condición de cierre concebible, y no la regularidad de Navier–Stokes. Un anillo puede avanzar mientras estos dos trazadores se desincronizan.

## 6. Comprobaciones y falsadores

Los archivos reproducibles superan **12 de 12 controles ejecutados**, incluyendo trazadores fuera del plano, fase meridiana y azimutal, reconstrucción de trayectorias archivadas, divergencia entre razones de frecuencia, deriva de un par fijado de antemano y comparaciones entre mallas. La prueba de derivada versus diferencia finita emplea un paso pequeño; el error máximo observado fue `0.240 rad/tiempo` en fase meridional rápida y `0.00377 rad/tiempo` en azimut, compatible con la curvatura de las fases en ese pequeño intervalo. **No** es un límite de error riguroso ni certifica convergencia temporal.

El experimento descarta una interpretación demasiado restrictiva: **dos giros materiales no son automáticamente engranajes con una razón entera fija por pertenecer a una misma geometría**.

Quedan abiertos tres mecanismos a distinguir:

1. **Referencia exacta local**: una coincidencia de fase que permanece durante un intervalo en una familia particular de soluciones.
2. **Referencia transportada**: una variable dinámica de historia o una fase colectiva que se reconstruye al cambiar la razón de los recorridos.
3. **Desacoplamiento sin destrucción**: la relación entre dos trazadores deja de cumplirse mientras el campo físico sigue siendo regular y conserva organización en otra representación.

**[A] Programa O70:** buscar un observable colectivo definido desde el campo y no desde una selección de partículas, y comprobar si su actualización tiene información predictiva propia. Cualquier hipótesis de sincronía debe probarse contra un campo suave con vorticidad intensa, contra perturbaciones azimutales y contra un cambio de referencia puramente representacional. Exigir una cota sobre gradientes antes de relacionarlo con la regularidad global 3D.

## 7. Reproducción

```bash
cd O69_Fases_Materiales_Semilla_Toroidal_2026_10_21
OPENBLAS_NUM_THREADS=1 python codigo/ejecutar_o69.py
python codigo/graficar_o69.py
```

Dependencias: Python 3, NumPy, SciPy, Matplotlib. El código `codigo/o63_operadores.py` es una copia sin modificación del laboratorio O63; `fuentes/ejecutar_o62_ORIGINAL.py` es el operador original de O62; `fuentes/datos_O53_originales` contiene los cuatro conjuntos O53 usados. `resultados/resumen.json` registra los controles. Fuente primaria numérica: **laboratorio O53 del propio programa**, no datos experimentales externos.
