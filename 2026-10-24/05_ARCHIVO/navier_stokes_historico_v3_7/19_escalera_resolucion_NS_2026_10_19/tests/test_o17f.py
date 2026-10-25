"""Pruebas de O17-F (sin correr la DNS completa). Requieren numpy y scipy.

python -B -m unittest discover -s 19_escalera_resolucion_NS_2026_10_19/tests -v
"""
import json
import sys
import unittest
from pathlib import Path

import numpy as np

RAIZ = Path(__file__).absolute().parents[1]
sys.path.insert(0, str(RAIZ / "experiments"))

import analisis_o17f as A        # noqa: E402
import escalera_ns_o17f as E     # noqa: E402
import instantaneous_budget as IB  # noqa: E402
from dns_forced_isotropic import Spectral, initial_field, refine  # noqa: E402


def alto_sintetico(N, rng, n=20000, desplazamiento=0.0):
    flat = rng.choice(N ** 3, n, replace=False)
    q = rng.gamma(2.0, 1.0, n)
    d = {"q": q, "qrms": np.sqrt(np.mean(q ** 2)), "w": np.where(q > 2, 1.0, 50.0), "flat": flat,
         "a": rng.normal(0.5, 1.0, n), "rho": np.clip(rng.beta(2, 1, n) + desplazamiento, 0, 1),
         "Me": rng.random(n), "bn": rng.random(n) + 0.1}
    for k in ("Lam", "Dperp", "cosphi", "sP", "sV", "dlogb_dG"):
        d[k] = rng.normal(0, 1, n) + desplazamiento
    return d


