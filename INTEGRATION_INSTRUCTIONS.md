# Instrucciones de Integración de Figura al Artículo
## Figure 2: Temporal Evolution of Simulation Platforms

**Documento:** articulo2a.pdf
**Sección objetivo:** 3.1 Electromagnetic Simulation-Guided Design Optimization
**Fecha:** 14 de noviembre de 2025

---

## 1. UBICACIÓN ÓPTIMA DE LA FIGURA

### Opción A (RECOMENDADA): Después de la Table 1
**Ubicación exacta:** Entre las páginas 9-10, después de la Table 1 y antes del párrafo "The platform specialization patterns..."

**Justificación:**
- La Table 1 presenta características estáticas de las plataformas
- La Figure 2 complementa mostrando la evolución temporal dinámica
- Flujo lógico: características → evolución temporal → análisis de patrones

**Texto de transición a insertar antes de la figura:**

```
Figure 2 synthesizes the temporal evolution and market dynamics underlying
the platform specialization patterns documented in Table 1, revealing three
distinct developmental phases and progressive CST consolidation from 27.3%
(2014-2017) to 34.0% (2022-2025).
```

### Opción B (ALTERNATIVA): En subsección "Temporal Evolution and Methodological Maturation"
**Ubicación exacta:** Página 10-11, al inicio del párrafo que comienza "Evidence organizes into three developmental phases..."

**Justificación:**
- Ilustra directamente el contenido de esta subsección
- Proporciona evidencia visual de las fases descritas en el texto

**Texto de transición:**

```
The temporal progression documented in Figure 2 demonstrates systematic
platform evolution across three developmental phases, with quantified
transitions in market share and publication volume.
```

---

## 2. NUMERACIÓN Y REFERENCIAS

### Actualizar numeración de figuras
- **Actual:** Figure 1 = PRISMA flowchart (página 6)
- **Nueva:** Figure 2 = Simulation Platform Evolution
- Si hay figuras posteriores, renumerar en consecuencia

### Referencias cruzadas en el texto

**Ubicaciones donde referenciar Figure 2:**

1. **Página 9, párrafo "Platform Specialization...":**
   ```
   Texto actual: "...with 28 studies demonstrating systematic optimization..."

   Añadir: "(Figure 2a)"

   Resultado: "...with 28 studies demonstrating systematic optimization
   of patches and arrays across Ka/C/S bands (Figure 2a)."
   ```

2. **Página 10, párrafo "Temporal Evolution...":**
   ```
   Texto actual: "Evidence organizes into three developmental phases..."

   Añadir: "(Figure 2a-c)"

   Resultado: "Evidence organizes into three developmental phases
   (Figure 2a-c) that progressively expand the application domains..."
   ```

3. **Página 11, donde se menciona "2014-2017", "2018-2021", "2022-2025":**
   ```
   Añadir referencia: "(Figure 2b)"
   ```

---

## 3. CAPTION DE LA FIGURA

**Insertar el siguiente caption debajo de la figura:**

```latex
Figure 2. Temporal Evolution and Specialization of Electromagnetic Simulation
Platforms in CubeSat Antenna Research. (a) Temporal trajectory of dominant
simulation platforms (2014-2025) showing CST emergence as market leader with
34% share in recent period (2022-2025), compared to balanced distribution in
consolidation phase (2018-2021) where HFSS, CST, and FEKO achieved parity at
30.3% each. Shaded regions delineate methodological maturation phases: early
consolidation (2014-2017) established circular polarization protocols, expansion
(2018-2021) normalized dual-band optimization, and advanced integration
(2022-2025) introduced metasurface and multiphysics validation. (b) Period-
stratified publication distribution quantifying 354% growth from early
consolidation (n=11) to advanced integration (n=50), with FEKO dominance (36.4%)
in early phase transitioning to CST leadership (34%) in contemporary practice.
(c) Market share evolution demonstrating oligopolistic consolidation where top-3
platforms (CST, FEKO, HFSS) maintain 86% combined coverage across all periods,
with progressive CST specialization in miniaturization and thermo-mechanical
verification complementing HFSS bandwidth optimization strengths and FEKO array
radiation expertise. Data derived from systematic analysis of 94 platform
instances across 90 peer-reviewed studies (2014-2025).
```

**Versión condensada (si hay limitación de espacio):**

