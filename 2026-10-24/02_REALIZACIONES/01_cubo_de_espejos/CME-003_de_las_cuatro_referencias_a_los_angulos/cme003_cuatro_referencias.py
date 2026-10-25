"""CME-003 — De las cuatro referencias a los ángulos.

Parte de las cuatro referencias de T8 (dos distinciones, cuatro estados) y de sus
tres comparaciones de paridad. No introduce ningún ángulo: los ángulos salen de
intercambiar referencias y de cambiar el signo de una comparación (el bit).

Comprueba, con aritmética exacta (enteros y fracciones):
  1. En las coordenadas de las tres comparaciones, las cuatro referencias son los
     vértices de un tetraedro regular, y los ejes de las comparaciones son los
     ejes de las aristas opuestas, perpendiculares entre sí.
  2. Intercambiar dos referencias es una reflexión. Dos intercambios disjuntos
     tienen orden 2 (ángulo π/2); dos que comparten una referencia, orden 3 (π/3).
     Los seis intercambios generan 24 orientaciones: el recinto (2, 3, 3).
  3. Las paredes de cada una de las 24 cámaras tienen órdenes (3, 3, 2):
     no hay que elegir generadores; da igual dónde se ubique el foco.
  4. Cambiar el signo de una comparación (el bit) lleva el tetraedro al
     complementario; juntos son los 8 vértices del cubo (O19). Con el bit, el
     producto de dos espejos puede tener orden 4 (π/4), y el grupo llega a 48:
     el recinto (2, 3, 4).
  5. Con 2 referencias solo hay un espejo (la mitad). Con 8 referencias el
     producto de dos intercambios sigue teniendo solo orden 2 o 3. El 5 no aparece.

Los órdenes que fijan ángulos son siempre los del producto de dos espejos. Los
elementos compuestos pueden tener otros: entre las 24 hay giros de orden 4, y
entre las 48, elementos de orden 6. El programa los cuenta por separado.
  6. Si una de las cuatro referencias fuera distinguible, solo se podrían
     intercambiar las otras tres: 6 orientaciones, y los tres espejos comparten
     la recta de la referencia fija. El recinto queda plano, el del triángulo:
     sus normales abarcan dos direcciones, no tres. Que no se pueda decir cuál
     es «la una» es lo que da las tres direcciones independientes.
  7. Reflejar en una cara no intercambia referencias: crea una nueva, fuera
     del tetraedro, a 5/3 del radio (O20). Es la reflexión que abre (CME-001).

Escribe cme003_resultados.json y falla si algo no se cumple.
"""
import itertools, json, math
from fractions import Fraction as Fr
from pathlib import Path


def estados(n):
    return list(itertools.product((0, 1), repeat=n))


def comparaciones(n):
    # subconjuntos no vacíos de las n distinciones: las 2^n - 1 paridades
    return [A for r in range(1, n + 1) for A in itertools.combinations(range(n), r)]


def vertice(s, comps):
    return tuple((-1) ** sum(s[i] for i in A) for A in comps)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def reflexion(normal):
    # R = I - 2 n n^T / (n^T n), exacta
    d = len(normal)
    nn = dot(normal, normal)
    return tuple(tuple(Fr(int(i == j)) - Fr(2 * normal[i] * normal[j], nn) for j in range(d)) for i in range(d))


def mul(A, B):
    d = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(d)) for j in range(d)) for i in range(d))


def ident(d):
    return tuple(tuple(Fr(int(i == j)) for j in range(d)) for i in range(d))


def orden(M, tope=60):
    d = len(M)
    P = M
    for k in range(1, tope + 1):
        if P == ident(d):
            return k
        P = mul(P, M)
    return None


def generar(gens):
    d = len(gens[0])
    vistos = {ident(d)}
    frontera = [ident(d)]
    while frontera:
        nueva = []
        for g in frontera:
            for s in gens:
                h = mul(g, s)
                if h not in vistos:
                    vistos.add(h)
                    nueva.append(h)
        frontera = nueva
    return vistos


