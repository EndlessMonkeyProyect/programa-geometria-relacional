# E-MIRROR v5 · Dos cuartos, vidrio y pared móvil

**Fecha de trabajo:** 2026-10-18  
**Estado:** experimento computacional reproducible. Modelo óptico reducido 1D, **no** una medición física ni una demostración ontológica.  
**Fuentes:** desarrollado como experimento independiente a partir de la candidata 3.4.1 y de los laboratorios v1-v4; ninguno se modifica.

## Pregunta central

¿Qué cambia en las familias de reflexiones cuando dos cuartos tienen profundidades diferentes, están conectados por un vidrio y desplazamos gradualmente la pared del cuarto lateral? ¿Hay una estructura privilegiada en la mitad? ¿Qué información contiene la paridad de reflexiones?

## Aparato virtual

- Cuarto A: longitud fija **2,00 m**.
- Cuarto B: longitud variable **0,35–2,00 m**, incrementos de **0,001 m**.
- En un extremo de cada cuarto hay un espejo plano normal al eje óptico, con reflectividad de intensidad **M=0,95**.
- Entre ellos hay un vidrio representado por **un divisor óptico ideal**, con reflectividad de intensidad **R=0,08** y transmitancia **T=0,92**; no es un modelo de todas las interfaces de una lámina real. Un vidrio común está aproximado por una R efectiva pequeña; además se estudia un divisor semiespejado de R=0,5 para explorar rutas transmitidas y reflejadas.
- Señales breves viajan en incidencia normal, con velocidad c en el aire aproximada por c en vacío; no modelamos índice óptico dentro del vidrio.
- Para valorar el solapamiento temporal, se usa un núcleo gaussiano de ancho **0,12 ns**. Es una tolerancia efectiva de correlación; no una derivación instrumental.
- Se consideran órdenes de eco n=1..8 y luego se estudia por separado la red totalmente acoplada (hasta ocho visitas sucesivas al espejo del fondo).

## Dos operaciones diferentes (no confundir)

### A. Correlación de familias de ecos sin cambiar de cuarto

El vidrio devuelve parte de cada retorno hacia la cavidad y transmite parte del eco al exterior. Consideramos el subconjunto de trayectorias que **no cruza** al cuarto vecino hasta la detección, suponiendo excitación normalizada en cada cavidad. Sus períodos e intensidades ideales son

\[
\tau_A = 2L_A/c,\qquad \tau_B = 2L_B/c,
\]
\[
I_j(n) = (1-R)M^nR^{n-1},\qquad n\ge1.
\]

Un retorno de orden p en A coincide con uno de orden q en B si

\[
p\tau_A=q\tau_B\quad\Longleftrightarrow\quad L_B/L_A=p/q.
\]

Para medir el solapamiento finito sin imponer proporciones privilegiadas:

\[
S(L_B)=\sum_{p,q=1}^{8}\sqrt{I_A(p)I_B(q)}
\exp\!\left[-\frac{(p\tau_A-q\tau_B)^2}{2\sigma^2}\right],\quad \sigma=0{,}12\,\mathrm{ns}.
\]

**S es una medida computacional de coincidencia temporal, no una intensidad óptica registrada ni el autovalor de un modo físico.** No se suman aquí las interferencias de onda, la difracción ni las rutas que cruzan de cavidad.

### B. Enumeración independiente de rutas que sí pueden cambiar de cuarto

Se parte de un impulso saliendo hacia A. Cada visita al espejo de fondo produce una reflexión, y cada llegada al vidrio se bifurca en reflexión (mismo cuarto) o transmisión (cambia de cuarto). El vidrio ideal tiene coeficientes de amplitud r=√R y t=i√(1−R), y el espejo del fondo r_m=−√M. Hasta ocho recorridos hay **255 historias de camino** en este árbol de bifurcaciones (2^8−1). Los resultados cuentan rutas que pueden llegar al vidrio al mismo tiempo y desde el mismo lado, pero el conteo **no se debe interpretar como número de manchas visibles** ni como energía medida sin calcular las fases/interferencias.

## Hallazgos [DERIVADOS EN EL MODELO]

