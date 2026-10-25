---
title: "O67 — El presupuesto multiescala ante el límite crítico"
subtitle: "Derivación de una desigualdad, cierre de datos pequeños y obstrucción para datos generales"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "2026-10-21"
status: "Suplemento autónomo aditivo para O66; identidades y teoremas condicionales conocidos; ningún resultado de regularidad global general para NS sin fuerza"
parents: ["O40", "O44N", "O45", "O53", "O58", "O59", "O60", "O61", "O62", "O63", "O66", "Imagen Total v3.8.1"]
---

# O67 — La estela, el normalizador físico y la barrera crítica

**Nota de autoría y método.** Ontología y pregunta de investigación del *Programa de Geometría Relacional* (Le Matt Ansatz Di Ego). La bibliografía es contraste; no es la fuente de los postulados del programa. Los resultados analíticos de energía, Sobolev, Gagliardo–Nirenberg, pequeña data y criterios de continuación son herramientas matemáticas **preexistentes**, no teoremas originales reivindicados aquí. El aporte del suplemento es someter las propuestas ontológicas y O66 a sus consecuencias y falsadores. Etiquetas: `[O]` ontología, `[D]` definición, `[T]` demostrado bajo hipótesis, `[F]` obstrucción o falsador, `[E]` reproducción numérica finita, `[A]` abierto.

## 0. Precisión externa de alcance [CONTRASTE]

El 8 de septiembre de 2026 OpenAI publicó una construcción anunciada de **blow-up en 3D con fuerza externa suave**; Clay el 11 de septiembre acogió el anuncio como aparentemente decisivo y sometido a examen. Es un resultado **con forzamiento** en una alternativa oficial del problema. En O67 estudiamos, de modo consciente, **NS viscoso, incompresible, tridimensional, sin fuerza**. La alegación externa no se transporta automáticamente a este último caso. Referencias: https://openai.com/index/navier-stokes-solution/ ; https://www.claymath.org/news/navier-stokes-announcement/ ; https://www.claymath.org/millennium/Navier-Stokes-Equation/

## I. Narrativa → ontología [O]

Las relaciones de la totalidad pueden existir antes de estar habitadas por un reflejo de una unidad determinada. El cierre propio admite continuidad al cambiar la escala de comparación. Lo ya resuelto es reconstruible en un nuevo normalizador, sin exigir que cada configuración futura repita su forma. La dirección espacial observada es **consecuencia** de las relaciones presentes, no el principio generador.

En O58/O60 existen cadenas exactas de normalizaciones aritméticas y restas de una unidad. Sin embargo, aun una cadena infinita de referencias compatibles no controla cuánto crece una derivada espacial. O66 identificó el presupuesto de entrada hacia colas espectrales como una condición suficiente, pero no encontró la ley que lo acote desde la dinámica. **O67 intenta cerrar exactamente ese salto**.

## II. Contrato físico y notación [D]

En el toro fijo \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), velocidad suave \(u\), divergencia cero, viscosidad \(\nu>0\), fuerza cero:

\[
\partial_tu+\mathbb P(u\cdot\nabla u)=\nu\Delta u,\qquad \nabla\cdot u=0.
\tag{67.1}
\]

Restamos la velocidad media, que se transporta por transformación galileana. Para las desigualdades funcionales usemos normas \(L^p\) ordinarias sobre el dominio físico (sin normalizar por volumen); constantes universales o del dominio se denotan \(C\). Definimos:

\[
U(t)=\|u(t)\|_2^2,\quad Y(t)=\|\nabla u(t)\|_2^2=\|\omega(t)\|_2^2,\quad Z(t)=\|\Delta u(t)\|_2^2.
\tag{67.2}
\]

El presupuesto energético exacto es

\[
\frac12 U'(t)+\nu Y(t)=0,\qquad U(t)\le U(0),\quad \int_0^T Y(t)\,dt\le\frac{U(0)}{2\nu}.
\tag{67.3}
\]

