# Mapa de lectura

## Recorrido conceptual

| Pregunta | Capítulo | Fuentes principales |
|---|---|---|
| ¿Qué vuelve visible una diferencia? | [1. Comparación](conceptos/01_comparacion_informacion.md) | MF-54, v0.72, v0.78 |
| ¿Qué conserva una identidad cerrada? | [2. Frontera](conceptos/02_frontera_cierre.md) | MF-54, MF-60B, v0.87 |
| ¿Cuándo se requiere una nueva referencia? | [3. Novedad](conceptos/03_novedad_resolucion.md) | MF-55, MF-57–58 |
| ¿Qué pertenece a la relación conjunta? | [4. Composición](conceptos/04_dependencia_composicion.md) | MF-56, MF-61B–62B |
| ¿Qué está demostrado sobre el cuatro? | [5. Geometría](conceptos/05_reflexion_geometria.md) | MF-57, v0.83–84, v0.90 |
| ¿Cómo se conserva una capa y se genera otra? | [6. Herencia](conceptos/06_capas_y_nuevo_operador.md) | v0.87, v0.91 |
| ¿Qué hace estable un cierre? | [7. Dinámica](conceptos/07_dinamica_estabilidad.md) | v0.74–77, v0.89 |
| ¿De dónde vienen 16, 15 y las octavas? | [8. Pesos](conceptos/08_bits_pesos_escalas.md) | v0.81, v0.84–86, v0.90 |
| ¿Qué significa tiempo relacional? | [9. Totalidad](conceptos/09_totalidad_tiempo_fisica.md) | v0.72–78 |
| ¿Qué falta para un algoritmo general? | [10. Computación](conceptos/10_computacion_acreditacion.md) | MF-59B–62B, v0.79–80 |

## Tres rutas

**Primera lectura:** síntesis, capítulos 1–4 y 6, registro de pendientes. Permite comprender la propuesta y su frontera sin reconstruir cada versión.

**Revisión matemática:** capítulos 3–8, resultados, correcciones y fuentes enlazadas. Las hipótesis se revisan en los originales; las etiquetas editoriales no reemplazan las demostraciones.

**Reproducción:** guía de datos, ejemplos editoriales y verificación. Los experimentos históricos carecen aquí de varios scripts y datos citados; la edición identifica esa limitación.

## Mapa de dependencias

~~~mermaid
flowchart TD
 A["Comparaciones y respuestas"] --> B["Cociente y frontera suficiente"]
 B --> C["Novedad por no-factorización"]
 B --> D["Compatibilidad conjunta"]
 C --> E["Extensión de descripción"]
 D --> E
 F["Postulados métricos locales"] --> G["Órbita de cuatro fases"]
 E -. "puente pendiente" .-> H["Nuevo operador geométrico"]
 G -. "herencia por justificar" .-> H
 H --> I["Estabilidad bajo acoplamiento"]
 J["Arquitectura y dinámica declaradas"] --> I
~~~

Las flechas punteadas son pendientes; las otras describen dependencias conceptuales y no certifican universalidad física.

## Herramientas de consulta

- [Glosario](GLOSARIO.md).
- [Correspondencia de notación](NOTACION.md).
- [Resultados](trazabilidad/RESULTADOS.md).
- [Linaje documental](trazabilidad/LINAJE.md).
- [Correcciones y pendientes](trazabilidad/CORRECCIONES_Y_PENDIENTES.md).
- [Catálogo completo](../fuentes/CATALOGO.md).
