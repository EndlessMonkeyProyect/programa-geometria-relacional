# VALIDATION v0.64 — dependencia relacional y canales

**Estado:** PASS para los teoremas combinatorios declarados. La generación física de canales permanece OPEN.

- Descomposición exacta: 5000 pruebas, 0 fallos.
- Criterio \(D_R=0\iff\Gamma=\pi_A(\Gamma)	imes\pi_B(\Gamma)\): 5000 pruebas, 0 fallos.
- Cota superior: 5000 pruebas, 0 fallos.
- Aditividad: 1000 pruebas, 0 fallos.
- No-go de frontera desnuda: 49 pares de tamaños probados, 0 fallos al construir un cociente binario común.

## Ejemplos

```json
{
  "pure_local_restriction": {
    "gamma": [
      [
        0,
        0
      ],
      [
        0,
        1
      ]
    ],
    "metrics": [
      1.0,
      0.0,
      0.0,
      1.0
    ]
  },
  "binary_equality_coupling": {
    "gamma": [
      [
        0,
        0
      ],
      [
        1,
        1
      ]
    ],
    "metrics": [
      0.0,
      0.0,
      1.0,
      1.0
    ]
  },
  "partial_coupling": {
    "gamma": [
      [
        0,
        0
      ],
      [
        0,
        1
      ],
      [
        1,
        1
      ]
    ],
    "metrics": [
      0.0,
      0.0,
      0.41503749927884376,
      0.41503749927884376
    ]
  },
  "perfect_matching_4": {
    "gamma": [
      [
        0,
        0
      ],
      [
        1,
        1
      ],
      [
        2,
        2
      ],
      [
        3,
        3
      ]
    ],
    "metrics": [
      0.0,
      0.0,
      2.0,
      2.0
    ]
  }
}
```

## No implica

- que \(D_R\) sea información mutua de Shannon;
- que todo acoplamiento físico se reduzca a cardinalidades;
- que la naturaleza generativa esté derivada;
- que \(a=V	imes R\) sea ya el operador físico de interacción;
- una ley de selección temporal;
- validación experimental.
