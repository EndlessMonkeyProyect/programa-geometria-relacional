# Registro epistemológico y cadena de pruebas — O93

## Ya está matemáticamente probado dentro de contratos explícitos

**T1. Paridad de circuito:** `Q_G s=0` tiene un grado de libertad en grafos conectados bipartitos y cero en conectados con ciclos impares (O72). No es una ley general de fluidos.

**T2. Holonomía cinemática:** cuatro enlaces ideales `a_i ω_i + b_i ω_{i+1}=0` admiten solución no nula si y solo si `H=∏a_i/b_i=1`. Una elección de radios consecutivos telescopa. Los brazos reales pueden no obedecer esos contratos (O74).

**T3. Fases toroidales:** Bézout y matriz unimodular reconstruyen las dos fases primarias; mapas no invertibles necesitan etiqueta de rama. No se deriva un bloqueo físico de las fases en NS (O68/O88).

**T4. Normalización doble O92:** `û_k=M z_k` reconstruye el campo si se retienen *todos* los coeficientes complejos vectoriales y la magnitud del sistema. Las ecuaciones de evolución normalizadas se derivan de la PDE original, no son una reducción finita universal.

**T5. Puente O92 ↔ O86:** bajo solución NS suave, periódica, solenoidal, sin fuerza y con escala definida: `W=M²D`, `B=M²D₂`, `P=M³ T`. La última identidad es demostrable por balance de vorticidad y la derivada de `M²D`; es un cambio exacto de representación.

**T6. Criterio condicional:** si el exceso positivo acumulado `∫[M T−νD₂]₊/D dt` es finito hasta un tiempo finito, la enstrofía se acota y aplica continuación estándar. Se demuestra la **implicación**, no la premisa para todo campo suave 3D.

**T7. Contabilidad O84:** bajo el presupuesto local importado de O82 y los supuestos bootstrap y de integrabilidad, las referencias actualizadas permiten no sobrecontar el mismo resto. Reproducimos la prueba por factor integrante y telescopaje.

## Experimentos reproducidos en este paquete

**E1 y E2:** matrices y productos algebraicos exactos.  
**E3:** sumas finitas de Fourier en aritmética simbólica.  
**E4:** solución analítica de NS (cizalla) con cálculos a 51 tiempos.  
**E5:** certificado O84 y margen intervalar verificados con 65 dígitos.  
**E6:** integración temporal aproximada 3D Galerkin con comprobaciones de resolución/paso temporal.

## Falsadores ya relevantes que deben mantenerse en la Imagen Total

- O75: incompresibilidad no conserva toda holonomía material de cuatro enlaces.
- O76: cuatro nodos locales no capturan necesariamente la contribución de presión no local.
- O86: la misma distribución de magnitudes, enstrofía, palinstrofía y radio espectral puede tener estiramiento de signo opuesto según fase.
- O85: el mero refinamiento de escala y margen por bloque no impiden una suma formal de costos divergente; el ejemplo no construye una solución NS singular.
- O88/O90: pérdida de bloqueo de fase no implica pérdida de suavidad ni destrucción de la topología material en el intervalo de existencia.

## Hipótesis centrales que no han sido demostradas

- Que el sistema físico de NS se origine universalmente de cuatro cápsulas activas de tipo engranaje.
- Que seleccionar una normalización de fase o cardinal garantice compensación de estiramiento en todos los datos.
- Que un algoritmo finito o una compresión relacional suficiente cierre exactamente todas las interacciones y la presión para cualquier dato 3D.
- Que el criterio positivo acumulado de O93 se satisfaga universalmente.

## Cómo atacar la conexión sin repetir trabajo

Definir desde el campo inicial un operador `C_0` de referencia y una transición causal `C_{j+1}=F(C_j,defecto_j)` que conserve fase/orientación y las interacciones pertinentes. Probar una cota de defecto y de concentración física acumulada independiente del horizonte de discretización. Aplicar pruebas adversariales de O76/O79/O85/O86 antes de declarar una ley universal.
