# O52 — Retornos de fase meridiana relativa, avance y deslizamieto entre capas

**Programa de Geometría Relacional** · Le Matt Ansatz Di Ego · 20-10-2026

Extensión temporal de O51 desde T=1.20 a T=2.40, sin retocar los perfiles ni velocidades iniciales. Galerkin NS 3D periódico, sin forzamiento. No constituye una solución exacta de PDE ni demostración de regularidad global.

Archivos principales:
- `O52_INFORME.es.md`: formalización, resultados y límites.
- `o51_ns_ring.py`: solucionador original O51 incorporado para reproducción autónoma.
- `run_long.py`: simulaciones `N=40,48`, `T=2.4`.
- `NS40_T2p4.json`, `NS48_T2p4.json`: datos crudos, incluyendo trayectorias de partículas.
- `analizar_o52.py`: encuentra primer cruce de −2π de fase relativa, grafica y verifica.
- `O52_RESULTADOS.json`: reporte y 22 chequeos.
- `o52_desfase_largo.png`, `o52_primeras_vueltas.png`: resultados gráficos.
- `MANIFEST_SHA256.txt`: hashes SHA-256 del paquete.

## Reproducción

Requiere `numpy`, `scipy`, `matplotlib`.

```bash
python run_long.py
python analizar_o52.py
```

Se puede ejecutar sólo el análisis con los datos crudos incluidos. Los resultados están afectados por la resolución y la interpretación del centro no material. **Una vuelta de fase no es un retorno espacial de Poincaré.**
