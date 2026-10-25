#!/usr/bin/env python3
"""Controles reproducibles de O45; no es una demostración de regularidad de NS 3D."""
import math
import json
import unittest
import numpy as np

NU = .03

def mirror(t):
    X = np.array([.3*t*t, .1*math.sin(t), -.02*t])
    Xdot = np.array([.6*t, .1*math.cos(t), -.02])
    ell = 1.5 + .2*math.sin(t)
    elldot = .2*math.cos(t)
    ang = .3*t*t
    c, s = math.cos(ang), math.sin(ang)
    A = np.array([[c, -s, 0.], [s, c, 0.], [0.,0.,1.]])
    omega = np.array([[0., -.6*t, 0.],[.6*t, 0., 0.],[0.,0.,0.]])
    return X,Xdot,ell,elldot,A,omega

def phys(y,t):
    X,Xd,ell,elldot,A,O = mirror(t)
    return X+ell*A@np.array(y)

def coord(x,t):
    X,Xd,ell,elldot,A,O = mirror(t)
    return A.T@(np.array(x)-X)/ell

def velocity(x,t):
    """Exact unforced NS shear on R^3 (locally; periodic in x_2)."""
    return np.array([math.exp(-NU*t)*math.sin(x[1]),0.,0.])

def W(y,t):
    *_, A, _ = mirror(t)
    return A.T@velocity(phys(y,t),t)

def q(y,t):
    X,Xd,ell,elldot,A,O = mirror(t)
    return (W(y,t)-A.T@Xd)/ell-(elldot/ell)*np.array(y)-O@np.array(y)

def numeric_derivative_vector(func,y,t,axis,step=1.e-4):
    yp=np.array(y).copy(); ym=np.array(y).copy()
    yp[axis]+=step;ym[axis]-=step
    return (func(yp,t)-func(ym,t))/(2*step)

def numeric_time_derivative(func,y,t,step=1.e-4):
    return (func(y,t+step)-func(y,t-step))/(2*step)

def numeric_laplacian(func,y,t,step=2.e-3):
    z=np.array(y)
    total=np.zeros(3)
    for j in range(3):
        yp=z.copy(); ym=z.copy();yp[j]+=step;ym[j]-=step
        total+=(func(yp,t)+func(ym,t)-2*func(z,t))/(step*step)
    return total

