"""Pruebas independientes de reproducción: python -m unittest -v test_razones_cavidades_v8.py"""
import unittest
import numpy as np
from razones_cavidades_v8 import (
    K0, XS, A, ETA, g_from_R, sheet_rt, determinant,interface_matrix,
    ratio_residual,tangent_residual,sheet_state_at_node,green_b_from_a,green_a_from_a,find_modes,finite_difference_cross)

class TestRazones(unittest.TestCase):
    def test_R_endpoints_and_invalid(self):
        self.assertEqual(g_from_R(0),0)
        for R in (-.1,1,1.1):
            with self.assertRaises(ValueError):g_from_R(R)
    def test_sheet_conserves_energy(self):
        for R in (0,.1,.5,.9,.999):
            r,t=sheet_rt(K0,g_from_R(R))
            self.assertAlmostEqual(abs(r)**2+abs(t)**2,1,places=11)
            self.assertAlmostEqual(abs(r)**2,R,places=11)
    def test_determinant_equals_matrix_determinant(self):
        rng=np.random.default_rng(48)
        for _ in range(600):
            k=float(rng.uniform(.5,13));b=float(rng.uniform(.2,1.3));g=float(rng.uniform(0,40))
            self.assertAlmostEqual(np.linalg.det(interface_matrix(k,b,g)),determinant(k,b,g),places=9)
    def test_ratio_equivalent_away_from_nodes(self):
        rng=np.random.default_rng(341)
        for _ in range(300):
            k=float(rng.uniform(.6,14));b=float(rng.uniform(.25,1.5));g=float(rng.uniform(0,40))
            if abs(np.sin(k))>.08 and abs(np.sin(k*b))>.08:
                rr=ratio_residual(k,b,g)
                self.assertAlmostEqual(rr* k*np.sin(k)*np.sin(k*b),determinant(k,b,g),places=8)
    def test_tangent_covers_common_node(self):
        self.assertAlmostEqual(tangent_residual(K0,.5,g_from_R(.9)),0,places=12)
        with self.assertRaises(ZeroDivisionError):tangent_residual(K0*.75,.5,g_from_R(.9))
    def test_tangent_matches_determinant(self):
        rng=np.random.default_rng(89)
        for _ in range(300):
            k=float(rng.uniform(.7,13));b=float(rng.uniform(.3,1.2));g=float(rng.uniform(0,30))
            if abs(np.cos(k))>.08 and abs(np.cos(k*b))>.08:
                tr=tangent_residual(k,b,g)
                self.assertAlmostEqual(tr*k*np.cos(k)*np.cos(k*b),determinant(k,b,g),places=8)
    def test_ratio_loses_phase_sign(self):
        # cot(theta+pi)=cot(theta): same ratio but fields differ by a sign.
        phi=.713
        self.assertAlmostEqual(np.cos(phi)/np.sin(phi),np.cos(phi+np.pi)/np.sin(phi+np.pi))
        self.assertAlmostEqual(np.sin(phi),-np.sin(phi+np.pi))
        self.assertAlmostEqual(np.cos(phi),-np.cos(phi+np.pi))
    def test_ratio_forgets_amplitude(self):
        phi=.713
        for scale in (.1,2,9):
            self.assertAlmostEqual((scale*np.cos(phi))/(scale*np.sin(phi)),np.cos(phi)/np.sin(phi))
    def test_ratio_undefined_at_common_node(self):
        with self.assertRaises(ZeroDivisionError):ratio_residual(K0,.5,g_from_R(.5))
    def test_projective_retains_common_node(self):
        for R in (0,.5,.9,.99):
            M=interface_matrix(K0,.5,g_from_R(R))
            self.assertLess(np.linalg.norm(M@np.array([1.,1.])),1e-12)
            self.assertLess(abs(determinant(K0,.5,g_from_R(R))),1e-12)
            self.assertEqual(np.linalg.matrix_rank(M,tol=1e-10),1)
    def test_node_ratio(self):
        self.assertAlmostEqual(sheet_state_at_node(K0,.5),1)
        with self.assertRaises(ValueError): sheet_state_at_node(K0,.51)
    def test_other_node_ratios(self):
        for b,p,m in ((.5,2,1),(2/3,3,2),(.6,5,3)):
            k=np.pi*p
            ratio=sheet_state_at_node(k,b)
            self.assertAlmostEqual(ratio,-(-1)**(p-m),places=10)
    def test_single_node_not_eigenmode(self):
        self.assertGreater(abs(determinant(K0,.45,g_from_R(.5))),1)
    def test_modes_include_pinned_node(self):
        for R in (0,.5,.9):
            roots=find_modes(.5,g_from_R(R))
            self.assertTrue(any(abs(q-1)<1e-9 for q in roots))
    def test_transfer_independent_exactly_zero(self):
        # Independent numerical finite-difference solver with a disconnected boundary.
        k=K0*.92*(1+1j*ETA)
        separate=finite_difference_cross(k,.5,g_from_R(.5),independent=True)
        self.assertLess(abs(separate),1e-12)
    def test_finite_difference_agrees_with_green(self):
        # Cross-check with a genuinely different discretization of the PDE.
        k=K0*.92*(1+1j*ETA);gg=g_from_R(.5)
        discrete=finite_difference_cross(k,.5,gg,independent=False)
        exact=green_b_from_a(k,.5,gg)
        self.assertLess(abs(discrete-exact)/abs(exact),.02)
    def test_transfer_coupled_nonzero(self):
        for R in (0,.5,.9,.99):
            response=green_b_from_a(K0*(1+1j*ETA),.5,g_from_R(R))
            self.assertGreater(abs(response),0.3)
    def test_away_from_node_transmission_declines_with_g(self):
        k=K0*.97*(1+1j*ETA);b=.53
        s1=abs(green_b_from_a(k,b,g_from_R(.5)))
        s2=abs(green_b_from_a(k,b,g_from_R(.99999)))
        self.assertGreater(s1,s2*15)
    def test_measured_response_position(self):
        k=K0*.93*(1+1j*ETA)
        r=green_a_from_a(k,.5,g_from_R(.5))
        self.assertTrue(np.isfinite(r.real) and np.isfinite(r.imag))
    def test_green_function_symmetry(self):
        # Reciprocity of Green function for real g and symmetric boundary problem.
        k=K0*.91*(1+1j*ETA);g=g_from_R(.5);b=.54;xB=A+.5*b
        ab=green_b_from_a(k,b,g)
        # Source at B, observe A -> exchange coordinates in symmetric min/max Green.
        ba=np.sin(k*XS)*np.sin(k*(A+b-xB))/determinant(k,b,g)
        self.assertAlmostEqual(abs(ab-ba),0,places=12)
    def test_node_field_derivative_continuity(self):
        left=np.cos(K0*A)
        right=-sheet_state_at_node(K0,.5)*np.cos(K0*.5)
        self.assertAlmostEqual(left,right)
        self.assertNotEqual(left,0)
    def test_energy_fraction(self):
        x=np.linspace(0,1.5,3001)
        e=np.where(x<=1,np.sin(K0*x),np.sin(K0*(1.5-x)))
        a=np.trapezoid(e[x<=1]**2,x[x<=1]);b=np.trapezoid(e[x>=1]**2,x[x>=1])
        self.assertAlmostEqual(a/(a+b),2/3,places=10)
        self.assertAlmostEqual(b/(a+b),1/3,places=10)
    def test_at_reduced_source_node_response_can_vanish(self):
        # At q=3/4, xs=2/3 is a field node; for B=.5 no eigenvalue there.
        k=K0*.75
        self.assertLess(abs(green_b_from_a(k,.5,g_from_R(.5),xs=2/3)),1e-10)

if __name__=='__main__':unittest.main(verbosity=2)
