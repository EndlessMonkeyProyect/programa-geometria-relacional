# O27 — perpendicularidad y suficiencia vorticial

**Estado:** suplemento sectorial, no integrado a la Imagen Total.

## Contenido

- `O27_PERPENDICULARIDAD_Y_CIERRE_VORTICIAL.es.md`: demostración, soluciones NS exactas, lenguaje del programa, falsadores y límites.
- `laboratorio_o27.py`: 19 aserciones simbólicas SymPy, independientemente verificables.
- `RESULTADOS_O27.txt`: ejecución grabada.
- `SHA256_MANIFEST.json`: checksums de los archivos del suplemento, excluyendo el propio manifiesto.
- `antecedentes/`: documentos históricos O25/O26 preservados como copias; no se modifican.

## Reproducir

```bash
python -m pip install 'sympy>=1.14'
python laboratorio_o27.py
```

La dependencia SymPy está limitada al ensayo exacto. Las identidades están demostradas analíticamente en el documento, bajo suavidad y las condiciones explícitas de NS.
