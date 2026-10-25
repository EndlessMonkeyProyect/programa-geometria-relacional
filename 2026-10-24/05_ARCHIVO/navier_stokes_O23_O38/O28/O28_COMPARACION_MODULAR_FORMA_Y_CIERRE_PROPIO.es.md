# O28 — Comparación modular sin agente: forma, ritmo y cierre común de los remolinos

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**19 de octubre de 2026 · Suplemento independiente de exploración formal**  
**Estado:** [O] lectura ontológica; [D] contrato explícito; [T] resultado matemático condicionado; [E] control ejecutable; [F] falsador; [H] hipótesis física abierta.  
**Política de integración:** no modifica el Núcleo Canónico ni la Imagen Total.

## 0. Tesis y precisión del lenguaje [O]

La nueva unidad **no aparece porque dos remolinos se reconozcan, piensen, elijan o busquen** una relación. La comparación es una operación de la estructura de referencia: dadas dos diferencias dotadas de forma y recurrencia, pueden o no sostener una relación modular común. La mera compatibilidad aritmética **no** obliga a una sincronización física, y una sincronización de fase **no** obliga a una fusión de vórtices.

La línea de continuidad con el núcleo es:

`diferencia → comparación de relaciones → módulo/residuo → compatibilidad dinámica → posible cierre propio común`.

«Módulo» designa aquí una relación de recurrencia definida, **no una voluntad**. «Residuo» no significa azar; señala información o condiciones que la comparación declarada no acredita. «Singularidad» solo puede emplearse ontológicamente como foco de una identidad relacional, **nunca** como sinónimo de una explosión de normas en Navier–Stokes.

## 1. Contrato mínimo para comparar dos estructuras [D]

Considérense dos estructuras etiquetadas \(V_1,V_2\) dentro de un flujo. Un contrato de comparación registra, cuando sean observables:

\[
\mathscr I_i=(\mathcal F_i,R_i,\theta_i,\Omega_i,\chi_i,\mathcal E_i),\quad i=1,2,
\]

con:

- \(\mathcal F_i\): firma de **forma propia** (distribución de vorticidad, orientación, deformación u otros invariantes definidos previamente), no simplemente un dibujo del contorno.
- \(R_i>0\): radio o escala declarados por un procedimiento de medición reproducible.
- \(\theta_i\in\mathbb T=\mathbb R/(2\pi\mathbb Z)\): fase válida **solo si se ha definido un fenómeno recurrente**.
- \(\Omega_i>0\): frecuencia natural de esa fase, en el régimen de referencia.
- \(\chi_i\in\{-1,+1\}\): orientación de giro; puede omitirse si se comparan fases orientadas apropiadamente.
- \(\mathcal E_i\): estructura del entorno/circunstancia, incluida separación, geometría y condiciones de acoplamiento.

Un remolino real no ofrece automáticamente una fase canónica ni una frontera única. Cada elección de \(\mathcal F_i,R_i,\theta_i\) forma parte del contrato, no del teorema. **La frecuencia espectral relacional \(v_*/R_i\) no debe confundirse sin prueba con la frecuencia angular material de cualquier remolino.**

## 2. Teorema O28-T1: recurrencia modular exacta [T]

En el modelo de **dos fases de rotación uniforme no acopladas**,

\[
\theta_i(t)=\theta_i(0)+\Omega_i t\pmod{2\pi},\qquad \Omega_i>0,
\]

las dos fases regresan simultáneamente a sus posiciones iniciales después de algún \(T>0\) si y solo si

\[
\boxed{\frac{\Omega_1}{\Omega_2}=\frac pq\in\mathbb Q_{>0}}
\]

para enteros coprimos \(p,q\ge1\). En ese caso el menor período conjunto es

\[
\boxed{T_0=\frac{2\pi p}{\Omega_1}=\frac{2\pi q}{\Omega_2}},
\]

y la fase relativa modular \(\psi=q\theta_1-p\theta_2\pmod{2\pi}\) es constante.

**Prueba.** El retorno simultáneo exige \(\Omega_1 T=2\pi m\) y \(\Omega_2 T=2\pi n\), con \(m,n\in\mathbb N\); su razón es \(m/n\). Reduciendo a \(p/q\) se obtiene \(T_0\). Recíprocamente, la expresión de \(T_0\) produce \(p,q\) vueltas completas y \(\dot\psi=q\Omega_1-p\Omega_2=0\). Al ser \(p,q\) coprimos, ningún retorno positivo más corto es posible. ∎

