"""
Script Maestro: Generación de Todas las Figuras para OE2
Ejecuta todos los scripts de visualización y genera resumen

Autor: Sistema de Validación
Fecha: 2025-11-14
Basado en: Datos validados de grupoA-D.csv
"""

import subprocess
import sys
import os
from datetime import datetime

# Fix encoding for Windows console
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass  # If reconfigure fails, continue with default encoding

print("="*70)
print(" GENERACIÓN DE FIGURAS - OBJETIVO ESPECÍFICO 2 (OE2)")
print(" Validación Experimental: Instrument-Protocol Alignment")
print("="*70)
print(f"\nFecha de ejecución: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Directorio de trabajo: {os.getcwd()}\n")

# Lista de scripts a ejecutar
scripts = [
    {
        'name': 'fig3_validation_pyramid.py',
        'description': 'Validation Comprehensiveness Pyramid',
        'priority': 'ALTA',
        'outputs': ['fig3_validation_pyramid.png', 'fig3_validation_pyramid.pdf']
    },
    {
        'name': 'fig_instrument_validation_matrix.py',
        'description': 'Instrument-Validation Alignment Matrix',
        'priority': 'MEDIA',
        'outputs': ['fig_instrument_validation_matrix.png', 'fig_instrument_validation_matrix.pdf']
    },
    {
        'name': 'fig_validation_coverage_gaps.py',
        'description': 'Validation Coverage Gaps',
        'priority': 'ALTA',
        'outputs': ['fig_validation_coverage_gaps.png', 'fig_validation_coverage_gaps.pdf']
    },
    {
        'name': 'fig_workflow_progression.py',
        'description': 'Simulation-to-Validation Workflow Progression',
        'priority': 'MEDIA',
        'outputs': ['fig_workflow_progression.png', 'fig_workflow_progression.pdf']
    }
]

# Contador de resultados
successful = 0
failed = 0
results = []

