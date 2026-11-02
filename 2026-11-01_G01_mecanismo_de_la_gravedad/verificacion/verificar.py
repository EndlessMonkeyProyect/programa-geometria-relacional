#!/usr/bin/env python3
"""G–01 v1.3 — verificación reproducible de los resultados exactos [T] y de los controles [F].

Uso:  python3 verificar.py            (escribe resultados.json junto a este archivo)
      python3 verificar.py --no-escribir

Solo usa la biblioteca estándar de Python (3.9 o posterior). Cada sección tiene aserciones
propias: si un enunciado no se cumple, el programa termina con error. Las secciones siguen
las referencias del documento (§ y anexo B). Un control numérico se informa como control,
no como demostración general; las demostraciones están en el anexo B del documento.
"""
from __future__ import annotations
import itertools, json, math, sys
from fractions import Fraction as Fr
from math import gcd, isqrt
from pathlib import Path

R = {}

def lcm(a, b): return a * b // gcd(a, b)
def dot(u, v): return sum(a * b for a, b in zip(u, v))
def matvec(M, v): return tuple(sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M)))
def matmul(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def transpose(A): return tuple(zip(*A))

# ---------------------------------------------------------------- §3  espejos paralelos
def espejos(L=Fr(1), p=Fr(3, 10), prof=8):
    imagenes, frontera = {p}, {p}
    for _ in range(prof):
        nueva = set()
        for x in frontera:
            nueva |= {-x, 2 * L - x}
        frontera = nueva - imagenes; imagenes |= nueva
    teoria = {2 * n * L + s * p for n in range(-prof, prof + 1) for s in (1, -1)}
    assert imagenes <= teoria, "imagen fuera de 2nL ± p"
    cerca = {x for x in teoria if abs(x) <= 6 * L}
    assert cerca <= imagenes, "faltan imágenes cercanas"
    R["A_espejos_2nL_mas_menos_p"] = {"imagenes_generadas": len(imagenes), "todas_de_la_forma_2nL_pm_p": True}

# ---------------------------------------------------------------- §6, B1  K4 binario
def k4_xor():
    aristas = list(itertools.combinations(range(4), 2))
    pat = {tuple(s[i] ^ s[j] for i, j in aristas) for s in itertools.product((0, 1), repeat=4)}
    for patron in pat:
        b = dict(zip(aristas, patron))
        for i, j, k in itertools.combinations(range(4), 3):
            assert b[(i, j)] ^ b[(j, k)] ^ b[(i, k)] == 0
    assert len(pat) == 8
    R["B_K4_xor"] = {"patrones_compatibles": len(pat), "patrones_totales": 2 ** 6}

# ---------------------------------------------------------------- §4, B2  coloración
def cromatico(n, aristas):
    for k in range(1, n + 1):
        for c in itertools.product(range(k), repeat=n):
            if all(c[i] != c[j] for i, j in aristas):
                return k, c
def coloracion():
    k4 = list(itertools.combinations(range(4), 2))
    diamante = [e for e in k4 if e != (2, 3)]
    x4, _ = cromatico(4, k4); xd, cd = cromatico(4, diamante)
    assert x4 == 4 and xd == 3 and cd[2] == cd[3] and cd[0] != cd[1]
    R["C_coloracion"] = {"K4": x4, "K4_menos_e": xd, "en_el_diamante_3_y_4_comparten_color": True}

# ---------------------------------------------------------------- §7, B3  dos reflejos
def reflejos():
    import random
    rnd = random.Random(20261101)
    for _ in range(200):
        F = tuple(Fr(rnd.randint(-9, 9)) for _ in range(3)); D = tuple(Fr(rnd.randint(-9, 9)) for _ in range(3))
        xp = tuple(f + d for f, d in zip(F, D)); xm = tuple(f - d for f, d in zip(F, D))
        assert dot(xp, xp) - dot(xm, xm) == 4 * dot(F, D)
    F = (3.0, 0.0, 0.0); err = 0.0
    for t in (0.5, 1.0, 2.0, 5.0):
        D = (0.0, t, 0.0); xp = (3.0, t, 0.0); xm = (3.0, -t, 0.0)
        Rr = math.sqrt(dot(xp, xp)); R0 = 3.0
        delta = math.acos(dot(xp, xm) / Rr ** 2)
        err = max(err, abs(Rr ** 2 - (R0 ** 2 + t ** 2)), abs(Rr * math.cos(delta / 2) - R0))
    h = 1e-6; R0, Rr = 3.0, 5.0
    d1 = ((R0 / (Rr + h)) - (R0 / (Rr - h))) / (2 * h); d2 = ((R0 / (Rr + h)) ** 2 - (R0 / (Rr - h)) ** 2) / (2 * h)
    assert err < 1e-12 and abs(d1 + R0 / Rr ** 2) < 1e-8 and abs(d2 + 2 * R0 ** 2 / Rr ** 3) < 1e-8
    R["D_reflejos"] = {"identidad_4FD_exacta_en_200_casos": True, "error_max_R_cos_mitad_delta": err,
                       "derivada_aV": d1, "derivada_aV2": d2}

# ---------------------------------------------------------------- §8, B4, B5  tetraedro
V4 = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
def rango(M):
    M = [list(map(Fr, f)) for f in M]; r = 0
    for c in range(len(M[0])):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r
def tetraedro():
    import random
    rnd = random.Random(7)
    assert tuple(map(sum, zip(*V4))) == (0, 0, 0)
    assert matmul(transpose(V4), V4) == ((4, 0, 0), (0, 4, 0), (0, 0, 4))
    for _ in range(300):
        s = [Fr(rnd.randint(-20, 20)) for _ in range(4)]; S = sum(s)
        c = tuple(Fr(1, 4) * sum(s[i] * V4[i][k] for i in range(4)) for k in range(3))
        pred = [dot(V4[i], c) for i in range(4)]
        res = sum((s[i] - pred[i]) ** 2 for i in range(4))
        assert res == S ** 2 / 4
        if S == 0:
            assert pred == s and sum(x * x for x in s) == 4 * dot(c, c)
            f2 = sum(dot(tuple(s[i] / 3 * a for a in V4[i]), tuple(s[i] / 3 * a for a in V4[i])) for i in range(4))
            assert f2 == Fr(4, 3) * dot(c, c)
    # isotropía de Σ w_i v_i v_iᵀ: los términos fuera de la diagonal sólo se anulan con pesos iguales
    fuera = [[V4[i][a] * V4[i][b] for i in range(4)] for a, b in ((0, 1), (0, 2), (1, 2))]
    assert rango(fuera) == 3 and all(sum(f) == 0 for f in fuera)
    # grupo rotacional del tetraedro (A4): clausura de dos generadores
    g1 = ((1, 0, 0), (0, -1, 0), (0, 0, -1)); g2 = ((0, 0, 1), (1, 0, 0), (0, 1, 0))
    G = {((1, 0, 0), (0, 1, 0), (0, 0, 1))}; frontera = set(G)
    while frontera:
        nuevo = {matmul(g, h) for g in frontera for h in (g1, g2)} - G; G |= nuevo; frontera = nuevo
    assert len(G) == 12
    for g in G:
        assert sorted(matvec(g, v) for v in V4) == sorted(V4)
    c = (1, 2, 3); prom = tuple(sum(matvec(g, c)[k] for g in G) for k in range(3))
    sist = [tuple(g1[i][j] - (i == j) for j in range(3)) for i in range(3)] + [tuple(g2[i][j] - (i == j) for j in range(3)) for i in range(3)]
    assert prom == (0, 0, 0) and rango(sist) == 3
    R["E_tetraedro"] = {"casos_aleatorios": 300, "Emin_igual_S2_sobre_4": True, "norma_4_c2": True, "norma_proyecciones_4_3_c2": True,
                        "isotropia_exige_pesos_iguales": True, "orden_A4": len(G), "Fix_A4_es_cero": True}

# ---------------------------------------------------------------- §9  O45 regla de la cadena
def o45():
    def Rz(a): return ((math.cos(a), -math.sin(a), 0), (math.sin(a), math.cos(a), 0), (0, 0, 1))
    def Rx(a): return ((1, 0, 0), (0, math.cos(a), -math.sin(a)), (0, math.sin(a), math.cos(a)))
    X = lambda t: (math.sin(t), t * t, 0.3 * t); l = lambda t: 2 + math.cos(t)
    A = lambda t: matmul(Rz(0.7 * t), Rx(0.4 * t * t)); y = lambda t: (math.cos(2 * t), t, math.sin(t))
    x = lambda t: tuple(Xi + l(t) * ai for Xi, ai in zip(X(t), matvec(A(t), y(t))))
    h = 1e-5; err = 0.0
    for t in (0.3, 1.1, 2.5):
        d = lambda f: tuple((a - b) / (2 * h) for a, b in zip(f(t + h), f(t - h)))
        v, Xd, yd = d(x), d(X), d(y); ld = (l(t + h) - l(t - h)) / (2 * h)
        Ad = tuple(tuple((A(t + h)[i][j] - A(t - h)[i][j]) / (2 * h) for j in range(3)) for i in range(3))
        At = transpose(A(t)); Om = matmul(At, Ad)
        rhs = tuple(a / l(t) - ld / l(t) * yi - o for a, yi, o in zip(matvec(At, tuple(vi - xi for vi, xi in zip(v, Xd))), y(t), matvec(Om, y(t))))
        err = max(err, max(abs(a - b) for a, b in zip(rhs, yd)), max(abs(Om[i][j] + Om[j][i]) for i in range(3) for j in range(3)))
    assert err < 1e-7
    R["F_O45_regla_de_la_cadena"] = {"error_max": err}

# ---------------------------------------------------------------- §9, B7  MF-43
def mf43(n=8, eta=0.5):
    err = 0.0
    for k in (1, 3, 6):
        lam = 2 - 2 * math.cos(math.pi * k / (n + 1)); u = [math.sin(math.pi * k * (j + 1) / (n + 1)) for j in range(n)]
        Om = 2 * math.asin(math.sqrt(eta * lam) / 2)
        Lx = lambda z: [2 * z[j] - (z[j - 1] if j > 0 else 0) - (z[j + 1] if j < n - 1 else 0) for j in range(n)]
        x0, x1 = u[:], [uj * math.cos(Om) for uj in u]
        for m in range(2, 300):
            L1 = Lx(x1); x2 = [2 * a - b - eta * c for a, b, c in zip(x1, x0, L1)]
            err = max(err, max(abs(a - uj * math.cos(m * Om)) for a, uj in zip(x2, u))); x0, x1 = x1, x2
    assert err < 1e-9
    R["G_MF43_dispersion"] = {"error_max": err, "eta": eta}

# ---------------------------------------------------------------- §13, B8, B11  potenciales y órbitas
def potenciales_y_orbitas():
    h = 1e-6; err = 0.0
    for p in (1, 2):
        Phi = lambda R: -(R0 / R) ** p; R0 = 1.3
        for Rr in (2.0, 5.0):
            num = -(Phi(Rr + h) - Phi(Rr - h)) / (2 * h); err = max(err, abs(num - (-p * R0 ** p / Rr ** (p + 1))))
    assert err < 1e-7
    estable = {}
    for p in (0.5, 1.0, 1.5, 1.9, 2.5):
        k, Rc = 1.0, 1.0; l2 = p * k * Rc ** (2 - p)
        U2 = 3 * l2 / Rc ** 4 - p * (p + 1) * k * Rc ** (-p - 2)
        estable[str(p)] = U2 > 0; assert (U2 > 0) == (p < 2)
    def orbita(p, pert=0.02, pasos=200000, dt=1e-3):
        k = 1.0; x, y = 1.0, 0.0; vt = math.sqrt(p * k) * (1 + pert); vx, vy = 0.0, vt
        acc = lambda x, y: tuple(-p * k * c / math.hypot(x, y) ** (p + 2) for c in (x, y))
        ax, ay = acc(x, y); rmin = rmax = 1.0
        for _ in range(pasos):
            vx += 0.5 * dt * ax; vy += 0.5 * dt * ay; x += dt * vx; y += dt * vy
            r = math.hypot(x, y); rmin, rmax = min(rmin, r), max(rmax, r)
            if r < 0.05 or r > 50: return rmin, rmax, False
            ax, ay = acc(x, y); vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
        return rmin, rmax, True
    o1 = orbita(1); o2 = orbita(2)
    assert o1[2] and 0.9 < o1[0] and o1[1] < 1.2 and not o2[2]
    R["H_potenciales_y_orbitas"] = {"error_max_aceleracion": err, "circular_estable_por_p": estable,
                                    "p1_orbita_perturbada_acotada": True, "p1_rmin": o1[0], "p1_rmax": o1[1],
                                    "p2_orbita_perturbada_escapa_o_cae": True}

# ---------------------------------------------------------------- §11, B10  peso del estado sintonizado
def sintonia():
    K = lambda r: 1.0 / r; h = 1e-6; r = 2.0
    V1 = lambda r, d: K(r) * (1 - math.cos(d)); V2 = lambda r, d: -K(r) * math.cos(d)
    F1 = -(V1(r + h, 0) - V1(r - h, 0)) / (2 * h); F2 = -(V2(r + h, 0) - V2(r - h, 0)) / (2 * h)
    Kp = -1 / r ** 2
    assert abs(F1) < 1e-12 and abs(F2 - Kp) < 1e-8 and F2 < 0
    R["I_sintonia_B10"] = {"fuerza_con_1_menos_cos": F1, "fuerza_con_menos_cos": F2, "K_prima": Kp, "atractiva": True}

# ---------------------------------------------------------------- §12, B12  primer y segundo orden
def primer_y_segundo_orden():
    W = lambda x, y: -1 / math.hypot(x, y); gW = lambda x, y: tuple(c / math.hypot(x, y) ** 3 for c in (x, y))
    x, y, vx, vy, dt = 1.0, 0.0, 0.0, 1.0, 1e-3
    E0 = 0.5 * (vx * vx + vy * vy) + W(x, y); deriva = 0.0; gx, gy = gW(x, y)
    for _ in range(20000):
        vx -= 0.5 * dt * gx; vy -= 0.5 * dt * gy; x += dt * vx; y += dt * vy; gx, gy = gW(x, y)
        vx -= 0.5 * dt * gx; vy -= 0.5 * dt * gy
        deriva = max(deriva, abs(0.5 * (vx * vx + vy * vy) + W(x, y) - E0) / abs(E0))
    x, y = 1.0, 0.0; Wprev = W(x, y); monotona = True
    for _ in range(2000):
        gx, gy = gW(x, y); x -= 1e-4 * gx; y -= 1e-4 * gy
        Wn = W(x, y); monotona &= Wn <= Wprev; Wprev = Wn
    assert deriva < 1e-6 and monotona
    R["J_B12_orden"] = {"deriva_relativa_energia_segundo_orden": deriva, "primer_orden_W_monotona_decreciente": True}

# ---------------------------------------------------------------- §2B, B13, B14  O40 y YM-02
def o40_ym02():
    assert lcm(2, 3) == 6 and Fr(1, 2) - Fr(1, 3) == Fr(1, 6)
    for N in range(1, 13):
        for m in range(1, 13):
            M = next(M for M in itertools.count(1) if all((Fr(j, N) * M).denominator == 1 for j in range(N)) and all((Fr(k, m) * M).denominator == 1 for k in range(m)))
            assert M == lcm(N, m)
            L = lcm(N, m)
            for x in range(L):
                for y2 in range(L):
                    assert ((x - y2) % N == 0 and (x - y2) % m == 0) == ((x - y2) % L == 0)
            fibra = sum(1 for z in range(L) if z % N == 0)
            assert fibra == L // N == m // gcd(N, m)
    R["K_O40_YM02"] = {"mcm_2_3": 6, "diferencia": "1/6", "minimalidad_y_fibras_hasta_12": True}

# ---------------------------------------------------------------- §2C, B15, B16  O58
def soluciones(Nmax):
    s = set()
    for N in range(1, Nmax + 1):
        t = N * N - 1; a = 0
        while a * a <= t:
            r = t - a * a; b = isqrt(r)
            if b * b == r: s.add((a, b, N))
            a += 1
    return s
def o58(S):
    for t in ((2, 2, 3), (4, 8, 9), (70, 70, 99)): assert t in S
    ramas = []
    for (a2, b2, M) in sorted(S, key=lambda t: (t[2], t[0])):
        if M % 3 == 0 and M > 3 and M <= 200 and a2 <= b2:
            q = M // 3
            bal = (a2 * a2 - q * q * 4) + (b2 * b2 - q * q * 4) + (1 - q * q)
            assert bal == 0; ramas.append([a2, b2, M])
    a, b, N, q = 2, 2, 3, 5
    assert (q * N) ** 2 - (q * a) ** 2 - (q * b) ** 2 == q * q
    R["L_O58"] = {"ternas_citadas_validas": True, "ramas_desde_2_2_3_hasta_200": ramas, "balance_B15_cero_en_todas": True, "B16_residuo_bruto_q2": True}

# ---------------------------------------------------------------- §2D, B18–B20  hiperboloide
M1 = ((1, -2, 2), (2, -1, 2), (2, -2, 3)); M2 = ((1, 2, 2), (2, 1, 2), (2, 2, 3)); M3 = ((-1, 2, 2), (-2, 1, 2), (-2, 2, 3))
J = ((1, 0, 0), (0, 1, 0), (0, 0, -1))
def hiperboloide(S):
    for (a, b, N) in S:
        assert 1 - Fr(a * a + b * b, N * N) == Fr(1, N * N)
    v2 = Fr(8, 9); assert 1 - v2 == Fr(1, 9)
    for M in (M1, M2, M3): assert matmul(matmul(transpose(M), J), M) == J
    sin_dos_negativos = True; descenso_ok = True; prod_aristas = set()
    for (a, b, N) in S:
        if N == 1: continue
        x, y, Np = a + 2 * b - 2 * N, 2 * a + b - 2 * N, 3 * N - 2 * a - 2 * b
        sin_dos_negativos &= not (x < 0 and y < 0)
        padre = (abs(x), abs(y), Np); descenso_ok &= (0 < Np < N) and padre in S
        gen = M2 if (x >= 0 and y >= 0) else (M1 if y < 0 else M3)
        descenso_ok &= matvec(gen, padre) == (a, b, N)
        prod_aristas.add(N * Np - a * abs(x) - b * abs(y))
    assert sin_dos_negativos and descenso_ok
    Nmax = max(t[2] for t in S); vistos = []; pila = [(2, 2, 3)]
    while pila:
        v = pila.pop(); vistos.append(v)
        for M in (M1, M2, M3):
            w = matvec(M, v)
            if w[2] <= Nmax: pila.append(w)
    objetivo = {t for t in S if t[2] > 1}
    assert len(vistos) == len(set(vistos)) == len(objetivo) and set(vistos) == objetivo
    hijos = [matvec(M, (2, 2, 3)) for M in (M1, M2, M3)]
    assert hijos == [(4, 8, 9), (12, 12, 17), (8, 4, 9)] and matvec(M2, (12, 12, 17)) == (70, 70, 99)
    eta1 = math.log(3 + 2 * math.sqrt(2)); pell = []; N_, a_ = 3, 2
    for k in range(1, 7):
        pell.append([N_, a_]); assert N_ * N_ - 2 * a_ * a_ == 1 and abs(math.acosh(N_) / eta1 - k) < 1e-9
        N_, a_ = 3 * N_ + 4 * a_, 2 * N_ + 3 * a_
    N_, m_ = 3, 2; anidada = [3]
    for _ in range(2):
        N_, m_ = N_ * (4 * N_ * N_ - 3), m_ * (4 * N_ * N_ - 1); assert N_ * N_ - 2 * m_ * m_ == 1; anidada.append(N_)
    assert anidada == [3, 99, 3880899] and abs(math.acosh(99) / eta1 - 3) < 1e-9 and abs(math.acosh(3880899) / eta1 - 9) < 1e-6
    mk = lambda X, Y: X[2] * Y[2] - X[0] * Y[0] - X[1] * Y[1]
    assert mk((2, 2, 3), (4, 8, 9)) == 3 and mk((2, 2, 3), (70, 70, 99)) == 17
    peq = [t for t in S if 3 < t[2] <= 120 and t[0] <= t[1]]
    mult = sorted(t for t in peq if t[2] % (3 * t[2] - 2 * t[0] - 2 * t[1]) == 0)
    assert len(peq) == 15 and mult == [(4, 8, 9), (22, 46, 51)]
    R["M_hiperboloide"] = {
        "Nmax": Nmax, "soluciones_N_mayor_que_1": len(objetivo), "alcanzadas_por_el_arbol": len(set(vistos)),
        "B18_uno_menos_v2_igual_1_sobre_N2": True, "generadores_conservan_la_forma": True,
        "patron_dos_negativos_ausente": True, "descenso_unico_correcto": True,
        "hijos_de_2_2_3": [list(h) for h in hijos], "primeros_productos_de_Minkowski_en_aristas": sorted(prod_aristas)[:6],
        "eta1": eta1, "pell": pell, "cadena_anidada_O58": anidada,
        "cosh_d_2_2_3_a_4_8_9": 3, "cosh_d_2_2_3_a_70_70_99": 17,
        "soluciones_3_menor_N_hasta_120_a_menor_b": len(peq), "con_N_multiplo_del_padre": [list(t) for t in mult]}

# ---------------------------------------------------------------- §2B, B21  resolución finita
def q_eps(alpha, eps):
    q = 1
    while True:
        p = round(alpha * q)
        if abs(alpha - Fr(p, q)) <= eps: return q, Fr(p, q)
        q += 1
def resolucion_finita():
    pares = [(Fr(1, 2), Fr(1, 3)), (Fr(1, 2), Fr(50, 99)), (Fr(1, 2), Fr(501, 1000))]
    exacto = [lcm(a.denominator, b.denominator) for a, b in pares]
    res = {}
    for eps in (Fr(1, 100), Fr(1, 1000)):
        res[str(eps)] = [lcm(q_eps(a, eps)[0], q_eps(b, eps)[0]) for a, b in pares]
    assert exacto == [6, 198, 1000] and res["1/100"] == [6, 2, 2] and res["1/1000"] == [6, 166, 2]
    assert q_eps(Fr(50, 99), Fr(1, 1000))[1] == Fr(42, 83)
    import random
    rnd = random.Random(31); peor = 0.0
    muestras = [Fr(math.sqrt(2)), Fr(math.pi), Fr(math.e), Fr((1 + math.sqrt(5)) / 2)] + [Fr(rnd.random()) for _ in range(400)]
    for al in muestras:
        for den in (2, 3, 7, 10, 50, 100, 333, 1000):
            eps = Fr(1, den); q, _ = q_eps(al, eps)
            assert q <= math.ceil(1 / eps); peor = max(peor, q / math.ceil(1 / eps))
    R["N_resolucion_finita"] = {"mcm_exacto": exacto, "L_eps": res, "aproximacion_50_99_a_1_1000": "42/83",
                                "cota_Dirichlet_cumplida": True, "max_q_sobre_cota": peor}

# ---------------------------------------------------------------- §16  legado numérico
def legado():
    techo = math.sqrt(16 / 15); dif = abs(2.037 - 2.05) / 2.05
    assert abs(techo - 1.0327955589886444) < 1e-12 and dif < 0.01
    R["O_legado_TOV"] = {"raiz_16_15": techo, "diferencia_relativa_con_SLy_RG": dif}

def main():
    espejos(); k4_xor(); coloracion(); reflejos(); tetraedro(); o45(); mf43(); potenciales_y_orbitas()
    sintonia(); primer_y_segundo_orden(); o40_ym02()
    S = soluciones(3000); o58(S); hiperboloide(S); resolucion_finita(); legado()
    R["_resumen"] = {"secciones": len(R), "todas_las_aserciones_pasaron": True}
    if "--no-escribir" not in sys.argv:
        Path(__file__).with_name("resultados.json").write_text(json.dumps(R, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"OK — {len(R) - 1} secciones verificadas")

if __name__ == "__main__":
    main()
