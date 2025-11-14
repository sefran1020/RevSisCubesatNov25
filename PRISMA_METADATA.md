# PRISMA 2020 Metadata - Systematic Review

## Revisión Sistemática: Diseño de Antenas Microstrip para CubeSat

### Información de Registro

**Protocolo**: PRISMA 2020
**Fecha de inicio**: Noviembre 2024
**Fecha de finalización**: Noviembre 2025
**Registro**: [Pendiente - PROSPERO o similar]

---

## 1. IDENTIFICACIÓN

### 1.1 Bases de Datos Consultadas

| Base de Datos | Registros Iniciales | Fecha de Búsqueda |
|---------------|---------------------|-------------------|
| Scopus | 441 | Noviembre 3, 2025 |
| EBSCOhost | 64 | Noviembre 3, 2025 |
| IEEE Xplore | 31 | Noviembre 3, 2025 |
| ScienceDirect | 15 | Noviembre 3, 2025 |
| **TOTAL** | **551** | |

### 1.2 Estrategia de Búsqueda

```
(TITLE-ABS-KEY(("microstrip antenna" OR "patch antenna" OR
"printed antenna" OR "microstrip patch"))
AND TITLE-ABS-KEY(("CubeSat" OR "small satellite" OR "nanosatellites")))
AND PUBYEAR > 1999 AND PUBYEAR < 2027
AND (LIMIT-TO(DOCTYPE,"ar") OR LIMIT-TO(DOCTYPE,"cp"))
```

**Conceptos principales**:
- Bloque 1 (Tecnología): microstrip antenna, patch antenna, printed antenna, microstrip patch
- Bloque 2 (Plataforma): CubeSat, small satellite, nanosatellites
- Operador: AND
- Período: 2000-2025
- Tipos de documento: Artículos (ar) y Actas de conferencia (cp)

---

## 2. SCREENING

### 2.1 Proceso de Eliminación de Duplicados

- **Registros iniciales**: 551
- **Duplicados eliminados**: 82
- **Método**: Zotero automático + revisión manual
- **Registros únicos para screening**: 469

### 2.2 Fase 1: Screening Título-Resumen

**Registros evaluados**: 469
**Registros excluidos**: 279

**Criterios de exclusión aplicados**:
- Falta de enfoque en antenas microstrip
- Referencia no significativa a CubeSat
- Ausencia de parámetros de comunicación
- Tecnologías no relacionadas (RFID, biomédico, infraestructura terrestre)

**Registros que pasan a Fase 2**: 190

### 2.3 Fase 2: Screening de Relevancia de Diseño

**Registros evaluados**: 190
**Registros excluidos**: 99

**Criterios de evaluación**:
- Contribución directa al diseño de antenas CubeSat
- Funciones de comunicación relevantes (downlink, uplink, ISL, telemetría)
- Contenido técnico sustantivo

**Registros que pasan a Fase 3**: 91

### 2.4 Fase 3: Recuperación de Texto Completo

**Registros para recuperar**: 91
**Registros recuperados**: 79
**Registros no accesibles**: 12

**Métodos de acceso**:
- Acceso institucional
- Repositorios abiertos
- Contacto con autores

---

## 3. ELEGIBILIDAD

### 3.1 Criterios de Inclusión

1. **Tecnología de antena**:
   - Microstrip / patch / printed / planar / metal-only

2. **Plataforma**:
   - Diseño/simulación/integración/prueba explícita para CubeSat/nanosatélites
   - Form factors: 1U-6U

3. **Evidencia empírica** (al menos uno):
   - Resultados de simulación EM (S₁₁, VSWR, relación axial, ganancia, eficiencia)
   - Validación experimental (fabricación, mediciones en cámara anecoica, pruebas de integración)
   - Análisis de integración estructural-térmica

4. **Tipo de publicación**:
   - Artículos de revista
   - Actas de conferencia

5. **Idioma y acceso**:
   - Texto completo disponible en inglés

