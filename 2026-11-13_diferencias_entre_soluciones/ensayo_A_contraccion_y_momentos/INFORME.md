# Conservar diferencias entre soluciones: prueba algebraica y ensayo de costo

**Endless Monkey Project**  
*Relational Geometry Program*

**Autor:** Le Matt Ansatz Di Ego.

**Ensayo A · 13 de noviembre de 2026**  
**Estado:** identidad algebraica probada y ensayo reproducible de modelos reducidos; la integración con los procedimientos completos de Anthropic y OpenAI es una pregunta de investigación.

## 1. Qué se examina

Sea $`F`$ una fórmula booleana y $`K_F`$ su conjunto de soluciones. Declarado un eje $`w(x)=\sum_{i=1}^{n}x_i`$, se miden:

```math
N=\sum_{x\in K_F}1,\qquad S=\sum_{x\in K_F}w(x),\qquad Q=\sum_{x\in K_F}w(x)^2.
```

No se almacena la lista de asignaciones para el cálculo principal: el conteo de referencia por fuerza bruta se utiliza **únicamente como auditor independiente** en instancias pequeñas. El objetivo es transportar diferencias mediante relaciones entre factores.

## 2. Proposición y demostración

Se trabaja en el anillo conmutativo de polinomios truncados $`R=\mathbb{Z}[u]/(u^3)`$. Se define

```math
J_F(u)=\sum_{x\models F}(1+u)^{w(x)}\pmod{u^3}.
```

La identidad binomial da

```math
J_F(u)=N+Su+\frac{Q-S}{2}u^2.
```

Para cada variable $`x_i`$, la contribución local es $`1`$ si $`x_i=0`$ y $`1+u`$ si $`x_i=1`$. Cada cláusula contribuye su indicador (0 o 1). El producto de factores de una asignación es entonces su indicador de satisfacción multiplicado por $`(1+u)^{w(x)}`$. La suma sobre las asignaciones produce $`J_F`$. Por asociatividad y distributividad, cualquier eliminación exacta que utilice solo suma y producto conserva el mismo resultado en $`R`$, independientemente del orden de eliminación. $`\square`$

En la notación directa de momentos, el producto para dos sistemas independientes con posiciones aditivas es

```math
(N,S,Q)\otimes(n,s,q)=(Nn,Sn+Ns,Qn+2Ss+Nq).
```

Si el eje se mueve de $`w`$ a $`w-a`$, las magnitudes se transforman sin resolver las soluciones:

```math
N_a=N,\qquad S_a=S-aN,\qquad Q_a=Q-2aS+a^2N.
```

El código comprueba estas identidades para $`a=0,1,2`$ en cada caso. Cuando $`N>0`$, el centro es $`S/N`$ y la dispersión cuadrática media mínima es $`Q/N-(S/N)^2`$. Si $`N=0`$, el centro no está definido.

## 3. Tres procedimientos ensayados

**A. Contracción conjunta** (modelo de red tensorial elemental). Una sola eliminación de variables sobre los factores de la CNF, con valores $`(c_0,c_1,c_2)`$ que representan $`c_0+c_1u+c_2u^2`$. El resultado se interpreta como $`N=c_0`$, $`S=c_1`$, $`Q=c_1+2c_2`$.

**B. Consultas de conteo condicionadas**. Se repite el mismo esquema escalar para $`\#F`$, $`\#(F\land x_i)`$ y $`\#(F\land x_i\land x_j)`$, hasta $`1+n+\binom n2`$ llamadas, y se recuperan $`N,S,Q`$. **No se aplica caché ni reutilización** entre llamadas: es una referencia directa, no un contador óptimo.

**C. Recuperación polinómica elemental**. Se evalúa $`G_F(t)=\sum_{x\models F}t^{w(x)}`$ en los $`n+1`$ puntos $`t=0,1,\ldots,n`$, con una contracción escalar por punto, y se reconstruye $`G_F`$ por interpolación exacta de Lagrange. Sus coeficientes cuentan soluciones de cada peso. Se calculan $`N=G_F(1)`$, $`S=G'_F(1)`$, $`Q=G''_F(1)+G'_F(1)`$. **Este polinomio generador no es el polinomio auxiliar $`H(T)`$ del procedimiento de OpenAI**; aquí se prueba una propiedad de recuperación algebraica, no su protocolo Hermite particular.

## 4. Resultados reproducidos

Número de operaciones aritméticas primitivas $`=`$ multiplicaciones enteras + sumas enteras dentro de la **contracción**. En el caso de la terna, cada multiplicación truncada se contabiliza como 6 multiplicaciones escalares y 3 sumas; cada suma truncada cuenta como 3 sumas. No se contabilizan construcción de tablas, movimientos, potencia escalar inicial, cálculo de coeficientes de Lagrange, ni costo de bits o sobrecarga de Python. Por ello las cifras **no son tiempos de ejecución ni comparaciones completas de bit-complejidad**.

