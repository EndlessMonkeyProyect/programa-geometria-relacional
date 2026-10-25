# MF-52 — La interfaz como cápsula: memoria interna, compilación y barrera de constructibilidad

**Versión:** v0.60-research  
**Estado:** construcción exacta para la familia umbral + teoremas de clasificación sobre interfaces intensionales/extensionales + barrera de compilación universal.  
**Alcance:** representación, proyección e inferencia booleana. No demuestra \(P=NP\) ni \(P\ne NP\).

---

## 1. De la interfaz plana a la cápsula

MF-51 mostró una separación fuerte:

- las dos capas umbral poseen codificaciones 3-CNF polinómicas con auxiliares;
- la interfaz CNF plana sobre las variables compartidas necesita ancho lineal y tamaño exponencial.

La reacción correcta no es aumentar indefinidamente el ancho.

Es permitir que la propia interfaz tenga interior:

\[
\boxed{
\mathcal K
=
(Z,\mathcal R_Z,\partial Z).
}
\]

Aquí:

- \(Z\): memoria interna de la interfaz;
- \(\mathcal R_Z\): relaciones que actualizan/conservan esa memoria;
- \(\partial Z\): información visible al contexto.

La interfaz pasa a ser una cápsula.

---

## 2. Dos significados de “representación compacta”

Sea:

\[
F(X,Z)
\]

un subsistema con frontera \(X\) e interior \(Z\).

Su comportamiento externo exacto es:

\[
\Gamma(X)
=
\exists Z\,F(X,Z).
\]

Hay dos representaciones distintas.

### 2.1 Representación intensional

Conservar:

\[
\boxed{
K_{\rm int}
=
(Z,F(X,Z)).
}
\]

Es compacta si \(F\) lo era.

Pero la cuantificación de \(Z\) sigue pendiente.

### 2.2 Representación extensional/compilada

Construir un objeto:

\[
\boxed{
K_{\rm ext}(X)
}
\]

que represente directamente:

\[
K_{\rm ext}(X)
\equiv
\exists Z\,F(X,Z)
\]

y cuyas operaciones futuras puedan ejecutarse sin volver a abrir \(Z\).

Esta segunda noción es la que constituye un cierre computacional fuerte.

---

## 3. No-go MF-52A — la compacidad intensional es trivial

Toda fórmula de entrada:

\[
F(X,Z)
\]

ya es una representación intensional de:

\[
\exists Z\,F(X,Z).
\]

Por tanto:

\[
\boxed{
\text{“existe una cápsula intensional pequeña”}
}
\]

no es, por sí solo, una afirmación de eficiencia.

Basta con no eliminar las variables internas.

Pero entonces el problema original puede seguir intacto en:

\[
\exists Z.
\]

Así:

\[
\boxed{
\text{memoria interna}
\neq
\text{compilación}.
}
\]

La memoria puede:

1. **compilar** una regularidad y volverla operable;
2. o simplemente **aplazar** la búsqueda.

Ésta es una distinción canónica.

---

## 4. Control positivo: cápsula contador

Para:

\[
H_{n,k}:\quad |x|\le k,
\]

defina un estado interno:

\[
q_i
=
\min
\left(
k+1,
\sum_{j=1}^{i}x_j
\right).
\]

El estado toma valores:

\[
\boxed{
q_i\in\{0,1,\ldots,k,k+1\}.
}
\]

La transición elemental es:

\[
\boxed{
q_{i+1}
=
\min(k+1,q_i+x_{i+1}).
}
\]

La condición final:

\[
q_n\le k
\]

representa exactamente `AtMost-k`.

Y:

\[
q_n=k+1
\]

representa exactamente `AtLeast-(k+1)`.

La misma memoria coordina ambas capas.

---

## 5. Teorema MF-52B — tamaño polinómico de la cápsula umbral

En la capa \(i\) sólo son alcanzables:

\[
0,\ldots,\min(i,k+1).
\]

El número total de estados alcanzables del DAG estratificado es:

\[
S(n,k)
=
\sum_{i=0}^{n}
\left[
\min(i,k+1)+1
\right].
\]

Por tanto:

\[
\boxed{
S(n,k)=O(nk).
}
\]

En el caso balanceado:

\[
k=\Theta(n),
\]

se obtiene:

\[
\boxed{
S(n,k)=O(n^2).
}
\]

Compare con la interfaz CNF plana de MF-51:

\[
\Theta
\left(
\frac{2^n}{\sqrt n}
\right)
\]

cláusulas.

Así:

\[
\boxed{
\text{la explosión de MF-51 era una explosión de representación plana,}
}
\]

no una necesidad de memoria exponencial para esta familia.

---

