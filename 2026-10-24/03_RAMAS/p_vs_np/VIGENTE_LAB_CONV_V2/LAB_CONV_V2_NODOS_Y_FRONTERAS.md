# Programa de Geometría Relacional · LAB-CONV v2
## El número como nodo de caminos: cierre por equivalencia, frontera y costo de reconocimiento

**Autoría del programa:** Le Matt Ansatz Di Ego  
**Fecha de integración:** 22 de octubre de 2026  
**Estatus:** suplemento aditivo de investigación; formalización contextual, demostraciones dentro de grafos, implementación y falsadores. **No demuestra P=NP.**  
**Orden metodológico:** narrativa → ontología → lenguaje → matemática → ejecución → auditoría → preguntas abiertas.

### Lectura inicial

La intuición rectora del autor es: «Cada número nuevo que aparece es un nodo de caminos para llegar a él como soluciones donde convergen estructuras». No equivale a afirmar que cualquier igualdad de números pruebe que las historias son intercambiables. Una convergencia puede ser **aritmética** (mismo valor), **contextual** (mismas respuestas futuras admisibles) o **estructuralmente acreditada** (existe una regla verificable que conserva las relaciones). El cierre propio pertenece a las últimas dos, siempre respecto de un contrato explícito.

La incertidumbre precede a su cuantificación radial. El radio cuenta/extiende diferencias pendientes solo después de disponer de comparador y medida. Dos cierres con igual número e igual medida radial pueden no representar el mismo nodo respecto de una nueva relación. La procedencia puede permanecer registrada en el marco; una firma de frontera, por sí sola, no promete reconstruir todas las historias individuales.

**Qué recuperamos, no repetimos:** MF-86 (normalizador suficiente, idempotente y composicional), MF-97 (equivalencia estable ante continuaciones), MF-99 (congruencia para composición declarada), CR-6 (interfaz por frontera, separación y costo), E11 (DSU/paridad), E19 (refinamiento de preguntas), E25 (ternarias invisibles en parejas), E26 (regla diamante para grafos) y O59/O60 (órbita óptica y ramas de ocupación bajo contratos distintos). El laboratorio v1 ya comprobó K4, Grötzsch, números de frontera y una definición de radio por diámetro. Ninguna de esas piezas debe renombrarse como resultado universal nuevo.

---

## I. Propuesta ontológica [O]

1. **Camino:** sucesión de relaciones/reflexiones desde referencias que pueden reconstruirse bajo la historia admitida.
2. **Convergencia:** caminos que encuentran una referencia común para ciertas comparaciones. No exige igualdad de historia interior.
3. **Número emergente:** etiqueta cardinal de una convergencia; por sí sola no indica qué operaciones quedan autorizadas.
4. **Nodo cerrado en sí:** referencia que puede sustituir relaciones interiores sin cambiar respuestas a nuevas comparaciones **del contrato**.
5. **Novedad:** una pregunta u operación que distingue historias previamente incluidas en una clase común; no significa que los pasos acreditados se hayan des-resuelto.
6. **Radio de incertidumbre:** medida posterior de extensión de diferencias todavía compatibles; no sustituye la relación de equivalencia ni la estructura de la frontera.
7. **Normalizador:** el que trasladó el valor y las relaciones entre escalas, no un denominador suelto ni una operación necesariamente física.

En el espejo ideal, diferentes imágenes de una órbita son representaciones vinculadas por las operaciones permitidas. Pero el acceso desde un observador y la pertenencia geométrica a la órbita son relaciones distintas. En el grafo hay una distinción homóloga de lenguaje —camino, referencia, consulta, cierre— pero no una equivalencia automática entre fotones/reflejos y variables de color.

---

## II. Definiciones del nuevo contrato de grafos [D]

Sea `G=(V,E)` un grafo simple no dirigido, con una asignación de colores `c:V→{0,1,2}`. Las relaciones son `c(u)≠c(v)` para cada arista. No hay anclajes que nombren un color absoluto.

Una subestructura `H(I,B)` distingue interiores `I` y frontera etiquetada `B`. Su **firma de existencia** es

\[
\Gamma_H(b)=\exists i\; H(i,b)\in\{0,1\}.
\]

Cuando `H` se encuentra con otra relación exterior `K(b,z)` únicamente por `B`, su factibilidad conjunta satisface

\[
\exists b,z,i\,[H(i,b)\land K(b,z)]
\iff \exists b,z\,[\Gamma_H(b)\land K(b,z)]. \tag{C1}
\]

Éste es el mismo principio ya demostrado por CR-6. No afirmar que `Γ_H` recupera la multiplicidad interior. Para consultas de conteo corresponde usar `Q_H(b)=∑_i H(i,b)` y la composición de conteos apropiada. Si el exterior accede a una variable interior no declarada en B, (C1) **no autoriza** sustituir el interior.

