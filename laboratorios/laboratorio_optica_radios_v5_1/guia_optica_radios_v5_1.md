# Laboratorio v5.1 — Radios, pared móvil y aparición de nuevas referencias

**Endless Monkey Project** · *Relational Geometry Program*
Le Matt Ansatz Di Ego · 7 de noviembre de 2026

*English version: [guide_optics_radii_v5_1.md](guide_optics_radii_v5_1.md)*

## La pregunta

Desde una referencia dada, una estructura extensa puede verse como una sola mancha. Esa reducción depende de la distancia, la escala de la estructura, la apertura y la longitud de onda del observador; la estructura interna sigue existiendo. El espectro conserva distinciones de frecuencia que la imagen espacial ya no separa.

El laboratorio mide tres cosas:

1. cuándo una distinción desaparece o reaparece al mover la referencia;
2. cuándo una observación de fase con un período nuevo agrega distinciones a las heredadas;
3. cuántas distinciones obtiene el observador y cuánto le cuestan (la economía).

En A, B y C el observador ve clases de configuraciones equivalentes respecto de los observables declarados. Mover la referencia divide o junta esas clases.

| Parte | Qué se mueve | Qué se ve igual | ¿Se pierde información? |
| --- | --- | --- | --- |
| A — espejos | La pared L | Puntos de una misma órbita | La escena se conserva; la firma da la órbita, no el punto |
| B — resolución | La distancia D | Fuentes separadas menos que el umbral angular | Sí; la escena lejana es irreversible (E) |
| C — fase | La colección de longitudes de onda | Posiciones que difieren en un múltiplo de H | No dentro del período; ambigua fuera de él |

## A — Espejos paralelos

- s₀(x) = −x y s_L(x) = 2L − x son involuciones; s_L(s₀(x)) = x + 2L.
- La firma de órbita F_L(x) = L − |(x mod 2L) − L| lleva cada punto a su representante en [0, L] dentro de la órbita {±x + 2kL}. El código verifica esa invariancia para k = −3 … 3.
- Con L = 1, los puntos 0,25 y 1,75 tienen firma 0,25: misma órbita. Con L = 2 sus firmas son 0,25 y 1,75: órbitas distintas.

Mover la pared cambia la partición en órbitas.

## B — Radios, distancia y resolución

**Escena.** Cinco fuentes en una sección perpendicular a la línea de visión, en −R, −R+s, 0, R−s y R, con R = 5×10⁸ m y s = 10⁷ m. Bandas 450, 450, 550, 650 y 650 nm; pesos 1,0; 1,2; 2,0; 1,3 y 1,0. Apertura de radio r₀ = 0,25 m. Distancia D(t) = 10¹⁵ − 2×10⁶·t m (|v|/c ≈ 0,0067, acercamiento).

**Umbral por banda** (Rayleigh, apertura circular, Doppler relativista de un solo trayecto, β = v/c < 0):

```
θ_R(λ) = 1,22 · λ_obs / (2 r₀),   λ_obs = λ · √((1+β)/(1−β))
```

Valores durante el acercamiento: 1,091×10⁻⁶ rad (450 nm), 1,333×10⁻⁶ rad (550 nm) y 1,575×10⁻⁶ rad (650 nm).

**Componentes.** Dos fuentes vecinas quedan en componentes distintas cuando su separación angular alcanza el umbral de la mayor longitud de onda del par (la mancha más ancha). Es un modelo discreto de resolución, sin ruido, interferencia ni umbral de sensibilidad.

**Extensión.** Tamaño angular total dividido entre el umbral a 550 nm. Menor que 1: imagen puntual; mayor que 1: imagen extendida.

| t (s) | D (m) | Componentes | Extensión | Imagen |
| ---: | ---: | ---: | ---: | --- |
| 0 | 1×10¹⁵ | 1 | 0,75 | puntual |
| 2×10⁸ | 6×10¹⁴ | 1 | 1,25 | extendida |
| 3,3×10⁸ | 3,4×10¹⁴ | 2 | 2,21 | extendida |
| 4×10⁸ | 2×10¹⁴ | 3 | 3,75 | extendida |
| 4,9×10⁸ | 2×10¹³ | 3 | 37,5 | extendida |
| 4,96×10⁸ | 8×10¹² | 4 | 93,8 | extendida |
| 4,99×10⁸ | 2×10¹² | 5 | 375 | extendida |

