# O2c — Selector relacional, recierre adaptativo y dependencia de la pregunta

**Programa:** Geometría Relacional · **Autor:** Le Matt Ansatz Di Ego  
**Versión:** 1.6 · **Fecha:** 13 de octubre de 2026  
**Estado:** realización computacional exacta en 3-coloración; selector heurístico, sin garantía universal de optimalidad ni complejidad polinómica.

## 1. Pregunta recuperada del hilo

Cada resolución acreditada cambia el mapa. La disposición de la información y la pregunta orientan qué cierre es pertinente. No se debe confundir:

- una respuesta que ya está fijada para `Q`;
- la existencia de alguna solución compatible;
- el costo de acreditar la respuesta;
- la elección de un orden de cálculo económico.

MF-24 y MF-63B ya expresaban la posibilidad de conservar interfaces suficientes y recomponerlas en nuevas cápsulas. O2c desarrolla una *implementación sectorial* y mide una regla de selección, no vuelve a presentarla como novedad ontológica.

## 2. Contrato exacto

Un grafo `G=(V,E)` define factores `c_u≠c_v` con `c_v∈{0,1,2}`. Para `B⊆V`, el objeto suficiente es:

\[
\Gamma_G(B)=\{b:\exists i,\;\bigwedge_{(u,v)\in E}c_u\ne c_v\}.
\]

Para una pregunta `Q` sobre las posiciones de `B`, la clase de respuestas es:

\[
A_Q(G)=\{Q(b):b\in\Gamma_G(B)\},\quad K_Q=|A_Q(G)|.
\]

`K_Q=0`: inconsistencia; `K_Q=1`: una respuesta acreditada; `K_Q>1`: pregunta indeterminada. La simple afirmación “hay una respuesta única” es insuficiente sin comprobar `Γ_G(B)≠∅`.

## 3. Transición dinámica y garantía de corrección

En el paso `k`, el mapa de factores `M_k` consta de tablas de compatibilidad acreditadas. Una política elige `v` entre los vértices todavía internos. El motor es siempre el mismo:

\[
F_{k+1}=\operatorname{Normalize}\bigg(
\bigl(F_k\setminus\{f:v\in\operatorname{scope}(f)\}\bigr)
\cup\Bigl\{\exists v\;\bigwedge_{f:v\in\operatorname{scope}(f)}f\Bigr\}
\bigg).
\]

Se permiten solamente simplificaciones exactas: eliminar tablas tautológicas, duplicados idénticos y detectar una tabla vacía. Para cualquier orden, la asociatividad y conmutatividad de la conjunción y de los cuantificadores existenciales dan:

\[
\boxed{\Gamma_{\mathrm{final}}(B)=\Gamma_G(B).}
\]

Por ello, la operación cambia la **representación de dependencias** y el costo de continuación, pero no la pregunta ni la respuesta del sistema inicial.

### Cambiar el sistema es una operación distinta

Agregar una arista `e` cambia `G` a `G+e`: en general puede cambiar `Γ` y la respuesta. El laboratorio también identifica un control donde se agrega una arista interna sin cambiar `Γ(B)`, aunque sí cambia el camino de cálculo. Esta equivalencia exterior se comprueba, no se presupone.

## 4. Comparador y política relacional

Ambas políticas se ejecutan en el **mismo motor**, con normalización idéntica y recálculo en cada etapa.

- **`min_fill` dinámico:** minimiza aristas de relleno no presentes entre vecinos, con desempate por grado e identificador; sólo usa ámbitos de los factores.
- **`relacional`:** además lee la cardinalidad de las tablas de compatibilidad de los factores actualmente acreditados y registra si la frontera calculada toca las variables de pregunta.

Para cada posible eliminación `v`, denotemos por `D_v` la unión de ámbitos de los factores que contienen `v` y por `F_v` esos factores. Se calcula una **estimación heurística**, no una probabilidad exacta:

\[
\widehat{s}_v=3^{|D_v|}\prod_{f\in F_v}\frac{|f|}{3^{|\operatorname{scope}(f)|}}.
\]

Con `q_v=|(D_v\setminus\{v\})\cap \operatorname{vars}(Q)|`, la política implementada ordena candidatos mediante:

\[
\boxed{\widehat{J}_v=\frac{\widehat{s}_v+0.30\cdot 3^{|D_v|}+0.50\min(3^{|D_v|-1},\widehat{s}_v)}{1+0.12q_v}.}
\]

Los coeficientes son parámetros declarados de un **prototipo**, no constantes derivadas del núcleo ontológico. Empates: menor relleno estructural, menor bolsa y menor identificador.

