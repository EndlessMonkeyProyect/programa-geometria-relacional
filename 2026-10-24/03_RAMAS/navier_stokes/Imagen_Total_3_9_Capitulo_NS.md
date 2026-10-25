# 7 Navier Stokes y la continuidad de un flujo

La rama de fluidos pregunta qué relaciones pueden sostener una organización en movimiento y qué información permite controlar su continuación. Ha pasado de la geometría material de la vorticidad a radios endógenos, fases de anillos, firmas por simetría, presupuestos de interacción y normalización de todos los armónicos. Los resultados responden preguntas diferentes y se conservan en su secuencia de correcciones.

## 7.1 El alcance físico

El contrato central reciente es Navier–Stokes viscoso e incompresible sobre el toro periódico tridimensional, sin fuerza externa:

$$\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,\qquad\nabla\cdot u=0,\qquad\nu>0.$$

Se distinguen soluciones suaves exactas, sistemas Fourier–Galerkin truncados, diagnósticos de simulaciones aportadas y criterios condicionales de continuación. Un resultado local o una ventana numérica corta conserva su valor sin transformarse en una afirmación global.

La referencia externa requiere una precisión temporal. El 8 de septiembre de 2026 OpenAI anunció una prueba de formación de singularidad con **fuerza externa suave**, presentada como las alternativas C y D del problema del milenio. Clay publicó el 11 de septiembre una declaración sobre el anuncio y su proceso de evaluación. Estas fuentes fueron comprobadas para esta edición. Ese anuncio no establece por sí mismo una respuesta sobre la evolución universal sin fuerza que estudia esta rama. La bibliografía de contraste identifica ambas fuentes y el enunciado oficial.

## 7.2 De la amplificación al giro

La rama histórica separa la variación material de la magnitud de vorticidad de su cambio de dirección. Para $q=|\omega|>0$ y $\xi=\omega/q$, una descomposición de $D_t\omega/q$ en componente paralela y perpendicular permite estudiar amplificación y giro por separado.

Los archivos conservan balances instantáneos, coordenadas de crecimiento, Hessiano de presión, contribuciones viscosas, controles de Burgers y Euler restringido, además de diagnósticos aportados de DNS y JHTDB. Las cifras de producción dependen del muestreo, la resolución y el método de diferenciación. La 3.9 conserva esos datos y sus auditorías; las nuevas ejecuciones de esta edición se concentran en los laboratorios detallados al final del capítulo.

El resultado conceptual que atraviesa la rama es que poco giro no determina por sí solo explosión, y una geometría favorable no acredita automáticamente la cota dinámica necesaria. El término que estira la vorticidad y la viscosidad deben compararse con sus escalas físicas.

## 7.3 El espejo móvil y los tres ritmos

O25 y O45 ya construyen marcos móviles mediante traslación, orientación y escala. Una forma es $x=X(t)+\ell(t)A(t)y$. La velocidad relativa contiene los términos correspondientes al movimiento del origen, a la variación de escala y a la rotación del marco.

El programa compara el ritmo del flujo, el de su referencia o singularidad espacial y el de una partícula. Tres fases proporcionan dos diferencias independientes. La igualdad de ritmos no se impone por normalización. El tiempo relacional se plantea mediante esas comparaciones; las realizaciones de fluidos emplean una ley temporal declarada y permiten construir relojes endógenos.

Para vorticidad no nula se define

$$\ell_\omega^2=\frac{\int|\omega|^2}{\int|\nabla\omega|^2}.$$

La ecuación determina la tasa de esa escala a través de sus balances. Por ello, el acoplamiento cuantitativo entre radio y dinámica ya está trabajado. La dificultad posterior es controlar esa evolución para todas las configuraciones de la clase buscada.

O37 y O38 conservan ejemplos de reorganización y cambio de estructura en 2D bajo condiciones particulares. O39–O53 incorporan balances materiales, anillos, retornos y perturbaciones. O52 registra cinco de seis trazadores completando vueltas en momentos distintos; O53 muestra cambios de desfase bajo una perturbación tridimensional. Un retorno material, un retorno de fase y el desplazamiento del centro son observables diferentes.

## 7.4 Orientación y superficie material

O54–O57 examinan la propuesta de conservar relaciones entre dos radios y una perpendicularidad común. Si $a,b$ son vectores materiales transportados por el gradiente del flujo y $S$ su parte simétrica,

$$\frac{D}{Dt}(a\cdot b)=2a^TSb.$$

