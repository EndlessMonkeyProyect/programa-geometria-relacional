# ¿Qué cálculo deja de hacerse?

**Endless Monkey Project**  
*Relational Geometry Program*  
10 de noviembre de 2026 · manuscrito para revisión independiente · versión 0.2

**Tema:** reconocimiento de relaciones heredadas, estructura mínima, cierre y costo total de un conteo exacto.

## Contenido

- [`PAPER_ES.md`](PAPER_ES.md): artículo completo en español.
- [`PAPER_EN.md`](PAPER_EN.md): artículo en inglés.
- [`PAPER_ES.pdf`](PAPER_ES.pdf): versión de lectura, español.
- [`ANEXO_EVIDENCIAS.md`](ANEXO_EVIDENCIAS.md): alcance, método, reproducción y significado de las denominaciones históricas.
- [`ANEXO_AUDITORIA.md`](ANEXO_AUDITORIA.md): registro de la reejecución de pruebas.
- [`experimentos/verificar_reconstruccion_y_convergencia.py`](experimentos/verificar_reconstruccion_y_convergencia.py): verificación autónoma en problemas pequeños, sin paquetes externos.
- [`experimentos/intercambio_y_convergencia/`](experimentos/intercambio_y_convergencia/): descomposición algebraica, raíz e interpolación en dos algoritmos externos, junto con resultados originales.
- [`experimentos/reconocimiento_de_paridades_distribuidas/`](experimentos/reconocimiento_de_paridades_distribuidas/): detector de compuertas, conteo exacto, datos originales y controles comparativos.

## Relación con el expediente anterior

Es **la continuación del mismo ramal de economía del cálculo**, preparada como carpeta nueva. No reemplaza la publicación del 8 de noviembre:
[¿Dónde se ahorra el cálculo?](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/tree/main/2026-11-08_economia_del_calculo).

Esta entrega integra la **economía de reconocimiento**: el costo de identificar y verificar una referencia útil antes del conteo. Las demostraciones se refieren a familias definidas; **no** se afirma un algoritmo eficiente universal para cualquier fórmula, ni superioridad sobre todas las técnicas de OpenAI, Anthropic o la literatura.

## Verificación inmediata

```bash
python3 -I experimentos/verificar_reconstruccion_y_convergencia.py
```

Para ejecutar el laboratorio de referencias ocultas hace falta NumPy; las instrucciones están en `ANEXO_EVIDENCIAS.md`.

## Publicación y revisión

Esta carpeta se incorpora a `EndlessMonkeyProyect/programa-geometria-relacional` como manuscrito para revisión independiente. No altera material anterior. El registro de reproducción de esta publicación figura en [`ANEXO_AUDITORIA.md`](ANEXO_AUDITORIA.md).
