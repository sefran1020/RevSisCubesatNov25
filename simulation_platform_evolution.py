#!/usr/bin/env python3
"""
Análisis de Evolución Temporal de Plataformas de Simulación
Basado en baseDatos.csv
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import numpy as np
import re

# Configuración de estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 10)

def load_data(file_path):
    """Cargar datos del archivo CSV"""
    df = pd.read_csv(file_path, delimiter=';', encoding='utf-8-sig')
    return df

def extract_software_platforms(software_string):
    """Extraer nombres de plataformas de software de simulación"""
    if pd.isna(software_string) or software_string == 'Not mentioned':
        return []

    # Lista de plataformas conocidas
    platforms = {
        'HFSS': r'HFSS',
        'CST': r'CST(?:\s+(?:Microwave|STUDIO|Studio))?',
        'FEKO': r'(?:Altair\s+)?FEKO',
        'MATLAB': r'MATLAB',
        'ANSYS': r'ANSYS',
        'ADS': r'ADS|Advanced Design System',
        'Momentum': r'Momentum',
        'COMSOL': r'COMSOL',
        'EMPro': r'EMPro',
        'Sonnet': r'Sonnet',
        'IE3D': r'IE3D',
        'GRASP': r'GRASP',
        'WIPL-D': r'WIPL-D',
        '4NEC2': r'4NEC2',
        'NEC': r'NEC(?!2)',
        'GprMax': r'GprMax',
        'XFdtd': r'XFdtd',
        'SEMCAD': r'SEMCAD',
    }

    found_platforms = []
    software_upper = str(software_string).upper()

    for platform, pattern in platforms.items():
        if re.search(pattern, str(software_string), re.IGNORECASE):
            found_platforms.append(platform)

    return found_platforms

def analyze_temporal_evolution(df):
    """Analizar la evolución temporal de plataformas de simulación"""
    # Extraer columnas relevantes
    df_analysis = df[['gen.metadata.year', 'esp.domain_methodology.simulation_software']].copy()
    df_analysis.columns = ['year', 'software']

    # Convertir año a numérico
    df_analysis['year'] = pd.to_numeric(df_analysis['year'], errors='coerce')

    # Filtrar años válidos
    df_analysis = df_analysis[df_analysis['year'].notna()]
    df_analysis = df_analysis[(df_analysis['year'] >= 2000) & (df_analysis['year'] <= 2025)]

    # Extraer plataformas de software
    df_analysis['platforms'] = df_analysis['software'].apply(extract_software_platforms)

    # Crear un registro por cada plataforma
    records = []
    for _, row in df_analysis.iterrows():
        year = int(row['year'])
        for platform in row['platforms']:
            records.append({'year': year, 'platform': platform})

    df_platforms = pd.DataFrame(records)

    return df_analysis, df_platforms

def create_temporal_evolution_chart(df_platforms, output_file='simulation_evolution_timeline.png'):
    """Crear gráfico de evolución temporal"""
    fig, axes = plt.subplots(3, 1, figsize=(16, 12))

    # 1. Tendencia temporal por plataforma
    platform_by_year = df_platforms.groupby(['year', 'platform']).size().unstack(fill_value=0)

    # Seleccionar las plataformas más populares
    top_platforms = df_platforms['platform'].value_counts().head(8).index

    ax1 = axes[0]
    for platform in top_platforms:
        if platform in platform_by_year.columns:
            ax1.plot(platform_by_year.index, platform_by_year[platform],
                    marker='o', label=platform, linewidth=2, markersize=6)

    ax1.set_xlabel('Año', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Número de Publicaciones', fontsize=12, fontweight='bold')
    ax1.set_title('Evolución Temporal de Plataformas de Simulación (Top 8)',
                  fontsize=14, fontweight='bold', pad=20)
    ax1.legend(loc='upper left', fontsize=10)
    ax1.grid(True, alpha=0.3)

    # 2. Distribución acumulada
    ax2 = axes[1]
    cumulative_data = platform_by_year.cumsum()

    for platform in top_platforms:
        if platform in cumulative_data.columns:
            ax2.plot(cumulative_data.index, cumulative_data[platform],
                    marker='s', label=platform, linewidth=2, markersize=5)

    ax2.set_xlabel('Año', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Publicaciones Acumuladas', fontsize=12, fontweight='bold')
    ax2.set_title('Adopción Acumulada de Plataformas de Simulación',
                  fontsize=14, fontweight='bold', pad=20)
    ax2.legend(loc='upper left', fontsize=10)
    ax2.grid(True, alpha=0.3)

    # 3. Heatmap de uso por período
    ax3 = axes[2]

    # Agrupar por períodos de 3 años
    df_platforms_copy = df_platforms.copy()
    df_platforms_copy['period'] = (df_platforms_copy['year'] // 3) * 3
    period_platform = df_platforms_copy.groupby(['period', 'platform']).size().unstack(fill_value=0)

    # Seleccionar top 10 plataformas
    top_10_platforms = df_platforms['platform'].value_counts().head(10).index
    period_platform_filtered = period_platform[[col for col in top_10_platforms if col in period_platform.columns]]

    sns.heatmap(period_platform_filtered.T, annot=True, fmt='g', cmap='YlOrRd',
                ax=ax3, cbar_kws={'label': 'Número de Publicaciones'})
    ax3.set_xlabel('Período (agrupado cada 3 años)', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Plataforma de Simulación', fontsize=12, fontweight='bold')
    ax3.set_title('Intensidad de Uso de Plataformas por Período',
                  fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado: {output_file}")

    return fig

def create_market_share_evolution(df_platforms, output_file='simulation_market_share.png'):
    """Crear gráfico de evolución de cuota de mercado"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # Definir períodos
    periods = [
        (2000, 2010, '2000-2010'),
        (2011, 2015, '2011-2015'),
        (2016, 2020, '2016-2020'),
        (2021, 2025, '2021-2025')
    ]

    for idx, (start, end, label) in enumerate(periods):
        ax = axes[idx // 2, idx % 2]

        period_data = df_platforms[(df_platforms['year'] >= start) &
                                   (df_platforms['year'] <= end)]

        if len(period_data) > 0:
            platform_counts = period_data['platform'].value_counts().head(8)

            colors = sns.color_palette('husl', len(platform_counts))
            wedges, texts, autotexts = ax.pie(platform_counts.values,
                                               labels=platform_counts.index,
                                               autopct='%1.1f%%',
                                               startangle=90,
                                               colors=colors)

            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontweight('bold')
                autotext.set_fontsize(9)

            for text in texts:
                text.set_fontsize(10)

            ax.set_title(f'Período {label}\n(n={len(period_data)})',
                        fontsize=12, fontweight='bold', pad=15)
        else:
            ax.text(0.5, 0.5, f'Sin datos\npara {label}',
                   ha='center', va='center', fontsize=12)
            ax.set_title(f'Período {label}', fontsize=12, fontweight='bold')

    plt.suptitle('Evolución de Cuota de Mercado de Plataformas de Simulación',
                 fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado: {output_file}")

    return fig

def generate_statistics_report(df_platforms):
    """Generar reporte estadístico"""
    report = []
    report.append("=" * 80)
    report.append("ANÁLISIS ESTADÍSTICO: PLATAFORMAS DE SIMULACIÓN")
    report.append("=" * 80)
    report.append("")

    # Estadísticas generales
    total_entries = len(df_platforms)
    unique_platforms = df_platforms['platform'].nunique()
    year_range = (df_platforms['year'].min(), df_platforms['year'].max())

    report.append("ESTADÍSTICAS GENERALES")
    report.append("-" * 80)
    report.append(f"Total de registros: {total_entries}")
    report.append(f"Plataformas únicas identificadas: {unique_platforms}")
    report.append(f"Rango temporal: {int(year_range[0])} - {int(year_range[1])}")
    report.append("")

    # Top plataformas
    report.append("TOP 10 PLATAFORMAS MÁS UTILIZADAS")
    report.append("-" * 80)
    top_platforms = df_platforms['platform'].value_counts().head(10)
    for idx, (platform, count) in enumerate(top_platforms.items(), 1):
        percentage = (count / total_entries) * 100
        report.append(f"{idx:2d}. {platform:20s} - {count:3d} ({percentage:5.2f}%)")
    report.append("")

    # Tendencias por período
    report.append("TENDENCIAS POR PERÍODO")
    report.append("-" * 80)

    periods = [
        (2000, 2010, '2000-2010'),
        (2011, 2015, '2011-2015'),
        (2016, 2020, '2016-2020'),
        (2021, 2025, '2021-2025')
    ]

    for start, end, label in periods:
        period_data = df_platforms[(df_platforms['year'] >= start) &
                                   (df_platforms['year'] <= end)]

        if len(period_data) > 0:
            report.append(f"\nPeríodo {label}:")
            report.append(f"  Total de publicaciones: {len(period_data)}")

            top_3 = period_data['platform'].value_counts().head(3)
            report.append("  Top 3 plataformas:")
            for idx, (platform, count) in enumerate(top_3.items(), 1):
                percentage = (count / len(period_data)) * 100
                report.append(f"    {idx}. {platform}: {count} ({percentage:.1f}%)")

    report.append("")
    report.append("=" * 80)

    return "\n".join(report)

def main():
    print("Iniciando análisis de evolución de plataformas de simulación...")

    # Cargar datos
    df = load_data('baseDatos.csv')
    print(f"Datos cargados: {len(df)} registros")

    # Analizar evolución temporal
    df_analysis, df_platforms = analyze_temporal_evolution(df)
    print(f"Plataformas identificadas: {len(df_platforms)} registros")
    print(f"Plataformas únicas: {df_platforms['platform'].nunique()}")

    # Generar visualizaciones
    print("\nGenerando visualizaciones...")
    create_temporal_evolution_chart(df_platforms)
    create_market_share_evolution(df_platforms)

    # Generar reporte estadístico
    print("\nGenerando reporte estadístico...")
    report = generate_statistics_report(df_platforms)
    print("\n" + report)

    # Guardar reporte
    with open('simulation_platform_evolution_report.txt', 'w', encoding='utf-8') as f:
        f.write(report)
    print("\nReporte guardado: simulation_platform_evolution_report.txt")

    # Guardar datos procesados
    df_platforms.to_csv('simulation_platforms_processed.csv', index=False, encoding='utf-8')
    print("Datos procesados guardados: simulation_platforms_processed.csv")

    print("\n✓ Análisis completado exitosamente")

if __name__ == "__main__":
    main()
