# 5. Reflexión, geometría y órbita de cuatro

## La realización local

La v0.84 parte de un espacio real con producto interno positivo, una referencia R no nula y una operación bilineal antisimétrica. Para A perpendicular a R exige norma compatible, transversalidad y cierre doble. No parte únicamente de distinguibilidad contextual.

Con \(r=\|R\|\), \(T_R(A)=A\times R\) y \(E_R=R^\perp\), la antisimetría y el cierre doble permiten demostrar que E_R es invariante. En él,

\[
J_R=T_R/r,\quad J_R^\ast=-J_R,\quad J_R^\ast J_R=I,
\quad J_R^2=-I.
\]

Por tanto la rama positiva del signo del cierre doble queda excluida. Para A no nulo:

\[
A,\ J_RA,\ -A,\ -J_RA,\ A.
\]

Hay cuatro estados diferentes y una quinta ocurrencia que retorna al primero.

## Qué significa el cuatro

Es el orden de la órbita discreta de esa semilla. El plano real generado por A y JA tiene dimensión dos y contiene infinitos vectores. No se ha demostrado que sólo pueda contener cuatro identidades arbitrarias.

Una fase adicional puede no pertenecer a la órbita discreta y pertenecer al mismo plano. Por ejemplo \((A+JA)/\sqrt2\). Esa novedad de parámetro no es una nueva dirección lineal.

J² = −I sin compatibilidad métrica tampoco implica perpendicularidad para una métrica previamente fijada. La prueba del programa utiliza sus hipótesis adicionales; deben trasladarse al citar el resultado.

## Corrección histórica

MF-57 y v0.84 muestran que la iteración del mismo eje produce

\[
V=-r^2A,\qquad a=-r^2U.
\]

No genera direcciones independientes indefinidamente. También resulta incompatible afirmar simultáneamente V = T_R U, U = V + m y m perpendicular a V para la semilla normalizada no trivial.

La identidad de amplitudes \(\mu^2=r^2(1-r^2)\) puede conservarse como una partición separada, con \(0\le r\le1\) para una amplitud real. No reconstruye la antigua identidad vectorial.

## Novedad en un módulo geométrico

Si W es J-invariante, J es ortogonal y y pertenece al espacio ambiente ya dotado de J, el residuo \(r_y=(I-P_W)y\ne0\) genera la mínima extensión J-invariante

\[
W'=W\oplus\operatorname{span}_{\mathbb R}\{r_y,Jr_y\}.
\]

Esto prueba cómo incorporar una novedad dada en esa realización. No demuestra cómo la interacción de dos cápsulas produce y ni cómo se elige un J nuevo si el ambiente todavía no lo contiene.

## Fuentes

- [MF-57](../../fuentes/originales/MF57_GENERATOR_AUDIT_AND_NEW_REFERENCE_RULE.md).
- [v0.84](../../fuentes/originales/CIERRE_ALGEBRAICO_MINIMO_v0_84.md).
- [v0.83](../../fuentes/originales/TEOREMA_ORBITAS_4_8_v0_83.md).
- [v0.90](../../fuentes/originales/REFLEXION_CIERRE_CUATRO_v0_90.md).

Siguiente: [capas y composición geométrica](06_capas_y_nuevo_operador.md).
