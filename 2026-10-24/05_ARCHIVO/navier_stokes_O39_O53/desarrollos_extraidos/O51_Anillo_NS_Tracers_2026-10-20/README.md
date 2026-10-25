# O51 — Anillo de Navier–Stokes con trazadores materiales

**Objeto:** evaluar si el avance axial de un anillo vorticial sincroniza materialmente dos capas de su núcleo.

**Resultados:** el centro de vorticidad avanza de forma autogenerada; las capas acumulan desfase de fase poloidal medido en el marco móvil; en `[0,1.2]` ningún trazador alcanza una vuelta completa. No se prueba compensación universal ni regularidad NS 3D.

- `O51_INFORME.es.md`: ontología, teoremas previos pertinentes, definición de observables, resultados y falsadores.
- `o51_ns_ring.py`: integrador NS 3D Galerkin Fourier, dealiased 2/3, RK4 y trazadores RK4.
- `NS32.json`, `NS40.json`, `NS40_halfdt.json`, `NS48.json`: salidas de las cuatro corridas.
- `validar_y_graficar.py`: controles sobre los resultados y generación de gráficas.
- `resumen_comparativo.csv`: resultados comparables.
- `o51_desfase_capas.png`, `o51_desplazamiento.png`: gráficas.
- `verificaciones_o51.json`: detalle de 28 controles.
- `MANIFEST_SHA256.txt`: hashes de los archivos reproducibles.

Reproducir (NumPy, SciPy y Matplotlib):

```bash
python o51_ns_ring.py --N 40 --T 1.20 --dt .004 --out NS40.json
python o51_ns_ring.py --N 48 --T 1.20 --dt .004 --out NS48.json
python validar_y_graficar.py
```

**Limitaciones:** periodicidad en cubo, núcleo no perfectamente resuelto en N32, interpolación trilineal, no existencia de retorno material completo. El código no demuestra existencia regular global del PDE.
