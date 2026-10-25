"""
MF-96 / Rama Yang–Mills — experimento E-YM.

Red 4D periódica L^4, acción de Wilson, baño térmico (heat-bath) + sobrerrelajación.
  * SU(2): Kennedy–Pendleton.     * U(1) compacto: von Mises (Best–Fisher).

Mide:
  (a) lazos de Wilson W(R,T) y razones de Creutz χ(R,R) a acoplamiento débil:
      control abeliano/no abeliano (SU(2) confina a todo β; U(1) entra en fase de Coulomb para β > ~1.01).
  (b) cota inferior del mejor coeficiente C_* de la forma por bloques (MF-94/95) usando
      - un modo gauge de un solo enlace  h = ½ReTr U_e   (SU(2))  /  h = cos θ_e  (U(1)),
      - una función gauge-invariante     h = ½ReTr U_p   (plaqueta),
      vía  C_* ≥ Var_μ(h) / Σ_e E_μ[ Var(h | U_{-e}) ],  con la varianza condicional calculada
      en forma cerrada (funciones de Bessel) a partir de las grapas.
"""
import sys, json, time, math
import numpy as np
import numba as nb
from scipy.special import ive


# ------------------------------------------------------------------ geometría
@nb.njit(cache=False)
def make_nbrs(L):
    V = L**4
    up = np.empty((V, 4), np.int64)
    dn = np.empty((V, 4), np.int64)
    c = np.empty(4, np.int64)
    for s in range(V):
        r = s
        for mu in range(4):
            c[mu] = r % L
            r //= L
        for mu in range(4):
            su = 0
            sd = 0
            m = 1
            for nu in range(4):
                cu = c[nu]
                cd = c[nu]
                if nu == mu:
                    cu = (c[nu] + 1) % L
                    cd = (c[nu] - 1) % L
                su += cu * m
                sd += cd * m
                m *= L
            up[s, mu] = su
            dn[s, mu] = sd
    return up, dn


# ------------------------------------------------------------ cuaterniones SU(2)
@nb.njit(inline="always")
def qmul(a0, a1, a2, a3, b0, b1, b2, b3):
    # (a0 + i a·σ)(b0 + i b·σ) = (a0 b0 − a·b) + i (a0 b + b0 a − a×b)·σ
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + b0 * a1 - (a2 * b3 - a3 * b2),
            a0 * b2 + b0 * a2 - (a3 * b1 - a1 * b3),
            a0 * b3 + b0 * a3 - (a1 * b2 - a2 * b1))


@nb.njit(inline="always")
def staple_su2(U, up, dn, s, mu):
    a0 = 0.0; a1 = 0.0; a2 = 0.0; a3 = 0.0
    smu = up[s, mu]
    for nu in range(4):
        if nu == mu:
            continue
        # adelante: U(s+μ,ν) U(s+ν,μ)† U(s,ν)†
        x = U[smu, nu]; y = U[up[s, nu], mu]; z = U[s, nu]
        t = qmul(x[0], x[1], x[2], x[3], y[0], -y[1], -y[2], -y[3])
        t = qmul(t[0], t[1], t[2], t[3], z[0], -z[1], -z[2], -z[3])
        a0 += t[0]; a1 += t[1]; a2 += t[2]; a3 += t[3]
        # atrás: U(s+μ−ν,ν)† U(s−ν,μ)† U(s−ν,ν)
        sdn = dn[s, nu]
        x = U[dn[smu, nu], nu]; y = U[sdn, mu]; z = U[sdn, nu]
        t = qmul(x[0], -x[1], -x[2], -x[3], y[0], -y[1], -y[2], -y[3])
        t = qmul(t[0], t[1], t[2], t[3], z[0], z[1], z[2], z[3])
        a0 += t[0]; a1 += t[1]; a2 += t[2]; a3 += t[3]
    return a0, a1, a2, a3


