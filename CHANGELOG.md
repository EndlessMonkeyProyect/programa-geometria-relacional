# Historial de esta edición

## Imagen Total 4.0 · 2026-11-10

- Nueva edición de lectura continua del programa. Sigue el hilo acordado el 24 de octubre y reúne la 3.9 con las entregas del 27 de octubre al 10 de noviembre, con el criterio de lenguaje del programa aplicado a todo el texto y los enlaces con la literatura en una capa final.
- Integra tres notas del 10 de noviembre: cuatro cápsulas en Navier–Stokes (C4‑E1 a C4‑E3), el mecanismo de economía frente a P y NP (con una proposición condicional) y el recierre de la economía en Yang–Mills (dos plaquetas $\mathbb Z_2$ y la base de caracteres de $SU(2)$).
- Verificadores nuevos en `verificadores/`. En el de cuatro cápsulas, la prueba con deformación uniforme calcula $H_F$ desde su definición nodo por nodo, con un control de deformación variable y la comparación de la forma reindexada de la prueba.
- El README raíz enlaza el registro de reproducción vigente de *¿Qué cálculo deja de hacerse?*.

## ¿Qué cálculo deja de hacerse? v0.3 · 2026-11-10

- El hilo del artículo se escribe en el vocabulario del programa: incertidumbre, reflejo, cierre, herencia y novedad. Los términos técnicos pasan a una sección de puentes con referencias.
- Se añade una línea base genérica: eliminación de variables sobre la fórmula sin reconocimiento, medida con el mismo protocolo que las demás rutas. La familia de conexiones largas se extiende hasta 256 variables primarias, y las fórmulas se exportan en DIMACS para contadores dedicados.
- Se añade una prueba del contrato del reconocedor con 5.889 fórmulas. El reconocedor rechaza de forma explícita una entrada de paridad fuera de la familia; sus conteos no cambian.
- La tabla del §9 sale de un único archivo de resultados, las fórmulas usan delimitadores que GitHub muestra, y el artículo en inglés queda completo y con PDF.
- El registro de reproducción queda en `ANEXO_EVIDENCIAS.md` y `EVIDENCE.en.md`. Se retiran el control editorial, el registro de auditoría, el laboratorio anterior y su control antes/después.

## ¿Qué cálculo deja de hacerse? · 2026-11-10

- Se añade un manuscrito de continuación en español e inglés, PDF de lectura, dos laboratorios con resultados originales y un verificador autónomo.
- Se cotejan los 14 archivos del manifiesto recibido. El verificador autónomo y el laboratorio de relaciones distribuidas se reejecutan; este último requiere retirar el límite de ocho segundos de las repeticiones de DPLL, conservando el límite de nodos. También se reejecuta C7 del laboratorio de intercambio y convergencia.
- El expediente se presenta para revisión independiente. No afirma una cota general nueva para 3-SAT.

## Revisión del intercambio de un par · 2026-11-04

- Se abre un [hilo específico](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/4) para un dictamen humano sobre las fórmulas de rango, su correspondencia con los preprints y sus antecedentes.
- Se fijan las referencias de OpenAI y Anthropic por commit y la entrega reproducible por el commit de la etiqueta `2026-11-03-pair-swap-review`.
- Se actualizan las guías en ambos idiomas y su manifiesto SHA-256. La etiqueta y el ZIP archivados conservan su contenido original.

## Solicitud de revisión de G–01 · 2026-11-02

- Se incorporan las solicitudes de revisión de G–01 v1.3 en español e inglés, los resúmenes de una página, las invitaciones y sus manifiestos SHA-256.
- Q1–Q3 se concentran en la prueba de descenso del árbol de pares ordenados positivos, sus antecedentes y la comprobación finita hasta $N=3000$.
- Se explicita la dificultad del campo débil bajo la identificación literal $r_s/r=1-1/N^2$. El salto desde el reposo al primer nodo es de 0 a $8/9$.

## Hilo de gravedad G–01 — 2026-11-01

- Incorporación del documento G–01 v1.3 en español e inglés, en Word, PDF y Markdown, con sus figuras.
- Verificador sin dependencias para los resultados exactos y los controles calculables; las 16 ramas O58 desde (2,2,3) coinciden con el archivo de O58. Manifiesto SHA-256 del paquete.
- Revisión de la v1.2 a la v1.3 en hoja de cálculo y versiones 1.0 a 1.2 en `historial/`. El estado es OPEN; no se afirma una derivación de la gravedad.

## Solicitud de revisión del cubo de espejos y P frente a NP — 2026-10-30

- Incorporación navegable de los paquetes español e inglés, con el documento integral, resúmenes y notas técnicas.
- Reproducción de las 4.672 consultas finitas de T-EXT-01; sus resultados coinciden con los JSON archivados.
- Manifiestos SHA-256 verificados: 23 archivos del paquete español y 13 del inglés. Se solicita revisión matemática independiente; no se afirma una solución de P versus NP.

## Complemento Más allá de Yang–Mills — 2026-10-27

- Incorporación del artículo en español e inglés, en Markdown y PDF, y de siete paquetes PR-01 a PR-07.
- Revisión independiente de R-02, resultados de referencia y manifiesto SHA-256: 47 archivos verificados.
- El complemento se presenta como borrador para revisión y deja explícita la brecha de masa como problema abierto.

## Edición ordenada — 2026-10-24

- Incorporación navegable del paquete fechado: 1.047 archivos cotejados con su manifiesto SHA-256.
- Manuscrito público, suplemento de ritmo y gravedad, hilo integrado, realizaciones, ramas, laboratorios y archivo histórico.
- Guía y textos principales en inglés; la edición conceptual 0.1.0 continúa disponible.

## 0.1.0-editorial — 2026-09-29

- Preservación de 79 archivos recibidos y extracción navegable de tres miembros del ZIP.
- Síntesis y diez capítulos conceptuales.
- Glosario, notación, linaje y registro de 26 resultados.
- Separación de correcciones históricas, nueve observaciones editoriales y ocho pendientes.
- Catálogo completo y manifiesto de integridad.
- Ejemplos nuevos y verificaciones identificados como editoriales.
- Repositorio Git inicial y bundle portable.
- Traducción inglesa de los 25 documentos editoriales; las fuentes originales permanecen intactas.
- Publicación en GitHub y protección de los bytes originales en las clonaciones de Windows.

Esta numeración describe el trabajo editorial. No sustituye las versiones v0.xx ni los identificadores MF del programa.
