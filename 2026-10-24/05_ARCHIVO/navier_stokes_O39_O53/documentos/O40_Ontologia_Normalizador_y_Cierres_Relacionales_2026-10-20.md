# O40 — Del hilo del dos al normalizador que se conserva

**Programa de Geometría Relacional · borrador de formalización ontología → matemática → física**  
**Fecha:** 20 de octubre de 2026  
**Estado:** suplemento independiente; no modifica la Imagen Total ni declara resuelto Navier–Stokes 3D.

## 0. Criterio de construcción

Este texto reconstruye el hilo conceptual expresado en la conversación, **antes** de elegir una notación matemática. Los símbolos que siguen son modelos candidatos de esa ontología, no definiciones retroactivas de ella. Se distingue entre **[POSTULADO ONTOLÓGICO]**, **[DERIVACIÓN MATEMÁTICA]**, **[HIPÓTESIS DE PUENTE FÍSICO]** y **[ABIERTA]**.

## 1. Narrativa ontológica, desde la unidad

**[POSTULADO ONTOLÓGICO · Unidad]** En la homogeneidad inicial, la unidad no necesita un referente exterior para ser ella misma. No hay todavía una diferencia acreditable por comparación. Esto no afirma que exista un observador, foco o espacio externos a la unidad.

**[POSTULADO ONTOLÓGICO · Reflexión]** La reflexión constituye una referencia interna: permite que la totalidad aparezca relacionalmente sin duplicar de antemano la unidad como dos objetos separados. La primera diferencia es interna a la comparación que emerge.

**[POSTULADO ONTOLÓGICO · Parte, todo y resto]** La diferencia permite distinguir una relación parte–todo. Al intentar resolverla mediante una referencia común aparece lo que queda pendiente: no necesariamente una magnitud material perdida, sino una relación todavía no incorporada al cierre actual.

**[POSTULADO ONTOLÓGICO · Normalizador]** La referencia común que hace comparables las proyecciones es el normalizador. Lo que pasa a la escala siguiente no es, por sí solo, el numerador de una fracción: **se conserva la regla relacional del normalizador**. Su representación numérica puede refinarse sin perder las relaciones ya acreditadas.

**[POSTULADO ONTOLÓGICO · Dos espejos]** Dos proyecciones pueden ser equivalentes en sus relaciones sin ser copias por simple aumento o reducción de tamaño. La equivalencia se reconoce por las relaciones que conserva cada proyección, no por igualdad de forma o de escala.

**[POSTULADO ONTOLÓGICO · Cambio de cierre]** Cuando la estructura presente ya no sostiene la relación pendiente, puede alterar una componente perpendicular, cambiar de topología y entrar en otra familia de cierres propios. La pérdida de una forma no prueba la desaparición de la información ni la singularidad del sistema completo.

La secuencia ontológica propuesta es:

**unidad → reflexión interna → diferencia → comparación parte/todo → normalizador común → relación pendiente → nuevo cierre compatible o cambio de topología**.

## 2. Primera representación matemática: la familia del normalizador

**[MODELO MATEMÁTICO CANDIDATO, SOLO PARA RELACIONES CONMENSURABLES]** Fijemos una unidad de referencia `U` y un entero positivo `N`. Denotamos

\[
G_N:=\left\{\frac{k}{N}U:k\in\mathbb Z\right\}.
\]

`G_N` es la familia aditiva de magnitudes que el normalizador `N` puede expresar exactamente. Una relación pendiente puede escribirse, en este caso restringido, como

\[
r=\frac{k}{N},\qquad 0\le r<1.
\]

La expresión «una unidad pendiente» debe interpretarse **ontológicamente** como un lugar de comparación aún no cerrado; **no** obliga matemáticamente a que `k=1` en todas las etapas.

**[DERIVACIÓN MATEMÁTICA · Lema de inclusión]** Si `N` divide a `M`, entonces `G_N ⊆ G_M`. En efecto,

\[
\frac{k}{N}U=\frac{k(M/N)}{M}U.
\]

Por tanto, si aparece una nueva relación con denominador reducido `b`, el menor refinamiento entero que permite expresar ambas familias es

\[
\boxed{M=\operatorname{mcm}(N,b).}
\]

Esto demuestra **conservación de expresabilidad**, no estabilidad física. El mínimo común múltiplo opera sobre **denominadores/restricciones de divisibilidad**, no sobre una nueva cardinalidad elegida sin explicar qué representa.

**Ejemplo.** Una relación pendiente de `1/6` y una nueva relación de `1/4` se escriben bajo `M=12` como `2/12` y `3/12`. Se conservó la referencia anterior y se incorporó una relación adicional; todavía no sabemos si pueden coexistir físicamente.

## 3. La equivalencia de los dos espejos no exige homotecia

**[DERIVACIÓN MATEMÁTICA · Ejemplo]** Representemos dos estados geométricos por matrices simétricas positivas:

\[
A=\begin{pmatrix}2&0\\0&1\end{pmatrix},\qquad
B=\begin{pmatrix}3/2&1/2\\1/2&3/2\end{pmatrix}.
\]

Estas matrices tienen los mismos invariantes `tr(A)=tr(B)=3` y `det(A)=det(B)=2`, y una se obtiene de la otra mediante cambio ortogonal de orientación. Sin embargo, **no** existe un escalar `c` para el que `B=cA`. Es un ejemplo de **equivalencia relacional sin escalamiento proporcional**. No prueba que el flujo del toroide tenga exactamente esa simetría; ilustra la diferencia lógica que pedía la ontología.

## 4. No confundir normalizar con cerrar

