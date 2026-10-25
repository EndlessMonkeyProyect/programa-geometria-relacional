---
title: "MF-104 — Peso de la novedad y transversalidad del recierre"
subtitle: "Un bit irreducible puede no tener peso mínimo: criterio exacto para la separación de la unidad"
author: "Le Matt Ansatz Di Ego · investigación formal asistida"
date: "2026-10-08"
version: "0.1 / rama complementaria MF-103"
status: "Teoremas exactos para recierres probabilísticos finitos y SU(2) algebraico; puente con Yang–Mills cuántico ABIERTO"
---

# MF-104 — Peso de la novedad y transversalidad del recierre

## 0. Pregunta de investigación

En la imagen del acordeón, una totalidad vale 1 mientras crece la profundidad interior. Cada burbuja puede contener comparaciones nuevas. Al recerrar, una parte interior puede ser sustituida por una referencia suficiente, sin que las consultas exteriores necesiten recorrer su historia.

La nueva tesis a **examinar**, no a suponer probada, es que el peso de una diferencia no es simplemente que exista un bit nuevo, sino **cuánto de su novedad queda irreducible cuando debe convivir con otras referencias y sostener nuevas comparaciones**.

La cuestión para Yang–Mills es si una composición no abeliana obliga una separación *cuantitativa* respecto de la referencia unitaria, bajo recierres sucesivos.

Conviene distinguir cuatro magnitudes:

1. **Unidad:** normalización de la totalidad, sin longitud ni masa asignada.
2. **Novedad lógica/contextual:** la nueva pregunta no factoriza por la interfaz anterior.
3. **Peso de novedad:** magnitud cuantitativa, dependiente de una medida, norma o costo previamente derivado.
4. **Gap físico:** infimum espectral del Hamiltoniano gauge-invariante relativo al vacío.

En particular, `bit` significa una alternativa binaria; **no significa automáticamente un bit completo de información condicional independiente**.

## 1. Cierre semántico existente: MF-86 y MF-97

MF-86 describe un normalizador de cápsulas `N_Q` con suficiencia, idempotencia y composición:

\[
N_Q^2=N_Q,
\qquad X\simeq_Q N_Q(X).
\]

MF-97 define equivalencia por todas las continuaciones permitidas:

\[
x\equiv_Q y \iff \forall c\in\mathcal C:\ Q(x\cdot c)=Q(y\cdot c).
\]

Estos son criterios precisos para sustituir una profundidad interior por una interfaz. No asignan automáticamente una geometría de Hilbert o un operador físico de transferencia.

En este módulo construiremos **una realización concreta auxiliar** con esperanzas condicionales. Es un modelo matemático de recierre, no la prueba de que todos los cierres semánticos tengan esta representación.

## 2. Modelo de dos burbujas: dos bits realmente distintos

Sea \(\Omega=\{(0,0),(0,1),(1,0),(1,1)\}\), con variables binarias \(X,Y\) y distribución, para \(0<\rho<1\),

\[
\mu_\rho(x,y)=
\begin{cases}
(1+\rho)/4,&x=y,\\
(1-\rho)/4,&x\ne y.
\end{cases}
\]

Las cuatro configuraciones tienen probabilidad estrictamente positiva. Las marginales de \(X\) y \(Y\) son uniformes. Por tanto **\(Y\) no puede reconstruirse como una función de \(X\)** ni viceversa: cada pregunta acredita una diferencia no absorbida completamente por la otra.

Sean \(P=\mathbb E[\,\cdot\mid X]\) y \(Q=\mathbb E[\,\cdot\mid Y]\) sobre \(\mathcal H=L^2(\Omega,\mu_\rho)\). Estos operadores son expectativas condicionales, luego:

\[
P^2=P,\quad Q^2=Q,\quad P^*=P,\quad Q^*=Q,
\quad P\mathbf1=Q\mathbf1=\mathbf1.
\]

Son recierres idempotentes auténticos en un espacio probabilístico, preservan positividad y la referencia \(\mathbf1\). Denotemos \(Z_X=(-1)^X\) y \(Z_Y=(-1)^Y\). Tienen media cero, norma 1 y

\[
\langle Z_X,Z_Y\rangle=\rho.
\]

Por simetría de la distribución,

\[
PZ_Y=\rho Z_X,\qquad QZ_X=\rho Z_Y.
\]

Definimos el **recierre alternado**:

\[
S_\rho=PQP.
\]

Entonces

\[
S_\rho\mathbf1=\mathbf1,
\quad S_\rho Z_X=\rho^2 Z_X.
\]

Los otros dos modos ortogonales a \(\operatorname{Ran}P=\operatorname{span}\{\mathbf1,Z_X\}\) quedan anulados. De este modo,

\[
\operatorname{Spec}(S_\rho)=\{1,\rho^2,0,0\}.
\]

