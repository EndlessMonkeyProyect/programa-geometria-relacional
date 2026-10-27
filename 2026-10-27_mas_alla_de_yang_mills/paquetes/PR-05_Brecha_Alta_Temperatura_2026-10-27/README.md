# PGR — PR-05: Brecha uniforme a alta temperatura — resolución local contra influencia

**Fecha:** 2026-10-27  
**Estado:** teorema demostrado para la dinámica de baño térmico de Ising 2D. Es un **resultado conocido, reproducido** con el vocabulario del programa: la demostración completa está en §4 y los números que exige se obtienen por enumeración exhaustiva. Brecha uniforme en el volumen para β < 0,3322, con constante explícita para β < 0,3161. **No es Yang–Mills.**  
**Procedencia:** PR-04 §7, siguiente contrato: pasar de medir a demostrar, sobre un caso de respuesta conocida.

## 1. Qué se buscaba

PR-04 mostró que los números ordenan los regímenes pero no certifican una brecha. La pregunta abierta era si el lenguaje del programa puede sostener una **demostración**, no sólo describir mediciones. Se elige un teorema que ya existe: la brecha del baño térmico de Ising 2D es uniforme en el volumen a alta temperatura.

## 2. Vocabulario

| programa | objeto preciso |
|---|---|
| **ventana** de escala `b` (cierre local) | intersección de un cuadrado `b×b` trasladado con el volumen `Λ`; todo sitio está en exactamente `b²` ventanas |
| **entorno** de una ventana | valores de los vecinos externos: cada lado está ausente (borde de `Λ`) o presente con valores ±1 |
| **resolución** `m_b` | la brecha interna más lenta de una ventana, mínima sobre todas las formas (lados ≤ `b`) y todos los entornos |
| **influencia** `a(R,y)` | cuántos espines de la ventana `R` cambian en promedio cuando se invierte un vecino externo `y`, en el peor entorno |
| **influencia recibida** `α_b = A_b/b²` | `A_b` acota la suma de las influencias de un sitio sobre las `4b` ventanas que toca; se reparte entre las `b²` ventanas que lo contienen |
| **condición** | `α_b < 1`: la influencia que recibe cada sitio es menor que lo que cada ventana resuelve |
| **duplicación de escala** | pasar de ventanas `b` a `2b` |
| **criterio (g) de PR-04** | pérdida logarítmica acumulada `ln(γ_1/γ_Λ) ≤ ln(1/((1−α_b) m_b))` para todo `Λ` |

## 3. Teorema

**Contrato.** `Λ` es un rectángulo de `Z²` con frontera libre (o con cualquier condición ±1 fija afuera); `π` es la medida de Ising con `β ≥ 0`. La dinámica es de baño térmico con tasa 1 por sitio, `L_Λ = Σ_x (π_x − I)`, con forma de Dirichlet `E(f) = Σ_x π(Var_x f)` y brecha `γ_Λ`.

**Teorema.** Si `α_b(β) < 1`, entonces para todo rectángulo `Λ`:

    γ_Λ ≥ (1 − α_b(β)) · m_b(β) > 0.

## 4. Demostración

**Paso 1 — Influencia como transporte (Holley, Strassen).** Sea `R` una ventana con entorno `τ`, y sean `τ^−` y `τ^+` iguales salvo en un vecino `y`. En Ising ferromagnético, `π_R^(τ^−)` está estocásticamente dominada por `π_R^(τ^+)` (Holley). Entonces existe un acoplamiento monótono (Strassen), y bajo él el número esperado de espines distintos es exactamente `Σ_x (⟨σ_x⟩^+ − ⟨σ_x⟩^−)/2`. En consecuencia, la distancia de transporte con métrica de Hamming entre las dos condicionales es a lo sumo `a(R,y)`.

**Paso 2 — Contracción de la dinámica por ventanas.**
- **Dinámica.** Cada ventana `R` se remuestrea a tasa 1 según su condicional: `L_W = Σ_R (π_R − I)`. Es reversible respecto de `π`.
- **Acoplamiento.** Dos copias usan los mismos relojes y, en cada actualización, el acoplamiento óptimo. Para pasar del entorno de una copia al de la otra se cambia un vecino a la vez; por el Paso 1 y la desigualdad triangular, las discrepancias nuevas en `R` valen en esperanza a lo sumo `Σ_(y∼R) a(R,y)·1{X_y≠Y_y}`.
- **Conteo.** Las discrepancias viejas de `R` se borran. Cada sitio está en `b²` ventanas y es vecino de a lo sumo `4b`; el máximo sobre recortes en la definición de `A_b` cubre las ventanas cortadas por el borde. Por tanto `d/dt E ρ ≤ (A_b − b²) E ρ`, donde `ρ` es la distancia de Hamming.

**Paso 3 — De la contracción a la brecha.** Sea `φ` una autofunción de `L_W` con autovalor `−λ`, y sea `κ = b² − A_b`. Por el Paso 2, `e^(−λt)|φ(x)−φ(y)| ≤ Lip(φ)·e^(−κt)·ρ(x,y)` para todo `t`. Luego `λ ≥ κ`, es decir, `Var_π(f) ≤ κ⁻¹ Σ_R π(Var_R f)`.

