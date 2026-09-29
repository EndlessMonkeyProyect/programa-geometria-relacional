# VALIDATION v0.68 — MF-60B

- Horn vs brute force: 1800 pruebas, 0 fallos.
- XOR vs brute force: 1800 pruebas, 0 fallos.
- 2-SAT SCC vs brute force: 1800 pruebas, 0 fallos.
- Subfórmulas propias del cubo 3-SAT: 254 pruebas, 0 fallos respecto de 'todas son SAT'.

Contraejemplo de propagación unitaria:
- fórmula completa SAT? False
- propagación unitaria reporta consistente? True
- asignaciones unitarias encontradas: {}

Los controles positivos verifican implementaciones finitas de algoritmos conocidos en sus familias. No constituyen una solución nueva de P vs NP. El contraejemplo sólo refuta la suficiencia universal de la propagación unitaria como certificado completo.
