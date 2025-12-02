"""
FIGURA 3.3.4: Integration Gap Heatmap

TRAZABILIDAD: Matriz cruzando tipos de feeding con etapas de workflow
Datos de analisisOE3.txt Grupos A, B, C, D con scoring de madurez por estudio
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# =====================================================
# DATOS TRAZABLES - MATRIZ DE MADUREZ POR ESTUDIO
# =====================================================

# Estructura: [EM_Sim, Param_Opt, Thermal, Mechanical, CubeSat_Body]
# Valores: 1 = high-maturity, 0.5 = partial, 0 = low/absent

# GRUPO A: Single-Feed (n=9)
single_feed_studies = {
    'Islam 2015': [1, 1, 1, 1, 1],           # Completo (HORYU-IV)
    'Lee 2018': [1, 1, 0, 0, 0],             # Solo EM+Opt
    'Rzymowski 2021': [1, 1, 0, 0, 0.5],     # EM+Opt, partial body
    'Semkin 2018': [1, 1, 0, 0, 0],          # Solo EM+Opt
    'Curreli 2021': [1, 1, 1, 1, 1],         # Completo (multiphysics)
    'Nguyen 2021': [1, 1, 0, 0, 0],          # Solo EM+Opt
    'Ta 2025': [1, 1, 0, 0.5, 0.5],          # EM+Opt, partial mech+body
    'Theoharis 2021': [1, 1, 0, 0, 1],       # EM+Opt+Body
    'Thunyakaset 2021': [1, 0, 0, 0, 0],     # Solo EM
}

# GRUPO B: Coaxial/Probe (n=8, eliminando duplicado Ta)
coaxial_probe_studies = {
    'Liu 2019': [1, 1, 0, 0, 0],             # EM+Opt
    'Sayeed 2018': [1, 0, 0, 0, 0],          # Solo EM
    'Mengu Cho 2015': [1, 1, 1, 0.5, 1],     # EM+Opt+Thermal+Body
    'Kibria 2018': [1, 1, 1, 1, 1],          # Completo (BIRDS-1)
    'Priscila 2022': [1, 1, 1, 0.5, 0.5],    # EM+Opt+Thermal
    'Fawzy Ibrahim 2018': [1, 1, 0.5, 0, 0], # EM+Opt+Partial thermal
    'Abd-Elmonieum 2023': [1, 1, 0, 0, 0],   # EM+Opt
}

# GRUPO C: Complex Networks (n=4)
complex_network_studies = {
    'Lehmensiek 2017': [1, 1, 0, 0, 0.5],    # EM+Opt, minimal body
    'Wang 2024': [1, 1, 0, 0, 0],            # EM+Opt
    'Puerto-Leguizamón 2017': [1, 1, 0, 0, 0], # EM+Opt
    'Kai Xue 2016': [1, 0.5, 0, 0, 0],       # EM, partial opt
}

# GRUPO D: Specialized (n=3)
specialized_studies = {
    'Wenquan Che 2021': [1, 1, 0, 0, 0],     # EM+Opt
    'Mahmoud Rajab 2018': [1, 1, 0, 0, 0],   # EM+Opt
    'Saeidi 2025': [1, 1, 0, 0, 0],          # EM+Opt
}

# Consolidar todos los estudios
all_studies_matrix = {
    **single_feed_studies,
    **coaxial_probe_studies,
    **complex_network_studies,
    **specialized_studies
}

# =====================================================
# CALCULAR PROMEDIOS POR GRUPO Y ETAPA
# =====================================================

def calculate_group_averages(studies_dict):
    """Calcula el promedio de madurez para cada etapa de workflow"""
    if not studies_dict:
        return [0, 0, 0, 0, 0]

    stages = list(zip(*studies_dict.values()))
    return [np.mean(stage) * 100 for stage in stages]

# Calcular promedios
single_feed_avg = calculate_group_averages(single_feed_studies)
coaxial_probe_avg = calculate_group_averages(coaxial_probe_studies)
complex_network_avg = calculate_group_averages(complex_network_studies)
specialized_avg = calculate_group_averages(specialized_studies)

# Crear matriz para heatmap
heatmap_data = np.array([
    single_feed_avg,
    coaxial_probe_avg,
    complex_network_avg,
    specialized_avg
])

# =====================================================
# CREAR FIGURA PRINCIPAL
# =====================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8),
                                gridspec_kw={'width_ratios': [3, 1]})

# --- HEATMAP PRINCIPAL ---
workflow_stages = ['EM\nSimulation', 'Parametric\nOptimization',
                   'Thermal\nAnalysis', 'Mechanical\nIntegration',
                   'CubeSat Body\nInteraction']

feeding_types = [f'Single-Feed\n(n={len(single_feed_studies)})',
                 f'Coaxial/Probe\n(n={len(coaxial_probe_studies)})',
                 f'Complex Networks\n(n={len(complex_network_studies)})',
                 f'Specialized\n(n={len(specialized_studies)})']

# Crear heatmap
sns.heatmap(heatmap_data, annot=True, fmt='.1f', cmap='RdYlGn',
            cbar_kws={'label': 'Average Maturity (%)'},
            xticklabels=workflow_stages,
            yticklabels=feeding_types,
            linewidths=1, linecolor='black',
            vmin=0, vmax=100, center=50,
            ax=ax1, annot_kws={'fontsize': 11, 'fontweight': 'bold'})

ax1.set_title('Figure 3.3.4: Integration Maturity Heatmap by Feeding Type\n' +
              'Percentage of studies achieving high-maturity in each workflow stage',
              fontsize=12, fontweight='bold', pad=20)

ax1.set_xlabel('Workflow Integration Stage', fontsize=11, fontweight='bold')
ax1.set_ylabel('Feeding Architecture Type', fontsize=11, fontweight='bold')

# Rotar etiquetas
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=0, ha='center')
ax1.set_yticklabels(ax1.get_yticklabels(), rotation=0, ha='right')

# Añadir anotaciones para valores críticos
for i, feeding_type in enumerate(feeding_types):
    for j, stage in enumerate(workflow_stages):
        value = heatmap_data[i, j]
        if value < 20 and j >= 2:  # Baja madurez en etapas avanzadas
            ax1.add_patch(plt.Rectangle((j, i), 1, 1, fill=False,
                                        edgecolor='red', lw=3))

# --- GRÁFICO DE BARRAS COMPLEMENTARIO ---
# Mostrar distribución de scores individuales

# Consolidar scores por grupo
group_scores = {
    'Single-Feed': [sum(scores) for scores in single_feed_studies.values()],
    'Coaxial/Probe': [sum(scores) for scores in coaxial_probe_studies.values()],
    'Complex': [sum(scores) for scores in complex_network_studies.values()],
    'Specialized': [sum(scores) for scores in specialized_studies.values()]
}

# Crear violin plot
positions = []
data_violin = []
colors_violin = ['#4CAF50', '#2196F3', '#FF9800', '#E91E63']

for i, (group_name, scores) in enumerate(group_scores.items()):
    positions.extend([i] * len(scores))
    data_violin.extend(scores)

# Crear DataFrame para violin plot
df_violin = pd.DataFrame({
    'Feeding Type': [list(group_scores.keys())[int(p)] for p in positions],
    'Integration Score': data_violin
})

import matplotlib.patches as mpatches
parts = ax2.violinplot([group_scores[g] for g in group_scores.keys()],
                        positions=range(len(group_scores)),
                        widths=0.7, showmeans=True, showmedians=True)

# Colorear violines
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors_violin[i])
    pc.set_alpha(0.7)

# Añadir scatter de puntos individuales
for i, (group_name, scores) in enumerate(group_scores.items()):
    y = scores
    x = np.random.normal(i, 0.04, size=len(y))  # Jitter
    ax2.scatter(x, y, alpha=0.6, s=50, color=colors_violin[i],
                edgecolors='black', linewidth=1)

ax2.set_xticks(range(len(group_scores)))
ax2.set_xticklabels([k.replace('-', '-\n') for k in group_scores.keys()],
                     fontsize=9, rotation=0)
ax2.set_ylabel('Total Integration Score (max=5)', fontsize=10, fontweight='bold')
ax2.set_title('Distribution of Individual\nStudy Integration Scores',
              fontsize=11, fontweight='bold', pad=15)
ax2.grid(axis='y', alpha=0.3)
ax2.set_ylim(-0.5, 5.5)

# Líneas de referencia
ax2.axhline(y=2.5, color='red', linestyle='--', linewidth=1.5,
            alpha=0.5, label='50% maturity')
ax2.axhline(y=4, color='green', linestyle=':', linewidth=1.5,
            alpha=0.5, label='80% maturity')
ax2.legend(fontsize=8, loc='lower right')

# --- ESTADÍSTICAS EN TEXTO ---
stats_text = "KEY FINDINGS:\n\n"
stats_text += f"• Single-Feed: {len([s for s in group_scores['Single-Feed'] if s >= 4])}/{len(group_scores['Single-Feed'])} studies ≥4/5\n"
stats_text += f"• Coaxial/Probe: {len([s for s in group_scores['Coaxial/Probe'] if s >= 4])}/{len(group_scores['Coaxial/Probe'])} studies ≥4/5\n"
stats_text += f"• Complex: {len([s for s in group_scores['Complex'] if s >= 4])}/{len(group_scores['Complex'])} studies ≥4/5\n"
stats_text += f"• Specialized: {len([s for s in group_scores['Specialized'] if s >= 4])}/{len(group_scores['Specialized'])} studies ≥4/5\n\n"

total_studies = sum(len(scores) for scores in group_scores.values())
complete_integration = sum(1 for scores_list in group_scores.values() for s in scores_list if s == 5)
stats_text += f"Complete Integration (5/5): {complete_integration}/{total_studies} ({complete_integration/total_studies*100:.1f}%)\n"

median_score = np.median([s for scores_list in group_scores.values() for s in scores_list])
stats_text += f"Median Integration Score: {median_score:.1f}/5"

ax2.text(0.02, 0.98, stats_text, transform=ax2.transAxes,
         fontsize=8, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# --- NOTA DE TRAZABILIDAD ---
fig.text(0.5, 0.01,
         'Data source: analisisOE3.txt Groups A-D | Individual study scoring matrix:\n' +
         f'Single-Feed n={len(single_feed_studies)}, Coaxial/Probe n={len(coaxial_probe_studies)}, ' +
         f'Complex n={len(complex_network_studies)}, Specialized n={len(specialized_studies)} | ' +
         f'Total studies analyzed: {total_studies}',
         ha='center', va='bottom', fontsize=7, style='italic',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig('G:/RevSisOrd/OE3Figuras/Figure_3_3_4_Integration_Heatmap.png', dpi=300, bbox_inches='tight')
plt.savefig('G:/RevSisOrd/OE3Figuras/Figure_3_3_4_Integration_Heatmap.pdf', bbox_inches='tight')

print("[OK] Figura 3.3.4 generada exitosamente")
print(f"[OK] Trazabilidad: {total_studies} estudios con scoring individual")
print(f"[OK] Matriz: 4 feeding types x 5 workflow stages")
print(f"[OK] Complete integration: {complete_integration} estudios (Islam 2015, Kibria 2018, Curreli 2021)")
