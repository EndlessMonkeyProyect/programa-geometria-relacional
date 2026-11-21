## Publicación 3.5 — 21 de noviembre de 2026

Edición de publicación que consolida el núcleo de herencia, granularidad y recierre, incorpora RA–01 con el alcance corregido, el laboratorio A–G–01 de armónicos, y el laboratorio S–RA–01 con medidas numéricas de recuperación por octavas. Conserva las fuentes históricas sin modificarlas. Las etapas internas v3, v4 y v5 quedan documentadas abajo como historial de preparación, **no** como etiquetas de publicación equivalentes a 3.5.

**Demostrado:** identidades algebraicas, recuperación por proyecciones y criterio de suficiencia condicionado de RA–01. **Verificado en casos finitos:** focos de Möbius, controles racionales y aproximaciones de Gram. **Pendiente:** cotas universales que impliquen el cierre funcional global necesario para RH.

**Edición para el PR:** el manuscrito completo se incorpora en Markdown y en PDF de siete páginas, con ecuaciones compuestas y revisión visual de todas las páginas. El DOCX de preparación no se incorpora.

**Ampliación bilingüe del PR:** el manuscrito completo se traduce al inglés y se incorpora en Markdown y PDF de siete páginas. Se cotejaron las 14 ecuaciones de bloque y 131 expresiones matemáticas con la edición española. Se corrigió un escape duplicado de notación en el párrafo español sobre ganancias relativas.

## 2026-11-21 — Consolidación de núcleo, herencia, granularidad y recierre

- Se unifica la distinción fundacional entre historia y herencia, manteniendo el núcleo como referencia persistente de crecimiento.
- Se formalizan las identidades exactas de transporte de referencia (O40) y de granularidad algebraica `1/N²` (O58).
- Se presenta con prueba la identidad `J_N(n)=-μ(n)` y `J_{2N}(n)=0` para todo `N≥1` y `N<n≤2N`.
- Se añaden verificadores exactos de la transición 1024→2048: 621 focos activos y 403 saltos ya nulos.
- Se integran el balance de proyecciones de Hilbert, la energía periódica y la estimación funcional de tres ventanas.
- Se consolidan correspondencias operativas entre ROSI, CME-002, esferas, O40/O58 y el marco aritmético R–01/R–03/R–RH–01.
- Se incluyen fuentes documentales de procedencia y guía de incorporación en repositorio.

**Endless Monkey Project / Relational Geometry Program**


### Ampliación v3 — RA–01

- Se incorpora RA–01 como criterio certificado de recuperación acumulada por semillas.
- Se recupera la identidad de ganancia por proyecciones y la forma matricial de Gram/Schur.
- Se documenta la semilla de Möbius por octavas como instrumento para medir recuperación.
- Se incorporan controles aritméticos y un laboratorio de Hilbert con aritmética racional exacta.
- Se añaden verificación conjunta, índices de lectura y referencia desde el documento principal.


### Preparación interna v4

- RA–01 se identifica como el Teorema 4 de CR–6 aplicado a la cadena diádica, con la cota por semilla; se distingue el criterio necesario y suficiente para ganancias óptimas del criterio suficiente por semilla; la suma certificada crece a lo sumo logarítmicamente, sin imponer tasa por octava.
- Se incorpora el laboratorio S–RA–01: fórmula exacta de productos internos validada contra integración directa, errores óptimos hasta 2048, ganancia de cada octava y de la semilla de Möbius (51–100 % de la óptima para `j≤10`).
- El registro numérico 1024→2048 (`e²_1024=0,0066723`, `e²_2048=0,0062291`, 6,64 %) queda reproducido.
- Se corrige la referencia interna de RA–01 al contrato de tres ventanas y se ajustan las etiquetas de estado.
- Las instrucciones de integración quedan en un solo procedimiento con un solo comando de verificación.

### Preparación interna v5 — auditoría del alcance de RA–01

- Se corrige la afirmación de necesidad: la divergencia de ganancias relativas es necesaria y suficiente **para ganancias óptimas exactas** cuando el error no llega a cero en una etapa; **para una semilla fijada**, la divergencia de su certificado es solo suficiente.
- Se añade contraejemplo exacto en `ℓ²` con recuperación óptima completa y semillas nuevas no nulas de ganancia cero; se incorpora al verificador racional.
- Se limita la regularidad aproximada `1/(j+1)` a las octavas realmente calculadas, sin presentarla como cota asintótica.
- Se explicita que los registros de Gram de doble precisión no contienen cotas rigurosas de error.
- Se conservan íntegros los seis documentos de `fuentes/` y los resultados históricos.

**Endless Monkey Project / Relational Geometry Program**


## Ajuste de compatibilidad Windows — 21-XI-2026

- `verificar_ra01.py`: el texto de consola `ℓ²` se sustituyó por `l2`.
- `medir_semilla_mobius.py`: los símbolos griegos y signos no disponibles en Windows-1252 se cambiaron por nombres ASCII **solo en mensajes de consola**; cálculos intactos.
- `verificar_publicacion.py` mantiene lecturas UTF-8 explícitas.
- Se regeneró `RESULTADOS_VERIFICACION_3_5.txt` y el manifiesto principal. Se verificaron ambos manifiestos y el recorrido completo con salida simulada `cp1252:strict`.
- El `.docx` se volvió a renderizar para revisión visual; el archivo de investigación no recibió cambios de contenido.
