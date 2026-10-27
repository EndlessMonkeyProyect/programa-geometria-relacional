# PGR — PR-06: Masa positiva por cierre de ventanas — el flujo de correlación por el borde

**Fecha:** 2026-10-27  
**Estado:** teorema con **un lema citado** (desigualdad de Simon–Lieb), que certifica **masa positiva** —decaimiento exponencial de correlaciones— en Ising 2D para β < 0,4067, es decir, el 92 % del camino a β_c. La masa queda explícita. Supera la pared de PR-05 y, en el límite de ventanas grandes, llega exactamente a β_c. **No es Yang–Mills.**  
**Procedencia:** PR-05 §7.4, siguiente paso: dejar de controlar el peor entorno y juzgar la ventana en su estado típico.

## 1. Qué se buscaba

PR-05 exigía que cada ventana resistiera **cualquier** entorno, y por eso se frenaba en 0,3322. Aquí la ventana se juzga **en su propio estado, sin entorno** (frontera libre). La pregunta es: de la diferencia que hay en el centro, ¿cuánta alcanza el borde y sale?

## 2. Vocabulario

| programa | objeto preciso |
|---|---|
| **ventana** `S_n` | caja `n×n` centrada en el origen, con `n` impar; su radio en el sentido del máximo es `R = (n+1)/2` hasta el primer sitio de afuera |
| **estado propio** de la ventana | medida de Ising en `S_n` con frontera libre, sin ningún entorno |
| **flujo por el borde** `φ_β(S_n)` | `tanh β · Σ_(x ∈ borde) (aristas que salen en x) · ⟨σ_0 σ_x⟩_(S_n)` |
| **cierre** | `φ < 1`: de la diferencia del centro sale por el borde menos que uno |
| **masa** | tasa de decaimiento exponencial de `⟨σ_0 σ_z⟩`, la cantidad que importa para Yang–Mills (PR-03 §5.6) |

[Lectura] Cada ventana atravesada multiplica la diferencia por `φ`. Si cada cierre retiene más de lo que deja salir, la diferencia se apaga a una tasa fija: eso es la masa.

## 3. Teorema

**Contrato.** Ising 2D ferromagnético de vecinos más cercanos, `β ≥ 0`, en el límite de volumen infinito tomado con frontera libre.

**Teorema.** Si `φ_β(S_n) < 1`, entonces para todo `z`:

    ⟨σ_0 σ_z⟩ ≤ φ_β(S_n)^⌊‖z‖∞ / R⌋,   por lo tanto   masa ≥ −ln φ_β(S_n) / R > 0.

Lo mismo vale para todo `β' ≤ β`.

## 4. Demostración

**Lema (Simon 1980; Lieb 1980), citado.** Sean `S ∋ 0` contenido en `Λ` y `z ∈ Λ∖S`. Entonces

    ⟨σ_0 σ_z⟩_Λ ≤ Σ_(x∈S, y∈Λ∖S, x∼y) tanh β · ⟨σ_0 σ_x⟩_S · ⟨σ_y σ_z⟩_Λ.

No se demuestra aquí; su prueba usa la representación por corrientes aleatorias. El script lo comprueba numéricamente en volúmenes 3×6 y 4×5, con `S` de 3×3 y cuatro valores de β, incluido uno mayor que β_c.

**Paso 1.** Todas las correlaciones son ≥ 0 (primera desigualdad de Griffiths). Entonces el lado derecho del lema es a lo sumo `φ_β(S) · máx ⟨σ_y σ_z⟩_Λ`, tomando el máximo sobre los `y` con `‖y‖∞ = R`.

**Paso 2 (inducción).** Se afirma que `⟨σ_u σ_z⟩ ≤ φ^⌊‖z−u‖∞/R⌋`.
- Si `‖z−u‖∞ < R`, el exponente es 0 y la cota es trivial.
- Si no, se aplica el Paso 1 a la ventana trasladada a `u`. Cada `y` cumple `‖z−y‖∞ ≥ ‖z−u‖∞ − R`, así que el exponente baja a lo sumo en uno.

Esto exige que las ventanas trasladadas queden dentro de `Λ`, lo que se cumple tomando `Λ` grande y pasando al límite.

**Paso 3 (monotonía).** `⟨σ_0 σ_x⟩_S` crece con β (segunda desigualdad de Griffiths), y también `tanh β`. Por lo tanto `φ` crece con β, y si `φ_β < 1` también `φ_β' < 1` para todo `β' ≤ β`. Esto además justifica la bisección. ∎

## 5. Cálculo

