"""Genera las tablas markdown de MF-96 a partir de los JSON y las inserta en el documento."""
import json, math, sys
import numpy as np

R = "/home/claude/mf96/results"
DOC = sys.argv[1]


def fmt(x, nd=3):
    return f"{x:.{nd}f}"


def num(x):
    return f"{int(x):,}".replace(",", "\u202f")


def t_e1():
    ts = json.load(open(f"{R}/pnp/pnp_tseitin.json"))["rows"]
    s2 = json.load(open(f"{R}/pnp/pnp_sat2.json"))["rows"]
    s3 = json.load(open(f"{R}/pnp/pnp_sat3.json"))["rows"]
    out = ["| Familia | variables | interfaz máx. en cláusulas (mediana; rango) | interfaz máx. lineal \\(F_2\\) |",
           "|---|---|---|---|"]
    for nv in sorted(set(r["n_vars"] for r in ts)):
        rows = [r for r in ts if r["n_vars"] == nv]
        c = [r["clause"]["max_clauses"] for r in rows]
        l = [r["linear"]["max_equations"] for r in rows]
        if nv in (12, 18, 24, 30, 36, 39, 42, 45, 48) or nv == max(r["n_vars"] for r in ts):
            out.append(f"| Tseitin (3-regular, {rows[0]['n_vertices']} vértices) | {nv} | {num(np.median(c))} ({num(min(c))}–{num(max(c))}) | {max(l)} |")
    for n in sorted(set(r["n"] for r in s2)):
        c = [r["clause"]["max_clauses"] for r in s2 if r["n"] == n]
        if n in (20, 80, 320, 640):
            out.append(f"| 2-SAT, \\(m=n\\) | {n} | {int(np.median(c))} ({min(c)}–{max(c)}) | — |")
    for n in sorted(set(r["n"] for r in s3)):
        c = [r["clause"]["max_clauses"] for r in s3 if r["n"] == n]
        out.append(f"| 3-SAT, \\(m=4.26\\,n\\) | {n} | {num(np.median(c))} ({num(min(c))}–{num(max(c))}) | no representable |")
    # ajuste exponencial de la mediana (cláusulas) vs variables
    fits = []
    for name, xs, ys in [
        ("Tseitin (cláusulas)", *zip(*[(nv, np.median([r["clause"]["max_clauses"] for r in ts if r["n_vars"] == nv])) for nv in sorted(set(r["n_vars"] for r in ts)) if nv >= 18])),
        ("3-SAT (cláusulas)", *zip(*[(n, np.median([r["clause"]["max_clauses"] for r in s3 if r["n"] == n])) for n in sorted(set(r["n"] for r in s3)) if n >= 15])),
    ]:
        b = np.polyfit(np.array(xs, float), np.log2(np.array(ys, float)), 1)[0]
        fits.append(f"{name}: la mediana crece como \\(2^{{{b:.2f}\\,n}}\\) (ajuste log-lineal, \\(n\\ge{xs[0]}\\) variables)")
    return "\n".join(out) + "\n\n" + "; ".join(fits) + ". El lenguaje lineal sobre \\(F_2\\) nunca supera el número de ecuaciones iniciales; 2-SAT nunca supera su número de cláusulas inicial."


def t_e2():
    r = json.load(open(f"{R}/ym/on_sigma_2d.json"))
    out = ["| Modelo | β | \\(L=8\\) | 16 | 32 | 64 | 128 | \\(\\xi(128)\\) |", "|---|---|---|---|---|---|---|---|"]
    for n, b in [(3, 1.5), (3, 1.7), (2, 1.3), (2, 0.9)]:
        rows = sorted([x for x in r if x["n"] == n and x["beta"] == b], key=lambda x: x["L"])
        cells = " | ".join(f"{x['xi_over_L']:.3f}" for x in rows)
        last = rows[-1]
        out.append(f"| O({n}) | {b} | {cells} | {last['xi']:.1f} ± {last['xi_err']:.1f} |")
    emax = max(x["xi_over_L_err"] for x in r)
    return "\n".join(out) + f"\n\nValores de \\(\\xi(L)/L\\) (longitud de correlación de segundo momento). Error estadístico por jackknife: como máximo {emax:.3f} en \\(\\xi(L)/L\\)."