### Tipo de nodo propuesto

\[
\mathcal N_Q(H,B)=\bigl(v,\;\nu,\;[\Gamma_H]_{\mathcal G},\;B,\;\mathscr P\bigr),\tag{C2}
\]

con `v` valor cardinal cuando proceda, `ν` referencia normalizadora, `[Γ_H]_G` soporte exterior tipado bajo simetrías **permitidas**, `B` frontera y `\mathscr P` registro de procedencia que permita auditar las transformaciones declaradas. (C2) es una **estructura de trabajo**, no una fórmula física derivada. El campo `\mathscr P` puede ser una lista de certificados compactos; no presupone almacenar cada camino.

---

## III. Tres proposiciones exactas [T]

### T1. Convergencia certificada por diamante — resultado E26 reutilizado

Si `a,b` están unidos y `u,v` son ambos vecinos de `a,b`, entonces toda 3-coloración satisface `c(u)=c(v)`. Demostración: `a,b` utilizan dos colores diferentes; tanto `u` como `v` solo pueden utilizar el tercero. Si `u,v` son adyacentes, no hay solución; si no lo son, contraerlos genera un grafo cuyas 3-coloraciones se corresponden biunívocamente con las originales mediante expansión.

Ésta es una **convergencia estructural acreditada**, no una coincidencia de cantidad. La prueba es sectorial: grafos 4-cromáticos sin triángulos pueden carecer de diamantes.

### T2. Firma suficiente por órbitas de renombramiento de colores

El grupo `S₃` renombra globalmente los tres colores. Como `c(u)≠c(v)` es invariante bajo cualquier `π∈S₃`, también lo es `Γ_H`:

\[
\Gamma_H(b)=\Gamma_H(\pi b).\tag{C3}
\]

Entonces para cada tupla `b` podemos guardar solamente `canon(b)`, la primera-occurrencia de cada color (por ejemplo `(2,1,2,0)↦(0,1,0,2)`). Se recupera **exactamente** `Γ_H(b)` consultando la entrada canónica, y (C1) permanece correcta en toda composición exterior a través de B.

**Prueba:** permutar globalmente los colores define una biyección entre extensiones interiores de `b` y las de `πb`, pues conserva cada desigualdad del grafo. Todas las combinaciones externas pueden consultar el soporte original a través del representante canónico. ∎

La cantidad de patrones de una frontera con `k` coordenadas es

\[
\boxed{P_3(k)=\sum_{j=1}^{\min(3,k)} {k\brace j}},\quad k\ge1,\tag{C4}
\]

con `{k\brace j}` números de Stirling de segunda especie. Para `k=8` son `1+127+966=1.094` patrones frente a `3⁸=6.561` asignaciones etiquetadas. Para `k=10`, `9.842` frente a `59.049`. La mejora asintótica es de **factor constante cercano a seis**, no transforma en polinómico un costo exponencial en `k`.

**Condición de invalidez:** anclar `c(v)=0` rompe la simetría. `canon((0,))=canon((1,))`, pero esas dos asignaciones no satisfacen el mismo anclaje. Tampoco se permite permutar las **referencias etiquetadas** de B como si fueran meros nombres de colores; eso puede cambiar las preguntas futuras.

### T3. Obstrucción por vecindario impar — nuevo certificado incorporado al laboratorio

Si para algún vértice `v` el subgrafo inducido por sus vecinos `N(v)` contiene un ciclo impar, `G` no es 3-coloreable.

**Prueba:** dado un color a `v`, todos sus vecinos deben utilizar los otros **dos** colores. Un ciclo impar no admite una 2-coloración, contradicción. ∎

El certificado se expresa mediante `v` y los vértices del ciclo impar, todos verificables contra las aristas originales. Esta prueba detecta ruedas impares, pero no grafos triangulares libres como Grötzsch: allí el subgrafo de vecinos no contiene aristas.

### T4. El reconocimiento de una igualdad **globalmente forzada** es coNP-completo

Esta proposición revela una barrera computacional directa para el proyecto. Para un grafo `G` y dos vértices distintos no adyacentes `u,v`, defina `Forzada(G,u,v)` si **toda** 3-coloración propia de `G` satisface `c(u)=c(v)`. Entonces:

\[
\boxed{\neg\operatorname{Forzada}(G,u,v)\iff\operatorname{3COL}(G+uv).}\tag{C5}
\]

**Prueba de (C5):** si existe una coloración de G con colores distintos para u,v, esa coloración es propia también para G con la arista uv agregada, y viceversa. ∎

