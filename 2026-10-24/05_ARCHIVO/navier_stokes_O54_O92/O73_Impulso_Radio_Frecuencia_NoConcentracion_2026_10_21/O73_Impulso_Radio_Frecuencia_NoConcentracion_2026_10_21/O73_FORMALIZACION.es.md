# O73 — Impulso, radio y normalización de la vorticidad: qué sostiene el anillo y qué no evita su concentración

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**21 de octubre de 2026 | Suplemento autónomo y aditivo a O53–O72**  
**Estado epistémico:** ontología y narrativa [O/N]; identidades clásicas deducidas [D]; construcción de familia de datos [T]; controles computacionales [E]; hipótesis de interpretación [H]; límites/falsadores [F]. **No es solución del problema general de regularidad de Navier–Stokes 3D.**

## 0. Narrativa → ontología → cálculo, sin energía como fundamento

**[N]** La cápsula alcanza cierre propio, y las cápsulas vinculadas pueden sostener un circuito en movimiento aunque se renueven sus participantes materiales. La proyección del tetraedro como anillo coplanar de cuatro enlaces activos libera grados de libertad. La dirección global puede emerger de una orientación de las relaciones; el momento sería el sostén en ejecución de la singularidad. No se identifica aquí la «singularidad ontológica» con una singularidad matemática del campo de velocidades.

**[O]** La referencia de la configuración es colectiva: el mismo múltiplo que la normalizó puede reaparecer en una escala distinta. La identidad no requiere inmovilidad de radios ni conservar partículas particulares; sí requiere alguna relación de continuidad suficientemente informativa. Lo resuelto no deja de serlo porque otra relación deje de estar habitada. La indefinición se expresa como libertad de evolución, no como azar intrínseco.

**Pregunta [F].** ¿Pueden circulación, área orientada, radio efectivo y frecuencias proporcionar la no-degeneración que no dieron los engranajes O72? ¿Existe una relación físicamente impuesta por Navier–Stokes que impida un núcleo arbitrariamente fino sin usar la energía como definición de la unidad?

La respuesta de O73 tiene dos partes: **(A)** impulso + circulación + radio colectivo no fijan un grosor mínimo del núcleo; **(B)** dentro de la clase axisimétrica sin giro azimutal existe una variable normalizada `η=ω^θ/r` que satisface una ecuación con principio del máximo. Es un puente dinámico exacto pero restringido.

## 1. Qué significa un anillo vorticial sin suponer dos giros sincronizados

Adoptamos coordenadas cilíndricas `(r, θ, z)` alrededor del eje de propagación `z`.

**[D]** En una configuración axisimétrica sin componente azimutal de velocidad (*without swirl*),

\[
 u(r,z,t)=u^r(r,z,t)e_r+u^z(r,z,t)e_z,
 \qquad \omega=\omega^\theta(r,z,t)e_\theta.
\]

El fluido puede girar en el plano meridiano `(r,z)` y el anillo propagarse a lo largo de `z`; esto **no** exige que sus partículas roten alrededor del eje `z`. Dos ciclos topológicos de un toroide no equivalen automáticamente a dos frecuencias materiales no nulas (O69).

Las cápsulas de O72 son un **laboratorio abstracto** de las diferencias sincronizadas, no partículas rígidas del fluido. Conservar el sentido del giro de un conjunto de engranajes no se identifica sin derivación con la circulación del anillo.

## 2. Impulso colectivo y dirección — identidad clásica [D]

Sea `ρ>0` la densidad constante y supongamos que el campo es suficientemente suave y decae en `R³` para justificar los cambios de orden y las integraciones por partes. El impulso hidrodinámico es

\[
 \boxed{\mathbf I=\frac{\rho}{2}\int_{\mathbb R^3}x\times\omega(x)\,d^3x.}\tag{73.1}
\]

Con vorticidad puramente azimutal, y por integración en `θ`,

