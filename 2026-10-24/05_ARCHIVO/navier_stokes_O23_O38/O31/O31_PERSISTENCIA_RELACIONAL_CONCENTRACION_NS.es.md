# O31 — Certificado finito de persistencia vorticial por comparación de módulos

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego** · 19 de octubre de 2026
**Estatus:** suplemento de investigación independiente. No modifica la Imagen Total ni el Núcleo Canónico. Continuidad O25–O30.
**Marcadores:** [O] interpretación ontológica; [D] hipótesis declarada; [T] identidad o teorema bajo hipótesis; [E] verificación reproducible; [F] falsador/no-go; [A] abierto; [H] hipótesis física pendiente.

## 0. Resultado y alcance

**[T]** A partir de los datos iniciales de dos distribuciones suaves de vorticidad positiva en Navier–Stokes 2D no forzado es posible certificar *a priori* un intervalo temporal en el cual cada distribución mantiene al menos una fracción `1−k⁻²` de su circulación dentro de dos discos **disjuntos**. El certificado utiliza solamente las circulaciones, el máximo inicial de vorticidad total, las dispersiones cuadráticas iniciales, la separación inicial y la viscosidad. No introduce velocidad de propagación `c`, coeficiente arbitrario `K` ni una ley externa de sincronización.

**[A]** Este certificado de **dos concentraciones etiquetadas distinguibles** NO es un teorema de conservación de la forma detallada, de bloqueo de fase, de identidad de vórtices no etiquetados, de fusión, ni de regularidad 3D. Es deliberadamente conservador: puede fallar aunque físicamente persistan dos remolinos, y sirve solo un horizonte finito explícito.

## 1. Contrato de la dinámica [D]

Dominio `R²`, viscosidad `ν>0`, sin forzamiento. Campo suave y suficientemente decaído para justificar integraciones por partes y todos los momentos usados:

\[
\partial_t\omega+u\cdot\nabla\omega=\nu\Delta\omega,\qquad
\nabla\cdot u=0,\quad u=K_{BS}*\omega,\quad
K_{BS}(z)=\frac{Jz}{2\pi|z|^2},\quad J(x,y)=(-y,x).
\]

Descomposición **inicialmente declarada** `ω(0)=ω_1(0)+ω_2(0)` con `ω_i(0)≥0`, `ω_i(0)∈ L¹∩L∞`, segundo momento finito, `Γ_i=∫ω_i>0`. Cada etiqueta resuelve la **misma ecuación lineal en el campo total**:

\[
\partial_t\omega_i+u\cdot\nabla\omega_i=\nu\Delta\omega_i.
\]

Por principio del máximo y conservación de masa, `ω_i(t)≥0`, `Γ_i(t)=Γ_i`. Sea `Γ=Γ_1+Γ_2` y `M_0=||ω(0)||_{L∞}`. Como la vorticidad total es escalar pasivo-difusivo en 2D, `||ω(t)||∞≤M_0`.

**Corrección del antecedente:** un renglón de O30 mostraba `u>0`; debe leerse `ω_i≥0`: el campo vectorial `u` no tiene signo positivo escalar.

Datos de cada etiqueta:

\[
c_i=\Gamma_i^{-1}\int x\omega_i\,dx,\quad
S_i=\Gamma_i^{-1}\int |x-c_i|^2\omega_i\,dx,\quad
d=|c_1-c_2|.
\]

Aquí `a_i=√S_i` mide dispersión geométrica, **no** radio espectral `ell_omega=√(∫|ω|²/∫|∇ω|²)` de O25. No se presupone `a_i Ω_i=v_*` ni un significado especial para `c`.

## 2. Lema O31-T1 — Velocidad acotada únicamente por datos de vorticidad [T]

Para cualquier `r>0`, por Biot–Savart, la positividad, `||ω(t)||∞≤M_0` y `||ω(t)||₁=Γ`,

\[
\begin{aligned}
|u(x,t)|
&\le\int_{|x-y|<r}\frac{\omega(y)}{2\pi|x-y|}\,dy
+\int_{|x-y|\ge r}\frac{\omega(y)}{2\pi|x-y|}\,dy\\
&\le M_0 r+\frac{\Gamma}{2\pi r}.
\end{aligned}
\]

