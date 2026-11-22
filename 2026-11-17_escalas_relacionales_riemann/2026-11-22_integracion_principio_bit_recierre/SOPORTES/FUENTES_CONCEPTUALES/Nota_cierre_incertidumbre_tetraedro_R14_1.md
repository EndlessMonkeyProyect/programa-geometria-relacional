# Nota de continuidad — cierre, tetraedro e incertidumbre

**Programa de Geometría Relacional · 11 de octubre de 2026**  
**Tema:** ¿Resolver la incertidumbre y conservarla en una unidad cerrada son dos mecanismos, o dos aspectos del mismo?

## Resultado de la revisión

**La tesis de que son dos aspectos de un mismo cierre es coherente con el núcleo formal ya documentado, y tiene una realización matemática elemental.** No implica todavía que la geometría tetraédrica emerja necesariamente ni que exista un mecanismo físico de almacenamiento de información. Se distingue aquí una equivalencia formal **bajo un contrato de observación** de una derivación ontológica o física.

### 1. Lo que ya estaba en el programa

En *Cierre, localidad y escala relacional mínima* (3 de octubre), una firma de comparaciones acreditadas, \(\Phi_{\mathcal A}:\Omega\to K\), define la **cápsula**

\[
\mathcal C_{\mathcal A}(x)=\Phi_{\mathcal A}^{-1}(\Phi_{\mathcal A}(x)).
\]

La cápsula reúne realizaciones diferentes que aún no son distinguibles por esa familia de comparaciones. Hay incertidumbre relativa a \(\mathcal A\) si su cardinalidad excede uno. El **cierre relativo** significa que todas las comparaciones *admitidas* factorizan por la firma; no significa que toda diferencia concebible haya desaparecido. La **interfaz suficiente** de \(R(I,B)\) es \(\exists I\,R(I,B)\): basta para contestar la clase de preguntas exteriores declaradas, pero puede ser compatible con distintos interiores.

La *Fotografía de continuidad* del 5 de octubre reafirma: «cierre no significa terminación» e «identidad nueva = herencia + novedad». La nota *Economía y hilo* de R14.1 distingue residuo representacional, déficit frente a clases declaradas y refinamientos; confirma en un sistema sintético que cierre predictivo y estructura interna no son el mismo observable.

### 2. Un mismo cierre: resolución exterior, incertidumbre interior

Sea \(X\) una configuración interna y \(C=\Phi(X)\) la identidad cerrada disponible hacia afuera.

- **Resolución a la escala exterior:** se conoce \(C=c\). Las preguntas admitidas a través de \(\Phi\) quedan contestadas.
- **Incertidumbre a la escala interior:** todavía son compatibles las configuraciones en la fibra \(\Phi^{-1}(c)\).

Por ejemplo, si \(X\in\{x_1,x_2,x_3,x_4\}\) y \(\Phi(x_i)=c\) para las cuatro opciones, la unidad tiene una sola identidad exterior y cuatro alternativas internas no resueltas respecto de esa interfaz. Si hay probabilidades \(p\), la identidad exacta

\[
H(X)=H(C)+H(X\mid C)
\]

separa la información identificada por el cierre de la incertidumbre interna condicional. Si las cuatro alternativas internas son equiprobables y \(C\) está fijado, \(H(C)=0\) y \(H(X\mid C)=2\) bits. **Este ejemplo algebraico no prueba una estructura tetraédrica ni que la unidad almacene físicamente dos bits**: muestra solamente que tener identidad exterior determinada es compatible con indeterminación interior.

**Síntesis:** resolver y conservar pueden ser, respectivamente, la proyección exterior y la fibra interior de una misma operación de cierre.

### 3. El punto decisivo: indeterminado no significa almacenado

Hay dos modelos con la misma interfaz \(\Phi(x_1)=\Phi(x_2)=c\):

1. Una evolución \(F\) mantiene distintos \(F(x_1)\) y \(F(x_2)\) y una comparación admisible posterior puede separarlos. Hay un candidato a **residuo retenido y recuperable**.
2. Otra evolución colapsa ambos, \(F(x_1)=F(x_2)\). La misma identidad exterior persiste, pero la diferencia interna **se perdió**.