El estado de referencia tiene valor 1 y es único si \(0<\rho<1\). El índice no trivial es \(q_\rho=\rho^2<1\), pero puede aproximarse arbitrariamente a 1 si \(\rho\uparrow1\), **aunque para cada \(\rho<1\) la diferencia contextual \(Y\) frente a \(X\) siga siendo real**.

### 2.1 Convertirlo en un operador de transferencia genuino

`S` tiene autovalores nulos; por sí solo no es la exponencial de un Hamiltoniano finito. Para evitar la identificación inválida, tomemos \(0<\epsilon<1\) y definamos

\[
T_{\rho,\epsilon}=\epsilon I+(1-\epsilon)S_\rho.
\]

`T` es un operador positivo, autoadjunto, invertible, preserva constantes y es positivo como operador de Markov. Posee exactamente los autovalores:

\[
\boxed{1,\quad \epsilon+(1-\epsilon)\rho^2,\quad\epsilon,\quad\epsilon.}
\]

Para cualquier parámetro de comparación \(\tau>0\),

\[
H_{\rho,\epsilon}:=-\frac{\hbar}{\tau}\log T_{\rho,\epsilon}
\]

es autoadjunto no negativo y verifica \(T=\exp(-\tau H/\hbar)\). Su separación positiva respecto del estado constante es exactamente

\[
\boxed{
\Delta_E(\rho,\epsilon)
=-\frac{\hbar}{\tau}\log\big[\epsilon+(1-\epsilon)\rho^2\big].
}
\]

**Teorema MF-104A — no-go de suficiencia semántica:** la idempotencia, la conservación de referencia, la no factorización de una nueva pregunta y una brecha positiva para cada realización finita **no implican una brecha uniforme entre realizaciones**.

**Prueba:** elegir \(\rho_n=1-2^{-n}\), con \(n=1,2,\dots\), deja todas las configuraciones posibles y mantiene las propiedades indicadas, pero

\[
q_n=\epsilon+(1-\epsilon)(1-2^{-n})^2\longrightarrow1,
\]

por lo que \(\Delta_E(n)\to0\). \(\square\)

Esta familia es un *modelo auxiliar probabilístico*, **no** un límite de retículas Wilson ni un contraejemplo a Yang–Mills cuántico.

## 3. El peso de la novedad sí puede calcularse, una vez fijado el contrato

El nuevo bit \(Y\) es no determinista respecto de \(X\), pero su peso cuantitativo depende de \(\rho\).

En este modelo, la parte de \(Z_Y\) irreducible por la primera interfaz es

\[
Z_Y-PZ_Y=Z_Y-\rho Z_X.
\]

Su magnitud cuadrática es

\[
\boxed{\eta(\rho):=\|Z_Y-PZ_Y\|_2^2=1-\rho^2.}
\]

Se cumple

\[
\boxed{q_\rho=1-\eta(\rho)}.
\]

Esta es una relación exacta entre *peso de nueva referencia* y *separación unitaria* **dentro de este modelo**, no una identidad universal del programa.

En términos informacionales, el bit \(Y\) tiene entropía de Shannon marginal de 1 bit, pero su información **nueva condicionada en \(X\)** es

\[
\boxed{H(Y\mid X)=h_2\!\left(\frac{1-\rho}{2}\right),}
\]

con \(h_2(p)=-p\log_2 p-(1-p)\log_2(1-p)\). Tiende a cero cuando \(\rho\uparrow1\). El suceso nuevo persiste; su costo informacional condicional puede desvanecerse.

**Lectura del acordeón:** profundizar no incrementa la unidad; una nueva burbuja puede ser distinguible, pero tras recierre puede quedar casi enteramente explicada por la referencia existente. `Una distinción` no fija `una cantidad universal de diferencia`.

### 3.0.1 La ortogonalidad que buscábamos

Como \(\rho=\langle Z_X,Z_Y\rangle\) para vectores unitarios, podemos escribir \(\rho=\cos\theta\). El peso de novedad se convierte en

\[
\boxed{\eta=\sin^2\theta,\qquad q_{\rho,\epsilon}=1-(1-\epsilon)\sin^2\theta.}
\]

- Si los dos bits son independientes y ortogonales (\(\theta=\pi/2\)), la novedad tiene peso cuadrático 1 y el índice del juguete es \(q=\epsilon\).
- Si son distintos pero casi paralelos (\(\theta\downarrow0\)), la novedad sigue siendo real y su peso tiende a 0.

**Ésta es una traducción precisa de los «ángulos» del autor, en esta realización.** Si la ontología exige ortogonalidad cuantitativa de todas las nuevas relaciones, hay que formular esa regla como hipótesis adicional y justificarla en la dinámica. Aun una ortogonalidad auxiliar perfecta no determina por sí sola la escala de tiempo ni el generador físico de Yang–Mills.

