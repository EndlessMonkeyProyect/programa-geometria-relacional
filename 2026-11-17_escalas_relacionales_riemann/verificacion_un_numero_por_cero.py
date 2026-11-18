"""
Verificación de «Un número por cero»
Reflexión sobre la Formalización R–01 / R–02 · Versión 1.0
Le Matt Ansatz Di Ego
Endless Monkey Project
Relational Geometry Program

Requiere: numpy, mpmath, sympy (matplotlib es opcional: si está, guarda figura_pivote.png).
Uso: python verificacion_un_numero_por_cero.py
Cada bloque corresponde a una sección del documento. Los bloques con assert detienen la
ejecución si algo falla; los demás miden y reportan.
"""
import itertools
import math
import random

import numpy as np
from mpmath import mp, mpf, mpc, zeta, gamma, pi, siegelz, siegeltheta, zetazero
from sympy import factorint, n_order

mp.dps = 20
random.seed(7)


def xi(s):
    """ξ(s) = ½ s(s−1) π^(−s/2) Γ(s/2) ζ(s): la ζ completada."""
    return mpf(1) / 2 * s * (s - 1) * pi ** (-s / 2) * gamma(s / 2) * zeta(s)


# ---------------------------------------------------------------- §3 pivote
print("§3  El pivote: ξ(½ + z) = ξ(½ − z)")
worst = 0
for _ in range(6):
    z = mpc(random.uniform(-0.4, 0.4), random.uniform(-40, 40))
    a, b = xi(mpf(1) / 2 + z), xi(mpf(1) / 2 - z)
    rel = float(abs(a - b) / abs(a))
    worst = max(worst, rel)
print(f"    6 valores de z al azar: diferencia relativa máxima {worst:.1e}")
assert worst < 1e-15
im = max(float(abs(xi(mpc(0.5, t)).imag / xi(mpc(0.5, t)).real)) for t in (3, 17.5, 33, 61.2))
print(f"    sobre la línea ½, ξ es real: |Im ξ / Re ξ| máximo {im:.1e} en cuatro alturas")
assert im < 1e-15

# ---------------------------------------------------------------- §4 un número por cero
print("\n§4  Un número por cero: ceros en la franja contra ceros sobre la línea, hasta T")
T = mpf(1000)

# (a) N(T), ceros en la franja 0 < Re s < 1, 0 < Im s <= T, por el principio del argumento:
#     N(T) = θ(T)/π + 1 + S(T), con S(T) = arg ζ(½ + iT)/π por variación continua 2 → 2+iT → ½+iT.
#     Sobre Re s = 2, |ζ(s) − 1| <= ζ(2) − 1 < 1, así que ahí el argumento principal es continuo.
args = []
for sig in np.linspace(2.0, 0.5, 3001):
    v = zeta(mpc(sig, T))
    args.append(math.atan2(float(v.imag), float(v.real)))
arg_total = np.unwrap(np.array(args))[-1]
N_franja = float(siegeltheta(T)) / math.pi + 1 + arg_total / math.pi
print(f"    N({int(T)}) por el principio del argumento = {N_franja:.6f}")
N_franja_int = round(N_franja)
assert abs(N_franja - N_franja_int) < 1e-3

# (b) cambios de signo de Z(t) = e^{iθ(t)} ζ(½ + it), real: cada uno es un cero sobre la línea.
#     Una rejilla rápida con la fórmula de Riemann–Siegel ubica los cruces; después se evalúa Z con
#     mpmath.siegelz en los puntos medios entre cruces consecutivos (lejos de los ceros) y se cuentan
#     los cambios de signo de esa sucesión: cada uno garantiza al menos un cero sobre la línea.
def theta_rs(t):
    return t / 2 * np.log(t / (2 * np.pi)) - t / 2 - np.pi / 8 + 1 / (48 * t) + 7 / (5760 * t**3)


def Z_rs(t):
    a = np.sqrt(t / (2 * np.pi))
    Nn = np.floor(a).astype(int)
    th = theta_rs(t)
    total = np.zeros_like(t)
    for n in range(1, Nn.max() + 1):
        m = Nn >= n
        total[m] += np.cos(th[m] - t[m] * np.log(n)) / np.sqrt(n)
    p = a - Nn
    c0 = np.cos(2 * np.pi * (p * p - p - 1 / 16)) / np.cos(2 * np.pi * p)
    return 2 * total + (-1.0) ** (Nn - 1) * a ** (-0.5) * c0


tt = np.arange(10.0, float(T), 0.002)
zz = Z_rs(tt)
cand = np.nonzero(np.sign(zz[:-1]) != np.sign(zz[1:]))[0]
cruces = (tt[cand] + tt[cand + 1]) / 2
puntos = [10.0] + list((cruces[:-1] + cruces[1:]) / 2) + [float(T)]
signos = [1 if siegelz(t) > 0 else -1 for t in puntos]
confirmados = sum(1 for a, b in zip(signos[:-1], signos[1:]) if a != b)
print(f"    cambios de signo de Z(t) en (0, {int(T)}], confirmados con mpmath: {confirmados}")
assert confirmados == N_franja_int
print(f"    ceros en la franja = ceros sobre la línea = {N_franja_int}: los {N_franja_int} ceros hasta altura "
      f"{int(T)} tienen β = ½ y cada uno queda fijado por un solo número τ")
print("    primeros τ: " + ", ".join(f"{float(zetazero(k).imag):.6f}" for k in range(1, 6)))