**Transiciones exactas.** Cada hueco gᵢ entre vecinas se abre a la distancia Dᵢ = gᵢ / θᵢ. El código comprueba el salto evaluando el conteo en Dᵢ·(1 ± 10⁻⁶).

| Transición | Hueco | Banda del umbral | Dᵢ (m) | Al aumentar D |
| --- | --- | --- | ---: | --- |
| D₁ | par rojo (R−s, R), 10⁷ m | 650 nm | 6,35×10¹² | 5 → 4 |
| D₂ | par azul (−R, −R+s), 10⁷ m | 450 nm | 9,17×10¹² | 4 → 3 |
| D₃ | centro – (R−s), 4,9×10⁸ m | 650 nm | 3,11×10¹⁴ | 3 → 2 |
| D₄ | (−R+s) – centro, 4,9×10⁸ m | 550 nm | 3,68×10¹⁴ | 2 → 1 |

Resultados:

- La escalera completa es 5 → 4 → 3 → 2 → 1 y es asimétrica: el lado azul se separa antes que el rojo, porque su umbral es menor.
- Una componente y un punto son cosas distintas: en D = 6×10¹⁴ m hay una sola componente y la imagen mide 1,25 veces el umbral.
- Movimiento invertido: con v = +2×10⁶ m/s (alejamiento) el umbral crece por el Doppler y cada Dᵢ se multiplica por 0,9867. La secuencia recorrida es 5-4-3-3-2-1-1, la inversa del acercamiento.
- Espectro del receptor ideal: pesos 2,2 (450 nm), 2,0 (550 nm) y 2,3 (650 nm). Las tres bandas se distinguen en todos los instantes y no dependen de las posiciones.
- El flujo total sigue la ley 1/D².

**Contraste con una imagen física idealizada** (`contraste_airy.py`): suma incoherente de patrones de Airy, uno por fuente con su longitud de onda, receptor pancromático sin ruido; se cuentan los máximos locales. Los tramos de la imagen Airy salen de un recorrido de 3000 distancias, con una resolución cercana al 0,2 %.

| Componentes | Criterio del laboratorio | Imagen Airy |
| ---: | --- | --- |
| 5 | D < 6,35×10¹² m | D < 7,28×10¹² m |
| 4 | 6,35×10¹² – 9,17×10¹² m | 7,28×10¹² – 1,07×10¹³ m |
| 3 | 9,17×10¹² – 3,11×10¹⁴ m | 1,07×10¹³ – 4,08×10¹⁴ m |
| 2 | 3,11×10¹⁴ – 3,68×10¹⁴ m | 4,08×10¹⁴ – 6,02×10¹⁴ m |
| 1 | D > 3,68×10¹⁴ m | D > 6,02×10¹⁴ m |

La imagen Airy reproduce la misma escalera en el mismo orden. Cada transición ocurre a una distancia entre 1,1 y 1,6 veces mayor, porque el valle entre dos máximos aparece antes de la separación de Rayleigh. En D = 6×10¹⁴ m la imagen Airy está en el borde: dos máximos con un valle del 0,01 % y un ancho 2,35 veces el de una fuente puntual.

## C — Fase de reflexión: períodos y referentes nuevos

En un interferómetro ideal, la luz de longitud de onda λ que va hasta el espejo a distancia D y vuelve tiene fase

```
φ(D) = 4π·D / λ   (mód 2π)
```

La fase identifica posiciones separadas por λ/2: φ(D) = φ(D + λ/2).

Con la unidad u = 100 nm y períodos p = 3, 5, 7 y 9 (λ = 600, 1000, 1400 y 1800 nm; de 1000 nm en adelante es infrarrojo cercano), dos posiciones enteras D/u tienen la misma colección de fases exactamente cuando su diferencia es múltiplo de H = mcm(P). Una observación nueva de período m da el período combinado H′ = mcm(H, m) y divide cada clase heredada en H′/H = m / mcd(H, m) clases. Aparece un referente nuevo exactamente cuando m no divide a H.

