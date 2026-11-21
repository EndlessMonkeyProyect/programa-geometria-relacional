# Instrucciones de incorporación para administración de repositorio

**Cambio propuesto:** consolidación de los resultados formalizados sobre herencia, granularidad, recierre, reconstrucción y recuperación acumulada, con dos laboratorios reproducibles.  
**Fecha:** 21 de noviembre de 2026 · **Versión de publicación:** 3.5  
**Modalidad:** aditiva, con conservación de la trazabilidad histórica.

Este documento es el procedimiento completo. Las instrucciones internas de `laboratorios/2026-11-21_armonicos_granularidad/integracion/` quedan como registro de ese laboratorio; la incorporación se hace con este documento.

## 1. Ubicación

Crear en el repositorio español la carpeta `2026-11-21_nucleo_herencia_granularidad_recierre/` y copiar dentro **el contenido completo del ZIP**:

- `README.md`, `MANIFIESTO_SHA256.txt`, `RESULTADOS_VERIFICACION_3_5.txt`
- `documentos/` (manuscrito íntegro en español e inglés, cada uno en Markdown y PDF; el DOCX de trabajo se sustituyó por PDF)
- `anexos/`
- `laboratorios/` (incluye `2026-11-21_armonicos_granularidad/` y `2026-11-21_RA01_semilla_mobius/`)
- `scripts/`
- `fuentes/`
- `integracion/`

El índice en inglés enlaza el manuscrito completo traducido; los anexos y laboratorios conservan su edición española.

## 2. Pasos

1. Abrir una rama nueva: `release/v3.5-nucleo-herencia-recierre`.
2. Descomprimir el ZIP en la carpeta indicada, conservando la estructura.
3. Desde la carpeta incorporada, ejecutar:

   ```bash
   python3 scripts/verificar_todo.py
   sha256sum -c MANIFIESTO_SHA256.txt
   (cd laboratorios/2026-11-21_armonicos_granularidad && sha256sum -c MANIFIESTO_SHA256.txt)
   ```

   Resultado esperado: `RESULTADO: VERIFICACIÓN CONJUNTA 3.5 SATISFACTORIA` y ambos manifiestos `OK` (**36/36 principal; 5/5 armónico**). En Windows, ejecutar `py -3 scripts/verificar_todo.py`; la validación editorial usa `encoding="utf-8"` y verifica automáticamente los cinco hashes internos. El laboratorio S–RA–01 requiere `numpy` (unos 15 s); sin `numpy`, el script lo informa y ejecuta los controles exactos.
4. Incorporar al índice principal la sección de `integracion/INSERCION_README.md`, ajustando la ruta relativa.
5. Registrar la entrada de publicación 3.5 en `integracion/REGISTRO_CAMBIOS.md`.
6. Comprobar que los seis documentos de `fuentes/` se mantienen íntegros como archivos históricos. Para lectura vigente, enlazar el compendio **revisado en PR #11** y R–03 v0.4 **en PR #9**; ambos PR estaban en borrador en el momento de esta revisión. No tratar la copia anterior de `fuentes/` como edición actual del PR #11.
7. Después de revisar y fusionar el PR, preparar una publicación de GitHub con título `Versión 3.5 — Herencia, granularidad y recierre` y etiqueta propuesta `v3.5` **solo si la etiqueta está disponible**; usar `integracion/NOTAS_PUBLICACION_3_5.md` como descripción. No reemplazar versiones existentes.

## 3. Revisión del PR

- Las pruebas de proyecciones y el criterio de suma divergente se describen como implicaciones demostradas bajo certificados explícitos.
- Las ganancias aritméticas en todas las escalas se presentan como condiciones a acreditar.
- Solo las ganancias óptimas exactas admiten la equivalencia de suma divergente; para semillas explícitas, la divergencia certificada es suficiente.
- La regularidad cercana a `1/(j+1)` es descriptiva del intervalo medido; los datos `numpy` no sustituyen cotas certificadas.
- Los valores del laboratorio S–RA–01 se describen como mediciones reproducibles en doble precisión.

## 4. Trazabilidad

- **Síntesis nueva:** presentación unificada de R1–R6, T1 y RA–01, con pruebas condensadas y contratos de aplicación.
- **Demostraciones recuperadas:** cancelación de saltos, O40, O58, criba/Möbius, balances de proyección, energía periódica, Teorema 4 de CR–6.
- **Controles exactos:** recuento 621/403, ejemplo 1030, controles racionales, laboratorio A–G–01.
- **Medición reproducible:** laboratorio S–RA–01 (errores óptimos hasta 2048, ganancias por octava y semilla de Möbius).

## 5. Commit y PR

**Commit:** `docs: consolida herencia, granularidad, recierre y RA-01 con laboratorio S-RA-01`

**Título del PR:** `Versión 3.5 — Núcleo persistente, herencia, recierre y recuperación acumulada`

**Resumen del PR:**

> Se incorpora una síntesis matemática de los mecanismos de herencia, granularidad y recierre con pruebas breves; el anexo RA–01 de recuperación acumulada por semillas (Teorema 4 de CR–6 aplicado a la cadena diádica, con distinción exacto/suficiente y contraejemplo); el laboratorio A–G–01 de armónicos y granularidad; y el laboratorio S–RA–01, que mide la semilla de Möbius por octavas y reproduce el registro numérico 1024→2048. Se preserva la procedencia de los manuscritos y se incluye un índice para su consulta.


## Actualidad documental antes de fusionar

- [PR #11 — Compendio CME–RH revisado](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/11): contiene revisiones posteriores a la copia histórica guardada en `fuentes/`. El PR estaba en borrador durante esta preparación; enlazar su versión revisada, comprobar las diferencias antes de fusionar y mantener la copia anterior solo como procedencia.
- [PR #9 — R–03 v0.4 y laboratorio Gram](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/9): fuente de la edición R–03 v0.4 en borrador. Distinguirla de la versión R–03 v0.3 presente en `main`.
- [Guía de ecuaciones Markdown de GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions): los documentos nuevos usan `$...$` y `$$...$$` sin barras duplicadas.

**Firma pública:** Le Matt Ansatz Di Ego  
**Identificación documental:** Endless Monkey Project / Relational Geometry Program
