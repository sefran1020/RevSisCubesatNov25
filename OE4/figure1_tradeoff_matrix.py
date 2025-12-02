"""
FIGURE 1: Fabrication Technology Performance-Cost Trade-off Matrix
Objective Specific 4 - CubeSat Antenna Systematic Review
Data source: grupoA.csv, grupoB.csv, grupoC.csv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Set publication-quality parameters
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9

# Load data from CSV files
grupoA = pd.read_csv('grupoA.csv', encoding='utf-8')
grupoB = pd.read_csv('grupoB.csv', encoding='utf-8')
grupoC = pd.read_csv('grupoC.csv', encoding='utf-8')

# Add group labels
grupoA['group'] = 'PCB Prototyping'
grupoB['group'] = 'Advanced Technologies'
grupoC['group'] = 'Cost-Effective'

# Combine datasets
df = pd.concat([grupoA, grupoB, grupoC], ignore_index=True)

# Extract relevant columns
data = []

for idx, row in df.iterrows():
    # Extract author and year
    authors = str(row['gen.metadata.authors']).split(';')[0] if pd.notna(row['gen.metadata.authors']) else 'Unknown'
    year = str(row['gen.metadata.year']) if pd.notna(row['gen.metadata.year']) else '0000'

    # Calculate Complexity Index (based on fabrication method description)
    fab_material = str(row['esp.technical_specifications.fabrication_material'])
    feeding = str(row['esp.technical_specifications.feeding_element_design'])

    complexity = 2  # base complexity for PCB
    if '3D' in fab_material or '3-D' in fab_material:
        complexity += 3
    if 'stacked' in fab_material.lower() or 'multilayer' in fab_material.lower():
        complexity += 2
    if 'AMC' in str(row['gen.metadata.keywords']) or 'metasurface' in str(row['gen.metadata.keywords']).lower():
        complexity += 2
    if 'Sequential' in feeding or 'network' in feeding.lower():
        complexity += 1

    # Calculate Performance Score (normalized aggregate)
    # Extract gain
    gain_str = str(row['esp.domain_results.gain'])
    gain = 0
    if 'dBic' in gain_str or 'dBi' in gain_str:
        # Extract numeric values
        import re
        numbers = re.findall(r'[-+]?\d*\.?\d+', gain_str)
        if numbers:
            gain = max([float(n) for n in numbers])

    # Extract bandwidth
    bw_str = str(row['esp.domain_results.bandwidth'])
    bandwidth = 0
    if '%' in bw_str:
        numbers = re.findall(r'[-+]?\d*\.?\d+', bw_str)
        if numbers:
            bandwidth = max([float(n) for n in numbers])
    elif 'GHz' in bw_str:
        # Calculate fractional bandwidth
        numbers = re.findall(r'[-+]?\d*\.?\d+', bw_str)
        if len(numbers) >= 2:
            f_low = float(numbers[0])
            f_high = float(numbers[1])
            if f_low > 0:
                bandwidth = ((f_high - f_low) / ((f_high + f_low) / 2)) * 100

    # Extract efficiency (from main_findings or radiation efficiency)
    efficiency_str = str(row['gen.detailed_results.main_findings'])
    efficiency = 0
    if 'efficiency' in efficiency_str.lower():
        numbers = re.findall(r'(\d+)%', efficiency_str)
        if numbers:
            efficiency = max([float(n) for n in numbers])

    # Normalize and combine (0-100 scale)
    performance_score = (
        (gain / 30 * 30) +  # Max gain ~30 dB -> 30 points
        (bandwidth / 100 * 40) +  # Max BW ~100% -> 40 points
        (efficiency / 100 * 30)  # Max eff ~100% -> 30 points
    )

    # Estimate Cost Factor (inverse - higher = more expensive)
    cost_factor = 1  # base cost
    if row['group'] == 'Advanced Technologies':
        cost_factor = 3
    elif row['group'] == 'Cost-Effective':
        cost_factor = 0.5
    else:  # PCB Prototyping
        cost_factor = 1

    # Adjust based on materials
    if 'Rogers' in fab_material:
        cost_factor *= 1.5
    if '3D' in fab_material:
        cost_factor *= 2

    data.append({
        'author': authors,
        'year': year,
        'citation': f"{authors} ({year})",
        'group': row['group'],
        'complexity': complexity,
        'performance': performance_score,
        'cost': cost_factor,
        'gain': gain,
        'bandwidth': bandwidth,
        'title': str(row['gen.metadata.title'])[:50]
    })

df_plot = pd.DataFrame(data)

# Create 3D scatter plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Color mapping
colors = {
    'PCB Prototyping': '#2E86AB',  # Blue
    'Advanced Technologies': '#A23B72',  # Purple-red
    'Cost-Effective': '#06A77D'  # Green
}

# Plot each group
for group_name, color in colors.items():
    group_data = df_plot[df_plot['group'] == group_name]

    scatter = ax.scatter(
        group_data['complexity'],
        group_data['performance'],
        group_data['cost'],
        c=color,
        s=group_data['cost']*200,  # Bubble size proportional to cost
        alpha=0.6,
        edgecolors='black',
        linewidths=1,
        label=f"{group_name} (n={len(group_data)})"
    )

# Annotations for key studies
annotations = [
    ('Curreli', 2021, 'Ka-band LEO-qualified'),
    ('Wang', 2024, '3D-printed FSP'),
    ('Torrungrueng', 2025, '0.72λ₀ compact'),
    ('Krairiksh', 2024, 'AMC 42% IBW'),
    ('DiCarlofelice', 2022, 'Mass production')
]

for author_key, year, label in annotations:
    match = df_plot[df_plot['citation'].str.contains(author_key) &
                    (df_plot['year'] == str(year))]
    if not match.empty:
        row = match.iloc[0]
        ax.text(row['complexity'], row['performance'], row['cost'],
                f"  {label}", fontsize=8, ha='left')

# Labels and formatting
ax.set_xlabel('Complexity Index\n(fabrication processes)', fontsize=11, labelpad=10)
ax.set_ylabel('Performance Score\n(gain + bandwidth + efficiency)', fontsize=11, labelpad=10)
ax.set_zlabel('Estimated Cost Factor', fontsize=11, labelpad=10)

ax.set_title('Figure 1. Fabrication Technology Performance-Cost Trade-off Matrix\n' +
             'Three-dimensional analysis of 14 CubeSat antenna fabrication configurations',
             fontsize=13, fontweight='bold', pad=20)

# Legend
ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)

# Grid
ax.grid(True, alpha=0.3)

# View angle
ax.view_init(elev=20, azim=45)

plt.tight_layout()
plt.savefig('Figure1_TradeoffMatrix.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure1_TradeoffMatrix.pdf', bbox_inches='tight')

# Create accompanying statistics table
print("\nFigure 1 - Statistics Summary")
print("="*70)
for group_name in ['PCB Prototyping', 'Advanced Technologies', 'Cost-Effective']:
    group_data = df_plot[df_plot['group'] == group_name]
    print(f"\n{group_name} (n={len(group_data)}):")
    print(f"  Complexity: μ={group_data['complexity'].mean():.2f}, σ={group_data['complexity'].std():.2f}")
    print(f"  Performance: μ={group_data['performance'].mean():.2f}, σ={group_data['performance'].std():.2f}")
    print(f"  Cost Factor: μ={group_data['cost'].mean():.2f}, σ={group_data['cost'].std():.2f}")
    print(f"  Studies: {', '.join(group_data['citation'].tolist())}")

print("\n" + "="*70)
print("Figure saved as: Figure1_TradeoffMatrix.png and Figure1_TradeoffMatrix.pdf")
