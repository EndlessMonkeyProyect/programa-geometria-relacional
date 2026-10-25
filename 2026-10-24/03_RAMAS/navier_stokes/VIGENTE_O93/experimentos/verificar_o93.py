#!/usr/bin/env python3
"""O93 / Programa de Geometría Relacional: comprobaciones exactas reproducibles.

Las comprobaciones algebraicas no son un teorema automático sobre todos los
flujos 3D. El certificado O84 reproduce fórmulas analíticas del expediente.
Requiere sympy, numpy, mpmath; opcional matplotlib para figuras numéricas.
"""
import csv
import json
import math
from pathlib import Path
import argparse
import sympy as sp
import mpmath as mp
import numpy as np

I = sp.I

def to_float(x): return float(sp.N(x, 17))
def vec_conj(x): return x.applyfunc(sp.conjugate)
def dot(x, y): return (x.T*y)[0]

def add_mode(dic, k, v, amplitude, trig):
    k = tuple(k)
    for sign in (+1, -1):
        kk = tuple(sign*x for x in k)
        factor = sp.Rational(amplitude, 2) if trig == 'cos' else sign * amplitude / (2*I)
        term = factor * sp.Matrix(v)
        dic[kk] = dic.get(kk, sp.zeros(3,1)) + term

def o86_fourier(c=1):
    u = {}
    add_mode(u, (1,0,0), (0,1,0), sp.S.One, 'cos')
    add_mode(u, (0,1,1), (1,0,0), sp.S.One, 'cos')
    add_mode(u, (1,1,1), (1,1,-2), sp.S(c), 'sin')
    add_mode(u, (0,0,1), (1,0,0), sp.Rational(1,3), 'cos')
    return u

def field_invariants(u):
    kinetic = ens = pal = sp.S.Zero
    omega = {}; strain = {}
    for k, v in u.items():
        kval = sp.Matrix(k)
        assert sp.simplify(dot(kval,v)) == 0
        norm2 = sp.simplify(dot(vec_conj(v), v))
        n2 = sum(x*x for x in k)
        kinetic += norm2
        ens += n2 * norm2
        pal += n2*n2 * norm2
        omega[k] = I*kval.cross(v)
        strain[k] = I*(v*kval.T+kval*v.T)/2
    P = sp.S.Zero
    for ka, wa in omega.items():
        for kb, wb in omega.items():
            ks = tuple(-ka[j]-kb[j] for j in range(3))
            if ks in strain:
                P += dot(wa, strain[ks]*wb)
    kinetic,ens,pal,P = [sp.simplify(x) for x in (kinetic,ens,pal,P)]
    return {'M2':kinetic,'W':ens,'B':pal,'P':P}

def circuito():
    C3 = [(0,1),(1,2),(2,0)]
    C4 = [(0,1),(1,2),(2,3),(3,0)]
    K4 = [(i,j) for i in range(4) for j in range(i+1,4)]
    def unsign_inc(edges,n):
        Q=sp.zeros(len(edges),n)
        for row,(a,b) in enumerate(edges):Q[row,a]=1;Q[row,b]=1
        return Q
    out={}
    for nm, edges, n, expected in [('C3',C3,3,0),('C4',C4,4,1),('K4',K4,4,0)]:
        Q=unsign_inc(edges,n)
        ker=Q.nullspace()
        assert len(ker)==expected
        out[nm]={'vertices':n,'aristas':len(edges),'rango':Q.rank(),'dimension_nucleo':len(ker),
                 'generadores':[[str(v) for v in x] for x in ker]}
    assert unsign_inc(C4,4)*sp.Matrix([1,-1,1,-1])==sp.zeros(4,1)
    return out

def holonomia():
    radii=[sp.Rational(1,2),sp.Integer(2),sp.Integer(3),sp.Rational(5,2)]
    H=sp.prod(radii[j]/radii[(j+1)%4] for j in range(4))
    assert sp.simplify(H-1)==0
    r_alt=[r*sp.Rational(7,3) for r in radii]
    H2=sp.prod(r_alt[j]/r_alt[(j+1)%4] for j in range(4))
    assert H2==1
    unequal=H*sp.Rational(11,10)
    assert unequal != 1
    return {'H_radii_variables':str(H),'H_reescalado':str(H2),'H_asimetrico':str(unequal),
            'nota':'Compatibilidad instantanea ideal; no se prueba ley NS.'}

