# O33 — Simetría modular, persistencia común y proyección de forma en Navier–Stokes

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**20 de octubre de 2026 · Suplemento independiente, continuidad de O25–O32**  
**Estado epistemológico:** [O] correspondencia ontológica; [D] hipótesis/contrato; [T] teorema condicionado; [E] comprobación computacional; [F] control negativo; [A] pregunta abierta.

## 0. Pregunta y respuesta

**Pregunta.** ¿Puede una relación común entre dos formas vorticiales persistir por la dinámica física misma, sin postular un coeficiente externo `K`, y sin eliminar sus particularidades? ¿Puede la imagen global ser menos informativa que la estructura de sus componentes?

**Respuesta precisa.** Sí, para la clase declarada de configuraciones con simetría de rotación en Navier–Stokes 2D: (i) una relación exacta entre formas etiquetadas se preserva durante toda la evolución suave, (ii) sus ritmos de orientación cuadrupolar coinciden cuando las fases están definidas, y (iii) una familia de tres o más etiquetas puede conservar formas locales anisótropas mientras el cuadrupolo **global** se anula por simetría. Con O31–O32 se certifica además una **ventana finita** con dos concentraciones distinguibles y anisotropía local positiva.

**Límite central.** La compatibilidad se presupone en la simetría de los datos iniciales; **no** se demuestra convergencia de pares inicialmente incompatibles ni sincronización atractora, fusión, conservación integral de forma, regularidad 3D, identificación de `v_*` con `c`, ni derivación de un principio físico nuevo desde la ontología. El núcleo ontológico se usa como lenguaje de comparación, no como premisa de una PDE.

## 1. Núcleo ontológico y diccionario [O/D]

El Núcleo Generativo Canónico distingue `diferencia → comparación → resto → cierre propio → nueva referencia`; la proyección es una lectura de una identidad bajo una relación, y el complemento es previo a su representación ortogonal. MF-43 construye ritmos de recurrencia sin atribuir agencia a estructuras. MF-86 exige suficiencia respecto de las preguntas de continuación admisibles. Los antecedentes O26 y O32 muestran, respectivamente, que un conjunto fijo de observables de bajo orden no basta para todos los futuros y que ciertas formas anisótropas pueden conservarse en intervalos a priori.

Aquí **«módulo común»** significa relación entre distribuciones preservada por una acción de simetría; **«forma propia»** es la distribución y/o un observable especificado, nunca un sujeto que reconoce. **«Singularidad relacional»** se reserva para foco/identidad ontológica y **no** equivale a una singularidad matemática de Navier–Stokes.

## 2. Contrato del flujo [D]

Trabajamos en `R²` con viscosidad `ν>0`, sin forzamiento:

\[
\partial_t\omega+u\cdot\nabla\omega=\nu\Delta\omega,
\quad \nabla\cdot u=0,
\quad u=K_{BS}*\omega,
\quad K_{BS}(x)=\frac{Jx}{2\pi|x|^2},\quad J(x_1,x_2)=(-x_2,x_1).
\tag{O33.1}
\]

Suponemos solución clásica suave, decaimiento suficiente para momentos e integración por partes, unicidad en la clase indicada, y una partición **inicial declarada** de vorticidad no negativa `ω=Σ_j ω_j`. Cada etiqueta satisface la misma ecuación lineal de transporte–difusión con el campo total `u`, por lo que conserva circulación `Γ_j` pero no necesariamente soporte espacial. El hecho de que una etiqueta persista como función **no** implica que su remolino siga distinguible dentro de la vorticidad total.

Sea `R_θ` una rotación plana. En complejos, `z=x+iy`, `U=u_x+iu_y` y `R_θ z=e^{iθ}z`.

## 3. Lema O33-T1 — Equivarianza rotacional [T]

Para cualquier rotación `R_θ`:

\[
K_{BS}(R_\theta x)=R_\theta K_{BS}(x),\qquad
\Delta(f\circ R_{-\theta})=(\Delta f)\circ R_{-\theta}.
\]

La transformación

