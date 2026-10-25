#!/usr/bin/env python3
"""E6. Galerkin Fourier 3D sin forzamiento, verificación adicional O86.

Método: pseudosespectral, proyección de Leray, filtro 2/3, RK4.
Las comparaciones N=16/24 y dt=0.004/0.002 controlan sensibilidad,
NO son una demostración de convergencia de la PDE en el continuo.
"""
import argparse
import csv
import json
import math
from pathlib import Path
import numpy as np


def setup(n):
    freq=np.fft.fftfreq(n,d=1/n)
    K=np.meshgrid(freq,freq,freq,indexing='ij')
    k=np.array(K)
    kk=np.sum(k*k,axis=0)
    mask=(np.abs(k[0])<n/3)&(np.abs(k[1])<n/3)&(np.abs(k[2])<n/3)
    return k,kk,mask

def initial(n,c):
    grid=(2*np.pi/n)*np.arange(n)
    x,y,z=np.meshgrid(grid,grid,grid,indexing='ij')
    m=x+y+z
    u=np.zeros((3,n,n,n),dtype=np.float64)
    u[0]=np.cos(y+z)+c*np.sin(m)+np.cos(z)/3
    u[1]=np.cos(x)+c*np.sin(m)
    u[2]=-2*c*np.sin(m)
    return np.fft.fftn(u,axes=(1,2,3))

def invariant(uh,k,kk,n,nu):
    # Parseval de la vorticidad para un campo exactamente solenoidal.
    mag2=np.sum(abs(uh)**2,axis=0)/n**6
    W=float(np.sum(kk*mag2).real)
    B=float(np.sum(kk*kk*mag2).real)
    return W,B

def solve(n,dt,T,c,nu=.01):
    k,kk,mask=setup(n)
    mask=mask[None,:,:,:]
    uh=initial(n,c)*mask
    invkk=np.zeros_like(kk)
    invkk[kk>0]=1/kk[kk>0]
    def rhs(a):
        a=a*mask
        u=np.fft.ifftn(a,axes=(1,2,3)).real
        na=np.zeros_like(u)
        for comp in range(3):
            for axis in range(3):
                derivative=np.fft.ifftn(1j*k[axis]*a[comp],axes=(0,1,2)).real
                na[comp]+=u[axis]*derivative
        Nhat=np.fft.fftn(na,axes=(1,2,3))
        kdot=np.sum(k*Nhat,axis=0)
        projected=Nhat-k*(kdot*invkk)[None,:,:,:]
        return (-projected-nu*kk[None,:,:,:]*a)*mask
    # Derivada instantánea de W calculada directamente del generador Galerkin.
    initial_rhs=rhs(uh)
    wprime=float(2*np.sum(kk*np.real(np.sum(np.conj(uh)*initial_rhs,axis=0)))/n**6)
    expected=2*(.75*c-nu*266/9)
    assert abs(wprime-expected)<1e-10, (n,c,wprime,expected)
    t=0.;rows=[]
    count=round(T/dt)
    assert abs(count*dt-T)<1e-12
    for j in range(count+1):
        W,B=invariant(uh,k,kk,n,nu)
        if j==0 or j%max(1,count//25)==0 or j==count:
            rows.append({'t':round(t,10),'W':W,'B':B,'n':n,'dt':dt,'fase':c})
        if j<count:
            k1=rhs(uh); k2=rhs(uh+.5*dt*k1);k3=rhs(uh+.5*dt*k2);k4=rhs(uh+dt*k3)
            uh=(uh+dt*(k1+2*k2+2*k3+k4)/6)*mask
            t+=dt
    return rows,wprime

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',default=str(Path(__file__).resolve().parent/'resultados'))
    ap.add_argument('--T',type=float,default=.08)
    args=ap.parse_args(); d=Path(args.out);d.mkdir(parents=True,exist_ok=True)
    allrows=[];result={}
    for n,dt in [(16,.004),(24,.004),(24,.002)]:
        for phase in [1,-1]:
            run,wprime=solve(n,dt,args.T,phase)
            allrows.extend(run)
            key=f'N{n}_dt{dt}_fase{phase:+d}'
            result[key]={'inicial_W':run[0]['W'],'final_W':run[-1]['W'],
                         'inicial_B':run[0]['B'],'derivada_W_inicial':wprime,'n_puntos':len(run)}
            assert abs(run[0]['W']-95/9)<1e-12
            assert abs(run[0]['B']-266/9)<1e-12
            print(key,'W(T)=',run[-1]['W'])
    with open(d/'galerkin_evolucion.csv','w',newline='',encoding='utf8') as f:
        w=csv.DictWriter(f,fieldnames=['t','W','B','n','dt','fase']);w.writeheader();w.writerows(allrows)
    (d/'galerkin_resumen.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    # Control de resolución y de paso temporal sobre enstrofía final.
    for phase in (1,-1):
        l=lambda n,dt:result[f'N{n}_dt{dt}_fase{phase:+d}']['final_W']
        print('fase',phase,'dif_N',abs(l(16,.004)-l(24,.004)),
              'dif_dt',abs(l(24,.004)-l(24,.002)))
    if __import__('importlib').util.find_spec('matplotlib'):
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        for phase in (1,-1):
            rows=[r for r in allrows if r['n']==24 and r['dt']==.002 and r['fase']==phase]
            plt.plot([r['t'] for r in rows],[r['W'] for r in rows],label='fase + (P>0)' if phase==1 else 'fase − (P<0)')
        plt.title('O93 · Navier–Stokes 3D Galerkin: dos fases iniciales')
        plt.xlabel('Tiempo');plt.ylabel('Enstrofía W(t)');plt.legend();plt.grid(alpha=.2)
        fig=Path(args.out).parent.parent/'figuras'/'galerkin_fases.png';fig.parent.mkdir(parents=True,exist_ok=True)
        plt.savefig(fig,dpi=160,bbox_inches='tight');plt.close()
    print('Control inicial exacto: W=95/9 y B=266/9; derivadas exactas O86:',
          'W\'(+)=2*(3/4-(266/9)*.01), W\'(-)=2*(-3/4-(266/9)*.01)')

if __name__=='__main__':main()
