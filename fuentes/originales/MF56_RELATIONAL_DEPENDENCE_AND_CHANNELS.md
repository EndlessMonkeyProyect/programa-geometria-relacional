# MF-56 — Naturaleza manifiesta, canales y dependencia relacional

**Versión:** v0.64-research  
**Estado:** teoremas exactos para relaciones finitas + no-go sobre cierres no tipados + definición mínima de naturaleza manifiesta.  
**Alcance:** estructura relacional previa a una dinámica física. No deriva todavía los canales físicos fundamentales ni selecciona el siguiente evento.

## 1. Preguntas

MF-55 dejó tres problemas: qué puede relacionar un cierre por su propia naturaleza; cuándo una restricción entre dos cierres constituye dependencia genuinamente conjunta; y qué relación posible se actualiza. MF-56 aborda los dos primeros.

## 2. Cierre y frontera

Para un cierre \(A=(X_A,\mathcal C_A,Q_A)\), su frontera suficiente es

\[
\boxed{K_A=X_A/{\sim_A}}.
\]

Por definición, toda comparación ya acreditada \(c\in\mathcal C_A\) factoriza por el cociente:

\[
Q_A(x,c)=\bar Q_{A,c}([x]).
\]

## 3. Naturaleza manifiesta

Definimos

\[
\boxed{\mathcal N_A^{\rm man}=(K_A,\mathscr O_A)}
\]

con

\[
\boxed{\mathscr O_A=\{\bar Q_{A,c}:K_A\to Y_c\mid c\in\mathcal C_A\}}.
\]

No agrega propiedades: registra qué distinciones puede expresar establemente el cierre usando el lenguaje que participó en su formación.

## 4. No-go MF-56A — la frontera desnuda no determina canales

Si sólo conocemos un conjunto \(K_A\) con \(|K_A|\ge2\), siempre existe una sobreyección \(K_A\twoheadrightarrow\{0,1\}\). Lo mismo vale para cualquier otro cierre no trivial.

Así, definir un canal sólo por la existencia de algún cociente común vuelve compatibles a todos los cierres no triviales.

\[
\boxed{\text{cardinalidad/partición desnuda}\not\Rightarrow\text{selectividad de interacción}.}
\]

La naturaleza debe incluir, como mínimo, qué respuestas o transformaciones son admisibles.

## 5. Canal manifiesto

Un canal de tipo \(\tau\) requiere respuestas compatibles

\[
o_A^\tau:K_A\to Z_\tau,\qquad o_B^\tau:K_B\to Z_\tau.
\]

Por tanto

\[
\boxed{\tau\in {\rm Type}(\mathscr O_A)\cap {\rm Type}(\mathscr O_B).}
\]

Compatibilidad significa existencia de lenguaje relacional compartido. Todavía no significa dependencia.

## 6. Relación conjunta

Sea

\[
\Gamma_{AB}\subseteq K_A\times K_B.
\]

Defina

\[
A_\Gamma=\pi_A(\Gamma),\qquad B_\Gamma=\pi_B(\Gamma).
\]

Si \(\Gamma=A_\Gamma\times B_\Gamma\), toda pérdida puede explicarse mediante restricciones locales separadas. Si

\[
\boxed{\Gamma\subsetneq A_\Gamma\times B_\Gamma,}
\]

hay combinaciones localmente posibles que sólo desaparecen por la relación entre ambos.

## 7. Déficit relacional de independencia

Definimos

\[
\boxed{D_R(A:B\mid\Gamma)=\log_2\frac{|A_\Gamma||B_\Gamma|}{|\Gamma|}.}
\]

Entonces

\[
\boxed{D_R\ge0}
\]

y

\[
\boxed{D_R=0\iff\Gamma=A_\Gamma\times B_\Gamma.}
\]

No es información mutua probabilística; es un déficit combinatorio de independencia del soporte.

## 8. Teorema MF-56B — descomposición exacta

