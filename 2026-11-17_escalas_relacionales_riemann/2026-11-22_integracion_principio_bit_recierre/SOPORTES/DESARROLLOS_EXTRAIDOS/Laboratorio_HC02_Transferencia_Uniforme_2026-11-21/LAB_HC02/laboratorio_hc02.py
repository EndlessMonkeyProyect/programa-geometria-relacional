#!/usr/bin/env python3
"""HC-02: exact finite-scale transfer G from theta and inherited prime powers.
Only Python stdlib. Produces CSV and JSON; no RH claims.
"""
import csv
import json
import math
from array import array
from bisect import bisect_right
from pathlib import Path
from fractions import Fraction

ROOT=Path(__file__).resolve().parent
N=2_000_000
GAMMA=0.577215664901532860606512090082402431
CONSTANT=8*math.log(2)+48/math.e


def sieve(n):
    b=bytearray(b'\x01')*(n+1)
    b[0:2]=b'\x00\x00'
    for d in range(2,math.isqrt(n)+1):
        if b[d]: b[d*d:n+1:d]=b'\x00'*((n-d*d)//d+1)
    return [p for p in range(2,n+1) if b[p]]


def assemble(n,primes):
    lam=array('d',[0])*(n+1)
    prime_w=array('d',[0])*(n+1)
    powers=[]
    for p in primes:
        w=math.log(p)
        prime_w[p]=w
        q=p
        k=1
        while q<=n:
            lam[q]=w
            if k>=2:powers.append((q,w,p,k))
            if q>n//p:break
            q*=p;k+=1
    psi=array('d',[0])*(n+1)
    theta=array('d',[0])*(n+1)
    aps=array('d',[0])*(n+1)
    ath=array('d',[0])*(n+1)
    for i in range(1,n+1):
        psi[i]=psi[i-1]+lam[i]
        theta[i]=theta[i-1]+prime_w[i]
        aps[i]=aps[i-1]+lam[i]/i
        ath[i]=ath[i-1]+prime_w[i]/i
    return psi,theta,aps,ath,powers


def value_g(x,psi,aps):
    return x*aps[x]-psi[x]-x*(math.log(x)-1-GAMMA)


def integral_error(x,y,phi,A):
    # Integral_x^y (phi(t)-t)/t^2 dt, phi cumulative weighted step function
    return phi[x]/x +(A[y]-A[x])-phi[y]/y -math.log(y/x)


def inherited(x,primes,z):
    h=0.0;theta=0.0
    for p in primes:
        if p>z:break
        lp=math.log(p)
        q=1;k=0
        while q<=x//p:q*=p;k+=1
        assert k>=1
        h+=lp*(k+x/(q*(p-1)))
        theta+=lp
    return h,theta


def power_error_direct(x,y,powers):
    # x * Integral_x^y U(t)/t^2 dt via positive summands
    # U(t)=sum_{p^k<=t,k>=2} log p
    return x*math.fsum(w*(1/max(x,q)-1/y) for q,w,p,k in powers if q<=y)


def elementary_tail_bound(x,Y):
    # For p>Y, sum log(p)/(p(p-1)) <= sum_n>Y <= integral_Y^inf log(t)/(t-1)^2 dt
    return x*(math.log(Y)/(Y-1)+math.log(Y/(Y-1)))


def rational_proof_checks():
    # Independent exact coefficient checks in Q for the contribution log(p).
    c=0
    for x in range(4,161):
        for p in (2,3,5,7,11,13,17,19,23):
            if p>x:continue
            q=1;k=0
            while q<=x//p:q*=p;k+=1
            direct=sum((Fraction(x,p**j)-1 for j in range(1,k+1)),Fraction(0))
            inherited=Fraction(x,p-1)-k-Fraction(x,q*(p-1))
            assert direct==inherited
            if p<=math.isqrt(x):
                # Prime-power tail truncated at x, completed to infinity.
                bpower=Fraction(k-1)+Fraction(x,q*(p-1))
                h=Fraction(k)+Fraction(x,q*(p-1))
                assert bpower==h-1
            c+=1
    # At x=p^2 a new reference is promoted to inherited; jumps match exactly.
    for p in (2,3,5,7,11,13):
        x=p*p
        delta_d=Fraction(x,p-1)-(p-1)
        delta_h=2+Fraction(1,p-1)
        assert delta_d==delta_h
        c+=1
    return c


def main():
    print('Criba hasta',N)
    ps=sieve(N)
    psi,theta,aps,ath,powers=assemble(N,ps)
    checks=rational_proof_checks()
    gY=value_g(N,psi,aps)
    Y=N
    samples=sorted(set([100,300,1000,3000,10000,30000,100000,300000,1000000] + 
                       [int(round(math.exp(math.log(100)+j*(math.log(1000000)-math.log(100))/299))) for j in range(300)]))
    rows=[]
    max_error=0.0
    max_constant=0.0
    max_pos=0.0
    max_abs=0.0
    for x in samples:
        g=value_g(x,psi,aps)
        I_theta=integral_error(x,Y,theta,ath)
        I_psi=integral_error(x,Y,psi,aps)
        iu=power_error_direct(x,Y,powers)/x
        assert iu>=-1e-11
        assert abs(I_psi-I_theta-iu)<1e-9, ('separation',x,I_psi-I_theta,iu)
        g_recon=x/Y*gY-x*(I_theta+iu)
        error=abs(g-g_recon)
        max_error=max(max_error,error)
        assert error<=2e-6 + 2e-11*x,(x,error)
        # Theorem: the one-sided finite-scale inequality is unconditional.
        upper=(x/Y)*gY-x*I_theta
        assert -CONSTANT*math.sqrt(x)-1e-6<=g-upper<=1e-6,(x,g,upper)
        max_constant=max(max_constant, (x*iu)/math.sqrt(x))
        max_pos=max(max_pos,g/math.sqrt(x))
        max_abs=max(max_abs,abs(g)/math.sqrt(x))
        rows.append(dict(x=x,G=g,G_sqrt=g/math.sqrt(x),theta_part=-x*I_theta,
             theta_part_sqrt=-x*I_theta/math.sqrt(x),power_part=-x*iu,
             power_part_sqrt=-x*iu/math.sqrt(x),boundary=(x/Y)*gY,
             boundary_sqrt=(x/Y)*gY/math.sqrt(x),reconstructed=g_recon,
             abs_error=error,upper=upper,gap=upper-g))

    with (ROOT/'escalas.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)

    checks2=0
    detailed=[]
    for x in (1000,10000,100000,1000000):
        z=math.isqrt(x)
        h,thetaz=inherited(x,ps,z)
        tail_finite=math.fsum(math.log(p)/(p*(p-1)) for p in ps if p>z)
        bpow_Y=h-thetaz+x*tail_finite
        # Independently reconstruct B_pow,Y as sum_p min(1,x/p^k) with infinite k-tail.
        direct=0.0
        for p in ps:
            if p<=z:
                q=1;k=0
                while q<=x//p:q*=p;k+=1
                direct+=math.log(p)*(k-1 + x/(q*(p-1)))
            else:
                direct+=x*math.log(p)/(p*(p-1))
        err=abs(direct-bpow_Y)
        assert err<2e-7,(x,err)
        checks2+=1
        offset=thetaz-x*tail_finite
        table=dict(x=x,z=z,G=value_g(x,psi,aps),H=h,H_sqrt=h/math.sqrt(x),theta_z=thetaz,
                   Bpow_finite=bpow_Y,Bpow_over_sqrt=bpow_Y/math.sqrt(x),
                   boundary_flux_approx=offset,flux_over_sqrt=offset/math.sqrt(x),
                   tail_bound=elementary_tail_bound(x,Y),max_reconstruction_error=err)
        detailed.append(table)
    with (ROOT/'frontera.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=detailed[0].keys());w.writeheader();w.writerows(detailed)

    cutoffs=[]
    for x in (10000,100000,1000000):
        g=value_g(x,psi,aps)
        for a in (0.35,0.45,0.50,0.55,0.65):
            z=math.floor(x**a)
            h,t=inherited(x,ps,z)
            cutoffs.append(dict(x=x,alpha=a,z=z,H=h,H_sqrt=h/math.sqrt(x),
                                D=g+h,D_sqrt=(g+h)/math.sqrt(x),G=g))
    with (ROOT/'cortes.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=cutoffs[0].keys());w.writeheader();w.writerows(cutoffs)

    meta={'N':N,'prime_count':len(ps),'prime_powers_count':len(powers),
          'samples':len(samples),'rational_checks':checks,'boundary_checks':checks2,
          'max_finite_identity_absolute_error':max_error,'theorem_constant':CONSTANT,
          'max_observed_normalized_power_correction':max_constant,
          'max_observed_G_over_sqrt':max_pos,'max_observed_abs_G_over_sqrt':max_abs,
          'G_terminal':gY,'G_terminal_normalized':gY/math.sqrt(Y),
          'sampling_note':'Finite sample in [100, 1000000]; these maxima are not global mathematical bounds.'}
    (ROOT/'metadatos.json').write_text(json.dumps(meta,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(meta,indent=2,ensure_ascii=False))
    print('Frontera:')
    for d in detailed: print({k:round(v,5) if isinstance(v,float) else v for k,v in d.items()})

if __name__=='__main__': main()
