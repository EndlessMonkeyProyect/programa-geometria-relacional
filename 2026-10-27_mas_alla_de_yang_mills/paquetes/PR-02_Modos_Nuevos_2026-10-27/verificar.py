#!/usr/bin/env python3
"""PR-02 — Dónde vive la brecha al duplicar: modos heredados frente a modos nuevos.

Todo se calcula a partir de matrices explícitas; ningún resultado se fija a mano.
Ejecutar: python verificar.py   (dependencia: numpy)
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

NIVELES = range(1, 11)          # n = 1..10  ->  nivel n+1 con 2^(n+1) puntos (hasta 2048)
TOL = 1e-9


# ---------------------------------------------------------------- utilidades
def u(N):
    return np.ones(N) / np.sqrt(N)


def lap(N, aristas):
    L = np.zeros((N, N))
    for x, y in aristas:
        L[x, x] += 1; L[y, y] += 1; L[x, y] -= 1; L[y, x] -= 1
    return L


def lap_ciclo(N):
    # C_2 como ciclo genuino: dos aristas entre 0 y 1 (así la copia periódica hereda la forma exacta)
    return lap(N, [(i, (i + 1) % N) for i in range(N)]) if N > 2 else lap(N, [(0, 1), (1, 0)])


def lap_hipercubo(N):
    n = N.bit_length() - 1
    return lap(N, [(x, x ^ (1 << b)) for x in range(N) for b in range(n) if x < x ^ (1 << b)])


def J_binaria(N):
    """PR-01: e_i -> (e_2i + e_2i+1)/sqrt2. El bit nuevo es el menos significativo."""
    M = np.zeros((2 * N, N)); K = np.zeros((2 * N, N))
    for i in range(N):
        M[2 * i, i] = M[2 * i + 1, i] = 1 / np.sqrt(2)
        K[2 * i, i], K[2 * i + 1, i] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    return M, K


def J_volumen(N):
    """Copia periódica: e_i -> (e_i + e_{i+N})/sqrt2. Lo nuevo es la copia con signo opuesto."""
    M = np.zeros((2 * N, N)); K = np.zeros((2 * N, N))
    for i in range(N):
        M[i, i] = M[i + N, i] = 1 / np.sqrt(2)
        K[i, i], K[i + N, i] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    return M, K


def base_ortogonal_a_u(N):
    """Base ortonormal de u^perp en R^N (Gram-Schmidt vía QR)."""
    A = np.column_stack([u(N), np.eye(N)[:, : N - 1]])
    Q, _ = np.linalg.qr(A)
    return Q[:, 1:]


def brecha(Lm, W):
    """min del cociente de Rayleigh de Lm sobre el subespacio con base ortonormal W."""
    return float(np.linalg.eigvalsh(W.T @ Lm @ W)[0])


# ------------------------------------------------- 0. PR-01 recalculado con matrices
pr01 = []
for n in range(1, 17):
    N = 2 ** n
    v = u(N)
    fila = {"n": n}
    for nombre, A in (("atomo", [0]), ("mitad", range(N // 2)), ("todo_menos_uno", range(N - 1))):
        d = np.zeros(N); d[list(A)] = 1
        r = v - d * v
        fila[nombre] = float(r @ r)
    esperado = {"atomo": 1 - 2.0 ** -n, "mitad": 0.5, "todo_menos_uno": 2.0 ** -n}
    assert all(abs(fila[k] - esperado[k]) < 1e-12 for k in esperado)
    pr01.append(fila)
if True:  # compatibilidad P'J = JP calculada como matriz (n <= 10)
    for n in range(1, 11):
        N = 2 ** n; Jm, _ = J_binaria(N)
        for nombre, A, A2, compatible in (("mitad", range(N // 2), range(N), True),
                                          ("todo_menos_uno", range(N - 1), range(2 * N - 1), False),
                                          ("atomo", [0], [0], False)):
            P = np.diag([1.0 if i in set(A) else 0.0 for i in range(N)])
            P2 = np.diag([1.0 if i in set(A2) else 0.0 for i in range(2 * N)])
            c = np.linalg.norm(P2 @ Jm - Jm @ P)
            assert (c < TOL) == compatible, (n, nombre, c)
            if compatible:  # el teorema de PR-01, comprobado numéricamente
                r1 = u(N) - P @ u(N); r2 = u(2 * N) - P2 @ u(2 * N)
                assert np.allclose(r2, Jm @ r1) and abs(r1 @ r1 - r2 @ r2) < 1e-12

# --------------------------------------------- 1. estructuras declaradas y medición
CASOS = {
    "hipercubo": dict(L=lap_hipercubo, J=J_binaria,
                      lectura="cada duplicación añade un eje nuevo e independiente (un bit nuevo)"),
    "ciclo_volumen": dict(L=lap_ciclo, J=J_volumen,
                          lectura="la duplicación alarga el mismo eje (pared que se corre, paso fijo)"),
    "ciclo_refinamiento": dict(L=lap_ciclo, J=J_binaria,
                               lectura="la duplicación subdivide el mismo eje (longitud fija, paso a=1/N)"),
}

salida = {"pr01_recalculado": pr01[:4] + [pr01[-1]], "casos": {}}
for nombre, c in CASOS.items():
    filas = []
    for n in NIVELES:
        N = 2 ** n
        Lv, Ln = c["L"](N), c["L"](2 * N)
        Jm, K = c["J"](N)
        # contrato de PR-01 y de la descomposición
        assert np.allclose(Jm.T @ Jm, np.eye(N)) and np.allclose(K.T @ K, np.eye(N))
        assert np.allclose(Jm.T @ K, 0) and np.allclose(Jm @ u(N), u(2 * N))
        assert np.allclose(Ln @ u(2 * N), 0)
        B = Jm @ base_ortogonal_a_u(N)             # modos heredados ortogonales al vacío
        val, vec = np.linalg.eigh(Ln)
        g = float(val[1])                           # brecha completa (grafo conexo)
        E = vec[:, np.abs(val - g) < 1e-8]          # espacio propio completo del modo bajo
        peso = float(np.trace(E.T @ Jm @ Jm.T @ E) / E.shape[1])   # fracción heredada, sin elegir base
        g_old, g_new = brecha(Ln, B), brecha(Ln, K)
        kappa = float(np.linalg.norm(Jm.T @ Ln @ K, 2))
        forma = float(np.linalg.norm(Jm.T @ Ln @ Jm - Lv))          # ¿se hereda la forma exacta?
        conm = float(np.linalg.norm(Ln @ Jm @ Jm.T - Jm @ Jm.T @ Ln))
        # lema: max(0, min(g_old,g_new) - kappa) <= g <= min(g_old, g_new)
        assert g <= min(g_old, g_new) + TOL
        assert g >= min(g_old, g_new) - kappa - TOL
        if kappa < TOL:
            assert abs(g - min(g_old, g_new)) < TOL
        fila = dict(n_mas_1=n + 1, puntos=2 * N, brecha=g, brecha_heredados=g_old,
                    brecha_nuevos=g_new, acoplamiento=kappa,
                    restriccion_menor=("nuevos" if g_new < g_old - TOL else "heredados" if g_old < g_new - TOL else "empate"),
                    multiplicidad_modo_bajo=int(E.shape[1]), peso_heredado_modo_bajo=peso,
                    forma_heredada_exacta=forma < TOL,
                    forma_heredada_a_la_mitad=float(np.linalg.norm(Jm.T @ Ln @ Jm - Lv / 2)) < TOL,
                    conmuta_con_duplicacion=conm < TOL)
        if nombre == "ciclo_refinamiento":
            fila["brecha_unidades_fisicas_a=1/puntos"] = g * (2 * N) ** 2
        filas.append(fila)
    salida["casos"][nombre] = dict(lectura=c["lectura"], filas=filas)

# ------------------------------------------------------ 2. comprobaciones de alcance
h = salida["casos"]["hipercubo"]["filas"]
cv = salida["casos"]["ciclo_volumen"]["filas"]
cr = salida["casos"]["ciclo_refinamiento"]["filas"]
assert all(abs(f["brecha"] - 2) < TOL and abs(f["brecha_nuevos"] - 2) < TOL for f in h)
assert all(f["forma_heredada_exacta"] and f["conmuta_con_duplicacion"] for f in h + cv)
assert all(abs(f["peso_heredado_modo_bajo"] - (f["n_mas_1"] - 1) / f["n_mas_1"]) < 1e-9 for f in h)
assert all(f["restriccion_menor"] == "nuevos" and f["peso_heredado_modo_bajo"] < 1e-9 for f in cv)
assert all(abs(f["brecha"] - 4 * np.sin(np.pi / f["puntos"]) ** 2) < TOL for f in cv + cr)
assert all(f["forma_heredada_a_la_mitad"] and not f["forma_heredada_exacta"] for f in cr)
assert all(f["acoplamiento"] > 0.1 and f["restriccion_menor"] == "heredados" for f in cr[1:])
assert all(f["brecha"] < 0.75 * min(f["brecha_heredados"], f["brecha_nuevos"]) for f in cr[1:])
assert all(abs(f["brecha_nuevos"] - 2) < TOL for f in cr)
assert all(f["peso_heredado_modo_bajo"] > 0.5 for f in cr[1:])
assert abs(cr[-1]["brecha_unidades_fisicas_a=1/puntos"] - 4 * np.pi ** 2) < 1e-3

salida["resumen"] = {
    "pr01": "residuos recalculados con matrices; compatibilidad y teorema comprobados numéricamente",
    "hipercubo": "brecha 2 en todo nivel; cada duplicación aporta una dirección nueva con la misma brecha",
    "ciclo_volumen": "brecha -> 0 como 4 sin^2(pi/2N); el modo bajo es enteramente nuevo (copia con signo opuesto)",
    "ciclo_refinamiento": "brecha de red -> 0 pero en unidades físicas -> 4 pi^2 (volumen finito); "
                          "el modo bajo es mayormente heredado; los nuevos son de escala fina (brecha 2); "
                          "la forma heredada pesa la mitad y el acoplamiento baja la brecha por debajo de ambas restricciones",
    "advertencia": "modelos auxiliares de grafos; no es Yang-Mills ni una prueba de brecha física",
}
root = Path(__file__).resolve().parent
(root / "resultados.json").write_text(json.dumps(salida, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def tabla(nombre, extra=None):
    print(f"\n{nombre}: {CASOS[nombre]['lectura']}")
    cab = f"{'pts':>5} {'brecha':>10} {'heredados':>10} {'nuevos':>10} {'acopl.':>8} {'peso_her':>8}"
    print(cab + (f"   {extra}" if extra else ""))
    for f in salida["casos"][nombre]["filas"]:
        s = (f"{f['puntos']:>5} {f['brecha']:>10.6f} {f['brecha_heredados']:>10.6f} "
             f"{f['brecha_nuevos']:>10.6f} {f['acoplamiento']:>8.4f} {f['peso_heredado_modo_bajo']:>8.4f}")
        if extra:
            s += f"  {f[extra]:.4f}"
        print(s)


for k in ("hipercubo", "ciclo_volumen"):
    tabla(k)
tabla("ciclo_refinamiento", "brecha_unidades_fisicas_a=1/puntos")
print("\nOK: todas las aserciones pasaron. No es una prueba de brecha de Yang-Mills.")
