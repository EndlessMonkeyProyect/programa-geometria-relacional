# Programa de Geometría Relacional — carpeta ordenada

**24 de octubre de 2026 · punto de partida para la nueva versión**

Esta carpeta reúne en un solo lugar los cinco paquetes compartidos hoy, ordenados en cinco partes y sin duplicados:

- `Programa_Geometria_Relacional_O93_NS_Pruebas_Reproducibles_2026-10-22.zip`
- `LAB_CONV_v2_NODOS_CIERRE_PNP_2026-10-22.zip`
- `R02_PUENTE_Y_LABORATORIO_2026-10-23.zip`, más el `.md` y el `.pdf` de R‑02 enviados sueltos
- `Programa_Geometria_Relacional_Rama_NS_Integral_O24_O93_2026-10-24.zip`

En la noche se sumaron el manuscrito público y el suplemento de ritmo, ciclo base, tiempo y gravedad, los dos del 24 de octubre.

**Nada se reescribió.** Los documentos y programas originales están intactos; solo cambió dónde viven. Lo único nuevo de esta edición es:
- este índice;
- `01_HILO/HILO_ONTOLOGICO_INTEGRADO_2026-10-24.md`, el texto de lectura de esta edición;
- `01_HILO/ESQUEMA_ACORDADO_2026-10-24.md`;
- las versiones en inglés (`.en.md`) del texto de lectura, de CME‑003, del manuscrito público y del suplemento, y `00_READ_FIRST.en.md`;
- los README de `00_PUBLICACION/` y de `01_HILO/fuentes/07_ritmo_y_gravedad_recuperados/`;
- las fichas y los programas `CME-001`, `CME-002` y `CME-003`;
- las carpetas `revision_2026-10-24/` de cada rama;
- `MANIFIESTO_SHA256.txt`, `PROCEDENCIA.csv`, `DUPLICADOS_RETIRADOS.csv` y `verificar_integridad.py`.

## Las partes

| Carpeta | Qué contiene | Estado |
|---|---|---|
| `00_PUBLICACION/` | El manuscrito público del 24 de octubre (md y PDF, tal como llegaron) y su versión en inglés. | Licencia y DOI sin asignar. |
| `01_HILO/` | `HILO_ONTOLOGICO_INTEGRADO_2026-10-24.md`, la imagen actual del programa con el lenguaje como guía y soporte (el lenguaje, el hilo, el diccionario, el núcleo formal, las realizaciones, las ramas, masa, tiempo y gravedad, la matriz y, aparte, la capa de enlaces); el esquema acordado; Imagen Total 3.9 (PDF, informe general, índice, atlas); continuidad y protocolo del 22 de octubre; secuencia ontología → matemática → computación; `SUPLEMENTOS/` con el suplemento de ritmo y gravedad; `fuentes/` con fundamentos, núcleo formal, lenguaje, síntesis del 20 de octubre, cristal semántico, «El hilo del dos» y las fuentes de ritmo y gravedad. Hay versión en inglés del texto de lectura y del suplemento. | Texto de lectura de esta edición; lo abierto está ordenado en su parte IX. |
| `02_REALIZACIONES/` | `01_cubo_de_espejos/`: acta, revisión del radio dinámico, documento del cubo, geometría O19–O22, O59, CME‑001, CME‑002 y CME‑003. `02_esferas/`. `03_circuito_C4/`. | CME‑001 a CME‑003 hechos; de CME‑003 queda la regla de la pared que da las cuatro referencias. |
| `03_RAMAS/` | Navier–Stokes, P frente a NP y Yang–Mills, cada una con su versión vigente y sus notas de revisión. | Ver «Qué es vigente». |
| `04_LABORATORIOS/` | Espejos E‑MIRROR v1–v8 y radios de esferas v10, con sus programas, datos y pruebas. | 151 pruebas pasan. |
| `05_ARCHIVO/` | Historia completa de Navier–Stokes (v3.7, O23–O38, O39–O53, O54–O92), imagen integral del 18 de octubre, auditorías anteriores, corpus textual 3.9 y las dos notas para el compilador recibidas el 24 de octubre (`notas_recibidas_2026-10-24/`). | Conservado tal cual. |

## Qué es vigente en cada rama

- **Navier–Stokes:** `03_RAMAS/navier_stokes/VIGENTE_O93/` (22 de octubre), con el capítulo NS de la Imagen Total 3.9 y los mapas de la rama. La vía hacia un teorema sobre la ecuación propia está en `modelo_propio_O18/`.
- **P frente a NP:** `03_RAMAS/p_vs_np/VIGENTE_LAB_CONV_V2/` (22 de octubre).
- **Yang–Mills:** `03_RAMAS/yang_mills/VIGENTE_R02/` (23 de octubre), con R‑01 y el acta de rescate del 22 de octubre en `FUENTES/`.

Cada rama tiene `revision_2026-10-24/` con lo comprobado, lo que conviene corregir en la próxima edición y el programa que lo verifica.

## Decisiones tomadas hoy

