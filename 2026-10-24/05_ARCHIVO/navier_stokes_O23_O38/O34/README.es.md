# O34 — Atractor de forma y residuo entre escalas

Suplemento autónomo de trabajo (20 de octubre de 2026), independiente del Núcleo Canónico y de la Imagen Total.

## Componentes
- `O34_ATRACTOR_DE_FORMA_Y_RESIDUO_ENTRE_ESCALAS_NS.es.md` — derivación matemática, puente ontológico, falsadores, genealogía y fuentes.
- `verificar_o34.py` — 306 comprobaciones de identidades gaussianas, cotas, perfiles radiales exactos y un ejemplo asimétrico mediante cuadratura.
- `VALIDACION_O34.json` — salida completa del programa de verificación.
- `MANIFIESTO_SHA256.txt` — hashes de contenido (excepto el propio manifiesto).
- `ANTECEDENTE_O33_2026-10-20.zip` — suplemento anterior, sin modificar.

## Reproducir

Desde esta carpeta:

```bash
python verificar_o34.py
```

Necesita Python 3, NumPy y SciPy.

## Alcance

Las soluciones concéntricas radiales del ejemplo sí son soluciones exactas de Navier–Stokes 2D; el programa verifica ecuaciones e identidades analíticas, **no hace una simulación DNS de dos vórtices separados**. La tasa por entropía usa la desigualdad logarítmica de Sobolev gaussiana (resultado matemático clásico). La convergencia al vórtice de Oseen es conocida en la literatura (Gallay–Wayne): el suplemento no reivindica prioridad sobre ella.

El resultado central para el Programa es la distinción entre *forma común normalizada* y *residuo físico entre escalas*. Queda abierto el cierre común con persistencia de dos remolinos separados.
