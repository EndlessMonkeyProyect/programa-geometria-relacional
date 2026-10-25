#!/usr/bin/env python3
"""O33: verificaciones reproducibles independientes; no es DNS completa."""
import json, math, unittest, pathlib
import numpy as np

ROOT=pathlib.Path(__file__).resolve().parent
SIGMA_X2=0.09; SIGMA_Y2=0.01
CENT_A=np.array([-4.,0.]); CENT_B=-CENT_A
NU=0.001; T=0.01

def gauss(x, c, sx2=SIGMA_X2,sy2=SIGMA_Y2):
    dx=x-c
    return np.exp(-.5*(dx[...,0]**2/sx2+dx[...,1]**2/sy2))/(2*math.pi*math.sqrt(sx2*sy2))

def lapgauss(x,c, sx2=SIGMA_X2,sy2=SIGMA_Y2):
    dx=x-c
    g=gauss(x,c,sx2,sy2)
    return g*(dx[...,0]**2/sx2**2+dx[...,1]**2/sy2**2-1/sx2-1/sy2)

def gradgauss(x,c,sx2=SIGMA_X2,sy2=SIGMA_Y2):
    dx=x-c
    return -gauss(x,c,sx2,sy2)[...,None]*np.stack((dx[...,0]/sx2, dx[...,1]/sy2),axis=-1)

def u_bs(eval_xy, source_xy, source_mass):
    """Biot-Savart discrete sampled quadrature without singular self-force."""
    out=[]
    for p in np.atleast_2d(eval_xy):
        dz=p-source_xy
        r2=np.sum(dz*dz,axis=1)
        mask=r2>1e-20
        fac=source_mass[mask]/(2*math.pi*r2[mask])
        d=dz[mask]
        out.append(np.sum(fac[:,None]*np.stack((-d[:,1],d[:,0]),axis=1),axis=0))
    return np.array(out)

def rotate(x,ang):
    ca,sa=math.cos(ang),math.sin(ang)
    return np.asarray(x) @ np.array([[ca,sa],[-sa,ca]])  # row formulation R_theta

def quad_cov(S):
    return complex(S[0,0]-S[1,1],2*S[0,1])

