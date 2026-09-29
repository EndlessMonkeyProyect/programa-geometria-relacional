# Auditoría adversarial v0.83

## DERIVADO

Bajo una acción libre de \(C_4\):

- toda órbita tiene tamaño 4;
- la cardinalidad total es múltiplo de 4;
- una quinta imagen fuera de la primera órbita pertenece a otra órbita;
- si el conjunto debe cerrarse bajo la acción, esa imagen obliga a incorporar cuatro estados y el mínimo pasa de 4 a 8;
- con dos órbitas, el índice de órbita contiene 1 bit;
- una órbita de cuatro estados contiene 2 bits de fase discreta.

## CORRECCIÓN

No es válido:

\[
J^4=I\Rightarrow4\text{ bits}.
\]

Tampoco es válido:

\[
J^4=I\Rightarrow16.
\]

El \(16\) sólo aparece si se introduce y justifica un segundo nivel de cierre de cuatro órbitas.

## HIPÓTESIS

- La acción relevante es libre.
- La identidad exige cierre de órbita completa.
- El operador de orden cuatro es ontológicamente privilegiado.
- Los cierres inferiores se convierten en unidades sobre las que actúa un operador análogo en el siguiente nivel.

## ABIERTO

1. Derivar la libertad de la acción desde la ontología.
2. Derivar la herencia \(J_k\mapsto J_{k+1}\).
3. Determinar si la jerarquía corresponde a las “octavas” históricas.
4. Construir un cociente computable para restricciones no afines.
5. Probar o refutar relevancia para P vs NP.

## NO-GO

Una reducción constante por 4 no cambia la clase exponencial:

\[
2^n/4=2^{n-2}.
\]

Para complejidad hace falta una reducción estructural recursiva cuyo costo total sea polinómico.