def prueba_fase():
    nu=sp.Rational(1,100)
    vals={}
    for nm,c in [('mas',1),('menos',-1)]:
        z=field_invariants(o86_fourier(c))
        assert z['W']==sp.Rational(95,9)
        assert z['B']==sp.Rational(266,9)
        assert z['P']==sp.Rational(3*c,4)
        assert z['M2']>0
        M=sp.sqrt(z['M2'])
        D=sp.simplify(z['W']/z['M2'])
        D2=sp.simplify(z['B']/z['M2'])
        T=sp.simplify(z['P']/M**3)
        Gamma=sp.simplify(z['P']/(nu*z['B']))
        assert sp.simplify((M**2)*D-z['W']) == 0
        assert sp.simplify((M**2)*D2-z['B']) == 0
        assert sp.simplify((M**3)*T-z['P']) == 0
        assert sp.simplify(M**3*T-nu*M**2*D2-(z['P']-nu*z['B'])) == 0
        vals[nm]={x:str(y) for x,y in z.items()}
        vals[nm].update({'D':str(D),'D2':str(D2),'T':str(T),'Gamma_nu':str(Gamma),
                          'W_derivada_inicial':str(2*(z['P']-nu*z['B']))})
    assert vals['mas']['W']==vals['menos']['W'] and vals['mas']['B']==vals['menos']['B']
    assert vals['mas']['P']!=vals['menos']['P']
    return vals

def ondas_exactas(outdir):
    nu=0.12
    ks=np.array([1,2,3,4],dtype=float)
    amps=np.array([1.0,0.35,0.15,0.08],dtype=float)
    rows=[]
    for t in np.linspace(0,1,51):
        a=amps*np.exp(-nu*ks**2*t)
        W=np.sum(ks**2*a**2)/2
        B=np.sum(ks**4*a**2)/2
        M2=np.sum(a*a)/2
        D=W/M2; D2=B/M2
        # Para la solución exacta de cizalla B(z,z)=0: no hay transferencia.
        dD_direct=-2*nu*(D2-D**2)
        # Cociente Q=W/B y ley de varianza de O78
        Q=B/W
        numerator=np.sum(ks**6*a**2)/2
        var= numerator/W - (B/W)**2
        dQ=-2*nu*var
        assert D2-D*D>=-1e-12
        assert dD_direct<=1e-12
        assert dQ<=1e-12
        rows.append(dict(t=float(t),M=float(np.sqrt(M2)),W=float(W),B=float(B),D=float(D),
                         D2=float(D2),derivada_D=float(dD_direct),Q_vorticidad=float(Q),
                         derivada_Q=float(dQ),Gamma_nu=0.0))
    with open(outdir/'ondas_exactas.csv','w',newline='',encoding='utf8') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    return {'n_tiempos':len(rows),'D_inicial':rows[0]['D'], 'D_final':rows[-1]['D'],
            'Q_inicial':rows[0]['Q_vorticidad'],'Q_final':rows[-1]['Q_vorticidad'],
            'comprobacion':'onda de cizalla exacta, sin transferencia ni integracion aproximada de PDE'}

def presupuesto_o84():
    mp.mp.dps=65
    nu=mp.mpf(1); L=mp.mpf(6); K=mp.mpf(9); d=mp.mpf(9)/500
    G0=2*L**2*(1-mp.exp(-2*d))
    M0=K/(4*L**2*mp.sqrt(2))*mp.expm1(G0)
    M1=mp.exp(4*d*(L+K*d)**2)*(L*K*d**2+K**2*d**3/3)
    assert M0 > mp.mpf('0.5') and M1 < mp.mpf('0.5')
    assert M0 > mp.mpf('0.5191') and M1 < mp.mpf('0.282456')
    return {'nu':1,'A':4,'B':1,'C':1,'delta':'9/500',
            'M0':mp.nstr(M0,22),'cota_M1':mp.nstr(M1,22),
            'certificado_inicial':False,'certificado_actualizado':True,
            'alcance':'Verifica las formulas y comparaciones analiticas de O84 en un intervalo: NO una regularidad general.'}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',default=str(Path(__file__).resolve().parent/'resultados'))
    args=parser.parse_args(); dest=Path(args.out);dest.mkdir(parents=True,exist_ok=True)
    results={'titulo':'O93 — auditoria reproducible de resultados O72/O74/O78/O84/O86/O92',
       'contrato':'T^3, ν>0, fuerza 0, campos solenoidales suaves; experimentos auxiliares bajo contratos particulares',
       'E1_circuitos':circuito(), 'E2_holonomia':holonomia(),
       'E3_polarizacion_de_fase':prueba_fase(), 'E4_ondas_exactas':ondas_exactas(dest),
       'E5_presupuesto_O84':presupuesto_o84(),
       'total':5, 'estado':'PASA, comprobaciones independientes algebraicas y cuantitativas de las formulas seleccionadas'}
    (dest/'verificacion_exacta.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps(results,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