Por tanto, **el cociente por sí mismo no garantiza almacenamiento**. Una formulación contrastable exigiría al menos:

- **Cierre exterior dinámico:** \(\Phi(x)=\Phi(y)\Rightarrow\Phi(F(x))=\Phi(F(y))\), de modo que la evolución induce una dinámica coherente de las unidades cerradas.
- **Retención interior contrastable:** distinguir si \(F\) conserva información dentro de las fibras (por ejemplo, es inyectiva en la fibra relevante) o si las alternativas pueden recuperarse por nuevas comparaciones. La persistencia plena necesita especificar transformaciones y clases de preguntas.

Estos dos contratos son independientes: se puede tener cierre exterior con o sin conservación interna.

### 4. Radio, tres relaciones y tetraedro

Tu construcción propone una referencia y tres relaciones sujetas a un mismo radio relacional; con ello las posiciones relativas no quedan determinadas. Si se da una realización métrica con punto \(o\) y tres puntos \(p_i\) tales que \(\lVert p_i-o\rVert=r\), permanecen abiertos los ángulos y las distancias mutuas \(\lVert p_i-p_j\rVert\).

Los cuatro puntos forman un tetraedro **no degenerado** solo si los tres vectores \(p_i-o\) son linealmente independientes; sería **regular** solo con restricciones adicionales de aristas. Un radio común no basta para imponer ninguna de las dos propiedades. Además, este ejemplo usa espacio euclídeo como realización, no deriva el espacio desde la diferencia.

El programa tiene además una realización de **cierre orientado** \(J^4=I\), pero no se debe identificar automáticamente «cuatro fases», «cuatro vértices», \(\varepsilon=4\), cuatro bits o una longitud. *Cierre, localidad y escala relacional mínima* separa explícitamente esas nociones. La hipótesis a probar sería que un cierre relacional mínimo obliga, sin presuponer un espacio tridimensional, a una estructura de cuatro incidencias que admita realización tetraédrica no degenerada y luego una nueva interfaz suficiente.

### 5. Qué cambió y qué falta

**[DERIVADO bajo un contrato formal]** Puede coexistir identidad exterior resuelta e incertidumbre interior: fibras de una firma y, si se fija una distribución, la descomposición de entropía lo expresan rigurosamente.

**[CONDICIONAL]** La incertidumbre puede quedar **retenida** en una unidad recursiva si la dinámica conserva distinciones relevantes o permite su recuperación futura.

**[ABIERTO]** Que tres relaciones a radio común produzcan necesariamente el cierre tetraédrico; que \(\varepsilon=4\) surja del núcleo sin asumir geometría; que el cierre genere otra referencia independiente; que la incertidumbre retenida sea una magnitud física y no solo epistemológica.

**Prueba siguiente propuesta:** construir dos microdinámicas sobre el mismo cociente contextual, una con conservación interior y otra con pérdida interior; mostrar cuál es su firma bajo nuevas relaciones y qué axioma adicional seleccionaría la primera. En paralelo, aislar condiciones estrictamente relacionales que obliguen a un complejo de cuatro incidencias no degenerado. Recién después estudiar escalas y observables físicos.

## Fuentes cotejadas

- *Hilo_canonico_cierre_localidad_escala_relacional_v1.md* (3 de octubre de 2026): capítulos II, IV, V y VI; distinción explícita de \(C_4\) y radio.
- *FOTOGRAFIA_CONTINUIDAD_CHAT_GEOMETRIA_RELACIONAL_2026-10-05.md*: tesis de cierre persistente, herencia, residuo y nueva referencia.
- *Markdown pegado.md*: radio primo frente a radio de comparación, y condición adicional para \(C_4\times C_4\).
- *Relational_Geometry_Program_v3_1_R14_1_Incremental.zip*: `08_language/economia_y_hilo.es.md`, `08_language/falsador_cierre_interno.es.md` y `STATUS_CANONICAL.md`.

**Estado:** nota de integración conceptual; no modifica el repositorio ni afirma validación física, prueba de P vs NP, Yang–Mills o regularidad global de Navier–Stokes.
