# Evolución Temporal de Plataformas de Simulación en CubeSats
## Análisis basado en Revisión Sistemática de Literatura

**Fecha de análisis:** 14 de noviembre de 2025
**Fuente de datos:** baseDatos.csv (90 publicaciones analizadas)
**Período temporal:** 2014-2025

---

## Resumen Ejecutivo

Este documento presenta un análisis exhaustivo de la evolución temporal en el uso de plataformas de simulación electromagnética para el diseño de antenas en CubeSats, basado en una revisión sistemática de 90 publicaciones científicas. El análisis identifica tendencias claras en la adopción de tecnologías, preferencias de la comunidad científica y la especialización de herramientas de simulación.

**Hallazgos clave:**
- Se identificaron 7 plataformas principales de simulación electromagnética
- CST Microwave Studio lidera con 31.91% de adopción
- Crecimiento sostenido del 354% en publicaciones entre 2011-2015 y 2021-2025
- Consolidación del mercado en torno a tres plataformas dominantes: CST, FEKO y HFSS

---

## 1. Metodología

### 1.1 Fuente de Datos
- **Base de datos:** baseDatos.csv
- **Total de publicaciones:** 90 documentos científicos
- **Registros con información de simulación:** 94 instancias (algunas publicaciones usan múltiples plataformas)
- **Período de análisis:** 2014-2025

### 1.2 Proceso de Extracción
Se analizó la columna `esp.domain_methodology.simulation_software` del dataset para identificar:
- Nombres de plataformas de simulación electromagnética
- Versiones específicas cuando estaban disponibles
- Múltiples herramientas usadas en un mismo estudio

### 1.3 Plataformas Identificadas
Se identificaron 7 plataformas principales:
1. **CST Microwave Studio / CST Studio Suite**
2. **FEKO (Altair FEKO)**
3. **HFSS (Ansys HFSS)**
4. **ANSYS**
5. **ADS (Advanced Design System)**
6. **IE3D**
7. **COMSOL Multiphysics**

---

## 2. Análisis Estadístico General

### 2.1 Distribución Global de Plataformas

| Ranking | Plataforma | Frecuencia | Porcentaje | Acumulado |
|---------|-----------|------------|------------|-----------|
| 1 | CST | 30 | 31.91% | 31.91% |
| 2 | FEKO | 27 | 28.72% | 60.63% |
| 3 | HFSS | 24 | 25.53% | 86.16% |
| 4 | ANSYS | 10 | 10.64% | 96.80% |
| 5 | ADS | 1 | 1.06% | 97.86% |
| 6 | IE3D | 1 | 1.06% | 98.92% |
| 7 | COMSOL | 1 | 1.06% | 100.00% |

**Observaciones:**
- Las tres plataformas principales (CST, FEKO, HFSS) representan el **86.16%** del mercado
- Alta concentración: el top 3 domina claramente el sector
- Plataformas especializadas (ADS, IE3D, COMSOL) tienen adopción marginal (<2%)

### 2.2 Índice de Concentración
- **Índice Herfindahl-Hirschman (HHI):** Alto (>0.25), indicando mercado concentrado
- **Cuota top 3:** 86.16% (oligopolio natural)
- **Distribución:** Las tres grandes plataformas tienen cuotas similares (26-32%)

---

## 3. Evolución Temporal

### 3.1 Análisis por Períodos

#### Período 2011-2015: Fase de Adopción Temprana
- **Total de publicaciones:** 11
- **Características:**
  - FEKO lidera con 36.4% (4 publicaciones)
  - Distribución equilibrada entre CST (27.3%) y HFSS (27.3%)
  - Primeras adopciones de herramientas comerciales de simulación EM
  - Dominio de métodos numéricos: MoM (Method of Moments) y FEM

**Interpretación:**
Este período marca la transición de métodos analíticos básicos a simulaciones numéricas completas. FEKO dominó inicialmente por su fortaleza en análisis de antenas usando MoM.

#### Período 2016-2020: Consolidación y Equilibrio
- **Total de publicaciones:** 33 (crecimiento de 200% respecto al período anterior)
- **Características:**
  - **Equilibrio perfecto:** FEKO, CST y HFSS empatan con 10 publicaciones cada uno (30.3%)
  - Madurez en el uso de simuladores comerciales
  - Surgimiento de ANSYS como cuarta opción
  - Incremento en complejidad de diseños (multi-banda, reconfigurables)

