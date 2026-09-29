# VALIDATION v0.65 — auditoría del generador

**Estado:** los tres resultados principales son consecuencias algebraicas exactas de los postulados actuales. Los cálculos numéricos son sólo controles de implementación.

## 1. Rigidez del signo

Para \(R>0\) y sector no trivial:

\[
\boxed{\sigma=-1}.
\]

La prueba usa exclusivamente compatibilidad de norma, ortogonalidad métrica y cierre doble.

## 2. Órbita de una sola referencia

Se verificó numéricamente para varios valores de \(R\) que las potencias de \(T_R=RJ\) permanecen en rango máximo 2.

```json
[
  {
    "R": 0.2,
    "power": 0,
    "rank_span_0_to_k": 1
  },
  {
    "R": 0.2,
    "power": 1,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.2,
    "power": 2,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.2,
    "power": 3,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.2,
    "power": 4,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.2,
    "power": 5,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.2,
    "power": 6,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.2,
    "power": 7,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.2,
    "power": 8,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.5,
    "power": 0,
    "rank_span_0_to_k": 1
  },
  {
    "R": 0.5,
    "power": 1,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.5,
    "power": 2,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.5,
    "power": 3,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.5,
    "power": 4,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.5,
    "power": 5,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.5,
    "power": 6,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.5,
    "power": 7,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.5,
    "power": 8,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.9,
    "power": 0,
    "rank_span_0_to_k": 1
  },
  {
    "R": 0.9,
    "power": 1,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.9,
    "power": 2,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.9,
    "power": 3,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.9,
    "power": 4,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.9,
    "power": 5,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.9,
    "power": 6,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.9,
    "power": 7,
    "rank_span_0_to_k": 2
  },
  {
    "R": 0.9,
    "power": 8,
    "rank_span_0_to_k": 2
  },
  {
    "R": 1.0,
    "power": 0,
    "rank_span_0_to_k": 1
  },
  {
    "R": 1.0,
    "power": 1,
    "rank_span_0_to_k": 2
  },
  {
    "R": 1.0,
    "power": 2,
    "rank_span_0_to_k": 2
  },
  {
    "R": 1.0,
    "power": 3,
    "rank_span_0_to_k": 2
  },
  {
    "R": 1.0,
    "power": 4,
    "rank_span_0_to_k": 2
  },
  {
    "R": 1.0,
    "power": 5,
    "rank_span_0_to_k": 2
  },
  {
    "R": 1.0,
    "power": 6,
    "rank_span_0_to_k": 2
  },
  {
    "R": 1.0,
    "power": 7,
    "rank_span_0_to_k": 2
  },
  {
    "R": 1.0,
    "power": 8,
    "rank_span_0_to_k": 2
  }
]
```

## 3. Incompatibilidad de P7

Controles:

```json
[
  {
    "R": 0.1,
    "norm_U": 0.1,
    "norm_V": 0.010000000000000002,
    "dot_U_V": 0.0,
    "dot_m_V": -0.00010000000000000005,
    "actual_m2": 0.010100000000000001,
    "claimed_m2": 0.009900000000000003,
    "a_plus_R2U_norm": 0.0,
    "T2_plus_R2I_norm": 0.0
  },
  {
    "R": 0.3,
    "norm_U": 0.3,
    "norm_V": 0.09,
    "dot_U_V": 0.0,
    "dot_m_V": -0.0081,
    "actual_m2": 0.09809999999999999,
    "claimed_m2": 0.0819,
    "a_plus_R2U_norm": 0.0,
    "T2_plus_R2I_norm": 0.0
  },
  {
    "R": 0.7,
    "norm_U": 0.7,
    "norm_V": 0.48999999999999994,
    "dot_U_V": 0.0,
    "dot_m_V": -0.24009999999999992,
    "actual_m2": 0.7300999999999999,
    "claimed_m2": 0.24989999999999998,
    "a_plus_R2U_norm": 0.0,
    "T2_plus_R2I_norm": 0.0
  },
  {
    "R": 1.0,
    "norm_U": 1.0,
    "norm_V": 1.0,
    "dot_U_V": 0.0,
    "dot_m_V": -1.0,
    "actual_m2": 2.0,
    "claimed_m2": 0.0,
    "a_plus_R2U_norm": 0.0,
    "T2_plus_R2I_norm": 0.0
  }
]
```

Para todo \(R>0\) probado:

- \(U\cdot V=0\);
- \((U-V)\cdot V\neq0\);
- \(\|U-V\|^2=R^2+R^4\), no \(R^2-R^4\);
- \(a=-R^2U\).

## 4. Dos generadores — sólo ilustración de existencia

```json
{
  "J2_square_error": 0.0,
  "K2_square_error": 0.0,
  "orbit_rank_with_two_independent_generators": 4,
  "status": "illustrative existence example only; cross-relations are not derived by the program"
}
```

Este ejemplo muestra que dos operadores independientes pueden ampliar el subespacio generado. **No deriva** las relaciones correctas entre generadores del programa.

## 5. No implica

- que una dimensión espacial física sea automáticamente un nuevo generador;
- que la estructura correcta entre generadores sea una álgebra conocida concreta;
- que el cierre binario \(2^{-n}\) esté derivado;
- que el protón quede explicado por esta corrección;
- una dinámica física completa.
