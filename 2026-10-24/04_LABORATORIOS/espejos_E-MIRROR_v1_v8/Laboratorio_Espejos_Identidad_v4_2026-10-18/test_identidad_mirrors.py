"""Pruebas v4: las conclusiones deben surgir de los sensores, no de etiquetas internas."""
import unittest
import numpy as np
from identidad_mirrors import (C1,C2,S1,S2,V1,V2,NOISE_STD,MIRROR,W,H,
    sensor,appearances,camera_project,pixel_ray,reflect_virtual,reflect_valid,
    reflect_point,fit_spots,fit_sparse_spots,infer_common_source_two_faces,
    infer_first_mirror,triangulate,core_experiment)

class TestMirrorV4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result,cls.images=core_experiment()

    def test_reflexion_involutiva(self):
        for face in ('X+','Y+'):
            self.assertTrue(np.allclose(reflect_point(reflect_point(S1,face),face),S1))

    def test_lado_finito_valida_reflejos(self):
        for s in (S1,S2):
            self.assertTrue(reflect_valid(C1,s,'X+'))
            self.assertTrue(reflect_valid(C2,s,'X+'))
            self.assertTrue(reflect_valid(C1,s,'Y+'))

    def test_fuente_fuera_apertura_no_visible(self):
        s=np.array([-.3,5.,.2])
        self.assertFalse(reflect_valid(C1,s,'X+'))

    def test_ray_pixel_unidad(self):
        px=camera_project(C1,V1)
        self.assertTrue(np.allclose(pixel_ray(C1,px),(V1-C1)/np.linalg.norm(V1-C1),atol=1e-12))

    def test_coincidencia_proyectada(self):
        self.assertLess(np.linalg.norm(camera_project(C1,V1)-camera_project(C1,V2)),1e-11)

    def test_fuentes_distintas(self):
        self.assertGreater(np.linalg.norm(S1-S2),.3)

    def test_uno_dos_igual_imagen_si_brillo_desconocido(self):
        self.assertTrue(np.array_equal(self.images['A_una_fuente'],self.images['A_dos_fuentes']))

    def test_primera_camara_un_spot_detectado(self):
        self.assertEqual(self.result['A_una_vs_dos_misma_camara']['estimacion_desde_una_imagen']['n_spots'],1)

    def test_primera_camara_infiere_amplitud_doble(self):
        s=self.result['A_una_vs_dos_misma_camara']['estimacion_desde_una_imagen']['spots'][0]
        self.assertAlmostEqual(s['amplitude'],2.,delta=.02)

    def test_camara_desplazada_dos_spots(self):
        self.assertEqual(self.result['B_mover_camara']['estimacion']['n_spots'],2)

    def test_segundo_espejo_desdobla(self):
        self.assertEqual(self.result['C_abrir_otro_espejo']['estimacion_y']['n_spots'],2)

    def test_dos_fuentes_reconstruibles_dos_vistas(self):
        rec=self.result['B_mover_camara']['triangulacion_inferencia_a_posteriori']
        self.assertEqual(len(rec),2)
        self.assertLess(max(v['error_contra_verdad_m'] for v in rec),.005)

    def test_una_fuente_dos_imagenes(self):
        self.assertEqual(len(appearances(C1,[S1],faces=('X+','Y+'),front=(1,1,0))),2)
        self.assertEqual(len(fit_sparse_spots(self.images['D_una_fuente_dos_espejos'])),2)

    def test_infiere_un_origen_desde_dos_reflejos(self):
        r=self.result['D_misma_fuente_dos_espejos']['reconstruccion']
        self.assertIsNotNone(r)
        self.assertEqual(set(r['canales_observados']),{'X+','Y+'})
        self.assertLess(r['error_contra_verdad_m'],.005)

    def test_pantalla_negra_no_fuentes(self):
        self.assertEqual(fit_spots(np.zeros((H,W)))['n_spots'],0)

    def test_ruido_seed_alternativas(self):
        # Robustez bajo semillas nuevas sin introducir las ubicaciones en el inferidor.
        for seed in (21,41,71):
            im1=sensor(C1,[S1,S2],seed=seed)
            im2=sensor(C2,[S1,S2],seed=seed+1)
            self.assertEqual(fit_spots(im1)['n_spots'],1)
            self.assertEqual(fit_spots(im2)['n_spots'],2)

    def test_calibracion_mirror_asignacion_sin_etiquetas(self):
        spots=self.result['D_misma_fuente_dos_espejos']['deteccion']
        faces={infer_first_mirror(C1,(p['x'],p['y']),(1.,1.,0.)) for p in spots}
        self.assertEqual(faces,{'X+','Y+'})

    def test_un_modelo_un_spot_bic(self):
        a=self.result['A_una_vs_dos_misma_camara']['estimacion_desde_una_imagen']
        self.assertLess(a['bic_1'],a['bic_2'])

    def test_modelo_dos_spots_bic(self):
        b=self.result['B_mover_camara']['estimacion']
        self.assertLess(b['bic_2'],b['bic_1'])

if __name__=='__main__':unittest.main(verbosity=2)
