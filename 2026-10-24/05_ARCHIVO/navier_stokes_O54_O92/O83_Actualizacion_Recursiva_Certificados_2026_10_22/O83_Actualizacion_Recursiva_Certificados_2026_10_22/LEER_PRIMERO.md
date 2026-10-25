# O83 · Inicio y alcance

**Pregunta:** ¿actualizar el cierre con información que genera Navier–Stokes permite recuperar una certificación de regularidad que una referencia fija no consigue?

**Hallazgo demostrable:** sí, localmente. Para el campo `(4 sin(2y),4 sin x,0)` con viscosidad 1 y el intervalo `[0,9/800]`, una referencia de calor falla su presupuesto (cota inferior demostrable >0.5303 frente al umbral 0.5), mientras que la primera referencia de Picard con la interacción incorporada lo supera (cota superior <0.4667). Los dos enunciados se prueban sin simulación ni redondeo usando series de Taylor acotadas racionalmente.

**Control adversarial global:** los datos anteriores son un campo 2D incrustado en 3D, conocido regular para todo tiempo. Sin embargo, ningún selector `F` de O82 puede certificarlo globalmente: si se omite algún modo, el resto inicial ≥2; si se retienen todos, la integral del defecto de calor es 1.92 >0.5. Un certificado suficiente que falla no demuestra singularidad.

**Resultado recursivo:** O83-T2 concatena certificados locales y da una condición adicional para evitar acumulación de pasos en tiempo finito (Zeno).

**No demostrado:** que este algoritmo proporcione una cadena de certificados para cualquier dato tridimensional; que el normalizador cardinal O58 sea idéntico a las proyecciones Fourier; la regularidad global de Navier–Stokes 3D sin fuerza.

**Orden de lectura:** `O83_FORMALIZACION.es.md` → `resultados/verificacion.json` → `graficos/o83_comparacion_defectos.png` → `codigo/o83_verificar.py`.
