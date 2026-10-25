# O17-F — Qué es contenido del plano en el presupuesto de vorticidad: escalera de resolución
**Le Matt Ansatz Di Ego · 19 octubre 2026**

**Leyenda:** [T] teorema; [E] medición; [D] criterio; [A] abierto.

## 1. Pregunta

O17-A dio un criterio: solo es contenido de un plano lo que no cambia cuando la misma realidad se describe con más detalle. En Navier–Stokes, «más detalle» es más resolución, y «el plano» son los observables a escala física fija. La rama ya había comparado N=128 con N=192 y encontrado que las medianas por clase coinciden y los términos puntuales de segundo orden no. Faltaba un nivel más fino para juzgar si su referencia (N=192) ya estaba convergida, y faltaba una reproducción independiente.

## 2. Diseño (prerregistrado antes de correr, `PRERREGISTRO_O17F.json`)

- **Flujo:** la corrida A de la rama (ν = 0.008, forzamiento de potencia constante 0.1 en |k| ≤ 2, semilla 20261004), con el solucionador y el presupuesto de la rama sin modificar. Arranque: N=64 hasta t=10, luego N=128 hasta t=15, todo en doble precisión.
- **Escalera:** desde el mismo estado en t=15, evolución de 0.6 unidades de tiempo (≈ 2.2 τ_η) con dt = 4·10⁻³ en N = 64 (truncado), 128, 192 y 256 (interpolados).

| N | kmax·η | Re_λ | ε | CFL | Puntos evaluados (modo alto) |
|---:|---:|---:|---:|---:|---:|
| 64 | 0.98 | 48.2 | 0.1144 | 0.09 | 15 714 |
| 128 | 1.96 | 48.2 | 0.1142 | 0.19 | 129 025 |
| 192 | 2.94 | 48.2 | 0.1142 | 0.28 | 435 587 |
| 256 | 3.93 | 48.2 | 0.1142 | 0.38 | 1 032 319 |

- **Comparación puntual:** los mismos 64³ puntos físicos en los cuatro niveles, en q > 3 q_rms con a > 0.
- **Comparación estadística:** el modo alto de la rama (todo q > 2 q_rms más 2 % uniforme, con pesos de volumen). Incertidumbre por bootstrap espacial pareado: 512 bloques físicos idénticos en todos los niveles, 400 réplicas.
- **Criterios [D]:** puntual acreditado si la mediana del error relativo frente a N=256 es ≤ 5 %. Estadística acreditada si el IC95 de la diferencia con N=256 contiene 0, o si la diferencia es ≤ 2 % relativo (≤ 0.01 absoluto en fracciones). «Contenido del plano» si está acreditada en N=192 y la diferencia baja de forma monótona desde N=64.

## 3. Reproducción independiente [E]

Antes de agregar N=256, reconstruí desde cero la auditoría 128↔192 de la rama con evolución en doble precisión (la rama la había hecho en simple). Sobre los mismos 720 puntos, los errores puntuales coinciden con la tabla publicada a 3–4 cifras: por ejemplo `b` 0.0935 frente a 0.0935, `V_c` 0.4287 frente a 0.4290, `Y` 0.2629 frente a 0.2628. A estos horizontes, la precisión de la evolución no cambia los observables.

Las estadísticas de clase de este único instante caen dentro de su propio IC95 en 24 de 26 comparaciones con las tablas de la rama, que promedian cinco y tres instantes. Las dos que quedan fuera son esperables, porque el bootstrap espacial no captura la variación temporal.

## 4. Resultados puntuales [E]

Mediana de |x_N − x_256| / |x_256| en q > 3 q_rms (* = acreditado, ≤ 5 %):

| Cantidad | N=64 | N=128 | N=192 |
|---|---:|---:|---:|
| ω (vorticidad) | 0.077 | 0.006* | 0.000* |
| τ (giro por deformación) | 0.37 | 0.026* | 0.002* |
| b (giro material) | 0.51 | 0.097 | 0.013* |
| r_ν⊥ (residuo viscoso transversal) | 0.76 | 0.25 | 0.039* |
| 𝒫 (presión, segundo orden) | 0.64 | 0.14 | 0.021* |
| 𝒱_c (viscoso, segundo orden) | 0.90 | 0.42 | **0.089** |
| 𝒴 (segunda derivada material) | 0.70 | 0.27 | **0.059** |