**Paso 4 — De las ventanas a los sitios.** Para cada ventana, la brecha interna da `Var_R(f) ≤ m_b⁻¹ Σ_(x∈R) π_R(Var_x f)`. Como cada sitio está en `b²` ventanas, `Σ_R π(Var_R f) ≤ (b²/m_b) E(f)`. Con el Paso 3, `γ_Λ ≥ κ·m_b/b² = (1 − α_b) m_b`. ∎

## 5. Cálculo

`α_b` y `m_b` son máximos y mínimos sobre conjuntos finitos: todas las formas `r×s` con `r, s ≤ b` y todos sus entornos. Se calculan por **enumeración exhaustiva**:
- `b ≤ 3`: cálculo directo;
- `b = 4`: matriz de transferencia por columnas, verificada contra el cálculo directo para `b ≤ 3`, con diferencia ≤ 10⁻¹⁵.

El script comprueba además el signo de Holley en cada par de entornos y que `α_1 = 4 tanh β`, que es la condición clásica de Dobrushin.

## 6. Resultados

**Umbrales** (`α_b(β*) = 1`):

| b | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| β*_b | 0,2554 | 0,2935 | 0,3161 | 0,3322 |
| fracción de β_c = 0,4407 | 58 % | 67 % | 72 % | 75 % |

**Cotas explícitas frente a brechas exactas:**

| β | cota b = 1 | cota b = 2 | cota b = 3 | brecha exacta 4×4 | brecha exacta 3×6 |
|---:|---:|---:|---:|---:|---:|
| 0,20 | 0,2105 | 0,2571 | 0,2656 | 0,418 | 0,421 |
| 0,25 | 0,0203 | 0,1097 | 0,1338 | 0,312 | 0,314 |
| 0,30 | — | — | 0,0284 | 0,225 | 0,227 |

La cota queda por debajo de todas las brechas exactas calculadas, como debe. La resolución mínima resultó ser siempre la de la ventana `b×b` con entorno ausente. Es una observación; el teorema no la usa.

## 7. Lo que esto dice

1. **El lenguaje del programa puede sostener una demostración.** Cada paso tiene nombre en el vocabulario del programa, y la condición se lee como *la resolución local domina la influencia recibida*. Se satisface el criterio (g) de PR-04 con constante explícita.
2. **El teorema no es nuevo.** Para `b = 1` es la condición de Dobrushin (1968). Con ventanas es una versión de Dobrushin–Shlosman (1985). Los demás ingredientes también son conocidos: el acoplamiento monótono (Holley 1974; Strassen 1965), la comparación de ventanas a sitios (Martinelli, notas de 1999) y la contracción que implica brecha (Chen; Ollivier 2009). La uniformidad para todo `β < β_c` en 2D es de Martinelli–Olivieri–Schonmann (1994). Aquí se reproduce, no se descubre.
3. **La descomposición que funcionó no es la de PR-02 a PR-04.** No fue heredado contra nuevo al agregar espines, sino **resolución dentro de una ventana contra influencia desde su borde**, a escala fija. Lo útil de "duplicar" es agrandar la ventana, no agregar sitios.
4. **Hay una pared.** Los umbrales crecen cada vez menos (+0,038, +0,023, +0,016). Las cotas de `b = 3` son las mejores en los tres `β`, pero la ganancia frente a `b = 2` se achica. Si la tendencia siguiera como `1/b`, algo que sugieren sólo tres puntos y no está probado, este esquema se detendría cerca de 0,37, antes de `β_c`. La causa es que controla el **peor** entorno. Llegar a `β_c` exigió otra idea, que en 2D es que la mezcla débil implica mezcla fuerte (MOS): controlar el entorno típico, no el peor.
5. **Para Yang–Mills.** Una verificación finita como ésta, a acoplamiento fijo, es el análogo de la brecha a acoplamiento fuerte (Osterwalder–Seiler). El continuo exige `β → ∞`, y ahí las ventanas necesarias crecen sin límite y el control del peor caso no alcanza. Es el primer peldaño, no la escalera.

## 8. Falsadores y límites

- **F1.** Los umbrales se ubican por bisección suponiendo que `α_b` crece con `β`. Se observa, pero no está probado. El teorema vale con seguridad en los `β` donde se calculó `α_b < 1` con margen: 0,20, 0,25 y 0,30 (`b = 3`).
- **F2.** El cálculo es en doble precisión. Los márgenes `1 − α_b` en los `β` informados (≥ 0,095) son muchísimo mayores que el error de redondeo, que es del orden de 10⁻¹⁵.
- **F3.** Para `β ∈ [0,3161; 0,3322)` la constante es positiva por finitud, pero no se calculó: `m_4` no se evaluó.
- **F4.** Si alguien encuentra una brecha exacta por debajo de la cota en un rectángulo con `β < β*_b`, el teorema o su cálculo están mal. El script contrasta 7 rectángulos en 3 valores de `β`.

## 9. Ejecución

    python verificar.py            # completo, ~6 min; escribe resultados.json
    python verificar.py --rapido   # b ≤ 2, ~10 s; no escribe resultados

Dependencias: `numpy`, `scipy`.

**Alcance:** demuestra la brecha uniforme del baño térmico de Ising 2D para `β < 0,3322`. No toca el régimen crítico, ni el continuo, ni Yang–Mills.
