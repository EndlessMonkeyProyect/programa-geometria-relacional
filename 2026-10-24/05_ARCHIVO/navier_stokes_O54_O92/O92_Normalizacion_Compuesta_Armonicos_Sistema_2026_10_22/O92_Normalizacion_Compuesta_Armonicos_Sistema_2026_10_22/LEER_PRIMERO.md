# O92 — Lectura rápida

**Pregunta:** ¿O91 olvidó que el programa ya normalizaba tanto las relaciones entre armónicos como el sistema completo?

**Respuesta:** Sí. Los estados C y D de O91 tienen pesos armónicos individuales diferentes; la normalización `(total, reparto armónico)` los separa, y el cuarto momento es calculable sin agregar un nuevo observable independiente.

**Prueba física:** se deriva un sistema exacto para `(A,z_k)` donde `A` es la intensidad global y `z_k` son coeficientes vectoriales complejos normalizados. La redistribución tiene un término viscoso de signo negativo y un término triádico de signo variable según fase y orientación. Los ensayos O61/O79 muestran cuándo las normalizaciones escalares son insuficientes.

**No afirma:** que la normalización completa sea una compresión finita; que todo vórtice tenga cuatro nodos; que H sea universal; que esté demostrada la regularidad global tridimensional.

**Fuente principal:** `O92_FORMALIZACION.es.md`. Verificación: `python codigo/verificar_o92.py`. Resultado máquina: `resultados/o92_verificacion.json`.
