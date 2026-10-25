# O89 — Prueba numérica adversarial de recurrencia y cierre

Fecha: 22 de octubre de 2026

## 1. Modelo mínimo de dos giros

Tomemos una vuelta exterior como unidad. Al completarse `n` vueltas exteriores, el giro interior habrá completado `n·α` vueltas, siendo `α` la razón de velocidades angulares. El cierre simultáneo ocurre exactamente si existe algún entero positivo `n` tal que `n·α` sea entero. Equivale a `α` racional.

Definimos el error de cierre (en vueltas):

`e(n,α) = |n α − entero_más_próximo(n α)|`.

Y el mejor error disponible antes de `N` vueltas:

`E(N,α) = min_{1≤n≤N} e(n,α)`.

**La recurrencia aproximada no es el cierre exacto.** Para α irracional, no hay cierre exacto, pero hay aproximaciones arbitrariamente buenas al aumentar N.

## 2. Cálculo verificado

| Razón α | Límite de vueltas exteriores N | Primera/mejor vuelta n | Error mínimo (vueltas) | Error angular |
|---|---:|---:|---:|---:|
| 3/2 | 2 | 2 | 0 | 0° |
| √2 | 10 | 5 | 0.0710678119 | 25.5844° |
| √2 | 30 | 29 | 0.0121933088 | 4.3896° |
| √2 | 100 | 70 | 0.0050506339 | 1.8182° |
| √2 | 1000 | 985 | 0.0003589375 | 0.1292° |

Para √2 la coincidencia es cada vez mejor, pero no llega a ser exacta. Por ejemplo, a la vuelta exterior 408, `408√2≈576.9991334482`: se desvía 0.0008665518 vueltas, es decir, 0.3120 grados. Una tolerancia de 0.001 vueltas ya se cumple a las 408 vueltas, aunque no hay ningún cierre exacto.

## 3. Resultado físico adversarial: solución exacta de Navier–Stokes

En el toro tridimensional periódico `(x,y,z)∈(R/2πZ)^3`, con viscosidad `ν>0`, consideremos

`u(x,y,z,t)=exp(−νt)·(sin z, cos z, 0)`.

Esta velocidad es incompresible, `∇·u=0`, y satisface exactamente Navier–Stokes sin forzamiento: `∂_t u = νΔu` y `(u·∇)u=0`, con presión constante. Su vorticidad es `ω=∇×u=u`, y la solución es suave para todo tiempo `t≥0`.

Para un marcador en el plano `z=π/6`, la razón entre las velocidades en direcciones `y` y `x` es `√3` (irracional). Sobre el toro periódico, la trayectoria no se cierra exactamente, aunque el campo es suave en todo tiempo finito. La amplitud decae continuamente por viscosidad, sin colapso en tiempo finito.

## 4. Resultado lógico

- **Demostrado por la aritmética:** si α es racional, el recorrido de dos giros uniformes se cierra; si α es irracional, nunca se cierra exactamente, aunque regresa arbitrariamente cerca.
- **Demostrado mediante solución explícita:** Navier–Stokes admite movimiento regular con trayectorias no periódicas.
- **Refutada como regla universal:** «No alcanzar un múltiplo entero de cierre implica colapso o pérdida de regularidad».
- **Abierto para el programa:** formular una noción de reconstrucción relacional de la unidad que no equivalga a periodicidad exacta, y derivar una cota física independiente sobre la vorticidad. Una tolerancia finita, umbral de información o condición de continuidad de ramas debe ser especificada antes de utilizarse en una prueba.

En particular, **ausencia de recurrencia exacta no equivale a ausencia de ritmo ni de continuidad**. El ejemplo irracional tiene un ritmo bien definido y constante entre direcciones, aunque no retorna exactamente a su posición inicial.
