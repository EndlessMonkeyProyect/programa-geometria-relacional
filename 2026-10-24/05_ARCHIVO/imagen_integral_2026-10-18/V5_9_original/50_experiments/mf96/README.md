# MF-96 · Controles numéricos E1–E6

Material reproducible de `20_cross_branch/04_MF96_EL_NUDO_DEL_REINGRESO.md`.

Requisitos: Python 3.11 o superior, NumPy, SciPy, Numba, NetworkX y Matplotlib. Ningún cálculo usa datos externos y todas las semillas están fijas.

| Control | Pregunta | Script | Comando | Tiempo aprox. (2 núcleos) |
|---|---|---|---|---|
| E1 | ¿La misma identidad cuesta distinto según el lenguaje de cierre? | `scripts/pnp_two_languages.py` | `python3 scripts/pnp_two_languages.py tseitin results/pnp/pnp_tseitin.json` (también `sat2`, `sat3`) | 15 min |
| E2 | ¿La recursión de escala termina en cierre? O(3) frente a O(2) en 2D | `scripts/on_sigma_2d.py` | `python3 scripts/on_sigma_2d.py results/ym/on_sigma_2d.json` | 1 min |
| E3 | ¿Hay ruptura entre acoplamiento fuerte y débil? U(1) frente a SU(2) en 4D | `scripts/ym_lattice_su2_u1.py` | `python3 scripts/ym_lattice_su2_u1.py scan results/ym/ym_scan.json` | 1 min |
| E4 | Razones de Creutz a acoplamiento débil | `scripts/ym_lattice_su2_u1.py` | `python3 scripts/ym_lattice_su2_u1.py wilson results/ym/ym_wilson_L10.json 10` | 4 min |
| E5 | Cota inferior de \(C_*\) (MF-94/95) por modos gauge | `scripts/ym_lattice_su2_u1.py` | `python3 scripts/ym_lattice_su2_u1.py cstar results/ym/ym_cstar.json` | 2 min |
| E6 | Balance de la identidad en el máximo de vorticidad (Taylor–Green) | `scripts/ns_taylor_green.py` | `python3 scripts/ns_taylor_green.py 96 400 10.0 0.02 results/ns` | 13 min (96³) |

Figuras: `python3 scripts/make_figures.py`. Tablas del documento: `python3 scripts/make_tables.py <archivo.md>`.

Las rutas absolutas de `make_figures.py` y `make_tables.py` apuntan al entorno donde se ejecutaron; hay que ajustarlas al copiar la carpeta.

## Qué es exacto y qué no

- Las identidades de las secciones V.1, V.2 y B.1–B.3 del documento son derivaciones.
- E1–E6 son **controles numéricos**: ilustran y falsan lecturas, no demuestran teoremas.
- E2–E5 usan redes pequeñas. E6 está en el límite de resolución (\(k_{\max}\eta\approx1.1\)); la verificación con 128³ está en el Apéndice A del documento.
