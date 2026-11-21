# Versión 3.5 — Herencia, granularidad y recierre

**Fecha:** 21 de noviembre de 2026  
**Identificador:** `v3.5` (propuesto; comprobar disponibilidad en el repositorio).  
**Firma pública:** Le Matt Ansatz Di Ego  
**Identificación documental:** Endless Monkey Project / Relational Geometry Program

La edición 3.5 integra la secuencia formal **referencia → herencia → granularidad → recierre → recuperación**, mediante definiciones, demostraciones de identidades y laboratorios reproducibles.

## Resultados incluidos

- Transporte racional entre normalizadores (O40) y resto algebraico decreciente en la familia O58.
- Recierre exacto por Möbius al duplicar cualquier escala entera: `J_N(n)=-μ(n)` y `J_{2N}(n)=0` para `N<n≤2N`.
- Identidades exactas de proyecciones, reflexión en Hilbert y certificado funcional de tres ventanas.
- Proposición RA–01: **criterio suficiente** de cierre global mediante la divergencia de una suma de ganancias relativas certificadas con semillas explícitas. La equivalencia necesaria y suficiente corresponde a las **ganancias óptimas exactas**, siempre que el error permanezca positivo; se conserva un contraejemplo a la necesidad para una semilla prefijada.
- Laboratorio A–G–01: resolución y coincidencia observacional de escalas armónicas para consultas declaradas.
- Laboratorio S–RA–01: mediciones finitas, reproducibles en doble precisión, de las ganancias de la semilla de Möbius por octavas. El registro 1024→2048 informa aproximadamente 59,75 % de la mejora óptima; el indicador $(j+1)d_j/e_j^2$ alcanza aproximadamente 0,437 en esa octava. La primera y segunda octava empatan con la mejor referencia individual; en las siguientes la semilla la supera. El contraste de productos internos integra por tramos y aproxima la cola; estos resultados están sujetos a certificación numérica rigurosa.

## Alcance de la publicación

La identidad de recierre de saltos y las identidades funcionales son exactas en sus contratos. Las regularidades numéricas de las octavas **no** son cotas universales. La transferencia del criterio RA–01 a toda la familia de Riemann requiere una estimación aritmética no circular, todavía abierta. No se anuncia demostración de RH ni GRH.

## Reproducción

Desde el directorio raíz del paquete:

```bash
python3 scripts/verificar_todo.py
sha256sum -c MANIFIESTO_SHA256.txt
(cd laboratorios/2026-11-21_armonicos_granularidad && sha256sum -c MANIFIESTO_SHA256.txt)
```

Los controles exactos usan la biblioteca estándar de Python. El laboratorio S–RA–01 utiliza `numpy`.

## Conservación de procedencia

Las seis fuentes documentales de `fuentes/` permanecen sin cambios de contenido y se califican como copias históricas; la versión revisada de CME–RH se enlaza al PR #11 y R–03 v0.4 al PR #9. El historial interno de preparación v3–v5 se conserva en `integracion/REGISTRO_CAMBIOS.md` y los registros de ejecución anteriores, sin confundirlo con la versión pública **3.5**.


## Actualidad documental antes de fusionar

- [PR #11 — Compendio CME–RH revisado](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/11): contiene revisiones posteriores a la copia histórica guardada en `fuentes/`. El PR estaba en borrador durante esta preparación; enlazar su versión revisada, comprobar las diferencias antes de fusionar y mantener la copia anterior solo como procedencia.
- [PR #9 — R–03 v0.4 y laboratorio Gram](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/9): fuente de la edición R–03 v0.4 en borrador. Distinguirla de la versión R–03 v0.3 presente en `main`.
- [Guía de ecuaciones Markdown de GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions): los documentos nuevos usan `$...$` y `$$...$$` sin barras duplicadas.

