# Measuring solutions relative to an axis

**Mathematical research note v0.2 · November 13, 2026**  
**Public author:** Le Matt Ansatz Di Ego  
**Program:** Endless Monkey Project · Relational Geometry Program

This delivery studies distributions of solutions projected onto a line of values. It obtains moments of real polynomial roots from coefficients, recovers the first three moments of Boolean solutions through restricted counts, and uses Hankel rank to certify the minimum number of positions in a positive atomic distribution. The paper includes two pairs of checked examples and a research agenda for query cost and reuse.

## Read

- [Full English manuscript](MEASURING_SOLUTIONS_RELATIVE_TO_AN_AXIS.en.md) · [PDF](MEASURING_SOLUTIONS_RELATIVE_TO_AN_AXIS.en.pdf)
- [Spanish reference manuscript](MEDICION_SOLUCIONES_DESDE_UN_EJE.md) · [PDF](MEDICION_SOLUCIONES_DESDE_UN_EJE.pdf)

The Spanish manuscript is the reference for mathematical notation and claims.

## Verify

With Python 3.12 and the dependency declared in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
python verificar_eje.py
```

A successful run prints `TODAS LAS PRUEBAS EXACTAS: OK` after checking moments, Sturm interval counts, restricted counts, dispersion, and Hankel ranks. [Reference results](RESULTADOS_VERIFICACION.txt).

## Rights

[Rights statement for this delivery](RIGHTS.md). Each file retains its own terms of use.
