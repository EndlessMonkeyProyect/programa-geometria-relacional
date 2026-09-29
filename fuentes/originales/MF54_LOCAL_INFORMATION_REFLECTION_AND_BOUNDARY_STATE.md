# MF-54 — Información local: reflexión, comparación y estado suficiente de frontera

**Versión:** v0.62.1-research  
**Estado:** formalización fundacional + teoremas elementales exactos + controles finitos.  
**Alcance:** ontología relacional y su traducción matemática mínima. No presupone una arquitectura computacional concreta y no resuelve \(P\) vs \(NP\).

---

## 1. Cambio metodológico

Las etapas MF-46–MF-53 probaron sucesivamente lenguajes de interfaz, fusiones, certificados, memoria auxiliar y normalizaciones.

Ese trabajo fue útil para eliminar falsos atajos.

Pero el programa no debe tomar esas representaciones como origen.

La dirección fundacional es:

\[
\boxed{
\text{ontología}
\to
\text{estructura}
\to
\text{matemática}
\to
\text{falsación}.
}
\]

MF-54 vuelve al origen.

La pregunta es:

> ¿Qué es información si sólo existe una diferencia cuando algo puede compararse con algo?

---

## 2. Reflexión como lenguaje primario

Sea \(X\) el conjunto de realizaciones posibles de un cierre local.

Sea \(\mathcal C\) una familia de comparaciones exteriores admisibles.

Sea \(Q\) una regla de respuesta a una comparación.

Definimos la **reflexión relacional**:

\[
\boxed{
\mathfrak R_{\mathcal C,Q}(x)
=
\bigl(Q(x,c)\bigr)_{c\in\mathcal C}.
}
\]

No es todavía lenguaje simbólico humano.

Es la imagen que una realización \(x\) produce al ser confrontada con las comparaciones disponibles.

En este sentido:

\[
\boxed{
\text{lenguaje primario}
=
\text{estructura de reflexión/comparación}.
}
\]

La matemática formaliza después esta estructura.

---

## 3. Diferencia local

Dos realizaciones:

\[
x,y\in X
\]

son distinguibles en el contexto \((\mathcal C,Q)\) si existe al menos una comparación:

\[
c\in\mathcal C
\]

tal que:

\[
Q(x,c)\neq Q(y,c).
\]

Definimos:

\[
\boxed{
x\sim_{\mathcal C,Q}y
\iff
\forall c\in\mathcal C,
\quad
Q(x,c)=Q(y,c).
}
\]

Entonces:

\[
x\sim_{\mathcal C,Q}y
\iff
\mathfrak R_{\mathcal C,Q}(x)
=
\mathfrak R_{\mathcal C,Q}(y).
\]

La diferencia no es una propiedad absoluta de \(x\) o \(y\).

Es una propiedad de:

\[
\boxed{
(x,y;\mathcal C,Q).
}
\]

---

## 4. Información como diferencia acreditable por comparación

Sea:

\[
\Pi_{\mathcal C,Q}(X)
=
X/{\sim_{\mathcal C,Q}}
\]

el conjunto de clases distinguibles.

Definimos su cardinalidad relacional:

\[
\boxed{
N_{\mathcal C,Q}(X)
=
\left|
\Pi_{\mathcal C,Q}(X)
\right|.
}
\]

Y, para sistemas finitos, una medida informacional:

\[
\boxed{
I_{\mathcal C,Q}^{\rm rel}(X)
=
\log_2
N_{\mathcal C,Q}(X).
}
\]

Este logaritmo no se identifica automáticamente con entropía de Shannon.

Mide únicamente la cantidad de clases localmente distinguibles bajo la familia de comparaciones declarada.

---

## 5. Caso sin comparación

Si:

\[
\mathcal C=\varnothing,
\]

entonces todas las realizaciones tienen la misma reflexión vacía.

Por tanto:

\[
\boxed{
N_{\varnothing,Q}(X)=1
}
\]

y:

\[
\boxed{
I_{\varnothing,Q}^{\rm rel}(X)=0.
}
\]

Esto formaliza una tesis central:

\[
\boxed{
\text{sin comparación no aparece información relacional local}.
}
\]

No afirma que el sistema “no exista” ni que carezca de estructura ontológica.

Afirma que no hay todavía una diferencia acreditada respecto de un exterior.

---

## 6. Teorema MF-54A — localidad de la información

Sea el mismo sistema \(X\) observado mediante dos familias de comparación:

\[
\mathcal C_1,
\qquad
\mathcal C_2.
\]

En general:

\[
\boxed{
I_{\mathcal C_1,Q}^{\rm rel}(X)
\neq
I_{\mathcal C_2,Q}^{\rm rel}(X).
}
\]

Por tanto no existe, en esta definición, una cantidad absoluta:

\[
I(X)
\]

independiente del contexto.

La información pertenece a la relación:

