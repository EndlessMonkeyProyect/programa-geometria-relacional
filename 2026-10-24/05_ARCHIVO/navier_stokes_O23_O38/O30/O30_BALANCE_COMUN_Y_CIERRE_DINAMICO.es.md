# O30 — Balance común, forma propia y cierre dinámico de pares vorticiales

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego** · 19 de octubre de 2026  
**Alcance:** suplemento independiente y contrastable. No modifica el Núcleo, O24–O29 ni la Imagen Total.  
**Etiquetas:** `[O]` lectura ontológica; `[D]` contrato matemático; `[T]` teorema condicionado; `[E]` control reproducible; `[F]` refutador; `[H]` puente físico hipotético; `[A]` abierto.

## 0. Pregunta y resultado principal

¿Puede la compatibilidad modular entre dos formas vorticiales producir un cierre común persistente desde el flujo, sin introducir por decreto un coeficiente `K` de sincronización?

**Respuesta:** de Navier–Stokes 2D sí se obtienen (i) una ley exacta para la velocidad de separación y el ritmo orbital; (ii) una relación exacta para la evolución de la forma y de la fase cuadrupolar; y (iii) un presupuesto exacto de segundo momento que relaciona ambas formas con su separación. **No** se obtiene de estas identidades un teorema universal de bloqueo de fases, persistencia de identidades, fusión, o regularidad de Navier–Stokes 3D. La palabra "módulo" denota una comparación entre relaciones, no la voluntad o el reconocimiento de un remolino.

La novedad interna frente a O29 es reunir exactamente **separación ↔ orientación ↔ extensión de forma ↔ difusión** e investigar su suficiencia para reconstruir una continuación. El balance de segundo momento y las leyes de vórtices forman parte de la matemática conocida de fluidos; no son descubrimientos físicos originales por cambiarles el lenguaje.

## 1. Contrato [D]

En `R²`, Navier–Stokes no forzado de viscosidad `ν>0`, escrito en vorticidad:

\[
\partial_t\omega+u\cdot\nabla\omega=\nu\Delta\omega,\qquad
u>0,\qquad u=K_{BS}*\omega,\qquad K_{BS}(z)=\frac{Jz}{2\pi|z|^2},\quad J(x,y)=(-y,x).
\]

Admitimos soluciones suaves suficientemente localizadas para integración por partes y momentos finitos, con `ω=ω_A+ω_B`, dos vorticidades etiquetadas no negativas, inicialmente declaradas y transportadas por el **mismo** campo `u`:

\[
\partial_t\omega_i+u\cdot\nabla\omega_i=\nu\Delta\omega_i,\quad i=A,B.
\]

Esta distinción es una **contabilidad por etiquetas elegidas en los datos iniciales**, no una segmentación objetiva única de remolinos. La difusión genera solapamiento de las etiquetas, aunque cada población etiquetada conserve su circulación `Γ_i=∫ω_i>0`.

Definimos:

\[
 c_i=\frac{1}{\Gamma_i}\int x\omega_i\,dx,\quad
 S_i=\frac{1}{\Gamma_i}\int|x-c_i|^2\omega_i\,dx,\quad
 r=c_A-c_B,\quad d=|r|,
\]

\[
 I_{AB}=\iint K_{BS}(x-y)\omega_A(x)\omega_B(y)\,dx\,dy.
\]

Para una fase interna de forma, en coordenadas complejas `z=x₁+i x₂`, definimos:

\[
Q_i=\frac{1}{\Gamma_i}\int (z-C_i)^2\omega_i\,dx,\qquad
\phi_i=\arg Q_i\ (Q_i\ne0),\qquad
\chi_i=\frac{|Q_i|}{S_i}\in[0,1].
\]

El ángulo del eje del elipsoide cuadrupolar es `φ_i/2 mod π`; `φ_i` **no** es automáticamente fase de circulación del agua, frecuencia `v*/R` ni periodicidad de un oscilador. Si `Q_i=0`, `φ_i` está indefinida, incluso si la población es un vórtice circular coherente.

