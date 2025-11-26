import streamlit as st
import json
import os
import tempfile
import shutil
from pathlib import Path
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

# Configurar tema y navbar
configure_modern_theme()
st.set_page_config(
    page_title="Conversor Sispro - Coosalud", 
    page_icon="🔄", 
    layout="wide"
)
modern_navbar()

st.title("🔄 Conversor Sispro - Coosalud")
st.markdown("Procesa archivos JSON de Sispro para Coosalud")

# Función de procesamiento (tu lógica adaptada)
def procesar_archivos_sispro(directorio):
    archivos_procesados = []
    errores = []
    
    try:
        for archivo in os.listdir(directorio):
            if archivo.lower().endswith('.json'):
                ruta_completa = os.path.join(directorio, archivo)
                
                try:
                    # Leer el archivo JSON original
                    with open(ruta_completa, 'r', encoding='utf-8') as f:
                        contenido = f.read()
                        datos = json.loads(contenido)
                    
                    # Extraer valores (manejando diferentes nombres de campos)
                    es_valido = datos.get('EsValido', datos.get('esValido', datos.get('ResultState', datos.get('resultState', True))))
                    proceso_id = datos.get('ProcesoId', datos.get('procesoId', 0))
                    numero_doc = datos.get('NumeroDocumento', datos.get('numeroDocumento', datos.get('numFactura', datos.get('NumFactura', ''))))
                    codigo_unico = datos.get('CodigoUnicoValidacion', datos.get('codigoUnicoValidacion', ''))
                    fecha_val = datos.get('FechaValidacion', datos.get('fechaValidacion', datos.get('fechaRadicacion', datos.get('FechaRadicacion', '0000-00-00T00:00:00.0000000'))))
                    doc_ref = datos.get('NumDocumentoReferenciado', datos.get('numDocumentoReferenciado', datos.get('rutaArchivos', datos.get('RutaArchivos', None))))

                    # Procesar la fecha
                    fecha_original = fecha_val
                    if fecha_val == "0000-00-00T00:00:00.0000000" or fecha_val == "0000-00-00T00:00:00":
                        # Renombrar archivo si la fecha está en ceros
                        nombre_base, extension = os.path.splitext(archivo)
                        nuevo_nombre = f"{nombre_base}-SIN FECHA{extension}"
                        nueva_ruta = os.path.join(directorio, nuevo_nombre)
                        os.rename(ruta_completa, nueva_ruta)
                        ruta_completa = nueva_ruta
                        archivo = nuevo_nombre  # Actualizar nombre para el registro
                    else:
                        # Formatear fecha válida (remover timezone offset)
                        if '+' in fecha_val:
                            fecha_val = fecha_val.split('+')[0]

                    # Crear la nueva estructura JSON
                    nuevo_json = {
                        "resultState": es_valido,
                        "procesoId": proceso_id,
                        "numFactura": numero_doc,
                        "codigoUnicoValidacion": codigo_unico,
                        "fechaRadicacion": fecha_val,
                        "rutaArchivos": doc_ref,
                        "resultadosValidacion": []
                    }

                    # Guardar el nuevo JSON con formato
                    with open(ruta_completa, 'w', encoding='utf-8') as f:
                        json_str = json.dumps(nuevo_json, indent=2, ensure_ascii=False)
                        # Asegurar que resultadosValidacion no tenga espacio
                        json_str = json_str.replace('"resultadosValidacion": []', '"resultadosValidacion":[]')
                        f.write(json_str)

                    archivos_procesados.append({
                        'nombre': archivo,
                        'estado': '✅ Procesado',
                        'fecha_original': fecha_original,
                        'fecha_procesada': fecha_val,
                        'proceso_id': proceso_id,
                        'num_factura': numero_doc
                    })
                    
                except Exception as e:
                    errores.append({
                        'nombre': archivo,
                        'error': str(e)
                    })
        
        return archivos_procesados, errores
        
    except Exception as e:
        errores.append({'nombre': 'Sistema', 'error': f"Error general: {str(e)}"})
        return [], errores

# INTERFAZ STREAMLIT
st.header("📤 Subida de Archivos")

# Opción 1: Subir archivos directamente
uploaded_files = st.file_uploader(
    "Selecciona archivos JSON Sispro para procesar",
    type=['json'],
    accept_multiple_files=True,
    help="Puedes seleccionar múltiples archivos JSON de Sispro"
)

