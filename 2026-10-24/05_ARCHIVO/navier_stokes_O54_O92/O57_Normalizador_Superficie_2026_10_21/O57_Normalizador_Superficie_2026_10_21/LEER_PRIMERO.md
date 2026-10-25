# O57 · La superficie toroidal completa y la novedad de forma

**Programa de Geometría Relacional — Le Matt Ansatz Di Ego — 21 de octubre de 2026**

Continuación aditiva del hilo O40 → O44N → O45 → O53 → O54 → O55 → O56, sin reescribir el núcleo o la Imagen Total 3.8.1.

**Resultado central:** la perpendicularidad de dos tangentes materiales es una condición más débil que la conservación de todas sus relaciones métricas hasta una escala común. Formalizamos `C = σ² D` con `det D = 1`: `σ` representa la escala geométrica local y `D` la forma residual no absorbible por una escala común. `D` es independiente de un cambio uniforme de escala del espejo, pero **no es el múltiplo entero del programa**. Su papel es una realización geométrica que podrá compararse con el normalizador relacional bajo un contrato explícito.

**Complemento perpendicular:** para flujo incompresible, la tasa de área del plano material es exactamente la opuesta a la tasa de deformación normal, y el factor de área por la componente de espesor normal es 1 (en unidades relativas). No es un tercero añadido al modelo, sino su complemento geométrico dentro de R³.

**Simulación reproducible:** tres preparaciones de anillo en caja periódica 32³, superficie de 384 puntos y 90 pasos; una perturbación X y su versión rotada Y producen los mismos invariantes globales, pero diferencias desde marcas fijas. En el caso base los ángulos materiales se conservan casi rectos y, sin embargo, la métrica se deforma de manera anisótropa. Este resultado cambia dónde debemos situar la novedad de forma.

**Comenzar en:** `O57_FORMALIZACION.es.md`. Ejecutar `python codigo/o57_superficie.py` para regenerar datos y gráficos y `python verificar_integridad.py` para comprobar las huellas SHA-256. Los scripts son una exploración numérica, no acreditan convergencia ni demuestran regularidad global 3D. Las relaciones exactas están demostradas separadamente en el documento.
