#!/usr/bin/env python3
"""Laboratorio E-MIRROR v3: trazador 3D vectorizado de paneles finitos.

Modelo: habitación cúbica [-1,1]^3, cinco paneles especulares centrales
sobre paredes opacas, y un panel x+ insertado en x=0.90 que puede inclinarse
o curvarse. Los rayos parten de cámara omnidireccional y se propagan hacia
una fuente esférica luminosa; solo se registran trayectorias físicamente
válidas, con apertura, oclusión, umbral de sensor y hasta max_bounces.

No representa interferencia, óptica ondulatoria, polarización o un humano real.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np

FACES = ('X-', 'X+', 'Y-', 'Y+', 'Z-', 'Z+')
NORMALS = np.array([[-1.,0,0],[1.,0,0],[0,-1.,0],[0,1.,0],[0,0,-1.],[0,0,1.]])
CAM = np.array([.12,-.22,.19])
SOURCE = np.array([-.37,.28,.11])
SOURCE_RADIUS = .115
WALL = 1.0
PANEL_HALF = .90
EPS = 1.e-7


def camera_directions(w=520,h=260):
    lon=(np.arange(w)+.5)/w*(2*np.pi)-np.pi
    lat=np.pi/2-(np.arange(h)+.5)/h*np.pi
    d=np.stack(np.broadcast_arrays(np.cos(lat)[:,None]*np.cos(lon)[None,:],
         np.cos(lat)[:,None]*np.sin(lon)[None,:], np.sin(lat)[:,None]*np.ones((1,w))),axis=-1)
    return d.reshape(-1,3)


def pinhole_directions(w=420,h=280,front=(1.,0.,0.),fov_horizontal_deg=90.):
    """Cámara pinhole orientada a una dirección, campo horizontal conocido."""
    forward=np.asarray(front,dtype=float);forward/=np.linalg.norm(forward)
    up=np.array([0.,0.,1.])
    if abs(np.dot(up,forward))>.97:up=np.array([0.,1.,0.])
    right=np.cross(forward,up);right/=np.linalg.norm(right)
    up=np.cross(right,forward);up/=np.linalg.norm(up)
    tanh=np.tan(np.radians(fov_horizontal_deg)/2)
    xv=(np.arange(w)+.5-w/2)/(w/2)*tanh
    yv=(h/2-np.arange(h)-.5)/(h/2)*tanh*(h/w)
    D=forward[None,None,:] + xv[None,:,None]*right[None,None,:] + yv[:,None,None]*up[None,None,:]
    return (D/np.linalg.norm(D,axis=2,keepdims=True)).reshape((-1,3))


def sphere_dist(o,d,center=SOURCE,radius=SOURCE_RADIUS):
    oc=o-center
    b=np.einsum('ij,ij->i',oc,d)
    c=np.einsum('ij,ij->i',oc,oc)-radius**2
    dis=b*b-c
    root=np.sqrt(np.maximum(dis,0))
    t=-b-root
    t=np.where((dis>=0)&(t>EPS),t,np.inf)
    return t


def main_mirror_t(o,d,tilt_deg=0.,curve=0.):
    # Intersección con x=0.90+tan(δ)y−κ(y²+z²); bounded |y|,|z|<=PANEL_HALF
    a=math.tan(math.radians(tilt_deg)); k=float(curve)
    A=k*(d[:,1]**2+d[:,2]**2)
    B=d[:,0]-a*d[:,1]+2*k*(o[:,1]*d[:,1]+o[:,2]*d[:,2])
    C=o[:,0]-.90-a*o[:,1]+k*(o[:,1]**2+o[:,2]**2)
    if abs(k)<1e-15:
        with np.errstate(divide='ignore', invalid='ignore'):
            t=-C/B
    else:
        disc=B*B-4*A*C
        sq=np.sqrt(np.maximum(0,disc))
        with np.errstate(divide='ignore',invalid='ignore'):
            t1=(-B-sq)/(2*A);t2=(-B+sq)/(2*A)
            t=np.where((t1>EPS)&(disc>=0),t1,np.where((t2>EPS)&(disc>=0),t2,np.inf))
            linear=-C/B
            t=np.where(abs(A)<1e-14,linear,t)
        t=np.where(disc>=0,t,np.inf)
    t_safe=np.where(np.isfinite(t),t,0.)
    hit=o+t_safe[:,None]*d
    # cara reflectante únicamente vista desde el interior (dot(d,normal)>0)
    n=np.stack([np.ones(len(t)), -a+2*k*hit[:,1],2*k*hit[:,2]],axis=1)
    n=n/np.linalg.norm(n,axis=1)[:,None]
    valid=(t>EPS)&np.isfinite(t)&(abs(hit[:,1])<=PANEL_HALF)&(abs(hit[:,2])<=PANEL_HALF)
    return np.where(valid,t,np.inf),n


def boundary_t(o,d):
    # Calcular próxima intersección en los 6 planos de paredes opacas.
    # Caso X+ actúa solo como pared opaca detrás del panel adelantado.
    out=np.full((len(o),6),np.inf)
    for axis in range(3):
        for sign_idx,sgn in enumerate((-1,1)):
            j=axis*2+sign_idx
            with np.errstate(divide='ignore',invalid='ignore'):
                t=(sgn-o[:,axis])/d[:,axis]
            h=o+np.where(np.isfinite(t),t,0.)[:,None]*d
            other=[a for a in range(3) if a != axis]
            ok=(t>EPS)&np.isfinite(t)&(np.abs(h[:,other[0]])<=1+1.e-8)&(np.abs(h[:,other[1]])<=1+1.e-8)
            out[:,j]=np.where(ok,t,np.inf)
    return out


def trace(w=520,h=260,max_bounces=6,tilt_deg=0,curve=0,
          reflectivity=.91,transmit_plus=1., min_signal=.07,
          view='panorama', front=(1.,0.,0.),fov_horizontal_deg=90.):
    directions=(camera_directions(w,h) if view=='panorama' else
                pinhole_directions(w,h,front,fov_horizontal_deg))
    n=len(directions)
    o=np.broadcast_to(CAM,(n,3)).copy()
    d=directions.copy()
    active=np.ones(n,dtype=bool)
    intensity=np.ones(n)
    bounce_count=np.zeros(n,dtype=np.int16)
    signatures=np.zeros(n,dtype=np.int64)
    reached=np.zeros(n,dtype=bool)
    last_origins=np.zeros((n,3))
    last_directions=np.zeros((n,3))
    last_path=np.full(n,np.inf)
    aperture_losses=np.zeros(n,dtype=bool)
    intensity_losses=np.zeros(n,dtype=bool)
    max_depth_losses=np.zeros(n,dtype=bool)
    pathway_count=np.zeros(max_bounces+1,dtype=int)
    for depth in range(max_bounces+1):
        idx=np.where(active)[0]
        if not len(idx):break
        O=o[idx];D=d[idx]
        ts=sphere_dist(O,D)
        tb=boundary_t(O,D)
        tm,nm=main_mirror_t(O,D,tilt_deg,curve)
        tbmin=np.min(tb,axis=1)
        wallidx=np.argmin(tb,axis=1)
        usepane=tm<tbmin
        tbar=np.minimum(tm,tbmin)
        hit_source=ts<tbar
        src_idx=idx[hit_source]
        reached[src_idx]=True
        last_origins[src_idx]=O[hit_source]
        last_directions[src_idx]=D[hit_source]
        last_path[src_idx]=ts[hit_source]
        pathway_count[depth]=len(src_idx)
        if depth==max_bounces:
            rest=idx[~hit_source]
            max_depth_losses[rest]=True
            active[idx]=False
            break
        rest=~hit_source
        ix=idx[rest]
        if not len(ix):
            active[idx]=False
            continue
        t=tbar[rest]
        widx=wallidx[rest]
        pane=usepane[rest]
        points=O[rest]+t[:,None]*D[rest]
        ns=NORMALS[widx].copy()
        ns[pane]=nm[rest][pane]
        # El panel avanzado tiene índice 1; la pared opaca X+ no refleja
        face=np.where(pane,1,widx)
        # Mirror stencil para cada pared salvo X+; x+ separado
        mirror=np.full(len(ix),False)
        for j in [0,2,3,4,5]:
            mask=(~pane)&(widx==j)
            if np.any(mask):
                other=[a for a in range(3) if a != j//2]
                mirror[mask]=(np.abs(points[mask][:,other[0]])<=PANEL_HALF)&(np.abs(points[mask][:,other[1]])<=PANEL_HALF)
        # El dorso del panel adelantado es opaco, no reflectante.
        mirror[pane]=np.einsum('ij,ij->i',D[rest][pane],ns[pane])>1.e-8
        next_intensity=intensity[ix]*reflectivity*np.where(pane,transmit_plus,1.)
        too_dim=next_intensity<min_signal
        light_reachable=mirror & ~too_dim & np.isfinite(t)
        losses=ix[~light_reachable]
        aperture_losses[losses]=~mirror[~light_reachable]
        intensity_losses[losses]=too_dim[~light_reachable]&mirror[~light_reachable]
        follow=ix[light_reachable]
        ff=face[light_reachable]
        bounce_count[follow]+=1
        signatures[follow]=7*signatures[follow]+(ff+1)
        unitn=ns[light_reachable]
        v=D[rest][light_reachable]
        reflected=v-2*np.sum(v*unitn,axis=1)[:,None]*unitn
        o[follow]=points[light_reachable]+EPS*reflected
        d[follow]=reflected
        intensity[follow]=next_intensity[light_reachable]
        active[idx]=False
        active[follow]=True
    visible_signatures,counts=np.unique(signatures[reached],return_counts=True)
    pathways=sorted(zip(visible_signatures.tolist(),counts.tolist()), key=lambda x:(-x[1],x[0]))
    # grupos de rayos válidos como pruebas de visibilidad; mínimo 8 píxeles
    strong=[(int(p),int(c)) for p,c in pathways if c>=8]
    # Recons.: líneas calibradas de tramo final; solo usa rayos detectados (esfera finita)
    reconstruction={}
    for mode in ['all','reflected_only']:
        inds=np.where(reached&(bounce_count>0 if mode=='reflected_only' else np.ones(n,dtype=bool)))[0]
        if not len(inds):
            reconstruction[mode]={'n_rayos':0,'identificable':False}
            continue
        # muestreo determinista para estabilidad y evitar sesgo de rayos densos
        if len(inds)>12000:inds=inds[np.linspace(0,len(inds)-1,12000).astype(int)]
        dirs=last_directions[inds]; pos=last_origins[inds]
        mats=np.eye(3)[None,:,:]-dirs[:,:,None]*dirs[:,None,:]
        A=np.sum(mats,axis=0); bb=np.sum(np.einsum('ijk,ik->ij',mats,pos),axis=0)
        eig=np.linalg.eigvalsh(A)
        if eig[0]/eig[-1] > 1.e-8:
            sol=np.linalg.solve(A,bb)
            err=float(np.linalg.norm(sol-SOURCE))
            rms=float(np.sqrt(np.mean(np.sum(np.cross(pos-sol,dirs)**2,axis=1))))
        else:sol=np.full(3,np.nan);err=None;rms=None
        reconstruction[mode]={'n_rayos':int(len(inds)),'rango':int(np.count_nonzero(eig>1.e-8*eig[-1])),
                 'valor_singular_min_matriz':float(eig[0]),'condicion':float(eig[-1]/eig[0]) if eig[0]>0 else None,
                 'fuente_estimada_m': [float(x) for x in sol] if err is not None else None,
                 'error_posicion_m':err,'rms_distancia_a_rectas_m':rms,'identificable':err is not None}
    # region ~ unique signatures count; a signature can cover several disconnected patches
    return {'configuracion':{'ancho':w,'alto':h,'max_rebotes':max_bounces,'inclinacion_grados':tilt_deg,
             'curvatura_m_inv':curve,'reflectividad':reflectivity,'transmision_panel_x_plus':transmit_plus,
             'umbral_sensor':min_signal,'apertura_semiancho_m':PANEL_HALF,'camara_m':CAM.tolist(),
             'fuente_m':SOURCE.tolist(),'radio_fuente_m':SOURCE_RADIUS,'tipo_camara':view,'orientacion':list(front), 'campo_horizontal_grados':fov_horizontal_deg if view !='panorama' else 360},
            'rayos_camara':n,'pixeles_con_fuente':int(sum(reached)),
            'pixel_porcentaje':float(np.mean(reached)*100),'rayos_por_numero_rebotes':pathway_count.tolist(),
            'trayectorias_distintas_con_fuente':len(pathways),'trayectorias_robustas_8pix':len(strong),
            'trayectorias_robustas_principales': [{'codigo_base_7':int(p),'n_pixeles':int(c)} for p,c in strong[:20]],
            'rayos_bloqueados_paneles':int(aperture_losses.sum()),'rayos_filtrados_sensor':int(intensity_losses.sum()),
            'rayos_fin_horizonte':int(max_depth_losses.sum()),'reconstruccion_calibrada':reconstruction,
            '_img':intensity.reshape(h,w)*reached.reshape(h,w),
            '_depth':np.where(reached,bounce_count,-1).reshape(h,w),
            '_sig':np.where(reached,signatures,-1).reshape(h,w)}


def clean(d):
    return {k: v for k,v in d.items() if not k.startswith('_')}


def run_experiments(w=520,h=260,depth=6):
    scen=[('simetrico',0.,0.,1.),('inclinacion_1',1.,0.,1.),
          ('inclinacion_3',3.,0.,1.),('inclinacion_5',5.,0.,1.),
          ('curvatura_002',0.,.02,1.),('curvatura_006',0.,.06,1.),
          ('inclinacion_3_opacidad_025',3.,0.,.25),
          ('inclinacion_3_opacidad_000',3.,0.,0.)]
    res={}
    for name,t,k,trans in scen:
        res[name]=trace(w=w,h=h,max_bounces=depth,tilt_deg=t,curve=k,transmit_plus=trans)
        print(name, 'fuente visible(px)=',res[name]['pixeles_con_fuente'],'rutas>=8px=',res[name]['trayectorias_robustas_8pix'],flush=True)
    return res


def make_figures(out,folder):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import Normalize
    names=['simetrico','inclinacion_1','inclinacion_3','inclinacion_5',
           'curvatura_002','curvatura_006','inclinacion_3_opacidad_025','inclinacion_3_opacidad_000']
    fig,axes=plt.subplots(4,2,figsize=(13,11),sharex=True,sharey=True)
    for ax,name in zip(axes.flat,names):
        v=out[name]
        ax.imshow(v['_img'], origin='upper',extent=(-180,180,-90,90),cmap='gray',vmin=0,vmax=1,aspect='auto')
        ax.set_title(name.replace('_',' ')+' · rutas: '+str(v['trayectorias_robustas_8pix']),fontsize=10)
        ax.set_ylabel('Elevación (°)')
    for ax in axes[-1,:]:ax.set_xlabel('Azimut (°)')
    fig.suptitle('Cámara omnidireccional: solo rayos reflejados físicamente válidos',fontsize=14)
    fig.tight_layout()
    fig.savefig(folder/'camara_virtual_paneles_finitos.png',dpi=160)
    plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,5))
    labels=[n.replace('inclinacion_','inclin. ').replace('curvatura_','curva ').replace('simetrico','simétrico').replace('_opacidad_',' filtro ') for n in names]
    xs=np.arange(len(names)); ys=[out[n]['trayectorias_robustas_8pix'] for n in names]
    ax.bar(xs,ys)
    ax.set_xticks(xs, labels,rotation=28,ha='right')
    ax.set_ylabel('Secuencias de reflejos visibles (≥ 8 píxeles)')
    ax.set_title('Trayectorias ópticas observables ≠ tamaño del grupo ideal')
    ax.grid(axis='y',alpha=.25)
    fig.tight_layout();fig.savefig(folder/'comparacion_trayectorias.png',dpi=160);plt.close(fig)


def finite_fov_experiment():
    """Observador limitado a un campo de 90°: mira a espejo o vértice."""
    plan=[('panel_frontal_0',(1,0,0),0.,0.,1.),
          ('panel_frontal_3',(1,0,0),3.,0.,1.),
          ('panel_frontal_5',(1,0,0),5.,0.,1.),
          ('panel_curvo_006',(1,0,0),0.,.06,1.),
          ('panel_opaco',(1,0,0),0.,0.,0.),
          ('mirando_vertice_0',(1,1,1),0.,0.,1.),
          ('mirando_vertice_3',(1,1,1),3.,0.,1.),
          ('mirando_fuente',tuple(SOURCE-CAM),0.,0.,1.)]
    res={}
    for name,front,tilt,curve,trans in plan:
        r=trace(w=420,h=280,max_bounces=6,view='pinhole',front=front,
             tilt_deg=tilt,curve=curve,transmit_plus=trans)
        res[name]=r
        print('PINHOLE',name,'pix',r['pixeles_con_fuente'],
              'rutas >=8',r['trayectorias_robustas_8pix'],flush=True)
    return res


def pinhole_figures(out,folder):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    names=list(out)
    fig,axes=plt.subplots(4,2,figsize=(12,13))
    for ax,name in zip(axes.flat,names):
        v=out[name]
        ax.imshow(v['_img'],cmap='gray',vmin=0,vmax=1,origin='upper')
        ax.set_title(name.replace('_',' ')+' · '+str(v['trayectorias_robustas_8pix'])+' rutas')
        ax.set_xticks([]);ax.set_yticks([])
    fig.suptitle('Cámara de 90°: imágenes físicamente observables',fontsize=14)
    fig.tight_layout()
    fig.savefig(folder/'camara_90grados_cambios.png',dpi=170)
    plt.close(fig)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--salida-dir',default='.')
    ap.add_argument('--ancho',type=int,default=520);ap.add_argument('--alto',type=int,default=260)
    ap.add_argument('--rebotes',type=int,default=6)
    args=ap.parse_args()
    folder=Path(args.salida_dir);folder.mkdir(parents=True,exist_ok=True)
    res=run_experiments(args.ancho,args.alto,args.rebotes)
    with open(folder/'resultados_v3.json','w',encoding='utf8') as f:
        json.dump({k:clean(v) for k,v in res.items()},f,indent=2,ensure_ascii=False)
    make_figures(res,folder)
    narrow=finite_fov_experiment()
    with open(folder/'resultados_camara_90grados.json','w',encoding='utf8') as f:
        json.dump({k:clean(v) for k,v in narrow.items()},f,indent=2,ensure_ascii=False)
    pinhole_figures(narrow,folder)
    print('Completo:',folder)

if __name__=='__main__':main()
