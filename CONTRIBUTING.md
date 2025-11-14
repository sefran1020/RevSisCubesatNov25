# Guía de Contribución

Gracias por tu interés en contribuir a esta revisión sistemática sobre diseño de antenas microstrip para CubeSat.

## Tipos de Contribuciones

### 1. 🐛 Reportar Errores en los Datos

Si encuentras errores en:
- Datos extraídos de estudios
- Categorizaciones incorrectas
- Información bibliográfica

**Por favor**:
1. Abre un issue con la etiqueta `data-error`
2. Incluye:
   - Archivo afectado (e.g., `OE1/grupoA.csv`)
   - Línea o registro específico
   - Error identificado
   - Corrección sugerida (con fuente)

### 2. 📚 Sugerir Estudios Adicionales

Si conoces estudios relevantes que no fueron incluidos:

**Requisitos para sugerencia**:
- Cumple criterios de inclusión PRISMA (ver PRISMA_METADATA.md)
- Publicado entre 2000-2025
- Texto completo en inglés
- Antenas microstrip/patch para CubeSat

**Proceso**:
1. Abre un issue con etiqueta `new-study`
2. Proporciona:
   - Referencia completa (APA o IEEE)
   - DOI o enlace
   - Justificación de relevancia
   - Verificación contra criterios de exclusión

### 3. 🔍 Proponer Análisis Adicionales

Ideas para análisis complementarios o extensiones:

**Áreas bienvenidas**:
- Meta-análisis cuantitativos
- Análisis de tendencias temporales
- Comparaciones cross-validation
- Visualizaciones adicionales

**Proceso**:
1. Abre un discussion en categoría `Ideas`
2. Describe:
   - Objetivos del análisis
   - Datos necesarios
   - Metodología propuesta
   - Valor añadido

### 4. 📝 Mejorar Documentación

Contribuciones a:
- README.md
- PRISMA_METADATA.md
- Comentarios en archivos de datos
- Traducciones

**Proceso**:
1. Fork del repositorio
2. Crear rama: `docs/descripcion-mejora`
3. Hacer cambios
4. Pull request con descripción clara

### 5. 💻 Código de Análisis

Si desarrollas scripts para procesar estos datos:

**Requisitos**:
- Código bien documentado
- Reproducible
- Con dependencias claras
- Licencia compatible (MIT, BSD, Apache 2.0)

**Estructura sugerida**:
```
scripts/
├── README.md
├── requirements.txt
├── nombre_script.py
└── ejemplo_uso.ipynb
```

## Proceso de Contribución

### Para Issues

1. **Busca primero**: Revisa issues existentes
2. **Usa plantillas**: Si están disponibles
3. **Sé específico**: Proporciona contexto y ejemplos
4. **Una issue = un tema**: No mezcles múltiples temas

### Para Pull Requests

1. **Fork** el repositorio
2. **Crea una rama** descriptiva:
   ```bash
   git checkout -b feature/descripcion-corta
   git checkout -b fix/descripcion-error
   git checkout -b docs/descripcion-mejora
   ```
3. **Haz commits claros**:
   ```bash
   git commit -m "Fix: Corregir dato en OE2/grupoA.csv línea 45"
   git commit -m "Docs: Añadir sección de instalación a README"
   ```
4. **Push a tu fork**:
   ```bash
   git push origin feature/descripcion-corta
   ```
5. **Abre Pull Request**:
   - Describe cambios claramente
   - Referencia issues relacionados
   - Explica por qué es necesario

## Estándares de Calidad

### Datos
- Formato CSV: UTF-8, delimitador coma
- Formato Excel: .xlsx (no .xls)
- Nombres de columna descriptivos
- Sin valores perdidos sin marcar (usar "N/A" o "")

### Documentación
- Markdown bien formateado
- Enlaces funcionales
- Lenguaje claro y profesional
- Español o inglés

### Código (si aplica)
- PEP 8 para Python
- Comentarios en español o inglés
- Funciones documentadas
- Tests si es apropiado

## Revisión de Contribuciones

Todas las contribuciones serán revisadas por:
1. **Verificación de datos**: Contra fuentes originales
2. **Consistencia**: Con protocolo PRISMA
3. **Calidad**: Cumplimiento de estándares
4. **Relevancia**: Alineación con objetivos de la revisión

**Tiempo de respuesta esperado**: 7-14 días

## Código de Conducta

### Esperamos que los contribuidores:

✅ Sean respetuosos y profesionales
✅ Proporcionen feedback constructivo
✅ Acepten críticas con mente abierta
✅ Se enfoquen en el mejor interés del proyecto
✅ Reconozcan el trabajo de otros

### No toleramos:

❌ Lenguaje o comportamiento ofensivo
❌ Ataques personales
❌ Spam o autopromoción
❌ Violación de privacidad
❌ Plagio o falsificación de datos

## Reconocimiento

Los contribuidores significativos serán:
- Listados en CONTRIBUTORS.md
- Mencionados en futuros trabajos derivados
- Agradecidos en publicaciones relacionadas

### Contribución significativa incluye:
- Corrección de ≥5 errores de datos
- Adición de ≥3 estudios validados
- Desarrollo de herramientas de análisis
- Mejoras sustanciales de documentación

## Preguntas Frecuentes

### ¿Puedo usar estos datos para mi propia investigación?

Sí, bajo licencia CC BY 4.0. Solo asegúrate de:
- Citar apropiadamente (ver CITATION.cff)
- Respetar licencias de artículos originales
- Compartir derivados bajo misma licencia

### ¿Puedo proponer cambios al protocolo PRISMA?

El protocolo está cerrado para esta revisión. Sin embargo:
- Puedes sugerir para futuras actualizaciones
- Puedes hacer fork para tu propia revisión
- Puedes proponer extensiones en discussions

### ¿Cómo reporto problemas de privacidad o sensibilidad?

Para temas sensibles, contacta directamente:
- Email: [contact@institution.edu]
- No uses issues públicos

### ¿Qué pasa si mi contribución es rechazada?

Recibirás feedback explicando:
- Razones específicas del rechazo
- Sugerencias para mejorar
- Alternativas si aplican

Puedes revisar y reenviar.

## Recursos

### Documentos de Referencia
- [PRISMA 2020 Guidelines](http://www.prisma-statement.org/)
- [Systematic Review Best Practices](https://training.cochrane.org/handbook)
- [Research Data Management](https://www.nature.com/sdata/)

### Herramientas Útiles
- **CSV validation**: [CSVLint](https://csvlint.io/)
- **Markdown editing**: [StackEdit](https://stackedit.io/)
- **Citation formatting**: [Zotero](https://www.zotero.org/)

## Contacto

**Para contribuciones**:
- GitHub Issues: Preferido para tracking
- GitHub Discussions: Ideas y preguntas generales

**Para consultas privadas**:
- Email: [research.contact@institution.edu]

---

## Proceso de Actualización

Este repositorio se actualiza:
- ✅ **Correcciones de errores**: En curso
- ✅ **Estudios adicionales validados**: Revisión mensual
- ⚠️ **Cambios mayores de protocolo**: Solo en versiones mayores
- ❌ **Nuevas búsquedas sistemáticas**: Requieren nueva revisión

Última actualización de este documento: 2025-11-13

---

¡Gracias por ayudar a mejorar la calidad y utilidad de esta revisión sistemática!
