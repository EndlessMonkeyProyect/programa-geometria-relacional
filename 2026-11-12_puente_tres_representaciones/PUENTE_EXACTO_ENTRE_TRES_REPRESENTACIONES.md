---
title: "¿Qué información puede recuperarse entre tres representaciones?"
subtitle: "Un puente algebraico explícito entre el Programa de Geometría Relacional, Anthropic y OpenAI"
author: "Le Matt Ansatz Di Ego"
date: "12 de noviembre de 2026"
lang: es-CR
---

**Autor:** Le Matt Ansatz Di Ego  
**Programa:** Endless Monkey Project · Relational Geometry Program  
**Extensión técnica v0.3 · Revisión de correspondencias · 12 de noviembre de 2026**

# Resumen

Esta extensión aplica los criterios ya demostrados en el programa —referencia, determinante, herencia, distinción recuperable, conservación de respuestas y economía— a una familia **común de consultas** sobre fórmulas booleanas. Se construye una firma canónica que registra qué asignaciones satisfacen una fórmula y se muestran dos maneras exactas de representarla: (i) un intercambio de índices mediante `SWAP = I − 2P₋`, operación local utilizada en la construcción tensorial de Anthropic; (ii) una deformación polinómica de tipo Cauchy que recupera su valor en `T = 0` mediante interpolación, operación local estudiada por OpenAI.

**Resultado matemático:** para tres variables, ambas rutas inducen la misma identidad sobre **toda** la firma de ocho componentes. La equivalencia se comprobó como matrices de 8 × 8, y se recuperaron las **27 consultas de fijación parcial**, además del conteo total. El argumento se generaliza, con representación explícita de tamaño exponencial, a cualquier número finito de variables. La comparación incorpora sus recursos concretos.

La correspondencia establecida es de **operadores locales y recuperación de consultas**; las optimizaciones recursivas y las cotas de tiempo de los artículos originales conservan sus propios contratos de demostración.

# 1. Qué se compara y desde qué referencia

Sea `F` una fórmula de `n` variables binarias. La firma canónica de sus respuestas de pertenencia es el vector

```math
f_F\in\lbrace0,1\rbrace^{2^n},\qquad (f_F)_a=\mathbf1[F(a)=1],\quad a\in\lbrace0,1\rbrace^n.
```

Una **consulta de fijación parcial** `p ∈ {0,1,*}ⁿ` especifica algunas variables y deja las demás libres. Su respuesta es

```math
Z_p(F)=\sum_{a\in\lbrace0,1\rbrace^n}\mathbf1[a\text{ coincide con }p]\,(f_F)_a.
```

La fijación `p=(*,…,*)` pregunta por el conteo total `Z(F)`; una fijación completa pregunta por la compatibilidad de una asignación y responde 0 o 1. Para toda variable todavía libre se cumple

```math
\boxed{Z_p(F)=Z_{p\cup\lbrace x_i=0\rbrace}(F)+Z_{p\cup\lbrace x_i=1\rbrace}(F).}\tag{1}
```

Esta identidad establece **herencia lógica entre las consultas**: la respuesta de una consulta menos específica procede de las respuestas de sus dos continuaciones. La familia completa permite reconstruir `f_F` porque incluye todas las fijaciones completas.

**Criterio ontológico.** La referencia es la familia de consultas; el determinante es qué variable se fija y con qué valor; la distinción es la respuesta acreditada; la conservación significa que una transformación permite recuperar esas respuestas. La firma es una realización matemática de esta comparación, sin sustituir la definición de cierre propio del programa [P1–P2].

# 2. Anthropic: una representación mediante intercambio

El operador sobre dos índices binarios intercambia sus posiciones:

```math
S\,|x_1,x_2\rangle=|x_2,x_1\rangle,\qquad S=I_4-2P_-,\tag{2}
```

con `P₋` proyector de rango uno sobre el subespacio antisimétrico. La identidad (2) es la operación local de intercambio que aparece en el análisis tensorial de Anthropic [A1–A2].

Para tres variables definimos `S₃=S⊗I₂`, que intercambia los dos primeros índices y deja el tercero intacto. Sea `P` la permutación de las entradas de una firma que intercambia, nuevamente, esos mismos dos índices. Entonces:

```math
\boxed{S_3P=I_8.}\tag{3}
```

Dada una firma `f_F`, la representación por índices cruzados es `b=Pf_F`. La contracción con `S₃` recupera **cada componente**:

```math
S_3b=S_3Pf_F=f_F.\tag{4}
```

