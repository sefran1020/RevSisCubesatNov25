"""
FIGURA 3.3.2: Feeding Architecture Distribution (Pie Chart)

TRAZABILIDAD: Datos extraídos de analisisOE3.txt Grupos A, B, C, D
"""

import matplotlib.pyplot as plt
import numpy as np

# =====================================================
# DATOS TRAZABLES
# =====================================================

# Conteo por categoría (de analisisOE3.txt)
feeding_types = {
    'Single-Feed': 9,        # Grupo A
    'Coaxial/Probe': 8,      # Grupo B (incluye variantes Ta)
    'Complex Networks': 4,   # Grupo C
    'Specialized': 3         # Grupo D
}

total_studies = sum(feeding_types.values())

# =====================================================
# CREAR FIGURA
# =====================================================

fig, ax = plt.subplots(figsize=(10, 8))

colors_pie = ['#4CAF50', '#2196F3', '#FF9800', '#E91E63']
wedges, texts, autotexts = ax.pie(
    feeding_types.values(),
    labels=[f'{k}\n(n={v})' for k, v in feeding_types.items()],
    autopct='%1.1f%%',
    colors=colors_pie,
    startangle=90,
    explode=(0.05, 0.05, 0.1, 0.1),
    textprops={'fontsize': 12, 'fontweight': 'bold'},
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}
)

# Mejorar legibilidad de porcentajes
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# Título
ax.set_title('Figure 3.3.2: Feeding Architecture Distribution\n' +
             f'81% convergence toward single-feed/probe configurations (n={total_studies} studies)',
             fontsize=13, fontweight='bold', pad=20)

# Anotación del hallazgo principal
convergence_pct = (feeding_types['Single-Feed'] + feeding_types['Coaxial/Probe']) / total_studies * 100
ax.text(0.5, -1.3,
        f'Key Finding: {convergence_pct:.0f}% convergence toward simplified architectures\n' +
        'suggests deployment reliability prioritized over EM optimization flexibility',
        ha='center', va='top', fontsize=10, style='italic',
        bbox=dict(boxstyle='round,pad=0.8', facecolor='lightyellow',
                 edgecolor='orange', linewidth=2, alpha=0.9),
        transform=ax.transAxes)

# Leyenda adicional con estudios destacados
legend_text = 'Examples by category:\n'
legend_text += '• Single-Feed: Islam 2015, Curreli 2021, Ta 2025\n'
legend_text += '• Coaxial/Probe: Kibria 2018, Mengu Cho 2015\n'
legend_text += '• Complex: Puerto-Leguizamon 2017, Wang 2024\n'
legend_text += '• Specialized: Saeidi 2025, Mahmoud Rajab 2018'

ax.text(1.05, 0.5, legend_text,
        transform=ax.transAxes, fontsize=9, va='center',
        bbox=dict(boxstyle='round,pad=0.7', facecolor='lightblue',
                 alpha=0.3, edgecolor='gray'))

# Nota de trazabilidad
fig.text(0.5, 0.02,
         'Data source: analisisOE3.txt Groups A-D classification | ' +
         'Base: 24 feeding element designs from systematic review OE3',
         ha='center', va='bottom', fontsize=8, style='italic',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig('G:/RevSisOrd/OE3Figuras/Figure_3_3_2_Feeding_Distribution_Pie.png', dpi=300, bbox_inches='tight')
plt.savefig('G:/RevSisOrd/OE3Figuras/Figure_3_3_2_Feeding_Distribution_Pie.pdf', bbox_inches='tight')

print("[OK] Figura 3.3.2 (Pie Chart) generada exitosamente")
print(f"[OK] Trazabilidad: {total_studies} estudios clasificados en 4 grupos")
print(f"[OK] Convergencia: {convergence_pct:.1f}% hacia single-feed/probe")