def aplicar(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(v)))


def angulo_pi(n1, n2):
    """Ángulo agudo entre los planos de normales n1 y n2, como fracción de π."""
    c = abs(dot(n1, n2)) / math.sqrt(dot(n1, n1) * dot(n2, n2))
    return round(math.acos(min(1.0, c)) / math.pi, 12)


res = {}

# 1. Cuatro referencias, tres comparaciones
n = 2
S = estados(n)
C = comparaciones(n)
V = {s: vertice(s, C) for s in S}
dist2 = {(s, t): dot(tuple(a - b for a, b in zip(V[s], V[t])), tuple(a - b for a, b in zip(V[s], V[t])))
         for s, t in itertools.combinations(S, 2)}
assert len(set(dist2.values())) == 1, "las cuatro referencias no son equidistantes"
assert all(sum(V[s][k] for s in S) == 0 for k in range(len(C)))
separan = {(s, t): sum(1 for k in range(len(C)) if V[s][k] != V[t][k]) for s, t in itertools.combinations(S, 2)}
assert set(separan.values()) == {2}
# ejes de aristas opuestas = ejes de las comparaciones
ejes = []
for (s, t) in itertools.combinations(S, 2):
    u, w = [x for x in S if x not in (s, t)]
    m1 = tuple(Fr(a + b, 2) for a, b in zip(V[s], V[t]))
    m2 = tuple(Fr(a + b, 2) for a, b in zip(V[u], V[w]))
    eje = tuple(a - b for a, b in zip(m1, m2))
    if eje not in ejes and tuple(-x for x in eje) not in ejes:
        ejes.append(eje)
assert len(ejes) == 3
assert all(dot(a, b) == 0 for a, b in itertools.combinations(ejes, 2)), "los ejes no son perpendiculares"
assert all(sum(1 for x in e if x != 0) == 1 for e in ejes), "los ejes no son los de las comparaciones"
res["1_tetraedro"] = {
    "estados": len(S), "comparaciones": len(C),
    "vertices": {"".join(map(str, s)): V[s] for s in S},
    "distancia2_comun": list(dist2.values())[0],
    "comparaciones_que_separan_cada_par": 2,
    "ejes_de_aristas_opuestas_son_las_comparaciones_y_perpendiculares": True,
}

# 2. Intercambios como reflexiones
inter = {}
for s, t in itertools.combinations(S, 2):
    nrm = tuple(a - b for a, b in zip(V[s], V[t]))
    R = reflexion(nrm)
    # es exactamente el intercambio: lleva s a t, t a s y deja quietas las otras
    for x in S:
        y = t if x == s else s if x == t else x
        assert aplicar(R, V[x]) == V[y], "el intercambio no es esta reflexión"
    inter[(s, t)] = (R, nrm)
pares = []
for (p, q) in itertools.combinations(inter, 2):
    comparten = len(set(p) & set(q)) == 1
    o = orden(mul(inter[p][0], inter[q][0]))
    a = angulo_pi(inter[p][1], inter[q][1])
    pares.append({"comparten_referencia": comparten, "orden": o, "angulo_en_pi": a})
    if comparten:
        assert o == 3 and abs(a - 1 / 3) < 1e-9
    else:
        assert o == 2 and abs(a - 1 / 2) < 1e-9
G24 = generar([inter[k][0] for k in inter])
assert len(G24) == 24
res["2_intercambios"] = {
    "intercambios": len(inter),
    "disjuntos": {"orden": 2, "angulo": "π/2", "casos": sum(1 for p in pares if not p["comparten_referencia"])},
    "comparten_una_referencia": {"orden": 3, "angulo": "π/3", "casos": sum(1 for p in pares if p["comparten_referencia"])},
    "orientaciones_generadas": len(G24),
    "recinto_CME002": "(2, 3, 3)",
}

