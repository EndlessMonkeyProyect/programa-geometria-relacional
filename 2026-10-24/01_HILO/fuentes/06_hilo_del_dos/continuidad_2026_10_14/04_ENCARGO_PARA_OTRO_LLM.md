# Encargo explícito para un segundo LLM — analizar primero, integrar sólo después de autorización

Actuás como **revisor independiente del Programa de Geometría Relacional («El hilo del dos»)**. Vas a recibir dos artefactos diferentes: (A) el archivo íntegro `HILO_DEL_DOS_FORMALIZACION_v2_8_CONSOLIDADA_2026-10-14.zip` y (B) este complemento aislado. **No sobrescribás ni reestructurés A, no sustituyás el lenguaje del autor y no incorporés automáticamente B al cuerpo canónico.**

El autor solicita preservar la secuencia ontología → lenguaje → lógica → matemática → computación; las fórmulas se proyectan desde la narrativa y deben ser auditables. La nueva intuición es que, cuando dos piezas se unen de verdad, **dejan de ser dos** y una normalización crea la siguiente referencia del **mismo repertorio relacional**. Las multiplicidades que ya no aportan diferencia se eliminan, como el ejemplo musical del compás que pierde una subdivisión. Lo importante para el autor no es clasificar una solución ya dada, sino **crear el recierre según la información efectiva y la pregunta**, midiendo ciclos, genealogía, radio, independencia y dependencias conjuntas.

### Trabajos requeridos

1. Reconstruí la genealogía de los conceptos y fórmulas desde las fuentes, citando **archivo y encabezado**; señalá dónde ya estaba cada resultado. No declares como nuevo algo formalizado antes en MF-34/MF-52/MF-63B/MF-86/MF-97/MF-98 u O1–O2c.
2. Clasificá la afirmación «misma clase de estructuras al siguiente nivel» en **clausura bajo operadores** (tipo), **compresión de representación**, **economía de construcción**, **certificabilidad de respuesta** y **mantenimiento de puertos/contextos**. Distinguir estas propiedades es obligatorio.
3. Recuperá todos los canales del anexo `02_CANALES_Y_CRECIMIENTO.md`; no los fusionés, especialmente Yang–Mills, masa, π, primos y física del tiempo con P vs NP. Indicá para cada canal: definición, teorema dentro del modelo, mera analogía, predicción contrastable, puente abierto y contraejemplo.
4. Para grafos, trabajá **directamente en 3-coloración y en cápsulas**, sin convertir SAT en lenguaje rector. Una conexión a 3-SAT puede aparecer sólo como equivalencia computacional acreditada, no como sustitución de la ontología.
5. Proponé el **menor** experimento o lema que pueda discriminar si cada recierre crea una cápsula normalizada del mismo repertorio sin aumento inevitable de recursos, incluso con crecimiento de fronteras y dependencias cruzadas. Incluí un **contraejemplo potencial** y medí el costo de encontrar equivalencias, no solamente su costo de lectura.
6. No infieras `P=NP` de `N_Q²=N_Q`, de que `K_Q=1`, de que una representación final sea corta, de disminuir soluciones, o de encadenar muchos cierres semánticos. Identificá qué resultado adicional sería necesario y si hay un obstáculo matemático conocido.
7. Devolvé una **matriz JSON estilo ROS-1 Lite** para cada afirmación esencial con `resolution_state`, `support_economy`, `novelty`, `missing_discriminants`, `reason`; podés acompañarla de una auditoría matemática explicativa. No simular invocaciones de plugins ni declarar pruebas que no ejecutaste.
8. Sólo si el análisis lo justifica, redactá un **parche ADITIVO propuesto** (archivo nuevo, ubicación recomendada, enlaces a fuentes); no reemplaces secciones existentes. Separá claramente POSTULADO, DEFINICIÓN, DERIVADO, CONDICIONAL, CONTRASTE, NO-GO, ABIERTO.

### Pregunta nuclear
**¿Es suficiente el repertorio de cápsulas y sus operadores de recierre para que, al incorporar nuevas relaciones en grafos de crecimiento arbitrario, la normalización produzca referencias del mismo tipo y evite que se acumulen diferencias exteriormente innecesarias? ¿Qué parte de esta frase es un teorema de clausura semántica, y qué parte aún exige demostrar una economía operacional uniforme?**

### Entrega esperada
A. mapa de antecedentes por archivo/sección; B. prueba/contraejemplo de la conjetura bien tipada; C. tabla de canales; D. protocolo ejecutable; E. JSON ROS-1 Lite; F. propuesta de integración separada como diff aditivo **sin aplicar**.

**Testigo nuevo prioritario:** cotejá primero `06_TESTIGO_DE_CREACION_DE_RELACION.md`. Debés decidir si el ejemplo estrella demuestra una nueva *aridad necesaria* sin demostrar un tipo ontológico nuevo. Después evaluá si un lenguaje cerrado de cápsulas puede conservar la economía operacional bajo composiciones arbitrarias, sin usar un `∃` no calculado como si fuese una respuesta compilada.