La incompresibilidad no obliga a que ese término sea cero. Dos preparaciones con magnitudes globales iguales pueden deformar de manera diferente un ángulo material. Elegir después ejes ortogonales en una superficie no prueba que sus relaciones materiales originales hayan sido preservadas.

O57 propone comparar la métrica de la superficie hasta un factor común de escala. La parte que ese factor no explica permite cuantificar una diferencia de forma. La identidad de un anillo puede estudiarse aun cuando varíe el ángulo de dos marcas; perder una perpendicularidad particular no obliga a perder toda organización.

O58–O60 separan las estelas aritméticas de estas magnitudes físicas. La identidad $N^2-(N-1)(N+1)=1$ vale para todo $N$; la condición $a^2+b^2+1=N^2$ exige soluciones específicas. Una cuadrícula normalizada no se identifica directamente con un espectro de fluido.

## 7.5 Relaciones disponibles y transferencias activas

O61 distingue triadas admitidas por la ecuación de transferencias efectivamente activas en un estado. O62 encuentra que las preparaciones estudiadas pueden tener transferencia inicial de energía entre bandas nula, mientras su segunda derivada ya distingue la reorganización siguiente. O63 separa esa lectura energética del desfase de trazadores: una marca anclada puede empezar a cambiar su fase aunque el balance inicial de bandas no cambie.

O64 y O65 examinan gotas e interfaces. En el modelo de fragmentación utilizado, la tensión superficial aporta información que no está determinada por la geometría ni por el flujo de referencia. La rama conserva también una solución bifásica particular donde variar esa tensión modifica un salto de presión sin obligar a una ruptura. El modelo de umbral, la solución exacta y una medición experimental tienen estados diferentes.

O68 y O88 formalizan dos giros del toro. Si $p,q$ son coprimos y $bq+cp=1$, el cambio de fases

$$\begin{pmatrix}\Phi\\\Psi\end{pmatrix}=\begin{pmatrix}b&c\\p&-q\end{pmatrix}\begin{pmatrix}\theta\\\varphi\end{pmatrix}$$

es invertible en el toro de fases porque su determinante es $-1$. Si posteriormente se multiplican fases por un entero mayor que uno, se debe conservar una etiqueta de rama para reconstruir la preimagen. Esta es una realización de continuidad de representación.

O69, O89 y O90 delimitan la sincronía. El acoplamiento a un mismo múltiplo entero puede perderse sin que se produzca una ruptura inmediata del fluido. O90 conserva cuatro trayectorias materiales distintas durante la ventana observada, aunque cambie su coherencia relativa. El falsador alcanza la necesidad de un múltiplo rígido específico; deja abierta la búsqueda de una referencia más general.

## 7.6 Lo que una semilla finita debe conservar

O70 y O71 muestran pérdida de suficiencia en proyecciones por simetría. O76 incorpora la presión no local como relación que una descripción solo local puede omitir. O77 demuestra que una familia toroidal concreta de pocos parámetros puede no ser invariante bajo la ecuación. O78 precisa el alcance: eso no refuta una regla generativa que amplíe sus relaciones.

La corrección O91–O92 es esencial. O91 compara estados con el mismo normalizador aritmético y los mismos primeros momentos agregados, pero distintos pesos armónicos. O92 observa que una interfaz que **ya conserva todos esos pesos** distingue los estados y recupera el momento adicional. No corresponde reclamarlo como información nueva respecto de esa interfaz más rica.

El siguiente paso conserva además fases y polarizaciones. Los pesos de los armónicos no bastan para determinar todas sus interacciones. La distinción relevante debe hacerse siempre respecto de la información que efectivamente guarda la firma.

## 7.7 Los presupuestos de continuación

O80 obtiene un control para datos pequeños en una norma crítica de Fourier, con el presupuesto comparado con la viscosidad. El propio documento lo sitúa en la familia de métodos clásicos de normas críticas. O81 permite una referencia coherente grande acompañada de un resto pequeño. O82 construye referencias desde datos y controla su defecto. O83 estudia actualizarlas incorporando interacciones.

O84 corrige la contabilidad: el mismo resto transportado no se cobra de nuevo en cada intervalo. Un factor integrante global permite acumular el defecto de la referencia y los saltos de referencia una sola vez. O85 comprueba que cambiar de escala no elimina gratuitamente los costos críticos. Son resultados efectivos bajo presupuestos explícitos.

