"""
MF-96 / Rama P vs NP — experimento E-PNP.

Misma familia de instancias, dos lenguajes de cierre (de identidades):

  L_cláusula : eliminación de Davis–Putnam (∃x por resolución) con subsunción.
               La interfaz de cada paso es un conjunto de cláusulas.
  L_lineal   : eliminación gaussiana sobre F2 (∃x por pivoteo).
               La interfaz de cada paso es un sistema afín (≤ #variables ecuaciones).

Familias:
  * Tseitin en grafos 3-regulares aleatorios (carga total impar ⇒ UNSAT).
    Relaciones afines (polimorfismo minoría): económicas en L_lineal, no en L_cláusula.
  * 2-SAT aleatorio (polimorfismo mayoría): económico en L_cláusula.
  * 3-SAT aleatorio en el umbral (sin polimorfismos no triviales): ningún
    lenguaje algebraico disponible; sólo L_cláusula.

Medida: tamaño máximo de interfaz durante la eliminación
  (cláusulas / literales en L_cláusula; ecuaciones / peso en L_lineal).
"""
import sys, json, random, time
from collections import defaultdict
import networkx as nx

CAP = 400_000  # tope de cláusulas: si se supera, se registra 'explota'


# ---------------------------------------------------------------- generadores
def tseitin(n, seed):
    rng = random.Random(seed)
    G = nx.random_regular_graph(3, n, seed=seed)
    edges = list(G.edges())
    eid = {frozenset(e): i + 1 for i, e in enumerate(edges)}
    charge = {v: rng.randint(0, 1) for v in G.nodes()}
    if sum(charge.values()) % 2 == 0:  # forzar carga total impar ⇒ insatisfacible
        v0 = next(iter(G.nodes()))
        charge[v0] ^= 1
    eqs, clauses = [], []
    for v in G.nodes():
        vs = [eid[frozenset((v, u))] for u in G.neighbors(v)]
        mask = 0
        for x in vs:
            mask |= 1 << x
        eqs.append((mask, charge[v]))
        # CNF de x1⊕x2⊕x3 = c : prohibir cada asignación con paridad ≠ c
        for a in range(8):
            bits = [(a >> i) & 1 for i in range(3)]
            if sum(bits) % 2 != charge[v]:
                clauses.append(frozenset(-x if b else x for x, b in zip(vs, bits)))
    return len(edges), clauses, eqs


def random_ksat(n, m, k, seed):
    rng = random.Random(seed)
    cls = set()
    while len(cls) < m:
        vs = rng.sample(range(1, n + 1), k)
        cls.add(frozenset(v if rng.random() < 0.5 else -v for v in vs))
    return n, list(cls)


# ------------------------------------------------------ L_cláusula: Davis–Putnam
def dp_eliminate(nvars, clauses, cap=CAP):
    cls = set()
    occ = defaultdict(set)

    def subsumed(c):
        lmin = min(c, key=lambda l: len(occ[l]))
        for d in occ[lmin]:
            if d <= c:
                return True
        return False

    def add(c):
        if c in cls or subsumed(c):
            return
        # subsunción hacia atrás: borrar cláusulas que c subsume
        lmin = min(c, key=lambda l: len(occ[l]))
        for d in list(occ[lmin]):
            if c <= d:
                remove(d)
        cls.add(c)
        for l in c:
            occ[l].add(c)

    def remove(c):
        cls.discard(c)
        for l in c:
            occ[l].discard(c)

    for c in sorted(clauses, key=len):
        add(c)
    alive = set(range(1, nvars + 1))
    max_cls, max_lits = len(cls), sum(len(c) for c in cls)
    trace = []
    while alive:
        v = min(alive, key=lambda x: len(occ[x]) * len(occ[-x]) - len(occ[x]) - len(occ[-x]))
        P, Nn = list(occ[v]), list(occ[-v])
        for c in P + Nn:
            remove(c)
        new = []
        for p in P:
            for q in Nn:
                r = (p - {v}) | (q - {-v})
                if any(-l in r for l in r):
                    continue
                new.append(frozenset(r))
        alive.discard(v)
        if frozenset() in new:
            trace.append(len(cls))
            return dict(status="UNSAT", max_clauses=max_cls, max_literals=max_lits, trace=trace)
        for r in sorted(set(new), key=len):
            add(r)
            if len(cls) > cap:
                return dict(status="EXPLOTA", max_clauses=len(cls), max_literals=None, trace=trace)
        max_cls = max(max_cls, len(cls))
        max_lits = max(max_lits, sum(len(c) for c in cls))
        trace.append(len(cls))
    return dict(status="SAT", max_clauses=max_cls, max_literals=max_lits, trace=trace)


