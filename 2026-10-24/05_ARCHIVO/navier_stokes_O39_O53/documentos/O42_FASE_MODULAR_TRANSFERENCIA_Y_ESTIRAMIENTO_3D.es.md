# O42 — Tubo vorticial tridimensional: la fase heredada, la transferencia y el estiramiento

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**20 de octubre de 2026** · Suplemento autónomo · **CANDIDATO AUDITABLE** · No modifica núcleo, Imagen Total v3.6.0 ni O39–O41.

**Contrato epistemológico.** [O] interpretación ontológica; [D] definición; [T] identidad/teorema para clase declarada; [E] evaluación reproducible; [NO-GO] afirmación refutada en la clase; [A] puente aún abierto. Los hechos estándar de análisis de Fourier y Navier–Stokes no se presentan como nuevos teoremas generales.

## 0. Discurso originario [O]

La unidad no se reconoce desde fuera ni decide continuar. Su referencia propia se sostiene mediante una **relación entre diferencias**, no por conservar una forma inmutable. Los dos espejos no necesitan moverse igual ni ser copias a distinta escala. Al relacionarse tienen una familia común y un normalizador; el resto o «semilla del uno» expresa continuidad de una comparación, pero no es una magnitud física misteriosa ni una partícula conservada. Una nueva escala puede incorporar relaciones no representadas en el módulo anterior. El mero mínimo común múltiplo asegura representabilidad, no predicción ni estabilidad.

En O40 se formalizó el normalizador heredado; O41 demostró que un comparador que recuerda únicamente las amplitudes puede fallar porque perdió la **fase de la relación**. En O39 la evolución tridimensional se separó en estiramiento, difusión de magnitud y difusión de orientación. Ahora se pregunta: **¿puede localizarse, sobre una estructura vorticial tridimensional concreta, la fase que el normalizador no distingue, y medirse su efecto tanto sobre el transporte entre escalas como sobre el estiramiento físico?**

El anillo de aire en agua, el resorte cerrado y el toroide de humo son imágenes heurísticas. El experimento aquí es deliberadamente **un tubo vorticial axial, cuasirecto y periódico**, no un anillo toroidal curvado, ni un flujo de dos fases con tensión superficial. No se atribuye sincronización temporal a la conmensurabilidad de números de onda espaciales.

## 1. Datos y ecuación exactos [D]

Dominio \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), variables \((x,y,z)\), viscosidad \(\nu>0\). Navier–Stokes incompresible sin forzamiento:

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,\qquad \nabla\cdot u=0,
\]
\[
\omega=\nabla\times u,\qquad \partial_t\omega=\nu\Delta\omega-u\cdot\nabla\omega+(\omega\cdot\nabla)u.
\]

Fijamos un perfil localizado en sección transversal
\[
 g(x,y)=\exp[-3(2-\cos x-\cos y)],
\]
\[
 a(x,y)=g(x,y)[\sin x+0.37\sin y+0.33\cos(x+y)],
\]
\[
 b(x,y)=g(x,y)[\sin y+0.43\cos(x-2y)+0.23\sin(2x+y)].
\]

Las posiciones espaciales relativas de \(a,b\) están fijadas antes de evaluar la respuesta. Los estados iniciales dependen de una fase \(\theta\):
\[
\boxed{\psi_\theta=g+A a\cos z+B b\cos(2z+\theta),\qquad
u_\theta=(\partial_y\psi_\theta,-\partial_x\psi_\theta,0).}\tag{O42.1}
\]
\[
A=0.22,\quad B=0.17,\quad \nu=0.03.
\]

La velocidad inicial es \(u_\theta\), distinta de la viscosidad \(\nu\). Este dato es suave, periódico, solenoidal y de energía finita. La solución genuina 3D de Navier–Stokes correspondiente existe lisa en algún intervalo \([0,T_\theta)\) por teoría local clásica. **No** se afirma que la forma (O42.1) se conserve a tiempos positivos: la presión puede generar \(u_z\) y la no linealidad genera nuevos armónicos.

La vorticidad inicial exacta es
\[
\boxed{\omega_\theta=(\partial_{xz}\psi_\theta,\partial_{yz}\psi_\theta,-\Delta_{xy}\psi_\theta).}\tag{O42.2}
\]

