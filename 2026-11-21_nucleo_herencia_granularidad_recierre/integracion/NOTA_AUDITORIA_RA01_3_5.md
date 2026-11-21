# Nota de auditoría matemática — RA–01 · publicación 3.5

**Fecha:** 21 de noviembre de 2026. **Tipo:** auditoría matemática de la edición de publicación 3.5 (trabajo previo: etapas internas v4 y v5).

## Corrección de alcance

El criterio $\sum_j\gamma_j=\infty$ es necesario y suficiente para cierre global **cuando** $\gamma_j=(e_j^2-e_{j+1}^2)/e_j^2$ representa la **ganancia óptima** y todos los errores $e_j$ permanecen positivos. Si alguno se anula, el cierre ocurre en ese paso.

Con semillas concretas $g_j$, el teorema RA–01 declara únicamente la suficiencia de la divergencia de $\sum_j a_j/E_j$, donde $a_j\le d_j$ y $E_j\ge e_j^2$. No se atribuye la necesidad a una semilla prefijada.

## Contraejemplo comprobable

En $\ell^2$, la secuencia $\chi=\sum_{k\ge0}2^{-(k+1)}v_{2k+1}$ y los espacios $W_j=\operatorname{span}(v_1,\ldots,v_{2j})$ cumplen $e_j^2=4^{-j}/3\to0$. No obstante, para $g_j=v_{2j+2}$ se obtiene $d_j=0$ para todo $j$. Esta distinción se comprueba también mediante aritmética racional en `scripts/verificar_ra01.py`.

## Lectura de los ensayos

Los porcentajes de ganancia de la capa de Möbius, el 59,75 % para `1024→2048` y el intervalo numérico observado, aproximadamente entre $0{,}437$ y $1{,}197$ para $(j+1)d_j/e_j^2$ corresponden a **resultados finitos en doble precisión**. No son cotas aritméticas verificadas para todas las octavas. Una cota universal previa $\gamma_{2^j}\ge1/(j+2)$ fue descartada por el registro numérico en `1024→2048`; no se restituye en la publicación 3.5.

## Método y trazabilidad

El contraste de productos internos es una integración por tramos hasta un corte finito más una cola aproximada mediante promedio periódico. La cota de Burnol se formula para $D(\lambda)$, distancia clásica de aproximación, no para la ganancia de una semilla $d_j$. Se conservan las fuentes originales y se enlazan [PR #11](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/11) y [PR #9](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/9), ambos en borrador.

## Verificación e integración

- Los resultados de `fuentes/` y los textos históricos permanecen sin editar.
- El anexo RA–01, el documento principal, el laboratorio S–RA–01 y las instrucciones de integración reflejan la corrección.
- El registro de verificación y el manifiesto SHA-256 se regeneran desde el paquete actualizado.
- Se solicita revisión independiente de las pruebas y certificación numérica por intervalos antes de presentar los valores como desigualdades rigurosas.


## Actualidad documental antes de fusionar

- [PR #11 — Compendio CME–RH revisado](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/11): contiene revisiones posteriores a la copia histórica guardada en `fuentes/`. El PR estaba en borrador durante esta preparación; enlazar su versión revisada, comprobar las diferencias antes de fusionar y mantener la copia anterior solo como procedencia.
- [PR #9 — R–03 v0.4 y laboratorio Gram](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/9): fuente de la edición R–03 v0.4 en borrador. Distinguirla de la versión R–03 v0.3 presente en `main`.
- [Guía de ecuaciones Markdown de GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions): los documentos nuevos usan `$...$` y `$$...$$` sin barras duplicadas.

**Le Matt Ansatz Di Ego**  
Endless Monkey Project / Relational Geometry Program
