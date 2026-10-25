# O53 · Perturbación 3D de un anillo de Navier–Stokes

Autor del programa: Le Matt Ansatz Di Ego. Fecha: 2026-10-20.

Continuación reproducible de O51–O52. **No prueba regularidad global de Navier–Stokes ni sincronización universal.**

## Resultado principal

Al añadir una perturbación no axisimétrica libre de divergencia, el avance axial y el desfase cambian conjuntamente. Si no igualamos la energía inicial, en estos casos aumenta el desfase. Al igualarla, el desfase disminuye. Los dos efectos se reproducen con `N=40` y `N=48`. Un cociente simple giro/avance no se conserva durante la evolución.

## Reproducir

Requiere Python con `numpy`, `scipy`, `matplotlib`.

```bash
python ejecutar_o53.py
python ejecutar_control_energia.py
# Replicar además N=48 y energía inicial igualada:
python -c 'from o53_perturbed_ring import run; import json; from pathlib import Path; r=run(N=48,T=2.4,dt=.004,epsilon=.14,match_energy=True); Path("NS_N48_eps14_equienergia.json").write_text(json.dumps(r,ensure_ascii=False,indent=2))'
python analizar_o53.py
```

La ejecución tarda varios minutos según hardware. Hay salidas precalculadas dentro del paquete.

El informe principal es `O53_INFORME.es.md`; los datos están en los siete archivos `NS_N*.json`.

## Límites

- Fourier–Galerkin en toro 3D periódico; no solución PDE analítica ni CFD convergencia certificada.
- El centro de enstrofía no es un punto material. Una vuelta de fase no equivale a retorno espacial de Poincaré.
- El control de energía no iguala enstrofía, palinstrofía y escala del espejo.
- El paquete contiene datos, código y verificación interna; no demuestra una ley de estabilización de anillos físicos ni regularidad global de NS.
