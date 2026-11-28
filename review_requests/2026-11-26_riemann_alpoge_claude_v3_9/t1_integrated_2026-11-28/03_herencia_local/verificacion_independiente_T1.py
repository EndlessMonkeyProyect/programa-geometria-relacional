"""Verificación independiente del Anexo T.1 (Nota técnica 01 v3.9).

Implementación propia, sin el paquete v3.9:
  * Gram de H = L^2((0,inf), dt/t^2) con e_d(t) = {t/d} por la fórmula cerrada de Vasyunin,
    validada contra integración directa por tramos.
  * Etapas p = 2..17: K^J, K^H, a, b+, b+/a, Q_{S+p}, p*beta_p, p*eta_p (tablas de la sección 6).
  * Comprobaciones: identidad (5) por tres vías, estructura de Kronecker de H_S,
    condicionamiento, cota testigo gamma_p = |c|^4 / (c*Mc Q_S) con la métrica de conteo
    y con el Gram funcional G, cota del espejo mu_p y testigos sueltos, y Q_{S+17} con álgebra lineal de 40 dígitos (si hay mpmath).

Uso:  python3 -I verificacion_independiente_T1.py   (numpy >= 1.24; mpmath opcional)
Escribe resultados_independientes_T1.json en el directorio actual.
"""
import json, math
from functools import lru_cache, reduce
from math import gcd, log, pi, sqrt
import numpy as np

EULER = 0.57721566490153286060651209008240243
LOG2PI = math.log(2 * math.pi)
PRIMES = [2, 3, 5, 7, 11, 13, 17]


# ---------- Gram funcional ----------
def _V(h, k):
    """Suma de Vasyunin V(h,k) = sum_{m=1}^{k-1} {mh/k} cot(pi m/k)."""
    if k == 1:
        return 0.0
    m = np.arange(1, k, dtype=np.int64)
    return float(np.sum(((m * h) % k) / k / np.tan(np.pi * m / k)))


@lru_cache(maxsize=None)
def _ipc(h, k):
    """<e_h, e_k> para h, k coprimos (fórmula de Vasyunin)."""
    return ((LOG2PI - EULER) / 2 * (1 / h + 1 / k) + (k - h) / (2 * h * k) * log(h / k)
            - pi / (2 * h * k) * (_V(h, k) + _V(k, h)))


