# Programa de Geometría Relacional

[Read this repository in English](README.en.md).

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
