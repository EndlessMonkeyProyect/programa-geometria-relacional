"""Controles unitarios del laboratorio de referencias."""
import unittest
from fractions import Fraction
from itertools import product

from laboratorio_referencias import (
    classes_count,
    economy_break_even,
    entails_clause,
    factorizes,
    pair_xor,
    pairwise_squared_distances,
    run,
    signed_volume6,
    supplementary_bits,
    update_compatible,
    wall_signature,
)


class IntegracionDeReferencias(unittest.TestCase):
    def test_firma_espejos(self):
        self.assertEqual(wall_signature(Fraction(1, 4), 1), Fraction(1, 4))
        self.assertEqual(wall_signature(Fraction(9, 4), 1), Fraction(1, 4))
        self.assertEqual(wall_signature(Fraction(9, 4), 2), Fraction(7, 4))
        with self.assertRaises(ValueError):
            wall_signature(1, 0)

    def test_factorizacion_preservada(self):
        ok, witness = factorizes(range(12), lambda x: x % 3, lambda x: x % 3)
        self.assertTrue(ok)
        self.assertIsNone(witness)

    def test_factorizacion_reabierta(self):
        states = [Fraction(1, 4), Fraction(9, 4)]
        ok, witness = factorizes(states, lambda x: wall_signature(x, 1),
                                lambda x: wall_signature(x, 2))
        self.assertFalse(ok)
        self.assertEqual(witness, tuple(states))

    def test_suplemento_modular(self):
        b, k, counts = supplementary_bits(range(30), lambda x: x % 6,
                                           lambda x: x % 10)
        self.assertEqual((b, k), (3, 5))
        self.assertEqual(set(counts.values()), {5})

    def test_suplemento_sin_novedad(self):
        b, k, _ = supplementary_bits(range(30), lambda x: x % 6,
                                      lambda x: (x % 6) % 2)
        self.assertEqual((b, k), (0, 1))
        with self.assertRaises(ValueError):
            supplementary_bits([], lambda x: x, lambda x: x)

    def test_refinamiento_consultas(self):
        states = range(30)
        a = classes_count(states, (lambda x: x % 6,))
        b = classes_count(states, (lambda x: x % 6, lambda x: x % 10))
        self.assertEqual((a, b), (6, 30))

    def test_cota_residual_exhaustiva_tres_estados(self):
        """Comprueba suficiencia y necesidad por búsqueda para 216 casos."""
        X = tuple(range(3))
        for phi_values in product(range(2), repeat=3):
            for q_values in product(range(3), repeat=3):
                phi = lambda x: phi_values[x]
                q = lambda x: q_values[x]
                b, _, _ = supplementary_bits(X, phi, q)

                def possible(bits):
                    alphabet = tuple(range(2 ** bits))
                    for h_values in product(alphabet, repeat=3):
                        ok, _ = factorizes(X, lambda x: (phi(x), h_values[x]), q)
                        if ok:
                            return True
                    return False

                self.assertTrue(possible(b))
                if b > 0:
                    self.assertFalse(possible(b - 1))

    def test_actualizacion_compatible(self):
        yes, witness = update_compatible(range(4), lambda x: x % 2,
                                         lambda x: (x + 1) % 4)
        self.assertTrue(yes)
        self.assertIsNone(witness)

    def test_actualizacion_incompatible(self):
        no, witness = update_compatible(range(5), lambda x: x % 2,
                                        lambda x: (x + 1) % 5)
        self.assertFalse(no)
        x, y = witness
        self.assertEqual(x % 2, y % 2)
        self.assertNotEqual(((x + 1) % 5) % 2, ((y + 1) % 5) % 2)

    def test_relaciones_xor(self):
        patterns = {pair_xor(x) for x in product((0, 1), repeat=4)}
        self.assertEqual(len(patterns), 8)

    def test_tetraedro_orientado(self):
        a = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
        b = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, -1))
        self.assertEqual(pairwise_squared_distances(a), pairwise_squared_distances(b))
        self.assertEqual((signed_volume6(a), signed_volume6(b)), (1, -1))

    def test_herencia_y_novedad(self):
        self.assertTrue(entails_clause(((1,),), (1,), 2))
        self.assertFalse(entails_clause(((1,),), (2,), 2))
        self.assertTrue(entails_clause(((1,), (-1,)), (2,), 2))

    def test_umbral_economia(self):
        self.assertEqual(economy_break_even(120, 20, 6), 9)
        self.assertLess(120 + 9 * 6, 9 * 20)
        self.assertGreaterEqual(120 + 8 * 6, 8 * 20)
        with self.assertRaises(ValueError):
            economy_break_even(10, 6, 6)

    def test_corrida_conjunta(self):
        self.assertEqual(run()["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