- **Método:** `φ` se calcula **exactamente** en cajas de hasta 21×21, con 2²¹ estados por columna. Se usa una matriz de transferencia factorizada (`T = ⊗ t`), cuyo coste es `n·2ⁿ` por columna.
- **Validación:** contra enumeración directa en 3×3 y contra una transferencia densa independiente en 5×5; el error es ≤ 10⁻¹⁶. Para `n = 1` se recupera `φ = 4 tanh β`, la condición de Dobrushin de PR-05.
- **Comprobaciones en cada caja:** en el umbral informado se verifica `φ < 1`, de modo que cada valor es un β certificado. En β_c se verifica `φ ≥ 1`, como exige el resultado de Duminil-Copin–Tassion.

## 6. Resultados

**Umbrales** (mayor β certificado con `φ_β(S_n) < 1`; las cifras se truncan hacia abajo, nunca se redondean hacia arriba):

| n | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 | 21 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| β_n | 0,2554 | 0,3241 | 0,3526 | 0,3688 | 0,3795 | 0,3871 | 0,3929 | 0,3974 | 0,4011 | 0,4041 | 0,4067 |
| % de β_c | 58 | 73 | 80 | 83 | 86 | 87 | 89 | 90 | 91 | 91 | 92 |

Lo mejor de PR-05, que controlaba el peor entorno con ventanas de hasta 4×4, era 0,3322. Este criterio lo supera **desde la caja 5×5**.

**Masa certificada frente a masa exacta** (Onsager, a lo largo del eje: `2(β* − β)`, con `β* = −½ ln tanh β`):

| β | masa certificada (caja 21) | masa exacta | fracción |
|---:|---:|---:|---:|
| 0,25 | 0,776 | 0,907 | 85 % |
| 0,30 | 0,500 | 0,633 | 79 % |
| 0,35 | 0,252 | 0,390 | 64 % |
| 0,38 | 0,114 | 0,254 | 45 % |
| 0,40 | 0,028 | 0,168 | 16 % |

La masa certificada nunca supera la exacta, como debe.

## 7. Lo que esto dice

1. **Juzgar la ventana en su estado típico pasa la pared.** La caja 5×5 ya supera todo lo de PR-05, y la de 21×21 llega al 92 % de β_c. Duminil-Copin y Tassion (2016) probaron que este criterio es **exacto en el límite**: para todo `β < β_c` existe una caja finita que cierra. No hay pared antes de β_c.
2. **Certifica masa, no sólo brecha dinámica.** Es la cantidad que importa para Yang–Mills. El paso a la brecha de Glauber en 2D lo da Martinelli–Olivieri–Schonmann; se cita, no se reproduce.
3. **No es nuevo.** Las piezas son de Simon (1980) y Lieb (1980); la exactitud del criterio, de Duminil-Copin–Tassion (2016); la masa exacta, de Onsager. Se reproduce, no se descubre.
4. **Por qué funciona lo típico.** No es que lo típico baste en general. Es que el modelo tiene una desigualdad que **convierte lo típico en una cota para todo entorno a la vez**: la de Simon–Lieb, propia de Ising ferromagnético. Hasta donde sé, no se conoce un análogo de este tipo para Yang–Mills no abeliano. Ésa es la pieza que falta allí.
5. **Cerca de β_c hace falta una ventana del tamaño de la longitud de correlación.** La fracción de masa certificada cae del 85 % al 16 % al acercarse a β_c, y la distancia a β_c baja lentamente con `n`. En el continuo de Yang–Mills la longitud de correlación en unidades de red diverge. Una verificación finita, por buena que sea, no alcanza: hace falta un argumento que funcione igual en todas las escalas.
6. **[Lectura] El cierre del programa, hecho preciso.** "Lo que sale por el borde es menos que uno" es una forma exacta, y en este modelo exacta en el límite, de la noción de cierre del programa.

## 8. Falsadores y límites

- **F1.** El lema de Simon–Lieb está citado, no demostrado; aquí sólo se comprobó en volúmenes pequeños. Si fallara, el teorema caería.
- **F2.** El cálculo es en doble precisión. En los umbrales el margen `1 − φ` es pequeño pero muy superior al redondeo de 10⁻¹⁵. Las masas informadas tienen márgenes amplios.
- **F3.** El enunciado es en volumen infinito, o para cadenas de ventanas que no tocan el borde de `Λ`. Una ventana cortada por el borde no tiene por qué cumplir `φ < 1`.
- **F4.** Si una masa certificada superara la masa exacta de Onsager, el cálculo estaría mal. El script lo comprueba en cinco valores de β.

## 9. Ejecución

    python verificar.py            # completo, cajas hasta 21×21; ~3 min; escribe resultados.json
    python verificar.py --rapido   # cajas hasta 13×13; ~10 s; no escribe resultados

Dependencia: `numpy`.

**Alcance:** certifica masa positiva de Ising 2D para `β < 0,4067`, con un lema citado. No toca el punto crítico, ni el continuo, ni Yang–Mills.
