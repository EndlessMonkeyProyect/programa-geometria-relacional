# MF-55 — Regla de transición ontológica: novedad, resolución y cierre local

**Versión:** v0.63-research  
**Estado:** formalización fundacional + teoremas exactos para sistemas finitos + controles computacionales.  
**Alcance:** transición informacional condicionada a una nueva relación/comparación. No deriva todavía una ley física que seleccione cuál relación ocurre.

## 1. Qué se intenta derivar

MF-54 definió información local mediante distinguibilidad contextual:

\[
x\sim_{\mathcal C,Q}y
\iff
\forall c\in\mathcal C,\quad
Q(x,c)=Q(y,c).
\]

El estado suficiente de frontera es:

\[
\theta_{\mathcal C,Q}(x)=[x]_{\mathcal C,Q}.
\]

La pregunta de MF-55 es:

> dada una nueva comparación o una nueva relación restrictiva, ¿cómo debe cambiar necesariamente ese estado?

No se postula una ecuación de movimiento. Se deriva la transformación forzada por la nueva estructura relacional.

## 2. Estado relacional local

Definimos:

\[
\boxed{\Omega=(X,\mathcal C,Q)}
\]

donde \(X\) son las realizaciones admisibles, \(\mathcal C\) las comparaciones disponibles y \(Q\) la respuesta a una comparación.

La frontera informacional es:

\[
\boxed{K(\Omega)=X/{\sim_{\mathcal C,Q}}}.
\]

Para \(X\neq\varnothing\):

\[
\boxed{I(\Omega)=\log_2|K(\Omega)|}.
\]

## 3. Dos operaciones ontológicamente distintas

### 3.1 Novedad

Ampliar lo que puede compararse:

\[
\mathcal C\to\mathcal C'=\mathcal C\cup D.
\]

La partición sólo puede refinarse, de modo que:

