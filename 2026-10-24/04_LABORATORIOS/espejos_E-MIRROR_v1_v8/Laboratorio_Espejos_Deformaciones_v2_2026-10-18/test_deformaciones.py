#!/usr/bin/env python3
"""Pruebas independientes de controles de la continuación 2."""
import math
import unittest
import numpy as np
from laboratorio_deformaciones import (
 I, P, RX, RY, tilted_z, reflection, rotation_order, dihedral_orbit,
 loop_deviation, observability, opacity_observability,
 curved_profile_results, focus_axis_intercepts, parabola_profile, sphere_profile)

class TestLaboratorioDeformaciones(unittest.TestCase):
    def test_reflection_involution(self):
        for d in [0,0.5,1,5,15,40]:
            R=tilted_z(d)
            np.testing.assert_allclose(R@R,I,atol=1e-14)
    def test_reflection_parity(self):
        for d in [0,1,5,13.5]:
            self.assertAlmostEqual(np.linalg.det(tilted_z(d)),-1,places=12)
    def test_finite_orders(self):
        self.assertEqual([rotation_order(d) for d in [0.,.5,1.,2.,5.]],[2,360,180,45,36])
    def test_orbit_counts(self):
        self.assertEqual([dihedral_orbit(d)['posiciones_genericas_distintas'] for d in [0.,.5,1.,2.,5.]],[8,1440,720,180,144])
    def test_loop_four_reflections(self):
        for d in [1,2,5,15]:
            self.assertAlmostEqual(loop_deviation(d)['angulo_lazo_cuatro_reflexiones_grados'],4*d,places=6)
    def test_closing_cycle_at_zero_tilt(self):
        self.assertAlmostEqual(loop_deviation(0)['distancia_entre_fuente_e_imagen_tras_lazo_m'],0,places=12)
    def test_source_invariance_under_calibrated_inverse(self):
        for d in [0,1,5,15]:
            self.assertLess(loop_deviation(d)['error_al_invertir_reflejo_calibrado_m'],1e-12)
    def test_observability_zero_angle_rank_two(self):
        self.assertEqual(observability(0)['rango'],2)
    def test_observability_tilt_rank_three(self):
        for d in [.1,1,5,15,45]:
            self.assertEqual(observability(d)['rango'],3)
    def test_condition_cosecant(self):
        for d in [1,2,5,15,45]:
            self.assertAlmostEqual(observability(d)['condicion_2'],1/math.sin(math.radians(d)),places=10)
    def test_noise_depth_exact(self):
        for d in [1,5,15]:
            self.assertAlmostEqual(observability(d)['error_profundidad_z_m'],-.01/math.sin(math.radians(2*d)),places=10)
    def test_zero_opacity_destroys_depth(self):
        self.assertEqual(opacity_observability(5,0)['rango'],2)
        self.assertEqual(opacity_observability(5,.05)['rango'],3)
    def test_opacity_amplifies_noise(self):
        strong=abs(opacity_observability(5,1)['error_z_m'])
        weak=abs(opacity_observability(5,.2)['error_z_m'])
        self.assertAlmostEqual(weak/strong,5.,places=10)
    def test_parabolic_focus_exact(self):
        dat=focus_axis_intercepts(lambda x:parabola_profile(x,1.,0.,.6))
        self.assertLess(dat['max_desviacion_del_foco_nominal_m'],1e-12)
    def test_curve_perturbation_defocuses(self):
        curves=curved_profile_results()
        a=[x['desviacion_estandar_de_intersecciones_m'] for x in curves[:5]]
        self.assertTrue(all(x<y for x,y in zip(a,a[1:])))
    def test_spherical_aberration(self):
        dat=focus_axis_intercepts(lambda x:sphere_profile(x,1.))
        self.assertGreater(dat['desviacion_estandar_de_intersecciones_m'],0.01)

if __name__=='__main__':
    unittest.main(verbosity=2)
