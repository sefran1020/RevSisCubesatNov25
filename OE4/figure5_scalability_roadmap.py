"""
FIGURE 5: Fabrication Scalability Roadmap
Objective Specific 4 - CubeSat Antenna Systematic Review
Temporal evolution from technology demonstration to mass production readiness
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches

# Set publication-quality parameters
plt.rcParams['figure.figsize'] = (18, 10)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9

# Load data
grupoA = pd.read_csv('grupoA.csv', encoding='utf-8')
grupoB = pd.read_csv('grupoB.csv', encoding='utf-8')
grupoC = pd.read_csv('grupoC.csv', encoding='utf-8')

grupoA['group'] = 'PCB'
grupoB['group'] = 'ADV'
grupoC['group'] = 'CE'

df = pd.concat([grupoA, grupoB, grupoC], ignore_index=True)

# Sort by year
df['year_int'] = pd.to_numeric(df['gen.metadata.year'], errors='coerce')
df = df.sort_values('year_int')

# Define phases based on years
phases = {
    'Phase 1: Technology Demonstration (2015-2020)': (2015, 2020),
    'Phase 2: Advanced Techniques Integration (2021-2023)': (2021, 2023),
    'Phase 3: Scalable Manufacturing (2024-2025)': (2024, 2025),
    'Phase 4: Mass Production Readiness (2026+)': (2026, 2030)
}

# Create figure
fig, ax = plt.subplots(figsize=(18, 10))

# Define timeline
timeline_y = 8
phase_height = 1.5
study_box_height = 0.6

# Draw phase boxes
phase_colors = ['#7209B7', '#2E86AB', '#06A77D', '#F18F01']
phase_y_positions = [6, 4, 2, 0]

for (phase_name, (start_year, end_year)), color, y_pos in zip(phases.items(), phase_colors, phase_y_positions):
    # Calculate x positions (normalize to 2015-2030 range)
    x_start = (start_year - 2015) / 15 * 16
    x_width = (end_year - start_year) / 15 * 16

    # Draw phase box
    phase_box = FancyBboxPatch((x_start, y_pos), x_width, phase_height,
                               boxstyle="round,pad=0.1",
                               facecolor=color, edgecolor='black',
                               linewidth=2, alpha=0.3)
    ax.add_patch(phase_box)

    # Add phase label
    ax.text(x_start + x_width/2, y_pos + phase_height + 0.2,
            phase_name.split(':')[0], fontsize=11, ha='center',
            fontweight='bold')

# Classify studies into phases
phase_studies = {
    'Phase 1: Technology Demonstration (2015-2020)': [],
    'Phase 2: Advanced Techniques Integration (2021-2023)': [],
    'Phase 3: Scalable Manufacturing (2024-2025)': [],
}

for idx, row in df.iterrows():
    year = row['year_int']
    if pd.isna(year):
        continue

    author = str(row['gen.metadata.authors']).split(';')[0].strip()
    year_str = str(int(year))
    group = row['group']

    study_info = {
        'author': author,
        'year': year_str,
        'group': group,
        'title': str(row['gen.metadata.title'])[:60],
        'fab_method': str(row['esp.technical_specifications.fabrication_material'])[:40],
        'key_achievement': '',
        'limitations': str(row['gen.limitations'])[:100]
    }

    # Extract key achievement
    main_findings = str(row['gen.detailed_results.main_findings'])
    if 'dual-band' in main_findings.lower():
        study_info['key_achievement'] = 'Dual-band operation'
    elif '3D' in study_info['fab_method']:
        study_info['key_achievement'] = '3D metal printing'
    elif 'AMC' in main_findings:
        study_info['key_achievement'] = 'AMC integration'
    elif 'stacked' in main_findings.lower():
        study_info['key_achievement'] = 'Stacked substrates'
    elif 'compact' in main_findings.lower():
        study_info['key_achievement'] = 'Miniaturization'
    else:
        study_info['key_achievement'] = 'Performance optimization'

    # Assign to phase
    if 2015 <= year <= 2020:
        phase_studies['Phase 1: Technology Demonstration (2015-2020)'].append(study_info)
    elif 2021 <= year <= 2023:
        phase_studies['Phase 2: Advanced Techniques Integration (2021-2023)'].append(study_info)
    elif 2024 <= year <= 2025:
        phase_studies['Phase 3: Scalable Manufacturing (2024-2025)'].append(study_info)

# Plot studies in each phase
group_colors = {'PCB': '#2E86AB', 'ADV': '#A23B72', 'CE': '#06A77D'}

for phase_idx, (phase_name, studies) in enumerate(phase_studies.items()):
    y_base = phase_y_positions[phase_idx] + 0.2

    for study_idx, study in enumerate(studies):
        # Calculate x position based on year
        year_num = int(study['year'])
        x_pos = (year_num - 2015) / 15 * 16 + 0.2

        # Draw study box
        study_box = FancyBboxPatch((x_pos, y_base + study_idx * (study_box_height + 0.1)),
                                   2, study_box_height,
                                   boxstyle="round,pad=0.05",
                                   facecolor=group_colors[study['group']],
                                   edgecolor='black', linewidth=1.5, alpha=0.7)
        ax.add_patch(study_box)

        # Add study text
        study_text = f"{study['author']} ({study['year']})\n{study['key_achievement']}"
        ax.text(x_pos + 1, y_base + study_idx * (study_box_height + 0.1) + study_box_height/2,
                study_text, fontsize=8, ha='center', va='center',
                color='white', fontweight='bold')

# Add milestones
milestones = [
    {
        'phase': 0,
        'y': phase_y_positions[0] - 0.3,
        'text': 'Milestone 1: Proof-of-concept antennas\nwith basic PCB fabrication',
        'gap': 'Gap: No scalability documentation,\nno cost analysis'
    },
    {
        'phase': 1,
        'y': phase_y_positions[1] - 0.3,
        'text': 'Milestone 2: Multiphysics-validated designs\nemerge, thermal validation <20%',
        'gap': 'Gap: 71% feeding-to-system\nintegration gap persists'
    },
    {
        'phase': 2,
        'y': phase_y_positions[2] - 0.3,
        'text': 'Milestone 3: Advanced technologies\ndemonstrate performance superiority',
        'gap': 'Current Gap: Limited performance data\nfor cost-effective approaches'
    },
]

for milestone in milestones:
    phase_idx = milestone['phase']
    y_pos = milestone['y']

    # Milestone marker
    ax.plot([0, 16], [y_pos, y_pos], 'k--', linewidth=1, alpha=0.5)

    # Milestone text
    ax.text(0.2, y_pos - 0.1, milestone['text'], fontsize=9,
            ha='left', va='top', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))

    # Gap text
    ax.text(16 - 0.2, y_pos - 0.1, milestone['gap'], fontsize=9,
            ha='right', va='top', style='italic', color='red',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFA07A', alpha=0.3))

# Add Phase 4 requirements (projected)
phase4_y = phase_y_positions[3] + 0.3
requirements = [
    '✓ Documented manufacturing process parameters',
    '✓ Quantitative cost-benefit analysis',
    '✓ Thermal-mechanical validation integration (currently 86% deficiency)',
    '✓ Scalability assessment with batch production quality data'
]

for req_idx, req in enumerate(requirements):
    ax.text(0.5, phase4_y + phase_height - 0.2 - req_idx * 0.25,
            req, fontsize=9, ha='left', va='top',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

# Add decision points
decision_points = [
    {'x': 5, 'y': 7.5, 'text': 'DP1: PCB vs Advanced Tech\nselection based on\nmission requirements'},
    {'x': 9, 'y': 5.5, 'text': 'DP2: Thermal qualification\nlevel based on\norbital regime'},
    {'x': 13, 'y': 3.5, 'text': 'DP3: Mass production pathway:\nMultilayer vs 3D printing'},
]

for dp in decision_points:
    # Diamond marker
    diamond = mpatches.FancyBboxPatch((dp['x'] - 0.3, dp['y'] - 0.3), 0.6, 0.6,
                                      boxstyle="round,pad=0.1",
                                      facecolor='#FFD700', edgecolor='black',
                                      linewidth=2)
    ax.add_patch(diamond)
    ax.text(dp['x'], dp['y'], 'DP', fontsize=8, ha='center', va='center',
            fontweight='bold')

    # Decision text
    ax.text(dp['x'] + 0.5, dp['y'], dp['text'], fontsize=8, ha='left', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFD700', alpha=0.4))

# Add arrows connecting phases
for i in range(len(phase_y_positions) - 1):
    arrow = FancyArrowPatch((8, phase_y_positions[i] - 0.5),
                            (8, phase_y_positions[i+1] + phase_height + 0.5),
                            arrowstyle='->', mutation_scale=30,
                            linewidth=3, color='black', alpha=0.5)
    ax.add_arrow(arrow)

# Add year labels on timeline
for year in range(2015, 2031, 5):
    x_pos = (year - 2015) / 15 * 16
    ax.text(x_pos, timeline_y + 0.3, str(year), fontsize=10,
            ha='center', fontweight='bold')
    ax.plot([x_pos, x_pos], [timeline_y, timeline_y + 0.2], 'k-', linewidth=2)

# Timeline
ax.plot([0, 16], [timeline_y, timeline_y], 'k-', linewidth=3)

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#2E86AB', edgecolor='black', label='PCB Prototyping'),
    mpatches.Patch(facecolor='#A23B72', edgecolor='black', label='Advanced Technologies'),
    mpatches.Patch(facecolor='#06A77D', edgecolor='black', label='Cost-Effective')
]
ax.legend(handles=legend_elements, loc='upper right', ncol=3,
          frameon=True, fancybox=True, shadow=True, fontsize=10)

# Formatting
ax.set_xlim(-0.5, 17)
ax.set_ylim(-0.5, 9)
ax.axis('off')

ax.set_title('Figure 5. Fabrication Scalability Roadmap\n' +
             'Temporal evolution of CubeSat antenna fabrication from technology demonstration to mass production readiness\n' +
             'DP=Decision Point; Yellow boxes=milestones; Red boxes=critical gaps',
             fontsize=13, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('Figure5_ScalabilityRoadmap.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure5_ScalabilityRoadmap.pdf', bbox_inches='tight')

# Print roadmap statistics
print("\nFigure 5 - Scalability Roadmap Statistics")
print("="*80)
for phase_name, studies in phase_studies.items():
    print(f"\n{phase_name} (n={len(studies)}):")
    for study in studies:
        print(f"  - {study['author']} ({study['year']}): {study['key_achievement']}")

print("\n" + "="*80)
print("Figure saved as: Figure5_ScalabilityRoadmap.png and Figure5_ScalabilityRoadmap.pdf")