### 3.2 Criterios de Exclusión

- **E1**: Menciones genéricas de satélites pequeños sin restricciones específicas de CubeSat
- **E2**: Antenas microstrip como componentes secundarios de otros subsistemas
- **E3**: Orientación primaria a aplicaciones terrestres (IoT, 5G, BLE, WiFi) sin adaptación a CubeSat
- **E4**: Ausencia de parámetros técnicos de diseño o métricas de rendimiento
- **E5**: Uso en experimentos de fenómenos físicos donde la comunicación es secundaria
- **E6**: Texto completo inaccesible

---

## 4. CORPUS FINAL

**Estudios incluidos**: 79

### 4.1 Distribución por Tipo de Documento

| Tipo | Cantidad | Porcentaje |
|------|----------|------------|
| Artículos de revista | ~45 | ~57% |
| Actas de conferencia | ~34 | ~43% |

### 4.2 Distribución por Año

| Período | Estudios |
|---------|----------|
| 2014-2017 | ~20 (Consolidación CP) |
| 2018-2021 | ~28 (Expansión dual-band) |
| 2022-2025 | ~31 (Integración avanzada) |

### 4.3 Cobertura de Frecuencias

- **UHF**: ~15 estudios
- **L-band**: ~8 estudios
- **S-band**: ~32 estudios (dominante)
- **C-band**: ~10 estudios
- **X-band**: ~8 estudios
- **Ka-band**: ~6 estudios

---

## 5. EXTRACCIÓN DE DATOS

### 5.1 Categorías Extraídas

1. **Metadatos bibliográficos**
   - Autores, año, journal/conferencia, DOI

2. **Configuración CubeSat**
   - Clasificación de unidades (1U-6U)
   - Estrategia de despliegue
   - Restricciones de integración

3. **Características de antena**
   - Geometría
   - Alimentación
   - Sustrato
   - Dimensiones

4. **Métricas de rendimiento**
   - S₁₁
   - Ancho de banda
   - Relación axial
   - Ganancia
   - Eficiencia
   - Patrones de radiación

5. **Enfoque de validación**
   - Herramientas de simulación (HFSS, CST, FEKO)
   - Detalles de fabricación
   - Entornos de medición

6. **Consideraciones de integración**
   - Estabilidad térmica
   - Restricciones mecánicas
   - Compatibilidad con paneles solares

### 5.2 Herramientas de Extracción

- Plantilla estructurada en Excel
- Validación cruzada por dos revisores
- Resolución de discrepancias por consenso

---

## 6. EVALUACIÓN DE CALIDAD

### 6.1 Dimensiones Evaluadas

1. **Claridad metodológica de diseño/simulación**
2. **Transparencia de parámetros de sustrato**
3. **Adecuación de validación electromagnética**
4. **Consistencia simulación-medición**
5. **Apropiación del modelado de integración CubeSat**

### 6.2 Niveles de Robustez

| Nivel | Criterios | Estudios |
|-------|-----------|----------|
| **Alta** | Acuerdo fuerte en ≥10 estudios con validación combinada simulación-experimental | ~30 |
| **Moderada** | Patrones consistentes en 4-9 estudios, impulsado por simulación con validación experimental limitada | ~35 |
| **Preliminar** | Diseños innovadores aislados con validación limitada | ~14 |

---

## 7. SÍNTESIS

### 7.1 Metodología de Síntesis

**Enfoque**: Convergente de evidencia de ingeniería

**Métodos aplicados**:
1. **Análisis temático**: Identificar patrones de flujo de trabajo dominantes
2. **Análisis de contenido**: Extraer métricas de rendimiento cuantitativas
3. **Síntesis narrativa**: Trazar evolución temporal de prácticas de diseño
4. **Síntesis crítica**: Exponer brechas sistemáticas entre caracterización de laboratorio y verificación de despliegue operacional

### 7.2 Análisis Inductivo Transversal

