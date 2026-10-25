# Programa de Geometría Relacional — Nodos numéricos como convergencia de caminos

**Le Matt Ansatz Di Ego · suplemento aditivo candidato v0.1 · 22 octubre 2026**

**Método:** narrativa → ontología → lenguaje → contrato matemático → pruebas existentes → controles nuevos → programa P versus NP.  
**Estado:** síntesis y formalización de un puente, no reemplaza a MF-86/97/99, CR-6, E11/E19/E25/E26, O58–O60 ni la Imagen Total v3.8.1.

## 0. La precisión ontológica que gobierna el ensayo [O]

> «Cada número nuevo que aparece es un nodo de caminos para llegar a él como soluciones donde convergen estructuras».

No se parte de los números como etiquetas sucesivas: se parte de una trama de posibles relaciones. Una nueva distinción habilita caminos; algunas continuaciones permanecen abiertas, otras resultan incompatibles y otras confluyen en un mismo cierre de comparación. El nodo emergente es una referencia que puede sostener nuevas relaciones.

La incertidumbre no es azar. Lo que no ha quedado distinguido puede seguir compatible en el interior de una unidad. El **radio relacional** es un intento de *cuantificar*, una vez adoptada una escala de comparación, la extensión de la diferencia abierta; no se introduce como una longitud primordial ni se lo iguala por definición al número de recorridos.

La palabra **número** puede apuntar a papeles diferentes: (i) valor o cardinal visible, (ii) identificador de un nodo, (iii) normalizador de una nueva escala, (iv) cantidad de caminos que confluyen, (v) dimensión/cantidad de libertades. La tesis ontológica que se investiga busca una regla generativa que los conecte cuando corresponde; no se permite sustituir uno por otro por similitud de vocabulario.

## 1. Lenguaje operativo [D]

| Término | Significado bajo un contrato de comparación |
|---|---|
| **Camino** | Historia finita de operaciones de reflexión/comparación, con procedencia conservable. |
| **Marco** | Reglas admitidas de comparación, transformación y composición. |
| **Convergencia de valor** | Dos caminos producen el mismo valor numérico: `ν(γ₁)=ν(γ₂)`. |
| **Convergencia de cierre** | Las continuaciones admitidas no distinguen las respuestas relevantes de ambos caminos. |
| **Nodo** | Clase de caminos/estados respecto del cierre escogido, con una firma que permita responder o actualizar lo pertinente. |
| **Novedad** | Distinción que no factoriza por la firma anterior y obliga a refinarla, o nuevo operador que cambia el marco. |
| **Normalizador** | Referencia explícita bajo la que se conserva una relación; no equivale necesariamente al valor del nodo. |
| **Radio** | Cuantificación de extensión de incertidumbre tras declarar comparador y métrica/probabilidad; no nombre de una cardinalidad. |
| **Procedencia** | Registro o certificado que permite reconstruir una historia cuando esas consultas se consideran admisibles. |

**Dos expresiones que NO son equivalentes:** «dos caminos terminan en el número 4» y «esos dos caminos son sustituibles para todo encuentro posterior autorizado». La segunda exige una prueba de suficiencia.

## 2. Genealogía de resultados ya establecidos [R: no redemostrados como novedad]

