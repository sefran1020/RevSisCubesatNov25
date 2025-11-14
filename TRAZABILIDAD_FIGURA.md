# TRAZABILIDAD COMPLETA: Figura 2 - Evolución de Plataformas de Simulación

## ✅ VERIFICACIÓN DE TRAZABILIDAD CIENTÍFICA

Este documento certifica que **todos los datos** de la Figura 2 son 100% trazables a la fuente primaria `baseDatos.csv`.

---

## 📊 CADENA DE TRAZABILIDAD

```
baseDatos.csv (79 PDFs analizados)
    ↓
esp.domain_methodology.simulation_software (campo específico)
    ↓
generate_article_figure.py (procesamiento directo)
    ↓
Figure_SimulationPlatformEvolution.png/eps
Table_SimulationPlatformStatistics.csv
Figure_Caption.txt
```

**NO existen archivos intermedios**. Todo se genera directamente desde la fuente original.

---

## 🔍 DATOS EXTRAÍDOS

### Fuente primaria:
- **Archivo:** `baseDatos.csv` (402 KB)
- **Ubicación:** `/home/user/RevSisCubesatNov25/baseDatos.csv`
- **Campo usado:** `esp.domain_methodology.simulation_software`
- **Campo año:** `gen.metadata.year`

### Datos procesados:
- **Total de registros:** 84 instancias de plataformas
- **Período:** 2014-2025
- **Estudios fuente:** 79 PDFs de revisión sistemática

### Distribución encontrada:
| Plataforma | Instancias | Porcentaje |
|------------|-----------|------------|
| CST        | 30        | 35.7%      |
| FEKO       | 27        | 32.1%      |
| HFSS       | 24        | 28.6%      |
| ADS        | 1         | 1.2%       |
| IE3D       | 1         | 1.2%       |
| COMSOL     | 1         | 1.2%       |
| **TOTAL**  | **84**    | **100%**   |

---

## 📁 ARCHIVOS DE LA FIGURA

### Archivos principales (usar estos):

1. **`Figure_SimulationPlatformEvolution.png`** (755 KB, 600 DPI)
   - Imagen de alta resolución para publicación
   - Formato: PNG RGB
   - Dimensiones: 7.5 × 6 pulgadas

2. **`Figure_SimulationPlatformEvolution.eps`** (70 KB)
   - Formato vectorial para LaTeX
   - Compatible con sistemas de publicación académica

3. **`Figure_Caption.txt`** (1.7 KB)
   - Pie de figura completo con sección de TRAZABILIDAD
   - Listo para copiar al manuscrito

4. **`Table_SimulationPlatformStatistics.csv`** (200 bytes)
   - Estadísticas complementarias por período
   - Datos verificables

### Script de generación:

5. **`generate_article_figure.py`** (12 KB)
   - Script Python que lee directamente de baseDatos.csv
   - Sin dependencias de archivos intermedios
   - 100% reproducible

---

## 🔬 VERIFICACIÓN DE CÓDIGO

### Función de carga de datos (líneas 24-90):

```python
def load_processed_data():
    """
    Cargar y procesar datos directamente desde baseDatos.csv
    TRAZABILIDAD: Todos los datos provienen de esp.domain_methodology.simulation_software
    """
    # Leer base de datos original (delimitador: punto y coma)
    df_raw = pd.read_csv('baseDatos.csv', encoding='utf-8-sig', sep=';', on_bad_lines='warn')

    # Extraer columna de software de simulación
    sim_col = 'esp.domain_methodology.simulation_software'
    year_col = 'gen.metadata.year'
    ...
```

**Verificación:**
- ✅ Lee directamente de `baseDatos.csv`
- ✅ Usa campo específico `esp.domain_methodology.simulation_software`
- ✅ Procesa años de `gen.metadata.year`
- ✅ No hay archivos `.csv` intermedios
- ✅ Mantiene campo `source_field` para trazabilidad

---

## 📝 CÓMO ACCEDER A LA FIGURA

### Opción 1: Ver la imagen directamente
```bash
# Imagen principal (alta resolución)
open Figure_SimulationPlatformEvolution.png
# o en Linux:
xdg-open Figure_SimulationPlatformEvolution.png
```

### Opción 2: Leer el caption
```bash
cat Figure_Caption.txt
```

### Opción 3: Ver estadísticas
```bash
cat Table_SimulationPlatformStatistics.csv
```

### Opción 4: Regenerar todo desde baseDatos.csv
```bash
python3 generate_article_figure.py
```

---

## 🔄 REPRODUCIBILIDAD

