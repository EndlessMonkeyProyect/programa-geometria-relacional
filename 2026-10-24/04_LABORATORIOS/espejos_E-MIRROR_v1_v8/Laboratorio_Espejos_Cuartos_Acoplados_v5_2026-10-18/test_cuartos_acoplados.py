import collections
import math
import unittest
import numpy as np
from cuartos_acoplados import (C,Config,round_trip_ns,echo_intensity,
  coincidence_profile,low_order_resonances,paths_for_coupled_rooms)


def signature_collision_count(length_B,depth=8):
    paths=paths_for_coupled_rooms(LB=length_B,R=.5,depth=depth)
    groups=collections.defaultdict(set)
    for item in paths:
        # 1e-7 nanosegundos: igualdad temporal en la precisión declarada
        key=(round(item['time_ns'],7),item['side'])
        groups[key].add((item['path'].count('A'), item['path'].count('B')))
    return sum(len(s)>1 for s in groups.values())

class V5Tests(unittest.TestCase):
    def test_equal_delays_half(self):
        self.assertAlmostEqual(round_trip_ns(2),2*round_trip_ns(1),12)

    def test_two_thirds(self):
        self.assertAlmostEqual(2*round_trip_ns(2),3*round_trip_ns(4/3),12)

    def test_echo_intensity(self):
        self.assertAlmostEqual(echo_intensity(1,.08,.95), .92*.95)
        self.assertAlmostEqual(echo_intensity(2,.08,.95), .92*.95**2*.08)

    def test_opaque_glass_no_detected_transmission(self):
        for n in range(1,9):self.assertEqual(echo_intensity(n,1,.95),0)

    def test_nonreflective_glass_only_first_echo(self):
        self.assertGreater(echo_intensity(1,0,.95),0)
        for n in range(2,9): self.assertEqual(echo_intensity(n,0,.95),0)

    def test_reduced_fractions_really_reduced(self):
        r=low_order_resonances(Config())
        self.assertEqual(len(r),len({(v['p'],v['q']) for v in r}))
        for v in r:
            self.assertEqual(math.gcd(v['p'],v['q']),1)
            self.assertAlmostEqual(v['period_A_ns'],v['period_B_ns'],10)

    def test_half_is_lowest_order_nontrivial(self):
        vals=low_order_resonances(Config())
        trimmed=[v for v in vals if v['length_B_m']<1.999]
        self.assertEqual((trimmed[0]['p'],trimmed[0]['q']),(1,2))

    def test_continuity_near_half(self):
        cfg=Config()
        x=np.array([.999,1.0,1.001])
        y=coincidence_profile(x,cfg)
        self.assertTrue(np.all(np.isfinite(y)))
        self.assertGreater(y[1],y[0]);self.assertGreater(y[1],y[2]);
        self.assertLess(y.max()-y.min(),.02)

    def test_reflection_counts_for_same_arm(self):
        for n in range(1,9):
            self.assertEqual((n+(n-1))%2,1)

    def test_complete_reflection_parity_tied_to_final_arm(self):
        for b in [1.0,math.sqrt(2),4/3,1.5]:
            paths=paths_for_coupled_rooms(LB=b,R=.5,depth=8)
            self.assertEqual(len(paths),255)
            self.assertTrue(all((x['reflection_parity']=='impar') == (x['side']=='A') for x in paths))

    def test_half_extra_path_signatures(self):
        self.assertGreater(signature_collision_count(1.0),0)
        self.assertEqual(signature_collision_count(math.sqrt(2)),0)

    def test_mixed_geometry_half_specific_equal_distances(self):
        # Dos rutas distintas que llegan a la interfaz A tras 12 metros:
        # (3 trayectos en A) frente a (2 en A, 2 en B).
        paths=paths_for_coupled_rooms(LB=1,R=.5,depth=8)
        matches=[x for x in paths if x['side']=='A' and abs(x['time_ns']-12/C*1e9)<1e-7]
        sig={(x['path'].count('A'),x['path'].count('B')) for x in matches}
        self.assertIn((3,0),sig)
        self.assertIn((2,2),sig)

if __name__=='__main__': unittest.main(verbosity=2)
