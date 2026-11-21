# Paquete aditivo para la nueva versión · 21-XI-2026 · versión 3.5

**Núcleo persistente, herencia, granularidad y recierre.**

**Identificador de publicación:** versión 3.5 · etiqueta propuesta `v3.5` · manuscrito completo en español e inglés.

Este paquete reúne una síntesis de resultados formales, el anexo RA–01 de recuperación acumulada, dos laboratorios reproducibles, seis fuentes de procedencia y la guía de incorporación al repositorio. Cada resultado se presenta con su objeto, su prueba o medición y su contrato.

## Punto de entrada

- `documentos/NUCLEO_HERENCIA_GRANULARIDAD_RECIERRE_2026-11-21.md` — fuente editorial canónica, con pruebas y trazabilidad.
- `documentos/NUCLEO_HERENCIA_GRANULARIDAD_RECIERRE_2026-11-21.pdf` — manuscrito completo de lectura, generado desde el `.md` y revisado página por página.
- [Manuscrito completo en inglés](documentos/PERSISTENT_CORE_INHERITANCE_GRANULARITY_RECLOSURE_2026-11-21_EN.md) ([PDF](documentos/PERSISTENT_CORE_INHERITANCE_GRANULARITY_RECLOSURE_2026-11-21_EN.pdf)) — traducción íntegra con las mismas hipótesis, ecuaciones y alcances. [Guía en inglés](README.en.md).
- `anexos/RA-01_recuperacion_acumulada/` — proposición de recuperación acumulada por semillas, con demostración.
- `laboratorios/2026-11-21_armonicos_granularidad/` — laboratorio A–G–01: armónicos, granularidad y cierre por celdas (aritmética exacta).
- `laboratorios/2026-11-21_RA01_semilla_mobius/` — laboratorio S–RA–01: semilla de Möbius por octavas y reproducción del registro 1024→2048 (requiere `numpy`).
- `fuentes/` — seis documentos históricos de procedencia, conservados sin alteraciones; el compendio revisado está en PR #11 y R–03 v0.4 en PR #9.
- `integracion/` — instrucciones para el administrador del repositorio, sección para el índice, registro de cambios y `NOTA_AUDITORIA_RA01_3_5.md`.
- `MANIFIESTO_SHA256.txt` — comprobación de integridad de los archivos del paquete.

## Comprobación

Desde la raíz del paquete:

```bash
python3 scripts/verificar_todo.py
sha256sum -c MANIFIESTO_SHA256.txt
(cd laboratorios/2026-11-21_armonicos_granularidad && sha256sum -c MANIFIESTO_SHA256.txt)
```

Resultado esperado: `RESULTADO: VERIFICACIÓN CONJUNTA 3.5 SATISFACTORIA` y todos los archivos `OK` en ambos manifiestos. El verificador editorial comprueba automáticamente el manifiesto del laboratorio armónico, también en Windows. En Windows: `py -3 scripts/verificar_todo.py`. Los archivos se leen con UTF-8 explícito; las salidas de los verificadores usan etiquetas compatibles con la consola Windows sin activar UTF-8. También se probó el recorrido completo simulando `cp1252:strict` (sin afirmar una prueba presencial en Windows). La salida completa está en `RESULTADOS_VERIFICACION_3_5.txt`.

## Mapa de resultados

| Nivel | Resultado | Estado |
|---|---|---|
| Herencia | Valor racional preservado bajo normalizador (R1) | Identidad |
| Granularidad | `1/N²` de O58 (R2) | Identidad y límite algebraico |
| Recierre | `J_N(n)=-mu(n)`, `J_2N(n)=0` (R3) | Identidad para todo `N≥1` y `N<n≤2N` |
| Laboratorio | 621 focos activos / 403 saltos nulos | Conteo finito exacto |
| Recuperación | Balance de proyecciones y reflexión (R4) | Identidad en espacios anidados |
| Reconstrucción | Tres ventanas (R5) y energía periódica (R6) | Desigualdad e identidad exactas |
| Transferencia | Criterio por aproximantes (T1) | Implicación con hipótesis explícitas |
| Acumulación | RA–01: suma divergente de ganancias por semilla | Suficiente por semilla; equivalencia solo con ganancias óptimas |
| Semilla | Capa de Möbius por octavas (S–RA–01) | proporciones medidas en octavas finitas; medición reproducible en doble precisión |
| Armónicos | `Δ_n=R0/[n(n+1)]`, `Q_K(R_n)=0` para `n>K²` (A–G–01) | Identidades exactas |

## Publicación 3.5 — integración auditada de RA–01

- RA–01 se presenta como el Teorema 4 de CR–6 aplicado a la cadena diádica, con la cota por semilla, y con el tamaño del certificado: crecimiento a lo sumo logarítmico de la suma de ganancias relativas, sin imponer una tasa fija por octava.
- Nuevo laboratorio S–RA–01: mide la semilla de Möbius y reproduce el registro numérico 1024→2048.
- Referencias internas corregidas; etiquetas de estado ajustadas a lo que cada resultado es.
- Instrucciones de integración unificadas en un solo procedimiento y un solo comando de verificación.
- Se separa el criterio exacto de ganancias óptimas del criterio suficiente por semillas. Se incorpora un contraejemplo racional de necesidad y se limita la lectura de la pauta `1/(j+1)` a las escalas medidas.


## Actualidad documental antes de fusionar

- [PR #11 — Compendio CME–RH revisado](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/11): contiene revisiones posteriores a la copia histórica guardada en `fuentes/`. El PR estaba en borrador durante esta preparación; enlazar su versión revisada, comprobar las diferencias antes de fusionar y mantener la copia anterior solo como procedencia.
- [PR #9 — R–03 v0.4 y laboratorio Gram](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/9): fuente de la edición R–03 v0.4 en borrador. Distinguirla de la versión R–03 v0.3 presente en `main`.
- [Guía de ecuaciones Markdown de GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions): los documentos nuevos usan `$...$` y `$$...$$` sin barras duplicadas.

**Le Matt Ansatz Di Ego**  
Endless Monkey Project / Relational Geometry Program
