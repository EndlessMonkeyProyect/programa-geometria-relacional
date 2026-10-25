# E-MIRROR v6 · De los ecos a la imagen accesible y la fase

**Fecha:** 18 de octubre de 2026. **Programa:** Geometría Relacional, rama experimental E-MIRROR.  
**Estado:** experimento computacional independiente, **no** validación de una hipótesis ontológica, no ensayo instrumental ni demostración de nuevos teoremas físicos. Se conserva la versión 3.4.1 y los laboratorios v1–v5 sin modificarlos.

## Pregunta

Si dos cuartos están separados por un vidrio parcialmente reflectante, uno mantiene 2 m de profundidad y movemos lentamente la pared del otro, ¿los máximos de coincidencia de retornos del v5 se convierten en imágenes visibles o interferencia física? ¿Qué conserva la paridad cuando dos espacios se iluminan desde un mismo origen repartido?

## Dos modelos complementarios (NO equivalentes)

**A. Cámara de barrido temporal de rayos 2D** [DERIVADO DEL MODELO]. Un emisor situado en el plano del vidrio ilumina hacia A y B. Los rayos viajan en incidencia angular limitada por ±8° y se reflejan en los espejos del fondo y en el vidrio. Los terminales planos y el vidrio tienen semianchura finita de 0,30 m. Una pequeña fracción de intensidad (~2 %) de cada retorno se mide en cada lado. Se trazan hasta ocho visitas a los espejos de fondo. Los resultados son mapas de **intensidad vs coordenada lateral y tiempo**; NO son fotografías con una cámara convencional, ni incluyen lentes, difracción, refracción real en vidrio, polarización, curvatura, ondas o 3D. Un fotodetector resuelto temporal y espacialmente se acercaría a esta observación ideal.

**B. Modelo de campo escalar de un solo modo** [DERIVADO DEL MODELO]. Misma pareja de longitudes y splitter óptico ideal R=0,35 (reflectividad de intensidad), M=0,95 (reflectividad de espejos); se inyecta una **única señal coherente dividida inicialmente entre ambos brazos**, con longitud de onda nominal 633 nm y pulso gaussiano de 0,12 ns. Se calculan las amplitudes de los recorridos; la onda que retorna por A y B se detecta separadamente o se recombina con un **combinador óptico adicional** de fase relativa ajustable. La fase afecta la intensidad de salida incluso cuando las longitudes de recorrido coinciden. Por razones de complejidad, la distribución transversal de rayos de A **no** se acopla a la solución de interferencia de B; se presentan dos experimentos complementarios, no una simulación Maxwell 3D unificada. La fracción capturada del 2 % es un puerto débil de medida, no un detector físicamente diseñado.

El splitter de campo ideal usa coeficientes r=√R y t=i√(1−R), con un puerto de medida débil η=0,02. La unidad del campo es arbitraria. La interferencia física real requiere coherencia suficiente, coincidencia espacial, polarización compatible, detector y calibración de fase.

## Resultado 1: coincidencia exacta no equivale a máximo de brillo

Para A=2 m y B=1 m, al llegar un retorno A (trayectoria 4 m) y dos retornos B (4 m), ambos ocurren a 13,3425638 ns. Para esa ventana temporal:

| Lectura | Intensidad relativa |
|---|---:|
| Suma incoherente de historias | 0,0062977875 |
| Mínimo con fase del combinador ajustada | 0,0008748766 |
| Máximo con fase del combinador ajustada | 0,0117206984 |

Es el **mismo montaje geométrico** con distintas condiciones de fase para reunir la señal. La diferencia máximo/mínimo ~13,4 veces es propia del modelo y sus parámetros. El valor 1 m es un punto de **coincidencia temporal**, no un punto obligatorio de máxima intensidad. Los límites «mínimo» y «máximo» del gráfico 02 se obtienen optimizando la fase del combinador en cada longitud; **no** son una curva experimental con fase fija.

## Resultado 2: aparecen dos métricas distintas

- Escala de retorno: τ_j=2 L_j/c; para dos cuartos, p τ_A=q τ_B equivale a L_B/L_A=p/q. La mitad 1/2 es un cociente simple, pero otros 1/3, 2/3, 3/4 producen coincidencias.
- Escala de interferencia: al desplazar la pared B, la fase relativa de un retorno **doble en B** cambia en proporción a 4 B/λ. El período local de franja es ΔB=λ/4 ≈ **158,25 nanómetros** para λ=633 nm, bajo el modelo de onda ideal y mirando la coincidencia A(1)–B(2).

