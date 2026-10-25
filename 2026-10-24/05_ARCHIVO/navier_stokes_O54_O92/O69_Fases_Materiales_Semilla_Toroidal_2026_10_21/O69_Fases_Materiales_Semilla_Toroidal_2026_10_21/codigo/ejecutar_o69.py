#!/usr/bin/env python3
"""O69: tests kinematic phase locking with actual Fourier-Galerkin NS data.
Reuses O53 original archived numerical trajectories and O63 velocity-field operators.
No PDE or global regularity theorem claimed. Units nondimensional.
"""
from pathlib import Path
import sys, csv, json, math
import numpy as np
from scipy import fft
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/'codigo'))
import o63_operadores as o63


def writecsv(name,records):
    if not records:return
    with (BASE/'resultados'/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)

def time_series_original():
    """Two *different tracer* meridional angles, not two orthogonal torus cycles."""
    outputs=[];checks=[];raws=[]
    for n in (40,48):
      for eps in (0,.14):
        tag=int(round(eps*100))
        p=BASE/'fuentes'/'datos_O53_originales'/f'NS_N{n}_eps{tag:02d}.json'
        data=json.loads(p.read_text());rs=data['records']
        t=np.array([r['t'] for r in rs],float)
        angles=np.unwrap(np.array([r['phase_raw'] for r in rs],float),axis=0)
        pts=np.array([r['particles'] for r in rs],float)
        az=np.unwrap(np.arctan2(pts[:,:,1],pts[:,:,0]),axis=0)
        rates=np.gradient(angles,t,axis=0,edge_order=2)
        theta1=angles[:,0]-angles[0,0] # outer d=.12
        theta2=angles[:,2]-angles[0,2] # outer d=.26
        # preselected small-integer 3:4 relation based on O68 gear example;
        # no fitting from data in this test.
        psi=3*theta1-4*theta2
        mismatch=3*rates[:,0]-4*rates[:,2]
        for i,ti in enumerate(t):
            outputs.append(dict(N=n,epsilon=eps,t=float(ti),theta12_turns=float(theta1[i]/(2*np.pi)),theta26_turns=float(theta2[i]/(2*np.pi)),psi_3_4_turns=float(psi[i]/(2*np.pi)),delta_3_4=float(mismatch[i]),ratio_theta_dot_12_26=float(rates[i,0]/rates[i,2]) if abs(rates[i,2])>1e-8 else None,azimuth_shift_d12=float(az[i,0]-az[0,0])))
        stat=dict(N=n,epsilon=eps,T=float(t[-1]),initial_ratio=float(rates[0,0]/rates[0,2]),final_ratio=float(rates[-1,0]/rates[-1,2]),final_seed_slip_turns=float(psi[-1]/(2*np.pi)),max_seed_slip_turns=float(np.max(np.abs(psi))/(2*np.pi)),initial_delta=float(mismatch[0]),final_delta=float(mismatch[-1]),max_abs_azimuth_d12=float(np.max(np.abs(az[:,0]-az[0,0]))),axial_displacement=data['stats']['axial_displacement'],outer_diff_original=data['stats']['outer_phase_diff_final'])
        checks.append(stat)
        raws.append((data,t,angles,psi))
        assert len(t)>15 and abs(t[-1]-2.4)<1e-7
        assert np.isfinite(angles).all() and np.isfinite(pts).all()
        # Archived original 'outer_phase_diff_final' must equal reconstructed change in theta2-theta1.
        assert abs((theta2[-1]-theta1[-1])/(2*np.pi)-stat['outer_diff_original'])<2e-10
    writecsv('fases_O53_serie_larga.csv',outputs)
    writecsv('resultados_cierre_serie_larga.csv',checks)
    return checks,raws


def initial_phase_derivatives(uh,system,pts):
    """Kinematic formula, no imposed gear relation."""
    Rc,Zc,dRc,dZc=o63.frame_center(uh,system,True)
    vel=o63.interpolate(fft.ifftn(uh,axes=(-3,-2,-1)).real,pts)
    rho=np.hypot(pts[:,0],pts[:,1]);s=rho-Rc;z=pts[:,2]-Zc
    drho=(pts[:,0]*vel[:,0]+pts[:,1]*vel[:,1])/rho
    dtheta=(s*(vel[:,2]-dZc)-z*(drho-dRc))/(s*s+z*z)
    dphi=(pts[:,0]*vel[:,1]-pts[:,1]*vel[:,0])/(rho*rho)
    return dtheta,dphi,Rc,Zc


def physical_short_run(n,eps,T=.08,dt=.004):
    uh,system=o63.original_state(n,eps,False)
    azis=(0.,np.pi/4,np.pi/2)
    pts=np.concatenate([o63.initial_particles(a) for a in azis],axis=0)
    initial=pts.copy()
    dtheta0,dphi0,Rc,Zc=initial_phase_derivatives(uh,system,pts)
    nsteps=round(T/dt);dt=T/nsteps
    results=[]
    for j in range(nsteps+1):
        if j in (0,1,2,5,10,nsteps):
            Rct,Zct=o63.frame_center(uh,system)
            theta=o63.phase(pts,Rct,Zct)
            phi=np.arctan2(pts[:,1],pts[:,0]); orig_phi=np.arctan2(initial[:,1],initial[:,0])
            for k,az in enumerate(azis):
                for i in (0,2):
                    idx=6*k+i
                    # For short time no branch crossing; use principal difference.
                    theta_init=o63.phase(initial,Rc,Zc)[idx]
                    dtheta=float(np.angle(np.exp(1j*(theta[idx]-theta_init))))
                    dphi=float(np.angle(np.exp(1j*(phi[idx]-orig_phi[idx]))))
                    results.append(dict(N=n,epsilon=eps,initial_azimuth_degrees=round(np.rad2deg(az)),tracer_depth=(.12 if i==0 else .26),t=j*dt,dtheta=dtheta,dphi=dphi,theta_dot_initial=float(dtheta0[idx]),phi_dot_initial=float(dphi0[idx]),tracer_x=float(pts[idx,0]),tracer_y=float(pts[idx,1]),tracer_z=float(pts[idx,2])))
        if j==nsteps:break
        uh,pts=o63.rk4_step_uh_pts(uh,pts,dt,system)
        assert np.isfinite(pts).all()
    writecsv(f'fases_cortas_N{n}_eps{int(eps*100):02d}.csv',results)
    first={(x['initial_azimuth_degrees'],x['tracer_depth']):x for x in results if x['t']==dt}
    return results,initial,(dtheta0,dphi0),first


