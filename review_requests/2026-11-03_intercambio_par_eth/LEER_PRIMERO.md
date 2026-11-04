# Solicitud de revisión independiente · El intercambio de un par en las dos refutaciones de la ETH · 3 de noviembre de 2026

[English](README.md)

## Revisión prioritaria · actualización editorial del 4 de noviembre de 2026

Se solicita primero un dictamen humano acotado: **¿son correctas las proposiciones 1, 2, 4 y 5 y el corolario 3 de la nota de prueba, y representan fielmente las construcciones citadas?** Como segunda pregunta, ¿existen antecedentes de las fórmulas exactas o de esta comparación? Se agradecen correcciones y referencias, incluso sobre una sola afirmación.

Las respuestas pueden reunirse en el [hilo específico de revisión](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/4). La cronología documental se mantiene como consulta separada. La posible consecuencia para las cotas sigue abierta; una respuesta sobre ella debe señalar una desigualdad o reducción concreta.

### Reproducir la entrega archivada

```bash
git clone https://github.com/EndlessMonkeyProyect/programa-geometria-relacional
cd programa-geometria-relacional
git checkout --detach 46e47274e9e573b9c91da1516d067c4f49c289f9
python -m pip install -r 2026-11-03_cruce_reflejo_central/requirements.txt
python review_requests/2026-11-03_intercambio_par_eth/verificar_pieza_compartida.py
```

El commit corresponde a la etiqueta `2026-11-03-pair-swap-review`. Estos comandos funcionan con `python` en Windows; en sistemas que lo requieran se puede usar `python3`. Fijan el contenido revisado; las dependencias conservan el rango declarado en `requirements.txt`. Los entornos previamente usados figuran en la solicitud y en la salida archivada. El resto de verificadores se describe en la sección 6 de la solicitud completa.

**Fuentes fijadas:** [OpenAI, commit `42907c9`](https://github.com/openai/math/blob/42907c9e999cc00d6abe7a50bfc1023250edd1b9/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) · [Anthropic, commit `16a5ce4`](https://github.com/anthropics/formal-math/blob/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/eth/paper.pdf).

## Alcance ampliado de la solicitud

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

Las verificaciones se corren con `python verificar_pieza_compartida.py`. Las respuestas son bienvenidas como [issues](https://github.com/EndlessMonkeyProyect/programa-geometria-relacional/issues/4).
