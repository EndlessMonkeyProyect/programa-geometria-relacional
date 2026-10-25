---
title: "O48 — Normalizador funcional, reloj de escala y límite de la suficiencia dinámica en Navier–Stokes"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-20"
status: "Teoremas y contraejemplos exactos para clases declaradas; verificaciones racionales y Fourier; NS 3D global abierto"
parents: ["MF-43", "MF-86", "MF-97", "O25", "O39", "O40", "O41", "O42", "O45", "O46", "O47"]
---

# O48 — Una interfaz que se actualiza sin agregar momentos uno por uno

## 0. Síntesis y procedencia

**[O, interpretación ontológica]** La singularidad relacional es una totalidad que se sostiene mediante una referencia que normaliza sus diferencias sin exigir que todas estén resueltas. El desplazamiento del espejo abre un espacio de comparación entre ritmos de referencia espacial, flujo y partícula. La continuidad de una representación no equivale a conservar siempre una figura, ni a declarar conservado físicamente un mínimo común múltiplo.

**[T1, exacto en una subclase de NS]** La evolución de toda la distribución espectral de enstrofía de una cizalla viscosa queda cerrada mediante **una función generadora** y una ecuación lineal de transporte en la variable de escala. Su normalización es también una ecuación cerrada y preserva exactamente el valor 1. En una familia de soporte espectral conocido y finito, basta un número finito *dependiente del soporte* de momentos, y no una lista creciente sin límite para ese soporte.

**[T2, contraejemplo exacto en la misma subclase]** Para cualquier orden finito R, existen dos soluciones exactas suaves de NS (cizallas) con los mismos números de onda, las mismas fases, la misma energía cinética y los mismos momentos espectrales m_0,…,m_R, pero con distintos futuros. Por tanto, **ningún catálogo de momentos de orden máximo R fijado de antemano sirve para todos los soportes espectrales arbitrariamente amplios**, ni siquiera cuando se incluye la energía cinética y el normalizador aritmético.

**[T3, contraejemplo 3D con no linealidad]** Hay dos datos iniciales suaves, solenoidales y genuinamente tridimensionales con el **mismo espectro de enstrofía completo** (misma función generadora inicial en todas las escalas), pero la fase de una tríada da funciones de transferencia opuestas. El espectro, por muy completo que sea, **no** constituye por sí solo una interfaz predictiva autónoma para NS 3D general.

**[A, abierto]** Construir una interfaz dinámica reducida y económicamente representable para las preguntas físicas seleccionadas, incluyendo transferencias y fases necesarias, y derivar una cota a priori de regularidad 3D. Nada en O48 resuelve el problema Clay ni identifica el reloj de escala con tiempo propio relativista o con la singularidad ontológica física.

## 1. Relación con pruebas anteriores

- **MF-86/MF-97:** normalizador idempotente/composicional y equivalencia por continuaciones. La suficiencia es relativa a las preguntas futuras.
- **O25:** espejo endógeno `ell_omega² = ||omega||²/||grad omega||²`; cambio de referencia exacto; la escala no es en sí un nuevo campo físico.
- **O39:** `E'=P−nu J` para `E=½<|omega|²>`, `J=<|grad omega|²>` y producción `P=<omega·(omega·grad)u>`.
- **O41:** criterio exacto de cociente dinámico y falsador de la fase olvidada, también con estiramiento 3D.
- **O42:** dependencia de transferencia instantánea de una fase de dos armónicos en tubo axial 3D.
- **O45:** separación de ritmos, gauge, reloj por recurrencia y marco móvil.
- **O46:** en una familia específica, `(E,ell)` determina `E'` cuando `P=0` inicialmente.
- **O47:** se igualaron además enstrofía, palinstrofía, fase y energía cinética; aun así, `J'` y el reloj del espejo diferían. O48 formaliza la obstrucción de momentos para orden arbitrario y distingue el límite aún más fuerte de un espectro radial completo bajo no linealidad tridimensional.

