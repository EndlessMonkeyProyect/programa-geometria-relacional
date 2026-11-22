#!/usr/bin/env python3
"""Compara SHA-256 de los archivos entregados con MANIFEST.sha256."""
from pathlib import Path
from hashlib import sha256

BASE = Path(__file__).resolve().parent
MAN = BASE / "MANIFEST.sha256"

def main() -> None:
    lineas = [line.strip() for line in MAN.read_text(encoding="ascii").splitlines() if line.strip()]
    verificados = 0
    for linea in lineas:
        digest, archivo = linea.split("  ", 1)
        archivo = archivo.removeprefix("*")
        ruta = BASE / archivo
        assert ruta.is_file(), f"Falta {archivo}"
        actual = sha256(ruta.read_bytes()).hexdigest()
        assert digest.lower() == actual, f"Hash distinto: {archivo}"
        verificados += 1
    print(f"OK | manifest {verificados}/{len(lineas)}")

if __name__ == "__main__":
    main()
