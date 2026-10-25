# CME-003 — De las cuatro referencias a los ángulos π/2 y π/3

**Laboratorio del Cubo de Espejos · Programa de Geometría Relacional · Le Matt Ansatz Di Ego · 24 de octubre de 2026**

**Estado:**
- [T] teoría de reflexiones conocida, comprobada aquí con aritmética exacta;
- [E] ensayo reproducible;
- [O] lectura del hilo;
- [A] lo que queda abierto.

## Pregunta

CME-002 muestra que lo que decide si un recinto cierra es la suma de las fracciones, pero toma como entrada los dos primeros ángulos, π/2 y π/3. ¿Salen esos ángulos de algo que el programa ya tiene, sin ponerlos a mano?

## Lo que ya estaba

**Del autor.**
- Al dejar de ser uno surgen dos; cada mitad vuelve a partirse en dos, y eso da el 4. Las soluciones emergen juntas, no una por una.
- El 2 aparece primero como mitad. El 3 no aparece hasta que se manifiesta el 4, y entonces surge como cantidad de nodos (24 de octubre).
- Las cuatro singularidades son tres y una, pero no se puede distinguir cuál es la una (octubre).

**T8, del 14 de octubre** (`../../../01_HILO/fuentes/06_hilo_del_dos/v2_8/docs/T8_DEL_LENGUAJE_AL_ESPACIO_v2_8.md`):
- dos distinciones dan cuatro estados y tres comparaciones de paridad;
- cada par de estados lo separan exactamente dos comparaciones;
- en tres dimensiones, los cuatro estados son un tetraedro regular;
- la identidad es simétrica y no designa ninguna referencia privilegiada.

**O19** (`../geometria_O19_O22/O19/`): los espejos centrales producen el tetraedro complementario; juntos son los ocho vértices del cubo, separados por paridad.

**O20 y O22** (`../geometria_O19_O22/O20/`, `O22/`):
- el espejo de cara crea una quinta referencia a 5/3 del radio;
- reflejar no es rellenar.

**CME-002, regla del bit** (`../CME-002_pared_que_se_corre/comprobacion_regla_del_bit.py`): un ±1 en cada nodo, junto con el intercambio de nodos, da solo π/2, π/3 y π/4, con 48 orientaciones para tres nodos.

La nota de rescate del 24 de octubre (`../../../05_ARCHIVO/notas_recibidas_2026-10-24/`) propuso leer los intercambios de las cuatro referencias como reflexiones. Esta ficha lo comprueba y lo completa.

## Reglas admitidas

Solo dos operaciones sobre las cuatro referencias, las dos ya presentes en el programa:
- **intercambiar** dos referencias, porque ninguna es privilegiada;
- **cambiar el signo** de una comparación: el bit ±1 en un nodo.

Cada referencia se representa por sus tres comparaciones. No se usa ningún ángulo como dato.

## Resultado [T · E]

1. **Las cuatro referencias son un tetraedro.** En las coordenadas de las comparaciones, las referencias son (1, 1, 1), (1, −1, −1), (−1, 1, −1) y (−1, −1, 1). Los ejes de las tres comparaciones son los ejes que unen aristas opuestas, y son perpendiculares entre sí.
2. **Intercambiar es reflejar.** El intercambio de dos referencias es la reflexión en el plano que deja quietas a las otras dos.
   - Dos intercambios **sin referencia común** conmutan: orden 2, ángulo π/2.
   - Dos intercambios **con una referencia común** recorren tres referencias: orden 3, ángulo π/3.
   - Los seis intercambios generan 24 orientaciones: es el recinto (2, 3, 3) de CME-002.
