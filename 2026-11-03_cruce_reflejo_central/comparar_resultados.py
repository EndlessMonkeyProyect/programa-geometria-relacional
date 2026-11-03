#!/usr/bin/env python3
"""Compara los JSON regenerados con los de referencia.

Enteros, booleanos y textos: igualdad exacta. Decimales: tolerancia relativa 1e-9.
Uso: python3 comparar_resultados.py referencia_resultados resultados
"""
import json
import math
import sys
from pathlib import Path

RTOL = 1e-9


def iguales(a, b, ruta, errores):
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a) != set(b):
            errores.append(f"{ruta}: claves distintas {sorted(set(a) ^ set(b))}")
            return
        for k in a:
            iguales(a[k], b[k], f"{ruta}.{k}", errores)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            errores.append(f"{ruta}: longitudes {len(a)} y {len(b)}")
            return
        for i, (x, y) in enumerate(zip(a, b)):
            iguales(x, y, f"{ruta}[{i}]", errores)
    elif isinstance(a, float) or isinstance(b, float):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))
                and math.isclose(a, b, rel_tol=RTOL, abs_tol=RTOL)):
            errores.append(f"{ruta}: {a} frente a {b}")
    elif a != b:
        errores.append(f"{ruta}: {a!r} frente a {b!r}")


def main():
    ref, nuevo = Path(sys.argv[1]), Path(sys.argv[2])
    total = 0
    for f in sorted(ref.glob("*.json")):
        errores = []
        g = nuevo / f.name
        if not g.exists():
            errores.append("falta el archivo regenerado")
        else:
            iguales(json.loads(f.read_text(encoding="utf-8")),
                    json.loads(g.read_text(encoding="utf-8")), f.stem, errores)
        print(("OK    " if not errores else "FALLA ") + f.name)
        for e in errores[:10]:
            print("      " + e)
        total += len(errores)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