El núcleo con concentración positiva de \(\omega_z\) cerca de \((x,y)=(0,0)\) se extiende a lo largo de \(z\), con perturbaciones que inclinan los vectores de vorticidad. Debido a la periodicidad, la vorticidad axial total de una sección debe tener integral cero y el núcleo positivo está acompañado por una distribución débil de signo opuesto fuera del centro. No es un filamento de vorticidad positiva aislado en \(\mathbb R^3\).

## 2. El normalizador y el residuo de fase [D/T]

Las variaciones axiales son armónicas espaciales \(1\) y \(2\), así que la aritmética es compartida para **todos** los \(\theta\). El normalizador de la frecuencia espacial puede declararse por \(\mathrm{mcm}(1,2)=2\), pero ese número no determina \(\theta\).

El campo axial de \(\omega_z\) tiene coeficientes \(\widehat w_n(x,y)=(2\pi)^{-1}\int_0^{2\pi}\omega_z(x,y,z)e^{-inz}dz\). Llamamos \(w_a=-\Delta_{xy}a\), \(w_b=-\Delta_{xy}b\). Entonces
\[
\widehat w_1=\frac{A}{2}w_a,\qquad \widehat w_2=\frac{B}{2}e^{i\theta}w_b.
\]

Para medir la fase relativa sin depender de dónde esté el origen axial, sean \(\alpha\) y \(\beta\) los coeficientes complejos obtenidos al proyectar \(\widehat\psi_1\) sobre \(a\) y \(\widehat\psi_2\) sobre \(b\), normalizados para que \(\alpha=A\), \(\beta=Be^{i\theta}\) en el origen elegido. La firma:
\[
\boxed{Z_{2:1}=\frac{\beta\,\overline\alpha^{\,2}}{|\beta|\,|\alpha|^2}=e^{i\theta}.}\tag{O42.3}
\]

Un cambio de origen \(z\mapsto z+\delta\) multiplica \(\alpha\) por \(e^{i\delta}\) y \(\beta\) por \(e^{2i\delta}\), dejando \(Z_{2:1}\) intacto. **Esta invariancia es axial, con perfiles transversales \(a,b\) declarados; no se está afirmando invariancia bajo todas las deformaciones ni reconstrucción canónica para un toroide arbitrario.**

Los estados \(\theta=0\) y \(\theta=\pi\) poseen exactamente los mismos módulos \(|\widehat \omega(k)|\) para cada modo de Fourier inicial, la misma \(\omega\) proyectada sobre \(k_z=0,\pm1\), la misma enstrofía y la misma disipación viscosa global instantánea. Difieren solo por la fase del armónico axial \(k_z=2\). Su firma \(Z_{2:1}\) es respectivamente \(+1\) y \(-1\).

## 3. Teorema O42-T1: transferencia analítica que depende de la fase [T]

Sea \(J(f,h)=f_xh_y-f_yh_x\). Como \(u_z=0\) inicialmente, la componente axial de la vorticidad obedece en ese instante
\[
\partial_t\omega_z=\nu\Delta\omega_z+J(\psi,\omega_z).
\]

Se define el observable de potencia del armónico axial \(1\):
\[
\boxed{S_1(t)=\left\langle\left|\widehat{\omega_z}_{\,1}(x,y,t)\right|^2\right\rangle_{xy},}\tag{O42.4}
\]
\(\langle\cdot\rangle_{xy}\) indica promedio espacial sobre el toro \(xy\).

Su derivada exacta se descompone como \(S_1'=S'_{1,\nu}+\mathcal T_1\) en \(t=0\), donde el término no viscoso es el aporte de \(J\). Expandiendo \(\cos z\cos(2z+\theta)=\tfrac12[\cos(z+\theta)+\cos(3z+\theta)]\), se obtiene
\[
\boxed{\mathcal T_1(\theta)=\mathcal T_1^{(0)}
+\frac{A^2B}{4}\,\mathfrak K\cos\theta,}\tag{O42.5}
\]
\[
\boxed{\mathfrak K=\left\langle w_a\left[J(a,w_b)+J(b,w_a)\right]\right\rangle_{xy}
=\langle w_aJ(a,w_b)\rangle_{xy}.}\tag{O42.6}
\]

