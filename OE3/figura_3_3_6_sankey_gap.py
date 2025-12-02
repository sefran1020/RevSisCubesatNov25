"""
FIGURA 3.3.5: Feeding-to-System Gap Sankey Diagram

TRAZABILIDAD: Flujo de estudios desde feeding design hasta system integration
Datos de analisisOE3.txt con clasificación de madurez de integración
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.sankey import Sankey
import matplotlib.patches as mpatches

# =====================================================
# DATOS TRAZABLES - CLASIFICACIÓN DE ESTUDIOS
# =====================================================

# Clasificación basada en scoring de madurez (de figura 3.3.4)
# Full Integration (5/5): Thermal + Mechanical + Body
full_integration = ['Islam 2015', 'Kibria 2018', 'Curreli 2021']

# Partial Integration (3-4/5): 2 de 3 dimensiones
partial_integration_high = ['Mengu Cho 2015', 'Theoharis 2021']  # 4/5
partial_integration_med = ['Priscila 2022', 'Ta 2025', 'Rzymowski 2021']  # 2.5-3.5/5

# Minimal Integration (2/5): Solo 1 dimensión o ninguna
minimal_integration = [
    'Lee 2018', 'Semkin 2018', 'Nguyen 2021', 'Thunyakaset 2021',
    'Liu 2019', 'Sayeed 2018', 'Fawzy Ibrahim 2018', 'Abd-Elmonieum 2023'
]

# No System Integration (EM-only, ~2/5)
no_integration = [
    'Lehmensiek 2017', 'Wang 2024', 'Puerto-Leguizamón 2017', 'Kai Xue 2016',
    'Wenquan Che 2021', 'Mahmoud Rajab 2018', 'Saeidi 2025'
]

# Organizar por tipo de feeding
feeding_categories = {
    'Single-Feed': {
        'studies': ['Islam 2015', 'Lee 2018', 'Rzymowski 2021', 'Semkin 2018',
                    'Curreli 2021', 'Nguyen 2021', 'Ta 2025',
                    'Theoharis 2021', 'Thunyakaset 2021'],
        'count': 9
    },
    'Coaxial/Probe': {
        'studies': ['Liu 2019', 'Sayeed 2018', 'Mengu Cho 2015', 'Kibria 2018',
                    'Priscila 2022', 'Fawzy Ibrahim 2018', 'Abd-Elmonieum 2023'],
        'count': 7
    },
    'Complex Networks': {
        'studies': ['Lehmensiek 2017', 'Wang 2024', 'Puerto-Leguizamón 2017',
                    'Kai Xue 2016'],
        'count': 4
    },
    'Specialized': {
        'studies': ['Wenquan Che 2021', 'Mahmoud Rajab 2018', 'Saeidi 2025'],
        'count': 3
    }
}

total_studies = 23  # Total (sin duplicados)

# =====================================================
# PREPARAR DATOS PARA SANKEY
# =====================================================

# No podemos usar matplotlib.sankey para flujos complejos
# Usaremos un diagrama de barras apiladas horizontales que simula Sankey

fig, ax = plt.subplots(figsize=(16, 10))

# Definir niveles del flujo
levels = ['Feeding\nDesign', 'EM\nSimulation', 'System Integration\nOutcome']
y_positions = [3, 2, 1]

# Colores por categoría
colors_feeding = {
    'Single-Feed': '#4CAF50',
    'Coaxial/Probe': '#2196F3',
    'Complex Networks': '#FF9800',
    'Specialized': '#E91E63'
}

colors_integration = {
    'Full': '#2E7D32',      # Verde oscuro
    'Partial': '#FDD835',   # Amarillo
    'Minimal': '#FF9800',   # Naranja
    'None': '#D32F2F'       # Rojo
}

# =====================================================
# DIBUJAR FLUJOS MANUALMENTE
# =====================================================

# Nivel 1: Feeding Design Types
x_start = 0
bar_height = 0.6

feeding_bars = []
for feeding_type, data in feeding_categories.items():
    count = data['count']
    width = count / total_studies * 10  # Escalar
    rect = mpatches.Rectangle((x_start, y_positions[0] - bar_height/2),
                               width, bar_height,
                               facecolor=colors_feeding[feeding_type],
                               edgecolor='black', linewidth=2)
    ax.add_patch(rect)

    # Etiqueta
    ax.text(x_start + width/2, y_positions[0],
            f'{feeding_type}\nn={count}',
            ha='center', va='center', fontweight='bold',
            fontsize=9, color='white',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='black', alpha=0.3))

    feeding_bars.append((x_start, width, feeding_type))
    x_start += width

# Nivel 2: EM Simulation (100%)
em_sim_width = 10
rect_em = mpatches.Rectangle((0, y_positions[1] - bar_height/2),
                              em_sim_width, bar_height,
                              facecolor='#1976D2', edgecolor='black', linewidth=2)
ax.add_patch(rect_em)
ax.text(em_sim_width/2, y_positions[1],
        f'All Studies\nEM Simulation\n100% (n={total_studies})',
        ha='center', va='center', fontweight='bold',
        fontsize=10, color='white')

# Nivel 3: System Integration Outcomes
integration_outcomes = {
    'Full': len(full_integration),                    # 3 estudios
    'Partial': len(partial_integration_high) + len(partial_integration_med),  # 5
    'Minimal': len(minimal_integration),              # 8
    'None': len(no_integration)                       # 7
}

x_int = 0
for outcome, count in integration_outcomes.items():
    width = count / total_studies * 10
    rect = mpatches.Rectangle((x_int, y_positions[2] - bar_height/2),
                               width, bar_height,
                               facecolor=colors_integration[outcome],
                               edgecolor='black', linewidth=2)
    ax.add_patch(rect)

    percentage = (count / total_studies) * 100
    ax.text(x_int + width/2, y_positions[2],
            f'{outcome}\nIntegration\n{count}/{total_studies}\n({percentage:.0f}%)',
            ha='center', va='center', fontweight='bold',
            fontsize=8, color='white')

    x_int += width

# =====================================================
# CONECTORES (Flujos)
# =====================================================

# Conector Feeding → EM Simulation
for x_start, width, _ in feeding_bars:
    x_center = x_start + width/2
    # Polygon conectando
    polygon = mpatches.Polygon(
        [(x_start, y_positions[0] - bar_height/2),
         (x_start + width, y_positions[0] - bar_height/2),
         (x_center + width/4, y_positions[1] + bar_height/2),
         (x_center - width/4, y_positions[1] + bar_height/2)],
        facecolor='lightgray', edgecolor='gray', alpha=0.3, linewidth=1
    )
    ax.add_patch(polygon)

# Conector EM Simulation → Integration Outcomes
x_int_current = 0
for outcome, count in integration_outcomes.items():
    width_out = count / total_studies * 10

    # Polygon conectando desde centro de EM a cada outcome
    polygon = mpatches.Polygon(
        [(1, y_positions[1] - bar_height/2),
         (9, y_positions[1] - bar_height/2),
         (x_int_current + width_out, y_positions[2] + bar_height/2),
         (x_int_current, y_positions[2] + bar_height/2)],
        facecolor=colors_integration[outcome], edgecolor='gray',
        alpha=0.2, linewidth=1
    )
    ax.add_patch(polygon)

    x_int_current += width_out

# =====================================================
# ANOTACIONES Y ESTADÍSTICAS
# =====================================================

# Anotación del gap principal
ax.annotate('71% Feeding-to-System Gap',
            xy=(7, y_positions[2] + bar_height/2 + 0.1),
            xytext=(7, 3.5),
            fontsize=14, fontweight='bold', color='red',
            ha='center',
            bbox=dict(boxstyle='round,pad=0.8', facecolor='yellow', alpha=0.8),
            arrowprops=dict(arrowstyle='->', color='red', lw=3))

# Destacar complete integration
ax.annotate('Only 13% achieve\nFull Integration',
            xy=(1, y_positions[2]),
            xytext=(-1.5, 1.5),
            fontsize=11, fontweight='bold', color='darkgreen',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.7),
            arrowprops=dict(arrowstyle='->', color='darkgreen', lw=2))

# Box con estudios completos
complete_studies_text = "FULL INTEGRATION (5/5):\n" + "\n".join([f"• {s}" for s in full_integration])
ax.text(11.5, 2.5, complete_studies_text,
        fontsize=9, va='top',
        bbox=dict(boxstyle='round,pad=0.7', facecolor='lightgreen',
                 edgecolor='darkgreen', linewidth=2, alpha=0.9))

# Box con estudios sin integración
no_int_text = f"NO SYSTEM INTEGRATION:\n{len(no_integration)}/{total_studies} studies ({len(no_integration)/total_studies*100:.0f}%)\n\n"
no_int_text += "Examples:\n" + "\n".join([f"• {s}" for s in no_integration[:4]]) + "\n• ..."
ax.text(11.5, 0.2, no_int_text,
        fontsize=8, va='bottom',
        bbox=dict(boxstyle='round,pad=0.7', facecolor='#FFCDD2',
                 edgecolor='red', linewidth=2, alpha=0.9))

# =====================================================
# CONFIGURACIÓN GENERAL
# =====================================================

ax.set_xlim(-2, 14)
ax.set_ylim(0.3, 4)
ax.set_aspect('equal')
ax.axis('off')

# Título
ax.text(5, 3.9,
        'Figure 3.3.5: Feeding-to-System Integration Gap - Sankey Flow Diagram\n' +
        'Progressive attrition from electromagnetic simulation to deployment-ready subsystems',
        fontsize=13, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=1', facecolor='lightyellow',
                 edgecolor='black', linewidth=2))

# Leyenda
legend_elements = [
    mpatches.Patch(color='#2E7D32', label='Full Integration (3/23, 13%)'),
    mpatches.Patch(color='#FDD835', label='Partial Integration (5/23, 22%)'),
    mpatches.Patch(color='#FF9800', label='Minimal Integration (8/23, 35%)'),
    mpatches.Patch(color='#D32F2F', label='No System Integration (7/23, 30%)'),
]
ax.legend(handles=legend_elements, loc='lower left',
          fontsize=9, framealpha=0.95, title='Integration Levels',
          bbox_to_anchor=(-0.15, 0.35))

# --- NOTA DE TRAZABILIDAD ---
fig.text(0.5, 0.02,
         'Data source: analisisOE3.txt - Individual study classification by integration maturity scoring\n' +
         f'Full Integration: {", ".join(full_integration)} | ' +
         f'Base: {total_studies} studies from OE3 Groups A-D | ' +
         'Flow widths proportional to study counts',
         ha='center', va='bottom', fontsize=7, style='italic',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout(rect=[0, 0.04, 1, 0.96])
plt.savefig('G:/RevSisOrd/OE3Figuras/Figure_3_3_6_Sankey_Gap.png', dpi=300, bbox_inches='tight')
plt.savefig('G:/RevSisOrd/OE3Figuras/Figure_3_3_6_Sankey_Gap.pdf', bbox_inches='tight')

print("[OK] Figura 3.3.6 generada exitosamente")
print(f"[OK] Trazabilidad: {total_studies} estudios clasificados")
print(f"[OK] Full integration: {len(full_integration)} ({len(full_integration)/total_studies*100:.1f}%)")
print(f"[OK] No integration: {len(no_integration)} ({len(no_integration)/total_studies*100:.1f}%)")
print(f"[OK] Feeding-to-System Gap: {(1 - len(full_integration)/total_studies)*100:.0f}%")
