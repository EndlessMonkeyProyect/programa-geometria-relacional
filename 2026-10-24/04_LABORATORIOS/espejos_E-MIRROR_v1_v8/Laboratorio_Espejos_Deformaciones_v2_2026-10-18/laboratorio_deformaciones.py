#!/usr/bin/env python3
"""Extensión E-MIRROR: perturbación angular, observabilidad y enfoque.

Submodelos separados:
 A: tres planos ideales infinitos que concurren en el origen; grupo abstracto
    de reflexiones, no el número de imágenes efectivamente visibles.
 B: dos vistas lineales calibradas de un punto 3D, proyecciones XY; profundidad
    recuperable y robustez numérica con incertidumbre.
 C: óptica de rayos 2D, incidencia paralela vertical, espejo parabólico y
    perturbación cuártica, sin difracción, tamaños 3D ni polarización.
"""
from __future__ import annotations
from fractions import Fraction
import argparse
import json
import math
import numpy as np

I = np.eye(3)
RX = np.diag([-1., 1., 1.])
RY = np.diag([1., -1., 1.])
PXY = np.array([[1.,0.,0.],[0.,1.,0.]])
P = np.array([0.4, 0.6, 0.8])

def reflection(normal):
    n = np.asarray(normal, dtype=float)
    n = n / np.linalg.norm(n)
    return I - 2 * np.outer(n,n)

def tilted_z(delta_deg):
    delta = math.radians(delta_deg)
    return reflection([math.sin(delta), 0, math.cos(delta)])

def rotation_order(delta_deg):
    """Para θ=(90-δ) grados, θ/180=a/b irreducible; (Rx Rθ)^b=I."""
    angle = Fraction(90) - Fraction(str(delta_deg))
    f = angle / 180
    return f.denominator

def dihedral_orbit(delta_deg, point=P):
    """Acción del grupo de 3 planos. Incluye y->-y, independiente de xz."""
    r = tilted_z(delta_deg)
    cyc = RX @ r
    order = rotation_order(delta_deg)
    imgs = []
    rot = np.eye(3)
    for i in range(order):
        for extra in (I, RX):
            for sy in (I, RY):
                imgs.append(tuple(np.round((sy @ extra @ rot) @ point, 9)))
        rot = rot @ cyc
    if not np.allclose(rot,I,atol=2e-10):
        raise AssertionError('El período algebraico no cerró numéricamente')
    return {'delta_grados':delta_deg, 'angulo_entre_dos_espejos_xz_grados':float(90-delta_deg),
            'orden_rotacion_2_reflexiones':order,'transformaciones':4*order,
            'posiciones_genericas_distintas':len(set(imgs)),
            'errores_acumulados_cierre':float(np.linalg.norm(rot-I,'fro'))}

def loop_deviation(delta_deg, point=P):
    r = tilted_z(delta_deg)
    loop = RX @ r @ RX @ r
    cosang = max(-1.0, min(1.0, (float(np.trace(loop)) - 1.)/2.))
    angle = math.degrees(math.acos(cosang))
    displacement = np.linalg.norm(loop @ point - point)
    # reconstrucción exacta vía inversa conocida de cada reflejo
    rec = r.T @ (r @ point)
    return {'delta_grados':delta_deg,
            'angulo_lazo_cuatro_reflexiones_grados':angle,
            'distancia_entre_fuente_e_imagen_tras_lazo_m':float(displacement),
            'error_al_invertir_reflejo_calibrado_m':float(np.linalg.norm(rec-point)),
            'modulo_determinante_cada_reflejo':round(float(np.linalg.det(r))),
            'error_ortogonalidad':float(np.linalg.norm(r.T @ r-I,'fro'))}

def observability(delta_deg, noise=0.01, source=P):
    r=tilted_z(delta_deg)
    A=np.vstack([PXY, PXY @ r])
    s=np.linalg.svd(A,compute_uv=False)
    rank=int(np.sum(s > 1e-10))
    condition = (float(s[0]/s[-1]) if rank == 3 else None)
    # dos observaciones calibradas, fuente única solo si rango completo
    exact=np.concatenate([PXY@source, PXY@r@source])
    perturbation=np.array([0.,0.,noise,0.])
    estimated=np.linalg.lstsq(A,exact+perturbation,rcond=None)[0]
    return {'delta_grados':delta_deg, 'rango':rank,
            'valores_singulares': [float(t) for t in s],
            'condicion_2':condition,'ruido_solo_x_reflejada_m':noise,
            'fuente_real_m':source.tolist(),
            'fuente_estimada_con_ruido_m':estimated.tolist(),
            'error_estimacion_m':float(np.linalg.norm(estimated-source)),
            'error_profundidad_z_m':float(estimated[2]-source[2]),
            'nota': ('sin unicidad en z; la pseudoinversa escoge una solución' if rank<3 else
                     'inversa única en ausencia de ruido y con reflejo calibrado')}

def opacity_observability(delta_deg, transmission, noise=0.01, source=P):
    """Filtrar canal horizontal de imagen reflejada por transmisión tau.
    El ruido aditivo NO baja con tau: modelo de capacidad de distinción.
    """
    r=tilted_z(delta_deg)
    filt=np.diag([transmission,1.])
    A=np.vstack([PXY, filt @ PXY @ r])
    singulars=np.linalg.svd(A,compute_uv=False)
    rank=int(np.sum(singulars > 1e-10))
    observation=A@source
    obs_noise=np.array([0.,0.,noise,0.])
    est=np.linalg.lstsq(A,observation+obs_noise,rcond=None)[0]
    return {'inclinacion_grados':delta_deg,'transmision':transmission,
            'rango':rank,'numero_condicion':float(singulars[0]/singulars[-1]) if rank==3 else None,
            'error_z_m':float(est[2]-source[2]),
            'nota':'Ruido instrumental fijo después del filtro; transparencia positiva no asegura robustez.'}

