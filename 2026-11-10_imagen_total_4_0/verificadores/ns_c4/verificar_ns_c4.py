#!/usr/bin/env python3
"""Verificación reproducible C4-E1 y C4-E3 (Imagen Total 4.0, 10 de noviembre de 2026).

Biblioteca estándar. Controles finitos de identidades demostradas; el alcance está en la sección 7.10.
Corre desde cualquier directorio; escribe datos/resultados_ns_c4.json junto a este archivo.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
import random

SEED = 20261110
OUT = Path(__file__).resolve().parent / 'datos' / 'resultados_ns_c4.json'


def B_directa(h: float, U: float = 1.) -> float:
    points = [(0., 0.), (h, 0.), (h, h), (0., h)]
    sides = [(1., 0.), (0., 1.), (-1., 0.), (0., -1.)]
    def stretch(p, e):
        sx = U * math.cos(p[0]) * math.cos(p[1])
        return sx * (e[0] ** 2 - e[1] ** 2)
    return sum(stretch(points[i], sides[(i - 1) % 4]) - stretch(points[i], sides[i]) for i in range(4))


def B_formula(h: float, U: float = 1.) -> float:
    return -2 * U * (1 - math.cos(h)) ** 2


def norm(v):
    return math.hypot(*v)


def monitor_cizalla(pts, eps):
    """Phi(x,y)=(x+eps*sin(y), y), F=[[1,eps*cos(y)],[0,1]]."""
    logh = 0.
    perimeter = 0.
    for i in range(4):
        x, y = pts[i]
        xx, yy = pts[(i + 1) % 4]
        vx, vy = xx - x, yy - y
        length = math.hypot(vx, vy)
        assert length > 0
        perimeter += length
        ex, ey = vx / length, vy / length
        before = math.hypot(ex + eps * math.cos(y) * ey, ey)
        after = math.hypot(ex + eps * math.cos(yy) * ey, ey)
        logh += math.log(after) - math.log(before)
    return logh, perimeter


def log_HF_definicion(pts, F_en):
    """log H_F desde su definición: en cada nodo, |F e^-| / |F e^+|.

    F_en(p) devuelve la matriz 2x2 de deformación en el nodo p.
    No usa la reindexación de la prueba de C4-E1, así que la contrasta.
    """
    logh = 0.
    for i in range(4):
        p, pm, pp = pts[i], pts[i - 1], pts[(i + 1) % 4]
        em = (p[0] - pm[0], p[1] - pm[1])
        ep = (pp[0] - p[0], pp[1] - p[1])
        em = (em[0] / norm(em), em[1] / norm(em))
        ep = (ep[0] / norm(ep), ep[1] / norm(ep))
        F = F_en(p)
        a = math.hypot(F[0][0] * em[0] + F[0][1] * em[1], F[1][0] * em[0] + F[1][1] * em[1])
        b = math.hypot(F[0][0] * ep[0] + F[0][1] * ep[1], F[1][0] * ep[0] + F[1][1] * ep[1])
        logh += math.log(a) - math.log(b)
    return logh


def main():
    records=[]
    for h in [0.10,0.25,0.50,1.0,math.pi/2,2.0]:
        for U in [1.0, 1.7, -0.4]:
            actual=B_directa(h,U)
            expected=B_formula(h,U)
            assert math.isclose(actual,expected,rel_tol=2e-13,abs_tol=2e-14), (h,U,actual,expected)
            records.append({'h':h,'U':U,'derivada_4_nodos':actual,'formula_exacta':expected,'error_abs':abs(actual-expected)})
    # Testigo particular h = pi/2
    assert abs(B_formula(math.pi/2) + 2.0) < 1e-14
    rng=random.Random(SEED)
    rngF=random.Random(SEED+1)  # matrices uniformes; no altera la secuencia de cizalla
    count=250
    max_ratio=0.
    max_abs=0.
    max_reindex=0.
    max_uniforme=0.
    for i in range(count):
        # Paralelogramo no degenerado, con variación de escala y orientación
        h=rng.uniform(.02,1.1)
        ang=rng.uniform(-math.pi,math.pi)
        p=(rng.uniform(-.5,.5),rng.uniform(-.5,.5))
        v=(h*math.cos(ang),h*math.sin(ang))
        a=ang+rng.uniform(.3,2.7)
        w=(h*rng.uniform(.7,1.5)*math.cos(a),h*rng.uniform(.7,1.5)*math.sin(a))
        pts=[p,(p[0]+v[0],p[1]+v[1]),(p[0]+v[0]+w[0],p[1]+v[1]+w[1]),(p[0]+w[0],p[1]+w[1])]
        eps=rng.uniform(-.8,.8)
        actual,P0=monitor_cizalla(pts,eps)
        # ||D²Phi|| <= |eps|, ||F^{-1}|| <= 1+|eps|  => min singular >= 1/(1+|eps|).
        bound=P0*abs(eps)*(1+abs(eps))
        assert abs(actual) <= bound + 1e-12, (i,actual,bound)
        max_ratio=max(max_ratio, abs(actual)/bound if bound else 0.)
        max_abs=max(max_abs,abs(actual))
        # La forma reindexada de la prueba coincide con la definición nodo por nodo.
        directo=log_HF_definicion(pts,lambda q:[[1.,eps*math.cos(q[1])],[0.,1.]])
        assert math.isclose(actual,directo,rel_tol=1e-12,abs_tol=1e-13), (i,actual,directo)
        max_reindex=max(max_reindex,abs(actual-directo))
        # F uniforme (aleatoria e invertible): H_F = 1 por la definición.
        F=[[rngF.uniform(.3,2.),rngF.uniform(-1.,1.)],[rngF.uniform(-1.,1.),rngF.uniform(.3,2.)]]
        if abs(F[0][0]*F[1][1]-F[0][1]*F[1][0])<.05: F[0][0]+=1.
        uniforme=log_HF_definicion(pts,lambda q,F=F:F)
        assert abs(uniforme)<1e-12, (i,uniforme)
        max_uniforme=max(max_uniforme,abs(uniforme))
    # Control negativo: la prueba uniforme distingue una F que varía entre nodos.
    var=log_HF_definicion([(.1,.2),(1.,0.),(1.3,.9),(.2,1.1)],lambda q:[[1.,.5*math.cos(q[1])],[0.,1.]])
    assert abs(var)>1e-3, var
    result={
      'programa':'Endless Monkey Project — Relational Geometry Program',
      'id':'C4-E1/C4-E3',
      'fecha':'2026-11-10',
      'semilla':SEED,
      'estado':'PASS',
      'taylor_green':{'tests':len(records),'casos':records,'tipo':'sustitucion numerica en una identidad demostrada'},
      'cizalla':{'tests':count,'formula':'Phi=(x+eps sin y,y,z); K<=abs(eps); m>=1/(1+abs(eps))','razon_mayor_observada':max_ratio,'max_abs_log_h':max_abs,
                 'reindexacion_contra_definicion_max':max_reindex},
      'uniforme':{'tests':count,'resultado':'H_F=1 para F uniforme, calculado nodo por nodo desde la definicion','max_abs_log_h':max_uniforme,
                  'control_variable_log_h':var},
      'alcance':'controles finitos, no teorema de regularidad 3D ni cota a priori',
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open('w', encoding='utf-8', newline='\n') as out_file:
        out_file.write(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    print('PASS: Taylor–Green',len(records),'comprobaciones; cizalla',count,
          '(reindexación = definición, dif. máx. %.1e); F uniforme' % max_reindex,count,
          '(máx. |log H_F| = %.1e); control con F variable: log H_F = %.4f' % (max_uniforme,var))


if __name__=='__main__':main()
