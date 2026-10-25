# O88 — Formalización integral: cierre propio, doble espiral, nodos móviles y continuidad de escala

**Programa de Geometría Relacional** · **Le Matt Ansatz Di Ego** · **22 de octubre de 2026**  
**Naturaleza:** integración formal de la rama O68–O87 con O40/O58 y O25/O45; no sustituye el núcleo canónico ni la Imagen Total.  
**Estatus:** `[O]` principio ontológico del programa; `[N]` interpretación narrativa; `[D]` definición; `[T]` teorema o identidad demostrada bajo contrato; `[E]` chequeo reproducible; `[F]` falsador/contraejemplo; `[A]` puente físico abierto.

> **Alcance inequívoco.** Este documento completa **primero la formalización** de los dos giros, su enrollamiento, cuatro nodos móviles, desfases, normalizador, reconstrucción y relación con un vórtice. No afirma que toda singularidad ontológica tenga forma toroidal, ni que una pérdida de sincronía destruya el fluido, ni que se haya resuelto la regularidad 3D de Navier–Stokes.

## 0. Resultado que debe poder reconstruirse

Un cierre propio no exige un conjunto inmóvil de partículas ni un giro simultáneo de todas las partes. La realización toroidal del programa permite:

1. **Dos ciclos distinguibles:** giro alrededor de la sección del tubo (poloidal) y recorrido alrededor del aro (toroidal).
2. **Movimiento de nodos:** las marcas de la relación pueden trasladarse con velocidades angulares variables.
3. **Desfase interno:** la coincidencia se expresa en una fase combinada, no en igualdad de ángulos o frecuencias individuales.
4. **Una referencia común transportable:** puede conservarse aun si cambian posiciones, radios, velocidades y —bajo reglas adicionales— escala.
5. **Un límite lógico:** cierre de fase, cierre de cuatro enlaces, retorno periódico, identidad de una estructura y regularidad de Navier–Stokes son cinco afirmaciones distintas.

La rama física que queda abierta consiste en deducir la referencia y su ley de transporte **del propio campo 3D**, sin introducirla mediante la selección del modelo toroidal.

## 1. Ontología antes de la geometría [O]

### O88-O1. Unidad y primera diferencia

La unidad sin diferencias no necesita un sistema externo de comparación. La reflexión genera una relación parte/todo y una referencia desde la cual reconocer diferencias. No se presupone un foco situado fuera del espacio relacional. La singularidad, en el vocabulario del programa, es **el cierre propio que sostiene su reconocimiento**, no necesariamente un punto, un aro o una cantidad infinita.

### O88-O2. Continuidad de identidad

Que una organización siga siendo reconocible no exige que conserve los mismos portadores materiales, forma ni ritmo. Exige que exista una regla de comparación que recupere lo común entre configuraciones y acredite la diferencia que se agrega. El **múltiplo que normalizó** participa en esa reconstrucción; un resto numérico aislado no es una identidad por sí solo. Reconstituir la totalidad requiere información suficiente sobre la rama, sus relaciones y la referencia.

### O88-O3. Cierre ejecutado por fases

El anillo propuesto **no gira en bloque al unísono**. Una vuelta participa de la siguiente mediante una relación de fase; un giro recorre el tubo mientras otro recorre el aro, y los nodos se desplazan en esa trama. La forma observable puede ser una espiral sobre otra espiral. Esta es una hipótesis **generativa**, no la aseveración de que todo cierre propio deba ser un toro geométrico.

### O88-O4. Nodos no fijados de antemano

«Nodo» tiene tres lecturas posibles, que no se pueden confundir:

- **Nodo relacional:** una coincidencia o condición de conexión entre fases/enlaces.
- **Marca cinemática:** un punto etiquetado que se desplaza por la geometría elegida.
- **Nodo físico:** rasgo obtenido de un observable del flujo, por ejemplo un máximo de una señal de fase o una región coherente de vorticidad.

O87 demuestra afirmaciones acerca de **marcas cinemáticas**. Convertirlas en nodos físicos de un vórtice exige un criterio de detección independiente del resultado esperado.