No se reclaman estas pruebas como nuevas. O48 agrega los resultados T1–T3 y sus controles autónomos.

## 2. La cizalla exacta: definir la referencia sin introducir leyes nuevas [D/T]

En el toro `T³ = (R/2πZ)³`, tomemos `nu>0`, frecuencias enteras positivas distintas `k_j`, fases `phi_j` y pesos `w_j>0`:

\[
 u(x,y,z,t)=(U(y,t),0,0),\quad
 U(y,t)=\sum_{j=1}^{K}\frac{2\sqrt{w_j}}{k_j}
      e^{-\nu k_j^2t}\sin(k_jy+\phi_j).
\tag{O48.1}
\]

Es divergencia cero y `(u·grad)u=0` porque `U` no depende de `x`. Por tanto `partial_t U=nu partial_yy U` y (O48.1) es una **solución exacta y globalmente suave** de NS 3D periódico: no es un truncamiento aproximado. Su estiramiento vorticial es cero; se utiliza justamente como control de un fenómeno de normalización libre de no linealidad.

Escribimos `lambda_j=k_j²`. Por ortogonalidad trigonométrica, la enstrofía por volumen y la palinstrofía son:

\[
E(t)=\frac12\langle |\omega|^2\rangle
=\sum_j w_j e^{-2\nu\lambda_jt}=m_0(t),
\qquad
J(t)=\langle|\nabla\omega|^2\rangle=2m_1(t),
\tag{O48.2}
\]

con momentos de escala

\[
m_r(t)=\sum_j w_j\lambda_j^r e^{-2\nu\lambda_jt}
\quad (r\ge -1).
\tag{O48.3}
\]

La energía cinética por volumen es `m_{−1}(t)` y la escala endógena de O25 satisface

\[
\boxed{\ell_\omega^2=\frac{2E}{J}=\frac{m_0}{m_1}.}\tag{O48.4}
\]

Por diferenciación exacta:

\[
\boxed{\dot m_r=-2\nu m_{r+1}.}\tag{O48.5}
\]

Esto exhibe el problema de pretender cerrar un sistema con una lista prefijada de momentos: cada derivada introduce el siguiente.

## 3. Teorema O48-T1: normalizador funcional cerrado [T]

En lugar de agregar momentos, definimos **una sola función** —la transformada de Laplace de la distribución de enstrofía sobre las escalas espectrales—:

\[
\mathcal M(\zeta,t)=\sum_j w_j e^{-\lambda_j(\zeta+2\nu t)},\quad \zeta\ge0.
\tag{O48.6}
\]

Su evolución es exacta:

\[
\boxed{\partial_t\mathcal M=2\nu\,\partial_\zeta\mathcal M,\qquad
\mathcal M(\zeta,t)=\mathcal M(\zeta+2\nu t,0).}\tag{O48.7}
\]

**Demostración:** cada exponencial satisface la identidad; se suman finitísimos términos o se justifica convergencia para un soporte suficientemente regular. `\mathcal M(0,t)=E(t)>0`.

La *referencia normalizadora* es ahora `E(t)` para esta consulta espectral. La **interfaz normalizada** es

\[
\boxed{\mathcal G(\zeta,t)=\frac{\mathcal M(\zeta,t)}{\mathcal M(0,t)},\quad \mathcal G(0,t)=1.}\tag{O48.8}
\]

Se obtiene una dinámica **autónoma en la función completa**:

\[
\boxed{\partial_t\mathcal G
=2\nu\bigl[\partial_\zeta\mathcal G
 -\mathcal G\,\partial_\zeta\mathcal G(0,t)\bigr],\quad
\mathcal G(\zeta,t)=\frac{\mathcal G(\zeta+2\nu t,0)}{\mathcal G(2\nu t,0)}.}\tag{O48.9}
\]

