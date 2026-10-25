# O84 — Contabilidad única del eco

**Punto de partida:** O83, en el que la suma de presupuestos por intervalo podía cobrar repetidamente la misma relación pendiente. Se mantienen íntegros O40–O83. No se modifica el núcleo ontológico.

## Dos resultados

**O84-T1 (teorema condicional).** Para una referencia discontinua por tramos, construir el presupuesto global ponderado por un solo factor integrante. Los cambios de referencia sólo cobran el salto `J_j`; si la nueva referencia coincide en el instante de transición, `J_j=0`. La desigualdad controla el resto aun con infinitas actualizaciones, si el gasto ponderado total, la exposición y el gradiente de referencia son sumables. **No prueba que se cumplan para todo dato inicial 3D.**

**O84-T2 (actualización sin salto).** Corrección de Duhamel a partir del defecto conocido. Con el mismo dato tridimensional suave `u0=(4 sin y, sin z, sin x)`, `nu=1`, en `[0,0.018]`:

- calor solo: presupuesto exacto `0.519488712836... > 0.5` (no certifica)
- corrección de primera interacción: presupuesto acotado `<=0.271724746562... <0.5` (certifica)
- aparecen 12 frecuencias nuevas; no se presupone la solución futura.

**Adversarial.** La suma antigua de cotas de intervalos puede divergir en una solución de cizalla explícita y suave sin fuerza, al partir artificialmente `[0,1)` en infinitos intervalos. El presupuesto telescópico permanece finito. Es una mejora de contabilidad, no un teorema nuevo de regularidad global.

## Cómo verificar

```
python codigo/o84_verificar.py
```

Requiere NumPy; imprime certificaciones y guarda `resultados/verificacion.json`. El script contiene comprobaciones de Fourier y cotas racionales; no reemplaza la demostración del documento principal.

## Límite pendiente, sin reabrir preguntas resueltas

Probar **desde cualquier dato inicial suave** que puede construirse una familia de referencias calculables para todo tiempo físico finito con exposición, salto y defecto acumulados controlados, sin presuponer regularidad. Esa obligación no está resuelta por O84. Ontología: singularidad como cierre propio, no identificada sin prueba con blow-up PDE; anillo/esfera/ola como posibles realizaciones, no cobertura física demostrada.
