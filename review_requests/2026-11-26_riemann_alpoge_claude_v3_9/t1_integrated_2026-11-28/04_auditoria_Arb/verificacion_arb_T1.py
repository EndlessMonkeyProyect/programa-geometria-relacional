"""Recalculo independiente del Anexo T.1 v1.3 con aritmetica de bolas (Arb, python-flint).

Construccion propia, sin reutilizar el script del paquete:
  * <e_a,e_b> en H = L^2((0,inf), dt/t^2), e_d(t) = {t/d}: formula de Vasyunin con las sumas
    V(h,k) = sum_{m<k} {mh/k} cot(pi m/k) evaluadas en Arb (cotangentes por modulo, terminos
    emparejados m <-> k-m). Cada entrada sale como bola con radio certificado.
  * <e_d, chi> = (log d + 1 - gamma)/d, ||chi||^2 = 1.
  * Por etapa: Q_S, Q_{S+p}, S_p, v, tres vias para Delta Q_S, K^J, K^H, M en coordenadas
    ortonormales de firmas con Cholesky exacto de Kronecker (L = kron_q L_q), c, a, b+,
    beta, gamma, eta, mu (espejo), testigos sueltos, lectura con G como referencia.
  * Las cotas inferiores se comprueban como desigualdades entre bolas.

Uso: python3 -I verificacion_arb_T1.py [pmax]   (pmax por defecto 17; 19 agrega una etapa)
"""
import sys, json, time, math
from math import gcd
from functools import reduce
import flint
from flint import arb, arb_mat, fmpq
import mpmath as mp
import numpy as np

flint.ctx.prec = 192
mp.mp.dps = 45
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 17
PRIMES = [q for q in [2, 3, 5, 7, 11, 13, 17, 19, 23] if q <= PMAX]

PI = arb.pi()
EUL = arb.const_euler()
LOG2PI = (2 * PI).log()


def divisors(S):
    ds = [1]
    for q in S:
        ds = ds + [d * q for d in ds]
    return ds  # orden de Kronecker: el primo mas reciente es el bit mas significativo


