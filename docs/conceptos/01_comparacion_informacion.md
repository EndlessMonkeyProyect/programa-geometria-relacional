# 1. Comparación e información local

## Concepto

Una diferencia adquiere contenido para un marco si al menos una comparación admite respuestas distintas. La información es contextual: no se asigna aquí como una cantidad absoluta a una cosa aislada.

Para un conjunto no vacío X, una familia de comparaciones C y respuestas Q, definimos

\[
x\sim_C y\iff Q(x,c)=Q(y,c)\quad\forall c\in C.
\]

La firma completa es \(\mathfrak R_C(x)=(Q(x,c))_{c\in C}\). El cociente \(K_C=X/{\sim_C}\) recoge las clases que ese lenguaje distingue. En el caso finito,

\[
I_{\rm dist}(X\mid C)=\log_2|K_C|.
\]

Es una medida de cardinalidad de clases, no una entropía de Shannon a menos que se añada una distribución y se justifique la identificación.

## Resultado

Si C está contenido en C', el segundo contexto refina la partición. Puede separar realizaciones antes indistinguibles; no reúne las que ya estaban separadas. Por tanto \(I_{\rm dist}(X\mid C')\ge I_{\rm dist}(X\mid C)\).

Con C vacío y X no vacío hay una sola clase. No se concluye que el interior carezca de estructura. Sólo que el contrato no distingue sus realizaciones.

## Ejemplo

En X = {00,01,10,11}, observar el primer bit produce dos clases. Observar ambos produce cuatro. Observar únicamente la paridad vuelve a producir dos, pero son clases distintas. El número de clases no determina por sí solo el contenido de las comparaciones.

## Incertidumbre y distinguibilidad

La incertidumbre de Hartley dentro de una cápsula C finita es \(U_H(C)=\log_2|C|\). La distinguibilidad del conjunto de clases es \(\log_2|K|\). Enriquecer las preguntas puede aumentar la segunda y disminuir el tamaño de las clases. No deben intercambiarse estas dos magnitudes por compartir un logaritmo.

## Fuentes

- [MF-54, §§2–9](../../fuentes/originales/MF54_LOCAL_INFORMATION_REFLECTION_AND_BOUNDARY_STATE.md).
- [Lenguaje como reflexión](../../fuentes/originales/LANGUAGE_AS_REFLECTION_LOCAL_INFORMATION_ES.md).
- [Núcleo v0.78, §§II–III](../../fuentes/originales/NUCLEO_INTEGRADO_v0_78.md).

Siguiente: [frontera y cierre](02_frontera_cierre.md).
