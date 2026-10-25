# O81 — Cierre relativo a una referencia dinámica: de los múltiplos al resto físico

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**22 de octubre de 2026** · suplemento posterior a O80  
**Estado:** [O] ontología del programa; [T] derivación exacta (condicional a hipótesis declaradas); [E] verificación computacional de álgebra de Fourier; [F] falsador/límite; [A] puente aún abierto. **No demuestra regularidad general de NS 3D.**

## 0. La pregunta, sin redefinir lo resuelto

La unidad que alcanza cierre propio no tiene por qué retener la misma forma ni las mismas partículas. En O40–O58 se probó que un múltiplo normalizador puede conservar la representación anterior; en O25–O45 se construyeron relojes endógenos; en O78–O79 se observaron nuevas ramas y dependencias de fase; O80 estableció un presupuesto de interacciones para datos cuya norma crítica de Fourier es menor que la viscosidad. O81 no redefine ninguna de esas piezas.

**Pregunta:** cuando el campo completo excede el presupuesto crítico, ¿puede haber una referencia dinámica *real* y un resto físicamente menor que sí permitan controlar todas las interacciones? ¿Se logra por la mera elección de un múltiplo?

La respuesta se divide: 

1. **No** basta cambiar la etiqueta o denominador. Una norma física no disminuye por escribir el mismo número sobre otro denominador.
2. **Sí**, si se dispone de una solución coherente `U` ya demostrada y la diferencia `v=u−U` es suficientemente pequeña en una norma crítica. Esta separación conduce a un criterio riguroso de continuación para un conjunto no vacío de datos iniciales tridimensionales con norma total arbitrariamente grande.
3. No se demostró un algoritmo/ley intrínseca que encuentre siempre tal `U` y un resto admisible para cualquier dato de Navier–Stokes.

## 1. La referencia aritmética no atenúa la física [T/F]

Por O40, `h/N = (qh)/(qN)` para todo múltiplo entero positivo `q`. Esto transporta la representación, no reduce el valor de `h/N`.

Para Navier–Stokes en `T³`, sea `u_λ(x,t)=λu(λx,λ²t)` con `λ` entero positivo (misma viscosidad). Si `\widehat u(k)` son coeficientes de Fourier, entonces `\widehat {u_λ}(λk)=λ\widehat u(k)`, y por tanto

\[
\boxed{R(u_λ)=R(u),\quad S(u_λ)=λS(u),\quad Q(u_λ)=λ^2Q(u).}\tag{81.1}
\]

Aquí `R(f)=Σ_{k≠0}|\hat f_k|/|k|`, `S(f)=Σ_{k≠0}|\hat f_k|` y `Q(f)=Σ_{k≠0}|k||\hat f_k|`, con media cero. `R` es crítica precisamente porque **no cae** bajo este cambio de escala físico.

Dividir artificialmente `u` por `N` produce `w=u/N`, que en general satisface

\[
\boxed{\partial_t w+N\mathbb P\nabla\cdot(w\otimes w)=\nu\Delta w,}\tag{81.2}
\]

no la misma ecuación de Navier–Stokes con coeficiente convectivo 1. Por eso no se demuestra regularidad al volver diminuto `R(w)` mediante una normalización superficial.

## 2. PDE exacta del resto respecto de una referencia [T]

Trabajamos en `T³=(R/2πZ)³`, con `ν>0`, presión eliminada por proyección de Leray `P` y datos solenoidales suaves de media cero:

\[
\partial_tu+\mathbb P\nabla\cdot(u\otimes u)=\nu\Delta u.
\]

Sea `U` otra solución suave con la misma viscosidad, cuya evolución se conoce. Escribimos **un cambio de descripción sin alterar el campo real**:

\[
\boxed{u=U+v.}\tag{81.3}
\]

Al restar las ecuaciones de `u` y `U`:

\[
\boxed{
\partial_t v+\mathbb P\nabla\cdot(v\otimes v+U\otimes v+v\otimes U)=\nu\Delta v.
}\tag{81.4}
\]

