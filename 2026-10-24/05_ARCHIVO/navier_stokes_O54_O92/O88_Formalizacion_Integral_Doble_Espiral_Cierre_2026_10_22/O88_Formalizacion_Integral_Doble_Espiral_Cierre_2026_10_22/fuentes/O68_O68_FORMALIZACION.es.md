# O68 — Semilla, normalización de dos giros y múltiplo del sistema

**Programa de Geometría Relacional**  
**Fecha:** 2026-10-21  
**Estado:** suplemento de investigación, no solución de Navier–Stokes.  
**Procedencia del hilo:** «el momento como sustentación en ejecución»; «si lo puede absorber manteniendo la unicidad se sostiene; si no cae en un múltiplo se desacopla»; «los giros están normalizados y dejan la diferencia de su normalizador; el sistema está normalizado y deja un múltiplo del mismo»; los grados de libertad proyectan la indefinición. 

## 0. Secuencia de lectura: narrativa, ontología, matemática, física

**[O] Ontología propuesta**. Una estructura puede lograr cierre propio mediante coincidencia de relaciones que ya no requieren que el medio que permitió su reconocimiento continúe proyectando reflejos. La referencia normalizadora puede transportarse como semilla hacia otra configuración. Cuando crecen o decrecen las relaciones «habitadas», los radios y frecuencias pueden cambiar. La continuidad exige compatibilidad de la nueva configuración con la referencia; desacoplarse de una referencia *no equivale* necesariamente a perder regularidad matemática.

**[N] Narrativa**. Dos engranajes no requieren la misma frecuencia: comparten una ley que organiza sus diferencias. Al «apagar los espejos de la caja», la pregunta es si la dinámica interna sigue realizando esa ley. La organización puede continuar sin conservar las mismas partículas. La condición para sostenerse debe examinarse en movimiento, no sólo en un instante.

**[D] Modelo aritmético exacto**. Si se observan dos ciclos cerrados en un intervalo y sus números de vueltas son enteros positivos \(k_1,k_2\), existe una descomposición **única**

\[
L=\gcd(k_1,k_2),\qquad (k_1,k_2)=L(q,p),\qquad \gcd(q,p)=1.
\]

Aquí \((q,p)\) es la clase de proporción primitiva y \(L\) es el número de repeticiones de esa clase en el intervalo. **El valor de \(L\) depende del intervalo/representación; no es por sí solo un invariante físico absoluto.**

Por la identidad clásica de Bézout existen enteros \(a,b\) tales que

\[
 a q+b p=1\quad \Longrightarrow \quad a k_1+b k_2=L.
\]

Esta es una realización aritmética exacta de «unidad de referencia en los giros normalizados» y «múltiplo de ella en el sistema». No requiere que \(|q-p|=1\), ni es una nueva demostración de Bézout. La combinación firmada \(a k_1+b k_2\) es un dato aritmético; interpretarla como diferencia de información física exige reglas adicionales.

## 1. El cambio de coordenadas que aísla la semilla

**[D]** Sean \(\theta_1,\theta_2\) dos ángulos (mod. \(2\pi\)), con velocidades angulares \(\omega_i=\dot\theta_i\). Para un par primitivo \((q,p)\), elijamos \(a,b\in\mathbb Z\) tales que \(aq+bp=1\). Definamos:

\[
\boxed{
\begin{pmatrix}\Phi\\\Psi\end{pmatrix} =
\underbrace{\begin{pmatrix}a&b\\p&-q\end{pmatrix}}_{M}
\begin{pmatrix}\theta_1\\\theta_2\end{pmatrix}}
\]

\[\det M=-aq-bp=-1.\]

La matriz es unimodular, por lo que la transformación es invertible con coeficientes enteros; preserva la estructura periódica del toro de fases \(\mathbb T^2\).

Si las velocidades satisfacen el **acoplamiento exacto**

\[
\boxed{(\omega_1,\omega_2)=(q,p)\Omega(t)},
\]

entonces

\[
\boxed{\dot\Phi=\Omega(t),\qquad \dot\Psi=p\omega_1-q\omega_2=0.}
\]

La referencia diferencial \(\Psi\) permanece constante mientras \(\Phi\) continúa evolucionando. Para velocidades instantáneas, la condición deja un parámetro escalar libre \(\Omega(t)\). *La dinámica del fluido puede restringir o determinar ese parámetro; no es necesariamente un grado de libertad físico independiente.*

