"""Figuras de MF-96 a partir de los resultados JSON (paleta validada, superficie clara)."""
import json, math, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = "/home/claude/mf96/results"
F = "/home/claude/mf96/figs"

SURF = "#fcfcfb"; INK = "#0b0b0b"; INK2 = "#52514e"; MUTED = "#898781"
GRID = "#e1e0d9"; AXIS = "#c3c2b7"
C1, C2, C3, C4 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"

plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "font.family": "DejaVu Sans", "font.size": 10,
    "axes.edgecolor": AXIS, "axes.linewidth": 0.8, "axes.labelcolor": INK2,
    "xtick.color": MUTED, "ytick.color": MUTED, "xtick.labelcolor": INK2, "ytick.labelcolor": INK2,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7, "grid.linestyle": "-",
    "axes.spines.top": False, "axes.spines.right": False,
    "legend.frameon": False, "legend.labelcolor": INK2,
    "axes.titlecolor": INK, "axes.titlesize": 11, "axes.titleweight": "bold", "axes.titlelocation": "left",
})


def line(ax, x, y, c, label, marker="o", **kw):
    ax.plot(x, y, color=c, lw=2, solid_capstyle="round", solid_joinstyle="round",
            marker=marker, ms=6.5, mfc=c, mec=SURF, mew=1.6, label=label, **kw)


def endlabel(ax, x, y, text, dy=0, dx=6):
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points", va="center", ha="left",
                color=INK2, fontsize=9)


# ---------------------------------------------------------------- E1 · P vs NP
def fig_pnp():
    ts = json.load(open(f"{R}/pnp/pnp_tseitin.json"))["rows"]
    s2 = json.load(open(f"{R}/pnp/pnp_sat2.json"))["rows"]
    s3 = json.load(open(f"{R}/pnp/pnp_sat3.json"))["rows"]
    fig, ax = plt.subplots(figsize=(7.6, 5.4))
    nv = sorted(set(r["n_vars"] for r in ts))
    med_c = [np.median([r["clause"]["max_clauses"] for r in ts if r["n_vars"] == v]) for v in nv]
    max_c = [np.max([r["clause"]["max_clauses"] for r in ts if r["n_vars"] == v]) for v in nv]
    min_c = [np.min([r["clause"]["max_clauses"] for r in ts if r["n_vars"] == v]) for v in nv]
    lin = [np.max([r["linear"]["max_equations"] for r in ts if r["n_vars"] == v]) for v in nv]
    ax.fill_between(nv, min_c, max_c, color=C1, alpha=0.10, lw=0)
    line(ax, nv, med_c, C1, "Tseitin · lenguaje de cláusulas (mediana; banda = rango de 5 semillas)")
    line(ax, nv, lin, C3, "Tseitin · lenguaje lineal sobre F₂ (máximo)", marker="s")
    n3 = sorted(set(r["n"] for r in s3))
    med3 = [np.median([r["clause"]["max_clauses"] for r in s3 if r["n"] == v]) for v in n3]
    line(ax, n3, med3, C2, "3-SAT aleatorio en el umbral · cláusulas (mediana)", marker="^")
    n2 = sorted(set(r["n"] for r in s2))
    m2 = [np.max([r["clause"]["max_clauses"] for r in s2 if r["n"] == v]) for v in n2]
    keep = [i for i, v in enumerate(n2) if v <= 40]
    line(ax, [n2[i] for i in keep], [m2[i] for i in keep], C4, "2-SAT aleatorio · cláusulas (máximo; sigue lineal hasta n = 640, ver tabla)", marker="D")
    ax.set_yscale("log")
    ax.set_xlim(8, 56)
    ax.set_xlabel("número de variables")
    ax.set_ylabel("tamaño máximo de la interfaz\n(cláusulas o ecuaciones)")
    ax.set_title("E1 · La misma identidad cuesta distinto según el lenguaje")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), fontsize=8.5, ncol=1)
    endlabel(ax, nv[-1], med_c[-1], num_s(med_c[-1]))
    endlabel(ax, nv[-1], lin[-1], f"{int(lin[-1])}")
    endlabel(ax, n3[-1], med3[-1], num_s(med3[-1]), dy=6)
    fig.tight_layout()
    fig.savefig(f"{F}/E1_dos_lenguajes.png", dpi=170)
    plt.close(fig)


