# Auditoría adversarial — v0.80

## Lo que sí se obtuvo

- Definición exacta de \(W_\pi(k)\) por funciones residuales.
- Cálculo exacto del orden óptimo para instancias pequeñas mediante DP sobre subconjuntos.
- Operador \(\Gamma_0\) computable usando sólo incidencias/frontera de restricciones.
- Control de igualdad permutada: \(\Gamma_0\) puede recuperar estructura emparejada sin conocer las parejas por nombre.
- Comparación exacta de \(\Gamma_0\) contra OPT en 3-CNF pequeñas.

## Lo que NO se obtuvo

- Una garantía aproximativa general para \(\Gamma_0\).
- Una cota polinómica de ancho para 3-SAT.
- Un criterio local universal que determine la mejor referencia global.
- Una prueba sobre \(P=NP\).

## No-go actualizado

\[
\text{información local de frontera}
\not\Rightarrow
\text{óptimo global}.
\]

## Hipótesis abierta

La información que falta podría aparecer en un horizonte relacional pequeño \(H_r\). Debe medirse, no asumirse.

## Peligro principal

Si calcular la referencia adecuada requiere horizonte global y búsqueda combinatoria, \(\Gamma\) sólo reubica la dificultad original.
