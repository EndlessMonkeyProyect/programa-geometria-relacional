# G–01 · El mecanismo de la gravedad — entrega del 1 de noviembre de 2026

**Programa de Geometría Relacional · Le Matt Ansatz Di Ego**

[Read this in English](READ_FIRST.en.md).

Esta carpeta reúne el documento *G–01. El mecanismo de la gravedad*, versión 1.3, en español y en inglés, junto con todo el material que respalda lo que afirma: un verificador reproducible, la revisión que llevó de la versión 1.2 a la 1.3, las versiones anteriores y el código de las figuras. Se agrega a las ediciones anteriores sin modificar nada de ellas.

**Estatus.** No es una teoría de la gravedad ni una derivación de la ley de Newton. Es el punto de partida declarado del hilo G–01, con estado ROSI **OPEN**:
- Establece resultados exactos en modelos declarados. El contrato de O58, a²+b²+1=N², es exactamente el conjunto de puntos enteros del hiperboloide de Minkowski en 2+1: la unidad pendiente 1/N² es el cuadrado del ritmo propio, (dτ/dt)², y el horizonte C corresponde al cono de las ternas pitagóricas. Todas sus soluciones forman un único árbol de transformaciones de Lorentz enteras (Berggren). Además, un normalizador con resolución finita corrige la discontinuidad del MCM.
- Deja abiertos y declarados: la regla que elige la continuación, el mapa de la distancia entre cierres a una separación física, la fuente y el acoplamiento, el contrato de tres canales en 3+1 y el puente gravitatorio. La coincidencia de forma con la dilatación gravitatoria √(1−r_s/r) se registra como hipótesis, no como resultado.

**Autoría y asistencia.** La ontología, las versiones 1.0 y 1.2 y las fuentes del programa son del autor. La revisión de la 1.0 (versión 1.1), la sección 2D, los anexos B18–B21, el verificador y la traducción inglesa se elaboraron con asistencia de IA (Claude) a partir de las versiones del autor. La versión de referencia es la española.

## Contenido

| Ruta | Qué contiene |
|---|---|
| `articulo/` | El documento v1.3 en Word, PDF y Markdown, en español (`G01_Mecanismo_de_la_Gravedad_v1.3_2026-11-01`) y en inglés (`G01_Mechanism_of_Gravity_v1.3_2026-11-01_EN`). Figuras en `figuras_es/` y `figures_en/` |
| `verificacion/verificar.py` | Verificador con aserciones para cada resultado exacto [T] y cada control [F] que se puede calcular. Sólo biblioteca estándar de Python |
| `verificacion/resultados.json` | Resultados regenerados por el verificador |
| `verificacion/cotejar_O58.py` | Coteja las ramas O58 calculadas con el archivo original de O58 de la edición del 24 de octubre |
| `referencia_resultados/` | Copia intacta de los resultados entregados, contra la que se compara |
| `reproducir_todo.sh` | Verifica integridad, corre el verificador, coteja O58 y compara con tolerancia |
| `comparar_resultados.py` | La comparación con tolerancia, también usable por separado |
| `entorno.json` | Versión de Python, semillas y parámetros |
| `revision/G01_revision_v1.2_a_v1.3.xlsx` | Revisión de la v1.2: 17 hallazgos, dónde se resolvió cada uno en la v1.3, comprobaciones con fórmulas y calculadoras del hiperboloide, del árbol de Berggren y del MCM |
| `historial/` | Versiones 1.0, 1.1 y 1.2 del documento, tal como se entregaron |
| `herramientas/generar_figuras.py` | Regenera las figuras dibujadas por código (requiere matplotlib; no forma parte de la verificación) |
| `MANIFIESTO_SHA256.txt` | Huella de cada archivo distribuido |

## Orden de lectura

