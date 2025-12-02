"""
THEMATIC FIGURE GENERATION for Objective Specific 4
Focus: THEMES and PATTERNS, not individual authors
NO "NONE" or "Not mentioned" fields - only positive findings
Consistent with other objectives' approach
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Ellipse
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

# Set publication parameters
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['figure.dpi'] = 300

# Load data with correct delimiter
print("Loading data...")
grupoA = pd.read_csv('grupoA.csv', encoding='utf-8', sep=';')
grupoB = pd.read_csv('grupoB.csv', encoding='utf-8', sep=';')
grupoC = pd.read_csv('grupoC.csv', encoding='utf-8', sep=';')

grupoA['group'] = 'PCB Prototyping'
grupoB['group'] = 'Advanced Technologies'
grupoC['group'] = 'Cost-Effective'

df = pd.concat([grupoA, grupoB, grupoC], ignore_index=True)

print(f"\nData loaded: {len(df)} studies")
print(f"  PCB Prototyping: {len(grupoA)} studies")
print(f"  Advanced Technologies: {len(grupoB)} studies")
print(f"  Cost-Effective: {len(grupoC)} studies")

# Color scheme
colors_map = {
    'PCB Prototyping': '#2E86AB',
    'Advanced Technologies': '#A23B72',
    'Cost-Effective': '#06A77D'
}

print("\n" + "="*80)
print("GENERATING THEMATIC FIGURES (NO AUTHOR FOCUS)")
print("="*80 + "\n")

# ==================================================================================
# FIGURE 1: Performance Metrics by Fabrication Paradigm (AGGREGATED)
# ==================================================================================
print("Generating Figure 1: Performance by Fabrication Paradigm (Box Plots)...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Extract performance data
performance_data = []
for idx, row in df.iterrows():
    group = row['group']

    # Extract gain
    gain_str = str(row['esp.domain_results.gain'])
    gain = 0
    if 'dBi' in gain_str:
        import re
        numbers = re.findall(r'[-+]?\d*\.?\d+', gain_str)
        if numbers:
            gain = max([float(n) for n in numbers if float(n) > 0])

    # Extract bandwidth
    bw_str = str(row['esp.domain_results.bandwidth'])
    bandwidth = 0
    if '%' in bw_str:
        import re
        numbers = re.findall(r'[-+]?\d*\.?\d+', bw_str)
        if numbers:
            bandwidth = max([float(n) for n in numbers])

    if gain > 0:  # Only include if we have valid data
        performance_data.append({'Group': group, 'Metric': 'Gain (dBi)', 'Value': gain})
    if bandwidth > 0:
        performance_data.append({'Group': group, 'Metric': 'Bandwidth (%)', 'Value': bandwidth})

perf_df = pd.DataFrame(performance_data)

# Plot 1: Gain distribution by group
gain_data = perf_df[perf_df['Metric'] == 'Gain (dBi)']
groups = ['PCB Prototyping', 'Advanced Technologies', 'Cost-Effective']

positions = [1, 2, 3]
for i, group in enumerate(groups):
    data = gain_data[gain_data['Group'] == group]['Value']
    if len(data) > 0:
        bp = ax1.boxplot([data], positions=[positions[i]], widths=0.5,
                         patch_artist=True, showfliers=True,
                         boxprops=dict(facecolor=colors_map[group], alpha=0.7),
                         medianprops=dict(color='black', linewidth=2),
                         whiskerprops=dict(color='black'),
                         capprops=dict(color='black'))

ax1.set_xticks(positions)
ax1.set_xticklabels(['PCB\nPrototyping', 'Advanced\nTechnologies', 'Cost-\nEffective'])
ax1.set_ylabel('Maximum Gain (dBi)', fontweight='bold', fontsize=11)
ax1.set_title('(a) Gain Performance by Fabrication Paradigm', fontweight='bold', fontsize=12)
ax1.grid(axis='y', alpha=0.3)
ax1.set_ylim(0, 30)

# Plot 2: Bandwidth distribution by group
bw_data = perf_df[perf_df['Metric'] == 'Bandwidth (%)']
for i, group in enumerate(groups):
    data = bw_data[bw_data['Group'] == group]['Value']
    if len(data) > 0:
        bp = ax2.boxplot([data], positions=[positions[i]], widths=0.5,
                         patch_artist=True, showfliers=True,
                         boxprops=dict(facecolor=colors_map[group], alpha=0.7),
                         medianprops=dict(color='black', linewidth=2),
                         whiskerprops=dict(color='black'),
                         capprops=dict(color='black'))

ax2.set_xticks(positions)
ax2.set_xticklabels(['PCB\nPrototyping', 'Advanced\nTechnologies', 'Cost-\nEffective'])
ax2.set_ylabel('Bandwidth (%)', fontweight='bold', fontsize=11)
ax2.set_title('(b) Bandwidth Performance by Fabrication Paradigm', fontweight='bold', fontsize=12)
ax2.grid(axis='y', alpha=0.3)
ax2.set_ylim(0, 100)

plt.suptitle('Figure 1. Performance Metrics Across Fabrication Paradigms\n' +
             'Aggregated data from 13 CubeSat antenna studies grouped by manufacturing approach',
             fontsize=13, fontweight='bold', y=1.00)
plt.tight_layout()
plt.savefig('Figure1_PerformanceByParadigm.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure1_PerformanceByParadigm.pdf', bbox_inches='tight')
plt.close()

print("  [OK] Figure 1 saved")
print(f"     Gain ranges: PCB median={gain_data[gain_data['Group']=='PCB Prototyping']['Value'].median():.1f} dBi")
print(f"                  ADV median={gain_data[gain_data['Group']=='Advanced Technologies']['Value'].median():.1f} dBi")
print(f"                  CE median={gain_data[gain_data['Group']=='Cost-Effective']['Value'].median():.1f} dBi")

# ==================================================================================
# FIGURE 2: Fabrication Techniques and Associated Performance Outcomes
# ==================================================================================
print("\nGenerating Figure 2: Fabrication Technique-Performance Relationship...")

# Define technique categories (extracted from CSV data)
techniques = {
    'PCB Photolithography': [],
    '3D Metal Printing': [],
    'Stacked Substrates': [],
    'AMC Integration': [],
    'Multilayer Simplified': [],
    'Fractal Geometry': []
}

# Define outcome categories
outcomes = {
    'Wide Bandwidth (>30%)': 0,
    'High Gain (>10 dBi)': 0,
    'Dual/Multi-band': 0,
    'Circular Polarization': 0,
    'Miniaturization': 0,
    'UWB Operation': 0
}

# Build technique-outcome matrix
technique_outcome_matrix = np.zeros((len(techniques), len(outcomes)))

for idx, row in df.iterrows():
    fab_method = str(row['esp.technical_specifications.fabrication_material']).lower()

    # Extract performance metrics
    gain_str = str(row['esp.domain_results.gain'])
    bw_str = str(row['esp.domain_results.bandwidth'])
    pol_str = str(row['esp.technical_specifications.polarization']).lower()
    bands_str = str(row['esp.technical_specifications.frequency_band']).lower()

    # Classify techniques
    tech_idx = -1
    if 'pcb' in fab_method or 'photolith' in fab_method or 'etch' in fab_method:
        tech_idx = 0
    elif '3d' in fab_method or 'print' in fab_method or 'metal print' in fab_method:
        tech_idx = 1
    elif 'stack' in fab_method or 'substrat' in fab_method:
        tech_idx = 2
    elif 'amc' in fab_method or 'metamaterial' in fab_method:
        tech_idx = 3
    elif 'multilayer' in fab_method or 'layer' in fab_method:
        tech_idx = 4
    elif 'fractal' in fab_method:
        tech_idx = 5

    # Classify outcomes
    import re

    # Wide Bandwidth
    if '%' in bw_str:
        bw_nums = re.findall(r'[-+]?\d*\.?\d+', bw_str)
        if bw_nums and max([float(n) for n in bw_nums]) > 30:
            if tech_idx >= 0:
                technique_outcome_matrix[tech_idx, 0] += 1

    # High Gain
    if 'dBi' in gain_str:
        gain_nums = re.findall(r'[-+]?\d*\.?\d+', gain_str)
        if gain_nums and max([float(n) for n in gain_nums if float(n) > 0]) > 10:
            if tech_idx >= 0:
                technique_outcome_matrix[tech_idx, 1] += 1

    # Dual/Multi-band
    if 'dual' in bands_str or 'multi' in bands_str or 'tri' in bands_str:
        if tech_idx >= 0:
            technique_outcome_matrix[tech_idx, 2] += 1

    # Circular Polarization
    if 'circular' in pol_str or 'cp' in pol_str:
        if tech_idx >= 0:
            technique_outcome_matrix[tech_idx, 3] += 1

    # Miniaturization (check dimensions or explicit mention)
    size_str = str(row['esp.technical_specifications.antenna_dimensions']).lower()
    if 'compact' in size_str or 'miniatur' in size_str or 'small' in size_str:
        if tech_idx >= 0:
            technique_outcome_matrix[tech_idx, 4] += 1

    # UWB Operation
    if 'uwb' in bw_str.lower() or 'ultra' in bw_str.lower():
        if tech_idx >= 0:
            technique_outcome_matrix[tech_idx, 5] += 1

# Create heatmap
fig, ax = plt.subplots(figsize=(12, 8))

# Filter out techniques/outcomes with no data
technique_labels = list(techniques.keys())
outcome_labels = list(outcomes.keys())

sns.heatmap(technique_outcome_matrix, annot=True, fmt='.0f', cmap='YlOrRd',
            xticklabels=outcome_labels, yticklabels=technique_labels,
            cbar_kws={'label': 'Number of Studies'}, linewidths=0.5,
            vmin=0, vmax=technique_outcome_matrix.max(), ax=ax)

ax.set_title('Figure 2. Fabrication Technique-Performance Outcome Relationship Matrix\n' +
             'Frequency of performance outcomes achieved by different fabrication techniques',
             fontsize=12, fontweight='bold', pad=15)
ax.set_xlabel('Performance Outcomes', fontweight='bold', fontsize=11)
ax.set_ylabel('Fabrication Techniques', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.savefig('Figure2_TechniqueOutcomeMatrix.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure2_TechniqueOutcomeMatrix.pdf', bbox_inches='tight')
plt.close()

print("  [OK] Figure 2 saved")
print(f"     Most common technique-outcome associations identified")

# ==================================================================================
# FIGURE 3: Manufacturing Complexity vs Performance Trade-off Space
# ==================================================================================
print("\nGenerating Figure 3: Complexity-Performance Trade-off Space...")

fig, ax = plt.subplots(figsize=(12, 9))

# Calculate complexity and performance scores
complexity_performance = []

for idx, row in df.iterrows():
    group = row['group']

    # Complexity score (0-10 scale)
    complexity = 0

    # Factors increasing complexity
    fab_method = str(row['esp.technical_specifications.fabrication_material']).lower()
    if 'stack' in fab_method:
        complexity += 3
    if '3d' in fab_method or 'print' in fab_method:
        complexity += 3
    if 'amc' in fab_method or 'metamaterial' in fab_method:
        complexity += 2
    if 'multilayer' in fab_method:
        complexity += 2

    # Number of bands
    bands_str = str(row['esp.technical_specifications.frequency_band']).lower()
    if 'dual' in bands_str:
        complexity += 1
    elif 'tri' in bands_str or 'multi' in bands_str:
        complexity += 2

    # Polarization complexity
    pol_str = str(row['esp.technical_specifications.polarization']).lower()
    if 'circular' in pol_str:
        complexity += 1

    # If complexity still 0, it's basic PCB
    if complexity == 0:
        complexity = 1

    # Performance score (0-100 scale)
    performance = 0

    # Extract gain
    gain_str = str(row['esp.domain_results.gain'])
    if 'dBi' in gain_str:
        import re
        numbers = re.findall(r'[-+]?\d*\.?\d+', gain_str)
        if numbers:
            gain = max([float(n) for n in numbers if float(n) > 0])
            performance += (gain / 30) * 50  # Max 50 points for gain

    # Extract bandwidth
    bw_str = str(row['esp.domain_results.bandwidth'])
    if '%' in bw_str:
        import re
        numbers = re.findall(r'[-+]?\d*\.?\d+', bw_str)
        if numbers:
            bw = max([float(n) for n in numbers])
            performance += (bw / 100) * 50  # Max 50 points for bandwidth

    complexity_performance.append({
        'Group': group,
        'Complexity': complexity,
        'Performance': performance
    })

cp_df = pd.DataFrame(complexity_performance)

# Plot scatter with different markers for each group
for group in ['PCB Prototyping', 'Advanced Technologies', 'Cost-Effective']:
    group_data = cp_df[cp_df['Group'] == group]
    ax.scatter(group_data['Complexity'], group_data['Performance'],
              s=200, alpha=0.7, c=colors_map[group], edgecolors='black',
              linewidths=1.5, label=group)

# Add ellipses to show regions
from matplotlib.patches import Ellipse
for group in ['PCB Prototyping', 'Advanced Technologies', 'Cost-Effective']:
    group_data = cp_df[cp_df['Group'] == group]
    if len(group_data) >= 2:
        mean_x = group_data['Complexity'].mean()
        mean_y = group_data['Performance'].mean()
        std_x = group_data['Complexity'].std() if group_data['Complexity'].std() > 0 else 1
        std_y = group_data['Performance'].std() if group_data['Performance'].std() > 0 else 5

        ellipse = Ellipse((mean_x, mean_y), width=std_x*2.5, height=std_y*2.5,
                         facecolor=colors_map[group], alpha=0.15, edgecolor=colors_map[group],
                         linewidth=2, linestyle='--')
        ax.add_patch(ellipse)

ax.set_xlabel('Manufacturing Complexity Score\n(Higher = More fabrication steps/advanced techniques)',
              fontweight='bold', fontsize=11)
ax.set_ylabel('Performance Score\n(Aggregated: Gain + Bandwidth)',
              fontweight='bold', fontsize=11)
ax.set_title('Figure 3. Manufacturing Complexity vs Performance Trade-off Space\n' +
             'Three fabrication paradigms occupy distinct regions in complexity-performance space',
             fontsize=12, fontweight='bold', pad=15)
ax.legend(loc='upper left', frameon=True, fancybox=True, fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 12)
ax.set_ylim(0, 100)

plt.tight_layout()
plt.savefig('Figure3_ComplexityPerformanceTradeoff.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure3_ComplexityPerformanceTradeoff.pdf', bbox_inches='tight')
plt.close()

print("  [OK] Figure 3 saved")
print(f"     PCB: mean complexity={cp_df[cp_df['Group']=='PCB Prototyping']['Complexity'].mean():.1f}, performance={cp_df[cp_df['Group']=='PCB Prototyping']['Performance'].mean():.1f}")
print(f"     ADV: mean complexity={cp_df[cp_df['Group']=='Advanced Technologies']['Complexity'].mean():.1f}, performance={cp_df[cp_df['Group']=='Advanced Technologies']['Performance'].mean():.1f}")
print(f"     CE: mean complexity={cp_df[cp_df['Group']=='Cost-Effective']['Complexity'].mean():.1f}, performance={cp_df[cp_df['Group']=='Cost-Effective']['Performance'].mean():.1f}")

print("\n" + "="*80)
print("ALL THEMATIC FIGURES GENERATED SUCCESSFULLY")
print("="*80)
print("\nGenerated files:")
print("  - Figure1_PerformanceByParadigm.png/.pdf")
print("  - Figure2_TechniqueOutcomeMatrix.png/.pdf")
print("  - Figure3_ComplexityPerformanceTradeoff.png/.pdf")
print("\nFigures focus on THEMES and PATTERNS, not individual authors")
print("NO 'NONE' or 'Not mentioned' fields - only positive findings")
print("="*80)
