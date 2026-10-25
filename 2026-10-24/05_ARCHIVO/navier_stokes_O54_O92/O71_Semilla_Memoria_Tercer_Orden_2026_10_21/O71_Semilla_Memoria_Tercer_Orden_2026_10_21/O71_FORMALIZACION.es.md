# O71 — La semilla que conserva el común y el segundo orden todavía puede perder el tercer orden

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 21 de octubre de 2026.**  
**Tipo:** suplemento aditivo autónomo de O70, O69 y O68.  
**Resultado:** identidad analítica exacta de la jerarquía del cociente por espejos y ensayo Fourier–Galerkin reproducible en 32³, 40³ y 48³. **No resuelve la regularidad global de Navier–Stokes 3D.**

## 0. Orden de exposición: narrativa → ontología → matemática → ensayo físico

**[N]** La caja de espejos muestra los reflejos de una configuración. De ellos aislamos lo común; al «apagar la caja», continúa el flujo físico, no la operación de comparación. En O70 vimos que las diferencias no visibles desde el común modifican su evolución: el residuo de segundo orden \(\tau\) basta para determinar la **primera derivada instantánea** del común. Ahora la pregunta es si ese segundo orden, unido a radios y frecuencias, constituye ya una semilla suficiente.

**[O]** En el programa la unidad persiste si una nueva circunstancia puede ser absorbida por la referencia normalizadora y conserva la unicidad de su cierre propio. Lo que persiste es la **referencia múltiplo** que normalizó las relaciones, no una molécula, una forma fija o necesariamente un valor de energía. La semilla pertenece a la totalidad relacional; puede conservar un común aun cuando el sistema permita relaciones no habitadas por esa proyección. La información ya resuelta no se des-resuelve por introducir otra configuración. Estas afirmaciones son la guía ontológica: no las confundimos con consecuencias de la PDE.

**[Pregunta formal]** ¿Conocer el campo común \(a\), la interacción de segundo orden \(\tau\), dos radios estadísticos y dos frecuencias *colectivas* determina el siguiente cambio del común? O71 muestra que **no**, en la subfamilia construida, y localiza un residuo dinámico más alto que esa lista omite.

## 1. La caja como proyección exacta de D₄

**[D]** Sea \(G=D_4\) el grupo finito de ocho simetrías del plano transversal en una caja periódica compatible. No es la caja óptica infinita del laboratorio original; es un modelo de comparación por reflexiones y rotaciones discretas. Para un campo incompresible \(u\), ponemos

\[
\mathcal G u=\frac1{8}\sum_{g\in G}g\cdot u=:a,\qquad w=(I-\mathcal G)u.
\]

La acción de cada simetría transforma tanto el argumento como el vector velocidad. Se cumple \(\mathcal G^2=\mathcal G\), \(\mathcal G w=0\). El campo \(a\) es el común; \(w\), las relaciones que esa medición no distingue. **La octava parte del promedio no identifica el múltiplo ontológico.**

Para Navier–Stokes incompresible, periódico, sin forzamiento, de viscosidad \(\nu>0\), escribimos \(u_t=F(u)=Lu+B(u,u)\), con \(L=\nu\Delta\) y \(B(u,u)=-\mathbb P\nabla\cdot(u\otimes u)\), siendo \(\mathbb P\) la proyección de Leray. Denotamos el promedio de grupo sobre tensores de rango 2 por \(\mathcal G^{(2)}\).

El tensor de relaciones omitidas es exactamente

\[
\boxed{\tau=\mathcal G^{(2)}(w\otimes w)},
\]

pues \(\mathcal G^{(2)}(a\otimes w)=a\otimes\mathcal Gw=0\). La ecuación del común es

\[
\boxed{a_t=F(a)-\mathbb P\nabla\cdot\tau.}\tag{71.1}
\]

Esta identidad es del tipo Reynolds/simetría, no una nueva ecuación de cierre.

## 2. Dos campos con igual común y exactamente el mismo tensor residual