## 2. O30-T1 — Movimiento relativo sin K arbitrario [T]

El mismo argumento de antisimetría de Biot–Savart que aparece en O29 da:

\[
\boxed{\dot c_A=\frac{I_{AB}}{\Gamma_A},\qquad
\dot c_B=-\frac{I_{AB}}{\Gamma_B},\qquad
\dot r=\left(\frac1{\Gamma_A}+\frac1{\Gamma_B}\right)I_{AB}.}\tag{1}
\]

En todo intervalo con `d>0`, la descomposición geométrica es exacta:

\[
\boxed{\dot r=g\,r+\Omega_{\rm orb}\,Jr,\qquad
 g=\frac{r\cdot\dot r}{d^2}=\frac{\dot d}{d},\quad
 \Omega_{\rm orb}=\frac{Jr\cdot\dot r}{d^2}=\dot{\arg r}.}\tag{2}
\]

Aquí `g` representa escala relativa (expansión/contracción); `Ω_orb` representa orientación orbital. Ambas se obtienen del **mismo funcional no local de forma** `I_AB`, y no se insertan como parámetros ajustados. No confundir `Ω_orb` con `ω_i=v*/R_i` del canal espectral del programa.

**Control puntual límite de Euler.** Dos masas vorticiales ideales en posiciones separadas `d` producen `I_AB=Γ_AΓ_B K_BS(r)` y entonces:

\[
g=0,\qquad \Omega_{\rm orb}=\frac{\Gamma_A+\Gamma_B}{2\pi d^2}.
\]

La recurrencia de la órbita no es una prueba para NS viscoso: las medidas Dirac de Euler no son las dos gaussianas suaves que interactúan para `ν>0`.

## 3. O30-T2 — Balance de forma y radio compartido [T]

Cada segundo momento central sigue la identidad:

\[
\boxed{\dot S_i=4\nu+\frac{2}{\Gamma_i}\int(x-c_i)\cdot u_j(x)\,\omega_i(x)\,dx,\quad j\ne i.}\tag{3}
\]

**Prueba:** derivar `∫|x-c_i|²ω_i` usando transporte-difusión. La derivada del centro desaparece porque `∫(x-c_i)ω_i=0`. La difusión da `ν∫ Δ|x-c_i|² ω_i /Γ_i=4ν`. La parte propia de advección es proporcional a la doble integral simétrica de `(x-y)·K_BS(x-y)=0`, de modo que se anula. Solo queda la velocidad inducida por la otra etiqueta. QED.

Sea `Γ=Γ_A+Γ_B`, `C=(Γ_A c_A+Γ_Bc_B)/Γ`. La identidad de varianza de mezcla (Huygens) da:

\[
\frac1\Gamma\int|x-C|^2\omega\,dx
=\frac{\Gamma_A}{\Gamma}S_A+\frac{\Gamma_B}{\Gamma}S_B+
\frac{\Gamma_A\Gamma_B}{\Gamma^2}d^2.
\]

La velocidad total `u` del fluido no cambia el segundo momento central global en 2D no forzado; de nuevo, `(x-y)·K_BS(x-y)=0`. La difusión aporta `4νΓ`. Por tanto:

\[
\boxed{\Gamma_A S_A(t)+\Gamma_B S_B(t)+\frac{\Gamma_A\Gamma_B}{\Gamma}d^2(t)
= M_0+4\nu\Gamma t,}\tag{4}
\]

con `M_0=∫|x-C|² ω(x,0)dx`. Esta es una **identidad exacta para NS 2D suave y no forzado**. Si `ν=0`, el presupuesto es conservado (Euler). Si `ν>0`, aumenta linealmente: **no** se conserva una energía o longitud física global; se conserva la forma explícita de un balance.

Por positividad de las vorticidades etiquetadas, `S_i≥0`. Por tanto se obtiene la cota rigurosa, aunque débil:

\[
\boxed{d(t)^2\le\frac{\Gamma}{\Gamma_A\Gamma_B}\bigl(M_0+4\nu\Gamma t\bigr).}\tag{5}
\]

