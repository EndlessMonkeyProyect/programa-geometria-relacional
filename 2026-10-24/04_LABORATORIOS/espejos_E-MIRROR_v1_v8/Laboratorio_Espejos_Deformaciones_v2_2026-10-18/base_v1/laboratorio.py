#!/usr/bin/env python3
"""Laboratorio de espejos: grupos planos exactos, observabilidad y orientaciones.

Es un modelo de imagen virtual de espejos planos ideales, NO ray tracing de
paredes finitas, óptica ondulatoria, teoría de la percepción ni prueba ontológica.
Ejecutar: python laboratorio.py --salida resultados.json
"""
from __future__ import annotations
from collections import Counter, deque
from fractions import Fraction
from itertools import product
import argparse, json

Mat = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
RX = ((-1, 0, 0), (0, 1, 0), (0, 0, 1))
RY = ((1, 0, 0), (0, -1, 0), (0, 0, 1))
RZ = ((1, 0, 0), (0, 1, 0), (0, 0, -1))
DXY = ((0, 1, 0), (1, 0, 0), (0, 0, 1))
DYZ = ((1, 0, 0), (0, 0, 1), (0, 1, 0))
DXZ = ((0, 0, 1), (0, 1, 0), (1, 0, 0))


def compose(a, b):
    """Aplicar b y después a."""
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def apply(m, p):
    return tuple(sum(row[j] * p[j] for j in range(3)) for row in m)


def det(m):
    a, b, c = m
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def generated_group(generators):
    found = {I}
    q = deque([I])
    while q:
        m = q.popleft()
        for g in generators:
            candidate = compose(g, m)
            if candidate not in found:
                found.add(candidate)
                q.append(candidate)
    return found


def orbit_report(generators, p):
    group = generated_group(generators)
    imgs = Counter(apply(g, p) for g in group)
    sign = Counter('directa_par' if det(g) == 1 else 'invertida_impar' for g in group)
    return {
        'transformaciones': len(group),
        'posiciones_virtuales_distintas': len(imgs),
        'multiplicidad_maxima_de_una_posicion': max(imgs.values()),
        'transformaciones_por_paridad': dict(sorted(sign.items())),
        'origen_hipotetico': list(p),
    }


def rank(a):
    mat = [[Fraction(x) for x in row] for row in a]
    if not mat: return 0
    nr, nc = len(mat), len(mat[0]); k=0
    for c in range(nc):
        t=next((i for i in range(k, nr) if mat[i][c]), None)
        if t is None: continue
        mat[k],mat[t]=mat[t],mat[k]
        denom=mat[k][c]
        mat[k]=[x/denom for x in mat[k]]
        for i in range(nr):
            if i!=k:
                factor=mat[i][c]
                mat[i]=[x-factor*y for x,y in zip(mat[i],mat[k])]
        k+=1
        if k==nr: break
    return k


def matrix_observation(projection, operation):
    return [list(r) for r in (compose(projection, operation) if len(projection)==3 else
        tuple(tuple(sum(projection[i][k] * operation[k][j] for k in range(3)) for j in range(3)) for i in range(len(projection))))]


def observations():
    pxy=((1,0,0),(0,1,0))
    py=((0,1,0),)
    ordinary=matrix_observation(pxy,I)
    copied=matrix_observation(pxy,RX)
    diagonal=matrix_observation(pxy,DXZ)
    opaque=matrix_observation(py,DXZ)
    return {
        'una_vista_xy_rango':rank(ordinary),
        'misma_direccion_con_reflejo_en_x_rango':rank(ordinary+copied),
        'segunda_vista_calibrada_con_intercambio_xz_rango':rank(ordinary+diagonal),
        'filtros_que_solo_dejan_y_rango':rank(matrix_observation(py,I)+opaque),
        'opacidad_exacta_z_cero_rango':rank([(1,0,0),(0,1,0),(0,0,0)]),
        'transmision_z_1_100_rango':rank([(1,0,0),(0,1,0),(0,Fraction(0),Fraction(1,100))]),
        'desplazamiento_z_1_medicion_1_100': '0.01',
        'umbral_de_ruido_ejemplo': '0.02',
        'accesibilidad_con_ruido': 'Una diferencia z=1, atenuada a 0.01, queda por debajo del umbral 0.02; el rango exacto 3 no garantiza distinguirla.',
    }


def virtual_cells(radius=2):
    """Centro p=(1/2,1/2,1/2) de caja [0,1]^3: imagen virtual en celda n es n+(1/2,1/2,1/2)."""
    grid=list(product(range(-radius,radius+1), repeat=3))
    signatures=Counter(tuple(abs(n)%2 for n in cell) for cell in grid)
    paridades=Counter('par' if sum(sig)%2==0 else 'impar' for sig,n in signatures.items() for _ in range(n))
    return {
        'radio_en_celdas':radius, 'celdas_virtuales':len(grid),
        'firmas_de_orientacion':len(signatures),
        'frecuencias_por_firma':{''.join(map(str,k)):v for k,v in sorted(signatures.items())},
        'paridades_totales':dict(sorted(paridades.items())),
        'posiciones_de_imagen_distintas':len({tuple(Fraction(n)+Fraction(1,2) for n in c) for c in grid}),
    }


