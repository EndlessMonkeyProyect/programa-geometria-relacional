"""
Laboratorio: economía del cálculo a partir de relaciones entre referencias.
Endless Monkey Project · Relational Geometry Program

Cada experimento (E1..E12, más E5x y E5c) comprueba una proposición del informe.
Ejecutar todo:        python3 -I laboratorio_economia_relacional.py
Un experimento:       python3 -I laboratorio_economia_relacional.py E5c
Varios:               python3 -I laboratorio_economia_relacional.py E5 E5x E5c
Requiere: numpy, networkx. Opcional: matplotlib (figuras de E6).
Tiempo aproximado: 4-6 minutos. Salida: resultados_laboratorio.json

EN: Reproducible lab for "The economy of computation from relations between
references". Each experiment (E1..E12, plus E5x and E5c) checks a proposition of the report
(report.md). Run everything with the command above; output keys are in Spanish.
Requires numpy and networkx; matplotlib is optional and draws the E6 figures
fusion_optica.png (Spanish labels) and optical_fusion.png (English labels).
"""
import itertools, math, random, json, time
from math import gcd
import numpy as np
import networkx as nx

P = 1_000_003            # primo para rangos modulares
P2 = 998_244_353         # segundo primo de control
OUT = {}

# ---------------------------------------------------------------- utilidades
def rank_mod_p(M, p=P):
    """Rango exacto sobre GF(p) por eliminación gaussiana."""
    A = np.unique(np.asarray(M, dtype=np.int64) % p, axis=0)
    nr, nc = A.shape
    r = 0
    for c in range(nc):
        if r == nr:
            break
        piv = np.nonzero(A[r:, c])[0]
        if piv.size == 0:
            continue
        i = r + piv[0]
        if i != r:
            A[[r, i]] = A[[i, r]]
        A[r] = (A[r] * pow(int(A[r, c]), p - 2, p)) % p
        f = A[r + 1:, c]
        nz = np.nonzero(f)[0]
        if nz.size:
            rows = r + 1 + nz
            A[rows] = (A[rows] - np.outer(A[rows, c], A[r])) % p
        r += 1
    return r

def all_bits(n):
    X = np.arange(1 << n, dtype=np.int64)
    return (X[:, None] >> np.arange(n)) & 1

def cut_matrix(F, A, B):
    """M[a,b] = F(a en A, b en B). F indexado por enteros de n bits."""
    def pos(S):
        a = np.arange(1 << len(S), dtype=np.int64)
        out = np.zeros_like(a)
        for j, v in enumerate(S):
            out |= ((a >> j) & 1) << v
        return out
    return F[pos(A)[:, None] | pos(B)[None, :]]

def distinct_rows(M):
    return len(np.unique(M, axis=0))

def nonzero_distinct_rows(M):
    U = np.unique(M, axis=0)
    return int(np.sum(U.any(axis=1)))

def is_rectangular(M):
    """Filas iguales o de soporte disjunto (bloques de unos)."""
    U = np.unique(M, axis=0)
    U = U[U.any(axis=1)].astype(np.int64)
    G = U @ U.T
    np.fill_diagonal(G, 0)
    return bool((G == 0).all())

