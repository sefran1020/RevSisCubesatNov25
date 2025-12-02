"""
Figura: Simulation-to-Validation Workflow Progression
Diagrama de flujo mostrando la progresión desde validación simple a completa

Basado en:
- 70% single-domain (Groups A+B)
- 30% multi-domain (Groups C+D)
- Tabla 2: Coverage percentages
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# Configuración
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.size'] = 10

# Crear figura
fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis('off')

# ============= DEFINIR NODOS DEL WORKFLOW =============

# Nivel 1: Inicio (común a todos)
start_box = FancyBboxPatch(
    (6, 7.5), 2, 1,
    boxstyle="round,pad=0.1",
    edgecolor='#2C3E50',
    facecolor='#ECF0F1',
    linewidth=2.5
)
ax.add_patch(start_box)
ax.text(7, 8, 'EM Simulation\n(HFSS/CST/FEKO)\n100% Coverage',
        ha='center', va='center', fontweight='bold', fontsize=10)

# ============= RAMA IZQUIERDA: Single-Domain (70%) =============

# Anechoic Chamber Path (40%)
anechoic_box = FancyBboxPatch(
    (0.5, 5), 2.5, 1.2,
    boxstyle="round,pad=0.1",
    edgecolor='#C0392B',
    facecolor='#FADBD8',
    linewidth=2
)
ax.add_patch(anechoic_box)
ax.text(1.75, 5.6, 'Anechoic Chamber\nFar-Field Only\n40% (n=20)',
        ha='center', va='center', fontsize=9, fontweight='bold')

# VNA Path (30%)
vna_box = FancyBboxPatch(
    (0.5, 3), 2.5, 1.2,
    boxstyle="round,pad=0.1",
    edgecolor='#E74C3C',
    facecolor='#FADBD8',
    linewidth=2
)
ax.add_patch(vna_box)
ax.text(1.75, 3.6, 'VNA Testing\nS-Parameters Only\n30% (n=15)',
        ha='center', va='center', fontsize=9, fontweight='bold')

# Outcome Single-Domain
single_outcome = FancyBboxPatch(
    (0.2, 0.8), 3.2, 1.2,
    boxstyle="round,pad=0.1",
    edgecolor='#E74C3C',
    facecolor='#F5B7B1',
    linewidth=3
)
ax.add_patch(single_outcome)
ax.text(1.8, 1.4, 'Laboratory\nCharacterization\nOnly',
        ha='center', va='center', fontsize=10, fontweight='bold', color='#7B241C')
ax.text(1.8, 0.95, '⚠ Inadequate for\nMission Deployment',
        ha='center', va='center', fontsize=8, style='italic', color='#922B21')

# ============= RAMA DERECHA: Multi-Domain (30%) =============

# Specialized Path (16%)
specialized_box = FancyBboxPatch(
    (11, 5), 2.5, 1.2,
    boxstyle="round,pad=0.1",
    edgecolor='#D68910',
    facecolor='#FAE5D3',
    linewidth=2
)
ax.add_patch(specialized_box)
ax.text(12.25, 5.6, 'Specialized Systems\nStarlab/TVAC\n16% (n=8)',
        ha='center', va='center', fontsize=9, fontweight='bold')

# Combined Path (14%)
combined_box = FancyBboxPatch(
    (11, 3), 2.5, 1.2,
    boxstyle="round,pad=0.1",
    edgecolor='#27AE60',
    facecolor='#D5F4E6',
    linewidth=2
)
ax.add_patch(combined_box)
ax.text(12.25, 3.6, 'Combined Testing\nMulti-Platform\n14% (n=7)',
        ha='center', va='center', fontsize=9, fontweight='bold')

# Outcome Multi-Domain
multi_outcome = FancyBboxPatch(
    (10.6, 0.8), 3.2, 1.2,
    boxstyle="round,pad=0.1",
    edgecolor='#27AE60',
    facecolor='#ABEBC6',
    linewidth=3
)
ax.add_patch(multi_outcome)
ax.text(12.2, 1.4, 'Mission-Ready\nValidation',
        ha='center', va='center', fontsize=10, fontweight='bold', color='#145A32')
ax.text(12.2, 0.95, '✓ Environmental\nQualification',
        ha='center', va='center', fontsize=8, style='italic', color='#1E8449')

# ============= FLECHAS DE CONEXIÓN =============

# Start -> Anechoic
arrow1 = FancyArrowPatch(
    (6.8, 7.5), (2.5, 6.2),
    arrowstyle='->,head_width=0.3,head_length=0.3',
    color='#C0392B', linewidth=2, connectionstyle="arc3,rad=0.3"
)
ax.add_patch(arrow1)

# Start -> VNA
arrow2 = FancyArrowPatch(
    (6.5, 7.5), (2.5, 4.2),
    arrowstyle='->,head_width=0.3,head_length=0.3',
    color='#E74C3C', linewidth=2, connectionstyle="arc3,rad=0.2"
)
ax.add_patch(arrow2)

# Start -> Specialized
arrow3 = FancyArrowPatch(
    (7.2, 7.5), (11.5, 6.2),
    arrowstyle='->,head_width=0.3,head_length=0.3',
    color='#D68910', linewidth=2, connectionstyle="arc3,rad=-0.3"
)
ax.add_patch(arrow3)

# Start -> Combined
arrow4 = FancyArrowPatch(
    (7.5, 7.5), (11.5, 4.2),
    arrowstyle='->,head_width=0.3,head_length=0.3',
    color='#27AE60', linewidth=2, connectionstyle="arc3,rad=-0.2"
)
ax.add_patch(arrow4)

# Paths -> Outcomes
arrow5 = FancyArrowPatch(
    (1.75, 5), (1.8, 2),
    arrowstyle='->,head_width=0.25,head_length=0.25',
    color='#922B21', linewidth=1.5, linestyle='dashed'
)
ax.add_patch(arrow5)

arrow6 = FancyArrowPatch(
    (1.75, 3), (1.8, 2),
    arrowstyle='->,head_width=0.25,head_length=0.25',
    color='#922B21', linewidth=1.5, linestyle='dashed'
)
ax.add_patch(arrow6)

arrow7 = FancyArrowPatch(
    (12.25, 5), (12.2, 2),
    arrowstyle='->,head_width=0.25,head_length=0.25',
    color='#145A32', linewidth=1.5, linestyle='dashed'
)
ax.add_patch(arrow7)

arrow8 = FancyArrowPatch(
    (12.25, 3), (12.2, 2),
    arrowstyle='->,head_width=0.25,head_length=0.25',
    color='#145A32', linewidth=1.5, linestyle='dashed'
)
ax.add_patch(arrow8)

# ============= ETIQUETAS DE BIFURCACIÓN =============

# Etiqueta 70% - Single Domain
ax.text(3.5, 6.5, '70%\nSingle-Domain',
        ha='center', va='center', fontsize=11, fontweight='bold',
        color='#E74C3C',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='#E74C3C', linewidth=2))

# Etiqueta 30% - Multi-Domain
ax.text(10.5, 6.5, '30%\nMulti-Domain',
        ha='center', va='center', fontsize=11, fontweight='bold',
        color='#27AE60',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='#27AE60', linewidth=2))

# ============= ANOTACIONES CRÍTICAS =============

# Brecha crítica
gap_annotation = FancyBboxPatch(
    (4.5, 4.5), 5, 2,
    boxstyle="round,pad=0.15",
    edgecolor='#E74C3C',
    facecolor='#FADBD8',
    linewidth=2,
    linestyle='dashed',
    alpha=0.7
)
ax.add_patch(gap_annotation)

ax.text(7, 5.8, 'WORKFLOW DISCONTINUITY',
        ha='center', va='top', fontsize=11, fontweight='bold', color='#7B241C')
ax.text(7, 5.3, 'Laboratory → Operational Gap',
        ha='center', va='center', fontsize=10, style='italic', color='#922B21')
ax.text(7, 4.85, '70% lack environmental qualification',
        ha='center', va='bottom', fontsize=9, color='#641E16')

# Título principal
ax.text(7, 8.8, 'Simulation-to-Validation Workflow Configurations:\nEmpirical Progression Patterns',
        ha='center', va='center', fontsize=14, fontweight='bold')

# Leyenda de colores
legend_elements = [
    mpatches.Patch(facecolor='#FADBD8', edgecolor='#C0392B', label='Single-Domain (70%)', linewidth=2),
    mpatches.Patch(facecolor='#FAE5D3', edgecolor='#D68910', label='Specialized (16%)', linewidth=2),
    mpatches.Patch(facecolor='#D5F4E6', edgecolor='#27AE60', label='Multi-Domain (14%)', linewidth=2)
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=9, framealpha=0.95)

# Caption
caption = """Figure. Workflow progression from electromagnetic simulation to validation outcomes across 50 CubeSat antenna studies.
Simulation (100% coverage) bifurcates into single-domain (70%, red pathway) and multi-domain (30%, green pathway) validation
configurations. Single-domain approaches (anechoic chamber 40% + VNA 30%) culminate in laboratory characterization inadequate
for mission deployment. Multi-domain approaches (specialized systems 16% + combined testing 14%) achieve mission-ready validation
through environmental qualification. Central annotation highlights critical workflow discontinuity where 70% of studies fail to
bridge laboratory-to-operational gap. Arrow thickness indicates study concentration.
Data source: Table 2 coverage percentages, validated from grupoA-D.csv databases."""

fig.text(0.5, 0.02, caption, ha='center', fontsize=8, wrap=True, va='bottom')

plt.tight_layout(rect=[0, 0.11, 1, 0.96])
plt.savefig('fig_workflow_progression.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('fig_workflow_progression.pdf', bbox_inches='tight', facecolor='white')
print("✓ Figura generada: fig_workflow_progression.png / .pdf")
plt.show()
