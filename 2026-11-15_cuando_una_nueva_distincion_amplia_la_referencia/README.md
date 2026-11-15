# Cuándo una nueva distinción amplía la referencia

**Autor público:** Le Matt Ansatz Di Ego · **Fecha:** 15 de noviembre de 2026 · **Estado:** nota para examen editorial.

La [nota en español](Nota_final.md) formaliza cuándo una consulta distingue estados que una referencia anterior reunía. Desarrolla una normalización mediante el mínimo común múltiplo y una descomposición por proyección ortogonal. Aplica ese marco a una correlación ponderada de Goldbach y compara el papel de las fases en Navier–Stokes y del orden de transporte en Yang–Mills. La condición de Goldbach es un certificado **condicional**; construir una semilla con estimaciones uniformes permanece abierto.

El [verificador](Verificar.py) comprueba identidades finitas de grillas, proyecciones y reflexión. Con Python 3 y su biblioteca estándar:

```sh
python Verificar.py
```

La ejecución entregada registra [4.427 controles y el valor de G(30)](Verificacion.txt). Estos controles son finitos y numéricos; las demostraciones y condiciones generales se leen en la nota.

En esta edición se incorporó la firma pública, se sustituyeron las referencias a ecuaciones sin numerar por referencias a su contenido y se enlazaron tres fuentes identificables. El texto matemático y el verificador proceden de la entrega del autor. [English guide](README.en.md) · [Derechos y uso](RIGHTS.md).