# --------------------------------------------------- L_lineal: eliminación sobre F2
def gauss_eliminate(nvars, eqs):
    eqs = [list(e) for e in eqs]
    alive = set(range(1, nvars + 1))
    max_eq = len(eqs)
    max_w = sum(bin(m).count("1") for m, _ in eqs)
    while alive:
        def deg(x):
            return sum(1 for m, _ in eqs if (m >> x) & 1)
        v = min(alive, key=deg)
        rows = [i for i, (m, _) in enumerate(eqs) if (m >> v) & 1]
        alive.discard(v)
        if rows:
            piv = min(rows, key=lambda i: bin(eqs[i][0]).count("1"))
            pm, pr = eqs[piv]
            for i in rows:
                if i != piv:
                    eqs[i][0] ^= pm
                    eqs[i][1] ^= pr
            eqs.pop(piv)
        # ecuaciones triviales 0=0 se descartan; 0=1 es la contradicción (UNSAT)
        if any(m == 0 and r == 1 for m, r in eqs):
            return dict(status="UNSAT", max_equations=max_eq, max_weight=max_w)
        eqs = [e for e in eqs if e[0] != 0]
        max_eq = max(max_eq, len(eqs))
        max_w = max(max_w, sum(bin(m).count("1") for m, _ in eqs))
    return dict(status="SAT", max_equations=max_eq, max_weight=max_w)


if __name__ == "__main__":
    fam = sys.argv[1]
    out = sys.argv[2]
    seeds = range(5)
    res = []
    t0 = time.time()
    def save():
        with open(out, "w") as fh:
            json.dump(dict(family=fam, cap=CAP, seeds=list(seeds), rows=res,
                           wallclock_s=time.time() - t0,
                           order="min-resolvents (DP) / min-degree (F2)", subsumption="forward+backward"), fh, indent=1)
    if fam == "tseitin":
        for n in [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]:
            for s in seeds:
                nv, cls, eqs = tseitin(n, 1000 * n + s)
                a = dp_eliminate(nv, cls)
                b = gauss_eliminate(nv, eqs)
                res.append(dict(n_vertices=n, n_vars=nv, n_clauses=len(cls), seed=s,
                                clause=dict(status=a["status"], max_clauses=a["max_clauses"], max_literals=a["max_literals"]),
                                linear=b))
            save()
            print("tseitin n", n, round(time.time() - t0, 1), "s",
                  [r["clause"]["max_clauses"] for r in res if r["n_vertices"] == n],
                  [r["linear"]["max_equations"] for r in res if r["n_vertices"] == n], flush=True)
    elif fam == "sat2":
        for n in [20, 40, 80, 160, 320, 640]:
            for s in seeds:
                nv, cls = random_ksat(n, n, 2, 7000 * n + s)
                a = dp_eliminate(nv, cls)
                res.append(dict(n=n, m=len(cls), seed=s, clause=dict(status=a["status"], max_clauses=a["max_clauses"])))
            save()
            print("2sat n", n, round(time.time() - t0, 1), "s", [r["clause"]["max_clauses"] for r in res if r["n"] == n], flush=True)
    elif fam == "sat3":
        CAP = 30_000
        for n in [10, 15, 20, 25, 30, 35, 40]:
            for s in seeds:
                nv, cls = random_ksat(n, int(round(4.26 * n)), 3, 9000 * n + s)
                a = dp_eliminate(nv, cls, cap=CAP)
                res.append(dict(n=n, m=len(cls), seed=s, clause=dict(status=a["status"], max_clauses=a["max_clauses"])))
            save()
            print("3sat n", n, round(time.time() - t0, 1), "s", [r["clause"]["max_clauses"] for r in res if r["n"] == n],
                  [r["clause"]["status"] for r in res if r["n"] == n], flush=True)
            if all(r["clause"]["status"] == "EXPLOTA" for r in res if r["n"] == n):
                break
    save()
    print("saved", out)