1. **MF-86.** Un normalizador contextual ha de ser suficiente, idempotente y composicional: `N_Q(N_Q(K))=N_Q(K)` y `N_Q(N_Q(K) ⋈ C) ≃_Q N_Q(K ⋈ C)` bajo el contrato.
2. **MF-97 / MF-99.** `x≡_Q y` si todas las continuaciones admisibles responden igual. El cociente es estable bajo la acción de esas continuaciones; una operación adicional `J` desciende al cociente únicamente si la equivalencia es congruencia también para `J`.
3. **CR-6 / MF-34.** Para un módulo `H(i,b)` y continuaciones que solo consultan la frontera `b`, la firma existencial `Γ_H(b)=∃_i H(i,b)` es suficiente para existencia. La tabla `Q_H(b)=Σ_i H(i,b)` es el contrato apropiado para conteos de interiores separables. Igual cardinalidad global no equivale a igual interfaz; costo de eliminación condicionado por ancho, no automáticamente polinómico.
4. **E11.** En XOR, enlaces que conectan componentes reducen libertad; enlaces internos ya implicados preservan el cierre; conflictos producen cero soluciones. Un representante con paridades reemplaza numerosos recorridos.
5. **E19.** Ampliar preguntas refina clases; las nuevas comparaciones no destruyen los hechos acreditados, pero pueden revelar distinciones que antes no se necesitaban. Una firma pequeña en tamaño semántico no garantiza evaluación eficiente.
6. **E25.** Paridad par e impar en tres bits: igual proyección por pares, información ternaria distinta; no se debe confundir convergencia aparente con cierre suficiente.
7. **E26.** El testigo «diamante» certifica igualdades para 3-coloración, pero hay instancias globalmente incompatibles sin testigos de esa clase.
8. **O59.** El cubo ideal de espejos organiza infinitas posiciones de imágenes en órbitas, reconocibles mediante firma plegada `I_L`; una órbita puede ser cerrada sin cubrir el espacio.
9. **O58/O60.** La referencia normalizadora y el múltiplo transportan representaciones entre escalas. Las rutas `3→9`, `3→51`, `3→99` no son todas iguales frente a la regla adicional de «ocupación sin borrado». Una misma referencia no elige por sí sola la siguiente rama.
10. **Radio y pseudoinversa (11 sep).** Bajo comparador lineal `C`, modelo gaussiano de máxima entropía y presupuesto declarado, `Σ=β⁻¹(C†C)^+` y `R_i²=1/(βλ_i)` sobre el espacio distinguible. No es una ley universal de cardinalidades ni de la física.

## 3. Contrato formal para el nodo [D]

Sean `H` las historias finitas admitidas por el marco, `C` un monoide de continuaciones admisibles que actúa por la derecha, y `Q` la respuesta que necesitamos conservar. Definimos (como en MF-97):

\[
\gamma_1\equiv_Q\gamma_2
\quad\Longleftrightarrow\quad
Q(\gamma_1\cdot c)=Q(\gamma_2\cdot c)
\text{ para toda }c\in C.
\]

El **nodo contextual** es `[γ]_Q`. Una etiqueta de número `ν([γ]_Q)` puede asignársele si el contrato la define, pero la igualdad `ν(γ₁)=ν(γ₂)` no es por sí sola suficiente para concluir `γ₁≡_Qγ₂`.

Para guardar simultáneamente la idea del programa y la trazabilidad del cálculo, proponemos una *ficha tipada* (no se impone que siempre se almacene explícitamente):

\[
\boxed{\mathfrak N_Q=(\nu,\,\sigma_Q,\,\lambda,\,\rho,\,\pi).}
\]

- `ν`: valor/código cardinal que representa la convergencia bajo una regla generativa todavía por derivar;
- `σ_Q`: firma suficiente respecto de las preguntas permitidas;
- `λ`: referencia y múltiplo normalizadores cuando existan (`valor/referencia`, no solo resto);
- `ρ`: radio o medida de incertidumbre **solo** si se proporciona una construcción métrica válida;
- `π`: procedencia/certificado de los caminos, si habrá preguntas futuras sobre ellos.

Los cinco campos son papeles distintos. No se obtiene gratuitamente uno a partir de los demás. Una interfaz puramente existencial puede omitir `π`; una interfaz de reconstrucción de historias no puede omitirlo sin justificar cómo recuperarla. La memoria/costo de una procedencia explícita puede ser exponencial si se exige listar todo.

### Teorema C1 — Sustitución por un nodo [T, recuperado de MF-97]

Si `γ₁≡_Qγ₂`, entonces, para cualquier continuación admitida `c`, `γ₁c≡_Qγ₂c`. Por tanto, la transición sobre clases `[γ]·c=[γc]` está bien definida.

**Prueba.** Dada toda continuación `d`, `Q(γ₁cd)=Q(γ₂cd)` porque `cd` sigue siendo una continuación admisible. Así `γ₁c≡_Qγ₂c`. ∎

**Límite:** esto acredita la legitimidad semántica de fusionar caminos, no la eficiencia de descubrir sus clases en un problema dado.

### Teorema C2 — Novedad que separa un nodo [T, recuperado de E19]

Sea `σ` una firma previamente suficiente para las preguntas `Q`, y sea `q` una nueva pregunta. Si existen caminos `γ₁,γ₂` con `σ(γ₁)=σ(γ₂)` y `q(γ₁)≠q(γ₂)`, no existe ningún decodificador `f` con `q=f∘σ` en todas las historias. La antigua firma debe refinarse (o la pregunta declararse exterior al contrato).

**Prueba.** Si `q=f∘σ`, la igualdad de firmas obligaría igualdad de respuestas; contradicción. ∎