@nb.njit(inline="always")
def kp_x0(kappa):
    # Kennedy–Pendleton: muestrea x0 con densidad ∝ sqrt(1−x0²) exp(κ x0)
    while True:
        r1 = 1.0 - np.random.random(); r2 = np.random.random(); r3 = 1.0 - np.random.random()
        lam2 = -(math.log(r1) + math.cos(2 * math.pi * r2) ** 2 * math.log(r3)) / (2.0 * kappa)
        r4 = np.random.random()
        if r4 * r4 <= 1.0 - lam2:
            return 1.0 - 2.0 * lam2


@nb.njit(cache=False)
def sweep_su2(U, up, dn, beta, n_or):
    V = U.shape[0]
    for s in range(V):
        for mu in range(4):
            a0, a1, a2, a3 = staple_su2(U, up, dn, s, mu)
            k = math.sqrt(a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3)
            v0 = a0 / k; v1 = a1 / k; v2 = a2 / k; v3 = a3 / k
            x0 = kp_x0(beta * k)
            r = math.sqrt(max(0.0, 1.0 - x0 * x0))
            ct = 2.0 * np.random.random() - 1.0
            ph = 2.0 * math.pi * np.random.random()
            st = math.sqrt(1.0 - ct * ct)
            x1 = r * st * math.cos(ph); x2 = r * st * math.sin(ph); x3 = r * ct
            n = qmul(x0, x1, x2, x3, v0, -v1, -v2, -v3)  # U = X V†
            U[s, mu, 0] = n[0]; U[s, mu, 1] = n[1]; U[s, mu, 2] = n[2]; U[s, mu, 3] = n[3]
    for _ in range(n_or):
        for s in range(V):
            for mu in range(4):
                a0, a1, a2, a3 = staple_su2(U, up, dn, s, mu)
                k = math.sqrt(a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3)
                v0 = a0 / k; v1 = -a1 / k; v2 = -a2 / k; v3 = -a3 / k  # V†
                u = U[s, mu]
                t = qmul(v0, v1, v2, v3, u[0], -u[1], -u[2], -u[3])  # V† U†
                t = qmul(t[0], t[1], t[2], t[3], v0, v1, v2, v3)      # V† U† V†
                nrm = math.sqrt(t[0] ** 2 + t[1] ** 2 + t[2] ** 2 + t[3] ** 2)
                U[s, mu, 0] = t[0] / nrm; U[s, mu, 1] = t[1] / nrm
                U[s, mu, 2] = t[2] / nrm; U[s, mu, 3] = t[3] / nrm


@nb.njit(cache=False)
def staple_info_su2(U, up, dn, beta):
    """Por enlace: κ = βk y la componente 0 de V (dirección de la grapa)."""
    V = U.shape[0]
    kap = np.empty((V, 4)); vq = np.empty((V, 4, 4))
    for s in range(V):
        for mu in range(4):
            a0, a1, a2, a3 = staple_su2(U, up, dn, s, mu)
            k = math.sqrt(a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3)
            kap[s, mu] = beta * k
            vq[s, mu, 0] = a0 / k; vq[s, mu, 1] = a1 / k; vq[s, mu, 2] = a2 / k; vq[s, mu, 3] = a3 / k
    return kap, vq


@nb.njit(cache=False)
def plaq_rest_su2(U, up, dn, s, mu, nu):
    """Para la plaqueta P = U1 U2 U3† U4† en (s;μ,ν) devuelve, para cada uno de sus 4 enlaces e,
    el cuaternión M_e tal que ½ReTr P = (X_e · conj(M_e)) con U_e = X_e V_e†  (ver texto)."""
    U1 = U[s, mu]; U2 = U[up[s, mu], nu]; U3 = U[up[s, nu], mu]; U4 = U[s, nu]
    P = qmul(U1[0], U1[1], U1[2], U1[3], U2[0], U2[1], U2[2], U2[3])
    P = qmul(P[0], P[1], P[2], P[3], U3[0], -U3[1], -U3[2], -U3[3])
    P = qmul(P[0], P[1], P[2], P[3], U4[0], -U4[1], -U4[2], -U4[3])
    return P[0]