Por lo tanto, toda consulta de fijación parcial se recupera mediante el mismo funcional `L_p`:

```math
Z_p(F)=L_p(S_3b).\tag{5}
```

La sustitución de `S` por `I₄−2P₋` es exacta, para cualquier tensor con el que se componga. Esta observación acredita la **conservación de la firma** en la representación local construida. El algoritmo de Anthropic utiliza además descomposiciones, rangos de corte y recurrencias para estudiar su costo global; las igualdades (2)–(5) establecen el componente local que utilizaremos en el puente [A2].

# 3. OpenAI: una representación mediante deformación e interpolación

Tomamos la deformación local tipo Cauchy expuesta en el apéndice de contracción de OpenAI [O1]. Para dos puertos definimos

```math
C(T)=(T+2)(T+1)T(T-1),\qquad W_{xy}(T)=\frac{C(T)}{C'(0)[T-(y-x)]},\quad x,y\in\lbrace0,1\rbrace.\tag{6}
```

Cada denominador cancela un factor de `C`, de modo que `W` es polinómica de grado tres y verifica

```math
W(0)=I_2.\tag{7}
```

Para una firma de tres variables construimos dos paquetes de dos puertos. Se añade un cuarto puerto auxiliar fijado en cero y se usa `W₄(T)=diag(W(T),W(T))`. Para una asignación `x=(x₁,x₂,x₃)` escribimos `x̄=(x₁,x₂,x₃,0)`.

Con `ℓ₀(z)=1−z` y `ℓ₁(z)=z`, definimos una matriz de ocho por ocho:

```math
K(T)_{y,x}=\prod_{i=1}^{4}\ell_{\bar y_i}\big((W_4(T)\bar x)_i\big).\tag{8}
```

Como `W₄(0)=I₄`, para vectores binarios se cumple `ℓ_b(c)=1` exactamente cuando `b=c`. En consecuencia:

```math
\boxed{K(0)=I_8.}\tag{9}
```

Cada entrada de (8) es un polinomio de grado a lo sumo `4×3=12`. Para cualquier polinomio de grado a lo sumo 12, sus valores en los trece nodos `T=1,…,13` permiten recuperar el valor en cero por interpolación de Lagrange:

```math
P(0)=\sum_{t=1}^{13}(-1)^{t-1}\binom{13}{t}P(t).\tag{10}
```

Aplicando (10) entrada por entrada a (8):

```math
\boxed{\sum_{t=1}^{13}w_tK(t)=I_8,\qquad w_t=(-1)^{t-1}\binom{13}{t}.}\tag{11}
```

Por tanto, para cualquier firma `f_F`:

```math
f_F=\sum_{t=1}^{13}w_tK(t)f_F,\qquad Z_p(F)=\sum_{t=1}^{13}w_tL_p(K(t)f_F).\tag{12}
```

La igualdad es una **reconstrucción vectorial**: preserva las respuestas de todas las fijaciones parciales del laboratorio. Los trece nodos se eligieron para una demostración directa, con aritmética racional exacta. Este ensayo utiliza el operador local de deformación de OpenAI; la selección de nodos, el empaquetamiento y el costo del algoritmo global publicado son diferentes [O1].

# 4. El puente explícito entre Anthropic y OpenAI

Combinando (3) y (11) obtenemos una identidad de operadores, válida para **todo** vector de ocho componentes:

```math
\boxed{\underbrace{S_3P}_{\text{intercambio}}\;=\;I_8\;=\;\underbrace{\sum_{t=1}^{13}w_tK(t)}_{\text{interpolación}}.}\tag{13}
```

**Teorema 1 — Correspondencia local de consultas.** Sean una firma `f ∈ ℚ⁸` y cualquier consulta lineal `L: ℚ⁸ → ℚ`. Las representaciones (3) y (11) producen la misma respuesta:

```math
L(S_3Pf)=L(f)=\sum_{t=1}^{13}w_t L(K(t)f).\tag{14}
```

**Demostración.** La primera igualdad procede de que intercambiar dos veces los mismos índices devuelve la identidad. La segunda procede de que cada entrada de `K(T)` es polinómica de grado a lo sumo doce y `K(0)=I₈`; la fórmula de interpolación (10) se aplica a todas sus entradas. La linealidad de `L` completa la demostración. ∎

El operador que lleva una firma de la ruta de intercambio a la ruta de deformación también queda definido explícitamente: se recupera `f=S₃b` y se construyen los trece vectores `K(t)f`; su recorrido inverso se realiza sumando los vectores con los pesos `w_t` y aplicando la permutación si se necesita regresar a los índices cruzados. **Existe transferencia exacta de datos entre estas dos representaciones locales declaradas.**

