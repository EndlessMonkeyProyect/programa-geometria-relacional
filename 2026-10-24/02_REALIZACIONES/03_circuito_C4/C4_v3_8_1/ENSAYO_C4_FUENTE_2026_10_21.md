# Ensayo C4 — Cierre común, independencia y encuentro de imágenes

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 21 de octubre de 2026**  
**Alcance:** resultado geométrico exacto en un modelo euclidiano regular. No equivale a prueba de cierre ontológico universal, origen de los primos, P versus NP ni mecanismo de luz física.

## 1. La pregunta del hilo

La unidad puede formar un cierre local y continuar por reflexión. ¿Qué condición hace que **cuatro** reflexiones locales constituyan otra unidad común sin que el numeral de la etapa decida el resultado? ¿Y es esa condición igual a que dos imágenes confluyan en un punto?

Distinguimos deliberadamente: (i) formar tetraedro local, (ii) recuperar el **mismo foco colectivo**, (iii) formar tetraedro regular a nueva escala, (iv) repetición de imagen por rutas distintas y (v) **novedad aritmética**. Ninguna de las cinco nociones implica por definición las demás.

## 2. Geometría exacta

Sea la unidad base, centrada en cero:

```
v1=( 1, 1, 1)   v2=( 1,-1,-1)
v3=(-1, 1,-1)   v4=(-1,-1, 1)
```

Todas las aristas cumplen `|vi-vj|²=8` y `vi·vj=-1` para `i≠j`. Al reflejar `vi` en la cara opuesta sin modificar las demás caras de referencia se obtiene exactamente

\[
w_i=-\frac53 v_i,\qquad w_i-v_i=-\frac83 v_i.
\]

La cara opuesta a `vi` es fija para esa operación. Las cuatro direcciones de desplazamiento tienen rango 3 y sus normales unitarias satisfacen `ni·nj=-1/3` (`i≠j`), con ángulo 109,471…°, no 90°. Se anulan al sumarse: `n1+n2+n3+n4=0`.

Si cada cara tiene una amplitud no negativa de intervención `ai`, la suma vectorial de sus desplazamientos es cero precisamente cuando `a1=a2=a3=a4` (pudiendo todos ser cero). **Demostración:** `n4=-(n1+n2+n3)` y `n1,n2,n3` son linealmente independientes; por tanto `Σ ai ni=0` implica `a1=a4`, `a2=a4`, `a3=a4`. Es una condición intrínseca al modelo, no una asignación de números a nodos.

En un espacio tridimensional, **tres direcciones linealmente independientes no admiten una suma vectorial nula con coeficientes estrictamente positivos**. Se necesitan al menos cuatro para equilibrar direcciones que abarcan las tres dimensiones. En un tetraedro regular, las cuatro tienen esa dependencia positiva mínima. Esta afirmación es condicional al criterio de equilibrio direccional y no convierte `4` en una constante ontológica universal.

## 3. Las 16 combinaciones — resultado exhaustivo

Elegimos un punto activo por dirección `pi=wi` si reflejamos la cara `i`, y `pi=vi` si no la reflejamos. Conservamos siempre el tetraedro original como referencia, incluso al desplazar el punto activo.

| Caras reflejadas | Nº de estados | Aristas de conjunto activo | Centro colectivo igual al original | Lectura |
|:--:|--:|:--|:--:|:--|
| 0 | 1 | todas `d²=8` | Sí | unidad original |
| 1 | 4 | todas `d²=8` | No | tetraedro local congruente; centro desplazado |
| 2 | 6 | `d²∈{8,200/9}` | No | composición no regular |
| 3 | 4 | `d²∈{8,200/9}` | No | composición no regular |
| 4 | 1 | todas `d²=200/9` | Sí | nueva unidad regular, escala de arista y radio `5/3`, orientación invertida |

Sea `S` el conjunto de caras reflejadas, `k=|S|`, y `C_S` el centroide activo. Se obtiene exactamente

\[
C_S=-\frac23\sum_{i\in S}v_i,\qquad \boxed{\|C_S\|^2=\frac49 k(4-k)}.
\]

Así, con un mismo **foco global y configuración regular**, la única transición no trivial de esta familia finita es activar las cuatro caras. La condición es *completar un conjunto de cuatro relaciones*; NO exige que se reflejen exactamente en un mismo instante.

## 4. Orden, espejo fijo y espejo móvil