\[
\tilde\omega(x,t)=\omega(R_{-\theta}x,t),\qquad
\tilde u(x,t)=R_\theta u(R_{-\theta}x,t)
\]

preserva (O33.1). Esto resulta de la identidad `J R_θ=R_θ J` y de que las rotaciones conservan norma, derivadas espaciales y divergencia. Por unicidad, una rotación que preserve **los datos completos del flujo** preservará su solución para todo tiempo admitido. No es un principio nuevo: es la simetría clásica de Navier–Stokes.

## 4. Teorema O33-T2 — Dos formas con relación modular exacta [T]

Supongamos dos etiquetas con

\[
\boxed{\omega_B(x,0)=\omega_A(-x,0),\qquad \omega(x,0)=\omega_A(x,0)+\omega_B(x,0).}\tag{O33.2}
\]

La vorticidad total es par: `ω(-x,0)=ω(x,0)`. Por el lema y unicidad, `ω(-x,t)=ω(x,t)` y `u(-x,t)=-u(x,t)`. La etiqueta transformada `ω_A(-x,t)` satisface la misma ecuación y condición inicial que `ω_B(x,t)`. Por unicidad de la ecuación lineal de etiquetas:

\[
\boxed{\omega_B(x,t)=\omega_A(-x,t)}\tag{O33.3}
\]

para toda duración en la que el contrato de solución clásica sea válido.

Definimos centros `C_j=Γ_j^{-1}∫zω_j`, dispersión `S_j=Γ_j^{-1}∫|z-C_j|²ω_j` y cuadrupolo

\[
Q_j=\frac1{\Gamma_j}\int(z-C_j)^2\omega_j(z,t)\,dA.
\]

El cambio de variable `z↦−z` implica

\[
\boxed{\Gamma_A=\Gamma_B,\quad C_B=-C_A,\quad S_B=S_A,\quad Q_B=Q_A.}\tag{O33.4}
\]

Si `Q_A(t)≠0`, la fase cuadrupolar `φ_j=arg Q_j` existe y, en ramas continuas coherentes,

\[
\boxed{\phi_B-\phi_A=0\pmod {2\pi},\quad\dot\phi_B=\dot\phi_A.}\tag{O33.5}
\]

El eje elíptico geométrico es `φ/2 mod π`, no la fase material de las partículas. **Lo demostrado es igualdad de ritmos de orientación de forma por simetría, no sincronización atractora.** No se concluye que `φ_j` sea constante respecto de la línea entre centros, ni que los dos núcleos permanezcan distintos para todo tiempo.

## 5. Corolario O33-T3 — Certificado de dos formas distinguibles [T]

Agreguemos a O33-T2 las hipótesis de O31–O32: `ω_j(0)≥0`, circulación positiva, momentos finitos, `M_0=||ω(0)||∞`, `Γ=Γ_A+Γ_B`, viscosidad `ν>0`, `Q_A(0)≠0`, separación inicial `d_0>0`. Definamos

\[
U_0=\sqrt{\frac{2\Gamma M_0}{\pi}},\quad
 a_j(T)=\sqrt{S_j(0)+4\nu T}+U_0T,
\]

\[
H_j(T)=\frac{U_0}{3\nu}\left[(S_j(0)+4\nu T)^{3/2}-S_j(0)^{3/2}\right]+U_0^2T^2.
\]

Fijado `k>1`, si

\[
\boxed{
 k[a_A(T)+a_B(T)]<d_0-2U_0T,
 \qquad H_A(T)<|Q_A(0)|,
}\tag{O33.6}
\]

entonces para `0≤t≤T`: (a) los discos de radio `k a_j(t)` centrados en `C_j(t)` son disjuntos y contienen al menos `1−k^{-2}` de su circulación etiquetada; (b) los cuadrupolos individuales permanecen no nulos, con anisotropía positiva; (c) la **relación de forma** `(O33.3)` y la fase común `(O33.5)` persisten. Prueba: O31-T4 + O32-T2 + O33-T2. La cota `U_0` viene de datos iniciales y no representa `c`.

