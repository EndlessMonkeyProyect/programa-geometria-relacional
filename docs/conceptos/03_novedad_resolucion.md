# 3. Novedad, resolución y nueva referencia

## Dos cambios

La novedad amplía las comparaciones; la resolución restringe realizaciones. Dado un evento e con comparaciones D y restricción Y:

\[
X'=X\cap Y,\qquad C'=C\cup D,\qquad K'=X'/{\sim_{C'}}.
\]

La regla determina el estado condicionado al evento. No determina qué evento ocurre. Si X' es vacío, el resultado es contradicción \(\bot\); no se calcula logaritmo de cero.

## Criterio exacto

Una comparación nueva c es redundante si existe una función sobre el cierre previo que reconstruya su respuesta:

\[
Q_c=\bar Q_c\circ q_C.
\]

En sistemas finitos no vacíos esto equivale a que c no divida ninguna clase. La novedad es

\[
\nu(c\mid C)=\log_2\frac{|K_{C+c}|}{|K_C|}.
\]

Para una comparación binaria, si N clases previas incluyen s clases divididas, \(N'=N+s\); de ahí \(0\le\nu\le1\). Un bit es la capacidad máxima de apertura de esa comparación, no el incremento obligatorio en todo contexto.

## Independencia plena y novedad parcial

MF-58 usa la imagen de la firma \(\Phi_C\). La independencia de soporte exige

\[
\operatorname{im}\Phi_{C+c}
=\operatorname{im}\Phi_C\times\operatorname{im}Q_c.
\]

Es más fuerte que no-factorización. No es independencia probabilística sin una distribución.

Para s = 0011, x = 0101 e y = 0001:
- x añade un bit a s;
- y añade \(\log_2(3/2)\) bits a s;
- y es redundante cuando ya se conocen s y x, pues y = s AND x.

La dependencia funcional no satisface en general el intercambio de los matroides. No existe por ello una «base lineal» universal de comparaciones.

## Alcance de una nueva referencia

La no-factorización obliga a enriquecer la descripción si se quiere responder la nueva pregunta. No determina un operador geométrico único, una dirección espacial ni la relación algebraica entre dos generadores.

MF-57 expresa la extensión como \(\mathcal A_{k+1}=\langle\mathcal A_k,R_{k+1}\rangle\), pero deja abiertas las relaciones cruzadas entre referencias.

## Fuentes

- [MF-55](../../fuentes/originales/MF55_ONTOLOGICAL_TRANSITION_RULE.md).
- [MF-58](../../fuentes/originales/MF58_RELATIONAL_INDEPENDENCE_AND_RANK.md).
- [Nueva diferencia, nueva referencia](../../fuentes/originales/NEW_DIFFERENCE_NEW_REFERENCE_ES.md).
- [Diferencia independiente y dimensión](../../fuentes/originales/INDEPENDENT_DIFFERENCE_AND_DIMENSION_ES.md).

Siguiente: [relaciones entre cierres](04_dependencia_composicion.md).
