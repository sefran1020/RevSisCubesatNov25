# Guía para Publicar en Zenodo

## ¿Qué es Zenodo?

Zenodo es un repositorio de datos de investigación de acceso abierto desarrollado por CERN. Es ideal para:
- ✅ Obtener un DOI permanente para tus datos
- ✅ Garantizar preservación a largo plazo
- ✅ Cumplir requisitos de datos abiertos de revistas
- ✅ Aumentar la citabilidad de tu investigación
- ✅ Integración con GitHub

## Preparación de este Repositorio para Zenodo

### ✅ Archivos ya incluidos:

1. **`.zenodo.json`**: Metadatos estructurados para Zenodo
2. **`README.md`**: Documentación principal
3. **`LICENSE`**: Licencia CC BY 4.0
4. **`CITATION.cff`**: Formato de citación
5. **`PRISMA_METADATA.md`**: Protocolo detallado

### 📋 Checklist Pre-publicación

Antes de publicar en Zenodo, verifica:

- [ ] Completar información de autores en `.zenodo.json`
- [ ] Actualizar ORCIDs de todos los autores
- [ ] Añadir información de grants/financiamiento (si aplica)
- [ ] Verificar que todos los archivos necesarios están incluidos
- [ ] Revisar que no hay archivos sensibles o temporales
- [ ] Confirmar que los PDFs tienen permisos de distribución
- [ ] Actualizar DOI del artículo publicado (cuando esté disponible)
- [ ] Revisar tamaño total del repositorio

## Dos Métodos de Publicación

### Método 1: Integración GitHub-Zenodo (Recomendado)

#### Ventajas:
- Automático cuando haces release en GitHub
- Sincronización perfecta
- Versionado automático
- Más fácil de actualizar

#### Pasos:

1. **Conectar GitHub con Zenodo**
   - Ve a https://zenodo.org/
   - Inicia sesión (crea cuenta si es necesario)
   - Ve a GitHub en configuración: https://zenodo.org/account/settings/github/
   - Autoriza acceso a tus repositorios

2. **Activar el repositorio**
   - En Zenodo GitHub settings, busca tu repositorio
   - Activa el toggle para este repositorio

3. **Crear un release en GitHub**
   ```bash
   git tag -a v1.0 -m "First release - Complete systematic review dataset"
   git push origin v1.0
   ```

   O desde la interfaz web de GitHub:
   - Ve a "Releases" → "Create a new release"
   - Tag: `v1.0`
   - Title: `v1.0 - Systematic Review Complete Dataset`
   - Description: Resumen de contenido
   - "Publish release"

4. **Verificar en Zenodo**
   - El DOI se genera automáticamente
   - Zenodo toma metadatos de `.zenodo.json`
   - Revisa y edita si es necesario

### Método 2: Subida Manual a Zenodo

#### Ventajas:
- Más control sobre qué se sube
- Útil si no quieres hacer público el GitHub
- Puedes editar todo antes de publicar

#### Pasos:

1. **Preparar el archivo ZIP**
   ```bash
   # Crear ZIP excluyendo archivos no necesarios
   # En Windows PowerShell:
   Compress-Archive -Path * -DestinationPath ../RevSisCubesat-v1.0.zip
   ```

2. **Subir a Zenodo**
   - Ve a https://zenodo.org/deposit/new
   - Arrastra el ZIP o selecciona archivos
   - Los metadatos de `.zenodo.json` se cargarán automáticamente

3. **Revisar metadatos**
   - Título
   - Autores (añadir ORCIDs)
   - Descripción
   - Palabras clave
   - Tipo de subida: "Dataset"
   - Licencia: CC BY 4.0

4. **Publicar**
   - Revisa todo cuidadosamente
   - "Publish" (⚠️ **No reversible**)

## Estructura de Versiones

### Versionado Semántico para Datos

- **v1.0**: Versión inicial completa
- **v1.1**: Correcciones menores, datos adicionales
- **v2.0**: Cambios mayores (nueva búsqueda, reanalisis)

### Cuándo crear nueva versión:

| Cambio | Tipo de Versión |
|--------|-----------------|
| Corrección de errores en datos | v1.0.1 (patch) |
| Añadir estudios validados (1-5) | v1.1 (minor) |
| Añadir estudios validados (>5) | v1.2 (minor) |
| Nueva búsqueda sistemática | v2.0 (major) |
| Cambio de metodología | v2.0 (major) |

## Completar Metadatos

### 1. Editar `.zenodo.json`

Campos que DEBES completar:

```json
{
  "creators": [
    {
      "name": "Apellido, Nombre",
      "affiliation": "Universidad/Institución",
      "orcid": "0000-0000-0000-0000"
    }
  ],
  "grants": [
    {
      "id": "ID_del_Grant"  // Opcional
    }
  ],
  "related_identifiers": [
    {
      "identifier": "10.xxxx/xxxxx",  // DOI del artículo
      "relation": "isSupplementTo",
      "scheme": "doi"
    }
  ]
}
```

### 2. Verificar Información

