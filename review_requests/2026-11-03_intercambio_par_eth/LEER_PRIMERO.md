# Solicitud de revisión independiente · El intercambio de un par en las dos refutaciones de la ETH · 3 de noviembre de 2026

[English](README.md)

Se pide revisión independiente de tres cosas, con estándares distintos:

1. **Precedencia documental.** Qué había hecho público el programa antes del 16 de octubre, con registros del contenido fechados independientemente.
2. **La pieza compartida.** Si el intercambio de un par es el mismo operador local en los algoritmos de OpenAI y de Anthropic, y si los conteos binomiales relacionados para los rangos de un bit de Anthropic y las filas de medición explícitas de OpenAI importan para alguna de las cotas.
3. **Capacidad explicativa.** Si el marco deriva algo de esto o solo lo describe.

No se reclama prioridad ni un algoritmo propio, y no se evalúa la validez de las dos refutaciones. La cronología se apoya en metadatos de commit y falta confirmarla con sellos de tiempo independientes.

| Archivo | Qué es |
| --- | --- |
| [`SOLICITUD_REVISION.md`](SOLICITUD_REVISION.md) | La solicitud completa |
| [`REVIEW_REQUEST_EN.md`](REVIEW_REQUEST_EN.md) | Edición inglesa |
| [`NOTA_PRUEBA_3_3.md`](NOTA_PRUEBA_3_3.md) | Prueba de las fórmulas de la sección 3.3 para todo t |
| [`PROOF_NOTE_3_3_EN.md`](PROOF_NOTE_3_3_EN.md) | Edición inglesa de la nota de prueba |
| [`verificar_pieza_compartida.py`](verificar_pieza_compartida.py) | Comprobaciones numéricas de la sección 3.3; solo numpy, menos de un segundo |
| [`salida_verificador_2026-11-03.txt`](salida_verificador_2026-11-03.txt) | Su salida, con versiones y el hash del script |
| [`MANIFIESTO_SHA256.txt`](MANIFIESTO_SHA256.txt) | Hashes SHA-256 de estos archivos |

Las verificaciones se corren con `python3 verificar_pieza_compartida.py`. Las respuestas son bienvenidas como [issues](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues).