| Estructura | Variables | Soluciones | Conjunta (A) | Condicionadas (B) | Evaluaciones (C) | B/A | C/A |
|---|---:|---:|---:|---:|---:|---:|---:|
| Cadena | 4 | 11 | 408 | 660 | 300 | 1,62 | 0,74 |
| Cadena | 6 | 30 | 816 | 2.552 | 812 | 3,13 | 1,00 |
| Cadena | 8 | 96 | 1.152 | 6.068 | 1.476 | 5,27 | 1,28 |
| Cadena | 10 | 277 | 1.560 | 12.320 | 2.420 | **7,90** | **1,55** |
| Ciclo | 6 | 22 | 2.568 | 7.656 | 2.436 | 2,98 | 0,95 |
| Ciclo | 8 | 68 | 4.128 | 20.868 | 5.076 | 5,05 | 1,23 |
| Ciclo | 10 | 198 | 5.616 | 43.232 | 8.492 | **7,70** | **1,51** |
| Incompatible | 6 | 0 | 960 | 2.904 | 924 | 3,03 | 0,96 |

Todas las 8 instancias pasaron los tres caminos de recuperación con aritmética exacta y la auditoría independiente por enumeración pequeña. La recuperación polinómica también reconstruye íntegramente el histograma de pesos, que contiene más información que los tres primeros momentos.

**Caso de cadena, 10 variables.** $`N=277`$, $`S=1523`$, $`Q=9185`$, centro $`1523/277`$. La contracción conjunta necesitó 1.560 operaciones primitivas, comparadas con 12.320 del baseline de conteos condicionados (56 llamadas). En el mismo caso, las 11 contracciones escalares para evaluación polinómica consumieron 2.420 operaciones, **sin incluir el costo de interpolación**.

**Costo de memoria (estimación parcial).** Para el caso anterior, las tablas de contracción tuvieron un máximo de 336 componentes enteras simultáneas en A frente a 112 en una sola ejecución de B o C. El máximo de bits de un entero de salida intermedia fue 12 en A frente a 9 en B, y hasta 35 en C por la evaluación de potencias. Son indicadores de carga de coeficientes, **no una medición de memoria real en bytes**. B tiene más operaciones acumuladas, pero menos componentes por ejecución; las consultas secuenciales se pueden ejecutar con una misma memoria de trabajo.

**Diferencia de referencias.** Los ensayos comprobaron las identidades de traslación del eje. Para recuperar todas las posiciones proyectadas se reconstruyeron también las matrices de Hankel usando todos los momentos derivados del histograma completo: su rango coincide con el número de pesos distintos en cada caso. **No** se infiere ese rango del primer par de momentos solamente.

## 5. Interpretación delimitada

1. **Demostrado:** la conservación exacta de conteo y primeros momentos en cualquier red finita de sumas y productos sobre anillos conmutativos, bajo las codificaciones declaradas. Es álgebra estándar; no se reivindica novedad del teorema.
2. **Observado:** frente a la referencia de consultas independientes *sin reutilización*, la contracción conjunta disminuye operaciones primitivas en las familias ensayadas de 6 a 10 variables. En 4 variables, la evaluación polinómica escalar emplea menos operaciones que la conjunta. Por tanto, el beneficio depende del tamaño y la referencia de comparación.
3. **Abierto:** la compatibilidad exacta, paso por paso, con las descomposiciones rank-optimizadas de Anthropic y con el esquema Hermite/modular completo de OpenAI. También están abiertos el bit-costo total, el costo de reconocer relaciones, la comparación con métodos especializados y cualquier mejora de sus cotas asintóticas.
4. **Atribución:** la extensión de conteos a álgebras conmutativas y polinomios generadores figura explícitamente en un preprint de octubre de 2026 sobre conteo ponderado. La contribución específica a examinar es si una referencia y medidas de diferencias/herencia permiten certificaciones nuevas o mejoras justificadas de costo para familias concretas.

## 6. Próximos controles técnicos

- Reemplazar el esquema elemental de eliminación por el código y las operaciones publicados de la construcción tensorial de Anthropic; verificar cada identidad sobre la terna y su costo de bits.
- Identificar en la construcción de OpenAI las evaluaciones exactas, matrices Hermite, truncamientos y pasos que utilizan división; demostrar que los coeficientes en el álgebra extendida admiten las operaciones exigidas y la misma precisión.
- Medir costo total (operaciones, tamaño de enteros y fracciones, memoria, tiempo y reconocimiento de equivalencias), comparando con baselines optimizados que **sí** compartan trabajo.
- Analizar la familia de referencias $`w_\alpha(x)=\sum_i\alpha_ix_i`$; medir qué elecciones reducen el número de posiciones sin ocultar distinciones exigidas por la consulta.

## 7. Reproducción

```bash
python3 ensayo_momentos.py
```

Solo requiere Python 3 y su biblioteca estándar. Regenera `resultados.csv` y `resultados.json`; todos los casos tienen aserciones de exactitud para los tres procedimientos, traslaciones del eje y rango de Hankel. La enumeración directa aparece solo en el validador de las 8 instancias (máximo 10 variables).

## 8. Fuentes contextuales

- Anthropic, *A $`2^{o(n)}`$ Time Algorithm for 3-SAT*, Hexagon, v1, 27-X-2026: https://hexagonmath.org/pdf/2610.00577v1
- OpenAI, *The Exponential Time Hypothesis is False*, 25-X-2026: https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026
- Deep Bhattacharjee, *Subexponential Weighted Counting and Exact Optimisation*, 29-X-2026: https://hexagonmath.org/2610.00594v1
- [*Medición de soluciones respecto de un eje* v0.2](https://doi.org/10.5281/zenodo.24213729), nota del 13-XI-2026, base conceptual del ensayo.

**Endless Monkey Project**  
Relational Geometry Program