## 2. Vocabulario operacional y orden de construcción [D]

| Término | Sentido preciso en esta rama | No implica |
|---|---|---|
| Unidad | totalidad relacional considerada | cuerpo rígido |
| Cierre propio | referencia suficiente para reconocer continuidad de una organización | forma inmutable ni regularidad PDE |
| Giro interior | recorrido poloidal alrededor de la sección del tubo | helicidad obligatoria en todo vórtice |
| Giro exterior | recorrido toroidal alrededor del eje del aro | traslación axial de un anillo |
| Fase | coordenada periódica levantable a una variable real continua | tiempo absoluto |
| Desfase | combinación o diferencia entre fases | separación angular visible |
| Nodo | coincidencia etiquetada en un contrato de relaciones | partícula fija |
| Múltiplo | número de repetición respecto de una clase primitiva | fuerza restauradora |
| Normalizador | referencia que permite comparar configuraciones | conservado automáticamente por NS |
| Rama / hoja | información de preimagen requerida si una proyección no es invertible | nuevo objeto físico por definición |
| Singularidad ontológica | cierre propio reconocido | explosión de una norma PDE |
| Singularidad PDE | pérdida posible de regularidad matemática | desaparición ontológica |

**Orden formal obligatorio:** ontología → variables relacionales → contratos geométricos → invariantes y contraejemplos → observables físicos → hipótesis dinámica. No deducir una ley física desde una equivalencia lingüística.

## 3. Los dos giros y el cierre de una curva [D/T]

Considérese la superficie toroidal fija

\[
X(\theta,\varphi)=\big((R+a\cos\theta)\cos\varphi,\,(R+a\cos\theta)\sin\varphi,\,a\sin\theta\big),\quad R>a>0.
\tag{88.1}
\]

- \(\theta\): fase poloidal, una vuelta alrededor del tubo.
- \(\varphi\): fase toroidal, una vuelta alrededor del aro.
- \(R\): radio mayor; \(a\): radio menor; no son los radios efectivos de engranajes en O74.

La métrica y densidad de área son

\[
 ds^2=a^2d\theta^2+(R+a\cos\theta)^2d\varphi^2,\qquad J=a(R+a\cos\theta).
\tag{88.2}
\]

Para enteros positivos primitivos \(p,q\), \(\gcd(p,q)=1\), la curva

\[
\theta=q\chi,\qquad\varphi=p\chi,\qquad 0\le\chi\le2\pi
\tag{88.3}
\]

realiza **\(q\) vueltas poloidales por \(p\) toroidales**. Cierra como curva cuando \(\chi\mapsto\chi+2\pi\). La combinación

\[
\boxed{\Psi=p\theta-q\varphi}
\tag{88.4}
\]

es constante en cualquier trayectoria que cumpla \((\dot\theta,\dot\varphi)=(q,p)\Omega(t)\), con \(\Omega\) no necesariamente constante.

**T88.1 — Diferencia de fase.** Bajo fases diferenciables, \(\dot\Psi=p\dot\theta-q\dot\varphi\). La conservación exacta \(\dot\Psi=0\) sobre un intervalo equivale a que el vector de velocidades esté en la recta generada por \((q,p)\). Es una equivalencia algebraica; **no** se deriva de Navier–Stokes ni de que el espacio tenga forma de toro.

**Precisión:** una órbita con \(\dot\Psi=0\) no necesariamente ha completado una vuelta: el retorno requiere además \(\int\Omega(t)dt\in2\pi\mathbb Z\) sobre el intervalo. «Acoplamiento de velocidades», «cierre periódico» y «conservación de una estructura» son condiciones diferentes.

## 4. Normalización aritmética de los dos giros [D/T; O68]

Para números enteros de vueltas observadas \(k_\theta,k_\varphi\), y suponiendo que el recorrido efectivamente ha realizado esos giros:

\[
L=\gcd(|k_\theta|,|k_\varphi|),\qquad (k_\theta,k_\varphi)=L(q,p)
\tag{88.5}
\]