def num_s(x):
    return f"{int(x):,}".replace(",", " ")


# ---------------------------------------------------------------- E2 · O(3) vs O(2)
def fig_on():
    r = json.load(open(f"{R}/ym/on_sigma_2d.json"))
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    spec = [((3, 1.5), C1, "O(3), β = 1.5 (no abeliano)", "o"),
            ((3, 1.7), C3, "O(3), β = 1.7 (no abeliano, acoplamiento más débil)", "s"),
            ((2, 1.3), C2, "O(2), β = 1.3 (abeliano, acoplamiento débil)", "^"),
            ((2, 0.9), C4, "O(2), β = 0.9 (abeliano, acoplamiento fuerte)", "D")]
    for (n, b), c, lab, mk in spec:
        rows = sorted([x for x in r if x["n"] == n and x["beta"] == b], key=lambda x: x["L"])
        L = [x["L"] for x in rows]; y = [x["xi_over_L"] for x in rows]; e = [x["xi_over_L_err"] for x in rows]
        line(ax, L, y, c, lab, marker=mk)
        ax.errorbar(L, y, yerr=e, fmt="none", ecolor=c, elinewidth=1, capsize=0)
    ax.set_xscale("log", base=2)
    ax.set_xticks([8, 16, 32, 64, 128]); ax.set_xticklabels(["8", "16", "32", "64", "128"])
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("tamaño de la caja L (cada paso = un nivel de la recursión de escala)")
    ax.set_ylabel("ξ(L) / L")
    ax.set_title("E2 · ¿La recursión de escala termina en cierre?")
    ax.legend(loc="lower left", fontsize=8.5)
    fig.tight_layout()
    fig.savefig(f"{F}/E2_recursion_O3_O2.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- E3/E4 · continuidad y Creutz
def fig_gauge():
    sc = json.load(open(f"{R}/ym/ym_scan.json"))
    wl = json.load(open(f"{R}/ym/ym_wilson_L10.json"))
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.2, 4.2))
    for g, ax_title in [("U1", None)]:
        for start, c, mk, lab in [("frio", C1, "o", "U(1) · arranque frío"), ("caliente", C2, "^", "U(1) · arranque caliente")]:
            rows = sorted([x for x in sc if x["group"] == g and x["start"] == start], key=lambda x: x["beta"])
            line(a1, [x["beta"] for x in rows], [x["plaquette"] for x in rows], c, lab, marker=mk)
    a1.set_xlabel("β"); a1.set_ylabel("plaqueta media ⟨½ Re Tr U_p⟩ / ⟨cos θ_p⟩")
    a1.set_title("E3 · U(1): ruptura entre acoplamiento fuerte y débil")
    a1.legend(loc="upper left", fontsize=8.5)
    a1.annotate("salto e histéresis\ncerca de β ≈ 1", (1.0, 0.63), xytext=(1.08, 0.48), color=INK2, fontsize=9,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
    spec = [("SU2", 2.4, C1, "o", "SU(2), β = 2.4"), ("SU2", 2.5, C3, "s", "SU(2), β = 2.5"),
            ("U1", 1.1, C2, "^", "U(1), β = 1.1 (Coulomb)"), ("U1", 1.3, C4, "D", "U(1), β = 1.3 (Coulomb)")]
    for g, b, c, mk, lab in spec:
        rr = [x for x in wl if x["group"] == g and abs(x["beta"] - b) < 1e-9][0]
        Rs = sorted(int(k) for k in rr["creutz"])
        y = [rr["creutz"][str(k)][0] for k in Rs]; e = [rr["creutz"][str(k)][1] for k in Rs]
        line(a2, Rs, y, c, lab, marker=mk)
        a2.errorbar(Rs, y, yerr=e, fmt="none", ecolor=c, elinewidth=1, capsize=0)
    a2.set_xticks([2, 3, 4]); a2.set_xlabel("R"); a2.set_ylabel("razón de Creutz χ(R,R)")
    a2.set_ylim(bottom=0)
    a2.set_title("E4 · Tensión de cuerda a acoplamiento débil")
    a2.legend(loc="upper right", fontsize=8.5)
    fig.tight_layout()
    fig.savefig(f"{F}/E3_E4_continuidad_y_creutz.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- E5 · cota de C_*
def fig_cstar():
    r = json.load(open(f"{R}/ym/ym_cstar.json"))
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    su = sorted([x for x in r if x["group"] == "SU2"], key=lambda x: x["beta"])
    u1 = sorted([x for x in r if x["group"] == "U1"], key=lambda x: x["beta"])
    bb = np.linspace(0.5, 8.2, 50)
    ax.plot(bb, 6 * bb, color=AXIS, lw=1); ax.plot(bb, 2 * bb, color=AXIS, lw=1)
    ax.annotate("6β (asíntota U(1))", (6.3, 41.5), color=MUTED, fontsize=8.5, ha="right")
    ax.annotate("2β (asíntota SU(2))", (8.0, 11.2), color=MUTED, fontsize=8.5, ha="right")
    line(ax, [x["beta"] for x in u1], [x["ratio_link"] for x in u1], C2, "U(1) · modo gauge de un enlace", marker="^")
    line(ax, [x["beta"] for x in su], [x["ratio_link"] for x in su], C1, "SU(2) · modo gauge de un enlace")
    line(ax, [x["beta"] for x in su], [x["ratio_plaq"] for x in su], C3, "SU(2) · plaqueta (gauge-invariante)", marker="s")
    ax.set_xlabel("β  (β → ∞ es la dirección del continuo)")
    ax.set_ylabel("cota inferior de C_*  =  Var_μ(h) / D_block[h]")
    ax.set_title("E5 · La constante de MF-94/95 diverge por modos puramente gauge")
    ax.legend(loc="upper left", fontsize=8.5)
    fig.tight_layout()
    fig.savefig(f"{F}/E5_cstar_gauge.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- E6 · Navier–Stokes
def fig_ns():
    d = json.load(open(f"{R}/ns/ns_N96_Re400.json"))
    s = [x for x in d["series"] if x["t"] >= 1.5]
    t = np.array([x["t"] for x in s])
    q = np.array([x["q"] for x in s])
    al = np.array([x["alpha"] for x in s])
    rad = np.array([-x["nu_lapq_over_q"] for x in s])
    ang = np.array([x["nu_gradxi2"] for x in s])
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(7.8, 6.2), sharex=True, gridspec_kw=dict(height_ratios=[1, 1.25]))
    line(a1, t, q, C1, "‖ω‖∞", marker=None)
    a1.set_ylabel("‖ω‖∞ (vorticidad máxima)")
    a1.set_title("E6 · Taylor–Green, Re = 400, 96³: la identidad del máximo se cierra por balance")
    pos = al > 0
    a2.plot(t, np.where(pos, al, np.nan), color=C2, lw=2, label="α  (amplificación, no local)")
    a2.plot(t, rad, color=C1, lw=2, label="−νΔq/q = ν/R_id²  (resolución radial)")
    a2.plot(t, ang, color=C3, lw=2, label="ν|∇ξ|²  (resolución por no coincidencia local)")
    a2.set_yscale("log"); a2.set_ylim(1e-5, 3)
    a2.set_xlabel("t"); a2.set_ylabel("tasas en el punto de ‖ω‖∞")
    a2.legend(loc="lower right", fontsize=8.5)
    fig.tight_layout()
    fig.savefig(f"{F}/E6_ns_balance.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    which = sys.argv[1:] or ["on", "gauge", "cstar", "ns", "pnp"]
    for w in which:
        dict(on=fig_on, gauge=fig_gauge, cstar=fig_cstar, ns=fig_ns, pnp=fig_pnp)[w]()
        print("ok", w)
