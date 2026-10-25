# Suplemento O30 — Índice

**Estado:** formalización candidata. Sin cambios en el núcleo o Imagen Total.

- `O30_BALANCE_COMUN_Y_CIERRE_DINAMICO.es.md`: contrato, demostraciones (movimiento de centros; balance geométrico con difusión; forma y fase; discriminantes; límites).
- `validate_o30.py`: controles reproducibles de la parte advectiva mediante vórtices puntuales ideales de Euler. No confundir con simulaciones de Navier–Stokes viscoso.
- `VALIDACION_O30.json`: salida efectiva de los controles.
- `ANTECEDENTE_O29_2026-10-19.zip`: instantánea íntegra del suplemento anterior (no alterado).
- `MANIFIESTO_SHA256.txt`: huellas de archivos para control de integridad (excluye el propio manifiesto).

**Ejecutar:** `python validate_o30.py` con `numpy` instalado.

**Conclusión cauta:** las leyes de movimiento relativo y el presupuesto conjunto se deducen del sistema 2D, pero no se acredita sincronía o cierre físico común universal.