El problema `Forzada` está en `coNP`, pues un contraejemplo es una 3-coloración con `c(u)≠c(v)` comprobable en tiempo polinómico. Además es `coNP`-difícil: tome cualquier grafo H, agregue dos vértices aislados u,v para formar G. Existe una coloración con `c(u)≠c(v)` **si y solo si** H es 3-coloreable. Así, `Forzada(G,u,v)` equivale a que H no sea 3-coloreable. Como 3-coloración general es NP-completa, la decisión general de igualdad forzada es `coNP`-completa. ∎

**Precaución ontológica imprescindible:** si G no tiene ninguna coloración, la expresión «toda coloración satisface igualdad» es verdadera por vacuidad. Esto no constituye un nodo convergente ni un vínculo positivo acreditado: es una **contradicción global**. El estado operacional correcto tiene tres posibilidades:

1. **CONTRADICCIÓN:** `Γ_G(∅)=0` (no existe coloración).
2. **CONVERGENCIA FORZADA:** existe una coloración de G, pero agregar la desigualdad `u≠v` elimina todas.
3. **SIN CONVERGENCIA FORZADA:** alguna coloración de G mantiene `u≠v`.

El diamante de E26 ofrece un **certificado local polinómico** para el segundo caso en una familia restringida; T4 demuestra por qué no podemos presumir que decidir globalmente cualquier igualdad forzada sea una operación barata. Este resultado **no demuestra P≠NP**: si P=NP, las preguntas anteriores podrían decidirse en tiempo polinómico. Sí identifica que un oráculo que encontrara todas las fusiones globales gratuitamente escondería ya la dificultad original.

---

## IV. Falsador simultáneo de cantidad y radio [T/E]

Frontera etiquetada `B=(a,b,c)`. Tomemos

\[
A=\{(a,b,c):a\neq b\},\qquad
D=\{(a,b,c):b\neq c\}.
\]

Ambas relaciones tienen 18 asignaciones. En la distancia de Hamming, ambas tienen **diámetro 3** y radio de ensayo `diam/2=1,5`. Sus etiquetas numéricas y sus radios coinciden.

Pero al incorporar `K=[a\neq b]`:

\[
|A\cap K|=18,\qquad |D\cap K|=12.
\]

No son un mismo nodo para esa continuación. Sus conjuntos de patrones canónicos son:

- `A`: `010`, `011`, `012`;
- `D`: `001`, `010`, `012`.

**Resultado:** valor cardinal y radio no son invariantes conjuntamente suficientes; la firma de compatibilidad etiquetada sí distingue el contexto. Este es un falsador concreto de la tesis fuerte «número + radio decide toda nueva relación»; no refuta la ontología de convergencia contextual.

---

## V. Experimento reproducible [E]

Dos programas independientes:

- `laboratorio_v2.py`: eliminación existencial exacta de vértices, con o sin normalización `S₃`; reglas de diamante; testigo de ciclo impar del vecindario; ejemplos adversariales y recuento de evaluaciones de frontera.
- `verificar_exhaustivo.py`: oráculo por enumeración independiente para grafos de cuatro y cinco vértices (todos los grafos simples etiquetados) más una muestra determinista de seis vértices. Compara ambas eliminaciones con el oráculo, comprueba contracciones y prueba por enumeración **conservación del número de coloraciones** ante cada cadena de fusiones. Los resultados son `controles_exhaustivos.json`.

**Validación nueva ejecutada en este entorno:** 64 grafos etiquetados de cuatro vértices + 1.024 de cinco vértices + 250 de seis vértices, para **1.338 instancias**. Todos los controles finalizaron sin discrepancias. Esta validación respalda la implementación en esas entradas; los teoremas T1–T3 son los argumentos generales en los contratos descritos.

### Casos de contraste (evaluaciones de asignaciones de frontera)

| Instancia | `|V|` | Solución | Min-fill sin simetría | Min-fill con simetría | Orden inverso sin simetría | Orden inverso con simetría | Diamante |
|---|---:|---|---:|---:|---:|---:|---|
| `K4` | 4 | No | 39 | 8 | 39 | 8 | contradicción |
| Rueda impar `W5` | 6 | No | 93 | 18 | 363 | 63 | contradicción tras fusiones |
| Grötzsch `M(C5)` | 11 | No | 495 | 87 | 6.438 | 1.078 | ninguno |
| `M(C7)` | 15 | No | 1.035 | 179 | 97.320 | 16.227 | ninguno |
| `M(C9)` | 19 | No | 1.575 | 271 | *límite 130.000* | *límite 130.000* | ninguno |
| Escalera `2×8` | 16 | Sí | 130 | 30 | 19.678 | 3.288 | ninguno |
| Cuadrícula `5×5` | 25 | Sí | 1.507 | 264 | 4.369 | 741 | ninguno |
| Dos anclajes unidos + nueve hojas | 11 | Sí | 85 | 20 | 85 | 20 | ocho fusiones: 11→3 |