- El objetivo es un hilo de economía mínima para entender la realidad. Primero el hilo en sus propios términos; los enlaces con la literatura van después, en una capa aparte al final.
- Orden del hilo: la totalidad, cuya propiedad es la indeterminación → la reflexión → cierre o apertura según los ángulos → las ramas.
- Los ángulos de cierre están dados por la estructura que generan los múltiplos que deja la pared que se corre. CME‑002 escribe esa regla y la prueba en dos lecturas, ángulos e identidades: lo que decide si el recinto cierra, se repite o se abre es la suma de las fracciones frente a la totalidad.
- La gramática común de las ramas es emergente, no fundamento.
- Criterio de control: si el hilo va por el buen camino, se cierra solo.

## Qué se recuperó que antes no estaba a la vista

- «El hilo del dos» completo, 37 documentos del 13 y 14 de octubre que solo vivían como texto dentro del corpus 3.9. Se recuperaron byte a byte, cada uno verificado con el sha256 que el corpus registra (`01_HILO/fuentes/06_hilo_del_dos/`). Ahí ya estaban la reflexión ±1 en cada nodo, la genealogía 4 → 3 y 5, 8 → 7 y 9, el bit abierto del 8, el tres como 2² − 1 y la cota N1 del motor de tablas.

- Los programas, resultados y registros de O44–O48, que solo estaban dentro de sus zips (`05_ARCHIVO/navier_stokes_O39_O53/desarrollos_extraidos/`).
- El cristal semántico integral, 12 archivos que solo estaban comprimidos (`01_HILO/fuentes/05_sintesis_y_lenguaje_2026-10-20/fuentes_cristal_semantico/`).
- Dos fuentes del suplemento de ritmo y gravedad, verificadas con su sha256: GR3, «Concordancia unísona», del 18 de octubre, y el falsador de sincronía de la v5.9, del 8 de octubre (`01_HILO/fuentes/07_ritmo_y_gravedad_recuperados/`). Otras dos fuentes que cita el suplemento no están en ningún material disponible; su README lo dice.
- El ensayo C4 completo: verificador, 16 estados y explorador HTML (`02_REALIZACIONES/03_circuito_C4/C4_v3_8_1/ENSAYO_C4_2026-10-21/`). Su `INFORME.md` es el `ENSAYO_C4_FUENTE_2026_10_21.md` de la carpeta superior.

## Qué se retiró

Se retiraron 85 elementos. `DUPLICADOS_RETIRADOS.csv` registra cada uno con su sha256 y dónde quedó la copia conservada:

- 62 zips cuyo contenido completo está extraído, incluidos los 40 paquetes originales O54–O92.
- La copia completa del paquete O93 del 22 de octubre, idéntica a `VIGENTE_O93/`.
- Las copias de reejecución, idénticas a los resultados de O93.
- Una copia del laboratorio de esferas.
- El `.md` suelto de R‑02, idéntico.
- El `.pdf` suelto de R‑02, con el mismo texto y otros bytes.
- Una caché `.pyc`.

Se conservan a propósito 63 copias internas, unos 3 MB:
- las copias internas de código y datos dentro de cada laboratorio, para que cada uno corra y verifique por sí solo;
- los dos zips `O53_ORIGINAL_SIN_MODIFICAR.zip` de O62 y O63, porque el verificador de O63 exige su presencia.

## Cómo verificar

```bash
python3 verificar_integridad.py
```

Comprueba el sha256 de cada archivo contra `MANIFIESTO_SHA256.txt`. `PROCEDENCIA.csv` dice de qué paquete y ruta vino cada archivo recuperado.

Los manifiestos internos de cada paquete siguen valiendo dentro de su carpeta. Los de la rama integral usan rutas antiguas y quedan en `05_ARCHIVO/auditorias/rama_NS_integral_2026-10-24_rutas_antiguas/` solo como registro.

Desde la nueva estructura se re-ejecutaron y dieron los mismos resultados, byte a byte:
- O93 (`verificar_o93.py`), LAB‑CONV v2 y su verificador exhaustivo, R‑02, CME‑001, CME‑002, CME‑003, O59, O63, O84 y el ensayo C4;
- las pruebas de los nueve laboratorios de espejos y esferas;
- los tres programas de revisión.

La única falla es la ya conocida de `simulacion_galerkin.py` en Python 3.13, al generar la figura; sus números salen idénticos. La corrección está en las notas de revisión de Navier–Stokes.

## Próximo paso de edición

1. Revisar `01_HILO/HILO_ONTOLOGICO_INTEGRADO_2026-10-24.md`, en especial la tabla «El lenguaje a lo largo del hilo» (lectura de edición) y la fila del electrón y el protón; después, los abiertos de su parte IX.
2. Lo que queda de CME‑003: la regla de la pared que se corre que da cuatro referencias intercambiables. π/2 y π/3 ya salen de esas referencias.
3. Atender los pendientes de cada `revision_2026-10-24/`.
4. Para publicar: elegir licencia y DOI, que el manuscrito deja sin asignar, y conseguir las dos fuentes del suplemento que faltan (MF‑43 y «Ritmo, radio y relatividad relacional»).