Prueba: derivar el cociente y usar O48.7; `\mathcal G(0,t)=1` resulta idénticamente. `\mathcal G` determina las *proporciones* de la distribución de enstrofía, no su magnitud total. Para reconstruir `E(t)` hay que conservar además `E(0)`:

\[
\boxed{E(t)=E(0)\,\mathcal G(2\nu t,0).}\tag{O48.10}
\]

Entonces `J(t)=−2E(t)\partial_\zeta\mathcal G(0,t)` y `\ell_\omega²=−1/\partial_\zeta\mathcal G(0,t)`. **La pareja `(E(0),\mathcal G(·,0))` es suficiente para todas las consultas futuras de magnitud de enstrofía, distribución por escala y espejo en la clase de cizallas.**

**No se gana automáticamente economía computacional:** `\mathcal G(·)` es una función entera de información potencialmente extensa; no es un único escalar. Si el soporte está restringido a K números de onda conocidos, existen representaciones compactas exactas que dependen de K.

### El ritmo del espejo queda determinado por la dispersión de escalas [T]

Sea `p_j(t)=w_j e^{-2nu lambda_j t}/m_0(t)`; es una distribución positiva normalizada. Defina `\mu=\sum p_j\lambda_j=m_1/m_0`, y `Var(\lambda)=m_2/m_0−\mu²`. Se deduce:

\[
\boxed{\frac{\dot\ell_\omega}{\ell_\omega}
=\nu\left(\frac{m_2}{m_1}-\frac{m_1}{m_0}\right)
=\nu\frac{\operatorname{Var}_p(\lambda)}{\mu}\ge0.}\tag{O48.11}
\]

**Prueba:** derivada logarítmica de O48.4, O48.5 y Cauchy–Schwarz (`m_0m_2≥m_1²`). La igualdad se da si todas las frecuencias activas tienen la misma `lambda` o si `nu=0`.

Esto formaliza un **ritmo de transformación de la referencia** sin confundirlo con tiempo universal. El espejo espectral se mueve hacia escalas mayores mientras se disipan más rápido las altas frecuencias. Un único modo tiene `dot ell=0` pese a evolucionar y disipar energía. Con reloj de escala `dot s=v_*/ell`, la tasa de ese reloj disminuye en esta clase si `nu>0` y hay dispersión de escalas; `v_*` se selecciona operacionalmente, no se deriva la velocidad de la luz.

## 4. Teorema O48-T2: ningún número fijo de momentos basta para todos los soportes [T/F]

**Afirmación.** Para cada entero `R≥1` existe una pareja de cizallas exactas, con `K=R+3` frecuencias positivas distintas `k_j`, las mismas fases `phi_j`, el mismo soporte de Fourier y, por tanto, el mismo MCM de números de onda, que comparte

\[
m_{-1}(0),\ m_0(0),\ m_1(0),\dots,\ m_R(0)
\]

pero tiene diferentes `m_{R+1}(0)`, y por tanto distinta evolución futura. La interfaz basada en esa lista no es autónoma sobre la familia.

**Construcción demostrativa.** Sea `lambda_j=k_j²` y `P(X)=prod_{j=1}^K(X−lambda_j)`. Definimos

