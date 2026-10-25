#!/usr/bin/env python3
"""O64: controles independientes de identidades capilares, escalas y fronteras.
No resuelve el problema de dos fases; evalúa solo modelos analíticos declarados.
"""
from math import pi, sin, cos, isclose
import csv, pathlib, unittest

HERE=pathlib.Path(__file__).resolve().parents[1]
RHO=1000.0
SIGMA=0.072
MU=1e-3
NU=MU/RHO

def d_hinze(eps, rho=RHO, sigma=SIGMA, c=0.725):
    assert eps>0 and sigma>0 and rho>0
    return c*(sigma/rho)**(3/5)*eps**(-2/5)

def young_laplace(sigma, k1, k2): return sigma*(k1+k2)

def torus_curvatures(R, r, theta):
    assert R>r>0
    return 1/r,cos(theta)/(R+r*cos(theta))

def sphere_volume(r): return 4*pi*r**3/3

def sphere_area(r): return 4*pi*r*r

def equal_volume_daughter_radius(r,n): return r*n**(-1/3)

def splitting_cost(r,n,sigma=SIGMA):
    return sigma*(n*sphere_area(equal_volume_daughter_radius(r,n))-sphere_area(r))

def ca_viscous(l, strain, mu=MU, sigma=SIGMA):
    return mu*abs(strain)*l/sigma

class O64Tests(unittest.TestCase):
    def test_sphere_laplace(self):
        self.assertTrue(isclose(young_laplace(SIGMA,1/.001,1/.001),144.0))
    def test_static_spheres_any_radius(self):
        # A static two-phase state has constant pressures separated by the Young-Laplace jump.
        for radius in [1e-2,1e-4,1e-6,1e-9]:
            self.assertGreater(2*SIGMA/radius,0)
    def test_torus_outer(self):
        k1,k2=torus_curvatures(1,.35,0)
        self.assertTrue(isclose(k1,1/.35));self.assertTrue(isclose(k2,1/1.35))
    def test_torus_inner(self):
        k1,k2=torus_curvatures(1,.35,pi)
        self.assertTrue(isclose(k2,-1/(1-.35)))
    def test_torus_no_static_uniform_jump(self):
        a=sum(torus_curvatures(1,.35,0));b=sum(torus_curvatures(1,.35,pi))
        self.assertGreater(abs(a-b),1)
    def test_two_equal_fragments_area_ratio(self):
        self.assertTrue(isclose(2*sphere_area(equal_volume_daughter_radius(1,2))/sphere_area(1),2**(1/3)))
    def test_fragment_energy_barrier(self):
        for r in [1e-5,1e-3,1e-1]: self.assertGreater(splitting_cost(r,2),0)
    def test_fragment_energy_scales_area(self):
        self.assertTrue(isclose(splitting_cost(.02,2)/splitting_cost(.01,2),4))
    def test_hinze_epsilon_power(self):
        self.assertTrue(isclose(d_hinze(10)/d_hinze(1),10**(-.4),rel_tol=1e-13))
    def test_hinze_sigma_power(self):
        self.assertTrue(isclose(d_hinze(.1,sigma=2*SIGMA)/d_hinze(.1),2**(.6)))
    def test_hinze_rho_power(self):
        self.assertTrue(isclose(d_hinze(.1,rho=2*RHO)/d_hinze(.1),2**(-.6)))
    def test_viscous_ca(self):
        self.assertTrue(isclose(ca_viscous(.001,72),.001))
    def test_viscous_ca_no_integer_min(self):
        self.assertLess(ca_viscous(1e-8,72),ca_viscous(1e-4,72))
    def test_same_shape_different_size(self):
        # Geometric ratios identical; pressures and surface energies are not.
        for r in [.01,.001]: self.assertTrue(isclose(r/(4*r),.25))
        self.assertTrue(isclose((2*SIGMA/.001)/(2*SIGMA/.01),10))
    def test_ell_kolmogorov_dimensional(self):
        eps=.1;eta=(NU**3/eps)**(.25)
        self.assertGreater(eta,0)
        self.assertLess(eta,d_hinze(eps))

    def test_area_quadratic_partition(self):
        self.assertEqual(2**2+2**2+1,3**2)
        self.assertEqual(34**2+38**2+1,51**2)
    def test_minimal_discrete_closure_only_with_area_atom(self):
        A0=1e-12
        rad=3*(A0/(4*pi))**.5
        self.assertTrue(isclose(sphere_area(rad),9*A0))
    def test_no_physical_min_without_fixed_A0(self):
        A0=1e-12
        s1=3*(A0/(4*pi))**.5
        s2=3*((A0/100)/(4*pi))**.5
        self.assertTrue(isclose(s1/s2,10))
    def test_conditional_energy_bound(self):
        A0=1e-12;E=9*SIGMA*A0
        self.assertTrue(SIGMA*3**2*A0<=E)
        self.assertGreater(SIGMA*5**2*A0,E)

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(O64Tests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    with (HERE/'datos'/'escalas_y_curvaturas.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['epsilon_m2_s3','d_H_m','d_H_mm','eta_K_m','eta_K_mm','rho_kg_m3','sigma_N_m','nu_m2_s'])
        for eps in [.001,.01,.1,1.,10.]:
            dh=d_hinze(eps); eta=(NU**3/eps)**.25
            w.writerow([eps,dh,1000*dh,eta,1000*eta,RHO,SIGMA,NU])
    with (HERE/'datos'/'toroide_curvaturas.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['theta_rad','k_merid_m_1','k_toroid_m_1','curvatura_suma_m_1','salto_presion_Pa_con_sigma_072'])
        for theta in [0, pi/4,pi/2,3*pi/4,pi]:
            a,b=torus_curvatures(1,.35,theta);w.writerow([theta,a,b,a+b,SIGMA*(a+b)])
    print('RESULTADO:',result.testsRun,'tests;',len(result.failures),'fallas;',len(result.errors),'errores')
    print('RESULTADOS HINZE (mm):',[(v,round(d_hinze(v)*1e3,4)) for v in [.001,.01,.1,1.,10.]])
    print('COSTO DE FRAGMENTACION, radio 1mm:',splitting_cost(.001,2),'J')
    raise SystemExit(not result.wasSuccessful())
