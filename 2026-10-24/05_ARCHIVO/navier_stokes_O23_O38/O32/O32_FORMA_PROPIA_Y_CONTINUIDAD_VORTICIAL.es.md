# O32 — Forma propia, anisotropía y continuidad de dos estructuras vorticiales

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego**  
**20 de octubre de 2026 — suplemento de investigación**  
**Alcance:** continuidad de O29–O31 sin modificar el Núcleo Canónico ni la Imagen Total.  
**Estados:** [O] lectura ontológica; [D] hipótesis explícita; [T] teorema bajo esas hipótesis; [E] controles; [F] límite/refutador; [A] abierto.

## 0. Pregunta, respuesta y atribución

¿Puede certificarse desde Navier–Stokes 2D que dos concentraciones de vorticidad conservan una **diferencia propia de forma**, además de seguir distinguiéndose espacialmente? **Sí**, para un observable de forma cuadrupolar no nulo y un horizonte explícitamente acotado por los datos iniciales. No demostramos preservación de todas las características geométricas, identidad física no etiquetada, bloqueo mutuo de fases, fusión ni regularidad 3D.

Las desigualdades de momentos, la descomposición de vorticidad por etiquetas y la ley de Biot–Savart son herramientas matemáticas conocidas; lo original del suplemento es su *organización* como un certificado de forma relativo a las preguntas del programa y al antecedente O31, no el descubrimiento de nuevas ecuaciones de fluidos.

## 1. Contrato [D]

Trabajamos en R² con Navier–Stokes no forzado de viscosidad ν>0, solución suave y localizada, ω=ω₁+ω₂≥0, y transporte–difusión de cada etiqueta por el mismo campo global:

\[
\partial_t\omega_i+u\cdot\nabla\omega_i=\nu\Delta\omega_i,
\qquad u=\frac{Jx}{2\pi |x|^2}*\omega,
\qquad\nabla\cdot u=0.
\]

Las condiciones iniciales de cada etiqueta son no negativas, integrables, acotadas y de segundo momento finito, y Γᵢ=∫ωᵢ>0. Las etiquetas son una partición inicial de la vorticidad, **no** identificaciones únicas de remolinos físicos. La difusión hace que sus soportes se solapen inmediatamente para t>0; la separación que se certifica es de *concentración*, no de soportes disjuntos.

Sean Γ=Γ₁+Γ₂, M₀=||ω(·,0)||∞. Como en O31, el principio máximo y Biot–Savart dan

\[
\boxed{\|u(t)\|_\infty\le U_0:=\sqrt{\frac{2\Gamma M_0}{\pi}}.}\tag{1}
\]

Para cada componente usamos notación compleja z=x₁+i x₂ y U=u₁+i u₂, centro complejo Cᵢ=(1/Γᵢ)∫zωᵢ, dispersión radial Sᵢ=(1/Γᵢ)∫|z−Cᵢ|²ωᵢ, y **cuadrupolo de forma**

\[
\boxed{Q_i(t)=\frac1{\Gamma_i}\int(z-C_i)^2\omega_i(z,t)\,dA.}\tag{2}
\]

Qᵢ=(Var(x)−Var(y))+2i Cov(x,y). Sᵢ=Var(x)+Var(y). Se sigue |Qᵢ|≤Sᵢ, con igualdad solo en el caso degenerado de covarianza de rango uno. Cuando Qᵢ≠0, la orientación geométrica del eje cuadrupolar es θᵢ=(arg Qᵢ)/2 (módulo π) y su anisotropía normalizada es eᵢ=|Qᵢ|/Sᵢ∈(0,1]. No se iguala θᵢ a la fase de circulación de las partículas, ni eᵢ a una identidad completa del remolino. Para vórtices circulares Qᵢ=0 y θᵢ **no está definida**.

## 2. Teorema O32-T1 — Ecuación exacta de la forma [T]

\[
\boxed{\dot Q_i=\frac2{\Gamma_i}\int(z-C_i)U(z,t)\omega_i(z,t)\,dA.}\tag{3}
\]

**Prueba.** Sea F(z,t)=(z−Cᵢ(t))². Derivar (2): transporte = ∫u·∇F ωᵢ /Γᵢ = (2/Γᵢ)∫(z−Cᵢ)U ωᵢ. El término de desplazamiento del centro es −2 dot Cᵢ∫(z−Cᵢ)ωᵢ/Γᵢ=0. La difusión aporta ν∫ΔF ωᵢ/Γᵢ=0 porque (z−Cᵢ)² es armónica en R². No se ha omitido la influencia indirecta de ν: u y ωᵢ **sí** dependen de la difusión. QED.

Por Cauchy–Schwarz y (1):

\[
\boxed{|\dot Q_i(t)|\le2U_0\sqrt{S_i(t)}.}\tag{4}
\]

Nota: (4) no impone una dinámica de amplitud monótona; solo limita el cambio complejo total desde el dato inicial.

