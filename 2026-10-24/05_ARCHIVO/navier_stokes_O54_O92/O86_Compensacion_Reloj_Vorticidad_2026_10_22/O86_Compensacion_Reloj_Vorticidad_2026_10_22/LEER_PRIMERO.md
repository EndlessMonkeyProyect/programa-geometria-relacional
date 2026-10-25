# O86 — Resumen y alcance

**Principal:** `O86_FORMALIZACION.es.md`. **Código:** `codigo/o86_verificar.py`.

**Hallazgo:** A partir de los balances de vorticidad de O39 y el espejo endógeno de O25 se deriva la identidad exacta `d(log A)/dτν=2(Γν−1)`, con `A=⟨|ω|²⟩`, `B=⟨|∇ω|²⟩`, `P=⟨ω·Sω⟩`, `Γν=P/(νB)`, `dτν=νB/A dt`. No confundir reloj endógeno con la fase O45 ni `Γν` con el entero de O58.

**Control adversarial exacto:** dos datos suaves incompresibles que dependen genuinamente de `x,y,z` tienen iguales `A=95/9`, `B=266/9` y `ℓω²=95/266`, pero `P=±3/4` por una inversión de fase; con `ν=0.01`, una enstrofía crece instantáneamente y la otra decrece. **No** son demostraciones de explosión ni globalidad.

**Control positivo exacto:** un campo ABC de Beltrami, a intensidad arbitraria, permanece suave globalmente y da `P=0`.

**Pendiente:** derivar de la regla relacional una cota *no circular* de `∫(Γν−1)_+ dτν` para toda evolución del campo 3D sin fuerza. No declarar resuelto el problema de Navier–Stokes.

Reproducción: `python codigo/o86_verificar.py`.