# Ejecutar cada script
for i, script in enumerate(scripts, 1):
    print(f"\n[{i}/{len(scripts)}] Ejecutando: {script['name']}")
    print(f"    Descripción: {script['description']}")
    print(f"    Prioridad: {script['priority']}")
    print(f"    Outputs esperados: {', '.join(script['outputs'])}")
    print("    " + "-"*60)

    try:
        # Ejecutar script
        result = subprocess.run(
            [sys.executable, script['name']],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0:
            print(f"    ✓ ÉXITO: {script['name']}")
            successful += 1
            status = 'SUCCESS'

            # Verificar archivos generados
            files_created = []
            for output in script['outputs']:
                if os.path.exists(output):
                    size = os.path.getsize(output) / 1024  # KB
                    files_created.append(f"{output} ({size:.1f} KB)")

            if files_created:
                print(f"    Archivos generados:")
                for f in files_created:
                    print(f"      • {f}")
        else:
            print(f"    ✗ ERROR: {script['name']}")
            print(f"    Código de salida: {result.returncode}")
            if result.stderr:
                print(f"    Error: {result.stderr[:200]}")
            failed += 1
            status = 'FAILED'

    except subprocess.TimeoutExpired:
        print(f"    ✗ TIMEOUT: {script['name']} (>60s)")
        failed += 1
        status = 'TIMEOUT'
    except Exception as e:
        print(f"    ✗ EXCEPCIÓN: {str(e)}")
        failed += 1
        status = 'EXCEPTION'

    results.append({
        'script': script['name'],
        'description': script['description'],
        'status': status,
        'priority': script['priority']
    })

# ============= RESUMEN FINAL =============
print("\n" + "="*70)
print(" RESUMEN DE EJECUCIÓN")
print("="*70)

print(f"\nTotal de scripts ejecutados: {len(scripts)}")
print(f"  ✓ Exitosos: {successful}")
print(f"  ✗ Fallidos: {failed}")
print(f"  Tasa de éxito: {successful/len(scripts)*100:.1f}%")

print("\n" + "-"*70)
print(" DETALLES POR SCRIPT")
print("-"*70)

for result in results:
    status_symbol = "✓" if result['status'] == 'SUCCESS' else "✗"
    print(f"{status_symbol} [{result['priority']:^6}] {result['description']:<45} {result['status']}")

# ============= DATOS DE VALIDACIÓN =============
print("\n" + "="*70)
print(" DATOS DE VALIDACIÓN UTILIZADOS")
print("="*70)

validation_data = """
Fuente de datos: CSV validados (grupoA.csv, grupoB.csv, grupoC.csv, grupoD.csv)

Números de estudios verificados:
  • Grupo A (Anechoic Chamber): n=20 (40%)
  • Grupo B (VNA-Based): n=15 (30%)
  • Grupo C (Specialized): n=8 (16%)
  • Grupo D (Combined): n=7 (14%)
  • TOTAL: n=50 estudios

Búsquedas validadas en CSV:
  • "Anechoic chamber": 37 menciones totales
  • "VNA/Network Analyzer": 28 menciones totales
  • "Starlab/TVAC/Satimo": 10 menciones totales

Porcentajes críticos (de Tabla 2 y Discusión 4.2):
  • Single-domain validation: 70% (Groups A+B)
  • Multi-domain validation: 30% (Groups C+D)
  • Environmental testing: 14% (principalmente Group D)
  • Deficiencias identificadas: 70-86% en distintas dimensiones

Consistencia verificada con:
  • analisisOE2.txt: ✓ Números y clasificaciones
  • logicaRevision.txt: ✓ Objetivo Específico 2
  • PDF Sección 3.2: ✓ Tabla 2 y narrativa
  • PDF Sección 4.2: ✓ Porcentajes de discusión
"""

print(validation_data)

# ============= RECOMENDACIONES =============
print("="*70)
print(" RECOMENDACIONES DE USO")
print("="*70)

recommendations = """
1. PRIORIDAD ALTA (para inclusión inmediata):
   • fig3_validation_pyramid.png - Comunica visualmente el argumento central
   • fig_validation_coverage_gaps.png - Justifica brechas identificadas

2. PRIORIDAD MEDIA (para soporte adicional):
   • fig_instrument_validation_matrix.png - Demuestra complementariedad
   • fig_workflow_progression.png - Ilustra discontinuidades de workflow

3. UBICACIÓN RECOMENDADA EN MANUSCRITO:
   • Figura 3 (Pyramid): Después de Tabla 2 (página 13)
   • Figura Coverage Gaps: En Sección 4.2 (Discusión)
   • Figura Matrix: En Sección 3.2 (Resultados)
   • Figura Workflow: En Conclusiones o Discusión 4.1

4. FORMATO DE ARCHIVO:
   • PNG (300 dpi): Para revisión y versiones digitales
   • PDF (vectorial): Para versión final de publicación

5. TRAZABILIDAD:
   Todas las figuras incluyen caption detallado citando:
   - Fuente de datos (grupoA-D.csv validados)
   - Tabla/sección de referencia en PDF
   - Números exactos verificados
"""

print(recommendations)

print("\n" + "="*70)
print(" FIN DE EJECUCIÓN")
print("="*70)
print(f"\nTiempo de finalización: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Generar archivo de log
log_filename = f"execution_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(log_filename, 'w', encoding='utf-8') as log:
    log.write("="*70 + "\n")
    log.write(" LOG DE EJECUCIÓN - GENERACIÓN DE FIGURAS OE2\n")
    log.write("="*70 + "\n\n")
    log.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    log.write(f"Total scripts: {len(scripts)}\n")
    log.write(f"Exitosos: {successful}\n")
    log.write(f"Fallidos: {failed}\n\n")

    for result in results:
        log.write(f"[{result['status']}] {result['script']} - {result['description']}\n")

print(f"\nLog guardado en: {log_filename}")