\[
 \boxed{I_z=\rho\pi\int_0^\infty\int_{-\infty}^{\infty}r^2\omega^\theta(r,z)\,dz\,dr.}\tag{73.2}
\]

Definimos la circulación de la sección **en el instante inicial** `Γ₀=∫ω₀^θ dr dz`. Si `Γ₀>0`, definimos un radio efectivo inicial

\[
 \boxed{R_{\mathrm{ef},0}^2=\frac{I_z(0)}{\rho\pi\Gamma_0}=\frac{\int r^2\omega_0^\theta\,dr\,dz}{\int\omega_0^\theta\,dr\,dz}.}\tag{73.3}
\]

Para un anillo de núcleo fino `a≪R`, `I_z≈ρπΓR²`. La igualdad de (73.2) es **exacta**, la fórmula del filamento es una **aproximación**. Como consecuencia de la estructura de `x×ω`, el signo de `I_z` especifica orientación global; no da por sí solo la velocidad instantánea del anillo.

### 2.1 Conservación condicional del impulso [D]

Para Navier–Stokes incomprensible en todo `R³` sin fuerza externa y decaimiento suficiente,

\[
 \omega_t=\nabla\times(u\times\omega)+\nu\Delta\omega.
\]

Multiplicar por `ρ x×/2` e integrar da

\[
 \frac{d\mathbf I}{dt}=\rho\int(u\times\omega)\,d^3x=0,
\]

porque `u×ω=∇(|u|²/2)−(u·∇)u` y, tras integrar, ambos términos tienen integral cero. El término viscoso integrado se anula bajo las mismas hipótesis de borde. Este paso no vale sin modificaciones en recipientes con paredes, flujo forzado, densidad variable o cajas periódicas con una coordenada `x` no globalmente definida.

**Advertencia:** el impulso conservado no demuestra que `Γ(t)` permanezca constante. Para Navier–Stokes viscoso, la circulación a lo largo de un lazo material puede variar: `dΓ_C/dt=ν∮_C Δu·dℓ`. Por ello tampoco se afirma que `R_ef(t)` de (73.3) sea constante.

## 3. Contraejemplo constructivo: mismo impulso, circulación y radio, núcleos cada vez más finos [T]

Tomemos una función no negativa, radial, suave y de soporte compacto sobre el disco unitario del plano `(ξ,ζ)`:

\[
 b(s)=\begin{cases}e^{-1/(1-s^2)},&0\le s<1,\\0,&s\ge1,\end{cases}
 \qquad
 \varphi(\xi,\zeta)=\frac{b(\sqrt{\xi^2+\zeta^2})}{C},
 \quad C=\iint_{\mathbb R^2}b\,d\xi\,d\zeta.
\]

Así `∫φ=1`, `∫ξφ=0`, `κ=∫ξ²φ>0`. Para valores fijos `R_*>0`, `Γ₀>0` y `ρ>0`, y para cualquier `a>0` suficientemente pequeño, definamos

\[
 \boxed{R_a=\sqrt{R_*^2-\kappa a^2},\qquad
 \omega_{0,a}^\theta(r,z)=\frac{\Gamma_0}{a^2}
 \varphi\left(\frac{r-R_a}{a},\frac za\right).}\tag{73.4}
\]

Imponemos `R_a>a`, de modo que la vorticidad se localice lejos del eje `r=0`. Es `C∞` de soporte compacto; el campo vectorial azimutal `ω=ωθ eθ` es divergencia-cero y el campo inicial `u_{0,a}` reconstruido por Biot–Savart es suave, incompresible y axisimétrico sin swirl.

**Demostración [T].** Cambio de variables `ξ=(r−R_a)/a`, `ζ=z/a` y simetría del perfil:

\[
 \Gamma_{0,a}=\iint\omega_{0,a}^\theta dr dz=\Gamma_0,
\]