Este último control es **temporal-integral**, no un control uniforme de \(Y(t)\).

## III. Paso exacto desde O66 hacia la no linealidad [T]

Repitamos \(e_k=\frac12|\widehat u_k|^2\), \(\mathcal E_{\ge K}=\sum_{|k|\ge K}e_k\), \(\Pi_K\) la transferencia no lineal de energía hacia la cola y \(D_K\ge0\) la disipación de la cola. Las normalizaciones de Fourier del O66 utilizan promedios espaciales; al usar normas integrales aquí se absorbe el volumen fijo en las constantes.

Defina la producción positiva ponderada que O66 acumulaba:

\[
F_{K_0}(t)=\int_{K_0}^{\infty}2K[\Pi_K(t)-D_K(t)]_+\,dK.
\tag{67.4}
\]

**Lema O67-T1 (cota instantánea).** Para \(K_0\ge0\) y solución suave con rápida caída espectral,

\[
\boxed{F_{K_0}(t)\le\sum_k |k|^2|T_k(t)|
\le \|\Delta u(t)\|_2\,\|\mathbb P(u\cdot\nabla u)(t)\|_2,}
\tag{67.5}
\]

salvo factor fijo de volumen si los dos lados usan convenciones distintas, donde \(T_k=\Re(\widehat u_k^*\cdot\widehat{-\mathbb P(u\cdot\nabla u)}_k)\) es transferencia modal no lineal. **Prueba.** Como \(D_K\ge0\), se tiene \([\Pi_K-D_K]_+\le |\Pi_K|\). Usar \(|\sum_{|k|\ge K}T_k|\le\sum_{|k|\ge K}|T_k|\); integrar \(2K\) desde \(K_0\), aplicar Tonelli y obtener \(\sum_k(|k|^2-K_0^2)_+|T_k|\le\sum_k|k|^2|T_k|\). Cauchy–Schwarz espectral y Plancherel dan la última desigualdad. \(\square\)

**Lema O67-T2 (barrera de Sobolev).** En la misma clase, para alguna constante \(C\),

\[
\|\mathbb P(u\cdot\nabla u)\|_2\le\|u\cdot\nabla u\|_2
\le\|u\|_6\|\nabla u\|_3
\le C Y^{3/4}Z^{1/4}.
\tag{67.6}
\]

En efecto \(\|u\|_6\le C\|\nabla u\|_2\) por Sobolev para campos sin media y \(\|\nabla u\|_3\le C\|\nabla u\|_2^{1/2}\|\Delta u\|_2^{1/2}\) por interpolación. Junto con O67-T1:

\[
\boxed{F_{K_0}(t)\le C Y(t)^{3/4}Z(t)^{3/4}.}
\tag{67.7}
\]

Por Young, con cualquier \(\nu>0\),

\[
\boxed{F_{K_0}(t)\le \frac\nu2 Z(t)+C_\nu Y(t)^3,\qquad C_\nu=C\nu^{-3}.}
\tag{67.8}
\]

Éste es el punto de obstrucción del método elemental: energía sólo acota \(\int Y\), **no** \(\int Y^3\) ni \(\int Z\). La desigualdad (67.8) no cierra por sí misma el presupuesto O66.

### Un error que debemos evitar

\(\int_0^T Y\,dt<\infty\) no implica \(\int_0^T Y^2\,dt<\infty\), menos aún \(\int_0^T Y^3\,dt<\infty\). Esto es cierto incluso para funciones no negativas con soporte compacto y mismo valor inicial; no es una afirmación acerca de la existencia de una solución de Navier–Stokes con explosión.

## IV. Control independiente: prueba de continuación condicional [T]

Probamos la desigualdad habitual de enstrofía al probar (67.1) contra \(-\Delta u\):

\[
\frac12Y'(t)+\nu Z(t)
\le C Y(t)^{3/4}Z(t)^{3/4}
\le \frac\nu2 Z(t)+C\nu^{-3}Y(t)^3.
\tag{67.9}
\]

