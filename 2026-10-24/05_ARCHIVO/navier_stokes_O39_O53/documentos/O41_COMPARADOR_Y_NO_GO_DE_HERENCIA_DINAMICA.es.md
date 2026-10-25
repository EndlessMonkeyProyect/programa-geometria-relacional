# O41 — Del normalizador heredado a un comparador dinámico: prueba y límite exacto en Navier–Stokes 3D

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**Fecha:** 20 de octubre de 2026. **Estado:** suplemento autónomo, no modifica el Núcleo Canónico ni la Imagen Total v3.6.0 ni los archivos O39–O40.  
**Leyenda:** [O] ontología/narrativa, [D] definición, [T] teorema bajo contrato, [F] falsador, [P] puente propuesto, [A] abierto. Los teoremas de flujo se apoyan en hechos clásicos de Navier–Stokes y se articulan aquí para el contrato relacional; no se reivindica una nueva prueba del problema de regularidad 3D.

## 0. Hilo narrativo [O]

Una unidad puede sostener su referencia propia mientras cambia de radio, y una unidad que pierde cierto cierre puede participar en cierres de nuevas estructuras. El tetraedro reflejado y la semilla del uno indican **continuidad de una referencia**, no conservación automática de una forma ni de toda su historia. Los dos espejos no necesitan coincidir en sus desplazamientos, pero la comparación debe preservar la trama anterior para las preguntas que promete contestar. La fracción pendiente no es una partícula suelta: es una relación al normalizador que todavía puede intervenir en continuaciones posteriores.

El anillo vorticial, el resorte cerrado, las olas y las burbujas aportan imágenes diferentes: un anillo gaseoso en agua tiene superficie material y tensión superficial; un remolino monofásico de Navier–Stokes tiene vorticidad, no una membrana interna. No se trasladan automáticamente leyes de una imagen a otra.

**Pregunta formal:** si conservamos el comparador de la escala anterior, ¿podemos seguir prediciendo exactamente sus respuestas futuras sin recuperar todo lo que la ampliación había descartado?

## 1. Tres tipos de conservación [D]

Sean \(X\) un espacio de estados, \(\Phi_t\) su evolución (cuando exista y sea única) y \(C:X\to Y\) una interfaz/comparador. Distinguimos:

- **Representabilidad:** una descripción antigua puede incluirse en una nueva representación; p. ej. \(H_N=(1/N)\mathbb Z/\mathbb Z\subseteq H_{\mathrm{mcm}(N,m)}\). Esto es O40 y es exacto aritméticamente.
- **Suficiencia predictiva:** existe una evolución \(\widehat\Phi_t:Y\to Y\) tal que \(C\circ\Phi_t=\widehat\Phi_t\circ C\) para el contrato entero, no sólo para algún dato aislado.
- **Estabilidad física:** una estimación en normas físicas, independiente de la representación y cuantitativamente uniforme en las escalas pertinentes. **No se deduce** de las dos anteriores.

**T1 (criterio de cociente predictivo).** \(\widehat\Phi_t\) bien definido sobre \(C(X)\) existe si y sólo si, para todo par \(u,v\in X\),
\[
 C(u)=C(v)\Longrightarrow C(\Phi_tu)=C(\Phi_tv)\quad \forall t\text{ permitidos}.
\]
*Prueba:* Si la evolución descendida existe, la implicación es inmediata. Si vale la implicación, defina \(\widehat\Phi_t(C(u)):=C(\Phi_tu)\). La implicación hace independiente del representante la definición. La propiedad de semigrupo se hereda de \(\Phi\). \(\square\)

Si \(C\) es diferenciable y el sistema obedece \(\dot u=F(u)\), una condición **necesaria** es \(C(u)=C(v)\Longrightarrow DC(u)F(u)=DC(v)F(v)\). Su fallo en un par ya niega la suficiencia.

## 2. Primer laboratorio — herencia dinámica exacta en una subclase tridimensional [T]

Dominio periódico \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), viscosidad \(\nu>0\), velocidad sin fuerza
\[
 u(x,y,z,t)=(U(y,z,t),0,0),\qquad \int_{\mathbb T^2}U\,dy\,dz=0.
\]
Es solenoidal, \((u\cdot\nabla)u=U\partial_xu=0\), la presión es constante y Navier–Stokes se reduce **exactamente** a
\[
 \partial_tU=\nu(\partial_y^2+\partial_z^2)U,\quad U(t)=e^{\nu t\Delta_{y,z}}U_0.
\]
La vorticidad es \(\omega=(0,\partial_zU,-\partial_yU)\); el estiramiento \((\omega\cdot\nabla)u=0\) en esta subclase.