\[
 d_j=\frac{\lambda_j}{P'(\lambda_j)}
 =\frac{\lambda_j}{\prod_{h\ne j}(\lambda_j−\lambda_h)}.
\tag{O48.12}
\]

La identidad de interpolación de Lagrange implica, para `K=R+3`:

\[
\boxed{\sum_jd_j\lambda_j^r=0\quad(-1\le r\le R),
\qquad\sum_jd_j\lambda_j^{R+1}=1.}\tag{O48.13}
\]

Elija un peso base positivo `b>0` y `epsilon>0` suficientemente pequeño para que

\[
 w_j^+=b+\epsilon d_j>0,\qquad w_j^-=b−\epsilon d_j>0.
\]

Entonces coinciden todos los momentos declarados pero

\[
\boxed{m_{R+1}^+(0)-m_{R+1}^-(0)=2\epsilon>0.}\tag{O48.14}
\]

La derivada inicial de `m_R` difiere por `−4nu epsilon`. Y, puesto que la derivada de orden `R+1` de `E=m_0` contiene `m_{R+1}`, las historias de `E(t)` no pueden coincidir como funciones analíticas para todo tiempo. **Esta es una prueba exacta para cada R, no una extrapolación numérica.**

**Control adicional:** al incluir `m_{−1}` igualamos también la energía cinética desde el principio; al conservar todas las `phi_j` igualamos las fases. No alegamos que *toda* interfaz finita concebible falle: por ejemplo los K coeficientes del campo cierran exactamente la evolución si K es un soporte fijo conocido. Refutamos únicamente el catálogo fijo de potencias `m_{−1}…m_R` para soportes no acotados.

### Realización R=1

Para `k=(1,2,3,4)`, las dos soluciones coinciden en energía cinética, `E(0)=1`, `J(0)=15`, `ell(0)=1/sqrt(7.5)=0.36514837` y fases. Sin embargo:

| Dato | Configuración + | Configuración − |
|:--|--:|--:|
| `m_2(0)` | 91.09259259 | 85.90740741 |
| `(dot ell/ell)(0)` | 0.13937037 | 0.11862963 |
| `ell(0.1)` | 0.37030171 | 0.36953261 |
| `E(0.1)` | 0.95659390 | 0.95650600 |

Tomamos `nu=0.03` y funciones exactas de calor. Los valores futuros son evaluaciones de fórmulas explícitas, sin error de integración temporal de Navier–Stokes.

## 5. Teorema O48-T3: el espectro completo tampoco determina la transferencia 3D [T/F]

El resultado T1 deja abierta una posible lectura demasiado fuerte: que conservar **toda** la distribución de magnitudes espectrales baste siempre. No es así en NS 3D con interacciones.

Tomemos tres números de onda en `T³`:

\[
k_1=(1,0,0),\quad k_2=(0,2,0),\quad k_3=k_1+k_2=(1,2,0).
\]

Sus polarizaciones perpendiculares al respectivo número de onda son

\[
p_1=(0,1,1),\quad p_2=(1,0,1),\quad p_3=(2,-1,1).
\]

Defina dos campos reales mediante coeficientes de Fourier no nulos

\[
\widehat u^{\pm}(k_1)=0.1p_1,\quad
\widehat u^{\pm}(k_2)=0.1p_2,\quad
\widehat u^{\pm}(k_3)=\pm 0.1i\,p_3,
\quad \widehat u^{\pm}(-k)=\overline{\widehat u^{\pm}(k)}.
\tag{O48.15}
\]

Con la convención `u(x)=sum_k \hat u(k)e^{ik·x}`, ambos son datos solenoidales, suaves y de energía finita en el toro. Tienen idénticos soportes y módulos de coeficientes, iguales `E=0.4`, `J=3.68`, `ell=sqrt(.4/1.84)≈0.4662524`, energía cinética `0.1` y la misma **función completa** `M(z,0)` para todo `z≥0`:

\[
\boxed{\mathcal M^{\pm}(\zeta,0)
=0.02e^{-\zeta}+0.08e^{-4\zeta}+0.30e^{-5\zeta}.}\tag{O48.16}
\]

Al calcular el término de interacción de Fourier de la ecuación NS para la vorticidad (suma finita de convoluciones, con proyección solenoidal), la fuente espectral `\mathcal T(z)=sum_k T_k e^{-z|k|²}` para el campo + es

\[
\boxed{\mathcal T_+(\zeta)=0.004e^{-\zeta}
+0.032e^{-4\zeta}-0.060e^{-5\zeta},\quad
\mathcal T_-(\zeta)=-\mathcal T_+(\zeta).}\tag{O48.17}
\]

En particular, la producción total global por estiramiento es

\[
\boxed{P_+(0)=\mathcal T_+(0)=-0.024,
\quad P_-(0)=+0.024.}\tag{O48.18}
\]

**Demostración de insuficiencia:** para `E_k=½|omega_hat(k)|²`, la ecuación exacta de modo es `dot E_k=-2nu|k|² E_k +T_k`. Por tanto

\[
\boxed{\partial_t\mathcal M
=2\nu\partial_\zeta\mathcal M+\mathcal T(\zeta,t).}\tag{O48.19}
\]

En `t=0`, `\mathcal M_+=\mathcal M_-` para *todo* `z`, por lo que las partes viscosas son idénticas, pero las fuentes `\mathcal T_+` y `\mathcal T_-` son distintas. Luego **no puede existir una regla autónoma exacta sobre `\mathcal M(·)` sola** que determine su propia derivada para ambos estados. No basta retener infinitos momentos radiales: el defecto está en relaciones de fase/orientación y transferencia entre modos. Se invoca solución local suave; la prueba usa su derivada inicial, no existencia global.

**Auditoría numérica del cálculo algebraico:** el verificador `verificar_O48_fase_3D.py` evalúa de manera independiente el término no lineal pseudospectral con proyección Helmholtz y filtro 2/3 en `16³`, `24³` y `32³`. En esas resoluciones el producto de los modos presentes no supera la banda resuelta, y recupera O48.17 con errores próximos a precisión de máquina. No se afirma que un Galerkin finito pruebe por sí mismo regularidad global.

### Ecuación exacta para la interfaz normalizada en NS 3D [T]

Donde `E(t)=M(0,t)>0`, sea `G(z,t)=M(z,t)/E(t)` y `T(z,t)` la transferencia espectral de NS. La derivación del cociente aplicada a O48.19 da:

\[
\boxed{\partial_t\mathcal G=2\nu\bigl[\partial_\zeta\mathcal G
-\mathcal G\,\partial_\zeta\mathcal G(0,t)\bigr]
+\frac{\mathcal T(\zeta,t)-\mathcal G(\zeta,t)\mathcal T(0,t)}{E(t)}.}\tag{O48.20}
\]

La igualdad **conserva siempre** `G(0,t)=1`. Pero la fuente adicional NO se calcula en general desde `G` sola. Ese es el lugar preciso donde el contrato de suficiencia necesita un canal de información más rico: tríadas, fases y estructuras de transferencia, o una ley efectiva con memoria demostrablemente equivalente para las preguntas especificadas.

## 6. Partículas, reloj y tres ritmos: qué información exige cada pregunta [T/A]

En la cizalla exacta (O48.1), un trazador material cumple `y_p(t)=y_p(0)`, `z_p(t)=z_p(0)` y

\[
\boxed{x_p(t)-x_p(0)=\sum_j\frac{2\sqrt{w_j}}{k_j}
\sin(k_jy_p(0)+\phi_j)
\frac{1-e^{-\nu k_j²t}}{\nu k_j²}.}\tag{O48.21}
\]

La función `G` y `E` determinan el espejo espectral, pero **no** la trayectoria de la partícula cuando las fases `phi_j` no están registradas. Dos campos con idéntico `G`, `E` y diferente fase producen velocidades/trayectorias diferentes. En la clase finita de K modos, el conjunto `(k_j,w_j,phi_j)` más posición inicial permite calcular exactamente el flujo, el espejo y el trazador. Si sólo interesa el espejo, las fases son redundantes y MF-86 permite omitirlas dentro de ese contrato.

Una partícula de cizalla sin circulación periódica no proporciona por sí una vuelta de fase material. El contador `s=∫v_*/ell dt` es un *reloj operacional de escala*; no puede convertirse por decreto en el ritmo físico propio de la singularidad. La tríada de ritmos de O45 requiere una regla **adicional y físicamente observable** para determinar `phi_s` y para definir la fase material si efectivamente hay retorno.

## 7. Decisión científica, límites y falsadores

**[T, aceptado]** Existe una interfaz funcional autónoma exacta para el sector de cizallas: la distribución espectral vía `G(·)` y su normalizador de magnitud `E`. En un soporte fijo de K frecuencias, K momentos `m_0…m_{K−1}` reconstruyen los pesos por la matriz de Vandermonde y se cierran mediante su polinomio característico. Para predecir partículas hay que guardar además fases y estado del trazador.

**[F, aceptado]** Ninguna jerarquía prefijada de momentos de orden máximo finito R es suficiente para cizallas con espectro de tamaño arbitrario, aunque mantenga energía cinética y fases. No se afirma un teorema de imposibilidad para toda codificación finita imaginable.

**[F, aceptado]** La distribución radial completa `G` no cierra NS 3D no lineal, ni siquiera en la primera derivada, por ausencia de las interacciones de fase: ejemplo O48.15–18. Éste es el control que evita trasladar ilegítimamente el cierre de cizallas al problema tridimensional general.

**[A]** La obligación en NS 3D pasa a ser construir un operador de actualización de `T(z,t)` desde una representación que sea suficiente para preguntas explícitas y ojalá económica. La suficiencia predictiva de MF-97/O41 no equivale a estabilidad ni a una cota de estiramiento. Para regularidad haría falta además controlar cantidades críticas a priori en todas las escalas.

**[O, interpretación protegida]** El normalizador aritmético `mcm(k_j)` etiqueta un soporte conmensurable; el normalizador `E` convierte los pesos espectrales en proporciones; el normalizador semántico `N_Q` identifica clases indistinguibles para preguntas futuras. **No son el mismo objeto.** La totalidad `G(0)=1` es un cierre de *representación* que materializa un aspecto de la ontología, no una singularidad física demostrada.

**Falsadores para el próximo laboratorio:**

1. Construir y medir una fuente `T(z,t)` reconstruible de manera autónoma a partir de un descriptor de triadas propuesto, no de la solución completa reintroducida subrepticiamente.
2. Probar si la evolución del descriptor de tríadas exige nuevos correladores y, de ser así, tratar de cerrar por memoria verificable (no solo por enumeración).
3. Hacer comparación entre dos referencias móviles equivalentes y descartar dependencias espurias del origen, escala o orientación.
4. Estudiar una trayectoria material que realmente complete una vuelta y permita una fase/ritmo referencial definido; O44/O47 no la acreditaron.
5. Si se propone coercividad de la fuente, probarla independientemente desde NS y confrontarla con el estiramiento sin giro de O39.

## 8. Reproducción y alcance

Desde esta carpeta:

```bash
python verificar_O48.py
python verificar_O48_fase_3D.py
```

- `verificar_O48.py` (solo biblioteca estándar): identidades racionales de interpolación para R=1…6, normalización funcional, cierre por Vandermonde K=1…7, variación de `ell`, trayectorias materiales en cizalla.
- `verificar_O48_fase_3D.py` (NumPy): espectro y transferencia de una tríada 3D con fase opuesta a tres resoluciones. Independencia del origen temporal y no afirmación de regularidad global.
- `O48_RESULTADOS.json` y `O48_RESULTADOS_FASE_3D.json`: datos generados por los verificadores.
- `REGRESION_ANTECEDENTES.md`: referencia a pruebas históricas sin reclamar ejecución nueva de O41–O47.
- `MANIFEST_SHA256.json`: hashes de los archivos de este suplemento.

**Cierre para continuidad:** la búsqueda no terminó en «agregar un momento». Encontró un **cierre funcional exacto**, su **normalización dinámica**, un **no-go de catálogos fijos de momentos** y un **no-go de la función radial como interfaz universal 3D**. La pregunta abierta es cuál es la menor trama dinámica que determina las continuaciones relevantes sin perder la economía que persigue el programa.
