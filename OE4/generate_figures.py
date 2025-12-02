"""
CORRECTED: Figure Generation for Objective Specific 4
Based on actual CSV structure: 13 studies total (6+4+3), delimiter=';'
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import FancyBboxPatch
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

print(f"\nData loaded successfully:")
print(f"  Grupo A (PCB Prototyping): {len(grupoA)} studies")
print(f"  Grupo B (Advanced Technologies): {len(grupoB)} studies")
print(f"  Grupo C (Cost-Effective): {len(grupoC)} studies")
print(f"  TOTAL: {len(df)} studies")
print(f"\nPercentages:")
print(f"  PCB: {len(grupoA)/len(df)*100:.1f}%")
print(f"  ADV: {len(grupoB)/len(df)*100:.1f}%")
print(f"  CE: {len(grupoC)/len(df)*100:.1f}%")

# Extract basic information for all studies
print("\n" + "="*80)
print("STUDY INFORMATION")
print("="*80)
for idx, row in df.iterrows():
    author = str(row['gen.metadata.authors']).split(';')[0].strip()
    year = str(row['gen.metadata.year'])
    group = row['group']
    print(f"{idx+1}. {author} ({year}) - {group}")

print("\n" + "="*80)
print("GENERATING FIGURES...")
print("="*80 + "\n")

# ==================================================================================
# FIGURE 1: Simple Performance Comparison Bar Chart
# ==================================================================================
print("Generating Figure 1: Performance Comparison by Group...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Extract performance data
performance_data = []
for idx, row in df.iterrows():
    author = str(row['gen.metadata.authors']).split(';')[0].strip()
    year = str(row['gen.metadata.year'])
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

    performance_data.append({
        'Study': f"{author} ({year})",
        'Group': group,
        'Gain_dBi': gain,
        'Bandwidth_%': bandwidth
    })

perf_df = pd.DataFrame(performance_data)

# Plot 1: Gain comparison
colors_map = {
    'PCB Prototyping': '#2E86AB',
    'Advanced Technologies': '#A23B72',
    'Cost-Effective': '#06A77D'
}

for group in ['PCB Prototyping', 'Advanced Technologies', 'Cost-Effective']:
    group_data = perf_df[perf_df['Group'] == group]
    ax1.barh(group_data['Study'], group_data['Gain_dBi'],
             color=colors_map[group], alpha=0.7, edgecolor='black')

ax1.set_xlabel('Maximum Gain (dBi)', fontweight='bold')
ax1.set_title('(a) Gain Performance by Study', fontweight='bold')
ax1.grid(axis='x', alpha=0.3)

# Plot 2: Bandwidth comparison
for group in ['PCB Prototyping', 'Advanced Technologies', 'Cost-Effective']:
    group_data = perf_df[perf_df['Group'] == group]
    ax2.barh(group_data['Study'], group_data['Bandwidth_%'],
             color=colors_map[group], alpha=0.7, edgecolor='black', label=group)

ax2.set_xlabel('Bandwidth (%)', fontweight='bold')
ax2.set_title('(b) Bandwidth Performance by Study', fontweight='bold')
ax2.grid(axis='x', alpha=0.3)
ax2.legend(loc='lower right', frameon=True, fancybox=True)

plt.suptitle('Figure 1. Performance Metrics Across 13 CubeSat Antenna Studies\n' +
             'Grouped by fabrication configuration (n=6 PCB, n=4 ADV, n=3 CE)',
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('Figure1_PerformanceComparison.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure1_PerformanceComparison.pdf', bbox_inches='tight')
plt.close()

print("  [OK] Figure 1 saved")

# ==================================================================================
# FIGURE 2: Documentation Completeness Heatmap
# ==================================================================================
print("Generating Figure 2: Documentation Completeness Heatmap...")

# Define dimensions
dimensions = [
    'Fabrication\nMethod',
    'Material\nSpecs',
    'Tolerance\nAnalysis',
    'Thermal\nValidation',
    'Mechanical\nTesting',
    'Cost\nAnalysis',
    'Scalability',
    'Failure\nModes'
]

doc_matrix = []
study_labels = []

for idx, row in df.iterrows():
    author = str(row['gen.metadata.authors']).split(';')[0].strip()
    year = str(row['gen.metadata.year'])
    group_abbr = {'PCB Prototyping': 'PCB', 'Advanced Technologies': 'ADV', 'Cost-Effective': 'CE'}[row['group']]

    study_labels.append(f"{author}-{year}\n[{group_abbr}]")
    scores = []

    # 1. Fabrication Method
    fab = str(row['esp.technical_specifications.fabrication_material'])
    scores.append(100 if fab not in ['Not mentioned', 'nan', 'NaN', ''] and len(fab) > 10 else 0)

    # 2. Material Specs
    mat_count = sum([1 for x in [
        row['esp.technical_specifications.substrate_material'],
        row['esp.technical_specifications.substrate_permittivity'],
        row['esp.technical_specifications.substrate_loss_tangent'],
        row['esp.technical_specifications.substrate_thickness']
    ] if str(x) not in ['Not mentioned', 'nan', 'NaN', '']])
    scores.append(mat_count * 25)

    # 3. Tolerance Analysis
    limitations = str(row['gen.limitations'])
    if 'tolerance' in limitations.lower():
        scores.append(100 if 'Manufacturing tolerances' in limitations else 50)
    else:
        scores.append(0)

    # 4. Thermal Validation
    instruments = str(row['gen.detailed_methodology.data_collection_instruments'])
    if 'TVAC' in instruments or 'thermal vacuum' in instruments.lower():
        scores.append(100)
    elif 'thermal' in instruments.lower():
        scores.append(50)
    else:
        scores.append(0)

    # 5. Mechanical Testing
    if 'vibration' in instruments.lower() or 'mechanical' in instruments.lower():
        scores.append(100)
    else:
        scores.append(0)

    # 6. Cost Analysis
    rec_practice = str(row['gen.recommendations.for_practice'])
    if 'cost' in rec_practice.lower():
        scores.append(50)
    else:
        scores.append(0)

    # 7. Scalability
    if 'mass production' in rec_practice.lower() or 'scalab' in rec_practice.lower():
        scores.append(100)
    elif 'manufacturing' in rec_practice.lower():
        scores.append(50)
    else:
        scores.append(0)

    # 8. Failure Modes
    if 'failure' in limitations.lower():
        scores.append(100)
    elif any(w in limitations.lower() for w in ['degradation', 'shift', 'sensitivity']):
        scores.append(50)
    else:
        scores.append(0)

    doc_matrix.append(scores)

doc_df = pd.DataFrame(doc_matrix, columns=dimensions, index=study_labels)

# Create heatmap
fig, ax = plt.subplots(figsize=(14, 10))
sns.heatmap(doc_df, annot=True, fmt='.0f', cmap='RdYlGn', center=50,
            cbar_kws={'label': 'Completeness (%)'}, linewidths=0.5,
            vmin=0, vmax=100, ax=ax)

ax.set_title('Figure 2. Manufacturing Documentation Completeness Heatmap\n' +
             'Assessment across 13 studies and 8 critical dimensions\n' +
             '(Green=Complete [100%], Yellow=Partial [50%], Red=Absent [0%])',
             fontsize=12, fontweight='bold', pad=15)
ax.set_xlabel('Documentation Dimensions', fontweight='bold')
ax.set_ylabel('Study [Group]', fontweight='bold')

plt.tight_layout()
plt.savefig('Figure2_DocumentationHeatmap.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure2_DocumentationHeatmap.pdf', bbox_inches='tight')
plt.close()

print(f"  [OK] Figure 2 saved")
print(f"     Overall documentation: {doc_df.values.mean():.1f}%")
print(f"     Thermal validation: {doc_df[dimensions[3]].mean():.1f}%")
print(f"     Cost analysis: {doc_df[dimensions[5]].mean():.1f}%")

# ==================================================================================
# FIGURE 3: Validation Level Stacked Bar Chart
# ==================================================================================
print("Generating Figure 3: Validation Level Distribution...")

validation_levels = []
for idx, row in df.iterrows():
    author = str(row['gen.metadata.authors']).split(';')[0].strip()
    instruments = str(row['gen.detailed_methodology.data_collection_instruments'])

    has_thermal = 'TVAC' in instruments or 'thermal' in instruments.lower()
    has_mechanical = 'vibration' in instruments or 'mechanical' in instruments.lower()

    if has_thermal and has_mechanical:
        level = 'Complete\n(Thermal+Mech)'
    elif has_thermal or has_mechanical:
        level = 'Partial\n(Either)'
    else:
        level = 'None'

    validation_levels.append({'Study': author, 'Level': level, 'Group': row['group']})

val_df = pd.DataFrame(validation_levels)

# Count by level
level_counts = val_df['Level'].value_counts()
total = len(val_df)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Pie chart
colors = ['#06A77D', '#F18F01', '#A23B72']
labels_with_pct = [f"{level}\nn={level_counts.get(level, 0)} ({level_counts.get(level, 0)/total*100:.0f}%)"
                   for level in ['Complete\n(Thermal+Mech)', 'Partial\n(Either)', 'None']]

ax1.pie([level_counts.get(l, 0) for l in ['Complete\n(Thermal+Mech)', 'Partial\n(Either)', 'None']],
        labels=labels_with_pct, colors=colors, autopct='', startangle=90,
        wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
ax1.set_title('(a) Validation Level Distribution', fontweight='bold')

# Plot 2: Bar chart by group
group_val_counts = val_df.groupby(['Group', 'Level']).size().unstack(fill_value=0)
group_val_counts.plot(kind='bar', stacked=True, ax=ax2, color=colors, edgecolor='black')
ax2.set_xlabel('Fabrication Configuration', fontweight='bold')
ax2.set_ylabel('Number of Studies', fontweight='bold')
ax2.set_title('(b) Validation by Group', fontweight='bold')
ax2.legend(title='Validation Level', frameon=True, fancybox=True)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')

plt.suptitle(f'Figure 3. Environmental Validation Gap Analysis (n={total} studies)\n' +
             f'Critical finding: {level_counts.get("None", 0)}/{total} ({level_counts.get("None", 0)/total*100:.0f}%) ' +
             'with NO thermal-mechanical testing',
             fontsize=12, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('Figure3_ValidationGap.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure3_ValidationGap.pdf', bbox_inches='tight')
plt.close()

print(f"  [OK] Figure 3 saved")
complete_count = level_counts.get('Complete\n(Thermal+Mech)', 0)
print(f"     Complete validation: {complete_count}/{total} ({complete_count/total*100:.0f}%)")

print("\n" + "="*80)
print("ALL FIGURES GENERATED SUCCESSFULLY")
print("="*80)
print("\nGenerated files:")
print("  - Figure1_PerformanceComparison.png/.pdf")
print("  - Figure2_DocumentationHeatmap.png/.pdf")
print("  - Figure3_ValidationGap.png/.pdf")
print("\nFigures ready for integration with Section 3.4 (978 words)")
print("="*80)
