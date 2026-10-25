# O2 — Cápsulas en grafos: interfaz contextual, radio y costo de construcción

**Programa:** Geometría Relacional — Le Matt Ansatz Di Ego  
**Fecha:** 2026-10-13  
**Versión:** v1.4, suplemento **aditivo** a O1c v1.3  
**Alcance:** problema de **3-coloración de grafos** por eliminación exacta de vértices (sin traducción a SAT). Prueba computacional de instancias finitas; no demostración de P=NP ni de P≠NP.

## 1. Qué retomamos, sin reinventarlo

El antecedente **MF-34A/B** había demostrado que, para la consulta de existencia de continuación interna, la interfaz obligada por todos los contextos de frontera es

\[
\boxed{\mathcal I_B(R)=\exists I\,R(I,B).}
\]

MF-34C ya había separado contenido conservado de orden de eliminación: \(\exists x\exists y R=\exists y\exists x R\), aunque el costo del cálculo cambie. Por eso, O2 **no atribuye como novedad** el teorema de interfaz ni esta conmutatividad. O1c aporta una instancia aritmética de misma continuidad futura bajo el mismo valor; O2 prueba la misma pregunta en relaciones combinatorias cuyo costo puede crecer de modo distinto.

## 2. Formalización directa mediante grafos

Sea \(G=(V,E)\) no dirigido y \(q=3\) el número de colores. Escribimos \(c_v\in\{0,1,2\}\). Una coloración válida es una asignación que verifica

\[
R_G(c_V)=\bigwedge_{\{u,v\}\in E} [c_u\ne c_v].
\]

Seleccionamos una frontera \(B\subseteq V\) y el interior \(I=V\setminus B\). La cápsula observacional es

\[
\boxed{\mathcal I_B(G)=\{b\in\{0,1,2\}^B:\exists i\in\{0,1,2\}^I, R_G(i,b)\}.}
\]

Para cualquier contexto exterior \(Z(B,W)\) que únicamente consulte la frontera, dos grafos interiores son intercambiables si y sólo si tienen la misma relación \(\mathcal I_B\) (MF-34A). Esto no implica que tengan el mismo costo interno ni la misma historia constructiva.

### Eliminación exacta

En una etapa con variable interior \(v\), combinamos todos los factores \(F_j\) en que aparece \(v\), y publicamos

\[
T(N)=\exists c_v\,\bigwedge_{j:\,v\in\mathrm{scope}(F_j)}F_j.
\]

La nueva relación se almacena como tabla de asignaciones compatibles de \(N\). Se continúa hasta eliminar todo \(I\). El programa implementa directamente las tablas de incompatibilidad de cada arista y la proyección de variables; **no llama a un solucionador SAT ni codifica CNF**.

## 3. Métricas tipadas: no confundir cardinalidad, radio y dificultad

Para una etapa \(t\), sea \(b_t\) el número de variables que aparecen en la unión de los factores consumidos, incluyendo \(v\). Para la ejecución concreta medimos:

\[
\begin{split}
w&=\max_t b_t,\\
C_{\mathrm{cand}}&=3^{|B|}+\sum_t3^{b_t},\\
M_{\mathrm{filas}}&=\max_t|T_t|,\\
K_B&=|\mathcal I_B(G)|.
\end{split}
\]

- \(C_{\mathrm{cand}}\) es el número **exacto de asignaciones candidatas enumeradas por este laboratorio**, no una cota inferior necesaria para otros algoritmos.
- \(M_{\mathrm{filas}}\) cuantifica las filas de la tabla individual más grande; no incluye todas las tablas vivas ni estructuras auxiliares.
- \(K_B\) es la cantidad de asignaciones exteriores compatibles, no el costo para calcularlas.
- Para esta representación tabular, \(C_{\mathrm{cand}}\le (|I|+1)3^{\max(w,|B|)}\). Por tanto, ancho de bolsa acotado implica costo polinómico en el número de vértices, **sólo para familias y órdenes que mantienen el ancho acotado**.

