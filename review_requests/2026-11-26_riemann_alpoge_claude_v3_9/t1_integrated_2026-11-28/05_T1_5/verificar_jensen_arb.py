"""Recalcula el Gram original en Arb y certifica la cota de Jensen. Requiere python-flint.
Ejecutar desde cualquier carpeta: python verificar_jensen_arb.py 19
No usar -I con un import local sin ruta explícita. No modifica archivos de origen.
"""
import sys, json, platform
from pathlib import Path
here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / '04_auditoria_Arb'))
# El módulo original lee sys.argv[1] durante el import; fijar 19 por defecto.
if len(sys.argv) == 1:
    sys.argv.append('19')
if len(sys.argv) != 2 or sys.argv[1] not in ('17','19'):
    raise SystemExit('Uso: python verificar_jensen_arb.py [17|19]')
import verificacion_arb_T1 as base
from flint import arb

def enclosure(x):
    # repr/str de Arb incluye un intervalo decimal con redondeo exterior;
    # almacenar también extremos calculados, sin convertir a float.
    return {'ball': str(x), 'lower_ball': str(x.lower()), 'upper_ball': str(x.upper())}

if __name__ == '__main__':
    stages, elapsed, gram_radius, n = base.run()
    rows = []
    for r in stages:
        p = r['p']; mu = r['mu']; g = r['gammaG']; eta = r['eta']
        assert mu > 0 and g > 0
        alpha = 1-mu/g
        assert alpha >= 0 and alpha < 1
        j4 = mu*sum((alpha**j for j in range(5)), arb(0))
        scaled = p*j4
        assert scaled > 1, (p, scaled)
        assert p*r['gamma'] > 1
        assert eta > j4
        assert eta > mu
        if r['r'] > 1:
            assert eta > r['gamma']
        rows.append({'p':p, 'r':r['r'], 'alpha':enclosure(alpha), 'J4':enclosure(j4),
                     'p_J4':enclosure(scaled), 'p_gamma':enclosure(p*r['gamma']),
                     'certified_p_J4_gt_1':True,
                     'arb_values':{k:enclosure(v) for k,v in r.items() if isinstance(v,arb) and k!='beta'},
                     'spectral_diagnostics_not_certified':{k:str(r[k]) for k in ('a','bplus','cond_M','condMG','cond_Gp','kappaH','beta')}})
        print(f'p={p}: pJ4={scaled} > 1; p*gamma > 1')
    dest = Path.cwd()/f'certificado_jensen_arb_p{base.PMAX}.json'
    dest.write_text(json.dumps({'python':platform.python_version(),'flint':base.flint.__version__,
        'numpy':base.np.__version__,'mpmath':base.mp.__version__,'precision_bits':base.flint.ctx.prec,
        'etapas':rows},indent=2)+'\n',encoding='utf-8')
    print('OK:', dest)