1. **El documento**, `articulo/`: resumen ejecutivo y §2D, que es lo nuevo de la versión 1.3.
2. **Anexo B**, B18 a B21: las demostraciones de §2D y del normalizador con resolución finita.
3. **§12 y §17**: qué candidato concreto queda para el mecanismo y qué está resuelto, superpuesto, abierto o prematuramente colapsado.
4. **La revisión**, `revision/`: por qué cambió el documento entre la 1.2 y la 1.3.

## Qué establece

| Resultado | Dónde | Estatus |
|---|---|---|
| a²+b²+1=N² es N²−a²−b²=1; normalizado, v²+(dτ/dt)²=1 con dτ/dt=1/N | §2D, B18 | [T] Identidad exacta |
| El horizonte C corresponde al cono a²+b²=N² (ternas pitagóricas); los cierres se acercan sin alcanzarlo | §2D | [T] en la realización hiperbólica |
| Las matrices M₁, M₂, M₃ (Berggren) conservan la forma; toda solución con N>1 tiene un padre único y todas forman un solo árbol con raíz (2,2,3) | §2D, B19 | [T] Demostración por descenso; 754 de 754 soluciones con 1<N≤3000 |
| En la rama Pell, arccosh N = k·ln(3+2√2); la cadena anidada de O58 (3→99→3 880 899) triplica la rapidez | §2D, B20 | [T] Ya estaba en O58 como cadena anidada; la lectura como rapidez es nueva |
| La regla de múltiplos M=qN no sigue las aristas del árbol: de 15 soluciones con 3<N≤120, sólo 2 tienen N múltiplo del de su padre | §2D | [F/T] Cuál composición es la física queda SUPERPOSED |
| El MCM de denominadores es discontinuo; con resolución ε, q_ε≤⌈1/ε⌉ (Dirichlet) | §2B, B21 | [T] La resolución como contrato físico es [H] |
| La sintonía produce fuerza radial sólo si el peso del estado sintonizado depende de la separación | §11, B10 | [T] en la familia declarada |
| La respuesta 1/R³ no admite órbitas circulares estables | §13, B11 | [T/F] |
| Lectura física 1/N = m/E, contrato de tres canales en 3+1, coincidencia con √(1−r_s/r) | §2D | [H] Hipótesis declaradas |

## Reproducción

    bash reproducir_todo.sh

No hay dependencias que instalar: el verificador usa sólo la biblioteca estándar de Python 3.9 o posterior y tarda unos segundos. El script hace cuatro cosas:
1. **Integridad.** Comprueba el manifiesto SHA-256 de los archivos tal como se distribuyeron.
2. **Verificación.** Corre `verificar.py`, que tiene sus propias aserciones y falla si un enunciado no se cumple.
3. **Cotejo con O58.** Comprueba que las 16 ramas desde (2,2,3) hasta M≤200 coinciden con `ramas_compatibles_hasta_200.csv` del propio O58. Fuera del repositorio este paso se omite.
4. **Comparación.** Compara los resultados regenerados con `referencia_resultados/`, con tolerancia y no bit a bit: reales con `RTOL = 1e-9` y `ATOL = 1e-12`; enteros, booleanos, textos y estructura, exactos.

## Relación con el resto del repositorio