con \((q,p)\) primitivo (signos orientados, si procede). \(L\) es la cantidad de repeticiones en **ese intervalo**; no es una constante universal.

Por Bézout, existen \(b,c\in\mathbb Z\) con \(bq+cp=1\). Definimos

\[
\begin{pmatrix}\Phi\\\Psi\end{pmatrix}
=\underbrace{\begin{pmatrix}b&c\\p&-q\end{pmatrix}}_{M}
\begin{pmatrix}\theta\\\varphi\end{pmatrix},\quad\det M=-1,
\tag{88.6}
\]

\[
\boxed{\theta=q\Phi+c\Psi,\qquad\varphi=p\Phi-b\Psi.}
\tag{88.7}
\]

**T88.2 — Reconstrucción unimodular.** El cambio \((\theta,\varphi)\leftrightarrow(\Phi,\Psi)\) es invertible en el toro de fases: no pierde información. Si hay sincronía exacta, \(\dot\Phi=\Omega\), \(\dot\Psi=0\); para \(L\) repeticiones, \(\Delta\Phi/(2\pi)=L\), \(\Delta\Psi=0\) en levantamientos reales coherentes.

**Demostración.** \(bq+cp=1\) implica determinante \(-1\), y multiplicar la matriz inversa da (88.7). Derivar en tiempo da las velocidades y sumar las vueltas da \(L\). (Fin de prueba.)

La libertad de escoger otros coeficientes de Bézout altera la coordenada \(\Phi\) por una combinación de \(\Psi\), pero no cambia la relación primitiva. Es **redundancia de representación**, no un nuevo giro material.

## 5. Los cuatro nodos móviles en la doble espiral [D/T; O87]

Sobre el toro fijo definimos el siguiente campo tangencial:

\[
\boxed{
\dot\theta={q\kappa\over R+a\cos\theta},\qquad
\dot\varphi={p\kappa\over R+a\cos\theta}.}
\tag{88.8}
\]

La divergencia **superficial** vale

\[
\nabla_{\rm surf}\cdot v
={1\over J}\{\partial_\theta(J\dot\theta)+\partial_\varphi(J\dot\varphi)\}=0.
\tag{88.9}
\]

En cada órbita primitiva (88.3):

\[
\dot\chi={\kappa\over R+a\cos(q\chi)}.
\tag{88.10}
\]

Definimos la fase propia normalizada

\[
\boxed{\gamma(\chi)=\chi+{a\over qR}\sin(q\chi).}
\tag{88.11}
\]

