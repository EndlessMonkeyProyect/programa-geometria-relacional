# O27 — La perpendicularidad del remolino: magnitud, orientación y cierre suficiente

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 19 de octubre de 2026**  
**Estado:** suplemento matemático/ontológico independiente; no constituye nueva ley física ni prueba de regularidad 3D.

## 0. Pregunta de continuidad

El autor propone que la insuficiencia de información hallada en O26 puede requerir una relación «perpendicular» y, quizá, una dimensión adicional. La investigación conserva dos distinciones: (i) una *diferencia informacional* nueva no es necesariamente una dimensión espacial nueva; (ii) la jerarquía espectral no cerrada de O26 ya aparece en flujos bidimensionales, mientras el estiramiento de vorticidad es un mecanismo físico adicional característico de la geometría 3D.

**Resultado:** una descomposición exacta en dos componentes, una paralela y otra perpendicular a la dirección vorticial, pone a prueba la intuición sin introducir geometría externa a Navier–Stokes. Es compatible con el orden del núcleo «complemento antes de ortogonalidad»: la ortogonalidad aquí pertenece solo a la realización euclídea posterior.

## 1. Ecuación base [T: clásica bajo regularidad]

En un dominio periódico o sin términos de frontera, con viscosidad `nu>0`, consideremos soluciones suaves de Navier–Stokes incompresible sin fuerza:

\[
\partial_t u+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,\qquad \nabla\cdot u=0.
\]

La vorticidad \(\omega=\nabla\times u\) obedece:

\[
D_t\omega=(\omega\cdot\nabla)u+\nu\Delta\omega,\qquad D_t=\partial_t+u\cdot\nabla.
\]

Introduzcamos \(S=(\nabla u+\nabla u^\top)/2\). La parte antisimétrica \(\Omega=(\nabla u-\nabla u^\top)/2\) satisface \(\Omega\omega=0\), por lo que:

\[
\boxed{D_t\omega=S\omega+\nu\Delta\omega.}\tag{1}
\]

Este resultado ya estaba en el *Módulo canónico de cierre y no concentración* del programa y en los desarrollos NS previos: O27 **lo recupera**, no reclama prioridad matemática.

## 2. Descomposición exacta [T]

Donde \(q=|\omega|>0\), sea \(\xi=\omega/q\). Definimos:

\[
\alpha=\xi^\top S\xi,\qquad
\eta=(I-\xi\xi^\top)S\xi.
\]

Así:

\[
\boxed{S\xi=\alpha\xi+\eta,\qquad \eta\cdot\xi=0,\qquad |S\xi|^2=\alpha^2+|\eta|^2.}\tag{2}
\]

- \(\alpha\) es la componente de deformación que produce crecimiento o decrecimiento local de la **magnitud** de la vorticidad.
- \(\eta\) es la componente **transversal** de deformación que puede reorientar la vorticidad.
- \(\eta\) es un vector en el plano perpendicular a \(\xi\) dentro de \(\mathbb R^3\); no hace falta una dimensión espacial cuarta.

**Importante:** \(\alpha\ne0\) puede ocurrir con \(\eta=0\) y viceversa. Una perpendicular no es condición necesaria del estiramiento en magnitud; una perpendicular no garantiza amortiguación.

## 3. Magnitud y dirección son ecuaciones diferentes [T]

A partir de (1) y \(\omega=q\xi\), usando \(\xi\cdot\Delta\xi=-|\nabla\xi|^2\), se obtiene:

\[
\boxed{(D_t-\nu\Delta)q=\bigl(\alpha-\nu|\nabla\xi|^2\bigr)q.}\tag{3}
\]

La dirección evoluciona según:

\[
\boxed{D_t\xi=\eta+\nu\left[\Delta\xi+|\nabla\xi|^2\xi+\frac2q(\nabla q\cdot\nabla)\xi\right].}\tag{4}
\]

El término angular disipativo \(-\nu q|\nabla\xi|^2\) en (3) ya figuraba en antecedentes NS del programa. La ecuación (4) separa la reorientación inducida por \(\eta\) y la difusión de la dirección.