### 3.1 Números reproducibles

Para \(\epsilon=1/4\), \(\rho_n=1-2^{-n}\):

| Profundidad \(n\) | \(\rho_n\) | \(q_n\) | \(\tau\Delta_E/\hbar=-\log q_n\) | \(\eta_n\) |
|---:|---:|---:|---:|---:|
| 1 | 0.500000 | 0.437500 | 0.826679 | 0.750000 |
| 2 | 0.750000 | 0.671875 | 0.397683 | 0.437500 |
| 4 | 0.937500 | 0.909180 | 0.095213 | 0.121094 |
| 8 | 0.996094 | 0.994152 | 0.005865 | 0.007797 |
| 16 | 0.999985 | 0.999977 | 0.00002289 | 0.00003052 |

El script adjunto verifica las proyecciones, la simetría ponderada, los espectros y las identidades.

## 4. Teorema exacto que hace visible el mecanismo prometedor

Sea \(\mathcal H\) un espacio de Hilbert, con referencia unitaria \(\Omega\), y \(P,Q\) proyecciones ortogonales que preservan \(\Omega\). Definimos \(S=PQP\). Como \(S\) es positivo, en el subespacio ortogonal a la referencia:

\[
\|S|_{\Omega^\perp}\|
=\sup_{\substack{f\in\operatorname{Ran}P\cap\Omega^\perp\\\|f\|=1}}
\|Qf\|^2.
\]

Definamos la **transversalidad mínima** de las dos interfaces:

\[
\boxed{
\eta_*:=\inf_{\substack{f\in\operatorname{Ran}P\cap\Omega^\perp\\\|f\|=1}}
\|(I-Q)f\|^2.
}
\]

Para cualquier subespacio no vacío de prueba, el teorema de Pitágoras da

\[
\boxed{\|S|_{\Omega^\perp}\|=1-\eta_*.}
\]

[Si \(\operatorname{Ran}P\cap\Omega^\perp=\{0\}\), la norma excitada de \(S\) es cero por definición; el criterio se interpreta separadamente.]

**Teorema MF-104B — criterio de transversalidad:** si \(\eta_*>0\), el recierre alternado separa estrictamente la referencia 1 del resto de su espectro. Para la transferencia regularizada \(T=\epsilon I+(1-\epsilon)S\),

\[
\boxed{
q=1-(1-\epsilon)\eta_*,
\qquad \Delta_E=-\frac{\hbar}{\tau}\log\big(1-(1-\epsilon)\eta_*\big)>0.
}
\]

Si una familia de escalas satisface \(\eta_*(a,L)\ge \eta_0>0\) y \(\tau\) es tiempo físico fijo, obtiene una brecha uniforme **para esa familia de operadores**. La falta de separación en la familia anterior se explica precisamente por \(\eta_n\to0\).

**Este teorema no afirma que la transferencia física de Yang–Mills sea de la forma \(\epsilon I+(1-\epsilon)PQP\).** Demostrar o refutar una representación / comparación coerciva válida es una tarea distinta.

## 5. Control SU(2): el cierre no abeliano no tiene un peso algebraico mínimo

Para los dos ciclos de SU(2) construidos mediante matrices de Pauli,

\[
U_t=e^{it\sigma_x},\qquad V_t=e^{it\sigma_y},
\qquad 0<t\le\pi/2,
\]

consideremos el descriptor gauge-invariante bajo conjugación simultánea ya usado en el programa:

\[
\nu(U,V)=1-\tfrac12\operatorname{ReTr}(UVU^{-1}V^{-1}).
\]

El cálculo exacto da

\[
\boxed{\nu(U_t,V_t)=2\sin^4t.}
\]

Por tanto, para todo \(t>0\) pequeño, \(U_t,V_t\) son no conmutativos y \(\nu>0\), pero

\[
\boxed{\inf_{0<t\le\pi/2}\nu(U_t,V_t)=0.}
\]

En \(t=\pi/2\) aparece el valor máximo \(\nu=2\), correspondiente a la anticomutación extrema \(UVU^{-1}V^{-1}=-I\). Sin embargo, la continuidad del grupo permite novedades no abelianas arbitrariamente pequeñas cerca de la identidad.

**Teorema MF-104C — no-go de cuantización por conmutador solo:** `SU(2)` no abeliano, retorno cuaterniónico en configuraciones particulares y descriptor \(\nu>0\) no imponen un \(\nu_{\min}>0\) universal sobre todas las configuraciones no conmutativas.

**Límite de la conclusión:** \(\nu\) es un descriptor de holonomías, no el espectro del Hamiltoniano. Su falta de mínimo **no demuestra** que Yang–Mills físico sea gapless. Sólo impide identificar automáticamente no conmutatividad con un quantum fijo de masa o de costo.

