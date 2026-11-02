#!/usr/bin/env python3
"""Regenera las figuras de G–01 v1.3 que se dibujaron por código (requiere matplotlib).

    python3 generar_figuras.py es  [carpeta]     -> figuras 1 y 3 en español
    python3 generar_figuras.py en  [carpeta]     -> figuras 1, 2, 3 y 4 en inglés

La figura 2 (mapa conceptual) y la figura 4 (dos reflejos) en español son originales del autor;
sus versiones inglesas se redibujaron con el mismo trazado. Este script no forma parte de la
verificación: las figuras ilustran, no demuestran.
"""
import sys
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Rectangle, FancyArrowPatch

LANG = sys.argv[1] if len(sys.argv) > 1 else "es"
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else ".")
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams["font.family"] = "DejaVu Sans"
dark, sub, teal, gold, brown = "#172B3B", "#536170", "#426E80", "#AB8755", "#7B4C2D"
TX = {
 "es": dict(k4="K₄ · TETRAEDRO", dia="K₄ − e · DIAMANTE", k4s="6 vínculos · 4 colores necesarios", dias="5 vínculos · 3 colores bastan: 3 y 4 comparten",
            inac="3–4 inaccesible", sub="punto (a, b)/(N + 1) · aristas: pasos M₁, M₂, M₃ (Berggren) · borde: horizonte C", rest="(0,0,1)\nreposo",
            l1="paso M₁: (2,2,3)→(4,8,9)", l2="pasos M₂·M₂: (2,2,3)→(12,12,17)→(70,70,99)", f1="fig1_hiperboloide_berggren.png", f3="fig3_K4_diamante.png"),
 "en": dict(k4="K₄ · TETRAHEDRON", dia="K₄ − e · DIAMOND", k4s="6 links · 4 colors needed", dias="5 links · 3 colors suffice: 3 and 4 share",
            inac="3–4 inaccessible", sub="point (a, b)/(N + 1) · edges: steps M₁, M₂, M₃ (Berggren) · boundary: horizon C", rest="(0,0,1)\nrest",
            l1="step M₁: (2,2,3)→(4,8,9)", l2="steps M₂·M₂: (2,2,3)→(12,12,17)→(70,70,99)", f1="fig1_hyperboloid_berggren.png", f3="fig3_K4_diamond.png"),
}[LANG]

def fig_k4():
    W, H = 1989, 704
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
    c1, c2, c3, c4 = "#547A85", "#8A8FA2", "#C28B70", "#BDAB87"
    def graph(ox, cols, edges, ecol, missing, title, subt):
        P = {1: (ox + 145, 365), 2: (ox + 847, 365), 3: (ox + 496, 126), 4: (ox + 496, 604)}
        if missing:
            a, b = missing; ax.plot([P[a][0], P[b][0]], [P[a][1], P[b][1]], ls=(0, (6, 6)), color="#B9C6CB", lw=2.2, zorder=1)
            ax.text(P[a][0] + 16, 250, TX["inac"], fontsize=14, color="#7D8C95", ha="left", va="bottom", style="italic", zorder=1)
        for a, b in edges: ax.plot([P[a][0], P[b][0]], [P[a][1], P[b][1]], color=ecol, lw=3.2, zorder=2)
        for k, (x, y) in P.items():
            ax.add_patch(Ellipse((x, y), 120, 74, facecolor=cols[k], edgecolor="none", zorder=3))
            ax.text(x, y, str(k), color="white", fontsize=19, fontweight="bold", ha="center", va="center", zorder=4)
        ax.text(ox + 496, 38, title, fontsize=24, fontweight="bold", color=dark, ha="center", va="center")
        ax.text(ox + 496, 663, subt, fontsize=19, color=sub, ha="center", va="center")
    E = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    graph(0, {1: c1, 2: c2, 3: c3, 4: c4}, E, "#426E80", None, TX["k4"], TX["k4s"])
    graph(982, {1: c1, 2: c2, 3: c3, 4: c3}, [e for e in E if e != (3, 4)], "#5B8D9D", (3, 4), TX["dia"], TX["dias"])
    fig.savefig(OUT / TX["f3"], dpi=100, facecolor="white"); plt.close(fig)