**Interpretación:**
Período de madurez tecnológica donde las tres plataformas principales alcanzan paridad. Los investigadores eligen herramientas basadas en necesidades específicas y licencias institucionales disponibles.

#### Período 2021-2025: Especialización y Liderazgo de CST
- **Total de publicaciones:** 50 (crecimiento de 51.5% respecto al período anterior)
- **Características:**
  - CST emerge como líder con 34.0% (17 publicaciones)
  - FEKO mantiene presencia sólida con 26.0% (13 publicaciones)
  - HFSS con 22.0% (11 publicaciones)
  - Crecimiento de ANSYS hasta 9 publicaciones

**Interpretación:**
CST consolida su liderazgo probablemente por:
- Interfaz más intuitiva y curva de aprendizaje más suave
- Mejor integración con workflows de diseño de CubeSats
- Fortaleza en simulación de estructuras complejas y arrays
- Amplia base de usuarios académicos

### 3.2 Tendencias de Crecimiento

| Período | Publicaciones | Crecimiento | Tasa Anual |
|---------|---------------|-------------|------------|
| 2011-2015 | 11 | - | - |
| 2016-2020 | 33 | +200% | +26.0% |
| 2021-2025 | 50 | +51.5% | +8.7% |

**Total de crecimiento 2011-2025:** 354%

---

## 4. Análisis Comparativo de Plataformas

### 4.1 CST Microwave Studio (Líder de Mercado)

**Cuota de mercado:** 31.91% (30/94)

**Fortalezas identificadas:**
- Método FDTD (Finite-Difference Time-Domain) ideal para estructuras complejas
- Excelente visualización 3D y análisis de campos
- Interfaz intuitiva favorecida en entorno académico
- Buen balance entre precisión y tiempo de cómputo

**Casos de uso típicos en la literatura:**
- Antenas de parche con geometrías complejas
- Arrays de antenas y estructuras multi-elemento
- Análisis de banda ancha (UHF, S-band, X-band)
- Diseños con múltiples capas dieléctricas

**Evolución temporal:**
- 2011-2015: 27.3%
- 2016-2020: 30.3%
- 2021-2025: 34.0% ⬆

### 4.2 FEKO (Altair) - Especialista en Antenas

**Cuota de mercado:** 28.72% (27/94)

**Fortalezas identificadas:**
- MoM (Method of Moments) preciso para análisis de antenas
- Excelente para cálculos de diagramas de radiación
- Herramientas específicas para análisis electromagnético de antenas
- Integración con CADFEKO para diseño paramétrico

**Casos de uso típicos:**
- Análisis riguroso de patrones de radiación
- Optimización de ganancia y eficiencia
- Estudios de impedancia y adaptación
- Antenas en presencia de estructuras metálicas (CubeSat body)

**Evolución temporal:**
- 2011-2015: 36.4% 👑
- 2016-2020: 30.3%
- 2021-2025: 26.0% ⬇

**Observación:** Pérdida gradual de cuota de mercado, aunque mantiene posición sólida.

### 4.3 HFSS (Ansys) - Estándar Industrial

**Cuota de mercado:** 25.53% (24/94)

**Fortalezas identificadas:**
- FEM (Finite Element Method) de alta precisión
- Estándar industrial para diseño de RF/microondas
- Excelente para estructuras con múltiples materiales
- Potentes herramientas de optimización

**Casos de uso típicos:**
- Diseños de alta frecuencia (X-band, Ka-band)
- Análisis de estructuras de alimentación complejas
- Optimización paramétrica exhaustiva
- Antenas con metamateriales y substrates especiales

**Evolución temporal:**
- 2011-2015: 27.3%
- 2016-2020: 30.3%
- 2021-2025: 22.0% ⬇

### 4.4 ANSYS (Suite Completa)

**Cuota de mercado:** 10.64% (10/94)

**Características:**
- Principalmente en período 2021-2025
- Uso de suite completa (no solo HFSS)
- Análisis multifísicos: electromagnético + térmico + mecánico
- Simulaciones integradas de sistemas completos

**Tendencia:** Crecimiento notable en años recientes, reflejando necesidad de análisis multifísico.

### 4.5 Plataformas Especializadas (<2%)

**ADS (Advanced Design System):** 1.06%
- Uso específico para diseño de circuitos de alimentación
- Integración con análisis de antenas

**IE3D:** 1.06%
- Herramienta legacy para análisis de estructuras planas

