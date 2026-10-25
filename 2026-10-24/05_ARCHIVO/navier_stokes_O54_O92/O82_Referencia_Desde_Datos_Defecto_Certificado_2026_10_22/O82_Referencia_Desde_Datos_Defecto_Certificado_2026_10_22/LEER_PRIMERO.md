# O82 · Índice de lectura

1. `O82_FORMALIZACION.es.md`: derivación desde el dato inicial y demostración del certificado de defecto para Navier–Stokes tridimensional periódico sin fuerza.
2. `codigo/o82_verificar.py`: recálculo de 826 verificaciones discretas y valores exactos de Fourier de tres ondas.
3. `resultados/referencias.csv` y `resultado.json`: comparación de las tres referencias.
4. `graficos/o82_certificado_defecto.png`: barrera de continuidad del resto para la referencia de calor.
5. `REGISTRO_AFIRMACIONES.csv`: clasificación de hipótesis y teoremas.

**Continuidad del programa:** O82 es aditivo a O40, O58 y O80–O81. No modifica las fuentes canónicas. Singularidad ontológica como cierre propio ≠ pérdida de regularidad de una PDE. La solución de Navier–Stokes 3D para datos suaves generales sigue abierta.

**Verificación:** `python3 codigo/o82_verificar.py`.
