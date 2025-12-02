"""
FIGURE 4: Thermal-Mechanical Validation Gap Analysis
Objective Specific 4 - CubeSat Antenna Systematic Review
Sankey diagram showing workflow progression and validation gaps
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.sankey import Sankey

# Set publication-quality parameters
plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10

# Load data
grupoA = pd.read_csv('grupoA.csv', encoding='utf-8')
grupoB = pd.read_csv('grupoB.csv', encoding='utf-8')
grupoC = pd.read_csv('grupoC.csv', encoding='utf-8')

df = pd.concat([grupoA, grupoB, grupoC], ignore_index=True)

# Analyze validation levels
total_studies = len(df)

# Level 1: Total Studies
level1_total = total_studies

# Level 2: EM Simulation (universal according to Table 3)
level2_em_sim = total_studies  # 100% have EM simulation

# Level 3: Fabrication & Testing
level3_fabricated = 0
for idx, row in df.iterrows():
    instruments = str(row['gen.detailed_methodology.data_collection_instruments'])
    if 'Fabricated' in instruments or 'prototype' in instruments.lower() or 'anechoic' in instruments.lower():
        level3_fabricated += 1

# Level 4: Environmental Testing (Thermal + Mechanical)
level4_complete_validation = []
level4_partial_validation = []
level4_no_validation = []

for idx, row in df.iterrows():
    author = str(row['gen.metadata.authors']).split(';')[0].strip()
    year = str(row['gen.metadata.year'])
    instruments = str(row['gen.detailed_methodology.data_collection_instruments'])
    main_findings = str(row['gen.detailed_results.main_findings'])
    limitations = str(row['gen.limitations'])

    # Check thermal validation
    has_thermal = False
    if 'TVAC' in instruments or 'thermal vacuum' in instruments.lower():
        has_thermal = True
    elif 'Thermal cycling' in main_findings or 'thermal' in main_findings.lower():
        has_thermal = True

    # Check mechanical validation
    has_mechanical = False
    if 'vibration' in instruments.lower() or 'mechanical' in instruments.lower():
        has_mechanical = True
    elif 'Mechanical deformation' in main_findings or 'deployment' in main_findings.lower():
        has_mechanical = True

    if has_thermal and has_mechanical:
        level4_complete_validation.append(f"{author} ({year})")
    elif has_thermal or has_mechanical:
        level4_partial_validation.append(f"{author} ({year})")
    else:
        level4_no_validation.append(f"{author} ({year})")

n_complete = len(level4_complete_validation)
n_partial = len(level4_partial_validation)
n_none = len(level4_no_validation)

# Level 5: Mission-Ready Status
level5_flight_qualified = n_complete
level5_lab_only = n_partial + n_none

# Create figure with custom Sankey-style visualization
fig, ax = plt.subplots(figsize=(16, 10))

# Define flow stages and positions
stages = [
    'Total Studies',
    'EM Simulation',
    'Fabrication & Testing',
    'Environmental Testing',
    'Mission-Ready Status'
]

stage_positions = [0, 2, 4, 6, 8]

# Define flows (from left to right)
flows = [
    # Stage 1 → 2
    {'from': 0, 'to': 1, 'value': level2_em_sim, 'color': '#2E86AB', 'label': f'{level2_em_sim} (100%)'},

    # Stage 2 → 3
    {'from': 1, 'to': 2, 'value': level3_fabricated, 'color': '#2E86AB', 'label': f'{level3_fabricated} ({level3_fabricated/total_studies*100:.0f}%)'},

    # Stage 3 → 4 (splits into three paths)
    {'from': 2, 'to': 3, 'value': n_complete, 'color': '#06A77D', 'label': f'Complete: {n_complete} ({n_complete/total_studies*100:.0f}%)', 'offset': 1},
    {'from': 2, 'to': 3, 'value': n_partial, 'color': '#F18F01', 'label': f'Partial: {n_partial} ({n_partial/total_studies*100:.0f}%)', 'offset': 0},
    {'from': 2, 'to': 3, 'value': n_none, 'color': '#A23B72', 'label': f'None: {n_none} ({n_none/total_studies*100:.0f}%)', 'offset': -1},

    # Stage 4 → 5 (convergence)
    {'from': 3, 'to': 4, 'value': level5_flight_qualified, 'color': '#06A77D', 'label': f'Flight-qualified: {level5_flight_qualified} ({level5_flight_qualified/total_studies*100:.0f}%)', 'offset': 0.5},
    {'from': 3, 'to': 4, 'value': level5_lab_only, 'color': '#A23B72', 'label': f'Lab-only: {level5_lab_only} ({level5_lab_only/total_studies*100:.0f}%)', 'offset': -0.5},
]

# Draw stage boxes
box_height = 2
box_width = 0.8
colors_stages = ['#7209B7', '#2E86AB', '#06A77D', '#F18F01', '#A23B72']

for i, (stage, x_pos) in enumerate(zip(stages, stage_positions)):
    # Draw box
    rect = plt.Rectangle((x_pos - box_width/2, -box_height/2),
                          box_width, box_height,
                          facecolor=colors_stages[i], edgecolor='black',
                          linewidth=2, alpha=0.7)
    ax.add_patch(rect)

    # Add text
    ax.text(x_pos, 0, stage, fontsize=11, ha='center', va='center',
            fontweight='bold', color='white', wrap=True)

    # Add count below
    if i == 0:
        count_text = f"n={total_studies}"
    elif i == 1:
        count_text = f"n={level2_em_sim}"
    elif i == 2:
        count_text = f"n={level3_fabricated}"
    elif i == 3:
        count_text = f"C:{n_complete} P:{n_partial} N:{n_none}"
    else:
        count_text = f"F:{level5_flight_qualified} L:{level5_lab_only}"

    ax.text(x_pos, -box_height/2 - 0.5, count_text, fontsize=9,
            ha='center', va='top', style='italic')

# Draw flows as gradient polygons
def draw_flow(ax, x1, x2, y1_start, y1_end, y2_start, y2_end, color, alpha=0.5):
    """Draw a gradient flow between two stages"""
    vertices = [
        (x1, y1_start),
        (x1, y1_end),
        (x2, y2_end),
        (x2, y2_start)
    ]
    from matplotlib.patches import Polygon
    poly = Polygon(vertices, facecolor=color, edgecolor=color,
                   alpha=alpha, linewidth=0.5)
    ax.add_patch(poly)

# Calculate flow positions
# Stage 0 → 1
y_offset = 0
draw_flow(ax, stage_positions[0] + box_width/2, stage_positions[1] - box_width/2,
          y_offset - 0.8, y_offset + 0.8,
          y_offset - 0.8, y_offset + 0.8,
          '#2E86AB', alpha=0.6)

# Stage 1 → 2
draw_flow(ax, stage_positions[1] + box_width/2, stage_positions[2] - box_width/2,
          y_offset - 0.8, y_offset + 0.8,
          y_offset - 0.8, y_offset + 0.8,
          '#2E86AB', alpha=0.6)

# Stage 2 → 3 (three paths)
flow_height = 1.6 / total_studies  # Normalize to total box height

# Complete validation path (top)
y_complete_start = 0.8 - (n_none + n_partial) * flow_height / 2
y_complete_end = y_complete_start - n_complete * flow_height
draw_flow(ax, stage_positions[2] + box_width/2, stage_positions[3] - box_width/2,
          y_complete_start, y_complete_end,
          0.8, 0.8 - n_complete * flow_height,
          '#06A77D', alpha=0.6)

# Partial validation path (middle)
y_partial_start = y_complete_end
y_partial_end = y_partial_start - n_partial * flow_height
draw_flow(ax, stage_positions[2] + box_width/2, stage_positions[3] - box_width/2,
          y_partial_start, y_partial_end,
          0.8 - n_complete * flow_height, 0.8 - (n_complete + n_partial) * flow_height,
          '#F18F01', alpha=0.6)

# No validation path (bottom)
y_none_start = y_partial_end
y_none_end = y_none_start - n_none * flow_height
draw_flow(ax, stage_positions[2] + box_width/2, stage_positions[3] - box_width/2,
          y_none_start, y_none_end,
          -0.8, -0.8 + n_none * flow_height,
          '#A23B72', alpha=0.6)

# Stage 3 → 4 (convergence)
# Flight-qualified (from complete)
draw_flow(ax, stage_positions[3] + box_width/2, stage_positions[4] - box_width/2,
          0.8, 0.8 - n_complete * flow_height,
          0.4, 0.4 - level5_flight_qualified * flow_height,
          '#06A77D', alpha=0.6)

# Lab-only (from partial and none)
draw_flow(ax, stage_positions[3] + box_width/2, stage_positions[4] - box_width/2,
          0.8 - n_complete * flow_height, -0.8 + n_none * flow_height,
          -0.4, -0.4 - level5_lab_only * flow_height,
          '#A23B72', alpha=0.6)

# Add annotations for critical findings
annotation_y = -3

# Annotation 1: Curreli-2021
ax.annotate('Curreli et al. (2021): "Proton radiation (5-year LEO equivalent)\n' +
            'induced <0.3 dB degradation for Rogers RT/duroid 5880\n' +
            'but 2.1 dB loss for FR4"',
            xy=(stage_positions[3], 0.8), xytext=(stage_positions[3] + 0.5, annotation_y),
            arrowprops=dict(arrowstyle='->', lw=1.5, color='#06A77D'),
            fontsize=8, ha='left', va='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#06A77D', alpha=0.2))

# Annotation 2: Munoz-Martin-2023
ax.annotate('Munoz-Martin et al. (2023): "TVAC testing: two thermal cycles\n' +
            'between +80°C and -20°C revealed manufacturing tolerance\n' +
            'and dielectric constant variation impacts"',
            xy=(stage_positions[3], 0.5), xytext=(stage_positions[3] + 0.5, annotation_y - 1.5),
            arrowprops=dict(arrowstyle='->', lw=1.5, color='#06A77D'),
            fontsize=8, ha='left', va='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#06A77D', alpha=0.2))

# Annotation 3: Critical gap
ax.annotate('CRITICAL GAP: 86% deficiency in thermal-mechanical validation\n' +
            f'{n_none} studies ({n_none/total_studies*100:.0f}%) with NO environmental testing',
            xy=(stage_positions[3], -0.8), xytext=(stage_positions[3] + 0.5, annotation_y - 3),
            arrowprops=dict(arrowstyle='->', lw=2, color='#A23B72'),
            fontsize=9, ha='left', va='top', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#A23B72', alpha=0.3))

# Formatting
ax.set_xlim(-1, 10)
ax.set_ylim(-6, 3)
ax.axis('off')

ax.set_title('Figure 4. Thermal-Mechanical Validation Gap Analysis\n' +
             'Workflow progression from electromagnetic simulation to mission-ready status (n=14 studies)\n' +
             'Green=complete validation, Orange=partial, Purple=absent',
             fontsize=13, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('Figure4_ValidationGapSankey.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure4_ValidationGapSankey.pdf', bbox_inches='tight')

# Print statistics
print("\nFigure 4 - Validation Gap Statistics")
print("="*80)
print(f"Total Studies: {total_studies}")
print(f"\nValidation Level Distribution:")
print(f"  Complete (Thermal + Mechanical): {n_complete} ({n_complete/total_studies*100:.1f}%)")
print(f"  Partial (Thermal OR Mechanical): {n_partial} ({n_partial/total_studies*100:.1f}%)")
print(f"  None: {n_none} ({n_none/total_studies*100:.1f}%)")
print(f"\nMission-Ready Status:")
print(f"  Flight-qualified: {level5_flight_qualified} ({level5_flight_qualified/total_studies*100:.1f}%)")
print(f"  Lab-characterized only: {level5_lab_only} ({level5_lab_only/total_studies*100:.1f}%)")
print(f"\nStudies with Complete Validation:")
for study in level4_complete_validation:
    print(f"  - {study}")
print(f"\nStudies with Partial Validation:")
for study in level4_partial_validation:
    print(f"  - {study}")
print(f"\nStudies with NO Environmental Validation:")
for study in level4_no_validation:
    print(f"  - {study}")

print("\n" + "="*80)
print("Figure saved as: Figure4_ValidationGapSankey.png and Figure4_ValidationGapSankey.pdf")