**Los términos cruzados permanecen**. La referencia no elimina las interacciones exteriores: las incluye en el balance de evolución de la información pendiente.

Por el mismo cálculo de Fourier de O80,

\[
\sum_{k≠0}\frac{|\widehat{\mathcal N(v,v)}_k|}{|k|}\le S_v^2\le R_v Q_v,
\]
\[
\sum_{k≠0}\frac{|\widehat{\mathcal N(U,v)}_k|+|\widehat{\mathcal N(v,U)}_k|}{|k|}\le2S_U S_v\le2S_U\sqrt{R_vQ_v}.
\]

Por tanto:

\[
\boxed{D^+R_v+\nu Q_v\le R_vQ_v+2S_U\sqrt{R_vQ_v}.}\tag{81.5}
\]

No se supone simetría de v, paridad de sus componentes ni sincronía de fases.

## 3. Teorema O81-T1: estabilidad del resto respecto de una referencia exacta [T]

**Hipótesis:** `U(t)` es una solución suave global sin fuerza en el toro, de media cero, y

\[
G_\infty:=\frac4\nu\int_0^\infty S_U(t)^2dt<\infty.
\]

Para el dato suave `u₀=U₀+v₀` con resto solenoidal y de media cero, suponga

\[
\boxed{R_v(0)<\frac\nu2 e^{-G_\infty}.}\tag{81.6}
\]

**Conclusión:** la solución de Navier–Stokes con dato `u₀` continúa globalmente de manera suave y el resto cumple, para `M=R_v(0)e^{G_\infty}<ν/2`,

\[
\boxed{R_v(t)\le M,\qquad \int_0^\infty Q_v(t)dt\le\frac{4M}{\nu}.}\tag{81.7}
\]

**Demostración.** Mientras `R_v≤ν/2`, se aplica Young a los términos cruzados:

\[
2S_U\sqrt{R_vQ_v}\le\frac\nu4Q_v+\frac4\nu S_U^2R_v.
\]

Combinando con (81.5) y `R_v Q_v≤νQ_v/2`,

\[
\boxed{D^+R_v+\frac\nu4 Q_v\le\frac4\nu S_U^2R_v.}\tag{81.8}
\]

Defina `G(t)=4/ν∫₀ᵗ S_U²`. Multiplicar por `e^{-G(t)}` da

\[
\boxed{e^{-G(t)}R_v(t)+\frac\nu4\int_0^t e^{-G(s)}Q_v(s)ds\le R_v(0).}\tag{81.9}
\]

De aquí `R_v(t)≤M<ν/2` y se cierra el argumento de continuidad; además, como `e^{-G(s)}≥e^{-G∞}`, se obtiene `∫Q_v≤4M/ν`. En cualquier intervalo finito, `U` es suave y su `Q_U` es integrable. Por (81.7),

\[
\int_0^T\|\nabla u\|_\infty dt\le\int_0^T Q_U(t)dt+4M/ν<\infty.
\]

Un criterio estándar de continuación para soluciones suaves de NS basado en `∫||∇u||∞` excluye la pérdida de regularidad en tiempo finito. La hipótesis sobre `U` ya aporta su regularidad: no se supone la del campo desconocido `u`. **QED.**

Este teorema es una estimación explícita de estabilidad alrededor de una solución conocida, en la tradición de los resultados de estabilidad de Navier–Stokes; no se reclama prioridad como nuevo teorema universal.

### 3.1. Referencia aproximada y costo de defecto [T, condicional]

Para `U` suave y solenoidal que **no necesariamente satisface** NS, defina

\[
F_U=\partial_tU+\mathbb P\nabla\cdot(U\otimes U)-\nu\Delta U,
\quad B_U=\sum_{k≠0}\frac{|\hat F_{U,k}|}{|k|}.
\]

Entonces el lado derecho de (81.5) contiene además `B_U`. Si `R_v≤ν/2`,

\[
D^+R_v+\frac\nu4Q_v\le\frac4\nu S_U^2R_v+B_U.
\]