**Foco conservado:** cada `wi` se calcula respecto de la cara de la base original. Aplicar los cuatro reemplazos en cualquier orden conduce a la **misma** nueva unidad: se verificaron las 24 permutaciones de las cuatro intervenciones. Esto corrige la necesidad de «sincronización» estrictamente temporal del ensayo anterior. La completitud relacional sí es necesaria para este foco y esta capa; la simultaneidad no.

**Foco móvil:** si después de cada reflexión se vuelven a calcular las caras usando el tetraedro actualizado, las operaciones dejan de conmutar. La secuencia cara 1 → cara 2 y la secuencia cara 2 → cara 1 generan configuraciones distintas, aunque cada una conserve las seis longitudes originales del tetraedro activo. Aquí es pertinente comparar ritmos, marco móvil y continuidad del normalizador, pero aún no hay una dinámica física derivada.

## 5. ¿Dónde aparece la «raíz» por coincidencia de dos imágenes?

Una afirmación surgida en la conversación es que una raíz aparece cuando **dos imágenes de direcciones diferentes coinciden en un punto**. Este ensayo separa tres sentidos:

1. **Coincidencia espacial:** `wi=wj` en tres dimensiones. **No sucede** para `i≠j` en la primera capa de cuatro reflexiones; son cuatro posiciones distintas.
2. **Coincidencia de la referencia:** el centro global vuelve a `O` al completar las cuatro reflexiones. **Sí sucede**, pero es una coincidencia de focos y relaciones, no de dos imágenes puntuales.
3. **Coincidencia proyectada:** desde un sensor que registra sólo `P(x,y,z)=(x,y−z)`, las imágenes `w1` y `w2` producen la **misma observación** aunque ocupen puntos tridimensionales distintos. El acceso del observador puede hacer indistinguibles rutas que no confluyen realmente.

No identificamos ninguno de esos sucesos con raíz aritmética (primo o generador modular) antes de declarar y demostrar un mapa de equivalencia. El criterio fuerte propuesto es que una raíz relacional esté acreditada por **confluencia de rutas con conservación del normalizador bajo consultas admisibles**, no por un encuentro que sólo depende de una proyección particular. Eso sigue siendo una hipótesis a contrastar.

## 6. Cómo conversa con los pasos 1–2–3–4–5

El programa coloca la diferencia antes de la cardinalidad y en cuatro una primera estructura tetraédrica repetible, **bajo su contrato**. Este ensayo no intenta reinterpretar el 1, 2 o 3 como tetraedros: parte de la base regular ya formada y demuestra qué cierres pueden **continuarla**. La aparición de una quinta referencia por reflejo de cara es exacta; afirmar que `4±1` constituye necesariamente la aritmética de raíces requiere una operación adicional que traduzca las direcciones y las coincidencias a números, sin imponer ese orden de antemano.

La geometría tampoco demuestra que el «8 abierto» del programa equivalga a ocho vértices: tras añadir cuatro nuevas referencias existen 8 puntos en el conjunto histórico, pero **el tipo de cierre activo y la incertidumbre de orientación son variables distintas**.

## 7. Próxima prueba discriminante

Hacer crecer **dos ramas** desde caras diferentes manteniendo la historia y la referencia de cada una. Comparar:

- intersección o coincidencia tridimensional de nuevos puntos,
- coincidencia sólo desde proyecciones de observador,
- posibilidad de recomponer un foco común e interfaz suficiente,
- independencia del resultado ante permutación de las intervenciones,
- efecto de bloquear una cara sobre accesibilidad, sin borrar el estado interno.

Primero registrar igualdades geométricas con fracciones exactas; después, y sólo si hay una regla derivada, construir la correspondencia con los múltiplos/raíces. El criterio experimental debe permitir hallar **ninguna raíz nueva** aun cuando se vean reflejos.

## 8. Reproducción y estatus

`python3 verificar.py` vuelve a producir `resultados_exactos.json` y `16_estados.csv`, ambos incluidos en este paquete. Las pruebas usan `fractions.Fraction`, sin librerías externas. `Explorar_16_estados.html` presenta una interfaz local, sin servidor.

**[DEMOSTRADO EN ESTE CONTRATO]** identidad `wi=−5vi/3`, 16 patrones, fórmula del centro, dependencia única de normales, conmutación de cuatro reflexiones con marco base fijo y no conmutación en marco móvil. **[NO ACREDITADO]** emergencia de raíces primas desde geometría, coincidencia espacial de dos imágenes independientes en la primera capa, tiempo físico o nueva ley óptica.
