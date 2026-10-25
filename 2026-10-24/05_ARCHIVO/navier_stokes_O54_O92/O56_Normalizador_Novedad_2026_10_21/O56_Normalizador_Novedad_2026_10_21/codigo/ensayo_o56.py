#!/usr/bin/env python3
"""O56, prueba exacta de dos direcciones materiales en cizallas Navier-Stokes 3D.
Biblioteca estandar para calculos; matplotlib opcional para graficos. Sin descarga ni ajuste.
"""
from __future__ import annotations
import csv, json, math, sys
from pathlib import Path

NU=0.025
BOX=8.0
K=2.0*math.pi/BOX
R=1.60
R_DUCTO=0.48
THETA=math.pi/4
Z0=R_DUCTO*math.sin(THETA)
AMPLITUD=0.22
MIRROR_RATE=0.23
N_BASE=10  # 0.3 = 3/10 del valor inicial, codificacion aritmetica, no ley fisica
M_DECLARADO=4  # Malla adicional declarada, no deducida de NS
T_MAX=1.26


def cizalla(t:float, amplitude:float, direction:str):
    """u=A exp(-nu k² t) sin(kz) e_direction, exacta sin forzamiento."""
    g=amplitude*math.exp(-NU*K*K*t)
    if direction not in ('x','y'):
        raise ValueError('Solo x o y')
    return g


def beta(t:float, amplitude:float)->float:
    """d/dz del desplazamiento acumulado en z0 (matriz gradiente material)."""
    return amplitude*(1.0-math.exp(-NU*K*K*t))/(NU*K)*math.cos(K*Z0)


def vectors(t:float, amplitude:float, direction:str):
    b0=(-math.sin(THETA),0.0,math.cos(THETA))
    a=(0.0,1.0,0.0)
    b=list(b0)
    dv=beta(t,amplitude)*b0[2]
    b[0 if direction=='x' else 1]+=dv
    return a,tuple(b)


def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))


def cos_angle(t:float,amplitude:float,direction:str)->float:
    a,b=vectors(t,amplitude,direction)
    return dot(a,b)/(norm(a)*norm(b))


def cross_strain_initial(amplitude:float,direction:str)->float:
    # a=e_y, b=(-sin(theta),0,cos(theta)); S_yz=A*k*cos(kz)/2 si dir=y
    return (0.5*amplitude*K*math.cos(K*Z0)*math.cos(THETA)) if direction=='y' else 0.0


def initial_prediction(amplitude:float,direction:str)->float:
    # d/dt cos(angle) = 2 a^T S b para a,b unitarios inicialmente ortogonales.
    return 2.0*cross_strain_initial(amplitude,direction)


def kinetic_energy(t:float, amplitude:float)->float:
    # E = 1/2 promedio |u|²; promedio sin²=1/2
    return 0.25*amplitude*amplitude*math.exp(-2*NU*K*K*t)


def enstrophy(t:float, amplitude:float)->float:
    return kinetic_energy(t,amplitude)*K*K


def lcm(a,b): return a*b//math.gcd(a,b)


