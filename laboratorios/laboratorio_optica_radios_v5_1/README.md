# Laboratorio de radios y pared móvil — v5.1 / Radii and moving-wall lab — v5.1

**Endless Monkey Project** · *Relational Geometry Program*
Le Matt Asantz Di Ego

## Español

Laboratorio reproducible sobre cómo cambia lo que un observador puede distinguir al mover su referencia: espejos (A), resolución óptica con la distancia (B), fases de interferometría con varias longitudes de onda (C), economía de las distinciones (D) y límite de la reconstrucción desde una señal lejana (E).

| Archivo | Contenido |
| --- | --- |
| `laboratorio_optica_radios_v5_1.py` | Secciones A–E con aserciones; solo biblioteca estándar |
| `resultados_optica_v5_1.csv` | Valores calculados en la ejecución estándar |
| `contraste_airy.py` | Contraste opcional de B con una imagen de patrones de Airy; requiere numpy y scipy |
| `guia_optica_radios_v5_1.md` | Guía: pregunta, fórmulas, resultados, lo verificado y lo abierto |
| `guide_optics_radii_v5_1.md` | La misma guía en inglés |
| `CHECKSUMS.sha256` | Sumas SHA-256 de los demás archivos; verificar con `sha256sum -c CHECKSUMS.sha256` |

```bash
python3 laboratorio_optica_radios_v5_1.py   # Python 3.9 o posterior, menos de 1 s
python3 -m pip install numpy scipy          # solo para el contraste opcional
python3 contraste_airy.py                   # opcional, unos 5–10 s
```

Ejecutar dentro de esta carpeta: el primer comando vuelve a generar el CSV. Las verificaciones usan `assert`, así que el laboratorio se detiene si se ejecuta con `python -O`. Este laboratorio complementa el protocolo v4 de verificación de economía (reflexión, herencia y economía computacional), que se publica por separado.

## English

A reproducible lab on how what an observer can distinguish changes as its reference moves: mirrors (A), optical resolution with distance (B), multi-wavelength interferometric phases (C), the economy of distinctions (D) and the limit of reconstruction from a distant signal (E).

| File | Contents |
| --- | --- |
| `laboratorio_optica_radios_v5_1.py` | Sections A–E with assertions; standard library only |
| `resultados_optica_v5_1.csv` | Values computed by the standard run |
| `contraste_airy.py` | Optional check of B against an Airy-pattern image; needs numpy and scipy |
| `guia_optica_radios_v5_1.md` | The guide in Spanish |
| `guide_optics_radii_v5_1.md` | Guide: question, formulas, results, what is verified and what is open |
| `CHECKSUMS.sha256` | SHA-256 sums of the other files; check with `sha256sum -c CHECKSUMS.sha256` |

```bash
python3 laboratorio_optica_radios_v5_1.py   # Python 3.9 or later, under 1 s
python3 -m pip install numpy scipy          # for the optional check only
python3 contraste_airy.py                   # optional, about 5–10 s
```

Run inside this folder: the first command regenerates the CSV. Checks rely on `assert`, so the lab stops if run with `python -O`. This lab complements the v4 economy-verification protocol (reflection, inheritance and computational economy), published separately.