**Precisión.** La razón racional permite un retorno conjunto, pero no implica fuerza mutua, transferencia de información ni cierre físico del par.

## 3. Teorema O28-T2: conservar las dos identidades bajo una relación [T]

El espacio de las dos fases es el toro \(\mathbb T^2\). Para \(p,q\) coprimos, la restricción

\[
\boxed{q\theta_1-p\theta_2=\psi_*\pmod{2\pi}}
\]

define una **circunferencia de configuraciones** en el toro, no un punto. Por tanto, fija una relación relativa y deja una fase libre.

**Prueba.** La aplicación \(F:\mathbb T^2\to\mathbb T\), \(F(\theta_1,\theta_2)=q\theta_1-p\theta_2\), tiene derivada \((q,-p)\) de rango uno. Por el teorema de la función implícita, cada fibra tiene dimensión uno. La coprimalidad asegura que la fibra es conexa: como existen enteros \(a,b\) con \(qa-pb=1\), el punto inicial \((a\psi_*,b\psi_*)\) satisface la restricción, y la parametrización

\[
(\theta_1,\theta_2)=(a\psi_*+pt,\ b\psi_*+qt)\pmod{2\pi},\quad t\in\mathbb T
\]

recorre toda la fibra una vez. ∎

**Lectura ontológica [O].** El cierre de la **relación** no elimina la pluralidad de fases. La unidad común no sustituye las identidades particulares. El resultado es sobre fases, no prueba que dos remolinos materiales se hayan convertido en un solo remolino.

## 4. Proposición O28-T3: módulo, acoplamiento y cierre dinámico son distintos [T/D]

Para un canal entero \(p:q\), sea \(\psi=q\theta_1-p\theta_2\), \(\delta=q\Omega_1-p\Omega_2\), \(K\ge0\). Considérese este **modelo mínimo declarado de acoplamiento de fases**:

\[
\begin{aligned}
\dot\theta_1&=\Omega_1-\frac{K}{2q}\sin\psi,\\
\dot\theta_2&=\Omega_2+\frac{K}{2p}\sin\psi.
\end{aligned}
\qquad\Longrightarrow\qquad
\boxed{\dot\psi=\delta-K\sin\psi}.
\]

Si \(K>0\) y \(|\delta|<K\), existe una rama de fase relativa estable,

\[
\psi_s=\arcsin(\delta/K)\pmod{2\pi},\qquad
\frac{d\dot\psi}{d\psi}\Big|_{\psi_s}=-K\cos\psi_s<0.
\]

Si \(|\delta|>K\), no hay equilibrio de fase relativa y esta deriva. Si \(|\delta|=K\), el equilibrio es degenerado, no una prueba de estabilidad robusta. Si \(K=0\) y \(\delta=0\), la fase relativa es constante pero **no es atractora**: hay recurrencia compartida sin sincronización dinámica estabilizada.

**Prueba.** Se resta \(p\dot\theta_2\) de \(q\dot\theta_1\); los términos de acoplamiento suman \(-K\sin\psi\). Las condiciones resultan de \(\delta=K\sin\psi\) y del signo de la derivada. ∎

**Contraejemplo relevante:** \(\Omega_1=\sqrt2,\ \Omega_2=1,\ p=q=1\) no tienen retorno conjunto en ausencia de acoplamiento; sin embargo, con \(K>\sqrt2-1\) aparece **bloqueo de fases** en este modelo: las frecuencias *efectivas* se ajustan. Por tanto, la racionalidad de los ritmos **naturales** no es una condición necesaria para sincronización con acoplamiento. La racionalidad exacta de T1 era una propiedad del régimen *no acoplado*.

**No-go interno:** dados los mismos \(R_i,\Omega_i\), elegir \(K=0\) o un \(K>|\delta|\) puede cambiar la existencia de fase relativa atractora. Ninguna regla dependiente **solo** del cociente de radios puede decidir universalmente el cierre dinámico dentro de esta familia de modelos.

## 5. Corolario O28-T4: cuando existe la correspondencia radio–ritmo [T/D]

