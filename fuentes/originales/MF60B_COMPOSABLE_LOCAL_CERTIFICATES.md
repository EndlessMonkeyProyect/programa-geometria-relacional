# MF-60B — Certificados locales composables: existencia, verificación y generación

**Versión:** v0.68-research  
**Rama:** complejidad / cierre acreditable.  
**Nota:** se usa MF-60B para no colisionar con el MF-60 histórico del programa.

## 1. Problema

MF-59B localizó una barrera: saber que una nueva restricción “ya cabe” en el cierre puede ser coNP-completo.

La respuesta natural es intentar que el propio cierre transporte una prueba local de su suficiencia.

Definimos una cápsula certificada:

\[
\boxed{\mathfrak K_t=(K_t,w_t)}
\]

donde:

- \(K_t\) es el estado de cierre;
- \(w_t\) es un certificado de por qué ese estado sigue representando exactamente las restricciones acumuladas.

La actualización buscada es:

\[
(K_t,w_t,C_{t+1})
\longrightarrow
(K_{t+1},w_{t+1}).
\]

## 2. Cuatro recursos distintos

No deben confundirse:

1. **Existencia:** ¿existe un certificado pequeño?
2. **Verificación:** dado el certificado, ¿puede comprobarse rápido?
3. **Generación:** ¿puede encontrarse rápido?
4. **Actualización:** ¿puede transformarse localmente al llegar una restricción nueva?

Un certificado puede existir y ser fácil de verificar, pero ser difícil de encontrar.

Por tanto:

\[
\boxed{
\text{existir}\neq
\text{verificar}\neq
\text{generar}\neq
\text{actualizar}.
}
\]

## 3. Consecuencia condicional para UNSAT

UNSAT de 3-CNF es un problema coNP-completo.

Si para toda 3-CNF insatisfacible existiera un certificado de tamaño polinómico verificable en tiempo polinómico, entonces UNSAT pertenecería a NP.

Por tanto:

\[
\boxed{
\text{certificados polinómicos verificables para todo 3-UNSAT}
\Rightarrow
NP=coNP.
}
\]

Esto no afirma que tales certificados no existan. Identifica la consecuencia de que existan universalmente.

## 4. Consecuencia más fuerte para generación incremental

Suponga además que:

- el estado y certificado tienen tamaño polinómico;
- pueden generarse/actualizarse en tiempo polinómico al incorporar cada cláusula;
- el estado certificado permite decidir vacío en tiempo polinómico.

Entonces:

\[
\boxed{P=NP.}
\]

La diferencia es importante.

Un sistema de pruebas corto y verificable no es todavía un algoritmo de decisión eficiente: falta generar la prueba.

## 5. Control positivo I — Horn

Una cláusula Horn contiene como máximo un literal positivo y puede leerse como:

\[
x_1\land\cdots\land x_k\Rightarrow y
\]

o, si no tiene literal positivo:

\[
x_1\land\cdots\land x_k\Rightarrow\bot.
\]

El cierre suficiente se obtiene por propagación hacia adelante hasta punto fijo.

El certificado puede contener:

- conjunto de variables ya forzadas a verdadero;
- regla que justificó cada nueva variable;
- regla de contradicción si se alcanza \(\bot\).

La actualización por una nueva cláusula permanece en la misma forma.

Así Horn posee una cápsula composable de tamaño y costo polinómicos.

## 6. Control positivo II — sistemas afines / XOR

Una restricción XOR es una ecuación lineal sobre \(\mathbb F_2\):

\[
a_1x_1+\cdots+a_nx_n=b.
\]

El cierre suficiente puede mantenerse como una base escalonada.

Cada ecuación nueva se reduce contra la base.

Si aparece:

\[
0=1,
\]

se acredita contradicción.

Por tanto la suficiencia se transporta mediante una estructura compacta y una actualización polinómica.

## 7. Control positivo III — 2-SAT

Cada cláusula:

\[
(a\lor b)
\]

