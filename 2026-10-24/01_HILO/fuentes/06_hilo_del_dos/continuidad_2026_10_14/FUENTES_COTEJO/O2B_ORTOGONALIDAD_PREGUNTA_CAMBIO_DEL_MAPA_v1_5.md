# O2b — Ortogonalidad informativa relativa a la pregunta y recierre dinámico

**Programa:** Geometría Relacional — Le Matt Ansatz Di Ego  
**Suplemento aditivo:** v1.5, 13 de octubre de 2026  
**Antecedentes conservados:** MF-24, MF-54, MF-63B; cápsulas O1–O1c; laboratorio O2 v1.4.  
**Método:** grafos y 3-coloración exacta sin traducir a SAT.  
**Estatus:** [DEFINICIÓN], [TEOREMA sectorial], [PRUEBA computacional], [NO-GO], [PUENTE ABIERTO]. No afirma que P=NP ni que P≠NP.

## 0. Enunciado del autor y obligación actual

> La solución cambia el camino; el camino depende del sistema y de la disposición de la información. Al cambiar el sistema, posibilidades antes distinguidas pueden convertirse en una sola respuesta. La información interna y la información de la pregunta pueden ser ortogonales.

Esto **no** se interpreta como independencia estadística ni como evidencia de que las direcciones ortogonales se puedan encontrar gratis. Se distingue el cambio del sistema físico/lógico de la recodificación correcta del *mismo* problema computacional.

## 1. Estado y respuesta

**[DEFINICIÓN]** Sea una arquitectura relacional finita `S`, con conjunto de configuraciones compatibles `Ω(S)`. Fijamos una pregunta `Q:Ω(S)→A`, donde `A` es el conjunto declarado de respuestas.

La relación de equivalencia y el cociente de respuesta son:

\[
 x\sim_Q y\iff Q(x)=Q(y),\qquad
 A_Q(S)=\{Q(x):x\in\Omega(S)\},\qquad
 K_Q(S)=|A_Q(S)|.
\]

- `K_Q=0`: inconsistencia: no hay ninguna configuración válida; **no** hay respuesta acreditada.
- `K_Q=1`: pregunta determinada, aunque existan muchas configuraciones.
- `K_Q>1`: incertidumbre respecto de `Q`.

No se confunde `|Ω(S)|`, `|I_B(S)|` (filas de frontera), ni `K_Q(S)`. En particular `K_Q=1` no implica `|Ω(S)|=1`.

**[TEOREMA O2b-1]** Si `Ω(S)` es no vacío, el cociente `Ω(S)/~Q` está en biyección con `A_Q(S)`. Prueba: las fibras no vacías de `Q` son las clases de equivalencia y cada clase posee una respuesta distinta. Este hecho es elemental y no se reivindica como nuevo teorema matemático.

## 2. Definición exacta de ortogonalidad

**[DEFINICIÓN]** Elegida una medida de probabilidad `μ` de soporte total sobre un `Ω` finito no vacío, tomamos el espacio de funciones reales:

\[
 \mathcal H=L^2(\Omega,\mu),\qquad
 \mathcal H_Q=\{g\circ Q:g:A_Q\to\mathbb R\}.
\]

La proyección ortogonal se realiza por esperanza condicional:

\[
 \boxed{P_Qf=\mathbb E_\mu[f\mid Q]},\qquad
 f=P_Qf+(f-P_Qf),\qquad
 f-P_Qf\perp \mathcal H_Q.
\]

**[TEOREMA O2b-2]** Para toda función `g` de la respuesta,

\[
 \langle f-P_Qf,g\circ Q\rangle_\mu=0.
\]

**Prueba.** Se descompone la suma sobre las fibras de `Q`; en cada fibra la suma ponderada del residual es cero por la definición de media condicional. Al ser `g(Q)` constante sobre la fibra, su producto integrado es cero. ∎

Con soporte total:

\[
 \dim\mathcal H=|\Omega|,\quad
 \dim\mathcal H_Q=K_Q,\quad
 \dim\mathcal H_Q^\perp=|\Omega|-K_Q.
\]

**Precauciones:** (i) estas dimensiones no son bits de memoria, radios ni costos de cálculo; (ii) ortogonalidad condicional **no implica independencia probabilística**; (iii) si `Ω=∅`, no se define medida uniforme ni esta proyección; (iv) para comparaciones no lineales/no probabilísticas, el cociente `~Q` sigue definido, pero la palabra *ortogonal* exige justificar una métrica o una medida.

