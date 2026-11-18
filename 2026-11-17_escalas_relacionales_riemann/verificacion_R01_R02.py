"""
Verificación de la Formalización R–01 / R–02
Las escalas relacionales de la criba · Versión 1.0
Le Matt Ansatz Di Ego
Endless Monkey Project
Relational Geometry Program

Requiere: numpy, mpmath (matplotlib es opcional: si está, guarda figura_ritmos.png).
Uso: python verificacion_R01_R02.py
Cada bloque corresponde a una sección del documento. Corre en menos de un minuto.
"""
from fractions import Fraction as F
import math
import random
import time

import numpy as np
from mpmath import mp, li, ei, riemannr, zeta, zetazero, mpf, mpc

mp.dps = 25
EULER_GAMMA = 0.5772156649015329
PI_CONOCIDO = {10**7: 664_579, 10**9: 50_847_534}


def primes_mask(n):
    s = np.ones(n + 1, bool)
    s[:2] = False
    for i in range(2, math.isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = False
    return s


P = [int(p) for p in np.nonzero(primes_mask(10**5))[0]]


def M_of(S):
    m = 1
    for p in S:
        m *= p
    return m


def delta_of(S):
    d = F(1)
    for p in S:
        d *= F(p - 1, p)
    return d


def A_of(S, x):
    """Enteros 1 <= n <= x coprimos con los primos de S (x real >= 0). Conteo directo, O(x).
    Para x grande conviene la forma cerrada con mobius_sq_free (Corolario 1)."""
    n = math.floor(x)
    M = M_of(S)
    return sum(1 for m in range(1, n + 1) if math.gcd(m, M) == 1)


def E_of(S, x):
    return A_of(S, x) - x * delta_of(S)


def mobius_sq_free(divs):
    """Divisores de M_S con su μ, a partir de la lista de primos."""
    out = [(1, 1)]
    for p in divs:
        out += [(d * p, -m) for d, m in out]
    return out


# ---------------------------------------------------------------- §2
print("§2  Herencia")
random.seed(1)
ok = True
for _ in range(400):
    S = random.sample(P[:7], random.randint(0, 4))
    p = random.choice([q for q in P[:9] if q not in S])
    x = F(random.randint(0, 4000), random.randint(1, 9))
    ok &= A_of(S + [p], x) == A_of(S, x) - A_of(S, x / p)
    ok &= E_of(S + [p], x) == E_of(S, x) - E_of(S, x / p)
print("    Teorema 1, 400 casos exactos con conjuntos arbitrarios:", "correcto" if ok else "FALLA")
assert ok

ok = True
for k in range(0, 6):
    for _ in range(40):
        x = F(random.randint(0, 3000), random.randint(1, 7))
        closed = sum(m * (math.floor(x / d) - x / d) for d, m in mobius_sq_free(P[:k]))
        ok &= closed == E_of(P[:k], x)
        if k >= 1:
            ok &= abs(E_of(P[:k], x)) < 2 ** (k - 1)
print("    Corolario 1 (forma cerrada) y cota |E_k| < 2^(k-1), k <= 5:", "correcto" if ok else "FALLA")
assert ok

ok = True
for _ in range(60):
    k = random.randint(0, 2)
    k2 = random.randint(k + 1, 6)
    x = F(random.randint(0, 3000), random.randint(1, 5))
    rhs = A_of(P[:k], x) - sum(A_of(P[:j - 1], x / P[j - 1]) for j in range(k + 1, k2 + 1))
    ok &= A_of(P[:k2], x) == rhs
print("    Corolario 2 (herencia acumulada, Buchstab), 60 casos:", "correcto" if ok else "FALLA")
assert ok

# ---------------------------------------------------------------- §3
print("\n§3  Forma de Mellin: ∫ E_k(x) x^(-s-1) dx = (ζ(s)/s) ∏ (1 - p_j^(-s))")
# Truncamiento: E_k tiene media cero sobre cada período M_k, así que su primitiva es acotada
# y la cola ∫_N^∞ E_k(x) x^(-s-1) dx es O(N^(-Re s - 1)). Con N = 4·10^5 el error queda < 1e-9.


def mellin_Ek(k, s, N=400_000):
    M = M_of(P[:k])
    d = float(delta_of(P[:k]))
    n = np.arange(1, N, dtype=np.float64)
    mask = np.array([math.gcd(int(m), M) == 1 for m in range(1, N)])
    A = np.cumsum(mask)
    s = complex(s)
    head = -d / (1 - s)  # [0,1): E_k = -x δ_k
    body = A * (n ** (-s) - (n + 1) ** (-s)) / s - d * ((n + 1) ** (1 - s) - n ** (1 - s)) / (1 - s)
    return head + body.sum()


worst = 0.0
for k in (1, 2):
    for s in (mpf("0.7"), mpc("0.6", "4")):
        num = mellin_Ek(k, s)
        prod = mpf(1)
        for p in P[:k]:
            prod *= 1 - mpf(p) ** (-s)
        ref = complex(zeta(s) / s * prod)
        rel = abs(num - ref) / abs(ref)
        worst = max(worst, rel)
        print(f"    k={k}  s={complex(s)}:  integral={num:.8f}  fórmula={ref:.8f}  error rel={rel:.1e}")
assert worst < 1e-9

# ---------------------------------------------------------------- §4
print("\n§4  Criterio puntual y ejemplo")
e3, e3p, e4 = E_of(P[:3], F(10)), E_of(P[:3], F(10, 7)), E_of(P[:4], F(10))
print(f"    E3(10)={e3}  E3(10/7)={e3p}  E4(10)={e4}  β(β-2α)={e3p * (e3p - 2 * e3)}")

x = 10**6
s = np.ones(x + 1, bool)
s[0] = False
d, prev, grew = 1.0, 0.0, 0
a = sum(1 for p in P if p * p <= x)
Ek = {}
for k in range(1, a + 1):
    p = P[k - 1]
    s[p::p] = False
    d *= 1 - 1 / p
    e = int(s.sum()) - x * d
    Ek[k] = e
    grew += abs(e) > prev
    prev = abs(e)
print(f"    x=10^6: |E_k| crece en {grew} de {a} pasos;  E_100 = {Ek[100]:.1f}")

# ---------------------------------------------------------------- §5
print("\n§5  Ley de energía por período (promedio continuo, fracciones exactas)")


def integ(a0, b0, a1, b1, n):
    """∫_n^{n+1} (a0 - b0 x)(a1 - b1 x) dx"""
    def prim(t):
        return a0 * a1 * t - (a0 * b1 + a1 * b0) * t**2 / 2 + b0 * b1 * t**3 / 3
    return prim(F(n + 1)) - prim(F(n))


for k in range(1, 5):
    S = P[:k]
    M, dk, p = M_of(S), delta_of(S), P[k]
    L = M * p
    A = [0] * (L + 1)
    c = 0
    for n in range(1, L + 1):
        c += math.gcd(n, M) == 1
        A[n] = c
    e2 = sum(integ(A[n], dk, A[n], dk, n) for n in range(L)) / L
    cr = sum(integ(A[n], dk, A[n // p], dk / p, n) for n in range(L)) / L
    assert e2 == F(2**k) * dk / 12 and cr / e2 == F(1, p)
    print(f"    k={k}: <E²>={e2}  2^k δ_k/12={F(2**k) * dk / 12}  "
          f"<E(x)E(x/p)>/<E²>={cr / e2}  1/p={F(1, p)}")

# ---------------------------------------------------------------- §6
print("\n§6  Cierre: referencia independiente, corregida y fluctuación")
h = 1e-4
us = np.arange(1, 12 + h / 2, h)
w = np.zeros_like(us)
cum = np.zeros_like(us)
n1 = int(round(1 / h))
for i in range(len(us)):
    if us[i] <= 2 + 1e-12:          # ω(u) = 1/u en [1, 2]
        w[i] = 1 / us[i]
    else:                            # u ω(u) = 1 + ∫_1^{u-1} ω
        w[i] = (1 + cum[i - n1]) / us[i]
    if i:
        cum[i] = cum[i - 1] + h * 0.5 * (w[i] + w[i - 1])
eg = math.exp(EULER_GAMMA)
print(f"    ω(2)={np.interp(2, us, w):.6f}  ω(3)={np.interp(3, us, w):.10f} "
      f"[(1+ln2)/3={(1 + math.log(2)) / 3:.10f}]  ω(10)={np.interp(10, us, w):.10f}  e^-γ={1 / eg:.10f}")

x = 10**8
s = np.ones(x + 1, bool)
s[0] = False
d = 1.0
print("    x=10^8:   k     p_k     u    A_k/(xδ_k)   e^γ ω(u)")
for k in range(1, 1230):
    p = P[k - 1]
    s[p::p] = False
    d *= 1 - 1 / p
    if k in (10, 50, 100, 200, 446, 1229):
        u = math.log(x) / math.log(p)
        print(f"           {k:5d} {p:7d} {u:5.2f}   {int(s[1:].sum()) / (x * d):.4f}     {eg * np.interp(u, us, w):.4f}")
del s

print("    Proposición 3:  x     x·δ_a      E_a(x)   estructural   π(x)−li(x)   estr./(x/log x)   √x·log x")
mask7 = primes_mask(10**7)
cum7 = np.cumsum(mask7)
P7 = np.nonzero(mask7)[0]
for e in (5, 6, 7):
    x = 10**e
    a = int(np.searchsorted(P7, math.isqrt(x), side="right"))
    pix = int(cum7[x])
    d = 1.0
    for p in P7[:a]:
        d *= 1 - 1 / p
    Ea = pix - (a - 1) - x * d
    lix = float(li(x))
    estr = lix - x * d - a + 1
    assert abs(Ea - (estr + (pix - lix))) < 1e-6   # Proposición 3
    print(f"                  10^{e}  {x * d:10.0f}  {Ea:9.0f}  {estr:11.1f}  {pix - lix:10.1f}"
          f"      {estr / (x / math.log(x)):8.4f}      {math.sqrt(x) * math.log(x):9.0f}")
print(f"    li(10^7) = {float(li(10**7)):.1f}   2e^-γ = {2 / eg:.4f}   1 - 2e^-γ = {1 - 2 / eg:.4f}   e^γ/2 = {eg / 2:.4f}")

# ---------------------------------------------------------------- §7
print("\n§7  Ritmos: la fluctuación como suma sobre los ceros de ζ")
rho1 = zetazero(1)
xx, pp = mpf(1234.5), 7
lhs = xx**rho1 - (xx / pp) ** rho1
rhs = (1 - mpf(pp) ** (-rho1)) * xx**rho1
print(f"    T_p x^ρ = (1 - p^-ρ) x^ρ  (ρ = primer cero, p = 7, x = 1234,5):  diferencia = {float(abs(lhs - rhs)):.1e}")

K = 200
t0 = time.time()
rho = [zetazero(n) for n in range(1, K + 1)]
print(f"    {K} ceros calculados en {time.time() - t0:.0f} s;  τ1, τ2, τ3 = "
      + ", ".join(f"{float(r.imag):.4f}" for r in rho[:3]))
print("    amplitudes 2/|ρ| de los tres primeros: " + ", ".join(f"{2 / float(abs(r)):.4f}" for r in rho[:3]))

ts = np.linspace(math.log(100), math.log(10**7), 400)
rows = []
for t in ts:
    x = math.exp(t)
    norm = t / math.sqrt(x)
    pix = int(cum7[int(x)])
    L = float(li(x))
    base = float(riemannr(x)) - L                      # R(x) - li(x)
    z = np.cumsum([2 * float(ei(r * t).real) for r in rho])   # li(x^ρ) + li(x^ρ̄) = 2 Re Ei(ρ log x)
    z2 = sum(-float(ei(r * t / 2).real) for r in rho)           # término n = 2 de cada R(x^ρ): −Re li(x^{ρ/2}) por par
    triv = -1 / t + math.atan(math.pi / t) / math.pi              # los dos últimos términos de la fórmula
    rows.append([(pix - L) * norm, base * norm] + [(base - z[k - 1]) * norm for k in (10, 50, 200)]
                + [(base - z[-1] - z2 + triv) * norm])
R = np.array(rows)
print("    Reconstrucción π(x) ≈ R(x) − Σ_{k≤K} 2 Re li(x^ρ_k), 400 puntos entre x = 10² y 10⁷ (unidades √x/log x):")
for j, k in ((1, 0), (2, 10), (3, 50), (4, 200)):
    rms = math.sqrt(np.mean((R[:, j] - R[:, 0]) ** 2))
    cor = np.corrcoef(R[:, j], R[:, 0])[0, 1]
    print(f"        K = {k:3d}:  correlación {cor:.3f}   diferencia cuadrática media {rms:.3f}")
cor5 = np.corrcoef(R[:, 5], R[:, 0])[0, 1]
print(f"    con 200 ceros + término n = 2 + dos últimos términos:  correlación {cor5:.3f}   diferencia cuadrática media {math.sqrt(np.mean((R[:, 5] - R[:, 0]) ** 2)):.3f}")
print(f"    fluctuación normalizada en [10², 10⁷]: mínimo {R[:, 0].min():.2f}, máximo {R[:, 0].max():.2f}")
print(f"    un cero con β = 0,6 crecería x^0,1 respecto de la línea: en x = 10⁷, factor {1e7 ** 0.1:.2f}")

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
    S1, S2, S3 = "#2a78d6", "#eb6834", "#1baf7a"
    plt.rcParams.update({"font.size": 9, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                         "xtick.color": MUTED, "ytick.color": MUTED})
    fig, axes = plt.subplots(2, 1, figsize=(6.2, 4.6), sharex=True, sharey=True)
    for ax, j, k, col in ((axes[0], 2, 10, S2), (axes[1], 4, 200, S3)):
        ax.plot(ts, R[:, 0], color=S1, lw=1.3, label="primos reales")
        ax.plot(ts, R[:, j], color=col, lw=1.3, label=f"suma de {k} ritmos")
        ax.grid(True, color=GRID, lw=0.6)
        ax.set_axisbelow(True)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        ax.legend(loc="lower right", frameon=False, fontsize=8, ncol=2)
        cor = np.corrcoef(R[:, j], R[:, 0])[0, 1]
        ax.set_title(f"{k} ceros  ·  correlación {cor:.2f}".replace(".", ","), loc="left",
                     fontsize=9, color=INK)
    axes[1].set_xlabel("log x   (x de 10² a 10⁷)")
    fig.supylabel("(π(x) − li(x)) · log x / √x", fontsize=9, color=INK)
    fig.tight_layout()
    fig.savefig("figura_ritmos.png", dpi=220)
    plt.close(fig)
    print("    figura guardada: figura_ritmos.png")
except ImportError:
    print("    (matplotlib no está instalado: se omite la figura)")

# ---------------------------------------------------------------- §8
print("\n§8  Firma de escala cerrada (Proposición 4): conteo exacto de π(x) sobre D(x)")


def pi_via_D(x):
    r = math.isqrt(x)
    D = [x // i for i in range(1, r + 1)]
    D += list(range(D[-1] - 1, 0, -1))
    S = {v: v - 1 for v in D}  # S(v) = #{2 <= n <= v : n primo o sin factores <= p}
    for p in range(2, r + 1):
        if S[p] > S[p - 1]:  # p es primo
            sp, p2 = S[p - 1], p * p
            for v in D:      # solo las entradas v >= p²
                if v < p2:
                    break
                S[v] -= S[v // p] - sp
    return S[x], len(D)


def check_lema(x):
    """Lema de §8: compara la tabla S_k con su invariante en cada etapa, para todo v en D(x)."""
    r = math.isqrt(x)
    D = sorted({x // i for i in range(1, x + 1)})
    S = {v: v - 1 for v in D}
    alive = np.ones(x + 1, bool)          # coprimos con M_k
    alive[0] = False
    pi_cum = np.cumsum(primes_mask(x))
    k, checks = 0, 0
    for p in range(2, r + 1):
        if S[p] > S[p - 1]:
            sp, p2 = S[p - 1], p * p
            for v in sorted(D, reverse=True):
                if v < p2:
                    break
                S[v] -= S[v // p] - sp
            k += 1
            alive[p::p] = False
            A = np.cumsum(alive)
            for v in D:
                esperado = int(pi_cum[v]) if v < p else int(A[v]) + k - 1
                assert S[v] == esperado, (p, v, S[v], esperado)
                checks += 1
    return k, checks


k_l, n_l = check_lema(10**4)
print(f"    Lema (tabla S_k): invariante correcto en {k_l} etapas y {n_l} comprobaciones, x = 10^4")

for x in (10**7, 10**9):
    t = time.time()
    v, nd = pi_via_D(x)
    assert v == PI_CONOCIDO[x]
    print(f"    π({x}) = {v} (coincide con el valor conocido)   |D(x)| = {nd}   2√x = {2 * math.isqrt(x)}   {time.time() - t:.2f} s")
