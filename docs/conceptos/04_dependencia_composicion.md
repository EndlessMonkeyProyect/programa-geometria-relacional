# 4. Dependencia y composición entre cierres

## Qué pertenece a la relación

Sean interfaces \(K_A,K_B\) y un soporte conjunto no vacío \(\Gamma_{AB}\subseteq K_A\times K_B\). Sus proyecciones son \(A_\Gamma,B_\Gamma\). Hay dependencia de soporte cuando

\[
\Gamma_{AB}\subsetneq A_\Gamma\times B_\Gamma.
\]

El déficit combinatorio es

\[
D_R=\log_2\frac{|A_\Gamma||B_\Gamma|}{|\Gamma_{AB}|}.
\]

D_R = 0 caracteriza el producto completo. No es información mutua de Shannon y no determina todo el contenido de la relación: soportes distintos pueden tener la misma cardinalidad.

La igualdad binaria conserva los dos márgenes {0,1} y sólo admite {00,11}. Su déficit es un bit. La dependencia restringe combinaciones sin tener que eliminar estados locales.

## Compatibilidad de canales

Conocer únicamente el tamaño de dos conjuntos no determina qué puede interactuar. MF-56 incluye respuestas admisibles y tipos compartidos. MF-57 propone transformaciones que entrelacen representaciones:

\[
T\rho_A(g)=\rho_B(g)T.
\]

Este criterio restringe canales, pero debe exigirse un canal operativo no trivial cuando corresponda: el mapa cero satisface la igualdad y por sí solo no acredita interacción. La selección del evento no se deduce de la existencia del canal.

## Composición exacta disponible

Para \(F_A(X,S)\) y \(F_B(S,Y)\), con X e Y disjuntos y única frontera común S:

\[
B_A=\{s:\exists x\,F_A(x,s)\},\qquad
B_B=\{s:\exists y\,F_B(s,y)\}.
\]

Entonces

\[
F_A\land F_B\text{ es SAT}\iff B_A\cap B_B\ne\varnothing.
\]

La recíproca funciona porque los testigos interiores pueden unirse sin compartir otras variables. Una nueva frontera se obtiene uniendo relaciones y proyectando variables internas. Es composición semántica exacta.

Ejemplo: x = s y s = y generan x = y al proyectar s. La relación conjunta conserva una dependencia que no aparece en los márgenes x e y tomados por separado.

## Qué no se deduce

No se deduce que el soporte tenga cuatro elementos, que la composición produzca un residuo vectorial perpendicular ni que su representación sea polinómica. Una frontera tabulada sobre k variables puede necesitar \(2^k\) entradas.

MF-62B muestra que la dificultad puede permanecer entre dos sectores tratables incluso sin residuo general: toda cláusula exacta de tres literales es Horn o dual-Horn. Ambos sectores pueden ser satisfacibles y su conjunción no.

## Fuentes

- [MF-56](../../fuentes/originales/MF56_RELATIONAL_DEPENDENCE_AND_CHANNELS.md).
- [MF-61B](../../fuentes/originales/MF61B_COORDINATION_AND_SHARED_BOUNDARY.md).
- [MF-62B](../../fuentes/originales/MF62B_HYBRID_FRONTIER_HORN_DUAL_HORN_NO_GO.md).
- [La dificultad entre cierres](../../fuentes/originales/DIFFICULTY_BETWEEN_CLOSURES_ES.md).

Siguiente: [realización geométrica](05_reflexion_geometria.md).