## 3. Construcción en grafos y cambio de pregunta

Tomamos coloraciones propias de 3 colores de un grafo `G` y dejamos visibles los terminales `0,1,2`. Se realizan dos preguntas:

\[
 Q_{01}(c)=[c_0=c_1],\qquad Q_{12}(c)=[c_1=c_2].
\]

**[PRUEBA COMPUTACIONAL]** Los estados siguientes fueron calculados por eliminación exacta O2 y contrastados con un oráculo DFS independiente para los casos pequeños:

| Disposición | Coloraciones globales | Filas en frontera (0,1,2) | Respuestas posibles Q01 |
|---|---:|---:|---|
| Tres terminales libres | 27 | 27 | `{no,sí}` |
| Arista directa 0–1 | 18 | 18 | `{no}` |
| Cápsula de igualdad 0–1 | 18 | 9 | `{sí}` |
| Dos cápsulas de igualdad 0–1 y 1–2 | 12 | 3 | `{sí}` |
| Cápsula de igualdad más K4 independiente | 0 | 0 | `∅` (inconsistencia) |

El gadget de igualdad 0–1 tiene vértices auxiliares `3,4` y aristas `(3,4),(0,3),(0,4),(1,3),(1,4)`. Como `3` y `4` toman colores distintos, ambos terminales sólo pueden usar el tercer color.

**[FALSADOR DE CARDINALIDAD]** Los grafos de desigualdad y de igualdad tienen ambos **18 coloraciones globales**, pero sus respuestas son opuestas. El conteo no determina la relación.

**[FALSADOR DE CIERRE GLOBAL]** En el gadget de igualdad 0–1, `Q01` ya está resuelta mientras `Q12` continúa abierta `{no,sí}`. Una cápsula es suficiente en relación con una pregunta, no automáticamente con cualquier otra.

## 4. Muchos interiores, una respuesta

Agreguemos `k` triángulos independientes al gadget de igualdad. Cada triángulo aporta `3!=6` coloraciones:

\[
 \boxed{\lvert\Omega_k\rvert=18\cdot 6^k}\quad\text{y}\quad
 \boxed{A_{Q01}(S_k)=\{\mathrm{sí}\}},\qquad k\ge0.
\]

Esto es exacto por factorización de componentes desconectados; el laboratorio confirmó la fórmula enumerando `k=0,1,2`, no los `6^{12}` casos de `k=12`.

La interfaz visible sobre los terminales conserva 9 filas en toda la familia. Bajo el orden `min_fill` implementado en O2, los **candidatos de tablas examinados** satisfacen la igualdad empírica de esta familia:

\[
 \boxed{T_{\mathrm{O2}}(k)=135+39k}.
\]

Los datos se verificaron para `k∈{0,1,2,3,5,8,12}`. La fórmula se explica por la desconexión completa: cada nuevo triángulo se elimina con bolsas de tamaños 3, 2 y 1, añadiendo `27+9+3=39` candidatos. **No es un teorema de eficiencia para grafos arbitrarios.**

## 5. Proyección ortogonal verificada

Sobre los 27 estados del sistema libre se usa la medida uniforme y:

\[
 q(c)=1[c_0=c_1],\qquad f(c)=q(c)+1[c_2=0].
\]

El laboratorio obtiene exactamente:

\[
 \mathbb E[f\mid q=0]=\tfrac13,\quad
 \mathbb E[f\mid q=1]=\tfrac43,\quad
 \|f-P_qf\|_2^2=\tfrac29.
\]

Los residuos tienen media cero sobre cada fibra y, por ello, son ortogonales a toda función de `q`. La descomposición tiene dimensiones:

\[
 \dim\mathcal H=27,\quad \dim\mathcal H_q=2,\quad
 \dim\mathcal H_q^\perp=25.
\]

**[FALSADOR]** El residual `h(c)=(1+q(c))(1[c_2=0]-1/3)` también tiene media cero condicionada, pero `Var(h|q=1)=4 Var(h|q=0)`. Por tanto **ortogonalidad ≠ independencia estadística**.

## 6. Cambio del sistema y recierre del mismo problema no son lo mismo

**[DISTINCIÓN OPERACIONAL]**

1. **Transformación del sistema:** `S→S'` por agregar/quitar una relación. Su conjunto compatible `Ω(S')` y el conjunto de respuestas pueden cambiar realmente. Por ejemplo, agregar la arista `(0,1)` a los tres terminales libres fija `Q01=no`, mientras adjuntar el gadget de igualdad fija `Q01=sí`.
2. **Recierre de cálculo:** `R→R'` es una transformación de la *representación del mismo problema*. Debe preservar exactamente la respuesta original:

