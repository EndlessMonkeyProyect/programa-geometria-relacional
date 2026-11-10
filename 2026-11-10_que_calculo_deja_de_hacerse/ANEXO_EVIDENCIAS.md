# Evidencias y reproducción

**Endless Monkey Project**  
*Relational Geometry Program*  
10 de noviembre de 2026 · versión 0.3

## Qué hay en cada carpeta

| Ruta | Contenido | Sección del artículo |
|---|---|---|
| `experimentos/verificar_reconstruccion_y_convergencia.py` | Teoremas 1 a 4 en tamaños pequeños, sin dependencias | §3–§6 |
| `experimentos/intercambio_y_convergencia/` | Controles C1–C8 y su archivo de resultados | §8, §10 |
| `experimentos/reconocimiento_de_paridades_distribuidas/` | Generador de fórmulas, reconocedor de compuertas, contador, DPLL y su archivo de resultados | §9 |
| `experimentos/linea_base_generica/` | Eliminación de variables sin reconocimiento, comparación y escala, prueba de contrato, con sus resultados | §9 |

## Requisitos

Python 3.10 o posterior. NumPy para los laboratorios. NetworkX es opcional: solo agrega una segunda ordenación de eliminación en la comparación.

## Cómo reproducir

Desde la raíz de esta carpeta:

```bash
python3 -I experimentos/verificar_reconstruccion_y_convergencia.py
python3 -I experimentos/linea_base_generica/eliminacion_generica.py
python3 -I experimentos/linea_base_generica/comparacion_y_escala.py --salida comparacion.json
python3 -I experimentos/linea_base_generica/prueba_adversarial.py --salida adversarial.json
python3 -I experimentos/linea_base_generica/comparacion_y_escala.py --dimacs instancias/
```

El último comando escribe las 23 fórmulas del §9 en formato DIMACS, cada una con su conteo esperado en la cabecera, para probarlas con cualquier contador dedicado.

Los dos laboratorios escriben su archivo de resultados en una ruta fija; conviene correrlos sobre una copia para conservar los archivos de esta carpeta:

```bash
cp -r experimentos /tmp/copia && cd /tmp/copia
python3 -I reconocimiento_de_paridades_distribuidas/laboratorio_relaciones_distribuidas.py
python3 -I intercambio_y_convergencia/laboratorio_convergencia.py          # C1–C8, unos dos minutos
python3 -I intercambio_y_convergencia/laboratorio_convergencia.py C6 C7    # controles sueltos
```

`laboratorio_relaciones_distribuidas.py` escribe junto a sí mismo; `laboratorio_convergencia.py`, en el directorio actual.

## Registro de reproducción

Entorno: Python 3.13.18, NumPy 2.5.3, NetworkX 3.7, Linux x86_64. Fecha: 10 de noviembre de 2026.

| Componente | Resultado |
|---|---|
| Verificador autónomo | 16 configuraciones → 8 patrones; 56 conjuntos de cinco estados; 336 trayectorias, 336 cierres y 1.344 retracciones; 56 ternas locales; 175 conteos aleatorios iguales a fuerza bruta |
| C1–C8 completo (133 s) | Coincide con `resultados_convergencia.json` en todos los campos no temporales |
| Laboratorio de paridades distribuidas | 11 controles principales y 8 con conexiones largas, 144 tablas de verdad, 30 fórmulas aleatorias y 2 controles fuera de contrato: coincide con `RESULTADOS_RELACIONES_DISTRIBUIDAS.json` en todos los campos no temporales |
| Eliminación genérica | 300 fórmulas aleatorias iguales a fuerza bruta |
| Comparación y escala | 23 fórmulas; todos los conteos completados coinciden entre rutas; `RESULTADOS_COMPARACION.json` |
| Prueba de contrato | 5.889 fórmulas: 4.444 rechazadas, 1.445 aceptadas con el mismo conteo que la eliminación genérica; `RESULTADOS_ADVERSARIAL.json` |

`RESULTADOS_RELACIONES_DISTRIBUIDAS.json` y `resultados_convergencia.json` son los archivos de la campaña del 9 de noviembre. El reconocedor actual rechaza explícitamente las entradas de paridad que salen de la familia; con él, el laboratorio reproduce esos archivos en todos los campos no temporales.

Los tiempos dependen del equipo y de la carga. Los del §9 salen de una sola ejecución de `comparacion_y_escala.py`, con el mismo protocolo para todas las rutas; los del §8, del archivo de C1–C8.

## Nombres históricos

Los archivos de código conservan identificadores anteriores para que se puedan rastrear. En el artículo se usa el nombre del mecanismo.

| Identificador | Nombre en el artículo |
|---|---|
| GR3 | Reconstrucción de las seis comparaciones del tetraedro |
| ROSI | Reconocer antes de cerrar: cierre con un estado pendiente |
| CAG | Conteo con reflejos dados |
| C1–C2 | Descomposición del intercambio y rangos |
| C3–C4 | Operador de cruce en los dos preprints de octubre |
| C5 | Unicidad del referente y su construcción |
| C6 | Reconocer antes de cerrar, recorrido exhaustivo |
| C7 | Conteo con ecuaciones de paridad y cláusulas disyuntivas |
| C8 | Ventana de interpolación y costo de reconstrucción |