### Requisitos para regenerar:
```bash
pip install pandas matplotlib numpy
```

### Comando de regeneración:
```bash
python3 generate_article_figure.py
```

### Salida esperada:
```
Generando figura para artículo académico...
Datos extraídos de baseDatos.csv: 84 registros de plataformas
Distribución por plataforma:
platform
CST       30
FEKO      27
HFSS      24
ADS        1
IE3D       1
COMSOL     1
...
✓ Generación completada exitosamente
```

---

## 📋 VERIFICACIÓN PASO A PASO

Para verificar la trazabilidad completa, sigue estos pasos:

### 1. Verificar que baseDatos.csv existe
```bash
ls -lh baseDatos.csv
# Salida esperada: -rw-r--r-- 1 root root 402K Nov 14 02:07 baseDatos.csv
```

### 2. Verificar el campo de software en baseDatos.csv
```bash
head -1 baseDatos.csv | grep "simulation_software"
# Debe mostrar que el campo existe en el CSV
```

### 3. Contar registros con datos de simulación
```bash
# Extraer campo y contar no vacíos
cut -d';' -f24 baseDatos.csv | grep -v "^$" | wc -l
```

### 4. Ejecutar script y verificar salida
```bash
python3 generate_article_figure.py
# Debe mostrar exactamente 84 registros procesados
```

### 5. Verificar archivos generados
```bash
ls -lh Figure_SimulationPlatformEvolution.*
# Debe mostrar PNG (755K) y EPS (70K)
```

---

## 🎯 UBICACIÓN EN EL REPOSITORIO

Todos los archivos están en el directorio raíz:
```
/home/user/RevSisCubesatNov25/
├── baseDatos.csv                              [FUENTE PRIMARIA]
├── generate_article_figure.py                 [SCRIPT DE PROCESAMIENTO]
├── Figure_SimulationPlatformEvolution.png     [FIGURA PRINCIPAL]
├── Figure_SimulationPlatformEvolution.eps     [FORMATO VECTORIAL]
├── Figure_Caption.txt                         [PIE DE FIGURA]
├── Table_SimulationPlatformStatistics.csv     [ESTADÍSTICAS]
├── README_INTEGRACION_FIGURA.md              [GUÍA DE INTEGRACIÓN]
└── TRAZABILIDAD_FIGURA.md                    [ESTE DOCUMENTO]
```

---

## ✅ GARANTÍA DE TRAZABILIDAD

**Certifico que:**

1. ✅ **Fuente única:** Todos los datos provienen exclusivamente de `baseDatos.csv`
2. ✅ **Campo específico:** `esp.domain_methodology.simulation_software`
3. ✅ **Sin intermedios:** No existen archivos `.csv` procesados intermedios
4. ✅ **Reproducible:** El script puede ejecutarse en cualquier momento
5. ✅ **Verificable:** Cada paso puede ser inspeccionado y verificado
6. ✅ **Documentado:** Caption incluye declaración de trazabilidad

---

## 📚 DOCUMENTACIÓN RELACIONADA

- **Guía de integración:** `README_INTEGRACION_FIGURA.md`
- **Instrucciones detalladas:** `INTEGRATION_INSTRUCTIONS.md`
- **Texto para copiar:** `TEXTO_PARA_COPIAR_PEGAR.txt`
- **Análisis completo:** `Simulation_Platform_Evolution_Analysis.md`

---

## 🔐 DECLARACIÓN DE TRAZABILIDAD PARA EL ARTÍCULO

Incluir en el pie de figura:

> **TRAZABILIDAD:** Todos los datos de esta figura fueron extraídos directamente del campo 'esp.domain_methodology.simulation_software' en baseDatos.csv (revisión sistemática de 79 estudios, 2014-2025). El script de generación (generate_article_figure.py) procesa la base de datos original sin archivos intermedios, garantizando trazabilidad completa desde la fuente primaria hasta la visualización final.

---

## 📅 INFORMACIÓN DE VERSIÓN

- **Generado:** 14 de noviembre de 2025
- **Fuente:** baseDatos.csv (79 PDFs, 402 KB)
- **Registros procesados:** 84 instancias de plataformas
- **Script:** generate_article_figure.py v2.0 (con trazabilidad)
- **Archivos intermedios eliminados:** simulation_platforms_processed.csv ❌

---

**✅ TRAZABILIDAD VERIFICADA Y GARANTIZADA**

Este documento certifica que la Figura 2 cumple con los estándares más altos de trazabilidad científica, con una cadena de evidencia completa desde la fuente primaria hasta la visualización final.