Se deduce el criterio **con defecto medido**:

\[
\boxed{R_v(t)\le e^{G(t)}\left[R_v(0)+\int_0^t e^{-G(s)}B_U(s)ds\right].}\tag{81.10}
\]

Si el mayorante estricto queda por debajo de `ν/2` para todo tiempo y `B_U` es integrable con la ponderación requerida, la continuidad se obtiene de manera análoga. Ésta es una herramienta para **comparar** un cierre aproximado con una ecuación física: los vínculos omitidos figuran en `F_U` y no pueden esconderse en la etiqueta del normalizador.

## 4. Familia explícita de datos grandes tridimensionales [T/E]

La referencia concreta será una cizalla viscosa exacta:

\[
\boxed{U(y,t)=(A e^{-\nu t}\sin y,\ 0,\ 0),\quad A\ne0.}\tag{81.11}
\]

Aquí `(U·∇)U=0`, `∇·U=0`, `∂t U=νΔU` y la presión puede tomarse constante. Su norma crítica total en el instante cero es `R(U₀)=|A|`, que puede ser arbitrariamente grande. Las magnitudes de Fourier son

\[
S_U(t)=|A|e^{-νt},\quad G_\infty=\frac{2A^2}{ν^2},\quad
\boxed{R_v(0)<\fracν2\exp\!\left(-\frac{2A^2}{ν^2}\right).}\tag{81.12}
\]

Ésta es una condición **explícita y no vacía** para cualquier amplitud `A` finita. La ventana de resto admisible se vuelve extremadamente pequeña para una referencia grande, pero no desaparece.

Instancia numérica con `ν=1`, `A=2` y resto verdaderamente tridimensional:

\[
\begin{split}
v_0(x,y,z)&=\bigl(0,\ \epsilon_1\sin(x+z),\ \epsilon_2\sin x\bigr),\\
\epsilon_1&=\sqrt2\times5\cdot10^{-5},\qquad \epsilon_2=5\cdot10^{-5}.
\end{split}\tag{81.13}
\]

`∇·v₀=0` y tiene contenido en `x` y `z`; junto con `U(y)`, el campo completo depende de las tres coordenadas.

- `R(U₀)=2`.
- `R(v₀)=ε₁/√2+ε₂=0.0001`.
- `R(u₀)=2.0001>ν=1` (soportes espectrales disjuntos).
- Límite admisible `ν e^{-8}/2=0.000167731313951...`.
- Cota de resto `M=R(v₀)e^8≈0.298095799<0.5`.
- Cota dinámica: `∫₀∞ Q_v dt≤4M≈1.192383195`.
- Cota de gradiente total: `∫₀∞ ||∇u||∞dt≤ A/ν+4M/ν≈3.192383195`.

Las interacciones de Fourier en `t=0` de **este mismo dato** producen 12 frecuencias inicialmente desocupadas con derivada no nula. Por ejemplo, un modo `k=(1,1,1)` es activado por el contacto entre la cizalla y el resto. Por tanto, la garantía de continuación no exige que las ramas permanezcan independientes ni que no aparezcan relaciones nuevas.

**Importante:** este ejemplo y su criterio de estabilidad quedan probados analíticamente; la verificación de Fourier en el código comprueba los valores y las interacciones iniciales, pero no hace una simulación temporal de NS.

### 4.1. Presupuesto del costo de nuevas interacciones relativas [T]

Definamos `\mathcal I_v=∫₀∞ Σ_{k≠0}|\widehat{\mathcal N(U,v)+\mathcal N(v,U)+\mathcal N(v,v)}_k|/|k| dt`.

La estimación de Fourier y (81.7) dan

\[
\boxed{\mathcal I_v\le\frac{4M^2}{ν}
+2\sqrt{\frac{A^2}{2ν}\cdot\frac{4M^2}{ν}}.}\tag{81.14}
\]