La segunda igualdad proviene de \(\langle w_aJ(b,w_a)\rangle=0\) por divergencia libre sobre el toro. \(\mathcal T_1^{(0)}\) es la contribución al modo \(1\) independiente de \(B,\theta\); para los perfiles fijados aquí resulta cero por las simetrías de este caso, como se comprueba directamente. En cualquier caso se cancela al comparar \(\theta=0\) con \(\theta=\pi\). Luego:
\[
\boxed{\mathcal T_1(0)-\mathcal T_1(\pi)=\frac{A^2B}{2}\,\mathfrak K.}\tag{O42.7}
\]

Ésta es una igualdad exacta derivada de la ecuación tridimensional al instante inicial. La no nulidad del valor particular de \(\mathfrak K\) se evaluó mediante derivadas espectrales y control por aumento de resolución; no se aporta aquí una demostración intervalar certificada de su signo para estos coeficientes decimales.

### Verificación numérica reproducible [E]

Con \(A=0.22\), \(B=0.17\), \(\nu=0.03\), resolución \(64^3\):

| Cantidad por unidad de volumen | \(\theta=0\) | \(\theta=\pi\) |
|---|---:|---:|
| Enstrofía inicial \(E=\langle|\omega|^2\rangle/2\) | 0.231345603644 | 0.231345603644 |
| Disipación \(D=\nu\langle|\nabla\omega|^2\rangle\) | 0.131109111853 | 0.131109111853 |
| Potencia axial inicial \(S_1\) | 0.003998675895 | 0.003998675895 |
| Transferencia no viscosa \(\mathcal T_1\) | +0.000068571721 | −0.000068571721 |
| Derivada de potencia \(S_1'\) | −0.003194579685 | −0.003331723128 |
| Producción global por estiramiento \(P\) | 0.000144853784 | 0.000176418482 |
| Derivada global de enstrofía \(E'\) | −0.130964258069 | −0.130932693371 |

Se obtuvo \(\mathfrak K\simeq0.0333357906002\) y \(\mathcal T_1(0)-\mathcal T_1(\pi)\simeq1.3714344253\times10^{-4}\). Las grillas \(24,32,40,48,64\) convergen en estos observables; los errores del balance \(E'-(P-D)\) descienden a \(\lesssim10^{-14}\) para \(N\ge32\). **Ésta es cuadratura espectral y evaluación exacta de derivadas iniciales del PDE, no simulación temporal de Navier–Stokes.**

Para los valores concretos usados, \(\mathcal T_1(\theta)\) es proporcional a \(\cos\theta\); al poner \(\theta=\pi/2\), la transferencia particular se anula. El signo positivo o negativo del **traspaso no viscoso** no es el signo de \(S_1'\): debido a la viscosidad, \(S_1'<0\) para ambos estados de la tabla.

## 4. Teorema O42-T2: efecto sobre el estiramiento tridimensional [T/E]

Aunque \(u_z(0)=0\), el campo presenta variación axial, la vorticidad tiene componentes horizontales y
\[
(\omega\cdot\nabla)u\not\equiv0.
\]

Para cualquier solución suave en \(\mathbb T^3\), el balance global estándar, por unidad de volumen, es
\[
\boxed{E'=P-D,\quad
P=\langle \omega\cdot(\omega\cdot\nabla)u\rangle,
\quad D=\nu\langle|\nabla\omega|^2\rangle.}\tag{O42.8}
\]

La comparación de las dos configuraciones arroja \(E(0;0)=E(0;\pi)\), \(D(0;0)=D(0;\pi)\), **pero**
\[
\boxed{P(0;0)-P(0;\pi)\simeq-3.1564698383\times10^{-5}\ne0.}\tag{O42.9}
\]

Como comprobación independiente, \(E'(0;0)-E'(0;\pi)\) coincide con esta diferencia a la precisión de cuadratura. El estiramiento no nulo también es visible punto a punto en \(\| (\omega\cdot\nabla)u\|_{L^\infty}>0\).

**Alcance:** el cambio de fase afecta una cantidad física global del PDE y no solamente la apariencia gráfica del tubo. Sin embargo, ambas configuraciones tienen \(P\ll D\) para los parámetros escogidos: ambas pierden enstrofía inicialmente. **El ejemplo no demuestra que \(\theta=0\) sea más estable que \(\theta=\pi\)**, ni que el cambio de fase provoque una transición de topología.

## 5. Comparador y herencia [D/T/NO-GO]

Defina un comparador incompleto \(C_{\mathrm{amplitud}}(u)\) que registra el campo de vorticidad proyectado a \(|k_z|\le1\), las potencias de todos los modos iniciales y el normalizador aritmético axial \(\mathrm{mcm}(1,2)\). Para \(\theta=0,\pi\):
\[
C_{\mathrm{amplitud}}(u_0)=C_{\mathrm{amplitud}}(u_\pi),
\]
pero \(\partial_tS_1(0;0)\ne\partial_tS_1(0;\pi)\). Por el criterio de cociente de O41, esta interfaz **no** admite una evolución cerrada exacta para la respuesta \(S_1\) en toda la familia.

Al ampliarla con \(Z_{2:1}\), se recupera la fase y se determina la **contribución de interacción de esos dos armónicos a la derivada instantánea** de \(S_1\), siempre que los perfiles \(g,a,b\) y amplitudes permanezcan en el contrato conocido. Esto es una interfaz **suficiente para esa pregunta instantánea dentro de la familia declarada**, no para las soluciones generales ni para todo tiempo. Una evolución NS plena genera más modos y más preguntas; las fases de nuevos triángulos o tríadas pueden ser necesarias.

La «semilla del uno» tiene aquí una realización **operacional limitada**: la descripción previa (modo 1) continúa existiendo, pero su próxima respuesta depende de una fase antes omitida. El salto a una representación mejor consiste en **acreditar la diferencia que la pregunta futura requiere**, no en atribuir a \(\mathrm{mcm}\) el poder de regularizar el fluido.

## 6. Puente con O39 y lo que **no** se ha probado [A]

O39 permite separar globalmente \(D= D_{\mathrm{amp}}+D_{\mathrm{ang}}\) siempre que se manejen correctamente los ceros de \(\omega\). Se comprobó esta descomposición como identidad algebraica; la estimación individual de \(D_{\mathrm{ang}}\) cerca de ceros de vorticidad presenta convergencia numérica más lenta y **no** se usa para sustentar el teorema de fase.

Para obtener regularidad de Navier–Stokes 3D se necesitaría una desigualdad **dinámica, independiente y uniforme** que controle el estiramiento \(P\) con mecanismos del PDE (difusión, orientación y transporte), por ejemplo en un criterio apropiado de continuación. La aritmética del normalizador, la existencia del tubo y el cálculo instantáneo no proporcionan tal desigualdad. Los teoremas de O42 constituyen una prueba de insuficiencia de descriptores y una medición controlada de la relación faltante.

## 7. Falsadores y próxima experiencia [A]

1. **Sin segundo armónico:** \(B=0\) elimina la contribución cruzada medida y deja la misma respuesta bajo cambio del «signo» no existente.
2. **Desfase relativo de 90°:** \(\theta=\pi/2\) cancela el término particular \(\propto\cos\theta\); es incompatible con una afirmación de transferencia siempre positiva.
3. **Cambio del origen axial:** \(z\mapsto z+\delta\) conserva \(Z_{2:1}\) y los observables globales.
4. **Cambio de viscosidad:** a dato inicial fijo el término viscoso escala con \(\nu\); la transferencia no viscosa instantánea no depende de \(\nu\). No prueba estabilidad a largo plazo.
5. **Cierre geométrico no es estabilidad:** exigir simulación temporal 3D con control de convergencia y seguimiento de radio, circulación, curvatura y nuevos modos; sin eso no hay umbral de reorganización demostrado.
6. **Próximo nivel físico:** reemplazar el tubo periódico recto por un anillo toroidal curvado, comparar fases poloidales/toroidales, rastrear radios móviles y contrastar con flujos perturbados no axisimétricos. La tensión superficial pertenece a un modelo multifásico diferente.

**Resultado consolidado:** igualdad aritmética de normalizador y de amplitudes **no** implica igualdad dinámica; una fase relativa invariante bajo traslaciones axiales explica exactamente una transferencia cruzada en datos vorticiales genuinamente 3D y modifica el término global de estiramiento. Falta toda prueba de estabilidad, reclutamiento de nuevas escalas con cierre propio y regularidad global.