La coincidencia temporal tiene ancho macroscópico fijado por el pulso (milímetros o centímetros según orden); dentro de ella puede haber muchas franjas submicrométricas constructivas/destructivas. Una escala **no** determina por sí sola la otra. La curva de barrido en pasos de 1 mm es una **envolvente de contraste**, no permite resolver franjas del campo real a 633 nm.

## Resultado 3: reglas de paridad necesitan origen identificado

En el v5 se demostró, **para historias iniciadas siempre en A**, que lado A requiere transmisiones pares y lado B transmisiones impares; con la convención adoptada, terminan con paridad de reflexiones impar/par respectivamente. Esa inferencia NO es invariante si no se conoce el lado de inicio.

En v6, al inyectar la señal en **ambas** cavidades, a t≈13,34 ns coinciden:

- una visita al espejo de A: una reflexión total (**impar**), lado A;
- dos visitas al espejo de B y una reflexión en el vidrio: tres reflexiones totales (**impar**), lado B.

Por tanto, la paridad no identifica por sí sola el lado de llegada cuando el sistema tiene varios estados de entrada posibles. No se debe confundir la paridad de visitas al espejo del fondo con la paridad de **todas** las reflexiones ni con la orientación visual de una imagen 3D.

## Resultado 4: los paneles finitos limitan la observación

La cámara temporal registra sólo rayos que alcanzan espejos y vidrio dentro de sus aperturas. En cuatro geometrías de comparación (A=2 m y B=0,667 m, 1,0 m, √2 m, 1,5 m), las observaciones temporales muestran familias de retornos distintas. Pero el **brillo total integrado en 48 ns** no alcanza un máximo general en B=1 m; favorece en este montaje también las cavidades cortas y la entrada angular. Así, las coincidencias de tiempo v5 no se pueden reinterpretar como brillo general de una imagen.

## Controles y límites

- **18 pruebas `unittest` superadas**, con controles de fase, longitud, retardo, apertura, opacidad del puerto de medida y paridad.
- **18 combinaciones de robustez** R×sigma (6×3). La visibilidad de fase cambia con el vidrio y exige coherencia. La matriz está en `controles_v6.json`.
- La potencia óptica absoluta no está calibrada; intensidades normalizadas.
- El tratamiento espectral utiliza la fase de una frecuencia central y una envolvente gaussiana; no modela dispersión, polarización, ruido de disparo, detector real ni conservación energética de la extracción por puertos físicos completos.
- Las pérdidas, truncamientos de historias y la geometría 2D acotan la validez. Los rayos 2D no forman necesariamente imágenes ópticas distinguibles de un objeto extendido; el laboratorio **no** prueba todavía una ley de «unicidad de foco» en imágenes 3D.
- La relación con cardinalidad, tiempo relacional, escalas ontológicas, P frente a NP o Yang–Mills sigue siendo [HIPÓTESIS], no derivación.

## Archivos

- `espejos_v6.py`: sensor de rayos 2D temporal, campo escalar, cálculos y gráficos 01–03.
- `controles_v6.py`: matriz de parámetros, gráfico 04 (paridad/robustez) y 05 (franjas subescala).
- `test_espejos_v6.py`: pruebas.
- `resultados_v6.json` y `controles_v6.json`: evidencia numérica estructurada.
- `01_camara_temporal_2D.png`, `02_interferencia_en_mitad.png`, `03_fase_y_observabilidad.png`, `04_paridad_y_robustez.png`, `05_franjas_subescala.png`: visualizaciones.
- `HALLAZGO.es.md`: interpretación investigable en narrativa→ontología→matemática.
- `PENDIENTE_LABORATORIO_ESFERAS.es.md`: conserva el encargo pendiente del usuario.
- `PRUEBAS.txt`, `MANIFIESTO_SHA256.json`: ejecución y hashes.

Reproducir con Python 3.10+, NumPy, SciPy y Matplotlib:

```bash
python espejos_v6.py
python controles_v6.py
python -m unittest -v test_espejos_v6.py
```