```latex
Figure 2. Temporal Evolution of Electromagnetic Simulation Platforms.
(a) Annual publication trends showing CST emergence (34% in 2022-2025) from
balanced three-platform parity (30.3% each in 2018-2021). (b) Period-stratified
distribution documenting 354% growth (n=11→50). (c) Market share evolution
demonstrating 86% top-3 consolidation across temporal phases. Shaded regions in
(a) indicate methodological maturation phases. Data: 94 instances across 90
studies (2014-2025).
```

---

## 4. MODIFICACIONES AL TEXTO EXISTENTE

### 4.1. Sección 3.1 - Párrafo "Platform Specialization and Application Domains"

**Texto actual (página 9):**
```
HFSS dominates circular polarization and bandwidth tuning through finite
element method architectures, with 28 studies demonstrating systematic
optimization of patches and arrays across Ka/C/S bands...
```

**Texto modificado (añadir datos cuantitativos de la figura):**
```
HFSS dominates circular polarization and bandwidth tuning through finite
element method architectures, accounting for 28 studies (25.53% overall,
Figure 2c) demonstrating systematic optimization of patches and arrays
across Ka/C/S bands...
```

### 4.2. Sección 3.1 - Párrafo "Temporal Evolution and Methodological Maturation"

**Texto actual (página 10-11):**
```
Evidence organizes into three developmental phases that progressively expand
the application domains shown in Table 1.
```

**Texto modificado (integrar referencia a figura):**
```
Evidence organizes into three developmental phases (Figure 2a) that
progressively expand the application domains shown in Table 1, with quantified
transitions documenting 354% publication growth and systematic platform
specialization (Figure 2b-c).
```

### 4.3. Añadir nuevo párrafo de síntesis (OPCIONAL)

**Ubicación:** Después del párrafo "Advanced integration (2022-2025)..." en página 11

**Texto propuesto:**
```
The temporal dynamics documented in Figure 2 reveal market consolidation
patterns wherein top-3 platforms maintain 86% combined coverage across all
developmental phases, yet exhibit pronounced specialization trajectories.
CST's progressive market share expansion (27.3%→30.3%→34.0%) correlates with
increasing emphasis on miniaturization and thermo-mechanical integration in
contemporary CubeSat designs, while FEKO's relative decline (36.4%→30.3%→26.0%)
reflects narrowing application focus on array-scale radiation control. This
oligopolistic consolidation, combined with the observed 68% algorithmic
hyperparameter opacity across all platforms, introduces systematic
vulnerabilities where platform-specific artifacts propagate to design
recommendations without independent verification.
```

---

## 5. INTEGRACIÓN EN DISCUSIÓN (Sección 4)

### 5.1. Referencia en "Frequency-Dependent Validation Myopia" (página 19-20)

**Texto actual:**
```
The concentration of validation protocols around S-band frequencies...
```

**Añadir después del primer párrafo:**
```
This frequency concentration aligns with the platform evolution documented
in Figure 2, where the three dominant solvers (CST, FEKO, HFSS) achieved
initial consolidation (2014-2017) primarily through S-band circular
polarization validation protocols, creating path-dependent infrastructure
investments that constrain contemporary Ka/W-band development.
```

---

## 6. FORMATO Y CALIDAD TÉCNICA

### Archivos disponibles:
- **PNG de alta resolución:** `Figure_SimulationPlatformEvolution.png` (600 DPI)
- **Formato vectorial:** `Figure_SimulationPlatformEvolution.eps` (para journals)
- **Datos estadísticos:** `Table_SimulationPlatformStatistics.csv`

### Especificaciones técnicas:
- **Resolución:** 600 DPI (cumple estándares IEEE, Elsevier, Springer)
- **Tamaño:** 7.5 × 6 pulgadas (ancho de columna doble estándar)
- **Formato de color:** RGB (convertir a CMYK si la revista lo requiere)
- **Fuente:** Times New Roman (coherente con texto del artículo)

### Proceso de inserción:

**Para LaTeX:**
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{Figure_SimulationPlatformEvolution.eps}
    \caption{[Caption completo aquí]}
    \label{fig:simulation_evolution}