Luego, para \(Y>0\),

\[
\frac{d}{dt}\log Y(t)\le C\nu^{-3}Y(t)^2.
\tag{67.10}
\]

**Corolario O67-T3.** Si \(\int_0^{T_*}Y(t)^2\,dt<\infty\) para una solución clásica en su intervalo maximal finito, entonces \(Y(t)\) queda acotada y la solución es prolongable. Es un criterio clásico, no una nueva cota a priori. **La desigualdad energética disponible (67.3) no aporta esa hipótesis.**

## V. Un régimen donde sí se cierra el argumento: datos pequeños [T, clásico]

El producto de normas

\[
\boxed{\chi[u]=\frac{\|u\|_2^{1/2}\|\nabla u\|_2^{1/2}}{\nu}}
\tag{67.11}
\]

es adimensional si las normas se calculan sobre el dominio tridimensional físico. Bajo el reescalamiento natural de NS en \(\mathbb R^3\), \(u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t)\), se conserva \(\chi\): \(\|u_\lambda\|_2=\lambda^{-1/2}\|u\|_2\) y \(\|\nabla u_\lambda\|_2=\lambda^{1/2}\|\nabla u\|_2\). En el toro fijo, \(\chi\) sigue siendo un índice físico de amplitud, aunque no toda homotecia preserve el mismo dominio periódico.

**Teorema O67-T4 (pequeñez suficiente; clásico).** Existe una constante \(c_*>0\), vinculada a las constantes de Sobolev del dominio, tal que, si \(u_0\) es suave, sin media y \(\chi[u_0]<c_*\), la solución sin fuerza permanece suave globalmente.

**Prueba elemental.** Sobolev e interpolación dan

\[
\|u\|_3\le \|u\|_2^{1/2}\|u\|_6^{1/2}
\le C\|u\|_2^{1/2}\|\nabla u\|_2^{1/2}=C\nu\chi[u].
\tag{67.12}
\]

La no linealidad en (67.9) también satisface

\[
\left|\int (u\cdot\nabla u)\cdot\Delta u\,dx\right|
\le\|u\|_3\|\nabla u\|_6\|\Delta u\|_2
\le C\|u\|_3 Z.
\tag{67.13}
\]

Si \(\chi\) es suficientemente pequeño, \(CY^{1/4}U^{1/4}\le\nu/2\). Entonces \(Y'\le-\nu Z\le0\), mientras (67.3) da \(U'\le0\). Por continuidad, \(\chi(t)\) no aumenta, el umbral pequeño se conserva y \(Y(t)\) permanece acotada para todo tiempo finito. La solución fuerte puede continuarse indefinidamente. \(\square\)

Esta es una **consecuencia física cuantitativa real** de un control conjunto de escala y amplitud. Pero no es un teorema universal: no sabemos deducir para datos generales la condición \(\chi<c_*\). Tampoco \(\chi\) es el entero \(N\) de O58 ni demuestra la existencia de una unidad física mínima.

## VI. Controles adversariales [F/E]

**F1 — escalas y energía.** Para \(m\ge1\), \(u_m=e^{-\nu m^2t}(\sin my,0,0)\) es solución exacta. A \(t=0\) toda la familia tiene la misma energía media, pero enstrofía media \(m^2/4\) y frecuencia sin cota. Todas son suaves globales: refutan solo la inferencia «igual energía implica igual control de gradientes».

**F2 — integrabilidad.** Para \(n\ge2\), tome \(Y_n(t)=n\sin^2(\pi n(t-1/4))\) para \(t\in[1/4,1/4+1/n]\) y cero fuera. Son funciones no negativas \(C^1\), no soluciones NS. Sus integrales son

\[
\int Y_n=\tfrac12,\quad\int Y_n^2=\tfrac{3n}8,\quad\int Y_n^3=\tfrac{5n^2}{16}.
\tag{67.14}
\]

