# MF-34 — Invariante contextual, multiplicidad interna y carga de transferencia

**Versión:** v0.41-research  
**Estado:** teoremas exactos para relaciones booleanas finitas + verificación exhaustiva/aleatoria.  
**Alcance:** contrato existencial de interfaz. No deriva momento físico, no establece una medida universal de complejidad y no resuelve `P vs NP`.

---

## 1. Pregunta

MF-33 dejó abierta una pregunta común a los frentes físico y computacional:

> ¿qué debe conservarse cuando una referencia cambia de soporte?

La primera corrección de MF-34 es conceptual: el objeto conservado no tiene por qué ser inicialmente un escalar. Antes de buscar una magnitud numérica hay que identificar el **contenido relacional que ningún contexto futuro puede dejar de distinguir**.

Sea una relación finita

\[
R(I,B),
\]

donde `I` son variables internas y `B` es la frontera accesible al exterior.

Definimos el **invariante contextual existencial**

\[
\boxed{
\mathcal I_B(R):=\exists I\,R(I,B).
}
\]

Es exactamente la relación de frontera que indica qué circunstancias `B` admiten alguna continuación interna.

---

## 2. Equivalencia contextual

Sean dos realizaciones internas `R(I,B)` y `S(J,B)` con la misma frontera `B`.

Definimos

\[
R\simeq_B S
\]

si para todo contexto exterior `Z(B,W)` producen exactamente la misma respuesta existencial:

\[
\exists I,B\,[R(I,B)\land Z(B,W)]
\iff
\exists J,B\,[S(J,B)\land Z(B,W)]
\]

para toda asignación de `W`.

La relación `\simeq_B` identifica implementaciones internas que ningún futuro permitido por la interfaz puede distinguir.

---

## 3. Teorema MF-34A — completitud del invariante contextual

Para cualesquiera `R(I,B)` y `S(J,B)`:

\[
\boxed{
R\simeq_B S
\iff
\mathcal I_B(R)=\mathcal I_B(S).
}
\]

### Prueba

Si

\[
\mathcal I_B(R)=\mathcal I_B(S),
\]

entonces para cualquier `Z(B,W)`:

\[
\exists I,B[R\land Z]
=
\exists B[\mathcal I_B(R)\land Z]
=
\exists B[\mathcal I_B(S)\land Z]
=
\exists J,B[S\land Z].
\]

Recíprocamente, suponga que los invariantes difieren. Existe entonces alguna asignación `b*` de la frontera perteneciente a la diferencia simétrica. Elija como contexto `Z_{b*}` el predicado que acepta únicamente esa asignación. Ese contexto distingue inmediatamente `R` de `S`, contradiciendo `R\simeq_BS`.

Por tanto ambos criterios son equivalentes. ∎

### Lectura

El objeto que debe conservarse bajo el contrato existencial no es una descripción particular de la historia interna. Es la **clase de equivalencia contextual**, representada de manera canónica por

\[
\mathcal I_B(R)=\exists I R.
\]

---

## 4. Teorema MF-34B — unicidad del resumen exacto

Suponga que un predicado `S(B)` pretende reemplazar exactamente a `R(I,B)` frente a **todos** los contextos futuros sobre `B`:

\[
\exists I,B[R\land Z]
\iff
\exists B[S\land Z]
\qquad\forall Z.
\]

Entonces necesariamente

\[
\boxed{S(B)\equiv\mathcal I_B(R).}
\]

La prueba vuelve a usar contextos singleton. Si `S` difiriera de `\mathcal I_B(R)` en una sola asignación de frontera, esa asignación construiría un contexto que los separa.

Esto da un sentido preciso a la frase **“lo que debe conservarse”**: dentro de este contrato, el contenido semántico de frontera no es una elección del normalizador. Está forzado por todas las continuaciones futuras que se desea preservar.

---

## 5. Conservación y cambio de soporte

Una transformación interna

\[
R(I,B)\longrightarrow R'(I',B)
\]

es una transferencia exacta respecto de la frontera si

