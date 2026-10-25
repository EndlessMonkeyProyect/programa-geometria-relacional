import unittest
import laboratorio as e

class TestEspejos(unittest.TestCase):
    def test_reflexiones_son_involuciones(self):
        for m in [e.RX,e.RY,e.RZ,e.DXY,e.DYZ,e.DXZ]:
            self.assertEqual(e.compose(m,m),e.I)
            self.assertEqual(e.det(m),-1)
    def test_grupos_y_orbitas(self):
        for gens, esperado in [([e.RX,e.RY,e.RZ],8),
                               ([e.RX,e.RY,e.RZ,e.DXY],16),
                               ([e.RX,e.RY,e.RZ,e.DXY,e.DYZ],48)]:
            g=e.generated_group(gens)
            self.assertEqual(len(g),esperado)
            self.assertEqual(len({e.apply(m,(1,2,3)) for m in g}),esperado)
            self.assertEqual(sum(e.det(m)==1 for m in g),esperado//2)
    def test_degeneracion_en_vertice_y_simetria(self):
        gs=[e.RX,e.RY,e.RZ]
        for p,expected in [((1,2,3),8),((0,2,3),4),((0,0,3),2),((0,0,0),1)]:
            self.assertEqual(e.orbit_report(gs,p)['posiciones_virtuales_distintas'],expected)
        self.assertEqual(e.orbit_report(gs+[e.DXY,e.DYZ],(1,1,1))['posiciones_virtuales_distintas'],8)
    def test_observabilidad(self):
        o=e.observations()
        self.assertEqual(o['una_vista_xy_rango'],2)
        self.assertEqual(o['misma_direccion_con_reflejo_en_x_rango'],2)
        self.assertEqual(o['segunda_vista_calibrada_con_intercambio_xz_rango'],3)
        self.assertEqual(o['filtros_que_solo_dejan_y_rango'],1)
        self.assertEqual(o['opacidad_exacta_z_cero_rango'],2)
        self.assertEqual(o['transmision_z_1_100_rango'],3)
    def test_celdas_y_angulos(self):
        c=e.virtual_cells(2)
        self.assertEqual(c['celdas_virtuales'],125)
        self.assertEqual(c['firmas_de_orientacion'],8)
        self.assertEqual(c['paridades_totales'],{'impar':62,'par':63})
        self.assertEqual({k['angulo_grados']:k['transformaciones_del_grupo_abstracto'] for k in [e.angle_group(n) for n in ['90','60','45','61','60.1']]}, {'90':4,'60':6,'45':8,'61':360,'60.1':3600})
    def test_atenuacion_de_reflejos(self):
        self.assertEqual(e.attenuation_layers('0.9')['rebotes_maximos_detectables'],28)
        self.assertEqual(e.attenuation_layers('0.5')['rebotes_maximos_detectables'],4)
        self.assertEqual(e.attenuation_layers('0.8')['rebotes_maximos_detectables'],13)
        self.assertIsNone(e.attenuation_layers('1')['rebotes_maximos_detectables'])
        self.assertEqual(e.attenuation_layers('0.5')['celdas_virtuales_en_bola_L1'],129)
    def test_control_esfera_objeto_etiquetado(self):
        c=e.control_esfera_vs_objeto_asimetrico()
        self.assertEqual(c['transformaciones'],48)
        self.assertEqual(c['esfera_homogenea_posiciones_de_centro_distintas'],8)
        self.assertEqual(c['cuatro_puntos_etiquetados_imagenes_completas_distintas'],48)
    def test_resultados(self):
        self.assertTrue(all(e.run()['H_proposiciones_comprobables'].values()))

if __name__=='__main__':
    unittest.main(verbosity=2)
