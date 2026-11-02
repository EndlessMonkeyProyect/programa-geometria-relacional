#!/usr/bin/env python3
"""Coteja las ramas O58 desde (2,2,3) calculadas por verificar.py con el archivo del propio O58
en la edición del 24 de octubre. Sólo funciona dentro del repositorio; fuera de él lo informa y sale sin error."""
import csv, json, sys
from pathlib import Path
aqui = Path(__file__).resolve().parent
o58 = aqui.parents[1] / "2026-10-24/05_ARCHIVO/navier_stokes_O54_O92/O58_Estela_Escalas_Normalizacion_Cuadratica_2026_10_21/O58_Estela_Escalas_Normalizacion_Cuadratica_2026_10_21/resultados/ramas_compatibles_hasta_200.csv"
if not o58.exists():
    print("   (archivo de O58 no disponible fuera del repositorio; se omite)"); sys.exit(0)
archivo = {(int(r["c"]), int(r["d"]), int(r["M"])) for r in csv.DictReader(open(o58, encoding="utf-8")) if r["N"] == "3"}
propias = {tuple(t) for t in json.loads((aqui / "resultados.json").read_text(encoding="utf-8"))["L_O58"]["ramas_desde_2_2_3_hasta_200"]}
assert archivo == propias, f"difieren: {sorted(archivo ^ propias)}"
print(f"   OK — las {len(propias)} ramas desde (2,2,3) coinciden con ramas_compatibles_hasta_200.csv de O58")