**[D] Construcción.** Tomamos un campo base \(a\) **invariante bajo D₄** y una diferencia divergencia libre \(v\) con \(\mathcal G v=0\). Definimos dos datos:

\[
\boxed{u_+(0)=a+v,\qquad u_-(0)=a-v.}\tag{71.2}
\]

Entonces, sin aproximación ni ajuste numérico,

\[
\mathcal G u_+=\mathcal G u_-=a,\qquad
\tau_+=\mathcal G^{(2)}(v\otimes v)=\tau_-.
\]

De (71.1) sigue \(a'_+(0)=a'_-(0)\). Por tanto, ni la referencia **ni su primera derivada** permiten distinguir esos dos sistemas. Este hecho es exacto siempre que la evolución esté definida y sea suficientemente regular para aplicar la identidad.

**[D] Radios medidos, no radios fundamentales.** Además podemos definir una geometría estadística del anillo con el peso \(W=|\nabla\times u|^2\), la distancia cilíndrica \(\rho=\sqrt{x^2+y^2}\) y el eje \(z\):

\[
R_W=\frac{\int\rho W}{\int W},\quad Z_W=\frac{\int z W}{\int W},\quad
r_W^2=\frac{\int((\rho-R_W)^2+(z-Z_W)^2) W}{\int W}.
\]

Para la familia (71.2), las integrales \(\int h(\rho,z)W_\pm\) coinciden con todo peso \(h\) invariante bajo \(D_4\): los términos cruzados entre la vorticidad base y la de \(\pm v\) tienen promedio de grupo nulo. Así \(R_W,Z_W,r_W,r_W/R_W\) coinciden entre los dos campos. \(r_W\) **no** es exactamente el parámetro de núcleo \(a=0.35\) utilizado para generar los datos iniciales: es una medida RMS explícita.

**[D] Frecuencias colectivas:** para dos componentes Fourier no nulas del **campo común**, elegimos \(z_j(t)=\widehat{a_z}(k_j,t)\), con \(k_1=(1,1,1)\), \(k_2=(1,1,2)\), y medimos \(f_j=(2\pi)^{-1}\operatorname{Im}(\dot z_j/z_j)\). Son tasas de fase espectral, **no equivalen todavía a los giros materiales de O69 ni a los dos ciclos topológicos del toroide**. Como \(a(0)\) y \(a_t(0)\) coinciden, ambos \(f_j\) coinciden exactamente entre los campos (71.2).

**[A] Normalizador:** cualquier etiqueta de múltiplo \(L\) o clase de proporciones \((p,q)\) derivada **solamente de estos observables comunes** también sería la misma en los dos casos. Esto no demuestra que exista un múltiplo entero exacto en las frecuencias medidas; sus razones no son, en general, racionales fijas. No elegimos \(p,q\) retroactivamente para afirmar una sincronía.

## 3. Lo que revela la derivada del tensor

**[D]** Sea \(N(v,v)=B(v,v)\), el término cuadrático no lineal, y definamos la parte no reconocida por los espejos de esa interacción:

\[
\boxed{Q=(I-\mathcal G)N(v,v).}\tag{71.3}
\]

La velocidad de la diferencia en (71.2) tiene una parte impar en \(v\) y otra par:

\[
\dot w_+=H+Q,\qquad \dot w_-=-H+Q,
\]

con \(H=Lv+B(a,v)+B(v,a)\). Como \(\tau=\mathcal G^{(2)}(w\otimes w)\), se obtiene al derivar

\[
\boxed{\dot\tau_+-\dot\tau_-=
2\mathcal G^{(2)}(v\otimes Q+Q\otimes v).}\tag{71.4}
\]

Por (71.1), \(a\) y \(a_t\) son los mismos al inicio en ambos casos, y por tanto

\[
\boxed{\ddot a_+(0)-\ddot a_-(0)=
-2\mathbb P\nabla\cdot\mathcal G^{(2)}(v\otimes Q+Q\otimes v).}\tag{71.5}
\]