# 5. Generalización finita

**Teorema 2 — Correspondencia para `n` variables.** Para cualquier `n≥2`, sean `m=⌈n/2⌉` y `n'=2m`. Añadimos `n'−n` puertos auxiliares fijados en cero, usamos `m` paquetes diagonales `W₂(T)` y definimos `K_n(T)` por el mismo producto de polinomios `ℓ`. Entonces

```math
K_n(0)=I_{2^n},\qquad \deg K_n(T)_{y,x}\le 3n'.
```

Sea `D=3n'`. Se verifica la identidad exacta

```math
\boxed{\sum_{t=1}^{D+1}(-1)^{t-1}\binom{D+1}{t}K_n(t)=I_{2^n}.}\tag{15}
```

Si `S_n` intercambia los primeros dos índices y deja los restantes intactos, y `P_n` los reordena de vuelta, entonces `S_nP_n=I_{2^n}`. Por ello ambas rutas recuperan toda consulta lineal sobre la firma canónica.

**Demostración.** La evaluación `W₂(0)=I₂` da `K_n(0)=I`; cada uno de los `n'` factores tiene grado a lo sumo tres, por lo que el grado total es a lo sumo `D`; la fórmula de interpolación en `1,…,D+1` da (15). La identidad de intercambio se obtiene de (2) por producto tensorial con identidades. ∎

La prueba generaliza **la correspondencia entre operadores locales**. Sus representaciones extensionales tienen `2^n` componentes, y las matrices densas `K_n(t)` tienen `4^n` entradas. Esto determina una cota de construcción directa de orden `poly(n)·4^n` operaciones aritméticas, más la contabilidad de precisión; se trata de una cota explícita de esta implementación y de un punto de partida para investigar representaciones implícitas más económicas.

# 6. Controles numéricos reproducibles

El script adjunto, `verificar_puente.py`, ejecutó comparaciones mediante aritmética racional exacta (SymPy):

| Control | Resultado |
|:--|:--|
| `SWAP=I₄−2P₋` | Identidad matricial exacta |
| `S₃P=I₈` | Identidad matricial exacta |
| `W₂(0)=I₂`, `K(0)=I₈` | Identidades exactas |
| `Σ wₜK(t)=I₈` | Identidad de matrices 8 × 8, trece nodos |
| Consultas `p∈{0,1,*}³` | **27 de 27** recuperadas exactamente por las dos rutas |
| Consultas completamente fijadas | **8 de 8** componentes recuperadas |
| Conteo de la fórmula común `F★` | **3** soluciones: 011, 101 y 110 |
| Herencia de consultas (1) | Verificada para todas las fijaciones parciales |

La transformación auxiliar `K(1)` tiene rango 2, mientras `K(2),…,K(13)` tienen rango 8 en este control. Esto muestra numéricamente que **una evaluación auxiliar puede reunir distinciones** que la familia de evaluaciones recupera en conjunto. Los rangos describen estas matrices locales, no la complejidad de las fórmulas generales.

## 6.1. Por qué el conteo total es una referencia menos fina

La fórmula común `F★` tiene soluciones `{011,101,110}`. Otra fórmula `G=(¬x₁)∧(¬x₂∨¬x₃)` tiene soluciones `{000,001,010}`. Ambas dan `Z=3`. Sin embargo:

```math
Z_{x_1=0}(F_\star)=1,\qquad Z_{x_1=0}(G)=3.\tag{16}
```

Por ello, una representación que ofrece únicamente el entero `Z` reúne estas dos funciones, mientras la familia de consultas parciales las distingue. La conservación de consultas depende de la **referencia declarada**, tal como exige la formulación del programa.

# 7. Economía: comparación de recursos

La demostración del puente utiliza una firma extensional; su costo se declara expresamente.

| Operación | Ruta de intercambio local | Ruta de deformación local |
|:--|:--|:--|
| Representación de partida | Vector de `2^n` entradas | Vector de `2^n` entradas |
| Transformación | Permutación e intercambio tensorial | `D+1=O(n)` matrices auxiliares |
| Exactitud | `S_nP_n=I` | Interpolación exacta `ΣwₜK_n(t)=I` |
| En el control de 3 variables | Una permutación 8 × 8 | Trece matrices de 8 × 8 |
| Construcción densa directa general | `O(2^n)` entradas permutadas | `O(poly(n)4^n)` operaciones aritméticas |
| Recurso adicional | Índices de la permutación | Coeficientes y precisión de interpolación |