En la familia modal del programa donde ha sido derivado \(R_i\omega_i=v_*\), con el **mismo** \(v_*>0\) y la misma normalización para ambos modos,

\[
\frac{\omega_1}{\omega_2}=\frac{R_2}{R_1},
\qquad
\boxed{q\omega_1=p\omega_2\iff qR_2=pR_1}.
\]

Por ejemplo, para \(R_1=2R_0, R_2=3R_0\), se tiene \(\omega_1/\omega_2=3/2\) y un módulo de recurrencia \(p:q=3:2\).

**Prueba.** Sustitución algebraica de \(\omega_i=v_*/R_i\). ∎

**Límite de aplicabilidad.** El \(\omega_i\) de la rama espectral no es automáticamente el \(\Omega_i\) de rotación del fluido. Para un vórtice de Lamb–Oseen, por ejemplo, la velocidad azimutal a radio \(r\) depende de la circulación \(\Gamma_{\rm circ}\), además de \(r,\nu,t\):

\[
\Omega_{\rm mat}(r,t)=\frac{\Gamma_{\rm circ}}{2\pi r^2}
\left(1-\exp\left[-\frac{r^2}{4\nu t}\right]\right),\qquad t>0.
\]

A igual radio característico, duplicar \(\Gamma_{\rm circ}\) duplica esa velocidad angular material. Así, no puede insertarse \(\Omega_{\rm mat}=v_*/R\) para todos los remolinos de Navier–Stokes sin nuevas hipótesis y pruebas.

## 6. Comparación con presupuesto finito y residuo [D/T]

Para frecuencias \(\Omega_1,\Omega_2>0\) y presupuesto entero \(N\ge2\), definimos la **firma modular finita**:

\[
\boxed{
\varepsilon_N=\min_{p,q\in\mathbb N,\ p+q\le N}
\frac{|q\Omega_1-p\Omega_2|}{q\Omega_1+p\Omega_2}}
\]

y guardamos al menos un par minimizador \((p_N,q_N)\). La elección de costo \(p+q\) es una hipótesis explícita de economía representacional; no es un axioma físico deducido.

**Propiedades:** \(\varepsilon_N\ge0\); no aumenta al aumentar \(N\); vale cero cuando el presupuesto alcanza un par entero exactamente compatible; para una razón irracional y todo \(N\) finito es estrictamente positiva. Estas propiedades se prueban por finitud y anidamiento de conjuntos de candidatos. Una razón irracional puede admitir aproximaciones arbitrariamente buenas; ningún presupuesto finito acredita su irracionalidad con medidas experimentales de precisión finita.

El residual orientado de fase para un par \((p,q)\) es \(\delta_{p,q}=q\Omega_1-p\Omega_2\). Sin acoplamiento, la diferencia modular se desplaza \(\psi(t)=\psi(0)+\delta_{p,q}t\). Una tolerancia \(\tau_\psi>0\) permanece satisfecha desde la alineación inicial, a lo sumo hasta \(\tau_\psi/|\delta_{p,q}|\) si \(\delta_{p,q}\ne0\).

**Lenguaje:** una relación modular aproximada deja un **resto comparativo**, no una probabilidad, intención ni «error del mundo».

## 7. Puente explícito con Navier–Stokes [H/A]

En Navier–Stokes incomprensible,

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u+f,\quad \nabla\cdot u=0,
\]

la forma y la continuidad de un remolino deben definirse mediante observables del campo \(u\) y su vorticidad. Dos estructuras no quedan identificadas por su radio solamente; O26 ya ofrece contrapruebas a la suficiencia de firmas espectrales truncadas. O27 distingue además estiramiento paralelo y desviación perpendicular de la vorticidad en 3D.

Para convertir el presente modelo en una predicción física se requiere, **antes de mirar el resultado**, decidir:

1. cómo segmentar y seguir estructuras vorticiales a lo largo del tiempo;
2. qué firma de **forma** \(\mathcal F\), radio, fase y frecuencia se usa, y con qué estabilidad frente a resolución;
3. cómo se extrae \(K\) o un operador de acoplamiento del campo de velocidades de Navier–Stokes **sin ajustarlo retrospectivamente al bloqueo observado**;
4. qué significa «nuevo cierre propio» en términos de persistencia, transporte, coherencia y reconstrucción de dos identidades dentro del flujo;
5. cómo se controla el caso negativo: fases aritméticamente compatibles pero flujo sin acoplamiento estable, y fases inicialmente incompatibles que se sincronizan por interacción.