La elección `r=√(Γ/(2πM_0))` da

\[
\boxed{\|u(t)\|_{L^\infty}\le U_0:=\sqrt{\frac{2\Gamma M_0}{\pi}}.}\tag{O31.1}
\]

Este `U_0` **no** es una velocidad causal universal ni está relacionado aquí con `c` o `v_*`; es una cota dependiente del estado inicial.

## 3. Lema O31-T2 — Balance de centros y radios [T]

Derivando las definiciones mediante la ecuación de transporte–difusión se obtiene

\[
\dot c_i=\frac{1}{\Gamma_i}\int u\omega_i\,dx,\qquad
\dot S_i=4\nu+\frac{2}{\Gamma_i}\int(x-c_i)\cdot u\,\omega_i\,dx.
\]

Por (O31.1) y Cauchy–Schwarz:

\[
|\dot c_i|\le U_0,\qquad
\boxed{\dot S_i\le4\nu+2U_0\sqrt{S_i}}.\tag{O31.2}
\]

Estas cotas son válidas sin asumir que los dos centros sigan la trayectoria de vórtices puntuales. En particular,

\[
\boxed{d(t)\ge d_0-2U_0t.}\tag{O31.3}
\]

La precisión mejorable de O30 es que, por antisimetría, la advección **propia** cancela exactamente en `dot S_i`; para este certificado utilizamos la desigualdad global más robusta (O31.2), que no requiere estimar el gradiente del flujo cruzado.

## 4. Lema O31-T3 — Cota explícita de extensión [T]

Sea

\[
\boxed{a_i^{\rm sup}(t)=\sqrt{S_i(0)+4\nu t}+U_0 t.}\tag{O31.4}
\]

Afirmación:

\[
\boxed{\sqrt{S_i(t)}\le a_i^{\rm sup}(t)}.\tag{O31.5}
\]

**Demostración por supersolución.** Definimos `F_i(t)=(a_i^{sup}(t))²`, `h_i=√(S_i(0)+4νt)`. Entonces

\[
\dot F_i=2(h_i+U_0t)\left(\frac{2\nu}{h_i}+U_0\right)
=4\nu+2U_0\sqrt{F_i}+\frac{4\nu U_0t}{h_i}
\ge4\nu+2U_0\sqrt{F_i}.
\]

Como `F_i(0)=S_i(0)` y `S_i` satisface la desigualdad diferencial (O31.2), el principio escalar de comparación demuestra `S_i(t)≤F_i(t)`; en caso de radio inicial nulo, usar el límite de regularización o `ν>0`, `t>0`. ∎

El crecimiento lineal `U_0 t` es intencionalmente conservador. Para una sola gaussiana circular de Lamb–Oseen, la identidad más fina es `S(t)=S(0)+4νt` porque la advección propia conserva segundo momento.

## 5. Teorema O31-T4 — Certificado a priori de dos concentraciones distinguibles [T]

Elegimos de antemano un factor `k>1`, y definimos

\[
\boxed{
\mathcal P_k(t)=
\frac{k\left(a_1^{\rm sup}(t)+a_2^{\rm sup}(t)\right)}{d_0-2U_0t}
}\tag{O31.6}
\]

cuando `d_0-2U_0t>0`. Es nuestra *relación modular geométrica* declarada, adimensional y computable con los datos iniciales.

Si en un tiempo `T≥0` se cumple

\[
\boxed{\quad
k\left[\sqrt{S_1(0)+4\nu T}+\sqrt{S_2(0)+4\nu T}+2U_0T\right]
<d_0-2U_0T,
\quad}\tag{O31.7}
\]

entonces, para todo `t∈[0,T]`, los discos

\[
D_i(t)=B\left(c_i(t),\; k\,a_i^{\rm sup}(t)\right)
\]

son disjuntos, y cada uno contiene al menos la fracción

\[
\boxed{\frac1{\Gamma_i}\int_{D_i(t)}\omega_i(x,t)dx\ge1-k^{-2}}.\tag{O31.8}
\]

