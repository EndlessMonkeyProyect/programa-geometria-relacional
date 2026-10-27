# PGR — PR-03: Duplicar con interacción — una cadena que crece por volumen

**Fecha:** 2026-10-27  
**Estado:** mediciones exactas en dimensión finita (hasta 11 espines, 2048 estados) y una cota elemental nueva (f). **No demuestra la brecha física de Yang–Mills.**  
**Procedencia conceptual:** PR-01 (unidad u, duplicación isométrica J); PR-02 (lema (a)–(e), hipercubo, falsador F5, ciclo como control); acta YM del 22-oct (forma de Poincaré `Var ≤ C·D`). Documento aditivo: no sustituye fuentes.

## 1. Narrativa

En PR-02 el hipercubo fue el caso en que cada duplicación añade un bit nuevo e independiente, y la brecha se conservaba. Pero ese bit no tocaba a nadie. Aquí el espín nuevo se acopla con su vecino: lo nuevo ya no es independiente de lo heredado. La pregunta es la de PR-02, ahora con interacción: ¿sobrevive la brecha al crecer el volumen, y dónde vive?

## 2. Contrato

- **Estados:** configuraciones de `m` espines ±1, es decir los mismos `2^m` puntos de PR-01.
- **Medida:** cadena abierta de Ising, `π_m(σ) ∝ exp(β Σ σ_k σ_(k+1))`, sin campo.
- **Dinámica declarada:** baño térmico en cada sitio, con tasa `π(σ^k)/(π(σ)+π(σ^k))`; es reversible respecto de `π`. Se trabaja en `L²(π)`. Su brecha es la constante de Poincaré `Var_π(f) ≤ γ⁻¹ E(f)`, la misma forma que pide el acta YM.
- **Duplicación por volumen:** agregar un espín al final de la cadena; `J` levanta `f(σ)` a la cadena más larga.
  - `J` es isometría exacta porque la marginal de la cadena de `m+1` espines sobre los primeros `m` es exactamente `π_m`: sumar el último espín da `2 cosh β`, constante. Además `J u = u` con `u = √π`.
  - Con `β = 0`, `J` es la de PR-01 y la estructura es el hipercubo de PR-02.
  - **Modos nuevos:** funciones con media condicional cero respecto del espín nuevo.
- **Medidas:** las de PR-02 (`γ`, `γ_her`, `γ_nue`, acoplamiento `κ`, peso heredado del modo bajo), más:
  - **defecto de herencia** `ε = ‖Jᵀ S J − S_m‖`, con `c = 1`;
  - **pérdida por nivel** `δ = γ_m − γ_(m+1)`;
  - **valores efectivos sobre el modo bajo previo** `φ`: `ε_ef = ⟨φ, Rφ⟩` y `κ_ef = ‖Kᵀ S J φ‖`.
- **Referencias externas, no constitutivas:**
  - Las tasas de baño térmico coinciden, en el interior de la cadena, con las de Glauber (1963). La brecha en volumen infinito es `1 − tanh 2β`.
  - La masa de la matriz de transferencia es `m = −ln tanh β`, y la longitud de correlación es `ξ = 1/m`.

## 3. Lema: una cota mejor que Weyl

Se conservan (a)–(e) de PR-02; el script las verifica en cada nivel. Se añade:

- **(f)** Si `γ_her ≥ a`, `γ_nue ≥ b` y el acoplamiento es `κ`, entonces `γ ≥ ½(a+b) − √(¼(b−a)² + κ²)`.

**Prueba.** Para `ψ = v + w`, con `v` heredado, `w` nuevo y `‖v‖² + ‖w‖² = 1`, se tiene `⟨ψ, Sψ⟩ ≥ a‖v‖² + b‖w‖² − 2κ‖v‖‖w‖`. Esto es al menos el mínimo de la matriz `[[a, −κ], [−κ, b]]`. ∎

La cota es creciente en `a`, así que puede combinarse con (e): `γ_(m+1) ≥ F(γ_m − ε, γ_nue, κ)`. Cuando `b ≫ a` es mucho más fina que Weyl, porque cobra aproximadamente `κ²/(b−a)` en lugar de `κ`.

## 4. Resultados

**β = 0.** Reproduce exactamente el hipercubo: `γ = 1`, `κ = ε = 0` en todo nivel.

**β = 1.0** (extracto; el resto en `resultados.json`):

| espines | γ | γ_her | γ_nue | κ | ε | κ_ef | ε_ef | pérdida δ | peso her. | cota iterada (e)+(f) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 0,1431 | 0,1834 | 1,367 | 0,482 | 0,367 | 0,166 | −0,044 | 0,0953 | 0,964 | −0,27 |
| 5 | 0,0880 | 0,0975 | 1,367 | 0,482 | 0,367 | 0,063 | −0,0062 | 0,0189 | 0,990 | −1,21 |
| 8 | 0,0631 | 0,0660 | 1,367 | 0,482 | 0,367 | 0,032 | −0,0016 | 0,0056 | 0,997 | −2,51 |
| 11 | 0,0532 | 0,0546 | 1,367 | 0,482 | 0,367 | 0,021 | −0,0007 | 0,0025 | 0,998 | −3,76 |

**Resumen por acoplamiento:**