# ---------------------------------------------------------------- §5 radio frente a la pared
print("\n§5  Radio de cada ritmo frente a la pared p: |p^(−ρ)| = p^(−β)")
rho = [zetazero(k) for k in range(1, 4)]
for p in (2, 3, 5, 7):
    radios = [float(abs(mpf(p) ** (-r))) for r in rho]
    fact = [float(abs(1 - mpf(p) ** (-r))) for r in rho]
    print(f"    p = {p}:  |p^-ρ| = " + ", ".join(f"{v:.6f}" for v in radios)
          + f"   (1/√p = {1 / math.sqrt(p):.6f});   |1 − p^-ρ| = " + ", ".join(f"{v:.4f}" for v in fact))
    assert all(abs(v - 1 / math.sqrt(p)) < 1e-12 for v in radios)

# ---------------------------------------------------------------- §6 frecuencias perpendiculares
print("\n§6  Frecuencias sin relación racional pequeña (ilustración de LI)")
taus = np.array([float(zetazero(k).imag) for k in range(1, 5)])
best = (math.inf, None)
R = range(-10, 11)
for coef in itertools.product(R, repeat=4):
    if not any(coef):
        continue
    v = abs(np.dot(coef, taus))
    if v < best[0]:
        best = (v, coef)
print(f"    τ1..τ4 con coeficientes enteros |a| <= 10: mínimo |Σ a·τ| = {best[0]:.4f}  con a = {best[1]}")

# ---------------------------------------------------------------- §7 octavas de Mersenne
print("\n§7  Octavas de Mersenne: M_n = 2^n − 1")
M = lambda n: 2**n - 1
Q = lambda k: 2**k + 1
assert all(M(2 * k) == M(k) * Q(k) and math.gcd(M(k), Q(k)) == 1 for k in range(1, 65))
print("    M_2k = M_k · (2^k + 1), con factores coprimos, k = 1..64: correcto")
assert all(M(k * n) % M(k) == 0 for k in range(1, 61) for n in range(1, 121 // k + 1))
print("    herencia: M_k divide a M_nk para todo k·n <= 120: correcto")

primos_vistos = set()
sin_novedad = []
for n in range(2, 65):
    f = factorint(M(n))
    nuevos = [q for q in f if q not in primos_vistos]
    primitivos = [q for q in f if n_order(2, q) == n]
    assert set(nuevos) == set(primitivos)          # lo nuevo es exactamente lo de período n
    if not nuevos:
        sin_novedad.append((n, f))
    primos_vistos |= set(f)
print(f"    niveles n = 2..64 sin primo nuevo: {[n for n, _ in sin_novedad]}  "
      f"(M_6 = 63 = {' · '.join(f'{q}^{e}' if e > 1 else str(q) for q, e in sin_novedad[0][1].items())})")
assert [n for n, _ in sin_novedad] == [6]
print("    en todos los demás niveles el primo nuevo tiene período exactamente n (orden de 2 = n)")

fermat = [Q(2**j) for j in range(7)]
assert all(math.gcd(a, b) == 1 for a, b in itertools.combinations(fermat, 2))
print("    números de Fermat F_0..F_6 coprimos dos a dos: correcto;  F_5 = "
      + " · ".join(str(q) for q in factorint(fermat[5])))
ok_rep, ok_new = True, True
for k in range(2, 65):
    impares = [r for r in range(3, k + 1, 2) if k % r == 0]
    if impares:
        r = impares[0]
        ok_rep &= Q(k) % Q(k // r) == 0              # 2^(k/r) + 1 divide a 2^k + 1
    else:                                            # k potencia de 2
        ok_new &= all(math.gcd(Q(k), Q(m)) == 1 for m in range(1, k))
assert ok_rep and ok_new
print("    2^k + 1 repite material de un nivel anterior si k tiene factor impar; si k es potencia de 2 "
      "es coprimo con todos los anteriores (k <= 64): correcto")

# ---------------------------------------------------------------- figura
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
    S1, S2 = "#2a78d6", "#eb6834"
    ts = np.linspace(0.5, 50, 1500)
    zs = np.array([float(siegelz(t)) for t in ts])
    ceros = [float(zetazero(k).imag) for k in range(1, 11)]
    ceros = [c for c in ceros if c <= 50]
    plt.rcParams.update({"font.size": 9, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                         "xtick.color": MUTED, "ytick.color": MUTED})
    fig, ax = plt.subplots(figsize=(6.2, 2.8))
    ax.axhline(0, color=MUTED, lw=0.8)
    ax.plot(ts, zs, color=S1, lw=1.4, label="Z(t) sobre la línea ½")
    ax.plot(ceros, [0] * len(ceros), "o", ms=7, color=S2, mec="white", mew=1.5, label="ceros: un número τ cada uno")
    for k, c in enumerate(ceros[:3], 1):
        ax.annotate(f"τ{k} = {c:.2f}".replace(".", ","), (c, 0), xytext=(c, (-2.5, -3.4, -2.5)[k - 1]),
                    ha="center", fontsize=8, color=INK)
    ax.grid(True, color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.set_xlabel("t  (altura sobre la línea ½)")
    ax.set_ylabel("Z(t)")
    ax.set_ylim(-4.3, 3.6)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), frameon=False, fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig("figura_pivote.png", dpi=220)
    plt.close(fig)
    print("\n    figura guardada: figura_pivote.png")
except ImportError:
    print("\n    (matplotlib no está instalado: se omite la figura)")