def run(out:Path):
    (out/'resultados').mkdir(parents=True,exist_ok=True)
    (out/'graficos').mkdir(parents=True,exist_ok=True)
    scenarios=[('sin_cizalla',0.0,'y'),('cizalla_en_y',AMPLITUD,'y'),('cizalla_en_x',AMPLITUD,'x'),('cizalla_y_inversa',-AMPLITUD,'y')]
    times=[T_MAX*i/126 for i in range(127)]
    n1=lcm(N_BASE,M_DECLARADO)
    data=[]
    for name,A,axis in scenarios:
        for t in times:
            c=cos_angle(t,A,axis)
            Lref=math.exp(MIRROR_RATE*t)
            row={
               'escenario':name,'t':round(t,10),'amplitud':A,'direccion':axis,
               'radio_mayor_inicial':R,'radio_ducto_inicial':R_DUCTO,
               'q_inicial':R_DUCTO/R,'Lref':Lref,'radio_mayor_observado_inicial':R/Lref,
               'radio_ducto_observado_inicial':R_DUCTO/Lref,
               'q_observado_inicial':(R_DUCTO/Lref)/(R/Lref),
               'M_inicial':N_BASE,'malla_nueva':M_DECLARADO,'M_refinado':n1,
               'indice_novedad_aritmetica':n1//N_BASE,
               'energia_cinetica':kinetic_energy(t,A),'enstrofia':enstrophy(t,A),
               'cos_angulo_material':c,'angulo_material_grados':math.degrees(math.acos(max(-1,min(1,c)))),
               'K0_deformacion_cruzada':cross_strain_initial(A,axis),
               'prediccion_pendiente_inicial':initial_prediction(A,axis),
            }
            data.append(row)
    csv_path=out/'resultados'/'serie_exacta.csv'
    with csv_path.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=list(data[0]));wr.writeheader();wr.writerows(data)
    final={}
    for name,A,axis in scenarios:
        final[name]={
            'A':A,'direccion':axis,'cos_final':cos_angle(T_MAX,A,axis),
            'angulo_final_deg':math.degrees(math.acos(cos_angle(T_MAX,A,axis))),
            'E_inicial':kinetic_energy(0,A),'Z_inicial':enstrophy(0,A),
            'q_inicial':R_DUCTO/R,'M_antes':N_BASE,'M_despues':n1,
            'novedad_aritmetica':n1//N_BASE,'K0':cross_strain_initial(A,axis),
            'pendiente_inicial':initial_prediction(A,axis)
        }

    # Identidades exactas/datos discriminantes, verificadas con 18 controles:
    checks={}
    def check(key,cond):
        checks[key]=bool(cond)
        if not cond: raise AssertionError('Control fallido: '+key)
    check('geometria_q_0_3', math.isclose(R_DUCTO/R,0.3,abs_tol=1e-14))
    check('normalizador_minimo_10', N_BASE==10 and math.gcd(3,N_BASE)==1)
    check('refinamiento_M_10_a_20', n1==20)
    check('novedad_aritmetica_indice_2',n1//N_BASE==2)
    check('misma_normalizacion_escenarios',len({(x['M_antes'],x['M_despues']) for x in final.values()})==1)
    check('mismo_E_inicial_dos_ejes',math.isclose(final['cizalla_en_x']['E_inicial'],final['cizalla_en_y']['E_inicial'],abs_tol=1e-15))
    check('misma_Z_inicial_dos_ejes',math.isclose(final['cizalla_en_x']['Z_inicial'],final['cizalla_en_y']['Z_inicial'],abs_tol=1e-15))
    check('mismo_E_inicial_signos',math.isclose(final['cizalla_en_y']['E_inicial'],final['cizalla_y_inversa']['E_inicial'],abs_tol=1e-15))
    check('cizalla_x_conserva_ortogonalidad',all(abs(cos_angle(t,AMPLITUD,'x'))<1e-13 for t in times))
    check('cizalla_y_rompe_ortogonalidad',abs(cos_angle(T_MAX,AMPLITUD,'y'))>0.10)
    check('cizallas_signo_opuesto',math.isclose(cos_angle(T_MAX,AMPLITUD,'y'),-cos_angle(T_MAX,-AMPLITUD,'y'),abs_tol=1e-13))
    check('sin_cizalla_conserva_ortogonalidad',all(abs(cos_angle(t,0,'y'))<1e-13 for t in times))
    check('deformacion_cruzada_x_nula',cross_strain_initial(AMPLITUD,'x')==0)
    check('deformacion_cruzada_y_no_nula',cross_strain_initial(AMPLITUD,'y')>0)
    for label,A,axis in scenarios:
        eps=1e-5
        fd=(cos_angle(eps,A,axis)-cos_angle(0,A,axis))/eps
        check('pendiente_inicial_'+label,abs(fd-initial_prediction(A,axis))<1e-6)
    # Comparación control O55: mismos q y angulo inicial, resultados distintos (numéricos históricos).
    o55_csv=out/'fuentes'/'O55_resultados_original.csv'
    validation=None
    if o55_csv.exists():
        with o55_csv.open(encoding='utf-8') as f:
            previous=list(csv.DictReader(f))
        starts=[x for x in previous if float(x['t'])==0]
        ends=[x for x in previous if math.isclose(float(x['t']),T_MAX,abs_tol=1e-8)]
        check('O55_misma_q_inicial',len(starts)==2 and all(math.isclose(float(x['q']),0.3,abs_tol=1e-12) for x in starts))
        check('O55_mismo_angulo_inicial',all(math.isclose(float(x['angle_cos']),0.0,abs_tol=1e-12) for x in starts))
        check('O55_futuros_distintos',len(ends)==2 and abs(float(ends[0]['angle_cos'])-float(ends[1]['angle_cos']))>0.1)
        validation={x['condition']:{'q0':float(next(y['q'] for y in starts if y['condition']==x['condition'])),
                        'cos_final':float(x['angle_cos']), 'angulo_final_deg':float(x['local_angle_deg'])} for x in ends}
    res={'ensayo':'O56','modelo':'cizallas exactas NS 3D + lectura separada de O55',
         'parametros':{'nu':NU,'k':K,'R':R,'r':R_DUCTO,'theta':THETA,'z0':Z0,'amplitud':AMPLITUD,
                       'espejo_L_ref':'exp(0.23 t)','tiempo_final':T_MAX},
         'casos':final,'controles':checks,'controles_aprobados':sum(checks.values()),
         'datos_o55':validation,
         'advertencias':['El flujo exacto de cizalla es un contraejemplo dinámico, no un anillo vorticial exacto aislado.',
             'Los radios R,r indicados son de la superficie inicial: no son necesariamente radios efectivos de superficie deformada.',
             'M=10 es codificacion de 3/10; m=4 es malla declarada, no seleccion fisica derivada.',
             'La novedad relacional de K requiere información de gradiente de velocidad; no deriva de M.',
             'Perpendicularidad no garantiza persistencia del toro fisico ni regularidad global 3D.']}
    (out/'resultados'/'resumen.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig,ax=plt.subplots(figsize=(9.4,5.4))
        for name,A,axis in scenarios:
            ax.plot(times,[math.degrees(math.acos(cos_angle(t,A,axis))) for t in times],label=name.replace('_',' '))
        ax.axhline(90,ls=':',lw=1)
        ax.set(xlabel='Tiempo del modelo', ylabel='Ángulo entre dos direcciones materiales (°)',
               title='O56 · Mismo normalizador inicial; dinámicas distintas')
        ax.grid(alpha=.25)
        ax.legend(fontsize=9)
        fig.tight_layout()
        fig.savefig(out/'graficos'/'angulos_cizallas_exactas.png',dpi=155)
        plt.close(fig)
    except ImportError:
        pass
    print(json.dumps({'controles_aprobados':sum(checks.values()), 'casos':final,'o55':validation},ensure_ascii=False,indent=2))
    return res

if __name__=='__main__':
    root=Path(__file__).resolve().parents[1]
    run(root)