`M(C_{2m+1})` designa la construcción de Mycielski sobre un ciclo impar, que da ejemplos triangulares libres no 3-coloreables. No hay diamantes ni ciclos impares en los vecindarios de estos grafos: las dos reglas locales no detectan su contradicción. La eliminación conjunta sí la detecta al llegar a una relación vacía en una frontera intermedia. **El efecto del orden es importante**: en `M(C9)` la ejecución inversa fue detenida por el presupuesto de estados; no se registra una decisión para esas dos ejecuciones interrumpidas. El min-fill sí terminó y decidió `NO`.

### Lectura rigurosa de la tabla

Los números son **tuplas de frontera candidatas examinadas por la implementación**, no milisegundos, complejidad intrínseca del problema ni número de soluciones globales. Los resultados dependen del orden de eliminación. La heurística `min-fill` no prueba una cota para todo grafo. El laboratorio usa tablas explícitas de aridad creciente; para anchura de eliminación `w`, pueden aparecer `O(3^w)` estados. La reducción por `S₃` no cambia el hecho de que `P₃(w)=\Theta(3^w)`.

Así, ninguna de estas pruebas implica que P=NP, ni prueba P≠NP. Simplemente exhibe cuándo se consigue ahorro exacto, cuándo una fusión tiene certificado y cuándo el método debe cargar una relación conjunta mayor.

---

## VI. Qué constituye avance y qué no

**Ya demostrado en el programa o en el contrato:** equivalencia contextual por continuaciones (MF-97); suficiencia de frontera declarada (CR-6); regla diamante (E26); cocientes de color correctamente tipados (T2); obstrucción de vecindario impar (T3); clasificación coNP-completa de decidir una igualdad globalmente forzada (T4); conservación de conteos por fusiones certificadas; contraejemplo número+radio.

**Validado experimentalmente:** igualdad del resultado exacto entre codificación completa y patrones `S₃` en los casos terminados; 1.338 controles de grafos pequeños y tres controles de la distinción trivalente entre convergencia, no convergencia y contradicción; detección de Grötzsch mediante eliminación de factores; diferencias de costo según orden.

**No acreditado:** normalizador universal económico para todas las relaciones de 3-coloración, cota polinómica total de construcción/actualización/decisión, ni identificación del radio de Hamming con el radio espectral de incertidumbre o con un radio físico de singularidad. Tampoco se demostró que todo número ontológico emergente sea necesariamente una clase de coloraciones.

### Resultado reflexivo

El lugar fértil de la intuición no es la igualdad de números ni la mera enumeración reducida de caminos: es el **tipo de relación que autoriza a reconocer la convergencia**. Cuando ese tipo posee un certificado local (diamante), cerrar y reutilizar es barato. Cuando una familia tiene simetrías admisibles (renombrar colores), una clase sustituye a seis realizaciones etiquetadas. Cuando el testigo solo existe en el conjunto, la interfaz conjunta puede crecer y su obtención debe contabilizarse. La incertidumbre que conserva el nodo es precisamente la parte de la historia que la pregunta aún no obliga a distinguir.

---

## VII. Próximo punto de falsación — propuesta, no conclusión

La siguiente tarea central no es volver a verificar K4, XOR, Grötzsch ni la órbita de espejos. Es intentar derivar un **selector de convergencias** que, sobre grafos de 3-coloración con fronteras que crecen, elija y certifique fusiones/interfases que mantengan la pregunta global sin materializar `3^w` estados. Debe resistir familias 4-cromáticas triangulares libres con alta anchura, no solamente Mycielski de ciclos (que admite órdenes de baja anchura), y debe llevar cuenta de costo de hallar certificados, comprobarlos, componer, refinar y decidir.

La meta falsable es un operador uniforme que produzca siempre `Γ_H` suficiente con costo total polinómico en `|V|+|E|` para una decisión NP-completa general, **o** un contraejemplo interno demostrable que refute la forma específica de ese operador. No hacer afirmaciones de P=NP ni de separación sin ese paso.

---

## VIII. Reproducción y genealogía

```bash
python laboratorio_v2.py
python verificar_exhaustivo.py
```

Resultados: `resultados_v2.json`, `controles_exhaustivos.json`, `tabla_resumen.csv`. La versión previa se conserva como referencia histórica en `antecedentes/`; este laboratorio es **LAB-CONV v2**, no «O61», número que pertenece a Navier–Stokes dentro de la genealogía del programa.

**Fuentes de sustento:** MF-86, MF-97/99, CR-6, E11/E19, E25/E26, O59/O60, suplemento «Nodos numéricos como convergencia de caminos» del 22-10-2026 y `LAB_CONV_2026_10_22_NODOS_FALSADORES.md`. Esta edición distingue resultados heredados, nuevas instancias ejecutadas y puente abierto hacia P=NP.
