"""Pruebas mínimas para el laboratorio físico de cámara y paneles finitos."""
import unittest
import numpy as np
from raytrace_cubo import (CAM, SOURCE, SOURCE_RADIUS, camera_directions, pinhole_directions,
                            main_mirror_t, boundary_t, sphere_dist, trace, WALL)


class OpticaFinitaTests(unittest.TestCase):
    def test_directo_centro_fuente(self):
        ray=(SOURCE-CAM);ray/=np.linalg.norm(ray)
        t=sphere_dist(CAM[None,:],ray[None,:])[0]
        self.assertAlmostEqual(t,np.linalg.norm(SOURCE-CAM)-SOURCE_RADIUS,places=8)

    def test_mirror_vertical_un_rebote_al_centro(self):
        image=SOURCE.copy();image[0]=1.80-SOURCE[0]
        D=image-CAM;D/=np.linalg.norm(D)
        t,n=main_mirror_t(CAM[None,:],D[None,:])
        self.assertTrue(np.isfinite(t[0]))
        self.assertAlmostEqual(float(n[0]@D),D[0],places=10)
        hit=CAM+t[0]*D
        bounced=D-2*np.dot(D,n[0])*n[0]
        direct=(SOURCE-hit);direct/=np.linalg.norm(direct)
        self.assertTrue(np.allclose(bounced,direct,atol=1.e-12))

    def test_reflexion_conserva_norma(self):
        O=np.array([[.1,-.2,.2],[.2,.1,.1]])
        D=np.array([[1.,.1,.1],[1.,-.1,.2]])
        D=D/np.linalg.norm(D,axis=1)[:,None]
        t,n=main_mirror_t(O,D,tilt_deg=5.,curve=.035)
        self.assertTrue(np.all(np.isfinite(t)))
        reflected=D-2*np.sum(D*n,axis=1)[:,None]*n
        self.assertTrue(np.allclose(np.linalg.norm(reflected,axis=1),1.))
        self.assertTrue(np.allclose(np.sum(D*n,axis=1),-np.sum(reflected*n,axis=1)))

    def test_pane_cuadratico_vs_plano_k0(self):
        O=np.array([[.1,-.2,.2],[.2,.1,.1]])
        D=np.array([[1.,.1,.1],[1.,-.1,.2]])
        D=D/np.linalg.norm(D,axis=1)[:,None]
        ta,na=main_mirror_t(O,D,tilt_deg=3.,curve=0)
        tb,nb=main_mirror_t(O,D,tilt_deg=3.,curve=0.0)
        self.assertTrue(np.allclose(ta,tb))
        self.assertTrue(np.allclose(na,nb))

    def test_plano_fuera_apertura_rechazado(self):
        O=np.array([[0.,.95,0.]])
        D=np.array([[1.,0.,0.]])
        t,_=main_mirror_t(O,D)
        self.assertTrue(np.isinf(t[0]))

    def test_esfera_rayo_se_aleja_no_detecta(self):
        D=CAM-SOURCE;D/=np.linalg.norm(D)
        self.assertTrue(np.isinf(sphere_dist(CAM[None,:],D[None,:])[0]))

    def test_rayos_camara_normados(self):
        a=camera_directions(22,12)
        b=pinhole_directions(22,12)
        self.assertEqual(a.shape,(264,3))
        self.assertEqual(b.shape,(264,3))
        self.assertTrue(np.allclose(np.linalg.norm(a,axis=1),1.))
        self.assertTrue(np.allclose(np.linalg.norm(b,axis=1),1.))

    def test_camara_frontal_no_ve_fuente_directa(self):
        r=trace(100,70,2,view='pinhole',front=(1.,0.,0.))
        self.assertEqual(r['rayos_por_numero_rebotes'][0],0)
        self.assertGreater(r['pixeles_con_fuente'],0)

    def test_camara_frontal_con_panel_opaco_no_ve_fuente(self):
        r=trace(100,70,3,view='pinhole',front=(1.,0.,0.),transmit_plus=0.)
        self.assertEqual(r['pixeles_con_fuente'],0)
        self.assertEqual(r['trayectorias_robustas_8pix'],0)

    def test_camara_cambia_perspectiva_revela_fuente(self):
        r=trace(100,70,0,view='pinhole',front=tuple(SOURCE-CAM),transmit_plus=0.)
        self.assertGreater(r['rayos_por_numero_rebotes'][0],0)

    def test_angulo_pequeno_preserva_fuente(self):
        r=trace(120,80,4,view='pinhole',front=(1.,0.,0.),tilt_deg=3.)
        self.assertGreater(r['trayectorias_robustas_8pix'],0)
        self.assertLess(r['reconstruccion_calibrada']['reflected_only']['error_posicion_m'],.06)

    def test_filtro_ademas_no_cambia_geometria_directa(self):
        a=trace(80,60,0,view='pinhole',front=tuple(SOURCE-CAM),transmit_plus=1.)
        b=trace(80,60,0,view='pinhole',front=tuple(SOURCE-CAM),transmit_plus=0.)
        self.assertEqual(a['pixeles_con_fuente'],b['pixeles_con_fuente'])

    def test_distancia_a_paredes_cubo(self):
        o=np.array([[0.,0.,0.]])
        d=np.array([[1.,0.,0.]])
        t=boundary_t(o,d)[0]
        self.assertAlmostEqual(t[1],1.)
        self.assertTrue(np.isinf(t[0]))

if __name__=='__main__':unittest.main()