En el ejemplo O84 reproducido dentro de O93, con $\nu=1$ y $\delta=9/500$, la primera referencia da un presupuesto $0,519488712836\ldots$, superior al umbral $1/2$. La referencia actualizada obtiene una cota $0,271724746561\ldots$, inferior al umbral. La mejora acredita ese intervalo y ese certificado; no demuestra que toda sucesión de actualizaciones pueda continuar indefinidamente.

## 7.8 La doble normalización de O92 y O93

Para un campo real, suave, solenoidal y de media cero, se separa la magnitud global de sus coeficientes Fourier completos:

$$M^2=\sum_{k\ne0}|\widehat u_k|^2,\qquad z_k=\widehat u_k/M,\qquad\sum_{k\ne0}|z_k|^2=1.$$

Se definen $D=\sum|k|^2|z_k|^2$ y $D_2=\sum|k|^4|z_k|^2$. Si $\mathcal B_k(z,z)$ es el término no lineal de Fourier con proyección de Leray, la dinámica exacta es

$$\dot M=-\nu MD,\qquad\dot z_k=-\nu(|k|^2-D)z_k+M\mathcal B_k(z,z).$$

Con la transferencia normalizada $\mathcal T=\sum|k|^2\operatorname{Re}(\overline{z_k}\cdot\mathcal B_k)$,

$$\dot D=-2\nu(D_2-D^2)+2M\mathcal T.$$

O93 conecta esta descripción con enstrofía $W$, palinstrofía $B$ y estiramiento $P$, usando el mismo promedio espacial:

$$\boxed{W=M^2D,\qquad B=M^2D_2,\qquad P=M^3\mathcal T.}$$

Es una reconstrucción exacta mientras se conservan **todos** los $z_k$. No constituye una compresión del continuo a un número finito de parámetros.

El reloj viscoso y el cociente de compensación son

$$d\tau_\nu=\nu\frac{D_2}{D}\,dt,\qquad\Gamma_\nu=\frac{M\mathcal T}{\nu D_2},\qquad\frac{d\log W}{d\tau_\nu}=2(\Gamma_\nu-1).$$

Para un horizonte finito de existencia suave, la condición

$$\int_0^{T_*}\frac{[M\mathcal T-\nu D_2]_+}{D}\,dt<\infty$$

acota la enstrofía y da continuación suave bajo el contrato periódico declarado. La prueba integra el balance y utiliza el criterio de continuación correspondiente. La obligación universal es obtener esa finitud **a priori**, sin suponerla ni escoger una referencia usando el futuro de la solución.

## 7.9 Dos fases y una diferencia verificable

O86 y O93 construyen dos campos con iguales magnitudes Fourier iniciales, energía, enstrofía y radio espectral, pero diferente fase. Los valores exactos son

$$W(0)=95/9,\qquad B(0)=266/9,\qquad P(0)=\pm3/4.$$

Para $\nu=0,01$,

$$\dot W_+(0)=409/450,\qquad\dot W_-(0)=-941/450.$$

La misma escala inicial admite crecimiento o disminución de enstrofía. El par refuta la suficiencia de magnitudes y radio para predecir esa transferencia.

La reproducción 3.9 obtiene a $T=0,08$, con $N=24$ y $\Delta t=0,002$, $W_+(T)=10,661906020726$ y $W_-(T)=10,423743782501$. Las diferencias frente al paso $0,004$ son inferiores a $6,3\times10^{-12}$ en este ensayo. La comparación con $N=16$ también reproduce la tabla archivada. La cercanía verifica esta simulación corta; no se extrapola a tiempos largos ni prueba el límite continuo.

Fuentes principales: NS-HIST, O25, O39–O93 y el expediente reproducible O93. El catálogo conserva todos los suplementos intermedios.

# 8 Yang Mills y la información de los caminos

La rama gauge examina una realización en la que importa el orden de composición de las relaciones. Su pregunta interna es qué conserva una referencia al transportar y combinar caminos, y qué diferencia aparece cuando consultas individuales iguales no determinan la composición.

## 8.1 La referencia local se cancela en el camino

En una red dirigida, un transporte $T_{ab}\in SU(2)$ cambia de representación local mediante

$$T'_{ab}=g_bT_{ab}g_a^{-1}.$$

Al componer un camino, las referencias intermedias se cancelan. Solo permanecen los cambios de base en sus extremos. En un lazo, la transformación es una conjugación y la traza permanece invariante.

