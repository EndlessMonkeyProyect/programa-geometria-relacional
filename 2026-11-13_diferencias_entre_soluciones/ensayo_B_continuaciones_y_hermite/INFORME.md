# Pruebas paralelas: continuaciones y recuperación por Hermite

**Endless Monkey Project**  
*Relational Geometry Program*

**Autor:** Le Matt Ansatz Di Ego.

**Ensayo B · 13 de noviembre de 2026 · nota experimental v0.1**

## Pregunta y alcance

¿Puede una misma familia de medidas cuantificar diferencias entre soluciones, conservarse bajo operaciones de composición y recuperarse a través de datos de evaluación y derivación, sin enumerar las soluciones?

Dos modelos pequeños verifican estas propiedades. El primero prueba una agrupación por continuaciones compatible con el transporte de momentos. El segundo recupera los mismos momentos mediante datos de Hermite de una deformación cúbica con coeficientes en un anillo truncado. Ambos proporcionan controles pedagógicos para estudiar componentes de los algoritmos de Anthropic y OpenAI; el polinomio auxiliar publicado por OpenAI conserva su definición específica.

## Modelo común

Sea $`K_F`$ el conjunto de asignaciones booleanas que satisfacen $`F`$, y sea $`w(x)=\sum_i x_i`$ el eje proyectado de peso de Hamming. Se definen:

```math
N=\sum_{x\in K_F}1,\qquad S=\sum_{x\in K_F}w(x),\qquad Q=\sum_{x\in K_F}w(x)^2.
```

La codificación en $`R=\mathbb Z[u]/(u^3)`$ es

```math
J_F(u)=\sum_{x\models F}(1+u)^{w(x)}\equiv N+Su+\frac{Q-S}{2}u^2\pmod{u^3}.
```

Estas identidades se conservan exactamente por suma y producto en $`R`$; el número de coeficientes representados es tres, aunque el costo de sus operaciones debe contarse por separado.

## Ruta 1. Contracción tensorial por equivalencia de continuaciones

Para $`F=(x\lor z)\land(y\lor z)`$, se comparan los prefijos $`p=(x,y)`$ frente a cada continuación admisible $`z\in\lbrace0,1\rbrace`$. El vector de compatibilidad es $`\sigma(p)=(F(p,0),F(p,1))`$.

| Prefijo | $`z=0`$ | $`z=1`$ | Firma |
|---|---:|---:|---|
| 00 | 0 | 1 | (0,1) |
| 01 | 0 | 1 | (0,1) |
| 10 | 0 | 1 | (0,1) |
| 11 | 1 | 1 | (1,1) |

Hay **cuatro prefijos y dos clases**. En vez de conservar los prefijos como cuatro estados distintos para conectarlos con el sufijo, se conservan las sumas de pesos de los miembros de cada clase. La operación sobre las continuaciones pasa de ocho verificaciones prefijo–sufijo a cuatro verificaciones clase–sufijo. Este último número mide únicamente las conexiones del ejemplo: **no incluye el costo de descubrir y construir las clases**.

El cálculo exacto devuelve

```math
J_F(u)=5+10u+6u^2,\qquad (N,S,Q)=(5,10,22).
```

Para esta instancia, la agrupación es correcta porque todos los miembros de una clase aceptan exactamente las mismas continuaciones; sus pesos de prefijo se suman primero y el aporte de cada continuación se aplica una sola vez por clase. No se presume que las firmas calculadas sean iguales para un conjunto más amplio de futuras consultas sin volver a comprobarlo.

**Condición de generalización.** Si la continuación usa únicamente la interfaz $`b(p)`$, y dos prefijos inducen la misma función de continuación bajo todas las consultas permitidas, sus contribuciones pueden agruparse sumando sus pesos en $`R`$. Esta es una condición exacta de reemplazo. El costo de reconocer equivalencias, la dimensión de interfaz y las modificaciones permitidas por la recursión deben acreditarse antes de afirmar una reducción total.

## Ruta 2. Recuperación cúbica mediante datos de Hermite

Se deforma una red de restricciones mediante

```math
H_F(T,u)=\sum_{x\models F}(1+u)^{w(x)}\prod_{i=1}^{\min(3,n)}(1+Tx_i)\pmod{u^3}.
```

Su grado en $`T`$ es a lo sumo 3. Como $`H_F(0,u)=J_F(u)`$, basta conocer valores y primeras derivadas en $`T=1,2`$. La identidad exacta de Hermite cúbico es

```math
\boxed{H_F(0,u)=-4H_F(1,u)-4\,\partial_TH_F(1,u)+5H_F(2,u)-2\,\partial_TH_F(2,u).}
```

**Prueba.** La identidad es cierta para los monomios $`1,T,T^2,T^3`$, que forman una base de los polinomios de grado menor que 4. Por linealidad se extiende a coeficientes en $`R`$. Para esos nodos, los coeficientes enteros de la fórmula evitan cualquier división; una elección general de nodos sobre otros anillos puede requerir condiciones de invertibilidad adicionales. Las evaluaciones y las derivadas se calcularon por eliminación de variables con parejas de valores $`(H,\partial_T H)`$, utilizando la regla del producto, sin enumeración durante el cálculo principal.

