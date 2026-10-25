import unittest
import numpy as np
from scipy.optimize import brentq
from onda_cavidades_v7 import (A,K0,XS,sheet_g,rt,determinant,eigen_roots,green_cross,green_interface,mode_shape)

class TestCavities(unittest.TestCase):
    def test_01_sheet_reflectivity_calibrated(self):
        for R in [0,.01,.25,.5,.9,.99]:
            with self.subTest(R=R):
                r,t=rt(K0,sheet_g(R))
                self.assertAlmostEqual(abs(r)**2,R,12)
                self.assertAlmostEqual(abs(r)**2+abs(t)**2,1,12)
    def test_02_zero_barrier(self):
        r,t=rt(K0,0)
        self.assertAlmostEqual(abs(r),0,14)
        self.assertAlmostEqual(t.real,1,14)
    def test_03_common_node_independent_of_divider(self):
        for R in [0,.1,.25,.5,.9,.99]:
            with self.subTest(R=R):
                self.assertLess(abs(determinant(K0,.5,sheet_g(R))),1e-12)
    def test_04_half_resonance_frequency_invariant(self):
        for R in [0,.25,.5,.9,.99]:
            roots=eigen_roots(.5,sheet_g(R),.85,1.22)
            self.assertLess(min(abs(q-1) for q in roots),1e-11)
    def test_05_not_all_rational_nodes_at_same_color(self):
        for b in [1/3,2/3,3/4,2/5]:
            with self.subTest(b=b):
                self.assertGreater(abs(np.sin(K0*b)),.1)
    def test_06_other_rational_mode_different_frequency(self):
        # At B/A=2/3, A supports n=3, B supports n=2 at q=3/2.
        self.assertLess(abs(determinant(1.5*K0,2/3,sheet_g(.5))),1e-12)
        self.assertGreater(abs(determinant(K0,2/3,sheet_g(.5))),1)
    def test_07_node_eigenfunction(self):
        x,e,ratio=mode_shape(1,.5,sheet_g(.5),n_pts=1501)
        self.assertAlmostEqual(ratio,1,11)
        self.assertLess(abs(e[np.argmin(abs(x-1))]),1e-11)
        self.assertAlmostEqual(np.trapezoid(e*e,x),1,10)
    def test_08_ratio_energy(self):
        x,e,_=mode_shape(1,.5,sheet_g(.5),n_pts=3001)
        a=np.trapezoid(e[x<=1]**2,x[x<=1]);b=np.trapezoid(e[x>=1]**2,x[x>=1])
        self.assertAlmostEqual(a/b,2,8)
    def test_09_sheet_continuity_and_jump_nodal(self):
        k=K0;g=sheet_g(.5);b=.5
        E_left=np.sin(k*1); E_right=np.sin(k*b)
        dL=k*np.cos(k*1);dR=-k*np.cos(k*b)
        self.assertAlmostEqual(E_left,E_right,12)
        self.assertAlmostEqual(dR-dL,g*E_left,12)
    def test_10_green_reciprocal_denom(self):
        k=K0*(1+.003j);b=.57;g=sheet_g(.5)
        D=determinant(k,b,g)
        hand=np.sin(k*XS)*np.sin(k*.5*b)/D
        self.assertAlmostEqual(abs(green_cross(k,b,g)-hand),0,12)
    def test_11_green_finite_with_loss(self):
        for b in [.25,.5,.7,.9]:
            self.assertTrue(np.isfinite(abs(green_cross(K0*(1+.003j),b,sheet_g(.5)))))
    def test_12_divider_amplitude_finite_loss(self):
        for b in [.25,.5,.9]:
            self.assertTrue(np.isfinite(abs(green_interface(K0*(1+.003j),b,sheet_g(.5)))))
    def test_13_modes_respect_char_eq(self):
        for b in [.31,.49,.5,.67,.91]:
            for q in eigen_roots(b,sheet_g(.5),q_lo=.1,q_hi=1.5):
                with self.subTest(b=b,q=q):
                    self.assertLess(abs(determinant(K0*q,b,sheet_g(.5))),1e-9)
    def test_14_finite_spectrum_positive(self):
        q=eigen_roots(.5,sheet_g(.5),q_lo=.1,q_hi=2.0)
        self.assertTrue(all(v>0 for v in q))
        self.assertTrue(all(q[i+1]>q[i] for i in range(len(q)-1)))
    def test_15_reflection_phase_unitary(self):
        r,t=rt(K0,sheet_g(.5))
        self.assertAlmostEqual((r*np.conj(t)).real,0,12)
    def test_16_fixed_frequency_resonance_local(self):
        k=K0*(1+.003j);g=sheet_g(.5)
        peak=abs(green_cross(k,.5,g))**2
        self.assertGreater(peak,abs(green_cross(k,.48,g))**2)
        self.assertGreater(peak,abs(green_cross(k,.52,g))**2)
    def test_17_frequency_dependence_sheet(self):
        g=sheet_g(.5)
        R_low=abs(rt(.6*K0,g)[0])**2
        R_high=abs(rt(1.4*K0,g)[0])**2
        self.assertGreater(R_low,R_high)
    def test_18_exact_geometric_phase(self):
        # E(x+lambda)=E(x) y E(x+lambda/2)=-E(x) solo para ondas viajeras.
        for x in [.12,.37,.89]:
            E=lambda z: np.exp(1j*K0*z)
            self.assertAlmostEqual(abs(E(x+1)-E(x)),0,12)
            self.assertAlmostEqual(abs(E(x+.5)+E(x)),0,12)
    def test_19_no_constant_rearrangement_claim(self):
        # b=1/2 crea modo protegido para k0, b=2/3 NO lo crea para k0
        g=sheet_g(.5)
        self.assertLess(abs(determinant(K0,.5,g)),1e-12)
        self.assertGreater(abs(determinant(K0,2/3,g)),1e-3)
    def test_20_ideal_sheet_no_internal_absorption(self):
        for q in [0.7,1,1.3]:
            for R in [.1,.8]:
                r,t=rt(K0*q,sheet_g(R))
                self.assertAlmostEqual(1-abs(r)**2-abs(t)**2,0,12)

if __name__=='__main__':unittest.main(verbosity=2)

class TestRelativeParity(unittest.TestCase):
    def test_21_opposite_sign_when_both_longitudinal_indices_odd(self):
        for b,p,expected in [(.5,2,1),(2/3,3,1),(.6,5,-1)]:
            with self.subTest(b=b,p=p):
                _,_,ratio=mode_shape(p/2,b,sheet_g(.5),n_pts=1001)
                self.assertAlmostEqual(ratio,expected,8)
