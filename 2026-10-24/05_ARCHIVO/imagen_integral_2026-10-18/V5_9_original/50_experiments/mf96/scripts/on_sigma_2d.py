"""
MF-96 / Rama Yang–Mills (laboratorio 2D) — experimento E-YM2.

Modelo sigma O(n) en red cuadrada L×L, acción  S = −β Σ_<ij> s_i·s_j,  algoritmo de Wolff.
  * O(3): rotaciones relativas no conmutan (SO(3)); libertad asintótica, transmutación
          dimensional, gap (numéricamente establecido; rigurosamente abierto).
  * O(2): rotaciones relativas conmutan (SO(2)); para β > β_BKT ≈ 1.12, fase sin gap
          (Fröhlich–Spencer): correlaciones de ley de potencia.

Observable de la recursión de escala:  ξ_2nd(L)/L  (longitud de correlación de segundo momento
en caja L).  Bajo L → 2L:
   → 0          : el flujo termina en el punto fijo trivial (toda diferencia cierra a radio finito) ⇒ gap
   → constante  : referencia autosimilar (línea de puntos fijos) ⇒ sin gap
"""
import sys, json, time, math
import numpy as np
import numba as nb


@nb.njit(cache=False)
def nbr_table(L):
    V = L * L
    nb_ = np.empty((V, 4), np.int64)
    for y in range(L):
        for x in range(L):
            i = y * L + x
            nb_[i, 0] = y * L + (x + 1) % L
            nb_[i, 1] = y * L + (x - 1) % L
            nb_[i, 2] = ((y + 1) % L) * L + x
            nb_[i, 3] = ((y - 1) % L) * L + x
    return nb_


@nb.njit(cache=False)
def wolff(sp, nb_, beta, stack, inC):
    V, n = sp.shape
    r = np.empty(n)
    nr = 0.0
    for a in range(n):
        r[a] = np.random.normal()
        nr += r[a] * r[a]
    nr = math.sqrt(nr)
    for a in range(n):
        r[a] /= nr
    seed = np.random.randint(V)
    p = 0.0
    for a in range(n):
        p += sp[seed, a] * r[a]
    for a in range(n):
        sp[seed, a] -= 2.0 * p * r[a]
    inC[seed] = True
    stack[0] = seed
    top = 1
    size = 0
    while top > 0:
        top -= 1
        i = stack[top]
        size += 1
        pi = 0.0
        for a in range(n):
            pi += sp[i, a] * r[a]
        pold = -pi  # proyección antes del volteo
        for k in range(4):
            j = nb_[i, k]
            if inC[j]:
                continue
            pj = 0.0
            for a in range(n):
                pj += sp[j, a] * r[a]
            x = 2.0 * beta * pold * pj
            if x > 0.0 and np.random.random() < 1.0 - math.exp(-x):
                inC[j] = True
                for a in range(n):
                    sp[j, a] -= 2.0 * pj * r[a]
                stack[top] = j
                top += 1
    # limpiar marcas
    for t in range(V):
        inC[t] = False
    return size


@nb.njit(cache=False)
def measure(sp, L, cx, sx, cy, sy):
    V, n = sp.shape
    M2 = 0.0
    F = 0.0
    for a in range(n):
        m = 0.0; rx = 0.0; ix = 0.0; ry = 0.0; iy = 0.0
        for y in range(L):
            for x in range(L):
                v = sp[y * L + x, a]
                m += v
                rx += v * cx[x]; ix += v * sx[x]
                ry += v * cy[y]; iy += v * sy[y]
        M2 += m * m
        F += 0.5 * (rx * rx + ix * ix + ry * ry + iy * iy)
    return M2 / V, F / V


@nb.njit(cache=False)
def run(L, n, beta, ntherm, nmeas, seed):
    np.random.seed(seed)
    V = L * L
    nb_ = nbr_table(L)
    sp = np.zeros((V, n))
    sp[:, 0] = 1.0
    stack = np.empty(V, np.int64)
    inC = np.zeros(V, np.bool_)
    k = 2 * math.pi / L
    cx = np.empty(L); sx = np.empty(L)
    for x in range(L):
        cx[x] = math.cos(k * x); sx[x] = math.sin(k * x)
    cy = cx.copy(); sy = sx.copy()
    # termalización: ntherm "barridos" (sitios volteados ≥ V)
    for _ in range(ntherm):
        flipped = 0
        while flipped < V:
            flipped += wolff(sp, nb_, beta, stack, inC)
    chis = np.empty(nmeas); Fs = np.empty(nmeas)
    for t in range(nmeas):
        flipped = 0
        while flipped < V:
            flipped += wolff(sp, nb_, beta, stack, inC)
        chis[t], Fs[t] = measure(sp, L, cx, sx, cy, sy)
    return chis, Fs


def xi2nd(chi, F, L):
    return math.sqrt(max(chi / F - 1.0, 0.0)) / (2 * math.sin(math.pi / L))


if __name__ == "__main__":
    out = sys.argv[1]
    t0 = time.time()
    res = []
    jobs = [(3, 1.5), (3, 1.7), (2, 1.3), (2, 0.9)]
    for n, beta in jobs:
        for L in [8, 16, 32, 64, 128]:
            nmeas = 4000
            chis, Fs = run(L, n, beta, 300, nmeas, 1234 + L)
            xi = xi2nd(chis.mean(), Fs.mean(), L)
            # jackknife
            nbk = 20
            blk = np.array_split(np.arange(nmeas), nbk)
            jk = []
            for b in blk:
                keep = np.setdiff1d(np.arange(nmeas), b)
                jk.append(xi2nd(chis[keep].mean(), Fs[keep].mean(), L))
            jk = np.array(jk)
            err = math.sqrt((nbk - 1) / nbk * np.sum((jk - jk.mean()) ** 2))
            rec = dict(n=n, beta=beta, L=L, chi=float(chis.mean()), xi=xi, xi_err=err, xi_over_L=xi / L, xi_over_L_err=err / L)
            res.append(rec)
            print(rec, round(time.time() - t0), "s", flush=True)
    with open(out, "w") as fh:
        json.dump(res, fh, indent=1)
    print("saved", out)