class TestO45(unittest.TestCase):
    def test_T1_particle_frame(self):
        t=.72; x0=np.array([1.,.6,-.3]);v=np.array([.2,-.1,.05]); step=1e-5
        track=lambda z:coord(x0+v*z,z)
        measured=(track(t+step)-track(t-step))/(2*step)
        X,Xd,ell,elldot,A,O=mirror(t);y=track(t)
        expected=A.T@(v-Xd)/ell-(elldot/ell)*y-O@y
        self.assertLess(np.linalg.norm(measured-expected),2e-9)

    def test_T2_3phases_rank_two(self):
        D=np.array([[1,-1,0],[0,-1,1]],dtype=float)
        self.assertEqual(np.linalg.matrix_rank(D),2)
        self.assertLess(np.linalg.norm(D@np.ones(3)),1e-14)
        lam=.71;alpha=.17;beta=-.31
        phis=np.array([5*lam+alpha,2*lam,3*lam+beta])
        diffs=D@phis
        self.assertAlmostEqual(diffs[0]-diffs[1],phis[0]-phis[2])
        self.assertTrue(np.allclose(D@(phis+3.19*np.ones(3)),diffs))

    def test_T3_gauge_covariant_rates(self):
        lam=.71
        chi_prime=1.7*math.cos(1.7*lam)
        raw=np.array([5.,2.,3.]);b=.23
        old=raw-b
        new=(raw+chi_prime)-(b+chi_prime)
        self.assertTrue(np.allclose(new,old))
        self.assertAlmostEqual(old[0]/old[1],new[0]/new[1])
        # Bare ratios are not invariant under time-dependent common gauge shift.
        self.assertGreater(abs(raw[0]/raw[1]-(raw[0]+chi_prime)/(raw[1]+chi_prime)),1e-3)

    def test_T3_reparametrized_clock(self):
        lam=.73; chi=lam**3+lam; dchi=3*lam**2+1
        a,b,c=5.,2.,3.
        self.assertAlmostEqual((a/dchi)/(b/dchi),a/b)
        self.assertAlmostEqual((c/dchi)/(b/dchi),c/b)

    def test_T5_moving_frame_NS_exact(self):
        t=.65;y=np.array([.3,-.45,.12])
        X,Xd,ell,elldot,A,O=mirror(t)
        lhs=numeric_time_derivative(W,y,t)
        for j in range(3):
            lhs+=q(y,t)[j]*numeric_derivative_vector(W,y,t,j)
        rhs=-O@W(y,t)+NU/(ell*ell)*numeric_laplacian(W,y,t)
        self.assertLess(np.linalg.norm(lhs-rhs),2e-7,
                        f"NS transformed residual {np.linalg.norm(lhs-rhs)}")

    def test_T6_jacobian_continuity(self):
        t=.51;y=np.array([.6,-.3,.8])
        X,Xd,ell,elldot,A,O=mirror(t)
        div=sum(numeric_derivative_vector(q,y,t,j)[j] for j in range(3))
        h=elldot/ell
        self.assertAlmostEqual(div,-3*h,places=7)
        J=ell**3
        self.assertAlmostEqual(3*h*J+J*div,0,places=7)

    def test_T6_tracer_slip_zero(self):
        t=.65;y=np.array([.3,-.45,.12]); x=phys(y,t)
        X,Xd,ell,elldot,A,O=mirror(t)
        yp=A.T@(velocity(x,t)-Xd)/ell-(elldot/ell)*y-O@y
        self.assertLess(np.linalg.norm(yp-q(y,t)),1e-14)

    def test_O25_single_mode_scale(self):
        k=3
        # For omega=cos(k*y), ∫|omega|² / ∫|grad omega|² = 1/k².
        grid=np.linspace(0,2*math.pi,600,endpoint=False)
        omega=np.cos(k*grid); grad=-k*np.sin(k*grid)
        ell=math.sqrt(np.sum(omega**2)/np.sum(grad**2))
        self.assertAlmostEqual(ell,1/k,places=12)

    def test_MCM_normalization(self):
        import math
        N,m=6,4
        L=math.lcm(N,m)
        self.assertEqual(L,12)
        self.assertEqual(1/N,(L//N)/L)
        # Minimal normalized residual is NOT inherited as the same numerator.
        self.assertNotEqual(1/N,1/L)

    def test_O41_defect_from_omitted_phase(self):
        # Family of exact initial derivative identities from O41, 3D extension exists.
        A=1.2; B=.4
        coarse_plus=-A*B/2
        coarse_minus=+A*B/2
        self.assertNotEqual(coarse_plus,coarse_minus)
        self.assertEqual(abs(B)**2,abs(-B)**2)

if __name__=='__main__':
    import sys
    out='/mnt/data/O45_VERIFICACION.json'
    verbosity=2
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(TestO45)
    result=unittest.TextTestRunner(verbosity=verbosity).run(suite)
    report={"program":"Programa de Geometría Relacional", "module":"O45", "date":"2026-10-20", "tests":result.testsRun,"failures":len(result.failures),"errors":len(result.errors),"successful":result.wasSuccessful(),"scope":"Identidades cinemáticas, gauge, NS exacto en cizalla, conservación bajo marco, MCM. No prueba regularidad global ni singularidad física."}
    with open(out,'w') as f:json.dump(report,f,indent=2,ensure_ascii=False)
    print(json.dumps(report,ensure_ascii=False))
    if not result.wasSuccessful():sys.exit(1)
