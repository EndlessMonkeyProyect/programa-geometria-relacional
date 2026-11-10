# ¿Qué cálculo deja de hacerse?

**Endless Monkey Project**  
*Relational Geometry Program*  
10 de noviembre de 2026 · manuscrito para revisión independiente · versión 0.3 · [English](README.en.md)

Cuando una parte de la incertidumbre ya está resuelta por relaciones heredadas, reconocerla ahorra cálculo, y reconocerla también cuesta. El manuscrito sigue esa cuenta en la caja de espejos: el tetraedro y la comparación sin dirección, el cierre que se reconoce antes de cerrarse, el conteo exacto cuando los reflejos están dados y el costo de reconocerlos cuando llegan escondidos en compuertas. Las mediciones comparan el reconocimiento con un DPLL que enumera y con la eliminación de variables sobre la fórmula tal como llega, hasta 256 variables primarias.

Es la continuación de [«¿Dónde se ahorra el cálculo?»](../2026-11-08_economia_del_calculo) (8 de noviembre de 2026).

## Contenido

- [`PAPER_ES.md`](PAPER_ES.md) y [`PAPER_ES.pdf`](PAPER_ES.pdf): artículo en español.
- [`PAPER_EN.md`](PAPER_EN.md) y [`PAPER_EN.pdf`](PAPER_EN.pdf): artículo en inglés.
- [`ANEXO_EVIDENCIAS.md`](ANEXO_EVIDENCIAS.md): contenido de cada carpeta, cómo reproducir y registro de reproducción.
- [`experimentos/`](experimentos/): verificador autónomo, dos laboratorios, línea base genérica y sus resultados.
- [`SHA256SUMS.txt`](SHA256SUMS.txt): sumas de todos los archivos.

## Verificación inmediata

```bash
python3 -I experimentos/verificar_reconstruccion_y_convergencia.py
```

Sin dependencias. Los laboratorios usan NumPy; las instrucciones están en `ANEXO_EVIDENCIAS.md`.
