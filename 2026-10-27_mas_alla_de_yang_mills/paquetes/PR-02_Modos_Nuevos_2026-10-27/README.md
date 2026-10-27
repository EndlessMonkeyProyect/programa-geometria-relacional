# PGR — PR-02: Dónde vive la brecha al duplicar — modos heredados y modos nuevos

**Fecha:** 2026-10-27  
**Estado:** lema exacto elemental; tres controles declarados antes de calcular, con matrices explícitas; corrige el verificador de PR-01. **No demuestra la brecha física de Yang–Mills.**  
**Procedencia conceptual:** PR-01 (unidad u, duplicación isométrica J); R-02 (T4, F3); acta YM del 22-oct (forma de Poincaré `Var ≤ C·D`, T1/T2); YM-R3A. Documento aditivo: no sustituye fuentes.

## 1. Narrativa

PR-01 mostró que la unidad transportada conserva su resto cuando la pregunta se respeta al profundizar. Pero la unidad es lo que no cambia: hace de vacío. La brecha no pregunta por la unidad sino por todo lo demás: cuánto cuesta la diferencia más barata.

Al duplicar, cada nivel contiene dos cosas. Lo **heredado**: lo que ya se distinguía, visto con más puntos. Lo **nuevo**: lo que la duplicación permite distinguir por primera vez, que en estos modelos es siempre el signo opuesto entre las dos copias, el ± de cada nodo. PR-02 pregunta en cuál de los dos vive la diferencia más barata.

## 2. Contrato

- `H_n = R^(2^n)`, `u_n = (1,…,1)/sqrt(2^n)`, `J_n : H_n → H_(n+1)` isometría con `J_n u_n = u_(n+1)` (PR-01).
- Estructura relacional declarada: un grafo conexo `G_n` sobre los `2^n` puntos, forma `E_n(f) = Σ_aristas (f_x − f_y)²`, operador `L_n` con `E_n(f) = fᵀ L_n f`. Su núcleo son las constantes, es decir `u_n`.
- **Brecha:** `γ_n = min { E_n(f)/‖f‖² : f ⊥ u_n }`. Es la constante de Poincaré `Var(f) ≤ γ_n⁻¹ E_n(f)` (medida de conteo), la misma forma que exige el acta YM.
- **Descomposición** en el nivel `n+1`: `H_(n+1) = span(u) ⊕ V_her ⊕ V_nue`, con `V_her = J H_n ⊖ u` y `V_nue = (J H_n)^⊥`.
- **Medidas:** `γ_her` y `γ_nue`, mínimos de `E/‖·‖²` restringidos a cada parte; acoplamiento `κ = ‖Jᵀ L_(n+1) K‖`, con `K` base ortonormal de `V_nue`.

## 3. Lema exacto

Con `L u = 0`, para cada nivel:

- **(a)** `γ ≤ min(γ_her, γ_nue)`.
- **(b)** `γ ≥ min(γ_her, γ_nue) − κ`.
- **(c)** Si `κ = 0`, entonces `γ = min(γ_her, γ_nue)`.
- **(d)** Si además `Jᵀ L_(n+1) J = L_n` (la forma se hereda exacta), entonces `γ_her = γ_n` y `γ_(n+1) = min(γ_n, γ_nue)`. Por tanto `inf_n γ_n = min(γ_base, inf_n γ_nue)`: **bajo estas dos hipótesis, la brecha uniforme la deciden sólo los modos nuevos.**
- **(e)** Versión cuantitativa: si `Jᵀ L_(n+1) J = c·L_n + R` con `‖R‖ ≤ ε`, entonces `γ_(n+1) ≥ min(c·γ_n − ε, γ_nue) − κ`.

**Prueba.** (a) El mínimo sobre un subespacio no baja del mínimo sobre el todo. (b) En `u^⊥`, `L = D + C` con `D` diagonal por bloques (mínimo `min(γ_her, γ_nue)`) y `C` fuera de la diagonal con `‖C‖ = κ`; desigualdad de Weyl. (c) `C = 0`. (d) y (e): `J` lleva `u_n^⊥` isométricamente sobre `V_her`, y `E_(n+1)(Jf) = fᵀ Jᵀ L J f`. ∎

**Procedencia matemática:** Courant–Fischer y Weyl. Para estructuras producto, (d) es la tensorización clásica de la brecha espectral. Nada aquí es nuevo; el lema fija el contrato del programa.

## 4. Controles declarados y resultados

Los tres cumplen el contrato de PR-01 (`J` isométrica, `J u = u`, mismo resto de la unidad). Valores en unidades del grafo; extracto de `resultados.json`.

**Hipercubo** (J de PR-01; cada duplicación añade un bit, un eje nuevo e independiente). `κ = 0`, forma heredada exacta.

| puntos | γ | γ_her | γ_nue | peso heredado del modo bajo |
|---:|---:|---:|---:|---:|
| 4 | 2 | 2 | 2 | 0,500 |
| 64 | 2 | 2 | 2 | 0,833 |
| 2048 | 2 | 2 | 2 | 0,909 |

Brecha 2 en todo nivel. Cada duplicación aporta una dirección nueva con la misma brecha.

