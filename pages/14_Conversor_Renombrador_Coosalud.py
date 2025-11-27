import streamlit as st
import json
import os
import re
import tempfile
import shutil
import pandas as pd
import random
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

# Configurar tema y navbar
configure_modern_theme()
st.set_page_config(
    page_title="Conversor + Renombrador - Coosalud", 
    page_icon="🔄", 
    layout="wide"
)
modern_navbar()

st.title("🔄 Conversor + Renombrador - Coosalud")
st.markdown("Procesa archivos JSON de Mantis y renombra archivos con patrón NE###### **al mismo tiempo**")

# Función para renombrar archivos sin fecha
def renombrar_archivo_sin_fecha(ruta_archivo, nombre_original):
    """Renombra archivo agregando 'sin fecha' si no tiene fechaRadicacion válida"""
    nombre_base, extension = os.path.splitext(nombre_original)
    nuevo_nombre = f"{nombre_base}_sin_fecha{extension}"
    nueva_ruta = os.path.join(os.path.dirname(ruta_archivo), nuevo_nombre)
    
    try:
        os.rename(ruta_archivo, nueva_ruta)
        return nuevo_nombre, True
    except Exception as e:
        return nombre_original, False

# Función de procesamiento JSON - BASADA EN TU CÓDIGO ORIGINAL
def procesar_archivos_json(directorio):
    archivos_procesados = []
    errores = []
    
    try:
        archivos_json = [archivo for archivo in os.listdir(directorio) if archivo.lower().endswith('.json')]
        
        for nombre_archivo in archivos_json:
            try:
                ruta_archivo = os.path.join(directorio, nombre_archivo)
                with open(ruta_archivo, 'r', encoding='utf-8') as file:
                    datos = json.load(file)
                
                # ✅ EXTRACCIÓN DE CAMPOS CON DIFERENTES NOMBRES (como en tu código original)
                fecha_original = datos.get('fechaRadicacion') or datos.get('FechaRadicacion')
                
                # 🎯 REGLA: Renombrar archivo si no tiene fecha válida
                archivo_renombrado = False
                if fecha_original == "0000-00-00T00:00:00" or not fecha_original:
                    nuevo_nombre, exito = renombrar_archivo_sin_fecha(ruta_archivo, nombre_archivo)
                    if exito:
                        nombre_archivo = nuevo_nombre
                        archivo_renombrado = True
                        ruta_archivo = os.path.join(directorio, nombre_archivo)
                
                # Formatear fecha válida (como en tu código original)
                if fecha_original and fecha_original != "0000-00-00T00:00:00" and '+' in fecha_original:
                    fecha_procesada = fecha_original.split('+')[0]
                    if 'fechaRadicacion' in datos:
                        datos['fechaRadicacion'] = fecha_procesada
                    if 'FechaRadicacion' in datos:
                        datos['FechaRadicacion'] = fecha_procesada
                
                # ✅ ESTRUCTURA FINAL - EXTRACCIÓN CON DIFERENTES NOMBRES
                resultado = {
                    "resultState": datos.get('resultState', datos.get('ResultState')),
                    "procesoId": datos.get('procesoId', datos.get('ProcesoId')),
                    "numFactura": datos.get('numFactura', datos.get('NumFactura')),
                    "codigoUnicoValidacion": datos.get('codigoUnicoValidacion', datos.get('CodigoUnicoValidacion')),
                    "fechaRadicacion": datos.get('fechaRadicacion', datos.get('FechaRadicacion')),
                    "rutaArchivos": datos.get('rutaArchivos', datos.get('RutaArchivos')),
                    "resultadosValidacion": []
                }
                
                # Guardar CON sangría pero SIN espacio en resultadosValidacion (como en tu código)
                with open(ruta_archivo, 'w', encoding='utf-8') as file:
                    json_str = json.dumps(resultado, indent=2, ensure_ascii=False)
                    json_str = json_str.replace('"resultadosValidacion": []', '"resultadosValidacion":[]')
                    file.write(json_str)
                
                # Determinar estado
                if archivo_renombrado:
                    estado = "✅ Estructura generada + 📝 Archivo renombrado (sin fecha)"
                else:
                    estado = "✅ Estructura generada"
                
                # Información para mostrar
                info_generacion = {
                    'resultState': resultado["resultState"],
                    'procesoId': resultado["procesoId"],
                    'numFactura': resultado["numFactura"],
                    'codigoCUV': resultado["codigoUnicoValidacion"][:20] + "..." if resultado["codigoUnicoValidacion"] else "N/A",
                    'fechaRadicacion': resultado["fechaRadicacion"][:19] if resultado["fechaRadicacion"] else "NO TIENE FECHA",
                    'archivoRenombrado': archivo_renombrado
                }
                
                archivos_procesados.append({
                    'nombre': nombre_archivo,
                    'estado': estado,
                    'factura': resultado["numFactura"],
                    'info_generacion': info_generacion
                })
                
            except Exception as e:
                errores.append({
                    'nombre': nombre_archivo,
                    'error': str(e)
                })
        
        return archivos_procesados, errores
        
    except Exception as e:
        errores.append({'nombre': 'Sistema', 'error': f"Error general: {str(e)}"})
        return [], errores

