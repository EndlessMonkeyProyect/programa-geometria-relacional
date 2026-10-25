# Testigo matemático nuevo para la revisión: ¿el recierre crea un tipo nuevo?

**Propósito:** discriminar la frase del autor «no hay que inventar estructuras nuevas; las mismas caen a la siguiente» sin interpretarla de forma hostil o trivial. Esto **no** modifica el núcleo v2.8; es una prueba sectorial propuesta al evaluador para contrastar dos significados distintos de «mismo tipo».

## Grafo estrella de cuatro vértices

Tomemos la estrella `K_{1,3}` con un centro interior `v` y tres terminales exteriores `a,b,c`; cada vértice toma color en `{0,1,2}`. Hay aristas `v—a`, `v—b`, `v—c`. Los tres factores iniciales son **binarios** y del mismo tipo: desigualdad de colores.

Al recerrar `v`, la interfaz de frontera es

`Γ(a,b,c)=∃v [(v≠a)∧(v≠b)∧(v≠c)]`.

El centro puede colorearse si y sólo si sus tres vecinos usan **a lo sumo dos colores**. Por tanto

`Γ(a,b,c)=NO-SON-LOS-TRES-DISTINTOS(a,b,c)`.

De las `3^3=27` asignaciones exteriores, `6` utilizan los tres colores y quedan excluidas; `21` sobreviven.

## Proposición verificable

**Γ no puede describirse exclusivamente como conjunción de restricciones unarias y binarias sobre `a,b,c` (sin auxiliares).** Prueba: para cada par de variables exteriores y cualquier elección de sus colores, existe un valor para la tercera que satisface Γ (basta repetir uno de los dos colores). En consecuencia, todas las proyecciones binarias de Γ son universales. Si Γ fuese conjunción de restricciones de a lo sumo dos variables, cada factor tendría que aceptar todas las proyecciones correspondientes y sería universal. Entonces aceptarían las 27 asignaciones, contradiciendo las 6 excluidas. ∎

## Qué demuestra y qué NO

- **Demuestra:** al eliminar el centro, una relación construida con tres aristas binarias puede necesitar una **relación ternaria** para expresar la interfaz exacta, si el lenguaje exterior prohíbe nuevos auxiliares.
- **No demuestra:** que se necesite inventar un tipo ontológico nuevo. Si `𝒦` ya contiene relaciones finitas de aridad arbitraria, Γ sigue perteneciendo al **mismo tipo general de cápsula**.
- **No demuestra:** que esa clase general tenga representación siempre corta o Join/Project baratos. Si conservamos el centro como variable interna, mantenemos una descripción pequeña con aristas, pero podemos haber aplazado la cuantificación en vez de compilarla.

**Lectura para el autor:** las piezas verdaderamente unidas forman una unidad exterior. Esa unidad puede conservar exactamente sus referencias de frontera; sin embargo, la **composición** puede crear una dependencia que ninguna de las aristas tomadas por separado expresa sobre los puertos. No es necesario decir «tipo ontológico nuevo» para admitir que apareció una interacción de mayor aridad.

## Protocolo
Ejecutar `experimento_ternaria.py` para confirmar las 21 filas admitidas y todas las proyecciones binarias. Luego preguntar al revisor si puede definir una gramática de cápsulas cerrada bajo todos esos recierres **con una representación y actualización económicas para familias arbitrarias**, no solo con el nombre abstracto de «relación».