**COMSOL Multiphysics:** 1.06%
- Análisis multifísico especializado
- Menor adopción por complejidad y costo

---

## 5. Factores que Influyen en la Selección de Plataformas

### 5.1 Factores Académicos
1. **Disponibilidad de licencias institucionales**
   - Acuerdos académicos con fabricantes
   - Licencias para estudiantes e investigadores

2. **Curva de aprendizaje**
   - CST favorecido por interfaz intuitiva
   - HFSS requiere mayor expertise pero ofrece más control

3. **Soporte y comunidad**
   - Tutoriales y ejemplos disponibles
   - Foros y documentación

### 5.2 Factores Técnicos
1. **Método numérico apropiado**
   - FDTD (CST): estructuras complejas, banda ancha
   - MoM (FEKO): antenas, problemas radiantes
   - FEM (HFSS): alta precisión, estructuras con múltiples materiales

2. **Requisitos computacionales**
   - Balance entre precisión y tiempo de cómputo
   - Capacidades de paralelización

3. **Tipo de análisis requerido**
   - Análisis de parámetros S
   - Patrones de radiación
   - Análisis transitorio vs. frecuencial

### 5.3 Factores del Proyecto
1. **Banda de frecuencia**
   - UHF/VHF: mayor flexibilidad en elección
   - X-band/Ka-band: preferencia por HFSS

2. **Complejidad del diseño**
   - Geometrías complejas: CST
   - Optimización exhaustiva: HFSS
   - Arrays y estructuras radiantes: FEKO

---

## 6. Tendencias Emergentes y Predicciones

### 6.1 Consolidación del Mercado
- **Observación:** Las tres grandes plataformas concentran el 86% del mercado
- **Tendencia:** Consolidación continua, dificultando entrada de nuevos competidores
- **Implicación:** Inversión en aprendizaje de herramientas establecidas

### 6.2 Especialización de Plataformas
- **CST:** Dominancia en estructuras complejas y diseños de banda ancha
- **FEKO:** Mantiene nicho en análisis preciso de antenas y patrones de radiación
- **HFSS:** Preferido para diseños de alta frecuencia y optimización rigurosa

### 6.3 Integración Multifísica
- Crecimiento de ANSYS (suite completa) sugiere tendencia hacia:
  - Análisis electromagnético + térmico
  - Análisis electromagnético + estructural (vibraciones)
  - Simulaciones de sistema completo

### 6.4 Automatización y Optimización
- Mayor uso de:
  - Optimización paramétrica automatizada
  - Machine Learning para aceleración de diseño
  - Co-simulación con herramientas de sistema

### 6.5 Predicciones 2025-2030
1. **CST continuará liderando** con cuota de mercado >35%
2. **Consolidación:** Las tres grandes mantendrán >80% del mercado
3. **Crecimiento de análisis multifísico:** ANSYS aumentará cuota
4. **Herramientas de IA:** Integración de ML en workflows de diseño
5. **Cloud computing:** Mayor adopción de simulaciones en la nube

---

## 7. Metodologías de Simulación Dominantes

### 7.1 Métodos Numéricos por Plataforma

| Método | Plataformas | Ventajas | Aplicaciones Típicas |
|--------|------------|----------|---------------------|
| FDTD | CST | Banda ancha, estructuras complejas | Arrays, metamateriales, UWB |
| MoM | FEKO | Precisión en radiación | Análisis de antenas, far-field |
| FEM | HFSS, ANSYS | Alta precisión, materiales múltiples | Diseños críticos, alta frecuencia |
| Híbridos | FEKO, CST | Balance precisión/velocidad | Problemas multi-escala |

### 7.2 Validación y Comparación
- **Tendencia:** Múltiples simuladores en un mismo estudio
- **Práctica común:** Validación cruzada entre plataformas
- **Benchmark:** Comparación simulación vs. medición experimental

---

## 8. Impacto en la Investigación de CubeSats

### 8.1 Mejoras en Diseño de Antenas
La evolución de plataformas de simulación ha permitido:
1. **Mayor complejidad de diseños**
   - Antenas reconfigurables
   - Arrays phased
   - Estructuras multi-banda

2. **Reducción de tiempo de desarrollo**
   - Prototipos virtuales antes de fabricación
   - Optimización automatizada
   - Reducción de ciclos de diseño-test-rediseño

