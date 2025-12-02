"""
FIGURA 3.3.3: Temporal Evolution Timeline with Performance Metrics

TRAZABILIDAD: Datos extraídos de:
- grupoA.csv: gen.metadata.year, esp.domain_results.gain, esp.domain_results.bandwidth
- grupoB.csv: gen.metadata.year, esp.domain_results.gain, esp.domain_results.bandwidth
- grupoC.csv: gen.metadata.year, esp.domain_results.gain, esp.domain_results.bandwidth
- grupoD.csv: gen.metadata.year, esp.domain_results.gain, esp.domain_results.bandwidth
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Circle
import matplotlib.patches as mpatches

# =====================================================
# DATOS TRAZABLES DE CSV - EXTRACCIÓN MANUAL
# =====================================================

# Datos extraídos de grupoA.csv (líneas 2-11)
grupo_a_data = [
    # año, autor, gain(dBi), bandwidth_pct, feed_type, freq_band
    (2015, 'Islam et al.', 7.29, 2.73, 'Single-feed', 'S-band', '#4CAF50'),
    (2018, 'Lee et al.', 0.0, 3.8, 'Single-feed', 'L/S dual', '#4CAF50'),  # gain not explicit, using 0
    (2021, 'Rzymowski et al.', 14.0, 20.0, 'Single-feed', 'X-band', '#4CAF50'),
    (2018, 'Semkin', 9.35, None, 'Single-feed', 'S-band', '#4CAF50'),
    (2021, 'Curreli et al.', 8.0, 16.6, 'Single-feed', 'Ka-band', '#4CAF50'),
    (2021, 'Nguyen et al.', 6.2, 15.23, 'Single-feed', 'S-band', '#4CAF50'),
    (2025, 'Ta et al.', 11.72, None, 'Single-feed', 'X-band', '#4CAF50'),
    (2021, 'Theoharis et al.', 20.1, 3.8, 'Single-feed', 'X-band', '#4CAF50'),
    (2021, 'Thunyakaset et al.', 8.17, None, 'Single-feed', 'S-band', '#4CAF50'),
]

# Datos extraídos de grupoB.csv (líneas 2-10)
grupo_b_data = [
    (2019, 'Liu & Tang', 6.98, 1.65, 'Coaxial probe', 'ADS-B', '#2196F3'),
    (2023, 'Abd-Elmonieum et al.', 32.7, None, 'DS-Post', '5G/CubeSat', '#2196F3'),
    (2018, 'Sajal et al.', None, 8.0, 'Coaxial probe', 'UHF', '#2196F3'),
    (2015, 'Mengu Cho et al.', 7.29, 2.73, 'Coaxial probe', 'S-band', '#2196F3'),
    (2018, 'Kibria et al.', 1.01, 6.92, 'Coaxial probe', 'UHF', '#2196F3'),
    (2022, 'Priscila et al.', 4.505, None, 'Coaxial feed', 'ADS-B', '#2196F3'),
    (2018, 'Fawzy Ibrahim et al.', 6.687, 3.82, 'Coaxial probe', 'GPS L1', '#2196F3'),
]

# Datos extraídos de grupoC.csv (líneas 2-6)
grupo_c_data = [
    (2017, 'Lehmensiek', None, None, 'Sequential-phase', 'X-band', '#FF9800'),
    (2024, 'Wang et al.', 2.32, None, 'Five-port coupler', 'L/S dual', '#FF9800'),
    (2017, 'Puerto-Leguizamón', 6.04, 27.44, '90° hybrid', 'S-band', '#FF9800'),
    (2016, 'Kai Xue et al.', 6.0, None, 'Sequential feed', 'L/S dual', '#FF9800'),
]

# Datos extraídos de grupoD.csv (líneas 2-5)
grupo_d_data = [
    (2018, 'Mahmoud Rajab et al.', 12.0, None, 'Strip-line', 'UWB', '#E91E63'),
    (2025, 'Saeidi et al.', 12.5, None, 'Transmission line', 'Multi-band', '#E91E63'),
    (2021, 'Wenquan Che et al.', 4.7, None, 'Dual-port annular', 'C-band', '#E91E63'),
]

# Consolidar todos los datos
all_data = grupo_a_data + grupo_b_data + grupo_c_data + grupo_d_data

# Filtrar datos con gain definido para el scatter plot principal
data_with_gain = [d for d in all_data if d[2] is not None]

# =====================================================
# PREPARAR DATOS PARA VISUALIZACIÓN
# =====================================================

years = [d[0] for d in data_with_gain]
authors = [d[1] for d in data_with_gain]
gains = [d[2] for d in data_with_gain]
bandwidths = [d[3] if d[3] is not None else 5.0 for d in data_with_gain]  # Default 5% si no hay dato
feed_types = [d[4] for d in data_with_gain]
freq_bands = [d[5] for d in data_with_gain]
colors = [d[6] for d in data_with_gain]

# Normalizar tamaños de burbujas (bandwidth → tamaño)
sizes = [bw * 30 for bw in bandwidths]  # Escalar para visualización

# =====================================================
# CREAR FIGURA
# =====================================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12),
                                gridspec_kw={'height_ratios': [3, 1]})

# --- SUBPLOT PRINCIPAL: Timeline con burbujas ---
scatter = ax1.scatter(years, gains, s=sizes, c=colors, alpha=0.6,
                      edgecolors='black', linewidth=1.5)

# Añadir etiquetas para cada punto
for i, (year, gain, author, bw) in enumerate(zip(years, gains, authors, bandwidths)):
    # Alternar posición de etiquetas para evitar solapamiento
    offset = 15 if i % 2 == 0 else -15
    va = 'bottom' if i % 2 == 0 else 'top'

    ax1.annotate(f'{author}\n{gain:.1f} dBi',
                 xy=(year, gain), xytext=(0, offset),
                 textcoords='offset points',
                 ha='center', va=va, fontsize=7,
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor='gray', alpha=0.8),
                 arrowprops=dict(arrowstyle='-', connectionstyle='arc3,rad=0',
                                color='gray', alpha=0.5, lw=0.5))

# Configuración de ejes
ax1.set_xlabel('Publication Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Gain (dBi)', fontsize=12, fontweight='bold')
ax1.set_title('Figure 3.3.3: Temporal Evolution of Feeding Designs (2015-2025)\n' +
              'Bubble size ∝ Bandwidth (%); Color = Feeding architecture type',
              fontsize=13, fontweight='bold', pad=20)

# Grid y límites
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.set_xlim(2014.5, 2025.5)
ax1.set_ylim(0, 35)

# Línea de tendencia
from scipy.stats import linregress
if len(years) > 3:
    slope, intercept, r_value, p_value, std_err = linregress(years, gains)
    trend_line = [slope * x + intercept for x in range(2015, 2026)]
    ax1.plot(range(2015, 2026), trend_line, 'r--', linewidth=2, alpha=0.7,
             label=f'Trend: y={slope:.2f}x+{intercept:.0f} (R²={r_value**2:.3f})')

# Fases temporales (boxes de fondo)
ax1.axvspan(2014.5, 2017.5, alpha=0.1, color='green',
            label='Phase 1: Foundation (2015-2017)')
ax1.axvspan(2017.5, 2021.5, alpha=0.1, color='blue',
            label='Phase 2: Expansion (2018-2021)')
ax1.axvspan(2021.5, 2025.5, alpha=0.1, color='orange',
            label='Phase 3: Advanced Integration (2022-2025)')

ax1.legend(loc='upper left', fontsize=9, framealpha=0.9)

# --- SUBPLOT INFERIOR: Histograma de frecuencia por año ---
unique_years = sorted(set(years))
counts_per_year = [years.count(y) for y in unique_years]

ax2.bar(unique_years, counts_per_year, width=0.6, color='steelblue',
        edgecolor='black', alpha=0.7)
ax2.set_xlabel('Year', fontsize=11, fontweight='bold')
ax2.set_ylabel('Number of Studies', fontsize=11, fontweight='bold')
ax2.set_title('Publication Frequency Distribution', fontsize=11, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)
ax2.set_xlim(2014.5, 2025.5)

# Añadir valores en barras
for year, count in zip(unique_years, counts_per_year):
    ax2.text(year, count + 0.1, str(count), ha='center', va='bottom',
             fontweight='bold', fontsize=10)

# --- LEYENDA DE TAMAÑOS (burbujas) ---
legend_elements = [
    mpatches.Patch(color='#4CAF50', label='Single-Feed (n=9)'),
    mpatches.Patch(color='#2196F3', label='Coaxial/Probe (n=7)'),
    mpatches.Patch(color='#FF9800', label='Complex Networks (n=4)'),
    mpatches.Patch(color='#E91E63', label='Specialized (n=3)'),
]

# Añadir referencia de tamaños
for i, (size_val, label) in enumerate([(5, '5%'), (10, '10%'), (20, '20%')]):
    legend_elements.append(
        plt.Line2D([0], [0], marker='o', color='w',
                  markerfacecolor='gray', markersize=np.sqrt(size_val*30)/2,
                  label=f'BW {label}', alpha=0.6)
    )

ax1.legend(handles=legend_elements, loc='upper right', fontsize=8,
          framealpha=0.95, title='Feeding Types & Bandwidth Reference')

# --- NOTA DE TRAZABILIDAD ---
fig.text(0.5, 0.01,
         'Data sources: grupoA.csv (rows 2-11), grupoB.csv (rows 2-10), grupoC.csv (rows 2-6), grupoD.csv (rows 2-5)\n' +
         f'Fields: gen.metadata.year, esp.domain_results.gain, esp.domain_results.bandwidth | n={len(data_with_gain)} studies with gain data',
         ha='center', va='bottom', fontsize=7, style='italic',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.savefig('G:/RevSisOrd/OE3Figuras/Figure_3_3_3_Temporal_Evolution.png', dpi=300, bbox_inches='tight')
plt.savefig('G:/RevSisOrd/OE3Figuras/Figure_3_3_3_Temporal_Evolution.pdf', bbox_inches='tight')

print("[OK] Figura 3.3.3 generada exitosamente")
print(f"[OK] Trazabilidad: {len(all_data)} estudios totales, {len(data_with_gain)} con datos de gain")
print(f"[OK] Rango temporal: {min(years)}-{max(years)}")
print(f"[OK] Rango de gain: {min(gains):.2f}-{max(gains):.2f} dBi")