3. **No hay generadores que elegir.** Los espejos dividen el espacio en 24 cámaras, y en todas las paredes forman el mismo recinto, con órdenes 3, 3 y 2. Da igual dónde esté el foco.
4. **El bit da el cubo.** Cambiar el signo de una comparación lleva el tetraedro a su complementario, y los dos juntos son los ocho vértices del cubo: la separación por paridad de O19. Con el bit, el producto de dos espejos puede tener orden 4 (π/4), y el grupo llega a 48 orientaciones, que es el recinto (2, 3, 4) del cubo.
5. **Ni antes ni después aparece otro ángulo.**
   - Con dos referencias hay un solo espejo y dos orientaciones: la mitad.
   - Con ocho referencias, el producto de dos intercambios sigue teniendo solo orden 2 o 3.
   - Con intercambios y bits, el producto de dos espejos solo tiene orden 2, 3 o 4, según la regla del bit.
   - El 5 no sale de aquí.
6. **Si una referencia fuera distinguible**, solo podrían intercambiarse las otras tres. Habría 6 orientaciones, y los tres espejos rodearían la recta de la referencia fija: un recinto plano, el del triángulo, con dos direcciones y no tres.
7. **Reflejar en una cara es otra cosa.** No intercambia referencias: crea una nueva fuera del tetraedro, a 5/3 del radio (O20). Las cuatro nuevas forman el tetraedro invertido, y esa es la reflexión que nunca cierra (CME-001).

**Precisión.** Los órdenes que fijan ángulos son siempre los del producto de dos espejos. Los elementos compuestos pueden tener otros: entre las 24 hay giros de orden 4, y entre las 48, elementos de orden 6. No se mezclan.

## Lectura en el hilo [O]

- **El 2 aparece primero como mitad:** con dos referencias hay un solo espejo.
- **El 3 aparece con el 4.** Con cuatro referencias, dos intercambios pueden compartir una, y eso da el orden 3. Al mismo tiempo aparecen tres nodos: hay tres comparaciones, y cada cámara tiene tres espejos.
- **Lo que no comparte nada es perpendicular.** Dos intercambios sin referencia común son independientes y forman un ángulo π/2. Es la misma lectura que la de dos números sin divisor común.
- **Que no se pueda decir cuál es la una** es lo que da las tres direcciones independientes. Si una fuera distinguible, el recinto quedaría plano.
- **El tetraedro, dos veces.** Reflejado en sus caras crea referencias nuevas y es el fondo que nunca cierra. Con el intercambio de sus referencias, que son sus espejos de simetría, cierra en 24. La misma figura da el fondo abierto y la isla cerrada; lo que cambia es si la reflexión trae una referencia nueva o intercambia las que ya están.
- **El cubo** son los intercambios más el bit: la regla del bit de CME-002, vista desde las cuatro referencias.

## Lo que NO establece

- No es matemática nueva. Que los intercambios de n cosas formen un grupo de reflexiones es un resultado clásico ‹1›‹2›.
- No deriva por qué son dos distinciones (n = 2). T8 lo deja abierto, y aquí sigue abierto.
- No deriva la métrica. Las coordenadas de las comparaciones son una realización.
- No prueba que la pared que se corre produzca exactamente estas referencias y estos intercambios.
- No dice nada sobre las ramas.

## Lo que queda [A]

1. **El mapa desde la pared que se corre.** Hay que escribir qué regla de la pared hace que su cascada (1 → 2 → 4) dé cuatro referencias intercambiables, ninguna privilegiada. Si se cumple, CME-002 queda sin datos puestos a mano hasta el 4.
2. **Las dos distinciones**, como pide T8.
3. **El 5.** No sale de intercambios ni de bits; necesita el paso de la cascada donde el uno se indefine.

## Reproducción

```bash
python3 cme003_cuatro_referencias.py
```

Usa solo la biblioteca estándar y aritmética exacta con enteros y fracciones. Escribe `cme003_resultados.json` y falla si alguno de los puntos no se cumple, incluida la separación entre los órdenes de los productos de dos espejos y los de los elementos compuestos.

## Referencias de enlace

- ‹1› E. H. Moore, «Concerning the abstract groups of order k! and ½k! holohedrically and hemihedrically isomorphic with the symmetric and the alternating substitution-groups on k letters», *Proceedings of the London Mathematical Society* 28 (1897).
- ‹2› H. S. M. Coxeter, «Discrete groups generated by reflections», *Annals of Mathematics* 35 (1934).