**Demostración.** La función `a_i^{sup}` es creciente y `d_0-2U_0t` decreciente; así la desigualdad estricta en `T` vale en todo el intervalo. Por (O31.3), `d(t)>k(a_1^{sup}+a_2^{sup})`, luego los discos están separados. La desigualdad de Markov/Chebyshev aplicada a la distribución de probabilidad `ω_i/Γ_i` da

\[
\int_{|x-c_i|\ge k a_i^{sup}}\omega_i\,dx
\le \Gamma_i\frac{S_i(t)}{k^2(a_i^{sup})^2}\le\frac{\Gamma_i}{k^2}.
\]

Restando de la masa total, (O31.8). ∎

**Corolario de dominancia mutua**: en `D_i`, la circulación de la etiqueta ajena es `≤Γ_j/k²`, porque `D_i` es disjunto de `D_j` que contiene al menos `Γ_j(1−k⁻²)`. La etiqueta `i` domina en circulación integrada en su disco si

\[
(k^2-1)\Gamma_i>\Gamma_j.
\]

En particular, si `Γ_1=Γ_2` y `k=2`, cada disco contiene al menos 75% de su propia circulación y como máximo 25% de la etiqueta ajena; dominancia en ambos discos. Esto NO garantiza una cresta puntual, un máximo local ni dos núcleos coherentes topológicos del campo total.

### Existencia de una ventana no trivial

Si `k(√S_1(0)+√S_2(0))<d_0`, por continuidad existe `T>0` que satisface (O31.7). La duración puede ser extremadamente corta cuando la viscosidad o el máximo inicial son grandes.

### Caso cuantitativo reproducible [E]

Datos iniciales: dos gaussianas positivas con `Γ_i=1`, centros `(−4,0)` y `(4,0)`, anchura `a=0.2` en `ω_i(x,0)=Γ_i/(πa²) exp(−|x−c_i|²/a²)`, con `S_i(0)=a²`, viscosidad `ν=0.005`. Sin evaluar el máximo exacto de la suma, usar la cota conservadora `M_0≤2/(πa²)`, `Γ=2`, entonces `U_0≤2√2/(πa)≈4.50158`. Para `T=0.25` y `k=2`:

- extensión acotada por etiqueta: `a_i^sup(T)≈1.33753`;
- suma de radios certificados: `k∑a_i^sup(T)≈5.35011`;
- separación mínima garantizada: `d_0−2U_0T≈5.74921`;
- margen positivo: `≈0.39910`.

**Conclusión certificada:** al menos 75% de cada circulación etiquetada permanece concentrada en discos disjuntos durante todo `[0,0.25]`, independientemente de los detalles adicionales de la interacción, siempre que las hipótesis declaradas se cumplan. Esta es una garantía amplia y débil, no una DNS de dos gaussianas.

## 6. Contraejemplos y límites [F]

1. **Difusión instantánea:** para `ν>0` las gaussianas tienen colas por todo `R²`. El certificado distingue masas dominantes, **no** soportes estrictamente disjuntos.
2. **Sincronización no deducida:** dos centros pueden orbitar sin que las formas cuadrupolares tengan fase `arg Q_i`; un vórtice circular tiene `Q_i=0`. No se deriva un `K` ni la condición de bloqueo de O28.
3. **No necesidad:** cuando (O31.7) falla, no se deduce que hayan desaparecido dos concentraciones; la cota es suficiente, no necesaria.
4. **No unicidad de etiquetas:** si se cambia el reparto inicial de `ω` entre `ω_1` y `ω_2`, cambian `c_i` y `S_i`; una identidad intrínseca de remolino requiere una regla objetiva de segmentación.
5. **No equivalencia de radios:** `√S_i` es un radio de dispersión y `ell_omega` de O25 un radio espectral global; no hay igualdad general entre ambos ni `Rω=v_*` para cualquier vórtice real.
6. **No 3D:** en dimensión tres la vorticidad es vectorial, puede cambiar de magnitud por estiramiento y no existe este principio de máximo para cada componente vorticial; la demostración no se transfiere.
7. **No originalidad física:** la literatura sobre concentración de vórtices 2D dispone de cotas mucho más refinadas, incluidas normas Wasserstein, que aproximan los sistemas de vórtices puntuales. O31 aporta al **programa** un certificado simple calculable con una firma inicial y una lectura epistemológica controlada, no reclama un teorema de Navier–Stokes desconocido.

