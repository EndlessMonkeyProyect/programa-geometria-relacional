# O89 — Resultado principal

**Prueba exacta:** El flujo periódico sin fuerza

`u=(2e^{-t}sin(y)+e^{-4t}sin(2z), 0, 0)`

resuelve Navier–Stokes con viscosidad 1 en todo tiempo. Dos canales de vorticidad comienzan con razón 1:1 y en `t=ln(2)/6` pasan por `sqrt(2):1`; cuatro trazadores empiezan con velocidades 2:1 y dejan de conservar ese acoplamiento. No hay singularidad. El medio es homogéneo.

**Ataque superado por el ejemplo:** se rechaza que los *múltiplos enteros persistentes* sean condición necesaria universal de regularidad.

**Ataque aún pendiente:** los trazadores no son nodos de un tubo vorticial toroidal; no se refuta el cierre propio relacional tal como puede definirse para esa familia específica.

**Precisión ontológica:** pérdida de sincronización entera no es pérdida de ritmo ni de referencia reconstructible. Los canales siguen una ley `rho(t)=e^{3t}` exacta.

**Reproducir:** desde esta carpeta, `python codigo/verificar_o89.py` (SymPy; Matplotlib opcional). 29 comprobaciones, tabla CSV, JSON y figura.

No afirma ni una prueba universal de regularidad ni una singularidad 3D.
