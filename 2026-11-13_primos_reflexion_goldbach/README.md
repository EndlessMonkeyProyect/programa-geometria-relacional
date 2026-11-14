# Primos, reflexión y Goldbach — 13 de noviembre de 2026

**Endless Monkey Project**  
*Relational Geometry Program*

**Autor:** Le Matt Ansatz Di Ego.

**Estado:** revisión v3.0. Presenta identidades finitas y analíticas bajo hipótesis explícitas, junto con las condiciones necesarias para conectar esta representación con el operador de Li–Liu.

## Contenido

- [`PRIMOS_REFLEXION_GOLDBACH_v3.md`](PRIMOS_REFLEXION_GOLDBACH_v3.md): la involución modular $`J_N f(r)=f(-r)`$ y la correlación ponderada de Goldbach como $`\|P_+a_N\|^2-\|P_-a_N\|^2`$. Incluye los sectores CRT, las identidades con funciones $`L`$, el defecto del peso de von Mangoldt, tres límites demostrados (NG–1, NG–2, NG–3), la estabilidad bajo reconstrucción, la certificación finita con peso escalón y la frontera espectral de Li–Liu.
- `verificar_puente_goldbach_v3.py`: comprobaciones exactas e intervalos racionales, solo biblioteca estándar.

## Reproducción

```bash
python3 verificar_puente_goldbach_v3.py
```

Verifica las identidades simbólicas en $`\mathbb Q[\log p]`$ para los 499 pares $`4\le N\le1000`$, la matriz CRT de $`N=30`$, la multiplicidad de clases de $`Q_N`$ y el soporte del defecto primo. Calcula intervalos racionales para $`N=30,42,60,210`$ y una banda certificada para $`\tfrac{16}{9}C_2-G_{\mathrm{step}}(30)`$.

## Cambios respecto de la v2

- Tabla inicial de contratos y estado de cada proposición.
- «Reflexión» reservada para la involución modular $`J_N`$; el operador de cuatro fases $`J^2=-I`$ es otro operador.
- Teorema C′ como forma principal; la forma con $`D`$ queda como corolario.
- Lema de soporte: con pesos no negativos, la positividad depende de si $`S\cap(-S)`$ es no vacío.
- No-go modular en dos versiones: sin soporte cambia la positividad; con soporte fijo cambia la magnitud.
- Norma exacta $`\|Q_{N,K}\|=\sqrt{\lceil K/N\rceil}`$.
- Dimensiones locales de los sectores CRT, incluido $`q=2`$.
- Norma del defecto primo en $`\mathrm{Re}(s)>1/2`$.
- Asintótico incondicional de $`D_\phi(N)`$ por el teorema de los números primos.
- Diagnóstico de $`N=30`$ separado del operador $`T_N`$ (peso escalón y $`N<e^{10}`$).
- Certificación simbólica para $`N\le1000`$ e intervalos racionales.
