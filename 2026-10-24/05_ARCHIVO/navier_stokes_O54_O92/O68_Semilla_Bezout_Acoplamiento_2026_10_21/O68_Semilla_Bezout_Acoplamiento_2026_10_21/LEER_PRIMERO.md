# O68: qué queda establecido

**Resultado exacto:** dado un par de conteos enteros de vueltas `(k1,k2)`, su máximo común divisor `L` y su par primitivo `(q,p)` definen una normalización única. Bézout da `a*q+b*p=1`, luego `a*k1+b*k2=L`. El cambio entero de fases `Phi=a*theta1+b*theta2; Psi=p*theta1-q*theta2` tiene determinante `-1` y bajo sincronía exacta `(omega1,omega2)=(q,p)*Omega` cumple `Phi'=Omega`, `Psi'=0`.

**No está demostrado:** que dos ciclos geométricos de un anillo vorticial sean siempre dos fases materiales independientes; que Navier–Stokes imponga ese bloqueo; que de él se derive una cota de regularidad; que la unidad de Bézout sea físicamente la misma que la diferencia cuadrática de O40.

**Prueba reproducible:** `python3 codigo/verificar_o68.py`, sin paquetes adicionales. Pruebas aritméticas exhaustivas sobre pares primitivos pequeños, ejemplos cinemáticos de cambio radial, ruptura de coincidencia, no-radio-mínimo y no-cota-de-frecuencia.

Lea `O68_FORMALIZACION.es.md` para el argumento completo. Este suplemento no reemplaza O66, O67 ni la Imagen Total.