| Fuente | Qué aporta a G–01 |
|---|---|
| [O58 — La estela de escalas](../2026-10-24/05_ARCHIVO/navier_stokes_O54_O92/O58_Estela_Escalas_Normalizacion_Cuadratica_2026_10_21/O58_Estela_Escalas_Normalizacion_Cuadratica_2026_10_21/O58_FORMALIZACION.es.md) | El contrato a²+b²+1=N², las ramas, la ecuación de Pell y la cadena anidada (O58.12) |
| [O40 — Normalizador heredado](../2026-10-24/05_ARCHIVO/navier_stokes_O39_O53/documentos/O40_NORMALIZADOR_HEREDADO_RESTO_Y_REORGANIZACION.es.md) | Normalizador común, inclusión de fases y resto |
| [O45 — Tiempo y espejo móvil](../2026-10-24/05_ARCHIVO/navier_stokes_O39_O53/documentos/O45_TIEMPO_ESPEJO_MOVIL_RITMOS_NS_2026-10-20.md) | Regla de la cadena del marco móvil y comparación de ritmos |
| [O78](../2026-10-24/05_ARCHIVO/navier_stokes_O54_O92/O78_Eco_Condicion_Dinamica_Onda_Esfera_Anillo_2026_10_22/O78_Eco_Condicion_Dinamica_Onda_Esfera_Anillo_2026_10_22/O78_FORMALIZACION.es.md) y [O81](../2026-10-24/05_ARCHIVO/navier_stokes_O54_O92/O81_Referencia_Coherente_Resto_Dinamico_2026_10_22/O81_Referencia_Coherente_Resto_Dinamico_2026_10_22/O81_FORMALIZACION.es.md) | Controles de Navier–Stokes: resto dinámico y referencia coherente |
| [R-01 — Puente de normalización y autorreferencia](../2026-10-24/03_RAMAS/yang_mills/R01/R01_PUENTE_NORMALIZACION_AUTORREFERENCIA_YM.es.md) | Múltiplo interno y múltiplo común |
| [Suplemento de ritmo, tiempo y gravedad](../2026-10-24/01_HILO/SUPLEMENTOS/Suplemento_Ritmo_Ciclo_Base_Tiempo_y_Gravedad_2026-10-24.md) ([en inglés](../2026-10-24/01_HILO/SUPLEMENTOS/Suplemento_Ritmo_Ciclo_Base_Tiempo_y_Gravedad_2026-10-24.en.md)) | Ciclo base, recurrencia y posible puente de gravedad |
| [Ritmo y gravedad recuperados](../2026-10-24/01_HILO/fuentes/07_ritmo_y_gravedad_recuperados/README.md) | Sintonización G–R3, contrato de escalas y no-go |
| [Imagen Total 3.9](../2026-10-24/01_HILO/imagen_total_3_9/Imagen_Total_3_9_Informe_General.md) | Ontología, laboratorios, cierre, masa, tiempo y gravedad |
| [Más allá de Yang–Mills](../2026-10-27_mas_alla_de_yang_mills/LEER_PRIMERO.md) | Rama gauge: refinamiento, defecto de cierre y acciones |
| [Cubo de espejos y P frente a NP](../review_requests/2026-10-30_mirror_cube_p_vs_np_es/LEER_PRIMERO.md) | Rama de grafos: diamantes e interfaces |

## Historial de versiones

| Versión | Archivo | Procedencia |
|---|---|---|
| 1.0 | `historial/G01_Mecanismo_de_la_Gravedad_v1.0_2026-11-01.docx` | Del autor. Primera fijación del hilo G–01 |
| 1.1 | `historial/G01_Mecanismo_de_la_Gravedad_v1.1_2026-11-01.docx` | Revisión de la 1.0 con asistencia de IA: figura de K4 corregida, criterio de sintonía, descarte de 1/R³, tesis de resolución con dinámica de segundo orden |
| 1.2 | `historial/G01_Mecanismo_de_la_Gravedad_v1.2_2026-11-01.docx` | Del autor. C como horizonte, normalizador común de O40/O58 como mecanismo generador, aceleración como consecuencia |
| 1.3 | `articulo/` | Sobre la 1.2: sección 2D, B18–B21, normalizador con resolución finita, correcciones y traducción inglesa |

El registro detallado de cambios de cada versión está al final del anexo C del documento.

## Validación de esta entrega

| Entorno | Qué se corrió | Resultado |
|---|---|---|
| Python 3.13.18, sin dependencias externas | `reproducir_todo.sh` en una copia limpia del repositorio | Todas las aserciones pasan; las 16 ramas coinciden con el archivo de O58; todo coincide con la referencia |

## Ruta de investigación siguiente

**Prueba P** (tres canales: ¿forma a²+b²+c²+1=N² un árbol con descenso en 3+1?) → **G–02** (regla que elige entre M₁, M₂ y M₃) → **G–04** (mapa de la distancia entre cierres a una longitud física).
