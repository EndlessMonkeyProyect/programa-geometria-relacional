# Entrega del programa · 12 y 13 de noviembre de 2026

[English overview](README_ENTREGA_2026-11-12_13.en.md) · [Derechos de esta entrega](RIGHTS_ENTREGA_2026-11-12_13.md)

**Autor:** Le Matt Ansatz Di Ego  
**Programa:** Endless Monkey Project · Relational Geometry Program  
**Publicación de esta edición:** 14 de noviembre de 2026

Esta entrega reúne siete trabajos con funciones distintas dentro del programa. Los manuscritos conservan sus estados editoriales; cada verificador comprueba las identidades y ejemplos que declara su propio texto.

| Trabajo | Contenido | Estado |
| --- | --- | --- |
| [De la indefinición al cierre de la información](2026-11-12_de_la_indefinicion_al_cierre/README.md) | Sintetiza el hilo conceptual del programa y formula suficiencia de firmas, actualización reducida e información suplementaria mínima. | Borrador público de síntesis v0.1 |
| [¿Cómo se cuantifica la información de un sistema?](2026-11-12_como_se_cuantifica_la_informacion/README.md) | Distingue medidas de posibilidades, reconstrucción de relaciones, conservación y costo; prueba dos resultados sobre grafos y reproduce laboratorios finitos. | Borrador público de formalización v1.0 |
| [Certificación de optimalidad local en conteo exacto](2026-11-12_certificacion_optimalidad_conteo/README.md) | Define un contrato de costo mínimo y demuestra cotas locales para cortes tensoriales y recuperación por Hermite. | Propuesta académica v2.0 |
| [Puente entre tres representaciones](2026-11-12_puente_tres_representaciones/README.md) | Construye una firma booleana común y recupera 27 consultas de fijación parcial por dos representaciones algebraicas exactas. | Extensión técnica v0.3 |
| [Diferencias entre soluciones](2026-11-13_diferencias_entre_soluciones/README.md) | Relaciona momentos, conservación de respuestas y costo mediante tres ensayos reproducibles de contracción, continuaciones, cortes y Hermite. | Borrador público para revisión independiente |
| [Cuatro referencias y un teseracto](2026-11-13_cuatro_referencias_teseracto/README_PUBLICACION.md) | Describe el hipercubo de 16 estados, sus clases de paridad, la firma por pares y un cociente de la órbita de cuatro espejos. | Publicación técnica v1.1 |
| [Primos, reflexión y Goldbach](2026-11-13_primos_reflexion_goldbach/README.md) | Presenta identidades modulares y analíticas, controles finitos y condiciones explícitas para conectar la representación con un operador espectral externo. | Nota de formalización v3.0 |

## Relación con la nota de medición

[*Medición de soluciones respecto de un eje* v0.2](https://doi.org/10.5281/zenodo.24213729) es la nota base de *Diferencias entre soluciones*. Se enlaza a su versión revisada, con [texto y código en GitHub](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/2026-11-13-medicion-soluciones-eje-v0.2/2026-11-13_medicion_soluciones_desde_un_eje), y se conserva una sola copia.

## Verificación de esta edición

Se ejecutaron los ocho verificadores incluidos en estas siete carpetas con Python 3.12.3; el puente de tres representaciones utilizó SymPy 1.14.0. Todos terminaron sin error. Sus comprobaciones son finitas o locales según cada manuscrito y se pueden repetir con las instrucciones de cada carpeta. Los archivos `resultados*.json` y `resultados*.csv` se generan al ejecutar los ensayos y quedan fuera del repositorio.

Las referencias a los preprints de Anthropic y OpenAI se usan para las operaciones locales especificadas por cada texto. La nota de Goldbach distingue sus identidades propias de las hipótesis del artículo de Li–Liu. Los manuscritos identifican por separado pruebas, cálculos finitos y preguntas abiertas.
