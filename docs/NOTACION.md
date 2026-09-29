# Notación y tipos de objetos

Esta tabla propone nombres de lectura para evitar colisiones. No modifica los originales.

| Símbolo histórico | Uso | Nombre recomendado al integrar |
|---|---|---|
| J en v0.73–74 | Función invariante de identidad. | \(\mathcal I\) |
| J o J_R desde MF-57 | Operador lineal transversal con cuadrado −I. | \(J_R\), con dominio indicado |
| Γ en v0.80 | Selector heurístico de siguiente variable/referencia. | \(\mathrm{Sel}_{\rm frontera}\) |
| Γ* en v0.81 | Coset nuevo en una extensión afín binaria. | \(\mathrm{Ext}_{\rm afin}\) |
| Γ en v0.82 y v0.87 | Operador idempotente de cierre. | \(\mathrm{Cl}_k\) |
| Γ en v0.89–91 | Operador positivo de relajación. | \(\Gamma_X\) o \(\Gamma_Y\) |
| Γ_AB en MF-56 | Subconjunto de pares permitidos. | \(\mathcal R_{AB}\) |
| C | Familia de comparaciones o matriz de restricciones, según la fuente. | \(\mathcal C\) para preguntas; ∂ para operador |
| c | Comparación individual o constante/escala física. | \(c_{\rm obs}\) o \(c_{\rm fis}\), según dominio |
| R | Vector de referencia, su magnitud, radio o relación. | R para vector; r = ||R||; radios con subíndice |
| q_C | Aplicación cociente a clases contextuales. | \(\pi_C\) |
| q_ij en v0.91 | Residuo de proyección de una diferencia de interfaces. | \(r^{\rm geom}_{ij}\) |
| q = Cx − b en v0.89 | Defecto de restricciones. | \(q^{\rm restr}\in Y\) |
| ρ en v0.86 | Estado positivo normalizado. | \(\rho_{\rm estado}\) |
| ρ en otras ramas | Resolución, escala, norma o razón de ritmos. | Subíndice explícito por tipo |
| V | Segunda aplicación del generador o canal modal histórico. | \(V_{\rm iter}\), \(V_{\rm modal}\) |
| I | Identidad lineal o medida informacional. | \(\mathrm{Id}\), \(I_{\rm dist}\) |
| k, s, t | Profundidad, paso o parámetro de evolución. | Declarar si son índices o variables continuas |
| K | Cociente contextual, complejo topológico o representación computacional. | \(K_C\), \(\mathscr K_{\rm top}\), \(K_F\) |

## Dos controles obligatorios de tipos

**Estados y residuos:** ∂ va de X a Y; ∂*∂ actúa sobre X y ∂∂* sobre Y. No deben aplicarse al mismo vector sin una identificación explícita.

**Eje y semilla:** J_R está probado sobre R perpendicular. Si la semilla es paralela al eje, el producto antisimétrico la anula.

## Operaciones de ampliación distintas

- Refinar una partición agrega distinciones.
- Añadir un sumando agrega direcciones lineales.
- Introducir una cara en un complejo cambia relaciones topológicas.
- Agregar un generador a un álgebra requiere especificar sus relaciones.
- Cambiar orden de variables puede modificar la representación sin cambiar la función booleana.

Estas operaciones pueden modelar aspectos relacionados; ninguna equivalencia se presume por compartir el nombre «nueva capa».
