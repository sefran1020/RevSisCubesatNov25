"""
Figura: Instrument-Validation Recommendation Alignment Matrix
Heatmap mostrando la complementariedad entre instrumentos y recomendaciones de validación

Basado en búsquedas validadas en CSV:
- Anechoic chamber: 37 menciones totales
- VNA/Network Analyzer: 28 menciones
- Starlab/TVAC/Satimo: 10 menciones
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Configuración para publicación
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.size'] = 10

# Datos validados de búsquedas en CSV
instrument_distribution = {
    'Anechoic Chamber': {'A': 17, 'B': 10, 'C': 6, 'D': 4},
    'VNA/Network Analyzer': {'A': 9, 'B': 14, 'C': 4, 'D': 1},
    'Specialized Systems\n(Starlab/TVAC)': {'A': 4, 'B': 1, 'C': 4, 'D': 1}
}

# Recomendaciones de validación (extraídas de analisisOE2.txt)
validation_recommendations = {
    'A': 'Further testing,\nReal-world validation',
    'B': 'Impedance validation,\nMulti-band testing',
    'C': 'Environmental testing,\nSpace qualification',
    'D': 'Comprehensive\nintegration validation'
}

# Crear matriz para heatmap
groups = ['Group A\n(n=20)', 'Group B\n(n=15)', 'Group C\n(n=8)', 'Group D\n(n=7)']
instruments = list(instrument_distribution.keys())

# Construir matriz de datos
matrix = []
for instrument in instruments:
    row = [instrument_distribution[instrument][g] for g in ['A', 'B', 'C', 'D']]
    matrix.append(row)

matrix = np.array(matrix)

# Calcular porcentajes por grupo
group_totals = np.array([20, 15, 8, 7])
matrix_pct = (matrix / group_totals * 100).round(1)

# Crear figura con subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})

# ============= SUBPLOT 1: HEATMAP =============
# Crear heatmap
sns.heatmap(
    matrix,
    annot=True,
    fmt='d',
    cmap='YlOrRd',
    cbar_kws={'label': 'Number of Studies'},
    linewidths=2,
    linecolor='white',
    square=False,
    ax=ax1,
    vmin=0,
    vmax=20
)

# Añadir porcentajes como texto secundario
for i in range(len(instruments)):
    for j in range(len(groups)):
        text = ax1.text(
            j + 0.5, i + 0.7,
            f'({matrix_pct[i, j]:.0f}%)',
            ha='center', va='center',
            color='gray',
            fontsize=8
        )

ax1.set_xticklabels(groups, rotation=0, ha='center')
ax1.set_yticklabels(instruments, rotation=0, va='center')
ax1.set_xlabel('Validation Configuration Group', fontweight='bold', fontsize=11)
ax1.set_ylabel('Measurement Instrument', fontweight='bold', fontsize=11)
ax1.set_title('Instrument Distribution Across Validation Configurations',
              fontweight='bold', fontsize=12, pad=15)

# Añadir líneas divisorias para destacar patrones
ax1.axhline(y=1, color='blue', linewidth=3, alpha=0.3)
ax1.axvline(x=2, color='green', linewidth=3, alpha=0.3)

# ============= SUBPLOT 2: BARRAS APILADAS =============
# Datos para barras apiladas (distribución por instrumento)
bar_data = pd.DataFrame(
    matrix.T,
    columns=instruments,
    index=groups
)

bar_data.plot(
    kind='barh',
    stacked=True,
    ax=ax2,
    color=['#E74C3C', '#3498DB', '#2ECC71'],
    edgecolor='black',
    linewidth=1.2
)

ax2.set_xlabel('Total Mentions', fontweight='bold', fontsize=11)
ax2.set_ylabel('')
ax2.set_title('Cumulative Instrument Usage', fontweight='bold', fontsize=12, pad=15)
ax2.legend(title='Instrument Type', loc='lower right', fontsize=8, framealpha=0.9)
ax2.grid(axis='x', alpha=0.3, linestyle='--')

# Añadir anotaciones de totales
for i, group in enumerate(groups):
    total = matrix[:, i].sum()
    ax2.text(
        total + 1, i,
        f'n={total}',
        va='center',
        fontweight='bold',
        fontsize=9
    )

# ============= ANOTACIONES CLAVE =============
# Anotar hallazgos principales
fig.text(
    0.5, 0.95,
    'Instrument-Validation Configuration Alignment Matrix',
    ha='center',
    fontsize=14,
    fontweight='bold'
)

# Caption
caption = """Figure. Distribution of experimental measurement instruments across four validation configuration groups (n=50 studies).
Left panel: Heatmap showing absolute counts and percentages. Right panel: Cumulative instrument usage per group.
Group A (40%) emphasizes anechoic chambers for far-field characterization; Group B (30%) relies on VNA for frequency-domain
analysis; Group C (16%) employs specialized systems (Starlab/TVAC) for environmental qualification; Group D (14%) integrates
multiple instruments for comprehensive validation. Color intensity indicates study concentration.
Data source: Validated searches in grupoA-D.csv (anechoic: 37 mentions, VNA: 28, specialized: 10)."""

fig.text(
    0.5, 0.02,
    caption,
    ha='center',
    fontsize=8,
    wrap=True,
    va='bottom'
)

plt.tight_layout(rect=[0, 0.10, 1, 0.93])
plt.savefig('fig_instrument_validation_matrix.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('fig_instrument_validation_matrix.pdf', bbox_inches='tight', facecolor='white')
print("✓ Figura generada: fig_instrument_validation_matrix.png / .pdf")
plt.show()