Para cualquier familia prefijada \(\Lambda\subset\mathbb Z^2\) de modos Fourier cerrada bajo conjugación, sea \(P_\Lambda\) la proyección que conserva esos modos de \(U\). \(P_\Lambda\) conmuta con \(\Delta_{y,z}\) y por tanto
\[
\boxed{P_\Lambda U(t)=e^{\nu t\Delta_{y,z}}P_\Lambda U(0).}\tag{O41.1}
\]
**T2:** el comparador \(C_\Lambda(U)=P_\Lambda U\) es exactamente suficiente, y \(P_\Lambda P_{\Lambda'}=P_\Lambda\) cuando \(\Lambda\subset\Lambda'\), por lo que los diagramas de herencia de O40 conmutan. No necesita conocer modos descartados. La prueba proviene de la diagonalización Fourier del calor. \(\square\)

*Advertencia:* no se ha resuelto la dificultad 3D: esta subclase tiene estiramiento vorticial nulo. Para \(U=Ae^{-\nu t}\sin y+Be^{-4\nu t}\sin 2z\), las dos componentes persisten en el campo, pero sus amplitudes relativas cambian como \((B/A)e^{-3\nu t}\). La conmensurabilidad de números de onda no impone sincronización temporal ni razón de amplitudes fija.

## 3. Segundo laboratorio — no-go exacto de la proyección gruesa, dentro del propio NS [T/F]

Tomamos soluciones de Navier–Stokes tridimensional sobre \(\mathbb T^3\) independientes de \(z\):
\[
 u=(\partial_y\psi,-\partial_x\psi,0),\qquad
 \psi_0(x,y)=A\cos x+B\cos(x-y),\qquad A B\ne0.
\]
Son datos solenoidales suaves de energía finita sobre \(\mathbb T^3\); la evolución 2D embebida existe lisa globalmente. Con la convención \(\omega_z=\partial_xu_y-\partial_yu_x=-\Delta\psi\),
\[
 \omega_{z,0}=A\cos x+2B\cos(x-y).
\]
La ecuación exacta escalar es \(\partial_t\omega_z+u\cdot\nabla\omega_z=\nu\Delta\omega_z\). Por cálculo directo,
\[
 u\cdot\nabla\omega_z=AB\sin x\sin(x-y)
 =\frac{AB}{2}\bigl[\cos y-\cos(2x-y)\bigr].
\]
De aquí,
\[
\boxed{\partial_t\omega_z(0)=
-\nu A\cos x-4\nu B\cos(x-y)
-\frac{AB}{2}\cos y+\frac{AB}{2}\cos(2x-y).}\tag{O41.2}
\]
Defina el comparador de escala gruesa \(C_1(\omega_z)=P_{|k|\le1}\omega_z\), con \(k\in\mathbb Z^2\). Se obtiene
\[
\boxed{C_1(\omega_z(0))=A\cos x,\qquad
\frac{d}{dt}C_1(\omega_z(t))\Big|_{t=0}
=-\nu A\cos x-\frac{AB}{2}\cos y.}\tag{O41.3}
\]
Considere \(B\) y \(-B\), conservando \(A\ne0\): los dos datos presentan **el mismo comparador grueso** (incluida la misma energía de modos alta frecuencia, si sólo se retiene \(|B|^2\)) y, sin embargo, tienen derivadas gruesas distintas de signos opuestos en el nuevo modo \(\cos y\).

**T3 / NO-GO:** no existe una dinámica autónoma \(\widehat\Phi_t\) del comparador \(C_1\) que reproduzca exactamente, para ambas soluciones de esta familia, la evolución gruesa de Navier–Stokes. Tampoco basta aumentar el comparador con la potencia \(|B|^2\) del modo omitido: la fase relativa de ese modo es decisiva. **Prueba:** T1 exige derivadas gruesas idénticas ante datos comparables. O41.3 contradice esa exigencia; \(\square\).

**Cuidado con la conclusión:** no se ha demostrado que todos los comparadores reducidos sean imposibles, ni que todo nuevo modo destruya la regularidad. El ejemplo prueba la insuficiencia de este comparador de amplitudes y escala prefijada, incluso en una subclase de soluciones 3D lisas para todo tiempo.


## 3 bis. Refuerzo: el mismo falsador con estiramiento vorticial realmente tridimensional [T/F]

La pareja T3 también puede transformarse en **datos tridimensionales con estiramiento de vorticidad no nulo**, sin perder la obstrucción. Fijemos \(\varepsilon\ne0\) y usemos
\[
\boxed{u^{B,\varepsilon}_0(x,y,z)=\bigl(\partial_y\psi_0,\,-\partial_x\psi_0+\varepsilon\cos z,\,0\bigr),\quad
\psi_0=A\cos x+B\cos(x-y).}\tag{O41.6}
\]
\(\nabla\cdot u=0\). La vorticidad de estos **datos tridimensionales** es
\[
\boxed{\omega_0=(\varepsilon\sin z,\,0,\,A\cos x+2B\cos(x-y)).}\tag{O41.7}
\]
El término de estiramiento de la ecuación 3D es exactamente, en el instante inicial,
\[
\boxed{(\omega_0\cdot\nabla)u_0
=\varepsilon B\sin z\cos(x-y)\,(1,-1,0),}\tag{O41.8}
\]
que **no es nulo** para \(\varepsilon B\ne0\). No se trata de una evolución 2D embebida: la solución local ya tiene vorticidad con componentes en ejes distintos y estiramiento no trivial. Su existencia lisa se garantiza en algún intervalo local por teoría clásica de Navier–Stokes periódico 3D; no se usa ni se presume existencia global.

Para \(P_{|k|\le1}\) actuando componente a componente sobre \(\mathbb T^3\),
\[
\boxed{\begin{aligned}
P_1\omega_0&=(\varepsilon\sin z,0,A\cos x),\\
P_1\partial_t\omega(0)&=(-\nu\varepsilon\sin z,0,-\nu A\cos x-\tfrac12 AB\cos y).
\end{aligned}}\tag{O41.9}
\]
*Prueba.* La ecuación 3D es \(\partial_t\omega=\nu\Delta\omega-u\cdot\nabla\omega+(\omega\cdot\nabla)u\). Las contribuciones \(\varepsilon\cos z\,\partial_y\omega_z\) y (O41.8) tienen solo frecuencias \((\pm1,\mp1,\pm1)\), de módulo \(\sqrt3\), eliminadas por \(P_1\). El término de interacción original produce \(-AB\cos y/2\), igual que en O41.3; difusión de los modos de norma uno produce las dos contribuciones \(-\nu\varepsilon\sin z\) y \(-\nu A\cos x\). \(\square\)

**T4 (no-go genuinamente 3D).** Cambiar \(B\) por \(-B\) deja idénticos el campo grueso \(P_1\omega_0\), las amplitudes modales iniciales y su energía/enstrofía modal, pero invierte el signo del aporte \(AB\cos y/2\) a la derivada del campo grueso. **No existe** una ley autónoma exacta del comparador espectral grueso, aun si el laboratorio admite estiramiento vorticial no nulo. Este resultado no muestra un estiramiento que explote ni una futura ruptura: exhibe el defecto de una interfaz insuficiente en datos 3D regulares al inicio.

## 3 ter. Control invariante por traslación: la fase cambia incluso la potencia de un modo [T/F]

Para no depender de comparar campos en posiciones absolutas, fijemos **dos modos gruesos** en lugar de uno:
\[
\psi_0=A\cos x+D\cos y+B\cos(x-y),\qquad A D B\ne0.
\]
El comparador grueso sigue siendo \(P_1\omega_z=A\cos x+D\cos y\) para \(B\) y \(-B\). La advección se calcula exactamente:
\[
 u\cdot\nabla\omega_z=B\bigl(A\sin x+D\sin y\bigr)\sin(x-y).
\]
Por tanto,
\[
\boxed{P_1\partial_t\omega_z(0)
=\bigl(-\nu A+\tfrac12 BD\bigr)\cos x
+\bigl(-\nu D-\tfrac12 AB\bigr)\cos y.}\tag{O41.10}
\]
La potencia de Fourier del modo \(k=(0,1)\), definida por \(S_y(t)=|\widehat\omega_{(0,1)}(t)|^2\) con normalización \(\widehat{\cos y}_{(0,1)}=1/2\), satisface
\[
\boxed{\dot S_y(0)=-\frac{\nu D^2}{2}-\frac{ABD}{4}.}\tag{O41.11}
\]
Cambiar \(B\to-B\) **invierte la contribución no viscosa** aunque \(P_1\omega_0\) y todas las magnitudes de Fourier iniciales permanezcan idénticas. A diferencia de una fase cruda, \(S_y\) es **invariante bajo traslaciones espaciales**. Por tanto, el déficit predictivo se registra también en una respuesta física que no depende del origen de coordenadas.

La construcción admite el mismo refuerzo genuinamente tridimensional \(u=(\psi_y,-\psi_x+\varepsilon\cos z,0)\). Las contribuciones adicionales tienen números de onda con componente \(z\) no nula y no alcanzan la proyección \(|k|\le1\) en la derivada inicial. El estiramiento es no nulo para \(\varepsilon B\ne0\). En esta variante también las potencias de los modos iniciales coinciden, pero la derivada de \(S_y\) difiere.

**T5 (falsador de cierre solo por magnitudes).** El conocimiento de un estado grueso completo y de las potencias de modos descartados no determina siquiera la derivada inicial de la potencia de un modo retenido. Una descripción que prometa esa pregunta debe acreditar las relaciones de fase o una variable equivalente de transferencia. El resultado es instantáneo y bajo la familia declarada; no demuestra una teoría general de cascadas ni control de vorticidad máxima.

## 4. Residuo exacto y espejo lateral [D/T]

Para el campo escalar 2D embebido, denotando \(\bar\omega=P_K\omega\) y \(\bar u=P_Ku\), con proyección Fourier que conmuta con derivadas,
\[
 \boxed{\partial_t\bar\omega+P_K(\bar u\cdot\nabla\bar\omega)
 =\nu\Delta\bar\omega-\mathcal R_K,\quad
 \mathcal R_K=P_K\bigl(u\cdot\nabla\omega-\bar u\cdot\nabla\bar\omega\bigr).}\tag{O41.4}
\]
Aquí \(\mathcal R_K\) no es una fuerza inventada ni un residuo ontológico que se pueda suponer pequeño: es la **transferencia no resuelta exacta**. Para la familia anterior,
\[
\boxed{\mathcal R_1(0)=\tfrac12 AB\cos y.}\tag{O41.5}
\]
Interpretación [O]: la normalización anterior puede estar perfectamente heredada y, aun así, la interacción con una diferencia omitida puede afectar su siguiente comparación. El «espejo lateral» no será un generador físico demostrado hasta identificar la parte del flujo que determina y controla \(\mathcal R_K\).

Para el flujo tridimensional general, la identidad pertinente de O39 es
\[
 \frac{d}{dt}\frac12\|\omega\|_2^2=
 \int q^2\alpha-\nu\int|\nabla q|^2-\nu\int q^2|\nabla\xi|^2,
\]
siempre que \(q>0\) donde se use \(\xi\), con interpretación integrable de los términos en los ceros. Esta identidad agrega el estiramiento tridimensional que el laboratorio de O41 no resuelve. No se puede reemplazar la no linealidad por sincronización aritmética sin demostrar una cota.

## 5. Qué significaría «cierra mejor» [P]

Proponemos contratos **alternativos, no equivalentes**: (i) **mejor predicción** = la nueva interfaz incluye el modo de fase que hacía fallar T1 y reduce un residuo definido, (ii) **mejor persistencia** = la nueva configuración sostiene una propiedad durante un intervalo declarado y robusto a perturbaciones declaradas, (iii) **mejor control físico** = una estimación de normas que excluya concentraciones prohibidas. En el ejemplo O41, conocer el signo de \(B\) sí permite conocer la derivada gruesa inicial, pero no garantiza una clausura futura del sistema con sólo dos modos: la no linealidad crea otros modos (\(2x-y\) y \(y\)) desde el instante inicial.

La semilla del uno se lee como referencia **conservada bajo la pregunta declarada**, nunca como un modo oculto que mágicamente controle amplitudes. O40-T1 conserva \(H_N\subset H_{\mathrm{mcm}(N,m)}\); T3 exige controlar la nueva dinámica y prueba que esa conclusión no sigue automáticamente de la inclusión.

## 6. Próxima prueba realmente decisiva [A]

1. Construir un **comparador sensible a fase**, no sólo amplitud, definido intrínsecamente en una clase de anillos vorticiales o tubos de vorticidad, y registrar su transformación por traslación/rotación/cambio de escala.
2. Medir el defecto \(\mathcal R_K\) o el estrés subescala para la evolución 3D real, no sólo en 2D embebido.
3. Relacionar cuantitativamente pérdida de suficiencia con balance de estiramiento, reorientación, difusión y flujo a través del radio móvil de O39.
4. Derivar de la ecuación una desigualdad no circular que controle \(\int_0^T\|\omega\|_\infty dt\) o un criterio de continuación comparable; protegerse de las cascadas infinitas en tiempo finito de O40.
5. Contrastar controles adversariales: vórtice Burgers (giro nulo con aumento material de intensidad), interacción de fases \(B\leftrightarrow-B\) y cambios de escala parabólica. No atribuir a viscosidad monofásica tensión superficial de burbujas.

**Estado final:** T1–T5 y O41.4 son matemáticos exactos para sus contratos. O41 ofrece un criterio operacional de suficiencia y un no-go de comparador grueso, no una solución de Navier–Stokes 3D ni una afirmación de novedad en análisis clásico de fluidos.
