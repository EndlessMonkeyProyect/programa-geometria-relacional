# 05. P versus NP: identidad de solución y costo de construirla

**Estado:** las preguntas de complejidad global continúan abiertas. No se demuestra `P=NP` ni `P≠NP`. El programa posee modelos exactos de comparación, compresión contextual, XOR y laboratorios SAT restringidos, pero no un algoritmo polinómico general para 3-SAT.

## El mapa de información [T]

Dada una CNF `F(I,S)` con interiores `I` y frontera `S`, la firma externa natural es `B_F(s)=∃i F(i,s)`. Dos bloques son equivalentes bajo todas las continuaciones de frontera si tienen el mismo `B_F`. Esa equivalencia separa:

- **decidir** satisfacibilidad de una consulta,
- **representar** un conjunto de asignaciones en una interfaz,
- **construir** esa interfaz,
- **actualizarla** al añadir relaciones,
- **leerla** bajo una continuación arbitraria.

Una presentación simbólica compacta puede ser semánticamente suficiente sin permitir consultas eficientes. Una tabla explícita de frontera puede ocupar `2^|S|` y no demuestra eficiencia uniforme. El resultado `F↦B_F` incluye la dureza de computar una proyección arbitraria.

## Exactitud del control XOR [T]

Para restricciones `x_u⊕x_v=b_uv`, cada componente conexa libre aporta un bit de elección; una arista entre componentes independientes reduce un grado libre; una arista interna está determinada por paridades o genera contradicción. Bajo consistencia, el número de soluciones es `2^c` donde c es el número de componentes no ancladas. Esto es un resultado de la clase **afín/XOR**, no de CNF ternaria arbitraria. La equivalencia contextual no convierte 3-SAT en XOR sin costo.

## La obligación de eficiencia [A]

Para resolver P vs NP mediante interfaces se requiere una regla uniforme que, para cualquier 3-CNF de tamaño n, construya/actualice interfaces y responda satisfacibilidad usando tamaño, tiempo, profundidad, memoria y política de continuaciones **polinomiales en n**, sin oráculo oculto, enumeración exponencial ni reformulación que presupueste `SAT`.

La normalización elimina duplicados *acreditados* respecto de un contrato, pero **no acredita gratis la posibilidad de encontrar todos los equivalentes ni de representarlos compactamente**. Rutas basadas en grafos y módulos pueden revelar clases tractables específicas; no equivalen a prueba para todas las instancias.

## Conexión transversal con física [LECTURA]

La misma arquitectura pregunta si unas comparaciones locales son suficientes para controlar toda diferencia global. En P vs NP el obstáculo es **costo computacional uniforme**; en Yang–Mills es **coercividad analítica y límite continuo**. No son el mismo teorema.

Ver `05_computation/contextual_sat_and_representation_cost.es.md`, `02_formal_core/contextual_reclosure_and_resource_cost.es.md`, `14_imagen_integral_2026_10_18/V5_9_original/10_branches/p_vs_np/`.
