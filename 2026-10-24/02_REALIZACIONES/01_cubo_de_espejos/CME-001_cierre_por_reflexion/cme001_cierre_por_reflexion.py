#!/usr/bin/env python3
"""CME-001 · Laboratorio del Cubo de Espejos — ¿cuándo se cierra un recinto de espejos?

Objeto y pregunta: un recinto cuyas paredes son espejos planos ideales. ¿Las reflexiones
sucesivas vuelven a repetirse (cierre) o cada nueva reflexión produce algo nuevo (apertura)?
Reglas admitidas: solo reflexiones en las caras del recinto (geometría euclídea, H1–H3 de O19).
Observable: número de partes lineales distintas (orientaciones) alcanzadas con palabras de
longitud <= L. Si se estabiliza, el recinto cierra; si crece sin fin, no cierra.
Recintos: cubo; tetraedro regular (módulo K4 de O19); ortoesquema (1/6 del cubo).
Resultado esperado según teoremas conocidos: el cubo cierra en 8 = (Z2)^3; el ortoesquema en
48 (grupo B3); el tetraedro regular nunca cierra: sus 4 reflexiones generan el producto libre
Z2*Z2*Z2*Z2 (Świerczkowski 1958), de modo que la cuenta es exactamente 2·3^L − 1.
Criterio general (Coxeter 1934): una celda de espejos cierra si y solo si cada par de caras
que se cortan forma un ángulo pi/k con k entero.
Ejecutar: python3 cme001_cierre_por_reflexion.py  -> imprime tabla y escribe cme001_resultados.json
"""
import itertools, json, math
from pathlib import Path
import numpy as np

def refl(n):
    n = np.asarray(n, float); n = n / np.linalg.norm(n)
    return np.eye(3) - 2 * np.outer(n, n)

def face_normals(V):
    out = []
    for i in range(4):
        f = [V[j] for j in range(4) if j != i]
        n = np.cross(f[1] - f[0], f[2] - f[0])
        if np.dot(n, V[i] - f[0]) > 0: n = -n
        out.append(n)
    return out

def dihedral(n1, n2):
    return math.pi - math.acos(np.dot(n1, n2) / np.linalg.norm(n1) / np.linalg.norm(n2))

def grow(gens, maxlen):
    key = lambda M: tuple(np.round(M, 8).ravel())
    seen = {key(np.eye(3))}; frontier = [np.eye(3)]; counts = []
    for _ in range(maxlen):
        new = []
        for M in frontier:
            for g in gens:
                P = g @ M; k = key(P)
                if k not in seen: seen.add(k); new.append(P)
        counts.append(len(seen)); frontier = new
        if not new: break
    return counts

CUBO = [refl(e) for e in np.eye(3)]  # caras opuestas tienen la misma parte lineal
REG = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)  # O19
ORTO = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 1]], float)

def main(maxlen=12):
    res = {}
    for nombre, gens, V in [("cubo", CUBO, None),
                            ("ortoesquema", [refl(n) for n in face_normals(ORTO)], ORTO),
                            ("tetraedro_regular", [refl(n) for n in face_normals(REG)], REG)]:
        c = grow(gens, maxlen)
        ang = None
        if V is not None:
            N = face_normals(V)
            ang = sorted({round(dihedral(N[i], N[j]) / math.pi, 6) for i, j in itertools.combinations(range(4), 2)})
        res[nombre] = {"conteo_por_longitud": c, "cierra": len(c) < maxlen, "diedros_en_pi": ang}
        print(f"{nombre:18s} {c}  diedros/pi={ang}")
    reg = res["tetraedro_regular"]["conteo_por_longitud"]
    assert reg == [2 * 3**L - 1 for L in range(1, len(reg) + 1)], "no coincide con producto libre"
    assert res["cubo"]["conteo_por_longitud"][-1] == 8 and res["ortoesquema"]["conteo_por_longitud"][-1] == 48
    res["comprobacion"] = "tetraedro regular = 2·3^L−1 (producto libre de cuatro Z2) hasta L=%d; cubo=8; ortoesquema=48" % len(reg)
    Path(__file__).with_name("cme001_resultados.json").write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(res["comprobacion"])

if __name__ == "__main__":
    main()