# Información adicional
st.info("""
**ℹ️ Este conversor procesa archivos JSON de Sispro y los adapta al formato estándar de Coosalud:**
- Corrige formatos de fecha
- Renombra archivos con fechas inválidas
- Estandariza nombres de campos
- Mantiene la estructura requerida
""")

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} archivo(s) Sispro listo(s) para procesar")
    
    # Mostrar archivos seleccionados
    with st.expander("📋 Archivos Seleccionados", expanded=True):
        for i, file in enumerate(uploaded_files):
            st.write(f"{i+1}. {file.name}")
    
    # Botón de procesamiento
    if st.button("🚀 Procesar Archivos Sispro", type="primary", use_container_width=True):
        with st.spinner("Procesando archivos Sispro..."):
            # Crear directorio temporal
            with tempfile.TemporaryDirectory() as temp_dir:
                # Guardar archivos subidos en directorio temporal
                for uploaded_file in uploaded_files:
                    temp_path = os.path.join(temp_dir, uploaded_file.name)
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getvalue())
                
                # Procesar archivos
                archivos_procesados, errores = procesar_archivos_sispro(temp_dir)
                
                # MOSTRAR RESULTADOS DETALLADOS
                st.markdown("---")
                st.header("📊 Resultados del Procesamiento")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("✅ Archivos Procesados")
                    if archivos_procesados:
                        for archivo in archivos_procesados:
                            with st.container():
                                st.success(f"**{archivo['nombre']}**")
                                col_a, col_b = st.columns(2)
                                with col_a:
                                    st.caption(f"📅 Fecha: {archivo['fecha_procesada']}")
                                    st.caption(f"🆔 Proceso: {archivo['proceso_id']}")
                                with col_b:
                                    st.caption(f"📄 Factura: {archivo['num_factura']}")
                                st.markdown("---")
                    else:
                        st.info("No se procesaron archivos")
                
                with col2:
                    st.subheader("❌ Errores")
                    if errores:
                        for error in errores:
                            st.error(f"**{error['nombre']}**")
                            st.caption(f"Error: {error['error']}")
                            st.markdown("---")
                    else:
                        st.success("✅ No hubo errores en el procesamiento")
                
                # ESTADÍSTICAS
                st.markdown("---")
                st.subheader("📈 Estadísticas del Procesamiento")
                
                col_stats1, col_stats2, col_stats3, col_stats4 = st.columns(4)
                with col_stats1:
                    st.metric("Total Archivos", len(uploaded_files))
                with col_stats2:
                    st.metric("Procesados", len(archivos_procesados))
                with col_stats3:
                    st.metric("Errores", len(errores))
                with col_stats4:
                    tasa_exito = (len(archivos_procesados) / len(uploaded_files)) * 100 if uploaded_files else 0
                    st.metric("Tasa Éxito", f"{tasa_exito:.1f}%")
                
                # PREPARAR DESCARGA
                st.markdown("---")
                st.subheader("📥 Descargar Archivos Procesados")
                
                if archivos_procesados:
                    # Crear ZIP con archivos procesados
                    zip_path = os.path.join(temp_dir, "archivos_sispro_procesados.zip")
                    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', temp_dir)
                    
                    # Leer el ZIP para descarga
                    with open(zip_path, "rb") as f:
                        zip_data = f.read()
                    
                    # Botón de descarga ZIP
                    st.download_button(
                        label="📦 Descargar Todos los Archivos (ZIP)",
                        data=zip_data,
                        file_name="archivos_sispro_procesados_coosalud.zip",
                        mime="application/zip",
                        use_container_width=True
                    )
                    
                    # Descargas individuales
                    st.markdown("**Descargas Individuales:**")
                    cols = st.columns(3)
                    for i, archivo in enumerate(archivos_procesados):
                        with cols[i % 3]:
                            file_path = os.path.join(temp_dir, archivo['nombre'])
                            with open(file_path, "rb") as f:
                                file_data = f.read()
                            
                            st.download_button(
                                label=f"📄 {archivo['nombre'][:20]}...",
                                data=file_data,
                                file_name=archivo['nombre'],
                                mime="application/json",
                                key=f"download_{i}"
                            )
                else:
                    st.warning("No hay archivos procesados para descargar")

else:
    st.info("👆 Por favor, selecciona al menos un archivo JSON Sispro para procesar")

# INSTRUCCIONES ESPECÍFICAS PARA SISPRO
with st.expander("📖 Instrucciones de Uso - Sispro"):
    st.markdown("""
    ### Cómo usar el Conversor Sispro:
    
    1. **Selecciona archivos JSON Sispro**: Archivos generados por el sistema Sispro
    2. **Procesa**: Haz clic en 'Procesar Archivos Sispro'
    3. **Revisa resultados**: Verifica el procesamiento de cada archivo
    4. **Descarga**: Obtén los archivos en formato estándar Coosalud
    
    ### Transformaciones aplicadas:
    - ✅ **Campos estandarizados**: Adapta nombres de campos al estándar Coosalud
    - ✅ **Fechas corregidas**: Formatea y valida fechas de radicación
    - ✅ **Renombrado automático**: Archivos con fechas inválidas se renombran
    - ✅ **Estructura uniforme**: JSON con estructura consistente
    
    ### Campos procesados:
    - `EsValido` → `resultState`
    - `ProcesoId` → `procesoId` 
    - `NumeroDocumento` → `numFactura`
    - `CodigoUnicoValidacion` → `codigoUnicoValidacion`
    - `FechaValidacion` → `fechaRadicacion`
    - `NumDocumentoReferenciado` → `rutaArchivos`
    """)

# FOOTER
st.markdown("---")
st.caption("🔄 Conversor Sispro - Coosalud • v1.0 • Especializado en transformación JSON Sispro")