\[
 I_{z,0,a}=\rho\pi\Gamma_0\underbrace{(R_a^2+\kappa a^2)}_{R_*^2}
 =\boxed{\rho\pi\Gamma_0R_*^2}.\tag{73.5}
\]

Por tanto, el radio efectivo es siempre `R_*`, aunque el grosor de núcleo es `a`. Entretanto,

\[
 \boxed{\|\omega_{0,a}\|_\infty
 =\frac{\Gamma_0\varphi(0,0)}{a^2}\xrightarrow[a\to0]{}\infty.}\tag{73.6}
\]

**Corolario [T].** No existe una función finita `F` sólo de `(ρ,Γ₀,I_z(0),R_ef,0)` tal que para todos los datos axisimétricos suaves sin swirl y con esos valores se cumpla `||ω₀||∞≤F`. En particular, el impulso, la circulación inicial y la referencia radial colectiva **no proporcionan un radio mínimo universal del núcleo**.

**Alcance preciso:** estas configuraciones son **datos iniciales diferentes**. No se ha mostrado que una sola solución evolucione contrayendo su núcleo como `a→0` en tiempo finito. De hecho, por la regularidad global conocida en la clase axisimétrica sin swirl, cada dato suave de esta familia genera su propia evolución suave global. La familia es un contraejemplo a una **cota uniforme basada en esos invariantes**, no un contraejemplo a la regularidad global.

## 4. Relación normalizada que sí obedece a la dinámica [D]

En esta clase sin giro azimutal se cumple

\[
 \partial_t\omega^\theta+u^r\partial_r\omega^\theta+u^z\partial_z\omega^\theta
 =\frac{u^r}{r}\omega^\theta
 +\nu\left(\partial_{rr}+\frac1r\partial_r+\partial_{zz}-\frac1{r^2}\right)\omega^\theta.\tag{73.7}
\]

**La cancelación central:** definamos `η=ω^θ/r` para `r>0`, extendida suavemente sobre el eje cuando procede. Al sustituir `ω^θ=rη`, el término de estiramiento `u^rω^θ/r` se cancela exactamente con el derivado material de `r`:

\[
 \boxed{\partial_t\eta+u^r\partial_r\eta+u^z\partial_z\eta
 =\nu\left(\partial_{rr}+\frac3r\partial_r+\partial_{zz}\right)\eta.}\tag{73.8}
\]

El operador radial `∂rr+3/r∂r` es el laplaciano para funciones radialmente simétricas en **cuatro coordenadas radiales**; al añadir `z`, la difusión equivale formalmente a un laplaciano de **cinco dimensiones**, con deriva. Esto no afirma que el fluido tenga cinco dimensiones espaciales: es una identidad de representación del operador.

Bajo las condiciones usuales de solución clásica y decaimiento, el principio del máximo da

\[
 \boxed{\|\eta(t)\|_{L^\infty}\le\|\eta(0)\|_{L^\infty},\quad t\ge0.}\tag{73.9}
\]

Esta no es una hipótesis puesta sobre los engranajes: es **consecuencia exacta de Navier–Stokes en la subclase indicada**. La ecuación (73.8) por sí sola no sustituye todos los pasos de una prueba de regularidad global; la regularidad de la clase ha sido establecida por literatura previa, entre otros trabajos de Gallay–Šverák (2015).

## 5. Una cota concreta de no-concentración, con hipótesis [T]

Sea `A` una región medible del corte meridiano, contenida en `0≤r≤Rmax`, y `M=||η(0)||∞`. Para tiempos en que rija (73.9),

\[
 \int_A|\omega^\theta(r,z,t)|\,dr\,dz
 =\int_A r|\eta|\,dr\,dz
 \le \boxed{R_{\max}M\,|A|}.\tag{73.10}
\]

Por consiguiente, si una región lleva al menos una circulación absoluta `γ_c>0`,