## 7. Qué significa en lenguaje del programa [O]

- **Trama común:** campo de velocidad `u` determinado por la totalidad de `ω`, no por las intenciones de partes.
- **Relación propia:** vorticidad etiquetada y su concentración geométrica en un marco de comparación. La forma detallada contiene todavía más información que el segundo momento.
- **Módulo:** razón adimensional entre radio total requerido para conservar una fracción dada y separación disponible: `\mathcal P_k`.
- **Comparación:** `\mathcal P_k<1` acredita dos regiones distinguibles; `\mathcal P_k≥1` no decide si se pierde la distinción (residuo abierto).
- **Cierre propio local:** **dentro del contrato de esa pregunta**, conservación temporal de una proporción de las dos circulaciones en regiones disjuntas, sin borrar las diferencias internas. No confundir este cierre operacional con el cierre ontológico universal.
- **Economía:** para la pregunta finita, la firma `\mathscr I=(Γ_i,S_i(0),d_0,M_0,ν,T,k)` es suficiente para acreditar **esta propiedad**, pero no para calcular la evolución completa ni todos los futuros.
- **Sin agencia:** ninguna estructura decide, reconoce o elige; la comparación es una consecuencia de ecuaciones y desigualdades.

### Dos proposiciones epistemológicas diferenciadas

**[T] Suficiencia para certificar:** el conjunto finito de datos iniciales determina una respuesta afirmativa a una consulta limitada y de horizonte finito cuando (O31.7) es estricta.

**[F] Insuficiencia para reconstruir:** los mismos datos no determinan forma, fase, campos locales ni sincronización. El contraejemplo O26 y las fases O29–O30 no desaparecen.

Esta distinción conecta directamente con el principio de interfaz suficiente de MF-86 y el Núcleo: *una nueva referencia conserva lo necesario para las preguntas futuras incluidas en su contrato, no una imagen microscópica exhaustiva de la totalidad*.

## 8. Literatura y genealogía

**Antecedentes del programa:** Núcleo generativo canónico (comparación `C(a,b)=(q,r)` y complemento antes de ortogonalidad); MF-43 (ritmo y recurrencia); O25 (radio espectral); O26 (insuficiencia de momentos finitos para toda evolución); O27 (perpendicularidad y estiramiento 3D); O28 (modelo de fase con coeficiente `K`); O29 (interacción cruzada desde Biot–Savart); O30 (centros, formas, balance de segundo momento).

**Antecedentes de matemática de fluidos — no reclamar descubrimiento original:**
- Stefano Ceci, Christian Seis, *On the dynamics of vortices in viscous 2D flows*, *Mathematische Annalen* 388, 1937–1967 (2024), https://doi.org/10.1007/s00208-023-02568-z . Acredita concentración finita de vórtices viscosos mediante distancias Wasserstein y comparaciones con vórtices puntuales.
- C. Marchioro, M. Pulvirenti, *Vortex Methods in Two-Dimensional Fluid Dynamics*, Springer (1984), https://doi.org/10.1007/3-540-13352-6 .
- O30: balance exacto de segundo momento y leyes de centro; O31 solo añade el certificado a priori de distancia vs. dispersión con supremo inicial de velocidad.

## 9. Pendiente, no promesa [A]

1. Refinar la cota conservadora `U_0` para parejas bien separadas mediante simetría y el gradiente del campo cruzado, en vez de usar la velocidad máxima global.
2. Diseñar una firma **no etiquetada y objetiva** para detectar regiones vorticiales distinguibles y persistentes antes de simularlas.
3. Acoplar el certificado de concentración al tensor de forma cuadrupolar y su orientación, con tolerancias fijadas de antemano, para probar persistencia de una **forma** y no solo de masa.
4. Contrastar las desigualdades con simulaciones 2D de alta resolución y fallos adversariales.
5. Investigar 3D separadamente, sin importar positividad escalar ni suponer regularidad global.

**Resultado O31:** el mecanismo de comparación ya produce una condición **verificable y suficiente para que dos concentraciones continúen distinguibles** durante un tiempo explícito. No impone fusión, sincronía, ni elimina la indefinición asociada a formas y futuros no consultados.