En un punto de máximo espacial positivo de \(q\), \(\Delta q\le0\) y \(u\cdot\nabla q=0\); por tanto, siempre que se satisfagan las condiciones de regularidad para evaluar esas derivadas:

\[
\partial_t\log q\le\alpha-\nu|\nabla\xi|^2.\tag{5}
\]

Esta desigualdad local **no** es una cota global uniforme: para demostrar regularidad 3D falta controlar el efecto de \(\alpha\) frente al término angular. En particular, \(\eta\) puede ser cero donde \(\alpha\) es positivo.

Para la enstrofía \(A=\int |\omega|^2dx\) y palinstrofía \(B=\int|\nabla\omega|^2dx\), en régimen periódico no forzado:

\[
\boxed{\dot A=2\int q^2\alpha\,dx-2\nu B.}\tag{6}
\]

Es el enlace exacto con la escala espectral de O25 \(\ell_\omega=\sqrt{A/B}\): la producción global de enstrofía recoge la componente paralela \(\alpha\), mientras las variaciones direccionales y de gradiente entran en los balances de orden superior. O26 ya mostró que \((H,A,B)\) no es una interfaz suficiente para predecir \(\dot\ell_\omega\) en general.

## 4. Por qué 2D y 3D son diferentes [T]

Para \(u=(u_1(x,y,t),u_2(x,y,t),0)\), independiente de \(z\), la vorticidad tiene forma \(\omega=(0,0,\zeta)\) y \(\partial_z u=0\). Por ello \((\omega\cdot\nabla)u=0\), y \(S\omega=0\). Consecuentemente, donde \(q>0\):

\[
\boxed{\alpha=0,\quad \eta=0,\quad
\partial_t\zeta+u\cdot\nabla\zeta=\nu\Delta\zeta.}\tag{7}
\]

Sin fuerza, esta ecuación escalar permite aplicar un principio del máximo para la vorticidad bidimensional. No obstante, **la existencia de una ecuación de vorticidad más simple no hace suficientes los primeros momentos espectrales**: el contraejemplo O26 vive en una familia bidimensional de cizallas exactas y sigue siendo válido.

En 3D el vector \(S\omega\) puede presentar componentes longitudinales y transversales. El estiramiento no implica automáticamente singularidad: existen flujos suaves con \(\alpha\) y \(\eta\) no nulos.

## 5. Laboratorio exacto: un mismo flujo 3D y dos mecanismos [E/T]

Sea el campo ABC periódico de parámetros unitarios en el toro \((2\pi\mathbb T)^3\):

\[
U=(\sin z+\cos y,\ \sin x+\cos z,\ \sin y+\cos x).
\]

Identidades directas \(\nabla\cdot U=0\), \(\nabla\times U=U\), \(\Delta U=-U\), \((U\cdot\nabla)U=\nabla(|U|^2/2)\) permiten construir una solución suave exacta para toda \(t\ge0\):

\[
\boxed{u(x,t)=e^{-\nu t}U(x),\qquad p(x,t)=-\tfrac12|u(x,t)|^2.}\tag{8}
\]

En \(t=0\), dos puntos de este **mismo** flujo:

| Punto | \(U\) | \(\alpha\) | \(\eta\) |
|---|---|---:|---|
| \((0,0,0)\) | \((1,1,1)\) | \(1\) | \((0,0,0)\) |
| \((\pi/2,0,0)\) | \((1,2,0)\) | \(0\) | \((0,0,1/\sqrt5)\) |

Los valores son simbólicamente exactos. Ilustran que la intensidad y el cambio transversal son distinguibles sin salir del espacio 3D. Aunque existe estiramiento local positivo en el primer punto, el flujo completo decae suavemente; no toda producción local genera inestabilidad global. Para tiempo \(t\) arbitrario, \(\alpha\) y \(\eta\) se multiplican por \(e^{-\nu t}\).

**Control 2D:** \(u_2(x,y,z,t)=e^{-\nu t}(\sin y,0,0)\) también resuelve NS exactamente, con \(S\omega=0\).

`laboratorio_o27.py` verifica las identidades de ambos flujos, las dos componentes y la ortogonalidad con aritmética simbólica; las pruebas no son una DNS ni una prueba global de regularidad.

