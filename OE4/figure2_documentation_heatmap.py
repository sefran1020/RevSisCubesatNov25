"""
FIGURE 2: Manufacturing Documentation Completeness Heatmap
Objective Specific 4 - CubeSat Antenna Systematic Review
Exposes systematic gaps in fabrication process documentation
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set publication-quality parameters
plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.titlesize'] = 12

# Load data
grupoA = pd.read_csv('grupoA.csv', encoding='utf-8')
grupoB = pd.read_csv('grupoB.csv', encoding='utf-8')
grupoC = pd.read_csv('grupoC.csv', encoding='utf-8')

grupoA['group'] = 'A-PCB'
grupoB['group'] = 'B-ADV'
grupoC['group'] = 'C-CE'

df = pd.concat([grupoA, grupoB, grupoC], ignore_index=True)

# Define documentation dimensions
dimensions = [
    'Fabrication Method Detail',
    'Material Specifications',
    'Tolerance Analysis',
    'Thermal Validation',
    'Mechanical Testing',
    'Cost Analysis',
    'Scalability Assessment',
    'Failure Mode Documentation'
]

# Create matrix (14 studies × 8 dimensions)
doc_matrix = []
study_labels = []

for idx, row in df.iterrows():
    author = str(row['gen.metadata.authors']).split(';')[0].strip()
    year = str(row['gen.metadata.year'])
    group = row['group']

    study_label = f"{author}-{year} [{group}]"
    study_labels.append(study_label)

    scores = []

    # 1. Fabrication Method Detail
    fab_material = str(row['esp.technical_specifications.fabrication_material'])
    if fab_material != 'Not mentioned' and fab_material != 'nan' and len(fab_material) > 10:
        scores.append(100)
    elif fab_material != 'Not mentioned' and fab_material != 'nan':
        scores.append(50)
    else:
        scores.append(0)

    # 2. Material Specifications
    substrate_mat = str(row['esp.technical_specifications.substrate_material'])
    substrate_perm = str(row['esp.technical_specifications.substrate_permittivity'])
    substrate_loss = str(row['esp.technical_specifications.substrate_loss_tangent'])
    substrate_thick = str(row['esp.technical_specifications.substrate_thickness'])

    mat_score = 0
    if substrate_mat not in ['Not mentioned', 'nan']:
        mat_score += 25
    if substrate_perm not in ['Not mentioned', 'nan']:
        mat_score += 25
    if substrate_loss not in ['Not mentioned', 'nan']:
        mat_score += 25
    if substrate_thick not in ['Not mentioned', 'nan']:
        mat_score += 25
    scores.append(mat_score)

    # 3. Tolerance Analysis
    limitations = str(row['gen.limitations'])
    main_findings = str(row['gen.detailed_results.main_findings'])

    if 'tolerance' in limitations.lower() or 'tolerance' in main_findings.lower():
        if 'Manufacturing tolerances' in limitations or 'fabrication tolerances' in limitations:
            scores.append(100)  # Explicitly documented
        else:
            scores.append(50)  # Mentioned but not detailed
    else:
        scores.append(0)

    # 4. Thermal Validation
    instruments = str(row['gen.detailed_methodology.data_collection_instruments'])
    main_findings_thermal = str(row['gen.detailed_results.main_findings'])

    thermal_score = 0
    if 'TVAC' in instruments or 'thermal vacuum' in instruments.lower():
        thermal_score = 100
    elif 'thermal' in instruments.lower() or 'temperature' in main_findings_thermal.lower():
        thermal_score = 50
    scores.append(thermal_score)

    # 5. Mechanical Testing
    if 'vibration' in instruments.lower() or 'mechanical' in instruments.lower():
        scores.append(100)
    elif 'deployment' in main_findings.lower():
        scores.append(50)
    else:
        scores.append(0)

    # 6. Cost Analysis
    recommendations_practice = str(row['gen.recommendations.for_practice'])
    if 'cost' in recommendations_practice.lower():
        if any(char.isdigit() for char in recommendations_practice):
            scores.append(100)  # Quantitative cost data
        else:
            scores.append(50)  # Cost mentioned qualitatively
    else:
        scores.append(0)

    # 7. Scalability Assessment
    if 'mass production' in recommendations_practice.lower() or 'scalability' in recommendations_practice.lower():
        scores.append(100)
    elif 'batch' in recommendations_practice.lower() or 'manufacturing' in recommendations_practice.lower():
        scores.append(50)
    else:
        scores.append(0)

    # 8. Failure Mode Documentation
    if 'failure' in limitations.lower():
        scores.append(100)
    elif any(word in limitations.lower() for word in ['degradation', 'shift', 'sensitivity']):
        scores.append(50)
    else:
        scores.append(0)

    doc_matrix.append(scores)

# Convert to DataFrame
doc_df = pd.DataFrame(doc_matrix, columns=dimensions, index=study_labels)

# Create heatmap
fig, ax = plt.subplots(figsize=(16, 10))

# Custom colormap: Red (0) -> Yellow (50) -> Green (100)
cmap = sns.diverging_palette(10, 130, s=80, l=55, as_cmap=True)

# Plot heatmap
sns.heatmap(doc_df, annot=True, fmt='.0f', cmap=cmap, center=50,
            cbar_kws={'label': 'Documentation Completeness (%)'},
            linewidths=0.5, linecolor='gray',
            vmin=0, vmax=100, ax=ax)

# Formatting
ax.set_xlabel('Documentation Dimensions', fontsize=12, fontweight='bold')
ax.set_ylabel('Study [Group]', fontsize=12, fontweight='bold')
ax.set_title('Figure 2. Manufacturing Documentation Completeness Heatmap\n' +
             'Systematic assessment of fabrication process documentation across 14 studies\n' +
             '(Green=Complete, Yellow=Partial, Red=Absent)',
             fontsize=13, fontweight='bold', pad=20)

# Rotate labels
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.tight_layout()
plt.savefig('Figure2_DocumentationHeatmap.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure2_DocumentationHeatmap.pdf', bbox_inches='tight')

# Calculate and print statistics
print("\nFigure 2 - Documentation Gap Statistics")
print("="*80)
print(f"\nOverall Documentation Completeness: {doc_df.values.mean():.1f}%")
print("\nBy Dimension:")
for dim in dimensions:
    mean_score = doc_df[dim].mean()
    complete = (doc_df[dim] == 100).sum()
    partial = (doc_df[dim] == 50).sum()
    absent = (doc_df[dim] == 0).sum()
    print(f"  {dim}:")
    print(f"    Mean: {mean_score:.1f}% | Complete: {complete}/14 | Partial: {partial}/14 | Absent: {absent}/14")

print("\nBy Group:")
for group in ['A-PCB', 'B-ADV', 'C-CE']:
    group_studies = [s for s in study_labels if group in s]
    group_data = doc_df.loc[group_studies]
    print(f"  {group}: {group_data.values.mean():.1f}%")

# Identify critical gaps (>70% deficiency)
print("\nCritical Gaps (>70% deficiency):")
for dim in dimensions:
    deficiency = (doc_df[dim] < 30).sum() / len(doc_df) * 100
    if deficiency > 70:
        print(f"  {dim}: {deficiency:.1f}% of studies lack adequate documentation")

print("\n" + "="*80)
print("Figure saved as: Figure2_DocumentationHeatmap.png and Figure2_DocumentationHeatmap.pdf")
