# Correcciones y pendientes

## Correcciones históricas ya registradas

| ID | Corrección | Fuente y alcance |
|---|---|---|
| H01 | El contador de umbral se recorta por lo que el futuro restante puede distinguir. | MF-54 y VALIDATION v0.62.1. |
| H02 | El signo de cierre doble queda fijado en −1 bajo los postulados métricos. | MF-57; prueba consolidada de invariancia en v0.84. |
| H03 | La antigua identidad U = V + m con m perpendicular a V es incompatible con la iteración declarada. | MF-57 y v0.84. La partición escalar se conserva separada. |
| H04 | Iterar un mismo eje no genera direcciones indefinidamente. | MF-57 y v0.84. |
| H05 | Dependencia funcional no garantiza intercambio ni base de tamaño único. | MF-58 y v0.73. |
| H06 | Monotonía, confluencia o cuatro estados locales no implican tiempo polinómico. | MF-59B–62B y v0.73–80. |
| H07 | Orden de fase cuatro no implica cuatro bits independientes. | v0.81–86 y v0.90. |

## Observaciones de esta revisión editorial

Estas observaciones no reemplazan los originales ni se atribuyen al autor sin revisión.

### E01. Residuo que no puede salir del subespacio

En v0.91, §§4–6, si x_i,x_j pertenecen a L y T_ij preserva L, entonces x_j − T_ij x_i pertenece a L y (I − P_L) lo anula.

**Reparación requerida:** especificar el espacio conjunto y la operación que contiene información no representable por la interfaz previa. MF-61B proporciona una referencia semántica exacta, no una identificación vectorial automática.

### E02. Eje y semilla paralelos

V0.91 toma R = q/||q|| y después usa q como semilla de J. Si J es el producto asociado a R, entonces q × R = 0. El teorema de v0.84 sólo vale en R perpendicular.

**Reparación requerida:** definir otro eje o un J nuevo y justificarlo. Si J es abstracto, declarar la estructura adicional.

### E03. Novedad orbital y lineal distintas

Una fase intermedia no pertenece a la órbita de cuatro y sí a su plano. No-factorización, pertenencia a una órbita y componente fuera de un subespacio son pruebas diferentes.

**Reparación requerida:** enunciar un teorema puente con representaciones y observables explícitos.

### E04. Estado mixto y vector uniforme

V0.86, §9, identifica indebidamente una superposición uniforme con I/D. Coinciden en probabilidades de la base elegida, no en todos los proyectores. El vector del mismo espacio no es una purificación de I/D.

**Reparación requerida:** restringir la equivalencia a observables diagonales o usar una purificación en un espacio ampliado. No afecta al teorema de invariancia del estado mixto.

### E05. Holonomía y diferencias exactas

En v0.72, diferencias de fases globales suman cero en ciclos. En v0.91, imponer universalmente composición independiente del camino con identidades e inversos compatibles impide holonomía no trivial.

**Reparación requerida:** distinguir una conexión en aristas de diferencias exactas; no identificar vínculo directo con todo transporte compuesto.

### E06. Ampliación al pasar de nodos a relaciones

Los gradientes B_1^T x son ortogonales a ciclos en ker B_1. Un flujo armónico general no procede necesariamente de esos gradientes. V0.77–89 permiten cochains generales, pero la integración debe declarar esa ampliación.

### E07. Dos usos de 1:3 y elección de Clifford

Contar tres roles distintos de una referencia en C4 no es la misma construcción que tres canales no escalares del libro de dos roles proyectivos. La completitud de Clifford de roles independientes es una elección adicional, no una consecuencia de independencia de soporte.

### E08. Dominios no vacíos y amplitudes

Las medidas logarítmicas de cardinalidad requieren conjuntos no vacíos. El cierre T de contrato vacío no es el estado ⊥. La amplitud real r sqrt(1−r²) requiere 0≤r≤1.

### E09. Canal trivial

La ecuación de entrelazamiento admite el mapa cero. Para inferir un canal operativo hay que exigir propiedades adicionales apropiadas, como no trivialidad y observables que efectivamente transporte.

## Pendientes priorizados

| ID | Pregunta | Evidencia necesaria para cerrarla |
|---|---|---|
| P01 | ¿Qué datos de una relación conjunta constituyen la nueva referencia? | Construcción de interfaz y prueba de suficiencia respecto de futuros declarados. |
| P02 | ¿Cómo se traduce novedad contextual a residuo geométrico? | Mapas explícitos y demostración de qué distinciones preservan. |
| P03 | ¿Qué determina J del nuevo nivel? | Operador construido desde la composición; dominio, métrica y prueba de J² = −I. |
| P04 | ¿Cómo se relacionan generadores diferentes? | Leyes derivadas o postulados claramente declarados y comprobados. |
| P05 | ¿Cuándo persiste el cierre compuesto? | Dinámica conjunta y criterio de estabilidad; separar estabilidad del estado y robustez del operador. |
| P06 | ¿Qué selecciona eventos y relaciones activas? | Regla independiente de conocer el resultado buscado. |
| P07 | ¿Cómo se conectan escalas y observables físicos? | Unidades, mediciones y predicciones sin calibración circular. |
| P08 | ¿Hay una consecuencia computacional general? | Contrato completo de exactitud y costos de peor caso. |

## Siguiente prueba concreta

Usar dos cierres pequeños con frontera compartida. Construir su relación por unión y proyección. Identificar una comparación que no factorice por el resumen anterior. Después proponer su realización geométrica y evaluar si puede derivarse un J nuevo, o si hay que adoptarlo como postulado.

Debe aceptarse un resultado negativo: podría funcionar la composición contextual sin exigir ninguna nueva órbita C4. Un buen ejemplo no debe incorporar el cuatro por definición y después anunciarlo como resultado.

## Trazabilidad

Ver [resultados](RESULTADOS.md), [linaje](LINAJE.md), [MF-57](../../fuentes/originales/MF57_GENERATOR_AUDIT_AND_NEW_REFERENCE_RULE.md), [MF-61B](../../fuentes/originales/MF61B_COORDINATION_AND_SHARED_BOUNDARY.md) y [v0.91](../../fuentes/originales/COMPOSICION_RECURSIVA_CAPSULAS_v0_91.md).
