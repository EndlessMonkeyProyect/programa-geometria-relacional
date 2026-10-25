# E-MIRROR v7 — El cubo como longitud de onda

**Programa de Geometría Relacional, 18 de octubre de 2026.** Laboratorio computacional reproducible e independiente, no integrado ni aprobado como teorema del programa. No se modifican los originales v3.4.1 ni E-MIRROR v1–v6.

## Pregunta

Si el cubo representa una **longitud de onda de la luz** (no simplemente una distancia en metros), ¿qué sucede al mover una pared de una segunda cavidad que comunica con la primera por un vidrio parcialmente reflectante? ¿En qué proporciones aparecen modos de campo compartidos? ¿Qué diferencia introducen los índices pares e impares de las ondas estacionarias?

## Modelo físico mínimo (exacto en 1D bajo los supuestos adoptados)

- Se estudia una componente transversal del campo eléctrico en una **geometría unidimensional**: no se resuelven seis caras de un cubo 3D ni modos TE/TM transversales generales.
- Distancias normalizadas por la longitud de onda de referencia `λ₀`; cavidad A de longitud `A=λ₀` y cavidad B de longitud variable `B`.
- Espejos extremos como **conductores perfectos (PEC)**: componente tangencial de E nula en los extremos.
- Divisor como **hoja reactiva ideal, sin pérdidas**, de respuesta conservativa; campo E continuo y salto de derivada proporcional a E: `E'(A+)−E'(A−)=g E(A)`.
- Para `k₀=2π/λ₀`, la hoja tiene reflectividad energética `R=g²/(4k₀²+g²)` (a frecuencia `k₀`); la reflectividad a otras frecuencias cambia. No se ha modelado vidrio real con espesor, índice, dispersión o absorción.
- Modos normales: **sin excitación ni pérdidas**. La señal de una fuente puntual utiliza un número de onda complejo fenomenológico `k=k₀(1+0.003 i)` para regularizar los picos. No es una calibración de potencia, cámara ni pérdida física exacta.

### Condición exacta para modos de campo

Partiendo de `E_A(x)=A₀ sin(kx)` y `E_B(x)=B₀ sin(k(A+B−x))`, las condiciones en el divisor producen:

`D(k,B,g) = k sin[k(A+B)] + g sin(kA) sin(kB) = 0`.

**Es una condición espectral de este modelo electromagnético 1D**, no una nueva ley física. Se verifica que reproduce el caso sin divisor (`g=0`) y modos compartidos cuando los nodos de ambas cavidades coinciden.

## Hallazgos obtenidos

### 1. Modo protegido por nodo compartido en B=λ₀/2

Con `A=λ₀`, `B=λ₀/2` y `k=k₀`, ambos lados tienen un nodo en el vidrio (`E(A)=0`). Por tanto, `D(k₀, B, g)=0` **para cualquier g finito**, y las 4 reflectividades probadas —0, 25, 50 y 90 %— conservan `q=k/k₀=1` como frecuencia propia (precisión numérica mejor que `4×10⁻¹⁴` en q). El perfil espacial es independiente de g, normalizado a la misma energía. En este modo, la energía espacial integrada se distribuye como **2/3 en A y 1/3 en B**.

> **Cuidado:** no basta para demostrar transporte de energía a través del vidrio. En el modo estacionario ideal, el campo es cero en el separador y el flujo promedio de energía a través de él también es cero. Tampoco prueba que el modo sea único ni que dos fuentes se identifiquen sin ambigüedad. Cuando `g→∞`, las cavidades se desacoplan y pueden degenerar en frecuencia.

### 2. La mitad es especial para una frecuencia elegida; otras fracciones también son importantes

Los cocientes racionales permiten nodos comunes a frecuencias correspondientes a índices longitudinales enteros:

| B/A | Índices `(n_A,n_B)` | Frecuencia `q=k/k₀` | Signo relativo de la amplitud B/A |
| --- | --- | ---: | ---: |
| 1/2 | (2,1) | 1 | +1 |
| 2/3 | (3,2) | 3/2 | +1 |
| 3/4 | (4,3) | 2 | +1 |
| 3/5 | (5,3) | 5/2 | −1 |

Para la **misma** longitud de onda de referencia, el modo protegido dentro del intervalo `B∈(0,λ₀)` aparece en `B=λ₀/2` (y en otros modos sólo cuando se cambia la frecuencia). No es una singularidad absoluta del espacio. El cambio al pasar por la mitad es continuo en el espectro, no un salto ontológico demostrado.

### 3. Paridad y cambio de signo

En modo de nodo común, la continuidad de la pendiente impone `B₀/A₀=−(−1)^(n_A−n_B)`. Por ello, algunas familias pares/impares conservan signo relativo y otras lo invierten. **Esta paridad se deduce de la onda y de las condiciones de borde**. No autoriza concluir que únicamente los pares transporten imágenes ni que las estructuras sólo nazcan de los impares.

### 4. Excitación a frecuencia fija

Se puso la fuente en `x_s=0.23 λ₀` dentro de A y se observó `E` en el punto medio de B. Con amortiguación fenomenológica fija, la intensidad de la señal a `q=1` muestra un pico estrecho al acercarse `B=λ₀/2`, conservado para los cuatro valores de R. Es señal sintética, en unidades arbitrarias. La altura y anchura dependen del punto de excitación, pérdidas, ancho de banda y cómo se modela el divisor. Se evita inferir un umbral universal de observabilidad.

## Estado epistémico y siguiente falsador

**[DERIVADO DEL MODELO]** Ecuación espectral, nodo común, distribución espacial, paridad, desplazamiento continuo de las ramas de frecuencia.

**[ILUSTRACIÓN/INTERPRETACIÓN]** Una unidad espacial de medida puede asociarse al período de campo; familias de cavidades distintas comparten un modo si sus nodos y fases son compatibles.

**[NO DERIVADO]** Que el cubo ontológico sea literalmente la longitud de onda, que la reflexión produzca cardinalidad, que el nodo común demuestre una singularidad de identidad, que el hallazgo resuelva P vs NP, Yang–Mills u otros problemas físicos.

**Próximo control difícil:** conservar `λ₀` como referencia y extender el problema a una celda 2D/3D con polarización, vidrio dieléctrico de espesor finito, excitación desde un solo lado, tiempos de estabilización y flujo de Poynting. Hay que distinguir un modo estacionario compartido de una **transferencia efectivamente observable de energía e información**.

## Archivos y reproducción

- `onda_cavidades_v7.py` — cálculo espectral, función de Green del sensor, CSV y seis figuras.
- `test_onda_cavidades_v7.py` — 21 pruebas y controles de consistencia.
- `resultados_v7.json` — parámetros y valores calculados.
- `barrido_campo_v7.csv` — variación de intensidad a frecuencia fija.
- `modos_v7.csv` — ramas espectrales versus pared móvil.
- `01_modos_pared_movil.png`, `02_senal_frecuencia_fija.png`, `03_modo_nodo_comun.png`, `04_nodo_y_respuesta_vidrio.png`, `05_vidrio_y_frecuencia.png`, `06_paridad_de_modos_comunes.png` — resultados gráficos.
- `HALLAZGO.es.md` — narrativa, ontología, matemática, límites.
- `PENDIENTE_LABORATORIO_ESFERAS.es.md` — hipótesis pendiente ya registrada en v1–v6.
- `PRUEBAS.txt`, `MANIFIESTO_SHA256.json` — auditoría reproducible.

Ejecutar (Python 3.10+, `numpy`, `scipy`, `matplotlib`):

```bash
python onda_cavidades_v7.py
python -m unittest -v test_onda_cavidades_v7.py
```