- [ ] Título descriptivo y completo
- [ ] Todos los autores con ORCID
- [ ] Descripción clara del contenido
- [ ] Palabras clave relevantes
- [ ] Licencia correcta (CC BY 4.0)
- [ ] Referencias al artículo principal
- [ ] Grant ID si aplica

## Consideraciones sobre PDFs

### ⚠️ Importante sobre `articulosPDF/`

Los 79 PDFs en `articulosPDF/` están sujetos a copyright de los publishers.

**Opciones**:

1. **Incluirlos** (con precaución)
   - Justificación: Revisión sistemática con fair use
   - Riesgo: Posibles reclamos de copyright
   - Recomendación: Consulta asesoría legal

2. **No incluirlos**
   - Más seguro legalmente
   - Proporciona lista de referencias en su lugar
   - Los usuarios pueden obtener PDFs por sus medios

3. **Solo incluir acceso abierto**
   - Identifica cuáles son Open Access
   - Solo incluye esos
   - Para el resto, proporciona DOIs

### Script para verificar:

```python
# Puedes añadir un script que verifique licencias
# Ejemplo conceptual:
import os
pdf_dir = "articulosPDF"
pdfs = os.listdir(pdf_dir)
print(f"Total PDFs: {len(pdfs)}")
# Generar lista de referencias en lugar de PDFs
```

## Tamaño del Repositorio

Zenodo permite:
- ✅ Hasta 50 GB por dataset
- ✅ Sin límite de archivos

Verifica el tamaño:
```bash
# PowerShell
Get-ChildItem -Recurse | Measure-Object -Property Length -Sum
```

## Después de Publicar

### 1. Obtén el Badge de Zenodo

Zenodo proporciona un badge DOI. Añádelo al README:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

### 2. Actualiza el Artículo

Incluye el DOI de Zenodo en:
- Sección de "Data Availability"
- Referencias del artículo
- Material suplementario

### 3. Comparte el Enlace

- Página del departamento
- ResearchGate
- Academia.edu
- Twitter/X académico
- LinkedIn

## Actualizar una Publicación Existente

Si ya publicaste y necesitas actualizar:

### Desde GitHub (Método 1):

1. Hacer cambios en el repositorio
2. Crear nuevo tag:
   ```bash
   git tag -a v1.1 -m "Update: Added 3 validated studies"
   git push origin v1.1
   ```
3. Crear release en GitHub
4. Zenodo crea nueva versión automáticamente

### Manual (Método 2):

1. Ve a tu depósito en Zenodo
2. Click "New version"
3. Sube archivos actualizados
4. Actualiza metadatos si es necesario
5. Publica nueva versión

## Comunidades en Zenodo

Considera unirte a comunidades relevantes:

- **Aerospace Engineering**
- **Satellite Communications**
- **Systematic Reviews**
- **Open Research Data**

Esto aumenta la visibilidad de tu dataset.

## Checklist Final Pre-publicación

### Metadatos
- [ ] `.zenodo.json` completo y correcto
- [ ] Todos los autores con ORCID
- [ ] Palabras clave relevantes
- [ ] Descripción completa
- [ ] Licencia CC BY 4.0

### Documentación
- [ ] README.md claro y completo
- [ ] PRISMA_METADATA.md detallado
- [ ] CITATION.cff actualizado
- [ ] LICENSE incluido

### Datos
- [ ] Todos los CSV verificados
- [ ] Excel sin archivos temporales (~$)
- [ ] Estructura de carpetas clara
- [ ] .gitignore actualizado

### Legal
- [ ] Decisión sobre PDFs tomada
- [ ] Permisos de datos verificados
- [ ] Licencia apropiada

### Calidad
- [ ] Datos revisados por segundo autor
- [ ] Sin errores obvios
- [ ] Nombres de archivo consistentes
- [ ] Codificación UTF-8

## Recursos Adicionales

- **Zenodo Help**: https://help.zenodo.org/
- **Zenodo FAQ**: https://help.zenodo.org/faq/
- **GitHub-Zenodo Integration**: https://guides.github.com/activities/citable-code/
- **OpenAIRE Guidelines**: https://www.openaire.eu/

## Preguntas Frecuentes

### ¿Puedo editar después de publicar?

❌ No puedes editar una versión publicada
✅ Pero puedes crear nueva versión

### ¿Cuánto cuesta Zenodo?

Gratis. Financiado por CERN y la Comisión Europea.

### ¿Qué pasa si elimino el repositorio de GitHub?

Si usaste integración GitHub-Zenodo:
- El DOI y datos en Zenodo permanecen
- Son independientes del GitHub

### ¿Puedo hacer privado primero?

Sí, puedes subir como "Restricted Access" mientras revisas.
Luego cambiar a "Open Access" cuando estés listo.

### ¿Cómo manejar actualizaciones frecuentes?

Para datos en evolución:
- Usa versiones patch (v1.0.1, v1.0.2)
- O espera a tener cambios sustanciales
- No hagas versión por cada pequeño cambio

## Contacto para Dudas

Si tienes preguntas sobre esta guía:
- Abre un issue en GitHub
- Email: [contact@institution.edu]
- Consulta Zenodo Support: https://zenodo.org/support

---

**Última actualización**: 2025-11-13
**Versión de esta guía**: 1.0
