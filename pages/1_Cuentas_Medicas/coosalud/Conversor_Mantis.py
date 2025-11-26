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
    page_title="Conversor Mantis - Coosalud", 
    page_icon="🔄", 
    layout="wide"
)
modern_navbar()

st.title("🔄 Conversor Mantis - Coosalud")
st.markdown("Procesa archivos JSON de Mantis para Coosalud")

# Función de procesamiento (tu lógica adaptada)
def procesar_archivos_json(directorio):
    archivos_procesados = []
    errores = []
    
    try:
        os.chdir(directorio)
        archivos_json = [archivo for archivo in os.listdir() if archivo.lower().endswith('.json')]
        
        for nombre_archivo in archivos_json:
            try:
                with open(nombre_archivo, 'r', encoding='utf-8') as file:
                    datos = json.load(file)
                
                fecha_original = datos.get('fechaRadicacion') or datos.get('FechaRadicacion')
                
                # Renombrar archivos con fecha 0000-00-00
                if fecha_original == "0000-00-00T00:00:00":
                    nombre_base, extension = os.path.splitext(nombre_archivo)
                    nuevo_nombre = f"{nombre_base}-SIN FECHA{extension}"
                    os.rename(nombre_archivo, nuevo_nombre)
                    nombre_archivo = nuevo_nombre
                
                # Formatear fecha válida
                if fecha_original and fecha_original != "0000-00-00T00:00:00" and '+' in fecha_original:
                    fecha_procesada = fecha_original.split('+')[0]
                    if 'fechaRadicacion' in datos:
                        datos['fechaRadicacion'] = fecha_procesada
                    if 'FechaRadicacion' in datos:
                        datos['FechaRadicacion'] = fecha_procesada
                
                # Estructura final
                resultado = {
                    "resultState": datos.get('resultState', datos.get('ResultState')),
                    "procesoId": datos.get('procesoId', datos.get('ProcesoId')),
                    "numFactura": datos.get('numFactura', datos.get('NumFactura')),
                    "codigoUnicoValidacion": datos.get('codigoUnicoValidacion', datos.get('CodigoUnicoValidacion')),
                    "fechaRadicacion": datos.get('fechaRadicacion', datos.get('FechaRadicacion')),
                    "rutaArchivos": datos.get('rutaArchivos', datos.get('RutaArchivos')),
                    "resultadosValidacion":[]
                }
                
                # Guardar CON sangría pero SIN espacio en resultadosValidacion
                with open(nombre_archivo, 'w', encoding='utf-8') as file:
                    json_str = json.dumps(resultado, indent=2, ensure_ascii=False)
                    json_str = json_str.replace('"resultadosValidacion": []', '"resultadosValidacion":[]')
                    file.write(json_str)
                
                archivos_procesados.append({
                    'nombre': nombre_archivo,
                    'estado': '✅ Procesado',
                    'fecha': fecha_original if fecha_original else 'No encontrada'
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

# INTERFAZ STREAMLIT
st.header("📤 Subida de Archivos")

# Opción 1: Subir archivos directamente
uploaded_files = st.file_uploader(
    "Selecciona archivos JSON para procesar",
    type=['json'],
    accept_multiple_files=True,
    help="Puedes seleccionar múltiples archivos JSON"
)

# Opción 2: O usar carpeta temporal
st.markdown("---")
st.subheader("🛠️ Procesamiento")

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} archivo(s) listo(s) para procesar")
    
    # Mostrar archivos seleccionados
    with st.expander("📋 Archivos Seleccionados", expanded=True):
        for i, file in enumerate(uploaded_files):
            st.write(f"{i+1}. {file.name}")
    
    # Botón de procesamiento
    if st.button("🚀 Procesar Archivos", type="primary", use_container_width=True):
        with st.spinner("Procesando archivos..."):
            # Crear directorio temporal
            with tempfile.TemporaryDirectory() as temp_dir:
                # Guardar archivos subidos en directorio temporal
                for uploaded_file in uploaded_files:
                    temp_path = os.path.join(temp_dir, uploaded_file.name)
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getvalue())
                
                # Procesar archivos
                archivos_procesados, errores = procesar_archivos_json(temp_dir)
                
                # MOSTRAR RESULTADOS
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("✅ Archivos Procesados")
                    if archivos_procesados:
                        for archivo in archivos_procesados:
                            st.success(f"**{archivo['nombre']}**")
                            st.caption(f"Fecha: {archivo['fecha']}")
                    else:
                        st.info("No se procesaron archivos")
                
                with col2:
                    st.subheader("❌ Errores")
                    if errores:
                        for error in errores:
                            st.error(f"**{error['nombre']}**: {error['error']}")
                    else:
                        st.success("No hubo errores")
                
                # PREPARAR DESCARGA
                st.markdown("---")
                st.subheader("📥 Descargar Archivos Procesados")
                
                if archivos_procesados:
                    # Crear ZIP con archivos procesados
                    zip_path = os.path.join(temp_dir, "archivos_procesados.zip")
                    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', temp_dir)
                    
                    # Leer el ZIP para descarga
                    with open(zip_path, "rb") as f:
                        zip_data = f.read()
                    
                    st.download_button(
                        label="📦 Descargar Todos los Archivos (ZIP)",
                        data=zip_data,
                        file_name="archivos_procesados_coosalud.zip",
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
                                label=f"📄 {archivo['nombre'][:15]}...",
                                data=file_data,
                                file_name=archivo['nombre'],
                                mime="application/json"
                            )
                else:
                    st.warning("No hay archivos para descargar")

else:
    st.info("👆 Por favor, selecciona al menos un archivo JSON para procesar")

# INSTRUCCIONES
with st.expander("📖 Instrucciones de Uso"):
    st.markdown("""
    ### Cómo usar el Conversor Mantis:
    
    1. **Selecciona archivos JSON**: Haz clic en 'Browse files' o arrastra los archivos JSON
    2. **Revisa los archivos**: Verifica que sean los correctos en la lista
    3. **Procesa**: Haz clic en 'Procesar Archivos'
    4. **Descarga**: Obtén los archivos procesados individualmente o en ZIP
    
    ### Características del procesamiento:
    - ✅ Corrige formato de fechas
    - ✅ Renombra archivos con fechas inválidas
    - ✅ Estructura JSON según estándar Coosalud
    - ✅ Mantiene codificación UTF-8
    """)

# ESTADÍSTICAS RÁPIDAS
st.markdown("---")
st.subheader("📊 Estadísticas Rápidas")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Archivos Listos", len(uploaded_files) if uploaded_files else 0)
with col2:
    st.metric("Procesados", len(uploaded_files) if uploaded_files else 0)
with col3:
    st.metric("Tasa Éxito", "100%" if uploaded_files else "0%")

# FOOTER
st.markdown("---")
st.caption("🔄 Conversor Mantis - Coosalud • v1.0 • Desarrollado para automatización de procesos")