**[DEFINICIÓN CANDIDATA]** Sea `C(t)` el conjunto de restricciones efectivas del entorno y `\mathcal F_N` la familia de configuraciones que conservan las referencias de `G_N`. Un **cierre propio viable** durante `[t_0,t_1]` existe si hay una trayectoria `z(t)` que, durante ese intervalo, satisface las restricciones de compatibilidad y no excede los recursos de su sistema:

\[
\exists z(t)\in\mathcal F_N:\quad
|F_i(z(t),t)|\le\varepsilon_i,
\quad \sum_j w_j(z(t),t)\le 1.
\]

Los `F_i`, `w_j` y tolerancias `\varepsilon_i` tienen que definirse operacionalmente en cada experimento. La condición de capacidad solo procede cuando los pesos representan partes de un recurso común; **no** se impone indiscriminadamente a toda magnitud.

Poder escribir todas las fracciones con un denominador común es necesario para cierto tipo de representación discreta, pero **no suficiente** para que una configuración sea dinámica o físicamente estable. Si las restricciones se vuelven incompatibles, la regla candidata permite otra geometría, otra orientación o varias unidades nuevas con cierre propio. Decir que el nuevo cierre es «mejor» exige identificar una medida concreta: menor incompatibilidad, menor costo bajo restricciones o mayor persistencia; esas medidas no son universalmente equivalentes.

## 5. La restricción crucial: reescalar indefinidamente no garantiza regularidad

**[DERIVACIÓN MATEMÁTICA · Contraejemplo abstracto]** Podemos tomar `N_n=2^n` y tiempos `t_n=T(1-2^{-n})`. Todas las familias se incluyen: `G_{N_n} ⊆ G_{N_{n+1}}`. Sin embargo, hay infinitos refinamientos antes del tiempo finito `T`. Por ello:

\[
\boxed{\text{normalizador conservado}\;\not\Rightarrow\;\text{cota dinámica uniforme}.}
\]

No es un contraejemplo a Navier–Stokes, sino una demostración de que **la sola aritmética del cierre no excluye una cascada en tiempo finito**.

## 6. Puente propuesto con Navier–Stokes 3D

Para soluciones suaves, incompresibles, viscosas y sin forzamiento en `\mathbb R^3` con decaimiento suficiente, sean `\omega=\nabla\times u`, `q=|\omega|`, `\xi=\omega/q` donde `q>0`, `S=(\nabla u+\nabla u^\top)/2` y `\alpha=\xi^\top S\xi`. La identidad exacta de enstrofía es

\[
\frac{d}{dt}\underbrace{\frac12\int q^2\,dx}_{E(t)}
=\int q^2\alpha\,dx
-\nu\int|\nabla q|^2\,dx
-\nu\int q^2|\nabla\xi|^2\,dx.
\]

**[HIPÓTESIS DE PUENTE FÍSICO]** Identificar en estructuras vorticiales un normalizador dinámico **medible independientemente** (por ejemplo, mediante razones de fases y radios de movimientos distinguibles) que prediga cuándo la incompatibilidad entre proyecciones produce cambios geométricos, transporte y/o disipación suficientes. El cambio de topología no basta: debe conectarse con términos específicos del balance anterior.

**[OBJETIVO CONDICIONAL]** Si desde las ecuaciones y la geometría se obtiene, sin presuponer ya el resultado buscado,

\[
\int q^2\alpha\,dx-\nu\int q^2|\nabla\xi|^2\,dx
\le K(t)E(t),\qquad \int_0^T K(t)\,dt<\infty,
\]

entonces, por el balance y Grönwall,

\[
E(t)\le E(0)\exp\left(\int_0^tK(s)\,ds\right).
\]

El control de enstrofía que resulta es un criterio de continuación de regularidad para una solución suave, pero **la hipótesis sobre `K` no está demostrada de manera universal**. Esta condición es una meta de prueba; no se presenta como un teorema nuevo del programa ni como solución del problema del milenio.

## 7. Qué quedó acreditado y qué permanece abierto

**[ACREDITADO]** La inclusión `G_N ⊆ G_M` si `N|M`; la elección mínima `M=mcm(N,b)` para expresar denominadores `N,b`; la existencia de ejemplos de equivalencia geométrica sin homotecia; el balance exacto de enstrofía en su dominio de validez.

**[NO ACREDITADO]** Que cada torbellino admita un normalizador entero finito elegido por la dinámica; que toda relación entre escalas sea conmensurable; que la ruptura de compatibilidad cause necesariamente reorientación disipativa; que los cambios de cierre excluyan refinamientos infinitos en tiempo finito; o que el control de `K(t)` se siga de la ontología.

**[PRUEBA PROPUESTA]** Fijar una definición independiente y reproducible de `N` y del desajuste de las dos proyecciones; identificar cambios de cierre con series temporales de orientación, estiramiento, enstrofía y radio; comprobar si las transiciones preceden sistemáticamente a los picos de estiramiento y ofrecen una cota cuantitativa; intentar construir flujos adversariales para refutar la regla.

## Conclusión formal provisional

La aportación ontológica es más estricta que «el resto genera una escala»: **la unidad se compara mediante una reflexión interna; el normalizador constituye la referencia común y conserva la familia de relaciones acreditadas; una relación pendiente solo puede participar de un nuevo cierre respetando esa compatibilidad; si no puede sostenerse, se abre una reorganización de topología o de cierre propio**. La aritmética construye una representación exacta de una parte de este principio. El trabajo físico pendiente es demostrar que esa restricción geométrica obliga al balance dinámico necesario para controlar la vorticidad.