\[
 \boxed{A_Q(R')=A_Q(R)}
\]

para la interfaz de consulta declarada, así como la presencia/ausencia de realizaciones. No es válido cambiar la instancia para hacer que la respuesta se vuelva fácil y presentar eso como solución a la instancia anterior.

Cada cierre puede cambiar el grafo de dependencias del algoritmo y el conjunto de comparaciones inmediatamente útiles. Sin embargo, un cambio de representación no puede cambiar legítimamente qué respuesta tiene la instancia fija. El `min_fill` de O2 ya actualiza conexiones según el *fill-in*, pero no consulta aún la información **acreditada en las filas** para seleccionar dinámicamente el siguiente cierre.

## 7. NO-GO formal: `K_Q=1` no implica acreditación económica

**[TEOREMA O2b-3: barrera de decisión]** Sea `H` cualquier grafo de entrada. Construimos, en tiempo lineal, la unión disjunta `H ⊔ E`, donde `E` es el gadget de igualdad de los terminales `0,1` (con un tercer terminal libre). Definimos `Q(c)=[c_0=c_1]`.

- Si `H` es 3-coloreable, `Ω(H⊔E)` no está vacío y `A_Q(H⊔E)={sí}`; por tanto `K_Q=1`.
- Si `H` no es 3-coloreable, `Ω(H⊔E)=∅`; por tanto `K_Q=0`.

Como decidir 3-colorabilidad de un grafo general es NP-completo, **decidir si `K_Q=1` frente a `K_Q=0` en esta familia es NP-completo**. La pertenencia a NP se acredita exhibiendo una coloración válida de todo `H⊔E`.

Éste es un resultado elemental por reducción que ilustra una barrera ya conocida, no una separación de clases. Refuta el atajo:

\[
 \boxed{\text{una sola respuesta distinguible}\;\Longrightarrow\;\text{algoritmo polinómico}}\quad\text{(falso)}.
\]

La información relevante puede ser un solo bit, pero establecer que existe un estado compatible que lo sostiene puede seguir siendo difícil.

## 8. Integración con profundidad, radio e interfaces

El cociente por `Q` conserva exactamente la información necesaria para **distinguir respuestas**. No garantiza que el cociente pueda **construirse/consultarse** económicamente. Coincide con la separación previa MF-24/MF-54/MF-63B entre interfaz semántica e interfaz acreditable.

Conservamos los tipos de radio del núcleo: `r_V(h)=2^{-h}` es una realización binaria particular; no se deriva de aquí una igualdad entre `h`, `K_Q`, dimensión ortogonal, ancho de árbol y radio físico. Un eventual radio relativo a `Q` necesita un comparador y un costo de resolución acreditados, no únicamente un conteo escalar.

**[HIPÓTESIS OPERACIONAL PARA O2c]** Tras cada cierre `C_k` construido **sin un oráculo global** debemos actualizar la arquitectura acreditada:

\[
 (M_{k+1},D_{k+1})=\mathcal C(M_k,D_k;C_k),\qquad
 C_{k+1}=\pi_{\rm acr}(M_{k+1},D_{k+1},Q)
\]

y medir `tamaño de interfaz`, `anchura máxima`, `costo de acreditación`, `costo de selección`, `costo de actualización` y `profundidad`, manteniendo la equivalencia con el problema original.

**Discriminante O2c:** ¿una política local basada en relaciones acreditadas encuentra cierres cuya economía supera consistentemente `min_fill`, o existen familias adversariales donde debe explorar costes crecientes? No se presupone descenso universal de ninguna medida.

## 9. Reproducibilidad y tipado epistémico

- `experiments/laboratorio_ortogonalidad_o2b.py`: instancias, proyecciones y reportes.
- `tests/test_ortogonalidad_o2b.py`: 20 pruebas nuevas, oráculo DFS, controles por simetría, incompletitud y falsadores.
- `results/o2b_resultados_detalle.json`: datos, medias condicionales y controles.
- `results/o2b_ortogonalidad_comparativa.csv`: evolución de interfaz, respuesta y trabajo.
- `results/O2B_RESULTADOS_ORTOGONALIDAD.md`: resumen legible.

**Alcance:** resultados exactos dentro de 3-coloración de grafos pequeños y familias desacopladas, más un NO-GO estándar mediante reducción. No constituye solución a P versus NP, ni una ley física de masa, ni una regla universal de selección radial.
