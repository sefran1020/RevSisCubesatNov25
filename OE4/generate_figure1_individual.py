"""
CORRECTED FIGURE 1: Individual Study Data Points (n=13)
Statistical justification: With n=13 (groups of 6, 4, 3), box plots are inappropriate.
Solution: Show each study individually, labeled by technical characteristic.
NO author names - only technical features (Option 3)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Set publication parameters
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['figure.dpi'] = 300

print("="*80)
print("GENERATING INDIVIDUAL DATA FIGURE (n=13 studies)")
print("Statistical justification: n too small for box plots")
print("="*80 + "\n")

# Manual data extraction with technical characteristic labels
# Based on review of CSV files - labeled by CHARACTERISTIC not AUTHOR

studies_data = [
    # PCB Prototyping (n=6) - Blue
    {'label': 'Dual-band L/S CP', 'gain': 2.0, 'bandwidth': 0, 'group': 'PCB Prototyping', 'paradigm_code': 'PCB'},
    {'label': 'Dual-band MWR/GPS LHCP', 'gain': 10.1, 'bandwidth': 0, 'group': 'PCB Prototyping', 'paradigm_code': 'PCB'},
    {'label': 'Fractal Tri-band', 'gain': 5.7, 'bandwidth': 0, 'group': 'PCB Prototyping', 'paradigm_code': 'PCB'},
    {'label': 'S-band Parasitic CP', 'gain': 7.5, 'bandwidth': 0, 'group': 'PCB Prototyping', 'paradigm_code': 'PCB'},
    {'label': 'Dual-band S/X Shared-Aperture', 'gain': 12.8, 'bandwidth': 1.5, 'group': 'PCB Prototyping', 'paradigm_code': 'PCB'},
    {'label': 'S-band Compact CP', 'gain': 5.8, 'bandwidth': 2.0, 'group': 'PCB Prototyping', 'paradigm_code': 'PCB'},

    # Advanced Technologies (n=4) - Purple
    {'label': '3D-Printed Dual-band L/S', 'gain': 2.32, 'bandwidth': 0, 'group': 'Advanced Technologies', 'paradigm_code': 'ADV'},
    {'label': 'UWB Stacked Spiral', 'gain': 12.0, 'bandwidth': 96.0, 'group': 'Advanced Technologies', 'paradigm_code': 'ADV'},  # UWB approximation
    {'label': 'Ka-band PSO Array', 'gain': 26.0, 'bandwidth': 0, 'group': 'Advanced Technologies', 'paradigm_code': 'ADV'},
    {'label': 'AMC Broadband CP', 'gain': 10.22, 'bandwidth': 42.42, 'group': 'Advanced Technologies', 'paradigm_code': 'ADV'},

    # Cost-Effective (n=3) - Green
    {'label': 'UWB Aperture-Coupled', 'gain': 10.3, 'bandwidth': 50.0, 'group': 'Cost-Effective', 'paradigm_code': 'CE'},
    {'label': 'Reconfigurable S-band', 'gain': 7.7, 'bandwidth': 6.9, 'group': 'Cost-Effective', 'paradigm_code': 'CE'},
    {'label': 'Tri-band Omnidirectional', 'gain': 5.2, 'bandwidth': 0, 'group': 'Cost-Effective', 'paradigm_code': 'CE'},
]

df = pd.DataFrame(studies_data)

print(f"Loaded {len(df)} individual studies")
print(f"  PCB Prototyping: {len(df[df['paradigm_code']=='PCB'])} studies")
print(f"  Advanced Technologies: {len(df[df['paradigm_code']=='ADV'])} studies")
print(f"  Cost-Effective: {len(df[df['paradigm_code']=='CE'])} studies")

# Color scheme
colors_map = {
    'PCB Prototyping': '#2E86AB',
    'Advanced Technologies': '#A23B72',
    'Cost-Effective': '#06A77D'
}

# ==================================================================================
# FIGURE 1: Individual Study Performance (Horizontal Bar Charts)
# ==================================================================================
print("\nGenerating Figure 1: Individual Study Performance...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9))

# Sort by group and gain for visual clarity
df_sorted = df.sort_values(['paradigm_code', 'gain'], ascending=[True, False])

# Create y-positions with group spacing
y_positions = []
current_y = 0
prev_group = None
for idx, row in df_sorted.iterrows():
    if prev_group and row['paradigm_code'] != prev_group:
        current_y += 0.5  # Add spacing between groups
    y_positions.append(current_y)
    current_y += 1
    prev_group = row['paradigm_code']

df_sorted['y_pos'] = y_positions

# Panel (a): Gain
for idx, row in df_sorted.iterrows():
    color = colors_map[row['group']]
    ax1.barh(row['y_pos'], row['gain'], height=0.7,
             color=color, alpha=0.8, edgecolor='black', linewidth=1)

ax1.set_yticks(df_sorted['y_pos'])
ax1.set_yticklabels(df_sorted['label'], fontsize=9)
ax1.set_xlabel('Maximum Gain (dBi)', fontweight='bold', fontsize=11)
ax1.set_title('(a) Gain Performance by Study', fontweight='bold', fontsize=12)
ax1.grid(axis='x', alpha=0.3)
ax1.set_xlim(0, 28)
ax1.invert_yaxis()

# Add group labels
group_positions = {
    'PCB': df_sorted[df_sorted['paradigm_code']=='PCB']['y_pos'].mean(),
    'ADV': df_sorted[df_sorted['paradigm_code']=='ADV']['y_pos'].mean(),
    'CE': df_sorted[df_sorted['paradigm_code']=='CE']['y_pos'].mean()
}

for code, y_pos in group_positions.items():
    if code == 'PCB':
        label = 'PCB\nPrototyping'
        color = colors_map['PCB Prototyping']
    elif code == 'ADV':
        label = 'Advanced\nTechnologies'
        color = colors_map['Advanced Technologies']
    else:
        label = 'Cost-\nEffective'
        color = colors_map['Cost-Effective']

    ax1.text(-1.5, y_pos, label, fontsize=9, fontweight='bold',
             ha='right', va='center', color=color)

# Panel (b): Bandwidth (only studies with bandwidth data)
df_with_bw = df_sorted[df_sorted['bandwidth'] > 0]

for idx, row in df_with_bw.iterrows():
    color = colors_map[row['group']]
    ax2.barh(row['y_pos'], row['bandwidth'], height=0.7,
             color=color, alpha=0.8, edgecolor='black', linewidth=1)

ax2.set_yticks(df_sorted['y_pos'])
ax2.set_yticklabels(df_sorted['label'], fontsize=9)
ax2.set_xlabel('Bandwidth (%)', fontweight='bold', fontsize=11)
ax2.set_title('(b) Bandwidth Performance by Study\n(Studies with explicit bandwidth data)',
              fontweight='bold', fontsize=12)
ax2.grid(axis='x', alpha=0.3)
ax2.set_xlim(0, 100)
ax2.invert_yaxis()

# Add group labels
for code, y_pos in group_positions.items():
    if code == 'PCB':
        label = 'PCB\nPrototyping'
        color = colors_map['PCB Prototyping']
    elif code == 'ADV':
        label = 'Advanced\nTechnologies'
        color = colors_map['Advanced Technologies']
    else:
        label = 'Cost-\nEffective'
        color = colors_map['Cost-Effective']

    ax2.text(-5, y_pos, label, fontsize=9, fontweight='bold',
             ha='right', va='center', color=color)

# Add note about missing bandwidth data
ax2.text(0.98, 0.02, f'Note: {len(df)-len(df_with_bw)} studies lack explicit\nbandwidth percentage data',
         transform=ax2.transAxes, fontsize=8, ha='right', va='bottom',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.suptitle('Figure 1. Performance Metrics Across 13 Individual CubeSat Antenna Studies\n' +
             'Each bar represents one study, labeled by technical characteristic (not author)',
             fontsize=13, fontweight='bold', y=0.98)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('Figure1_IndividualStudies_FINAL.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure1_IndividualStudies_FINAL.pdf', bbox_inches='tight')
plt.close()

print("  [OK] Figure 1 saved as Figure1_IndividualStudies_FINAL.png/.pdf")

# Print statistics
print("\n" + "="*80)
print("PERFORMANCE STATISTICS BY PARADIGM (AGGREGATED FROM INDIVIDUAL DATA)")
print("="*80)

for group_name in ['PCB Prototyping', 'Advanced Technologies', 'Cost-Effective']:
    group_data = df[df['group'] == group_name]
    print(f"\n{group_name} (n={len(group_data)}):")

    gain_values = group_data['gain']
    print(f"  Gain (dBi):")
    print(f"    Median: {gain_values.median():.1f}")
    print(f"    Range: {gain_values.min():.1f} - {gain_values.max():.1f}")
    print(f"    Mean: {gain_values.mean():.1f}")

    bw_values = group_data[group_data['bandwidth'] > 0]['bandwidth']
    if len(bw_values) > 0:
        print(f"  Bandwidth (%):")
        print(f"    Median: {bw_values.median():.1f}")
        print(f"    Range: {bw_values.min():.1f} - {bw_values.max():.1f}")
        print(f"    Mean: {bw_values.mean():.1f}")
        print(f"    n={len(bw_values)} studies with explicit BW data")
    else:
        print(f"  Bandwidth: No explicit percentage data")

print("\n" + "="*80)
print("STATISTICAL JUSTIFICATION")
print("="*80)
print(f"""
Sample sizes per paradigm:
  PCB Prototyping: n=6
  Advanced Technologies: n=4
  Cost-Effective: n=3

Box plot requirements: Typically n≥10-15 per group for meaningful distribution
Our approach: Individual data points with paradigm grouping

Justification: With n=13 total (and n=3-6 per group), showing individual
studies preserves data transparency while enabling paradigm comparison.
This approach is statistically appropriate for small-n systematic reviews.
""")

print("="*80)
print("FIGURE GENERATION COMPLETE")
print("="*80)
print("\nGenerated files:")
print("  - Figure1_IndividualStudies_FINAL.png (300 dpi)")
print("  - Figure1_IndividualStudies_FINAL.pdf (vector)")
print("\nApproach: Individual data presentation (statistically appropriate for n=13)")
print("Labeling: Technical characteristics (NOT author names)")
print("Grouping: Visual paradigm segregation (PCB/Advanced/Cost-Effective)")
print("="*80)
