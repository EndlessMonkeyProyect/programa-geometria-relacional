# O46 — Auditoría de antecedentes ejecutables (20-X-2026)

Se ejecutaron **sin modificar los archivos de origen** con `OPENBLAS_NUM_THREADS=1`:

| Módulo | Ejecución | Resultado observado | Alcance |
|---|---|---|---|
| O43R | `python verificacion_resto.py` | 10.100 pruebas modulares superadas | Aritmética del resto, normalización y cinemática ideal |
| O42 | `python verificar_O42.py` | 24³, 32³, 40³, 48³ y 64³, todos controles superados | Derivadas iniciales NS en un tubo 3D con fases opuestas, no evolución completa |
| O43E | `python VERIFICACION_O43E.py` | 103 verificaciones OK | Galerkin periódico 3D de corto tiempo, fase espacial ≠ retorno material |
| O44 | `python VERIFICACION_O44.py` | 114 PASS | Ocho fases, ausencia de vuelta completa en los trazadores de esa corrida |
| O45 | `python verificar_O45_espejo_ritmos_NS.py` | 10/10 OK | Cadenas cinemáticas, marcos móviles, fase libre de gauge y NS particular |
| O46 | `python verificar_O46.py` | 66/66 PASS | Teoremas instantáneos adicionales para datos suaves NS 3D con estiramiento local no nulo |

**Falsador del barrido O44:** el predictor escalar a partir de enstrofía inicial (LOOCV 1.5839e-8) fue mejor que el predictor de fase (1.8171e-8). La fase no quedó causalmente aislada por ese barrido. **No** declarar «fase causalmente necesaria en O44» basándose exclusivamente en ajuste.

La numeración de O44 y O44-N no indica que sean el mismo experimento: O44 evalúa un anillo toroidal mediante truncación Galerkin; O44-N usa una pareja exacta de cizallas con MCM 6.

Procedencia relativa en este entorno de trabajo:

- `../ns_work/O43R_Resto_Heredado_2026-10-20/verificacion_resto.py`
- `../ns_work/O42_Tubo_Vorticial_Fase_Heredable_NS_2026-10-20/verificar_O42.py`
- `../ns_work/O43E_Resto_Fase_Trayectoria_y_Balance_2026-10-20/VERIFICACION_O43E.py`
- `../O44_NS_Toroide_Semilla_2026-10-20/VERIFICACION_O44.py`
- `../O45_TIEMPO_ESPEJO_MOVIL_2026-10-20/verificar_O45_espejo_ritmos_NS.py`

Los logs completos de las seis ejecuciones verificadas están incluidos en el ZIP como evidencia de ejecución local. **No se ejecutaron aquí todas las ramas MF-86/97 y O39**, cuyas afirmaciones se revisaron documentalmente.
