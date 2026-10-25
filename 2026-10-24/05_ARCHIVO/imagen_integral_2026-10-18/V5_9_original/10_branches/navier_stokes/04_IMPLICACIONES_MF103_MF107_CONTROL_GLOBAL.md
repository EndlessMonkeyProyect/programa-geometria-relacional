# Navier–Stokes — qué aporta la información ternaria a la dinámica de vorticidad

**Estado:** extensión del diseño de observables; **regularidad 3D global OPEN**.

Las identidades del manuscrito `01_NAVIER_STOKES_CANALES_GEOMETRICOS_v3.tex` permanecen:

```
D_t ω = Sω + νΔω + curl f,    ω=q ξ,
a=D_t log q,   b=D_t ξ ⟂ ξ,
D_t ω/q = a ξ+b,
P_ξ^⊥ D_t b = S_cal,⊥ − 2ab,   S_cal=D_t²ω/q.
```

MF104 aporta un contraejemplo **externo al PDE**: mantener una distinción semántica no implica intensidad uniforme. MF107 aporta un contraejemplo representacional: relaciones por parejas pueden olvidar un observable conjunto. Ellos **no añaden** una cota nueva a `||ω(t)||_∞`.

Una interfaz euleriana candidata `I_t=I(u(t))` debe ser suficiente para predecir *evolución del máximo, no solo trayectoria individual*. Necesita memoria de: posición de máximos, migración, estiramiento `S`, términos viscosos, información espacial conjunta entre escalas y contribuciones no locales de presión.

En incompresible, la presión está ligada globalmente a la velocidad por

```
−Δp = Σ_{i,j} (∂_i u_j)(∂_j u_i).
```

Por tanto, una interfaz exclusivamente local o de relaciones por parejas carece, sin más hipótesis, de garantía de control de `∇∇p` o de la migración del máximo. Este es un **riesgo operacional**, no un teorema de que toda interfaz local falla.

**Protocolo:** fijar antes del ensayo un registro `I_t` que incluya comparaciones conjuntas por escala; construir pares de campos de velocidad suaves e incompresibles con registros iguales e intentar refutar que `I_t` determine la evolución de un observable como `max_x|ω(x,t+τ)|`. Comparar distintas representaciones y computar costo.

**Obligación matemática no satisfecha:** demostrar una desigualdad a priori uniforme que controle `∫_0^T ||ω(t)||_∞ dt` o un criterio de continuación equivalente, incluyendo migración y reentrada en todas las escalas. El signo de un descriptor de orientación por sí solo no puede controlar universalmente la regularidad: las ecuaciones de Navier–Stokes mantienen sus propiedades de existencia/regularidad bajo reflexiones espaciales.

**Estatus:** hipótesis de interfaz `OPEN`; identidades materiales locales dentro de sus hipótesis; resolución del problema del milenio `OPEN`.
