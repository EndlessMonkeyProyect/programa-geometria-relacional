# Escalas relacionales y la hipótesis de Riemann

**Le Matt Ansatz Di Ego**<br>
Endless Monkey Project<br>
Relational Geometry Program

17 de noviembre de 2026 · Versión 1.0

Dos documentos y sus verificaciones. La formalización demuestra cómo se hereda la discrepancia de la criba entre escalas y dónde queda la hipótesis de Riemann. La reflexión sigue ese hilo hasta los ceros de $\zeta$ y lo lee en el vocabulario del programa, con un puente final al vocabulario estándar.

## Archivos

| Archivo | Qué es |
|:--|:--|
| [Reflexión](REFLEXION_UN_NUMERO_POR_CERO_ES.md) · [PDF](REFLEXION_UN_NUMERO_POR_CERO_ES.pdf) | **Un número por cero.** Novedad, espejo y el pivote ½ de la hipótesis de Riemann. El hilo completo, lo demostrado, lo verificado con números, lo abierto y el puente. |
| [Formalización](FORMALIZACION_R01_R02_ES.md) · [PDF](FORMALIZACION_R01_R02_ES.pdf) | **Las escalas relacionales de la criba.** Herencia, cierre y la escala √x de la hipótesis de Riemann. Las demostraciones. |
| `verificacion_un_numero_por_cero.py` | Reproduce los números de la reflexión y genera `figura_pivote.png` (unos 30 s). |
| `verificacion_R01_R02.py` | Reproduce los números de la formalización y genera `figura_ritmos.png` (unos 25 s). |
| `figura_pivote.png`, `figura_ritmos.png` | Figuras generadas por los scripts. |

Para una lectura de entrada, la reflexión; para las pruebas, la formalización.

## Complemento bilingüe R–03 · 18 de noviembre de 2026

[R–03 en español](2026-11-18_r03_herencia_espectral/R03_HERENCIA_Y_LOCALIZACION_ES.md) · [R–03 in English](2026-11-18_r03_herencia_espectral/R03_SPECTRAL_INHERITANCE_EN.md) · [Anexo breve](2026-11-18_r03_herencia_espectral/ANEXO_V1_1_CONSERVACION_CEROS_ES.md) · [Guía y verificación](2026-11-18_r03_herencia_espectral/README.md).

El complemento demuestra la conservación de ceros bajo filtros primos finitos, cuantifica la estabilidad de la normalización y examina la simetría mediante un modelo de control. La hipótesis de Riemann permanece abierta.

## Reproducción

```bash
pip install numpy mpmath sympy matplotlib
python verificacion_R01_R02.py
python verificacion_un_numero_por_cero.py
```

Los bloques con aserciones detienen la ejecución si algo falla; los demás miden y reportan.

## Estado en una línea

Demostrado y verificado: la herencia exacta de la criba, su ley de energía, las tres capas del cierre, el conteo exacto de primos sobre las escalas relacionales, los ritmos que la herencia conserva, el pivote $\xi(\tfrac12 + z) = \xi(\tfrac12 - z)$, los 649 ceros hasta altura 1000 sobre la línea y la herencia y la novedad en las octavas de Mersenne. Abierto: la hipótesis de Riemann, leída como «un número por cero».

## Edición de publicación

Se unificó la firma pública con la del repositorio y se precisaron la referencia a Conrad, la aplicación de Kronecker–Weyl a colecciones finitas y el carácter de cruce de los ceros simples. Los PDF y Markdown contienen estas precisiones.

[English overview](README.en.md) · [Derechos y uso](RIGHTS.md).
