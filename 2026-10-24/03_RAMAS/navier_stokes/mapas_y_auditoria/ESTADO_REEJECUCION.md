# ESTADO DE REEJECUCIÓN · 24 octubre 2026

- **Hecho en esta compilación:** prueba completa de integridad SHA-256 de los archivos extraídos del corpus histórico (953/953 antes de anexos finales; la verificación final contabiliza también los anexos). 
- **Hecho en esta compilación:** ejecutar `experimentos/verificar_o93.py` sobre una COPIA de O93, para no sobrescribir ni alterar los archivos de origen. Comprobaciones E1–E5 informan PASA, total 5 grupos. Incluir registros exactos en `REEJECUCION_O93_2026-10-24/log_verificar_o93.txt`.
- **Hecho en esta compilación:** ejecutar `experimentos/simulacion_galerkin.py` sobre la misma copia, con N=16 dt=0.004; N=24 dt=0.004 y dt=0.002; ambas fases c=±1 y tiempo T=0.08. Los resultados finales coinciden con los históricamente reportados hasta aproximaciones del orden de 10⁻¹².
- **No hecho:** reejecutar cada uno de los cientos de experimentos O24–O92. Se preservan sus scripts y resultados históricos, que no deben confundirse con pruebas recién auditadas.
- **No hecho:** un chequeo independiente matemático línea por línea de todas las demostraciones, ni validación externa por pares.
- **No demostrado:** regularidad global incondicional NS 3D para todos los datos. El hallazgo integrado O93 es identidad exacta y criterio suficiente condicional.

### Reejecución de O93
```bash
python3 06_O93_SINTESIS_CERTIFICADOS/experimentos/verificar_o93.py
python3 06_O93_SINTESIS_CERTIFICADOS/experimentos/simulacion_galerkin.py
```
Estas llamadas pueden sobreescribir resultados en la carpeta original. Para auditoría estricta, trabajar sobre una copia como se hizo aquí.