**Clasificación individual de estados de bajo giro** (ρ⊥ < 0.05 en q > 3 q_rms) frente a N=256, índice de Jaccard: 0.03 en N=64, 0.50 en N=128 y 0.77 en N=192. Con N=256 hay solo 12 estados así en la malla común.

## 5. Resultados estadísticos [E]

| Estadística (N=256 [IC95]) | Δ N=64 | Δ N=128 | Δ N=192 | Prerregistro | Acreditada desde (posterior) |
|---|---:|---:|---:|---|---|
| mediana ρ⊥, a>0: 0.693 [0.680, 0.705] | +0.067 | +0.007 | +0.000 | plano, robusta | 128 |
| mediana ρ⊥, q>2: 0.809 [0.780, 0.835] | −0.047 | −0.004 | +0.001 | plano, robusta | 128 |
| mediana ρ⊥, q>3: 0.786 [0.719, 0.845] | −0.002 | −0.006 | +0.002 | no monótona | 64 |
| mediana ρ⊥, q>4: 0.648 [0.542, 0.805] | −0.063 | +0.040 | +0.006 | plano, robusta | 64 |
| mediana Λ⊥, q>3: 2.73 [2.33, 3.24] | −0.22 | +0.02 | −0.01 | plano, robusta | 64 |
| mediana 𝒟⊥, q>3: 0.770 [0.727, 0.805] | +0.053 | −0.004 | −0.002 | plano, robusta | 128 |
| mediana cos φ, q>3: −0.385 [−0.520, −0.277] | +0.009 | +0.024 | −0.003 | no monótona | 64 |
| mediana s_P, q>3: 9.96 [8.56, 11.64] | −2.40 | −0.06 | −0.09 | no monótona | 128 |
| mediana s_V, q>3: −8.63 [−10.29, −7.15] | +2.19 | +0.06 | +0.02 | plano, robusta | 128 |
| mediana d log|b|/dG, q>3: −0.29 [−1.16, +0.52] | −0.04 | **+0.25** | +0.04 | no monótona | 192 |
| fracción s_P > 0, q>3: 0.860 [0.820, 0.894] | −0.023 | −0.004 | −0.001 | plano, robusta | 64 |
| fracción s_V < 0, q>3: 0.904 [0.875, 0.930] | +0.013 | **−0.026** | −0.005 | no monótona | 192 |
| fracción d log|b|/dG > 0, q>3: 0.484 [0.438, 0.533] | −0.010 | **+0.014** | +0.002 | no monótona | 192 |
| P(ρ⊥<0.05), q/q_rms ∈ [0,1): 0.045 | −0.022 | −0.005 | −0.001 | plano, robusta | 128 |
| P(ρ⊥<0.05), [1,2): 0.034 | +0.002 | −0.002 | −0.001 | plano, robusta | 64 |
| P(ρ⊥<0.05), [2,3): 0.021 | +0.007 | +0.001 | −0.000 | plano, robusta | 64 |
| P(ρ⊥<0.05), [3,4): 0.024 | −0.004 | +0.001 | −0.001 | plano, robusta | 64 |
| P(ρ⊥<0.05), [4,5): 0.009 | +0.021 | +0.002 | +0.002 | no monótona | 64 |
| mediana \|e⊥\|/\|b\| (truncamiento), q>3: 0.0015 | +0.58 | +0.12 | +0.014 | **no acreditada** | — |

**Con el criterio prerregistrado**, 11 de las 19 estadísticas son contenido del plano y las 11 son además robustas: ya están acreditadas en N=128. Siete más están acreditadas en N=192 pero no cumplen la monotonía, porque algún nivel grueso cayó cerca del valor de referencia por azar de muestreo. El diagnóstico de truncamiento no se acredita en ningún nivel, y no debería: mide por construcción el error de la descripción y tiende a cero.