# ------------------------------------------------------------------ U(1) compacto
@nb.njit(inline="always")
def vonmises0(kappa):
    if kappa < 1e-8:
        return 2 * math.pi * np.random.random() - math.pi
    tau = 1.0 + math.sqrt(1.0 + 4.0 * kappa * kappa)
    rho = (tau - math.sqrt(2.0 * tau)) / (2.0 * kappa)
    r = (1.0 + rho * rho) / (2.0 * rho)
    while True:
        u1 = np.random.random(); u2 = np.random.random(); u3 = np.random.random()
        z = math.cos(math.pi * u1)
        f = (1.0 + r * z) / (r + z)
        c = kappa * (r - f)
        if c * (2.0 - c) - u2 > 0.0 or math.log(c / u2) + 1.0 - c >= 0.0:
            th = math.acos(max(-1.0, min(1.0, f)))
            return th if u3 > 0.5 else -th


@nb.njit(inline="always")
def staple_u1(th, up, dn, s, mu):
    zr = 0.0; zi = 0.0
    smu = up[s, mu]
    for nu in range(4):
        if nu == mu:
            continue
        p = th[smu, nu] - th[up[s, nu], mu] - th[s, nu]
        zr += math.cos(p); zi += math.sin(p)
        sdn = dn[s, nu]
        p = -th[dn[smu, nu], nu] - th[sdn, mu] + th[sdn, nu]
        zr += math.cos(p); zi += math.sin(p)
    return zr, zi


@nb.njit(cache=False)
def sweep_u1(th, up, dn, beta, n_or):
    V = th.shape[0]
    for s in range(V):
        for mu in range(4):
            zr, zi = staple_u1(th, up, dn, s, mu)
            k = math.sqrt(zr * zr + zi * zi)
            chi = math.atan2(zi, zr)
            th[s, mu] = -chi + vonmises0(beta * k)
    for _ in range(n_or):
        for s in range(V):
            for mu in range(4):
                zr, zi = staple_u1(th, up, dn, s, mu)
                chi = math.atan2(zi, zr)
                th[s, mu] = -2.0 * chi - th[s, mu]


@nb.njit(cache=False)
def staple_info_u1(th, up, dn, beta):
    V = th.shape[0]
    kap = np.empty((V, 4)); chi = np.empty((V, 4))
    for s in range(V):
        for mu in range(4):
            zr, zi = staple_u1(th, up, dn, s, mu)
            kap[s, mu] = beta * math.sqrt(zr * zr + zi * zi)
            chi[s, mu] = math.atan2(zi, zr)
    return kap, chi


# --------------------------------------------------------------- lazos de Wilson
@nb.njit(cache=False)
def wilson_su2(U, up, dn, Rmax):
    V = U.shape[0]
    W = np.zeros((Rmax + 1, Rmax + 1))
    cnt = 0
    for s in range(V):
        for mu in range(4):
            for nu in range(4):
                if nu == mu:
                    continue
                for R in range(1, Rmax + 1):
                    for T in range(1, Rmax + 1):
                        p0 = 1.0; p1 = 0.0; p2 = 0.0; p3 = 0.0
                        x = s
                        for _ in range(R):
                            u = U[x, mu]; t = qmul(p0, p1, p2, p3, u[0], u[1], u[2], u[3])
                            p0, p1, p2, p3 = t; x = up[x, mu]
                        for _ in range(T):
                            u = U[x, nu]; t = qmul(p0, p1, p2, p3, u[0], u[1], u[2], u[3])
                            p0, p1, p2, p3 = t; x = up[x, nu]
                        for _ in range(R):
                            x = dn[x, mu]; u = U[x, mu]
                            t = qmul(p0, p1, p2, p3, u[0], -u[1], -u[2], -u[3]); p0, p1, p2, p3 = t
                        for _ in range(T):
                            x = dn[x, nu]; u = U[x, nu]
                            t = qmul(p0, p1, p2, p3, u[0], -u[1], -u[2], -u[3]); p0, p1, p2, p3 = t
                        W[R, T] += p0
        cnt += 1
    return W / (V * 12)


