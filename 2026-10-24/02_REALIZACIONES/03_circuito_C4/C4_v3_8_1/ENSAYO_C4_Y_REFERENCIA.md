# C4 — Reflexión, cierre colectivo y continuidad de la referencia
**Estado [T] para el modelo euclidiano declarado; [O/A] para generalizaciones ontológicas y aritméticas.**

## Regla en el laboratorio

La narrativa anterior no cambia: unidad → primera reflexión → diferencia abierta → comparación → cierre propio → continuación. La afirmación ontológica de los hitos 1–2–3–4–5 es distinta de un algoritmo geométrico que presupone un tetraedro ya completo. Esta prueba **comienza** después de disponer de cuatro puntos equidistantes; no deriva que la cardinalidad deba nacer en cuatro.

Tomemos el tetraedro centrado en el origen:

```
v1 = ( 1, 1, 1)   v2 = ( 1,-1,-1)
v3 = (-1, 1,-1)   v4 = (-1,-1, 1)
```

Sus seis aristas satisfacen ||vi-vj||²=8 y el producto vi·vj=-1 para i≠j. Reflejar un vértice sobre su cara opuesta, **manteniendo fija la referencia original**, produce wi=−5vi/3. Sean S las caras reflejadas y k=|S|. La colección activa usa pi=wi para i∈S y pi=vi en caso contrario. El centroide es

`C(S)=−(2/3) Σ(i∈S) vi`, de modo que `||C(S)||²=(4/9) k(4−k)`.

Esta identidad implica centro original exactamente para k=0 y k=4. Para k=1, se mantiene un tetraedro regular congruente pero **con centro desplazado**; para k=2,3, los seis pares no comparten la misma longitud; para k=4, los nuevos cuatro vértices conforman un tetraedro regular invertido y escalado 5/3 respecto de la unidad de referencia. Recorremos exhaustivamente C(4,k)=1,4,6,4,1: **16 estados**.

## Independencia, compensación y orden

Las cuatro normales exteriores son independientes por tríos, pero no entre sí: sus productos cruzados son −1/3 (normalizadas), el ángulo entre pares es 109,471...°, y la suma de las cuatro es cero. La relación de dependencia tiene dimensión uno. Para pesos `a_i` en estas normales, su suma es nula si y solo si todos los `a_i` son iguales. El cierre direccional **no necesita simultaneidad temporal**: reemplazos basados siempre en la referencia fija conmutan, independientemente del orden. Si se actualizan las caras tras cada reemplazo, el operador cambia y el orden puede importar. Esto requiere separar espejo fijo de espejo móvil y comparar ritmos sin presuponer un reloj físico.

## Coincidencias que no deben confundirse

- **Cierre colectivo / foco común:** tras las cuatro intervenciones el centroide original reaparece. Sí está demostrado en la familia de 16 estados.
- **Encuentro espacial de imágenes:** wi=wj para i≠j. No ocurre en la primera capa regular: son puntos distintos.
- **Encuentro de observaciones:** proyectar puede identificar puntos diferentes. Depende del observador; no implica confluencia espacial.
- **Raíz relacional y raíz aritmética:** la propuesta es que dos rutas genuinamente diferentes acrediten una coincidencia conservando una referencia/normalizador. La equivalencia con una raíz numérica o número primo **no está demostrada**.

El programa preserva **valor y referencia normalizadora**. La igualdad h/N = (hL)/(NL) es una identidad de representación; el portador geométrico o dinámico del múltiplo que normalizó exige un contrato adicional. No sustituirlo por el resto aislado ni por la forma visible.

## Negativos que hacen útil el resultado

C4 no demuestra la repetición necesaria en las etapas 8, 12 o 16. Una sola reflexión iterada puede construir un tetraedro local en cada paso. C4 tampoco prueba que "cuatro" sea una ley universal de toda dimensión, ni prueba raíces primas, ni obliga una dinámica física. El siguiente falsador crece dos ramas desde una referencia común, sin numerarlas, y busca primer encuentro de **posiciones y firmas**, registrando longitud de representación y número de operaciones.

**Fuente y trazabilidad:** `archivo/ENSAYO_C4_FUENTE_2026_10_21.md` (auditoría exacta previa del ensayo). El script `tests/verificar_addenda.py` repite las 16 configuraciones con aritmética racional.
