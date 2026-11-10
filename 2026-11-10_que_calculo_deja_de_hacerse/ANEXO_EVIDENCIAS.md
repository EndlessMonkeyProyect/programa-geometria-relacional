# Evidencias y condiciones de reproducción

**Endless Monkey Project**  
*Relational Geometry Program*  
10 de noviembre de 2026 — revisión editorial 0.2

## Qué está demostrado

El artículo contiene demostraciones bajo condiciones explícitas de: reconstrucción de los seis vínculos del tetraedro usando tres bits; unicidad *si existe* una raíz afín de dimensión fijada por debajo del umbral de superposición; descomposición local de tres cláusulas en raíz y residuo; conteo exacto de paridad explícita más disyunciones; y conservación del conteo al eliminar circuitos de compuertas con extensión auxiliar única **si se reconoce y verifica completamente su codificación**.

## Qué se verificó en esta revisión

- Ejecutado de nuevo `experimentos/verificar_reconstruccion_y_convergencia.py`: 16 patrones de vértices, 56 subconjuntos de cinco estados, 336 trayectorias de tres exclusiones, 1.344 retracciones, 56 ternas locales y 175 conteos aleatorios pequeños contra fuerza bruta.
- Importado `experimentos/reconocimiento_de_paridades_distribuidas/laboratorio_relaciones_distribuidas.py`: 144 comprobaciones semánticas de compuertas, los dos controles negativos, las 30 validaciones aleatorias, los once tamaños de 8 a 96 variables y los ocho controles con conexiones largas. Los conteos coincidieron con su método de referencia; la enumeración primaria se ejecutó en los tamaños pequeños. Los tiempos medidos no son idénticos a los de la campaña anterior.
- El archivo original de resultados del laboratorio de intercambio y el del laboratorio distribuido se incluyen sin reescritura. No se volvió a ejecutar aquí la suite densa de matrices completa ni toda la campaña de tiempos de los experimentos distribuidos.

## Evidencias que no autorizan conclusiones generales

Los tiempos dependen de implementaciones de Python, hardware y líneas base específicas. Los controles de compuertas conectadas reconocen una familia sintáctica, no todas las formas de ocultar una paridad. Los rangos de intercambio no implican equivalencia de algoritmos completos. No se demuestra una cota general para satisfacibilidad de tres literales ni mejora frente a todos los métodos existentes.

## Terminología para lectores nuevos

Los archivos antiguos conservan identificadores históricos para permitir trazabilidad. En el artículo se escribe su mecanismo concreto:

| Identificador histórico | Nombre explicativo utilizado |
|---|---|
| GR3 | Reconstrucción focal de los seis vínculos del tetraedro |
| ROSI | Atlas de convergencia hacia una raíz afín con estado residual |
| CAG | Extracción de relaciones afines y conteo exacto |
| C1–C2 | Descomposición de intercambios y rangos tensoriales |
| C3–C4 | Operador local de cruce en dos métodos externos |
| C5 | Referencia periódica común e interpolación |
| C6 | Unicidad anticipada de raíz y retracción |
| C7 | Conteo de ecuaciones de paridad con cláusulas disyuntivas |
| C8 | Ventana de interpolación y costo de reconstrucción |

Los identificadores se reservan a este anexo y al código histórico. Su presencia no establece novedad matemática por sí sola.

## Reproducción rápida

```bash
python3 -I experimentos/verificar_reconstruccion_y_convergencia.py
```

## Reconocimiento de relaciones ocultas

```bash
python3 -m pip install numpy
python3 -I experimentos/reconocimiento_de_paridades_distribuidas/laboratorio_relaciones_distribuidas.py
```

La ejecución completa escribe un JSON en la carpeta del programa; se recomienda ejecutarla sobre una copia temporal para no alterar la evidencia original. Los controles grandes pueden tardar; el código tiene semillas declaradas.

## Intercambio y convergencia con los artículos externos

```bash
python3 -I experimentos/intercambio_y_convergencia/laboratorio_convergencia.py C5 C6 C7 C8
```

La suite completa puede requerir recursos elevados, incluidas matrices densas. El paquete conserva datos y versiones de los experimentos originales, sin afirmar revalidación completa en este turno.
