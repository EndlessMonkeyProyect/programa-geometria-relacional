# Code and controls / Código y controles

**Public author / Autor público:** Le Matt Ansatz Di Ego

**Source edition / Edición fuente:** [What Computation Becomes Unnecessary? / ¿Qué cálculo deja de hacerse?, v0.3](../../2026-11-10_que_calculo_deja_de_hacerse/README.en.md), November 10, 2026.

The review request examines the source edition's stated theorem, recognizer, and measurements. Its [reproduction record](../../2026-11-10_que_calculo_deja_de_hacerse/EVIDENCE.en.md) gives the requirements, commands, and test scope. The [Spanish evidence note](../../2026-11-10_que_calculo_deja_de_hacerse/ANEXO_EVIDENCIAS.md) records the same controls.

| Review item | Code | Recorded control |
|---|---|---|
| Closure and exact-counting identities | [Standalone verifier](../../2026-11-10_que_calculo_deja_de_hacerse/experimentos/verificar_reconstruccion_y_convergencia.py) | Output described in the reproduction record |
| Recognizer and circuit-family controls | [Distributed-parity laboratory](../../2026-11-10_que_calculo_deja_de_hacerse/experimentos/reconocimiento_de_paridades_distribuidas/laboratorio_relaciones_distribuidas.py) | [Laboratory results](../../2026-11-10_que_calculo_deja_de_hacerse/experimentos/reconocimiento_de_paridades_distribuidas/RESULTADOS_RELACIONES_DISTRIBUIDAS.json) |
| Generic exact-count baseline | [Variable elimination](../../2026-11-10_que_calculo_deja_de_hacerse/experimentos/linea_base_generica/eliminacion_generica.py) | [Comparison and scaling](../../2026-11-10_que_calculo_deja_de_hacerse/experimentos/linea_base_generica/RESULTADOS_COMPARACION.json) |
| Recognizer comparison and DIMACS export | [Comparison script](../../2026-11-10_que_calculo_deja_de_hacerse/experimentos/linea_base_generica/comparacion_y_escala.py) | [Comparison and scaling](../../2026-11-10_que_calculo_deja_de_hacerse/experimentos/linea_base_generica/RESULTADOS_COMPARACION.json) |
| Contract mutations | [Adversarial test](../../2026-11-10_que_calculo_deja_de_hacerse/experimentos/linea_base_generica/prueba_adversarial.py) | [Adversarial results](../../2026-11-10_que_calculo_deja_de_hacerse/experimentos/linea_base_generica/RESULTADOS_ADVERSARIAL.json) |

From the source edition's root, run the dependency-free first check with:

```bash
python3 -I experimentos/verificar_reconstruccion_y_convergencia.py
```

The comparison and contract tests use NumPy; NetworkX adds an optional width estimate. The source edition includes a [SHA-256 manifest](../../2026-11-10_que_calculo_deja_de_hacerse/SHA256SUMS.txt). Recorded times describe the stated implementations and measurement environment; reproduce them with a documented machine and software stack.

The Zenodo archive for this review contains a snapshot of the source edition, including these scripts, recorded controls, and the bilingual request.