En el ejemplo numérico la cota es `≈2.04172891`. Es conservadora, pero **es finita a pesar de las nuevas frecuencias**. La diferencia respecto de O80 es que no exige `R(u₀)<ν`, sino un resto pequeño alrededor de una solución coherente conocida.

## 5. Correspondencia con singularidad/cierre propio: qué prueba y qué no [O/T/A]

**[O]** Se puede interpretar `U` como una realización dinámica de la referencia consolidada y `v` como una diferencia pendiente que se transforma dentro de la totalidad. No es necesario llamar singularidad matemática a `U`, ni identificarla con un cuerpo geométrico fijo. El normalizador entero, la referencia dinámica y el resto físico son niveles distinguibles.

**[T]** Si la referencia es una solución de NS y el resto cumple (81.6), las interacciones pueden producir nuevas relaciones, pero su costo crítico acumulado es controlable. **La condición no postula ausencia de novedad.**

**[F]** El cálculo no prueba que *cualquier* flujo grande tenga una descomposición `u=U+v` con `U` conocida, exacta y `R_v` pequeño. Si se toma `U=u` para hacer `v=0`, se incurre en una **circularidad**: se habría supuesto conocida la solución que se quiere demostrar.

**[F]** Una caja de espejos o un refinamiento aritmético no aportan por sí solos un campo `U` que resuelva la ecuación física. Es preciso demostrar el defecto `F_U=0` o mantenerlo en el presupuesto.

**[F]** La escala crítica tampoco se reduce por pasar `N→qN`; la igualdad (81.1) impide esa confusión en el caso de escala física NS.

**[A]** Para una generalización genuina al programa, habría que construir desde el dato inicial (y sin usar el futuro desconocido) un operador intrínseco `u₀→U` o `u₀→(U,v₀)` que entregue referencias dinámicas certificadas, reste defectos controlables y opere para una clase de datos más amplia. Las relaciones de fase y presión de O79/O76 hacen esto no trivial.

## 6. Contraste con bibliografía (no origen de la ontología)

- Lei y Lin, *Global mild solutions of Navier–Stokes equations*, **CPAM 64** (2011), 1297–1304, DOI 10.1002/cpa.20361: criterio clásico de norma crítica de Fourier pequeña en `R³`; O80 es una formulación periódica emparentada.
- Livio Pizzocchero, *On the global stability of smooth solutions of the Navier–Stokes equations*, **Applied Mathematics Letters 115** (2021), 106970: estabilidad global bajo perturbación alrededor de soluciones suaves.
- Chemin, Gallagher y Paicu, *Global regularity for some classes of large solutions to the Navier–Stokes equations*, **Annals of Mathematics 173** (2011), 983–1012: existen clases no triviales de datos iniciales grandes que generan soluciones globales regulares.

Estos precedentes son contrastes externos; no se atribuyen a ellos los conceptos del programa relativos a cierre propio, referencia o eco.

## 7. Siguiente obligación O82, sin repetir la ontología

La pregunta correcta no es «¿puedo dividir por más múltiplos?» sino:

**¿Podemos construir una referencia dinámica física desde las relaciones ya disponibles, certificar su defecto y encontrar una ley de reorganización que mantenga pequeño el resto para configuraciones que no sean perturbaciones diminutas de un flujo conocido?**

Un candidato que no satisfaga las hipótesis debe ser medido como modelo aproximado, no presentado como demostración. Resolver esa pregunta para todos los datos NS generales sería un avance radical; O81 no lo presupone ni lo reclama.

## 8. Reproducción

`python codigo/verificar_o81.py`: verifica analíticamente mediante coeficientes finitos de Fourier las normas, la identidad de escala, solenoidalidad, proyección de la no linealidad, aparición de frecuencias y constantes de la barrera. Genera `resultados/o81_resumen.json` y `o81_ventana_residuo.csv`. `python codigo/graficar_o81.py` crea una gráfica de la ventana admisible frente al tamaño de la referencia. Los 633 chequeos son **comprobaciones de álgebra inicial y de constantes**, no 633 demostraciones de evolución PDE.
