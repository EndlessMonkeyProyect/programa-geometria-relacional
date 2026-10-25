import numpy as np
# Independent physical-space check of W, B, P for the E3 field (exact quadrature for trig polynomials on a fine grid)
n=24; g=2*np.pi*np.arange(n)/n; x,y,z=np.meshgrid(g,g,g,indexing='ij')
k1=np.fft.fftfreq(n,1/n); KX,KY,KZ=np.meshgrid(k1,k1,k1,indexing='ij'); K=[KX,KY,KZ]
def d(f,a): return np.fft.ifftn(1j*K[a]*np.fft.fftn(f)).real
for c in (1,-1):
    m=x+y+z
    u=[np.cos(y+z)+c*np.sin(m)+np.cos(z)/3, np.cos(x)+c*np.sin(m), -2*c*np.sin(m)]
    G=[[d(u[i],j) for j in range(3)] for i in range(3)]   # G[i][j]=du_i/dx_j
    w=[G[2][1]-G[1][2], G[0][2]-G[2][0], G[1][0]-G[0][1]]
    S=[[0.5*(G[i][j]+G[j][i]) for j in range(3)] for i in range(3)]
    W=np.mean(sum(wi**2 for wi in w)); B=np.mean(sum(d(w[i],j)**2 for i in range(3) for j in range(3)))
    P=np.mean(sum(w[i]*S[i][j]*w[j] for i in range(3) for j in range(3)))
    E=np.mean(sum(ui**2 for ui in u)); M=np.sqrt(E)
    print(f"c={c:+d}  W={W:.12f} (95/9={95/9:.12f})  B={B:.12f} (266/9={266/9:.12f})  P={P:.12f}  M^2={E:.6f} (73/18={73/18:.6f})")
# Homogeneity: T is P/M^3 by definition-scaling: scaling u->lam*u gives P->lam^3 P, M->lam M, so T invariant. Check numerically.
