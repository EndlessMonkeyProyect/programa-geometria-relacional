# Diferencias entre soluciones: medición, conservación y costo — 13 de noviembre de 2026

**Endless Monkey Project**  
*Relational Geometry Program*

**Autor:** Le Matt Ansatz Di Ego.

**Estado:** borrador público para revisión independiente.

## Contenido

| Pieza | Qué es | Verificador |
|---|---|---|
| [`DIFERENCIAS_ENTRE_SOLUCIONES.md`](DIFERENCIAS_ENTRE_SOLUCIONES.md) | Artículo que conecta medición, conservación y costo con los tres ensayos | — |
| [Nota base revisada v0.2](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-13-medicion-soluciones-eje-v0.2/2026-11-13_medicion_soluciones_desde_un_eje/MEDICION_SOLUCIONES_DESDE_UN_EJE.md) | Momentos respecto de una referencia escalar, conteos restringidos y certificado de posiciones por rango de Hankel | [Verificador](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/blob/2026-11-13-medicion-soluciones-eje-v0.2/2026-11-13_medicion_soluciones_desde_un_eje/verificar_eje.py) (SymPy) |
| [`ensayo_A_contraccion_y_momentos/`](ensayo_A_contraccion_y_momentos/INFORME.md) | Transporte de $`(N,S,Q)`$ en $`\mathbb Z[u]/(u^3)`$; tres rutas de recuperación en ocho instancias y su costo | `ensayo_momentos.py` |
| [`ensayo_B_continuaciones_y_hermite/`](ensayo_B_continuaciones_y_hermite/INFORME.md) | Agrupación por continuaciones y recuperación por Hermite cúbico; resultado negativo de costo (6,35 a 6,52 veces) | `verificar_paralelo.py` |
| [`ensayo_C_cortes_y_hasse/`](ensayo_C_cortes_y_hasse/INFORME.md) | Identidad firmada de ocho cuadrados de Anthropic en 4.096 casos, rangos 8 y 64, recuperación con seis datos de Hasse | `verificar_transformaciones.py` |

## Reproducción

Desde cada subcarpeta de ensayo:

```bash
python3 ensayo_momentos.py            # ensayo A: genera resultados.csv y resultados.json
python3 verificar_paralelo.py         # ensayo B: genera resultados_paralelos.json
python3 verificar_transformaciones.py # ensayo C: genera resultados.json
```

Los tres ensayos usan solo la biblioteca estándar y aritmética entera exacta. La nota base v0.2 se consulta en su entrega propia, junto con su PDF, traducción inglesa y verificador.
