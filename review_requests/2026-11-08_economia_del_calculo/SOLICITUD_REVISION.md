# ¿Dónde se ahorra el cálculo?

**Solicitud de revisión independiente**  
**Endless Monkey Project**  
*Relational Geometry Program*

8 de noviembre de 2026 · versión 2

**Versión revisada:** [etiqueta `2026-11-08-economia-del-calculo-v2`](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/2026-11-08-economia-del-calculo-v2/2026-11-08_economia_del_calculo) · [informe](../../2026-11-08_economia_del_calculo/informe.md) · [laboratorio](../../2026-11-08_economia_del_calculo/laboratorio_economia_relacional.py) · [cambios](../../2026-11-08_economia_del_calculo/CAMBIOS.md) · [English](REVIEW_REQUEST_EN.md)

---

## Una pregunta concreta

Las 3-coloraciones propias de la rejilla w × m, con bordes libres, cumplen una recurrencia lineal en m. Para cada ancho, la simetría S₃ × Z₂ (permutar colores, invertir la columna) reúne las columnas en órbitas. El orden mínimo de la recurrencia es la dimensión de la representación lineal mínima de la sucesión de conteos:

| Ancho w | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Columnas | 3 | 6 | 12 | 24 | 48 | 96 | 192 | 384 | 768 | 1536 |
| Órbitas | 1 | 1 | 2 | 3 | 6 | 10 | 20 | 36 | 72 | 136 |
| Orden mínimo | 1 | 1 | 2 | 3 | 5 | 7 | 13 | 19 | 35 | 51 |

**¿Tiene una explicación conocida la sucesión de órdenes 1, 1, 2, 3, 5, 7, 13, 19, 35, 51? ¿Figuran los órdenes de los anchos 8 a 10 en la literatura de matrices de transferencia?**

**Lo demostrado.** Cada orden de la tabla está certificado con aritmética exacta (sección siguiente). En w = 10, la simetría reúne 1536 columnas en 136 órbitas, y la sucesión admite una representación lineal mínima de dimensión 51 sobre los racionales.