La pérdida total desde el producto inicial es

\[
L_{\rm tot}=\log_2\frac{|K_A||K_B|}{|\Gamma|}.
\]

Defina

\[
\rho_A=\log_2\frac{|K_A|}{|A_\Gamma|},\qquad
\rho_B=\log_2\frac{|K_B|}{|B_\Gamma|}.
\]

Entonces

\[
\boxed{L_{\rm tot}=\rho_A+\rho_B+D_R.}
\]

Es decir:

\[
\boxed{\text{pérdida total}=\text{resolución local A}+\text{resolución local B}+\text{dependencia conjunta}.}
\]

## 9. Ejemplos mínimos

Sólo resolución local: \(\Gamma=\{(0,0),(0,1)\}\) da \(\rho_A=1,\rho_B=0,D_R=0\).

Igualdad binaria: \(\Gamma=\{(0,0),(1,1)\}\) mantiene ambos márgenes completos y produce \(D_R=1\) bit.

Dependencia parcial: \(\Gamma=\{(0,0),(0,1),(1,1)\}\) produce

\[
D_R=\log_2(4/3)\approx0.415\text{ bits}.
\]

Una correspondencia uno-a-uno de cuatro estados produce \(D_R=2\) bits.

## 10. Teorema MF-56C — cota

Como \(|\Gamma|\ge\max(|A_\Gamma|,|B_\Gamma|)\),

\[
\boxed{D_R\le\log_2\min(|A_\Gamma|,|B_\Gamma|).}
\]

## 11. Teorema MF-56D — aditividad

Para relaciones independientes \(\Gamma=\Gamma_1\times\Gamma_2\),

\[
\boxed{D_R(\Gamma)=D_R(\Gamma_1)+D_R(\Gamma_2).}
\]

## 12. Qué significa “compartían información”

La relación descubre que parte de lo que parecía información independiente sólo puede existir de manera conjunta. No es necesario que desaparezcan estados locales; puede desaparecer únicamente la libertad de combinarlos arbitrariamente.

\[
\boxed{\text{una interacción puede eliminar independencia sin eliminar identidades locales}.}
\]

## 13. Determinante mínimo de interacción

MF-56 distingue tres niveles:

- compatibilidad: existe un canal compartido;
- diferencia: el canal puede producir más de una respuesta;
- dependencia efectiva: la relación inducida satisface \(D_R>0\).

Por tanto:

\[
\boxed{\text{interacción efectiva}=\text{compatibilidad}+\text{diferencia}+\text{dependencia}.}
\]

## 14. Naturaleza manifiesta frente a naturaleza generativa

La naturaleza manifiesta sólo contiene respuestas ya acreditadas. Falta derivar la naturaleza generativa:

\[
\boxed{\mathcal N_A^{\rm gen}=\text{regla que determina qué nuevos canales puede sostener }A.}
\]

Ésta no puede ser un catálogo agregado externamente.

## 15. Puente con \(U,V,m,a\)

El álgebra previa distingue \(U\) como arena de diferencias, \(V\) como modo de proyección/transporte, \(m\) como complemento de identidad y \(a=V\times R\) como modo de reajuste/interacción.

MF-56 sugiere, todavía sólo como correspondencia programática:

\[
U\leftrightarrow\text{espacio de distinciones},\quad
V\leftrightarrow\text{información expuesta},\quad
m\leftrightarrow\text{interior conservado},\quad
a\leftrightarrow\text{reconfiguración por dependencia no factorizable}.
\]

Este puente no está derivado todavía.

## 16. Próximo frente

MF-57 debe intentar derivar \(\mathcal N_A^{\rm gen}\) desde la arquitectura interna del cierre. La pregunta es si \(U,V,m,a\), o una estructura más mínima nacida de reflexión y cierre, determina los tipos de respuesta que una identidad puede sostener. Sólo después tendría sentido volver a preguntar qué canal se actualiza primero.
