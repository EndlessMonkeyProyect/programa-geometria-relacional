# Evidence and reproduction

**Endless Monkey Project**  
*Relational Geometry Program*  
November 10, 2026 · version 0.3

## What each folder holds

| Path | Content | Paper section |
|---|---|---|
| `experimentos/verificar_reconstruccion_y_convergencia.py` | Theorems 1 to 4 at small sizes, no dependencies | §3–§6 |
| `experimentos/intercambio_y_convergencia/` | Controls C1–C8 and their results file | §8, §10 |
| `experimentos/reconocimiento_de_paridades_distribuidas/` | Formula generator, gate recognizer, counter, DPLL and their results file | §9 |
| `experimentos/linea_base_generica/` | Variable elimination without recognition, comparison and scaling, contract test, with their results | §9 |

## Requirements

Python 3.10 or later. NumPy for the laboratories. NetworkX is optional: it only adds a second elimination ordering to the comparison.

## How to reproduce

From the root of this folder:

```bash
python3 -I experimentos/verificar_reconstruccion_y_convergencia.py
python3 -I experimentos/linea_base_generica/eliminacion_generica.py
python3 -I experimentos/linea_base_generica/comparacion_y_escala.py --salida comparison.json
python3 -I experimentos/linea_base_generica/prueba_adversarial.py --salida adversarial.json
python3 -I experimentos/linea_base_generica/comparacion_y_escala.py --dimacs instances/
```

The last command writes the 23 formulas of §9 in DIMACS format, each with its expected count in the header, to be tried with any dedicated counter.

The two laboratories write their results file to a fixed path; run them on a copy to keep the files in this folder:

```bash
cp -r experimentos /tmp/copy && cd /tmp/copy
python3 -I reconocimiento_de_paridades_distribuidas/laboratorio_relaciones_distribuidas.py
python3 -I intercambio_y_convergencia/laboratorio_convergencia.py          # C1–C8, about two minutes
python3 -I intercambio_y_convergencia/laboratorio_convergencia.py C6 C7    # single controls
```

`laboratorio_relaciones_distribuidas.py` writes next to itself; `laboratorio_convergencia.py`, to the current directory.

## Reproduction record

Environment: Python 3.13.18, NumPy 2.5.3, NetworkX 3.7, Linux x86_64. Date: November 10, 2026.

| Component | Result |
|---|---|
| Standalone verifier | 16 configurations → 8 patterns; 56 five-state sets; 336 paths, 336 closures and 1,344 retractions; 56 local triples; 175 random counts equal to brute force |
| Full C1–C8 (133 s) | Matches `resultados_convergencia.json` in every non-timing field |
| Distributed-parity laboratory | 11 main and 8 long-connection controls, 144 truth tables, 30 random formulas and 2 out-of-contract controls: matches `RESULTADOS_RELACIONES_DISTRIBUIDAS.json` in every non-timing field |
| Generic elimination | 300 random formulas equal to brute force |
| Comparison and scaling | 23 formulas; all completed counts agree across routes; `RESULTADOS_COMPARACION.json` |
| Contract test | 5,889 formulas: 4,444 rejected, 1,445 accepted with the same count as generic elimination; `RESULTADOS_ADVERSARIAL.json` |

`RESULTADOS_RELACIONES_DISTRIBUIDAS.json` and `resultados_convergencia.json` are the files of the November 9 campaign. The current recognizer explicitly rejects parity inputs outside the family; with it, the laboratory reproduces those files in every non-timing field.

Timings depend on hardware and load. Those in §9 come from a single run of `comparacion_y_escala.py`, with the same protocol for every route; those in §8, from the C1–C8 results file.

## Historical names

Code files keep earlier identifiers for traceability. The paper uses the name of the mechanism.

| Identifier | Name in the paper |
|---|---|
| GR3 | Rebuilding the six comparisons of the tetrahedron |
| ROSI | Recognizing before closing: closure with one pending state |
| CAG | Counting with given reflections |
| C1–C2 | Swap decomposition and ranks |
| C3–C4 | Crossing operator in the two October preprints |
| C5 | Uniqueness of the reference and its construction |
| C6 | Recognizing before closing, exhaustive walk |
| C7 | Counting with parity equations and disjunctive clauses |
| C8 | Interpolation window and reconstruction cost |
