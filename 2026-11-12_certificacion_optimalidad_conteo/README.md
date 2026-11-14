# Certificación de optimalidad local en conteo exacto — 12 de noviembre de 2026

**Endless Monkey Project**  
*Relational Geometry Program*

**Autor:** Le Matt Ansatz Di Ego.

**Estado:** propuesta académica, versión 2.0. Resultados locales demostrados; la composición en un certificado global es la pregunta de investigación.

## Contenido

- [`CERTIFICACION_OPTIMALIDAD_CONTEO_EXACTO.md`](CERTIFICACION_OPTIMALIDAD_CONTEO_EXACTO.md): contrato de economía mínima (cota superior por construcción, cota inferior para toda la clase). Incluye dos certificados locales aplicados a los algoritmos de conteo de Anthropic y OpenAI: $`q^2`$ frente a $`1`$ términos separables en los dos cortes del tensor de cruce, y $`d+1`$ datos de Hermite para recuperar $`H(0)`$. Añade un criterio de núcleo para familias polinómicas estructuradas.
- `verificar_certificacion.py`: comprobaciones racionales exactas, solo biblioteca estándar.

## Reproducción

```bash
python3 verificar_certificacion.py
```

Última línea esperada: `TODAS LAS COMPROBACIONES PASARON.`

Esta versión reúne y sustituye a *¿Dónde está el mínimo?* v1.0 y a su nota para revisores v1.1, ambas del 12 de noviembre.
