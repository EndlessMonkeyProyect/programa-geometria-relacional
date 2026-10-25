# O72 — Tetraedro → anillo coplanar

Suplemento autónomo del Programa de Geometría Relacional (21-10-2026), secuencia ontología → lenguaje/narrativa → matemática → contraste con el flujo.

**Hallazgo:** para cuatro giros sujetos a coincidencia tangencial ideal de engranaje exterior, el grafo completo del tetraedro `K4` tiene núcleo de giro trivial, mientras el anillo de cuatro enlaces `C4` deja un modo alternado de dimensión 1. Otra dimensión de flexión aparece en la geometría de barras del anillo. La mera proyección plana del tetraedro no quita sus diagonales: seleccionar cuatro enlaces es una operación adicional.

**Espejos:** el modo alternado se anula al promediar rotaciones de cuarto de vuelta. El sector correspondiente puede contribuir al común por interacciones cuadráticas; pero invertirlo solo equivale a una rotación, y no genera una diferencia en el futuro del común. Esto corrige cualquier extrapolación mecánica excesiva de O70–O71.

**Límite:** la condición de engrane no impide que el cuadrilátero pierda área ni demuestra que un anillo vorticial físico tenga cuatro cápsulas mínimas, que la circulación se conserve exactamente en Navier–Stokes viscoso o que exista regularidad global.

## Uso

```bash
python codigo/verificar_o72.py
python codigo/ensayo_ns_sector.py
```

Ver `O72_FORMALIZACION.es.md` para demostraciones, ecuaciones, límites y referencias.