def angle_group(degrees):
    """Orden de las reflexiones en dos rectas infinitas de ángulo racional en grados.
    Si ángulo/pi racional a/b, la rotación doble tiene orden b y el grupo diedral 2*b.
    NO equiparar grupo geométrico con imágenes visibles en espejos finitos.
    """
    x=Fraction(str(degrees))/180
    return {'angulo_grados':str(degrees), 'orden_de_la_rotacion_doble':x.denominator,
            'transformaciones_del_grupo_abstracto':2*x.denominator}


def attenuation_layers(reflectivity, detection_threshold='0.05'):
    """Modelo fotométrico simplificado: una imagen tras k rebotes tiene I/I0 = rho^k.
    No modela el tamaño del espejo, la dispersión ni interferencia.
    """
    rho=Fraction(str(reflectivity)); cutoff=Fraction(str(detection_threshold))
    if not (0 <= rho <= 1 and 0 < cutoff <= 1):
        raise ValueError('0 <= reflectividad <= 1; 0 < umbral <= 1')
    if rho==1:
        return {'reflectividad':str(reflectivity),'umbral':str(detection_threshold),
                'rebotes_maximos_detectables':None,'celdas_virtuales_en_bola_L1':None,
                'nota':'sin límite por atenuación, solamente en este modelo ideal'}
    k=0; intensity=Fraction(1)
    while intensity*rho >= cutoff and k < 100000:
        k+=1
        intensity*=rho
    # Celdas n enteras tales que |nx|+|ny|+|nz|<=k: suma exacta.
    cells=(4*k**3 + 6*k**2 + 8*k + 3)//3
    return {'reflectividad':str(reflectivity),'umbral':str(detection_threshold),
            'rebotes_maximos_detectables':k,'celdas_virtuales_en_bola_L1':cells,
            'intensidad_en_k':str(round(float(intensity),8)),
            'intensidad_en_k_mas_1':str(round(float(intensity*rho),8))}

def control_esfera_vs_objeto_asimetrico():
    """Esfera isotrópica frente a objeto de cuatro puntos ETIQUETADOS; acciones del grupo.
    Las copias pueden no ser realizables en un recinto con espejos diagonales materiales.
    """
    group=generated_group([RX,RY,RZ,DXY,DYZ])
    centro=(1,1,1)
    tetra=((0,0,0),(1,0,0),(0,2,0),(0,0,3))
    def add(a,b): return tuple(x+y for x,y in zip(a,b))
    esfera={apply(g,centro) for g in group}
    tetra_etiquetado={tuple(apply(g,add(centro,off)) for off in tetra) for g in group}
    return {
        'transformaciones':len(group),
        'esfera_homogenea_posiciones_de_centro_distintas':len(esfera),
        'esfera_homogenea_orientaciones_detectables_a_partir_de_su_forma':1,
        'cuatro_puntos_etiquetados_imagenes_completas_distintas':len(tetra_etiquetado),
        'nota':'Control de simetría de objeto, no un experimento realizado con esferas materiales.'
    }

def run():
    G0=[RX,RY,RZ]
    G1=G0+[DXY]
    G2=G1+[DYZ]
    return {
      'metadatos': {'nombre':'Continuacion E-MIRROR', 'base':'Programa v3.4.1, 18-10-2026',
                    'tipo':'modelos exactos de reflexion plana y observaciones lineales',
                    'no_es':'simulacion fotometrica ni prueba de singularidad ontologica'},
      'A_puntos_de_fuente_en_esquina_de_tres_planos':{
          'general_1_2_3':orbit_report(G0,(1,2,3)),
          'en_una_cara_0_2_3':orbit_report(G0,(0,2,3)),
          'en_una_arista_0_0_3':orbit_report(G0,(0,0,3)),
          'en_vertice_0_0_0':orbit_report(G0,(0,0,0)),
          'simetria_del_centro_1_1_1_con_diagonales':orbit_report(G2,(1,1,1)),
      },
      'B_diagonales_fuente_asimetrica':{
          'tres_perpendiculares':orbit_report(G0,(1,2,3)),
          'mas_diagonal_xy':orbit_report(G1,(1,2,3)),
          'mas_diagonal_yz':orbit_report(G2,(1,2,3)),
      },
      'C_cubo_cerrado_centro_celdas_virtuales':virtual_cells(2),
      'D_acceso_por_observacion_y_filtros':observations(),
      'E_angulos_dos_espejos_infinitos': [angle_group(k) for k in ('90','60','45','61','60.1')],
      'F_capas_de_reflexion_con_atenuacion_ideal': [attenuation_layers(x) for x in ('1','0.9','0.8','0.5')],
      'G_control_de_forma_esfera_frente_a_marcadores':control_esfera_vs_objeto_asimetrico(),
      'H_proposiciones_comprobables':{
          'cada_generador_reflejo_cuadra_a_identidad':all(compose(g,g)==I for g in [RX,RY,RZ,DXY,DYZ,DXZ]),
          'grupo_48_con_24_directas_y_24_invertidas':Counter(det(g) for g in generated_group(G2))=={1:24,-1:24},
          'en_la_fuente_central_simetrica_48_operaciones_producen_8_posiciones':len({apply(g,(1,1,1)) for g in generated_group(G2)})==8,
      }
    }

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--salida',default='resultados.json')
    args=parser.parse_args()
    content=run()
    with open(args.salida,'w',encoding='utf8') as f:
        json.dump(content,f,indent=2,ensure_ascii=False,sort_keys=True)
        f.write('\n')
    print('OK:',args.salida, '| resultados A–H calculados')