1. **La mitad reaparece sin haberla impuesto:** cuando B=1,00 m, un retorno en A coincide exactamente con dos retornos en B: 13,34256 ns en ambos. Es la coincidencia de orden más bajo no trivial que se detecta con estas longitudes; por ello produce el **máximo interior** del score con vidrio de R=0,08.
2. **No es la única reorganización:** B≈0,667 m corresponde a 1:3; B≈1,333 m a 2:3; B=1,5 m a 3:4; B=0,50 m a 1:4. Las proporciones de racionales de orden pequeño generan picos de diferente visibilidad.
3. **No hay salto espontáneo en B=1 m:** para señales y tolerancias finitas el score cambia continuamente. Un máximo geométrico no es por sí solo un cambio de fase ni una cardinalidad nueva.
4. **El vidrio gobierna accesibilidad:** con R=0 no hay eco repetido del mismo cuarto de orden ≥2; con R=1 no sale señal por transmisión en este canal, aunque las trayectorias internas persistan. Los picos observables dependen de reflectividad y pérdidas.
5. **Resultado no trivial de la paridad completa.** Si el camino atraviesa K veces el vidrio y completa N recorridos de fondo antes de llegar de nuevo al separador, refleja en los espejos del fondo N veces y en el vidrio N−1−K veces. Luego

   \[ N_{\mathrm{ref}}=2N-1-K. \]

   Como salir de A y llegar a A requiere K par, sus historias tienen N_ref **impar**; llegar a B exige K impar y N_ref **par**. La regla se verificó sobre las 255 historias enumeradas para cada geometría. **Cuenta las reflexiones antes de otra interacción con el vidrio; añadir una reflexión final o cambiar el observador modifica la paridad registrada.** No basta para afirmar orientación de una imagen física arbitraria.
6. **En la red conectada se superponen firmas de recorridos diferentes.** A B=1 m, aparecen 18 grupos (tiempo, lado) en los que coinciden caminos con diferentes números de visitas a A y B; con B=√2 m, 0 grupos de ese tipo hasta ocho recorridos. En ambos casos existen rutas distintas de igual número de visitas a cada cuarto (permutaciones), así que no toda coincidencia proviene de razones racionales.
7. **Ejemplo explícito.** Con L_A=2 m y L_B=1 m, las firmas (3 visitas A, 0 B) y (2 visitas A, 2 B) pueden llegar al divisor del lado A tras un recorrido óptico total de 12 m, a **40,0276914 ns**, pese a que sus historias son diferentes. Esto no exige que sus campos se refuercen: las fases pueden sumar o cancelar.
8. **Control de robustez:** de 54 escenarios (6 reflectividades, 3 tolerancias, 3 topes de recorridos), las 45 combinaciones con R entre 0,02 y 0,95 identificaron 1,00 m como su mayor pico interior no trivial; las nueve con R=1 no tienen señal transmitida y no admiten ranking observable en este canal. Este resultado está condicionado a la función de score, el barrido y el modelo.

## Qué permanece por probar [CONDICIONAL]

- La reorganización de **imágenes en una cámara real**, sus inversiones, su nitidez y eventuales caústicas: requiere trazado 2D/3D, vidrio con espesor, refracción y varios observadores.
- La conversión de picos de coincidencia en resonancias de onda: requiere interferencia, espectro, polarización, pérdidas, frecuencia e índice de refracción. La sincronización temporal no obliga al aumento de intensidad en un detector.
- Si aparece alguna escala privilegiada que no se explique simplemente por cocientes racionales y atenuación de los retornos. En este modelo **no** apareció una escala universal nueva.
- Si existe reconstrucción única de un origen desde los rayos detectados sin conocer previamente la geometría y el número de fuentes; esta versión no es una prueba de identificabilidad general.

## Lectura para el Programa [HIPÓTESIS, NO TEOREMA]

La métrica de retorno \(\tau=2L/c\) permite que un sistema establezca relaciones de escala desde la repetición. El cierre compartido \(p\tau_A=q\tau_B\) ofrece un ejemplo de **comunes** entre marcos que no tienen la misma extensión. La paridad completa de reflexiones puede codificar, en este montaje, el cruce de un límite entre marcos. No derivamos de aquí la ontología global de la reflexión, el nacimiento de dimensiones, P=NP ni la brecha de masa de Yang–Mills.

## Archivos y reproducción

- `cuartos_acoplados.py` — barrido, correlación, enumerador óptico reducido y figuras 01–04.
- `analisis_rutas.py` — control de recorridos cruzados y figura 05.
- `robustez.py` — 54 controles de parámetros.
- `test_cuartos_acoplados.py` — 12 pruebas `unittest`.
- `resultados_v5.json`, `auditoria_rutas_v5.json`, `robustez_v5.json`, `barrido_v5.csv` — datos para evaluación de otro agente.
- `PENDIENTE_LABORATORIO_ESFERAS.es.md` — idea reservada de tres y cuatro esferas, sin convertirla en resultado.
- `MANIFIESTO_SHA256.json` — listado SHA256 de archivos del laboratorio.

Requisitos: Python 3.10+, NumPy, SciPy y Matplotlib.

```bash
python cuartos_acoplados.py
python analisis_rutas.py
python robustez.py
python -m unittest -v test_cuartos_acoplados.py
```

La salida se puede reproducir sin intervenir los archivos canónicos 3.4.1.