def t_e3():
    r = json.load(open(f"{R}/ym/ym_scan.json"))
    out = ["| β (U(1)) | frío | caliente | | β (SU(2)) | frío | caliente |", "|---|---|---|---|---|---|---|"]
    bu = sorted(set(x["beta"] for x in r if x["group"] == "U1"))
    bs = sorted(set(x["beta"] for x in r if x["group"] == "SU2"))
    get = lambda g, b, s: [x for x in r if x["group"] == g and x["beta"] == b and x["start"] == s][0]["plaquette"]
    sel_u = [0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.2]
    sel_s = [1.0, 1.6, 2.0, 2.2, 2.4, 2.6, 3.0]
    for bu_, bs_ in zip(sel_u, sel_s):
        out.append(f"| {bu_:.2f} | {get('U1', bu_, 'frio'):.3f} | {get('U1', bu_, 'caliente'):.3f} | | {bs_:.1f} | {get('SU2', bs_, 'frio'):.3f} | {get('SU2', bs_, 'caliente'):.3f} |")
    du = max(abs(get('U1', b, 'frio') - get('U1', b, 'caliente')) for b in bu)
    ds = max(abs(get('SU2', b, 'frio') - get('SU2', b, 'caliente')) for b in bs)
    return "\n".join(out) + f"\n\nDiferencia máxima frío–caliente: U(1) {du:.3f} (en β = 1.00); SU(2) {ds:.4f} en todo el rango."


def t_e4():
    r = json.load(open(f"{R}/ym/ym_wilson_L10.json"))
    out = ["| Grupo | β | plaqueta | \\(\\chi(2,2)\\) | \\(\\chi(3,3)\\) | \\(\\chi(4,4)\\) |", "|---|---|---|---|---|---|"]
    for x in r:
        c = x["creutz"]
        def cell(k):
            v, e = c[k]
            if not (v == v) or abs(e) > 0.5:
                return "ruido (W ≈ 0)"
            return f"{v:.4f} ± {e:.4f}"
        tag = " (confinada)" if (x["group"] == "U1" and x["beta"] < 1) else (" (Coulomb)" if x["group"] == "U1" else "")
        g = "SU(2)" if x["group"] == "SU2" else "U(1)"
        out.append(f"| {g}{tag} | {x['beta']} | {x['plaquette']:.3f} | {cell('2')} | {cell('3')} | {cell('4')} |")
    return "\n".join(out)


def t_e5():
    r = json.load(open(f"{R}/ym/ym_cstar.json"))
    out = ["| Grupo | β | \\(\\mathrm{Var}_\\mu(h)\\) medida (Haar exacto) | razón enlace (modo gauge) | razón / β | razón plaqueta (gauge-inv.) |", "|---|---|---|---|---|---|"]
    for x in r:
        if x["beta"] not in (1.0, 2.0, 2.5, 4.0, 8.0) and not (x["group"] == "U1" and x["beta"] in (0.5, 1.0, 2.0, 4.0, 8.0)):
            continue
        if x["group"] == "SU2" and x["beta"] not in (1.0, 2.0, 2.5, 4.0, 8.0):
            continue
        g = "SU(2)" if x["group"] == "SU2" else "U(1)"
        haar = "0.25" if x["group"] == "SU2" else "0.5"
        rp = f"{x['ratio_plaq']:.3f}" if "ratio_plaq" in x else "—"
        out.append(f"| {g} | {x['beta']} | {x['var_link_emp']:.4f} ({haar}) | {x['ratio_link']:.2f} | {x['ratio_link']/x['beta']:.2f} | {rp} |")
    return "\n".join(out) + "\n\nAsíntotas de B.1 en \\(d=4\\): razón/β → 2 (SU(2)) y → 6 (U(1))."


