"""Relectura decimal de centros suministrados; NO certificación de intervalos."""
import json
from pathlib import Path
from decimal import Decimal as D, localcontext

if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    data = json.loads((here.parent / '04_auditoria_Arb/resultados_arb_T1.json').read_text())
    rows = []
    with localcontext() as ctx:
        ctx.prec = 50
        for r in data['etapas']:
            p = r['p']; mu = D(r['mu']); g = D(r['gammaG']); eta = D(r['eta'])
            assert 0 < mu <= g <= eta + D('1e-24')
            alpha = 1 - mu/g
            bound = p*mu*sum(alpha**j for j in range(5))
            assert bound > 1
            rows.append(dict(p=p,alpha=str(alpha),p_J4=str(bound),p_gamma=str(p*D(r['gamma']))))
            print(f'{p:2d}  pJ4={bound:.12f}  p*gamma={p*D(r["gamma"]):.12f}')
    print('OK: ocho centros superan 1; no es certificado de bolas.')
