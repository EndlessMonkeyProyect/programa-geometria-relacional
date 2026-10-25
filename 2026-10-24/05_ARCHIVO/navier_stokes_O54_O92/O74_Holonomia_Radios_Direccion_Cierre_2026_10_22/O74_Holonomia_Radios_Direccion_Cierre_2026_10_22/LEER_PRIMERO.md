# O74 — Leer primero

**22 de octubre de 2026 · Programa de Geometría Relacional**

**Pregunta:** ¿cuándo los cuatro enlaces de un anillo pueden compartir un giro no nulo mientras cambian sus radios, y qué implica para la continuidad de la identidad?

**Resultado de grafo [D]:** para contactos externos generales `a_i ω_i + b_i ω_{i+1}=0`, cuatro enlaces admiten un giro no nulo exactamente cuando `H=∏(a_i/b_i)=1`. Si `a_i=r_i,b_i=r_{i+1}`, el producto telescópico da 1 aun con radios variables. Con brazos por contacto desiguales, la paridad sola no basta.

**Resultado adversarial [T]:** `H=1` no garantiza que exista un múltiplo entero de repetición de fases, ni un área mínima del anillo, ni separación geométrica de cápsulas.

**Puente con NS [D-NS]:** una solución exacta afín e incompresible comprime un lazo material en el plano y mantiene suavidad; una solución periódica viscosa exacta muestra que la circulación de un lazo material puede decaer. Son ejemplos especiales, **no una solución del problema de Navier–Stokes 3D**.

**Documentos:** `O74_FORMALIZACION.es.md` (pruebas completas), `codigo/verificar_o74.py` (autónomo), `datos/resumen.json`, `datos/o74_serie.csv`, `graficos/` y `REGISTRO_AFIRMACIONES.csv`.

**Próximo falsador O75:** intentar construir `H` **desde el campo del fluido**, sin imponer cápsulas rígidas ni contactos ideales, y derivar su evolución con NS.
