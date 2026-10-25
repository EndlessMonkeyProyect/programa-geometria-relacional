# Programa de Geometría Relacional — Imagen Total v3.8.1, candidata aditiva
**Le Matt Ansatz Di Ego · 21 de octubre de 2026**

Esta revisión **parte de la última base localizada, v3.8.0-candidata**, sin rebajar su versión a 3.5. El ZIP original se conserva **íntegro y con huella SHA-256** en `archivo/BASE_V3_8_0_INTACTA.zip`. Dentro de esa base permanece a su vez íntegra la v3.7.0 y su genealogía. No se han editado los originales ni actualizado GitHub.

## Qué se incorpora (no se supone demostrado)

1. `01_geometria/ENSAYO_C4_Y_REFERENCIA.md`: formalización del cierre colectivo tetraédrico con referencia fija y de la distinción foco común / encuentros puntuales / raíces aritméticas.
2. `02_computacion/P_VINCULOS_Y_CERTIFICADOS.md`: interpretación de la propuesta de **P como cristal directo**, con ruta positiva, negativa verificable, indeterminación relacional, coste y frontera NP.
3. `03_integracion/IMAGEN_TOTAL_INCREMENTO.md`: lugar exacto de ambos resultados en las cinco capas y condiciones de promoción.
4. `04_auditoria/INFORME_REVISION.md`: auditoría independiente de la v3.8.0 en este entorno y límites de cobertura.

## Estado de las afirmaciones

- [T] C4: 16 estados de 4 reflexiones y recuperación del centro en 0/4 caras bajo referencia fija; 4 refleja un nuevo tetraedro regular con escala 5/3. **Condicionado al modelo euclidiano y al operador elegido.**
- [T] Un grafo dirigido **explícito** admite certificado positivo (camino) o negativo (conjunto alcanzable cerrado) para accesibilidad en tiempo O(V+E). Es conocimiento algorítmico establecido, usado aquí como realización de la intuición relacional.
- [T] XOR de pares con estructuras de paridad admite distinción entre relación forzada, independencia y contradicción con costes eficientes.
- [A] No hay prueba de que toda instancia NP se reduzca a una interfaz de costo polinómico; tampoco de que la coincidencia geométrica determine raíces aritméticas.

## Reconstrucción

Abrir esta edición, consultar `04_auditoria/INFORME_REVISION.md` y extraer `archivo/BASE_V3_8_0_INTACTA.zip` en otra carpeta para acceder a los 37 registros de v3.8.0, sus cinco capas, tests, manifiesto y base archivada v3.7.0. Los suplementos son aditivos y **no alteran** el registro histórico. Para verificar la nueva edición: `python verificar_integridad.py` y `python tests/verificar_addenda.py`.

**Alcance:** investigación formal en desarrollo. P versus NP, Yang–Mills y Navier–Stokes no quedan resueltos. La bibliografía es comparación externa, no fuente constitutiva de las reglas del programa.