La relación con el radio binario **ya formalizado en el programa**, \(r_V=2^{-h}\), se conserva tipada: aquí no hemos identificado \(h\) ontológico con \(w\). Si se quiere comparar sólo escalas computacionales, se puede definir **como proxy explícito**, no como ley derivada,

\[
 h^{\mathrm{trabajo}}=w\log_2 3,\qquad
 r^{\mathrm{trabajo}}=2^{-h^{\mathrm{trabajo}}}=3^{-w}.
\]

Es una reexpresión de la capacidad de enumeración de una bolsa, no un radio geométrico ni una predicción independiente. **No debe presentarse como demostración de la fórmula radial del programa para grafos**.

## 4. Resultados reproducibles

Frontera usada en caminos, escaleras y cuadrículas: dos vértices extremos, con tres colores. Las dos políticas de eliminación son `min_fill` (minimizar nuevas conexiones entre vecinos en cada paso) y `reverse` (orden numérico descendente de los vértices interiores). La tabla reporta conteos deterministas de asignaciones examinadas, no tiempos de máquina.

| Grafo | Vértices | K de frontera | Bolsa máx. (`min_fill` / `reverse`) | Candidatos (`min_fill` / `reverse`) |
|---|---:|---:|---:|---:|
| Camino | 16 | 9 | 3 / 3 | 387 / 387 |
| Escalera 2×8 | 16 | 9 | 4 / 9 | 981 / 59 031 |
| Cuadrícula 4×4 | 16 | 9 | 5 / 6 | 1 791 / 6 111 |
| Cuadrícula 5×5 | 25 | 9 | 7 / 7 | 9 324 / 33 570 |
| Camino | 48 | 9 | 3 / 3 | 1 251 / 1 251 |

**Observación O2-A:** la escalera con dieciséis vértices conserva *exactamente* la misma interfaz (9 pares de colores) con dos trayectorias. El orden descendente enumera 59 031 candidatos frente a 981 con `min_fill`, una razón de aproximadamente **60,17**. Bajo esta implementación, el costo de construir la cápsula depende de la trayectoria, no exclusivamente de la información final conservada.

**Observación O2-B:** caminos de 8 a 48 vértices mantienen bolsa máxima 3 y crecimiento lineal del conteo de candidatos. Esto es **compatible** con teoría clásica de ancho arbóreo acotado; no es un algoritmo polinómico para todos los grafos.

**Observación O2-C:** en los grafos de estas familias, \(K_B=9\) para ambas esquinas seleccionadas. Una interfaz exterior idéntica no predice por sí misma el costo de construirla.

## 5. Control adversarial: el escalar radial no basta

Tomemos frontera \(B=(0,1,2)\). Introducimos dos vértices internos \(a,b\) conectados entre sí. Para cualquier pareja de frontera \((u,v)\), conectamos tanto \(a\) como \(b\) con \(u\) y \(v\). Con tres colores, \(a\ne b\) y los dos colores internos quedan prohibidos en \(u\) y \(v\). Por tanto

\[
\mathcal I_B(G_{01})=\{(x,y,z):x=y\},\qquad
\mathcal I_B(G_{12})=\{(x,y,z):y=z\}.
\]

Ambos grafos poseen 5 vértices, 5 aristas, una frontera de tres vértices y \(K_B=9\). Sin embargo,

\[
\mathcal I_B(G_{01})\ne\mathcal I_B(G_{12}).
\]

Por ejemplo, \((0,0,1)\) es compatible con \(G_{01}\), pero incompatible con \(G_{12}\). La comparación conserva su capacidad discriminante aunque el número total de continuaciones sea igual.

**Resultado:** la sola cardinalidad de la interfaz, y cualquier \(r=f(K_B,|B|)\), es insuficiente como identidad relacional exacta. Este control favorece conservar primero **la relación** antes de proponer un escalar que la resuma. No prueba que toda noción de radio sea insuficiente: podría codificar otros invariantes que aún no se han derivado.

