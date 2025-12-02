"""
Figura: Validation Coverage Gaps - Critical Deficiencies
Gráfico de barras horizontales mostrando brechas de validación identificadas

Basado en Tabla 2 (Critical Gaps) y datos de discusión:
- Environmental testing inadequacy: 86% deficiency
- Multi-domain characterization: 70% single-domain only
- Resource accessibility: Specialized systems only 16%
"""

import matplotlib.pyplot as plt
import numpy as np

# Configuración
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.size'] = 11

# Datos validados de Tabla 2 y Sección 4.2
gaps = {
    'Environmental Testing\n(Thermal/Vibration/Radiation)': {
        'adequate': 14,
        'deficient': 86,
        'group': 'Specialized + Combined',
        'n_adequate': 7,  # Grupo D primarily
        'color': '#E74C3C'
    },
    'Multi-Domain\nCharacterization': {
        'adequate': 30,
        'deficient': 70,
        'group': 'Specialized + Combined',
        'n_adequate': 15,  # Groups C+D
        'color': '#E67E22'
    },
    'Resource Accessibility\n(Starlab/TVAC)': {
        'adequate': 16,
        'deficient': 84,
        'group': 'Specialized only',
        'n_adequate': 8,  # Group C
        'color': '#F39C12'
    },
    'Platform Interaction\nModeling': {
        'adequate': 29,
        'deficient': 71,
        'group': 'Feeding integration',
        'n_adequate': 14,  # De Tabla 3 (OE3 pero relevante)
        'color': '#D35400'
    }
}

# Crear figura
fig, ax = plt.subplots(figsize=(12, 7))

# Preparar datos
categories = list(gaps.keys())
deficient = [gaps[cat]['deficient'] for cat in categories]
adequate = [gaps[cat]['adequate'] for cat in categories]
colors_def = [gaps[cat]['color'] for cat in categories]
colors_adeq = ['#27AE60' for _ in categories]

y_pos = np.arange(len(categories))

# Barras horizontales apiladas
bars_def = ax.barh(y_pos, deficient, color=colors_def, alpha=0.8,
                    edgecolor='black', linewidth=1.5, label='Deficient Coverage')
bars_adeq = ax.barh(y_pos, adequate, left=deficient, color=colors_adeq,
                     alpha=0.8, edgecolor='black', linewidth=1.5,
                     label='Adequate Coverage')

# Añadir valores en las barras
for i, (d, a) in enumerate(zip(deficient, adequate)):
    # Texto deficiente
    ax.text(d/2, i, f'{d}%\n(n={50-gaps[categories[i]]["n_adequate"]})',
            ha='center', va='center', color='white', fontweight='bold',
            fontsize=10)

    # Texto adecuado
    if a > 10:  # Solo si hay espacio suficiente
        ax.text(d + a/2, i, f'{a}%\n(n={gaps[categories[i]]["n_adequate"]})',
                ha='center', va='center', color='white', fontweight='bold',
                fontsize=10)
    else:
        ax.text(d + a + 2, i, f'{a}%',
                ha='left', va='center', color='#27AE60', fontweight='bold',
                fontsize=9)

# Añadir anotaciones de grupo responsable
for i, cat in enumerate(categories):
    ax.text(103, i, gaps[cat]['group'],
            ha='left', va='center', fontsize=8, style='italic',
            color='#34495E')

# Línea vertical en 70% (punto crítico)
ax.axvline(x=70, color='red', linestyle='--', linewidth=2, alpha=0.7,
           label='Critical Threshold (70%)')

# Configuración de ejes
ax.set_yticks(y_pos)
ax.set_yticklabels(categories)
ax.set_xlabel('Coverage Percentage (%)', fontweight='bold', fontsize=12)
ax.set_xlim(0, 110)
ax.set_title('Validation Coverage Gaps: Critical Deficiencies in CubeSat Antenna Research',
             fontweight='bold', fontsize=13, pad=20)

# Grid
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Leyenda
ax.legend(loc='lower right', fontsize=10, framealpha=0.95)

# Anotación de hallazgo crítico
textstr = """Critical Finding:
70-86% of studies lack
comprehensive validation
required for mission-ready
deployment"""

props = dict(boxstyle='round', facecolor='#FCF3CF', alpha=0.9,
             edgecolor='#E74C3C', linewidth=2)
ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props, fontweight='bold',
        color='#922B21')

# Estadísticas adicionales
stats_text = f"""Total corpus: n=50 studies
Single-domain validation: 70% (n=35)
Environmental testing: 14% (n=7)
Comprehensive validation: 14% (n=7)"""

props2 = dict(boxstyle='round', facecolor='white', alpha=0.9,
              edgecolor='gray', linewidth=1)
ax.text(0.98, 0.02, stats_text, transform=ax.transAxes, fontsize=9,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=props2, color='#2C3E50', family='monospace')

# Caption
caption = """Figure. Systematic validation coverage gaps across four critical dimensions in CubeSat antenna research (n=50 studies).
Red bars indicate deficient coverage; green bars show adequate coverage. Environmental testing shows highest deficiency (86%),
followed by platform interaction modeling (71%) and multi-domain characterization (70%). Dashed line marks critical 70% threshold
beyond which validation inadequacy threatens mission reliability. Data extracted from: Table 2 (Critical Gaps column),
Table 3 (Platform Interaction: 29% high-maturity), and Discussion Section 4.2 (validation deficiency percentages).
Source: Validated analysis of grupoA-D.csv databases."""

fig.text(0.5, 0.01, caption, ha='center', fontsize=8, wrap=True, va='bottom')

plt.tight_layout(rect=[0, 0.12, 1, 0.96])
plt.savefig('fig_validation_coverage_gaps.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('fig_validation_coverage_gaps.pdf', bbox_inches='tight', facecolor='white')
print("✓ Figura generada: fig_validation_coverage_gaps.png / .pdf")
plt.show()