\[
\boxed{
I(X\,|\,\mathcal C,Q).
}
\]

---

## 7. Teorema MF-54B — monotonía bajo enriquecimiento de comparación

Si:

\[
\mathcal C_1\subseteq\mathcal C_2,
\]

entonces:

\[
x\sim_{\mathcal C_2,Q}y
\Rightarrow
x\sim_{\mathcal C_1,Q}y.
\]

Es decir, el contexto más rico puede separar clases que antes estaban juntas, pero no puede identificar dos realizaciones que el contexto más pobre ya distinguía.

Luego:

\[
\boxed{
N_{\mathcal C_1,Q}(X)
\le
N_{\mathcal C_2,Q}(X)
}
\]

y:

\[
\boxed{
I_{\mathcal C_1,Q}^{\rm rel}(X)
\le
I_{\mathcal C_2,Q}^{\rm rel}(X).
}
\]

Interpretación:

\[
\boxed{
\text{una nueva comparación puede crear una nueva distinción efectiva}.
}
\]

Ésta es una forma precisa de novedad relacional.

---

## 8. Estado suficiente de frontera

Defina:

\[
\boxed{
\theta_{\mathcal C,Q}(x)
=
[x]_{\mathcal C,Q}.
}
\]

Éste es el estado de frontera de \(x\): no conserva la historia completa, sino únicamente la clase de diferencias que el exterior todavía puede acreditar.

---

## 9. Teorema MF-54C — minimalidad del estado suficiente

Sea:

\[
\sigma:X\to S
\]

cualquier resumen determinista que permita reconstruir exactamente:

\[
Q(x,c)
\]

para todo:

\[
x\in X,
\qquad
c\in\mathcal C.
\]

Entonces:

\[
\sigma(x)=\sigma(y)
\Rightarrow
x\sim_{\mathcal C,Q}y.
\]

Por contraposición, realizaciones contextualmente distinguibles no pueden compartir el mismo resumen exacto.

Por tanto:

\[
\boxed{
|S|
\ge
N_{\mathcal C,Q}(X).
}
\]

El cociente:

\[
\theta_{\mathcal C,Q}
\]

alcanza esa cota.

Así:

\[
\boxed{
\theta_{\mathcal C,Q}
=
\text{estado exacto mínimo relativo a la comparación}.
}
\]

Esto no es una compresión elegida desde fuera.

Es consecuencia de qué diferencias pueden seguir apareciendo localmente.

---

## 10. La información no se “guarda” completa

Una cápsula puede contener muchas configuraciones internas:

\[
x_1,x_2,\ldots
\]

pero si:

\[
x_i\sim_{\mathcal C,Q}x_j,
\]

esas diferencias internas no necesitan conservarse en la frontera para responder a ningún contexto permitido.

Por tanto:

\[
\boxed{
\text{memoria de frontera}
=
\text{diferencias todavía discriminables},
}
\]

no:

\[
\text{historia completa del interior}.
\]

---

## 11. Novedad y resolución son operaciones distintas

MF-54 separa dos cambios.

### 11.1 Novedad por nueva comparación

Mantenga fijo \(X\) y amplíe:

\[
\mathcal C
\to
\mathcal C'.
\]

Puede aumentar:

\[
N_{\mathcal C,Q}(X).
\]

Una diferencia que antes no tenía lugar donde aparecer se vuelve discriminable.

### 11.2 Resolución por restricción

Mantenga fijo \(\mathcal C\) y añada una relación que restringe:

\[
X
\to
X'\subseteq X.
\]

Algunas clases dejan de ser realizables.

Entonces puede disminuir el conjunto de diferencias pendientes.

Por tanto:

\[
\boxed{
\text{novedad}
\neq
\text{resolución}.
}
\]

La primera enriquece la comparación.

La segunda restringe las realizaciones compatibles.

---

## 12. Cierre local

Un cierre no requiere borrar toda diferencia interna.

Requiere que toda diferencia interna que no pertenezca a la frontera sea irrelevante para el conjunto de comparaciones admisibles.

Formalmente, la frontera cerrada es el cociente:

\[
\boxed{
X/{\sim_{\mathcal C,Q}}.
}
\]

Las variaciones dentro de una clase son interior.

Las diferencias entre clases son información de frontera.

Así:

\[
\boxed{
\text{cierre}
=
\text{interior}
+
\text{equivalencia contextual}
+
\text{frontera suficiente}.
}
\]

---

## 13. Dinámica sin introducir primero el tiempo

Sea un estado relacional:

\[
\Omega=(X,\mathcal C,Q).
\]

Una nueva relación puede modificar:

\[
X\to X'
\]

y una nueva referencia puede modificar:

\[
\mathcal C\to\mathcal C'.
\]

El objeto observable cambia entonces de:

\[
\Pi_{\mathcal C,Q}(X)
\]

a:

\[
\Pi_{\mathcal C',Q}(X').
\]

La dinámica primaria puede definirse como una sucesión causal de transformaciones:

\[
\boxed{
(X,\mathcal C)
\longrightarrow
(X',\mathcal C').
}
\]

El índice temporal no es necesario para definir el cambio.

Sólo después puede ordenarse la sucesión:

\[
e_1\prec e_2\prec e_3\prec\cdots
\]

y comparar ritmos entre ciclos.

Esto preserva la tesis previa del programa:

\[
\boxed{
\text{el tiempo no es el contenedor del cambio;
es una comparación de procesos de cambio}.
}
\]

---

## 14. Control positivo — umbral y corrección de localidad

Sea la pregunta:

\[
Q(p,s)
=
\mathbf 1[
|p|+|s|\le k
],
\]

donde \(p\) es un prefijo ya cerrado y \(s\) pertenece al futuro todavía disponible.

Sea:

\[
r=n-t
\]

el número de bits futuros restantes.

El primer candidato heredado de MF-52 era:

\[
\min(k+1,|p|).
\]

El control exhaustivo mostró que este objeto es suficiente, pero **no siempre mínimo** para un horizonte futuro finito.

La razón es ontológicamente importante: dos conteos distintos pueden dejar de ser distinguibles si ningún futuro todavía accesible puede hacer que produzcan respuestas diferentes.

El estado mínimo exacto es la capacidad restante:

\[
c(p)=k-|p|,
\]

recortada por el dominio de comparaciones futuras:

\[
\boxed{
\theta_t(p)
=
\operatorname{clip}
\bigl(
k-|p|,
-1,
r
\bigr).
}
\]

Interpretación:

- \(\theta=-1\): todo futuro rechaza;
- \(\theta=r\): todo futuro disponible acepta;
- \(0\le\theta<r\): el futuro puede todavía distinguir según cuántos unos aporte.

El control exhaustivo verifica:

\[
\boxed{
p\sim_{\mathcal C_t,Q}p'
\iff
\theta_t(p)=\theta_t(p').
}
\]

Así, el estado suficiente depende no sólo del interior acumulado, sino de:

\[
\boxed{
\text{lo que el futuro local todavía puede distinguir}.
}
\]

Ésta es una corrección importante respecto de MF-52: el contador capado era una cápsula correcta, pero no siempre la cápsula mínima relativa al contexto.

El resultado fortalece la tesis central de MF-54:

\[
\boxed{
\text{el estado suficiente no es intrínseco al objeto;
es relativo a la comparación disponible}.
}
\]

---

## 15. Control positivo — paridad

Para:

\[
Q(p,s)
=
(|p|+|s|)\bmod2,
\]

el cociente produce dos clases:

\[
\boxed{
\theta(p)=|p|\bmod2.
}
\]

Otra vez, el parámetro emerge de la comparación.

No fue impuesto como una técnica de compresión.

---

## 16. Lenguaje, cardinalidad y matemática

MF-54 no pretende derivar la cardinalidad desde el lenguaje.

La cardinalidad se utiliza como capacidad formal de contar clases ya distinguibles.

La tesis es más precisa:

\[
\boxed{
\text{la comparación determina qué multiplicidades son informacionalmente distintas}.
}
\]

El lenguaje primario es la arquitectura de reflexión.

La matemática es la formalización posterior de:

- equivalencias;
- cardinalidades;
- cierres;
- transformaciones.

---

## 17. Consecuencia para la rama \(P\) vs \(NP\)

Las etapas anteriores buscaban una representación:

\[
K.
\]

MF-54 cambia la pregunta:

> ¿qué diferencias puede realmente acreditar el contexto relevante?

La representación debería venir después:

\[
\boxed{
\theta
=
X/{\sim_{\mathcal C,Q}}
\quad
\longrightarrow
\quad
\text{representación computable de }\theta.
}
\]

El problema computacional reaparece en la constructibilidad:

- definir semánticamente la equivalencia no basta;
- hay que poder acreditarla sin resolver globalmente la instancia.

Así se conserva la distinción:

\[
\boxed{
\text{estado suficiente semántico}
\neq
\text{estado suficiente acreditable eficientemente}.
}
\]

---

## 18. Nuevo frente

El siguiente paso ya no debe probar otra estructura de datos.

Debe preguntar:

\[
\boxed{
\text{¿qué operaciones locales permiten acreditar}
\sim_{\mathcal C,Q}
\text{ sin consultar todos los futuros?}
}
\]

Ésa es la versión computacional de la pregunta ontológica.

Si se obtiene una regla local completa y polinómica para 3-SAT, la consecuencia sería extraordinaria.

Si aparecen familias donde acreditar la equivalencia exige trabajo superpolinómico dentro de la arquitectura propuesta, habremos localizado exactamente dónde la ontología deja de traducirse automáticamente en economía computacional.
