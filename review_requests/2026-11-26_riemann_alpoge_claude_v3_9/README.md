# Solicitud de revisión independiente · Riemann–Alpöge–Claude v3.9

**Le Matt Ansatz Di Ego** · Endless Monkey Project · Relational Geometry Program · 26 de noviembre de 2026

Esta entrega propone examinar relaciones entre referencias aritméticas sucesivas, aproximación funcional y economía de recuperación. Presenta identidades y equivalencias bajo sus hipótesis, y formula el **Problema T** sobre posibles transferencias cuantitativas entre construcciones. La edición inglesa está adaptada para revisión; acompaña al original español y no es una traducción página por página.

## Documentos

- [Solicitud de revisión en inglés](english/Independent_Review_Request_EN.md) y [nota técnica inglesa](english/Riemann_Alpoge_Claude_Independent_Review_EN_v3_9.pdf).
- [Presentación inglesa](english/Riemann_Alpoge_Claude_Review_Presentation_EN_v3_9.pdf).
- [Manuscrito original en español](original_spanish/Equivalencias_Riemann_Alpoge_Claude_v3_9.pdf) y [presentación original](original_spanish/Presentacion_Riemann_Alpoge_Claude_v3_9.pdf).
- [Fuentes LaTeX inglesas](english/) y [fuentes y verificadores originales](original_spanish/Equivalencias_v3_9_fuente_y_verificacion.zip).
- [Guía original de reproducción](README_EN.txt), [manifiesto de la entrega](SHA256SUMS.txt) y [manifiesto de publicación](MANIFIESTO_PUBLICACION_SHA256.txt).
- [Nota editorial bilingüe](NOTA_EDITORIAL_ES_EN.md) sobre la referencia [15] y la procedencia de los informes de Lean.

El archivo original conserva nueve scripts, sus informes y los materiales en español. La edición inglesa verifica la integridad de archivos y documenta resultados previos; no presenta una ejecución nueva de los nueve scripts ni una auditoría independiente de Lean. La solicitud invita a verificar fórmulas, fuentes, hipótesis y posibles estimaciones de transferencia.

En Python 3.12 con NumPy y mpmath actuales, `checks.py` necesita [una conversión explícita de `numpy.int64` a `int`](compat/checks_numpy_int.patch) antes de construir `mp.mpf`. Aplicar el parche a una **copia extraída** del ZIP español; los archivos originales y sus hashes permanecen intactos. En una consola Windows con codificación cp1252, establecer `PYTHONIOENCODING=utf-8` permite imprimir el símbolo integral del informe. Estos ajustes de ejecución no cambian las fórmulas.

**Auditoría de esta preparación:** con Python 3.12.14, NumPy 2.3.5 y mpmath 1.3.0, la copia parcheada de `checks.py` completó sus apartados (a)–(g); `vasyunin.py` y `cadena_lc.py` también terminaron correctamente. Los otros seis scripts y el desarrollo Lean no se ejecutaron en esta revisión.

Los [soportes comparativos R–03/Alpöge](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/13) y la [edición O58 v2.1](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/pull/14) están en PR separados, aún sin incorporar a `main`. Esta carpeta los cita como antecedentes, sin duplicarlos.

Sin licencia general de reutilización; se conservan los derechos correspondientes a cada archivo y a sus fuentes citadas.
