# Auditoría adversarial v0.79

## DEMOSTRADO

1. Las cápsulas exactas de prefijos son clases de igualdad de funciones residuales.
2. El ancho \(W_\pi(k)\) cuenta exactamente futuros inequivalentes bajo un orden de referencia.
3. En la familia \(F_m=\bigwedge_i(x_i\leftrightarrow y_i)\), el orden \(x_1,\ldots,x_m,y_1,\ldots,y_m\) produce \(W(m)=2^m\).
4. Un árbol explícito de aridad máxima cuatro con \(W\) hojas necesita al menos \(\lceil(W-1)/3\rceil\) nodos internos.
5. Paridad requiere sólo dos estados residuales bajo la representación natural.

## NO-GO

\[
\text{capacidad local 4}\not\Rightarrow\text{compresión global}.
\]

La explosión puede reaparecer como:
- número de cápsulas;
- ancho de interfaz;
- costo de descubrir referencias;
- costo de acreditar equivalencia.

## CONTROL POSITIVO

La misma familia de igualdad tiene una representación pequeña bajo un orden intercalado. Esto prueba que el ancho exponencial puede ser artefacto de una referencia mala.

## HIPÓTESIS ABIERTA

Una regla endógena de “quinta novedad” podría tal vez descubrir referencias que mantengan pequeño el futuro relevante sin búsqueda combinatoria.

No existe todavía prueba de que funcione para 3-SAT general.

## CONEXIÓN CON P vs NP

Si esa regla fuera uniforme, exacta y polinómica para toda 3-SAT, implicaría \(P=NP\).

Actualmente: **OPEN**.
