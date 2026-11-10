#!/usr/bin/env python3
"""Laboratorio de convergencia: programa relacional, OpenAI y Anthropic (9-nov-2026).

Uso:  python3 -I laboratorio_convergencia.py [C1 C2 ...]   (sin argumentos: todos)
Escribe resultados_convergencia.json en el directorio actual.

C1  Cruce por bits (Anthropic, Ap. H y README): piezas B_j = 2^j·binom(N, j), rangos y rho.
C2  Ocho cuadrados (Anthropic, Lema 2): A_i como polinomio en N, rangos exactos y rho.
C3  Matriz M0 de OpenAI (§2.7, paso 2): M0 = (-1)^N f(N), soporte, ventana y medidas.
C4  Misma operación: V0 de OpenAI (r = 2) es el SWAP por bits de Anthropic.
C5  Unicidad del referente frente a construcción: Hermite (OpenAI §2.5) y residuos enteros.
C6  Raíz única compatible (atlas ternario de ROSI): umbral 3·2^(d-1) en F2^n y retracción.
C7  Familia XOR + cláusulas OR: herencia afín con novedad por inclusión-exclusión,
    eliminación de variables y fuerza bruta sobre las mismas instancias.
C8  Ventana de OpenAI demasiado estrecha: el cambio de referencia encarece.
"""
import itertools, json, math, random, sys, time
from fractions import Fraction
import numpy as np

RES = {}

def log(*a):
    print(*a, flush=True)