class TestHerramientas(unittest.TestCase):
    def test_mediana_igual_a_la_del_autor(self):
        rng = np.random.default_rng(1)
        for _ in range(50):
            x, w = rng.normal(size=500), rng.random(500) + 0.01
            o = np.argsort(x)
            self.assertAlmostEqual(A.mediana_ponderada_ordenada(x[o], w[o]), float(IB.wquantile(x, w, [0.5])[0]), places=12)

    def test_replica_por_bloques(self):
        rng = np.random.default_rng(2)
        x, w = rng.normal(size=3000), rng.random(3000) + 0.01
        b = rng.integers(0, 512, 3000)
        med = A.Mediana(x, w, b)
        self.assertAlmostEqual(med.valor(np.ones(512)), med.valor(), places=12)
        c = np.zeros(512)
        c[:200] = 1.0
        sub = b < 200
        self.assertAlmostEqual(med.valor(c), float(IB.wquantile(x[sub], w[sub], [0.5])[0]), places=12)
        cond = (x > 0).astype(float)
        fr = A.Fraccion(cond, w, b)
        self.assertAlmostEqual(fr.valor(c), float(np.sum(w[sub] * cond[sub]) / np.sum(w[sub])), places=12)
        c2 = rng.multinomial(512, np.full(512, 1 / 512)).astype(float)
        rep = np.repeat(np.arange(3000), c2[b].astype(int))
        self.assertAlmostEqual(fr.valor(c2), float(np.sum(w[rep] * cond[rep]) / np.sum(w[rep])), places=12)

    def test_bloques_fisicos_comunes(self):
        for N in (64, 128, 192, 256):
            s = N // 64
            i = np.array([0, 7, 8, 63]) * s
            flat = np.ravel_multi_index((i, i, i), (N,) * 3)
            self.assertEqual(list(A.bloque_de(flat, N)), [0, 0, 73, 511])

    def test_puntos_comunes(self):
        for N in (64, 128, 192, 256):
            sel = E.puntos_comunes(N)
            self.assertEqual(sel[0].size, 64 ** 3)
            self.assertEqual(int(sel[0].max()), 63 * (N // 64))

    def test_criterio(self):
        self.assertTrue(A.acreditado(0.05, [-0.01, 0.1], 1.0, "mediana")[0])
        self.assertTrue(A.acreditado(0.015, [0.01, 0.02], 1.0, "mediana")[0])
        self.assertFalse(A.acreditado(0.05, [0.03, 0.07], 1.0, "mediana")[0])
        self.assertTrue(A.acreditado(0.008, [0.005, 0.011], 0.3, "fraccion")[0])

    def test_truncamiento_ida_y_vuelta(self):
        sp = Spectral(64)
        U = initial_field(sp)
        V = E.coarsen(refine(U, 64, 128), 128, 64)
        self.assertLess(np.abs(V - U * sp.mask).max(), 1e-12 * np.abs(U).max())


class TestAnalisisSintetico(unittest.TestCase):
    def test_niveles_identicos_son_contenido_del_plano(self):
        rng = np.random.default_rng(3)
        base = alto_sintetico(256, rng)
        datos = {}
        for N in A.NIVELES:
            alto = dict(base)
            alto["flat"] = np.ravel_multi_index(
                tuple((np.array(np.unravel_index(base["flat"], (256,) * 3)) * N) // 256), (N,) * 3)
            datos[N] = {"alto": alto}
        filas = A.estadistico(datos, B=60)
        for f in filas:
            for N in (64, 128, 192):
                self.assertAlmostEqual(f["niveles"][N]["delta"], 0.0, places=12)
                self.assertTrue(f["niveles"][N]["acreditado"])
            self.assertTrue(f["robusto"])

    def test_desplazamiento_grande_no_se_acredita(self):
        rng = np.random.default_rng(4)
        datos = {N: {"alto": alto_sintetico(N, np.random.default_rng(5), desplazamiento=(0.0 if N == 256 else 0.5))}
                 for N in A.NIVELES}
        filas = {f["estadistica"]: f for f in A.estadistico(datos, B=60)}
        self.assertFalse(filas["mediana Lam | q>3qrms"]["niveles"][192]["acreditado"])
        self.assertFalse(filas["mediana Lam | q>3qrms"]["contenido_del_plano"])


class TestResultadosGuardados(unittest.TestCase):
    """Coherencia interna de results/RESULTADOS_O17F.json con los criterios prerregistrados."""

    def setUp(self):
        self.r = json.loads((RAIZ / "results" / "RESULTADOS_O17F.json").read_text(encoding="utf-8"))

    def test_criterio_aplicado(self):
        for f in self.r["estadistico"]:
            for N in ("64", "128", "192"):
                n = f["niveles"][N]
                cero = n["ic95_delta"][0] <= 0 <= n["ic95_delta"][1]
                self.assertEqual(n["acreditado"], bool(cero or abs(n["delta"]) <= n["tolerancia"] + 1e-15), f["estadistica"])
            d = [abs(f["niveles"][N]["delta"]) for N in ("64", "128", "192")]
            self.assertEqual(f["convergente"], d[0] >= d[1] >= d[2])
            self.assertEqual(f["contenido_del_plano"], f["niveles"]["192"]["acreditado"] and f["convergente"])

    def test_puntual(self):
        for f in self.r["puntual"]:
            self.assertEqual(f["acreditado"], f["mediana"] <= A.TOL_PUNTUAL)
        b = {(f["N"], f["cantidad"]): f["mediana"] for f in self.r["puntual"]}
        for k in A.VECTORES:
            self.assertGreater(b[(64, k)], b[(192, k)])          # el error puntual baja al refinar

    def test_niveles_mismo_flujo(self):
        re = [self.r["diagnosticos"][str(N)]["Re_lambda"] for N in A.NIVELES]
        self.assertLess(max(re) - min(re), 0.2)
        k = [self.r["diagnosticos"][str(N)]["kmax_eta"] for N in A.NIVELES]
        self.assertEqual(k, sorted(k))


class TestPrerregistro(unittest.TestCase):
    def test_parametros_coinciden(self):
        p = json.loads((RAIZ / "PRERREGISTRO_O17F.json").read_text(encoding="utf-8"))
        self.assertEqual(p["escalera"]["niveles_N"], list(A.NIVELES))
        self.assertTrue(p["registrado_antes_de_correr"])
        self.assertEqual((E.NU, E.EPS_IN, E.KF, E.SEMILLA), (p["flujo"]["nu"], p["flujo"]["eps_in"], p["flujo"]["kf"], p["flujo"]["semilla"]))
        self.assertEqual(E.DT, 4e-3)
        self.assertEqual(A.B_REPLICAS, 400)
        self.assertEqual(A.BLOQUES_POR_LADO ** 3, 512)


if __name__ == "__main__":
    unittest.main()