@nb.njit(cache=False)
def wilson_u1(th, up, dn, Rmax):
    V = th.shape[0]
    W = np.zeros((Rmax + 1, Rmax + 1))
    for s in range(V):
        for mu in range(4):
            for nu in range(4):
                if nu == mu:
                    continue
                for R in range(1, Rmax + 1):
                    for T in range(1, Rmax + 1):
                        a = 0.0
                        x = s
                        for _ in range(R):
                            a += th[x, mu]; x = up[x, mu]
                        for _ in range(T):
                            a += th[x, nu]; x = up[x, nu]
                        for _ in range(R):
                            x = dn[x, mu]; a -= th[x, mu]
                        for _ in range(T):
                            x = dn[x, nu]; a -= th[x, nu]
                        W[R, T] += math.cos(a)
    return W / (V * 12)


# ------------------------------------------------- varianzas condicionales (Bessel)
def su2_moments(kappa):
    i1, i2, i3 = ive(1, kappa), ive(2, kappa), ive(3, kappa)
    m1 = i2 / i1
    m2 = (i2 / kappa + i3) / i1
    return m1, m2


def u1_moments(kappa):
    i0, i1, i2 = ive(0, kappa), ive(1, kappa), ive(2, kappa)
    return i1 / i0, i2 / i0


def cstar_bounds_su2(U, up, dn, beta):
    kap, vq = staple_info_su2(U, up, dn, beta)
    m1, m2 = su2_moments(kap)
    varx0 = m2 - m1 ** 2
    perp = (1.0 - m2) / 3.0
    # modo gauge de un enlace: h = ½ReTr U_e = x·v  ⇒  Var = v0² Var(x0) + |v⃗|² perp
    v0sq = vq[..., 0] ** 2
    var_link = v0sq * varx0 + (1.0 - v0sq) * perp
    h_link = U[..., 0]
    # plaqueta en (μ,ν) = (0,1): h_p = ½ReTr(U_e M) por enlace; se obtiene M numéricamente
    return dict(var_link_cond_mean=float(var_link.mean()), h_link_mean=float(h_link.mean()),
                h_link_var=float(h_link.var()), kappa_mean=float(kap.mean()))


def plaquette_block_su2(U, up, dn, beta, kap, vq):
    """D_block[h_p] para h_p = ½ReTr de la plaqueta (0,1) en cada sitio, exacto vía Bessel."""
    V = U.shape[0]
    m1, m2 = su2_moments(kap)
    varx0 = m2 - m1 ** 2
    perp = (1.0 - m2) / 3.0
    D = np.zeros(V)
    H = np.zeros(V)
    mu, nu = 0, 1
    for s in range(V):
        links = [(s, mu, False), (up[s, mu], nu, False), (up[s, nu], mu, True), (s, nu, True)]
        Us = [U[a, b].copy() for a, b, _ in links]
        H[s] = _plaq_from(Us)[0]
        for e, (a, b, dag) in enumerate(links):
            # h_p como función lineal de X_e: h_p = Σ_c X_c * g_c (g se obtiene evaluando en la base)
            v = vq[a, b]
            g = np.zeros(4)
            for c in range(4):
                X = np.zeros(4); X[c] = 1.0
                Ue = _qm(X, _qd(v))           # U_e = X V†
                Uc = list(Us); Uc[e] = Ue
                g[c] = _plaq_from(Uc)[0]
            D[s] += g[0] ** 2 * varx0[a, b] + (g[1] ** 2 + g[2] ** 2 + g[3] ** 2) * perp[a, b]
    return H, D


def _qm(a, b):
    return np.array(qmul(a[0], a[1], a[2], a[3], b[0], b[1], b[2], b[3]))


def _qd(a):
    return np.array([a[0], -a[1], -a[2], -a[3]])