**Interpretación:** sus extensiones radiales y la distancia relativa participan en un mismo presupuesto. La relación no afirma que un acortamiento de distancia *deba* aumentar una extensión en cierta proporción a cada instante; la difusión añade presupuesto.

## 4. O30-T3 — La diferencia entre coherencia de órbita y forma [T]

La fase de forma cuadrupolar, cuando existe, satisface la identidad O29:

\[
\dot Q_i=\frac2{\Gamma_i}\int (z-C_i)U(z)\omega_i\,dx,
\qquad \dot\phi_i=\operatorname{Im}\frac{\dot Q_i}{Q_i}.
\]

Definamos la fase **relativa a la órbita** de la forma elíptica:

\[
\boxed{\psi_i=\phi_i-2\arg r,\qquad
\dot\psi_i=\operatorname{Im}\frac{\dot Q_i}{Q_i}-2\Omega_{\rm orb}.}\tag{6}
\]

La razón `2` aparece porque la fase del momento cuadrupolar es dos veces la orientación del eje de forma.

Y para la magnitud anisótropa:

\[
\boxed{\frac{d}{dt}\log\chi_i=
\operatorname{Re}\left(\frac{\dot Q_i}{Q_i}\right)-\frac{\dot S_i}{S_i},\qquad Q_i\ne0,\ S_i>0.}\tag{7}
\]

**Criterio de control prospectivo, no ley universal:** una estructura de pares podría considerarse persistente en una ventana `[t_0,T]` si, tras fijar de antemano las tolerancias, el radio orbital `d(t)` no se anula, las fases `ψ_i` permanecen en ventanas establecidas y sus anisotropías `χ_i` no colapsan a cero; si la identidad de cada vórtice no es elíptica, debe especificarse otra firma de forma objetiva y verificable. Satisfacer estas condiciones no equivale automáticamente a fusión física ni a un atractor.

**Diferencia exacta:** `Ω_orb` puede existir con `Q_A=Q_B=0`. Entonces existe giro conjunto de centros, pero **no** hay orientación de forma cuadrupolar que sincronizar. En el límite puntual `Q_i=S_i=0`, el giro de centros está definido y la forma interna no. Esto refuta una equivalencia automática entre cierre orbital, cierre de forma y cierre físico de identidad.

## 5. O30-F1 — Un contraejemplo a equiparar fase y conservación de forma [T/F]

La familia exacta de NS 2D de cizalla

\[
u(x,y,t)=(a e^{-\nu t}\sin y+b e^{-4\nu t}\sin 2y,\ 0)
\]

con `a,b≠0` es una solución periódica no forzada: `(u·∇)u=0`, y cada componente evoluciona por difusión. Las **fases espaciales de ambos armónicos permanecen constantes** sin acoplamiento alguno, mientras su relación de amplitudes cambia como

\[
\frac{|b|e^{-4\nu t}}{|a|e^{-\nu t}}=\frac{|b|}{|a|}e^{-3\nu t}.
\]

La forma espacial normalizada cambia. Un acuerdo constante de fases de Fourier **no es** persistencia de forma, y esta cizalla no se presenta como pareja de remolinos aislados. La prueba opera a nivel de modos: demuestra la insuficiencia de una firma de fase sola, incluso dentro de una solución exacta de NS.

Otro control: el vórtice de Oseen radial es una solución exacta, de forma gaussiana autosimilar, cuya escala crece como raíz del tiempo. Tiene `Q=0`: su persistencia relativa a escala no depende de una fase cuadrupolar.

## 6. O30-T4 — Suficiencia relativa a la pregunta [T/O]

La interfaz

\[
\mathscr I_{\rm centros}=(\Gamma_A,\Gamma_B,r,I_{AB})
\]

**es suficiente para responder la pregunta instantánea** "¿cuál es la velocidad relativa de centros?", porque la ecuación (1) factoriza por ella. Pero no es automáticamente suficiente para "¿cómo será esa velocidad mañana?"; la derivada de `I_AB` depende de la evolución de las formas, la viscosidad y el transporte. La jerarquía no desaparece cambiando el nombre de la proyección.

