# ¿Cómo se cuantifica la información de un sistema? — 12 de noviembre de 2026

**Endless Monkey Project**  
*Relational Geometry Program*

**Autor:** Le Matt Ansatz Di Ego.

**Estado:** borrador público de formalización, versión de trabajo 1.0.

## Contenido

- [`COMO_SE_CUANTIFICA_LA_INFORMACION.md`](COMO_SE_CUANTIFICA_LA_INFORMACION.md): formalización integrada. Separa cuatro preguntas: contar distinciones, reconstruir relaciones, conservar respuestas y comparar recursos. Laboratorios: cuadrado y tetraedro bajo paridad, ley escalar, cinco de ocho estados, economía del tetraedro con dos modelos de costo, E9 y paridad con cláusulas OR.
- `verificar_cuantificacion.py`: comprobaciones exactas, solo biblioteca estándar.

## Reproducción

```bash
python3 verificar_cuantificacion.py
```

Última línea esperada: `TODAS LAS COMPROBACIONES PASARON.` Comprueba:

- C₄ y K₄: 8 patrones y derivaciones.
- Teorema 1 ($`2^{n-c}`$ patrones) en los 1.099 grafos etiquetados de 1 a 5 vértices.
- Teorema 2 (componentes bipartitas) en los mismos grafos.
- Cinco de ocho estados: 14 planos y 336 / 1.344 continuaciones.
- Costos de los modelos A y B con respuestas idénticas.
- Inclusión–exclusión para paridad con cláusulas OR frente a enumeración.

Los resultados de E9 y de la rejilla de ancho diez se citan desde el informe del 8 de noviembre y se reproducen con sus propios scripts.