El mismo esquema debe someterse a flujos bidimensionales y tridimensionales, e identificar separadamente circulación, orientación, estiramiento y disipación. El módulo algebraico no reemplaza las ecuaciones de presión, difusión ni estiramiento.

### Falsadores [F]

- [F1] Una regla propuesta de unión basada únicamente en \(R_1/R_2\) falla ante dos campos con esos radios iguales pero geometría o acoplamiento diferentes.
- [F2] La fase no se puede definir de manera estable al cambiar la resolución o el observador: la firma modular física no está bien planteada.
- [F3] El parámetro \(K\) se ajusta desde la propia sincronización que pretende predecir: la propuesta es circular.
- [F4] El criterio atribuye identidad persistente a estructuras que se disipan o se disgregan en una solución NS suave.
- [F5] Se proclama \(R\Omega_{\rm mat}=c\) como universal sin medir la circulación, contrariando casos conocidos.

## 8. Complemento lingüístico con la gramática existente

| Voz del programa | O28: correspondencia disciplinada | Evitar |
|---|---|---|
| Diferencia | fases/formas distinguibles dentro de la trama | voluntad o elección |
| Comparación | relación entera \(p:q\), residuo de fase, circunstancia | reconocimiento consciente |
| Módulo común | recurrencia exacta o aproximada declarada | fuerza de atracción automática |
| Comunes / trama | relaciones compartidas que permiten describir el conjunto | «herencia» donde no corresponda |
| Cierre propio | conjunto dinámico coherente, con contrato de persistencia | simple coincidencia de radios |
| Indefinición | múltiples estructuras que una firma aún no discrimina | azar intrínseco demostrado |
| Proyección | descripción bajo una referencia explícita | borrado ontológico de componentes |
| Complemento | diferencias necesarias para nuevas consultas | perpendicularidad asumida a priori |
| Ritmo | fase por actualización o frecuencia física **según contrato** | identificar sin puente ambos relojes |
| Singularidad | foco relacional de identidad (lectura ontológica) | singularidad PDE / blow-up |

La regla originaria se conserva sin antropomorfismo: **comparar módulos no es elegir una solución; es declarar qué relación se sostiene y qué resto permanece.** Si aparece una referencia común estable, las diferencias pueden seguir existiendo dentro de ella.

## 9. Resultado de integración

**[T] Demostrado en modelos declarados:** recurrencia común ↔ razón racional de frecuencias para fases uniformes libres; una relación modular primitiva conserva una fase libre; el acoplamiento mínimo admite bloqueo estable bajo \(|\delta|<K\), incluso con frecuencias naturales inconmensurables; los radios sin acoplamiento no seleccionan ese bloqueo.

**[O] Propuesta ontológica compatible:** la forma es información propia de una estructura vorticial dentro de la trama del flujo; su compatibilidad con otra estructura depende de relaciones de módulo, circunstancia y estabilidad, sin que ninguna entidad «reconozca» o «decida».

**[A] No demostrado:** que todos los remolinos admitan una fase única; que su frecuencia material obedezca \(R\omega=v_*\); que una resonancia entera origine fusión de remolinos; que la gramática fundacional implique el acoplamiento concreto \(K\); que esto dé una cota a priori de vorticidad, regularidad global 3D o equivalencia física completa con Navier–Stokes.

**Decisión editorial:** suplemento autónomo, **no** canónico todavía y no incorporado a la Imagen Total.

## 10. Antecedentes internos consultados

- *Núcleo generativo canónico v0.1*: diferencia, comparación y residuo, complemento antes de ortogonalidad.
- *MF-43*: sincronización de modo y recurrencia; tiempo relacional sin segundos absolutos.
- *Ritmo, radio y relatividad relacional v0.1*: \(R_i\omega_i=v_*\) dentro de familia modal.
- *O25*: espejo como escala espectral extraída del flujo.
- *O26*: insuficiencia de una firma de momentos finitos para la evolución en familias de flujos.
- *O27*: descomposición tridimensional de vorticidad en amplitud y orientación perpendicular.
