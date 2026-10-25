# E-MIRROR v8 — Economía de razones, nodos y criterio de acoplamiento

**18 de octubre de 2026.** Extensión **independiente y aditiva** de los laboratorios v1–v7, especialmente del v7 de cavidades de ondas. No modifica ni valida en su conjunto el Programa de Geometría Relacional 3.4.1.

## Pregunta

¿Permiten las razones trigonométricas describir con menos variables las relaciones entre dos cavidades con una longitud de onda de referencia, y distinguir una **solución extendida y acoplada** de dos cavidades **independientes** que coinciden en frecuencia?

## Narrativa → ontología → matemática

**Narrativa.** Dos cuartos de distinta profundidad comparten una pared parcialmente reflectante. Cada cuarto admite ondas estacionarias; no basta ver que sus frecuencias coinciden. Podemos intervenir excitando solo uno y preguntar si el otro responde. Si hay campo nulo en el vidrio, la pendiente del campo puede seguir viva y contener la relación compartida.

**Ontología [PROPUESTA, NO DERIVACIÓN].** Una relación puede permanecer estable cuando un valor local se anula, y una sola razón puede ocultar diferencias de signo o escala. La reflexión, como operación fundante de la unidad, es una hipótesis del programa, no un teorema demostrado por estas cavidades.

**Matemática [DERIVADO DEL MODELO].** El campo transversal escalar (modelo 1D de incidencia normal) satisface `E''+k² E = -F δ(x-xs)`, con `E(0)=E(A+B)=0`, continuidad de `E` en `A` y salto de derivada `E'(A+)-E'(A-)=g E(A)`. La hoja es reactiva y sin pérdidas; `g` real controla su reflectividad.

La condición espectral sin divisiones es

\[
D(k,A,B,g)=k\sin[k(A+B)]+g\sin(kA)\sin(kB)=0.
\]

Cuando `sin(kA) sin(kB) != 0`, es equivalente a la **carta por cotangentes**:

\[
\cot(kA)+\cot(kB)=-g/k.
\]

Cuando `cos(kA) cos(kB) != 0`, es equivalente a la **carta por tangentes**:

\[
\tan(kA)+\tan(kB)+(g/k)\tan(kA)\tan(kB)=0.
\]

La carta por tangentes **incluye** el nodo compartido `kA=2π`, `kB=π`, mientras que la de cotangentes tiene polos allí. Ninguna carta cubre todos los casos. La matriz de frontera los incluye sin dividir:

\[
M=\begin{pmatrix}
\sin(kA)&-\sin(kB)\\
k\cos(kA)+g\sin(kA)&k\cos(kB)
\end{pmatrix},\quad M\binom{C_A}{C_B}=0.
\]

`det(M)=D`. Para `A=λ₀=1`, `B=λ₀/2=0.5`, `k₀=2π` y cualquier `g` finito, `M` admite la solución `(C_A,C_B)=(1,1)`; `E(A)=0` pero `E'(A−)=E'(A+)=k₀ C_A ≠0`. Por tanto, un nodo **no significa ausencia de campo o relación**. La partición ideal de energía de ese modo es `2/3` en A y `1/3` en B.

El dato reducido `cot(θ)` o `tan(θ)` **no distingue** `θ` y `θ+π`: los signos de `sin` y `cos` se invierten simultáneamente pero sus cocientes permanecen iguales. También se pierde amplitud absoluta en una razón. Para conservar fase relativa es necesario un referente coherente, una rama de fase/signo o la pareja ordenada del campo y su pendiente con una calibración. Esto **no demuestra** un bit ontológico universal ni confunde inversión de fase con inversión espacial en espejo.

## Resultado de transferencia controlada

El modelo compara (i) una fuente que excita **solo A** y una lectura en B, frente a (ii) dos cavidades con pared perfectamente reflectante que por casualidad tienen la misma frecuencia. En (ii), por construcción de las ecuaciones, la transferencia lineal A→B es exactamente `0`. En (i), para `g` finito, puede ser no nula incluso cuando el separador coincide con un nodo propio. Una prueba independiente por diferencias finitas reproduce la transferencia analítica con menos del 2 % de error en la configuración ensayada.

Para el montaje A=1, B=0.5, frecuencia q=1, pérdida fenomenológica pequeña `Im(k)/Re(k)=0.003`, fuente `xs=0.23` y sensor a mitad de B:

| Reflectividad energética a q=1 | Respuesta |G_BA| (u. arbitrarias) |
|---|---:|
| 0 % | 5.583915 |
| 50 % | 5.583264 |
| 90 % | 5.579322 |
| 99 % | 5.538732 |
| Cavidades totalmente separadas | 0 |

Esta similitud de amplitudes cerca de la resonancia no significa que los cuatro casos transmitan la misma potencia fuera de resonancia ni que el límite `g→∞` sea intercambiable con una pérdida `Im(k)→0`. La función de transferencia, no la mera frecuencia compartida, permite distinguir acoplamiento **dentro del modelo**. La coherencia por excitaciones externas comunes también puede correlacionar cavidades no acopladas; por eso se requiere una intervención controlada.

Al mover la pared a frecuencia fija, la posición del máximo de transferencia cambia. En un barrido de B/A de 0.4 a 0.6, con R=90 %:

| Frecuencia relativa q | B/A donde hay máximo dentro del barrido |
|---:|---:|
| 0.96 | 0.455667 |
| 1.00 | 0.499667 |
| 1.04 | 0.465000 |

**La mitad no es un máximo universal**: es un cierre nodal especial a la frecuencia y las condiciones dadas.

## Lo que demuestra y lo que no

- **[DERIVADO]** Identidad exacta entre el determinante, la matriz de frontera y las cartas por razones en los dominios donde son definidas.
- **[DERIVADO]** En el nodo compartido, el campo transversal puede anularse mientras la pendiente continúa y enlaza ambos espacios.
- **[DERIVADO]** En cavidades acopladas existe una transferencia A→B que una pareja de cavidades aisladas no tiene al excitar solo A.
- **[COMPROBACIÓN NUMÉRICA]** 23 pruebas; comparación entre solución analítica y discretización de la ecuación diferencial.
- **[NO DEMOSTRADO]** Que el cociente trigonométrico sea por sí solo información física completa; que toda coincidencia modal represente una sola fuente; que la mitad sea condición ontológica universal; que un campo 1D explique por sí solo un cubo Maxwell 3D, Yang–Mills o P/NP.

## Reproducir

Entorno: Python 3, NumPy, SciPy, Matplotlib.

```bash
python razones_cavidades_v8.py
python -m unittest -v test_razones_cavidades_v8.py
```

Se generan `resultados_v8.json`, dos CSV y siete PNG. `PRUEBAS.txt` contiene la ejecución verificada. `MANIFIESTO_SHA256.json` contiene sumas de verificación.

## Propuesta v9

Sostener la economía por razones, pero pasar a un **campo vectorial electromagnético con condiciones de polarización** y separación de cavidades en 3D; medir transferencia causal, fase de referencia y zonas de invisibilidad, distinguiendo el efecto de desplazamiento de espejo y respuesta compleja del vidrio. Mantener aparte el laboratorio de esferas.