**Ejemplo prospectivo.** Dos gaussianas elípticas idénticas con `Γ_A=Γ_B=1`, covarianza `diag(0.09,0.01)`, centros `(-4,0)` y `(4,0)`, `ν=0.001`, `k=2`, `T=0.01`. Se tiene `S_j(0)=0.10`, `Q_j(0)=0.08`, `d_0=8`; utilizando la cota `M_0≤1/(π\sqrt{0.09\cdot0.01})`, la condición (O33.6) es satisfecha. La duración es corta y conservadora, pero no seleccionada retrospectivamente.

## 6. Teorema O33-T4 — Familia de m formas y selección de momentos [T]

Para un entero `m≥2`, sean `θ_j=2πj/m` y `m` etiquetas iniciales obtenidas por rotaciones de una misma distribución inicial:

\[
\omega_j(x,0)=\rho(R_{-\theta_j}x),\qquad j=0,\ldots,m-1.
\tag{O33.7}
\]

La vorticidad total es `m`-rotacionalmente invariante. Por equivarianza y unicidad:

\[
\omega_j(x,t)=\omega_0(R_{-\theta_j}x,t).
\]

Así, si `Q_0(t)≠0`,

\[
\boxed{C_j=e^{i\theta_j}C_0,\quad Q_j=e^{2i\theta_j}Q_0,\quad S_j=S_0.}\tag{O33.8}
\]

Luego las **fases de forma** tienen una relación modular exacta:

\[
\phi_j-\phi_0=2\theta_j\pmod {2\pi},\qquad \dot\phi_j=\dot\phi_0.
\]

No se requiere acoplamiento `K`, aunque tampoco hay una fuerza de atracción hacia la relación si se rompen los datos simétricos. Si `C_0\ne0`, el ángulo de la forma respecto del radio desde el centro global es igual para todas las etiquetas: `φ_j−2arg C_j=φ_0−2arg C_0`.

Sea el momento complejo global (sin centrar) de orden `k`, con integral finita:

\[
M_k(t)=\int_{\mathbb R^2} z^k\,\omega(z,t)\,dA.
\]

La simetría total implica

\[
M_k=e^{ik2\pi/m}M_k,
\]

por tanto

\[
\boxed{m\nmid k \ \Longrightarrow \ M_k(t)=0.}\tag{O33.9}
\]

**Corolario notable.** Para `m≥3`, el primer momento global es cero y el cuadrupolo **global** `M_2=0`, aun cuando **cada** cuadrupolo local `Q_j` sea no nulo. En `m=3`, `M_3` no está obligado a anularse: puede distinguir una estructura triple invisible al segundo orden. Esto formaliza **un cierre de la proyección global que no suprime la información de forma individual**; el modo del siguiente orden porta una nueva distinción.

**Ejemplo analítico m=3.** Tres gaussianas idénticas, rotadas `0°,120°,240°`, con centro de referencia `C_0=4`, covarianza `diag(0.09,0.01)`, `Γ_0=1`. Entonces al inicio `Q_0=0.08`, `M_2=0`, mientras

\[
M_3(0)=3\,[C_0^3+3C_0 Q_0]=194.88\ne0.
\]

La nulidad de `M_2` persiste por simetría. La no nulidad de `M_3(0)` solo garantiza `M_3(t)≠0` durante un intervalo pequeño por continuidad, no para todo tiempo.

## 7. O33-F1 — Misma firma cuadrupolar no garantiza módulo común [F/E]

Dos formas con igual `Γ`, centro relativo, `S` y `Q` no tienen por qué ser imágenes por rotación exacta. Ejemplo:

- `A`: gaussiana elíptica centrada en `(-4,0)` con varianzas `(0.09,0.01)`;
- `B`: mezcla por mitades de gaussianas centradas en `(4±0.2,0)` con varianzas `(0.05,0.01)`.

La mezcla B tiene varianza horizontal `0.05+(0.2)^2=0.09`, la misma varianza vertical, y por tanto `S=0.10`, `Q=0.08`, circulación unidad y centro `(4,0)`. Sin embargo, el cuarto momento central horizontal difiere:

