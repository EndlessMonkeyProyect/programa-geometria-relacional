#!/usr/bin/env python3
"""Verifica esta edición, sin modificar los originales ni necesitar red."""
from pathlib import Path
import hashlib
import json
import csv
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    manifest = json.loads((ROOT / "fuentes/MANIFIESTO.json").read_text())
    for item in manifest["originales"] + manifest["extraidos"]:
        p = ROOT / item["ruta"]
        if not p.is_file():
            errors.append("Falta: " + item["ruta"])
            continue
        raw = p.read_bytes()
        if len(raw) != item["bytes"] or hashlib.sha256(raw).hexdigest() != item["sha256"]:
            errors.append("Integridad: " + item["ruta"])
    expected = {i["nombre"] for i in manifest["originales"]}
    actual = {p.name for p in (ROOT / "fuentes/originales").iterdir() if p.is_file()}
    if expected != actual:
        errors.append("Inventario distinto del manifiesto")
    for item in manifest["extraidos"]:
        with zipfile.ZipFile(ROOT / "fuentes/originales" / item["paquete"]) as z:
            if z.read(item["miembro"]) != (ROOT / item["ruta"]).read_bytes():
                errors.append("Extracción distinta: " + item["miembro"])
        if item["duplicado_exacto_de"]:
            if (ROOT / item["ruta"]).read_bytes() != (ROOT / item["duplicado_exacto_de"]).read_bytes():
                errors.append("Duplicado inconsistente: " + item["ruta"])
    json_count = 0
    for p in (ROOT / "fuentes").rglob("*.json"):
        try:
            json.loads(p.read_text())
            json_count += 1
        except Exception as exc:
            errors.append(f"JSON {p.name}: {exc}")
    links = 0
    editorial = list((ROOT / "docs").rglob("*.md"))
    editorial += list(ROOT.glob("*.md"))
    editorial += list((ROOT / "verificacion").glob("*.md"))
    editorial += [ROOT / "fuentes/CATALOGO.md", ROOT / "datos/README.md", ROOT / "ejemplos/README.md"]
    for p in editorial:
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", p.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            links += 1
            dest = (p.parent / target).resolve()
            if not dest.is_relative_to(ROOT) or not dest.exists():
                errors.append(f"Enlace roto en {p.relative_to(ROOT)}: {target}")
    with (ROOT / "fuentes/originales/mf53_equality_order.csv").open(newline="") as f:
        rows = list(csv.DictReader(f))
    data53 = json.loads((ROOT / "fuentes/originales/mf53_obdd_normalization_summary.json").read_text())
    reported = data53["equality_order_experiment"]
    if len(rows) != len(reported):
        errors.append("Filas MF53 distintas")
    for row, ref in zip(rows, reported):
        for key, value in row.items():
            if key not in ref or abs(float(value) - float(ref[key])) > 1e-10:
                errors.append(f"MF53 CSV/JSON: {key}")
    data80 = json.loads((ROOT / "fuentes/originales/gamma_reference_results_v0_80.json").read_text())
    stress = data80["stress"]
    hits = sum(r["gamma_width"] == r["optimal_width"] for r in stress)
    for r in stress:
        if sorted(r["gamma_order"]) != list(range(1, r["n"] + 1)):
            errors.append("Orden inválido en datos v0.80")
        if r["gamma_width"] < r["optimal_width"]:
            errors.append("Ancho menor al óptimo reportado")
    if len(stress) != 24 or hits != 14:
        errors.append("Resumen v0.80 distinto del texto editorial")
    result = {
        "estado": "PASS" if not errors else "FAIL",
        "originales": len(manifest["originales"]),
        "extraidos": len(manifest["extraidos"]),
        "json_validos_incluido_manifiesto": json_count,
        "documentos_editoriales_con_enlaces_revisados": len(editorial),
        "enlaces_locales": links,
        "filas_csv_mf53": len(rows),
        "v080_instancias_reportadas": len(stress),
        "v080_aciertos_optimo_reportado": hits,
        "validaciones_historicas_disponibles": len(list((ROOT / "fuentes/originales").glob("VALIDATION*.md"))),
        "alcance": "Integridad y consistencia documental; no reproduce los experimentos históricos completos.",
        "errores": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