# ---------- Gram funcional en bolas ----------
def gram_entries(divs):
    """Devuelve dict {(a,b): <e_a,e_b>} para todos los pares de divs (a<=b)."""
    need = {}  # modulo k -> conjunto de h (mod k) con gcd(h,k)=1
    pairs = []
    for i, a in enumerate(divs):
        for b in divs[i:]:
            g = gcd(a, b); h, k = sorted((a // g, b // g))
            pairs.append((a, b, g, h, k))
            if k > 1: need.setdefault(k, set()).add(h % k)
            if h > 1: need.setdefault(h, set()).add(k % h)
    V = {}
    for k in sorted(need):
        half = (k - 1) // 2
        cot = [None] + [(arb(fmpq(m, k))).cot_pi() for m in range(1, half + 1)]
        for h in need[k]:
            s = arb(0)
            for m in range(1, half + 1):
                s += (2 * ((m * h) % k) - k) * cot[m]
            V[(h, k)] = s / k
        del cot
    out = {}
    for a, b, g, h, k in pairs:
        Vhk = V[(h % k, k)] if k > 1 else arb(0)
        Vkh = V[(k % h, h)] if h > 1 else arb(0)
        I = ((LOG2PI - EUL) / 2 * (arb(1) / h + arb(1) / k)
             + arb(k - h) / (2 * h * k) * (arb(h) / k).log()
             - PI / (2 * h * k) * (Vhk + Vkh))
        out[(a, b)] = out[(b, a)] = I / g
    return out


def ipchi(d):
    return (arb(d).log() + 1 - EUL) / d


def col(lst):
    return arb_mat([[x] for x in lst])


def dot(u, w):
    return (u.transpose() * w)[0, 0]


def to_mp(A):
    return mp.matrix([[mp.mpf(A[i, j].mid().str(50, radius=False)) for j in range(A.ncols())]
                      for i in range(A.nrows())])


def f(x, n=12):
    return float(x.mid().str(n + 5, radius=False))


def run():
    t0 = time.time()
    alldiv = divisors(PRIMES)
    E = gram_entries(alldiv)
    t_gram = time.time() - t0
    rad_max = max(float(E[k].rad()) for k in E)
    stages = []
    for i, p in enumerate(PRIMES):
        S = PRIMES[:i]; D = divisors(S); r = len(D)
        G = arb_mat([[E[(d, e)] for e in D] for d in D])
        C = arb_mat([[E[(d, p * e)] for e in D] for d in D])
        Gp_ = G * (arb(1) / p)
        Gpr = arb_mat([[E[(x, y)] for y in D + [p * e for e in D]] for x in D + [p * e for e in D]])
        b = col([ipchi(d) for d in D]); bp = col([ipchi(p * d) for d in D])
        bb = col([ipchi(d) for d in D] + [ipchi(p * d) for d in D])
        Gb = G.solve(b)
        QS = 1 - dot(b, Gb)
        QSp = 1 - dot(bb, Gpr.solve(bb))
        X = G.solve(C)
        Sp = Gp_ - C.transpose() * X
        v = bp - X.transpose() * b
        dQ_dir = QS - QSp
        dQ_schur = dot(v, Sp.solve(v))
        # firmas: H_S = (1/lcm) y Cholesky exacto de Kronecker
        H = arb_mat([[arb(fmpq(1, d * e // gcd(d, e))) for e in D] for d in D])
        L = arb_mat([[1]])
        for q in S:
            Lq = arb_mat([[1, 0], [arb(fmpq(1, q)), (arb(fmpq(q - 1, q * q))).sqrt()]])
            # kron(Lq, L) respeta el orden de divisors(): bit alto = primo q
            n = L.nrows()
            K = arb_mat(2 * n, 2 * n)
            for a_ in range(2):
                for b_ in range(2):
                    for x in range(n):
                        for y in range(n):
                            K[a_ * n + x, b_ * n + y] = Lq[a_, b_] * L[x, y]
            L = K
        LLt = L * L.transpose()
        chol_err = max(float(abs(LLt[x, y] - H[x, y]).upper()) for x in range(r) for y in range(r))
        Li = L.inv()
        fac = arb(p * p) / (p - 1)
        M = fac * (Li * Sp * Li.transpose())
        c = (arb(p) / arb(p - 1).sqrt()) * (Li * v)
        dQ_transp = dot(c, M.solve(c))
        Mm = to_mp(M); Mm = (Mm + Mm.T) / 2
        ev = mp.eigsy(Mm, eigvals_only=True)
        ev = sorted([ev[j] for j in range(r)])
        a_min, b_max = ev[0], ev[-1]
        c2 = dot(c, c); cMc = dot(c, M * c)
        beta = c2 / (arb(str(b_max)) * QS)
        gamma = c2 * c2 / (cMc * QS)
        eta = dQ_schur / QS
        # referencia G
        Gv = G.solve(v)
        gammaG = dot(v, Gv) ** 2 / (dot(Gv, Sp * Gv) * QS)
        Gm = to_mp(G); Spm = to_mp(Sp)
        LG = mp.cholesky((Gm + Gm.T) / 2); LGi = mp.inverse(LG)
        MG = LGi * Spm * LGi.T; MG = (MG + MG.T) / 2
        evG = sorted([x for x in mp.eigsy(MG, eigvals_only=True)])
        # espejo
        gvec = v * arb(p)                       # <e_d, g> = p v_d
        mu = dot(gvec, G.solve(gvec)) / (arb(p) * QS)
        def wit(xvec):
            x = col(xvec)
            return arb(p) * dot(x, gvec) ** 2 / (dot(x, G * x) * arb(p) * QS)
        w_unit = wit([1] + [0] * (r - 1))
        w_eul = wit([(-1) ** sum(1 for q in S if d % q == 0) for d in D])
        w_apr = wit([Gb[j, 0] for j in range(r)])
        # costos
        KJ = arb(r) / 2 * (arb(p) / (p - 1)).log()
        Hn = arb_mat(2 * r, 2 * r); s = arb(1) / arb(p).sqrt()
        for x in range(r):
            for y in range(r):
                Hn[x, y] = Hn[r + x, r + y] = H[x, y]
                Hn[x, r + y] = Hn[r + x, y] = H[x, y] * s
        KJ_det = -(Hn.det() / H.det() ** 2).log() / 2
        detG = G.det()
        KH = -(Gpr.det() / (detG * detG * arb(p) ** (-r))).log() / 2
        kappaH = reduce(lambda acc, q: acc * (lambda lm: lm[1] / lm[0])(
            sorted(np.linalg.eigvalsh(np.array([[1, 1 / q], [1 / q, 1 / q]])))), S, 1.0)
        cond_Gp = float(np.linalg.cond(np.array(to_mp(Gpr).tolist(), dtype=float)))  # norma 2 (SVD)
        R = dict(p=p, r=r, QS=QS, QSp=QSp, dQ_dir=dQ_dir, dQ_schur=dQ_schur, dQ_transp=dQ_transp,
                 KJ=KJ, KJ_det=KJ_det, KH=KH, a=a_min, bplus=b_max, cond_M=b_max / a_min,
                 kappaH=kappaH, beta=beta, gamma=gamma, eta=eta, mu=mu, gammaG=gammaG,
                 condMG=evG[-1] / evG[0], w_unit=w_unit, w_eul=w_eul, w_apr=w_apr,
                 chol_err=chol_err, cond_Gp=cond_Gp)
        stages.append(R)
        print(f"  etapa p={p:2d} lista ({time.time()-t0:6.1f} s)", flush=True)
    return stages, t_gram, rad_max, len(E) // 2


if __name__ == "__main__":
    stages, t_gram, rad_max, nent = run()
    print(f"\nGram: {nent} entradas en {t_gram:.1f} s; radio maximo de bola = {rad_max:.1e}")
    print("\nTabla 1")
    print(" p    r    K^J     K^H        a         b+      b+/a   kappa(H_S)")
    for R in stages:
        print(f"{R['p']:2d} {R['r']:4d}  {f(R['KJ']):.4f}  {f(R['KH']):8.4f}  {float(R['a']):.5f}  {float(R['bplus']):.5f}"
              f"  {float(R['cond_M']):7.2f}  {R['kappaH']:.4g}")
    print("\nTabla 2 (Q con 15 cifras; radio de la bola entre corchetes)")
    print(" p   Q_{S+p}                         p*beta     p*gamma    p*mu      p*eta      gamma/eta")
    for R in stages:
        p = R['p']
        print(f"{p:2d}  {R['QSp'].mid().str(15, radius=False):>18s} [{float(R['QSp'].rad()):.0e}]"
              f"  {p*f(R['beta']):.6f}  {p*f(R['gamma']):.5f}  {p*f(R['mu']):.4f}  {p*f(R['eta']):.6f}"
              f"  {f(R['gamma'])/f(R['eta']):.3f}")
    print("\nCoherencia y desigualdades (comprobadas como bolas)")
    for R in stages:
        e1 = abs(R['dQ_dir'] - R['dQ_schur']).upper(); e2 = abs(R['dQ_schur'] - R['dQ_transp']).upper()
        ok_mu = (R['eta'] - R['mu']) > 0
        ok_g = (R['eta'] - R['gamma']) >= 0 or R['r'] == 1
        ok_KJ = abs(R['KJ'] - R['KJ_det']).upper()
        print(f"  p={R['p']:2d}: |dQ dir-Schur|<={float(e1):.1e}  |Schur-transp|<={float(e2):.1e}  "
              f"eta>mu: {ok_mu}  eta>=gamma: {ok_g}  |KJ-det|<={float(ok_KJ):.1e}  "
              f"|LL^T-H|<={R['chol_err']:.0e}  cond(G')={R['cond_Gp']:.2e}")
    print("\nReferencia G y testigos sueltos (p*fraccion)")
    print(" p   b+/a(G)   gammaG/eta   unidad   Euler   aproximante   p*mu")
    for R in stages:
        p = R['p']
        print(f"{p:2d}  {float(R['condMG']):7.2f}    {f(R['gammaG'])/f(R['eta']):.4f}     {f(R['w_unit']):.3f}   "
              f"{f(R['w_eul']):.3f}   {f(R['w_apr']):.3f}        {p*f(R['mu']):.4f}")
    out = []
    for R in stages:
        out.append({k: (R[k].mid().str(25, radius=False) if isinstance(R[k], arb) else
                        (str(R[k]) if isinstance(R[k], mp.mpf) else R[k])) for k in R})
    json.dump(dict(etapas=out, radio_max_gram=rad_max), open(f"resultados_arb_T1_p{PMAX}.json", "w"), indent=1)
