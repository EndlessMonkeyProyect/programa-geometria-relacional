# 8. Bits, pesos y escalas

## Cuatro estados y cuatro roles

Una órbita con cuatro estados requiere dos bits para identificar un estado. Para disponer de dieciséis configuraciones se necesita otra construcción: registrar presencia o ausencia independiente de cuatro roles, o una estructura equivalente que justifique ese repertorio.

La v0.85 declara el puente booleano: todos los subconjuntos de n roles. Su cardinalidad es \(2^n\). El espacio libre sobre roles distingue etiquetas que pueden tener imágenes linealmente dependientes en el plano geométrico; esto no agrega automáticamente dimensiones físicas.

## Álgebra exterior y Clifford

\(\Lambda^\bullet F_n\) tiene dimensión \(2^n\). La v0.86 utiliza la completitud de Clifford de un espacio cuadrático formal de n generadores. Elegir ese espacio de roles, su forma cuadrática y su pertinencia son condiciones adicionales.

La independencia de soporte de observables no implica por sí sola las relaciones de Clifford. MF-57 ya advertía contra imponer relaciones cruzadas entre generadores sin derivación. La construcción puede adoptarse como modelo condicional, no presentarse como consecuencia inevitable de no-factorización.

## Peso uniforme

En un espacio de coeficientes de dimensión D = \(2^n\), un operador positivo de traza uno invariante bajo todas las permutaciones y cambios independientes de signo de la base debe ser

\[
\rho_0=I/D.
\]

Entonces \(w(P)=\operatorname{Tr}(\rho_0P)=\operatorname{rank}(P)/D\). Un sector de rango uno pesa \(2^{-n}\); su complemento pesa \(1-2^{-n}\).

Esta simetría sobre todos los canales es más fuerte que permutar los generadores. Tampoco es automáticamente una simetría de automorfismos del álgebra de Clifford, que preservan la unidad. La homogeneidad debe justificar qué transformaciones admite y qué estructura retiene.

## Corrección de v0.86, §9 — revisión editorial

El vector uniforme \(|\Omega\rangle=D^{-1/2}\sum_i|i\rangle\) y el estado mixto I/D coinciden para mediciones diagonales en esa base, pero no para todos los proyectores. El primero es puro; no es una purificación del segundo dentro del mismo espacio.

Sobre \(P_\Omega=|\Omega\rangle\langle\Omega|\), los pesos son respectivamente 1 y 1/D. El teorema de uniformidad del estado mixto permanece válido bajo sus hipótesis. Una purificación requiere un espacio auxiliar y reducción parcial.

## Escala y correspondencia física

El puente de octava de v0.84 adopta una identificación fiel \(C_4\to\mathbb R/\mathbb Z\) en una escala logarítmica binaria. Bajo esa elección, el generador corresponde a ±1/4 de octava, con factor \(2^{\pm1/4}\). No deriva la base dos desde la órbita.

Si se identifica un peso con \(\omega_V^2/\omega^2=2^{-n}\), resulta \(R_V/R_U=2^{n/2}\) para radios definidos como c/frecuencia. La interpretación física de esos radios, el entero n y el observable medido siguen siendo puentes.

El 1:3 de v0.85 proviene del libro de dos roles proyectivos. El 1:3 de v0.90 cuenta una referencia y tres estados restantes de C4. La misma razón numérica no demuestra identidad entre ambas construcciones.

## Fuentes

- [v0.81](../../fuentes/originales/REFLEXION_ESCALA_BIT_v0_81.md).
- [v0.84](../../fuentes/originales/CIERRE_ALGEBRAICO_MINIMO_v0_84.md).
- [v0.85](../../fuentes/originales/PUENTE_BOOLEANO_C2_C4_v0_85.md).
- [v0.86](../../fuentes/originales/MEDIDA_INVARIANTE_PESO_BINARIO_v0_86.md).
- [v0.90](../../fuentes/originales/REFLEXION_CIERRE_CUATRO_v0_90.md).

Siguiente: [totalidad y tiempo](09_totalidad_tiempo_fisica.md).
