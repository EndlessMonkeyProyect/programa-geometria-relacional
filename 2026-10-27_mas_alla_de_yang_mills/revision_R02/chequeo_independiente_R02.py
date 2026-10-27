"""Chequeo independiente (escrito desde cero) de las afirmaciones centrales de R-02.
No importa ni ejecuta código del repositorio.
"""
import numpy as np

rng = np.random.default_rng(7)
I = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
S = (sx, sy, sz)


def su2(q):
    q = np.asarray(q, float)
    q = q / np.linalg.norm(q)
    return q[0] * I + 1j * (q[1] * sx + q[2] * sy + q[3] * sz)


def rnd():
    return su2(rng.standard_normal(4))


def ht(M):
    return np.trace(M).real / 2


def nu(U, V):
    return 1 - ht(U @ V @ U.conj().T @ V.conj().T)


def firma(U, V):
    return np.array([ht(U), ht(V), ht(U @ V)])


def vec(U):  # parte vectorial del cuaternión: U = x I + i a·σ
    return np.array([np.trace(U @ s).imag / 2 for s in S])


err = {"nu_formula": 0.0, "D_cruz": 0.0, "region": 0.0, "T3_reciproca": 0.0, "T1": 0.0}
N = 5000
for _ in range(N):
    U, V = rnd(), rnd()
    x, y, z = firma(U, V)
    D = 1 - x * x - y * y - z * z + 2 * x * y * z
    err["nu_formula"] = max(err["nu_formula"], abs(nu(U, V) - 2 * D))
    a, b = vec(U), vec(V)
    err["D_cruz"] = max(err["D_cruz"], abs(D - np.dot(np.cross(a, b), np.cross(a, b))))
    lhs = abs(z - x * y) - np.sqrt(max((1 - x * x) * (1 - y * y), 0))
    err["region"] = max(err["region"], max(lhs, 0))

    # T3, dirección difícil: construir un segundo par con la MISMA firma
    # pero por camino independiente, y reconstruir la conjugación que los une.
    # Par 2: elegir a' en eje z, b' en plano xz con la misma Gram.
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    ab = np.dot(a, b)
    a2 = np.array([0, 0, na])
    cos = ab / (na * nb)
    b2 = nb * np.array([np.sqrt(max(1 - cos * cos, 0)), 0, cos])
    sgn = rng.choice([-1, 1])  # orientación arbitraria del segundo par
    b2 = b2 * np.array([sgn, 1, 1])
    U2 = x * I + 1j * (a2[0] * sx + a2[1] * sy + a2[2] * sz)
    V2 = y * I + 1j * (b2[0] * sx + b2[1] * sy + b2[2] * sz)
    assert np.allclose(firma(U2, V2), (x, y, z), atol=1e-12)
    # Rotación R con R a = a2, R b = b2, R ∈ SO(3) (completar con el producto vectorial)
    A = np.column_stack([a, b, np.cross(a, b)])
    B = np.column_stack([a2, b2, np.cross(a2, b2)])
    R = B @ np.linalg.inv(A)
    assert abs(np.linalg.det(R) - 1) < 1e-8
    # Levantar R a g ∈ SU(2) (fórmula de Rodrigues inversa vía cuaternión)
    w = np.sqrt(max(1 + np.trace(R), 1e-30)) / 2
    qv = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (4 * w)
    g = su2([w, -qv[0], -qv[1], -qv[2]])
    e = max(np.linalg.norm(g @ U @ g.conj().T - U2), np.linalg.norm(g @ V @ g.conj().T - V2))
    if e > 1e-6:  # convención de signo opuesta del levantamiento
        g = su2([w, qv[0], qv[1], qv[2]])
        e = max(np.linalg.norm(g @ U @ g.conj().T - U2), np.linalg.norm(g @ V @ g.conj().T - V2))
    err["T3_reciproca"] = max(err["T3_reciproca"], e)

    # T1: covariancia de un camino de tres aristas
    g0, g1, g2, g3 = (rnd() for _ in range(4))
    T01, T12, T23 = (rnd() for _ in range(3))
    P = T23 @ T12 @ T01
    Pp = (g3 @ T23 @ g2.conj().T) @ (g2 @ T12 @ g1.conj().T) @ (g1 @ T01 @ g0.conj().T)
    err["T1"] = max(err["T1"], np.linalg.norm(Pp - g3 @ P @ g0.conj().T))

# T4: testigo de bloqueo
U1, V1, U2, V2 = 1j * sx, 1j * sy, I, -1j * sz
t4 = (np.allclose(U1 @ V1, U2 @ V2), nu(U1, V1), nu(U2, V2))

print("ensayos:", N)
for k, v in err.items():
    print(f"  error máx {k:13s}: {v:.2e}")
print("T4  mismo UV:", t4[0], "| nu1 =", round(t4[1], 12), "| nu2 =", round(t4[2], 12))

# Aserciones: el chequeo falla si alguna afirmación de R-02 no se cumple
assert err["nu_formula"] < 1e-10 and err["D_cruz"] < 1e-10 and err["region"] < 1e-12
assert err["T3_reciproca"] < 1e-8 and err["T1"] < 1e-10
assert t4[0] and abs(t4[1] - 2) < 1e-12 and abs(t4[2]) < 1e-12
print("OK: todas las afirmaciones de R-02 comprobadas.")
