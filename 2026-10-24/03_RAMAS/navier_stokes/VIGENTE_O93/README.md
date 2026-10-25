# O93 — Cierre propio, doble normalización y regularidad condicional

**Programa de Geometría Relacional** · Autoría del programa: **Le Matt Ansatz Di Ego**  
**Fecha de integración:** 22 octubre 2026  
**Naturaleza:** suplemento **aditivo y sujeto a auditoría crítica**, no modificación autónoma del núcleo ni de la Imagen Total.

## Propósito

Formalizar el enlace entre las formulaciones O92 y O86, preservando las capas:

1. **Ontología y lenguaje:** unidad, primera diferencia, referencia normalizadora, cierre propio, circuito de cuatro cápsulas, libertad interna, continuidad, reorganización.
2. **Matemática:** paridad y holonomía bajo modelos de enlaces; reconstrucción de fases; doble normalización exacta para NS; identidad entre transferencia normalizada y estiramiento; criterio **condicional** de continuación; esquema O84 de defecto y actualización.
3. **Computación:** 5 verificaciones simbólicas/analíticas + 1 integración Galerkin 3D independiente, con archivos originales de esta reproducción.

**Advertencia central:** la regularidad global de Navier–Stokes tridimensional **para todos los datos suaves** no está demostrada en este suplemento. Sí hay soluciones exactas, teoremas de ciertas subclases y criterios suficientes demostrados bajo hipótesis. Un cierre relacional o de fase no garantiza una cota dinámica por sí solo.

## Archivos

- `O93_Cierre_Propio_Flujo_Regularidad.pdf`: manuscrito principal (9 páginas), con definiciones, teoremas, demostraciones, resultados, limitaciones y procedencia.
- `O93_Cierre_Propio_Flujo_Regularidad.tex`: fuente editable LaTeX. Compilar con `pdflatex` dos veces desde esta carpeta (incluye una figura existente).
- `experimentos/verificar_o93.py`: pruebas reproducibles E1–E5.
- `experimentos/simulacion_galerkin.py`: experimento E6 de evolución Fourier–Galerkin y controles.
- `experimentos/resultados/`: JSON y CSV efectivamente producidos por los programas.
- `figuras/galerkin_fases.png`: evolución computacional de la enstrofía por fase.
- `ESTADO_DE_PRUEBAS.md`: matriz de alcance, estatus y próximos falsadores.
- `SHA256SUMS.txt`: hashes de los archivos de trabajo (excepto el propio manifiesto).

## Cómo reproducir

Requisitos: Python 3.10 o superior, NumPy, SymPy, mpmath y matplotlib. Una instalación habitual desde la raíz del paquete:

```bash
python -m pip install -r requirements.txt
python experimentos/verificar_o93.py
python experimentos/simulacion_galerkin.py
```

Se sobrescriben los resultados de los verificadores, no los documentos fuente. El experimento Galerkin tarda segundos o decenas de segundos según equipo. No requiere Internet para ejecutarse tras instalar dependencias.

Para comprobar la integridad de los archivos incluidos:

```bash
sha256sum -c SHA256SUMS.txt
```

## Experimentos y expectativas

| ID | Contrato | Comprobación | Salida |
|---|---|---|---|
| E1 | Grafo abstracto de contactos | `dim ker(C3)=0`, `dim ker(C4)=1`, `dim ker(K4)=0` | `verificacion_exacta.json` |
| E2 | Cuatro contactos ideales | `H=1` por telescopaje; enlace alterado `H=11/10` | `verificacion_exacta.json` |
| E3 | Campo trigonométrico solenoidal 3D | Exacto: `W=95/9`, `B=266/9`, `P=±3/4`; doble normalización `W=M²D`, `B=M²D₂`, `P=M³T` | `verificacion_exacta.json` |
| E4 | Cizalla NS exacta con cuatro modos | Evolución de `M,D,D₂,W,B`, disipación y ley de varianza con `T=0` | `ondas_exactas.csv` |
| E5 | Certificado intervalar de O84, ν=1 | `M0≈0.5194887 > 1/2`, `M1≤0.2717247 < 1/2` | `verificacion_exacta.json` |
| E6 | Fourier–Galerkin 3D sin fuerza, ν=0.01, T=0.08 | `N=16,24`, `dt=.004,.002`; diferencia por fase y sensibilidad a resolución | `galerkin_evolucion.csv`, `galerkin_resumen.json`, `galerkin_fases.png` |

**E3** usa coeficientes exactos de Fourier (`SymPy`) y el producto `⟨ω·Sω⟩` calculado mediante todas las ternas finitas de modos que cierran en frecuencia cero. No emplea una cuadratura que pudiera ocultar diferencia de signo.

**E5** comprueba fórmulas analíticas de O84 para el intervalo y las desigualdades. No es la integración temporal exacta completa del campo tridimensional.

**E6** emplea la proyección de Leray, 2/3 de-aliasing, RK4 y volúmenes periódicos. Con mallas finitas, la concordancia no garantiza convergencia global de la PDE. Las referencias del artículo original O53, O55, O69 y O90 se citan pero **no** se presentan como si hubiéramos reproducido sus corridas completas aquí.

## Estado de la investigación

La identidad formal `P=M³ T` es correcta bajo el contrato de Fourier completo de NS sin forzamiento, pero no impone signo o estimación nueva. El criterio

`∫₀ᵀ [M(t) T(t) - ν D₂(t)]₊ / D(t) dt < ∞`

es equivalente a la forma de O86 y **suficiente** para continuación suave si se cumple. **No** se demostró que se cumpla para toda condición inicial suave 3D.

La tarea abierta de la siguiente fase es producir una selección **intrínseca y causal** de referencias o normalizadores a partir de datos iniciales y demostrar un presupuesto físico uniforme, sin usar el campo futuro como oráculo. Las pruebas O76 (presión no local), O79/O86 (fases adversas) y O85 (costos bajo escalamiento) son controles adversariales obligatorios.

## Referencias internas cotejadas

Núcleo Canónico de Geometría Relacional; O25; O39; O40; O45; O58; O68; O72–O76; O78–O88; O91–O92. Este paquete es una **síntesis con nuevos verificadores**, no un archivo completo de las fuentes anteriores.