# Función de renombrado CUV (Renombrador Coosalud)
def renombrar_archivos_cuv(directorio):
    resultados = []
    contador = 0
    
    try:
        for archivo in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, archivo)
            
            # Verificar si es un archivo (no carpeta) y no es JSON (para evitar conflictos)
            if os.path.isfile(ruta_completa) and not archivo.lower().endswith('.json'):
                # Buscar el patrón NE seguido de números en el nombre del archivo
                patron = r'(NE\d+)'
                coincidencia = re.search(patron, archivo)
                
                if coincidencia:
                    numero_factura = coincidencia.group(1)
                    nombre_base, extension = os.path.splitext(archivo)
                    
                    # Crear el nuevo nombre: CUV_NE651.ext (FORMATO COOSALUD)
                    nuevo_nombre = f"CUV_{numero_factura}{extension}"
                    nueva_ruta = os.path.join(directorio, nuevo_nombre)
                    
                    # Renombrar el archivo
                    try:
                        os.rename(ruta_completa, nueva_ruta)
                        resultados.append({
                            'original': archivo,
                            'nuevo': nuevo_nombre,
                            'estado': '✅ Renombrado',
                            'tipo': 'success',
                            'numero_factura': numero_factura
                        })
                        contador += 1
                    except Exception as e:
                        resultados.append({
                            'original': archivo,
                            'nuevo': nuevo_nombre,
                            'estado': f'❌ Error: {str(e)}',
                            'tipo': 'error',
                            'numero_factura': numero_factura
                        })
                else:
                    # Solo mostrar info si no es un archivo JSON (para evitar duplicados)
                    if not archivo.lower().endswith('.json'):
                        resultados.append({
                            'original': archivo,
                            'nuevo': archivo,
                            'estado': 'ℹ No coincide con patrón NE######',
                            'tipo': 'info',
                            'numero_factura': 'N/A'
                        })
        
        return resultados, contador
        
    except Exception as e:
        st.error(f"Error general: {str(e)}")
        return [], 0

# Función principal que procesa TODO
def procesar_todo(directorio):
    """Procesa tanto archivos JSON como archivos para renombrar"""
    # Procesar archivos JSON
    json_procesados, json_errores = procesar_archivos_json(directorio)
    
    # Procesar archivos para renombrar
    renombrados, contador_renombrados = renombrar_archivos_cuv(directorio)
    
    return {
        'json_procesados': json_procesados,
        'json_errores': json_errores,
        'archivos_renombrados': renombrados,
        'total_renombrados': contador_renombrados
    }

# INTERFAZ PRINCIPAL
st.header("📤 Subida de Archivos")

