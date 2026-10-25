"""
MF-96 / Rama Navier–Stokes — experimento E-NS.

DNS pseudo-espectral incompresible (caja periódica 2π, sin forzamiento) con
condición inicial Taylor–Green. Mide, en el punto de vorticidad máxima y en
la población de alta vorticidad:

  D_t q = α q + ν Δq − ν q |∇ξ|²        (q = |ω|, ξ = ω/q, α = ξ·Sξ)

  * α           : amplificación (estiramiento), no local vía Biot–Savart
  * ν Δq / q    : resolución radial (difusión fuera del núcleo)
  * ν |∇ξ|²     : resolución por no coincidencia local de direcciones
  * κ = α q /(ν|Δq|) : balance de la identidad (κ = 1 en un vórtice de Burgers estacionario)
  * b = P⊥(D_t ω)/q  : giro temporal (variable de MF-95)  vs  |∇ξ| espacial

Uso: python3 ns_taylor_green.py N Re Tend dt outdir
"""
import sys, json, time
import numpy as np
import scipy.fft as sfft

N = int(sys.argv[1]) if len(sys.argv) > 1 else 96
Re = float(sys.argv[2]) if len(sys.argv) > 2 else 400.0
Tend = float(sys.argv[3]) if len(sys.argv) > 3 else 10.0
dt = float(sys.argv[4]) if len(sys.argv) > 4 else 0.01
outdir = sys.argv[5] if len(sys.argv) > 5 else "."
nu = 1.0 / Re
WK = 2

k1 = sfft.fftfreq(N, 1.0 / N)
kz1 = sfft.rfftfreq(N, 1.0 / N)
KX, KY, KZ = np.meshgrid(k1, k1, kz1, indexing="ij")
K = np.array([KX, KY, KZ])
K2 = KX**2 + KY**2 + KZ**2
K2inv = np.where(K2 == 0, 0.0, 1.0 / np.where(K2 == 0, 1.0, K2))
kcut = N // 3
mask = (np.abs(KX) < kcut) & (np.abs(KY) < kcut) & (np.abs(KZ) < kcut)


def fwd(f):
    return sfft.rfftn(f, axes=(-3, -2, -1), workers=WK)


def inv(fh):
    return sfft.irfftn(fh, s=(N, N, N), axes=(-3, -2, -1), workers=WK)


def curl_hat(uh):
    return 1j * np.array([K[1] * uh[2] - K[2] * uh[1],
                          K[2] * uh[0] - K[0] * uh[2],
                          K[0] * uh[1] - K[1] * uh[0]])


def project(fh):
    kdot = (K[0] * fh[0] + K[1] * fh[1] + K[2] * fh[2]) * K2inv
    return fh - K * kdot


def rhs(uh):
    u = inv(uh)
    w = inv(curl_hat(uh))
    nl = np.array([u[1] * w[2] - u[2] * w[1],
                   u[2] * w[0] - u[0] * w[2],
                   u[0] * w[1] - u[1] * w[0]])
    return project(fwd(nl) * mask) - nu * K2 * uh


# ---------- condición inicial Taylor–Green ----------
x = 2 * np.pi * np.arange(N) / N
X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
u0 = np.array([np.sin(X) * np.cos(Y) * np.cos(Z),
               -np.cos(X) * np.sin(Y) * np.cos(Z),
               np.zeros_like(X)])
uh = project(fwd(u0) * mask)
del X, Y, Z, u0


def fields(uh):
    """Campos físicos necesarios para los diagnósticos."""
    u = inv(uh)
    wh = curl_hat(uh)
    w = inv(wh)
    # A_ij = ∂_j u_i
    A = np.empty((3, 3, N, N, N))
    for i in range(3):
        A[i] = inv(1j * K * uh[i][None])
    # G_ij = ∂_j ω_i
    G = np.empty((3, 3, N, N, N))
    for i in range(3):
        G[i] = inv(1j * K * wh[i][None])
    Lw = inv(-K2 * wh)  # Δω
    return u, w, A, G, Lw


def point_diag(w, A, G, Lw, idx):
    i, j, k = idx
    om = w[:, i, j, k]
    q = np.linalg.norm(om)
    xi = om / q
    Ap = A[:, :, i, j, k]
    S = 0.5 * (Ap + Ap.T)
    alpha = xi @ S @ xi
    Gp = G[:, :, i, j, k]               # Gp[a,b] = ∂_b ω_a
    proj = xi @ Gp                       # (ξ·∂_b ω)_b
    dxi = (Gp - np.outer(xi, proj)) / q  # ∂_b ξ_a
    gradxi2 = float(np.sum(dxi**2))
    xiLw = float(xi @ Lw[:, i, j, k])
    lapq = xiLw + q * gradxi2
    Dtw = S @ om + nu * Lw[:, i, j, k]
    b = (Dtw - xi * (xi @ Dtw)) / q
    return dict(q=float(q), alpha=float(alpha), gradxi2=gradxi2,
                nu_gradxi2=float(nu * gradxi2), nu_lapq_over_q=float(nu * lapq / q),
                growth_pred=float(alpha + nu * xiLw / q),
                kappa=float(alpha * q / (nu * abs(lapq))) if lapq < 0 else float("nan"),
                Theta=float(alpha / (nu * gradxi2)) if gradxi2 > 0 else float("inf"),
                b_norm=float(np.linalg.norm(b)),
                Rid2=float(q / abs(lapq)) if lapq < 0 else float("nan"))