## 6. Verificación y falsadores

- Las 26 instancias del banco experimental, con ambas políticas, se exportan en `results/o2_grafos_detalle.json` y `results/o2_grafos_comparativa.csv`.
- Se verifica la igualdad exacta de interfaces para órdenes distintos y la coincidencia con oráculos independientes: búsqueda por fuerza bruta en grafos pequeños y retroceso de coloreado en cuadrículas más grandes.
- `K4` proporciona una obstrucción inequívoca a la 3-coloración: interfaz vacía, tanto si el borde sólo consulta dos vértices como si existen vértices adicionales aislados.
- Se comprueba la simetría de renombrar los tres colores.
- **Falsador metodológico:** inferir igualdad de interfaces porque coincide \(K_B\) falla en los gadgets \(G_{01},G_{12}\).
- **Falsador de una noción de costo basada sólo en \(K_B\):** la escalera 2×8 exhibe la misma interfaz con costos muy distintos según el orden.

### Predicción sectorial contrastable

Si una familia de grafos tiene una política que logra mantener \(w\le w_0\) constante, el número de candidatos del laboratorio crece a lo sumo linealmente en \(|I|\), multiplicado por \(3^{w_0}\), para frontera fija. Si \(w\) aumenta, esta **realización tabular** pierde esa garantía. Esto no establece una cota inferior para todos los algoritmos: puede haber representaciones comprimidas, simetrías o técnicas adicionales.

### Estado frente a P versus NP

3-coloración de grafos generales es un problema NP-completo. Por ello **sería suficiente** exhibir para *todos* los grafos un algoritmo exacto polinómico, con construcción y consulta incluidas, para obtener \(P=NP\). No lo hemos obtenido. Mostrar crecimiento exponencial en un orden malo o una familia tampoco demuestra \(P\ne NP\).

El avance exacto de O2 es **operacional**: separa tamaño de la interfaz, contenido de la interfaz, ancho de las relaciones intermedias y costo de la trayectoria; permite someter a contraste hipótesis del programa sin confundirlas.

## 7. Enlace con la pregunta sobre números primos

Un mapa de divisibilidad es otra posible realización del mismo enfoque: un número como nodo, divisores y relaciones modulares como incidencias, y una interfaz que responda «¿existe divisor propio?» o «¿qué residuos son compatibles?». Pero hay dos precauciones:

1. **Determinar si un número es primo ya pertenece a P**; resolver primalidad no implica resolver P versus NP.
2. La factorización entera es distinta de primalidad. Una visualización de residuos puede ayudar a proponer una interfaz, pero se debe contar el costo de **construirla a partir de los dígitos del número**, no sólo el de consultarla ya construida.

El ensayo de primos requerirá un contrato independiente (entrada binaria \(n\), conjunto de consultas permitidas y costo medido en \(\log_2 n\) bits). No importaremos el radio ni el ancho de grafos coloreados sin una transformación matemática acreditada.

## 8. Próxima obligación O2b

Definir una política de *selección del próximo cierre* usando sólo información local y comparar su costo con `min_fill` sobre familias estructuralmente difíciles. Distinguir:

- \(S\): tamaño de un resumen exacto de frontera;
- \(C\): costo verificable para construirlo;
- \(U\): costo para actualizarlo ante una relación nueva;
- \(Q\): costo para responder la consulta exterior.

Una verdadera predicción P vs NP requiere garantías uniformes para \(C,U,Q\), no sólo compresión de \(S\) una vez calculada.

## 9. Reproducción

Desde la raíz del paquete, Python estándar, sin dependencias externas:

```bash
python -m unittest discover -s tests -q
python experiments/laboratorio_grafos_o2.py
```

Los experimentos miden el **algoritmo implementado**; no acreditan novedad frente a la literatura clásica de eliminación de variables, programación dinámica en descomposiciones arbóreas ni complejidad parametrizada.
