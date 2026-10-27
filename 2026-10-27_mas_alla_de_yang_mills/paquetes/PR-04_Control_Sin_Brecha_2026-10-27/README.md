# PGR — PR-04: El control que puede fallar — interacción sin brecha

**Fecha:** 2026-10-27  
**Estado:** corrige un argumento de PR-03; añade el criterio exacto (g); pone a prueba las medidas de PR-02 y PR-03 en Ising 2D, que tiene brecha o no según el acoplamiento. Cálculo exacto en dimensión finita, hasta 20 espines (2²⁰ estados). **No demuestra la brecha física de Yang–Mills.**  
**Procedencia conceptual:** PR-01 a PR-03; acta YM del 22-oct (forma de Poincaré). Documento aditivo: no sustituye fuentes.

## 1. Corrección de PR-03

PR-03 §5.4 presentó como apoyo a la brecha que la pérdida por nivel `δ = γ_N − γ_(N+1)` "decae como N^(−2,5), que es sumable". Ese argumento es vacío. Si la brecha baja y nunca es negativa, entonces `Σ δ = γ_inicial − γ_∞ ≤ γ_inicial`: la suma de pérdidas absolutas es finita **siempre**, haya brecha o no. Por la misma razón su falsador F1 no discrimina nada.

Este documento además muestra (§5.1) que el acoplamiento efectivo `κ_ef` también decrece en sistemas sin brecha; tampoco es evidencia.

La conclusión de PR-03 —la cadena 1D tiene brecha uniforme— sigue en pie, porque coincide con el valor exacto conocido `1 − tanh 2β`. Lo que estaba mal era el argumento, no el resultado.

## 2. El criterio correcto (g)

Sea `ℓ_N = ln(γ_N / γ_(N+1))`, la **pérdida logarítmica** por nivel. Entonces:

- `ln γ_N = ln γ_1 − Σ_(k<N) ℓ_k`, de modo que **la brecha es uniforme si y sólo si `Σ ℓ_k` está acotada**.
- Con `L = N^(1/d)` el lado del sistema, se define el **exponente efectivo** `z_ef = ℓ / Δ ln L`. Entonces `Σ ℓ = Σ z_ef · Δ ln L`.
- Si `z_ef ≥ z₀ > 0` de cierto tamaño en adelante, la brecha cae al menos como `L^(−z₀)`. Una brecha uniforme exige que `z_ef → 0` lo bastante rápido como para que esa suma converja.

Es una identidad telescópica; no hay nada que probar. Su valor está en que señala la cantidad correcta: **la pérdida relativa por escala, no la absoluta**.

## 3. Contrato del control

- **Modelo:** Ising 2D con frontera libre, sobre un cuadrado que crece espín a espín. Cada prefijo de `k²` espines es un cuadrado `k×k` y cada prefijo de `k(k+1)` un rectángulo `k×(k+1)`. Misma dinámica de baño térmico en `L²(π)` que PR-03.
- **Tres regímenes**, con sus resultados conocidos en la literatura:
  - **alta temperatura**, `β = 0,25`: brecha uniforme (Martinelli–Olivieri–Schonmann, para todo `β < β_c` en 2D);
  - **crítico**, `β_c = ½ ln(1+√2) ≈ 0,4407`: la brecha cierra como `L^(−z)`, con `z ≈ 2,17` según estimaciones numéricas;
  - **baja temperatura**, `β = 0,6`: la brecha cierra más rápido que cualquier potencia, exponencialmente en `L` por el paso entre las fases + y − (Thomas; Martinelli).
- **Referencias:** cadena 1D de PR-03 con β = 0,5 y 1,5, ahora hasta 16 espines; ciclo libre de PR-02, con `z = 2` exacto.
- **Lo heredado cambia en 2D.** Cuando el espín nuevo tiene dos vecinos viejos, sumarlo induce una interacción efectiva entre ellos: la marginal de `π_(N+1)` sobre los espines viejos ya no es `π_N`. `J` es entonces isometría desde `L²(μ_N)`, con `μ_N` esa marginal. El cambio se mide con la distancia de variación total `TV(μ_N, π_N)`: es 0 cuando el espín nuevo tiene un solo vecino, y entre 0,03 y 0,12 cuando tiene dos. El lema (a), (b), (c) y (f) se aplica en cada nivel; (d) y (e) no, porque comparan espacios distintos.

## 4. Resultados

**Exponente efectivo, comparando forma con forma.** Pasar de cuadrado a rectángulo y de rectángulo a cuadrado no son pasos equivalentes, así que se separan.

| régimen | cuadrados 1→4 · 4→9 · 9→16 | rectángulos 2→6 · 6→12 · 12→20 | tendencia | lo conocido |
|---|---|---|---|---|
| alta T | 0,89 · 0,84 · 0,71 | 0,91 · 0,80 · 0,67 | baja | brecha uniforme |
| crítico | 1,77 · 1,92 · 1,97 | 1,90 · 1,99 · 2,01 | sube hacia ≈ 2 | sin brecha, `z ≈ 2,17` |
| baja T | 2,59 · 3,09 · 3,59 | 2,85 · 3,37 · 3,88 | crece | sin brecha, cierre exponencial |
| 1D, β = 0,5 | — | — | 0,15 → 0,09 (espines 10→16) | brecha uniforme |
| 1D, β = 1,5 | — | — | 0,81 → 0,67 (espines 10→16) | brecha uniforme, `ξ = 10` |
| ciclo libre | — | — | 2 exacto | sin brecha |

**Brecha en los cuadrados y en 4×5:**