induce:

\[
\neg a\Rightarrow b,
\qquad
\neg b\Rightarrow a.
\]

El estado se representa mediante el grafo de implicaciones y sus componentes fuertemente conexas.

Hay contradicción exactamente cuando alguna variable \(x\) y \(\neg x\) pertenecen a la misma componente.

La actualización puede recomputarse en tiempo polinómico sin enumerar \(2^n\) asignaciones.

## 8. Qué tienen en común los controles positivos

En los tres casos existe una **estructura cerrada bajo actualización**:

\[
\boxed{
\text{restricción nueva}
+
\text{estado suficiente}
\longrightarrow
\text{estado suficiente del mismo tipo}.
}
\]

- Horn: punto fijo de implicaciones;
- XOR: subespacio afín / base lineal;
- 2-SAT: cierre por alcanzabilidad en grafo de implicaciones.

La clave no es sólo que el estado sea compacto.

La clave es que el lenguaje de cierre posee una regla de normalización eficiente.

## 9. Control negativo mínimo — 3-SAT y propagación unitaria

Considere las ocho cláusulas de tres literales que excluyen, una por una, las ocho asignaciones de tres variables.

La fórmula completa es UNSAT.

Sin embargo:

- no contiene cláusulas unitarias;
- la propagación unitaria no produce ninguna asignación;
- toda subfórmula propia es satisfacible.

Así una forma de acreditación estrictamente local basada sólo en propagación unitaria es:

\[
\boxed{\text{sound pero incompleta}.}
\]

El ejemplo no demuestra que toda regla local falle.

Demuestra que una regla local candidata concreta puede dejar intacta una contradicción global.

## 10. Lección estructural

La pregunta no es:

> “¿existe alguna información local útil?”

Sí existe.

La pregunta es:

\[
\boxed{
\text{¿existe un lenguaje de certificados cerrado bajo toda actualización 3-SAT,
con normalización y generación polinómicas?}
}
\]

Para Horn, XOR y 2-SAT, tenemos controles positivos.

Para 3-SAT general, esa propiedad permanece abierta y, si incluyera decisión exacta de vacío, resolvería \(P\) vs \(NP\).

## 11. Criterio de una verdadera novedad algorítmica

Una propuesta del programa sólo cuenta como avance hacia \(P=NP\) si exhibe explícitamente:

\[
\boxed{
\mathcal S
=
(\mathrm{State},\mathrm{Witness},
\mathrm{Update},\mathrm{Verify},\mathrm{Empty})
}
\]

y demuestra simultáneamente:

1. exactitud;
2. completitud;
3. tamaño polinómico;
4. generación polinómica;
5. actualización polinómica;
6. detección de vacío polinómica;
7. cierre de la representación bajo todas las 3-cláusulas.

Una analogía informacional no sustituye ninguna de estas siete condiciones.

## 12. Puente ontológico

El cierre ontológico decía:

> conservar sólo las diferencias que aún pueden hacer una diferencia futura.

La versión computacional exige algo adicional:

> conservar además una prueba económicamente actualizable de que ninguna diferencia futura relevante fue descartada.

Por tanto:

\[
\boxed{
\text{cierre computacional}
=
\text{estado suficiente}
+
\text{acreditación composable}.
}
\]

Éste es un refinamiento importante del concepto de cierre.

## 13. Próximo experimento

El siguiente paso debe intentar construir un lenguaje de certificados más expresivo que:

- generalice al menos dos de los controles positivos;
- sobreviva a mezclas de restricciones;
- detecte contradicciones que la propagación unitaria no detecta;
- mantenga tamaño y actualización medibles.

La primera prueba adversarial debe ser una familia mixta, no una instancia aislada.

Si la representación crece exponencialmente o la normalización requiere una consulta semántica global, se registra como no-go.

Si permanece polinómica, se amplía la batería adversarial.

No se considerará avance hacia \(P=NP\) hasta superar explícitamente ese contrato operacional.
