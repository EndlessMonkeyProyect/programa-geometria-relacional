# E-MIRROR v4 — La unidad no se deduce contando imágenes

**Fecha:** 18 de octubre de 2026  
**Relación:** laboratorio independiente, derivado conceptualmente de v3 y de la candidata 3.4.1, sin modificar los ZIP originales.  
**Estatus:** prueba **de un modelo matemático computacional**, no demostración física ni ontológica general.

## Pregunta

> ¿Puede un sistema de reflexiones reconocer si sus imágenes provienen de una unidad, sin haber recibido de antemano el número de fuentes? ¿Cuándo cambia esa capacidad al cambiar de posición o abrir otro canal de reflexión?

## Hallazgos de los escenarios implementados

**A. Dos fuentes reales, una sola imagen.** Se eligen dos puntos luminosos distintos (a 0,32 m de separación), cuyas imágenes virtuales vistas desde la cámara C1 están exactamente sobre la misma línea proyectiva del espejo X+. Si el brillo no es conocido, el sensor ideal del ejemplo recibe *la misma matriz de píxeles* que produciría una sola fuente con doble intensidad aparente. La identidad de observaciones no requiere ruido: es exacta en el modelo. La inferencia ajusta una mancha; no puede descubrir la segunda mediante ese único canal.

**B. Cambio de observador.** Al mover C1 lateralmente 0,68 m hasta C2, aparecen dos manchas distinguibles. Un ajuste que compara modelos de 1 o 2 manchas mediante BIC recupera dos. Usando la dirección de ambas imágenes desde C2 y la dirección común desde C1, con el plano y cámaras calibrados, se triangulan las dos fuentes con errores de 0,13 y 0,29 mm **en esta simulación idealizada**. Las coordenadas reales solo se consultan al evaluar el error, nunca se pasan al ajuste ni a la triangulación.

**C. Cambio de canal sin desplazar la cámara.** C1 mira el espejo Y+ en lugar de X+; las dos fuentes producen dos manchas separadas. La observación inicial no era una imposibilidad de distinguir en todos los marcos.

**D. Una sola fuente, dos imágenes.** Una fuente reflejada una vez en cada uno de dos espejos perpendiculares aparece en dos manchas diferentes dentro de una vista amplia. El detector registra dos manchas, pero la calibración identifica por cuál espejo llega cada una. La reconstrucción inversa de esas dos direcciones estima **una misma fuente** (en esta simulación, ~0,016 mm de error). Contar imágenes no equivale a contar fuentes.

**E. Tolerancia al desplazamiento.** Con los valores de ruido y PSF fijados y 10 semillas de ruido por caso: 0 cm da 0/10 resoluciones de dos manchas; 4 cm, 5/10; 6 cm, 9/10; 8 cm, 10/10. **Esto no es un umbral universal**; cambia al variar exposición, calibración, ruido, tipo de fuente y algoritmo.

## Construcción geométrica

Cada plano especular horizontal o vertical representa una reflexión isométrica. Para X+ situado en x=a:

```text
R_x(x,y,z) = (2a-x, y, z)
R_x(R_x(s)) = s
```

El centro virtual de una fuente s es R_x(s). Con observador c, la dirección de su imagen es proporcional a R_x(s)-c. Los dos emisores s1 y s2 se eligen para que

```text
R_x(s2) = c1 + alpha * (R_x(s1) - c1), alpha=1.15.
```

Así comparten la dirección en C1, aunque no la profundidad, y difieren en C2. En el modelo de cámara puntual con PSF angular gaussiana de amplitud desconocida:

```text
O_C1({s1 con amplitud A, s2 con amplitud A})
  = O_C1({s1 con amplitud 2A}).
```

Con ese canal de observación, **el operador no es inyectivo** respecto de cantidad de fuentes y profundidad. En términos de identificabilidad, no hay cálculo que separe situaciones con datos idénticos. Agregar otra proyección puede romper esa equivalencia para los casos analizados.

Para el control D, una reflexión invertida a partir de una observación (posición c, píxel p y espejo conocido) define un rayo en el espacio real. Los dos rayos de dos espejos independientes se intersectan aproximadamente en un mismo punto; se estima la fuente por mínimos cuadrados sin suministrar su posición verdadera.

## Tres niveles epistemológicos

- **[DERIVADO DENTRO DEL MODELO]** Indistinguibilidad exacta entre dos fuentes y una más brillante desde C1. Resolubilidad de dos manchas desde C2 y desde Y+. Dos manchas compatibles con una sola fuente mediante dos canales ópticos distintos.
- **[CONDICIONAL]** Determinar cantidad de fuentes requiere calibración, hipótesis sobre brillo, PSF, número de rebotes y alternativas admitidas. El detector compara hasta dos componentes *por canal*; no demuestra que un sistema con tres o más fuentes no pueda reproducir los datos.
- **[HIPÓTESIS DEL PROGRAMA]** Una operación de reflexión podría ser el mecanismo que sostiene una unidad a través de proyecciones y marcos distintos. El laboratorio ilustra un sistema reversible y el acceso relacional, pero no establece esa ontología como un teorema.

## Límites (indispensables)

1. Este v4 es una **reducción del v3**, no una ampliación del trazado multirrebote: los espejos son planos, finitos y se considera **un rebote por imagen**, sin interferencia ni dispersión.
2. Las fuentes son puntos emisores ópticamente delgados. La imagen PSF es una gaussiana fija; la radiometría inversa-cuadrática, el desenfoque dependiente de distancia, obstáculos, saturación, movimiento, espectro, polarización, bordes de difracción y oclusiones entre fuentes **no están modelados**. Las amplitudes representan brillo aparente desconocido, que puede calibrarse para producir la equivalencia.
3. Se supone la geometría de espejos, cámaras y canal de reflexión **conocida y exacta**. La reconstrucción no es posible de forma única si estas calibraciones faltan.
4. En la inferencia no se pasa el número verdadero de fuentes, pero los modelos candidatos se restringen a **una o dos manchas**. Esto es un control pequeño, no una solución del problema general de mezclas con cantidad arbitraria de emisores.
5. Múltiples orígenes exactamente co-localizados, o fuentes que permanecen observacionalmente equivalentes en todos los canales disponibles, no se pueden distinguir a partir de esos datos sin información adicional.
6. Este laboratorio no resuelve P vs NP ni Yang–Mills; la similitud con información inaccesible es conceptual. Ni identificabilidad ni reversibilidad de reflejos implican costos polinómicos o brecha espectral.

## Reproducibilidad

Requiere Python 3.10+, NumPy, SciPy, Matplotlib.

```sh
python identidad_mirrors.py
python estudio_umbral.py
python -m unittest -v test_identidad_mirrors.py
```

Archivos generados por esos comandos: `resultados_v4.json`, `estudio_umbral.json` y cinco gráficos PNG. `PRUEBAS_V4.txt` registra el control automatizado.

La candidata original 3.4.1 y los laboratorios previos permanecen intactos. El expediente pendiente sobre las **tres y cuatro esferas** se conserva en `PENDIENTE_LABORATORIO_ESFERAS.es.md` como propuesta no validada.

## Siguiente experimento recomendado

Pasar de imágenes de emisores puntuales a **marcas con orientación y forma** en el cubo 3D, sumar calibración incierta y reflexiones múltiples, e intentar encontrar dos configuraciones distintas que sigan siendo indistinguibles aun al cambiar de cámara y de espejo. Eso define una prueba adversaria real para la hipótesis de unicidad.