**Ciclo por volumen** (copia periódica `e_i → (e_i + e_(i+N))/√2`; el eje se alarga a paso fijo). `κ = 0`, forma heredada exacta.

| puntos | γ | γ_her | γ_nue | peso heredado |
|---:|---:|---:|---:|---:|
| 4 | 2 | 4 | 2 | 0 |
| 64 | 0,00963 | 0,0384 | 0,00963 | 0 |
| 2048 | 0,0000094 | 0,0000376 | 0,0000094 | 0 |

`γ = 4 sin²(π/2N) → 0`. El modo bajo es **enteramente nuevo**: la copia con signo opuesto.

**Ciclo por refinamiento** (J de PR-01; el mismo eje se subdivide a longitud fija, paso `a = 1/puntos`). Las hipótesis de (d) fallan: `Jᵀ L J = ½ L_n` y `κ = 1`.

| puntos | γ (red) | γ_her | γ_nue | peso heredado | γ física (`γ/a²`) |
|---:|---:|---:|---:|---:|---:|
| 8 | 0,586 | 1 | 2 | 0,854 | 37,49 |
| 64 | 0,00963 | 0,0192 | 2 | 0,998 | 39,45 |
| 2048 | 0,0000094 | 0,0000188 | 2 | 1,000 | 39,478 |

Los modos nuevos son de escala fina (`γ_nue = 2` siempre). El modo bajo es casi todo heredado, pero el acoplamiento baja su valor a la mitad de `γ_her`, aun con un peso nuevo minúsculo. En unidades de red `γ → 0`; en unidades físicas `γ → 4π² ≈ 39,478`, la brecha de un intervalo de longitud fija.

## 5. Lo que esto enseña

1. **Corrección.** En la revisión de PR-01 se afirmó que las excitaciones bajas aparecen en los modos nuevos. Es cierto cuando la duplicación agrega volumen. Es falso cuando subdivide a longitud fija: ahí lo nuevo es de escala fina y el modo bajo es heredado.
2. **PR-01 es ciego a la brecha.** Los tres controles conservan exactamente el resto de la unidad y tienen brechas opuestas.
3. **A volumen fijo todo tiene brecha.** El ciclo refinado tiene brecha física positiva y convergente sin masa alguna. Una red de dos plaquetas (propuesta R-03) tendrá brecha por la misma razón; el discriminante exige la dirección de volumen.
4. **Unidades.** El mismo `γ` de red que tiende a cero en el refinamiento corresponde a una brecha física positiva. El factor `c` de (e) es donde viven las unidades: `c = ½` en red, `c = 2` en unidades físicas.
5. **La cota de Weyl paga el acoplamiento completo.** En el refinamiento, (e) da una cota trivial (`min(0,29; 2) − 1 < 0`) aunque la brecha física verdadera converge; en unidades físicas `κ` crece como `1/a²`. Controlar el acoplamiento mejor que Weyl es exactamente la dificultad de un análisis multiescala.
6. **[H] Lectura en el lenguaje del programa.** Misma duplicación, misma unidad, mismo resto: brecha uniforme cuando lo nuevo es un eje independiente (hipercubo) y brecha que se diluye cuando lo nuevo repite el mismo eje (ciclo). Ver F5 antes de usar esta lectura.

## 6. Falsadores

- **F1.** Si al duplicar volumen la estructura física no hereda la forma (`c ≠ 1`) o acopla (`κ > 0`), (d) no aplica: usar (e) y medir `c`, `ε`, `κ`.
- **F2.** El ciclo por volumen es el control sin brecha, análogo de U(1) en fase de Coulomb. Un método que le atribuya brecha uniforme está mal.
- **F3.** Brecha positiva a volumen fijo no discrimina nada (refinamiento del ciclo: `4π²` sin masa).
- **F4.** Si (e) es trivial en un caso con brecha verdadera, falla el control del acoplamiento, no la brecha.
- **F5.** La brecha del hipercubo es pura tensorización de factores independientes, sin interacción. La lectura de §5.6 sólo cuenta si sobrevive con `κ > 0`; en Yang–Mills los grados de libertad nuevos están acoplados.

## 7. Siguiente contrato

Para Yang–Mills en red el bloqueo no hereda la forma exacta (el acoplamiento corre), `κ ≠ 0`, y la brecha se decide en la dirección de volumen y en unidades físicas. El paso mínimo es medir `c_n`, `ε_n`, `κ_n` y `γ_nue` sobre una estructura con interacción, en ambas direcciones, junto al control sin brecha de F2, y buscar una cota del acoplamiento más fina que Weyl.

## 8. Ejecución

    python verificar.py

Dependencia: `numpy`; unos 10 segundos. Regenera `resultados.json` a partir de matrices explícitas. Además recalcula con matrices los residuos de PR-01 y comprueba numéricamente su teorema; el `verificar.py` de PR-01 fijaba los residuos a mano y no construía `J`.

**Alcance:** modelos auxiliares de grafos con espectros conocidos de libro de texto. No usa datos físicos, no es Yang–Mills y no prueba una brecha física.