**Ésta es la obstrucción O71:** dos semillas con el mismo \((a,\tau)\) pueden tener **distintas derivadas de \(\tau\)** y, por tanto, distintos futuros del común. El residuo (71.5) es **cúbico** en la diferencia \(v\), porque \(Q\) es cuadrático. En esta familia,

\[
\|\ddot a_+(cv)-\ddot a_-(cv)\|=c^3\|\ddot a_+(v)-\ddot a_-(v)\|\quad(c>0).
\]

La igualdad no dice que *toda* solución de Navier–Stokes tenga un efecto cúbico global; es una identidad de comparación para la familia construida alrededor de un \(a\) simétrico. Para un dato genérico, otros términos también intervienen.

**[D/E]** El operador \(F\) del sistema Fourier–Galerkin es la suma de un término lineal y otro cuadrático, así que la fórmula centrada

\[
D F(u)[h]=\frac{F(u+\alpha h)-F(u-\alpha h)}{2\alpha},\quad \alpha\ne0,
\]

es algebraicamente exacta para cualquier \(\alpha\) (salvo redondeo). Permite calcular \(a_{tt}=\mathcal G D F(u)[F(u)]\) directamente, y contrastarlo de manera independiente con (71.4–71.5).

## 4. Laboratorio numérico: tres mallas, dos futuros

**[E] Datos iniciales.** Mismo anillo de O53/O70 (radio nominal \(R=1\), núcleo nominal \(0.35\), \(\Gamma=6\), \(\nu=0.025\)); \(v=u_{14\%}-\mathcal G u_{14\%}\). Simulaciones periódicas Fourier–Galerkin con recorte \(|k_j|<N/3\), RK4, \(\Delta t=0.004\), observación hasta \(t=0.032\). Las dos configuraciones son \(a+v\) y \(a-v\).

| Medición adimensional | 32³ | 40³ | 48³ |
|---|---:|---:|---:|
| Diferencia entre \(a_+(0)\) y \(a_-(0)\) | ~0 | ~0 | ~0 |
| Diferencia entre \(\tau_+(0)\) y \(\tau_-(0)\) | ~0 | ~0 | ~0 |
| Diferencia entre \(a'_+(0)\) y \(a'_-(0)\) | ~0 | ~0 | ~0 |
| \(\|\dot\tau_+-\dot\tau_-\|_\mathrm{RMS}\) | 0.01559920 | 0.01957182 | 0.02036559 |
| \(\|\ddot a_+-\ddot a_-\|_\mathrm{RMS}\) | **0.01940043** | **0.02783819** | **0.03108091** |
| Error de identidad (71.5) | 3.45×10⁻¹⁵ | 6.51×10⁻¹⁵ | 9.96×10⁻¹⁵ |

Para N=40, la geometría vorticidad-ponderada común de los dos campos fue \(R_W=1.05308145\), \(r_W=0.24271420\) y \(r_W/R_W=0.23047999\). Las dos frecuencias colectivas elegidas fueron \(-0.16854040\) y \(-0.34220986\) ciclos por unidad de tiempo, **idénticas en ambos campos**, pero distintas entre sí y no ligadas aquí por una razón entera exacta.

**[E]** En los tres cortes, al multiplicar \(v\) por \(c\in\{0.5,1,2\}\), la diferencia entre aceleraciones colectivas sigue \(c^3\) hasta error de redondeo. La separación futura entre los dos campos colectivos comienza proporcionalmente a \(\frac12\|\Delta a''(0)\|t^2\) para tiempos cortos; se integra la dinámica sin ajustar las fases a posteriori.