def _plaq_from(Us):
    U1, U2, U3, U4 = Us
    return _qm(_qm(_qm(U1, U2), _qd(U3)), _qd(U4))


def creutz(W, R):
    return -math.log(W[R, R] * W[R - 1, R - 1] / (W[R, R - 1] * W[R - 1, R]))


def run_wilson(group, L, beta, ntherm, nmeas, every, Rmax, n_or, cold, seed):
    np.random.seed(seed)
    _seed(seed)
    up, dn = make_nbrs(L)
    V = L**4
    if group == "SU2":
        if cold:
            U = np.zeros((V, 4, 4)); U[..., 0] = 1.0
        else:
            U = np.random.normal(size=(V, 4, 4)); U /= np.linalg.norm(U, axis=-1)[..., None]
        sweep, wl = sweep_su2, wilson_su2
        state = U
    else:
        state = np.zeros((V, 4)) if cold else np.random.uniform(-np.pi, np.pi, size=(V, 4))
        sweep, wl = sweep_u1, wilson_u1
    for _ in range(ntherm):
        sweep(state, up, dn, beta, n_or)
    Ws = []
    for i in range(nmeas):
        for _ in range(every):
            sweep(state, up, dn, beta, n_or)
        W = wl(state, up, dn, Rmax)
        Ws.append(0.5 * (W + W.T))
    Ws = np.array(Ws)
    Wm = Ws.mean(0)
    # jackknife por bloques para las razones de Creutz
    nb_ = 10
    blk = np.array_split(np.arange(nmeas), nb_)
    out = dict(group=group, L=L, beta=beta, plaquette=float(Wm[1, 1]), W=Wm.tolist(), creutz={})
    for R in range(2, Rmax + 1):
        try:
            full = creutz(Wm, R)
            jk = []
            for b in blk:
                keep = np.setdiff1d(np.arange(nmeas), b)
                jk.append(creutz(Ws[keep].mean(0), R))
            jk = np.array(jk)
            err = math.sqrt((nb_ - 1) / nb_ * np.sum((jk - jk.mean()) ** 2))
            out["creutz"][str(R)] = [full, err]
        except ValueError:
            out["creutz"][str(R)] = [float("nan"), float("nan")]
    return out


@nb.njit(cache=False)
def _seed(s):
    np.random.seed(s)


def run_cstar(group, L, beta, ntherm, nmeas, n_or, seed):
    np.random.seed(seed)
    _seed(seed)
    up, dn = make_nbrs(L)
    V = L**4
    rec = dict(group=group, L=L, beta=beta)
    if group == "SU2":
        U = np.zeros((V, 4, 4)); U[..., 0] = 1.0
        for _ in range(ntherm):
            sweep_su2(U, up, dn, beta, n_or)
        dl, hv, hm, Hs, Ds = [], [], [], [], []
        for _ in range(nmeas):
            sweep_su2(U, up, dn, beta, n_or)
            kap, vq = staple_info_su2(U, up, dn, beta)
            m1, m2 = su2_moments(kap)
            v0sq = vq[..., 0] ** 2
            dl.append(float((v0sq * (m2 - m1 ** 2) + (1 - v0sq) * (1 - m2) / 3.0).mean()))
            hv.append(U[..., 0].ravel())
            H, D = plaquette_block_su2(U, up, dn, beta, kap, vq)
            Hs.append(H); Ds.append(D)
        hv = np.concatenate(hv); Hs = np.concatenate(Hs); Ds = np.concatenate(Ds)
        rec.update(var_haar_link=0.25, var_link_emp=float(hv.var()), mean_link_emp=float(hv.mean()),
                   D_link=float(np.mean(dl)), ratio_link=0.25 / float(np.mean(dl)),
                   var_plaq=float(Hs.var()), D_plaq=float(Ds.mean()), ratio_plaq=float(Hs.var() / Ds.mean()),
                   plaq_mean=float(Hs.mean()))
    else:
        th = np.zeros((V, 4))
        for _ in range(ntherm):
            sweep_u1(th, up, dn, beta, n_or)
        dl, hv = [], []
        for _ in range(nmeas):
            sweep_u1(th, up, dn, beta, n_or)
            kap, chi = staple_info_u1(th, up, dn, beta)
            a1, a2 = u1_moments(kap)
            # θ_e = −χ + φ, φ ~ vM(0,κ):  h = cos θ_e  ⇒ Var = ½(1 + A2 cos 2χ) − A1² cos² χ
            var = 0.5 * (1 + a2 * np.cos(2 * chi)) - (a1 * np.cos(chi)) ** 2
            dl.append(float(var.mean()))
            hv.append(np.cos(th).ravel())
        hv = np.concatenate(hv)
        rec.update(var_haar_link=0.5, var_link_emp=float(hv.var()), mean_link_emp=float(hv.mean()),
                   D_link=float(np.mean(dl)), ratio_link=0.5 / float(np.mean(dl)))
    return rec