def population_stats(w, A, G, Lw, t):
    q = np.linalg.norm(w, axis=0)
    qs = np.where(q > 0, q, 1.0)
    xi = w / qs
    S = 0.5 * (A + A.transpose(1, 0, 2, 3, 4))
    Sxi = np.einsum("ab...,b...->a...", S, xi)
    alpha = np.einsum("a...,a...->...", xi, Sxi)
    proj = np.einsum("a...,ab...->b...", xi, G)
    dxi = (G - xi[:, None] * proj[None, :]) / qs
    gradxi2 = np.sum(dxi**2, axis=(0, 1))
    xiLw = np.einsum("a...,a...->...", xi, Lw)
    lapq = xiLw + q * gradxi2
    Dtw = np.einsum("ab...,b...->a...", S, w) + nu * Lw
    b = (Dtw - xi * np.einsum("a...,a...->...", xi, Dtw)[None]) / qs
    bnorm = np.linalg.norm(b, axis=0)
    # no coincidencia local a separación r (en celdas): media de |ξ(x) × ξ(x ± r e_i)|
    mis = {}
    for r in (1, 2, 4):
        acc = np.zeros_like(q)
        for ax in (1, 2, 3):
            for s in (r, -r):
                xs = np.roll(xi, s, axis=ax)
                cr = np.cross(xi, xs, axis=0)
                acc += np.linalg.norm(cr, axis=0)
        mis[r] = acc / 6.0
    qf = q.ravel()
    p = np.percentile(qf, [50, 90, 99, 99.9])
    bins = [("50-90", p[0], p[1]), ("90-99", p[1], p[2]),
            ("99-99.9", p[2], p[3]), ("99.9-100", p[3], np.inf)]
    out = dict(t=t, q_p50=p[0], q_p90=p[1], q_p99=p[2], q_p999=p[3], q_max=float(qf.max()), bins={})
    for name, lo, hi in bins:
        m = (q >= lo) & (q < hi)
        rec = dict(n=int(m.sum()))
        for r in (1, 2, 4):
            rec[f"mis_r{r}"] = float(mis[r][m].mean())
        rec["alpha_over_q_mean"] = float((alpha[m] / q[m]).mean())
        rec["alpha_pos_frac"] = float((alpha[m] > 0).mean())
        rec["gradxi_median"] = float(np.median(np.sqrt(gradxi2[m])))
        rec["b_over_q_median"] = float(np.median(bnorm[m] / q[m]))
        neg = m & (lapq < 0) & (alpha > 0)
        rec["kappa_median"] = float(np.median(alpha[neg] * q[neg] / (nu * np.abs(lapq[neg])))) if neg.any() else None
        th = m & (gradxi2 > 0) & (alpha > 0)
        rec["Theta_median"] = float(np.median(alpha[th] / (nu * gradxi2[th]))) if th.any() else None
        rec["Theta_gt1_frac"] = float((alpha[th] / (nu * gradxi2[th]) > 1).mean()) if th.any() else None
        # comparación temporal b vs espacial ∇ξ (rangos de Spearman)
        if m.sum() > 20:
            from scipy.stats import spearmanr
            rho, _ = spearmanr(bnorm[m], np.sqrt(gradxi2[m]))
            rec["spearman_b_vs_gradxi"] = float(rho)
            rho2, _ = spearmanr(alpha[m] / q[m], mis[2][m])
            rec["spearman_alphaq_vs_mis2"] = float(rho2)
        out["bins"][name] = rec
    return out


nsteps = int(round(Tend / dt))
ndiag = max(1, int(round(0.05 / dt)))
pop_times = {2.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0}
series, pops = [], []
t0 = time.time()
for n in range(nsteps + 1):
    t = n * dt
    if n % ndiag == 0:
        u, w, A, G, Lw = fields(uh)
        q = np.linalg.norm(w, axis=0)
        idx = np.unravel_index(np.argmax(q), q.shape)
        d = point_diag(w, A, G, Lw, idx)
        d["t"] = t
        d["E"] = float(0.5 * np.mean(np.sum(u**2, axis=0)))
        d["Z"] = float(0.5 * np.mean(np.sum(w**2, axis=0)))
        d["eps"] = float(2 * nu * d["Z"])
        d["idx"] = [int(v) for v in idx]
        series.append(d)
        if any(abs(t - tp) < 1e-9 for tp in pop_times):
            pops.append(population_stats(w, A, G, Lw, t))
        if n % (ndiag * 20) == 0:
            print(f"t={t:6.2f} E={d['E']:.5f} eps={d['eps']:.5f} qmax={d['q']:.3f} "
                  f"alpha={d['alpha']:.3f} kappa={d['kappa']:.3f} elapsed={time.time()-t0:.0f}s", flush=True)
        del u, w, A, G, Lw, q
    if n == nsteps:
        break
    k1_ = rhs(uh)
    k2_ = rhs(uh + 0.5 * dt * k1_)
    k3_ = rhs(uh + 0.5 * dt * k2_)
    k4_ = rhs(uh + dt * k3_)
    uh = uh + (dt / 6.0) * (k1_ + 2 * k2_ + 2 * k3_ + k4_)

# tasa de crecimiento observada de log q_max (diferencias centradas) para cotejar con α + ν ξ·Δω / q
ts = np.array([s["t"] for s in series])
lq = np.log(np.array([s["q"] for s in series]))
obs = np.gradient(lq, ts)
for s, o in zip(series, obs):
    s["growth_obs"] = float(o)

meta = dict(N=N, Re=Re, nu=nu, dt=dt, Tend=Tend, dealias="2/3 cubic", scheme="RK4 pseudo-spectral, rotational form",
            init="Taylor-Green", forcing="none", wallclock_s=time.time() - t0)
with open(f"{outdir}/ns_N{N}_Re{int(Re)}.json", "w") as fh:
    json.dump(dict(meta=meta, series=series, populations=pops), fh, indent=1)
print("done", meta)