La interfaz aumentada `(Γ_i,r,I_AB,S_i,Q_i,dot Q_i)` responde más consultas instantáneas, pero no se acredita como interfaz finita suficiente para todas las continuaciones. Esta es una realización de la distinción entre *parte resuelta* y *resto* del Núcleo Canónico y de O23/O26.

**El cierre relacional del discurso no se basa en intención:** un cambio de escala, orientación o forma es efecto de las ecuaciones del flujo. El módulo compartido no asegura la anulación de las diferencias propias. Sin embargo, la identidad de cada etiqueta depende de la segmentación inicial, y una etiqueta difusa puede persistir matemáticamente aunque ya no exista un remolino distinguible físicamente.

## 7. Falsadores, atribuciones y pasos siguientes [F/A/H]

- `[T]` Demostrado: (1)–(7) bajo el contrato de NS 2D, localización, signos no negativos, etc. El cálculo de `Q_i` requiere `Q_i≠0`.
- `[E]` Los controles computacionales prueban solo la parte de advección en el submodelo de vórtices puntuales inviscidos de Euler. No ejecutan DNS ni verifican numericamente una identidad viscosa en campos suaves; `4νΓ` y (4) se deducen por integración por partes.
- `[F]` La igualdad de los radios y circulaciones, o una relación racional de frecuencias, no determina por sí misma la persistencia. O29 ya ofreció formas con la misma firma radial y distinto acoplamiento.
- `[F]` `Q_i=0` refuta la pretensión de que toda estructura coherente tenga fase de orientación cuadrupolar. No invalida su circulación.
- `[A]` Una reducción de fase `dot ψ=δ−K sin ψ` no se deriva de (1)–(7) sin un teorema de reducción, promedio o régimen asintótico adicional.
- `[A]` En 3D hay estiramiento vorticial y transporte de dirección; las identidades de segundo momento para vorticidad escalar positiva no se exportan por sustitución.
- `[A]` Ningún resultado prueba `v_*=c`, ni regularidad global NS 3D, ni una ley nueva de fuerza o sincronización universal.
- `[H]` Para avanzar: definir firma objetiva de formas vorticiales (posiblemente mediante segundo tensor de momentos y transporte), establecer ventanas de coherencia sin ajuste retrospectivo y contrastar con pares de vortices viscosos de alta resolución y con adversarios.

## 8. Genealogía documentada y literatura

- Núcleo generativo canónico v0.1: `C(a,b)=(q,r)` como comparación y residuo; complemento antes de ortogonalidad, economía de la estructura.
- MF-43: recurrencia y ritmo relativo bajo hipótesis; no equivale al tiempo físico absoluto.
- O25: espejo dinámico seleccionado desde vorticidad.
- O26: radio y primeros momentos espectrales no son suficientes para toda continuación.
- O27: perpendicularidad y estiramiento en 3D; complemento relacional ≠ dimensión añadida.
- O28: relaciones enteras de fase sin agencia; `K` ilustrativo pendiente.
- O29: identidad exacta `I_AB`, fase compleja cuadrupolar, contraste de forma longitudinal/transversal.
- Thierry Gallay, *Stability and interaction of vortices in two-dimensional viscous flows*, DCDS-S (2012), DOI 10.3934/dcdss.2012.5.1091, https://www.aimsciences.org/article/doi/10.3934/dcdss.2012.5.1091.
- Thierry Gallay, *Interaction of vortices in viscous planar flows*, https://arxiv.org/abs/0908.2518. Reconoce límites rigurosos de núcleos viscosos y aproximación por vórtices puntuales; no deduce fusión universal.
- Thierry Gallay y Yasunori Maekawa, *Existence and stability of viscous vortices*, https://arxiv.org/abs/1610.08384.

**Tesis O30:** el mismo sistema puede sostener dos formas particulares y un presupuesto geométrico común; el cierre del presupuesto no borra la diferencia entre las formas, y la coincidencia instantánea de módulos no garantiza su estabilidad futura.