\[
 \boxed{|A|\ge \frac{\gamma_c}{R_{\max}\,\|\eta(0)\|_\infty}.}\tag{73.11}
\]

**Lectura:** en esta familia de flujos, una cantidad no nula especificada de circulación no puede concentrarse en un área arbitrariamente pequeña **dentro de un radio acotado**, si el valor inicial `||ωθ/r||∞` permanece fijado. Ésta es una condición condicional de no-concentración verdadera, expresada primero mediante una relación de vorticidad y radio, no mediante energía.

**Límites exactos:** (i) `M` depende del dato inicial y puede hacerse arbitrariamente grande manteniendo `I`, `Γ₀` y `R_ef` fijos, según §3; (ii) no se ha demostrado una cota global de `r≤Rmax` para todo el soporte viscoso, que deja de ser compacto inmediatamente; (iii) el enunciado se refiere a una **región seleccionada** con cota radial y circulación absoluta, no a la existencia eterna de una superficie material de cápsula.

## 6. ¿Qué sucede si activamos el segundo giro? [F]

En la clase axisimétrica con componente azimutal de velocidad `u^θ≠0`, la ecuación para `η=ω^θ/r` contiene además un término de fuente:

\[
 \boxed{D_t\eta=\nu(\partial_{rr}+3r^{-1}\partial_r+\partial_{zz})\eta
 +\frac{1}{r^4}\partial_z\left[(ru^\theta)^2\right].}\tag{73.12}
\]

El término adicional se puede comprobar sustituyendo la ecuación de vorticidad axisimétrica. La **cancelación simple** del caso sin giro azimutal deja de bastar: la fuente puede tener ambos signos, por lo que la cota (73.9) no se obtiene aplicando el mismo argumento directamente.

Ésta es la conexión con la propuesta de O72: en la subclase de anillo sin giro azimutal, una relación normalizada sostiene una regla regularizante. Cuando se permite otro grado de libertad de giro, su interacción introduce una obligación adicional. **No hemos demostrado** que el modo alternado del circuito de cuatro cápsulas sea equivalente a `u^θ`, ni que el término fuente determine de forma universal la dirección o provoque la pérdida de regularidad.

## 7. Radios y frecuencias sin inventar sincronía [H/F]

Si se desea medir un giro material meridiano, conviene definirlo con un centro móvil `R_c(t),Z_c(t)` y una trayectoria material `(r_p(t),z_p(t))`:

\[
 \vartheta_p=\operatorname{atan2}(z_p-Z_c,r_p-R_c),\quad
 \dot\vartheta_p=\frac{(r_p-R_c)(u^z_p-\dot Z_c)-(z_p-Z_c)(u^r_p-\dot R_c)}{(r_p-R_c)^2+(z_p-Z_c)^2}.\tag{73.13}
\]

Esta frecuencia depende del punto, el referente móvil y la evolución. No se reduce automáticamente al cociente de dos radios ni es una constante del anillo. En un toroide sin swirl, la frecuencia azimutal material sobre el eje `z` es cero. En un toroide con swirl puede ser no nula y entonces la nueva fuente de (73.12) importa.

Una aproximación local ilustrativa de un núcleo vorticial de sección casi circular indica una frecuencia característica proporcional a `Γ/a²`; no se usa como identidad exacta del campo curvo de O73. Precisamente, mantener `Γ₀` e `I₀` idénticos **no fija esa escala de frecuencia interna**, porque `a` permanece libre.

## 8. Ensayo reproducible [E]

`codigo/verificar_o73.py` construye la familia (73.4) para `ρ=1`, `Γ₀=6`, `R_*=1` y grosores `a = 0.35, 0.22, 0.14, 0.09, 0.06, 0.035, 0.02`. El perfil `φ` es `C∞` de soporte compacto; la constante de segundo momento calculada es `κ≈0.13065560171027932`.