**Proceso único**:
1. Extracción temática de instrumentos de recolección de datos
2. Identificación de relaciones de alta robustez (≥10-18 estudios)
3. Mapeo de configuraciones de flujo de trabajo empíricas
4. Cuantificación de discontinuidades de integración
5. Formulación de objetivos basada en datos

### 7.3 Objetivos Emergentes

| Objetivo | Estudios | Robustez |
|----------|----------|----------|
| **OE1**: Simulación EM y optimización | 50 | Alta |
| **OE2**: Validación experimental | 50 | Alta |
| **OE3**: Integración de alimentación | 14 | Mixta |
| **OE4**: Fabricación y escalabilidad | 13 | Moderada |

---

## 8. HALLAZGOS PRINCIPALES

### 8.1 Configuraciones Dominantes

1. **Simulación-Validación** (60-70% cobertura)
   - HFSS (56%), CST (38%), FEKO (12%)
   - Acuerdo ±1.5 dB simulación-medición

2. **Validación Experimental** (distribuida)
   - Cámara anecoica: 40%
   - VNA: 30%
   - Especializado: 16%
   - Combinado: 14%

3. **Alimentación** (distribución)
   - Alimentación simple: 64%
   - Coaxial/probe: 57%
   - Redes complejas: 29%

4. **Fabricación** (distribución)
   - PCB convencional: 53.8%
   - Tecnologías avanzadas: 30.8%
   - Estrategias de bajo costo: 23.1%

### 8.2 Brechas Críticas Identificadas

| Brecha | Déficit | Estudios con Alta Madurez |
|--------|---------|---------------------------|
| **Interacción antena-plataforma** | 71% | 29% |
| **Validación térmica** | 86% | 14% |
| **Integración mecánica** | 79% | 21% |
| **Alimentación-sistema** | 71% | 29% |
| **Opacidad de hiperparámetros** | 68% | 32% |
| **Validación cruzada de plataformas** | >92% | <8% |

---

## 9. LIMITACIONES

### 9.1 Limitaciones Metodológicas

1. **Textos completos inaccesibles**: 12 estudios (13.2% de elegibles)
   - Potencial sesgo de selección

2. **Restricción de idioma**: Solo inglés
   - Exclusión sistemática de programas no anglófonos

3. **Enfoque en revisión por pares**:
   - Omite protocolos de industria propietaria
   - Omite metodologías de constelaciones comerciales

4. **Objetivos derivados inductivamente**:
   - Reflejan prácticas de documentación más que flujos de trabajo reales
   - Integración comprehensiva puede ser implementada pero selectivamente reportada

---

## 10. TRANSPARENCIA Y REPRODUCIBILIDAD

### 10.1 Datos Disponibles

✅ Estrategia de búsqueda completa
✅ Listas de inclusión/exclusión por fase
✅ Datos extraídos en formato CSV/Excel
✅ Criterios de categorización documentados
✅ Análisis cuantitativo reproducible
✅ Artículos incluidos en PDF

### 10.2 Materiales Suplementarios

- `recoleccion/`: Datos de búsqueda brutos
- `screening/`: Decisiones de inclusión/exclusión
- `OE[1-4]/`: Datos categorizados por objetivo
- `objetive-dataDriven/`: Análisis inductivo transversal
- `articulosPDF/`: Corpus completo de 79 estudios

---

## 11. INFORMACIÓN DE CONTACTO

**Investigador Principal**: [Nombre]
**Institución**: [Institución]
**Email**: [email@institution.edu]
**ORCID**: [0000-0000-0000-0000]

**Repositorio**: https://github.com/[username]/[repository-name]
**DOI**: [Pendiente]

---

## 12. ACTUALIZACIONES

| Fecha | Versión | Cambios |
|-------|---------|---------|
| 2025-11-13 | 1.0 | Versión inicial del protocolo PRISMA |

---

**Nota**: Este documento sigue las directrices PRISMA 2020 para reportar revisiones sistemáticas.
**Referencia**: Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ 2021;372:n71. doi: 10.1136/bmj.n71
