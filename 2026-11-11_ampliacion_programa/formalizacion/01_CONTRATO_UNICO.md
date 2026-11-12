# Un contrato para transportar una afirmación entre laboratorios

## 1. Datos mínimos [D]

Se declara

\[
\mathcal K=(X,R,\mathcal Q,C,\cdot,\Phi,\delta,\mathsf{Enc},\mathsf{Cost}),
\]

con:

| Símbolo | Función |
|---|---|
| `X` | conjunto de estados admisibles (finito en los controles de este paquete) |
| `R` | referencia y las transformaciones o escalas que permite |
| `𝒬` | familia de consultas con codominio especificado |
| `(C,∘,e)` | monoide de continuaciones, cuando se necesite la noción de futuro |
| `x·c` | acción de continuación sobre `X` |
| `Φ:X→S` | firma que se pretende conservar |
| `δ` | modificación admisible de referencia, vínculo, consulta o dinámica |
| `Enc` | codificación y algoritmos de construcción, actualización y lectura |
| `Cost` | modelo de operaciones, bits, memoria, precisión y línea base |

Una realización puramente estática puede fijar `C={e}`. Si se afirma un resultado sobre **todas** las continuaciones, sus elementos y su acción deben estar definidos.

## 2. Distinciones observables [D]

\[
x\sim_{\mathcal Q}y \quad\Longleftrightarrow\quad \forall q\in\mathcal Q:\;q(x)=q(y).
\]

En conjuntos finitos, el número de clases `N_𝒬 = |X/∼_𝒬|` mide la capacidad de discriminación de la familia; `log₂ N_𝒬` es una cantidad informacional y no el tiempo de ejecución.

Para una única consulta `q`, su recuperación desde `Φ` equivale a la existencia de `g` con `q=g∘Φ`. Si se requiere continuidad, la firma debe conservar `q(x·c)` para cada continuación admitida, no solo `q(x)`.

## 3. Continuaciones [T: resultado ya conocido]

Para `Q:X→Y`, defina

\[
x\equiv_{Q,C}y \quad\Longleftrightarrow\quad
Q(x\cdot c)=Q(y\cdot c)\ \text{para todo }c\in C.
\]

El cociente `X/≡` conserva las respuestas a todas las continuaciones. La estabilidad de esta relación bajo la acción y su minimalidad como interfaz son parte del **resultado ya publicado** en *Recierre contextual, residuo y costo de una interfaz*. El presente paquete adopta esa construcción y añade una medición finita del residuo requerido cuando cambia la consulta.

## 4. Estado lógico de una consulta [D]

Dada una familia de configuraciones compatibles `A⊆X` y una consulta `q`:

- **Incompatible:** `A=∅`.
- **Determinada:** `A≠∅` y `|q(A)|=1`.
- **Indefinida:** `A≠∅` y `|q(A)|>1`.

Esta triple partición evita confundir falta de respuesta única con contradicción.

## 5. Ficha de una afirmación

Cada nueva entrada del programa identifica: `ID; formulación; tipo de estado [O/D/T/E/I/A/F]; fuente/versión; contrato K; determinante δ; respuesta conservada; testigo de novedad; demostración o prueba; costo; falsador; siguiente obligación`.
