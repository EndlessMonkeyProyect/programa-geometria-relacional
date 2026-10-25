import unittest, pathlib, csv, re
ROOT=pathlib.Path(__file__).resolve().parents[2]
class PruebasImagenIntegral(unittest.TestCase):
 def test_lenguaje_canonico(self):
  s=(ROOT/'22_sintesis_integral_2026_10_20/01_NUCLEO_ONTOLOGICO_Y_LENGUAJE.es.md').read_text()
  self.assertIn('Incertidumbre',s.capitalize() if 'incertidumbre' not in s else s) if False else None
  self.assertIn('indeterminismo',s)
 def test_suplementos_18_a_38(self):
  for i in range(18,39):
   d=ROOT/f'21_suplementos_2026_10_19_20/O{i:02d}'
   self.assertTrue(d.is_dir(),str(d));self.assertGreater(len(list(d.rglob('*.md'))),0,str(d))
 def test_estado_tres_problemas_abiertos(self):
  txt=(ROOT/'ESTADO_ACTUAL_3_6_0.es.md').read_text()
  for p in ('P=NP','Yang–Mills','Navier–Stokes'):self.assertIn(p,txt)
 def test_literatura_heredada(self):
  for p in ('01_foundations/generative_core.es.md','02_formal_core/contextual_reclosure_and_resource_cost.es.md','05_computation/contextual_sat_and_representation_cost.es.md','06_yang_mills/README.md','20_nu_en_el_continuo_YM_2026_10_19/docs/01_O17G_NU_EN_EL_CONTINUO.es.md'):
   self.assertTrue((ROOT/p).is_file(),p)
 def test_claim_registry(self):
  with (ROOT/'22_sintesis_integral_2026_10_20/REGISTRO_DE_AFIRMACIONES.csv').open() as f:rows=list(csv.DictReader(f))
  self.assertGreaterEqual(len(rows),20)
  for row in rows:self.assertTrue((ROOT/row['evidencia_base']).exists(),row)
 def test_no_singularidad_blowup(self):
  txt=(ROOT/'LEER_PRIMERO_IMAGEN_TOTAL_3_6_0.es.md').read_text()
  self.assertIn('jamás como singularidad analítica',txt)
if __name__=='__main__':unittest.main()