## 3. Teorema O32-T2 — Certificado *a priori* de anisotropía no extinguida [T]

Recuperamos de O31 la cota

\[
\boxed{\sqrt{S_i(t)}\le a_i(t):=\sqrt{S_i(0)+4\nu t}+U_0t.}\tag{5}
\]

Integramos (4):

\[
|Q_i(t)-Q_i(0)|\le H_i(t):=2U_0\int_0^t a_i(s)ds.
\]

Para ν>0 se evalúa **solo con datos iniciales**:

\[
\boxed{H_i(t)=\frac{U_0}{3\nu}\left[(S_i(0)+4\nu t)^{3/2}-S_i(0)^{3/2}\right]+U_0^2t^2.}\tag{6}
\]

Si se considera el límite ν→0, Hᵢ(t)=2U₀√Sᵢ(0)t+U₀²t². El límite debe interpretarse como Euler bajo el correspondiente contrato de regularidad, no como un teorema de NS 3D.

Por desigualdad triangular:

\[
\boxed{|Q_i(t)|\ge |Q_i(0)|-H_i(t).}\tag{7}
\]

Así, si **|Qᵢ(0)|>Hᵢ(T)**, se obtiene Qᵢ(t)≠0 para todo t∈[0,T] y

\[
\boxed{e_i(t)\ge\frac{|Q_i(0)|-H_i(T)}{a_i(T)^2}>0.}\tag{8}
\]

Como Hᵢ y aᵢ son crecientes, usar sus valores en T proporciona una cota común para la ventana entera. Una forma con segundo momento inicialmente anisótropo conserva, entonces, **una diferencia medible de segundo orden** durante ese horizonte.

## 4. Corolario O32-T3 — Acotar la orientación de la forma respecto de la órbita [T]

Si |Qᵢ(0)|>Hᵢ(T), el segmento de Qᵢ(0) a Qᵢ(t) permanece en el disco complejo que no contiene el origen. Para una elección continua de fase:

\[
\boxed{|\arg Q_i(t)-\arg Q_i(0)|\le\arcsin\!\left(\frac{H_i(T)}{|Q_i(0)|}\right).}\tag{9}
\]

Sea r(t)=c₁(t)−c₂(t) y d₀=|r(0)|>0. Como |dot cᵢ|≤U₀, si d₀>2U₀T,

\[
\boxed{|\arg r(t)-\arg r(0)|\le\log\frac{d_0}{d_0-2U_0T}.}\tag{10}
\]

Por tanto, para la orientación de cada forma **relativa al segmento entre centros**, θᵢ^rel=(arg Qᵢ)/2−arg r, resulta

\[
\boxed{|\theta_i^{rel}(t)-\theta_i^{rel}(0)|\le\frac12\arcsin\frac{H_i(T)}{|Q_i(0)|}+\log\frac{d_0}{d_0-2U_0T}.}\tag{11}
\]

Estas cotas son conservadoras, locales en el tiempo y miden deriva angular **máxima**. Una deriva acotada en un intervalo corto no es un atractor de fase ni prueba de sincronización asintótica.

## 5. O32-T4 — Certificado conjunto de concentración separada y forma anisótropa [T]

Fijemos, *antes* del ensayo, un factor k>1, un horizonte T>0 y tolerancias de anisotropía/orientación. Si

\[
\boxed{\begin{aligned}
&k\,[a_1(T)+a_2(T)]<d_0-2U_0T,\\
&|Q_i(0)|>H_i(T)\quad (i=1,2),
\end{aligned}}\tag{12}
\]

entonces durante toda la ventana [0,T]:

1. Los discos B(cᵢ(t), k aᵢ(t)) permanecen disjuntos.
2. Cada disco contiene al menos 1−k^{-2} de la circulación de su propia etiqueta.
3. Ambas etiquetas mantienen eᵢ(t)>0: sus formas **no son circulares respecto de su segundo momento**.
4. Cada orientación relativa a la órbita puede acotarse mediante (11).

**Prueba.** 1–2 son exactamente O31-T4 (Markov/Chebyshev y separación de centros); 3 se deduce de (7)–(8); 4 de (9)–(11). QED.

Es un certificado simultáneo de **persistencia distinguible de dos poblaciones etiquetadas anisótropas**, no prueba de estabilidad de un remolino como objeto topológico de la vorticidad total, conservación de toda su forma, ni formación de una nueva identidad común.

## 6. Ejemplo calculable antes de la evolución [E]

Tomemos dos gaussianas elípticas iguales, positivas, de circulación Γ₁=Γ₂=1 y covarianza inicial diag(0.09,0.01), con centros (−4,0) y (4,0) en R², viscosidad ν=0.001, horizonte T=0.01 y k=2. Entonces:

- S₁(0)=S₂(0)=0.10.
- Q₁(0)=Q₂(0)=0.08 real.
- d₀=8.
- M₀≤1/(π\sqrt{0.09\cdot0.01})=1/(0.03π), cota por suma de picos (no requiere encontrar exactamente el máximo de dos gaussianas).
- U₀≤\sqrt{4/(0.03π²)}≈3.675526.
- aᵢ(T)≈0.3530463 y Hᵢ(T)≈0.02459934.

Para k=2, el criterio de separación compara 4 aᵢ(T)≈1.412185 con d₀−2U₀T≈7.926489: se satisface holgadamente. También Hᵢ(T)<0.08; resulta anisotropía eᵢ(t)≥~0.44448 y deriva del eje relativo ≤~9.483° durante la ventana, usando la cota superior conservadora de M₀. Son **certificados analíticos para cualquier solución bajo este contrato con estos datos iniciales**, no el resultado de una DNS ni una estimación exacta de la rotación real.

## 7. Controles negativos y límites [F/A]

- **No universalidad de la forma cuadrupolar.** Un vórtice circular de Lamb–Oseen tiene Q=0 y aun así posee circulación y escala propias. O32-T2 no lo detecta: la firma debe adaptarse a la pregunta y la simetría de la forma.
- **No cierre espectral absoluto.** O26 demostró con cizallas exactas que las primeras cantidades escalares no determinan toda continuación. Agregar Q mejora una consulta pero no reconstruye todos los futuros.
- **No inferir periodicidad de giro.** El argumento de Q mide orientación de una forma, no fase material de partículas; no se identifica automáticamente con ωᵢ=v*/Rᵢ ni con c, velocidad de la luz.
- **No extender a vorticidad signada por reemplazo.** La positividad y conservación de la circulación positiva son esenciales para la probabilidad ωᵢ/Γᵢ y para U₀ en (1). Se necesita una nueva prueba para remolinos de signos opuestos.
- **No extrapolar a 3D.** El estiramiento de vorticidad y la naturaleza vectorial impiden copiar los momentos positivos escalares.
- **No confundir etiquetas y vórtices físicos.** Dos etiquetas pueden seguir transportándose linealmente aunque el campo total no presente dos centros vorticiales topológicamente identificables. Las condiciones (12) solo garantizan separación de circulación integrada y forma de segundo orden.
- **No afirmar novedad física.** Se trata de desigualdades construidas desde identidad de momentos conocida, no de una nueva fuerza ni de un mecanismo microscópico relacional derivado.

## 8. Correspondencia precisa con el lenguaje del programa [O]

| Noción del núcleo | Correspondencia controlada | No implica |
|---|---|---|
| Forma propia | Qᵢ/Sᵢ como una firma medible de asimetría | descripción exhaustiva de una identidad |
| Comparación | leer dos configuraciones bajo un mismo contrato k,T | selección consciente, voluntad |
| Comunes | mismo flujo u que transporta simultáneamente las dos etiquetas | iguales microestados |
| Módulo | comparación cuantitativa entre extensión y separación | sincronización automática |
| Resto/indefinición | características no determinadas por segundos momentos y etiquetas | azar físico, singularidad blow-up |
| Cierre propio | persistencia relativa a preguntas declaradas durante [0,T] | estabilidad global, autorreferencia física demostrada |
| Referente y escala | centros, d, extensión S y orientación θ | c universal o expansión cosmológica |

La secuencia **diferencia→comparación→comunes→posible cierre propio** pertenece al núcleo; la elección de Q, separación y tolerancias es una *realización física explícita*, no una deducción necesaria de los axiomas. El término «singularidad» se conserva solo para el sentido ontológico de foco, nunca como divergencia del campo.

## 9. Próximo discriminante [A]

Para evaluar un posible cierre común, el siguiente problema **no** es demostrar que cada Q permanece distinto de cero. Es hallar un observable del conjunto que:

1. sea computable desde u y ω sin elección retrospectiva;
2. conserve predicción ante nuevos flujos o perturbaciones;
3. distinga advección coincidente de una fase relativa realmente acoplada;
4. se contraste con dos etiquetas que persisten pero no forman una estructura conjunta estable.

Un blanco concreto es buscar una región/cociente de fase orbital cuya derivada de NS exhiba contracción uniformemente verificable, sin insertar un K arbitrario. Es una obligación abierta, no una conclusión del presente documento.

## 10. Antecedentes

O25 (espejo de escala); O26 (no-go de momentos finitos); O27 (complemento transversal 3D); O28 (fase modular sin agente); O29 (forma y acoplamiento desde Biot–Savart); O30 (momentos conjuntos); O31 (concentración a priori); MF-43 (ritmo lógico sin reloj absoluto); MF-86 (suficiencia por preguntas); Núcleo generativo canónico v0.1 (reflexión, comparación, módulo, residuo).

**Política de integración:** O32 permanece independiente; no modifica la Imagen Total. Toda pretensión de sincronización estructural física exige un nuevo teorema y controles adversariales adicionales.
