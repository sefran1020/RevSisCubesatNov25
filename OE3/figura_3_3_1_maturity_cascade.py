"""
FIGURA 3.3.1: Maturity Cascade Diagram
Visualiza la disminución de madurez desde EM Simulation (100%) hasta CubeSat Body Interaction (29%)

TRAZABILIDAD: Datos extraídos de analisisOE3.txt Objective 3
Base: 14 estudios documentados en OE3 grupos A-D
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# =====================================================
# DATOS TRAZABLES DE analisisOE3.txt
# =====================================================

# Conteos de estudios por etapa de madurez
workflow_stages = {
    'EM Simulation': {
        'high_maturity': 14,  # TODOS los 14 estudios del OE3
        'low_maturity': 0,
        'studies': [
            'Islam 2015', 'Lee 2018', 'Rzymowski 2021', 'Semkin 2018',
            'Curreli 2021', 'Nguyen 2021', 'Ta 2025', 'Theoharis 2021',
            'Thunyakaset 2021', 'Liu 2019', 'Sayeed 2018', 'Mengu Cho 2015',
            'Kibria 2018', 'Priscila 2022'
        ]
    },
    'Parametric\nOptimization': {
        'high_maturity': 11,  # 79% de 14 = ~11 estudios
        'low_maturity': 3,
        'studies_high': [
            'Islam 2015', 'Lee 2018', 'Rzymowski 2021', 'Curreli 2021',
            'Nguyen 2021', 'Ta 2025', 'Liu 2019', 'Mengu Cho 2015',
            'Kibria 2018', 'Priscila 2022', 'Fawzy Ibrahim 2018'
        ],
        'studies_low': ['Sayeed 2018', 'Thunyakaset 2021', 'Kai Xue 2016']
    },
    'Mechanical\nIntegration': {
        'high_maturity': 3,  # 21% de 14 = ~3 estudios
        'low_maturity': 11,
        'studies_high': ['Kibria 2018', 'Islam 2015', 'Ta 2025 (partial)'],
        'studies_low': 'Otros 11 estudios sin documentación mecánica'
    },
    'Thermal\nAnalysis': {
        'high_maturity': 2,  # 14% de 14 = ~2 estudios
        'low_maturity': 12,
        'studies_high': ['Curreli 2021', 'Priscila 2022'],
        'studies_low': 'Otros 12 estudios sin análisis térmico'
    },
    'CubeSat Body\nInteraction': {
        'high_maturity': 4,  # 29% de 14 = ~4 estudios
        'low_maturity': 10,
        'studies_high': ['Islam 2015', 'Kibria 2018', 'Theoharis 2021', 'Mengu Cho 2015'],
        'studies_low': 'Otros 10 estudios sin modelado de interacción'
    }
}

# Calcular porcentajes
stages = list(workflow_stages.keys())
percentages = []
colors = []

for stage in stages:
    data = workflow_stages[stage]
    total = 14  # Base de 14 estudios del OE3
    high = data['high_maturity']
    percentage = (high / total) * 100
    percentages.append(percentage)

    # Asignar colores según nivel de madurez
    if percentage >= 80:
        colors.append('#2E7D32')  # Verde oscuro
    elif percentage >= 60:
        colors.append('#66BB6A')  # Verde
    elif percentage >= 40:
        colors.append('#FFA726')  # Naranja
    elif percentage >= 20:
        colors.append('#FF7043')  # Rojo-naranja
    else:
        colors.append('#D32F2F')  # Rojo

# =====================================================
# CREAR FIGURA
# =====================================================

fig, ax = plt.subplots(figsize=(12, 8))

# Crear barras horizontales
y_pos = np.arange(len(stages))
bars = ax.barh(y_pos, percentages, color=colors, edgecolor='black', linewidth=1.5)

# Añadir valores y conteos en las barras
for i, (bar, stage) in enumerate(zip(bars, stages)):
    width = bar.get_width()
    data = workflow_stages[stage]
    count = data['high_maturity']

    # Texto dentro de la barra
    ax.text(width/2, bar.get_y() + bar.get_height()/2,
            f'{width:.0f}%\n({count}/14)',
            ha='center', va='center', fontweight='bold',
            fontsize=11, color='white')

    # Texto fuera de la barra con gap específico
    ax.text(width + 3, bar.get_y() + bar.get_height()/2,
            f'Low: {data["low_maturity"]}/14',
            ha='left', va='center', fontsize=9, style='italic')

# Configuración de ejes
ax.set_yticks(y_pos)
ax.set_yticklabels(stages, fontsize=11, fontweight='bold')
ax.set_xlabel('High-Maturity Coverage (%)', fontsize=12, fontweight='bold')
ax.set_title('Figure 3.3.1: Workflow Maturity Cascade - Feeding Element Integration\n' +
             'Progressive Decline from EM Sophistication to System Integration (n=14 studies)',
             fontsize=13, fontweight='bold', pad=20)

# Líneas de referencia
ax.axvline(x=50, color='gray', linestyle='--', linewidth=1, alpha=0.5, label='50% threshold')
ax.axvline(x=75, color='green', linestyle=':', linewidth=1, alpha=0.5, label='75% high-maturity')

# Límites y grid
ax.set_xlim(0, 110)
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.legend(loc='lower right', fontsize=9)

# Anotación del gap crítico
ax.annotate('71% Feeding-to-System Gap',
            xy=(29, 4), xytext=(50, 4.5),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=11, fontweight='bold', color='red',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))

# Nota al pie con trazabilidad
fig.text(0.12, 0.02,
         'Data source: analisisOE3.txt, Objective 3 - Feeding Design and System Integration\n' +
         'Base: 14 studies from Groups A-D (Single-Feed n=9, Coaxial/Probe n=8, Complex Networks n=4, Specialized n=3)',
         fontsize=8, style='italic', va='bottom', ha='left',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('G:/RevSisOrd/OE3Figuras/Figure_3_3_1_Maturity_Cascade.png', dpi=300, bbox_inches='tight')
plt.savefig('G:/RevSisOrd/OE3Figuras/Figure_3_3_1_Maturity_Cascade.pdf', bbox_inches='tight')

print("[OK] Figura 3.3.1 generada exitosamente")
print(f"[OK] Trazabilidad: {sum([d['high_maturity'] for d in workflow_stages.values()])} puntos de datos de 14 estudios")
