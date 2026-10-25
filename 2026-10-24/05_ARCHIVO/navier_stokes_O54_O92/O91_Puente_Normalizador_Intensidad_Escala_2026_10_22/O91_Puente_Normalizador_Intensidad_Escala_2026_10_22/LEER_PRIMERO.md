# O91 — Resultado de la prueba

**Sí se terminó la prueba concreta de intensidad/escala.**

- **Falsador exacto:** dos soluciones suaves, no forzadas, con mismo normalizador `N=12`, intensidad, enstrofía, escala y fases iniciales, pero con **signos opuestos de la derivada** de `K=U_rms*ell_omega/nu`.
- **Teorema positivo restringido:** sumar `C=<|Delta omega|²>` cierra algebraicamente la evolución para la familia de cuatro ondas de cizalla, porque la matriz de momentos es invertible.
- **Límite:** no se obtiene una cota dinámica general de Navier–Stokes 3D ni una identificación automática entre cuatro armónicos y cuatro nodos ontológicos.

Leer `O91_FORMALIZACION.es.md`. Reproducir: `python codigo/verificar_o91.py`. Opcional: gráfico con matplotlib.

**Corrección importante:** el cociente con velocidad RMS global no puede ser el detector definitivo de singularidad. O91 muestra campos solenoidales localizados con `K_global→0` pero `L³→∞`; por eso se propone un comparador local, que todavía no constituye una ley de regularidad universal.