| β | γ (11 espines) | límite exacto | extrapolado | error | ξ (sitios) | κ | ε | exponente de δ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0,5 | 0,2605 | 0,2384 | 0,2389 | +0,2 % | 1,3 | 0,381 | 0,176 | 2,7 |
| 1,0 | 0,0532 | 0,0360 | 0,0381 | +5,9 % | 3,7 | 0,482 | 0,367 | 2,5 |
| 1,5 | 0,0133 | 0,00495 | 0,00687 | +39 % | 10,0 | 0,498 | 0,450 | 2,4 |

**Control: ciclo por volumen** (PR-02). La brecha tiende a 0, `κ = ε = 0`, y el modo bajo es enteramente nuevo (peso heredado 0). El método lo detecta como sin brecha.

**Observación sin prueba:** `γ_nue = 1 + ε` en todos los niveles y acoplamientos, con error menor que 10⁻¹⁰. No se usa como lema.

## 5. Lo que esto enseña

1. **La brecha sobrevive a la interacción.** En esta cadena es uniforme en volumen para todo `β` finito y tiende a `1 − tanh 2β`. Es lo esperado: en una dimensión no hay transición de fase.
2. **No la deciden los modos nuevos.** Lo nuevo es rápido y local (`γ_nue` entre 1,2 y 1,5 desde 3 espines). El modo bajo es colectivo y casi enteramente heredado (peso > 0,99). Es lo contrario del control. Esto responde F5 de PR-02: con interacción, el mecanismo del hipercubo ("cada eje nuevo trae la misma brecha") no persiste, y la lectura [H] de PR-02 §5.6 no sobrevive como mecanismo.
3. **Las normas de operador no alcanzan.** `ε` y `κ` son constantes por nivel, porque son defectos locales en la frontera. Toda recursión que los cobre completos pierde una cantidad fija por nivel y queda trivial después de dos o tres niveles, aun usando (f). Mientras tanto, la brecha verdadera sigue positiva.
4. **Lo que sí decrece son los efectos sobre el modo bajo.**
   - `κ_ef` decae como `N^(−1,3)` y `ε_ef` como `N^(−2,6)`.
   - La pérdida por nivel decae como `N^(−2,4…2,7)`, que es sumable.
   - El defecto actúa en la frontera, y el modo bajo, extendido sobre toda la cadena, apenas lo siente.

   Una prueba de brecha uniforme tiene que acotar la pérdida por nivel con algo sumable, como el peso del modo bajo donde actúa el defecto, y no con la norma de operador. Ése es el núcleo de los argumentos de localidad y multiescala.
5. **El volumen tiene que ser mucho mayor que ξ.** Extrapolar desde 11 espines falla por 0,2 % con `ξ = 1,3`, por 6 % con `ξ = 3,7` y por 39 % con `ξ = 10`. Cuando `ξ` es comparable al volumen, el volumen finito sobreestima la brecha. En Yang–Mills en red, cerca del continuo, `ξ` en unidades de red diverge; por eso la evidencia numérica no sustituye el control analítico de la dirección de volumen.
6. **Brecha de Poincaré no es masa.** La brecha medida aquí es dinámica; la masa es la de la matriz de transferencia.
   - Para `β` grande, `γ_∞ ≈ m²/2`: con β = 1,5, `0,00495` frente a `0,00497`.
   - Hay teoremas que relacionan la positividad uniforme de una con el decaimiento exponencial de correlaciones en sistemas de espines de alcance finito (Stroock–Zegarlinski; Martinelli–Olivieri). No relacionan sus valores.
   - La forma de Poincaré del acta YM sería, a lo sumo, una ruta hacia la positividad de la masa, no hacia su valor.

## 6. Falsadores

- **F1.** Si la pérdida por nivel decae como `N⁻¹` o más lento, su suma diverge y no hay brecha uniforme. Hay que medir el exponente, no sólo el signo.
- **F2.** Con volumen menor que unos 10 `ξ`, las extrapolaciones no son confiables (caso β = 1,5).
- **F3.** No leer una brecha de Poincaré como masa.
- **F4.** En una dimensión la brecha está garantizada. El ciclo es un control sin interacción. Falta un control **con** interacción y **sin** brecha, como Ising 2D crítico o U(1) 4D a acoplamiento débil; sin él, el método no ha sido puesto a prueba donde puede fallar.
- **F5.** `γ_nue = 1 + ε` es sólo una observación numérica; no usarla sin prueba.

## 7. Siguiente contrato

1. Probar una cota sumable de la pérdida por nivel en términos del peso del modo bajo en la región donde actúan `R` y el acoplamiento (localidad).
2. Construir un control con interacción y sin brecha (F4).
3. Abrir la dirección del continuo: hacer crecer `β` con el nivel para que `ξ` crezca con el volumen, y medir en unidades físicas.

## 8. Ejecución

    python verificar.py

Dependencia: `numpy`; unos 25 segundos. Regenera `resultados.json` a partir de matrices explícitas en `L²(π)`. Las aserciones comprueban la marginal exacta, la isometría, la reversibilidad, el lema (a), (b), (e) y (f) en cada nivel, y las afirmaciones cualitativas de la §4. Los exponentes y errores de extrapolación se calculan y se informan, no se imponen.

**Alcance:** la cadena de Ising unidimensional y su dinámica de Glauber son modelos de libro de texto; aquí se usan como banco de pruebas del contrato de duplicación del programa. No es Yang–Mills y no prueba una brecha física.