# Subida de archivos múltiples (todos los tipos)
uploaded_files = st.file_uploader(
    "Selecciona archivos para procesar (JSON de Mantis y archivos con patrón NE######)",
    accept_multiple_files=True,
    help="Puedes seleccionar archivos JSON y otros archivos con formato NE651.pdf, NE999999.xlsx, etc.",
    type=['json', 'pdf', 'xlsx', 'xls', 'txt', 'doc', 'docx', 'jpg', 'png', 'jpeg']
)

# Información adicional
st.info("""
**🔄 Funcionalidad Combinada - Coosalud:**

**Para archivos JSON:**
- ✅ **EXTRAE**: resultState, procesoId, numFactura, codigoUnicoValidacion, fechaRadicacion (con diferentes nombres)
- ✅ **GENERA**: rutaArchivos y resultadosValidacion:[] (formato exacto)
- ✅ **RENOMBRA**: Archivos sin fecha válida → agrega "_sin_fecha"

**Para archivos con patrón NE######:**
- ✅ Convierte `NE651.pdf` → `CUV_NE651.pdf` (Formato Coosalud)
""")

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} archivo(s) listo(s) para procesar")
    
    # Mostrar PREVISUALIZACIÓN de archivos JSON
    with st.expander("🔍 Previsualización de Archivos JSON", expanded=True):
        for i, file in enumerate(uploaded_files):
            if file.name.lower().endswith('.json'):
                try:
                    contenido = json.loads(file.getvalue().decode('utf-8'))
                    
                    st.write(f"**{i+1}. {file.name}**")
                    st.write(f"   - resultState: `{contenido.get('resultState', contenido.get('ResultState', 'No encontrado'))}`")
                    st.write(f"   - procesoId: `{contenido.get('procesoId', contenido.get('ProcesoId', 'No encontrado'))}`")
                    st.write(f"   - numFactura: `{contenido.get('numFactura', contenido.get('NumFactura', 'No encontrado'))}`")
                    st.write(f"   - codigoUnicoValidacion: `{contenido.get('codigoUnicoValidacion', contenido.get('CodigoUnicoValidacion', 'No encontrado'))[:20]}...`" if contenido.get('codigoUnicoValidacion') or contenido.get('CodigoUnicoValidacion') else "   - codigoUnicoValidacion: `No encontrado`")
                    st.write(f"   - fechaRadicacion: `{contenido.get('fechaRadicacion', contenido.get('FechaRadicacion', 'NO TIENE FECHA - Se renombrará'))}`")
                    st.write("---")
                    
                except Exception as e:
                    st.error(f"Error leyendo {file.name}: {str(e)}")
    
    # Botón de procesamiento COMBINADO
    if st.button("🚀 Procesar Todo", type="primary", use_container_width=True):
        with st.spinner("Extrayendo datos originales y procesando archivos..."):
            # Crear directorio temporal
            with tempfile.TemporaryDirectory() as temp_dir:
                # Guardar archivos subidos en directorio temporal
                for uploaded_file in uploaded_files:
                    temp_path = os.path.join(temp_dir, uploaded_file.name)
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getvalue())
                
                # Procesar TODO
                resultados = procesar_todo(temp_dir)
                
                # MOSTRAR RESULTADOS COMBINADOS
                st.markdown("---")
                st.header("📊 Resultados del Procesamiento Combinado")
                
                # RESULTADOS DETALLADOS - JSON
                if resultados['json_procesados'] or resultados['json_errores']:
                    st.subheader("📊 Resultados Conversor JSON")
                    
                    # Mostrar tabla detallada de JSON procesados
                    if resultados['json_procesados']:
                        st.markdown("#### ✅ JSON Procesados Exitosamente")
                        
                        # Crear DataFrame para mejor visualización
                        df_data = []
                        for archivo in resultados['json_procesados']:
                            info = archivo['info_generacion']
                            df_data.append({
                                'Archivo': archivo['nombre'],
                                'resultState': info['resultState'],
                                'procesoId': info['procesoId'],
                                'numFactura': info['numFactura'],
                                'CUV': info['codigoCUV'],
                                'Fecha Radicación': info['fechaRadicacion'],
                                'Estado': archivo['estado']
                            })
                        
                        df = pd.DataFrame(df_data)
                        st.dataframe(df, use_container_width=True)
                        
                        # Mostrar ejemplo de estructura generada
                        st.markdown("#### 🔄 Ejemplo de Estructura Generada")
                        if resultados['json_procesados']:
                            primer_archivo = resultados['json_procesados'][0]
                            info = primer_archivo['info_generacion']
                            
                            ejemplo_estructura = {
                                "resultState": info['resultState'],
                                "procesoId": info['procesoId'],
                                "numFactura": info['numFactura'],
                                "codigoUnicoValidacion": info['codigoCUV'] + "...",
                                "fechaRadicacion": info['fechaRadicacion'],
                                "rutaArchivos": None,
                                "resultadosValidacion": []
                            }
                            
                            st.success(f"**{primer_archivo['nombre']}** - Estructura generada:")
                            st.code(json.dumps(ejemplo_estructura, indent=2), language='json')
                    
                    if resultados['json_errores']:
                        st.markdown("#### ❌ Errores en JSON")
                        for error in resultados['json_errores']:
                            st.error(f"**{error['nombre']}**: {error['error']}")
                
                # RESULTADOS DETALLADOS - RENOMBRADO
                if resultados['archivos_renombrados']:
                    st.subheader("🔢 Resultados Renombrado CUV - Coosalud")
                    
                    # Separar por tipo de resultado
                    renombrados = [r for r in resultados['archivos_renombrados'] if r['tipo'] == 'success']
                    
                    if renombrados:
                        st.markdown("#### ✅ Archivos Renombrados Exitosamente")
                        for resultado in renombrados:
                            st.success(f"**{resultado['original']}** → **{resultado['nuevo']}**")
                
                # PREPARAR DESCARGA COMBINADA
                st.markdown("---")
                st.subheader("📥 Descargar Archivos Procesados")
                
                if resultados['json_procesados'] or resultados['archivos_renombrados']:
                    # Crear ZIP con todos los archivos procesados
                    zip_path = os.path.join(temp_dir, "archivos_procesados_coosalud.zip")
                    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', temp_dir)
                    
                    # Leer el ZIP para descarga
                    with open(zip_path, "rb") as f:
                        zip_data = f.read()
                    
                    st.download_button(
                        label="📦 Descargar TODOS los Archivos (ZIP)",
                        data=zip_data,
                        file_name="archivos_procesados_coosalud.zip",
                        mime="application/zip",
                        use_container_width=True
                    )