def parabola_profile(x,f,epsilon,a):
    y=x*x/(4*f) + epsilon*x**4/(4*f*a*a)
    dy=x/(2*f) + epsilon*x**3/(f*a*a)
    return y,dy

def sphere_profile(x,f):
    R=2*f
    y=R-math.sqrt(R*R-x*x)
    dy=x/math.sqrt(R*R-x*x)
    return y,dy

def focus_axis_intercepts(profile, f=1., aperture=.6, sample=80):
    """Rayos verticales entrantes (0,-1). Calcular intersecciones x=0 tras reflexión.
    Rechaza centro exacto porque rayo sobre eje cruza infinitos puntos del eje.
    """
    xs=np.linspace(-aperture, aperture, sample+1)
    xs=xs[abs(xs)>1e-12]
    ys=[]
    for x in xs:
        y, dy=profile(float(x))
        n=np.array([-dy,1.]); n/=np.linalg.norm(n)
        inc=np.array([0., -1.])
        out=inc-2*np.dot(inc,n)*n
        t=-x/out[0]
        if t < 0:
            raise AssertionError('Rayo reflejado no intersecta eje en dirección de avance')
        ys.append(y+t*out[1])
    ys=np.array(ys)
    return {'n_rayos':len(ys), 'foco_nominal_m':f,
            'interseccion_minima_m':float(np.min(ys)),
            'interseccion_maxima_m':float(np.max(ys)),
            'interseccion_promedio_m':float(np.mean(ys)),
            'desviacion_estandar_de_intersecciones_m':float(np.std(ys)),
            'max_desviacion_del_foco_nominal_m':float(np.max(abs(ys-f))),
            'intersecciones_m':ys.tolist()}

def curved_profile_results():
    out=[]
    f=1.0; a=.6
    for eps in [0., .005, .01, .03, .05]:
        dat=focus_axis_intercepts(lambda x:parabola_profile(x,f,eps,a),f,a)
        dat['modelo']='parabola_perturbacion_cuartica';dat['epsilon']=eps
        out.append(dat)
    dat=focus_axis_intercepts(lambda x:sphere_profile(x,f),f,a)
    dat['modelo']='esfera_radio_2f';dat['epsilon']=None
    out.append(dat)
    return out

def run():
    return {
      'metadatos':{
          'titulo':'E-MIRROR deformaciones v2',
          'fecha':'2026-10-18',
          'tipo':'simulaciones numéricas reproducibles de tres submodelos delimitados',
          'fuente_m':P.tolist(), 'unidades':'m y grados',
          'limites':'no cuenta rayos físicamente visibles ni demuestra afirmaciones ontológicas'},
      'A_deformacion_de_lazos': [loop_deviation(d) for d in [0., .5,1.,2.,5.,15.]],
      'B_orden_grupo_perturbado': [dihedral_orbit(d) for d in [0.,.5,1.,2.,5.]],
      'C_observabilidad': [observability(d) for d in [0., .1, .5, 1., 2., 5., 15., 45.]],
      'D_enfoque_de_curvaturas': curved_profile_results(),
      'E_opacidad_y_perdida_de_rango':[opacity_observability(5.,t) for t in [1.,.2,.05,0.]]
    }

def figures(data,output_prefix):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    obs=data['C_observabilidad']
    xs=[d['delta_grados'] for d in obs if d['delta_grados']>0]
    ys=[abs(d['error_profundidad_z_m']) for d in obs if d['delta_grados']>0]
    fig,ax=plt.subplots(figsize=(8,5))
    ax.plot(xs,ys,marker='o')
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_xlabel('Inclinación δ del espejo (grados)')
    ax.set_ylabel('Error absoluto de profundidad (m)')
    ax.set_title('Dos vistas XY y ruido fijo de 0,01 m')
    ax.grid(True,which='both',alpha=.3)
    fig.tight_layout()
    fig.savefig(output_prefix+'_observabilidad.png',dpi=170)
    plt.close(fig)
    curved=data['D_enfoque_de_curvaturas']
    fig,ax=plt.subplots(figsize=(8,5))
    curves=[r for r in curved if r['modelo']=='parabola_perturbacion_cuartica']
    ax.plot([d['epsilon'] for d in curves],
             [1000*d['desviacion_estandar_de_intersecciones_m'] for d in curves],marker='o')
    ax.set_xlabel('Perturbación cuártica relativa ε')
    ax.set_ylabel('Dispersión del foco sobre el eje (mm)')
    ax.set_title('Rayos paralelos, espejo parabólico deformado')
    ax.grid(True,alpha=.3)
    fig.tight_layout()
    fig.savefig(output_prefix+'_enfoque.png',dpi=170)
    plt.close(fig)

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--salida',default='resultados_v2.json')
    ap.add_argument('--figuras-prefijo',default='figura')
    args=ap.parse_args()
    data=run()
    with open(args.salida,'w',encoding='utf8') as f:
        json.dump(data,f,ensure_ascii=False,sort_keys=True,indent=2)
        f.write('\n')
    figures(data,args.figuras_prefijo)
    print('OK:',args.salida)