No implica que el antiguo cierre fuese falso; era suficiente para otra familia de preguntas.

## 4. Un modelo numérico ejecutable de convergencia [T/E, realización restringida]

Considérese cada camino de `n` reflexiones binarias codificadas `0/1`, y adoptemos como única pregunta futura la **suma de las marcas**. Las historias pueden diferir en el orden, pero convergen en el mismo entero `k` si contienen exactamente `k` unos.

Existen `2^n` recorridos y solamente `n+1` valores finales `k=0,…,n`. La cantidad de caminos que confluyen en `k` es

\[
\boxed{m_n(k)=\binom nk.}
\]

La regla de continuación está cerrada:

\[
\boxed{k\overset{0}{\longmapsto}k,\qquad k\overset{1}{\longmapsto}k+1.}
\]

Así, no hace falta enumerar todas las historias para contar sus familias. La recurrencia `m_{n+1}(k)=m_n(k)+m_n(k-1)` produce las multiplicidades en `O(n²)` sumas de enteros de a lo sumo `O(n)` bits.

Con `n=18` el control ejecutado obtuvo **262.144 caminos**, **19 nodos finales de suma**, y multiplicidades binomiales exactas. Es una convergencia de valores y también un cierre respecto de **todas las continuaciones que solamente añaden marcas y consultan su suma**.

**Falsador inmediato:** los caminos `01` y `10` confluyen en el valor `1`, pero la pregunta «¿qué marca apareció primero?» los distingue. Si esa pregunta se admite, `1` deja de ser un nodo suficiente por sí solo. Es la diferencia entre número de salida, referencia estructural y memoria de procedencia.

Esto conecta ontología y matemática sin atribuir a la realidad la obligación de usar sumas binarias como mecanismo originario.

## 5. Falsador conjunto de E25: un mismo número, dos cierres incompatibles [T/E]

Sean los conjuntos de ternas binarias

\[
E=\{(x,y,z):x\oplus y\oplus z=0\},\qquad
O=\{(x,y,z):x\oplus y\oplus z=1\}.
\]

Ambos poseen cuatro realizaciones y la misma proyección sobre **cada pareja**. Pero `E∩O=∅`. Frente a la continuación que impone paridad par, `E` conserva soluciones y `O` no.

Así:

\[
|E|=|O|=4,\qquad \forall i<j:\pi_{ij}(E)=\pi_{ij}(O),
\qquad E\cap O=\varnothing.
\]

**Conclusión exacta:** el valor `4`, ni siquiera acompañado por todas las relaciones binarias marginales, garantiza un nodo común respecto de preguntas ternarias. Esta prueba ya existía en E25; aquí se aplica explícitamente a la lectura emergente de números.

## 6. Radio cuantificado: prueba de invariancia necesaria [N, observación derivada del modelo de septiembre]

En el contrato gaussiano del programa, `G=C†C`, `Σ=β⁻¹G⁺` y `R_i=1/sqrt(βλ_i)`.

Tómese un espacio real de una coordenada. Si `C₁=[1]`, entonces `G₁=1`. Si registramos **dos veces la misma comparación exacta**, `C₂=[1;1]`, entonces `G₂=2`. Bajo **el mismo β**, se obtiene

\[
R_1=\frac1{\sqrt\beta},\qquad R_2=\frac1{\sqrt{2\beta}}.
\]

Ambos comparadores distinguen exactamente los mismos pares de estados y tienen el mismo núcleo `{0}`, pero sus radios gaussianos brutos difieren.

**Teorema C3 (no invariancia bajo repetición, para ese contrato).** La fórmula `R²∝(C†C)^+` no define por sí sola un radio que dependa únicamente de las clases de indistinguibilidad: repetir una fila no nula del comparador altera en general `G`, sus autovalores y el radio, sin añadir distinción semántica.

**Prueba.** El caso escalar anterior es un contraejemplo exacto. ∎

Este resultado no invalida la derivación por máxima entropía: ese modelo trata la duplicación como **mayor peso o rigidez de la medición**, y eso puede ser útil si realmente hay dos observaciones independientes con significado físico. Sí impide equiparar automáticamente radio espectral y número de caminos sin fijar qué cuenta como diferencia independiente. La posible corrección es **definir el radio sobre clases de comparaciones independientes o un comparador ponderado invariantemente**, y luego justificar cómo se eligen los pesos; no basta anunciar la equivalencia.

## 7. P frente a NP: obligación exacta [A]