else:
    st.info("👆 Por favor, selecciona al menos un archivo para procesar")

# INSTRUCCIONES
with st.expander("📖 Instrucciones de Uso"):
    st.markdown("""
    ### Estructura generada:
    ```json
    {
      "resultState": true,                    // ← Del original
      "procesoId": 790938,                    // ← Del original  
      "numFactura": "NE1315",                 // ← Del original
      "codigoUnicoValidacion": "1043ee6f9...", // ← Del original
      "fechaRadicacion": "2025-08-21T20:42...", // ← Del original
      "rutaArchivos": null,                   // ← Del original
      "resultadosValidacion": []              // ← SIEMPRE array vacío
    }
    ```
    
    **Qué se extrae del original:**
    - ✅ `resultState` (o `ResultState`)
    - ✅ `procesoId` (o `ProcesoId`) 
    - ✅ `numFactura` (o `NumFactura`)
    - ✅ `codigoUnicoValidacion` (o `CodigoUnicoValidacion`)
    - ✅ `fechaRadicacion` (o `FechaRadicacion`)
    - ✅ `rutaArchivos` (o `RutaArchivos`)
    
    **Qué se genera automáticamente:**
    - `resultadosValidacion`: [] (SIEMPRE array vacío)
    
    **Nueva regla especial:**
    - Si el archivo NO tiene `fechaRadicacion` válida → Se renombra agregando "_sin_fecha"
    """)

# FOOTER
st.markdown("---")
st.caption("🔄 Conversor + Renombrador - Coosalud • v8.0 • Extracción con diferentes nombres de campos")