\[
\boxed{
\nu_D(X|\mathcal C)
=
I(X,\mathcal C')-I(X,\mathcal C)\ge0.
}
\]

### 3.2 Resolución

Restringir lo que todavía puede realizarse:

\[
X\to X'\subseteq X.
\]

Entonces:

\[
\boxed{
\rho_{X'}(\mathcal C|X)
=
I(X,\mathcal C)-I(X',\mathcal C)\ge0
}
\]

si \(X'\neq\varnothing\).

Si \(X'=\varnothing\), se alcanza un estado contradictorio terminal \(\bot\).

## 4. Regla de transición mínima

Un evento relacional \(e\) puede contener nuevas comparaciones \(D_e\) y una restricción de realizabilidad \(Y_e\).

Entonces:

\[
\boxed{X_{t+1}=X_t\cap Y_e}
\]

y

\[
\boxed{\mathcal C_{t+1}=\mathcal C_t\cup D_e}.
\]

La nueva frontera es:

\[
\boxed{
K_{t+1}
=
X_{t+1}/{\sim_{\mathcal C_{t+1},Q}}.
}
\]

Ésta es una cinemática relacional del cierre. No especifica qué evento \(e\) ocurre.

## 5. Teorema MF-55A — una comparación binaria aporta como máximo un bit

Sea \(c\) binaria. Cada clase previa puede permanecer intacta o dividirse en dos.

Si \(N\) es el número de clases previas y \(s_c\) el número de clases que \(c\) divide:

\[
\boxed{N'=N+s_c}.
\]

Como \(0\le s_c\le N\):

\[
N\le N'\le2N.
\]

Por tanto:

\[
\boxed{
0\le
\nu_c
=
\log_2\frac{N'}{N}
\le1.
}
\]

Una diferencia binaria elemental puede abrir como máximo un bit de distinguibilidad local.

## 6. El bit fundamental, formulado localmente

\(U_0=1\) bit debe entenderse como capacidad máxima de una distinción binaria elemental.

La novedad global puede ser fraccionaria si sólo algunas clases previas se dividen.

Así no se afirma que toda información de la realidad sea intrínsecamente binaria.

## 7. Teorema MF-55B — criterio exacto de novedad

Sea \(q_{\mathcal C}:X\to K(X,\mathcal C)\) el cociente actual.

Una nueva comparación \(c\) no añade información si y sólo si existe:

\[
\bar Q_c:K(X,\mathcal C)\to A_c
\]

tal que:

\[
\boxed{
Q(x,c)=\bar Q_c(q_{\mathcal C}(x)).
}
\]

Equivalente:

\[
\boxed{
\nu_c=0
\iff
c\text{ es constante sobre cada clase previa}.
}
\]

Si la nueva comparación puede responderse enteramente desde la frontera existente, no hace falta ampliar el marco.

## 8. Evento de apertura

Si no existe esa factorización, entonces hay \(x,y\) tales que:

\[
x\sim_{\mathcal C}y
\]

pero:

\[
Q(x,c)\neq Q(y,c).
\]

La frontera anterior ya no es suficiente.

Por tanto:

\[
\boxed{
\text{comparación no factorizable}
\Rightarrow
\text{apertura necesaria de la frontera}.
}
\]

## 9. Correspondencia tentativa con dimensión

El resultado matemático dice que la partición previa debe refinarse.

La lectura ontológica es que se requiere una capacidad nueva para conservar una diferencia que el marco previo no podía expresar.

Esto formaliza la intuición:

\[
\boxed{
\text{dimensión}
\sim
\text{espacio requerido por información que no cabe en el marco anterior}.
}
\]

Identificar esta apertura con una dimensión espacial física sigue siendo una hipótesis posterior.

## 10. Teorema MF-55C — cierre idempotente

Una vez formado:

\[
K=X/{\sim_{\mathcal C,Q}},
\]

la respuesta inducida sobre \(K\) está bien definida.

Volver a cerrar con la misma familia de comparaciones no produce una nueva identificación:

\[
\boxed{
K/{\sim_{\mathcal C,\bar Q}}\cong K.
}
\]

Por tanto:

\[
\boxed{
\text{cierre respecto del mismo lenguaje es idempotente}.
}
\]

## 11. Teorema MF-55D — resolución no crea clases nuevas

Para \(X'\subseteq X\), con la misma \(\mathcal C\):

\[
\boxed{
|K(X',\mathcal C)|
\le
|K(X,\mathcal C)|.
}
\]

La resolución puede eliminar diferencias realizables, pero no fabricar una diferencia que el contexto no distinguía.

Así:

\[
\boxed{\text{resolución}\neq\text{novedad}}.
\]

## 12. Acoplamiento entre novedad y resolución

Con \(X'\subseteq X\) y \(\mathcal C'\supseteq\mathcal C\), el cambio total:

\[
\Delta I
=
I(X',\mathcal C')-I(X,\mathcal C)
\]

puede descomponerse de dos maneras:

\[
\Delta I=\nu_X-\rho_{\mathcal C'}
\]

o:

\[
\Delta I=-\rho_{\mathcal C}+\nu_{X'}.
\]

Por tanto:

\[
\boxed{
\nu_X-\nu_{X'}
=
\rho_{\mathcal C'}-\rho_{\mathcal C}.
}
\]

Definimos el balance:

\[
\boxed{
\chi_{\rm NR}
=
\nu_X-\nu_{X'}.
}
\]

No es una fuerza ni una energía. Mide cuánto de la novedad potencial dependía de realizaciones que la resolución eliminó.

## 13. Ejemplo elemental

Sea:

\[
X=\{00,01,10,11\}
\]

y la frontera inicial sólo distingue \(b_0\).

Entonces \(I=1\).

Añadir \(b_1\) da \(I=2\): se abre un bit.

Si después imponemos \(b_1=0\), volvemos a \(I=1\).

Si la restricción hubiera ocurrido primero, añadir después \(b_1\) no habría abierto ninguna diferencia.

El estado final puede ser el mismo, pero la historia intermedia de diferencias no.

## 14. Orden causal antes de tiempo métrico

El ejemplo muestra que el orden de eventos puede determinar qué diferencias llegan a existir como información local.

No hace falta introducir segundos.

Basta:

\[
e_1\prec e_2.
\]

Esto da una noción primaria de orden causal antes de una métrica temporal.

## 15. Qué se derivó y qué sigue abierto

### Derivado

Dado un evento \(e\):

\[
\Omega_t\xrightarrow{e}\Omega_{t+1}
\]

queda determinado por la restricción de \(X\), el enriquecimiento de \(\mathcal C\) y el cociente contextual.

### Abierto

Todavía no se ha derivado:

\[
\boxed{
\text{qué evento }e\text{ ocurre a continuación}.
}
\]

Ésta es la diferencia entre regla de actualización y ley de selección del evento.

## 16. Puente hacia computación

En SAT, \(X\) puede representar realizaciones todavía compatibles y \(\mathcal C\) preguntas/interfases acreditadas.

Pero construir semánticamente el cociente puede ser costoso.

Por tanto:

\[
\boxed{
\text{transición ontológica definida}
\neq
\text{algoritmo eficiente}.
}
\]

## 17. Puente hacia física

MF-55 no identifica esta transición con ninguna fuerza física.

Todavía falta derivar:

1. qué constituye una comparación física;
2. qué restringe realizaciones;
3. qué selecciona el siguiente evento;
4. cómo emerge una escala temporal;
5. cómo aparecen observables dimensionales.

## 18. Resultado conceptual

La cadena queda:

\[
\boxed{
\text{reflexión}
\to
\text{comparación}
\to
\text{diferencia}
\to
\text{novedad}
\to
\text{restricción}
\to
\text{residuo}
\to
\text{cierre}
\to
\text{nueva frontera}.
}
\]

## 19. Próximo problema

La pregunta decisiva pasa a ser:

\[
\boxed{
\text{¿qué selecciona una relación posible como el siguiente evento real?}
}
\]

MF-56 deberá investigar si esa selección puede derivarse de diferencia pendiente, cierre mínimo, economía relacional o incompatibilidad local sin introducir una nueva ley arbitraria.