| espines | alta T | crítico | baja T |
|---:|---:|---:|---:|
| 4 | 0,538 | 0,293 | 0,166 |
| 9 | 0,383 | 0,134 | 0,0476 |
| 16 | 0,312 | 0,0762 | 0,0169 |
| 20 | 0,292 | 0,0619 | 0,0112 |

**Medidas estructurales con 20 espines.**

| régimen | peso heredado | γ_nue | κ | κ_ef | TV (dos vecinos) |
|---|---:|---:|---:|---:|---:|
| alta T | 0,996 | 1,10 | 0,32 | 0,042 | 0,03 |
| crítico | 0,999 | 1,20 | 0,46 | 0,032 | 0,08 |
| baja T | 1,000 | 1,21 | 0,50 | 0,017 | 0,09 |

## 5. Lo que esto enseña

1. **Las medidas estructurales no deciden la brecha.** Peso heredado cercano a 1, modos nuevos rápidos, acoplamiento de operador constante y acoplamiento efectivo decreciente aparecen igual con brecha y sin ella. El `κ_ef` incluso es menor en baja temperatura, donde la brecha cierra más rápido. Las medidas de PR-02 y PR-03 describen dónde viven los modos, no si hay brecha.
2. **El exponente efectivo sí separa los casos nítidos.** El crítico sube hacia el valor conocido; la baja temperatura crece; la cadena 1D con β = 0,5 cae a 0,09; el ciclo da 2. En los tamaños medidos, el orden alta T < crítico < baja T se cumple en cada paso.
3. **Pero no certifica una brecha.** La alta temperatura en 2D y la cadena 1D con β = 1,5 tienen brecha según la teoría, y sin embargo sus `z_ef` valen 0,6 o 0,7 y bajan despacio. Con estos tamaños son indistinguibles de un sistema sin brecha con exponente pequeño. En 2D con frontera libre, además, es de esperar que la fracción de frontera (≈ 4/L) haga que la brecha se acerque a su valor de bulto sólo como `1/L`, lo que retrasaría la caída de `z_ef`.
4. **Lo heredado no es lo anterior.** En 2D, agregar un espín con dos vecinos cambia la estadística de lo que ya estaba (TV hasta 0,12). Toda recursión entre niveles tiene que incluir ese cambio de medida, no sólo el acoplamiento. [Lectura] Es la versión medible del recierre: lo nuevo obliga a volver a cerrar lo heredado.
5. **Para Yang–Mills.** Lo que una prueba necesita es acotar `Σ ℓ`, la pérdida relativa por escala, con constantes controladas al acercarse al continuo. Estos cálculos muestran que, cuando el tamaño es comparable a la longitud de correlación, los números ordenan los regímenes pero no deciden. En la red 4D, cerca del continuo, esa longitud crece muy rápido con β; por eso la dirección de volumen sólo puede controlarse analíticamente.

## 6. Falsadores

- **F1** (sustituye al F1 de PR-03). Una afirmación de brecha debe acotar `Σ ℓ` (relativa), no `Σ δ` (absoluta).
- **F2.** Peso heredado, `γ_nue`, `κ` y `κ_ef` no son criterios de brecha.
- **F3.** Que `z_ef` decrezca en tamaños menores que unos 10 ξ no es evidencia de brecha (alta T en 2D, cadena con β = 1,5).
- **F4.** En 2D lo heredado cambia (TV > 0); una recursión que lo ignore es incorrecta.
- **F5.** Todo aquí descansa en sistemas pequeños: hasta 20 espines, lado ≤ 4,5. Las tendencias son cualitativas.

## 7. Estado de la serie y siguiente contrato

PR-01 a PR-04 dejaron:

- **un vocabulario preciso:** unidad (vacío), heredado y nuevo, acoplamiento, pérdida logarítmica;
- **cuatro hechos:**
  1. el resto de PR-01 es ciego a la brecha;
  2. dónde vive el modo bajo depende de la dirección de crecimiento;
  3. las medidas estructurales no deciden la brecha;
  4. la cantidad decisiva es `Σ ℓ`, que los números no certifican cerca de la criticidad.

El siguiente paso con sentido es **analítico y sobre un caso de respuesta conocida**: acotar `ℓ` por duplicación de escala en Ising 2D con `β < β_c`, reproduciendo con el vocabulario del programa un teorema que ya existe. Sería la primera comprobación de que el lenguaje del programa puede sostener una demostración, y no sólo describir resultados.

## 8. Ejecución

    python verificar.py            # completo, hasta 20 espines en 2D; ~10 min; escribe resultados.json
    python verificar.py --rapido   # hasta 16 espines; ~1 min; no escribe resultados

Dependencias: `numpy`, `scipy`. Todo se calcula con matrices dispersas explícitas. Los resolvedores dispersos arrancan de un vector fijo, y `resultados.json` se regenera idéntico en una carpeta limpia. La norma del acoplamiento se calcula como la raíz del mayor autovalor de XᵀX, con una tolerancia alcanzable en doble precisión. Una versión anterior usaba una tolerancia inalcanzable que a veces impedía converger; el cambio altera los resultados en menos de 2·10⁻¹⁵. Las aserciones comprueban en cada nivel la isometría, el vacío y el lema (a), (b) y (f). También comprueban el orden entre regímenes en cada paso, la tendencia de cada régimen, la semejanza de las medidas estructurales y que la marginal 1D sea exacta.

**Alcance:** Ising 1D y 2D con dinámica de Glauber son modelos de libro de texto, y los resultados de brecha citados son conocidos. Aquí se usan para poner a prueba el método del programa donde puede fallar. No es Yang–Mills y no prueba una brecha física.
