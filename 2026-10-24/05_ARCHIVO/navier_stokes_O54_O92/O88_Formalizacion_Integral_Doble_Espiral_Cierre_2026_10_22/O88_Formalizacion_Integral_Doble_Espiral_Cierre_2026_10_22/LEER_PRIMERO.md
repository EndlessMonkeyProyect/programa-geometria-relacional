# O88 — Leer primero

**Qué es:** una formalización integral y aditiva de la rama de **doble espiral, nodos móviles, desfase y cierre propio** del Programa de Geometría Relacional, con trazabilidad hacia O68–O87, las reglas ontológicas y el transporte entre escalas. **No altera** el Núcleo Canónico ni la Imagen Total.

**Cómo leer:**
1. `SINTESIS_ONTOLOGICA.md`: conclusión conceptual en lenguaje breve.
2. `O88_FORMALIZACION_INTEGRAL.es.md`: definiciones, ocho proposiciones y pruebas, límites físicos y conexiones con los resultados previos.
3. `MATRIZ_DE_INTEGRACION.md`: distinción de cinco tipos de cierre y de los documentos originales.
4. `REGISTRO_AFIRMACIONES.csv`: auditoría de resultados y afirmaciones abiertas.
5. `fuentes/`: copias de los suplementos originales consultados; no los sustituye.
6. `codigo/verificar_o88.py`: verificaciones aritméticas/cinemáticas reproducibles (Python estándar).
7. `resultados/`: registro de controles y muestra de trayectorias en fases.

**Lo ya demostrado:** normalización de dos ciclos por matriz unimodular; cuatro marcas móviles con desfase normalizado exacto sobre un toro de superficie incompresible; desacoplamiento suave de la fase; necesidad de identificar la hoja al multiplicar coordenadas periódicas por N > 1.

**Lo abierto:** derivar fases y nodos del propio campo de Navier–Stokes 3D; probar transportabilidad colectiva entre reorganizaciones en dicho campo; demostrar una estimación dinámica universal que controle la vorticidad. No se realiza un nuevo experimento PDE en O88.

**Reproducción:** `python codigo/verificar_o88.py` desde cualquier directorio. No instala paquetes ni necesita internet.

**Seudónimo de autoría del programa:** Le Matt Ansatz Di Ego. Las proposiciones de topología, Bézout y cálculo diferencial empleadas son matemáticas conocidas; su integración aquí es parte del trabajo de formalización.