**Lo que preguntamos.** Si la sucesión de órdenes tiene una explicación y si ya está publicada. En las fuentes consultadas, las recurrencias citadas llegan al ancho 7: OEIS da recurrencias de orden 7 y 13 para los anchos 6 y 7 ([A207995](https://oeis.org/A207995), [A207996](https://oeis.org/A207996)). La tabla de conteos [A207997](https://oeis.org/A207997) incluye anchos mayores, pero no da por sí misma los órdenes mínimos para los anchos 8 a 10. Queda por revisar la literatura de matrices de transferencia.

## La evidencia reproducible

Sea b_k = 1ᵀ·T^k·1, con T la matriz de transferencia entre columnas; b_k cuenta las coloraciones de k + 1 columnas. Como T es simétrica, el Hankel H_N con entradas b_(i+j) es la matriz de Gram de los N primeros vectores de Krylov T^i·1. Entonces det H_d ≠ 0 y det H_(d+1) = 0 fijan el orden d de la recurrencia mínima válida para todo m ≥ 1, que es la dimensión de la representación lineal mínima (Kronecker). El Hankel desplazado b_(1+i+j) también es no singular: la recurrencia no tiene raíz nula y ninguna más corta vale desde m = 2.

Un determinante no nulo módulo un primo es no nulo sobre los enteros; el determinante nulo se calcula en exacto. Para w = 10 la recurrencia tiene coeficientes enteros y orden 51. El 51 es una propiedad de la sucesión de conteos y de sus representaciones lineales.

```bash
python3 -I laboratorio_economia_relacional.py E5 E5x E5c
```

E5 comprueba los rangos módulo dos primos, E5x calcula la dimensión de Krylov exacta sobre los racionales y E5c certifica el orden en cada ancho.

## La economía entre referencias

### La pregunta general

¿Puede surgir una mejor economía del cálculo de las relaciones entre referencias, sin perder la respuesta que buscamos?

Nuestro punto de partida son **distinciones, herencia y economía**. Una referencia reúne configuraciones que observa como iguales; una nueva relación puede heredar, distinguir o reabrir lo reunido. El laboratorio del **cubo de espejos, la pared móvil y las esferas** permite imaginar ese cambio de referencia sin cambiar la estructura observada.

Pedimos determinar **qué puede demostrarse**, con qué hipótesis, dónde falla y qué antecedentes existen. Una imposibilidad o un contraejemplo también es un resultado.

La cuestión más precisa es distinguir tres costos: **(i)** cuántas diferencias siguen siendo observables, **(ii)** cuántas deben conservarse para representar exactamente los futuros posibles y **(iii)** cuántas operaciones hacen falta para responder una consulta. Son tres costos distintos, aunque relacionados. Toda afirmación de *economía* debe especificar qué se calcula, con qué representación y contra qué referencia de costo se compara.

La rejilla es un caso de esta pregunta: la simetría reúne 1536 columnas en 136 órbitas, y la consulta de conteo permite una reducción adicional, de 136 a 51 dimensiones.

### Dos controles que separan los costos

El experimento **E9** mantiene la misma función y la misma cuenta exacta (**6561**), pero al cambiar el orden de las variables el rango máximo pasa de **256 a 2**: la referencia modifica drásticamente el costo de una representación secuencial. Las fórmulas de **Tseitin** satisfacibles sobre expansores exigen representación ordenada exponencial y aun así se cuentan en tiempo polinómico por eliminación de Gauss (§6). Estos dos casos separan el **ancho de representación** del **costo de resolver**.

### El mecanismo que queremos explorar

En un **cubo de espejos**, cambiar la pared de referencia puede reunir o separar imágenes sin modificar los objetos. En las **esferas**, la distancia y el umbral determinan qué distinciones sobreviven a la observación. La pregunta computacional es si esa imagen permite formular una operación exacta de **reflexión, cierre o reapertura** que reduzca el trabajo necesario para una consulta.

Una ruta propuesta en el **§10** del informe es estudiar identidades con signos, del tipo

`X = Σ_j s_j c_j O_j`, con `s_j ∈ {−1,+1}`,

relacionables con la involución `SWAP = I − 2P₋`, donde `P₋` proyecta sobre el subespacio antisimétrico. Que cada término tenga menor rango de corte es fácil de lograr: toda matriz se descompone en términos de rango uno, a veces demasiados. La economía exige acotar también **cuántos términos hay, cómo se encuentran, cuánto cuesta evaluarlos y recombinarlos, y que la identidad sea exacta para toda la familia de entradas**.

Ese es el desafío que proponemos: encontrar una familia con ahorro demostrado, demostrar un límite para esta clase de descomposiciones o construir un contraejemplo.

## Nueve afirmaciones y su estado

Cada número remite a su prueba en el informe y, cuando corresponde, a un experimento reproducible. El estado indica qué se pide revisar.

1. **Herencia entre particiones.** Para particiones P y Q de un conjunto finito, si J recorre los bloques de P ∨ Q y p_J, q_J cuentan los bloques de P y Q dentro de J, entonces `|P ∧ Q| ≤ Σ_J p_J q_J`, con igualdad exactamente cuando P y Q permutan. Con permutación y k = |P ∨ Q|, `|P ∧ Q|·|P ∨ Q| = |P|·|Q| + k²·Cov_J(p_J, q_J)`: la ley del producto exige permutación y covarianza nula, por ejemplo bloques homogéneos. Para residuos da `mcm(H,m)·mcd(H,m) = Hm`. *Estado:* por revisar; la identidad modular es clásica y se buscan antecedentes de la versión para particiones. **§2, Prop. 2.1, Cor. 2.2–2.3; E1.**
2. **Distinciones activas y rango de corte.** En una representación **lineal secuencial sobre un campo**, el ancho mínimo en cada corte pasado–futuro es el rango de su matriz. Para equivalencias deterministas de futuros, el criterio es Myhill–Nerode. *Estado:* con antecedente: teorema de Fliess (1974) y Carlyle–Paz (1971). **§3, Teo. 3.1 y 3.3.**
3. **Límite de la reducción universal.** Si `L: K^X → K^r` es lineal y su equivalencia es compatible con multiplicar por **cualquier** restricción indicadora, su núcleo es un ideal del álgebra de funciones. Si además permite recuperar la cuenta exacta de toda función, `r ≥ |X|` (en asignaciones booleanas, `2^n`). *Estado:* por revisar, en especial la universalidad y la condición de recuperación de la cuenta. **§4, Teo. 4.1.**
4. **Costo de reconocer la referencia mínima.** Dada una 3-CNF, decidir si dos asignaciones del pasado permiten exactamente los mismos futuros es coNP-completo. También lo es decidir si una cláusula nueva es **lógicamente redundante** (`F ⊨ C`). *Estado:* con antecedente: ambas se reducen desde la insatisfacibilidad. **§4, Prop. 4.2–4.3.**
5. **Representaciones por orden en expansores.** Para la 2-CNF monótona de familias de expansores de grado acotado, en **todo orden de variables y sobre cualquier campo**, algún corte tiene rango `2^Ω(n)`. La prueba usa emparejamientos inducidos y una submatriz de **conjuntos disjuntos**. *Estado:* por revisar; la técnica de rectángulos es la de Bova, Capelli, Mengel y Slivovsky (2016). **§6, Teo. 6.1; E2, E2b.**
6. **Cortes de Tseitin.** Para G conexo, cualquier carga satisfacible y una partición de aristas `(A,B)`, `rank M_{A,B} = 2^λ(A)`, donde `λ(A) = r(A) + r(B) − r(E)` es la función de conectividad del matroide gráfico. En el grafo, `λ(A) = β + 1 − c_A − c_B`, con β los vértices incidentes a aristas de ambos lados y c_A, c_B las componentes del grafo de cada lado. *Estado:* con antecedente: con carga nula es el teorema del espacio de estados de Forney (1994) para el código de ciclos, y λ es la función que usa Kashyap (2008) para el ancho de trellis. El rango se comprobó directamente en 3003 cortes con carga nula, 3003 con carga aleatoria y 216 de grafos aleatorios. **§6, Teo. 6.2; E3b.**
7. **Rejilla de tres colores, ancho 10.** 1536 columnas, 136 órbitas bajo `S₃ × Z₂` y una representación lineal mínima de dimensión **51** sobre los racionales: la recurrencia mínima tiene orden 51. *Estado:* certificada por cálculo exacto (det H_51 ≠ 0, det H_52 = 0, sin raíz nula). Lo abierto es la pregunta del comienzo. **§5.5; E5, E5x, E5c.**
8. **Fusión óptica bajo un modelo especificado.** Para cinco fuentes y el operador de observación de E6, `R_ℓ ≈ r(c_ℓ/ε)^(1/ℓ)` es la distancia a la cual una distinción cae bajo un umbral relativo ε. En la configuración simétrica estudiada, el último modo observable es el dipolo impar. *Estado:* por revisar sus condiciones. **§7, Prop. 7.1–7.2; E6.**
9. **Comparación con octubre de 2026.** Los trabajos publicados por OpenAI y Anthropic afirman algoritmos de conteo exacto en tiempo `2^o(n)` para `k` fijo, incluido `k = 2`. **Si sus resultados y su aplicación a esta familia se sostienen**, el punto 5 ilustra una separación entre el costo de toda representación por orden y el de un algoritmo que usa otras operaciones. Las lecturas propuestas son deformación con interpolación y cancelación con signo. *Estado:* condicionada a esos trabajos. **§8.**

## Qué revisión solicitamos

- **Pruebas:** ¿qué afirmación falla, qué hipótesis falta o dónde se confunden rango, tamaño de representación, operaciones y tiempo de construcción? En especial, las afirmaciones 1, 3, 5 y 8.
- **Antecedentes:** ¿dónde se encuentran formulaciones equivalentes de las afirmaciones 1 y 3? ¿Hay una explicación de la sucesión de órdenes de la rejilla, o una publicación anterior de los órdenes 19, 35 y 51? Agradecemos referencias precisas.
- **Mecanismo:** ¿existen transformaciones exactas por reflexión o cancelación con signo cuyo **costo total** sea menor? ¿Qué condiciones necesarias o suficientes permitirían probarlo o descartarlo?
- **Correspondencias:** ¿qué conexiones con los trabajos de OpenAI y Anthropic son identidades matemáticas verificables, cuáles son analogías y cuáles dependen de hipótesis todavía abiertas?

## Reproducción

El informe contiene las pruebas, los contraejemplos, los experimentos E1–E12 (más E5x y E5c) y una tabla de estados de revisión.

```bash
pip install -r requirements.txt
python3 -I laboratorio_economia_relacional.py                # todo, unos 4 minutos
python3 -I laboratorio_economia_relacional.py E5 E5x E5c     # la rejilla y su certificado
python3 -I laboratorio_economia_relacional.py E1 E3b         # particiones y Tseitin, unos 30 s
```

**Fuentes:** [informe y laboratorio, versión 2](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/2026-11-08-economia-del-calculo-v2/2026-11-08_economia_del_calculo) · [preprint de OpenAI](https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026) · [trabajo de Anthropic](https://hexagonmath.org/2610.00577) · OEIS [A207995](https://oeis.org/A207995), [A207996](https://oeis.org/A207996), [A207997](https://oeis.org/A207997) · G. D. Forney, *Dimension/length profiles and trellis complexity of linear block codes*, IEEE Trans. Inf. Theory 40(6), 1994 · [N. Kashyap, *Matroid pathwidth and code trellis complexity*, arXiv:0705.1384](https://arxiv.org/pdf/0705.1384).

**Cómo responder:** abrir un *issue* en el repositorio o comentar aquí, citando **número de afirmación, hipótesis, paso de prueba, experimento o referencia anterior**. Las correcciones se publican en [`CAMBIOS.md`](../../2026-11-08_economia_del_calculo/CAMBIOS.md) junto con su justificación.
