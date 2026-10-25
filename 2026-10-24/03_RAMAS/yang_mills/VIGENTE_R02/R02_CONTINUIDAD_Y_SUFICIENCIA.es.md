---
title: "R–02 — Lo que conserva la reflexión: identidad, composición y suficiencia entre escalas"
subtitle: "Formalización del puente R–01 hacia una geometría de lazos gauge-invariantes"
author: "Le Matt Ansatz Di Ego — Programa de Geometría Relacional"
date: "23 de octubre de 2026"
lang: es
geometry: margin=26mm
fontsize: 10pt
---

> **Alcance:** suplemento aditivo autónomo de R–01. Se prueba un conjunto de proposiciones sobre grupos de transporte, clases de conjugación y firmas de dos lazos `SU(2)`; se proponen interpretaciones ontológicas y un futuro puente físico. **No se afirma la solución de Yang–Mills en cuatro dimensiones ni de P vs NP o Navier–Stokes.**

**Convención de lectura:** [O] ontología y lenguaje del programa; [D] definición; [T] teorema bajo contrato; [F] contraejemplo; [H] hipótesis puente; [A] problema abierto. En todos los productos matriciales se actúa sobre vectores columna: un transporte de $a$ a $b$, seguido de uno de $b$ a $c$, se escribe $T_{bc}T_{ab}$.

# 1. Narrativa: la reflexión se sostiene en el resto

[O] La totalidad es su referencia de comparación. Una reflexión nueva constituye novedad cuando introduce una diferencia que la trama existente no podía distinguir. La nueva reflexión puede dividir las coincidencias anteriores, abrir un ámbito de contención interna y adquirir cierre propio. Lo anterior no se borra por cambiar de escala **si la referencia conserva las relaciones que lo acreditaban**. El foco significa convergencia de escalas bajo una referencia común; no una mirada exterior ni necesariamente un punto geométrico. Las distancias físicas no son la premisa ontológica: en el programa se investigan como comparaciones de radios.

La realización aritmética de R–01 usa una referencia $N$, un primo $p\nmid N$ y una ampliación $L=\operatorname{mcm}(N,p)=Np$. La nueva pregunta $x\bmod p$ divide cada clase $x\bmod N$ en $p$ clases; el par referencia/valor se conserva bajo el múltiplo normalizador. El **primo** tiene aquí un significado aritmético exacto: nuevo factor multiplicativo independiente relativo a $N$. No es una definición universal de la singularidad.

Lo que probamos a continuación es distinto: qué se conserva si las relaciones se **componen en un orden que importa**, como ocurre en el transporte gauge. La unidad de normalización no se traduce por decreto en $\operatorname{mcm}$ para matrices. Investigamos el lugar estructural de la referencia interna, su firma suficiente y su posible pérdida.

# 2. Cristal semántico mínimo [D]

| Concepto | Operación controlable | No equivale por sí solo a |
|:---|:---|:---|
| Referencia local | Elección de base $g_a$ en un nodo | Cambio físico de configuración |
| Camino | Composición ordenada de transportes $T_e$ | Suma de longitudes o trayectos indistintos |
| Convergencia | Dos caminos llegan a la misma referencia; su diferencia se compara | Igualdad de los transportes acumulados |
| Firma | Conjunto declarado de consultas gauge-invariantes | Toda la información física imaginable |
| Novedad | Una consulta que no factoriza por la firma antigua | Necesariamente un primo numérico |
| Cierre propio | Suficiencia, persistencia y actualización frente a continuaciones declaradas | Invariancia de forma, mera idempotencia |
| Refinamiento | Introducir referencias intermedias conservando transportes anteriores | Crear automáticamente nuevas diferencias |
| Bloqueo | Sustituir relaciones internas por un descriptor exterior | Preservación garantizada de la identidad interna |
| Brecha espectral | Separación positiva en espectro de operador físico | Un conmutador no nulo o una distinción lógica |

# 3. Primer teorema: cancelación de la referencia intermedia [T1]

Sea $G$ una red dirigida. Asignemos a cada arista $a\to b$ un transporte $T_{ab}\in SU(2)$. Cambiar la base de cada nodo por $g_a\in SU(2)$ induce:

$$
T'_{ab}=g_bT_{ab}g_a^{-1}.
$$

Para un camino $p=(a_0,a_1,\ldots,a_k)$, su transporte es

