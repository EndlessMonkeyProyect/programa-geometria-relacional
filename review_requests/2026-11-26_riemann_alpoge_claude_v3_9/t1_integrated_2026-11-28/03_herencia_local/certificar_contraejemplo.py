"""Control por intervalos de la transición S={11}, p=13.
Vasyunin, como en el anexo v1.4; todos los datos se forman desde enteros.
Requiere mpmath. Sin conversión previa a float.
"""
from mpmath import iv
from math import gcd
iv.dps = 50

def V(h,k):
    return sum((iv.mpf((m*h)%k)/k)*iv.cos(iv.pi*m/k)/iv.sin(iv.pi*m/k) for m in range(1,k))

def gram(a,b):
    g=gcd(a,b); h,k=sorted((a//g,b//g))
    return ((iv.log(2*iv.pi)-iv.euler)/2*(1/iv.mpf(h)+1/iv.mpf(k)) + iv.mpf(k-h)/(2*h*k)*iv.log(iv.mpf(h)/k)-iv.pi/(2*h*k)*(V(h,k)+V(k,h)))/g

def b(d):
    return (iv.log(d)+1-iv.euler)/d

def q(ds):
    A=[[gram(d,e) for e in ds]+[b(d)] for d in ds]; n=len(ds)
    for i in range(n):
        assert A[i][i].a>0
        for j in range(i+1,n):
            c=A[j][i]/A[i][i]
            for k in range(i+1,n+1): A[j][k]-=c*A[i][k]
    x=[iv.mpf(0)]*n
    for i in reversed(range(n)):
        x[i]=(A[i][n]-sum(A[i][j]*x[j] for j in range(i+1,n)))/A[i][i]
    return 1-sum(b(d)*a for d,a in zip(ds,x))

Q=q([1,11]); Qp=q([1,11,13,143]); val=13*(Q-Qp)/Q
assert Q.a>0 and Qp.a>0
assert val.a>iv.mpf('0.70261') and val.b<iv.mpf('0.70263')
print('Q_S =',Q)
print('Q_S+p =',Qp)
print('13 eta_13 =',val)
print('CERTIFICADO (aritmetica de intervalos mpmath.iv, formula Vasyunin): 0.70261 < 13 eta_13 < 0.70263 < 1.')
print('Por R_{13,k} <= eta_13, ninguna profundidad k cumple 13 R_{13,k} >= 1 para S={11}.')
