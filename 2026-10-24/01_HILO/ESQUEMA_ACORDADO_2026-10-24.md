# Esquema del hilo acordado · 24 de octubre de 2026

**Estado:** esquema acordado. El texto redactado sobre este orden es `HILO_ONTOLOGICO_INTEGRADO_2026-10-24.md`.

## Orden

1. **La totalidad.** La indeterminación es una propiedad de la totalidad, no un punto de partida aparte.
2. **La reflexión.** Es la primera operación sobre la totalidad: lo que la hace distinguible.
3. **Cierre o apertura, según los ángulos.** La misma reflexión abre sin fin o se cierra sola, según los ángulos que forman sus espejos (CME-001: el tetraedro regular abre, el cubo cierra en 8).
4. **Las ramas.** Navier–Stokes, P frente a NP y Yang–Mills son realizaciones donde reaparece la misma pareja de abrir y cerrar.

## Precisiones de Diego

- Los ángulos de cierre están dados por la estructura que generan los múltiplos que van quedando de la pared que se corre. Desde adentro la celda mide siempre uno; desde afuera queda normalizada a la totalidad como 1/k, y un múltiplo nuevo fija el ángulo π/k.
- Lo que vale para los ángulos vale para las identidades: un ángulo π/k es la identidad «aplicar los dos espejos k veces es no hacer nada». Así queda más clara la consecuencia de la escala.
- CME-002 escribe la regla y la prueba en las dos lecturas. Lo que decide si el recinto cierra, se repite o se abre es la suma de las fracciones frente a la totalidad: sobra, llena justo o no alcanza. CME-003 deriva π/2 y π/3 de intercambiar las cuatro referencias; queda la regla de la pared que da esas referencias.
- La gramática común de las ramas (novedad como pregunta que no se deduce de la firma anterior, cierre como firma suficiente, pérdida por bloqueo) es emergente: sale de la reflexión, no la sustituye como fundamento.
- El objetivo es un hilo de economía mínima para entender la realidad. Primero se construye el hilo en sus propios términos; los enlaces con lo que otros hayan descubierto van después, en una capa aparte al final.
- Criterio de control: si el hilo va por el buen camino, todo debería cerrarse solo. Donde haya que forzar un cierre, ahí está la señal de revisión.

## Dónde ya estaba cada idea

Lo conversado el 24 de octubre ya estaba en «El hilo del dos» (13 y 14 de octubre), recuperado en `fuentes/06_hilo_del_dos/`:

| Idea | Dónde está |
|---|---|
| La incertidumbre como bit; el bit que queda abierto en el 8 | `v2_8/docs/EL_BIT_ABIERTO_v2_3.md` |
| La reflexión en cada nodo como ±1: el centro N da N − 1 y N + 1 (3·5 = 16 − 1, 7·9 = 64 − 1) | `v2_8/docs/HILO_DEL_DOS_FORMALIZACION_v2.md`, §5 |
| Del 4 salen el 3 y el 5; del 8, el 7 (nuevo) y el 9 = 3² (heredado) | misma, §7 |
| El 8 es el único centro sin palabra nueva arriba (excepción de Zsigmondy, 7·9 = 63 = 2⁶ − 1) | misma, §8 |
| El recierre hasta el 16 y más allá: cada paso cierra lo anterior y trae una novedad coprima | misma, §9 (cadena de Fermat) |
| El 3 no se supone: son las comparaciones de dos distinciones, 2² − 1; las cuatro referencias realizan las 24 permutaciones | `v2_8/docs/DEL_CUATRO_A_LA_DISTANCIA_Y_EL_TIEMPO_v2_7.md`, T8 (a) y (b) |
| La quinta solo cabe con otro radio | misma, T8 (c) |
| Cada primo entra cuando duplicar n veces vuelve a uno: ord_p(2) = n | `HILO_DEL_DOS_FORMALIZACION_v2.md`, §7 |
| Coprimo como independiente: dos fases con razón p/q coprima fijan una relación y dejan una libre | `../05_ARCHIVO/navier_stokes_O23_O38/O28/` |

## Lo que agrega el 24 de octubre

- **El criterio de cierre por la normalización** (CME-002): si las fracciones sobran, el recinto cierra; si llenan justo la totalidad, se repite; si no alcanzan, se abre. No estaba en el material.
- **El puente entre ángulo e identidad.** El ord_p(2) de §7 es la lectura por identidades: «duplicar n veces vuelve a uno». Los primeros órdenes que aparecen son 2 y 4 (centro 4, primos 3 y 5) y 3 (centro 8, primo 7): exactamente los ángulos del cubo. El 5 llega en el centro 32 (primo 31).
- **La regla del bit genera el cubo, y solo el cubo.** Un ±1 en cada nodo y el intercambio de nodos dan espejos con ángulos π/2, π/3 y π/4, y siempre cierran (48 orientaciones con tres nodos, 384 con cuatro). El 5 no sale de bits: necesita otro radio, como dice T8 (c). Comprobación: `../02_REALIZACIONES/01_cubo_de_espejos/CME-002_pared_que_se_corre/comprobacion_regla_del_bit.py`.
- **El 6, el mismo mecanismo.** En la genealogía, el 6 es el único entero que nunca aparece como orden nuevo (Zsigmondy). En los espejos, es donde el recinto deja de cerrar y se repite. El autor sostiene que no es casualidad: es el mismo mecanismo, la multiplicidad del 2 y del 3 que se repite. Falta escribir el puente formal entre los dos lados.

## Lo que falta afinar

- La genealogía decide qué es nuevo y qué es heredado; la normalización decide qué cierra. No son el mismo criterio: el 4 es heredado y cierra, el 9 es heredado y se abre, el 7 es nuevo y se abre. Falta escribir cómo se relacionan.
- Los números 3, 5, 7 y 9 de la genealogía son imágenes alrededor de un centro, no ángulos. Leerlos como ángulos fue un paso de la conversación, no de la regla; si se usa, hay que justificarlo.

## Material de partida en esta carpeta

- `imagen_total_3_9/`: la versión 3.9 completa (PDF, informe general, índice y atlas).
- `Continuidad_y_protocolo_2026-10-22.md` y `SECUENCIA_ONTOLOGIA_MATEMATICA_COMPUTACION.md`.
- `fuentes/`: fundamentos, núcleo formal, lenguaje, síntesis integral del 20 de octubre, síntesis y lenguaje con el cristal semántico, y «El hilo del dos» completo.
- `../02_REALIZACIONES/01_cubo_de_espejos/CME-001_cierre_por_reflexion/`, `CME-002_pared_que_se_corre/` y `CME-003_de_las_cuatro_referencias_a_los_angulos/`: las realizaciones exactas del punto 3.