\[
\mathbb E_A(X-C_A)^4=3(0.09)^2=0.0243,
\]

\[
\mathbb E_B(X-C_B)^4=3(0.05)^2+6(0.05)(0.2)^2+(0.2)^4=0.0211.
\]

Por tanto **no** satisfacen la relación completa `(O33.2)` aunque compartan la firma de bajo orden.

En un control numérico independiente de la ley instantánea exacta de `\dot Q_j`, evaluando Biot–Savart en cuadraturas con pasos espaciales `0.08` y `0.04`, se obtiene para la diferencia inicial de velocidades de fase `\dot\phi_A−\dot\phi_B≈−0.0176` (unidades del ejemplo), mientras que al reemplazar B por la copia rotada exacta, la misma diferencia es cero al error de redondeo. **Esto es evidencia numérica con convergencia de malla, no una demostración analítica de ese número ni una DNS temporal.**

## 8. Qué cerramos y qué no [O/T/F/A]

- **[T] Conservación de módulo común por simetría:** O33-T2 y T4 son exactos bajo el contrato declarado.
- **[T] Persistencia conjunta distinguible durante un intervalo:** O33-T3 aplica certificados a priori O31–O32 a la familia simétrica.
- **[T] Nulidad de momentos globales por simetría:** un modo de proyección global puede ocultar diferencias de los módulos locales, y órdenes superiores pueden expresarlas.
- **[F] Firmas de bajo orden insuficientes:** el contraejemplo de las gaussianas y el antecedente O26 impiden sustituir la distribución completa por radio, circulación y cuadrupolo como interfaz universal.
- **[A] Formación del cierre:** las ecuaciones 2D todavía no han derivado que pares inicialmente asimétricos converjan a una relación modular atractora, ni que esa condición produzca nueva identidad física.
- **[A] Estabilidad ante perturbaciones:** el subespacio simétrico es invariante, pero la invariancia **no es** un teorema de atracción transversal. Debe construirse una cota de detuning o un funcional de distancia a la clase de simetría con descenso real.
- **[A] 3D:** las etiquetas positivas y el transporte escalar por difusión son específicos de 2D; la vorticidad tridimensional tiene estiramiento y no es una densidad positiva escalar.
- **[A] Radio y frecuencia:** no hemos demostrado que la fase cuadrupolar `arg Q` o su ritmo cumplan universalmente `R_i ω_i=v_*` ni que `v_*=c`.

## 9. El siguiente discriminante y propuesta

La dirección realmente nueva no es construir otra simetría exacta. Es investigar si existe, para soluciones de Navier–Stokes 2D **sin simetría inicial**, un observable de distancia a un módulo común `D_sym(t)` que satisfaga una desigualdad de contracción prospectiva `dD_sym/dt≤−κ(t)D_sym` con `κ` deducido del propio flujo, no postulado; y si se puede certificar simultáneamente que las formas locales permanecen distinguibles. La dinámica viscoso-advectiva puede crear o destruir configuraciones coherentes, pero **no** hay tal desigualdad universal demostrada aquí.

## 10. Reproducción y genealogía

Ejecutar: `python verificar_o33.py`. Se verifican las identidades de simetría/rotación, selección de momentos, ejemplos gaussianos, cotas previas O31–O32, paridad del campo de Biot–Savart por cuadratura simétrica y control adversarial de fase a dos resoluciones. Las pruebas son complementarias a las demostraciones y **no** constituyen una simulación completa de NS.

Documentos consultados: Núcleo Generativo Canónico v0.1 (comparación y residuo), MF-43 (recurrencia y ritmo lógico), MF-86 (interfaz suficiente), O25–O26 (espejo y no-go de firma), O27 (componentes transversales 3D), O28 (módulos de fase), O29 (acoplamiento endógeno), O30 (balance), O31 (certificado de concentración), O32 (certificado cuadrupolar).

**O33 es un suplemento independiente. Ninguna premisa o resultado de O33 ha sido promovido automáticamente al Núcleo Canónico ni a la Imagen Total.**
