# RAMA INTEGRAL NAVIER–STOKES · Programa de Geometría Relacional
**Compilación de fuentes originales, pruebas, falsadores y experimentos | 24 octubre 2026**
**Autoría intelectual del programa: Le Matt Ansatz Di Ego**

## Lectura antes de integrar
Este paquete es una RAMA ADITIVA del Programa, no sustituye la Imagen Total ni cambia sus axiomas. Agrupa los documentos fuente localizados dentro de la **Imagen Total 3.9** y de su versión histórica **3.7**, además de los laboratorios originales O54–O92 y el suplemento O93. Se han extraído archivos de sus ZIP anidados, preservando los ZIP originales O54–O92 para cotejar su identidad. Las versiones previas se guardan sin declarar automáticamente que cada prueba se haya ejecutado ahora.

**Capas:** ontología y lenguaje → definiciones y contratos → matemáticas exactas y límites → cálculos y computación → contraste físico y falsadores → extrapolaciones condicionadas.

## Estructura
- `01_DOCUMENTOS_DE_ENLACE/`: visión 3.9, acta cubo de espejos, esferas, C4, continuidad y radio dinámico.
- `02_ORIGENES_O24_A_O53/`: antecedentes históricos y modelos computacionales de la Imagen 3.7: rama NS, O24–O38, O39–O53, reloj móvil, simulaciones, síntesis, experimentos de caja de espejos y esferas.
- `03_DESARROLLOS_O54_A_O92/`: carpetas de cada suplemento con texto, código, resultados y figuras originales extraídos de sus ZIP.
- `04_PAQUETES_ORIGINALES_O54_O92/`: ZIPs originales conservados sin modificación.
- `05_CORPUS_PARA_AUDITORIA/`: respaldo textual e índices globales de la Imagen 3.9; contiene ramas ajenas a NS, se incluye como referencia transversal de trazabilidad.
- `06_O93_SINTESIS_CERTIFICADOS/`: manuscrito PDF y TeX, verificadores y resultados reproducibles de O93.
- `07_MAPAS_Y_AUDITORIA/`: geneología de resultados, matriz de afirmaciones, localizador temático, inventario con SHA-256 y prueba automática de integridad.

## Cómo recorrerlo
1. Leer `07_MAPAS_Y_AUDITORIA/SECUENCIA_ONTOLOGIA_MATEMATICA_COMPUTACION.md`.
2. Seguir `07_MAPAS_Y_AUDITORIA/GENEALOGIA_NS.md` para encontrar el laboratorio precedente de cada enunciado.
3. Abrir O25, O39, O45 y O49–O53; continuar O54–O69, O72–O88, O92–O93.
4. Ejecutar los verificadores DE CADA LABORATORIO desde su carpeta con dependencias propias, respetando la versión del entorno indicada allí. Consultar primero los registros históricos; las simulaciones pesadas son optativas.
5. Integrar únicamente las proposiciones cuyo contrato físico y matemático quede explicitado y cuya prueba sea auditada independientemente.

## Estado epistémico
- `[O]` ontología, `[N]` interpretación narrativa, `[T]` teorema/identidad bajo hipótesis, `[E]` comprobación computacional, `[F]` contraejemplo, `[A]` abierto, `[C]` condición suficiente.
- Hay teoremas genuinos **condicionados**, soluciones NS exactas en clases especiales y comprobaciones numéricas. **No** se prueba regularidad global para todos los datos iniciales suaves 3D ni que una semilla finita sea universal.
- La ontología de cierre propio NO es sinónimo de singularidad de la PDE.
- La proyección 3D→2D no elimina enlaces por sí sola; pasar K4→C4 también requiere seleccionar restricciones activas.
- Los pares de fases muestran que normalización solo de amplitudes no predice la transferencia: preservar orientación y fase.
- El normalizador aritmético que transporta h/N no es automáticamente una escala física ni una cota de estiramiento.

## Reproducibilidad e integridad
`python3 07_MAPAS_Y_AUDITORIA/verificar_integridad.py` valida los SHA-256 registrados de todos los archivos de origen. O93: `python3 06_O93_SINTESIS_CERTIFICADOS/experimentos/verificar_o93.py`. Las corridas Fourier–Galerkin pueden requerir numpy/scipy y más tiempo; ejecutarlas es opcional y NO se presume aquí haber repetido cada una. Consultar `ESTADO_REEJECUCION.md`.

## Proveniencia de conversaciones
No tenemos un volcado de todas las conversaciones palabra por palabra. Incluimos un **registro de decisiones recuperables** desde la conversación disponible y documentos fuente, claramente identificado como reconstrucción, no como transcripción íntegra. El corpus textual original 3.9 compila documentos, no la totalidad de chats.