**Lectura posterior, marcada como tal.** El requisito de monotonía resultó demasiado estricto frente al ruido de muestreo. La columna «acreditada desde» (el menor N desde el cual la estadística queda acreditada en todos los niveles más finos) no reemplaza la clasificación registrada; la describe. Con ella:
- En N=192 están acreditadas todas las estadísticas de clase.
- En N=128 están acreditadas todas salvo tres: la mediana de la tasa neta d log|b|/dG, la fracción con s_V < 0 y la fracción con tasa neta positiva. Las tres dependen del término viscoso de segundo orden o de la diferencia entre términos grandes.
- En N=64 fallan además ρ⊥ global y en q > 2, 𝒟⊥, s_P, s_V y P(ρ⊥ < 0.05) en [0, 1).

## 6. Qué queda acreditado como contenido del plano [E]

1. **Las conclusiones de clase de la rama se sostienen.** La presión sostiene el giro en la mayoría de los estados intensos (fracción s_P > 0 ≈ 0.86, robusta desde N=64). La viscosidad lo quita (s_V < 0 ≈ 0.90, acreditada desde N=192). Las medianas de primer orden y las probabilidades de bajo giro por rango de vorticidad están acreditadas desde kmax·η ≈ 2. Λ⊥, 𝒟⊥ y cuatro de los cinco rangos de probabilidad cumplen además el criterio prerregistrado completo; ρ⊥ en q > 3 y cos φ están acreditadas en todos los niveles, pero sin monotonía.
2. **El signo de la tasa neta no se puede afirmar.** En N=256 su IC95 es [−1.16, +0.52]. Es la misma cautela que ya tenía la rama, ahora cuantificada.
3. **La referencia N=192 vale para el primer orden y para la presión, no para el término viscoso de segundo orden puntual.** 𝒱_c y 𝒴 todavía cambian 9 % y 6 % entre N=192 y N=256. Cualquier afirmación sobre esos términos estado por estado necesita kmax·η > 3, y no está demostrado que N=256 baste.
4. **La clasificación de estados individuales no es contenido del plano a estas resoluciones.** Entre N=192 y N=256 cambia la pertenencia de cerca de un cuarto de los estados de bajo giro (Jaccard 0.77). Lo acreditable son fracciones y medianas de la población, no qué punto concreto está en el canal.

En el lenguaje de O17: las distinciones de la población (cuántos estados de bajo giro, con qué balance de términos) se sostienen al refinar. Qué estado concreto pertenece al canal depende de la descripción, como los microestados.

## 7. Límites

- Un solo instante y un solo Reynolds (Re_λ ≈ 48). La incertidumbre es espacial, no de ensamble temporal.
- N=256 es la referencia y su propia convergencia no se prueba. Para 𝒱_c y 𝒴 lo más probable es que todavía se muevan.
- 400 réplicas de bootstrap: los extremos de los IC95 tienen error de Monte Carlo del orden de una o dos milésimas en las fracciones.
- Nada de esto toca la regularidad global. Describe qué diagnósticos de esta rama son medidas del flujo y cuáles de su discretización.

## 8. Siguiente paso [A]

- Repetir la escalera desde dos o tres instantes más, para tener incertidumbre temporal.
- Agregar N=384 solo para 𝒱_c y 𝒴 en la malla común.
- En el próximo prerregistro, usar «acreditada en todos los niveles desde N» como criterio principal en lugar de la monotonía estricta.

Código: `experiments/escalera_ns_o17f.py` (DNS y presupuesto, reutiliza los scripts de la rama sin modificarlos) y `experiments/analisis_o17f.py`. Resultados: `results/RESULTADOS_O17F.json` y `.txt`, `DIAGNOSTICOS_NIVELES.json`, `PROGRESO_CORRIDA.log`. Los estados de la DNS (≈ 0.5 GB) no se incluyen. El protocolo los regenera de forma determinista en unas dos horas con dos núcleos.