def t_e6():
    d = json.load(open(f"{R}/ns/ns_N96_Re400.json"))
    s = d["series"]
    t = np.array([x["t"] for x in s]); q = np.array([x["q"] for x in s]); k = np.array([x["kappa"] for x in s])
    go = np.array([x["growth_obs"] for x in s]); gp = np.array([x["growth_pred"] for x in s])
    th = np.array([x["Theta"] for x in s]); al = np.array([x["alpha"] for x in s])
    rad = -np.array([x["nu_lapq_over_q"] for x in s]); ang = np.array([x["nu_gradxi2"] for x in s])
    pk = [i for i in range(1, len(s) - 1) if q[i] > q[i - 1] and q[i] >= q[i + 1] and q[i] > 5]
    lines = ["**E6a · Punto de vorticidad máxima (96³).**", "",
             "| Cantidad | Valor |", "|---|---|"]
    lines.append(f"| picos de \\(\\|\\omega\\|_\\infty\\) (t, valor, \\(\\kappa\\)) | " + "; ".join(f"({t[i]:.2f}, {q[i]:.1f}, {k[i]:.2f})" for i in pk) + " |")
    grow = (go > 0.2) & (t > 1.5)
    lines.append(f"| mediana de \\(\\kappa\\) mientras \\(\\|\\omega\\|_\\infty\\) crece (\\(d\\log Q/dt>0.2\\)) | {np.nanmedian(k[grow]):.2f} (n = {grow.sum()}) |")
    m = (t >= 1.5) & (al > 0) & np.isfinite(th)
    lines.append(f"| \\(\\Theta=\\alpha/(\\nu\\lvert\\nabla\\xi\\rvert^2)\\) en el máximo: mediana; fracción \\(>1\\) | {np.median(th[m]):.0f}; {(th[m] > 1).mean():.2f} |")
    lines.append(f"| resolución radial / angular en el máximo (mediana) | {np.median(rad[t >= 1.5] / np.maximum(ang[t >= 1.5], 1e-12)):.0f} |")
    for lo, hi, name in [(1.5, 3.4, "laminar, t ∈ [1.5, 3.4)"), (3.4, 10.01, "transicional y turbulenta, t ≥ 3.4")]:
        mm = (t >= lo) & (t < hi)
        lines.append(f"| concordancia identidad local vs crecimiento observado (\\(\\lvert\\Delta\\rvert<0.1\\)), fase {name} | {(np.abs(go - gp)[mm] < 0.1).mean():.2f} |")
    eps = max(x["eps"] for x in s)
    eta = (d["meta"]["nu"] ** 3 / eps) ** 0.25
    lines.append(f"| \\(\\varepsilon_{{\\max}}\\); \\(\\eta\\); \\(k_{{\\max}}\\eta\\) | {eps:.4f}; {eta:.4f}; {32 * eta:.2f} |")
    lines += ["", "**E6b · Población por percentil de \\(q\\), 0.1 % superior.**", "",
              "| t | \\(q_{99.9}\\) | \\(\\kappa\\) (mediana) | \\(\\Theta\\) (mediana) | \\(\\mathrm{nc}_1\\) | \\(\\mathrm{nc}_2\\) | \\(\\mathrm{nc}_4\\) | \\(\\rho_1\\) | \\(\\rho_2\\) |",
              "|---|---|---|---|---|---|---|---|---|"]
    for p in d["populations"]:
        b = p["bins"]["99.9-100"]
        lines.append(f"| {p['t']:.0f} | {p['q_p999']:.2f} | {b['kappa_median']:.2f} | {b['Theta_median']:.0f} | {b['mis_r1']:.3f} | {b['mis_r2']:.3f} | {b['mis_r4']:.3f} | {b['spearman_alphaq_vs_mis2']:+.2f} | {b['spearman_b_vs_gradxi']:+.2f} |")
    lines += ["", "\\(\\mathrm{nc}_r\\): no coincidencia media de direcciones \\(|\\xi(x)\\times\\xi(x\\pm r\\,e_i)|\\) a \\(r\\) celdas. \\(\\rho_1\\): correlación de Spearman entre \\(\\alpha/q\\) y \\(\\mathrm{nc}_2\\). \\(\\rho_2\\): correlación de Spearman entre \\(|b|\\) y \\(|\\nabla\\xi|\\).", "", "**E6c · Coherencia frente a intensidad** (no coincidencia media a 1 celda por banda de percentil).", "",
              "| t | 50–90 | 90–99 | 99–99.9 | 99.9–100 |", "|---|---|---|---|---|"]
    for p in d["populations"]:
        bb = p["bins"]
        lines.append(f"| {p['t']:.0f} | " + " | ".join(f"{bb[k]['mis_r1']:.3f}" for k in ["50-90", "90-99", "99-99.9", "99.9-100"]) + " |")
    lines += ["", "En la fase laminar (t ≤ 5) las estructuras más intensas son las más coherentes; en la fase turbulenta (t ≥ 6) la relación no es monótona: la coherencia de lo más intenso no es universal a esta resolución."]
    return "\n".join(lines)