Todos tienen exactamente, por identidades analíticas, `I_z=6π≈18.8495559215`, `Γ₀=6` y `R_ef=1`. Los picos calculados de `ωθ` crecen desde aproximadamente `38.624` hasta `11 828.607`, sin cambio de esas tres referencias iniciales.

Los controles incluyen: identidad simbólica del operador de cinco dimensiones; cancelación del estiramiento; normalización de la función suave; cuadratura angular/radial independiente; igualdad de impulso y radio; y ley `1/a²` del pico. Se generan `datos/resultados_o73.json`, `datos/controles_o73.json` y tres gráficos.

**No** se integró en tiempo el sistema NS 3D: las curvas son perfiles iniciales exactos y verificaciones del teorema, no evidencia de concentración en una evolución singular.

## 9. Registro de afirmaciones

| Código | Afirmación | Estado |
|---|---|---|
| O73-D1 | Fórmula exacta del impulso axisimétrico (73.2) y conservación en `R³` libre sin forzamiento | Clásica, derivada bajo hipótesis |
| O73-T1 | Familia de datos suaves con iguales `Γ₀`, `I₀`, `R_ef` y grosor arbitrariamente pequeño | Demostrado constructivamente |
| O73-F1 | Impulso/circulación/radio no imponen por sí solos una cota uniforme del núcleo | Demostrado dentro de la clase construida |
| O73-D2 | Identidad PDE `η=ωθ/r` y principio del máximo sin giro azimutal | Clásica, deducida |
| O73-T2 | Cota local de área (73.11) bajo `r≤Rmax` y circulación prescrita | Demostrado condicionalmente |
| O73-F2 | Giro azimutal agrega fuente que impide cerrar por el mismo principio del máximo | Derivado; no demuestra singularidad |
| O73-H1 | Identificar la semilla ontológica con una norma de `η` | Hipótesis **no establecida** |
| O73-A1 | Regularidad global general 3D de Navier–Stokes | **No demostrada** |

## 10. Reflexión y obligación O74

La dirección física de un anillo puede estar codificada colectivamente en el impulso aun cuando las partículas y las frecuencias locales cambien. Pero una referencia global conservada puede coexistir con un núcleo arbitrariamente delgado. Por ello **conservar la referencia no equivale a conservar una escala de regularidad**.

Hay una vía que sí emerge de la ecuación: normalizar `ωθ` por el radio `r` cancela exactamente el término de estiramiento en un régimen específico. Para extender el análisis, O74 debería estudiar la **fuente de giro azimutal** de (73.12), y preguntar qué combinación de proporciones, orientación y estructura de fase puede controlarla, **sin postular que está acotada**. El verdadero obstáculo es demostrar un control de esa fuente para clases amplias o exhibir por qué nuestra candidata a normalizador no puede hacerlo.

## Fuentes de contraste (comparación, no origen ontológico)

1. Gallay, T. y Šverák, V. (2015), *Remarks on the Cauchy problem for the axisymmetric Navier–Stokes equations*, Confluentes Mathematici, DOI 10.5802/cml.25 — https://cml.centre-mersenne.org/articles/10.5802/cml.25/
2. *Formation of an orifice-generated vortex ring*, J. Fluid Mech., sección 4.2, fórmula de impulso axisimétrico — https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/formation-of-an-orificegenerated-vortex-ring/B9F8E5CB0B396AEB19D79D3EA509E02B
3. Chen, H., Fang, D. y Zhang, T. (2017), *Regularity of 3D axisymmetric Navier–Stokes equations*, DCDS 37, 1923–1939 — https://www.aimsciences.org/article/doi/10.3934/dcds.2017081

**Nota de autoría:** la narrativa ontológica y la propuesta de lectura relacional pertenecen al hilo del programa. Las identidades clásicas, teoremas conocidos y comparaciones bibliográficas se reconocen como externos; la familia explícita aquí documentada es la aplicación adversarial reproducible de O73 y no una reivindicación de nueva solución a un problema abierto.