### Verificación y comparación de operaciones

| Sistema | $`N`$ | $`S`$ | $`Q`$ | Contracción conjunta $`J_F`$ | Hermite: 2 evaluaciones y 2 derivadas |
|---|---:|---:|---:|---:|---:|
| 3 variables, $`(x\lor z)(y\lor z)`$ | 5 | 10 | 22 | 138 | 900 |
| Cadena, 4 variables | 8 | 22 | 64 | 240 | 1.548 |
| Ciclo, 6 variables | 18 | 78 | 348 | 780 | 4.956 |
| Fórmula incompatible, 4 variables | 0 | 0 | 0 | 312 | 2.028 |

Fórmulas de la tabla: cadena $`(x_1\lor x_2)(x_2\lor x_3)(x_3\lor x_4)`$; ciclo $`(x_1\lor x_2)(x_2\lor x_3)\cdots(x_5\lor x_6)(x_6\lor x_1)`$; fórmula incompatible: la cadena de cuatro variables con las cláusulas unitarias $`(x_1)`$ y $`(\lnot x_1)`$. Ambas rutas eliminan las variables en el orden $`x_1,\ldots,x_n`$; una suma de ternas cuenta 3 sumas enteras y un producto truncado, 6 productos y 3 sumas. En la ruta de Hermite, el producto de pares $`(H,\partial_TH)`$ cuenta tres productos truncados y una suma de ternas, más un producto final por nodo.

En los cuatro casos la recuperación Hermite coincide exactamente con los momentos de la contracción directa y con la enumeración de auditoría. Las cifras se refieren al número fijo de sumas y multiplicaciones escalares asignado a cada operación de la aritmética de coeficientes en estos dos programas, **no al tiempo real ni al costo de bits**. Además, las cifras de Hermite aún excluyen la combinación lineal final de sus cuatro datos, de modo que su costo total sería algo mayor.

**Interpretación:** la recuperación polinómica es correcta en estos ejemplos, pero resulta **entre 6,35 y 6,52 veces más costosa** en operaciones contadas que la contracción directa de tres componentes. Este resultado negativo es importante: el transporte algebraico no demuestra por sí mismo ahorro en una construcción de interpolación. El polinomio auxiliar usado aquí es elegido deliberadamente como prueba de compatibilidad, y no representa la optimización exacta del algoritmo publicado por OpenAI.

## Comparación con construcciones publicadas

- **Anthropic:** el artículo sobre #3-SAT describe redes tensoriales y una expansión con signos que se contrae en distintos órdenes. Antes de extrapolar el ejemplo de clases de continuación, deben examinarse las operaciones que introducen signos, recursión y cambios de interfaz.
- **OpenAI:** el trabajo publicado utiliza deformaciones e interpolación en su mecanismo de conteo. El ensayo presente utiliza una deformación cúbica propia y una identidad Hermite de grado tres; aún no verifica grados, cuerpos o anillos, puntos, exactitud ni límites del procedimiento publicado.
- **Antecedente sobre novedad:** *Subexponential Weighted Counting and Exact Optimisation* (29-X-2026) ya declara extensiones del método de OpenAI a pesos en álgebras conmutativas sobre $`\mathbb Q`$. Una extensión genérica de coeficientes no debe presentarse como nueva. Un aporte posible sería certificar qué equivalencias de continuación son recuperables, qué referencias preservan las respuestas exigidas y qué reducción de costo total puede demostrarse.

## Próxima condición necesaria para una mejora

Para cualquier representación comprimida debe demostrarse simultáneamente:

1. **Exactitud bajo consultas:** dos estados agrupados producen la misma función de continuación para todas las consultas exigidas, no solo para el conteo total.
2. **Composición:** el reemplazo sigue siendo válido después de cada transformación usada por la construcción original.
3. **Costo neto:** reconocimiento de clases + composición + recuperación + costos de precisión y memoria es menor que el mejor comparador que reutiliza cálculos compatibles.

Estas condiciones dejan abierta, en lugar de presuponer, la posibilidad de economía. La siguiente integración técnica es cotejar las identidades de ambos preprints paso a paso y desarrollar comparadores optimizados en sus modelos reales.

## Reproducción

```bash
python3 verificar_paralelo.py
```

El comando reproduce las dos rutas y la tabla de operaciones, y genera `resultados_paralelos.json`. Solo requiere Python 3 estándar. El código incluye enumeración directa como auditoría independiente en instancias de máximo seis variables; no se usa en las contracciones principales.

### Fuentes

- Anthropic, *A $`2^{o(n)}`$ Time Algorithm for 3-SAT*, Hexagon, v1, 27-X-2026: https://hexagonmath.org/pdf/2610.00577v1
- OpenAI, *The Exponential Time Hypothesis is False*, 25-X-2026: https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026
- Deep Bhattacharjee, *Subexponential Weighted Counting and Exact Optimisation*, v1, 29-X-2026: https://hexagonmath.org/2610.00594v1

---

**Endless Monkey Project**  
*Relational Geometry Program*
