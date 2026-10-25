# O80 — Presupuesto crítico del eco y transferencia no lineal

**Primero leer:** `O80_FORMALIZACION.es.md`.

**Hallazgo positivo con alcance delimitado:** un presupuesto espectral físico `R=Σ |û_k|/|k|` satisface `D⁺R+(ν−R)A₁≤0` y si `R(0)<ν` controla `∫A₁dt` y la inyección no lineal acumulada; la solución suave de Navier–Stokes periódico 3D sin fuerza continúa globalmente. Es una adaptación de metodología clásica de norma crítica de Fourier, no una solución nueva al problema general. Lo que se investiga aquí es su relación con el eco aritmético del Programa.

**Ensayo O79 ampliado:** fases opuestas con mismo R, amplitudes y gradientes, pero distinto signo de transferencia. Al sumar triadas de escalas 1 y 2 nacen 18 modos cruzados. El presupuesto los cuenta. Se verificaron 2717 condiciones en el código.

## Reproducción

Desde esta carpeta, ejecutar:

```bash
python codigo/verificar_o80.py
python codigo/graficar_o80.py
```

**Dependencias:** NumPy, Matplotlib (solo gráficos). Resultados: `resultados/*.json`, `resultados/*.csv`, gráficos PNG.

**Pendiente:** demostrar control físico comparable para *todos* los datos iniciales suaves, incluso si `R(0)≥ν`. No identificar sin una construcción explícita el normalizador aritmético `N` con `R`.