**[A — detalle reproducible importante]** El filtro heredado del código O53 acepta \(|k_j|\le N//3\). Cuando \(N=48\), incluye modos \(|k_j|=16\), cuyo producto puede aliasar sobre otro modo aún retenido (\(16+16=32\equiv-16\) módulo 48). Eso rompía la comprobación tensorial a nivel ~3×10⁻⁵, por un error de **dealiasing de borde**, no por física nueva. O71 aplica explícitamente el corte estricto \(|k_j|<N/3\) a todas las mallas; entonces el residuo de (71.5) cae a ~10⁻¹⁴ en N=48. Esto **no corrige retrospectivamente los archivos previos**; declara el refinamiento usado aquí.

**[A — convergencia]** Los valores absolutos entre N=32,40,48 todavía cambian de modo visible. Son pruebas de no cierre en los sistemas espectrales finitos elegidos, **no** una estimación certificada del límite continuo ni una evidencia de formación de singularidad. No se afirma convergencia rigurosa ni control de error de discretización.

## 5. Qué puede «computar» la caja y qué no

**[T]** Conocer \(a\) determina el común. Conocer además \(\tau\) determina su **derivada instantánea** mediante (71.1). Para determinar la **segunda derivada** generalmente se necesita al menos la combinación divergencia-proyectada de \(\dot\tau\) en (71.1). Conocer \(\dot\tau\) en un instante tampoco prueba que haya un cierre autónomo para todo futuro: la evolución de ese dato puede requerir información de órdenes superiores o una descripción no local en el tiempo.

Esto es una **jerarquía de cierre** de la descripción reducida, no una nueva prueba del problema de Clay. En el espacio Galerkin finito completo, el campo original siempre permite evolucionar con una ODE cerrada: la dificultad es si existe una **semilla comprimida relacionalmente suficiente**.

Para la narrativa del programa, la unidad mínima no puede definirse únicamente por el común de sus reflejos, ni siquiera necesariamente por su varianza de segundo orden. La semilla debe contener la regla que transporta la referencia durante los cambios, o bien un término de memoria calculable. La diferencia \(v\mapsto-v\) es información que no registra \(\tau\), pero que importa en su dinámica.

### Límite sobre radios y múltiplos

Las proporciones de radios y las frecuencias examinadas **son sólo observables parciales**. Si el programa propone una referencia más rica que distinga el signo relacional relevante, O71 no la refuta; obliga a definirla, calcularla y comprobar que prediga la transformación de la caja sin incorporar el resultado futuro como dato de entrada. No hay derivación de un múltiplo entero único desde el campo del anillo; tampoco equivalencia probada entre Bézout y una ley hidrodinámica.

## 6. Próximo intento O72

Investigar una **semilla dinámica aumentada**, definida antes de evolucionar, que transporte \(a\), la información específica de \(\tau\) que alimenta al común y un funcional mínimo del término (71.5) o de la memoria de fase. El falsador es fuerte: fabricar dos campos con la misma nueva semilla pero **tercera derivada colectiva distinta**; no añadir parámetros retroactivamente para evitar el resultado. Para Navier–Stokes general, una descripción cerrada de una subfamilia sigue siendo insuficiente para demostrar regularidad global: requeriría además una cota a priori no circular sobre las escalas pequeñas.

## 7. Archivos y reproducción

- `codigo/experimento_o71.py`: genera gemelos y verifica identidad tensorial, radios, frecuencias, leyes cúbicas y trayectorias.
- `codigo/graficar_o71.py`: genera dos gráficas.
- `resultados/resumen.json` y `resultados/evolucion.csv`: resultados completos.
- `codigo/experimento_o70.py`, `codigo/o63_operadores.py`, `fuentes/ejecutar_o62_ORIGINAL.py`: código original reutilizado, **incluido** para evitar dependencias externas.
- `REGISTRO_AFIRMACIONES.csv`: trazabilidad de afirmaciones ontológicas, teoremas, ensayos e hipótesis.

Se requieren Python 3, `numpy`, `scipy`, `matplotlib`. Ejecutar:

```bash
python codigo/experimento_o71.py
python codigo/graficar_o71.py
```

Los **39 de 39 controles** son pruebas de consistencia de una discretización y de identidades derivadas; no 39 validaciones independientes de la regularidad del PDE.