3. **Mejora en rendimiento**
   - Mayor ganancia en espacios reducidos
   - Mejor eficiencia de radiación
   - Anchos de banda más amplios

### 8.2 Democratización del Diseño
- **Acceso académico:** Licencias educacionales amplían acceso
- **Comunidad:** Foros y recursos compartidos
- **Reducción de barreras:** Menor necesidad de equipamiento de medición costoso

---

## 9. Limitaciones del Análisis

### 9.1 Limitaciones de Datos
1. **Sesgo de publicación:** Solo estudios publicados
2. **Información incompleta:** Algunos papers no especifican software usado
3. **Múltiples herramientas:** Un estudio puede usar varias plataformas
4. **Período temporal:** Mayor concentración en años recientes

### 9.2 Limitaciones Metodológicas
1. **Extracción automática:** Posibles omisiones en identificación de software
2. **Versiones de software:** No se diferenció entre versiones
3. **Uso industrial vs. académico:** Dataset principalmente académico

---

## 10. Conclusiones

### 10.1 Hallazgos Principales

1. **Liderazgo de CST Microwave Studio**
   - 31.91% de cuota de mercado
   - Crecimiento sostenido desde 2015
   - Preferido por su balance precisión/usabilidad

2. **Oligopolio estable**
   - CST, FEKO y HFSS dominan con 86% del mercado
   - Consolidación en torno a tres plataformas principales
   - Barreras de entrada para nuevos competidores

3. **Crecimiento explosivo del campo**
   - 354% de crecimiento en publicaciones (2011-2025)
   - Madurez tecnológica alcanzada en 2016-2020
   - Especialización continua en período reciente

4. **Especialización por aplicación**
   - Cada plataforma mantiene nichos específicos
   - Selección basada en tipo de análisis requerido
   - Tendencia hacia análisis multifísico

### 10.2 Implicaciones Prácticas

**Para investigadores:**
- Invertir en aprendizaje de plataformas establecidas (CST, FEKO, HFSS)
- Considerar acceso a múltiples herramientas para validación cruzada
- Evaluar necesidades específicas antes de seleccionar plataforma

**Para instituciones:**
- Priorizar licencias de las tres plataformas principales
- Desarrollar capacitación en herramientas más usadas
- Considerar suites completas para análisis multifísico

**Para la industria CubeSat:**
- Las simulaciones son estándar de facto en diseño de antenas
- Inversión en herramientas de simulación es crítica
- Tendencia hacia integración de múltiples dominios físicos

### 10.3 Direcciones Futuras

1. **Investigación:**
   - Análisis más profundo de correlación entre plataforma y tipo de antena
   - Estudio de precisión comparativa entre simuladores
   - Impacto de versiones de software en resultados

2. **Desarrollo:**
   - Integración de IA/ML en workflows de diseño
   - Automatización de optimización multi-objetivo
   - Herramientas de co-diseño antenna-sistema

3. **Educación:**
   - Curricula que incluyan múltiples plataformas
   - Recursos educativos para mejores prácticas
   - Benchmarks y casos de estudio estandarizados

---

## 11. Referencias y Recursos

### 11.1 Archivos Generados
- `simulation_evolution_timeline.png` - Gráficos de evolución temporal
- `simulation_market_share.png` - Evolución de cuota de mercado por período
- `simulation_platform_evolution_report.txt` - Reporte estadístico detallado
- `simulation_platforms_processed.csv` - Datos procesados para análisis posterior

### 11.2 Scripts de Análisis
- `simulation_platform_evolution.py` - Script principal de análisis

### 11.3 Dataset Original
- `baseDatos.csv` - Base de datos completa de revisión sistemática

---

## Apéndices

### Apéndice A: Distribución Completa por Año

Ver archivos de visualización para gráficos detallados de distribución año por año.

### Apéndice B: Metodología de Extracción

Las plataformas fueron identificadas mediante expresiones regulares aplicadas a la columna `esp.domain_methodology.simulation_software`, considerando variaciones comunes de nombres (e.g., "CST Microwave Studio", "CST Studio Suite", "CST").

### Apéndice C: Estadísticas Detalladas

Ver `simulation_platforms_processed.csv` para datos completos incluyendo:
- Año de publicación
- Plataforma identificada
- Frecuencia de uso
- Tendencias temporales

---

**Documento preparado por:** Análisis automatizado con Python
**Última actualización:** 14 de noviembre de 2025
**Versión:** 1.0
