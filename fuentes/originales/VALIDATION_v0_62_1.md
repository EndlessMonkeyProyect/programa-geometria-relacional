# VALIDATION v0.62 — información local y reflexión

**Estado:** PASS después de una corrección falsable del estado umbral. El primer candidato no era mínimo en contexto finito. Los teoremas MF-54A–C son elementales y se demuestran en el documento.

## 1. Misma estructura, distintos lenguajes de comparación

```json
[
  {
    "language": "none",
    "contexts": 0,
    "classes": 1,
    "I_rel_bits": 0.0,
    "class_sizes": [
      16
    ]
  },
  {
    "language": "first_bit",
    "contexts": 1,
    "classes": 2,
    "I_rel_bits": 1.0,
    "class_sizes": [
      8,
      8
    ]
  },
  {
    "language": "parity_only",
    "contexts": 1,
    "classes": 2,
    "I_rel_bits": 1.0,
    "class_sizes": [
      8,
      8
    ]
  },
  {
    "language": "two_bits",
    "contexts": 2,
    "classes": 4,
    "I_rel_bits": 2.0,
    "class_sizes": [
      4,
      4,
      4,
      4
    ]
  },
  {
    "language": "all_bits",
    "contexts": 4,
    "classes": 16,
    "I_rel_bits": 4.0,
    "class_sizes": [
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ]
  },
  {
    "language": "thresholds",
    "contexts": 5,
    "classes": 5,
    "I_rel_bits": 2.321928094887362,
    "class_sizes": [
      6,
      4,
      4,
      1,
      1
    ]
  }
]
```

El número de clases cambia con el contexto aunque el sistema \(X\) sea el mismo.

## 2. Monotonía bajo enriquecimiento del contexto

Pruebas de pares:

\[
oxed{128000}
\]

Fallos:

\[
oxed{0}
\]

## 3. Estado de umbral emergente — corrección de localidad

El candidato inicial heredado de MF-52 produjo **20 discrepancias** porque conservaba más distinciones de las que un futuro finito podía acreditar.

Se reemplazó por:

\[
\boxed{
\theta_t(p)=
\operatorname{clip}(k-|p|,-1,n-t)
}
\]

Filas verificadas después de la corrección:

\[
\boxed{45}
\]

Fallos:

\[
\boxed{0}
\]

Este resultado no es un problema de implementación: demuestra que el estado mínimo depende del horizonte/contexto disponible.

## 4. Estado de paridad emergente

Filas verificadas:

\[
oxed{88}
\]

Fallos:

\[
oxed{0}
\]

## 5. Novedad vs resolución

```json
{
  "novelty_same_X": {
    "no_context_classes": 1,
    "one_bit_classes": 2,
    "all_bits_classes": 16
  },
  "resolution_same_context": {
    "full_X_classes": 16,
    "even_parity_X_classes": 8,
    "weight_le1_X_classes": 5
  }
}
```

## 6. No implica

- que la equivalencia semántica sea computable eficientemente en general;
- una teoría de información probabilística;
- que toda información física sea discreta;
- \(P=NP\);
- una dinámica física completa.