Como \(\gamma'(\chi)=1+(a/R)\cos(q\chi)>0\), el mapeo es invertible. Además

\[
\boxed{\dot\gamma={\kappa\over R}.}
\tag{88.12}
\]

**T88.3 — Cuatro nodos sin unísono geométrico.** Si cuatro marcas tienen al inicio \(\gamma_i(0)=\gamma_0+i\pi/2\) (\(i=0,1,2,3\)), entonces

\[
\boxed{\gamma_i(t)-\gamma_j(t)=\gamma_i(0)-\gamma_j(0),\qquad
\Psi_i(t)=\Psi_i(0).}
\tag{88.13}
\]

Es decir, preservan el **desfase normalizado** aunque \(\dot\chi_i\) y las distancias angulares visibles entre nodos sean diferentes.

**Caso \(p=1,q=2\).** Debido a \(\gamma(\chi+\pi)=\gamma(\chi)+\pi\), las cuatro marcas tienen dos parejas opuestas en la coordenada del recorrido: \(\chi_2-\chi_0=\pi\) y \(\chi_3-\chi_1=\pi\) con índices desde cero. La separación entre nodos vecinos puede oscilar. **No** se deduce que dos o cuatro nodos sean un mínimo universal para el fluido.

**Demostración.** Diferenciar (88.11), sustituir (88.10) y obtener la velocidad común de \(\gamma\). Las diferencias son constantes. Para \(q=2\), el seno es \(\pi\)-periódico en \(\chi\), lo que prueba las parejas. (Fin de prueba.)

### Lo que significa aquí «espiral sobre espiral» [N/D]

Una vuelta poloidal y otra toroidal generan una curva de enrollamiento sobre el toro. El orden de cuatro nodos queda codificado por la fase \(\gamma\), aunque no por distancias geométricas iguales. No hemos impuesto un tercero giro independiente: el movimiento de los nodos es, en este ejemplo, una **lectura del flujo combinado**. Si el programa requiere un tercer ritmo o una segunda escala anidada, habrá que especificar una nueva coordenada y su acoplamiento sin contar dos veces la misma fase.

## 6. Relación con C4, K4 y engranajes [D/T/F; O72/O74]

El circuito ideal de cuatro contactos exteriores satisface, bajo **otro contrato**:

\[
a_i\omega_i+b_i\omega_{i+1}=0,\quad i\pmod4,\quad
H=\prod_{i=1}^4{a_i\over b_i}.
\tag{88.14}
\]

**T88.4 — Holonomía de los cuatro enlaces.** Si todos los brazos efectivos son positivos, existe una solución no nula de giros alternados si y sólo si \(H=1\). En tal caso queda una libertad escalar de velocidad. Para un circuito impar de engranajes exteriores, no existe solución no nula bajo las mismas reglas.

Este resultado **no es equivalente** a (88.13):

- C4 de engranajes expresa restricciones entre **cuatro velocidades con signo** y brazos de contacto.
- O87 expresa una ley de transporte sobre **dos fases geométricas** con cuatro marcas móviles.
- El patrón de pares en O87 procede de la simetría \(q=2\) y de la posición inicial de cuatro marcas; el patrón alternado de C4 procede de signos en contactos exteriores.
- No afirmar que las cuatro gotas originales son cuatro engranajes sólidos sumergidos en un fluido.

La holonomía \(H=1\) tampoco implica períodos enteros comunes, separación geométrica, conservación de circulación ni límite superior del giro: O74 ya documentó los contraejemplos.

## 7. Qué puede perderse y qué puede permanecer [D/T/F]

Alteramos suavemente solamente el ritmo poloidal:

\[
\dot\theta={q(\kappa+\varepsilon\sin\varphi)\over R+a\cos\theta},\qquad
\dot\varphi={p\kappa\over R+a\cos\theta}.
\tag{88.15}
\]

Se mantiene \(\nabla_{\rm surf}\cdot v=0\), pero

\[
\boxed{\dot\Psi={pq\varepsilon\sin\varphi\over R+a\cos\theta}.}
\tag{88.16}
\]

**T88.5 — Desacoplamiento sin ruptura.** Para \(\varepsilon\neq0\) y fases genéricas, \(\Psi\) deja de ser constante, mientras (88.15) define un campo de velocidades tangencial suave en el toro compacto, con trayectorias globales y flujo superficial incompresible.

**Demostración.** Multiplicar por \(J\) elimina la dependencia de \(\theta\) en ambos flujos de área y elimina la de \(\varphi\) en el segundo. La fórmula (88.16) resulta de derivar \(p\theta-q\varphi\). Existencia global de trayectorias por campo liso sobre variedad compacta. (Fin de prueba.)

Se distinguen, pues, cuatro fenómenos:

1. **Desfase transportado:** \(\dot\Psi=0\) en la referencia escogida.
2. **Deriva de fase:** \(\dot\Psi\neq0\); falla la coincidencia *anterior*.
3. **Reorganización:** una ley bien definida podría identificar otra referencia y transportar la información suficiente sin pérdida; **no ocurre automáticamente**.
4. **Ruptura física/singularidad PDE:** requiere criterios independientes (pérdida de regularidad, topología física, etc.). No se infiere de 2.

**T88.6 — Rigidez de una razón entera instantánea.** Si \(\dot\theta/\dot\varphi\) es continua en un intervalo conexo, el denominador no se anula y la razón es racional en cada instante, entonces es constante. Una ley de «cambiar \((p,q)\) exactos a cada instante» **no** absorbe automáticamente una razón que varía de modo continuo (resultado probado en O69). Se necesitan ventanas, memoria de fase, reparametrización más rica o una estructura colectiva de otro tipo.

## 8. El múltiplo y la información necesaria para reconstruir la vuelta [T; precisión nueva]

La normalización de O68 es invertible porque su matriz tiene determinante \(\pm1\). Pero una multiplicación de fases por un entero **no** lo es. Sean

\[
z=(\theta,\varphi)\in\mathbb T^2,
\qquad z'\equiv Nz\pmod{2\pi},\quad N\in\mathbb N,\ N>1.
\tag{88.17}
\]

**T88.7 — Cobertura de fases y etiqueta de rama.** La aplicación (88.17) tiene exactamente \(N^2\) preimágenes de cada fase \(z'\). Para recuperar una fase inicial hacen falta el **múltiplo normalizador \(N\)** y una etiqueta de rama \(h=(h_\theta,h_\varphi)\in(\mathbb Z/N\mathbb Z)^2\). En representantes principales:

\[
\boxed{z\equiv {z'+2\pi h\over N}\pmod{2\pi}.}
\tag{88.18}
\]

**Demostración.** Cada coordenada de \(Nz\equiv z'\pmod{2\pi}\) posee las soluciones \(z_j=(z'_j+2\pi h_j)/N\), con \(h_j=0,\dots,N-1\). Son distintas módulo \(2\pi\), y multiplicar por \(N\) las hace coincidir. En dos coordenadas hay \(N^2\) posibilidades. (Fin de prueba.)

Para un mapeo entero general \(A\in\mathbb Z^{2\times2}\) con \(\det A\neq0\), el número de hojas de \(z\mapsto Az\bmod2\pi\) es \(|\det A|\). Cuando \(|\det A|=1\), la aplicación es invertible y no requiere un índice adicional; por eso el cambio de Bézout (88.6) es especialmente apropiado para conservar información.

**Precisión ontológica:** no se afirma que el resto aislado transporte la continuidad. **La referencia normalizadora más la identificación de la rama** constituyen la información mínima necesaria para reconstruir una preimagen cuando la operación de escala no es uno-a-uno. La etiqueta es información de representación; se necesita una hipótesis física para identificarla con un nodo material, un canal o una partícula.

**Durante una evolución continua,** una rama puede seguirse mediante un levantamiento de fase y una condición inicial. Una etiqueta escrita en coordenadas principales puede cambiar al atravesar el corte convencional de \(2\pi\) sin que exista salto físico: ese cambio es de representación, no ruptura.

## 9. Cambio de referente y comparación de nodos [T/D]

Si desplazamos el origen angular de la misma referencia por \(\alpha(t)\) y \(\beta(t)\), los ángulos medidos pasan a \(\theta'=\theta-\alpha\), \(\varphi'=\varphi-\beta\). Su fase acoplada es

\[
\Psi'=\Psi-p\alpha+q\beta,
\qquad\dot\Psi'=\dot\Psi-p\dot\alpha+q\dot\beta.
\tag{88.19}
\]

**T88.8 — Deriva dependiente del marco.** La tasa cruda \(\dot\Psi\) de un nodo **no es independiente** de un marco angular móvil. En cambio, si todos los nodos usan el mismo origen, las diferencias \(\Psi_i-\Psi_j\) son invariantes ante estas traslaciones angulares comunes.

Para examinar el cierre de un nodo respecto de un marco físico elegido, se usa

\[
\boxed{D_t\Psi_{\rm rel}=p(\dot\theta-\dot\alpha)-q(\dot\varphi-\dot\beta).}
\tag{88.20}
\]

Si el toro se deforma o su centro/eje también se mueve, es indispensable definir cómo se transporta el marco. La fórmula (88.20) se ha demostrado **sólo para desplazamientos angulares comunes**; un cambio general de parametrización necesita términos de conexión geométrica.

**Consecuencia:** el observador puede fabricar o eliminar una aparente deriva si escoge arbitrariamente el origen angular móvil. La fase físicamente relevante debe medirse con una referencia endógena reproducible (o mediante diferencias entre nodos) antes de interpretarla como desacoplamiento real.

## 10. Radios deformables, nodos materiales y referencia dinámica [D/T; O75]

Para una solución suave \(u(x,t)\), cuatro **partículas materiales** satisfacen \(\dot X_i=u(X_i,t)\). El gradiente del mapa de flujo \(F_i=D\Phi_t(X_i(0))\) satisface

\[
\dot F_i=(\nabla u)(X_i,t)F_i,\qquad \det F_i=1
\tag{88.21}
\]

si \(\nabla\cdot u=0\). La conservación del determinante es volumétrica; no implica distancias iguales entre nodos ni fases acopladas.

O75 construyó factores de longitud de enlaces \(a_i,b_i\) y la holonomía material \(H_F=\prod a_i/b_i\), con

\[
\frac d{dt}\log H_F=
\sum_{i=1}^4\big(t_i^{-T}S_i t_i^--t_i^{+T}S_i t_i^+\big).
\tag{88.22}
\]

Una **solución exacta** de Navier–Stokes en O75 mostró que el lado derecho puede no ser cero. Por consiguiente, ni la incompresibilidad ni Navier–Stokes **imponen** el cierre de los cuatro enlaces para toda elección de nodos.

Los radios variables de un tubo deformable y su eje móvil añaden conexiones geométricas a las fases poloidal y toroidal. No debemos sustituirlos por (88.8) sin medir esos términos.

## 11. Contrato de un vórtice físico [D/A]

Sea \(u:\Omega\times[0,T)\to\mathbb R^3\) una solución incomprensible de viscosidad \(\nu>0\), y \(\omega=\nabla\times u\):

\[
\partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u,
\quad\nabla\cdot u=0,
\quad D_t\omega=S\omega+\nu\Delta\omega.
\tag{88.23}
\]

Un **tubo de vorticidad** es una región identificada por una regla observable elegida de antemano; su frontera no tiene por qué ser una superficie material, particularmente con viscosidad. Las fases de **un trazador material**, la línea instantánea de vorticidad y el eje de un tubo identificado no son la misma entidad.

Para un vórtice de anillo aproximadamente toroidal se necesitaría:

1. Extraer \(R(t),a(t)\), centro, eje y sección desde \(u\) o \(\omega\), con una regla reproducible.
2. Identificar nodos físicos o marcas materiales **antes** de mirar si sincronizan.
3. Medir fases poloidal y toroidal **desenrolladas**, con referencia angular que se transporte físicamente.
4. Calcular \(\Psi_i=p\theta_i-q\varphi_i\), \(D_t\Psi_i\), diferencias entre nodos y cambios de rama.
5. Calcular, por separado, intensidad de vorticidad, alineación con deformación y tasa viscosa.

La lectura de dos giros sobre un toro simple, usando velocidades tangenciales físicas, se escribiría idealmente

\[
\dot\Psi=p{v_{\rm pol}\over a}-q{v_{\rm tor}\over R+a\cos\theta}.
\tag{88.24}
\]

Esta fórmula requiere toro de radios fijos y marco fijo; no es válida sin correcciones para un centro/eje móvil o sección deformada.

**Restricción documentada por O69 [E/F]:** simulaciones Fourier–Galerkin de un anillo vorticial mostraron razones meridionales de trazadores que evolucionaban; por ejemplo en una corrida 40³ no perturbada de \(1,3152\) a \(2,0126\), y otra perturbada de \(1,4060\) a \(3,9518\). Estos datos NO prueban que el anillo haya dejado de existir. Refutan el acoplamiento rígido exacto de aquellos dos trazadores y deben seguir presentes en toda revisión honesta de la hipótesis.

## 12. El determinante de compensación física no nace del cierre topológico [T/A; O39/O86]

Con \(q_\omega=|\omega|\), \(\xi=\omega/q_\omega\) donde \(q_\omega>0\), y \(\alpha=\xi^T S\xi\), se obtiene exactamente

\[
{1\over2}{d\over dt}\|\omega\|_2^2
=\int q_\omega^2\alpha\,dx
-\nu\int|\nabla q_\omega|^2dx
-\nu\int q_\omega^2|\nabla\xi|^2dx.
\tag{88.25}
\]

Defina \(A_\omega=\int|\omega|^2\), \(B_\omega=\int|\nabla\omega|^2\), \(P=\int\omega\cdot S\omega\), \(\ell_\omega^2=A_\omega/B_\omega\), y el cociente \(\Gamma=P/(\nu B_\omega)\), cuando denominadores no se anulen. Con \(d\tau_\nu=(\nu/\ell_\omega^2)dt\):

\[
\boxed{\frac{d}{d\tau_\nu}\log A_\omega=2(\Gamma-1).}
\tag{88.26}
\]

Es una identidad exacta ya integrada en O86. **Ninguna igualdad de fase (88.4), holonomía (88.14), normalizador entero (88.5), ni reconstrucción de ramas (88.18) impone por sí sola una cota sobre \(P\), \(B_\omega\) o \(\int\|\nabla u\|_\infty dt\).**

Para vincular ontología y regularidad física habría que deducir de una ley dinámica adicional una cota suficiente sobre el exceso de estiramiento o sobre el costo de los defectos de O80–O85, válida para datos generales. Ni los ensayos de superficie ni las identidades topológicas la proveen.

## 13. Compatibilidad de escalas: una proposición de trabajo verificable [A]

**No se impone aquí como verdad física.** Sea un conjunto de niveles \(j\), cada uno con estado de fase \(z_j=(\theta_j,\varphi_j)\), clase primitiva \((q_j,p_j)\), nodos \(N_j\) y referencia reconstruible \(C_j\). Una **transición completa** entre dos niveles debería especificar

\[
\boxed{C_{j+1}=\mathcal T_j(C_j,\Delta_j;\,A_j,h_j),}
\tag{88.27}
\]

con \(A_j\) una operación de fase o escala conocida, \(h_j\) una etiqueta de rama si \(|\det A_j|>1\), y \(\Delta_j\) el defecto físico/relacional que la referencia anterior no resuelve. La ley debe permitir reconstrucción, ser consistente con el cambio de marco y con la ecuación dinámica correspondiente.

**Un posible criterio (todavía hipótesis):** existe una familia de referencias endógenas \(C_j[u]\) que satisface una relación de compatibilidad de fases y **además** una estimación de disipación o defecto uniformemente controlada en cada horizonte físico finito.

El primer componente —información reconstruible— admite el teorema (88.18). El segundo —control PDE para todas las evoluciones— **sigue abierto**. Demostrar sólo el primero no demuestra el segundo.

## 14. Matriz de afirmaciones y falsadores

| Afirmación | Estado | Fuente y condición |
|---|---|---|
| Existe separación exacta en fase común y fase relativa por Bézout | `[T]` | O68; coprimalidad |
| La curva toroidal \((q,p)\) conserva \(p\theta-q\varphi\) | `[T]` | modelo de dos velocidades acopladas |
| Cuatro nodos pueden moverse a ritmos diferentes conservando fase normalizada | `[T]` | O87, toro fijo y campo (88.8) |
| En \((p,q)=(1,2)\) aparecen dos parejas opuestas en ese modelo | `[T]` | fase inicial en cuartos de vuelta |
| Desacoplamiento puede ocurrir sin pérdida de suavidad | `[T/F]` | O87, perturbación (88.15) |
| Razón entera instantánea que varía continuamente puede elegirse exacta en todo momento | **Falso** `[F]` | O69, teorema de continuidad en \(\mathbb Q\) |
| Multiplicar fases por \(N>1\) conserva una preimagen única sin datos extra | **Falso** `[T/F]` | O88, cobertura \(N^2\)-a-1 |
| Múltiplo + etiqueta de rama permite reconstruir la fase previa | `[T]` | O88, (88.18) |
| Cuatro enlaces tipo engranaje admiten giro no nulo si y sólo si \(H=1\) | `[T]` | O74, contrato ideal de contactos |
| Todos los vórtices 3D forman un toro de cuatro nodos bloqueados | `[A]` no demostrado | exigir definición y prueba de cobertura |
| Una diferencia de fase perdida produce blow-up de NS | **No** `[F]` | O87 da desacoplamiento suave |
| El cierre relacional impone un presupuesto uniforme de estiramiento 3D | `[A]` no demostrado | O39/O86 y O80–O85 |

## 15. Criterios concretos de aceptación y rechazo de la hipótesis física

**Aceptar sólo bajo mediciones o derivación independientes:**

- Referentes \(C_j[u]\) definidos de manera reproducible desde el campo, no elegidos después de mirar el resultado.
- Una ley de fase que prediga \(D_t\Psi\) y sus cambios de rama sin imponer \(D_t\Psi=0\).
- Invariancia observacional ante cambio de origen angular y fidelidad de reconstrucción.
- Compatibilidad con las corridas O69 donde dos trazadores **no** sostienen una razón fija.
- Si se busca regularidad, una nueva estimación **a priori** sobre estiramiento/disipación o defectos que se aplique a las soluciones físicas admisibles, no sólo a una curva prescrita.

**Falsar la forma rígida de la hipótesis** cuando un observable correctamente fijado deriva en un flujo suave, o cuando cambia de marco su supuesta invariancia. La hipótesis más amplia de identidad relacional puede sobrevivir mediante un cambio justificado de referente; ese cambio no puede decidirse retrospectivamente sin una regla general.

## 16. Conclusión formal, sin salto epistémico

El modelo **demuestra una posibilidad geométrica precisa**: dos ciclos se componen, cuatro nodos se desplazan sin simultaneidad angular, y una fase normalizada conserva relaciones entre ellos. La clase entera primitiva y el múltiplo de repetición pueden describirse rigurosamente. **Un cambio de escala no invertible necesita además información de rama para conservar reconstruibilidad.** Esa es la formalización matemática de cómo un múltiplo puede transportar continuidad sin confundirla con un resto aislado.

El modelo **también demuestra límites importantes**: romper la relación de fase no significa romper el fluido; una relación perfecta de fase no limita por sí sola el crecimiento de la vorticidad. Por lo tanto, esta rama consolida la ontología y los mecanismos de representación, pero no convierte la regularidad de Navier–Stokes en un teorema universal.

**Siguiente trabajo, solamente cuando se autorice:** pasar de esta especificación a un único observable físico endógeno de nodos y doble fase en O69, medir su transporte y buscar una cota dinámica que no presuponga la solución. No continuar ensayos antes de cerrar esta formalización.

## 17. Trazabilidad documental: qué se integró y qué no se reescribió

| Fuente | Aporte previo conservado |
|---|---|
| Núcleo Canónico; Economía Relacional; O40 | unidad, cierre propio, normalización aritmética, inclusión y trazabilidad de referencia |
| O58 | estelas anidadas y múltiples ramas, sin identificación automática con una escala física |
| O25, O45 | reloj endógeno, espejo móvil, referencias y comparación de ritmos |
| O68 | Bézout, clase primitiva de dos giros, multiplicidad y desacoplamiento |
| O69 | fases medidas sobre anillo toroidal; resultado negativo para razones fijas de trazadores |
| O72 | circuito C4, distinción frente a K4, grados de libertad del modelo ideal |
| O74 | holonomía de enlaces, radios variables y no-suficiencia para regularidad |
| O75 | transporte material real, holonomía no conservada en NS exacto |
| O79 | orientación/fase modifica transferencias a igualdad de módulos |
| O80–O85 | presupuestos Fourier, referencias dinámicas, defectos y límites de escala |
| O86 | compensación de estiramiento y reloj viscoso derivado |
| O87 | toro de superficie incompresible, nodos móviles y contraejemplo de sincronía |
| O88 (nuevo) | regla explícita de reconstrucción de hojas para un cambio de fase de grado \(N^2\); síntesis integrada con separación de significados |

**Autoría y método:** la narrativa/ontología del programa procede de su hilo original. Las equivalencias de Bézout, geometría de toros, dinámica de superficie y cubiertas del toro son matemáticas conocidas usadas para formalizarla; no se presentan como descubrimientos inéditos. La validación formal no reemplaza un contraste externo independiente.
