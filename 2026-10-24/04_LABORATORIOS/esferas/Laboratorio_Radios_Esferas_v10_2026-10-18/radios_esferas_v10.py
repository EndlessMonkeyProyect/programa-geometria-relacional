#!/usr/bin/env python3
"""Laboratorio relacional v10: ritmos radiales y ambigüedad de reflexión.
Sólo modelos geométricos exactos/discretos; no representa campos electromagnéticos.
"""
import csv
import json
from math import sqrt
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent
U=1.0
A=2.0*U
RADII=np.arange(2,25,2,dtype=int)    # retícula generada por gcd(4,6)=2u
ANGLES=np.arange(0,360,30,dtype=int) # retícula generada por gcd(60,90)=30°


def radial_mask(radial_step, angle_step, offset=0):
    return np.array([[(r%radial_step==0) and ((theta-offset)%angle_step==0)
                     for theta in ANGLES] for r in RADII], dtype=bool)


def radial_experiment():
    m_a=radial_mask(4,60)
    m_b=radial_mask(6,90)
    m_c=radial_mask(4,60,30)
    union_ab=m_a|m_b
    union_abc=union_ab|m_c
    return dict(A=m_a,B=m_b,C=m_c,AB=union_ab,ABC=union_abc,
        counts={"total":int(union_ab.size),"A":int(m_a.sum()),"B":int(m_b.sum()),
                "intersection_AB":int((m_a&m_b).sum()),
                "projection_AB":int(union_ab.sum()),
                "silence_AB":int((~union_ab).sum()),
                "C":int(m_c.sum()),"new_projection_C":int((m_c&~union_ab).sum()),
                "projection_ABC":int(union_abc.sum()),
                "silence_ABC":int((~union_abc).sum())})


def tetrahedron():
    """Equilateral base, two positions for a fourth center with all 3 distances A."""
    a=A
    anchors = np.array([[0.,0.,0.],[a,0.,0.],[a/2,sqrt(3)*a/2,0.]])
    c=np.array([a/2,sqrt(3)*a/6,0.])
    h=sqrt(2/3)*a
    pplus=c+np.array([0.,0.,h])
    pminus=c-np.array([0.,0.,h])
    fourth_coplanar=np.array([a/2,-sqrt(3)*a/2,0.])
    fourth_out=np.array([0.,0.,a])
    return anchors,pplus,pminus,fourth_coplanar,fourth_out


def trilateration_difference(anchors, distances, reference=0):
    """Linearized difference equations: rank and particular solution.
    For every i != reference,
    2(ai-a0)·p = ||ai||²-||a0||² - (di²-d0²).
    Does not by itself enforce first quadratic equation; returns linear affine set.
    """
    anchors=np.asarray(anchors,dtype=float)
    distances=np.asarray(distances,dtype=float)
    a0=anchors[reference]
    d0=distances[reference]
    keep=np.arange(len(anchors))!=reference
    rest=anchors[keep]
    rd=distances[keep]
    mat=2*(rest-a0)
    rhs=(rest*rest).sum(axis=1)-np.dot(a0,a0) - (rd*rd-d0*d0)
    sol=np.linalg.lstsq(mat,rhs,rcond=None)[0]
    rank=int(np.linalg.matrix_rank(mat,tol=1e-11))
    residual=float(np.max(np.abs(mat@sol-rhs))) if len(rhs) else 0.
    return sol, rank, residual


def signed_volume(a,b,c,p):
    return float(np.linalg.det(np.stack([b-a,c-a,p-a],axis=1))/6)


def geom_experiment():
    anchors,plus,minus,plane4,out4=tetrahedron()
    coplanar=np.vstack([anchors,plane4])
    noncoplanar=np.vstack([anchors,out4])
    d3=np.linalg.norm(anchors-plus,axis=1)
    d4plane=np.linalg.norm(coplanar-plus,axis=1)
    d4out=np.linalg.norm(noncoplanar-plus,axis=1)
    # both possible when only three plane anchors or four plane anchors are used
    recon3=trilateration_difference(anchors,d3)
    recon4plane=trilateration_difference(coplanar,d4plane)
    recon4space=trilateration_difference(noncoplanar,d4out)
    d_plus_out=float(np.linalg.norm(plus-out4))
    d_minus_out=float(np.linalg.norm(minus-out4))
    return dict(anchors=anchors,plus=plus,minus=minus,
        fourth_coplanar=plane4,fourth_out_of_plane=out4,
        d3=d3, d4_coplanar=d4plane, d4_noncoplanar=d4out,
        rank_3=recon3[1],rank_4_coplanar=recon4plane[1],rank_4_noncoplanar=recon4space[1],
        reconstructed_non_coplanar=recon4space[0],
        error_non_coplanar=float(np.linalg.norm(recon4space[0]-plus)),
        coplanar_same_distances=bool(np.allclose(np.linalg.norm(coplanar-minus,axis=1),d4plane)),
        plus_distance_to_anchor4=d_plus_out,
        minus_distance_to_anchor4=d_minus_out,
        signed_volume_plus=signed_volume(*anchors,plus),
        signed_volume_minus=signed_volume(*anchors,minus))


