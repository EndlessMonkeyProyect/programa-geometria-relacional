# O75 — Transporte de las relaciones y prueba de cierre con Navier–Stokes

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego**  
**22 de octubre de 2026**

## Lectura recomendada

1. `O75_FORMALIZACION.es.md`: ontología, narrativa y demostraciones matemáticas.
2. `codigo/verificar_o75.py`: prueba y regeneración de datos.
3. `datos/resumen.json`: cifras y condiciones experimentales.
4. `graficos/o75_cierre_y_area.png`: evolución de la referencia propuesta y del área proyectada.
5. `REGISTRO_AFIRMACIONES.csv`: estatus epistemológico de las afirmaciones.

## Resultado central

Sea `F_i=DΦ_t(x_i)` el transporte de direcciones materiales. Una candidata a referencia de cuatro enlaces es

`H_F=∏|F_i e_i^-|/|F_i e_i^+|`.

La identidad derivada es `d log H_F/dt = Σ [t_i^-·S_i t_i^- − t_i^+·S_i t_i^+]`.

La identidad de Cauchy viscosa `D_t(F^{-1}ω)=ν F^{-1}Δω` ofrece un transporte físico de referencia: la contribución nueva no se determina sólo por cuatro nodos.

Los campos analíticos exactos Taylor–Green y ABC, ambos sin fuerzas externas, muestran que `H_F` **no** se conserva universalmente aunque `det F_i=1`. Un segundo contraejemplo muestra que cuatro muestras iniciales de `u, ∇u` no bastan para predecir su futuro.

**Conclusión:** se ha construido un puente físico matemático comprobable y delimitado. **No se ha demostrado la regularidad global de Navier–Stokes tridimensional** ni una ley universal de sincronización entre cuatro cápsulas. El programa conserva su ontología de relaciones; los criterios de conservación se someten a refutación en vez de imponerse.

## Ejecutar

```bash
python codigo/verificar_o75.py
```
