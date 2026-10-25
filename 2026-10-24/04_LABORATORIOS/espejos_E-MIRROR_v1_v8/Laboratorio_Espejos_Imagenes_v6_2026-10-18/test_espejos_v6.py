import unittest
import numpy as np
from espejos_v6 import C,Setup,histories,gated_fields,geometric_return_paths,streak_image

class TestMirrorV6(unittest.TestCase):
    def test_retorno_de_mitad(self):
        s=Setup(B=1.0)
        self.assertAlmostEqual(2*s.A/C,4*s.B/C,places=14)

    def test_no_coincidencia_irracional(self):
        s=Setup(B=np.sqrt(2))
        self.assertGreater(abs(2*s.A/C-4*s.B/C),1e-9)

    def test_historias_cuantificadas(self):
        self.assertEqual(len(histories(Setup(depth=7))),2*(2**7-1))

    def test_retorno_A_y_B_a_13ns(self):
        s=Setup(B=1)
        t=2*s.A/C*1e9
        h=[r for r in histories(s) if abs(r['time_ns']-t)<1e-8]
        self.assertTrue(any(r['side']=='A' and r['visits']==1 for r in h))
        self.assertTrue(any(r['side']=='B' and r['visits']==2 for r in h))

    def test_paridad_no_esta_fijada_por_lado_con_dos_semillas(self):
        s=Setup(B=1)
        t=2*s.A/C*1e9
        h=[r for r in histories(s) if abs(r['time_ns']-t)<1e-8]
        self.assertEqual({r['reflection_parity'] for r in h},{1})
        self.assertEqual({r['side'] for r in h},{'A','B'})

    def test_paridad_condicional_semilla_A(self):
        for r in histories(Setup(depth=7),launch='A'):
            self.assertEqual(r['side']=='A',r['transmissions']%2==0)
            self.assertEqual(r['reflection_parity'], (1-r['transmissions'])%2)

    def test_cota_de_interferencia(self):
        s=Setup()
        t=2*s.A/C*1e9
        e=gated_fields(s,t)
        self.assertGreater(e['max_posible'],e['incoherente'])
        self.assertLess(e['min_posible'],e['incoherente'])
        for phi in np.linspace(0,2*np.pi,30):
            val=gated_fields(s,t,phi=phi)['coherente']
            self.assertGreaterEqual(val,e['min_posible']-1e-12)
            self.assertLessEqual(val,e['max_posible']+1e-12)

    def test_promedio_fase_entre_canales(self):
        s=Setup();t=2*s.A/C*1e9
        e=gated_fields(s,t)
        vals=[gated_fields(s,t,phi=p)['coherente'] for p in np.linspace(0,2*np.pi,2048,endpoint=False)]
        self.assertAlmostEqual(float(np.mean(vals)),(abs(e['E_A'])**2+abs(e['E_B'])**2)/2,places=9)

    def test_opacidad_tap_cero(self):
        s=Setup(tap=0)
        e=gated_fields(s,2*s.A/C*1e9)
        self.assertEqual(e['incoherente'],0)
        self.assertEqual(e['coherente'],0)

    def test_diferencia_fase(self):
        s=Setup();t=2*s.A/C*1e9
        self.assertGreater(gated_fields(s,t,phi=np.pi)['coherente'],gated_fields(s,t,phi=0)['coherente'])

    def test_rayos_fuera_apertura(self):
        s=Setup(aperture=.03,y0=.04,depth=4)
        self.assertEqual(len(geometric_return_paths(s,np.array([0.]))),0)

    def test_rayos_centro_dentro_apertura(self):
        s=Setup(depth=4)
        rows=geometric_return_paths(s,np.array([0.]))
        self.assertGreater(len(rows),0)
        self.assertTrue(all(abs(r['y_m'])<=s.aperture for r in rows))

    def test_rayo_directo_y_desplazamiento(self):
        s=Setup(depth=1,y0=0)
        theta=.01
        rows=geometric_return_paths(s,np.array([theta]))
        for arm,L in [('A',s.A),('B',s.B)]:
            x=next(r for r in rows if r['side']==arm)
            self.assertAlmostEqual(x['y_m'],round(2*L*np.tan(theta),7),places=7)

    def test_R_uno_sin_cruces_desde_A(self):
        s=Setup(R=1,depth=6)
        self.assertTrue(all(r['side']=='A' for r in histories(s,'A')))

    def test_R_cero_sin_rebotes_en_vidrio(self):
        s=Setup(R=0,depth=4)
        h=histories(s,'A')
        self.assertTrue(all(abs(r['amplitude'])<1e-14 for r in h if r['pane_reflections']>0))

    def test_camara_finita(self):
        s=Setup(depth=4)
        img,rows=streak_image(s,angles=19,t_bins=40,y_bins=20)
        self.assertEqual(img['A'].shape,(20,40))
        self.assertTrue(np.isfinite(img['B']).all())
        self.assertGreater(float(img['B'].sum()),0)

    def test_consistencia_intensidad(self):
        for B in [.7,1.0,1.4]:
            e=gated_fields(Setup(B=B),2*2/C*1e9)
            self.assertGreaterEqual(e['incoherente'],0)
            self.assertGreaterEqual(e['min_posible'],0)
            self.assertGreaterEqual(e['max_posible'],e['min_posible'])

    def test_validacion(self):
        with self.assertRaises(ValueError): histories(Setup(R=1.3))
        with self.assertRaises(ValueError): histories(Setup(A=-1))

if __name__=='__main__': unittest.main()
