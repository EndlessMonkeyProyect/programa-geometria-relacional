#!/usr/bin/env python3
"""Compara los resultados regenerados con los entregados, con tolerancia y no bit a bit.

Uso:  python comparar_resultados.py [carpeta_de_referencia]
Por omisión compara contra referencia_resultados/, que guarda copias intactas de los
resultados.json entregados, con las mismas rutas relativas.

Reglas:
  - números reales: |a − b| ≤ ATOL + RTOL·|b|;
  - excepción documentada: unos pocos observables numéricamente sensibles, listados uno por uno
    en TOLERANCIAS_ESPECIFICAS con el motivo; todo lo demás conserva RTOL y ATOL;
  - enteros, booleanos, textos, claves y longitudes de listas: comparación exacta;
  - claves que son una parametrización no única (p. ej. los pesos ajustados de PR-07): no se
    comparan sus coordenadas; se compara el invariante correspondiente, que ya figura en el
    mismo archivo (p. ej. el espectro ajustado).
Además informa las versiones del entorno actual frente a las registradas en entorno.json.
"""
from __future__ import annotations
import json, math, platform, sys
from pathlib import Path

RTOL, ATOL = 1e-9, 1e-12
PARAMETRIZACIONES = {"pesos_ajustados": "espectro_ajustado"}

# Campo (ruta completa, o prefijo de una lista) → (rtol, atol, motivo). Sólo observables cuyo error
# numérico esperado es del orden de la tolerancia general o mayor. No relaja nada más.
_PR07 = "paquetes/PR-07_Principios_Accion_2026-10-27"
TOLERANCIAS_ESPECIFICAS = {
    f"{_PR07}/D_U2/sensibilidad_mezcla": (
        1e-7, ATOL,
        "ν/ε⁴ con ε = 0,05: ν ≈ 7·10⁻⁸ se obtiene como 1 − ½ tr de una matriz próxima a la identidad; "
        "la cancelación deja un error relativo ≈ 10⁻¹⁶/ν ≈ 2·10⁻⁹, que depende de la biblioteca de álgebra lineal"),
    f"{_PR07}/D_U2/sensibilidad_direccion_central": (
        0.0, 1e-9,
        "el valor exacto es 0; lo almacenado (≈ 2·10⁻¹¹) es redondeo dividido por ε⁴ ≈ 6·10⁻⁶. "
        "Se compara en absoluto; la aserción del verificador exige < 10⁻⁶"),
    f"{_PR07}/E_control_grafo/espectro_ajustado": (
        1e-7, ATOL,
        "sale de un ajuste por mínimos cuadrados con autovalores degenerados; el optimizador se detiene "
        "con tolerancia ≈ 10⁻⁸ y la aserción exige |espectro − objetivo| < 10⁻⁸, así que dos ejecuciones "
        "correctas pueden diferir en unos 10⁻⁸ relativos"),
}
_usadas = set()


def tolerancia(ruta):
    for clave, (rtol, atol, _) in TOLERANCIAS_ESPECIFICAS.items():
        if ruta == clave or ruta.startswith(clave + "["):
            _usadas.add(clave)
            return rtol, atol, clave
    return RTOL, ATOL, None


def comparar(a, b, ruta, problemas):
    if isinstance(b, bool) or isinstance(a, bool):
        if a != b:
            problemas.append(f"{ruta}: {a!r} ≠ {b!r}")
    elif isinstance(b, int) and isinstance(a, int):
        if a != b:
            problemas.append(f"{ruta}: entero {a} ≠ {b}")
    elif isinstance(b, (int, float)) and isinstance(a, (int, float)):
        if math.isnan(b) and math.isnan(a):
            return
        rtol, atol, especifica = tolerancia(ruta)
        if not abs(a - b) <= atol + rtol * abs(b):
            nota = f"; tolerancia específica rtol={rtol:g}, atol={atol:g}" if especifica else ""
            problemas.append(f"{ruta}: {a!r} frente a {b!r} (dif. relativa {abs(a - b) / max(abs(b), 1e-300):.2e}{nota})")
    elif isinstance(b, dict) and isinstance(a, dict):
        if set(a) != set(b):
            problemas.append(f"{ruta}: claves distintas {sorted(set(a) ^ set(b))}")
            return
        for k in b:
            if k in PARAMETRIZACIONES:
                if PARAMETRIZACIONES[k] not in b:
                    problemas.append(f"{ruta}/{k}: falta el invariante {PARAMETRIZACIONES[k]}")
                continue                      # se compara el invariante, no la parametrización
            comparar(a[k], b[k], f"{ruta}/{k}", problemas)
    elif isinstance(b, list) and isinstance(a, list):
        if len(a) != len(b):
            problemas.append(f"{ruta}: longitud {len(a)} ≠ {len(b)}")
            return
        for i, (x, y) in enumerate(zip(a, b)):
            comparar(x, y, f"{ruta}[{i}]", problemas)
    elif a != b:
        problemas.append(f"{ruta}: {a!r} ≠ {b!r}")


def main():
    raiz = Path(__file__).resolve().parent
    ref = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else raiz / "referencia_resultados"
    reg = json.loads((raiz / "entorno.json").read_text(encoding="utf-8"))
    import numpy, scipy
    actual = {"python": platform.python_version(), "numpy": numpy.__version__, "scipy": scipy.__version__,
              "plataforma": platform.platform()}
    print("Entorno registrado:", {k: reg["generado_con"][k] for k in actual})
    print("Entorno actual:    ", actual)
    total_problemas = 0
    for f in sorted(ref.rglob("resultados.json")):
        rel = f.relative_to(ref)
        nuevo = raiz / rel
        problemas = []
        comparar(json.loads(nuevo.read_text(encoding="utf-8")), json.loads(f.read_text(encoding="utf-8")), str(rel.parent), problemas)
        estado = "OK" if not problemas else f"{len(problemas)} diferencias"
        print(f"  {estado:>15}  {rel.parent}")
        for p in problemas[:10]:
            print("      ", p)
        total_problemas += len(problemas)
    print()
    if _usadas:
        print("Tolerancias específicas aplicadas (el resto usa la general):")
        for clave in sorted(_usadas):
            rtol, atol, motivo = TOLERANCIAS_ESPECIFICAS[clave]
            print(f"  {clave}: rtol={rtol:g}, atol={atol:g}. Motivo: {motivo}.")
        print()
    if total_problemas:
        print(f"Hay {total_problemas} diferencias fuera de tolerancia (general RTOL={RTOL}, ATOL={ATOL}).")
        sys.exit(1)
    print(f"Todos los resultados coinciden con los entregados dentro de la tolerancia "
          f"(general RTOL={RTOL}, ATOL={ATOL}; {len(_usadas)} campos con tolerancia específica).")


if __name__ == "__main__":
    main()
