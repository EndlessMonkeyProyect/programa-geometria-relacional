# Economía total de una representación

## 1. Las magnitudes [D]

La economía se registra como un vector, antes de decidir cualquier ponderación:

\[
\mathcal E=(N_{\mathrm{obs}},\;N_{\mathrm{int}},\;b_{\mathrm{ext}},\;T,\;M,\;P),
\]

con `N_obs` clases observables, `N_int` clases exigidas por las continuaciones, `b_ext` bits adicionales necesarios para recuperar la consulta nueva dentro de una firma antigua, `T` trabajo total, `M` memoria máxima y `P` error/precisión declarada (exacto o `ε`). No se suman sin especificar unidades y ponderaciones.

Para una entrada `F` y una secuencia de consultas `W=(w1,…,wm)`:

\[
T_A(F,W)=T_{\rm extraer}+T_{\rm construir}+T_{\rm verificar}
+\sum_{j=1}^{m}(T_{\rm actualizar,j}+T_{\rm resolver,j}+T_{\rm reconstruir,j}).
\]

El espacio máximo incluye el extractor, tablas, coeficientes, certificados y estado intermedio. Para dos implementaciones A y B, la ganancia relativa `1−T_A/T_B` solo se calcula si `T_B>0`, respuestas y precisión coinciden, y el problema de entrada es el mismo.

## 2. Umbral de reutilización [T]

Suponga una ruta directa de costo `D` por consulta y una ruta que paga `H` de preparación total más `R` por consulta, con `H≥0` y `0≤R<D` en un modelo fijo. Para `m` consultas, la ruta con reconocimiento gana exactamente cuando

\[
H+mR<mD \quad\Longleftrightarrow\quad m>H/(D-R).
\]

La igualdad es empate. La preparación `H` incluye extracción, certificación y codificación; `R` incluye actualizaciones, reconstrucción y lectura por consulta. Si los costos dependen de cada consulta, usar las sumas reales en lugar del umbral simplificado.

**Ejemplo ilustrativo (unidades abstractas, no medición):** `H=120`, `D=20`, `R=6`: el primer número entero de consultas con economía neta es `m=9` (`120+9·6=174 < 180`). Para `m=8`, `168 >160`.

## 3. Descripciones cortas y reconocimiento caro [F]

Una firma que necesita un solo bit puede costar tanto como el problema original en calcularse. `Φ(x)=Q(x)` responde a la consulta de inmediato solo si ya se computó `Q`: el coste no desaparece por cambiar de nombre a la salida. Del mismo modo, una matriz de rango `d` sobre los racionales no representa automáticamente `d` bits de memoria: hay que medir longitudes de los coeficientes y representación de vectores.

## 4. Formato de resultados comparables

Cada fila de una tabla de rendimiento incluirá como mínimo:

`familia; semilla/versión; n; tamaño de entrada; consultas; representación; extractor; verificador; tiempo total; pico de memoria; error; comparador; entorno; hash de código`.

En esta entrega se contrastan **invariantes y certificados finitos**, no un nuevo benchmark de conteo. Para los experimentos de 8–10 XI se remite a los datos publicados; cualquier comparación nueva con contadores dedicados debe ejecutarse y documentarse aparte.

## 5. Contexto de aplicaciones

- **P frente a NP:** la oportunidad está en reducir el costo completo del reconocimiento más el cálculo; los ejemplos con estructura expuesta no establecen una cota para instancias generales.
- **3-coloración:** comparar cierres locales con obstrucciones globales; la existencia de una frontera pequeña no se presupone.
- **Yang–Mills, gravedad, Navier–Stokes:** declarar la ley de evolución, observables, invariantes y una predicción física contrastable antes de trasladar una estimación de economía de información a física.
