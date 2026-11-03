# El cruce como reflejo central · 3 de noviembre de 2026

**Programa de Geometría Relacional** · Le Matt Ansatz Di Ego · [English](READ_FIRST.en.md)

**En una línea.** El programa tenía piezas del terreno (el recierre por interfaces, el tetraedro, la duplicación por reflexión y el nivel 8) y había diagnosticado el límite de su propio motor. Después de los anuncios de octubre se establecieron tres correspondencias exactas con el algoritmo de Claude (2026). Son teoremas clásicos dichos en el lenguaje del programa: no es un algoritmo propio ni un reclamo de prioridad, y la equivalencia algorítmica sigue abierta.

## Contenido

| Archivo | Qué es |
| --- | --- |
| [`articulo/El_cruce_como_reflejo_central_2026-11-03.md`](articulo/El_cruce_como_reflejo_central_2026-11-03.md) ([PDF](articulo/El_cruce_como_reflejo_central_2026-11-03.pdf)) | El paper. La ganancia del cruce viene de repartirlo entre dos cortes; los cruces ocupan el tetraedro par; en la duplicación, solo el 8 abarata el cruce, a costa de la asociatividad |
| [`articulo/The_Cross_as_Central_Reflection_2026-11-03_EN.md`](articulo/The_Cross_as_Central_Reflection_2026-11-03_EN.md) ([PDF](articulo/The_Cross_as_Central_Reflection_2026-11-03_EN.pdf)) | Edición inglesa del paper |
| [`articulo/La_caja_de_espejos_v0.3_2026-11-03.md`](articulo/La_caja_de_espejos_v0.3_2026-11-03.md) ([EN](articulo/La_caja_de_espejos_v0.3_2026-11-03_EN.md)) | El recorrido del programa, con su cronología y cuatro niveles: qué está demostrado y qué sigue abierto |
| [`articulo/Notas_2026-11-03.md`](articulo/Notas_2026-11-03.md) ([EN](articulo/Notes_2026-11-03_EN.md)) | Puntos tratados (particiones, autorreferencia, tareas abiertas) y el origen del tetraedro |
| `verificacion/` | Cinco verificadores en Python 3 con numpy |
| `referencia_resultados/` | Sus resultados de referencia |
| `reproducir_todo.sh`, `comparar_resultados.py` | Regeneran todo y lo comparan con la referencia |
| `requirements.txt`, `entorno.json`, `MANIFIESTO_SHA256.txt` | Dependencias, entorno de referencia y hashes |

## Los cinco verificadores

| Verificador | Respalda |
| --- | --- |
| `experimento_cruce_dos_cortes.py` | Los dos cortes del cruce (paper, §5) |
| `experimento_tetraedro.py` | El tetraedro como alfabeto y como geometría de los cruces (paper, §6) |
| `verificar_cadena_duplicacion.py` | La cadena de duplicación: por qué el 8 (paper, §7) |
| `verificar_particiones.py` | Particiones y autorreferencia (notas, §1) |
| `verificar_origen_tetraedro.py` | El tetraedro desde el origen en los bits, el cristal y E8 (notas, §2) |

## Reproducir

```bash
pip install -r requirements.txt   # numpy
bash reproducir_todo.sh           # unos 45 s; termina con código 0 solo si los cinco coinciden con la referencia
sha256sum -c MANIFIESTO_SHA256.txt
```

Los verificadores escriben su salida en UTF-8, así que corren igual en Windows.

## Verificación

La [solicitud de verificación](../review_requests/2026-11-03_cruce_reflejo_central/SOLICITUD_VERIFICACION.md) pide revisar la reproducibilidad, las pruebas de la §7 del paper y la precedencia documental. Ahí está también la revisión de la §7 hecha por DeepSeek, un modelo de IA.

## Etiquetas

[O] ontológico · [T] proposición con prueba · [C] resultado clásico · [E] verificación computacional · [I] correspondencia interpretativa · [A] pregunta abierta.

## Uso de herramientas de IA

Este material se preparó con asistencia de dos modelos de IA generativa, Claude (Anthropic) y DeepSeek. Cada documento declara qué hizo cada uno. El autor revisó el contenido y asume la responsabilidad por él.