Para una trayectoria que da \(k_1=Lq\), \(k_2=Lp\) vueltas, se obtiene

\[
\boxed{\frac{\Delta\Phi}{2\pi}=L,\qquad \frac{\Delta\Psi}{2\pi}=0.}
\]

Así la **semilla representacional** es la clase primitiva \((q,p)\), la fase relativa \(\Psi\) que define la coincidencia, y la regla de reconstrucción; el múltiplo \(L\) expresa la repetición sobre el intervalo escogido. Si \(\Omega\) varía, la sincronía puede mantenerse sin frecuencia fija, siempre que la igualdad diferencial valga en todo instante.

### Ejemplo 1: giros 12 y 8

\(L=\gcd(12,8)=4\); \((q,p)=(3,2)\). Una solución de Bézout es \((a,b)=(1,-1)\). Así:

\[
\Phi=\theta_1-\theta_2,\qquad \Psi=2\theta_1-3\theta_2.
\]

En vueltas observadas: \(\Delta\Phi/(2\pi)=12-8=4\), mientras \(\Delta\Psi/(2\pi)=2(12)-3(8)=0\). Una unidad primitiva y cuatro repeticiones del sistema, con una dirección de movimiento de fase todavía libre.

### Ejemplo 2: la diferencia unitaria no requiere vueltas consecutivas

Para \((q,p)=(5,3)\), \(2\cdot 5-3\cdot3=1\). Si \((k_1,k_2)=(20,12)\), entonces \(2(20)-3(12)=4\). No hay necesidad de que las frecuencias sean vecinas; la combinación normalizada produce la unidad porque \(\gcd(5,3)=1\).

**[A] Aclaración:** Esta identidad de Bézout no es idéntica a la identidad cuadrática O40 \(N^2-(N-1)(N+1)=1\). Ambas tienen un resto entero unitario, pero **no** se ha probado una equivalencia ontológica/física entre ellas.

## 2. Cambio de radios: cuándo se absorbe y cuándo se desacopla

**[H] Hipótesis cinemática, todavía no ley de NS**. En dos recorridos aproximadamente circulares con radios \(r_1,r_2>0\), sean \(v_i\) sus velocidades tangenciales características y \(\omega_i=v_i/r_i\). La compatibilidad de la semilla es:

\[
\boxed{\delta(t):=p\frac{v_1}{r_1}-q\frac{v_2}{r_2}=0.}
\]

La evolución de la fase relativa es \(\dot\Psi=\delta\). Por tanto, una coincidencia inicial \(\delta(t_0)=0\) no basta: necesitamos \(\delta(t)\equiv0\) en el intervalo, o una cota explícita para su deriva.

Diferenciando cuando las variables son suaves:

\[
\boxed{\dot\delta=p\left(\frac{\dot v_1}{r_1}-\frac{v_1\dot r_1}{r_1^2}\right)-q\left(\frac{\dot v_2}{r_2}-\frac{v_2\dot r_2}{r_2^2}\right).}
\]

Esto precisa qué quiere decir **absorber un cambio de radios**: las modificaciones de radios y velocidades tienen que ajustarse conjuntamente para mantener \(\delta=0\), no basta escoger después una fracción que se le parezca.

**Ejemplo.** \((q,p)=(3,2)\), radios iniciales \((r_1,r_2)=(1,2)\), velocidades angulares \((\omega_1,\omega_2)=(3,2)\); las velocidades tangenciales son \((v_1,v_2)=(3,4)\). Si los radios pasan a \((1.2,1.8)\), la sincronía persiste si \((v_1,v_2)\) cambia a \((3.6,3.6)\). Si se conservan las velocidades tangenciales previas \((3,4)\), la nueva deriva es \(\delta=2(3/1.2)-3(4/1.8)=-5/3\), no cero. 

**[H] Desacoplamiento**. Cuando \(\delta\ne0\), \(\Psi(t)-\Psi(0)=\int_0^t\delta(s)\,ds\), y la antigua coincidencia deja de ser un invariante. No se deduce de ello ruptura física, pérdida de identidad global ni blow-up de Navier–Stokes.

## 3. Caso sin múltiplo periódico exacto