def balanced_cuts(n):
    rest = list(range(1, n))
    for comb in itertools.combinations(rest, n // 2 - 1):
        A = [0] + list(comb)
        B = [v for v in range(n) if v not in A]
        yield A, B

def max_induced_matching_across(G, A, B):
    """Máximo emparejamiento inducido entre A y B (fuerza bruta, n pequeño)."""
    cross = [(u, v) for u, v in G.edges() if (u in A) != (v in A)]
    best = 0
    def ok(S):
        verts = set()
        for e in S:
            verts |= set(e)
        if len(verts) != 2 * len(S):
            return False
        H = G.subgraph(verts)
        return H.number_of_edges() == len(S)
    # búsqueda por tamaño creciente
    for k in range(1, len(cross) + 1):
        found = any(ok(S) for S in itertools.combinations(cross, k))
        if not found:
            break
        best = k
    return best

# ---------------------------------------------------------------- E1
def E1():
    """Ley de herencia: mcm·mcd = H·m es CRT de congruencias permutables.
    Particiones: |P∧Q| ≤ Σ_J p_J q_J, con igualdad si y solo si permutan; con permutación,
    |P∧Q|·|P∨Q| = |P|·|Q| + k²·Cov_J(p_J, q_J), k = |P∨Q|."""
    res = {}
    # (a) residuos: |P∧Q|·|P∨Q| = |P|·|Q| y novedad uniforme
    ok = True
    for H in range(1, 60):
        for m in range(1, 60):
            L = H * m // gcd(H, m)
            X = range(L)
            meet = len({(x % H, x % m) for x in X})
            join_classes = gcd(H, m)
            ok &= (meet == L) and (meet * join_classes == H * m)
            # novedad por clase heredada: constante m/gcd
            per = {}
            for x in X:
                per.setdefault(x % H, set()).add(x % m)
            ok &= len({len(s) for s in per.values()}) == 1
            ok &= next(iter(per.values())).__len__() == m // gcd(H, m)
    res["residuos_ley_producto_y_novedad_uniforme_H,m<60"] = bool(ok)
    res["mcm(15,9)"] = 15 * 9 // gcd(15, 9)
    res["mcm(315,9)"] = 315 * 9 // gcd(315, 9)

    # (b) particiones generales: desigualdad |P∧Q| <= Σ_J p_J q_J,
    #     igualdad  <=> P y Q permutan (P∘Q = Q∘P)
    def blocks_of(labels):
        d = {}
        for i, l in enumerate(labels):
            d.setdefault(l, set()).add(i)
        return list(d.values())
    def join(Pl, Ql, n):
        parent = list(range(n))
        def f(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for lab in (Pl, Ql):
            first = {}
            for i, l in enumerate(lab):
                if l in first:
                    parent[f(i)] = f(first[l])
                else:
                    first[l] = i
        return [f(i) for i in range(n)]
    def permute(Pl, Ql, n):
        PQ = {(x, z) for x in range(n) for y in range(n) for z in range(n)
              if Pl[x] == Pl[y] and Ql[y] == Ql[z]}
        QP = {(x, z) for x in range(n) for y in range(n) for z in range(n)
              if Ql[x] == Ql[y] and Pl[y] == Pl[z]}
        return PQ == QP
    rng = random.Random(1)
    n = 7
    viol = 0; eq_perm = 0; total = 0; perm_count = 0
    ok_cov = True; prod_ok = 0; prod_ok_cov0 = 0
    for _ in range(3000):
        Pl = [rng.randrange(3) for _ in range(n)]
        Ql = [rng.randrange(3) for _ in range(n)]
        J = join(Pl, Ql, n)
        meet = len({(Pl[i], Ql[i]) for i in range(n)})
        bound = 0; pJ = []; qJ = []
        for Jb in blocks_of(J):
            pJ.append(len({Pl[i] for i in Jb})); qJ.append(len({Ql[i] for i in Jb}))
            bound += pJ[-1] * qJ[-1]
        pm = permute(Pl, Ql, n)
        total += 1
        perm_count += pm
        if pm:
            # con permutación: |P∧Q|·|P∨Q| − |P|·|Q| = k·Σp_Jq_J − Σp_J·Σq_J = k²·Cov_J(p_J, q_J)
            k = len(pJ); nP, nQ = len(set(Pl)), len(set(Ql))
            cov_k2 = k * sum(a * b for a, b in zip(pJ, qJ)) - sum(pJ) * sum(qJ)
            ok_cov &= (meet * k - nP * nQ == cov_k2) and (nP == sum(pJ)) and (nQ == sum(qJ))
            prod_ok += (meet * k == nP * nQ); prod_ok_cov0 += ((meet * k == nP * nQ) == (cov_k2 == 0))
        if meet > bound:
            viol += 1
        if (meet == bound) == pm:
            eq_perm += 1
    res["particiones_aleatorias"] = total
    res["violaciones_desigualdad"] = viol
    res["igualdad_sii_permutan_(casos_que_cumplen)"] = eq_perm
    res["pares_que_permutan"] = perm_count
    res["con_permutacion:_|P∧Q||P∨Q|−|P||Q|_=_k²·Cov(p_J,q_J)"] = bool(ok_cov)
    res["pares_que_permutan_y_cumplen_|P∧Q||P∨Q|=|P||Q|"] = prod_ok
    res["identidad_de_producto_sii_covarianza_nula_(casos)"] = prod_ok_cov0
    # permutan pero la identidad de producto falla: {12|34|5} y {13|24|5}
    Pl = [0, 0, 1, 1, 2]; Ql = [0, 1, 0, 1, 2]
    res["contraejemplo_producto_{12|34|5}_{13|24|5}"] = {
        "permutan": permute(Pl, Ql, 5), "|P∧Q|": len({(Pl[i], Ql[i]) for i in range(5)}),
        "|P∨Q|": len(set(join(Pl, Ql, 5))), "|P|·|Q|": len(set(Pl)) * len(set(Ql))}
    # contraejemplo explícito {123|4} vs {1|234}
    Pl = [0, 0, 0, 1]; Ql = [0, 1, 1, 1]
    meet = len({(Pl[i], Ql[i]) for i in range(4)})
    res["contraejemplo_{123|4}_{1|234}"] = {
        "|P|": 2, "|Q|": 2, "|P∧Q|": meet,
        "|P∨Q|": len(set(join(Pl, Ql, 4))),
        "permutan": permute(Pl, Ql, 4)}

    # (c) grupo GF(2)^n: ecuación XOR nueva divide cada clase en 1 o 2 (o mata todo);
    #     cláusula nueva elimina fracciones arbitrarias de las soluciones heredadas
    rng = random.Random(2); n = 10
    bits = all_bits(n)
    alive_x = np.ones(1 << n, bool); alive_c = np.ones(1 << n, bool)
    fx, fc = [], []
    for _ in range(12):
        S = rng.sample(range(n), 3)
        b = rng.randrange(2)
        new = (bits[:, S].sum(1) % 2) == b
        if alive_x.sum():
            fx.append(round(float((alive_x & ~new).sum() / alive_x.sum()), 4))
        alive_x &= new
        sg = [rng.randrange(2) for _ in S]
        cl = np.zeros(1 << n, bool)
        for v, s in zip(S, sg):
            cl |= bits[:, v] == s
        if alive_c.sum():
            fc.append(round(float((alive_c & ~cl).sum() / alive_c.sum()), 4))
        alive_c &= cl
    res["fraccion_eliminada_por_XOR_nueva"] = sorted(set(fx))
    res["fraccion_eliminada_por_clausula_nueva"] = fc
    OUT["E1_herencia_CRT"] = res

# ---------------------------------------------------------------- E2
def monotone_2cnf(G, n):
    bits = all_bits(n)
    F = np.ones(1 << n, dtype=np.int64)
    for u, v in G.edges():
        F &= (bits[:, u] | bits[:, v])
    return F

def min_over_balanced_cuts(F, n, G=None, want_matching=False):
    best_rank = None; best_rows = None; best_cut = None
    for A, B in balanced_cuts(n):
        M = cut_matrix(F, A, B)
        dr = distinct_rows(M)
        if best_rows is None or dr < best_rows:
            best_rows = dr
        # rango solo si puede mejorar (rango <= filas distintas)
        if best_rank is None or dr < best_rank or True:
            rk = rank_mod_p(M)
            if best_rank is None or rk < best_rank:
                best_rank = rk; best_cut = (A, B)
    out = {"min_rango_GFp": best_rank, "min_filas_distintas": best_rows}
    if want_matching and G is not None:
        A, B = best_cut
        out["emparejamiento_inducido_en_corte_optimo"] = max_induced_matching_across(G, set(A), set(B))
        out["aristas_que_cruzan_corte_optimo"] = sum(1 for u, v in G.edges() if (u in A) != (v in A))
    return out

def E2():
    """Rango de corte (= distinciones que el pasado manifiesta al futuro)
    para 2-CNF monótona: expansor 3-regular vs ciclo."""
    res = {}
    for n in (8, 10, 12, 14, 16):
        G = nx.random_regular_graph(3, n, seed=7 + n)
        while not nx.is_connected(G):
            G = nx.random_regular_graph(3, n, seed=random.randrange(10**6))
        C = nx.cycle_graph(n)
        t = time.time()
        rG = min_over_balanced_cuts(monotone_2cnf(G, n), n, G, want_matching=(n <= 14))
        rC = min_over_balanced_cuts(monotone_2cnf(C, n), n)
        res[f"n={n}"] = {"3-regular": rG, "ciclo": rC,
                         "soluciones_3reg": int(monotone_2cnf(G, n).sum()),
                         "seg": round(time.time() - t, 1)}
        print("E2", n, res[f"n={n}"], flush=True)
    OUT["E2_rango_de_corte_2CNF"] = res

# ---------------------------------------------------------------- E3/E4
def E3_E4():
    """XOR (afín): reflexión x⊕y⊕z cerrada, cortes rectangulares,
    conteo por rango (Gauss) aunque el rango de corte sea grande."""
    res = {}
    rng = random.Random(5)
    n = 16; m = 10
    bits = all_bits(n)
    eqs = []
    F = np.ones(1 << n, dtype=np.int64)
    for _ in range(m):
        S = rng.sample(range(n), 3); b = rng.randrange(2)
        eqs.append((S, b))
        F &= ((bits[:, S].sum(1) % 2) == b).astype(np.int64)
    # conteo por eliminación sobre GF(2)
    rows = []
    for S, b in eqs:
        v = 0
        for s in S: v |= 1 << s
        rows.append((v, b))
    basis = []  # (pivot, vec, b)
    consistent = True
    for v, b in rows:
        for pv, bv, bb in basis:
            if (v >> pv) & 1:
                v ^= bv; b ^= bb
        if v == 0:
            if b: consistent = False
            continue
        basis.append((v.bit_length() - 1, v, b))
    rank = len(basis)
    res["conteo_fuerza_bruta"] = int(F.sum())
    res["conteo_Gauss_2^(n-rango)"] = (2 ** (n - rank)) if consistent else 0
    # rango de corte mínimo sobre todos los cortes balanceados
    mins = min_over_balanced_cuts(F, n)
    res["min_rango_corte_XOR_n16"] = mins
    # rectangularidad en todos los cortes balanceados
    rect = all(is_rectangular(cut_matrix(F, A, B)) for A, B in itertools.islice(balanced_cuts(n), 400))
    res["cortes_rectangulares_(400_cortes)"] = rect
    # reflexión: x⊕y⊕z ∈ Sol
    sol = np.nonzero(F)[0]
    solset = set(sol.tolist())
    trip = [tuple(rng.choice(sol) for _ in range(3)) for _ in range(20000)]
    res["XOR_cerrado_bajo_reflexion_(20000_ternas)"] = all((x ^ y ^ z) in solset for x, y, z in trip)
    # marco compacto: d+1 puntos generan todo por reflexión
    d = n - rank
    x0 = int(sol[0]); gens = [x0]
    span = {0}
    for s in sol:
        dv = int(s) ^ x0
        if dv not in span:
            gens.append(int(s))
            span |= {a ^ dv for a in span}
        if len(gens) == d + 1: break
    closure = set(gens)
    while True:
        lst = list(closure)
        new = {a ^ b ^ c for a in lst for b in lst for c in lst} - closure if len(lst) < 60 else None
        if new is None:
            # cierre incremental para conjuntos grandes
            new = set()
            for a in lst:
                for g1 in gens:
                    for g2 in gens:
                        w = a ^ g1 ^ g2
                        if w not in closure: new.add(w)
        if not new: break
        closure |= new
    res["marco_compacto"] = {"dim": d, "puntos_generadores": len(gens),
                             "cierre_por_reflexion": len(closure), "|Sol|": len(solset),
                             "coincide": closure == solset}
    # contraste: 2-CNF monótona en expansor NO es cerrada ni rectangular
    G = nx.random_regular_graph(3, 14, seed=21)
    F2 = monotone_2cnf(G, 14)
    sol2 = np.nonzero(F2)[0]; s2 = set(sol2.tolist())
    viol = sum((x ^ y ^ z) not in s2 for x, y, z in
               (tuple(rng.choice(sol2) for _ in range(3)) for _ in range(20000)))
    res["2CNF_monotona_fraccion_ternas_que_rompen_reflexion"] = round(viol / 20000, 3)
    A, B = next(balanced_cuts(14))
    res["2CNF_monotona_corte_rectangular"] = is_rectangular(cut_matrix(F2, A, B))
    OUT["E3_E4_afin_reflexion"] = res

# ---------------------------------------------------------------- E5
def E5():
    """Rejilla de 3 colores, ancho 10: 1536 estados → 136 órbitas (Burnside,
    grupo de orden 12) → dimensión de Krylov (mínimo exacto para la consulta)."""
    w = 10
    states = [c for c in itertools.product(range(3), repeat=w)
              if all(c[i] != c[i + 1] for i in range(w - 1))]
    idx = {c: i for i, c in enumerate(states)}
    N = len(states)
    S = np.array(states, dtype=np.int8)
    T = np.ones((N, N), dtype=np.int64)
    for i in range(w):
        T &= (S[:, i][:, None] != S[:, i][None, :]).astype(np.int64)
    # órbitas bajo S3 (colores) × Z2 (reflexión de la columna)
    perms = list(itertools.permutations(range(3)))
    def images(c):
        out = []
        for p in perms:
            pc = tuple(p[x] for x in c)
            out.append(pc); out.append(pc[::-1])
        return out
    orbit_id = [-1] * N; orbits = []
    for i, c in enumerate(states):
        if orbit_id[i] < 0:
            orb = sorted({idx[x] for x in images(c)})
            for j in orb: orbit_id[j] = len(orbits)
            orbits.append(orb)
    K = len(orbits)
    # matriz cociente exacta
    Tq = np.zeros((K, K), dtype=object)
    for a, orb in enumerate(orbits):
        rep = orb[0]
        for b, orb2 in enumerate(orbits):
            Tq[a, b] = int(T[rep, orb2].sum())
    sizes = np.array([len(o) for o in orbits], dtype=object)
    # conteos exactos a_m (m columnas) por ambas vías
    v = np.ones(N, dtype=object); vq = np.ones(K, dtype=object)
    full, quot = [], []
    Tobj = T.astype(object)
    for mcol in range(1, 9):
        full.append(int(v.sum())); quot.append(int((sizes * vq).sum()))
        v = Tobj.dot(v); vq = Tq.dot(vq)
    # Krylov mod p: dim span{T^k 1}
    def krylov_dim(p):
        vec = np.ones(N, dtype=np.int64); basis = []
        dims = []
        for k in range(N + 1):
            basis.append(vec.copy())
            r = rank_mod_p(np.array(basis), p)
            dims.append(r)
            if r < len(basis):
                return r
            vec = (T @ vec) % p
        return dims[-1]
    kd1 = krylov_dim(P); kd2 = krylov_dim(P2)
    # rango de Hankel de la sucesión exacta a_m
    # b_k = 1ᵀ T^k 1 mod p (el rango de Hankel solo necesita la sucesión mod p)
    vv = np.ones(N, dtype=np.int64)
    bseq = []
    for k in range(2 * kd1 + 6):
        bseq.append(int(vv.sum() % P)); vv = (T @ vv) % P
    L = kd1 + 3
    Hk = np.array([[bseq[i + j] for j in range(L)] for i in range(L)], dtype=np.int64)
    OUT["E5_rejilla_3_colores"] = {
        "estados_columna": N, "orbitas_S3xZ2": K,
        "cota_orbita_estabilizador_N/|G|": N / 12,
        "conteos_completos_m=1..8": full[:5], "conteos_cociente_coinciden": full == quot,
        "dim_Krylov_modp": kd1, "dim_Krylov_mod_segundo_primo": kd2,
        "rango_Hankel_modp": rank_mod_p(Hk)}
    print("E5", OUT["E5_rejilla_3_colores"], flush=True)

# ---------------------------------------------------------------- E6
def E6():
    """Óptica: distinciones observables = rango-ε del operador fuente→observación."""
    res = {}
    xs = np.linspace(-1, 1, 5)          # 5 fuentes colineales, radio r = 1
    # (a) campo estático (núcleo 1/|y-x|), observación en esfera de radio R
    def fib_sphere(k):
        i = np.arange(k) + 0.5
        phi = np.arccos(1 - 2 * i / k); th = np.pi * (1 + 5 ** 0.5) * i
        return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], 1)
    Y = fib_sphere(600)
    src = np.stack([xs, 0 * xs, 0 * xs], 1)
    Rs = np.logspace(np.log10(1.05), 4, 300)
    def sv_static(R):
        D = np.linalg.norm(R * Y[:, None, :] - src[None, :, :], axis=2)
        s = np.linalg.svd(1.0 / D, compute_uv=False)
        return s / s[0]
    svs = np.array([sv_static(R) for R in Rs])
    stair = {}
    thresholds = {}
    for eps in (1e-2, 1e-3, 1e-4):
        ranks = (svs > eps).sum(1)
        stair[str(eps)] = sorted(set(ranks.tolist()), reverse=True)
        th = {}
        for l in range(1, 5):   # R donde σ_{l+1}/σ_1 cruza eps
            above = svs[:, l] > eps
            if above.any() and not above.all():
                th[l] = float(Rs[np.nonzero(above)[0][-1]])
        thresholds[str(eps)] = th
    # pendiente d log R_l / d log(1/eps) ≈ 1/l
    slopes = {}
    for l in range(1, 5):
        a = thresholds["0.01"].get(l); b = thresholds["0.0001"].get(l)
        if a and b:
            slopes[l] = round(math.log(b / a) / math.log(100), 3)
    res["estatico_escalera_rango_eps"] = stair
    res["estatico_umbrales_R_l"] = thresholds
    res["estatico_pendiente_logR_vs_log(1/eps)_(predicho_1/l)"] = slopes
    res["estatico_sigma_min/sigma_1_en_R=1e4_(rango_exacto_sigue_5)"] = float(svs[-1, 4])
    # Último bit antes de la singularidad: la penúltima distinción (2 -> 1) es el dipolo, impar.
    dip = {}
    for R in (20.0, 100.0, 400.0):
        D = np.linalg.norm(R * Y[:, None, :] - src[None, :, :], axis=2)
        _, _, Vt = np.linalg.svd(1.0 / D)
        v1, v2 = Vt[0] * np.sign(Vt[0].sum()), Vt[1] * np.sign(Vt[1][-1])
        dip[str(R)] = {"v1_total": [round(float(a), 3) for a in v1],
                       "v2_dipolo": [round(float(a), 3) for a in v2],
                       "v2_residuo_par": float(np.linalg.norm(v2 + v2[::-1]) / np.linalg.norm(v2)),
                       "corr_v2_con_posicion": round(float(abs(v2 @ xs) / np.linalg.norm(xs)), 6)}
    res["ultima_distincion_es_el_dipolo_impar"] = dip
    # (b) onda, Fraunhofer paraxial: G[u,j] = exp(-i k x_j u / R), apertura D
    lam = 1.0; k = 2 * np.pi / lam; Dap = 20.0
    u = np.linspace(-Dap / 2, Dap / 2, 400)
    Rw = np.logspace(0.5, 5, 300)
    sw = []
    for R in Rw:
        Gm = np.exp(-1j * k * np.outer(u, xs) / R)
        s = np.linalg.svd(Gm, compute_uv=False); sw.append(s / s[0])
    sw = np.array(sw)
    res["onda_escalera_eps=1e-2"] = [int(r) for r in sorted(set((sw > 1e-2).sum(1).tolist()), reverse=True)]
    # (c) dos distribuciones con los mismos observables lejos, distintas cerca
    def G_static(R):
        D = np.linalg.norm(R * Y[:, None, :] - src[None, :, :], axis=2); return 1.0 / D
    Rfar, Rnear = 300.0, 1.5
    U_, s_, Vt = np.linalg.svd(G_static(Rfar))
    a1 = np.ones(5); a2 = a1 + 0.5 * Vt[-1]
    def rel(R):
        G_ = G_static(R)
        return float(np.linalg.norm(G_ @ (a1 - a2)) / np.linalg.norm(G_ @ a1))
    res["mismo_observable_lejos_distinto_cerca"] = {
        "dif_relativa_R=300": rel(Rfar), "dif_relativa_R=1.5": rel(Rnear)}
    OUT["E6_optica_rango_eps"] = res
    print("E6", res, flush=True)