\[
\boxed{
\mathcal I_B(R)=\mathcal I_B(R').
}
\]

La representación interna, el número de variables, la factorización y la sintaxis pueden cambiar. El invariante contextual no.

Éste es el objeto conservado por MF-33 cuando

\[
R(A,x)\land S(x,B)
\longrightarrow
T(A,B)=\exists x[R\land S].
\]

La referencia `x` cambia de soporte, pero la clase de consecuencias externas permanece.

---

## 6. Teorema MF-34C — el orden de liberación no altera el invariante final

Sean `X` y `Y` conjuntos disjuntos de variables internas. Entonces

\[
\boxed{
\exists X\exists Y\,R
=
\exists Y\exists X\,R.
}
\]

Por inducción, cualquier permutación de las variables internas produce la misma relación final sobre la frontera.

Por tanto:

\[
\boxed{
\text{el orden puede cambiar el costo sin cambiar el contenido conservado.}
}
\]

Esta separación explica el resultado de MF-32: `min_scope`, `natural` y `reverse` pueden recorrer representaciones intermedias de tamaños radicalmente distintos y, sin embargo, terminar en la misma semántica proyectada.

Así, la sensibilidad al orden pertenece a la **economía de la trayectoria**, no a la identidad del resultado.

---

## 7. Multiplicidad interna de un mismo invariante

La economía ontológica puede cuantificarse, en un sentido limitado y exacto, contando cuántas realizaciones internas distintas tienen el mismo invariante externo.

Sean `k` variables internas booleanas. Para cada asignación `b` de la frontera, la fibra interna

\[
R_b\subseteq\{0,1\}^k
\]

puede ser cualquier subconjunto de las `2^k` configuraciones internas.

Si

\[
\mathcal I_B(R)(b)=0,
\]

la única fibra compatible es la vacía.

Si

\[
\mathcal I_B(R)(b)=1,
\]

la fibra puede ser cualquier subconjunto no vacío, es decir existen

\[
2^{2^k}-1
\]

posibilidades.

Si el soporte del invariante contiene `s` asignaciones de frontera, el número exacto de relaciones internas que proyectan al mismo invariante es

\[
\boxed{
M_k(\mathcal I)=\left(2^{2^k}-1\right)^s.
}
\]

### Ejemplos verificados

Para `k=1` y tres variables de frontera, el invariante total (`s=8`) representa una clase de

\[
3^8=6561
\]

relaciones internas diferentes.

Para `k=2` y dos variables de frontera, la clase del invariante total contiene

\[
15^4=50625
\]

relaciones internas.

Esto formaliza una idea importante:

\[
\boxed{
\text{muchas diferencias internas pueden ser irrelevantes para toda consecuencia futura accesible desde una interfaz.}
}
\]

No se destruyen “absolutamente”; quedan identificadas por el contrato de observación elegido.

---

## 8. Conservación semántica no implica compresión computacional

MF-34 también produce un límite que conviene registrar.

Con `b=|B|` variables booleanas existen

\[
2^{2^b}
\]

relaciones posibles de frontera.

Por simple conteo, cualquier codificación **inyectiva de longitud fija** capaz de representar todas ellas necesita en el peor caso al menos

\[
\boxed{2^b\text{ bits}.}
\]

Así, no puede existir una representación universal de tamaño `poly(b)` para **todas** las relaciones booleanas arbitrarias sobre una frontera de tamaño `b`.

Esto no prueba nada por sí solo sobre `P vs NP`, porque la cota relevante allí debe medirse respecto del tamaño de la fórmula de entrada, y las relaciones de frontera que aparecen como proyecciones de entradas pequeñas constituyen una subfamilia estructurada.

Sí falsifica una versión demasiado fuerte de la esperanza:

> “toda relación de frontera admite siempre una descripción polinómica sólo en el número de variables de frontera”.

No es cierto en general.

La ruta computacional debe explotar estructura heredada del problema de entrada y controlar el costo respecto de `|F|`, no sólo respecto de `|B|`.

---

## 9. El objeto conservado no es todavía una cantidad física

El invariante

\[
\mathcal I_B(R)
\]

es una **relación**, no un escalar ni un vector con unidades físicas.

Esto corrige la búsqueda de MF-33: antes de encontrar una “cantidad conservada” tipo momento, el programa ya dispone de un objeto semántico conservado bajo cambio de soporte.

Pero para obtener una ley física hace falta un paso adicional.

Debe encontrarse una valoración

\[
\mu:\mathcal I\longrightarrow G
\]

hacia algún espacio de magnitudes `G` que posea la estructura apropiada —por ejemplo aditividad, orientación, unidades y regla de composición— y demostrar que la dinámica relacional preserva `\mu` por necesidad de la arquitectura.

Sólo entonces tendría sentido contrastar si

\[
\mu\leftrightarrow p
\]

u otra cantidad física conocida.

Por tanto:

\[
\boxed{
\text{invariante contextual}
\neq
\text{momento físico}
}
\]

pero el primero ofrece un lugar matemático preciso desde el cual buscar el segundo.

---

## 10. Nueva lectura de fuerza

MF-33 propuso como conjetura que una fuerza puede ser una dinámica de redistribución entre cierres y circunstancias.

MF-34 permite refinarla:

1. una interacción puede reorganizar la realización interna;
2. una transferencia exacta debe conservar el invariante contextual del contrato correspondiente;
3. una conservación física adicional requerirá una valoración `\mu` que sea estable bajo esa dinámica;
4. la fuerza correspondería a la ley de cambio de distribución de esa magnitud, no al invariante contextual desnudo.

Esquemáticamente:

\[
R\longrightarrow R',
\qquad
\mathcal I_B(R)=\mathcal I_B(R'),
\]

mientras una distribución interna

\[
(q_A,q_B,q_{AB})
\]

puede cambiar conservando una valoración total aún por derivar.

---

## 11. Consecuencia para el frente NP

El resultado semántico ya no es el cuello de botella.

Para una secuencia de eliminaciones, el invariante final es único y no depende del orden. Lo abierto es construirlo sin atravesar representaciones intermedias demasiado costosas.

La pregunta queda separada en tres niveles:

\[
\boxed{
\text{qué debe conservarse}
}
\]

—resuelto por `\mathcal I_B` dentro del contrato declarado—;

\[
\boxed{
\text{cómo representarlo económicamente}
}
\]

—abierto—;

\[
\boxed{
\text{cómo escoger eficientemente la trayectoria económica}
}
\]

—abierto—.

Para 3-SAT todavía se necesita demostrar, respecto del tamaño original `|F|`, una familia uniforme de representaciones y un selector que mantengan tamaño, actualización y `Empty` bajo cotas polinómicas.

`P vs NP` permanece **OPEN**.

---

## 12. Verificación reproducible

El script

`experiments/foundations/mf34_contextual_invariant.py`

verifica:

1. **equivalencia contextual exhaustiva** para una variable interna y dos de frontera:
   - 65.536 pares de relaciones;
   - 16 contextos por par;
   - 0 fallos;
   - todo par con invariantes distintos posee un contexto singleton testigo;
2. **fórmula de multiplicidad**:
   - `k=1, b=3`: 65.536 relaciones, 256 invariantes, 0 fallos;
   - `k=2, b=2`: 65.536 relaciones, 16 invariantes, 0 fallos;
3. **independencia del orden**:
   - 200 relaciones aleatorias con cuatro variables internas y tres de frontera;
   - 24 órdenes por relación;
   - 4.800 comparaciones;
   - 0 fallos.

La prueba de los teoremas no depende de la enumeración; los experimentos auditan la implementación.

---

## 13. Qué queda abierto después de MF-34

### MF-35A — valoración conservativa

Encontrar una función no trivial

\[
\mu(\mathcal I,\text{cierre},\text{dirección})
\]

con estructura composicional cuya conservación se derive y no se imponga.

### MF-35B — carga de transferencia independiente

Definir una medida de cuánta **estructura independiente** debe pasar a la frontera durante una eliminación, evitando confundir soporte, número de estados o tamaño de una sintaxis concreta con complejidad intrínseca.

### MF-35C — selector económico

Usar esa carga para predecir un orden de liberación y contrastarlo contra `min_scope`, `min_degree`, `fill-in` y órdenes adversariales.

### MF-35D — puente físico

Sólo si una valoración conservativa adquiere una realización con unidades, composición y dinámica, contrastar si corresponde a momento, carga u otra magnitud física.

La pregunta central queda ahora dividida limpiamente:

\[
\boxed{
\text{conservación semántica}
\quad\text{vs}\quad
\text{economía de representación}
\quad\text{vs}\quad
\text{conservación física}.
}
\]