## 6. Composición de cápsulas contador

Dos bloques pueden resumirse por:

\[
q_A
=
\min(k+1,|A|),
\]

\[
q_B
=
\min(k+1,|B|).
\]

Su composición es:

\[
\boxed{
q_{A\cup B}
=
q_A\oplus_k q_B
=
\min(k+1,q_A+q_B).
}
\]

La operación es asociativa:

\[
(a\oplus_k b)\oplus_k c
=
a\oplus_k(b\oplus_k c).
\]

Por tanto bloques completos pueden cerrarse, resumirse y volver a entrar como objetos del mismo tipo.

Ésta es una realización exacta de:

\[
\boxed{
\text{interfaz como cápsula composicional}.
}
\]

---

## 7. Qué diferencia este caso de “guardar las variables”

La cápsula contador no conserva las \(2^i\) configuraciones del prefijo.

Conserva sólo una clase suficiente:

\[
q_i.
\]

Dos prefijos son equivalentes para todo futuro respecto de la pregunta umbral cuando producen el mismo valor capado.

Así:

\[
\boxed{
q_i
}
\]

es un **estado suficiente de frontera**.

La memoria interna ha realizado una compresión semántica, no sólo una renominación de variables.

---

## 8. Contrato operacional de una cápsula útil

El tamaño de la representación no basta.

Una clase de cápsulas computacionalmente útil debe especificar operaciones:

\[
\boxed{
\mathfrak K
=
(
\mathrm{Join},
\mathrm{Project},
\mathrm{Normalize},
\mathrm{Empty},
\mathrm{Read}
).
}
\]

Y controlar:

\[
\boxed{
\mathcal C(\mathfrak K)
=
(
|\mathcal K|,
T_{\rm join},
T_{\rm project},
T_{\rm normalize},
T_{\rm empty},
T_{\rm read}
).
}
\]

Una cápsula es económicamente cerrada sólo si estas cantidades permanecen dentro del presupuesto declarado a lo largo de las composiciones necesarias.

---

## 9. Teorema MF-52C — una compilación uniforme universal implicaría \(P=NP\)

Suponga que existe un algoritmo uniforme:

\[
\mathrm{Compile}(F(X,Z))
\]

que, para toda CNF \(F\) de tamaño \(N\):

1. corre en tiempo \(\operatorname{poly}(N)\);
2. produce una representación exacta:

\[
K(X)
\equiv
\exists Z\,F(X,Z);
\]

3. mantiene:

\[
|K|=\operatorname{poly}(N);
\]

4. permite decidir `Empty`/verdad de la representación final en tiempo polinómico.

Aplique el compilador con frontera vacía:

\[
X=\varnothing.
\]

Entonces:

\[
K
\equiv
\exists Z\,F(Z)
\]

es una constante booleana.

Leerla decide SAT en tiempo polinómico.

Por tanto:

\[
\boxed{
\text{compilador uniforme universal de este tipo}
\Rightarrow
P=NP.
}
\]

Esto no es una solución.

Es una clasificación precisa de la barrera.

---

## 10. Versión no uniforme

Suponga sólo que para toda proyección:

\[
\exists Z\,F(X,Z)
\]

existe algún circuito de tamaño polinómico, sin exigir que podamos construirlo eficientemente desde \(F\).

Eso no da automáticamente \(P=NP\).

Una hipótesis de esta fuerza implicaría, en particular, que lenguajes de NP poseen circuitos polinómicos:

\[
\boxed{
NP\subseteq P/poly.
}
\]

La diferencia reproduce:

\[
\boxed{
\text{existencia}
\neq
\text{constructibilidad}.
}
\]

---

## 11. Relación con MF-32

MF-32 demostró cierre composicional sintáctico para DAGs:

\[
\Gamma_x
=
B_0\lor B_1
=
\exists x\,B.
\]

La salida vuelve a pertenecer a la misma gramática.

Pero ya había quedado abierta la economía iterada.

MF-52 permite reinterpretar ese resultado:

\[
\boxed{
\text{DAG cerrado}
}
\]

es la condición de **tipo**.

Lo que falta para \(P=NP\) es:

\[
\boxed{
\text{normalización económica uniforme}.
}
\]

No basta que el objeto siga siendo un DAG.

Hace falta impedir que su tamaño o el costo de operarlo se conviertan en el lugar donde reaparece la búsqueda exponencial.

---

## 12. La cápsula contador como control de normalización

En la familia umbral sí existe una normalización conocida:

\[
\text{prefijo}
\mapsto
q_i.
\]

Después de leer cada bit:

\[
q_i
\]

es una forma canónica suficiente para todos los futuros respecto del umbral.

Por eso:

\[
\boxed{
\text{Join + Project + Normalize}
}
\]

permanece polinómico.

El éxito no proviene simplemente de introducir auxiliares.

Proviene de conocer una **regla de normalización suficiente**.

---

## 13. Nuevo diagnóstico para 3-SAT

La pregunta fundamental puede escribirse ahora:

> Dado un DAG \(C_t\) obtenido tras una secuencia de cierres y proyecciones, ¿existe una transformación polinómica
>
> \[
> N(C_t)
> \]
>
> que conserve exactamente las consecuencias de frontera pertinentes y mantenga
>
> \[
> |N(C_t)|=\operatorname{poly}(|F|)?
> \]

Si sí para toda 3-SAT y la secuencia es construible uniformemente:

\[
P=NP.
\]

Si no, necesitamos identificar qué familia fuerza la explosión.

---

## 14. Tres tipos de memoria

MF-52 propone distinguir:

### A. Memoria redundante

Conserva variables que podrían eliminarse sin costo.

### B. Memoria diferida

Conserva variables internas porque eliminarlas es difícil.

No ha reducido la complejidad; la ha pospuesto.

### C. Memoria compilada

Conserva un estado interno nuevo cuyo tamaño es menor que la información extensional y para el cual las operaciones futuras son eficientes.

La cápsula contador es tipo C.

La mera fórmula original tratada como cápsula es tipo B.

La ruta a \(P=NP\) necesita demostrar que la coordinación general puede convertirse uniformemente de B a C.

---

## 15. Un criterio más fuerte que “tamaño pequeño”

Defina el **perfil operacional de cierre**:

\[
\boxed{
\mathcal O(\mathcal K)
=
(
S,
J,
P,
N,
E
)
}
\]

con:

- \(S\): tamaño;
- \(J\): costo de composición;
- \(P\): costo de proyección;
- \(N\): costo de normalización;
- \(E\): costo de decidir vaciedad.

Una representación es económicamente útil sólo cuando el perfil completo permanece controlado.

Esto evita falsos avances del tipo:

\[
\boxed{
\text{“la fórmula todavía es pequeña”}
}
\]

cuando `Empty` sigue siendo NP-difícil.

---

## 16. Validación de la cápsula umbral

Se verificó exhaustivamente para:

\[
2\le n\le16,
\qquad
k=\lfloor n/2\rfloor,
\]

que:

\[
q_n
=
\min(k+1,|x|),
\]

para todas las asignaciones.

También se verificó:

\[
q_n\le k
\iff
|x|\le k,
\]

\[
q_n=k+1
\iff
|x|\ge k+1.
\]

Fallos:

\[
\boxed{0}.
\]

Se verificó además la composición por bloques:

\[
q_{A\cup B}
=
q_A\oplus_k q_B
\]

en todas las asignaciones hasta \(n=14\).

Fallos:

\[
\boxed{0}.
\]

---

## 17. Comparación cuantitativa

Para \(n=40\), \(k=20\):

- CNF plana máxima de MF-51:

\[
137\,846\,528\,820
\]

cláusulas en la dirección más costosa relevante del umbral central según el parámetro correspondiente;

- cápsula contador estratificada:

\[
671
\]

estados alcanzables.

Para valores mayores la diferencia crece exponencialmente frente a polinomialmente.

La comparación no dice que todo problema posea un contador semejante.

Dice exactamente lo contrario:

\[
\boxed{
\text{el objeto que falta en 3-SAT es una normalización análoga, si existe.}
}
\]

---

## 18. Resultado principal

MF-52 cambia el criterio de éxito.

Antes:

\[
\text{“mantener una representación compacta”.}
\]

Ahora:

\[
\boxed{
\text{construir una forma normal suficiente, composicional y operable.}
}
\]

La interfaz como cápsula sólo es una ventaja computacional cuando su interior es una **memoria compilada**, no una zona donde ocultar las variables todavía no resueltas.

---

## 19. Próximo blanco

MF-53 debe buscar una normalización dinámica sobre DAGs generales y atacarla adversarialmente.

No debe preguntarse primero si el DAG es pequeño.

Debe medir simultáneamente:

\[
\boxed{
|C_t|,
\quad
T_{\rm restrict},
\quad
T_{\rm project},
\quad
T_{\rm normalize},
\quad
T_{\rm empty}.
}
\]

El control positivo será la cápsula contador.

El control negativo debe incluir fórmulas donde diferentes órdenes de proyección producen DAGs radicalmente distintos.

El discriminante será:

\[
\boxed{
\text{¿la normalización descubre estados suficientes,
o sólo memoiza una expansión de búsqueda?}
}
\]

Éste es ahora el frente computacional más limpio del programa.
