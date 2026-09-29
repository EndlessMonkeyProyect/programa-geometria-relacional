# 10. Computación, acreditación y coordinación

## Qué se busca

La rama computacional pregunta si una representación suficiente puede construirse y actualizarse sin enumerar todas las alternativas. Deben medirse por separado longitud, acreditación, actualización y decisión.

Que SAT/UNSAT sea un bit no acota el trabajo requerido para obtenerlo. MF-59B muestra directamente que decidir redundancia de una cláusula puede contener la dificultad de UNSAT: una fórmula G sobre variables originales implica una cláusula sobre tres variables frescas si y sólo si G es insatisfacible.

## Controles positivos y sus límites

Horn admite propagación; XOR, eliminación lineal; 2-SAT, implicaciones y componentes fuertemente conexas. Son algoritmos conocidos y las fuentes los usan como controles.

La mezcla de sectores no hereda automáticamente su tractabilidad. MF-62B particiona cláusulas exactas de tres literales en Horn y dual-Horn; coordinar ambos sectores contiene el problema general aunque cada sector posea un testigo trivial.

## Cápsulas de futuros

En v0.79, dos prefijos pertenecen a la misma cápsula si inducen la misma función sobre todas las continuaciones. Para un orden π:

\[
W_\pi(k)=|\{F_\alpha:\alpha\in\{0,1\}^k\}|.
\]

Es un número de funciones residuales, no una órbita de cuatro fases.

En \(F_m=\bigwedge_i(x_i\leftrightarrow y_i)\), fijar todos los x antes de los y genera \(2^m\) futuros distintos. Intercalar parejas conserva ancho pequeño. Una representación mala puede crecer exponencialmente incluso para una familia fácil.

Organizar W hojas en un árbol de aridad cuatro necesita al menos \(\lceil(W-1)/3\rceil\) nodos internos. Reducir profundidad no garantiza reducir el tamaño total.

## Selector de referencia v0.80

\(\Gamma_0\) es una heurística de ordenación basada en incidencias y frontera. No es el operador de relajación de v0.89.

Los resultados adjuntos reportan 24 instancias plantadas pequeñas y siete controles. En las 24, \(\Gamma_0\) alcanza el ancho óptimo reportado en 14. Son controles finitos, sin garantía asintótica y sin código generador incluido en este corpus. El óptimo de laboratorio usa búsqueda exacta sobre subconjuntos; no forma parte del selector.

## Contrato para una consecuencia sobre P versus NP

Una solución general requiere, de forma uniforme:
- representación exacta de tamaño polinómico;
- construcción y actualización polinómicas;
- acreditación de las equivalencias necesarias;
- número polinómico de pasos;
- decisión correcta de vacío y recuperación de la respuesta.

Las fuentes no satisfacen conjuntamente ese contrato para toda 3-SAT. Tampoco prueban que ningún método pueda hacerlo. Los obstáculos de una representación particular no demuestran P distinto de NP.

## Fuentes

- [MF-59B](../../fuentes/originales/MF59B_3SAT_ACCREDITATION_BARRIER.md).
- [MF-60B](../../fuentes/originales/MF60B_COMPOSABLE_LOCAL_CERTIFICATES.md).
- [MF-61B](../../fuentes/originales/MF61B_COORDINATION_AND_SHARED_BOUNDARY.md).
- [v0.79](../../fuentes/originales/CAPSULE_SAT_EXPERIMENT_v0_79.md).
- [v0.80](../../fuentes/originales/GAMMA_REFERENCE_OPERATOR_v0_80.md).
- [Guía de datos](../../datos/README.md).

Continuar con [resultados y dependencias](../trazabilidad/RESULTADOS.md).
