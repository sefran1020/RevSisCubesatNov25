"""
FINAL VERSION: Single High-Impact Figure for Objective Specific 4
Figure 1 ONLY: Performance Metrics Across Fabrication Paradigms (Box Plots)
Additional insights presented as TABLES in text, not as figures with empty cells
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
print(f"  PCB Prototyping: {len(grupoA)} studies (46.2%)")
print(f"  Advanced Technologies: {len(grupoB)} studies (30.8%)")
print(f"  Cost-Effective: {len(grupoC)} studies (23.1%)")

# Color scheme
colors_map = {
    'PCB Prototyping': '#2E86AB',
    'Advanced Technologies': '#A23B72',
    'Cost-Effective': '#06A77D'
}

print("\n" + "="*80)
print("GENERATING FIGURE 1: Performance Metrics by Fabrication Paradigm")
print("="*80 + "\n")

# ==================================================================================
# FIGURE 1: Performance Metrics by Fabrication Paradigm (Box Plots)
# ==================================================================================

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

    if gain > 0:
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
plt.savefig('Figure1_PerformanceByParadigm_FINAL.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure1_PerformanceByParadigm_FINAL.pdf', bbox_inches='tight')
plt.close()

print("  [OK] Figure 1 saved as Figure1_PerformanceByParadigm_FINAL.png/.pdf")

# Print statistics
print("\n" + "="*80)
print("PERFORMANCE STATISTICS BY PARADIGM")
print("="*80)

for group in groups:
    print(f"\n{group}:")

    gain_values = gain_data[gain_data['Group'] == group]['Value']
    if len(gain_values) > 0:
        print(f"  Gain (dBi):")
        print(f"    Median: {gain_values.median():.1f}")
        print(f"    Range: {gain_values.min():.1f} - {gain_values.max():.1f}")
        print(f"    Mean: {gain_values.mean():.1f}")
        print(f"    n={len(gain_values)} studies")

    bw_values = bw_data[bw_data['Group'] == group]['Value']
    if len(bw_values) > 0:
        print(f"  Bandwidth (%):")
        print(f"    Median: {bw_values.median():.1f}")
        print(f"    Range: {bw_values.min():.1f} - {bw_values.max():.1f}")
        print(f"    Mean: {bw_values.mean():.1f}")
        print(f"    n={len(bw_values)} studies")

print("\n" + "="*80)
print("SUPPORTING TABLES (for text integration)")
print("="*80)

# ==================================================================================
# TABLE 1: Fabrication Technique-Outcome Associations (for text)
# ==================================================================================
print("\nTABLE 1: Key Fabrication Technique-Performance Outcome Associations")
print("-" * 80)

technique_outcomes = [
    ("PCB Photolithography", "Dual/Multi-band + Circular Polarization", "n=6 (most common)"),
    ("Stacked Substrates", "Wide Bandwidth (>30%)", "n=2 (UWB, 49% IBW)"),
    ("3D Metal Printing", "Dual-band + CP", "n=1 (emerging)"),
    ("AMC Integration", "High Gain + CP", "n=1 (10.22 dBic, 42.42% IBW)"),
    ("Multilayer Simplified", "Mass Production Suitable", "n=3 (cost-effective)"),
    ("Fractal Geometry", "Miniaturization", "n=1 (electrically small)")
]

print(f"{'Technique':<25} {'Performance Outcome':<35} {'Evidence':<20}")
print("-" * 80)
for tech, outcome, evidence in technique_outcomes:
    print(f"{tech:<25} {outcome:<35} {evidence:<20}")

# ==================================================================================
# TABLE 2: Paradigm Characteristics Summary (for text)
# ==================================================================================
print("\n\nTABLE 2: Fabrication Paradigm Characteristics Summary")
print("-" * 80)

paradigm_chars = [
    ("PCB Prototyping", "46.2% (n=6)", "7.5 dBi", "Variable", "Low", "Well-established"),
    ("Advanced Technologies", "30.8% (n=4)", "26.0 dBi", "Up to 49% / UWB", "High", "Innovation focus"),
    ("Cost-Effective", "23.1% (n=3)", "10.9 dBi", "Competitive", "Medium", "Mass production")
]

print(f"{'Paradigm':<22} {'Coverage':<12} {'Median Gain':<13} {'Bandwidth':<18} {'Complexity':<12} {'Maturity':<18}")
print("-" * 80)
for paradigm, coverage, gain, bw, complexity, maturity in paradigm_chars:
    print(f"{paradigm:<22} {coverage:<12} {gain:<13} {bw:<18} {complexity:<12} {maturity:<18}")

print("\n" + "="*80)
print("FIGURE AND TABLES GENERATION COMPLETE")
print("="*80)
print("\nGenerated files:")
print("  - Figure1_PerformanceByParadigm_FINAL.png (300 dpi)")
print("  - Figure1_PerformanceByParadigm_FINAL.pdf (vector)")
print("\nSupporting tables printed above for text integration")
print("  - Table 1: Technique-Outcome Associations (6 key relationships)")
print("  - Table 2: Paradigm Characteristics Summary (3 paradigms)")
print("\nRecommendation: Use Figure 1 as main visual, Tables 1-2 in text")
print("="*80)
