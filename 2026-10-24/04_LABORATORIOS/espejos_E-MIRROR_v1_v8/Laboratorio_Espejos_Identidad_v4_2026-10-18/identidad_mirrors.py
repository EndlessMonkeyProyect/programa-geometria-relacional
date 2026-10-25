#!/usr/bin/env python3
"""Laboratorio E-MIRROR v4: inferencia sin etiquetas de procedencia.

Óptica geométrica ideal, reflectores PLANOS FINITOS y exactamente un rebote.
Las fuentes son emisores puntuales ópticamente delgados con brillo desconocido;
el sensor integra dos gaussianas de PSF + ruido. La inferencia recibe SOLO las
imágenes y calibraciones de cámara/espejo, nunca la cantidad de fuentes ni
sus coordenadas verdaderas.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.ndimage import maximum_filter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

W,H = 640,360
FOV_DEG = 125.
SIGMA_PX=2.4
NOISE_STD=.004
SIDE=.90
MIRROR=.90
C1=np.array([.12,-.22,.19],float)
C2=np.array([.12,.46,.19],float)
S1=np.array([-.37,.28,.11],float)
V1=np.array([2*MIRROR-S1[0],S1[1],S1[2]])
V2=C1+1.15*(V1-C1)
S2=np.array([2*MIRROR-V2[0],V2[1],V2[2]])


def frame(front=(1.,0.,0.)):
    f=np.asarray(front,float);f=f/np.linalg.norm(f)
    up0=np.array([0.,0.,1.]);right=np.cross(f,up0);right/=np.linalg.norm(right)
    up=np.cross(right,f)
    return f,right,up


def camera_project(c, virtual, front=(1.,0.,0.), w=W,h=H,fov=FOV_DEG):
    f,r,u=frame(front);v=virtual-c
    depth=np.dot(v,f)
    if depth<=0:return None
    focal=(w/2)/math.tan(math.radians(fov/2))
    return np.array([w/2+focal*np.dot(v,r)/depth,h/2-focal*np.dot(v,u)/depth])


def pixel_ray(c, p, front=(1.,0.,0.), w=W,h=H,fov=FOV_DEG):
    f,r,u=frame(front)
    focal=(w/2)/math.tan(math.radians(fov/2))
    d=f+((p[0]-w/2)/focal)*r-((p[1]-h/2)/focal)*u
    return d/np.linalg.norm(d)


def reflect_virtual(s,face):
    v=s.copy()
    ax=0 if face=='X+' else 1
    v[ax]=2*MIRROR-s[ax]
    return v


def reflect_valid(c,s,face):
    v=reflect_virtual(s,face)
    ax=0 if face=='X+' else 1
    denom=(v[ax]-c[ax])
    if denom<=0:return False
    t=(MIRROR-c[ax])/denom
    if not 0<t<1:return False
    hit=c+t*(v-c)
    other=[j for j in range(3) if j!=ax]
    return bool(all(abs(hit[j])<=SIDE for j in other))


def appearances(c,sources,faces=('X+',),front=(1.,0.,0.),amplitudes=None):
    if amplitudes is None:amplitudes=[1.]*len(sources)
    spots=[]
    for src, amp in zip(sources,amplitudes):
        for face in faces:
            if not reflect_valid(c,src,face):continue
            p=camera_project(c,reflect_virtual(src,face),front)
            if p is not None and 0<=p[0]<W and 0<=p[1]<H:
                spots.append({'x':float(p[0]),'y':float(p[1]),'amplitude':float(amp),'face':face})
    return spots


def sensor(c,sources,faces=('X+',),front=(1.,0.,0.),amplitudes=None,seed=123):
    yy,xx=np.mgrid[0:H,0:W]
    im=np.zeros((H,W),float)
    for spot in appearances(c,sources,faces,front,amplitudes):
        im+=spot['amplitude']*np.exp(-((xx-spot['x'])**2+(yy-spot['y'])**2)/(2*SIGMA_PX**2))
    if seed is not None:im+=np.random.default_rng(seed).normal(0,NOISE_STD,im.shape)
    return im


def fit_spots(image, min_amplitude=.15, verbose=False):
    """Detección de máximos + ajuste de PSF y selección BIC. Sin acceso al render latente.
    Ventana local, hasta dos emisores/panel en el ejemplo de control. Un detector
    real general requeriría segmentar múltiples caras y mayor orden de modelos.
    """
    smooth_max=maximum_filter(image,size=9)
    cand=np.argwhere((image==smooth_max)&(image>.09))
    cand=sorted(cand,key=lambda yx:-image[tuple(yx)])
    if not cand:return {'n_spots':0,'spots':[],'bic':None}
    selected=[]
    for y,x in cand:
        if all(np.hypot(x-x0,y-y0)>3.0 for x0,y0 in selected):selected.append((x,y))
        if len(selected)>=4:break
    cx,cy=selected[0]
    # Los puntos pueden estar próximos; ventana de >= 44 píxeles por eje.
    lo_x=max(0,int(cx)-30);hi_x=min(W,int(cx)+31)
    lo_y=max(0,int(cy)-25);hi_y=min(H,int(cy)+26)
    if len(selected)>=2:
        lo_x=max(0,min(lo_x,int(selected[1][0])-18));hi_x=min(W,max(hi_x,int(selected[1][0])+19))
        lo_y=max(0,min(lo_y,int(selected[1][1])-18));hi_y=min(H,max(hi_y,int(selected[1][1])+19))
    yy,xx=np.mgrid[lo_y:hi_y,lo_x:hi_x]
    z=image[lo_y:hi_y,lo_x:hi_x].ravel()
    X=xx.ravel();Y=yy.ravel()
    def model(pars):
        result=np.zeros_like(z)
        for x,y,a in pars.reshape(-1,3).tolist():
            result+=a*np.exp(-((X-x)**2+(Y-y)**2)/(2*SIGMA_PX**2))
        return result
    def opt(params):
        n=len(params)//3
        lower=[lo_x-1,lo_y-1,0.]*n
        upper=[hi_x+1,hi_y+1,8.]*n
        res=least_squares(lambda p:model(p)-z,params,bounds=(lower,upper),xtol=1e-10,ftol=1e-10,gtol=1e-10,max_nfev=250)
        rss=np.sum(res.fun**2)
        # desviación del sensor conocida/calibrada
        bic=rss/(NOISE_STD**2)+(3*n)*np.log(len(z))
        return res.x,rss,bic
    p1,rss1,b1=opt([float(cx),float(cy),float(image[cy,cx])])
    # Segundo punto puede no ser máximo local (resolución sub-PSF).
    if len(selected)>=2:
        x2,y2=selected[1]
    else:
        x2,y2=cx+3*SIGMA_PX,cy
    p2,rss2,b2=opt([*p1,max(lo_x,min(hi_x-1,float(x2))),max(lo_y,min(hi_y-1,float(y2))),.5])
    # Si fuera una sola fuente, prohíbe 'ganar' con un artefacto casi nulo.
    use_two=(b2+0.0 < b1) and all(a>=min_amplitude for a in p2[2::3])
    chosen=(p2 if use_two else p1)
    spots=[{'x':round(float(x),5),'y':round(float(y),5),'amplitude':round(float(a),5)} for x,y,a in chosen.reshape(-1,3)]
    spots.sort(key=lambda x:x['x'])
    return {'n_spots':len(spots),'spots':spots,'bic_1':float(b1),'bic_2':float(b2),
            'rss_1':float(rss1),'rss_2':float(rss2), 'window':[lo_x,lo_y,hi_x,hi_y]}


def triangulate(ca,pa,cb,pb,face='X+'):
    # Debe conocerse qué canal reflejado corresponde a cada observación.
    a=pixel_ray(ca,pa);b=pixel_ray(cb,pb)
    A=np.eye(3)-np.outer(a,a);B=np.eye(3)-np.outer(b,b)
    v=np.linalg.solve(A+B,A@ca+B@cb)
    src=v.copy();ax=0 if face=='X+' else 1;src[ax]=2*MIRROR-v[ax]
    residual=np.linalg.norm(np.cross(v-ca,a))+np.linalg.norm(np.cross(v-cb,b))
    return src,residual


def reflect_point(point,face):
    r=np.asarray(point,float).copy()
    ax=0 if face=='X+' else 1
    r[ax]=2*MIRROR-r[ax]
    return r


def reflected_line(c,p,face,front):
    """Rayo invertido mediante calibración del espejo, sin usar la fuente real."""
    return reflect_point(c,face),reflect_direction(pixel_ray(c,p,front),face)


def reflect_direction(d,face):
    out=d.copy();out[0 if face=='X+' else 1]*=-1
    return out


def infer_first_mirror(c,p,front):
    d=pixel_ray(c,p,front)
    options=[]
    for face in ['X+','Y+']:
        ax=0 if face=='X+' else 1
        if d[ax]<1e-12:continue
        t=(MIRROR-c[ax])/d[ax]
        hit=c+t*d
        other=[j for j in range(3) if j!=ax]
        if t>0 and all(abs(hit[j])<=SIDE for j in other): options.append((t,face))
    return min(options)[1] if options else None


def fit_sparse_spots(image):
    """Localiza puntos ampliamente separados, sin conocimiento de qué fuente los creó."""
    peaks=np.argwhere((image==maximum_filter(image,size=17))&(image>.18))
    peaks=sorted(peaks,key=lambda yx:-image[tuple(yx)])
    selected=[]
    for y,x in peaks:
        if any(math.hypot(x-v[0],y-v[1])<10 for v in selected):continue
        selected.append((int(x),int(y)))
    result=[]
    for cx,cy in selected:
        x0=max(0,cx-9);x1=min(W,cx+10);y0=max(0,cy-9);y1=min(H,cy+10)
        YY,XX=np.mgrid[y0:y1,x0:x1]
        z=image[y0:y1,x0:x1]
        def diff(p):return (p[2]*np.exp(-((XX-p[0])**2+(YY-p[1])**2)/(2*SIGMA_PX**2))-z).ravel()
        fit=least_squares(diff,[cx,cy,float(image[cy,cx])],bounds=([x0,y0,0],[x1,y1,9]))
        result.append({'x':float(fit.x[0]),'y':float(fit.x[1]),'amplitude':float(fit.x[2])})
    return sorted(result,key=lambda s:s['x'])


def infer_common_source_two_faces(c,spots,front):
    if len(spots)!=2:return None
    classified=[(infer_first_mirror(c,(s['x'],s['y']),front),s) for s in spots]
    if None in [x[0] for x in classified] or classified[0][0]==classified[1][0]:return None
    (fa,pa),(fb,pb)=classified
    oa,da=reflected_line(c,(pa['x'],pa['y']),fa,front)
    ob,db=reflected_line(c,(pb['x'],pb['y']),fb,front)
    A=np.eye(3)-np.outer(da,da);B=np.eye(3)-np.outer(db,db)
    src=np.linalg.solve(A+B,A@oa+B@ob)
    residual=np.linalg.norm(np.cross(src-oa,da))+np.linalg.norm(np.cross(src-ob,db))
    return {'canales_observados':[fa,fb], 'fuentes_minimas_compatibles':1,
            'posicion_fuente_estimada_m':[float(v) for v in src],
            'desacuerdo_rayos_m':float(residual),
            'error_contra_verdad_m':float(np.linalg.norm(src-S1))}


def core_experiment():
    # Experimento A: mundos con 1 vs 2 emisores idénticos para C1, brillo desconocido.
    im_two=sensor(C1,[S1,S2],seed=11)
    im_one=sensor(C1,[S1],amplitudes=[2.],seed=11)
    im_shift=sensor(C2,[S1,S2],seed=12)
    # Alternativa: cambiar de canal espejo sin mover la primera cámara.
    im_y=sensor(C1,[S1,S2],faces=('Y+',),front=(.5,1.,0.),seed=13)
    # Control: la misma fuente puede tener dos imágenes (canales X e Y).
    im_double=sensor(C1,[S1],faces=('X+','Y+'),front=(1.,1.,0.),seed=14)
    # Imágenes generadas de varias reflexiones: esto es para demostración.
    o={'montaje':{'pared_cubo_m':2.,'plano_espejo_m':MIRROR,'semiancho_panel_m':SIDE,
          'rebotes_maximos':1,'fuentes':'puntuales, transparentes entre sí, espectro y brillo no etiquetados',
          'camara1':C1.tolist(),'camara2':C2.tolist(),'fov_horizontal_grados':FOV_DEG,
          'psf_sigma_px':SIGMA_PX,'ruido_desviacion':NOISE_STD,'resolucion':[W,H]},
       'A_una_vs_dos_misma_camara':{
           'max_diferencia_ideal_con_mismo_ruido':float(np.max(abs(im_one-im_two))),
           'diferencia_rms':float(np.sqrt(np.mean((im_one-im_two)**2))),
           'fuentes_reales_separacion_m':float(np.linalg.norm(S1-S2)),
           'estimacion_desde_una_imagen':fit_spots(im_two)},
       'B_mover_camara':{'estimacion':fit_spots(im_shift)},
       'C_abrir_otro_espejo':{'estimacion_y':fit_spots(im_y)},
       'D_misma_fuente_dos_espejos':{'n_caminos_de_primera_reflexion':len(appearances(C1,[S1],faces=('X+','Y+'),front=(1.,1.,0.))),
            'maximos_sensor':len(appearances(C1,[S1],faces=('X+','Y+'),front=(1.,1.,0.)))} }
    pa=o['A_una_vs_dos_misma_camara']['estimacion_desde_una_imagen']['spots'][0]
    recovered=[]
    for pb in o['B_mover_camara']['estimacion']['spots']:
        src,res=triangulate(C1,(pa['x'],pa['y']),C2,(pb['x'],pb['y']))
        recovered.append({'posicion_m':[float(x) for x in src],'residuo_optico_m':float(res)})
    recovered.sort(key=lambda s:s['posicion_m'][0])
    true_sorted=sorted([S1,S2],key=lambda x:x[0])
    for rec,truth in zip(recovered,true_sorted):rec['error_contra_verdad_m']=float(np.linalg.norm(np.asarray(rec['posicion_m'])-truth))
    o['B_mover_camara']['triangulacion_inferencia_a_posteriori']=recovered
    front_diag=(1.,1.,0.)
    o['D_misma_fuente_dos_espejos']['deteccion'] = fit_sparse_spots(im_double)
    o['D_misma_fuente_dos_espejos']['reconstruccion'] = infer_common_source_two_faces(C1,o['D_misma_fuente_dos_espejos']['deteccion'],front_diag)
    return o, {'A_una_fuente':im_one,'A_dos_fuentes':im_two,'B_camara_desplazada':im_shift,'C_espejo_Y':im_y,'D_una_fuente_dos_espejos':im_double}


def make_figures(images,outdir):
    fig,axs=plt.subplots(2,2,figsize=(12,7),layout='constrained')
    captions=[('A_dos_fuentes','Una cámara, dos fuentes superpuestas'),('B_camara_desplazada','Otra posición: dos manchas'),
              ('C_espejo_Y','Misma posición, otro espejo'),('D_una_fuente_dos_espejos','Una fuente, dos espejos')]
    for ax,(key,label) in zip(axs.ravel(),captions):
        arr=images[key]
        ax.imshow(arr,origin='upper',vmin=0,vmax=1.4,cmap='magma')
        ax.set_title(label,fontsize=11)
        ax.set(xlim=(0,W),ylim=(H,0),xlabel='Píxel x',ylabel='Píxel y')
    fig.savefig(outdir/'figura_cambio_marco.png',dpi=145)
    plt.close(fig)
    # Dibujo geométrico superior x-y, que muestra procedencia vs imagen virtual.
    fig,ax=plt.subplots(figsize=(8,6),layout='constrained')
    square=np.array([[-1,-1],[1,-1],[1,1],[-1,1],[-1,-1]])
    ax.plot(square[:,0],square[:,1],color='.55',linestyle='--',label='Contorno de habitación')
    ax.plot([MIRROR,MIRROR],[-SIDE,SIDE],lw=4,label='Espejo X+')
    ax.plot([-SIDE,SIDE],[MIRROR,MIRROR],lw=4,label='Espejo Y+')
    ax.scatter([S1[0],S2[0]],[S1[1],S2[1]],marker='*',s=160,label='Dos fuentes reales',zorder=5)
    ax.scatter([C1[0],C2[0]],[C1[1],C2[1]],marker='s',s=80,label='Cámaras',zorder=5)
    for c,lbl in [(C1,'C1'),(C2,'C2')]:
        ax.text(c[0]+.02,c[1]-.10,lbl)
        for i,s in enumerate([S1,S2]):
            v=reflect_virtual(s,'X+')
            # Extiende la línea hasta el punto virtual, atravesando el espejo.
            ax.plot([c[0],v[0]],[c[1],v[1]],alpha=.48,linestyle='-' if i==0 else ':')
    ax.plot([V1[0],V2[0]],[V1[1],V2[1]],'o',alpha=.6,label='Imágenes virtuales X+')
    ax.set(xlabel='x (m)',ylabel='y (m)',title='Dos fuentes pueden proyectarse en un mismo rayo',aspect='equal',xlim=(-1.05,2.8),ylim=(-1.05,1.75))
    ax.legend(fontsize=9,loc='lower right')
    fig.savefig(outdir/'figura_geometria.png',dpi=150);plt.close(fig)
    # zoom de superposición a dos manchas: y-slices around max
    fig,axs=plt.subplots(1,2,figsize=(10,3.6),layout='constrained')
    for ax,key,title in zip(axs,['A_dos_fuentes','B_camara_desplazada'],
                            ['Cámara 1: coincidencia exacta','Cámara 2: separación por paralaje']):
        a=images[key]
        row=int(np.argmax(a)//W);col=int(np.argmax(a)%W)
        ax.imshow(a,origin='upper',vmin=0,vmax=1.4,cmap='magma')
        ax.set(xlim=(col-38,col+38),ylim=(row+18,row-18),title=title,xlabel='Píxel x',ylabel='Píxel y')
    fig.savefig(outdir/'figura_zoom.png',dpi=170)
    plt.close(fig)
    # ideal profile cross-section (not using ground-truth in inference): noise-free
    fig,ax=plt.subplots(figsize=(9,4),layout='constrained')
    for key,label in [('A_una_fuente','1 fuente con doble brillo'),('A_dos_fuentes','2 fuentes coincidentes')]:
        a=images[key]
        row=int(np.argmax(a)//W);col=int(np.argmax(a)%W)
        ax.plot(np.arange(col-20,col+21),a[row,col-20:col+21],label=label,alpha=.8)
    ax.set(xlabel='Píxel horizontal',ylabel='Intensidad (u. a.)',title='Mismas observaciones, dos modelos físicos',ylim=(-.05,2.15))
    ax.legend();fig.savefig(outdir/'figura_indistinguibilidad.png',dpi=155);plt.close(fig)


def main():
    out=Path(__file__).resolve().parent
    metrics,images=core_experiment()
    (out/'resultados_v4.json').write_text(json.dumps(metrics,indent=2,ensure_ascii=False),encoding='utf-8')
    make_figures(images,out)
    print(json.dumps({'comparacion_un_canal':metrics['A_una_vs_dos_misma_camara']['max_diferencia_ideal_con_mismo_ruido'],
       'inferidos_C1':metrics['A_una_vs_dos_misma_camara']['estimacion_desde_una_imagen']['n_spots'],
       'inferidos_C2':metrics['B_mover_camara']['estimacion']['n_spots'],
       'inferidos_Y':metrics['C_abrir_otro_espejo']['estimacion_y']['n_spots'],
       'reconstruccion_errores_m':[v['error_contra_verdad_m'] for v in metrics['B_mover_camara']['triangulacion_inferencia_a_posteriori']]},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