Para frecuencias constantes no nulas, si \(\omega_1/\omega_2\) es **irracional**, no existen enteros positivos \(p,q\) que impongan \(p\omega_1-q\omega_2=0\). La evolución sobre el toro de dos fases es no periódica y, bajo esta hipótesis, densa en él. Se pueden tener recurrencias aproximadas, no un período común exacto.

Ello da un sentido formal a «no cae en un múltiplo»: **no se puede representar como cierre periódico exacto de dos vueltas enteras**. No significa que un fluido cuasiperiódico carezca de coherencia ni que se desestabilice necesariamente.

## 4. La dirección total no se obtiene gratis

El espacio de velocidades \(\{(\omega_1,\omega_2):p\omega_1-q\omega_2=0\}\) es una recta generada por \((q,p)\). Ésa es una «dirección» en el **espacio de fases**, no todavía el vector de propagación espacial de un anillo vorticial. Traducirlo en traslación axial precisa una ley dinámica, geometría y signos de circulación. Un toroide tiene dos ciclos geométricos, pero un anillo de vorticidad sin remolino azimutal adicional no tiene necesariamente dos circulaciones materiales independientes. Sus regiones interior y exterior no son engranajes sólidos.

La libertad de elegir coeficientes de Bézout \((a,b)\) también es **redundancia de representación**, no un grado de libertad físico. Las soluciones de \(aq+bp=1\) son \((a+kp,b-kq)\). Esto modifica \(\Phi\) mediante un múltiplo de la coordenada congelada \(\Psi\), pero no la sincronía.

## 5. Barrera frente a la regularidad global de Navier–Stokes

**[F] Falsador del salto indebido.** La sincronización \((\omega_1,\omega_2)=(q,p)\Omega\) no impone ninguna cota superior sobre \(|\Omega|\), ni un radio mínimo positivo. Para cualquier \(M>0\), elegir \(\Omega=M\) respeta la igualdad. También pueden escogerse \(r_1=\varepsilon\), \(r_2=2\varepsilon\), y \(v_i=r_i\omega_i\), con \(\varepsilon\to0\), manteniendo sincronía perfecta. Esto es una familia **cinemática**, no una solución evolutiva de NS, y basta para demostrar que el cierre por sí solo carece de control de gradientes.

**[T] Teorema aritmético**: la descomposición \((k_1,k_2)=L(q,p)\), la existencia de una combinación unitaria primitiva, el determinante \(-1\), y la separación de \(\Phi\) y \(\Psi\) son exactos.

**[H] Hipótesis dinámica nueva**: las fases físicamente bien definidas de ciertas familias de vórtices obedecen una ecuación que conserva o aproxima \(\dot\Psi=0\).

**[F] Prueba adversarial pendiente**: definir las fases desde el campo de Navier–Stokes, verificar \(\dot\Psi\) sin forzar las frecuencias a resonar, y localizar la pérdida de sincronía. Un criterio de regularidad global requeriría además una cota *a priori* que controle escalas y gradientes para datos iniciales generales. Ninguna se deriva de Bézout.

## 6. Programa operativo O69

1. Elegir una familia física bien delimitada: toroide idealizado con y sin componente de remolino azimutal (*swirl*), sin confundir ciclo topológico y recorrido material.
2. Definir \(\theta_1[u],\theta_2[u]\) y \(r_1[u],r_2[u]\) de modo reproducible sin seleccionar retrospectivamente pares enteros.
3. Medir la deriva \(\delta=p\dot\theta_1-q\dot\theta_2\); comparar referencias que aparentemente se sostienen y referencias que se desacoplan.
4. Determinar si la dinámica conserva un modo \(\Psi\) (ley exacta), sólo presenta bloqueo de fase transitorio (fenómeno de una familia), o no ofrece ese acoplamiento.
5. Si aparece una ley, demostrar si impone alguna cota física no tautológica sobre concentraciones; someterla a campos con igual espectro y fases diferentes (O66–O67).

**Conclusión.** O68 sí identifica una manera exacta de transformar «dos giros normalizados dejan una unidad y su conjunto deja un múltiplo» en una semilla aritmética y una coordenada de fase congelada. No demuestra que todo anillo físico obedezca ese acoplamiento ni resuelve el problema de regularidad de Navier–Stokes. El avance es distinguir *qué sería el cierre* y *qué ecuación debe probar que se sostiene*.