# ---------------------------------------------------------------- E9
def E9():
    """Misma estructura, otra referencia: F(s,t)=∏(¬s_i ∨ ¬t_i), k=8."""
    k = 8; n = 2 * k
    bits = all_bits(n)
    F = np.ones(1 << n, dtype=np.int64)
    for i in range(k):
        F &= (1 - (bits[:, i] & bits[:, k + i]))
    def seq_width(order):
        best = 0
        for c in range(1, n):
            A = order[:c]; B = order[c:]
            best = max(best, rank_mod_p(cut_matrix(F, A, B)))
        return best
    bloque = list(range(n))                                  # s1..s8 | t1..t8
    intercalado = [v for i in range(k) for v in (i, k + i)]  # s1 t1 s2 t2 ...
    OUT["E9_cambio_de_referencia"] = {
        "max_rango_orden_en_bloques": seq_width(bloque),
        "max_rango_orden_intercalado": seq_width(intercalado),
        "conteo": int(F.sum()), "3^k": 3 ** k}
    print("E9", OUT["E9_cambio_de_referencia"], flush=True)

# ================================================================ ADENDA
def rank_Q(rows):
    """Rango exacto sobre Q (eliminación sin fracciones, enteros de Python)."""
    A = [list(map(int, r)) for r in rows]
    nr = len(A); nc = len(A[0]); r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(r + 1, nr):
            if A[i][c]:
                a, b = A[r][c], A[i][c]
                A[i] = [a * x - b * y for x, y in zip(A[i], A[r])]
                g = 0
                for x in A[i]:
                    g = math.gcd(g, x)
                if g > 1:
                    A[i] = [x // g for x in A[i]]
        r += 1
        if r == nr:
            break
    return r

def E5_exacto():
    """Dimensión de Krylov exacta sobre Q, vía la matriz cociente (136×136)."""
    w = 10
    states = [c for c in itertools.product(range(3), repeat=w)
              if all(c[i] != c[i + 1] for i in range(w - 1))]
    idx = {c: i for i, c in enumerate(states)}
    S = np.array(states, dtype=np.int8); N = len(states)
    T = np.ones((N, N), dtype=np.int64)
    for i in range(w):
        T &= (S[:, i][:, None] != S[:, i][None, :]).astype(np.int64)
    perms = list(itertools.permutations(range(3)))
    orbit_id = [-1] * N; orbits = []
    for i, c in enumerate(states):
        if orbit_id[i] < 0:
            ims = set()
            for p in perms:
                pc = tuple(p[x] for x in c); ims.add(pc); ims.add(pc[::-1])
            orb = sorted(idx[x] for x in ims)
            for j in orb: orbit_id[j] = len(orbits)
            orbits.append(orb)
    K = len(orbits)
    Tq = [[int(T[orb[0], orb2].sum()) for orb2 in orbits] for orb in orbits]
    sizes = [len(o) for o in orbits]
    # Krylov en coordenadas del cociente: v_k = Tq^k 1 (vector invariante)
    v = [1] * K; kr = [v[:]]
    for _ in range(60):
        v = [sum(Tq[a][b] * v[b] for b in range(K)) for a in range(K)]
        kr.append(v[:])
    # pesos: el producto interno natural es <x,y> = Σ |O| x_O y_O; el rango no cambia
    rk = rank_Q(kr[:56])
    # sucesión exacta b_k = 1ᵀT^k1 = Σ |O| (Tq^k 1)_O y su Hankel
    b = [sum(s * x for s, x in zip(sizes, vv)) for vv in kr]
    L = 28  # Hankel 28×28 usa b_0..b_54
    H = [[b[i + j] for j in range(L)] for i in range(L)]
    OUT["E5_exacto"] = {"dim_Krylov_sobre_Q": rk,
                        "rango_Hankel_Q_28x28": rank_Q(H),
                        "b_0..b_4": b[:5]}
    print("E5_exacto", OUT["E5_exacto"], flush=True)

def bareiss_det(M):
    """Determinante exacto de una matriz entera (Bareiss, sin fracciones)."""
    M = [list(r) for r in M]; n = len(M); prev = 1; sign = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if M[i][k] != 0), None)
            if sw is None:
                return 0
            M[k], M[sw] = M[sw], M[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[n - 1][n - 1]

def rejilla_cociente(w):
    """Columnas propias de ancho w, órbitas bajo S3 × Z2 y matriz cociente exacta."""
    states = [c for c in itertools.product(range(3), repeat=w)
              if all(c[i] != c[i + 1] for i in range(w - 1))]
    idx = {c: i for i, c in enumerate(states)}
    perms = list(itertools.permutations(range(3)))
    oid = [-1] * len(states); orbits = []
    for i, c in enumerate(states):
        if oid[i] < 0:
            ims = set()
            for p in perms:
                pc = tuple(p[x] for x in c); ims.add(pc); ims.add(pc[::-1])
            orb = sorted(idx[x] for x in ims)
            for j in orb:
                oid[j] = len(orbits)
            orbits.append(orb)
    comp = lambda a, b: all(x != y for x, y in zip(a, b))
    Tq = [[sum(comp(states[o[0]], states[j]) for j in o2) for o2 in orbits] for o in orbits]
    return len(states), [len(o) for o in orbits], Tq

def sucesion_conteos(sizes, Tq, n_terms, mod=None):
    """b_k = 1ᵀ T^k 1 = a_{k+1} (colorings of the w×(k+1) grid), exact or mod p."""
    K = len(sizes); v = [1] * K; b = []
    for k in range(n_terms):
        b.append(sum(s * x for s, x in zip(sizes, v)) if mod is None
                 else sum(s * x for s, x in zip(sizes, v)) % mod)
        v = [sum(Tq[a][c] * v[c] for c in range(K)) for a in range(K)]
        if mod is not None:
            v = [x % mod for x in v]
    return b

def E5c():
    """Certificado del orden mínimo de la recurrencia (rejilla w×m, 3 colores, bordes libres).
    T es simétrica, así que H_N[i][j] = b_{i+j} = <T^i 1, T^j 1> es la matriz de Gram de los
    N primeros vectores de Krylov. det H_d ≠ 0 y det H_{d+1} = 0 certifican que el orden mínimo
    de una recurrencia válida para todo m ≥ 1 es d. El Hankel desplazado H'_d[i][j] = b_{1+i+j}
    es Kᵀ T K; si det H'_d ≠ 0, la recurrencia no tiene raíz nula y no existe otra más corta
    ni siquiera desde m = 2. Un determinante no nulo módulo p es no nulo sobre Z."""
    res = {}
    for w in range(1, 11):
        n_states, sizes, Tq = rejilla_cociente(w)
        K = len(sizes)
        bp = sucesion_conteos(sizes, Tq, 2 * K + 3, mod=P)
        d = rank_mod_p([[bp[i + j] for j in range(K + 1)] for i in range(K + 1)])
        b = sucesion_conteos(sizes, Tq, 2 * d + 2)
        Hd = [[b[i + j] % P for j in range(d)] for i in range(d)]
        Hs = [[b[1 + i + j] % P for j in range(d)] for i in range(d)]
        Hd1 = [[b[i + j] for j in range(d + 1)] for i in range(d + 1)]
        cert = {"det_H_d_no_nulo": rank_mod_p(Hd) == d,
                "det_H_d+1_cero_exacto": bareiss_det(Hd1) == 0,
                "sin_raiz_nula_(det_H'_d_no_nulo)": rank_mod_p(Hs) == d}
        res[f"ancho={w}"] = {"columnas": n_states, "orbitas_S3xZ2": K, "orden_minimo": d,
                             "certificado": cert, ("a_1..a_5" if w == 10 else "a_1..a_3"): b[:5] if w == 10 else b[:3]}
        print("E5c", w, res[f"ancho={w}"], flush=True)
    res["ordenes_por_ancho"] = [res[f"ancho={w}"]["orden_minimo"] for w in range(1, 11)]
    res["orbitas_por_ancho"] = [res[f"ancho={w}"]["orbitas_S3xZ2"] for w in range(1, 11)]
    res["todo_certificado"] = all(all(res[f"ancho={w}"]["certificado"].values()) for w in range(1, 11))
    OUT["E5c_certificado_orden_minimo"] = res

def boundary_vertices(G, A):
    VA = {v for v in A}
    return [v for v in A if any(u not in VA for u in G[v])]

def E2b():
    """Cotas cut a cut: 2^μ ≤ rango ≤ 2^{|∂A|}+1 (2-CNF monótona)."""
    res = {}
    for n in (10, 12):
        G = nx.random_regular_graph(3, n, seed=7 + n)
        F = monotone_2cnf(G, n)
        ok_low = ok_up = True; cuts = 0
        for A, B in balanced_cuts(n):
            M = cut_matrix(F, A, B); rk = rank_mod_p(M)
            mu = max_induced_matching_across(G, set(A), set(B))
            dA = len(boundary_vertices(G, A)); dB = len(boundary_vertices(G, B))
            ok_low &= (2 ** mu <= rk)
            ok_up &= (rk <= 2 ** min(dA, dB) + 1)
            cuts += 1
        res[f"n={n}"] = {"cortes": cuts, "2^mu<=rango": bool(ok_low), "rango<=2^frontera+1": bool(ok_up)}
    OUT["E2b_cotas_por_corte"] = res
    print("E2b", res, flush=True)

def tseitin_formula_log2rank(G, edges, Aset):
    """log2(rango de corte) = β + 1 − c_A − c_B (G conexo, carga satisfacible).
    β = vértices tocados por aristas de ambos lados; c_A, c_B = componentes del grafo
    formado por las aristas de cada lado (solo con los vértices que tocan)."""
    def comps(es):
        parent = {}
        def f(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        for (u, v) in es:
            parent.setdefault(u, u); parent.setdefault(v, v)
            ru, rv = f(u), f(v)
            if ru != rv: parent[ru] = rv
        return len({f(x) for x in parent}), set(parent)
    EA = [edges[i] for i in Aset]; EB = [edges[i] for i in range(len(edges)) if i not in Aset]
    cA, VA = comps(EA); cB, VB = comps(EB)
    beta = len(VA & VB)
    return beta + 1 - cA - cB

def conectividad_matroide_grafico(G, edges, Aset):
    """λ(A) = r(A) + r(B) − r(E), con r(S) = |V(S)| − componentes de (V(S), S)."""
    def r(es):
        H = nx.Graph(); H.add_edges_from(es)
        return H.number_of_nodes() - nx.number_connected_components(H) if es else 0
    EA = [edges[i] for i in Aset]; EB = [edges[i] for i in range(len(edges)) if i not in Aset]
    return r(EA) + r(EB) - r(edges)

def tseitin_tabla(G, edges, cargas):
    """Tabla de verdad de TS_{G,c}: x_e por arista, ⊕_{e∋v} x_e = c(v)."""
    E = len(edges); bits = all_bits(E)
    F = np.ones(1 << E, dtype=np.int64)
    for v in G.nodes():
        inc = [i for i, e in enumerate(edges) if v in e]
        F &= (bits[:, inc].sum(1) % 2 == cargas[v]).astype(np.int64)
    return F

def E3b():
    """Tseitin satisfacible: rango de corte = 2^λ(A), λ la función de conectividad del
    matroide gráfico (= β + 1 − c_A − c_B). Rango calculado directamente sobre GF(p).
    Para c ≡ 0 es el teorema del espacio de estados de Forney aplicado al código de ciclos."""
    res = {}
    # (a) 3-regular, V = 10: los 3003 cortes con |A| = 7, carga nula y carga aleatoria
    G = nx.random_regular_graph(3, 10, seed=3)
    edges = list(G.edges()); E = len(edges)
    rng = random.Random(5)
    c_al = [rng.randint(0, 1) for _ in range(10)]
    if sum(c_al) % 2: c_al[0] ^= 1
    for nombre, cargas in (("carga_nula", [0] * 10), ("carga_aleatoria", c_al)):
        F = tseitin_tabla(G, edges, cargas)
        ok = ok_lam = True; checked = 0; minr = None
        for comb in itertools.combinations(range(1, E), E // 2 - 1):
            A = [0] + list(comb); B = [i for i in range(E) if i not in A]
            r = rank_mod_p(cut_matrix(F, A, B))
            lam = conectividad_matroide_grafico(G, edges, set(A))
            ok &= (r == 2 ** tseitin_formula_log2rank(G, edges, set(A)))
            ok_lam &= (lam == tseitin_formula_log2rank(G, edges, set(A)))
            checked += 1; minr = r if minr is None else min(minr, r)
        res[f"V=10_{nombre}"] = {"cortes": checked, "rango_directo_=_2^(β+1−c_A−c_B)": bool(ok),
                                 "β+1−c_A−c_B_=_λ(A)": bool(ok_lam), "soluciones": int(F.sum()),
                                 "2^(E−V+1)": 2 ** (E - 10 + 1), "min_rango_corte": minr}
        print("E3b", nombre, res[f"V=10_{nombre}"], flush=True)
    # (b) grafos conexos aleatorios, cortes arbitrarios, cargas satisfacibles aleatorias
    rng = random.Random(1); checked = 0; ok = True
    while checked < 216:
        V = rng.randint(5, 8); m = rng.randint(V, min(12, V * (V - 1) // 2))
        H = nx.gnm_random_graph(V, m, seed=rng.randrange(10 ** 6))
        if not nx.is_connected(H):
            continue
        ed = list(H.edges()); cargas = [rng.randint(0, 1) for _ in range(V)]
        if sum(cargas) % 2: cargas[rng.randrange(V)] ^= 1
        F = tseitin_tabla(H, ed, cargas)
        for _ in range(6):
            k = rng.randint(1, len(ed) - 1); A = sorted(rng.sample(range(len(ed)), k))
            B = [i for i in range(len(ed)) if i not in A]
            ok &= (rank_mod_p(cut_matrix(F, A, B)) == 2 ** conectividad_matroide_grafico(H, ed, set(A)))
            checked += 1
    res["grafos_aleatorios_cortes_arbitrarios"] = {"cortes": checked, "rango_=_2^λ(A)": bool(ok)}
    # (c) árbol con carga nula: una sola solución y rango 1 en todo corte (λ = 0)
    T = nx.random_labeled_tree(12, seed=4) if hasattr(nx, "random_labeled_tree") else nx.random_tree(12, seed=4)
    ed = list(T.edges()); F = tseitin_tabla(T, ed, [0] * 12)
    rangos = {rank_mod_p(cut_matrix(F, list(A), [i for i in range(len(ed)) if i not in A]))
              for A in itertools.combinations(range(len(ed)), 5)}
    res["arbol_12_vertices"] = {"soluciones": int(F.sum()), "rangos_de_corte": sorted(rangos)}
    print("E3b", res["grafos_aleatorios_cortes_arbitrarios"], res["arbol_12_vertices"], flush=True)
    # (d) mínimo sobre cortes balanceados por la fórmula, V = 8..16
    for V in (8, 10, 12, 14, 16):
        G = nx.random_regular_graph(3, V, seed=40 + V)
        while not nx.is_connected(G):
            G = nx.random_regular_graph(3, V, seed=random.randrange(10**6))
        edges = list(G.edges()); E = len(edges)
        best = None
        for comb in itertools.combinations(range(1, E), E // 2 - 1):
            val = tseitin_formula_log2rank(G, edges, {0, *comb})
            if best is None or val < best: best = val
        res[f"V={V}_E={E}"] = {"min_log2_rango_corte": best, "log2_conteo": E - V + 1}
        print("E3b", V, res[f"V={V}_E={E}"], flush=True)
    OUT["E3b_tseitin"] = res

import sys
EXPERIMENTOS = {"E1": lambda: (E1(), print("E1", OUT["E1_herencia_CRT"], flush=True)),
                "E9": E9, "E5": E5, "E5x": E5_exacto, "E5c": E5c, "E6": E6,
                "E3": lambda: (E3_E4(), print("E3/E4", OUT["E3_E4_afin_reflexion"], flush=True)),
                "E3b": E3b, "E2": E2, "E2b": E2b}


def E10():
    """Simetrías globales de 3-CNF aleatorias (cota órbita-estabilizador: ahorro ≤ |Aut|)."""
    from networkx.algorithms import isomorphism as iso
    rng = random.Random(11); n = 16; m = 68; sizes = []
    for t in range(30):
        cls = set()
        while len(cls) < m:
            S = sorted(rng.sample(range(n), 3))
            cls.add(tuple((v, rng.randrange(2)) for v in S))
        G = nx.Graph()
        for v in range(n):
            G.add_node(("l", v, 0), t="lit"); G.add_node(("l", v, 1), t="lit")
            G.add_edge(("l", v, 0), ("l", v, 1))
        for j, c in enumerate(cls):
            G.add_node(("c", j), t="cl")
            for v, s in c:
                G.add_edge(("c", j), ("l", v, s))
        GM = iso.GraphMatcher(G, G, node_match=lambda a, b: a["t"] == b["t"])
        cnt = 0
        for _ in GM.isomorphisms_iter():
            cnt += 1
            if cnt > 1000: break
        sizes.append(cnt)
    OUT["E10_simetrias_3CNF_aleatorias"] = {"n": n, "m": m, "instancias": 30,
        "tamaños_|Aut|": sorted(set(sizes)), "fraccion_con_Aut_trivial": sizes.count(1) / 30}
    print("E10", OUT["E10_simetrias_3CNF_aleatorias"], flush=True)

EXPERIMENTOS["E10"] = E10

# ---------------------------------------------------------------- E11
def E11():
    """Hipercubo con la referencia «peso»: 2^n estados -> n+1 clases, exacto.
    Contraejemplo calculado: con tasas distintas por posición la referencia deja de ser exacta."""
    res = {}
    def full_dynamics(n, t, rates):
        v = np.zeros(1 << n, dtype=object); v[0] = 1
        for _ in range(t):
            w = np.zeros(1 << n, dtype=object)
            for s in range(1 << n):
                if v[s]:
                    for j in range(n):
                        w[s ^ (1 << j)] += v[s] * rates[j]
            v = w
        out = [0] * (n + 1)
        for s in range(1 << n):
            out[bin(s).count("1")] += v[s]
        return [int(a) for a in out]
    def lumped(n, t):
        a = [0] * (n + 1); a[0] = 1
        for _ in range(t):
            b = [0] * (n + 1)
            for w in range(n + 1):
                if w < n: b[w + 1] += (n - w) * a[w]
                if w > 0: b[w - 1] += w * a[w]
            a = b
        return a
    ok = True
    for n in range(2, 9):
        ok &= full_dynamics(n, 6, [1] * n) == lumped(n, 6)
    res["recurrencia_por_peso_igual_a_dinamica_completa_n=2..8_t=6"] = bool(ok)
    res["n=6_t=6_por_peso"] = lumped(6, 6)
    res["suma=6^6"] = sum(lumped(6, 6)) == 6 ** 6
    # Partición equitativa: todos los estados de un mismo peso deben tener la misma
    # tasa total hacia cada clase de peso. Con tasas (1, 2) falla.
    def equitable(n, rates):
        for s in range(1 << n):
            for s2 in range(1 << n):
                if bin(s).count("1") != bin(s2).count("1"): continue
                for target in range(n + 1):
                    r1 = sum(rates[j] for j in range(n) if bin(s ^ (1 << j)).count("1") == target)
                    r2 = sum(rates[j] for j in range(n) if bin(s2 ^ (1 << j)).count("1") == target)
                    if r1 != r2: return False, (format(s, f"0{n}b"), format(s2, f"0{n}b"), target, r1, r2)
        return True, None
    res["tasas_iguales_equitativa"] = equitable(3, [1, 1, 1])[0]
    eq, testigo = equitable(2, [1, 2])
    res["tasas_(1,2)_equitativa"] = eq
    res["testigo_(estado_a, estado_b, clase_destino, tasa_a, tasa_b)"] = testigo
    OUT["E11_hipercubo"] = res
    print("E11", res, flush=True)

# ---------------------------------------------------------------- E12
def E12():
    """Verificación cruzada de afirmaciones de las dos investigaciones independientes (§12)."""
    res = {}
    res["umbral_8_de_18"] = sum(math.comb(18, w) for w in range(8, 19))
    def mycielski(G):
        n = G.number_of_nodes(); H = nx.Graph(); H.add_nodes_from(range(2 * n + 1))
        for u, v in G.edges():
            H.add_edge(u, v); H.add_edge(u, n + v); H.add_edge(v, n + u)
        for i in range(n): H.add_edge(n + i, 2 * n)
        return H
    def colorable(H, k):
        nodes = sorted(H.nodes(), key=lambda v: -H.degree(v)); col = {}
        def bt(i):
            if i == len(nodes): return True
            v = nodes[i]
            for c in range(k):
                if all(col.get(u) != c for u in H[v]):
                    col[v] = c
                    if bt(i + 1): return True
                    del col[v]
            return False
        return bt(0)
    G = mycielski(nx.cycle_graph(5))
    contiene_C5 = all(G.has_edge(i, (i + 1) % 5) for i in range(5))
    res["grotzsch"] = {"vertices": G.number_of_nodes(), "aristas": G.number_of_edges(),
                       "triangulos": sum(nx.triangles(G).values()) // 3,
                       "3-coloreable": colorable(G, 3), "4-coloreable": colorable(G, 4),
                       "todo_borrado_de_vertice_3-coloreable":
                           all(colorable(G.subgraph([u for u in G if u != v]).copy(), 3) for v in G),
                       "contiene_C5": contiene_C5, "cintura": nx.girth(G)}
    # Cadena óptica por conteo de máximos (parámetros leídos de la figura del informe B)
    pos = np.array([-4.2, -1.6, 0.7, 2.5, 4.4]); amp = np.array([1.0, 0.7, 1.2, 0.5, 0.9])
    x = np.linspace(-9, 9, 36001)
    def picos(s):
        f = (amp[None, :] * np.exp(-(x[:, None] - pos[None, :]) ** 2 / (2 * s * s))).sum(1)
        d = np.diff(f); idx = np.nonzero((d[:-1] > 0) & (d[1:] <= 0))[0] + 1
        return [round(float(x[i]), 2) for i in idx if f[i] > 1e-6 * f.max()]
    sig = np.round(np.arange(0.03, 2.0, 0.005), 3)
    cuentas = [len(picos(s)) for s in sig]
    primero = {}
    for s, c in zip(sig, cuentas): primero.setdefault(c, float(s))
    res["optica_conteo_de_maximos"] = {
        "primer_sigma_con_k_maximos": primero,
        "monotono": all(a >= b for a, b in zip(cuentas, cuentas[1:])),
        "maximos_en_sigma=1.45": picos(1.45)}
    OUT["E12_verificacion_cruzada"] = res
    print("E12", res, flush=True)

# ---------------------------------------------------------------- figura
def figura_optica():
    """Figura de la ley de fusión (E6). Requiere matplotlib; si no está, se omite."""
    try:
        import matplotlib; matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("figura omitida: falta matplotlib"); return
    xs = np.linspace(-1, 1, 5)
    i = np.arange(600) + 0.5
    phi = np.arccos(1 - 2 * i / 600); th = np.pi * (1 + 5 ** 0.5) * i
    Y = np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], 1)
    src = np.stack([xs, 0 * xs, 0 * xs], 1)
    Rs = np.logspace(0, 4, 400)
    svs = []
    for R in Rs:
        D = np.linalg.norm(R * Y[:, None, :] - src[None, :, :], axis=2)
        s = np.linalg.svd(1.0 / D, compute_uv=False); svs.append(s / s[0])
    svs = np.array(svs)
    textos = {"fusion_optica.png": ("distancia R/r", "distinciones observables",
                                    "Cada distinción se funde a R ∝ ε^(−1/ℓ)"),
              "optical_fusion.png": ("distance R/r", "observable distinctions",
                                     "Each distinction merges at R ∝ ε^(−1/ℓ)")}
    for nombre, (xl, yl, titulo) in textos.items():
        fig, ax = plt.subplots(figsize=(8, 4))
        for eps, a in ((1e-2, 0.35), (1e-3, 0.65), (1e-4, 1.0)):
            ax.step(Rs, (svs > eps).sum(1), where="post", color="#2563eb", alpha=a, lw=2,
                    label=f"ε = {eps:g}")
        ax.set_xscale("log"); ax.set_yticks([1, 2, 3, 4, 5])
        ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_title(titulo)
        ax.grid(alpha=0.3); ax.legend(frameon=False)
        fig.tight_layout(); fig.savefig(nombre, dpi=160); plt.close(fig)
        print("figura:", nombre)

EXPERIMENTOS["E11"] = E11
EXPERIMENTOS["E12"] = E12
EXPERIMENTOS["figura"] = figura_optica

if __name__ == "__main__":
    random.seed(0)
    t0 = time.time()
    elegidos = sys.argv[1:] or list(EXPERIMENTOS)
    for k in elegidos:
        EXPERIMENTOS[k]()
    OUT["segundos_totales"] = round(time.time() - t0, 1)
    nombre = "resultados_laboratorio.json" if not sys.argv[1:] else "resultados_" + "_".join(elegidos) + ".json"
    with open(nombre, "w", encoding="utf-8") as fh:
        json.dump(OUT, fh, ensure_ascii=False, indent=1, default=str)
    print("listo", OUT["segundos_totales"], "s")