def write_results():
    rad=radial_experiment()
    geo=geom_experiment()
    with open(OUT/'reticula_radial.csv','w',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        w.writerow(['radio_u','angulo_grados','canal_A','canal_B','canal_C','AB','ABC','silencio_AB','silencio_ABC'])
        for ir,r in enumerate(RADII):
            for ia,theta in enumerate(ANGLES):
                w.writerow([int(r),int(theta),*[int(rad[k][ir,ia]) for k in ('A','B','C','AB','ABC')],int(not rad['AB'][ir,ia]),int(not rad['ABC'][ir,ia])])
    with open(OUT/'distancias_anclajes.csv','w',newline='',encoding='utf-8') as f:
        w=csv.writer(f)
        w.writerow(['anclaje','x_u','y_u','z_u','distancia_+_u','distancia_-_u'])
        arr=np.vstack([geo['anchors'],geo['fourth_coplanar'],geo['fourth_out_of_plane']])
        for i,v in enumerate(arr):
            w.writerow([i,*[f'{x:.12g}' for x in v],
                        f'{np.linalg.norm(v-geo["plus"]):.12g}',
                        f'{np.linalg.norm(v-geo["minus"]):.12g}'])
    summary={
        'unit':'u, length units arbitrary',
        'radial_periods_u':[4,6],
        'radial_generated_spacing_u':2,
        'angular_periods_degrees':[60,90],
        'angular_generated_spacing_degrees':30,
        'radial_counts':rad['counts'],
        'three_sphere_centers':geo['anchors'].tolist(),
        'candidate_centers_fourth_sphere':[geo['plus'].tolist(),geo['minus'].tolist()],
        'fourth_coplanar_anchor':geo['fourth_coplanar'].tolist(),
        'fourth_noncoplanar_anchor':geo['fourth_out_of_plane'].tolist(),
        'ranks':{'3_anchors':geo['rank_3'],'4_coplanar_anchors':geo['rank_4_coplanar'],'4_noncoplanar_anchors':geo['rank_4_noncoplanar']},
        'mirror_solutions_identical_distances_to_four_coplanar_anchors':geo['coplanar_same_distances'],
        'off_plane_anchor_distances':{'plus':geo['plus_distance_to_anchor4'],'minus':geo['minus_distance_to_anchor4']},
        'unique_reconstruction_error':geo['error_non_coplanar'],
        'oriented_tetra_volumes':{'plus':geo['signed_volume_plus'],'minus':geo['signed_volume_minus']},
        'epistemic_limits':[
            'A blank radial cell is a silence of the given projection rules, not evidence of a hidden sphere.',
            'Adding an angular channel requires an independent angular relation, not an independent radial ruler.',
            'Coplanar distances determine mirror alternatives, not absolute spatial handedness.',
            'Adding a non-coplanar reference resolves the ambiguity relative to that oriented reference, without introducing a new primitive unit of length.',
            'The optical v1-v8 results and Maxwell dynamics are not deduced from this combinatorial/Euclidean model.'
        ]}
    (OUT/'resultados_v10.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return summary,rad,geo


def make_plots(rad,geo):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle
    plt.rcParams.update({'font.size':10,'figure.dpi':130,'savefig.dpi':165})
    # Heatmaps for radial occupancy before and after extra angular orientation
    fig, axes=plt.subplots(1,3,figsize=(14.4,4.2),constrained_layout=True)
    for ax,data,name in zip(axes,[rad['A'],rad['AB'],rad['ABC']],
            ['A: Δr = 4u, Δθ = 60°','A ∪ B: Δr = 4u / 6u','A ∪ B ∪ C: C rotado 30°']):
        ax.imshow(data.astype(int),origin='lower',aspect='auto',interpolation='nearest',vmin=0,vmax=1,cmap='Greys')
        ax.set_xticks(np.arange(len(ANGLES)),[str(x) for x in ANGLES],rotation=60)
        ax.set_yticks(np.arange(len(RADII)),[str(x) for x in RADII])
        ax.set_title(name)
        ax.set_xlabel('Orientación (grados)')
        ax.set_ylabel('Radio / u')
    fig.suptitle('Misma retícula de radios, diferentes proyecciones: blanco = silencio del canal')
    fig.savefig(OUT/'01_trama_radial.png',bbox_inches='tight')
    plt.close(fig)
    # Polar projection A U B and C addition
    fig=plt.figure(figsize=(12,5.3),constrained_layout=True)
    for i,(mask,title) in enumerate([(rad['AB'],'A + B'),(rad['ABC'],'A + B + C')]):
        ax=fig.add_subplot(1,2,i+1,projection='polar')
        th, rr=np.meshgrid(np.deg2rad(ANGLES),RADII)
        ax.scatter(th[mask],rr[mask],s=50,alpha=.86)
        ax.set_rmax(26)
        ax.set_rticks([4,8,12,16,20,24])
        ax.set_title(title+' — proyecciones radiales',pad=17)
    fig.savefig(OUT/'02_radios_polares.png',bbox_inches='tight')
    plt.close(fig)
    # mirrored tetrahedron illustration
    fig=plt.figure(figsize=(11.8,5.4),constrained_layout=True)
    for j,(anchor4,title) in enumerate([(geo['fourth_coplanar'],'Cuarto anclaje coplanar: persisten ±'),
                                       (geo['fourth_out_of_plane'],'Cuarto anclaje fuera del plano: resuelve ±')]):
        ax=fig.add_subplot(1,2,j+1,projection='3d')
        base=geo['anchors']
        ax.scatter(base[:,0],base[:,1],base[:,2],s=90,label='Tres centros coplanares')
        ax.scatter(*geo['plus'],s=110,marker='^',label='Posición +')
        ax.scatter(*geo['minus'],s=100,marker='v',label='Posición −')
        ax.scatter(*anchor4,s=105,marker='s',label='Referencia adicional')
        cyc=np.vstack([base,base[0]])
        ax.plot(cyc[:,0],cyc[:,1],cyc[:,2],linestyle=':')
        for vertex in base:
            for p in (geo['plus'],geo['minus']):
                ax.plot([vertex[0],p[0]],[vertex[1],p[1]],[vertex[2],p[2]],alpha=.35)
        ax.set_title(title,pad=11)
        ax.set(xlabel='x / u',ylabel='y / u',zlabel='z / u')
        ax.set(xlim=(-.4,2.4),ylim=(-2,2.4),zlim=(-2.2,2.2))
        ax.view_init(elev=17,azim=-65)
    handles, labels=ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center',ncol=4,fontsize=9)
    fig.savefig(OUT/'03_esferas_reflejo.png',bbox_inches='tight')
    plt.close(fig)
    # one face against a coplanar extra reference: identical distance signatures
    arr=np.vstack([geo['anchors'],geo['fourth_coplanar'],geo['fourth_out_of_plane']])
    dplus=np.linalg.norm(arr-geo['plus'],axis=1)
    dminus=np.linalg.norm(arr-geo['minus'],axis=1)
    fig,ax=plt.subplots(figsize=(9.1,4.6),constrained_layout=True)
    ix=np.arange(len(arr)); w=.34
    ax.bar(ix-w/2,dplus,width=w,label='Candidato +')
    ax.bar(ix+w/2,dminus,width=w,label='Candidato −',alpha=.75)
    ax.set_xticks(ix,['Plano 1','Plano 2','Plano 3','Plano 4','Fuera del plano'])
    ax.set_ylabel('Distancia / u')
    ax.set_title('Cuatro relaciones coplanares no distinguen el signo de la altura')
    ax.legend()
    fig.savefig(OUT/'04_distancias_orientacion.png',bbox_inches='tight')
    plt.close(fig)

if __name__=='__main__':
    summary,rad,geo=write_results()
    make_plots(rad,geo)
    print(json.dumps({'radial_counts':summary['radial_counts'],'ranks':summary['ranks'],
        'off_plane_anchor_distances':summary['off_plane_anchor_distances'],
        'error':summary['unique_reconstruction_error'],
        'signed_volumes':summary['oriented_tetra_volumes']},ensure_ascii=False,indent=2))