if __name__ == "__main__":
    mode = sys.argv[1]
    out = sys.argv[2]
    t0 = time.time()
    res = []
    if mode == "cstar":
        for b in [1.0, 1.5, 2.0, 2.3, 2.5, 3.0, 4.0, 6.0, 8.0]:
            r = run_cstar("SU2", 6, b, 60, 20, 2, 11)
            res.append(r); print(r, round(time.time() - t0), flush=True)
        for b in [0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0]:
            r = run_cstar("U1", 6, b, 60, 20, 2, 12)
            res.append(r); print(r, round(time.time() - t0), flush=True)
    elif mode == "wilson":
        L = int(sys.argv[3]) if len(sys.argv) > 3 else 10
        jobs = [("SU2", 2.3, False), ("SU2", 2.4, False), ("SU2", 2.5, False),
                ("U1", 0.9, False), ("U1", 1.1, True), ("U1", 1.3, True)]
        for g, b, cold in jobs:
            r = run_wilson(g, L, b, 150, 120, 2, 4, 3, cold, 21)
            res.append(r)
            print(g, b, "plaq", round(r["plaquette"], 4), {k: [round(v[0], 4), round(v[1], 4)] for k, v in r["creutz"].items()},
                  round(time.time() - t0), "s", flush=True)
    elif mode == "scan":
        # continuidad del flujo: plaqueta media vs β con arranque frío y caliente (histéresis)
        L = 6
        for g, betas in [("U1", np.round(np.arange(0.70, 1.31, 0.05), 3)), ("SU2", np.round(np.arange(1.0, 3.01, 0.2), 3))]:
            up, dn = make_nbrs(L)
            V = L**4
            for start in ("frio", "caliente"):
                for b in betas:
                    np.random.seed(5); _seed(5)
                    if g == "SU2":
                        if start == "frio":
                            st = np.zeros((V, 4, 4)); st[..., 0] = 1.0
                        else:
                            st = np.random.normal(size=(V, 4, 4)); st /= np.linalg.norm(st, axis=-1)[..., None]
                        sw, wl = sweep_su2, wilson_su2
                    else:
                        st = np.zeros((V, 4)) if start == "frio" else np.random.uniform(-np.pi, np.pi, size=(V, 4))
                        sw, wl = sweep_u1, wilson_u1
                    for _ in range(60):
                        sw(st, up, dn, float(b), 2)
                    ps = []
                    for _ in range(60):
                        sw(st, up, dn, float(b), 2)
                        ps.append(wl(st, up, dn, 1)[1, 1])
                    rec = dict(group=g, beta=float(b), start=start, plaquette=float(np.mean(ps)), plaq_err=float(np.std(ps) / math.sqrt(len(ps))))
                    res.append(rec)
                    print(rec, round(time.time() - t0), flush=True)
    with open(out, "w") as fh:
        json.dump(res, fh, indent=1)
    print("saved", out, round(time.time() - t0), "s")
