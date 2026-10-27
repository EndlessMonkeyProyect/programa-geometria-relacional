#!/usr/bin/env python3
"""PR-07 — De los principios relacionales a la acción, y la separación 3+1 que hace ν.

Comprueba numéricamente cada afirmación del README:
  A. la elección de Wilson cumple los cuatro principios (invariancia de referencia, no negatividad);
  B. con transportes constantes, el defecto de Wilson de la plaqueta es exactamente ν(U,V);
  C. límite continuo clásico, para campos suaves: Σ defecto → (a⁴/8) Σ F^a F^a;
  D. en U(2), ν es ciego a la fase y sólo la parte su(2) de cada dirección cuenta;
  E. control: el 3+1 de cuatro referencias en grafo es puro conteo y su modo nulo nunca es el fotón;
  F. matriz electrodébil conocida y fracción ν-sensible del fotón = sin²θ_W;
  G. principio 4 general: defectos d(U) ≥ 0, invariantes por conjugación y nulos en la identidad.
     Wilson y Manton tienen término cuadrático no degenerado y el mismo límite clásico;
     [1 − ½ Re tr U]² empieza en orden cuatro y no lo tiene. En U(2) el término cuadrático
     invariante tiene dos constantes independientes (su(2) y u(1)), que los principios no fijan;
  H. separación 3+1, precisa: ν(e^{iεX}, e^{iεY}) = ε⁴|x×y|²/8 + O(ε⁶); dos transportes no
     centrales alineados dan ν = 0; sólo la familia completa de comparaciones aísla el centro.
Las secciones A–F son las de la primera versión y dan los mismos valores; G y H usan un
generador aleatorio aparte y, para valores pequeños de ν, la forma sin cancelación |c|²/(1 + c0).
Ejecutar: python verificar.py   (dependencias: numpy, scipy; ~6 s)
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares

rng = np.random.default_rng(20261027)
I2 = np.eye(2, dtype=complex)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
T = [s / 2 for s in SIG]
salida = {}


def su2(gen=rng):
    q = gen.standard_normal(4); q /= np.linalg.norm(q)
    return q[0] * I2 + 1j * sum(q[k + 1] * SIG[k] for k in range(3))


def inv(U):
    return U.conj().T


def nu(U, V):
    return float(1 - 0.5 * np.trace(U @ V @ inv(U) @ inv(V)).real)


def defecto(Up):
    return float(1 - 0.5 * np.trace(Up).real)


# ---- miembros de la familia de defectos (sección G); funciones de clase de SU(2)
def partes_su2(S):
    """S = s0·I + i s·σ en SU(2) → (s0, s)."""
    return 0.5 * np.trace(S).real, np.array([0.5 * np.trace(S @ SIG[k]).imag for k in range(3)])


def d_wilson(S):
    """1 − ½ Re tr S = 1 − s0, escrito |s|²/(1 + s0) para no perder dígitos cerca de la identidad."""
    s0, s = partes_su2(S)
    return float(s @ s / (1 + s0)) if s0 >= 0 else float(1 - s0)


def d_manton(S):
    """θ²/8, con θ ∈ [0, 2π] el ángulo de rotación de S (acción de Manton, 1980)."""
    s0, s = partes_su2(S)
    return float(np.arctan2(np.linalg.norm(s), s0) ** 2 / 2)


def d_cuadrado(S):
    """Contraejemplo: [1 − ½ Re tr S]². No negativo, invariante, nulo sólo en I; empieza en orden cuatro."""
    return d_wilson(S) ** 2


def nu_estable(U, V):
    """ν(U,V) = d_wilson(UVU⁻¹V⁻¹): el conmutador está en SU(2) aunque U, V estén en U(2)."""
    return d_wilson(U @ V @ inv(U) @ inv(V))


# ---------------------------------------------------------------- A. principios → peso de Wilson
L = 6
links = {(x, y, mu): su2() for x in range(L) for y in range(L) for mu in (0, 1)}


def plaqueta(lk, x, y):
    U1 = lk[(x, y, 0)]; U2 = lk[((x + 1) % L, y, 1)]
    U3 = lk[(x, (y + 1) % L, 0)]; U4 = lk[(x, y, 1)]
    return U1 @ U2 @ inv(U3) @ inv(U4)


def accion(lk):
    return sum(defecto(plaqueta(lk, x, y)) for x in range(L) for y in range(L))


g = {(x, y): su2() for x in range(L) for y in range(L)}
links_g = {}
for (x, y, mu), U in links.items():
    xn, yn = ((x + 1) % L, y) if mu == 0 else (x, (y + 1) % L)
    links_g[(x, y, mu)] = g[(x, y)] @ U @ inv(g[(xn, yn)])        # cambio de referencia local
S0, S1 = accion(links), accion(links_g)
defs = [defecto(plaqueta(links, x, y)) for x in range(L) for y in range(L)]
assert abs(S0 - S1) < 1e-10                                         # principio 2: sólo cuentan los lazos cerrados
assert min(defs) >= -1e-15 and max(defs) <= 2 + 1e-15              # principio 4: nunca negativo
assert abs(defecto(I2)) < 1e-15                                     # defecto nulo en el cierre perfecto
salida["A_invariancia_y_positividad"] = {"accion": S0, "accion_tras_cambio_de_referencia": S1,
                                         "defecto_min": min(defs), "defecto_max": max(defs)}

# ---------------------------------------------------------------- B. ν es el defecto con transportes constantes
errB = 0.0
for _ in range(2000):
    U, V = su2(), su2()
    lk = {(x, y, mu): (U if mu == 0 else V) for x in range(L) for y in range(L) for mu in (0, 1)}
    errB = max(errB, abs(defecto(plaqueta(lk, 0, 0)) - nu(U, V)))
assert errB < 1e-13
salida["B_nu_igual_defecto_transportes_constantes_error"] = errB


# ---------------------------------------------------------------- C. límite continuo
def campos(x, y):
    """Conexión su(2) suave y periódica en [0, 2π)²."""
    A1 = 0.7 * np.sin(y) * T[0] + 0.5 * np.cos(x + y) * T[2] + 0.3 * np.sin(2 * x) * T[1]
    A2 = 0.6 * np.cos(x) * T[1] + 0.4 * np.sin(2 * y) * T[0] + 0.5 * np.cos(x - y) * T[2]
    return A1, A2


def F12(x, y, h=1e-5):
    dA2dx = (campos(x + h, y)[1] - campos(x - h, y)[1]) / (2 * h)
    dA1dy = (campos(x, y + h)[0] - campos(x, y - h)[0]) / (2 * h)
    A1, A2 = campos(x, y)
    return dA2dx - dA1dy + 1j * (A1 @ A2 - A2 @ A1)


cocientes, cocientes_manton, cocientes_cuadrado = {}, {}, {}
for Lc in (16, 32, 64, 128):
    a = 2 * np.pi / Lc
    tot, cont, tot_m, tot_c = 0.0, 0.0, 0.0, 0.0
    for i in range(Lc):
        for j in range(Lc):
            x, y = i * a, j * a
            U1 = expm(1j * a * campos(x + a / 2, y)[0])
            U2 = expm(1j * a * campos(x + a, y + a / 2)[1])
            U3 = expm(1j * a * campos(x + a / 2, y + a)[0])
            U4 = expm(1j * a * campos(x, y + a / 2)[1])
            Up = U1 @ U2 @ inv(U3) @ inv(U4)
            tot += defecto(Up)
            tot_m += d_manton(Up)                                      # para G: otro miembro de la familia
            tot_c += d_cuadrado(Up)                                    # para G: el contraejemplo
            Fc = F12(x + a / 2, y + a / 2)
            cont += a ** 4 / 8 * 2 * np.trace(Fc @ Fc).real            # (a⁴/8) F^a F^a, con F^aF^a = 2 tr F²
    cocientes[str(Lc)] = tot / cont
    cocientes_manton[str(Lc)] = tot_m / cont
    cocientes_cuadrado[str(Lc)] = tot_c / cont
c = list(cocientes.values())
assert all(abs(c[k + 1] - 1) < abs(c[k] - 1) for k in range(len(c) - 1)) and abs(c[-1] - 1) < 2e-3
salida["C_limite_continuo_defecto_sobre_a4F2_8"] = cocientes

# ---------------------------------------------------------------- D. U(2): ν ciego a la fase, núcleo = centro
errD = 0.0
for _ in range(2000):
    U, V = su2(), su2()
    f1, f2 = rng.uniform(0, 2 * np.pi, 2)
    errD = max(errD, abs(nu(np.exp(1j * f1) * U, np.exp(1j * f2) * V) - nu(U, V)))
assert errD < 1e-13


def sensibilidad(c0, xv, eps=0.05, muestras=400):
    """máx_Y ν(e^{iεX}, e^{iεY})/ε⁴ para X = c0·I/2 + x·σ/2 en u(2)."""
    X = c0 * I2 / 2 + sum(xv[k] * T[k] for k in range(3))
    Ux = expm(1j * eps * X)
    m = 0.0
    for _ in range(muestras):
        yv = rng.standard_normal(4); yv /= np.linalg.norm(yv)
        Y = yv[0] * I2 / 2 + sum(yv[k + 1] * T[k] for k in range(3))
        m = max(m, nu(Ux, expm(1j * eps * Y)) / eps ** 4)
    return m


s_centro = sensibilidad(1.0, np.zeros(3))
s_su2 = sensibilidad(0.0, np.array([1.0, 0, 0]))
s_mezcla = sensibilidad(1.0, np.array([0, 0, 0.3]))
assert s_centro < 1e-6 and s_su2 > 1e-2 and s_mezcla > 1e-4
salida["D_U2"] = {"error_ceguera_de_fase": errD, "sensibilidad_direccion_central": s_centro,
                  "sensibilidad_direccion_su2": s_su2, "sensibilidad_mezcla": s_mezcla,
                  "dimensiones": {"nu_sensibles": 3, "nu_ciegas": 1}}

# ---------------------------------------------------------------- E. control: cuatro referencias en grafo
nulos_uniformes, conteos = 0, set()
for _ in range(500):
    N = int(rng.integers(3, 9))
    W = np.triu(rng.uniform(0.1, 2.0, (N, N)) * (rng.uniform(size=(N, N)) < 0.7), 1)
    W = W + W.T
    for k in range(N - 1):                                           # garantiza conexidad con un camino
        W[k, k + 1] = W[k + 1, k] = max(W[k, k + 1], 0.5)
    Lg = np.diag(W.sum(1)) - W
    val, vec = np.linalg.eigh(Lg)
    ceros = int(np.sum(val < 1e-10))
    conteos.add((N, ceros, N - ceros))
    if ceros == 1 and abs(abs(vec[:, 0] @ (np.ones(N) / np.sqrt(N))) - 1) < 1e-10:
        nulos_uniformes += 1
assert nulos_uniformes == 500 and all(z == 1 and p == n - 1 for n, z, p in conteos)

tw = np.linspace(0.01, np.pi / 2 - 0.01, 200)                       # fotón (0,0,sinθ,cosθ) en base (W1,W2,W3,B)
solape_max = float(max((np.sin(t) + np.cos(t)) / 2 for t in tw))
assert solape_max <= np.sqrt(2) / 2 + 1e-12                          # nunca es el modo uniforme


def lap4(w):
    Wm = np.zeros((4, 4)); k = 0
    for i in range(4):
        for j in range(i + 1, 4):
            Wm[i, j] = Wm[j, i] = w[k]; k += 1
    return np.diag(Wm.sum(1)) - Wm


g_, gp = 0.6517, 0.3576
objetivo = np.array([0, g_ ** 2, g_ ** 2, g_ ** 2 + gp ** 2])
ajuste = least_squares(lambda w: np.linalg.eigvalsh(lap4(np.abs(w))) - objetivo, x0=np.full(6, 0.12))
w_aj = np.abs(ajuste.x)
esp_aj = np.linalg.eigvalsh(lap4(w_aj))
assert np.allclose(esp_aj, objetivo, atol=1e-8)                       # ajustar pesos reproduce las masas...
modo_nulo = np.linalg.eigh(lap4(w_aj))[1][:, 0]
assert abs(abs(modo_nulo @ np.full(4, 0.5)) - 1) < 1e-8               # ...pero el modo nulo sigue siendo uniforme
salida["E_control_grafo"] = {"casos_aleatorios": 500, "todos_un_cero_y_N_menos_1_positivos": True,
                             "solape_maximo_modo_uniforme_con_foton": solape_max,
                             "pesos_ajustados": w_aj.tolist(), "espectro_ajustado": esp_aj.tolist()}

# ---------------------------------------------------------------- F. matriz electrodébil (resultado conocido)
v = 246.22
M2 = v ** 2 / 4 * np.array([[g_ ** 2, 0, 0, 0], [0, g_ ** 2, 0, 0], [0, 0, g_ ** 2, -g_ * gp], [0, 0, -g_ * gp, gp ** 2]])
val, vec = np.linalg.eigh(M2)
foton = vec[:, 0] * np.sign(vec[3, 0])
s2w = gp ** 2 / (g_ ** 2 + gp ** 2)
MW, MZ = np.sqrt(val[1]), np.sqrt(val[3])
assert abs(val[0]) < 1e-9 and np.allclose(foton, [0, 0, gp, g_] / np.hypot(g_, gp))
assert abs(MW / MZ - np.sqrt(1 - s2w)) < 1e-12
frac_sensible = float(foton[0] ** 2 + foton[1] ** 2 + foton[2] ** 2)   # parte en su(2), la que ν ve
assert abs(frac_sensible - s2w) < 1e-12
salida["F_electrodebil"] = {"g": g_, "g_prima": gp, "v_GeV": v, "M_W_arbol_GeV": float(MW), "M_Z_arbol_GeV": float(MZ),
                            "sin2_theta_W": float(s2w), "fraccion_nu_sensible_del_foton": frac_sensible,
                            "foton_en_base_W1_W2_W3_B": foton.tolist()}

# ---------------------------------------------------------------- G. principio 4 general: la familia de defectos
rng2 = np.random.default_rng(20261028)                               # aparte: no altera A–F
familia = {"wilson": d_wilson, "manton": d_manton, "wilson_al_cuadrado": d_cuadrado}
G = {"admisibilidad": {}, "coeficiente_cuadratico": {}}
errW = 0.0
for nombre, d in familia.items():
    e_conj, d_min = 0.0, np.inf
    for _ in range(1000):
        U, h = su2(rng2), su2(rng2)
        e_conj = max(e_conj, abs(d(h @ U @ inv(h)) - d(U)))             # invariante por conjugación
        d_min = min(d_min, d(U))
        if nombre == "wilson":
            errW = max(errW, abs(d(U) - defecto(U)))                     # la forma estable es la misma función
    assert e_conj < 1e-12 and d_min > 0 and d(I2) == 0                   # ≥ 0, invariante, nulo en la identidad
    G["admisibilidad"][nombre] = {"error_invariancia_conjugacion": e_conj, "minimo_en_1000_muestras": d_min, "valor_en_identidad": d(I2)}
assert errW < 1e-14

eps_q = 1e-3                                                          # d(e^{iεX})/ε² → κ|x|², X = x·σ/2, |x| = 1
direcciones = [np.eye(3)[k] for k in range(3)] + [u / np.linalg.norm(u) for u in rng2.standard_normal((20, 3))]
for nombre, d in familia.items():
    ks = [d(expm(1j * eps_q * sum(u[k] * T[k] for k in range(3)))) / eps_q ** 2 for u in direcciones]
    G["coeficiente_cuadratico"][nombre] = {"min": min(ks), "max": max(ks)}
kq = G["coeficiente_cuadratico"]
assert abs(kq["wilson"]["min"] - 1 / 8) < 1e-6 and kq["wilson"]["max"] - kq["wilson"]["min"] < 1e-12
assert abs(kq["manton"]["min"] - 1 / 8) < 1e-6 and kq["manton"]["max"] - kq["manton"]["min"] < 1e-12
assert kq["wilson_al_cuadrado"]["max"] < 1e-6                        # sin término cuadrático
G["epsilon_coeficiente"] = eps_q

cm, cc = list(cocientes_manton.values()), list(cocientes_cuadrado.values())
assert all(abs(cm[k + 1] - 1) < abs(cm[k] - 1) for k in range(len(cm) - 1)) and abs(cm[-1] - 1) < 2e-3
assert all(12 < cc[k] / cc[k + 1] < 20 for k in range(len(cc) - 1)) and cc[-1] < 1e-4   # ∝ a⁴ → 0
G["limite_continuo_sobre_a4F2_8"] = {"wilson": cocientes, "manton": cocientes_manton, "wilson_al_cuadrado": cocientes_cuadrado}


def d_u2(U, lam=0.0):
    """En U(2): 1 − ½ Re tr U + λ(1 − Re det U). Con U = e^{iφ}S, S ∈ SU(2), sin cancelación:
    1 − ½ Re tr U = 2 sen²(φ/2) + cos φ · d_wilson(S),   1 − Re det U = 2 sen² φ."""
    phi = 0.5 * np.angle(np.linalg.det(U))
    S = np.exp(-1j * phi) * U
    return float(2 * np.sin(phi / 2) ** 2 + np.cos(phi) * d_wilson(S) + lam * 2 * np.sin(phi) ** 2)


e_u2 = 0.0
for _ in range(500):
    U, h = su2(rng2) * np.exp(1j * rng2.uniform(0, 2 * np.pi)), su2(rng2) * np.exp(1j * rng2.uniform(0, 2 * np.pi))
    for lam in (0.0, 1.0):
        e_u2 = max(e_u2, abs(d_u2(h @ U @ inv(h), lam) - d_u2(U, lam)))
        assert d_u2(U, lam) >= 0
    e_u2 = max(e_u2, abs(d_u2(U) - defecto(U)))
assert e_u2 < 1e-12
k_u2 = {}
for lam in (0.0, 1.0):
    k_central = d_u2(expm(1j * eps_q * I2 / 2), lam) / eps_q ** 2
    k_su2 = d_u2(expm(1j * eps_q * T[2]), lam) / eps_q ** 2
    k_u2[f"lambda_{lam:g}"] = {"kappa_u1": k_central, "kappa_su2": k_su2, "cociente_u1_su2": k_central / k_su2}
assert abs(k_u2["lambda_0"]["cociente_u1_su2"] - 1) < 1e-6 and abs(k_u2["lambda_1"]["cociente_u1_su2"] - 5) < 1e-5
G["U2_dos_constantes"] = {"error_invariancia_y_forma_estable": e_u2, **k_u2}
salida["G_familia_de_defectos"] = G

# ---------------------------------------------------------------- H. separación 3+1, formulación precisa
def gen_u2(c, x):
    """X = (c·I + x·σ)/2 en u(2)."""
    return c * I2 / 2 + sum(x[k] * T[k] for k in range(3))


errH = 0.0                                                            # forma cerrada, ε = 1
for _ in range(500):
    c, d_, x, y = rng2.standard_normal(), rng2.standard_normal(), rng2.standard_normal(3), rng2.standard_normal(3)
    U, V = expm(1j * gen_u2(c, x)), expm(1j * gen_u2(d_, y))
    cerrada = 2 * np.sin(np.linalg.norm(x) / 2) ** 2 * np.sin(np.linalg.norm(y) / 2) ** 2 * \
        (np.linalg.norm(np.cross(x, y)) / (np.linalg.norm(x) * np.linalg.norm(y))) ** 2
    errH = max(errH, abs(nu(U, V) - cerrada), abs(nu_estable(U, V) - cerrada))
assert errH < 1e-13

pares = [(rng2.standard_normal(), rng2.standard_normal(3), rng2.standard_normal(), rng2.standard_normal(3)) for _ in range(200)]
desviacion, resto6 = {}, {}
for eps in (0.4, 0.2, 0.1, 0.05):
    dv, r6 = 0.0, 0.0
    for c, x, d_, y in pares:
        n = nu_estable(expm(1j * eps * gen_u2(c, x)), expm(1j * eps * gen_u2(d_, y)))
        lider = eps ** 4 * np.linalg.norm(np.cross(x, y)) ** 2 / 8
        dv = max(dv, abs(n / lider - 1))
        r6 = max(r6, abs(n - lider) / eps ** 6)
    desviacion[str(eps)], resto6[str(eps)] = dv, r6
dvs, r6s = list(desviacion.values()), list(resto6.values())
assert all(3.5 < dvs[k] / dvs[k + 1] < 4.5 for k in range(1, len(dvs) - 1)) and dvs[-1] < 2e-2   # relativo O(ε²)
assert max(r6s) < 2 * min(r6s)                                         # el resto es O(ε⁶)

xa = np.array([0.3, -0.5, 0.8])
ortogonal = np.cross(xa, [1.0, 0.0, 0.0])
X_a = gen_u2(0.7, xa)                                                  # no central
Y_alineado = gen_u2(-1.3, 1.7 * xa)                                    # no central, misma dirección en su(2)
Y_no_alineado = gen_u2(-1.3, 1.7 * ortogonal)
nu_al = nu(expm(1j * X_a), expm(1j * Y_alineado))
nu_no = nu(expm(1j * X_a), expm(1j * Y_no_alineado))
assert abs(nu_al) < 1e-14 and nu_no > 1e-2


def coordenadas(M):
    """M hermítica = Σ m_j B_j, con B = (I/2, σ1/2, σ2/2, σ3/2) y tr(B_j B_k) = δ_jk/2."""
    return np.array([2 * np.trace(M @ B).real for B in [I2 / 2] + T])


def matriz_ad(X):
    return np.column_stack([coordenadas(-1j * (X @ B - B @ X)) for B in [I2 / 2] + T])


def dim_nucleo(M):
    return int(M.shape[1] - np.linalg.matrix_rank(M, tol=1e-12))


nucleo = {"X_central": dim_nucleo(matriz_ad(gen_u2(1.0, np.zeros(3)))),
          "X_no_central": dim_nucleo(matriz_ad(X_a)),
          "comun_a_todas_las_X": dim_nucleo(np.vstack([matriz_ad(B) for B in [I2 / 2] + T]))}
v_comun = np.linalg.svd(np.vstack([matriz_ad(B) for B in [I2 / 2] + T]))[2][-1]
assert nucleo == {"X_central": 4, "X_no_central": 2, "comun_a_todas_las_X": 1}
assert abs(abs(v_comun[0]) - 1) < 1e-12                               # el núcleo común es el centro
salida["H_separacion_3_mas_1"] = {
    "error_forma_cerrada_eps_1": errH,
    "desviacion_relativa_max_respecto_de_eps4_xy2_8": desviacion,
    "resto_sobre_eps6_max": resto6,
    "control_no_centrales_alineados_nu": nu_al,
    "control_no_centrales_no_alineados_nu": nu_no,
    "control_no_alineados_forma_cerrada": float(2 * np.sin(np.linalg.norm(xa) / 2) ** 2 * np.sin(np.linalg.norm(1.7 * ortogonal) / 2) ** 2),
    "dimension_nucleo_de_la_comparacion": nucleo}

(Path(__file__).resolve().parent / "resultados.json").write_text(json.dumps(salida, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(salida, indent=2, ensure_ascii=False))
print("\nOK: todas las aserciones pasaron. Familia de acciones (Wilson como elección particular) y separación 3+1;"
      " clásico; no resuelve la brecha, no da el mecanismo de masas ni fija θ_W.")
