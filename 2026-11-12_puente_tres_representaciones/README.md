# ¿Qué información puede recuperarse entre tres representaciones? — 12 de noviembre de 2026

**Endless Monkey Project**  
*Relational Geometry Program*

**Autor:** Le Matt Ansatz Di Ego.

**Estado:** extensión técnica v0.3.

## Contenido

- [`PUENTE_EXACTO_ENTRE_TRES_REPRESENTACIONES.md`](PUENTE_EXACTO_ENTRE_TRES_REPRESENTACIONES.md): firma canónica de una fórmula y familia de consultas de fijación parcial. La misma firma se representa de dos formas exactas: por intercambio de índices ($`\mathrm{SWAP}=I-2P_-`$, Anthropic) y por deformación de Cauchy con interpolación en trece nodos (OpenAI). Las 27 consultas de tres variables se recuperan por ambas rutas. Incluye la generalización a $`n`$ variables y su costo extensional.
- `verificar_puente.py`: comprobación exacta con SymPy.

## Reproducción

```bash
pip install sympy
python3 verificar_puente.py
```

Genera `resultados_puente.json` junto al script.
