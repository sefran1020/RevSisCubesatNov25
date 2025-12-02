"""
Figura 3: Validation Comprehensiveness Pyramid
Visualización de la jerarquía de validación experimental para OE2

Basado en datos validados de:
- grupoA.csv: Anechoic Chamber (n=19-20)
- grupoB.csv: VNA-Based (n=15)
- grupoC.csv: Specialized (n=8)
- grupoD.csv: Combined (n=7)
Total: 49-50 estudios
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Configuración para publicación
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 1.2

# Datos validados de CSV
total_studies = 50  # Redondeado según PDF
levels = {
    'Level 4\nCombined': {
        'n': 7,
        'percentage': 14,
        'description': 'Multi-Domain Validation',
        'instruments': 'Anechoic + VNA + TVAC/Radiation',
        'maturity': 'Mission-Ready',
        'color': '#2ECC71'  # Verde
    },
    'Level 3\nSpecialized': {
        'n': 8,
        'percentage': 16,
        'description': 'Specialized Systems',
        'instruments': 'Starlab, TVAC, Near-field',
        'maturity': 'Environmental Qualified',
        'color': '#F39C12'  # Naranja
    },
    'Level 2\nVNA-Based': {
        'n': 15,
        'percentage': 30,
        'description': 'Frequency Domain Only',
        'instruments': 'S-parameters, Impedance',
        'maturity': 'Component-Level',
        'color': '#E74C3C'  # Rojo claro
    },
    'Level 1\nAnechoic': {
        'n': 20,  # Asumiendo 20 después de corrección
        'percentage': 40,
        'description': 'Far-Field Patterns Only',
        'instruments': 'Radiation Pattern, Gain',
        'maturity': 'Electromagnetic Only',
        'color': '#C0392B'  # Rojo oscuro
    }
}

# Crear figura
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

# Dimensiones de la pirámide (invertida - base arriba)
pyramid_levels = [
    ('Level 1\nAnechoic', 0.5, 8, 40),          # y_bottom, width, percentage
    ('Level 2\nVNA-Based', 2.5, 6.5, 30),
    ('Level 3\nSpecialized', 4.5, 5, 16),
    ('Level 4\nCombined', 6.5, 3.5, 14)
]

# Dibujar niveles de la pirámide
y_positions = []
for i, (level_name, y_bottom, width, perc) in enumerate(pyramid_levels):
    level_data = levels[level_name]

    # Calcular posición x centrada
    x_left = (12 - width) / 2

    # Crear rectángulo con bordes redondeados
    rect = FancyBboxPatch(
        (x_left, y_bottom), width, 1.5,
        boxstyle="round,pad=0.05",
        edgecolor='black',
        facecolor=level_data['color'],
        linewidth=2,
        alpha=0.85,
        zorder=3
    )
    ax.add_patch(rect)

    # Texto del nivel (nombre + porcentaje)
    ax.text(
        6, y_bottom + 0.75,
        f"{level_name.replace('Level ' + str(4-i) + chr(10), '')}\n({perc}%, n={level_data['n']})",
        ha='center', va='center',
        fontsize=12, fontweight='bold',
        color='white',
        zorder=4
    )

    # Descripción a la derecha
    ax.text(
        x_left + width + 0.3, y_bottom + 0.75,
        level_data['description'],
        ha='left', va='center',
        fontsize=9,
        style='italic',
        zorder=4
    )

    # Instrumentos a la izquierda
    ax.text(
        x_left - 0.3, y_bottom + 0.75,
        level_data['instruments'],
        ha='right', va='center',
        fontsize=8,
        color='#34495E',
        zorder=4
    )

    y_positions.append(y_bottom + 0.75)

# Flechas indicando dimensiones crecientes
arrow_x = 0.5

# Flecha 1: Resource Requirements
arrow1 = FancyArrowPatch(
    (arrow_x, 0.8), (arrow_x, 7.8),
    arrowstyle='->,head_width=0.4,head_length=0.4',
    color='#E67E22',
    linewidth=2.5,
    zorder=2
)
ax.add_patch(arrow1)

ax.text(
    arrow_x - 0.2, 4.3,
    'Resource\nRequirements\nIncrease',
    ha='right', va='center',
    fontsize=9,
    color='#E67E22',
    fontweight='bold',
    rotation=90
)

# Flecha 2: Characterization Completeness
arrow_x2 = 11.5
arrow2 = FancyArrowPatch(
    (arrow_x2, 0.8), (arrow_x2, 7.8),
    arrowstyle='->,head_width=0.4,head_length=0.4',
    color='#27AE60',
    linewidth=2.5,
    zorder=2
)
ax.add_patch(arrow2)

ax.text(
    arrow_x2 + 0.2, 4.3,
    'Characterization\nCompleteness\nIncreases',
    ha='left', va='center',
    fontsize=9,
    color='#27AE60',
    fontweight='bold',
    rotation=90
)

# Anotación crítica principal
annotation_box = FancyBboxPatch(
    (1.5, 8.5), 9, 1.2,
    boxstyle="round,pad=0.1",
    edgecolor='#E74C3C',
    facecolor='#FCF3CF',
    linewidth=2,
    zorder=5
)
ax.add_patch(annotation_box)

ax.text(
    6, 9.1,
    '70% of studies employ single-domain validation\ninadequate for mission reliability assessment',
    ha='center', va='center',
    fontsize=11,
    fontweight='bold',
    color='#922B21',
    zorder=6
)

# Estadística adicional (izquierda inferior)
stats_text = f"""Validation Coverage (n={total_studies}):
• Single-domain: 70% (n=35)
• Multi-domain: 30% (n=15)
• Environmental: 14% (TVAC/Radiation)"""

ax.text(
    0.2, 0.3,
    stats_text,
    ha='left', va='bottom',
    fontsize=8,
    color='#2C3E50',
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='gray'),
    zorder=5
)

# Título
ax.text(
    6, 9.7,
    'Validation Comprehensiveness Pyramid: Resource-Performance Trade-offs',
    ha='center', va='top',
    fontsize=14,
    fontweight='bold',
    color='#1C2833'
)

# Pie de figura
caption = """Figure 3. Hierarchical distribution of experimental validation approaches across 50 CubeSat antenna studies.
Color gradient indicates maturity level (red: electromagnetic-only → green: mission-ready). Level 1+2 (70%) represent
single-domain characterization inadequate for operational deployment, while Level 3+4 (30%) demonstrate comprehensive
multi-physics validation. Arrow directions indicate increasing resource requirements and characterization completeness.
Data source: Validated CSV databases (grupoA-D.csv)."""

fig.text(
    0.5, 0.02,
    caption,
    ha='center', va='bottom',
    fontsize=9,
    wrap=True,
    color='#34495E'
)

plt.tight_layout(rect=[0, 0.08, 1, 0.98])
plt.savefig('fig3_validation_pyramid.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('fig3_validation_pyramid.pdf', bbox_inches='tight', facecolor='white')
print("✓ Figura 3 generada: fig3_validation_pyramid.png / .pdf")
plt.show()
