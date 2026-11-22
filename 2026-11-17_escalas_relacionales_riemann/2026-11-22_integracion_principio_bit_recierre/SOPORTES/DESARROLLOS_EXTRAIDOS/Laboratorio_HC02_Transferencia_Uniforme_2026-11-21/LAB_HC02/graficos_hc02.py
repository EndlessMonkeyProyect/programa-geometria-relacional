#!/usr/bin/env python3
"""Optional matplotlib plots from the reproducible CSVs."""
import csv
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
with (ROOT/'escalas.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
x=[float(r['x']) for r in rows]
plt.figure(figsize=(10.5,5.4))
plt.plot(x,[float(r['theta_part_sqrt']) for r in rows],label='Primos ordinarios: término θ',linewidth=1.5)
plt.plot(x,[float(r['power_part_sqrt']) for r in rows],label='Potencias heredadas: corrección U',linewidth=1.5)
plt.plot(x,[float(r['G_sqrt']) for r in rows],label='Resultado total: G(x)/√x',linewidth=2.1)
plt.axhline(0,color='gray',linewidth=0.7)
plt.xscale('log');plt.xlabel('Escala x (logarítmica)');plt.ylabel('Contribución normalizada por √x')
plt.title('HC-02 · Cancelación entre primos y potencias primas')
plt.legend(loc='best');plt.grid(alpha=0.2);plt.tight_layout()
plt.savefig(ROOT/'transferencia_normalizada.png',dpi=190)
plt.close()
with (ROOT/'frontera.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
x=[float(r['x']) for r in rows]
plt.figure(figsize=(10.2,5.0))
plt.plot(x,[float(r['H_sqrt']) for r in rows],marker='o',label='H(x)/√x (HC-01)')
plt.plot(x,[float(r['Bpow_over_sqrt']) for r in rows],marker='s',label='B_potencias, truncada/√x (HC-02)')
plt.axhline(2,linestyle='--',color='gray',label='Escala asintótica 2')
plt.xscale('log');plt.xlabel('Escala x (logarítmica)');plt.ylabel('Corrección heredada /√x')
plt.title('HC-02 · Dos representaciones de la corrección heredada')
plt.legend();plt.grid(alpha=.2);plt.tight_layout()
plt.savefig(ROOT/'frontera_cuadratica.png',dpi=190)
plt.close()
print('Gráficos guardados.')