def ip(a, b):
    g = gcd(a, b)
    h, k = sorted((a // g, b // g))
    return _ipc(h, k) / g


def ip_chi(d):
    """<e_d, chi> = (log d + 1 - gamma)/d."""
    return (log(d) + 1 - EULER) / d


def direct(a, b, nper=100000, nodes=12):
    """Integral directa de {t/a}{t/b}/t^2: Gauss-Legendre por tramo hasta X = nper*mcm, más cola media/X."""
    L = a * b // gcd(a, b)
    per = np.array(sorted({i * a for i in range(L // a + 1)} | {j * b for j in range(L // b + 1)}), float)
    u0, w0 = per[:-1], per[1:]
    offs = np.arange(nper, dtype=float) * L
    U = (u0[None, :] + offs[:, None]).ravel(); W = (w0[None, :] + offs[:, None]).ravel()
    keep = U > 0; U, W = U[keep], W[keep]
    xg, wg = np.polynomial.legendre.leggauss(nodes)
    mid, half = (U + W) / 2, (W - U) / 2
    t = mid[:, None] + half[:, None] * xg[None, :]
    m = np.floor(mid / a)[:, None]; n = np.floor(mid / b)[:, None]
    vals = half * (((t / a - m) * (t / b - n) / t**2) @ wg)
    fs = 0.0
    for uu, ww in zip(u0, w0):
        mm, nn = uu // a, uu // b
        F = lambda s: s**3 / (3 * a * b) - (nn / a + mm / b) * s**2 / 2 + mm * nn * s
        fs += F(ww) - F(uu)
    return math.fsum(vals.tolist()) + per[1] / (a * b) + (fs / L) / (nper * L)


# ---------- Etapas ----------
def divisors(S):
    ds = [1]
    for q in S:
        ds = ds + [d * q for d in ds]
    return sorted(ds)


def lcm(a, b):
    return a * b // gcd(a, b)


def stage(S, p):
    D = divisors(S); r = len(D)
    G = np.array([[ip(d, e) for e in D] for d in D])
    C = np.array([[ip(d, p * e) for e in D] for d in D])
    Gp = np.block([[G, C], [C.T, G / p]])
    b = np.array([ip_chi(d) for d in D]); bp = np.array([ip_chi(p * d) for d in D])
    Sp = G / p - C.T @ np.linalg.solve(G, C); Sp = (Sp + Sp.T) / 2
    v = bp - C.T @ np.linalg.solve(G, b)
    QS = 1.0 - b @ np.linalg.solve(G, b)
    bb = np.concatenate([b, bp]); QSp = 1.0 - bb @ np.linalg.solve(Gp, bb)
    dQ_schur = v @ np.linalg.solve(Sp, v)
    H = np.array([[1.0 / lcm(d, e) for e in D] for d in D])
    Li = np.linalg.inv(np.linalg.cholesky(H))
    M = p**2 / (p - 1) * Li @ Sp @ Li.T; M = (M + M.T) / 2
    c = p / sqrt(p - 1) * Li @ v
    ev = np.linalg.eigvalsh(M); a_, bplus = ev[0], ev[-1]
    dQ_transport = c @ np.linalg.solve(M, c)
    # costo de firmas: fórmula (3) y determinante directo del Gram normalizado de los dos bloques
    KJ = r / 2 * log(p / (p - 1))
    _, ldH = np.linalg.slogdet(H)
    _, ldHn = np.linalg.slogdet(np.block([[H, H / sqrt(p)], [H / sqrt(p), H]]))
    KJ_det = -0.5 * (ldHn - 2 * ldH)
    # K^H como -1/2 log det del Gram funcional normalizado por bloques (coincide con la tabla)
    _, ldGp = np.linalg.slogdet(Gp); _, ldG = np.linalg.slogdet(G)
    KH = -0.5 * (ldGp - 2 * ldG + r * log(p))
    # H_S como producto de Kronecker de [[1,1/q],[1/q,1/q]]
    K = reduce(np.kron, [np.array([[1, 1 / q], [1 / q, 1 / q]]) for q in S], np.array([[1.0]]))
    kron_ok = bool(np.allclose(np.sort(np.linalg.eigvalsh(K)), np.sort(np.linalg.eigvalsh(H))))
    beta = (c @ c) / (bplus * QS); eta = dQ_schur / QS
    gamma = (c @ c) ** 2 / ((c @ M @ c) * QS)
    # misma cota de espectro con el Gram funcional G como métrica de referencia
    LGi = np.linalg.inv(np.linalg.cholesky(G))
    MG = LGi @ Sp @ LGi.T; MG = (MG + MG.T) / 2; cG = LGi @ v
    evG = np.linalg.eigvalsh(MG)
    beta_G = (cG @ cG) / (evG[-1] * QS)
    gamma_G = (cG @ cG) ** 2 / ((cG @ MG @ cG) * QS)
    # cota del espejo: g = u_S(p.), <e_d, g> = p v_d, |g|^2 = p Q_S, eta_p >= mu_p = |Pi_S g|^2/|g|^2
    gc = p * v
    mu = (gc @ np.linalg.solve(G, gc)) / (p * QS)
    def wit(x):   # fracción de g reconocida por un solo elemento sum x_d e_d de V_S
        return (x @ gc) ** 2 / ((x @ G @ x) * p * QS)
    x_unit = np.zeros(r); x_unit[0] = 1.0                                   # e_1 (espejo: e_p)
    x_mob = np.array([(-1.0) ** sum(1 for q in S if d % q == 0) for d in D])  # sum mu(d) e_d
    x_apr = np.linalg.solve(G, b)                                           # aproximante Pi_S chi
    return dict(p=p, r=r, mu=mu, p_mu=p * mu, mu_over_eta=mu / eta,
                p_wit_unidad=p * wit(x_unit), p_wit_euler=p * wit(x_mob), p_wit_aproximante=p * wit(x_apr),
                KJ=KJ, KJ_det=KJ_det, KH=KH, a=a_, bplus=bplus, cond_M=bplus / a_,
                QS=QS, QSp=QSp, p_beta=p * beta, p_eta=p * eta, eta=eta, p_gamma=p * gamma,
                beta_over_eta=beta / eta, gamma_over_eta=gamma / eta,
                betaG_over_eta=beta_G / eta, gammaG_over_eta=gamma_G / eta, cond_MG=evG[-1] / evG[0],
                err_dQ_direct_vs_schur=abs((QS - QSp) - dQ_schur),
                err_schur_vs_transport=abs(dQ_schur - dQ_transport),
                cond_Gprime=float(np.linalg.cond(Gp)), cond_H=float(np.linalg.cond(H)),
                H_is_kronecker=kron_ok, norm_c2=float(c @ c))


if __name__ == "__main__":
    print("1) Validación de Vasyunin contra integración directa")
    val = []
    for a, b in [(1, 1), (1, 2), (2, 3), (1, 5), (3, 5), (2, 15), (6, 35), (10, 21), (1, 7)]:
        L = a * b // gcd(a, b)
        dv = direct(a, b, nper=max(2000, 200000 // L))
        val.append(dict(a=a, b=b, vasyunin=ip(a, b), directa=dv, dif=abs(ip(a, b) - dv)))
        print(f"   <e_{a},e_{b}>  Vasyunin={ip(a,b):.12f}  directa={dv:.12f}  dif={abs(ip(a,b)-dv):.1e}")
    print("\n2) Etapas (columnas de las tablas de la sección 6 y diagnósticos)")
    hdr = " p   r   K^J     K^H       a        b+     b+/a    Q_{S+p}      p*beta    p*eta    p*gamma  cond(G')"
    print(hdr)
    out = []
    for i, p in enumerate(PRIMES):
        R = stage(PRIMES[:i], p); out.append(R)
        print(f"{p:2d} {R['r']:3d}  {R['KJ']:.4f}  {R['KH']:8.4f}  {R['a']:.5f}  {R['bplus']:.5f}"
              f"  {R['cond_M']:6.2f}  {R['QSp']:.9f}  {R['p_beta']:.6f}  {R['p_eta']:.6f}"
              f"  {R['p_gamma']:.5f}  {R['cond_Gprime']:.1e}")
    print("\n   max |K^J(3) - K^J(det)|      =", f"{max(abs(R['KJ']-R['KJ_det']) for R in out):.1e}")
    print("   max |dQ directo - v*Sp^-1 v| =", f"{max(R['err_dQ_direct_vs_schur'] for R in out):.1e}")
    print("   max |v*Sp^-1 v - c*M^-1 c|   =", f"{max(R['err_schur_vs_transport'] for R in out):.1e}")
    print("   H_S = kron_q [[1,1/q],[1/q,1/q]] en todas las etapas:", all(R['H_is_kronecker'] for R in out))
    print("\n3) Lectura con otra referencia (Gram funcional G) y cocientes testigo")
    print(" p   cond(H_S)   b+/a (H)   b+/a (G)   gamma/eta (H)   gamma/eta (G)")
    for R in out:
        print(f"{R['p']:2d}  {R['cond_H']:9.4g}  {R['cond_M']:8.2f}  {R['cond_MG']:8.2f}     {R['gamma_over_eta']:.3f}          {R['gammaG_over_eta']:.3f}")
    print("\n4) Cota del espejo: eta_p >= mu_p = |Pi_S u_S(p.)|^2 / |u_S(p.)|^2")
    print(" p    p*mu    p*eta   mu/eta  | testigos sueltos (p*fracción): unidad   Euler   aproximante")
    for R in out:
        print(f"{R['p']:2d}  {R['p_mu']:6.3f}  {R['p_eta']:6.3f}  {R['mu_over_eta']:6.3f}  |"
              f"                          {R['p_wit_unidad']:6.3f}  {R['p_wit_euler']:6.3f}  {R['p_wit_aproximante']:6.3f}")
    print("   mu_p <= eta_p en todas las etapas:", all(R['mu'] <= R['eta'] * (1 + 1e-12) for R in out))
    q40 = None
    try:
        import mpmath as mp
        mp.mp.dps = 40
        D = divisors(PRIMES[:6]); D2 = D + [17 * d for d in D]
        Gp = mp.matrix([[ip(a, b) for b in D2] for a in D2]); bb = mp.matrix([ip_chi(d) for d in D2])
        x = mp.lu_solve(Gp, bb); q40 = 1 - sum(bb[i] * x[i] for i in range(len(D2)))
        print("\n5) Q_{S+17} con álgebra lineal de 40 dígitos (entradas en doble):", mp.nstr(q40, 12))
        q40 = float(q40)
    except ImportError:
        print("\n5) mpmath no disponible: se omite la comprobación de 40 dígitos")
    json.dump(dict(validacion_vasyunin=val, etapas=out, Q_S17_40digitos=q40), open("resultados_independientes_T1.json", "w"),
              indent=1, default=float)
