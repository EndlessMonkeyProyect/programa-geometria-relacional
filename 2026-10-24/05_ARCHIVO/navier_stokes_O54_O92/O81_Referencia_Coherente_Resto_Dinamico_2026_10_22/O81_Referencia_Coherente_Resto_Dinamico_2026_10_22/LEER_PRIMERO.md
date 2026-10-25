# O81 — Referencia dinámica y resto controlado

## Resultado

- **Positivo y exacto:** si `U` es una solución conocida global de Navier–Stokes y `R(u₀-U₀)<(ν/2)exp[-(4/ν)∫S_U²]`, la evolución completa continúa suavemente; la interacción con `U` está incluida explícitamente.
- **Ejemplo grande 3D:** `ν=1`, cizalla base `U₀=(2 sin y,0,0)` y resto dependiente de `x,z`, `R(u₀)=2.0001>ν`, `R(v₀)=0.0001<0.000167731...`, con nuevos modos generados de inmediato.
- **Límite demostrado:** un mero cambio del múltiplo de normalización no disminuye la norma crítica física. No se demostró cómo extraer universalmente `U` para todo dato inicial.
- **Estatus:** resultado de estabilidad especial relacionado con teoría conocida; NO prueba regularidad global general ni resuelve el problema Clay.

## Reproducir

```bash
python codigo/verificar_o81.py
python codigo/graficar_o81.py
```

Archivos: `O81_FORMALIZACION.es.md` (prueba), `REGISTRO_AFIRMACIONES.csv` (estatus), `resultados/o81_resumen.json` y gráficas.