## 6. Puente con el lenguaje canónico del programa [O/D]

| Término del programa | Correspondencia propuesta | Límite de la interpretación |
|---|---|---|
| **Unidad/cierre propio** | Campo vorticial considerado respecto de un contrato de observables | No acredita conservación global de una «identidad física» |
| **Foco/referente** | Dirección local \(\xi\), o escala global \(\ell_\omega\) según el contrato | Son objetos diferentes y no pueden intercambiarse |
| **Proyección** | \(\alpha\xi\): parte del estiramiento en la dirección observada | No es la proyección ontológica primitiva |
| **Complemento** | \(\eta\): deformación no contenida en la componente longitudinal | Es ortogonal solo porque ya elegimos producto interno euclídeo |
| **Diferencia pendiente** | Dos estados pueden coincidir en firma \(\Phi\) y diferir en orientación o altos momentos | O26 prueba no suficiencia incluso si \(\eta=0\) |
| **Comunes/trama** | Identidades \((1)\)–\((6)\) que enlazan intensidad, dirección y viscosidad | No implican un algoritmo de predicción económica |
| **Ritmo y escala** | \(\ell_\omega\), y relación modal preexistente \(R\omega_{\rm modal}=v_*\) | \(v_*\) no es automáticamente velocidad física de la luz ni del flujo |

La frase «la incertidumbre solicita una perpendicular» puede formularse condicionalmente: *si las consultas futuras incluyen reorientación vorticial, una firma que solo registra estiramiento paralelo es insuficiente; el componente perpendicular es una distinción necesaria para esas consultas*. No se deduce que ese canal cierre todas las demás preguntas dinámicas.

Una firma candidata de observables para una prueba posterior podría ser
\(\Phi=(A,B,\int q^2\alpha dx,\int q^2|\eta|^2dx,\int q^2|\nabla\xi|^2dx)\), **sin afirmar suficiencia**. En particular, no contiene automáticamente todos los momentos superiores ni toda la información de transporte no local.

## 7. Falsadores y clasificación ROSI

- **[RESOLVED / clásico]** descomposición ortogonal (2), ecuaciones (3)–(4) bajo \(q>0\), desaparición de estiramiento (7) en flujos 2D y equivalencia de (8) con NS, bajo sus hipótesis.
- **[RESOLVED / control]** ejemplos 3D de \(\alpha>0,\eta=0\) y \(\alpha=0,\eta\ne0\) con la misma solución exacta.
- **[NO-GO]** concluir que la no suficiencia de O26 obliga a una dimensión espacial nueva: ya ocurre en 2D.
- **[NO-GO]** concluir que la componente perpendicular impide concentración: \(\alpha\) puede ser positiva cuando \(\eta=0\).
- **[NO-GO]** identificar la nueva comparación dinámica con cuarta dimensión espacial sin hipótesis de inmersión y métrica.
- **[OPEN]** ¿qué gramática de interfaces más pequeña conserva las consultas dinámicas pertinentes en 3D, con costo controlado, y permite derivar un límite a priori no contenido ya en NS?
- **[OPEN]** relación operativa demostrable entre reflexión tetraédrica, foco de los espejos y dirección de vorticidad, sin imponer equivalencias solo por analogía.

## 8. Procedencia preservada

Se recupera sin reescribir: (i) Núcleo Generativo Canónico: complemento anterior a ortogonalidad; (ii) módulo canónico de cierre y no concentración (septiembre 2026), en particular \(D_t\omega=S\omega+\nu\Delta\omega\) y (3); (iii) O25: \(\ell_\omega=\sqrt{A/B}\); (iv) O26: contraejemplo de no suficiencia y jerarquía de momentos; (v) MF-86: suficiencia y composicionalidad relativa a preguntas; (vi) ritmo-radio espectral \(R_i\omega_i=v_*\) como relación de otro sector del programa.

**Declaración de alcance:** O27 organiza y verifica relaciones clásicas para explorar una tesis ontológica del programa. No demuestra una teoría física nueva, Navier–Stokes global 3D ni equivalencia física del cubo de espejos.