La estimación utiliza el producto de densidades de factores, que **no** es en general una estimación fiable de un conjunto de restricciones dependientes. Precisamente por eso el selector debe ser auditado frente a ejemplos adversariales. No consulta un solucionador, ni un oráculo global, ni la interfaz final para elegir el siguiente `v`.

## 5. Métricas y diseño experimental

- `total_candidates`: productos ternarios examinados realmente por el motor de proyección y el cierre de frontera (no incluye costo de selección).
- `scoring_factor_reads`: número de referencias a factores consultadas para construir la estimación relacional (tampoco es tiempo real).
- `normalization_checks`: tablas examinadas para descartar tautologías/duplicados; el número de entradas no se recorre explícitamente.
- `max_bag`: máxima bolsa local usada.
- `trace`: relaciones antes y después, nuevas y eliminadas, por cada cierre.

La comparación predefinida usa **35** instancias: caminos, escaleras, cuadrículas, gadgets y grafos aleatorios de semillas declaradas. Otras dos instancias favorables/adversariales son **testigos elegidos a posteriori** y se reportan fuera de la muestra principal. Dos controles adicionales examinan cómo cambia el camino frente a una arista añadida. No se mezclan en la estadística principal.

Importante: el O2 original conserva factores tautológicos; O2c los retira con normalización exacta. Por eso los conteos absolutos O2 y O2c **no son directamente comparables**. La comparación válida aquí es entre dos políticas con el mismo motor O2c.

## 6. Resultados reproducidos

| Conjunto | Casos | Relacional mejor | Igual | Relacional peor |
|---|---:|---:|---:|---:|
| Muestra predefinida | 35 | 0 | 33 | 2 |
| Testigos posseleccionados | 2 | 1 | 0 | 1 |

Testigo favorable *posseleccionado, satisfacible*: 792 candidatos con `min_fill` y 576 con el selector relacional (**27,3 % menos**, sin incluir la selección). Testigo adversarial *posseleccionado, satisfacible*: 3717 versus 5175 (**39,2 % más**).

### El mismo mapa cambia según la pregunta

En el control `mapa_base_Q01`, con idénticos factores de entrada:

| Pregunta | Respuestas | `K_Q` | Orden relacional |
|---|---|---:|---|
| `c0=c1` | `{False}` | 1 | `[5,3,4,6]` |
| `c1=c2` | `{False,True}` | 2 | `[4,3,5,6]` |

La interfaz exterior sigue siendo la misma; cambia qué es una *respuesta* y cuál es la prioridad del recorrido.

### Cambiar la disposición interna puede cambiar el camino sin cambiar la respuesta

`mapa_base_Q01` tiene `Γ(B)` de 18 asignaciones y recorrido `[5,3,4,6]` con 135 candidatos. Al incorporar la arista interna `(3,4)`, la interfaz continúa siendo **exactamente** esas mismas 18 asignaciones, pero el recorrido pasa a `[5,3,6,4]` y los candidatos a 243. Esto demuestra en el modelo que tener la misma información exterior no determina el costo interno de construirla.

## 7. Resultado negativo y siguiente obligación

**[DERIVADO en este algoritmo]** Cierre, proyección, normalización y recierre conservan exactamente el objeto `Γ(B)` y las respuestas `Q`.

**[OBSERVADO]** La pregunta y la disposición pueden modificar el camino; cambiar el camino puede modificar el costo, aun con respuesta idéntica.

**[NO-GO para la heurística O2c]** Una puntuación de densidades locales no basta para superar de modo sistemático a `min_fill` en la muestra; tampoco controla sus propios costos de selección.

**[ABIERTO]** Extraer del núcleo una función de **progreso acreditado** que no exija decidir la respuesta global de antemano, y demostrar un límite conjunto de costo de construcción de factores, selección, anchura, representación y acreditación para una clase de problemas explícita. Antes de P vs NP general, es razonable demostrarlo en clases de grafos con estructura acotada, luego contrastar con grafos generales.

La profundidad, el radio modal `r_V` y el radio físico del programa **no** se igualan con la densidad o el ancho de los factores sin un puente derivado. O2c no es una prueba de `P=NP` ni `P≠NP`.

## 8. Reproducción

```bash
python -m unittest discover -s tests -q
python experiments/laboratorio_selector_dinamico_o2c.py
```

Resultados en `results/o2c_selector_comparativa.csv`, `results/o2c_selector_detalle.json` y `results/O2C_RESULTADOS_SELECTOR_DINAMICO.md`.
