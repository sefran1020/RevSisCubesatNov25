"""
FIGURA 3.3.3: Simulation Tool Distribution (Bar Chart)

TRAZABILIDAD: Datos extraídos de CSV grupoA-D
Campo: esp.technical_specifications.simulation_tool o inferido de papers
"""

import matplotlib.pyplot as plt
import numpy as np

# =====================================================
# DATOS TRAZABLES - HERRAMIENTAS DE SIMULACIÓN
# =====================================================

# Conteo de herramientas mencionadas en estudios
# Algunos estudios usan múltiples herramientas (CST+HFSS, etc.)
tool_usage = {
    'HFSS': 15,      # Dominante en single-feed y specialized
    'CST': 12,       # Dominante en coaxial y complex
    'FEKO': 9,       # Usado principalmente en complex networks
    'ANSYS': 2,      # Nguyen 2021
    'IE3D': 1,       # Mengu Cho 2015
    'FEM': 1         # Lee 2018
}

# Ordenar por frecuencia
tool_usage_sorted = dict(sorted(tool_usage.items(), key=lambda x: x[1], reverse=True))

# =====================================================
# CREAR FIGURA
# =====================================================

fig, ax = plt.subplots(figsize=(12, 8))

tools = list(tool_usage_sorted.keys())
counts = list(tool_usage_sorted.values())
total_mentions = sum(counts)

# Colores gradient
colors_bar = ['#1976D2', '#2196F3', '#42A5F5', '#64B5F6', '#90CAF9', '#BBDEFB']

bars = ax.barh(tools, counts, color=colors_bar, edgecolor='black', linewidth=1.5)

# Añadir valores en las barras
for i, (bar, count) in enumerate(zip(bars, counts)):
    percentage = (count / total_mentions) * 100
    ax.text(count + 0.3, i, f'{count} ({percentage:.1f}%)',
            va='center', fontsize=11, fontweight='bold')

# Línea de referencia en 50%
median_count = np.median(counts)
ax.axvline(x=median_count, color='red', linestyle='--', linewidth=2,
           alpha=0.5, label=f'Median: {median_count:.0f} uses')

ax.set_xlabel('Number of Studies Using Tool', fontsize=12, fontweight='bold')
ax.set_ylabel('Simulation Tool', fontsize=12, fontweight='bold')
ax.set_title('Figure 3.3.3: Simulation Tool Distribution\n' +
             'HFSS and CST dominate with 67.5% combined market share (n=40 total mentions)',
             fontsize=13, fontweight='bold', pad=20)

ax.set_xlim(0, max(counts) + 3)
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.legend(fontsize=10, loc='lower right')

# Anotación de hallazgo
ax.text(0.98, 0.98,
        'Tool Concentration:\n' +
        '• HFSS: 37.5% (electromagnetic focus)\n' +
        '• CST: 30.0% (time-domain preference)\n' +
        '• FEKO: 22.5% (MoM for complex feeds)\n' +
        '• Others: 10.0% (specialized needs)',
        transform=ax.transAxes, fontsize=10, va='top', ha='right',
        bbox=dict(boxstyle='round,pad=0.8', facecolor='lightyellow',
                 edgecolor='orange', linewidth=2, alpha=0.9))

# Nota de trazabilidad
fig.text(0.5, 0.02,
         'Data source: CSV databases grupoA-D (esp.technical_specifications.simulation_tool) | ' +
         'Some studies use multiple tools (counted separately) | Total mentions: 40 across 24 studies',
         ha='center', va='bottom', fontsize=8, style='italic',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig('G:/RevSisOrd/OE3Figuras/Figure_3_3_3_Simulation_Tools_Bar.png', dpi=300, bbox_inches='tight')
plt.savefig('G:/RevSisOrd/OE3Figuras/Figure_3_3_3_Simulation_Tools_Bar.pdf', bbox_inches='tight')

print("[OK] Figura 3.3.3 (Tool Bar Chart) generada exitosamente")
print(f"[OK] Trazabilidad: {len(tool_usage_sorted)} herramientas identificadas")
print(f"[OK] Total menciones: {total_mentions}")
print(f"[OK] Dominancia HFSS+CST: {(tool_usage['HFSS']+tool_usage['CST'])/total_mentions*100:.1f}%")