En el control de tres variables, trece productos matriz–vector densos de 8 × 8 tienen **832 productos de entrada** como cuenta directa superior, antes de sumar componentes y reconstruir consultas. Estas cantidades caracterizan **esta construcción de prueba**. El método canónico evalúa todas las asignaciones si se construye por enumeración, y la propia salida completa tiene `2^n` componentes.

El examen de economía de las publicaciones originales requiere conservar sus estructuras implícitas, sus cotas de rango, los tamaños de las contracciones, las evaluaciones auxiliares, su precisión y las recurrencias globales. Las igualdades locales (13) y (15) no establecen una mejora de tiempo de SAT; establecen el mapa exacto sobre el cual se puede plantear la comparación.

# 8. Lectura ROSI y continuidad del lenguaje

| Afirmación | Determinante y evidencia | Estado |
|:--|:--|:--|
| La familia de fijaciones parciales reconstruye las respuestas individuales | Fijaciones completas y (1); demostración | **[T]** |
| Intercambio local y deformación recuperan la misma firma | (13)–(15); demostración | **[T]** |
| Las 27 consultas y ocho componentes se recuperan | Verificación exacta adjunta | **[E]** |
| Anthropic y OpenAI publican procedimientos generales de conteo | Fuentes primarias [A1–A2], [O1] | **[P]** |
| La misma cota de recursos se transfiere entre sus algoritmos completos | Exige mapas entre operaciones y contabilidades globales | **[A]** |

**Interpretación.** El cubo de espejos proporciona una imagen de cambio de referencia y de agrupación de manifestaciones. La comparación formal muestra cuándo las respuestas permanecen recuperables. Las relaciones entre consultas tienen procedencia explícita; las transformaciones se juzgan por las respuestas que permiten reconstruir. La palabra **conservación** se reserva a esa continuidad verificable; **economía** se aplica después de establecer un modelo de operaciones. El cierre propio permanece como concepto ontológico de la organización y se examina mediante realizaciones operativas delimitadas.

# 9. Conclusión

La comparación alcanza un resultado matemático adicional respecto de la matriz anterior: **existe un puente explícito de operadores entre una representación local por intercambio y otra por deformación–interpolación, que preserva todas las consultas lineales de una firma común**. El control de tres variables recupera las 27 consultas de fijación parcial y permite distinguir firmas con el mismo conteo total.

El teorema finito describe cómo generalizar el puente y también identifica su costo extensional. La siguiente pregunta computacional queda determinada: encontrar condiciones que permitan construir y utilizar estas transferencias **sin desplegar la firma completa de `2^n` componentes**, y demostrar sus recursos frente a las contracciones y recurrencias concretas de los dos artículos.

# Fuentes y procedencia

**Documentos del programa**

- [P1] [*¿Cómo se cuantifica la información de un sistema?*](../2026-11-12_como_se_cuantifica_la_informacion/COMO_SE_CUANTIFICA_LA_INFORMACION.md), formalización integrada, Endless Monkey Project, 12-XI-2026.
- [P2] *¿Qué se conserva al cambiar la representación?*, extensión técnica v0.2, Endless Monkey Project, 12-XI-2026.
- [P3] *Una misma pregunta, tres mecanismos*, estudio comparativo v0.1, Endless Monkey Project, 12-XI-2026.
- [P4] *Imagen Total 3.9*, Ontología, lenguaje, formalización y laboratorios, 23-X-2026.

**Fuentes primarias de las construcciones externas**

- [A1] Anthropic, *A $`2^{o(n)}`$ Time Algorithm for 3-SAT*, Hexagon, versión 1, 27-X-2026, <https://hexagonmath.org/2610.00577>.
- [A2] Anthropic, *formal-math/eth*, README y formalización en Lean 4; el README enuncia, por bit, SWAP = I − 2·singlete, <https://github.com/anthropics/formal-math/blob/main/eth/README.md>.
- [O1] OpenAI, *The Exponential Time Hypothesis is False*, apéndice de contracción cuantitativa, § «A Cauchy deformation and integral local coordinates», <https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-contraction.tex>.

**Reproducción:** ejecutar `python3 verificar_puente.py` (requiere SymPy); el script genera `resultados_puente.json`. Contiene las matrices de intercambio, los trece operadores auxiliares, las 27 consultas y el contraste con una fórmula distinta del mismo conteo.

---

**Endless Monkey Project**  
*Relational Geometry Program*