Esta construcción es la idealización entera del método de las fracciones excedentes (o exactas) de la interferometría multilongitud de onda, que se usa en la calibración de bloques patrón desde la década de 1890 (ver Referencias). Supone fase coherente sin ruido, períodos conmensurables y posiciones enteras.

| Herencia (H) | Nuevo m | H′ | Clases por clase heredada | Bits que cuesta | Bits que aporta | Eficiencia |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| {3} (3) | 5 | 15 | 5 | 2,32 | 2,32 | 100 % |
| {3,5} (15) | 9 | 45 | 3 | 3,17 | 1,58 | 50 % |
| {3,5,9} (45) | 7 | 315 | 7 | 2,81 | 2,81 | 100 % |
| {3,5,7} (105) | 9 | 315 | 3 | 3,17 | 1,58 | 50 % |
| {3,5,7,9} (315) | 9 | 315 | 1 | 3,17 | 0 | 0 % |
| {3,5} (15) | 5 | 15 | 1 | 2,32 | 0 | 0 % |

El caso del 9: 15 contiene el factor 3 pero no 3², así que la fase de período 9 separa posiciones que antes eran equivalentes. Lo que cambia es la colección de observables; la incertidumbre de esta sección es la ambigüedad de fase sobre la posición D.

## D — Economía

La economía se mide como el número de clases que distingue el observador (en bits, log₂ del número de clases) frente al número de estados que existen.

**B ahorra porque olvida.** El número de componentes es una función en escalones de la distancia:

```
N(D) = 1 + #{ i : gᵢ ≥ θ_R(λᵢ) · D }
```

Cada distinción aparece a su propia distancia, y el orden de aparición lo fija la jerarquía de huecos de la estructura: es un dendrograma de enlace simple (el código de barras H₀ de la homología persistente). Desde lejos la descripción es mínima (una componente, su extensión y tres bandas), y la sección E muestra que esa descripción corresponde a más de una estructura. Producir la imagen requiere sumar las n fuentes: el ahorro está en lo que se distingue, y el costo de cómputo se mantiene.

**C ahorra porque reutiliza.** Una observación de período m cuesta log₂ m bits, los que ocupa su resultado, y aporta log₂(m / mcd(H, m)) bits (tabla de C). Rinde completa cuando trae una potencia de primo nueva. Los residuos de {3, 5, 7, 9} ocupan 9,88 bits y distinguen 315 clases (8,30 bits): el residuo módulo 3 es redundante porque el módulo 9 lo contiene. La base mínima son las potencias máximas de primos de H: {5, 7, 9}.

**El límite.** Ubicar una posición entre 630 requiere log₂ 630 = 9,30 bits, y ninguna representación baja de esa cota.

| Períodos | Firmas en [0, 630) | Posiciones por firma | Bits que distingue | Bits guardados | Bits redundantes |
| --- | ---: | ---: | ---: | ---: | ---: |
| {3, 5} | 15 | 42 | 3,91 | 3,91 | 0 |
| {3, 5, 9} | 45 | 14 | 5,49 | 7,08 | 1,58 |
| {5, 7, 9} | 315 | 2 | 8,30 | 8,30 | 0 |
| {3, 5, 7, 9} | 315 | 2 | 8,30 | 9,88 | 1,58 |

- La firma modular es un cambio de coordenadas: el teorema chino del resto es una correspondencia uno a uno.
- La economía real es incremental. Con {3, 5, 9} (H = 45), las consultas x mod 3, 9, 15 y 45 se responden con la firma heredada; x mod 2 y x mod 7 requieren una observación nueva. En general, x mod m se responde con lo heredado exactamente cuando m divide a H.
- Agregar una observación cuesta solo su residuo.

**Qué miden los bits.** Cuentan clases distinguibles y redundancia de la representación; el costo físico de medir y el tiempo de cálculo se evalúan aparte. Las fórmulas ópticas y los umbrales son aproximaciones del modelo idealizado.