$$
T(p)=T_{a_{k-1}a_k}\cdots T_{a_0a_1}.
$$

**T1 (covariancia de caminos).** Cualquier cambio de referencias locales produce

$$
\boxed{T'(p)=g_{a_k}T(p)g_{a_0}^{-1}.}
$$

**Demostración.** Sustituir la expresión de cada arista da el producto de factores $g_{a_j}^{-1}g_{a_j}=I$ en todos los vértices intermedios; sólo quedan los extremos. $\square$

Si el camino se cierra en $o$, entonces $T'(p)=g_oT(p)g_o^{-1}$ y su traza es invariante. Dos lazos $U,V$ anclados en $o$ se conjugan simultáneamente por el mismo $g_o$. Esto establece una realización exacta de **independencia respecto de la descripción interna**, no una nueva ley física de continuidad temporal.

# 4. Segundo teorema: subdividir no obliga a crear novedad [T2]

Supongamos una arista con transporte $T$. Insertamos un nodo nuevo y elegimos $A\in SU(2)$:

$$
T_1=A,\qquad T_2=TA^{-1},\qquad T_2T_1=T.
$$

**T2 (refinamiento conservador).** Los observables de los caminos antiguos, calculados por el producto de aristas refinadas, se mantienen exactamente. Una transformación gauge arbitraria del nodo intermedio se cancela. Como el nodo nuevo sólo está unido a esas dos aristas, su $A$ puede eliminarse mediante una elección local de referencia; no constituye por sí solo una holonomía de lazo independiente.

**Demostración.** La igualdad $T_2T_1=T$ es inmediata. Tras cambios $g_0,h,g_2$ de las referencias en origen, nodo nuevo y destino,

$$
(g_2T_2h^{-1})(hT_1g_0^{-1})=g_2Tg_0^{-1}.
$$

No hay ciclo nuevo cuya traza revele información independiente. $\square$

**Lectura ontológica:** un múltiplo de representación puede ampliar la resolución sin introducir una reflexión genuinamente nueva. Ésta es la contraparte gauge de distinguir profundización de referencia frente a primo nuevo.

# 5. Tercer teorema: la firma suficiente de dos circuitos [T3]

Sean $U,V\in SU(2)$ dos holonomías de lazos con la misma base. La única libertad gauge residual es la conjugación simultánea $(U,V)\mapsto(gUg^{-1},gVg^{-1})$.

Definimos la firma

$$
\boxed{Q(U,V)=(x,y,z),\quad x=\tfrac12\operatorname{tr}U,\quad y=\tfrac12\operatorname{tr}V,\quad z=\tfrac12\operatorname{tr}(UV).}
$$

**T3 (suficiencia de la firma triple).** Dos pares de matrices $SU(2)$ tienen la misma firma $(x,y,z)$ **si y sólo si** son equivalentes por una misma conjugación $SU(2)$. En este dominio preciso, cualquier observable invariante bajo conjugación simultánea factoriza por $(x,y,z)$.

**Demostración.** Toda matriz $SU(2)$ se representa como un cuaternión unitario:

$$
U=xI+i\mathbf a\cdot\boldsymbol\sigma,\qquad V=yI+i\mathbf b\cdot\boldsymbol\sigma,
$$

con $|\mathbf a|^2=1-x^2$, $|\mathbf b|^2=1-y^2$, y $z=xy-\mathbf a\cdot\mathbf b$. Por tanto $(x,y,z)$ determina las normas de $\mathbf a,\mathbf b$ y su producto escalar: su **matriz de Gram**. Dos pares de vectores reales de dimensión tres con la misma Gram son relacionados por una rotación de $SO(3)$: cualquier isometría de su subespacio generado (dimensión a lo sumo dos) se prolonga a una rotación que preserve orientación en $\mathbb R^3$. La representación adjunta $SU(2)\to SO(3)$ realiza esa rotación mediante conjugación simultánea. La implicación inversa se obtiene por invariancia de trazas. $\square$

La región de firmas es

$$
-1\le x,y\le1,\qquad |z-xy|\le\sqrt{(1-x^2)(1-y^2)}.
$$

Tiene interior tridimensional; por eso, **genéricamente**, hacen falta tres parámetros reales independientes para describir continuamente estas clases gauge de dos lazos. Esto es dimensión del **espacio de comparaciones**; no una dimensión espacial nueva.

Un indicador de diferencia no abeliana es

$$
\nu(U,V)=1-\tfrac12\operatorname{tr}(UVU^{-1}V^{-1})
=\boxed{2(1-x^2-y^2-z^2+2xyz)}.
$$

Por tanto, $(x,y,z)$ es suficiente para reconstruir $\nu$; $(x,y)$ no lo es en general. Testigo: $U=i\sigma_z$ y las alternativas $V_1=i\sigma_z$, $V_2=i\sigma_x$ comparten $x=y=0$ pero producen $z=-1$ y $z=0$, respectivamente; $\nu_1=0$ y $\nu_2=2$.

**Procedencia matemática:** esta descripción de clases mediante trazas es una realización de identidades clásicas de caracteres de `SU(2)`, demostradas aquí para fijar el contrato del programa; no se reivindica como descubrimiento matemático previo desconocido.

**Interpretación:** la composición vuelve distinguible algo que antes era invisible al lenguaje de los dos radios aislados. La diferencia se acredita por la nueva pregunta $z$, no por atribuir un primo numérico a cada matriz.

# 6. Cuarto teorema: el bloqueo exterior puede destruir la información interna [T4/F1]

Consideremos el bloque que registra sólo el transporte total:

$$
B(U,V)=UV.
$$

Se trata de un mapa gauge-equivarante: $B(gUg^{-1},gVg^{-1})=gB(U,V)g^{-1}$.

**T4 (contraejemplo de suficiencia).** No existe una función $f$ del transporte acumulado $UV$ que reconstruya $\nu(U,V)$ para todos los pares.

**Demostración por testigo exacto.** Sean

$$
(U_1,V_1)=(i\sigma_x,i\sigma_y),\qquad
(U_2,V_2)=(I,-i\sigma_z).
$$

En ambos casos $U_jV_j=-i\sigma_z$. Sin embargo,

$$
\boxed{\nu(U_1,V_1)=2,\qquad \nu(U_2,V_2)=0.}
$$

Si existiera $f$, asignaría simultáneamente $2$ y $0$ al mismo argumento $-i\sigma_z$, contradicción. $\square$

**Resultado conceptual:** el cambio gauge no destruye los observables invariantes; el bloqueo no inyectivo **sí puede borrar** una diferencia acreditada. La igualdad de transporte exterior no garantiza la identidad de la contención interna. El criterio del programa «lo resuelto no se des-resuelve» exige un contrato de transporte que evite esta pérdida para las preguntas pertinentes.

# 7. Quinto teorema: una nueva reflexión sí puede dividir cada familia antigua [T5]

Conservemos dos lazos y su firma $Q(U,V)$, pero **agreguemos un nuevo lazo independiente** $S\in SU(2)$ con la misma referencia de base. Extendamos la firma:

$$
\widetilde Q(U,V,S)=(x,y,z,s),\qquad s=\tfrac12\operatorname{tr}S.
$$

**T5 (novedad no factorizable).** Ninguna función de $(x,y,z)$ reconstruye $s$ para todas las configuraciones triples. Para cualquier par antiguo $(U,V)$, su clase de firma admite valores distintos de $s$ sin alterar $(x,y,z)$.

**Demostración.** Mantener fijos $U,V$ y tomar $S=I$ o $S=-I$ deja $Q(U,V)$ inalterada mientras produce $s=1$ y $s=-1$. Incluso puede elegirse una familia continua $S(\theta)=e^{i\theta\sigma_z}$ con $s=\cos\theta$. $\square$

Ésta es una realización no abeliana de **refinamiento de distinciones**, análoga a la nueva pregunta modular de R–01. No afirma que el lazo nuevo aparezca físicamente de forma espontánea: el modelo declara su nuevo operador de comparación.

**Precisión sobre el primo.** En la aritmética modular un primo $p\nmid N$ divide cada clase en exactamente $p$ clases nuevas. En el laboratorio $SU(2)$ el nuevo lazo puede producir una familia **continua** de respuestas. No hay una función natural que identifique automáticamente cada nueva holonomía con un factor primo. Lo común es la **no-factorización de una nueva comparación**, no una igualdad universal entre números primos y grupos gauge.

# 8. Sexto teorema: qué significa conservar identidad bajo una dinámica [T6/F2]

Sea $X$ un espacio de configuraciones completas, $F:X\to X$ una actualización física o computacional admitida, y $Q:X\to Y$ una firma. Queremos una actualización cerrada sobre firmas $\widehat F:Q(X)\to Q(X)$ tal que

$$
\boxed{Q\circ F=\widehat F\circ Q.}
$$

**T6 (criterio exacto de suficiencia dinámica, recuperado del hilo O45/MF-97).** Tal $\widehat F$ existe si y sólo si

$$
Q(a)=Q(b)\implies Q(F(a))=Q(F(b))
\quad\text{para todo }a,b\in X.
$$

**Demostración.** La necesidad se obtiene aplicando $\widehat F$ a firmas iguales. Para la suficiencia se define $\widehat F(Q(a))=Q(F(a))$; la implicación garantiza independencia del representante. $\square$

**F2 (contraejemplo incluso con gauge-covariancia).** Ampliemos el estado a $(U,V,S)$, pero sigamos observando sólo la firma anterior $Q(U,V)$. Declaramos la actualización

$$
F(U,V,S)=(US,V,S).
$$

Esta regla conmuta con la conjugación simultánea, por lo que es gauge-covariante como **actualización abstracta**. Sin embargo, desde estados $(I,I,I)$ y $(I,I,-I)$, ambos con la misma firma antigua $(1,1,1)$, pasamos a firmas $(1,1,1)$ y $(-1,1,-1)$. La firma anterior no permite actualizar su propio futuro: perdió una relación interior relevante.

En consecuencia, la completitud de $(x,y,z)$ para los **dos lazos aislados** no implica suficiencia para un mundo con lazos adicionales o continuaciones que dependan de ellos.

# 9. Séptimo teorema: criterio de no pérdida al cambiar de escala [T7]

Supongamos un mapa de refinamiento $J:X\to X'$ y firmas $Q:X\to Y$, $Q':X'\to Y'$. Sea $C=Q'\circ J$ la firma que observamos después del refinamiento.

**T7 (criterio de preservación de respuestas).** Existe una recuperación $P:C(X)\to Q(X)$ tal que

$$
\boxed{Q=P\circ Q'\circ J}
$$

si y sólo si $C(a)=C(b)$ implica $Q(a)=Q(b)$ para todos los estados iniciales.

**Prueba.** Si existe $P$, la implicación es inmediata. Recíprocamente, asignar $P(C(a))=Q(a)$ está bien definido exactamente por esa implicación. $\square$

El teorema separa tres nociones: (i) gauge-equivariancia del mapa; (ii) conservación de observables **declarados**; (iii) suficiencia dinámica de esa firma para posteriores continuaciones. Ninguna implica automáticamente las otras. Para preservar **todas** las diferencias gauge de un modelo de dos lazos basta conservar una firma equivalente a $(x,y,z)$; para un sistema físico mayor hace falta un contrato más rico.

**Corolario.** La subdivisión conservadora de T2 preserva todas las respuestas de lazos antiguos. El bloqueo $B(U,V)=UV$ del T4 no preserva $\nu$; la condición de T7 falla. Éste es el límite exacto de la afirmación «lo resuelto no se des-resuelve» dentro de estos modelos.

# 10. Octavo resultado: por qué todavía no hay brecha de Yang–Mills [F3]

La invariancia gauge, la existencia de firmas suficientes y el carácter no abeliano de $SU(2)$ son condiciones **algebraicas**. Una brecha física exige una afirmación adicional sobre el espectro de un operador dinámico.

Tómese un espacio de dos estados con un vacío unitario $\Omega$ y un operador auxiliar $H_0$ de espectro $\{0,1\}$. Para cada escala declarada $a>0$ considérese $H_a=aH_0$. Los estados y sus comparaciones no cambian; la brecha auxiliar es $\Delta_a=a>0$ pero

$$
\boxed{\lim_{a\to0}\Delta_a=0.}
$$

Su transferencia relativa satisface $T_{\tau,a}=e^{-\tau H_a/\hbar}$ y la norma excitada $q_{\tau,a}=e^{-\tau a/\hbar}\to1$. Éste es un contraejemplo **lógico**, no una configuración ni un límite de Yang–Mills real: prueba que la autorreferencia y la conservación de identidades no fijan por sí mismas el **peso espectral** de las excitaciones.

La rama YM-R3A del programa construyó un análogo más cercano al grupo $SU(2)^2$: un comparador con brecha finita fija y una dinámica $H_a$ con brecha tendente a cero. MF-103 estableció la equivalencia $\Delta>0\iff q_\tau<1$ bajo las hipótesis espectrales del Hamiltoniano; MF-104 demostró que la novedad cuantitativa puede tender a cero sin perder distinción lógica.

**Aún faltan:** derivar una acción/medida y dinámica físicas de Yang–Mills, obtener un transporte de escalas compatible con observables gauge-invariantes y un control espectral positivo **uniforme en unidades físicas**, construir el límite cuántico no trivial 4D y verificar controles abelianos (especialmente $U(1)$ Coulomb). El experimento de este suplemento no cumple esas obligaciones.

# 11. Resultado del laboratorio reproducible [E]

El archivo `verificar_r02.py` comprueba con aritmética simbólica las dos configuraciones del T4; hace los controles CRT para $N=6,p=5,L=30$; y ensaya $1\,200$ configuraciones aleatorias de $SU(2)$ con cambios gauge independientes, subdivisión de aristas, invariancia de la firma triple y fórmula del conmutador.

**Ejecución:** `python verificar_r02.py`. El JSON `resultados_r02.json` conserva semilla, número de ensayos, error máximo y casos adversariales.

Los teoremas T1–T7 están demostrados en este texto por argumentos generales bajo sus contratos; los ensayos confirman implementaciones específicas. **Ni el conteo de ensayos ni el error numérico certifican una teoría de campos continua.**

# 12. Interpretación y siguiente discriminante [O/H/A]

La respuesta a la pregunta «¿qué información no puede perderse?» depende de la operación:

1. **Cambio de referencias locales:** no se pierden trazas de lazos ni funciones de clases gauge; T1.
2. **Subdivisión sin ciclos nuevos:** puede conservarse exactamente lo acreditado; T2.
3. **Nueva reflexión/lazo independiente:** la antigua firma ya no responde todas las preguntas; T5.
4. **Bloqueo de varios recorridos a uno:** puede borrarse una diferencia interna físicamente distinguible en el modelo; T4.
5. **Evolución con relaciones ocultas:** la firma necesita incluir lo que influye en las futuras respuestas; T6.

**Propuesta R–03.** Aplicar esta distinción a la primera red euclídea mínima de lazos Wilson $SU(2)$ con dos plaquetas que comparten base: escoger lazos originales, introducir un mapa de bloqueo $a\to2a$, identificar qué parte de la firma triple sobrevive y qué parte se vuelve invisible, y contrastarlo con un operador/medida derivados de la acción Wilson (no de un Hamiltoniano elegido a posteriori). Repetir el control con $U(1)$ para impedir inferencias espurias. Medir por separado **suficiencia de la interfaz** y **desigualdad dinámica de escala**.

**Balance:** el programa dispone ya de un teorema de composición gauge, un resultado de suficiencia exacta para dos ciclos $SU(2)$, un testigo inequívoco de pérdida de novedad bajo bloqueo y una condición formal necesaria y suficiente de preservación entre escalas. **Eso constituye un puente algebraico comprobable con la ontología; no demuestra aún la brecha física de Yang–Mills.**

---

## Fuentes internas y continuidad

- R–01: `R01_PUENTE_NORMALIZACION_AUTORREFERENCIA_YM.es.md` (23 oct. 2026), incluido sin modificaciones.
- YM–01 y YM–02, fuentes formales (23 oct. 2026).
- O40, O59, O60, O92; MF-69, MF-86, MF-97; O45, criterio de suficiencia dinámica.
- `RAMA_YM_RESCATE_ACTUALIZACION_2026-10-22.md`, identificación de la celda de dos ciclos, la gramiana y fronteras T3b–T5.
- MF-103, `MF103_UNIDAD_INVERSA_Y_AISLAMIENTO_ESPECTRAL.md`, y MF-104, `MF104_PESO_DE_NOVEDAD_Y_TRANSVERSALIDAD.md`.

**Regla de integración:** este suplemento es **aditivo y falsable**. Conservar documentos previos, lenguaje ontológico, pruebas y contradictores; no atribuir a una analogía aritmética una nueva demostración física sin un puente independiente.
