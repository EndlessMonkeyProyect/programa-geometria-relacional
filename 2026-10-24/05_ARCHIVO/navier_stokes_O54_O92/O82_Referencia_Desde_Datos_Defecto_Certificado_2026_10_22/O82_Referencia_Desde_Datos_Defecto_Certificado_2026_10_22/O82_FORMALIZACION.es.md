# O82 — Referencia calculada desde el dato inicial, defecto medido y certificado de continuidad

**Programa de Geometría Relacional** — Le Matt Ansatz Di Ego  
**22 de octubre de 2026 · suplemento O82 posterior a O81**  
**Clasificación:** `[O]` hipótesis/lectura ontológica; `[T]` matemática exacta bajo condiciones; `[E]` comprobación algorítmica de coeficientes; `[F]` límite o falsador; `[A]` puente abierto.

> **Alcance:** Obtiene un criterio suficiente, construido **exclusivamente a partir de los datos iniciales**, para certificar regularidad global de ciertas soluciones tridimensionales periódicas de Navier–Stokes sin fuerza. Es una aplicación explícita y computable del esquema de defectos ya formulado en O81, dentro de un método clásico de estabilidad; **no resuelve la regularidad general de Navier–Stokes 3D** y no identifica el criterio con el entero ontológico de O58.

## 0. Prioridad de la pregunta

**Ontología y narrativa `[O]`:** el cierre propio no requiere que las partículas o la forma geométrica sean inmutables. Una referencia puede conservar una parte de la relación y dejar un resto; la novedad puede ser absorbida o requerir reorganización. El normalizador múltiplo aritmético de O40–O58 transporta representación, el reloj de O25–O45 permite comparar ritmos, y O78–O79 muestran el costo de nuevas ramas físicas. La «singularidad» ontológica es un cierre de identidad, no el estallido de una solución PDE.

**Pregunta matemática:** ¿se puede escoger una **referencia física concreta** a partir del dato inicial, sin adivinar la evolución no lineal futura, y certificar que todas las interacciones restantes no generan pérdida de suavidad?

## 1. El operador de selección es anterior a la evolución `[D]`

Trabajamos en el toro tridimensional `T³=(R/2πZ)³` de periodos `2π`, con viscosidad `ν>0`, sin fuerza, velocidades solenoidales suaves y de media cero:

\[
\partial_t u+\mathbb P\nabla\cdot(u\otimes u)=\nu\Delta u,\qquad\nabla\cdot u=0.\tag{82.1}
\]

Sean `F⊂Z³\{0}` finito, simétrico bajo `k↦−k`. La selección espectral `Π_F` conserva solamente los modos de Fourier iniciales con etiquetas en `F`. **No es la proyección de Leray `P`**. Definimos, sin usar la solución futura:

\[
\boxed{U_0=\Pi_F u_0,\quad U(t)=e^{\nu t\Delta}U_0,\quad v_0=u_0-U_0,\quad u=U+v.}\tag{82.2}
\]

La referencia `U` satisface exactamente la **ecuación lineal de calor**, pero normalmente no la ecuación completa de Navier–Stokes. Su defecto es:

\[
\boxed{F_U=\partial_tU+\mathbb P\nabla\cdot(U\otimes U)-\nu\Delta U=\mathbb P\nabla\cdot(U\otimes U).}\tag{82.3}
\]

El defecto **se calcula directamente de `U₀`** por convoluciones finitas de Fourier y exponentes conocidos. Las fases, la presión y los modos nuevos entran en el cálculo mediante la proyección de Leray; no se los declara inexistentes.

## 2. Desigualdad de defecto del resto `[T]`

Para cualquier campo `f` con media cero, defina las normas de coeficientes:

\[
R(f)=\sum_{k\ne0}\frac{|\hat f_k|}{|k|},\quad S(f)=\sum_{k\ne0}|\hat f_k|,\quad Q(f)=\sum_{k\ne0}|k|\,|\hat f_k|.\tag{82.4}
\]

Definimos `R_v=R(v)`, `Q_v=Q(v)`, `S_U(t)=S(U(t))` y el defecto

\[
 B(t)=\sum_{k\ne0}\frac{|\widehat{F_U}(k,t)|}{|k|}\ge0.\tag{82.5}
\]

Al insertar `u=U+v` en (82.1) y usar (82.3):

\[
\partial_tv+\mathbb P\nabla\cdot(v\otimes v+U\otimes v+v\otimes U)=\nu\Delta v-F_U.\tag{82.6}
\]

Para cada modo, `|\hat{\mathbb P\nabla\cdot(f\otimes g)}_k|/|k|≤\sum_{p+q=k}|\hat f_p||\hat g_q|`. Por suma y Cauchy–Schwarz `S_v²≤R_vQ_v`. Consecuentemente:

\[
\boxed{D^+R_v+\nu Q_v\le R_vQ_v+2S_U\sqrt{R_vQ_v}+B(t).}\tag{82.7}
\]

Esta parte deriva directamente de la ecuación completa y **no presupone una dinámica cerrada para una semilla de número fijo de parámetros**.

Mientras `R_v≤ν/2`, aplicar Young con `2S_U√(R_vQ_v)≤(ν/4)Q_v+(4/ν)S_U²R_v` implica:

\[
\boxed{D^+R_v+\frac\nu4Q_v\le g(t)R_v+B(t),\quad g(t)=\frac4\nu S_U(t)^2.}\tag{82.8}
\]

Defina `G(t)=∫₀ᵗg(s)ds`, y `G∞=∫₀∞g(s)ds`. Multiplicando por `e^{-G(t)}`:

\[
\boxed{e^{-G(t)}R_v(t)+\frac\nu4\int_0^t e^{-G(s)}Q_v(s)ds
\le R(v_0)+\int_0^t e^{-G(s)}B(s)ds.}\tag{82.9}
\]

## 3. Teorema O82-T1: certificado a priori desde el dato inicial `[T]`

**Hipótesis:** `u₀` es solenoidal, suave y de media cero; `F` es finito y simétrico; `U` es la referencia de calor (82.2). Calcule únicamente desde `u₀`:

\[
\boxed{\mathcal M_F=
 e^{G_\infty}\left[R(u_0-\Pi_Fu_0)+\int_0^\infty e^{-G(t)}B(t)dt\right].}\tag{82.10}
\]

**Si**

\[
\boxed{\mathcal M_F<\nu/2,}\tag{82.11}
\]

**entonces** la solución de Navier–Stokes con ese dato inicial existe y permanece suave para todo tiempo positivo; además:

\[
\boxed{R_v(t)\le\mathcal M_F,\qquad
\int_0^\infty Q_v(t)dt\le\frac{4\mathcal M_F}{\nu}.}\tag{82.12}
\]

Y, por linealidad del calor en `U`:

\[
\boxed{\int_0^\infty\|\nabla u(t)\|_\infty dt
\le\frac{R(U_0)}\nu+\frac{4\mathcal M_F}\nu<\infty.}\tag{82.13}
\]

**Demostración:** por contradicción en el primer tiempo de cruce de `R_v=ν/2`, (82.9) obliga a `R_v≤\mathcal M_F<ν/2`, contradicción; por ende el intervalo con barrera es todo el intervalo suave de existencia. También se obtiene (82.12) de (82.9) y `e^{-G(t)}≥e^{-G∞}`. Para la referencia de calor, `∫₀∞Q_U dt=∑_{k∈F}|\hat u_0(k)|/(ν|k|)=R(U0)/ν`. Así, (82.13) vale en todo intervalo de existencia y es finito independientemente de su extremo. La estimación estándar en normas `H^s` para `s>5/2`, con `∫||∇u||∞`, excluye pérdida de suavidad en tiempo finito. La elección de `U` **no requiere conocer `u(t)`** y la demostración no la presupone globalmente suave. QED.

**Certificado más simple (más conservador):** Basta comprobar

\[
\boxed{e^{G_\infty}\bigl[R(v_0)+\int_0^\infty B(t)dt\bigr]<\nu/2,}\tag{82.14}
\]

porque `e^{-G(t)}≤1`. El programa numérico comprueba ambas cotas en el ejemplo.

**Origen matemático:** (82.7)–(82.9) es el esquema del defecto de O81, ahora con una referencia `U` enteramente calculable del dato inicial y una desigualdad global explícita. No se presenta como una teoría de estabilidad novedosa frente a la literatura.

## 4. Ensayo con dependencia tridimensional genuina `[T/E]`

Con `ν=1`, `A=2`, `B=C=0.00005`, tomamos:

\[
\boxed{u_0(x,y,z)=(A\sin y,\,B\sin z,\,C\sin x).}\tag{82.15}
\]

Este campo depende de las tres coordenadas, es real, suave, de media cero y solenoidal. `R(u₀)=A+B+C=2.0001>ν` por lo que **no** pasa la condición directa de datos pequeños de O80.

Construimos **tres referencias** a partir del mismo `u₀`:

| Selección previa | `R(v₀)` | `G∞` | `∫B` | Cota conservadora `e^{G∞}(R(v₀)+∫B)` | ¿Certifica? |
|---|---:|---:|---:|---:|---|
| Ningún modo: `U=0` | 2.0001 | 0 | 0 | 2.0001 | No |
| Solo la cizalla `A sin y` | 0.0001 | 8 | 0 | 0.298095799 | Sí |
| Los seis modos de `u₀`, evolucionados por calor | 0 | 8.00080002 | 0.000070711562 | 0.210956898 | Sí |

Para la última referencia `U(t)=e^{-t}u₀` **no** satisface Navier–Stokes, porque la proyección de su transporte cuadrático es no nula. Se verifica de modo analítico:

\[
\mathbb P((U\cdot\nabla)U)
=e^{-2t}\begin{pmatrix}
 AB\sin z\cos y\\ BC\sin x\cos z\\ CA\sin y\cos x
\end{pmatrix}.\tag{82.16}
\]

Las tres componentes son ya solenoidales y activan **doce** frecuencias espaciales inicialmente ausentes: cuatro por cada pareja de ondas. La norma del defecto es exactamente:

\[
\boxed{B(t)=\frac{|AB|+|BC|+|CA|}{\sqrt2}\,e^{-2t}.}\tag{82.17}
\]

La exposición de la referencia y el término viscoso dan

\[
\boxed{G(t)=2(A+B+C)^2(1-e^{-2t}).}\tag{82.18}
\]

De (82.10), con `R(v0)=0`, se calcula **analíticamente** el presupuesto ponderado de la referencia completa:

\[
\boxed{\mathcal M_F
=\frac{B(0)}{2G_\infty}\bigl(e^{G_\infty}-1\bigr)
\approx0.0263581374<0.5.}\tag{82.19}
\]

La cota conservadora de la tabla también pasa. La cota de gradiente global mediante la versión ponderada es

\[
\boxed{\int_0^\infty\|\nabla u\|_\infty dt\le2.0001+4(0.0263581374)\approx2.10553255.}\tag{82.20}
\]

**La afirmación es analítica**; el código comprueba los coeficientes de Fourier del defecto, su divergencia nula, su conjugación real y las constantes. No se está simulando la trayectoria completa.

## 5. ¿Qué aprendimos sobre el múltiplo y el resto? `[O/T/F]`

- `[T]` La regla `u₀→Π_Fu₀→U(t)` produce un candidato desde los datos iniciales. El defecto `F_U` es la parte de la dinámica que esa referencia simplificada todavía no resuelve. El resto `v` incluye los modos adicionales generados. **No se descartan las interacciones**.
- `[T]` Un resto inicial nulo (`v₀=0`) puede convertirse en uno no nulo cuando el defecto es distinto de cero. El certificado controla las novedades en lugar de exigir su ausencia.
- `[O]` Esto ofrece una realización físico-matemática del lenguaje de **referencia suficiente para una clase de evoluciones**. No establece que el operador de selección `Π_F` sea la singularidad ontológica universal ni que su defecto sea el «resto uno» aritmético.
- `[F]` Distintos `F` generan cotas distintas para el mismo campo físico. El mero número de modos o el refinamiento entero de un múltiplo **no** reducen por sí mismos el defecto; tienen que existir desigualdades reales como (82.11).
- `[F]` Para datos iniciales grandes arbitrarios **no** probamos que exista algún `F` finito con `\mathcal M_F<ν/2`. Un caso que no pasa el test puede ser regular; este criterio es suficiente, no necesario.
- `[A]` Todavía queda abierta la posibilidad de un operador intrínseco del programa, construido de cierres propios locales o multiescala, que tenga defectos controlados para familias significativamente más amplias, incluidos anillos con deformación y giro azimutal.

## 6. Repetibilidad y control de afirmaciones

- `codigo/o82_verificar.py`: verifica el campo de tres ondas y sus 12 modos de defecto para 24 combinaciones de amplitudes, comprueba solenoidalidad, simetría conjugada, magnitudes exactas y tres presupuestos, y genera `resultados/referencias.csv`, `resultados/resultado.json` y una gráfica.
- En la ejecución de referencia pasó **826 comprobaciones** de coeficientes y desigualdades finitas. No son 826 soluciones de NS ni una certificación por simulación.
- `graficos/o82_certificado_defecto.png`: evolución del mayorante ponderado calculado de manera exacta a partir del defecto.
- `REGISTRO_AFIRMACIONES.csv`: distingue teorema, álgebra computacional, interpretación y cuestiones abiertas.

**Cierre O82:** se demostró cómo construir una referencia aproximada computable exclusivamente a partir del dato inicial y certificar la continuación **para algunos campos tridimensionales grandes**. No se convirtió la normalización aritmética de O58 en una ley universal de estabilización ni se declaró resuelto el problema general de Navier–Stokes 3D.