R02 muestra además que subdividir una arista no obliga a introducir novedad. Si $T_1=A$ y $T_2=TA^{-1}$, el producto es $T_2T_1=T$. Insertar un nodo de grado dos conserva los transportes antiguos sin crear un lazo independiente. Una mayor resolución de representación puede mantener exactamente las mismas respuestas.

## 8.2 Dos lazos necesitan una relación conjunta

Para dos lazos $U,V$ con la misma base, R02 prueba que la firma

$$Q(U,V)=(x,y,z)=\left(\tfrac12\operatorname{tr}U,\tfrac12\operatorname{tr}V,\tfrac12\operatorname{tr}(UV)\right)$$

determina el par hasta conjugación simultánea. La demostración utiliza la representación por cuaterniones: $x,y,z$ fijan las normas y el producto escalar de dos vectores reales. Su matriz de Gram determina el par hasta una rotación que puede realizarse mediante $SU(2)$.

La suficiencia es exacta para **dos** lazos bajo ese grupo de equivalencias. Al añadir un tercer lazo o una continuación que dependa de relaciones omitidas, la firma debe reevaluarse.

El defecto de orden se escribe

$$\nu(U,V)=1-\tfrac12\operatorname{tr}(UVU^{-1}V^{-1})=2(1-x^2-y^2-z^2+2xyz).$$

También satisface $\nu=\tfrac14\|UV-VU\|_F^2$. En la representación vectorial es dos veces el determinante de Gram de las componentes correspondientes. Las trazas individuales $x,y$ no bastan; la consulta conjunta $z$ acredita una distinción adicional.

## 8.3 Un bloqueo puede borrar una diferencia

El mapa $B(U,V)=UV$ es gauge-equivariante. Aun así, los pares

$$ (i\sigma_x,i\sigma_y),\qquad (I,-i\sigma_z)$$

producen la misma matriz bloqueada $-i\sigma_z$ y valores $\nu=2$ y $\nu=0$. El transporte exterior común no conserva toda la información de la composición interior.

Este testigo da contenido exacto al principio de continuidad: para preservar una respuesta hay que conservar una firma de la que pueda recuperarse. La invariancia frente a cambios de base y la suficiencia de un bloqueo son propiedades distintas.

Un lazo nuevo independiente puede añadir una traza no reconstruible desde la firma anterior. Esa novedad comparte con el ejemplo modular la no factorización de una consulta. En $SU(2)$ sus valores pueden formar una familia continua; no hay una identificación automática de cada nueva holonomía con un primo numérico.

## 8.4 De la distinción a una brecha física

La positividad de un defecto no abeliano no impone un mínimo positivo uniforme. Para $U_t=e^{it\sigma_x}$ y $V_t=e^{it\sigma_y}$,

$$\nu(U_t,V_t)=2\sin^4t\longrightarrow0.$$

La diferencia sigue existiendo para valores pequeños no nulos de $t$, pero su peso puede disminuir sin cota uniforme. Los laboratorios espectrales preservan el mismo límite lógico: una brecha positiva en cada regulador puede tender a cero al retirar la escala.

Una brecha cuántica requiere una dinámica física y un operador con un sector excitado separado del vacío. El programa conserva las rutas MF–103, MF–104, YM-R3A y YM-R3B, las equivalencias condicionales de contracción y aislamiento y sus falsadores. R02 añade composición, suficiencia y no pérdida entre escalas; no reemplaza las obligaciones de construcción del límite cuántico 4D y control espectral uniforme.

El próximo contrato concreto, denominado R03 en el expediente, propone estudiar dos plaquetas Wilson, un bloqueo de escala y los observables que sobreviven. La comparación con $U(1)$ debe impedir que un criterio puramente formal atribuya una brecha al control abeliano equivocado. La acción y la dinámica deben preceder a la conclusión espectral.

## 8.5 Verificaciones de la edición

La ejecución de YM–02 completó **129.371 aserciones auxiliares** sobre refinamiento, módulos, actualizaciones, conmutadores y espectros de ciclos. R02 reprodujo **1.200 configuraciones aleatorias** y controles simbólicos, con error máximo $1,45\times10^{-15}$ redondeado hacia arriba. Se verificaron la firma triple, cambios gauge, subdivisión y el testigo de pérdida bajo bloqueo.

Esos conteos describen ejecuciones. Las proposiciones generales se sostienen por las demostraciones incluidas en los documentos. El laboratorio es finito y no constituye una construcción de la teoría cuántica continua.

Fuentes principales: YM-RES, YM01, YM02, R01, R02 y rama histórica 06_yang_mills.