## E — Reapertura y límite de la herencia

Dos escenas con las mismas bandas y los mismos pesos: A, con cinco posiciones distintas, y B = (−R, −R, 0, R, R), con tres posiciones distintas (fuentes coincidentes).

- A 10¹⁵ m ambas tienen una componente, extensión 0,75 y el mismo espectro.
- A 2×10¹² m, A tiene cinco componentes y B tres.
- En una imagen ideal sin ruido, sus centroides ponderados a 10¹⁵ m difieren en 1,54×10⁻¹⁰ rad, es decir 1,15×10⁻⁴ veces el umbral a 550 nm.

El observable lejano (conteo de componentes, extensión y espectro) es el mismo para dos distribuciones distintas: esa señal determina la clase, y la distribución de fuentes queda indeterminada. Recuperarla requiere cambiar la observación (acercarse, otra banda, otro observable) o haber conservado más relaciones.

## Verificado en esta implementación

Cada punto corresponde a aserciones del código y a valores calculados del CSV.

1. **A:** involuciones, composición igual a la traslación 2L, invariancia de la firma en toda la órbita y cambio de la partición al mover L.
2. **B:** escalera 5 → 4 → 3 → 2 → 1 con cuatro transiciones exactas Dᵢ = gᵢ/θᵢ; una componente extendida en D = 6×10¹⁴ m; inversión con alejamiento real (v > 0); tres bandas espectrales en todos los instantes.
3. **B, contraste opcional:** la imagen Airy da la misma escalera en el mismo orden, con transiciones a distancias entre 1,1 y 1,6 veces mayores.
4. **C:** periodicidad λ/2, criterio del mcm, referente nuevo exactamente cuando m no divide a H, y bits que cuesta y aporta cada observación.
5. **D:** clases de tamaño exacto en [0, 630); base mínima {5, 7, 9}; redundancia del residuo módulo 3; consultas x mod m respondidas con lo heredado exactamente cuando m divide a H.
6. **E:** el mismo observable lejano para dos distribuciones distintas, y la diferencia de centroides calculada.

## Abierto

- Demostrar una economía computacional mayor que la de los métodos de álgebra, programación dinámica, teorema chino del resto, compresión e inferencia existentes.
- Encontrar una familia de problemas en la que la estructura heredada permita saltarse trabajo y no solo reordenarlo; es ahí donde entra la pregunta por SAT.
- Demostrar un vínculo equivalente con los algoritmos de OpenAI/Anthropic.
- Trasladar esta realización idealizada a observaciones físicas de alta complejidad.
- Incorporar ruido, coherencia finita, retardo temporal y relatividad completa en B; períodos no conmensurables, distancias continuas y fase con ruido en C.

## Reproducir

```bash
python3 laboratorio_optica_radios_v5_1.py   # solo biblioteca estándar, menos de 1 s
python3 contraste_airy.py                   # opcional; numpy y scipy, unos 5–10 s
```

El primero verifica las secciones A–E y genera `resultados_optica_v5_1.csv`. El segundo imprime las tablas del contraste Airy de la sección B.

Este laboratorio complementa el protocolo v4, «Convocatoria abierta de revisión: reflexión, herencia y economía computacional», que define la singularidad de normalización y mide la economía de las interfaces; ese protocolo se publica por separado.

## Referencias

- M. Wengierow, L. Salbut, Z. Ramotowski, R. Szumski y K. Szykiedans, [«Measurement system based on multi-wavelength interferometry for long gauge block calibration»](https://journals.pan.pl//Content/90167/PDF/Journal10178-VolumeXX%20Issue3_14.pdf), Academia Polaca de Ciencias, vol. XX, núm. 3, 2013.
- [«Method of excess fractions with application to absolute distance metrology: wavelength selection and the effects of common error sources»](https://doi.org/10.1364/AO.51.006471), *Applied Optics* 51, 6471 (2012).
- [«Phase-step calibration extends 19th century standard into 21st»](https://www.laserfocusworld.com/test-measurement/test-measurement/article/16549948/phasestep-calibration-extends-19th-century-standard-into-21st), *Laser Focus World*.