# 3. Cámaras: no hay elección de generadores
camaras = []
for orden_vals in itertools.permutations(S):
    paredes = [tuple(sorted((orden_vals[i], orden_vals[i + 1]))) for i in range(3)]
    Rs = [inter[p][0] for p in paredes]
    o = (orden(mul(Rs[0], Rs[1])), orden(mul(Rs[1], Rs[2])), orden(mul(Rs[0], Rs[2])))
    camaras.append(o)
assert len(camaras) == 24 and set(camaras) == {(3, 3, 2)}
res["3_camaras"] = {"camaras": 24, "ordenes_entre_paredes": [3, 3, 2],
                     "lectura": "en las 24 cámaras las paredes forman el mismo recinto (2, 3, 3)"}

# 4. El bit: cambiar el signo de una comparación
flip = tuple(tuple(Fr(-1 if (i == j == 0) else int(i == j)) for j in range(3)) for i in range(3))
T = set(V.values())
Tf = {aplicar(flip, v) for v in T}
assert T.isdisjoint(Tf)
assert all(math.prod(v) == 1 for v in T) and all(math.prod(v) == -1 for v in Tf)
cubo = T | Tf
assert cubo == set(itertools.product((-1, 1), repeat=3)), "no son los 8 vértices del cubo"
G48 = generar([inter[k][0] for k in inter] + [flip])
assert len(G48) == 48
normal_flip = (1, 0, 0)
ords_flip = sorted({orden(mul(flip, inter[k][0])) for k in inter})
angs_flip = sorted({angulo_pi(normal_flip, inter[k][1]) for k in inter})
assert ords_flip == [2, 4] and angs_flip == [0.25, 0.5]
# generadores de la nota: r1 signo de x1, r2 intercambio x1<->x2, r3 intercambio x2<->x3
def perm_mat(p):
    return tuple(tuple(Fr(int(p[i] == j)) for j in range(3)) for i in range(3))
r1, r2, r3 = flip, perm_mat((1, 0, 2)), perm_mat((0, 2, 1))
nota = (orden(mul(r1, r2)), orden(mul(r2, r3)), orden(mul(r1, r3)), len(generar([r1, r2, r3])))
assert nota == (4, 3, 2, 48)
res["4_bit"] = {
    "tetraedro_y_complementario_son_el_cubo": True,
    "ordenes_bit_con_intercambio": ords_flip, "angulos_en_pi": angs_flip,
    "orientaciones_con_el_bit": len(G48), "recinto_CME002": "(2, 3, 4)",
    "generadores_de_la_nota_r1_r2_r3": {"ordenes": list(nota[:3]), "grupo": nota[3]},
}

# 5. Dos referencias y ocho referencias
S1 = estados(1); C1 = comparaciones(1)
V1 = {s: vertice(s, C1) for s in S1}
R1 = reflexion(tuple(a - b for a, b in zip(V1[S1[0]], V1[S1[1]])))
assert orden(R1) == 2 and len(generar([R1])) == 2
S3 = estados(3); C3 = comparaciones(3)
V3 = {s: vertice(s, C3) for s in S3}
inter8 = [reflexion(tuple(a - b for a, b in zip(V3[s], V3[t]))) for s, t in itertools.combinations(S3, 2)]
ords8 = sorted({orden(mul(a, b)) for a, b in itertools.combinations(inter8, 2)})
assert ords8 == [2, 3]
res["5_otras_escalas"] = {
    "dos_referencias": {"espejos": 1, "orientaciones": 2, "lectura": "solo la mitad"},
    "ocho_referencias": {"intercambios": len(inter8), "ordenes_entre_intercambios": ords8},
    "aparece_el_5": False,
}