Este ejemplo demuestra que un presupuesto \(L^1_t\) no da por sí uno \(L^2_t\) o \(L^3_t\). Se pueden usar funciones compactas \(C^\infty\) con la misma propiedad de escalamiento.

**F3 — fases y presupuesto.** Reprodujimos la familia O66 de dos campos solenoidales con las mismas energías modales, energía total y enstrofía, pero distinta transferencia en la cola \(K=1.1\). Para \(\nu=0.025\), el flujo original tiene \(\Pi_{1.1}-D_{1.1}<0\); el de fase modificada tiene \(\Pi_{1.1}-D_{1.1}=+0.00095875\) en unidades medias. Por integración exacta de las bandas (en malla Fourier finita), la producción positiva instantánea \(F_{K_0=1}\) es **cero** en el primer caso y \(0.00095875\) en el segundo. La cota exacta por Cauchy de O67-T1 se verifica en ambas representaciones. No se deduce de aquí evolución futura global.

**F4 — invariancia de escala.** La combinación \(\chi\) no cambia bajo el reescalamiento propio de NS en \(\mathbb R^3\), a diferencia de la energía o de la enstrofía separadas. Esto es relevante como candidato de *comparación*, pero no convierte \(\chi\) en el «múltiplo cardinal» de la ontología.

## VII. Dictamen: qué demostró y qué no demostró O67

**[T]** De NS sí derivamos la cota conocida \(F_{K_0}\lesssim Y^{3/4}Z^{3/4}\), la desigualdad de crecimiento cúbico de enstrofía, el criterio condicional de \(Y\in L^2_t\) y un régimen de datos pequeños gobernado por una combinación adimensional de magnitudes. Bajo hipótesis de cierre, el programa puede representarlo sin introducir nuevas dimensiones.

**[F]** El balance energético controla \(\int Y\) pero no, por desigualdades elementales, \(\int Y^2\) ni \(\int Y^3\). La información modal de amplitudes tampoco determina transferencias: importan las relaciones de fase. Esto no demuestra la imposibilidad de toda vía de normalización, sólo la insuficiencia de las hipótesis actuales.

**[A]** El paso hacia datos generales exige demostrar una desigualdad **más fuerte que (67.7)/(67.9)** aprovechando cancelaciones, restricciones de fase, localización de interacciones o alguna propiedad física rigurosamente deducida de NS. Debe reducirse a una cota integrable a priori que controle \(F_{K_0}\) o \(Y\), sin asumirse de antemano. En especial, la ontología de «relaciones habitadas» no suministra todavía esa propiedad dinámica.

**Pregunta operacional O68 propuesta:** ¿Existe una cantidad objetiva \(\mathfrak C[u]\), calculable desde interacciones de fase y no sólo desde cuadrados modales, que permita probar \(F_{K_0}\le g(t)(1+Y(t))\) con \(g\in L^1_{loc}\) controlable por \(u_0,\nu\), **uniformemente al abrir todas las frecuencias**? Antes de proponerla como ley, someterla a F1–F4 y a campos 3D no simétricos. Si no existe bajo la interfaz del programa, registrar el no-go y enriquecer solamente la relación estrictamente necesaria.

## VIII. Reproducibilidad y fuentes

- Ejecutar `python codigo/verificar_o67.py` (NumPy), revisar `resultados/controles.json`.
- El ensayo evalúa identidades de la cizalla exacta, ejemplos funcionales de integrabilidad, el presupuesto espectral finito y la distinción de fase de O66, el control de Cauchy y el índice de escalamiento.
- Este paquete es **aditivo**. No modifica las versiones O66, O53 ni la Imagen Total v3.8.1.
- Referencias externas comparativas: Clay (problema y anuncio de septiembre de 2026), comunicado OpenAI (caso forzado); desigualdades de Sobolev, Gagliardo–Nirenberg, continuación fuerte y resultados clásicos de datos pequeños. Ninguno de esos enunciados externos sustituye la ontología del programa.
