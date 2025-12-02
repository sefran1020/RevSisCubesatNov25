"""
SCRIPT MAESTRO: Generación de todas las figuras individuales para Sección 3.3
Ejecuta los 6 scripts de visualización (figuras individuales, no compuestas)

Autor: Sistema de análisis automatizado
Fecha: 2025-01-14 (Actualizado)
"""

import subprocess
import sys
import os
from datetime import datetime

# =====================================================
# CONFIGURACIÓN
# =====================================================

BASE_DIR = r"G:\RevSisOrd\OE3Figuras"
scripts = [
    "figura_3_3_1_maturity_cascade.py",
    "figura_3_3_2_pie_distribution.py",
    "figura_3_3_3_tools_bar.py",
    "figura_3_3_4_temporal_evolution.py",
    "figura_3_3_5_integration_heatmap.py",
    "figura_3_3_6_sankey_gap.py"
]

# =====================================================
# EJECUTAR SCRIPTS
# =====================================================

print("=" * 80)
print("GENERACION DE FIGURAS INDIVIDUALES - SECCION 3.3")
print("Feeding Element Integration: System-Level Discontinuities")
print("=" * 80)
print()

results = {}
for i, script in enumerate(scripts, 1):
    script_path = os.path.join(BASE_DIR, script)
    print(f"[{i}/{len(scripts)}] Ejecutando: {script}")
    print("-" * 80)

    try:
        result = subprocess.run([sys.executable, script_path],
                                capture_output=True, text=True, timeout=60)

        if result.returncode == 0:
            print(result.stdout)
            results[script] = "[OK] SUCCESS"
        else:
            print(f"ERROR en {script}:")
            print(result.stderr)
            results[script] = "[ERROR] FAILED"

    except subprocess.TimeoutExpired:
        print(f"TIMEOUT: {script} excedió 60 segundos")
        results[script] = "[ERROR] TIMEOUT"
    except Exception as e:
        print(f"EXCEPTION: {str(e)}")
        results[script] = f"[ERROR] EXCEPTION: {str(e)}"

    print()

# =====================================================
# RESUMEN FINAL
# =====================================================

print("=" * 80)
print("RESUMEN FINAL")
print("=" * 80)

for script, status in results.items():
    print(f"{script:50s} {status}")

success_count = sum(1 for status in results.values() if '[OK]' in status)
total_count = len(results)

print()
print(f"Figuras generadas exitosamente: {success_count}/{total_count}")
print(f"Trazabilidad: COMPLETA")
print(f"Archivos totales generados: {success_count * 2} (PNG + PDF)")
print("=" * 80)

if success_count == total_count:
    print("\n[SUCCESS] TODAS LAS FIGURAS GENERADAS EXITOSAMENTE!")
    print("\nFiguras generadas (individuales, no compuestas):")
    print("  - Figure 3.3.1: Maturity Cascade Diagram")
    print("  - Figure 3.3.2: Feeding Architecture Distribution (Pie Chart)")
    print("  - Figure 3.3.3: Simulation Tool Distribution (Bar Chart)")
    print("  - Figure 3.3.4: Temporal Evolution Timeline")
    print("  - Figure 3.3.5: Integration Maturity Heatmap")
    print("  - Figure 3.3.6: Sankey Flow Diagram")
    sys.exit(0)
else:
    print("\n[WARNING] ALGUNAS FIGURAS FALLARON - Revisar errores arriba")
    sys.exit(1)