class O33Tests(unittest.TestCase):
    def test_mirror_exact_profile(self):
        pts=np.array([[-4,-.2],[-3.9,.1],[-2,0],[0,0],[3,1],[4,.2]])
        np.testing.assert_allclose(gauss(pts,CENT_B),gauss(-pts,CENT_A),rtol=1e-13,atol=1e-14)
    def test_rotation_two_pi(self):
        pts=np.array([[.1,.2],[2.,3.],[-3.,.8]])
        np.testing.assert_allclose(rotate(rotate(pts, math.pi),math.pi),pts,rtol=0,atol=1e-14)
    def test_centroid_mirror(self): self.assertTrue(np.array_equal(CENT_B,-CENT_A))
    def test_initial_quadrupole_mirror(self): self.assertEqual(complex(SIGMA_X2-SIGMA_Y2,0),complex(.08,0))
    def test_ratio_anisotropy(self): self.assertAlmostEqual((SIGMA_X2-SIGMA_Y2)/(SIGMA_X2+SIGMA_Y2),.8)
    def test_gradient_covariance(self):
        p=np.array([[-4.02,.04],[-3.92,-.08],[4.01,-.01]])
        np.testing.assert_allclose(gradgauss(-p,CENT_B),-gradgauss(p,CENT_A),atol=1e-13,rtol=1e-13)
    def test_laplacian_covariance(self):
        p=np.array([[-4.02,.04],[-3.92,-.08],[4.01,-.01]])
        np.testing.assert_allclose(lapgauss(-p,CENT_B),lapgauss(p,CENT_A),atol=1e-12,rtol=1e-13)
    def test_cyclic_three_quadrupoles(self):
        S=np.diag([.09,.01]); q=quad_cov(S)
        for j in (0,1,2):
            th=2*math.pi*j/3
            R=np.array([[math.cos(th),-math.sin(th)],[math.sin(th),math.cos(th)]])
            qr=quad_cov(R@S@R.T)
            self.assertAlmostEqual(abs(qr-q*complex(math.cos(2*th),math.sin(2*th))),0,delta=1e-14)
    def test_cyclic_three_centers(self):
        p=np.array([4.,0.]); pts=[rotate(p,2*math.pi*j/3) for j in range(3)]
        np.testing.assert_allclose(sum(pts),[0,0],atol=2e-15)
    def test_quadrupole_frame_invariance(self):
        S=np.array([[.09,.017],[.017,.02]])
        for th in (.03,.41,1.77,math.pi):
            R=np.array([[math.cos(th),-math.sin(th)],[math.sin(th),math.cos(th)]])
            self.assertAlmostEqual(abs(quad_cov(R@S@R.T)-quad_cov(S)*np.exp(2j*th)),0,delta=1e-14)
    def test_threefold_total_quadrupole_cancels(self):
        # Para 3 copias rotadas, el segundo momento del total se anula
        # aunque cada una tenga forma eliptica local Q_j != 0.
        c0=4.+0j; q0=.08+0j
        terms=[complex(math.cos(2*j*math.pi/3),math.sin(2*j*math.pi/3))**2*(c0*c0+q0) for j in range(3)]
        self.assertAlmostEqual(abs(sum(terms)),0,delta=1e-13)
        self.assertGreater(abs(q0),0)
    def test_threefold_third_moment_survives(self):
        c0=4.+0j; q0=.08+0j
        # Cada gaussiana tiene tercer momento central complejo nulo.
        terms=[complex(math.cos(2*j*math.pi/3),math.sin(2*j*math.pi/3))**3*(c0**3+3*c0*q0) for j in range(3)]
        self.assertAlmostEqual(sum(terms).real,194.88,delta=1e-12)
        self.assertAlmostEqual(sum(terms).imag,0,delta=1e-12)
    def test_cyclic_moment_selection_rules(self):
        for m in range(3,9):
            phase=np.exp(2j*math.pi/m)
            for k in range(1,2*m+1):
                sm=sum((phase**j)**k for j in range(m))
                self.assertAlmostEqual(abs(sm-(m if k%m==0 else 0)),0,delta=1e-12)
    def test_fourth_moment_adversary(self):
        a=.2; base=.09-a*a
        m4_gauss=3*.09**2
        m4_mix=3*base**2+6*base*a*a+a**4
        self.assertAlmostEqual(m4_gauss,.0243)
        self.assertAlmostEqual(m4_mix,.0211)
        self.assertGreater(abs(m4_gauss-m4_mix),.003)
    def test_same_quadrupole_different_fourth(self):
        a=.2; base=.09-a*a
        self.assertAlmostEqual(base+a*a,.09)
        self.assertAlmostEqual((base+a*a)-.01,.08)
    def test_o31_o32_certificates(self):
        gamma=2.; M0=1/(math.pi*math.sqrt(.09*.01)) # sum of individual peak bounds
        U0=math.sqrt(2*gamma*M0/math.pi)
        S0=.10; q0=.08
        aT=math.sqrt(S0+4*NU*T)+U0*T
        H=U0/(3*NU)*((S0+4*NU*T)**1.5-S0**1.5)+U0**2*T*T
        self.assertLess(4*aT,8-2*U0*T)
        self.assertLess(H,q0)
        self.assertGreater((q0-H)/(aT*aT),.44)
    def test_even_total_velocity_odd(self):
        # Cuadratura Biot-Savart instantanea de un flujo positivo en R2
        coords=np.linspace(-5.5,5.5,221)
        xx,yy=np.meshgrid(coords,coords,indexing='xy')
        pos=np.stack([xx.ravel(),yy.ravel()],axis=1)
        dm=(gauss(pos,CENT_A)+gauss(pos,CENT_B))*(coords[1]-coords[0])**2
        pts=np.array([[-4,.08],[-3.8,-.05],[-.2,.1],[1.,.3],[3.9,.05]])
        u=u_bs(np.concatenate((pts,-pts)),pos,dm)
        np.testing.assert_allclose(u[:len(pts)],-u[len(pts):],atol=5e-12,rtol=0)
    def test_adversarial_same_quadrupole_different_shape_frequency(self):
        # Integración cuadratural de la expresión exacta de dot Q en NS 2D.
        # Se auditan dos resoluciones; son controles numéricos, no prueba PDE completa.
        from scipy.signal import fftconvolve
        detunings=[]
        for h in (.08,.04):
            xs=np.arange(-6,6+h/2,h)
            X,Y=np.meshgrid(xs,xs)
            def gg(cx,a=.09,b=.01):
                return np.exp(-.5*((X-cx)**2/a+Y**2/b))/(2*math.pi*math.sqrt(a*b))
            A=gg(-4)
            B=.5*(gg(4.2,.05,.01)+gg(3.8,.05,.01))
            Bmirror=gg(4)
            N=len(xs)
            dd=np.arange(-(N-1),N)*h
            DX,DY=np.meshgrid(dd,dd)
            rr=DX*DX+DY*DY
            kx=np.divide(-DY,2*math.pi*rr,out=np.zeros_like(rr),where=rr>0)
            ky=np.divide(DX,2*math.pi*rr,out=np.zeros_like(rr),where=rr>0)
            def phase_speed(Bb):
                w=A+Bb
                U=(fftconvolve(w,kx,mode='same')+1j*fftconvolve(w,ky,mode='same'))*h*h
                out=[]
                for wi,c in ((A,-4),(Bb,4)):
                    gamma=np.sum(wi)*h*h
                    z=X-c+1j*Y
                    Q=np.sum(z*z*wi)*h*h/gamma
                    Qdot=2*np.sum(z*U*wi)*h*h/gamma
                    out.append((Qdot/Q).imag)
                return out
            fa,fb=phase_speed(B)
            fma,fmb=phase_speed(Bmirror)
            self.assertLess(abs(fma-fmb),1e-9)
            self.assertLess(fa,fb)
            detunings.append(fa-fb)
        self.assertLess(abs(detunings[0]-detunings[1]),3e-5)
        self.assertTrue(-.018<detunings[-1]<-.017)
    def test_ns_rhs_mirror_instant(self):
        coords=np.linspace(-5.5,5.5,221)
        xx,yy=np.meshgrid(coords,coords,indexing='xy')
        pos=np.stack([xx.ravel(),yy.ravel()],axis=1)
        dm=(gauss(pos,CENT_A)+gauss(pos,CENT_B))*(coords[1]-coords[0])**2
        pts=np.array([[-4,.06],[-3.8,-.05],[-4.16,.06],[-.2,.1]])
        ue=u_bs(np.concatenate((pts,-pts)),pos,dm)
        fA=-(ue[:len(pts)]*gradgauss(pts,CENT_A)).sum(axis=1)+NU*lapgauss(pts,CENT_A)
        fB=-(ue[len(pts):]*gradgauss(-pts,CENT_B)).sum(axis=1)+NU*lapgauss(-pts,CENT_B)
        np.testing.assert_allclose(fA,fB,atol=2e-11,rtol=1e-10)

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(O33Tests)
    res=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'version':'O33-2026-10-20','testsRun':res.testsRun,'failures':len(res.failures),'errors':len(res.errors),'passed':res.wasSuccessful(), 'scope':'Identidades por simetría, momentos gaussianos, controles instantaneos cuadratura Biot Savart; no DNS.'}
    (ROOT/'VALIDACION_O33.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    if not res.wasSuccessful():raise SystemExit(1)