# 6. Una referencia distinguible
fija = S[0]
otras = [x for x in S if x != fija]
inter3 = [inter[tuple(sorted(p))][0] for p in itertools.combinations(otras, 2)]
normales3 = [inter[tuple(sorted(p))][1] for p in itertools.combinations(otras, 2)]
G6 = generar(inter3)
assert len(G6) == 6
# los tres espejos contienen la recta de la referencia fija: su normal es perpendicular a ella
assert all(dot(nm, V[fija]) == 0 for nm in normales3)
def rango(vs):
    filas = [list(map(Fr, v)) for v in vs]
    r = 0
    ncol = len(filas[0])
    for c in range(ncol):
        piv = next((i for i in range(r, len(filas)) if filas[i][c] != 0), None)
        if piv is None:
            continue
        filas[r], filas[piv] = filas[piv], filas[r]
        for i in range(len(filas)):
            if i != r and filas[i][c] != 0:
                f = filas[i][c] / filas[r][c]
                filas[i] = [x - f * y for x, y in zip(filas[i], filas[r])]
        r += 1
    return r
rango3 = rango(normales3)
rango4 = rango([inter[k][1] for k in inter])
assert rango3 == 2 and rango4 == 3
res["6_una_distinguible"] = {
    "orientaciones": len(G6),
    "los_tres_espejos_contienen_la_recta_de_la_referencia_fija": True,
    "direcciones_de_las_normales": rango3,
    "direcciones_con_las_cuatro_indistinguibles": rango4,
}

# 7. Espejo de cara: crea una referencia nueva
def refl_afin(v, normal, c):
    # reflexión en el plano normal·x = c
    k = Fr(2 * (dot(normal, v) - c), dot(normal, normal))
    return tuple(Fr(a) - k * b for a, b in zip(v, normal))
radio2 = dot(V[S[0]], V[S[0]])
nuevas = []
for opuesto in S:
    cara = [x for x in S if x != opuesto]
    normal = V[opuesto]
    c = dot(normal, V[cara[0]])  # plano de la cara
    assert all(dot(normal, V[x]) == c for x in cara)
    w = refl_afin(V[opuesto], normal, c)
    assert w not in set(V.values())
    nuevas.append(w)
    assert Fr(dot(w, w), radio2) == Fr(25, 9), "la nueva referencia no está a 5/3 del radio"
res["7_espejo_de_cara"] = {
    "crea_referencia_nueva": True,
    "radio_de_la_nueva_sobre_el_radio": "5/3",
    "las_cuatro_nuevas_forman_tetraedro_invertido": sorted(map(lambda w: tuple(str(x) for x in w), nuevas)) ==
        sorted(tuple(str(Fr(-5, 3) * x) for x in v) for v in V.values()),
}
assert res["7_espejo_de_cara"]["las_cuatro_nuevas_forman_tetraedro_invertido"]

# Órdenes de elementos compuestos, que no son ángulos
ord24 = sorted({orden(g) for g in G24})
ord48 = sorted({orden(g) for g in G48})
assert ord24 == [1, 2, 3, 4] and ord48 == [1, 2, 3, 4, 6]
res["8_ordenes_de_elementos_compuestos"] = {
    "en_las_24": ord24, "en_las_48": ord48,
    "lectura": "los ángulos los fija el orden del producto de dos espejos, no el orden de cualquier elemento",
}

out = Path(__file__).with_name("cme003_resultados.json")
out.write_text(json.dumps(res, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
print("CME-003: todo se cumple")
print(" 4 referencias -> tetraedro regular; ejes de las 3 comparaciones perpendiculares")
print(" intercambios disjuntos: orden 2 (π/2); con una referencia común: orden 3 (π/3); grupo 24 = (2,3,3)")
print(" 24 cámaras, todas con paredes de órdenes (3,3,2)")
print(" el bit (signo de una comparación): tetraedro -> complementario, cubo; producto de dos espejos de orden 2 o 4; grupo 48 = (2,3,4)")
print(" 2 referencias: un espejo; 8 referencias: solo órdenes", ords8, "; el 5 no aparece")
print(" una referencia distinguible: 6 orientaciones, espejos alrededor de una recta: 2 direcciones, no 3")
print(" espejo de cara: crea una referencia nueva a 5/3 del radio; las cuatro, tetraedro invertido")