El programa investiga la posibilidad de reconocer nodos comunes sin recorrer todos los caminos. La demostración restringida en sumas y en XOR no decide complejidad para grafos arbitrarios. Una vía hacia `P=NP` requiere que, para un problema NP-completo natural como **3-coloración de grafos**, exista un procedimiento determinista uniforme que:

1. Construya o descubra los nodos y sus relaciones necesarias **desde el grafo dado**, no desde una tabla de soluciones precalculadas.
2. Preserve la respuesta de existencia bajo todas las continuaciones que su procedimiento introduce, incluidos conflictos de aridad superior.
3. Acredite fusiones y contradicciones tanto en instancias con solución como sin ella.
4. Mantenga polinómico el **costo conjunto** de identificar nodos, construir firmas, combinarlas, buscar testigos, refinar, actualizar, almacenar, consultar y certificar la respuesta.
5. No presuponga que el número de clases, el tamaño de sus firmas o la facilidad de calcularlas son polinómicos.

La ruta «directa por vínculos» de v3.8.1 aporta certificados positivos y negativos eficientes para **alcanzabilidad en grafos explícitos**, una clase que ya está en P. No traslada automáticamente esa facilidad a relaciones generales ni a espacios implícitos exponenciales.

### Tres preguntas que no deben colapsarse

- **¿Convergen?** Dos caminos son equivalentes para las continuaciones autorizadas.
- **¿Podemos reconocerlo eficientemente?** El test de equivalencia y la construcción de la firma tienen costo polinómico.
- **¿Cuántos nodos hacen falta?** Puede haber demasiadas clases aunque cada comparación local sea barata.

La unión de las tres exigencias —corrección, descubrimiento económico y representación económica— es el desafío real hacia P vs NP.

## 8. Resultado de la revisión [síntesis]

**Resuelto bajo contratos declarados:** convergencia contextual estable (MF-97); normalizador idempotente (MF-86); interfaz suficiente por frontera (CR-6); caminos XOR y testigos locales (E11/E26); convergencia numérica aditiva con multiplicidades binomiales; contraejemplo ternario; y no invariancia del radio gaussiano ante duplicaciones de medición.

**Abierto:** una ley ontológica y aritmética que seleccione **qué nuevo número** debe aparecer como nodo de convergencia más allá de una etiqueta elegida, y que determine cuándo los distintos caminos son realmente el mismo cierre estructural. La línea P=NP requiere, además, prueba universal de corrección y cotas polinómicas completas. La teoría física del radio requiere puente independiente.

**Propuesta de siguiente experimento discriminante:** grafos de 3-coloración sin diamantes, con igual cardinalidad aparente de ramas locales y diferencia ternaria/global. Medir número de nodos verdaderamente suficientes, ancho efectivo de su interfaz y costo de descubrirlos; comparar contra eliminación exacta y contra una descripción por conteos. No cambiar la ontología para acomodar el resultado.

## 9. Reproducción

```bash
python3 verificar_convergencia.py
```

El script crea `resultados_verificacion.json` y ejecuta **11 comprobaciones** de convergencia por suma, estabilidad bajo sufijos, refinamiento por pregunta nueva, firma del espejo con fracciones exactas, paridad ternaria, traza E11, invarianza radial fallida y transporte aritmético exacto. Son controles matemáticos finitos; no experimentos ópticos físicos ni una prueba de P=NP.

### Fuentes internas cotejadas

- `MF86_AUTORREFERENCIA_IDEMPOTENCIA_NORMALIZACION_v0_1.md`
- `17_LENGUAJE_VIVO_SINTESIS_CANONICA.md` (MF-97/MF-99)
- `CR6_Economia_Herencia_2026-10-16.docx`
- `01_E11_FORMALIZACION_RELACIONAL_POR_GRAFOS.es.md`
- `01_E19_FORMALIZACION.es.md`
- `01_GRAFOS_IMAGEN_TOTAL.es.md` (E25/E26 y límites)
- `O59_AUTORREFERENCIA_Y_SECTORES.es.md`
- `O58_FORMALIZACION.es.md` / `O60_FORMALIZACION.es.md`
- `incertidumbre_radio_pseudoinversa_v0_1.md`
- `P_VINCULOS_Y_CERTIFICADOS.md` de la Imagen Total v3.8.1.

**Proveniencia:** todas las referencias a demostraciones anteriores son recuperaciones de esos trabajos, no nuevos descubrimientos adjudicados a este suplemento. Las comprobaciones nuevas y la aplicación a la noción de «número como nodo» están declaradas como tales.
