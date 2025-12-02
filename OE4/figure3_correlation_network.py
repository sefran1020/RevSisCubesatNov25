"""
FIGURE 3: Fabrication-Performance Correlation Network
Objective Specific 4 - CubeSat Antenna Systematic Review
Network diagram showing relationships between fabrication techniques and performance outcomes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyBboxPatch

# Set publication-quality parameters
plt.rcParams['figure.figsize'] = (16, 12)
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

# Create directed graph
G = nx.DiGraph()

# Define node categories
fabrication_techniques = [
    'PCB Photolithography',
    '3D Metal Printing',
    'Stacked Substrates',
    'AMC Integration',
    'Multilayer Simplified',
    'Reconfigurable Materials'
]

performance_outcomes = [
    'Wide Bandwidth (>30%)',
    'High Gain (>10 dBi)',
    'Dual/Multi-band',
    'Circular Polarization',
    'Miniaturization (<0.25λ)',
    'High Efficiency (>90%)'
]

# Add nodes
for tech in fabrication_techniques:
    G.add_node(tech, node_type='fabrication', color='#2E86AB')

for outcome in performance_outcomes:
    G.add_node(outcome, node_type='performance', color='#06A77D')

# Extract relationships from data
edges = []

for idx, row in df.iterrows():
    author = str(row['gen.metadata.authors']).split(';')[0].strip()
    year = str(row['gen.metadata.year'])
    citation = f"{author} et al. ({year})"

    fab_material = str(row['esp.technical_specifications.fabrication_material'])
    bandwidth_str = str(row['esp.domain_results.bandwidth'])
    gain_str = str(row['esp.domain_results.gain'])
    antenna_type = str(row['esp.technical_specifications.antenna_type'])
    polarization = str(row['esp.technical_specifications.polarization'])
    antenna_size = str(row['esp.technical_specifications.antenna_size'])
    main_findings = str(row['gen.detailed_results.main_findings'])

    # Identify fabrication technique
    fab_tech = None
    if '3D' in fab_material or '3-D' in fab_material or 'metal printing' in fab_material.lower():
        fab_tech = '3D Metal Printing'
    elif 'stacked' in fab_material.lower() or 'stacking' in main_findings.lower():
        fab_tech = 'Stacked Substrates'
    elif 'AMC' in antenna_type or 'AMC' in main_findings:
        fab_tech = 'AMC Integration'
    elif 'multilayer' in fab_material.lower() or 'Multilayer' in main_findings:
        fab_tech = 'Multilayer Simplified'
    elif 'reconfigurable' in antenna_type.lower() or 'reconfigurable' in main_findings.lower():
        fab_tech = 'Reconfigurable Materials'
    else:
        fab_tech = 'PCB Photolithography'

    # Identify performance outcomes
    performances = []

    # Wide Bandwidth
    if '%' in bandwidth_str:
        import re
        numbers = re.findall(r'[-+]?\d*\.?\d+', bandwidth_str)
        if numbers and float(numbers[0]) > 30:
            performances.append('Wide Bandwidth (>30%)')

    # High Gain
    if 'dBi' in gain_str or 'dBic' in gain_str:
        import re
        numbers = re.findall(r'[-+]?\d*\.?\d+', gain_str)
        if numbers:
            max_gain = max([float(n) for n in numbers])
            if max_gain > 10:
                performances.append('High Gain (>10 dBi)')

    # Dual/Multi-band
    if 'dual-band' in main_findings.lower() or 'dual band' in main_findings.lower():
        performances.append('Dual/Multi-band')
    elif 'multi-band' in main_findings.lower() or 'tri-band' in main_findings.lower():
        performances.append('Dual/Multi-band')

    # Circular Polarization
    if 'circular' in polarization.lower() or 'CP' in polarization or 'circularly' in main_findings.lower():
        performances.append('Circular Polarization')

    # Miniaturization
    if '<' in antenna_size or 'compact' in main_findings.lower() or 'miniaturization' in main_findings.lower():
        performances.append('Miniaturization (<0.25λ)')

    # High Efficiency
    if 'efficiency' in main_findings.lower() and '>90%' in main_findings.lower():
        performances.append('High Efficiency (>90%)')
    elif 'radiation efficiency exceeds 90%' in main_findings.lower():
        performances.append('High Efficiency (>90%)')

    # Add edges
    for perf in performances:
        edge_exists = False
        for edge in edges:
            if edge[0] == fab_tech and edge[1] == perf:
                edge['weight'] += 1
                edge['citations'].append(citation)
                edge_exists = True
                break

        if not edge_exists:
            edges.append({
                'source': fab_tech,
                'target': perf,
                'weight': 1,
                'citations': [citation]
            })

# Add edges to graph
for edge in edges:
    G.add_edge(edge['source'], edge['target'],
               weight=edge['weight'],
               citations=edge['citations'])

# Create layout
pos = {}

# Position fabrication techniques on left
fab_y_positions = np.linspace(5, 1, len(fabrication_techniques))
for i, tech in enumerate(fabrication_techniques):
    pos[tech] = (0, fab_y_positions[i])

# Position performance outcomes on right
perf_y_positions = np.linspace(5, 1, len(performance_outcomes))
for i, outcome in enumerate(performance_outcomes):
    pos[outcome] = (3, perf_y_positions[i])

# Create figure
fig, ax = plt.subplots(figsize=(16, 12))

# Draw edges with varying thickness based on weight
for edge in edges:
    source = edge['source']
    target = edge['target']
    weight = edge['weight']
    citations = edge['citations']

    x_coords = [pos[source][0], pos[target][0]]
    y_coords = [pos[source][1], pos[target][1]]

    # Determine robustness
    if weight >= 2:
        color = '#A23B72'  # High robustness (purple-red)
        linestyle = '-'
        robustness = 'High'
    else:
        color = '#F18F01'  # Medium robustness (orange)
        linestyle = '--'
        robustness = 'Medium'

    ax.plot(x_coords, y_coords, color=color, linewidth=weight*2,
            alpha=0.6, linestyle=linestyle, zorder=1)

    # Add edge label
    mid_x = (x_coords[0] + x_coords[1]) / 2
    mid_y = (y_coords[0] + y_coords[1]) / 2
    label = f"n={weight}\n{robustness}"
    ax.text(mid_x, mid_y, label, fontsize=7, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor=color))

# Draw nodes
for node in G.nodes():
    x, y = pos[node]
    node_type = G.nodes[node]['node_type']
    color = G.nodes[node]['color']

    if node_type == 'fabrication':
        bbox = FancyBboxPatch((x-0.25, y-0.15), 0.5, 0.3,
                              boxstyle="round,pad=0.05",
                              facecolor=color, edgecolor='black',
                              linewidth=2, zorder=2)
        ax.add_patch(bbox)
        ax.text(x, y, node, fontsize=9, ha='center', va='center',
                fontweight='bold', color='white', zorder=3)
    else:
        bbox = FancyBboxPatch((x-0.35, y-0.15), 0.7, 0.3,
                              boxstyle="round,pad=0.05",
                              facecolor=color, edgecolor='black',
                              linewidth=2, zorder=2)
        ax.add_patch(bbox)
        ax.text(x, y, node, fontsize=9, ha='center', va='center',
                fontweight='bold', color='white', zorder=3)

# Add section labels
ax.text(-0.5, 6, 'FABRICATION\nTECHNIQUES', fontsize=12,
        fontweight='bold', ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#2E86AB', alpha=0.3))

ax.text(3.5, 6, 'PERFORMANCE\nOUTCOMES', fontsize=12,
        fontweight='bold', ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#06A77D', alpha=0.3))

# Formatting
ax.set_xlim(-0.8, 4.2)
ax.set_ylim(0.5, 6.5)
ax.axis('off')

ax.set_title('Figure 3. Fabrication-Performance Correlation Network\n' +
             'Documented relationships between fabrication techniques and performance outcomes (n=14 studies)\n' +
             'Edge thickness indicates number of supporting studies; solid=high robustness, dashed=medium robustness',
             fontsize=13, fontweight='bold', pad=20)

# Add legend for robustness
legend_elements = [
    plt.Line2D([0], [0], color='#A23B72', linewidth=3, linestyle='-', label='High robustness (≥2 studies)'),
    plt.Line2D([0], [0], color='#F18F01', linewidth=3, linestyle='--', label='Medium robustness (1 study)')
]
ax.legend(handles=legend_elements, loc='lower center', ncol=2,
          frameon=True, fancybox=True, shadow=True, fontsize=10)

plt.tight_layout()
plt.savefig('Figure3_CorrelationNetwork.png', dpi=300, bbox_inches='tight')
plt.savefig('Figure3_CorrelationNetwork.pdf', bbox_inches='tight')

# Print network statistics
print("\nFigure 3 - Network Statistics")
print("="*80)
print(f"Total nodes: {G.number_of_nodes()}")
print(f"Total edges: {G.number_of_edges()}")
print(f"\nEdge Details:")
for edge in edges:
    print(f"  {edge['source']} → {edge['target']}")
    print(f"    Weight: {edge['weight']} | Citations: {', '.join(edge['citations'])}")

print("\n" + "="*80)
print("Figure saved as: Figure3_CorrelationNetwork.png and Figure3_CorrelationNetwork.pdf")
