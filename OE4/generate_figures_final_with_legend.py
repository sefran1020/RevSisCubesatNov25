"""
FINAL FIGURES for OE4 - Individual Studies with Legend
Figure 1: Individual performance data (n=13)
Figure 2: Fabrication workflow configuration summary
Both with legends to avoid text overlap on axes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

# Set publication parameters
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['figure.dpi'] = 300

print("="*80)
print("GENERATING FINAL FIGURES WITH LEGENDS (n=13 studies)")
print("="*80 + "\n")

# Manual data with technical characteristic labels
studies_data = [
    # PCB Prototyping (n=6)
    {'code': 'P1', 'label': 'Dual-band L/S CP', 'gain': 2.0, 'bandwidth': 0, 'group': 'PCB Prototyping'},
    {'code': 'P2', 'label': 'Dual-band MWR/GPS LHCP', 'gain': 10.1, 'bandwidth': 0, 'group': 'PCB Prototyping'},
    {'code': 'P3', 'label': 'Fractal Tri-band', 'gain': 5.7, 'bandwidth': 0, 'group': 'PCB Prototyping'},
    {'code': 'P4', 'label': 'S-band Parasitic CP', 'gain': 7.5, 'bandwidth': 49.0, 'group': 'PCB Prototyping'},
    {'code': 'P5', 'label': 'Dual-band S/X Shared-Aperture', 'gain': 12.8, 'bandwidth': 1.5, 'group': 'PCB Prototyping'},
    {'code': 'P6', 'label': 'S-band Compact CP', 'gain': 5.8, 'bandwidth': 2.0, 'group': 'PCB Prototyping'},

    # Advanced Technologies (n=4)
    {'code': 'A1', 'label': '3D-Printed Dual-band L/S', 'gain': 2.32, 'bandwidth': 0, 'group': 'Advanced Technologies'},
    {'code': 'A2', 'label': 'UWB Stacked Spiral', 'gain': 12.0, 'bandwidth': 96.0, 'group': 'Advanced Technologies'},
    {'code': 'A3', 'label': 'Ka-band PSO Array', 'gain': 26.0, 'bandwidth': 0, 'group': 'Advanced Technologies'},
    {'code': 'A4', 'label': 'AMC Broadband CP', 'gain': 10.22, 'bandwidth': 42.42, 'group': 'Advanced Technologies'},

    # Cost-Effective (n=3)
    {'code': 'C1', 'label': 'UWB Aperture-Coupled', 'gain': 10.3, 'bandwidth': 50.0, 'group': 'Cost-Effective'},
    {'code': 'C2', 'label': 'Reconfigurable S-band', 'gain': 7.7, 'bandwidth': 6.9, 'group': 'Cost-Effective'},
    {'code': 'C3', 'label': 'Tri-band Omnidirectional', 'gain': 5.2, 'bandwidth': 0, 'group': 'Cost-Effective'},
]

df = pd.DataFrame(studies_data)

# Color scheme
colors_map = {
    'PCB Prototyping': '#2E86AB',
    'Advanced Technologies': '#A23B72',
    'Cost-Effective': '#06A77D'
}

# ==================================================================================
# FIGURE 1: Individual Study Performance with Legend
# ==================================================================================
print("Generating Figure 1: Individual Performance with Legend...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Sort by group and gain
df_sorted = df.sort_values(['group', 'gain'], ascending=[True, False])

# Panel (a): Gain - Use codes on Y-axis, legend for descriptions
y_positions = list(range(len(df_sorted)))
df_sorted['y_pos'] = y_positions

for idx, row in df_sorted.iterrows():
    color = colors_map[row['group']]
    ax1.barh(row['y_pos'], row['gain'], height=0.7,
             color=color, alpha=0.8, edgecolor='black', linewidth=1)

ax1.set_yticks(df_sorted['y_pos'])
ax1.set_yticklabels(df_sorted['code'], fontsize=10)  # Use codes instead of full labels
ax1.set_xlabel('Maximum Gain (dBi)', fontweight='bold', fontsize=11)
ax1.set_ylabel('Study Code', fontweight='bold', fontsize=11)
ax1.set_title('(a) Gain Performance', fontweight='bold', fontsize=12)
ax1.grid(axis='x', alpha=0.3)
ax1.set_xlim(0, 28)
ax1.invert_yaxis()

# Panel (b): Bandwidth
df_with_bw = df_sorted[df_sorted['bandwidth'] > 0]

for idx, row in df_with_bw.iterrows():
    color = colors_map[row['group']]
    ax2.barh(row['y_pos'], row['bandwidth'], height=0.7,
             color=color, alpha=0.8, edgecolor='black', linewidth=1)

ax2.set_yticks(df_sorted['y_pos'])
ax2.set_yticklabels(df_sorted['code'], fontsize=10)
ax2.set_xlabel('Bandwidth (%)', fontweight='bold', fontsize=11)
ax2.set_ylabel('Study Code', fontweight='bold', fontsize=11)
ax2.set_title('(b) Bandwidth Performance', fontweight='bold', fontsize=12)
ax2.grid(axis='x', alpha=0.3)
ax2.set_xlim(0, 100)
ax2.invert_yaxis()

# Add note
ax2.text(0.98, 0.02, f'{len(df)-len(df_with_bw)} studies lack explicit bandwidth data',
         transform=ax2.transAxes, fontsize=8, ha='right', va='bottom',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

# Create legend patches
pcb_patch = mpatches.Patch(color=colors_map['PCB Prototyping'], label='PCB Prototyping (n=6)', alpha=0.8)
adv_patch = mpatches.Patch(color=colors_map['Advanced Technologies'], label='Advanced Technologies (n=4)', alpha=0.8)
ce_patch = mpatches.Patch(color=colors_map['Cost-Effective'], label='Cost-Effective (n=3)', alpha=0.8)

fig.legend(handles=[pcb_patch, adv_patch, ce_patch], loc='lower center',
           ncol=3, frameon=True, fontsize=10, bbox_to_anchor=(0.5, -0.05))

plt.suptitle('Figure 1. Individual Performance Metrics Across 13 CubeSat Antenna Studies\n' +
             'Grouped by fabrication paradigm (see legend below; code-to-study mapping in caption)',
             fontsize=13, fontweight='bold', y=0.98)

plt.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.savefig('Figure1_Individual_WithLegend.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure1_Individual_WithLegend.pdf', bbox_inches='tight')
plt.close()

print("  [OK] Figure 1 saved")

# ==================================================================================
# FIGURE 2: Fabrication Workflow Configuration Summary
# ==================================================================================
print("\nGenerating Figure 2: Workflow Configuration Summary...")

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# Panel (a): Study distribution by paradigm
paradigm_counts = df.groupby('group').size()
colors = [colors_map[p] for p in paradigm_counts.index]

wedges, texts, autotexts = ax1.pie(paradigm_counts.values, labels=None, autopct='%1.1f%%',
                                     colors=colors, startangle=90,
                                     wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
ax1.set_title('(a) Distribution by Paradigm\n(n=13 studies)', fontweight='bold', fontsize=11)

# Make percentage text bold
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

# Panel (b): Gain distribution by paradigm
paradigm_order = ['PCB Prototyping', 'Advanced Technologies', 'Cost-Effective']
gain_medians = [df[df['group']==p]['gain'].median() for p in paradigm_order]
gain_means = [df[df['group']==p]['gain'].mean() for p in paradigm_order]

x_pos = np.arange(len(paradigm_order))
width = 0.35

bars1 = ax2.bar(x_pos - width/2, gain_medians, width, label='Median',
                color=[colors_map[p] for p in paradigm_order], alpha=0.7, edgecolor='black')
bars2 = ax2.bar(x_pos + width/2, gain_means, width, label='Mean',
                color=[colors_map[p] for p in paradigm_order], alpha=0.4, edgecolor='black')

ax2.set_ylabel('Gain (dBi)', fontweight='bold', fontsize=10)
ax2.set_title('(b) Gain Statistics by Paradigm', fontweight='bold', fontsize=11)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(['PCB\n(n=6)', 'Advanced\n(n=4)', 'Cost-Eff.\n(n=3)'], fontsize=9)
ax2.legend(fontsize=9)
ax2.grid(axis='y', alpha=0.3)

# Panel (c): Bandwidth availability
bw_available = df.groupby('group').apply(lambda x: (x['bandwidth'] > 0).sum())
bw_missing = df.groupby('group').size() - bw_available

x_pos = np.arange(len(paradigm_order))
bars1 = ax3.bar(x_pos, bw_available, label='With BW data',
                color=[colors_map[p] for p in paradigm_order], alpha=0.8, edgecolor='black')
bars2 = ax3.bar(x_pos, bw_missing, bottom=bw_available, label='Without BW data',
                color='lightgray', alpha=0.6, edgecolor='black')

ax3.set_ylabel('Number of Studies', fontweight='bold', fontsize=10)
ax3.set_title('(c) Bandwidth Data Availability', fontweight='bold', fontsize=11)
ax3.set_xticks(x_pos)
ax3.set_xticklabels(['PCB\n(n=6)', 'Advanced\n(n=4)', 'Cost-Eff.\n(n=3)'], fontsize=9)
ax3.legend(fontsize=9)
ax3.grid(axis='y', alpha=0.3)

# Panel (d): Technique distribution
techniques = {
    'PCB Standard': 6,
    'Stacked Substrates': 1,
    '3D Printing': 1,
    'AMC Integration': 1,
    'Simplified Multilayer': 3,
    'Fractal': 1
}

ax4.barh(list(techniques.keys()), list(techniques.values()),
         color=['#2E86AB', '#A23B72', '#A23B72', '#A23B72', '#06A77D', '#2E86AB'],
         alpha=0.8, edgecolor='black')
ax4.set_xlabel('Number of Studies', fontweight='bold', fontsize=10)
ax4.set_title('(d) Fabrication Technique Distribution', fontweight='bold', fontsize=11)
ax4.grid(axis='x', alpha=0.3)

# Overall legend for paradigms
fig.legend(handles=[pcb_patch, adv_patch, ce_patch], loc='lower center',
           ncol=3, frameon=True, fontsize=10, bbox_to_anchor=(0.5, -0.02))

plt.suptitle('Figure 2. Fabrication Workflow Configuration Summary\n' +
             'Distribution and characterization across paradigms (n=13)',
             fontsize=13, fontweight='bold', y=0.98)

plt.tight_layout(rect=[0, 0.02, 1, 0.96])
plt.savefig('Figure2_WorkflowSummary.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure2_WorkflowSummary.pdf', bbox_inches='tight')
plt.close()

print("  [OK] Figure 2 saved")

# ==================================================================================
# Generate Study Code Mapping Table (for caption)
# ==================================================================================
print("\n" + "="*80)
print("STUDY CODE MAPPING (For Figure 1 Caption)")
print("="*80)

for group_name in ['PCB Prototyping', 'Advanced Technologies', 'Cost-Effective']:
    group_data = df[df['group'] == group_name].sort_values('gain', ascending=False)
    print(f"\n{group_name}:")
    for _, row in group_data.iterrows():
        print(f"  {row['code']}: {row['label']}")

print("\n" + "="*80)
print("STATISTICS SUMMARY")
print("="*80)

for group_name in ['PCB Prototyping', 'Advanced Technologies', 'Cost-Effective']:
    group_data = df[df['group'] == group_name]
    print(f"\n{group_name} (n={len(group_data)}):")
    print(f"  Gain - Median: {group_data['gain'].median():.1f} dBi, Mean: {group_data['gain'].mean():.1f} dBi")
    bw_data = group_data[group_data['bandwidth'] > 0]
    if len(bw_data) > 0:
        print(f"  Bandwidth - Median: {bw_data['bandwidth'].median():.1f}%, Mean: {bw_data['bandwidth'].mean():.1f}%")
        print(f"  BW data available: {len(bw_data)}/{len(group_data)} studies")
    else:
        print(f"  Bandwidth - No explicit data")

print("\n" + "="*80)
print("FIGURES GENERATED SUCCESSFULLY")
print("="*80)
print("\nFiles:")
print("  - Figure1_Individual_WithLegend.png/.pdf")
print("  - Figure2_WorkflowSummary.png/.pdf")
print("\nApproach: Individual data with codes + legend (no axis overlap)")
print("Consistency: Aligned with logicaRevision.txt OE4 objectives")
print("="*80)
