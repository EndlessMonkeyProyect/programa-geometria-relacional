# Independent test of the nontrivial direction of T3: same (x,y,z) => simultaneously conjugate.
import numpy as np
rng=np.random.default_rng(1)
I=np.eye(2,dtype=complex); s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
def mat(q0,v): return q0*I+1j*sum(v[i]*s[i] for i in range(3))
def rand_su2():
    q=rng.standard_normal(4); q/=np.linalg.norm(q); return q[0],q[1:]
def sig(U,V): t=lambda M: np.trace(M).real/2; return np.array([t(U),t(V),t(U@V)])
worst=0; worst_sig=0
for trial in range(2000):
    x,a=rand_su2(); y,b=rand_su2()
    U,V=mat(x,a),mat(y,b)
    # build a second pair with the SAME Gram data but from scratch, in a random frame
    na,nb=np.linalg.norm(a),np.linalg.norm(b); c=a@b
    e1=rng.standard_normal(3); e1/=np.linalg.norm(e1)
    e2=rng.standard_normal(3); e2-=e2@e1*e1; e2/=np.linalg.norm(e2)
    a2=na*e1
    cos=c/(na*nb); sin=np.sqrt(max(0,1-cos**2))
    b2=nb*(cos*e1+(rng.choice([-1,1]))*sin*e2)   # either orientation
    U2,V2=mat(x,a2),mat(y,b2)
    worst_sig=max(worst_sig,np.abs(sig(U,V)-sig(U2,V2)).max())
    # find R in SO(3) with R a=a2, R b=b2 (Kabsch on {a,b,a x b})
    A=np.stack([a,b,np.cross(a,b)],1); B=np.stack([a2,b2,np.cross(a2,b2)],1)
    H=A@B.T; Uu,_,Vt=np.linalg.svd(H); d=np.sign(np.linalg.det(Vt.T@Uu.T))
    R=Vt.T@np.diag([1,1,d])@Uu.T
    # lift R to g in SU(2): rotation axis/angle
    ang=np.arccos(np.clip((np.trace(R)-1)/2,-1,1))
    if ang<1e-12: g=I
    else:
        w=np.array([R[2,1]-R[1,2],R[0,2]-R[2,0],R[1,0]-R[0,1]])
        if np.linalg.norm(w)<1e-9:  # angle ~ pi
            M=(R+np.eye(3))/2; k=np.argmax(np.diag(M)); w=M[:,k]
        w/=np.linalg.norm(w); g=np.cos(ang/2)*I-1j*np.sin(ang/2)*sum(w[i]*s[i] for i in range(3))
    for gg in (g, g.conj().T):
        err=max(np.abs(gg@U@gg.conj().T-U2).max(),np.abs(gg@V@gg.conj().T-V2).max())
        if err<1e-8: break
    worst=max(worst,err)
print("max diferencia de firma:",worst_sig)
print("max error de conjugacion encontrada (2000 pares, ambas orientaciones):",worst)