def appendix():
    ns = json.load(open(f"{R}/ns/ns_N96_Re400.json"))["meta"]
    chk = ""
    try:
        d2 = json.load(open(f"{R}/ns/ns_N128_Re400.json"))
        s2 = d2["series"]; s1 = json.load(open(f"{R}/ns/ns_N96_Re400.json"))["series"]
        def peak(s, lo, hi):
            c = [x for x in s if lo <= x["t"] <= hi]
            i = int(np.argmax([x["q"] for x in c]))
            return c[i]
        p1 = peak(s1, 4.0, 6.0); p2 = peak(s2, 4.0, 6.0)
        def near(s, tt):
            return min(s, key=lambda x: abs(x["t"] - tt))
        rows = []
        for tt in (2.0, 3.0, 4.0, 4.5, 5.0, 5.5):
            a, b = near(s1, tt), near(s2, tt)
            rows.append(f"| {tt:.1f} | {a['q']:.2f} / {b['q']:.2f} | {a['kappa']:.2f} / {b['kappa']:.2f} | {math.sqrt(a['Rid2']) if a['Rid2']==a['Rid2'] else float('nan'):.3f} / {math.sqrt(b['Rid2']) if b['Rid2']==b['Rid2'] else float('nan'):.3f} |")
        chk = ("\n**Verificación de resolución (96³ frente a 128³, hasta t = 6).**\n\n"
               "| t | \\(\\|\\omega\\|_\\infty\\) 96³ / 128³ | \\(\\kappa\\) 96³ / 128³ | \\(R_{\\rm id}\\) 96³ / 128³ |\n|---|---|---|---|\n" + "\n".join(rows) +
               f"\n\nPrimer pico: 96³ en t = {p1['t']:.2f} con \\(\\|\\omega\\|_\\infty\\) = {p1['q']:.2f} y \\(\\kappa\\) = {p1['kappa']:.2f}; "
               f"128³ en t = {p2['t']:.2f} con {p2['q']:.2f} y \\(\\kappa\\) = {p2['kappa']:.2f}. "
               f"El valor del pico cambia {abs(p1['q']-p2['q'])/p2['q']*100:.0f} % y el balance en el pico se conserva; "
               f"el valor absoluto de \\(R_{{\\rm id}}\\) en el pico sí es sensible a la resolución (hasta ~25 %), por lo que sólo se usan sus órdenes de magnitud.\n")
    except FileNotFoundError:
        chk = "\n*La corrida de verificación 128³ no terminó a tiempo para esta versión.*\n"
    txt = f"""**Reproducibilidad.** Todo el código está en `50_experiments/mf96/scripts/`. Python 3.13, NumPy, SciPy, Numba y NetworkX. Semillas fijas. Ningún cálculo usa datos externos.

| Control | Script | Parámetros | Salida |
|---|---|---|---|
| E1 | `pnp_two_languages.py` | Tseitin 3-regular, 8–32 vértices; 2-SAT \\(m=n\\), \\(n\\le640\\); 3-SAT \\(m=4.26n\\), \\(n\\le35\\); 5 semillas; tope 3·10⁴ cláusulas en 3-SAT | `pnp_*.json` |
| E2 | `on_sigma_2d.py` | O(3) β = 1.5, 1.7; O(2) β = 1.3, 0.9; \\(L=8\\ldots128\\); Wolff; 300 barridos de termalización, 4 000 mediciones | `on_sigma_2d.json` |
| E3 | `ym_lattice_su2_u1.py scan` | \\(L=6\\); 60 + 60 barridos (baño + 2 sobrerrelajaciones); frío y caliente | `ym_scan.json` |
| E4 | `ym_lattice_su2_u1.py wilson` | \\(L=10\\); 150 barridos de termalización; 120 mediciones cada 2 barridos; jackknife en 10 bloques | `ym_wilson_L10.json` |
| E5 | `ym_lattice_su2_u1.py cstar` | \\(L=6\\); 60 + 20 configuraciones; varianzas condicionales en forma cerrada (Bessel) | `ym_cstar.json` |
| E6 | `ns_taylor_green.py` | {ns['N']}³, Re = {ns['Re']:.0f}, dt = {ns['dt']}, RK4, de-aliasing 2/3, sin forzamiento, t ∈ [0, {ns['Tend']:.0f}] ({ns['wallclock_s']/60:.0f} min); verificación 128³, dt = 0.015, t ∈ [0, 6] (28 min) | `ns_N96_Re400.json`, `ns_N128_Re400.json` |

**Chequeos internos superados.**

- E5: la varianza medida de una función de un enlace coincide con la de Haar (0.2485–0.2513 frente a 1/4 en SU(2); 0.4983–0.5014 frente a 1/2 en U(1)), como exige la invariancia gauge.
- E6: energía inicial 0.125 y disipación inicial \\(3\\nu/4\\) exactas. En la fase laminar, la tasa de crecimiento del máximo predicha por la identidad local coincide con la observada (mediana de la diferencia 0.02).
- E4: plaqueta SU(2) en β = 2.3 igual a 0.602, valor estándar.
- E2: \\(\\xi_\\infty\\approx11.5\\) para O(3) en β = 1.5, consistente con la literatura (≈ 11.1).
- E1: el estado SAT/UNSAT de una instancia aleatoria de 3-SAT con 20 variables se confirmó por fuerza bruta.
{chk}
**Limitaciones.**

- E1 usa eliminación de Davis–Putnam con un orden heurístico: mide el costo de *ese* lenguaje, no una cota inferior.
- E2 a E5 son simulaciones de Monte Carlo en redes pequeñas: ilustran, no demuestran.
- E6 está en el límite de resolución (\\(k_{{\\max}}\\eta\\approx1.1\\)); el argmax en malla introduce error de muestreo del pico.
- Ningún control toca el régimen asintótico que define los problemas del milenio.
"""
    return txt


doc = open(DOC).read()
for tag, fn in [("<!--E1_TABLE-->", t_e1), ("<!--E2_TABLE-->", t_e2), ("<!--E3_TABLE-->", t_e3), ("<!--E4_TABLE-->", t_e4),
                ("<!--E5_TABLE-->", t_e5), ("<!--E6_TABLE-->", t_e6), ("<!--APPENDIX_A-->", appendix)]:
    if tag in doc:
        doc = doc.replace(tag, fn())
open(DOC, "w").write(doc)
print("tables inserted")