# ---------------------------------------------------------------- utilidades
def rank_mod_p(M, p=2147483629):
    """Rango exacto de una matriz entera módulo un primo grande (cota inferior del rango sobre Q)."""
    A = np.array(M, dtype=np.int64) % p
    n, m = A.shape
    r = 0
    for c in range(m):
        if r == n:
            break
        piv = np.nonzero(A[r:, c])[0]
        if piv.size == 0:
            continue
        i = r + piv[0]
        if i != r:
            A[[r, i]] = A[[i, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        col = A[:, c].copy(); col[r] = 0
        nz = np.nonzero(col)[0]
        if nz.size:
            A[nz] = (A[nz] - np.outer(col[nz], A[r]) % p) % p
        r += 1
    return r

def rank_float(M):
    return int(np.linalg.matrix_rank(np.asarray(M, dtype=float)))

def binom_op(N, j):
    """binom(N, j) para una matriz diagonalizable N (polinomio de grado j)."""
    D = N.shape[0]
    out = np.eye(D)
    for i in range(j):
        out = out @ (N - i * np.eye(D)) / (i + 1)
    return out

def as_matrix(T, lam, rows):
    """T: tensor con ejes [x1,y1,u1,v1, x2,...]; rows: dos letras de 'xyuv' para filas."""
    pos = {'x': 0, 'y': 1, 'u': 2, 'v': 3}
    cols = [c for c in 'xyuv' if c not in rows]
    order = [4 * s + pos[c] for c in rows for s in range(lam)] + \
            [4 * s + pos[c] for c in cols for s in range(lam)]
    side = 2 ** (2 * lam) if T.shape[0] == 2 else T.shape[0] ** (2 * lam)
    return np.transpose(T, order).reshape(side, -1)

# ---------------------------------------------------------------- C1
def C1():
    log("\n== C1 · cruce por bits: SWAP = I - 2P_singlete, piezas por número de singletes ==")
    b = (0, 1)
    I1 = np.zeros((2,) * 4, dtype=np.int64)   # [x=u][y=v]
    S1 = np.zeros((2,) * 4, dtype=np.int64)   # [x!=y](-1)^x [u!=v](-1)^u
    X1 = np.zeros((2,) * 4, dtype=np.int64)   # cruce [x=v][y=u]
    s = lambda p, q: (1 if p != q else 0) * (-1) ** p
    for x, y, u, v in itertools.product(b, repeat=4):
        I1[x, y, u, v] = int(x == u and y == v)
        S1[x, y, u, v] = s(x, y) * s(u, v)
        X1[x, y, u, v] = int(x == v and y == u)
    assert np.array_equal(X1, I1 - S1)
    out = {"identidad_por_bit": "[x=v][y=u] = [x=u][y=v] - [x!=y](-1)^x [u!=v](-1)^u : comprobada en 16 casos"}
    filas = []
    for lam in range(1, 6):
        coef = [np.ones((), dtype=np.int64)]
        X = np.ones((), dtype=np.int64)
        for _ in range(lam):
            new = [np.multiply.outer(coef[0], I1)]
            for j in range(1, len(coef)):
                new.append(np.multiply.outer(coef[j], I1) + np.multiply.outer(coef[j - 1], S1))
            new.append(np.multiply.outer(coef[-1], S1))
            coef = new
            X = np.multiply.outer(X, X1)
        # identidad exacta: cruce = sum_j (-1)^j B_j
        tot = sum(((-1) ** j) * coef[j] for j in range(lam + 1))
        ok_sum = bool(np.array_equal(tot, X))
        # operador número N (disposición por filas (x,y)|(u,v)): N = sum_s P_s, P = S1/2
        P = as_matrix(S1, 1, 'xy') / 2.0
        Id4 = np.eye(4)
        N = np.zeros((4 ** lam, 4 ** lam))
        for k in range(lam):
            term = np.ones((1, 1))
            for t in range(lam):
                term = np.kron(term, P if t == k else Id4)
            N += term
        # mismo orden de índices que as_matrix(..., 'xy') con lam bits: filas (x1..,y1..)
        # construimos los B_j también con kron por bit para comparar sin reordenar
        Bk = [np.ones((1, 1))]
        Im, Sm = as_matrix(I1, 1, 'xy'), as_matrix(S1, 1, 'xy')
        for _ in range(lam):
            nb = [np.kron(Bk[0], Im)]
            for j in range(1, len(Bk)):
                nb.append(np.kron(Bk[j], Im) + np.kron(Bk[j - 1], Sm))
            nb.append(np.kron(Bk[-1], Sm))
            Bk = nb
        ok_poly = all(np.allclose(Bk[j], (2 ** j) * binom_op(N, j)) for j in range(lam + 1))
        Xm = np.ones((1, 1))
        for _ in range(lam):
            Xm = np.kron(Xm, as_matrix(X1, 1, 'xy'))
        ok_parity = bool(np.allclose(Xm, sum(((-2.0) ** j) * binom_op(N, j) for j in range(lam + 1))))
        piezas = []
        for j in range(lam + 1):
            rf = rank_mod_p(as_matrix(coef[j], lam, 'xy'))
            rc = rank_mod_p(as_matrix(coef[j], lam, 'xu'))
            fr = sum(math.comb(lam, z) * 3 ** (lam - z) for z in range(j, lam + 1))
            fc = sum(math.comb(lam, z) * 3 ** (lam - z) for z in range(lam - j, lam + 1))
            piezas.append({"j_singletes": j, "rango_filas": rf, "rango_columnas": rc,
                           "formula_filas": fr, "formula_columnas": fc})
        worst = max(math.log2(p["rango_filas"] * p["rango_columnas"]) for p in piezas)
        filas.append({"lambda": lam, "suma_con_signo_igual_al_cruce": ok_sum,
                      "B_j_igual_2^j_binom(N,j)": bool(ok_poly),
                      "cruce_igual_(-1)^N": ok_parity,
                      "piezas": piezas, "bits_por_bit_peor_pieza": worst / lam,
                      "rho_rangos": worst / (4 * lam)})
        log(f"lambda={lam}: suma ok={ok_sum}, B_j=2^j binom(N,j) {ok_poly}, cruce=(-1)^N {ok_parity}, "
            f"rho={worst/(4*lam):.4f}; formulas coinciden="
            f"{all(p['rango_filas']==p['formula_filas'] and p['rango_columnas']==p['formula_columnas'] for p in piezas)}")
    lim = {}
    for lam in (10, 100, 1000, 10000):
        w = [math.comb(lam, z) * 3 ** (lam - z) for z in range(lam + 1)]
        suf = [0] * (lam + 2)
        for z in range(lam, -1, -1):
            suf[z] = suf[z + 1] + w[z]
        best = max(math.log2(suf[j]) + math.log2(suf[lam - j]) for j in range(lam + 1))
        lim[lam] = best / (4 * lam)
    out.update({"por_lambda": filas, "rho_por_formula": lim, "limite_log2_12_sobre_4": math.log2(12) / 4})
    log("rho por fórmula:", {k: round(v, 4) for k, v in lim.items()}, " límite", round(math.log2(12) / 4, 4))
    RES["C1"] = out

# ---------------------------------------------------------------- C2
def sigma8(p, q):
    p1, p2, p3 = (p >> 2) & 1, (p >> 1) & 1, p & 1
    q1, q2, q3 = (q >> 2) & 1, (q >> 1) & 1, q & 1
    P, Qv = (p1, p2, p3), (q1, q2, q3)
    phi = sum(P[i] * Qv[j] for i in range(3) for j in range(i, 3))
    phi += q1 * p2 * p3 + p1 * q2 * p3 + p1 * p2 * q3
    return -1 if phi % 2 else 1

def C2():
    log("\n== C2 · ocho cuadrados: A_i como polinomio del operador número ==")
    B = range(8)
    fallos = 0
    for x, y, u, v in itertools.product(B, repeat=4):
        lhs = 2 * int(x == v and y == u)
        rhs = int((x ^ y ^ u ^ v) == 0) * (sigma8(x, y) * sigma8(v, u) + sigma8(x, u) * sigma8(v, y))
        fallos += int(lhs != rhs)
    R = np.zeros((8,) * 4, dtype=np.int64); C = np.zeros_like(R)
    for x, y, u, v in itertools.product(B, repeat=4):
        R[x, y, u, v] = int((x ^ y) == (v ^ u)) * sigma8(x, y) * sigma8(v, u)
        C[x, y, u, v] = int((x ^ u) == (v ^ y)) * sigma8(x, u) * sigma8(v, y)
    Rxyvu = np.transpose(R, (0, 1, 3, 2)).reshape(64, 64)   # filas (x,y), columnas (v,u)
    Cxyvu = np.transpose(C, (0, 1, 3, 2)).reshape(64, 64)
    ok_idemp = bool(np.array_equal(Rxyvu @ Rxyvu, 8 * Rxyvu))
    ok_comp = bool(np.array_equal(Rxyvu + Cxyvu, 2 * np.eye(64, dtype=np.int64)))
    ok_sym = bool(np.array_equal(C, np.transpose(R, (0, 2, 1, 3))))   # C(x,y,u,v) = R(x,u,y,v)
    out = {"fallos_identidad_(12)_en_4096": fallos, "R^2=8R": ok_idemp, "R+C=2Id": ok_comp,
           "C(x,y,u,v)=R(x,u,y,v)": ok_sym, "rango_R_xy|vu": rank_float(Rxyvu)}
    log(f"identidad (12): {fallos} fallos de 4096; R^2=8R {ok_idemp}; R+C=2Id {ok_comp}; C=R con y<->u {ok_sym}")
    Q = Rxyvu / 8.0
    filas = []
    for t in (1, 2):
        # A_i desde la definición: coeficientes de prod_s (R_s + T C_s) en la disposición (x,y)|(v,u)
        polys = [np.ones((1, 1))]
        for _ in range(t):
            new = [np.kron(polys[0], Rxyvu)]
            for i in range(1, len(polys)):
                new.append(np.kron(polys[i], Rxyvu) + np.kron(polys[i - 1], Cxyvu))
            new.append(np.kron(polys[-1], Cxyvu))
            polys = new
        D = 64 ** t
        Nop = np.zeros((D, D))
        for k in range(t):
            term = np.ones((1, 1))
            for s_ in range(t):
                term = np.kron(term, Q if s_ == k else np.eye(64))
            Nop += term
        # predicción: A_i = sum_k binom(N,k) [T^i] (2T)^(t-k) (8(1-T))^k
        def coef_T(i, k):
            c = 0
            for a in range(k + 1):     # (8(1-T))^k = sum_a C(k,a) 8^k (-T)^a
                if (t - k) + a == i:
                    c += math.comb(k, a) * 8 ** k * (-1) ** a * 2 ** (t - k)
            return c
        ok = True
        for i in range(t + 1):
            pred = sum(coef_T(i, k) * binom_op(Nop, k) for k in range(t + 1))
            ok &= bool(np.allclose(polys[i], pred))
        # simetría A_i(x,u,y,v) = A_{t-i}(x,y,u,v): rango por columnas = rango por filas de A_{t-i}
        piezas = []
        for i in range(t + 1):
            rf = sum(math.comb(t, j) * 8 ** j * 56 ** (t - j) for j in range(t - i, t + 1))
            rc = sum(math.comb(t, j) * 8 ** j * 56 ** (t - j) for j in range(i, t + 1))
            piezas.append({"i": i, "rango_filas_formula": rf, "rango_columnas_formula": rc,
                           "cota_Lema2_filas": 2 ** min(6 * t, 4 * t + 3 * i),
                           "cota_Lema2_columnas": 2 ** min(6 * t, 7 * t - 3 * i)})
        if t == 1:
            for p_, i in zip(piezas, range(2)):
                T4 = polys[i].reshape(8, 8, 8, 8)              # ejes x,y,v,u
                T4 = np.transpose(T4, (0, 1, 3, 2))            # x,y,u,v
                p_["rango_filas_medido"] = rank_float(T4.reshape(64, 64))
                p_["rango_columnas_medido"] = rank_float(np.transpose(T4, (0, 2, 1, 3)).reshape(64, 64))
        if t == 2:
            # una medición directa por columnas en la pieza central (4096 x 4096)
            T8 = polys[1].reshape(8, 8, 8, 8, 8, 8, 8, 8)      # x1,y1,x2,y2 | v1,u1,v2,u2
            T8 = np.transpose(T8, (0, 1, 2, 3, 5, 4, 7, 6))     # x1,y1,x2,y2,u1,v1,u2,v2
            col = np.transpose(T8, (0, 2, 4, 6, 1, 3, 5, 7)).reshape(4096, 4096)  # (x,u)|(y,v)
            piezas[1]["rango_columnas_medido"] = rank_float(col)
            piezas[1]["rango_filas_medido"] = rank_float(polys[1])
        worst = max(math.log2(p_["rango_filas_formula"]) + math.log2(p_["rango_columnas_formula"]) for p_ in piezas)
        filas.append({"t_bloques": t, "A_i_igual_polinomio_en_N": ok, "piezas": piezas,
                      "rho_rangos": worst / (12 * t)})
        log(f"t={t}: A_i = polinomio en N: {ok}; piezas {[(p_['rango_filas_formula'], p_['rango_columnas_formula']) for p_ in piezas]}")
        log("   medidos:", [(p_.get('rango_filas_medido'), p_.get('rango_columnas_medido')) for p_ in piezas])
    lim = {}
    for t in (10, 100, 1000, 10000):
        w = [math.comb(t, j) * 8 ** j * 56 ** (t - j) for j in range(t + 1)]
        suf = [0] * (t + 2)
        for j in range(t, -1, -1):
            suf[j] = suf[j + 1] + w[j]
        best = max(math.log2(suf[t - i]) + math.log2(suf[i]) for i in range(t + 1))
        lim[t] = best / (12 * t)
    out.update({"por_t": filas, "rho_rangos_por_formula": lim,
                "limite_(2+log2_448)/12": (2 + math.log2(448)) / 12, "rho_conteo_Lema2": 11 / 12})
    log("rho (rangos):", {k: round(v, 4) for k, v in lim.items()}, " límite", round((2 + math.log2(448)) / 12, 4),
        " conteo del Lema 2: 11/12 =", round(11 / 12, 4))
    RES["C2"] = out

# ---------------------------------------------------------------- C3, C4
def lagrange_coefs_forward(I_pts, deg_max):
    """f de grado < len(I) con f(j) = (-1)^j en I; devuelve los valores f(0..Q) y diferencias a_k."""
    def f(x):
        tot = Fraction(0)
        for i, xi in enumerate(I_pts):
            term = Fraction((-1) ** xi)
            for jj, xj in enumerate(I_pts):
                if jj != i:
                    term *= Fraction(x - xj, xi - xj)
            tot += term
        return tot
    return f

def build_M0(r, Q, R):
    p = Fraction(r - 1, 2 * r)
    A0 = math.floor(Q * p - Fraction(R - 1, 2))
    A0 = max(0, min(A0, Q - R + 1))
    I_pts = list(range(A0, A0 + R))
    f = lagrange_coefs_forward(I_pts, R - 1)
    # diferencias hacia adelante: f(j) = sum_k a_k binom(j,k), a_k = 0 para k >= R
    vals = [f(j) for j in range(Q + 1)]
    a = []
    cur = vals[:]
    for k in range(Q + 1):
        a.append(cur[0])
        cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
    d = r * r
    Pi = np.zeros((d, d))
    for aa in range(r):
        for dd in range(r):
            u = aa * r + dd; w = dd * r + aa
            Pi[u, w] = 1.0                      # (Pi z)_u = z_{swap(u)}
    Id = np.eye(d)
    half = (Pi - Id) / 2.0                     # V0·P_s en la posición s
    coef = [np.ones((1, 1))]
    for _ in range(Q):
        new = [np.kron(coef[0], Pi)]
        for k in range(1, len(coef)):
            new.append(np.kron(coef[k], Pi) + np.kron(coef[k - 1], half))
        new.append(np.kron(coef[-1], half))
        coef = new
    M0 = sum(float(a[k]) * coef[k] for k in range(Q + 1) if a[k] != 0)
    V0 = coef[0]
    return dict(M0=M0, V0=V0, Pi=Pi, I_pts=I_pts, f=f, a=a, p=p, d=d)

def C3():
    log("\n== C3 · matriz M0 de OpenAI: M0 = V0 f(W0) con f(j) = (-1)^j en una ventana ==")
    out = []
    for (r, Q, R) in [(2, 5, 3), (2, 6, 3), (3, 3, 2)]:
        B = build_M0(r, Q, R)
        M0, V0, Pi, d = B["M0"], B["V0"], B["Pi"], B["d"]
        D = d ** Q
        ok_V0_parity = None
        if D <= 1024:
            # W0 = (1/2) sum_s (I - Pi_s);  V0 = (-1)^W0 = sum_j (-2)^j binom(W0, j)
            W0 = np.zeros((D, D))
            for k in range(Q):
                term = np.ones((1, 1))
                for s_ in range(Q):
                    term = np.kron(term, (np.eye(d) - Pi) / 2 if s_ == k else np.eye(d))
                W0 += term
            ok_V0_parity = bool(np.allclose(V0, sum(((-2.0) ** j) * binom_op(W0, j) for j in range(Q + 1))))
        # índices: u = sum_s (a_s r + d_s) d^(Q-1-s)
        digits = np.array([[(u // d ** (Q - 1 - s_)) for s_ in range(Q)] for u in range(D)]) % d
        A_ = digits // r; Dd = digits % r
        E = np.zeros((D, D), dtype=np.int64)
        for s_ in range(Q):
            E += (A_[None, :, s_] != Dd[:, None, s_]).astype(np.int64)   # E[u,w]: a_w(s) != d_u(s)
        nz = np.abs(M0) > 1e-12
        max_E_M0 = int(E[nz].max())
        max_E_V0 = int(E[np.abs(V0) > 1e-12].max())
        diag_viol = int((np.diag(E) > R - 1).sum())
        # base propia producto: e_aa, e_ab+e_ba (simétricos), e_ab-e_ba (antisimétricos)
        cols, labs = [], []
        for aa in range(r):
            v = np.zeros(d); v[aa * r + aa] = 1; cols.append(v); labs.append(0)
        for aa in range(r):
            for bb in range(aa + 1, r):
                v = np.zeros(d); v[aa * r + bb] = 1; v[bb * r + aa] = 1; cols.append(v); labs.append(0)
        for aa in range(r):
            for bb in range(aa + 1, r):
                v = np.zeros(d); v[aa * r + bb] = 1; v[bb * r + aa] = -1; cols.append(v); labs.append(1)
        Bpos = np.array(cols).T
        Psi = np.ones((1, 1)); jl = np.zeros(1, dtype=int)
        for _ in range(Q):
            Psi = np.kron(Psi, Bpos)
            jl = (jl[:, None] + np.array(labs)[None, :]).reshape(-1)
        G = Psi.T @ Psi
        Mt = Psi.T @ M0 @ Psi
        Ddiag = np.diag(Mt) / np.diag(G)
        offdiag = float(np.abs(Mt - np.diag(np.diag(Mt))).max())
        Vt = Psi.T @ V0 @ Psi
        ok_V0_diag = bool(np.allclose(np.diag(Vt) / np.diag(G), (-1.0) ** jl)) and \
            float(np.abs(Vt - np.diag(np.diag(Vt))).max()) < 1e-8
        pred = np.array([float(((-1) ** j) * B["f"](j)) for j in jl])
        ok_diag = bool(np.allclose(Ddiag, pred)) and offdiag < 1e-8
        fixed_in_window = bool(np.allclose(Ddiag[np.isin(jl, B["I_pts"])], 1.0))
        rank_IM = int(np.sum(np.abs(Ddiag - 1.0) > 1e-9))
        a_sym, b_alt = r * (r + 1) // 2, r * (r - 1) // 2
        tail = sum(math.comb(Q, j) * a_sym ** (Q - j) * b_alt ** j for j in range(Q + 1) if j not in B["I_pts"])
        rank_dense = rank_float(np.eye(D) - M0) if D <= 1024 else None
        row = {"r": r, "Q": Q, "R": R, "D": D, "ventana_I": B["I_pts"],
               "V0_igual_(-1)^N_por_binomios": ok_V0_parity, "V0_diagonal_(-1)^j_en_base_producto": ok_V0_diag,
               "M0_diagonal_en_base_producto_con_(-1)^j_f(j)": ok_diag,
               "M0_fija_la_ventana": fixed_in_window,
               "max_|E_uw|_en_soporte_de_M0": max_E_M0, "cota_R-1": R - 1,
               "max_|E_uw|_en_soporte_de_V0": max_E_V0,
               "indices_donde_la_identidad_viola_el_soporte": diag_viol,
               "rango(I-M0)_base_propia": rank_IM, "rango(I-M0)_denso": rank_dense,
               "cola_binomial_D·Pr[W fuera de I]": tail, "fraccion_medida": rank_IM / D}
        out.append(row)
        log(f"r={r} Q={Q} R={R} D={D}: V0=(-1)^N {ok_V0_parity}/{ok_V0_diag}; M0 diagonal {ok_diag}; fija ventana {fixed_in_window}; "
            f"max|E| soporte M0={max_E_M0}<= {R-1}; V0 -> {max_E_V0}; identidad viola en {diag_viol}/{D}; "
            f"rango(I-M0)={rank_IM} (denso {rank_dense}) cola={tail}")
    RES["C3"] = out

def C4():
    log("\n== C4 · la misma operación: V0 de OpenAI con r = 2 es el SWAP por bits del cruce de Anthropic ==")
    out = []
    for lam in range(1, 6):
        B = build_M0(2, lam, 1 if lam < 2 else 2)
        V0 = B["V0"]
        X1 = np.zeros((4, 4))
        for x, y, u, v in itertools.product((0, 1), repeat=4):
            X1[x * 2 + y, u * 2 + v] = float(x == v and y == u)
        Xm = np.ones((1, 1))
        for _ in range(lam):
            Xm = np.kron(Xm, X1)
        out.append({"lambda_igual_Q": lam, "V0_igual_cruce_por_filas": bool(np.array_equal(V0, Xm))})
    log(out)
    RES["C4"] = out

# ---------------------------------------------------------------- C5
def C5():
    log("\n== C5 · unicidad del referente (teorema chino del resto) frente al costo de construirlo ==")
    rng = random.Random(5)
    d = 12
    H = [Fraction(rng.randint(-9, 9)) for _ in range(d + 1)]           # coeficientes c_0..c_d
    pts = [1, 2, 3]
    def taylor(coefs, t, J):
        # coeficientes de z^0..z^{J-1} de H(t+z)
        out = []
        for jj in range(J):
            out.append(sum(c * math.comb(k, jj) * Fraction(t) ** (k - jj) for k, c in enumerate(coefs) if k >= jj))
        return out
    def solve(J):
        rows, rhs = [], []
        for t in pts:
            for jj, val in enumerate(taylor(H, t, J)):
                rows.append([Fraction(math.comb(k, jj)) * Fraction(t) ** (k - jj) if k >= jj else Fraction(0)
                             for k in range(d + 1)])
                rhs.append(val)
        # eliminación exacta; devuelve (rango, solución si es única)
        M = [r_[:] + [b_] for r_, b_ in zip(rows, rhs)]
        nr, nc = len(M), d + 1
        piv_cols, rk = [], 0
        for c in range(nc):
            pr = next((i for i in range(rk, nr) if M[i][c] != 0), None)
            if pr is None:
                continue
            M[rk], M[pr] = M[pr], M[rk]
            pv = M[rk][c]
            M[rk] = [e / pv for e in M[rk]]
            for i in range(nr):
                if i != rk and M[i][c] != 0:
                    fct = M[i][c]
                    M[i] = [e - fct * g for e, g in zip(M[i], M[rk])]
            piv_cols.append(c); rk += 1
        unique = rk == nc
        h0 = M[piv_cols.index(0)][-1] if (unique and 0 in piv_cols) else None
        return rk, unique, h0
    rk5, u5, h05 = solve(5)          # Q·J = 15 > 12
    rk4, u4, _ = solve(4)            # Q·J = 12, no basta
    # testigo de no unicidad: H + prod (T - t)^4 tiene los mismos datos y otro valor en 0
    prod0 = 1
    for t in pts:
        prod0 *= (-t) ** 4
    out = {"grado_H": d, "puntos": pts,
           "J=5 (QJ=15>12)": {"rango": rk5, "unica": u5, "H(0)_recuperado": str(h05), "H(0)_real": str(H[0])},
           "J=4 (QJ=12)": {"rango": rk4, "unica": u4,
                           "testigo": "H + prod_t (T-t)^4 da los mismos datos; H(0) cambia en %d" % prod0}}
    # análogo entero: x queda determinado por (x mod 12, x mod 18) solo en [0, mcm) = [0, 36)
    pares = {}
    for x in range(72):
        pares.setdefault((x % 12, x % 18), []).append(x)
    out["enteros_mod_12_y_18"] = {"mcm": 36, "mcd": 6, "clases_distintas_en_[0,72)": len(pares),
                                  "repeticiones": max(len(v) for v in pares.values()),
                                  "pares_compatibles_que_existen": len(pares), "pares_posibles": 12 * 18}
    log(json.dumps(out, ensure_ascii=False))
    RES["C5"] = out

# ---------------------------------------------------------------- C6
def flats(n, dim):
    pts = range(2 ** n)
    seen = set()
    for basis in itertools.combinations(range(1, 2 ** n), dim):
        span = {0}
        for bvec in basis:
            span |= {s ^ bvec for s in span}
        if len(span) != 2 ** dim:
            continue
        for off in pts:
            seen.add(frozenset(off ^ s for s in span))
    return [set(f) for f in seen]

def C6():
    log("\n== C6 · raíz única compatible: umbral 3·2^(d-1) para d-planos afines de F2^n ==")
    out = {}
    for (n, dim, sizes) in [(3, 2, range(4, 9)), (4, 2, range(4, 8)), (4, 3, range(8, 14))]:
        F = flats(n, dim)
        masks = [sum(1 << p for p in f) for f in F]
        tab = {}
        for k in sizes:
            mx, uno, total = 0, 0, 0
            for S in itertools.combinations(range(2 ** n), k):
                sm = sum(1 << p for p in S)
                c = sum(1 for m in masks if m & sm == m)
                mx = max(mx, c); total += 1; uno += int(c == 1)
            tab[k] = {"max_planos_contenidos": mx, "subconjuntos_con_exactamente_uno": uno, "subconjuntos": total}
        thr = 3 * 2 ** (dim - 1)
        out[f"F2^{n}, d={dim}"] = {"planos": len(F), "umbral_teorico": thr, "por_tamaño": tab}
        log(f"F2^{n}, d={dim}: {len(F)} planos; umbral {thr}; ",
            {k: v["max_planos_contenidos"] for k, v in tab.items()})
    # secuencia del atlas ternario 8 -> 7 -> 6 -> 5 -> 4: raíz única en 5, cierre o retracción en 4
    F = flats(3, 2)
    alcanza, retrae = 0, 0
    for a, b, c in itertools.permutations(range(8), 3):
        S = set(range(8)) - {a, b, c}
        roots = [f for f in F if f <= S]
        assert len(roots) == 1
        for e in S:
            S2 = S - {e}
            if any(f <= S2 for f in F):
                alcanza += 1
            else:
                retrae += 1
    out["atlas_ternario"] = {"secuencias_de_tres_exclusiones": 8 * 7 * 6,
                             "raiz_unica_en_5_estados": True,
                             "cuarta_exclusion_alcanza_el_cierre": alcanza,
                             "cuarta_exclusion_retrae_la_raiz": retrae,
                             "info": "log2(5/4)+log2(8/5) = %.12f" % (math.log2(5 / 4) + math.log2(8 / 5))}
    log(out["atlas_ternario"])
    RES["C6"] = out

# ---------------------------------------------------------------- C7
def gen_instance(n, mx, k, seed):
    rng = random.Random(seed)
    while True:
        xors = [(tuple(rng.sample(range(n), 3)), rng.randint(0, 1)) for _ in range(mx)]
        basis = gauss_basis(n, [(sum(1 << v for v in vs), c) for vs, c in xors])
        if basis is not None:
            break
    ors = []
    for _ in range(k):
        vs = rng.sample(range(n), 3)
        ors.append(tuple((v, rng.randint(0, 1)) for v in vs))   # (variable, negada?)
    return xors, ors

OPS = [0]
def insert_eq(basis, mask, rhs):
    """basis: dict pivote -> (máscara, rhs). Devuelve nuevo dict o None si es inconsistente."""
    for pv in sorted(basis, reverse=True):
        if mask >> pv & 1:
            m2, r2 = basis[pv]
            mask ^= m2; rhs ^= r2; OPS[0] += 1
    if mask == 0:
        return basis if rhs == 0 else None
    nb = dict(basis)
    nb[mask.bit_length() - 1] = (mask, rhs)
    return nb

def gauss_basis(n, eqs):
    b = {}
    for m, c in eqs:
        b = insert_eq(b, m, c)
        if b is None:
            return None
    return b

def count_affine_IE(n, xors, ors, cap=2_000_000):
    """Herencia afín + novedad por inclusión-exclusión, con poda de subconjuntos inconsistentes."""
    OPS[0] = 0
    base = gauss_basis(n, [(sum(1 << v for v in vs), c) for vs, c in xors])
    leaves = [0]; total = [0]
    def violate(basis, clause):
        for v, neg in clause:            # literal falso: x_v = neg
            basis = insert_eq(basis, 1 << v, neg)
            if basis is None:
                return None
        return basis
    def dfs(i, basis, sign):
        if leaves[0] > cap:
            return
        if i == len(ors):
            leaves[0] += 1
            total[0] += sign * (1 << (n - len(basis)))
            return
        dfs(i + 1, basis, sign)
        b2 = violate(basis, ors[i])
        if b2 is not None:
            dfs(i + 1, b2, -sign)
    dfs(0, base, 1)
    nov = []
    for cl in ors:                       # novedad de cada cláusula respecto de lo heredado (solo XOR)
        b2 = violate(base, cl)
        nov.append(0.0 if b2 is None else 2.0 ** (len(base) - len(b2)))
    if leaves[0] > cap:
        return None, leaves[0], OPS[0], nov
    return total[0], leaves[0], OPS[0], nov

def count_brute(n, xors, ors):
    x = np.arange(2 ** n, dtype=np.uint32)
    ok = np.ones(2 ** n, dtype=bool)
    for vs, c in xors:
        par = np.zeros(2 ** n, dtype=np.uint32)
        for v in vs:
            par ^= (x >> v) & 1
        ok &= par == c
    for cl in ors:
        sat = np.zeros(2 ** n, dtype=bool)
        for v, neg in cl:
            sat |= ((x >> v) & 1) != neg
        ok &= sat
    return int(ok.sum())

def count_elim(n, xors, ors):
    """Eliminación de variables (programación dinámica secuencial) con orden de grado mínimo."""
    factors = []
    for vs, c in xors:
        sc = tuple(sorted(vs)); T = np.zeros((2, 2, 2), dtype=np.int64)
        for bits in itertools.product((0, 1), repeat=3):
            asg = dict(zip(vs, bits))
            T[tuple(asg[v] for v in sc)] = int(sum(bits) % 2 == c)
        factors.append((sc, T))
    for cl in ors:
        vs = [v for v, _ in cl]; sc = tuple(sorted(vs)); T = np.zeros((2, 2, 2), dtype=np.int64)
        for bits in itertools.product((0, 1), repeat=3):
            asg = dict(zip(vs, bits))
            T[tuple(asg[v] for v in sc)] = int(any(asg[v] != neg for v, neg in cl))
        factors.append((sc, T))
    remaining = set(range(n)); maxsize = 1; ops = 0; free = 0
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while remaining:
        def deg(v):
            s = set()
            for sc, _ in factors:
                if v in sc:
                    s |= set(sc)
            return len(s)
        v = min(remaining, key=lambda v: (deg(v), v))
        remaining.discard(v)
        inv = [f for f in factors if v in f[0]]
        if not inv:
            free += 1; continue
        factors = [f for f in factors if v not in f[0]]
        sc_all = sorted(set().union(*[set(sc) for sc, _ in inv]))
        if len(sc_all) > 25:
            return None, 2 ** len(sc_all), ops
        lab = {u: letters[i] for i, u in enumerate(sc_all)}
        out_sc = tuple(u for u in sc_all if u != v)
        expr = ','.join(''.join(lab[u] for u in sc) for sc, _ in inv) + '->' + ''.join(lab[u] for u in out_sc)
        T = np.einsum(expr, *[T for _, T in inv])
        size = 2 ** len(sc_all); maxsize = max(maxsize, size); ops += size * len(inv)
        factors.append((out_sc, T))
    val = 1
    for sc, T in factors:
        val *= int(T)
    return val * 2 ** free, maxsize, ops

def C7():
    log("\n== C7 · familia XOR + cláusulas OR: tres referencias sobre las mismas instancias ==")
    rows = []
    for n, k in [(20, 4), (20, 12), (32, 4), (32, 12), (32, 20), (48, 4), (48, 12), (48, 20), (64, 8), (64, 16)]:
        mx = n // 2
        xors, ors = gen_instance(n, mx, k, seed=1000 * n + k)
        t0 = time.perf_counter(); cie, leaves, gops, nov = count_affine_IE(n, xors, ors); t_ie = time.perf_counter() - t0
        t0 = time.perf_counter(); cel, maxsize, eops = count_elim(n, xors, ors); t_el = time.perf_counter() - t0
        cbf = count_brute(n, xors, ors) if n <= 22 else None
        row = {"n": n, "ecuaciones_XOR": mx, "clausulas_OR": k,
               "conteo_herencia_afin_IE": cie, "conteo_eliminacion": cel, "conteo_fuerza_bruta": cbf,
               "IE_subconjuntos_compatibles": leaves, "IE_cota_2^k": 2 ** k, "IE_operaciones_de_fila": gops,
               "IE_segundos": round(t_ie, 4),
               "elim_tabla_maxima": maxsize, "elim_operaciones": eops, "elim_segundos": round(t_el, 4),
               "novedad_por_clausula": sorted(set(nov))}
        rows.append(row)
        log(f"n={n} k={k}: IE={cie} elim={cel} bf={cbf} | IE hojas={leaves}/{2**k} ops={gops} | "
            f"elim tabla={maxsize} ops={eops} | novedades {sorted(set(nov))}")
    # régimen denso: sistema XOR por encima del umbral del 2-núcleo (m/n = 0,85), ancho inducido grande
    densas = []
    for n, k in [(32, 8), (48, 8), (48, 16), (64, 8), (64, 16), (80, 8), (96, 8)]:
        mx = int(0.85 * n)
        xors, ors = gen_instance(n, mx, k, seed=31 * n + k)
        t0 = time.perf_counter(); cie, leaves, gops, nov = count_affine_IE(n, xors, ors); t_ie = time.perf_counter() - t0
        t0 = time.perf_counter(); cel, maxsize, eops = count_elim(n, xors, ors); t_el = time.perf_counter() - t0
        rank = len(gauss_basis(n, [(sum(1 << v for v in vs), c) for vs, c in xors]))
        densas.append({"n": n, "ecuaciones_XOR": mx, "rango_XOR": rank, "clausulas_OR": k,
                       "conteo_herencia_afin_IE": cie, "conteo_eliminacion": cel,
                       "IE_subconjuntos_compatibles": leaves, "IE_operaciones_de_fila": gops, "IE_segundos": round(t_ie, 4),
                       "elim_tabla_maxima": maxsize, "elim_completa": cel is not None, "elim_segundos": round(t_el, 4),
                       "novedad_por_clausula": sorted(set(nov))})
        log(f"[denso] n={n} xor={mx} rango={rank} k={k}: IE={cie} elim={cel} | IE hojas={leaves} ops={gops} "
            f"| elim tabla={maxsize} | novedades {sorted(set(nov))}")
    RES.setdefault("C7_denso", densas)
    # régimen contrario: muchas cláusulas OR y pocas XOR
    contra = []
    for n, mx, k in [(24, 2, 24), (24, 2, 36), (24, 2, 48)]:
        xors, ors = gen_instance(n, mx, k, seed=7 * k)
        cie, leaves, gops, _ = count_affine_IE(n, xors, ors)
        cel, maxsize, eops = count_elim(n, xors, ors)
        cbf = count_brute(n, xors, ors)
        contra.append({"n": n, "ecuaciones_XOR": mx, "clausulas_OR": k, "conteo_IE": cie, "conteo_elim": cel,
                       "conteo_fuerza_bruta": cbf, "IE_subconjuntos_compatibles": leaves,
                       "elim_tabla_maxima": maxsize, "fuerza_bruta_asignaciones": 2 ** n})
        log(f"[contrario] n={n} xor={mx} k={k}: IE={cie} elim={cel} bf={cbf} | IE hojas={leaves} elim tabla={maxsize}")
    RES["C7"] = {"filas": rows, "regimen_contrario": contra}

# ---------------------------------------------------------------- C8
def C8():
    log("\n== C8 · ventana de OpenAI: fracción que debe medirse según R/sqrt(Q) (r = 2, p = 1/4) ==")
    out = []
    Q = 400; p = 0.25
    pmf = [math.comb(Q, j) * p ** j * (1 - p) ** (Q - j) for j in range(Q + 1)]
    for R in (2, 5, 10, 20, 40, 60, 80, 120):
        A0 = math.floor(Q * p - (R - 1) / 2)
        inside = sum(pmf[j] for j in range(A0, A0 + R) if 0 <= j <= Q)
        out.append({"Q": Q, "R": R, "R/sqrt(Q)": round(R / math.sqrt(Q), 2),
                    "fraccion_fuera_de_la_ventana": 1 - inside,
                    "cota_del_articulo_2exp(-R^2/8Q)": min(1.0, 2 * math.exp(-R * R / (8 * Q)))})
    for o in out:
        log(o)
    RES["C8"] = out

if __name__ == "__main__":
    todos = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]
    pedidos = [a for a in sys.argv[1:] if a in todos] or todos
    t0 = time.time()
    for name in pedidos:
        globals()[name]()
    RES["_meta"] = {"segundos": round(time.time() - t0, 1), "numpy": np.__version__, "python": sys.version.split()[0]}
    with open("resultados_convergencia.json", "w") as fh:
        json.dump(RES, fh, ensure_ascii=False, indent=1, default=str)
    log("\nresultados_convergencia.json escrito;", RES["_meta"])