def fig_hiperboloide():
    M1 = ((1, -2, 2), (2, -1, 2), (2, -2, 3)); M2 = ((1, 2, 2), (2, 1, 2), (2, 2, 3)); M3 = ((-1, 2, 2), (-2, 1, 2), (-2, 2, 3))
    ap = lambda M, v: tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))
    P = lambda v: (v[0] / (v[2] + 1), v[1] / (v[2] + 1))
    edge = "#8FAAB3"
    fig = plt.figure(figsize=(9.2, 7.0), dpi=220); ax = fig.add_axes([0.02, 0.02, 0.96, 0.92]); ax.set_aspect("equal"); ax.axis("off")
    th = np.linspace(0, 2 * np.pi, 600); ax.plot(np.cos(th), np.sin(th), color=dark, lw=1.8)
    ax.text(0.86, 0.86, "C\n(a² + b² = N²)", color=dark, fontsize=15, fontweight="bold", ha="left", va="bottom")
    def draw(v, depth, sx, sy):
        if depth == 0: return
        for M in (M1, M2, M3):
            w = ap(M, v); p, q = P((sx * v[0], sy * v[1], v[2])), P((sx * w[0], sy * w[1], w[2]))
            ax.plot([p[0], q[0]], [p[1], q[1]], color=edge, lw=0.7, zorder=1)
            ax.scatter([q[0]], [q[1]], s=[0, 9, 16, 26][depth], color="#547A85", zorder=2, lw=0)
            draw(w, depth - 1, sx, sy)
    for sx, sy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        q = P((sx * 2, sy * 2, 3)); ax.plot([0, q[0]], [0, q[1]], color=edge, lw=0.9, zorder=1)
        ax.scatter([q[0]], [q[1]], s=34, color="#547A85", zorder=2, lw=0); draw((2, 2, 3), 3, sx, sy)
    ax.scatter([0], [0], s=70, color=dark, zorder=3); ax.text(0.03, -0.07, TX["rest"], fontsize=12.5, color=dark, ha="left", va="top")
    def path(pts, col):
        xy = [P(t) for t in pts]; ax.plot([x for x, _ in xy], [y for _, y in xy], color=col, lw=2.6, zorder=4)
        ax.scatter([x for x, _ in xy], [y for _, y in xy], s=42, color=col, zorder=5, lw=0)
    path([(2, 2, 3), (4, 8, 9)], "#C28B70"); path([(2, 2, 3), (12, 12, 17), (70, 70, 99)], "#9C6B4E")
    lab = dict(fontsize=13, color=dark, zorder=6, bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9))
    x, y = P((2, 2, 3)); ax.text(x + 0.03, y - 0.04, "(2,2,3)", ha="left", va="center", **lab)
    x, y = P((4, 8, 9)); ax.text(x - 0.03, y + 0.03, "(4,8,9)", ha="right", va="center", **lab)
    for t, (tx, ty) in (((12, 12, 17), (1.0, 0.50)), ((70, 70, 99), (1.0, 0.64))):
        x, y = P(t); ax.annotate(f"({t[0]},{t[1]},{t[2]})", xy=(x, y), xytext=(tx, ty), ha="left", va="center",
                                 arrowprops=dict(arrowstyle="-", color="#9C6B4E", lw=0.9, shrinkA=2, shrinkB=3), **lab)
    ax.text(0, 1.07, TX["sub"], ha="center", fontsize=13, color="#536170")
    ax.plot([-1.08, -0.98], [-1.06, -1.06], color="#C28B70", lw=2.6); ax.text(-0.96, -1.06, TX["l1"], fontsize=12.5, va="center", color=dark)
    ax.plot([0.02, 0.12], [-1.06, -1.06], color="#9C6B4E", lw=2.6); ax.text(0.14, -1.06, TX["l2"], fontsize=12.5, va="center", color=dark)
    ax.set_xlim(-1.08, 1.32); ax.set_ylim(-1.12, 1.12)
    fig.savefig(OUT / TX["f1"], facecolor="white"); plt.close(fig)

def figs_solo_en():
    W, H = 2188, 558
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
    for x, t, s, fc, ec in ((44, "1 · IDENTITY", "unity · reference ·\ndifference · closure", "#EAF1F3", teal),
                            (772, "2 · COMPATIBILITY", "questions · projections ·\nrhythms · invariants", "#F0F3F4", teal),
                            (1500, "3 · PHYSICAL DYNAMICS", "action · metric · source ·\norbits · clocks", "#F7F4EF", gold)):
        ax.add_patch(Rectangle((x, 126), 633, 284, facecolor=fc, edgecolor=ec, lw=3.2))
        ax.text(x + 34, 200, t, fontsize=21, fontweight="bold", color=dark, va="center")
        ax.text(x + 34, 298, s, fontsize=19, color=sub, va="center", linespacing=1.5)
    for x0 in (688, 1416): ax.add_patch(FancyArrowPatch((x0, 268), (x0 + 68, 268), arrowstyle="-|>", mutation_scale=22, color=teal, lw=3.5))
    ax.text(W / 2, 488, "The second level does not prove the third: the physical bridge remains open.", fontsize=19.5, color=brown, ha="center", va="center")
    fig.savefig(OUT / "fig2_conceptual_map.png", dpi=100, facecolor="white"); plt.close(fig)
    W, H = 1914, 634
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
    O, Fp, Xp, Xm = (278, 316), (1247, 316), (1247, 134), (1247, 498)
    for X in (Xp, Xm): ax.plot([O[0], X[0]], [O[1], X[1]], ls=(0, (6, 5)), color="#AA8A5D", lw=2.6)
    ax.add_patch(FancyArrowPatch(O, (Fp[0] - 4, Fp[1]), arrowstyle="-|>", mutation_scale=22, color=teal, lw=5))
    ax.add_patch(FancyArrowPatch(Fp, (Xp[0], Xp[1] + 8), arrowstyle="-|>", mutation_scale=18, color="#5B8D9D", lw=4.5))
    ax.add_patch(FancyArrowPatch(Fp, (Xm[0], Xm[1] - 8), arrowstyle="-|>", mutation_scale=18, color="#5B8D9D", lw=4.5))
    for (x, y), c in ((O, dark), (Fp, teal), (Xp, "#5B8D9D"), (Xm, "#5B8D9D")): ax.scatter([x], [y], s=210, color=c, zorder=5)
    for x, y, t, c, fs, ha in ((195, 333, "O", dark, 24, "center"), (825, 282, "F · focus", teal, 22, "center"), (1315, 214, "D", "#5B8D9D", 22, "center"),
                                (1325, 418, "−D", "#5B8D9D", 22, "center"), (1325, 110, "x₊ = F + D", dark, 23, "left"), (1325, 502, "x₋ = F − D", dark, 23, "left")):
        ax.text(x, y, t, fontsize=fs, color=c, ha=ha, va="center")
    ax.text(718, 549, "||x₊|| = ||x₋|| ⇒ F · D = 0", fontsize=25, fontweight="bold", color=dark, ha="center", va="center")
    fig.savefig(OUT / "fig4_two_reflections.png", dpi=100, facecolor="white"); plt.close(fig)

fig_k4(); fig_hiperboloide()
if LANG == "en": figs_solo_en()
print("figuras escritas en", OUT.resolve())
