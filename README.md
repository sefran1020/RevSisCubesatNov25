# Revisión Sistemática: Diseño de Antenas Microstrip para Plataformas CubeSat

[![DOI](https://img.shields.io/badge/DOI-pending-blue)]()
[![License](https://img.shields.io/badge/License-CC--BY--4.0-green)](LICENSE)
[![PRISMA](https://img.shields.io/badge/Protocol-PRISMA%202020-orange)](PRISMA_METADATA.md)
[![Zenodo](https://img.shields.io/badge/Zenodo-Guide-informational)](ZENODO_GUIDE.md)

> **Bridging Component Optimization and System Integration: Systematic Evidence of Workflow Discontinuities in Microstrip Antenna Design for Small Satellite Platforms**

---

## 🎯 Sobre este Repositorio

Este repositorio contiene **todos los datos, análisis y documentación** de una revisión sistemática exhaustiva que examina configuraciones empíricas de flujos de trabajo en el diseño de antenas CubeSat.

### Alcance de la Revisión
- **551 registros** iniciales de 4 bases de datos
- **79 estudios** finales incluidos (PRISMA 2020)
- **25 años** de investigación (2000-2025)
- **4 objetivos específicos** con análisis inductivo

### Metodología Única
Análisis de configuraciones de flujo de trabajo empíricas examinando relaciones entre:
- 🔬 Simulación electromagnética (HFSS, CST, FEKO)
- 🧪 Validación experimental (cámaras anecoicas, VNA, TVAC)
- 📡 Integración de elementos de alimentación
- 🏭 Procesos de fabricación y escalabilidad

![Diagrama PRISMA](prismaRevSisCubesat.png)
*Figura: Diagrama de flujo PRISMA 2020 mostrando el proceso de selección de estudios*

---

## 📊 Hallazgos Principales

| Área | Hallazgo Clave | Métrica |
|------|----------------|---------|
| **Simulación EM** | Dominancia HFSS/CST/FEKO | 85% acuerdo ±1.5 dB |
| **Validación** | Predominio cámara anecoica/VNA | 70% cobertura |
| **Brecha Crítica 1** | Integración alimentación-sistema | **71% déficit** |
| **Brecha Crítica 2** | Validación térmica | **86% déficit** |
| **Brecha Crítica 3** | Integración mecánica | **79% déficit** |

### 🚨 Conclusión Principal
> Extraordinaria sofisticación electromagnética coexiste con profundas deficiencias de integración en validación térmica, integración mecánica y modelado de interacción con plataforma.

---

## 📋 Contenido

### Artículo Principal
- **`articulo2a.pdf`**: Artículo científico completo resultante de la revisión sistemática

### Estructura de Datos

#### 📁 `recoleccion/`
Datos de la fase de recolección de búsqueda en bases de datos:
- `baseDatos.csv`: Base de datos consolidada de todos los registros
- `consolidado.xlsx`: Archivo Excel con datos integrados
- `ebsco.csv`: Registros de EBSCOhost (64 registros)
- `IEEE.csv`: Registros de IEEE Xplore (31 registros)
- `scopus.csv`: Registros de Scopus (441 registros)
- `sd.csv`: Registros de ScienceDirect (15 registros)
- `inFase1.xlsx`: Resultados procesados de fase 1

#### 📁 `screening/`
Datos del proceso de cribado PRISMA:
- `baseDatos.csv`: Base completa para screening
- `incluidos.xlsx`: Estudios incluidos tras el cribado (79 estudios finales)
- `outFase1.csv`: Estudios excluidos en fase 1
- `outFase2.csv`: Estudios excluidos en fase 2

#### 📁 `OE1/` - Objetivo Específico 1
**Simulación Electromagnética y Optimización de Diseño**
- `analisisOE1.txt`: Análisis detallado del objetivo 1
- `grupoA.csv`: Estudios con HFSS/CST/FEKO
- `grupoB.csv`: Estudios con optimización paramétrica
- `grupoC.csv`: Estudios con algoritmos genéticos/PSO
- `logicaRevision.txt`: Lógica de categorización

#### 📁 `OE2/` - Objetivo Específico 2
**Validación Experimental e Instrumentación**
- `analisisOE2.txt`: Análisis de instrumentos y protocolos de validación
- `grupoA.csv`: Cámaras anecoicas y VNA
- `grupoB.csv`: Sistemas especializados (Starlab, TVAC)
- `grupoC.csv`: Metodologías combinadas
- `grupoD.csv`: Validación multi-dominio
- `logicaRevision.txt`: Criterios de clasificación

#### 📁 `OE3/` - Objetivo Específico 3
**Integración de Elementos de Alimentación**
- `analisisOE3.txt`: Análisis de discontinuidades de integración
- `grupoA.csv`: Configuraciones de alimentación simple
- `grupoB.csv`: Redes de alimentación complejas
- `grupoC.csv`: Integración con CubeSat
- `grupoD.csv`: Validación térmica-mecánica
- `logicaRevision.txt`: Matriz de madurez

#### 📁 `OE4/` - Objetivo Específico 4
**Fabricación y Escalabilidad**
- `analisisOE4.txt`: Análisis de procesos de fabricación
- `grupoA.csv`: Prototipado PCB convencional
- `grupoB.csv`: Tecnologías avanzadas (3D printing, stacked)
- `grupoC.csv`: Estrategias de bajo costo
- `logicaRevision.txt`: Criterios de evaluación

#### 📁 `objetive-dataDriven/`
Análisis inductivo transversal:
- `estudiosObjetivos.xlsx`: Mapeo de estudios a objetivos
- `fase3_analisis_transversal_inductiv.txt`: Análisis inductivo de patrones
- `fase4_objetivos_data_driven.txt`: Formulación de objetivos basada en datos
- `logicaRevision.txt`: Metodología inductiva

#### 📁 `articulosPDF/`
Colección de 79 artículos incluidos en la revisión (formato PDF)

### Archivos de Datos Generales
- **`nuevoCubeSat.ris`**: Referencias bibliográficas en formato RIS (1.37 MB)

## 🔬 Metodología

### Protocolo PRISMA 2020
La revisión sigue estrictamente las directrices PRISMA 2020:
- **Búsqueda**: 4 bases de datos (Scopus, EBSCOhost, ScienceDirect, IEEE Xplore)
- **Período**: Enero 2000 - Noviembre 2025
- **Registros iniciales**: 551
- **Registros únicos**: 469 (tras eliminación de duplicados)
- **Estudios incluidos**: 79

### Criterios de Inclusión
1. Tecnologías de antena microstrip/patch/printed/planar
2. Diseño explícito para CubeSat/nanosatélites (1U-6U)
3. Evidencia empírica (simulación EM, validación experimental, análisis térmico-estructural)
4. Artículos de revista o actas de conferencia
5. Texto completo en inglés

### Análisis Inductivo
Metodología única de configuraciones de flujo de trabajo empíricas:
- Extracción temática de instrumentos y herramientas
- Identificación de relaciones de alto robustez
- Formulación de objetivos basada en datos
- Cuantificación de brechas de integración

## 📊 Resultados Principales

### Hallazgos Clave
- **Simulación**: HFSS (56%), CST (38%), FEKO (12%) - acuerdo simulación-medición ±1.5 dB
- **Validación**: 40% cámaras anecoicas, 30% VNA, solo 14% multi-dominio
- **Brechas Críticas**:
  - 71% brecha alimentación-sistema
  - 86% deficiencia validación térmica
  - 79% inadecuación integración mecánica
  - 29% evaluación interacción antena-plataforma

### Configuraciones Dominantes
1. **Simulación-Validación** (60-70% cobertura)
2. **Prototipado-Fabricación** (5-10% cobertura)
3. **Alimentación-Integración** (10-15% cobertura)

## 📈 Cómo Usar este Repositorio

### Para Investigadores
1. **Replicar análisis**: Utilice los archivos CSV en cada carpeta OE
2. **Extender revisión**: Base de datos en `recoleccion/baseDatos.csv`
3. **Validar hallazgos**: Compare con `analisisOE[1-4].txt`

### Para Diseñadores de CubeSat
1. Consulte las configuraciones de flujo de trabajo en cada objetivo específico
2. Identifique mejores prácticas por categoría (simulación, validación, fabricación)
3. Evalúe brechas de integración relevantes para su misión

### Para Revisores y Editores
- Diagrama PRISMA disponible en el artículo
- Criterios de inclusión/exclusión documentados
- Evaluación de calidad por dimensión

## 🔄 Transparencia y Reproducibilidad

### Trazabilidad Completa
- Todas las búsquedas documentadas por base de datos
- Proceso de screening en múltiples fases
- Criterios de categorización explícitos en `logicaRevision.txt`
- Análisis cuantitativo reproducible desde CSV

### Control de Versiones
Este repositorio mantiene:
- Versión completa de datos de búsqueda
- Histórico de decisiones de inclusión/exclusión
- Evolución de categorías inductivas
- Actualizaciones de análisis

## 📝 Citación

Si utiliza datos o hallazgos de esta revisión, por favor cite:

```bibtex
@article{cubesat_systematic_review_2025,
  title={Bridging Component Optimization and System Integration: Systematic Evidence of Workflow Discontinuities in Microstrip Antenna Design for Small Satellite Platforms},
  author={[Autores]},
  journal={[Revista]},
  year={2025},
  doi={[DOI]}
}
```

## 📄 Licencia

- **Datos**: CC BY 4.0 - Libre uso con atribución
- **Código de análisis**: MIT License (si aplica)
- **Artículo**: Sujeto a derechos de publicación

## 🤝 Contribuciones

Este es un repositorio de datos de investigación. Para:
- **Errores en datos**: Abrir un issue
- **Sugerencias de análisis**: Discussions
- **Extensiones**: Fork y pull request

## 📧 Contacto

Para preguntas sobre la revisión sistemática:
- Crear un issue en este repositorio
- Contactar a los autores (ver artículo)

## 🔗 Enlaces Relacionados

- Directrices PRISMA 2020: http://www.prisma-statement.org/
- Datos suplementarios: [si aplica]
- Pre-registro: [si aplica]

---

## 📂 Organización del Repositorio

### Vista General

```
RevSisCubesatNov25/
│
├── 📄 Documentación Principal
│   ├── README.md                          ⭐ Empieza aquí
│   ├── PRISMA_METADATA.md                 📋 Protocolo PRISMA completo
│   ├── ZENODO_GUIDE.md                    🚀 Guía para publicar en Zenodo
│   ├── CONTRIBUTING.md                    🤝 Cómo contribuir
│   ├── SETUP_SUMMARY.md                   📝 Resumen de setup
│   ├── LICENSE                            ⚖️  CC BY 4.0
│   ├── CITATION.cff                       📖 Formato de citación
│   ├── .gitignore                         🚫 Control de archivos Git
│   └── .zenodo.json                       🏷️  Metadata para Zenodo
│
├── 📊 Datos de la Revisión
│   ├── articulo2a.pdf                     📄 Artículo resultante (618 KB)
│   ├── nuevoCubeSat.ris                   📚 551 referencias (1.37 MB)
│   └── prismaRevSisCubesat.png            🖼️  Diagrama PRISMA
│
├── 📁 recoleccion/                        🔍 FASE 1: Búsqueda en Bases de Datos
│   ├── baseDatos.csv                      📊 Consolidado (551 registros)
│   ├── consolidado.xlsx                   📊 Excel integrado
│   ├── scopus.csv                         🔵 Scopus (441 registros)
│   ├── ebsco.csv                          🟢 EBSCOhost (64 registros)
│   ├── IEEE.csv                           🔴 IEEE Xplore (31 registros)
│   ├── sd.csv                             🟠 ScienceDirect (15 registros)
│   └── inFase1.xlsx                       📋 Procesados fase 1
│
├── 📁 screening/                          ✅ FASE 2-4: Proceso de Cribado PRISMA
│   ├── baseDatos.csv                      📊 Base para screening
│   ├── incluidos.xlsx                     ✅ 79 estudios finales
│   ├── outFase1.csv                       ❌ Excluidos fase 1 (279)
│   └── outFase2.csv                       ❌ Excluidos fase 2 (99)
│
├── 📁 OE1/                                🎯 Objetivo Específico 1
│   │                                      📡 Simulación Electromagnética
│   ├── analisisOE1.txt                    📝 Análisis detallado (50 estudios)
│   ├── grupoA.csv                         🔷 HFSS/CST/FEKO
│   ├── grupoB.csv                         🔷 Optimización paramétrica
│   ├── grupoC.csv                         🔷 Algoritmos GA/PSO
│   └── logicaRevision.txt                 📖 Lógica de categorización
│
├── 📁 OE2/                                🎯 Objetivo Específico 2
│   │                                      🧪 Validación Experimental
│   ├── analisisOE2.txt                    📝 Análisis (50 estudios)
│   ├── grupoA.csv                         🔶 Cámara anecoica + VNA
│   ├── grupoB.csv                         🔶 Sistemas especializados
│   ├── grupoC.csv                         🔶 Metodologías combinadas
│   ├── grupoD.csv                         🔶 Validación multi-dominio
│   └── logicaRevision.txt                 📖 Criterios de clasificación
│
├── 📁 OE3/                                🎯 Objetivo Específico 3
│   │                                      🔌 Integración de Alimentación
│   ├── analisisOE3.txt                    📝 Análisis (14 estudios)
│   ├── grupoA.csv                         🔸 Alimentación simple
│   ├── grupoB.csv                         🔸 Redes complejas
│   ├── grupoC.csv                         🔸 Integración CubeSat
│   ├── grupoD.csv                         🔸 Validación térmica-mecánica
│   └── logicaRevision.txt                 📖 Matriz de madurez
│
├── 📁 OE4/                                🎯 Objetivo Específico 4
│   │                                      🏭 Fabricación y Escalabilidad
│   ├── analisisOE4.txt                    📝 Análisis (13 estudios)
│   ├── grupoA.csv                         🔹 Prototipado PCB
│   ├── grupoB.csv                         🔹 Tecnologías avanzadas
│   ├── grupoC.csv                         🔹 Estrategias bajo costo
│   └── logicaRevision.txt                 📖 Criterios de evaluación
│
├── 📁 objetive-dataDriven/                🧠 Análisis Inductivo Transversal
│   ├── estudiosObjetivos.xlsx             📊 Mapeo estudios→objetivos
│   ├── fase3_analisis_transversal_inductiv.txt  📊 Análisis de patrones
│   ├── fase4_objetivos_data_driven.txt    📊 Formulación de objetivos
│   └── logicaRevision.txt                 📖 Metodología inductiva
│
└── 📁 articulosPDF/                       📚 Corpus Completo
    └── [79 artículos en PDF]              📄 Estudios incluidos
```

### 🗺️ Mapa de Navegación

| Si quieres... | Ve a... |
|---------------|---------|
| **Empezar aquí** | `README.md` (este archivo) |
| **Ver metodología PRISMA** | `PRISMA_METADATA.md` |
| **Publicar en Zenodo** | `ZENODO_GUIDE.md` |
| **Citar este trabajo** | `CITATION.cff` |
| **Contribuir** | `CONTRIBUTING.md` |
| **Ver datos de búsqueda** | `recoleccion/baseDatos.csv` |
| **Ver estudios incluidos** | `screening/incluidos.xlsx` |
| **Análisis de simulación** | `OE1/analisisOE1.txt` |
| **Análisis de validación** | `OE2/analisisOE2.txt` |
| **Análisis de alimentación** | `OE3/analisisOE3.txt` |
| **Análisis de fabricación** | `OE4/analisisOE4.txt` |
| **Análisis inductivo** | `objetive-dataDriven/` |

### 📈 Estadísticas del Repositorio

| Métrica | Valor |
|---------|-------|
| **Archivos de documentación** | 9 archivos |
| **Archivos de datos (CSV/Excel)** | 23 archivos |
| **Archivos de análisis (TXT)** | 11 archivos |
| **PDFs incluidos** | 79 artículos |
| **Tamaño total** | ~210 MB |
| **Estudios analizados** | 79 estudios |
| **Registros procesados** | 551 registros |
| **Período cubierto** | 2000-2025 (25 años) |

---

**Última actualización**: Noviembre 2025
**Versión**: 1.0
**Estado**: Publicación pendiente