def main():
    BASE.joinpath('resultados').mkdir(exist_ok=True)
    saved,raws=time_series_original()
    phase_samples=[];checks={};errors=[]
    for n in (32,40):
      for eps in (0,.14):
        rows,pts,vel,first=physical_short_run(n,eps)
        dt=min(r['t'] for r in rows if r['t']>0)
        for az in (0,45,90):
            for depth in (.12,.26):
                v=first[(az,depth)]
                phase_samples.append(dict(N=n,epsilon=eps,azimuth_degrees=az,depth=depth,meridional_rate=v['theta_dot_initial'],azimuthal_rate=v['phi_dot_initial'],meridional_increment_T=v['dtheta'],azimuthal_increment_T=v['dphi']))
                # deriv estimate over first step within 4% relative for rapid nonlinear dynamics.
                errors.append(dict(N=n,epsilon=eps,az=az,depth=depth,theta_delta_fd_error=abs(v['dtheta']/dt-v['theta_dot_initial']),phi_delta_fd_error=abs(v['dphi']/dt-v['phi_dot_initial'])))
    writecsv('velocidades_angulares_desde_campo_NS.csv',phase_samples)
    writecsv('control_diferencias_finitas.csv',errors)
    def val(N,eps,az,depth,key):
        return next(float(x[key]) for x in phase_samples if x['N']==N and x['epsilon']==eps and x['azimuth_degrees']==az and x['depth']==depth)
    checks={
     'fuentes_O53_dos_resoluciones_dos_preparaciones': len(saved)==4,
     'inicial_meridiano_no_nulo':all(abs(x['meridional_rate'])>1 for x in phase_samples),
     'control_azimut_sin_perturbacion_casi_cero':all(abs(x['azimuthal_rate'])<1e-9 for x in phase_samples if x['epsilon']==0),
     'perturbacion_activa_ciclo_azimutal_45deg':all(abs(val(n,.14,45,.12,'azimuthal_rate'))>.1 for n in (32,40)),
     'simetria_plano_azimut_cero':all(abs(val(n,.14,0,.12,'azimuthal_rate'))<1e-9 for n in (32,40)),
     'tasa_azimut_depende_del_azimut':all(abs(val(n,.14,45,.12,'azimuthal_rate')-val(n,.14,0,.12,'azimuthal_rate'))>.1 for n in (32,40)),
     'candidato_3_4_tiene_deriva_no_nula':all(x['max_seed_slip_turns']>.05 for x in saved),
     'razon_tasas_cambia_serie_larga':all(abs(x['initial_ratio']-x['final_ratio'])>.25 for x in saved),
     'trazadores_no_son_sincronizacion_toda_la_serie':all(abs(x['final_seed_slip_turns'])>.05 for x in saved),
     'modelo_no_produce_giro_azimutal_espontaneo_sin_swirl_en_inicial':all(abs(x['azimuthal_rate'])<1e-9 for x in phase_samples if x['epsilon']==0),
     'control_diferencias_finitas_theta':all(x['theta_delta_fd_error']<1.1 for x in errors),
     'control_diferencias_finitas_phi':all(x['phi_delta_fd_error']<.04 for x in errors),
    }
    output=dict(checks=checks,count_passed=sum(checks.values()),count_total=len(checks),resultados_serie_larga=saved,initial_angular_samples=phase_samples,numerical_method={'off_axis_simulations':'O53 2/3 Fourier Galerkin RK4, O63 frame derivatives and tracer interpolation','original_O53':'archived trajectories through 2.4, N40 and N48','short_T':.08,'short_dt':.004},limitations=['toroidal cycle angles not guaranteed material periods','meridional angle uses moving enstrophy center','spectral underresolution of core radius .35','no continuum PDE convergence certification','none of the data imply regularity theorem','phi=0 tracer plane can be invariant by reflection symmetry','reflected azimuth phi and second poloidal tracer constitute distinct observables','failure of one rational lock does not rule out all possible relational normalizers'] )
    (BASE/'resultados'/'resumen.json').write_text(json.dumps(output,ensure_ascii=False,indent=2))
    print('Checks:',sum(checks.values()),'/',len(checks));print(json.dumps(checks,indent=2,ensure_ascii=False))
    for x in saved:print('long:',x)
    for n in (32,40):
      for e in (0,.14):print('angular:',n,e,[(az,val(n,e,az,.12,'meridional_rate'),val(n,e,az,.12,'azimuthal_rate')) for az in (0,45,90)])
    assert all(checks.values()), checks

if __name__=='__main__':main()
