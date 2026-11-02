#!/usr/bin/env python3
"""Compara verificacion/resultados.json con referencia_resultados/verificacion/resultados.json,
con tolerancia y no bit a bit.

Reglas: reales con |a − b| ≤ ATOL + RTOL·|b|; enteros, booleanos, textos, claves y longitudes, exactos.
Informa además las versiones del entorno actual frente a las registradas en entorno.json.
"""
import json, math, platform, sys
from pathlib import Path
RTOL, ATOL = 1e-9, 1e-12
raiz = Path(__file__).resolve().parent

def comparar(a, b, ruta, prob):
    if isinstance(b, bool) or isinstance(a, bool):
        if a != b: prob.append(f"{ruta}: {a!r} ≠ {b!r}")
    elif isinstance(a, int) and isinstance(b, int):
        if a != b: prob.append(f"{ruta}: entero {a} ≠ {b}")
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if not math.isclose(a, b, rel_tol=RTOL, abs_tol=ATOL): prob.append(f"{ruta}: {a!r} ≠ {b!r} (rtol {RTOL}, atol {ATOL})")
    elif isinstance(a, dict) and isinstance(b, dict):
        if set(a) != set(b): prob.append(f"{ruta}: claves distintas {sorted(set(a) ^ set(b))}")
        for k in set(a) & set(b): comparar(a[k], b[k], f"{ruta}/{k}", prob)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b): prob.append(f"{ruta}: longitud {len(a)} ≠ {len(b)}"); return
        for i, (x, y) in enumerate(zip(a, b)): comparar(x, y, f"{ruta}[{i}]", prob)
    elif a != b:
        prob.append(f"{ruta}: {a!r} ≠ {b!r}")

def main():
    ref = Path(sys.argv[1]) if len(sys.argv) > 1 else raiz / "referencia_resultados"
    actual = json.loads((raiz / "verificacion/resultados.json").read_text(encoding="utf-8"))
    referencia = json.loads((ref / "verificacion/resultados.json").read_text(encoding="utf-8"))
    prob = []; comparar(actual, referencia, "verificacion", prob)
    ent = json.loads((raiz / "entorno.json").read_text(encoding="utf-8"))["generado_con"]
    print(f"   entorno actual: Python {platform.python_version()} · registrado: Python {ent['python']}")
    if prob:
        print("   DIFERENCIAS:"); [print("   - " + p) for p in prob]; sys.exit(1)
    print("   OK — todo coincide con la referencia dentro de la tolerancia")

if __name__ == "__main__":
    main()
