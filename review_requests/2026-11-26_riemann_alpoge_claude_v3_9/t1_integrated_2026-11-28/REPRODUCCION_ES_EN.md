# Reproducción de T.1 / T.1 reproduction · 28-XI-2026

**Le Matt Ansatz Di Ego** · Endless Monkey Project · Relational Geometry Program

Se ejecutaron los verificadores en una copia extraída, manteniendo intactos los archivos de la entrega. Entorno: Python 3.12.14, NumPy 2.5.5, mpmath 1.4.1 y python-flint 0.9.0. Cada comando se ejecutó desde la carpeta indicada; las salidas generadas permanecieron en la copia de trabajo.

The verifiers were run in an extracted working copy, preserving the delivered files. Environment: Python 3.12.14, NumPy 2.5.5, mpmath 1.4.1, and python-flint 0.9.0. Each command ran from its indicated folder; generated outputs remained in the working copy.

| Carpeta / Folder | Comando / Command | Resultado / Result |
| --- | --- | --- |
| raíz del ZIP original / original ZIP root | `python verificar_integridad.py` | 40/40 SHA-256 OK |
| `01_T1_v1_4` | `python verificacion_independiente_T1.py` | exit 0; ~10.8 s |
| `01_T1_v1_4` | `python verificar_reflexion_iterada.py` | exit 0; ~1.7 s |
| `03_herencia_local` | `python verificacion_independiente_T1.py` | exit 0; ~13.3 s |
| `03_herencia_local` | `python verificar_herencia_local.py` | exit 0; ~1.5 s |
| `03_herencia_local` | `python certificar_contraejemplo.py` | exit 0; ~0.5 s |
| `05_T1_5` | `python verificar_jensen_centros.py` | exit 0; ~0.2 s |
| `05_T1_5` | `python verificar_jensen_arb.py 19` | exit 0; ~161 s; ocho etapas / eight stages |

El último verificador ejecuta también la auditoría Arb base. Para $p=2,3,5,7,11,13,17,19$, sus intervalos certifican $pJ_4>1$ y $p\gamma>1$. El menor centro de $pJ_4$ es $1.0091299238108005\ldots$, en $p=2$. El [certificado JSON](05_T1_5/certificado_jensen_arb_p19.json) conserva las bolas; SHA-256: `8da6580c64b1d712edb0f4c482edb55bfedaab93c3e43ddfc83a93dd141dd2a2`.

The final verifier also runs the base Arb audit. For $p=2,3,5,7,11,13,17,19$, its intervals certify $pJ_4>1$ and $p\gamma>1$. The smallest $pJ_4$ centre is $1.0091299238108005\ldots$, at $p=2$. The [JSON certificate](05_T1_5/certificado_jensen_arb_p19.json) retains the balls; SHA-256: `8da6580c64b1d712edb0f4c482edb55bfedaab93c3e43ddfc83a93dd141dd2a2`.

Estos controles son finitos. Los extremos espectrales de la auditoría base se calcularon sobre centros y requieren certificación separada. La divergencia asintótica y la transferencia aritmética directa son cuestiones abiertas en esta entrega.

These checks are finite. Spectral endpoints in the base audit were computed on centres and require separate certification. Asymptotic divergence and direct arithmetic transfer remain open questions in this delivery.
