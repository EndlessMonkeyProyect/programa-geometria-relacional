# Programa de Geometría Relacional

[Read this repository in English](README.en.md).

## Solicitud de revisión actual: 30 de octubre de 2026

La [solicitud de revisión independiente sobre el cubo de espejos y P frente a NP](review_requests/2026-10-30_mirror_cube_p_vs_np_es/LEER_PRIMERO.md) reúne el documento integral, el resumen ejecutivo, la nota técnica T-EXT-01 y sus antecedentes. La [edición inglesa](review_requests/2026-10-30_mirror_cube_p_vs_np/README.md) ofrece el texto completo y un resumen en inglés. T-EXT-01 establece una cota informacional cuadrática para una familia delimitada de consultas de 3-coloración; no demuestra P = NP ni P ≠ NP.

## Complemento anterior: 27 de octubre de 2026

El [complemento «Más allá de Yang–Mills»](2026-10-27_mas_alla_de_yang_mills/LEER_PRIMERO.md) añade un [artículo en español](2026-10-27_mas_alla_de_yang_mills/articulo/Mas_alla_de_Yang_Mills_2026-10-27.md), su [traducción inglesa](2026-10-27_mas_alla_de_yang_mills/articulo/Beyond_Yang_Mills_2026-10-27_EN.md) y siete paquetes de comprobación PR-01 a PR-07, además de una revisión independiente de R-02. El artículo es un borrador para revisión; no afirma resolver la brecha de masa de Yang–Mills.

## Edición base: 24 de octubre de 2026

La [edición ordenada](2026-10-24/00_LEER_PRIMERO.md) reúne el hilo integrado, las realizaciones, las tres ramas de investigación, laboratorios y archivo histórico. El [manuscrito público](2026-10-24/00_PUBLICACION/Programa_Geometria_Relacional_Manuscrito_Publico_2026-10-24.md) y el [suplemento sobre ritmo, tiempo y gravedad](2026-10-24/01_HILO/SUPLEMENTOS/Suplemento_Ritmo_Ciclo_Base_Tiempo_y_Gravedad_2026-10-24.md) forman parte del paquete.

La [guía en inglés](2026-10-24/00_READ_FIRST.en.md) enlaza las traducciones principales. El manifiesto de esta edición verifica 1.047 archivos; el ZIP original se conserva como archivo de distribución.

## Edición conceptual anterior: 0.1.0

**Edición conceptual 0.1.0 · 29 de septiembre de 2026**  
**Autor del programa en las fuentes:** Le Matt Ansatz Di Ego  
**Organización y revisión editorial:** elaboradas con asistencia de IA a partir de los archivos aportados.

El programa investiga cómo una estructura de comparaciones hace distinguibles ciertas diferencias, cómo un cierre conserva una frontera suficiente y cómo las relaciones entre cierres pueden exigir nuevas referencias. Explora realizaciones algebraicas, dinámicas y computacionales de esa idea.

Este repositorio reúne el desarrollo recibido en una lectura conceptual, conserva íntegros los originales y muestra qué conexiones están demostradas, cuáles dependen de hipótesis y cuáles permanecen abiertas. No declara una solución de P versus NP ni una teoría física validada.

## Empezar por aquí

1. [Síntesis conceptual](docs/SINTESIS.md): el argumento completo en lenguaje conectado.
2. [Mapa de lectura](docs/MAPA_DE_LECTURA.md): recorrido por preguntas, con capítulos y fuentes.
3. [Resultados y dependencias](docs/trazabilidad/RESULTADOS.md): qué se puede sostener y bajo qué condiciones.
4. [Correcciones y pendientes](docs/trazabilidad/CORRECCIONES_Y_PENDIENTES.md): separa correcciones históricas de observaciones editoriales nuevas.
5. [Catálogo de fuentes](fuentes/CATALOGO.md): acceso a los 79 adjuntos preservados.

## Estructura

| Carpeta | Contenido |
|---|---|
| docs/conceptos | Diez capítulos de síntesis conceptual y formal. |
| docs/trazabilidad | Resultados, cambios históricos, pendientes y relaciones entre fuentes. |
| fuentes/originales | Los 79 adjuntos, sin modificaciones. |
| fuentes/paquetes_extraidos | Contenido navegable del ZIP recibido. |
| datos | Guía de resultados experimentales reportados y sus límites. |
| ejemplos | Comprobaciones nuevas, pequeñas y reproducibles, identificadas como editoriales. |
| herramientas | Verificación de integridad, datos y enlaces de la edición. |
| verificacion | Informe de comprobación de esta entrega. |

## Qué significa «sin perder información»

La síntesis no pretende sustituir cada ecuación o cada ensayo de los originales. La preservación se garantiza mediante copias completas, catálogo, manifiesto SHA-256 y enlaces desde la exposición conceptual. Las formulaciones incompatibles o superadas permanecen en el archivo y se señalan en la revisión.

El alcance son los archivos adjuntos disponibles en esta conversación. No se ha recuperado todo el repositorio histórico, sus conversaciones de origen ni los scripts experimentales mencionados pero no incluidos. No hay fuentes v0.71 ni v0.88 en esta entrega; no se inventan entregas faltantes. El paquete v0.91 es una entrega parcial, no una recopilación de toda la historia.

## Dos formas de usar la entrega

- Abrir README.md en [el repositorio público](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional) y seguir los enlaces con un visor Markdown.
- Clonar el repositorio público y ejecutar las comprobaciones:

~~~bash
git clone https://github.com/EndlessMonkeyProyect/programa-geometria-relacional.git
cd programa-geometria-relacional
python3 herramientas/verificar.py
python3 ejemplos/comprobaciones.py
~~~

El archivo historial.git.bundle forma parte del ZIP original de esta entrega, no del repositorio publicado. Conserva el commit inicial de esta edición y no contiene el historial histórico del autor. El contenido también puede leerse sin Git.

## Estado central

La definición contextual de información, la composición por fronteras y el cierre algebraico local disponen de resultados condicionales precisos. Sigue pendiente demostrar que la composición relacional determina el operador geométrico de una nueva cápsula y verificar su estabilidad bajo el acoplamiento propuesto.

La edición conceptual tiene su propia versión; no se renombra el programa como v0.92 ni se presenta una revisión editorial como aprobación del autor. Véanse [alcance](docs/ALCANCE_Y_CRITERIOS.md) y [cómo contribuir](CONTRIBUTING.md).