\end{figure}
```

**Para Microsoft Word:**
1. Insertar → Imagen
2. Seleccionar `Figure_SimulationPlatformEvolution.png`
3. Ajustar ancho a "Ancho de columna"
4. Aplicar caption como "Figura 2"

---

## 7. COHERENCIA CON HALLAZGOS DEL ARTÍCULO

### Datos que la figura respalda directamente:

| Afirmación en el texto | Panel de la figura | Evidencia visual |
|------------------------|-------------------|------------------|
| "CST emphasizes miniaturization... (38%)" | Panel (c) | 34% cuota en 2022-2025 |
| "HFSS dominates circular polarization... (56%)" | Panel (b), (c) | Distribución por período |
| "FEKO supports array-scale radiation... (12%)" | Panel (c) | 26% cuota reciente |
| "Early consolidation (2014-2017)" | Panel (a) | Banda gris con 11 publicaciones |
| "Expansion (2018-2021)" | Panel (a) | Banda azul con 33 publicaciones |
| "Advanced integration (2022-2025)" | Panel (a) | Banda verde con 50 publicaciones |
| "354% growth" | Panel (b) | 11→33→50 publicaciones |

### Verificar consistencia numérica:

**IMPORTANTE:** Los porcentajes en el texto del artículo deben coincidir con la figura.

- Table 1 muestra: HFSS (28 estudios), CST (19), FEKO (6)
- Figure 2 muestra: HFSS (25.53%), CST (31.91%), FEKO (28.72%)

**Nota:** Hay diferencia porque Table 1 cuenta estudios, Figure 2 cuenta instancias de uso (algunos estudios usan múltiples plataformas).

**Aclaración a añadir en caption o nota al pie:**
```
Note: Percentages reflect platform usage instances (n=94) rather than study
counts (n=50 in Table 1), as some studies employed multiple simulation tools
for cross-platform validation.
```

---

## 8. CHECKLIST DE INTEGRACIÓN

Antes de finalizar la integración, verificar:

- [ ] Figura insertada en ubicación óptima (después de Table 1 o en subsección temporal)
- [ ] Numeración actualizada (Figure 2)
- [ ] Caption completo insertado debajo de la figura
- [ ] Referencias cruzadas añadidas en el texto (mínimo 3 ubicaciones)
- [ ] Datos numéricos coherentes entre texto y figura
- [ ] Calidad de imagen verificada (600 DPI visible en zoom)
- [ ] Formato de archivo apropiado para la revista (EPS para LaTeX, PNG para Word)
- [ ] Texto de transición añadido antes de la figura
- [ ] Nuevo párrafo de síntesis considerado (opcional)
- [ ] Coherencia con Table 1 verificada
- [ ] Nota aclaratoria sobre diferencia estudios/instancias incluida

---

## 9. JUSTIFICACIÓN METODOLÓGICA

### Por qué esta figura es esencial para el artículo:

1. **Complementa análisis estático con dinámico:**
   - Table 1 = características de plataformas (estático)
   - Figure 2 = evolución temporal (dinámico)

2. **Evidencia visual de hallazgos clave:**
   - Consolidación oligopolística (86% top-3)
   - Especialización progresiva de plataformas
   - Tres fases de maduración metodológica

3. **Respalda argumentos de la Discusión:**
   - Path dependency (sección 4.3)
   - Fragmentación disciplinaria (sección 4.1)
   - Necesidad de estandarización (sección 4.4)

4. **Valor para lectores:**
   - Comprensión rápida de tendencias (visual > tabular)
   - Identificación de plataforma dominante según período
   - Contexto histórico para decisiones de diseño

---

## 10. ALTERNATIVAS DE PRESENTACIÓN

### Si el espacio es limitado:

**Opción 1:** Dividir en dos figuras separadas
- Figure 2a: Panel (a) completo - Evolución temporal
- Figure 2b: Paneles (b) y (c) - Análisis por período

**Opción 2:** Versión simplificada de un solo panel
- Usar solo panel (a) con anotaciones expandidas
- Mover paneles (b) y (c) a material suplementario

**Opción 3:** Integrar como subfigura de Table 1
- Crear "Table 1 + Figure" combinada
- Panel (a) de la figura insertado junto a la tabla

---

## 11. MATERIAL SUPLEMENTARIO

Si la revista permite material suplementario, considerar añadir:

- **Supplementary Figure S1:** Análisis extendido con las 7 plataformas
- **Supplementary Table S1:** Datos numéricos completos por año y plataforma
- **Supplementary Data:** Archivo CSV con datos procesados

---

## 12. CONTACTO Y SOPORTE

Para dudas sobre la integración de esta figura:
- Datos fuente: `simulation_platforms_processed.csv`
- Script de generación: `generate_article_figure.py`
- Análisis completo: `Simulation_Platform_Evolution_Analysis.md`

---

**Última actualización:** 14 de noviembre de 2025
**Versión:** 1.0
**Autor:** Análisis sistemático de revisión de literatura
