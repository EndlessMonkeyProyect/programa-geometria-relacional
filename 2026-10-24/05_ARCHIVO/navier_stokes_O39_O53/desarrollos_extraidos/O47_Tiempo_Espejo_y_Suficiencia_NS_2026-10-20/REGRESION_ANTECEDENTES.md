# O47 — Inventario de pruebas anteriores e integración

Fecha: 20 de octubre de 2026. Se reutilizan antecedentes disponibles sin sustituir originales.

- **O43R**: laboratorio aritmético del normalizador, resultado previo de 10100 comprobaciones. No afirma dinámica del flujo.
- **O43E**: anillos 3D pseudoespectrales; 103 comprobaciones reportadas en regresión O46; diferencias de fase espacial no son vueltas materiales.
- **O44**: 114 verificaciones del experimento toroidal previo; trazadores sin retorno completo en el intervalo anterior. No transferirlo como evidencia universal de ausencia de retorno.
- **O45**: repetido en sesión de O47: 10 pruebas, 0 fallos; gauge/cambio de referencia y cinemática. No prueba reloj físico absoluto.
- **O46**: repetido en sesión de O47: 66 controles de identidad/derivadas iniciales, sin integración larga. O47 replica su familia y la extiende.
- **O47-A**: nuevo. Datos NS 3D iguales `(mcm,E,J,ell,beta,dot E)` y distintos `dot J`. Evolución corta N=24/32/48, refinamiento temporal N32.
- **O47-B**: nuevo control adversarial. Datos iguales también en energía cinética, distintos `dot J`; evolución N=32/48.

El archivo O47 principal contiene detalles y límites. Los datos son reproducibles con NumPy; la regla física singularidad/foco/partícula no queda demostrada por el éxito del esquema numérico.