## 6. Dónde podría tener razón la intuición ontológica

La nueva información que realmente necesitamos no es otro recuento de burbujas, sino una regla de **transversalidad física del recierre**:

- Dos referencias deben contener una diferencia que ninguna composición de interfaces físicamente admisible pueda atenuar arbitrariamente.
- La ley debe referirse a todas las excitaciones gauge-invariantes físicamente relevantes, no solo a un descriptor \(\nu\) o un subconjunto.
- La ley no puede nacer de asignar por definición a cada bit una masa mínima: debe seguirse de una medida o generador físico derivado de la teoría.
- La cota debe conservarse al variar tamaño de bloque, volumen espacial y espaciado del regulador, usando un tiempo físico fijo.
- La misma demostración **no debe generar gap para U(1)** en el régimen de Coulomb.

Aquí se abre una posibilidad coherente con el programa: el peso no sería un contenido almacenado en una burbuja aislada, sino el **mínimo residuo no absorbible por el recierre de sus relaciones**. El resultado relevante tendría que ser un límite inferior uniforme para ese residuo, en el sector físico correcto.

En la realización lineal finita esto es \(\eta_*\). En Yang–Mills será necesario definir el análogo gauge-invariante en términos de campos, transferencias físicas y correladores, y demostrar un puente entre ambos. Elegir \(\eta_*\) a posteriori para igualar un gap conocido sería circular.

## 7. Próxima prueba, formulada sin presumir su resultado

1. **Derivar las interfaces físicas:** escoger bloques de Wilson en 4D y un álgebra de observables gauge-invariantes locales. Definir dos contratos contiguos y su composición sin usar un Hamiltoniano cuya brecha se suponga.
2. **Demostrar una desigualdad local específica:** comparar el residuo de una perturbación gauge-invariante a través de ambos bloques. Identificar los términos de contorno y las variables conservadas que impiden una estimación trivial.
3. **Controlar la escala:** obtener una cota positiva en distancia física fija, o demostrar por qué la estrategia no puede lograrla. Una desigualdad en unidades de retícula que se desvanezca al tomar \(a\to0\) no sirve.
4. **Falsador abeliano:** repetir con U(1) en su régimen gapless y verificar que falla alguna hipótesis cuantitativa.
5. **Puente espectral:** sólo tras esos pasos, obtener \(\|T_\tau|_{\Omega^\perp}\|<1\) y aplicar MF-103. Construcción cuántica continua y volumen infinito permanecen requisitos independientes.

### Estado de lo conseguido

| Proposición | Estado |
|---|---|
| Cierre idempotente y nueva pregunta no factorizable | **Demostrados** en modelo finito de expectativas condicionales |
| Recierre alternado: espectro exacto y \(q\to1\) | **Demostrado** |
| Fórmula \(\eta=1-\rho^2\) como peso cuadrático condicional | **Demostrado**, depende del modelo |
| Transversalidad uniforme \(\eta_*>0\) implica gap del operador auxiliar | **Demostrado**, condicional a la hipótesis |
| SU(2) permite \(0<\nu\to0\) | **Demostrado** |
| Regla de pesos físicos de cada burbuja | **Abierta** |
| Deducción desde Wilson / Yang–Mills de transversalidad uniforme | **Abierta** |
| Existencia de Yang–Mills cuántico 4D y gap físico | **Abierta** |

**Conclusión:** el acordeón proporciona el vocabulario correcto para preguntar por profundidad, interfaces y novedad. Este módulo muestra por qué la novedad cualitativa no basta, pero también precisa una cantidad que sí podría llevar a una cota: **el residuo transversal que sobrevive al recierre**. La prioridad es encontrarlo y controlarlo directamente en la dinámica de Yang–Mills, no asignarlo por decreto.

## 8. Trazabilidad

- MF-69/70: herencia, generadores aritméticos y novedad dinámica versus novedad representacional.
- MF-86: normalización idempotente, suficiente y composicional.
- MF-97/98: interfaz contextual mínima y economía del reingreso.
- `ANEXO_EXCESO_DE_CIERRE_Y_NOVEDAD_RELACIONAL.md`: separación entre factor de extensión, profundidad y generador nuevo.
- `MF103_UNIDAD_INVERSA_Y_AISLAMIENTO_ESPECTRAL.md`: equivalencia \(q=e^{-\tau\Delta_E/\hbar}\).
- `RECIERRE_ENTRE_ESCALAS_Y_GAP_YANG_MILLS.md`: falsador continuo y contrato físico 4D.

**Reproducibilidad:** `50_experiments/mf104_controles.py`. No requiere datos experimentales ni calibración física; comprueba únicamente las identidades finitas y el cálculo SU(2) declarados.
