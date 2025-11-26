import streamlit as st
import os
import tempfile
import shutil
from pathlib import Path
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

# Configurar tema y navbar
configure_modern_theme()
st.set_page_config(
    page_title="Renombrador RIPS - Savia Salud", 
    page_icon="📋", 
    layout="wide"
)
modern_navbar()

st.title("📋 Renombrador RIPS - Savia Salud")
st.markdown("Elimina '_RIPS' de los nombres de archivo automáticamente")

# Función de procesamiento
def renombrar_archivos_rips(directorio):
    resultados = []
    contador = 0
    
    try:
        for archivo in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, archivo)
            
            # Verificar si es un archivo (no carpeta)
            if os.path.isfile(ruta_completa):
                # Verificar si el archivo contiene "_RIPS"
                if "_RIPS" in archivo:
                    # Crear el nuevo nombre eliminando "_RIPS"
                    nuevo_nombre = archivo.replace("_RIPS", "")
                    nueva_ruta = os.path.join(directorio, nuevo_nombre)
                    
                    # Renombrar el archivo
                    try:
                        os.rename(ruta_completa, nueva_ruta)
                        resultados.append({
                            'original': archivo,
                            'nuevo': nuevo_nombre,
                            'estado': '✅ Renombrado',
                            'tipo': 'success'
                        })
                        contador += 1
                    except Exception as e:
                        resultados.append({
                            'original': archivo,
                            'nuevo': nuevo_nombre,
                            'estado': f'❌ Error: {str(e)}',
                            'tipo': 'error'
                        })
                else:
                    resultados.append({
                        'original': archivo,
                        'nuevo': archivo,
                        'estado': 'ℹ Sin _RIPS (no se renombra)',
                        'tipo': 'info'
                    })
        
        return resultados, contador
        
    except Exception as e:
        st.error(f"Error general: {str(e)}")
        return [], 0

# INTERFAZ STREAMLIT
st.header("📤 Subida de Archivos")

# Opción 1: Subir archivos directamente
uploaded_files = st.file_uploader(
    "Selecciona archivos para renombrar (eliminar '_RIPS')",
    accept_multiple_files=True,
    help="Puedes seleccionar múltiples archivos de cualquier tipo"
)

# Información adicional
st.info("""
**ℹ️ Funcionalidad:**
- Elimina automáticamente "_RIPS" de los nombres de archivo
- Mantiene la extensión original del archivo
- Procesa múltiples archivos simultáneamente
- No modifica el contenido, solo el nombre
""")

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} archivo(s) listo(s) para procesar")
    
    # Mostrar archivos seleccionados
    with st.expander("📋 Archivos Seleccionados", expanded=True):
        for i, file in enumerate(uploaded_files):
            st.write(f"{i+1}. {file.name}")
    
    # Botón de procesamiento
    if st.button("🚀 Renombrar Archivos", type="primary", use_container_width=True):
        with st.spinner("Procesando archivos..."):
            # Crear directorio temporal
            with tempfile.TemporaryDirectory() as temp_dir:
                # Guardar archivos subidos en directorio temporal
                for uploaded_file in uploaded_files:
                    temp_path = os.path.join(temp_dir, uploaded_file.name)
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getvalue())
                
                # Procesar archivos
                resultados, contador = renombrar_archivos_rips(temp_dir)
                
                # MOSTRAR RESULTADOS
                st.markdown("---")
                st.header("📊 Resultados del Procesamiento")
                
                # Estadísticas rápidas
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Archivos", len(uploaded_files))
                with col2:
                    st.metric("Renombrados", contador)
                with col3:
                    tasa_renombre = (contador / len(uploaded_files)) * 100 if uploaded_files else 0
                    st.metric("Tasa Renombre", f"{tasa_renombre:.1f}%")
                
                # Resultados detallados
                st.subheader("📋 Detalle de Archivos")
                
                for resultado in resultados:
                    if resultado['tipo'] == 'success':
                        st.success(f"**{resultado['original']}** → **{resultado['nuevo']}**")
                    elif resultado['tipo'] == 'error':
                        st.error(f"**{resultado['original']}** → {resultado['estado']}")
                    else:
                        st.info(f"**{resultado['original']}** → {resultado['estado']}")
                
                # PREPARAR DESCARGA
                st.markdown("---")
                st.subheader("📥 Descargar Archivos Renombrados")
                
                if contador > 0:
                    # Crear ZIP con archivos renombrados
                    zip_path = os.path.join(temp_dir, "archivos_renombrados_savia.zip")
                    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', temp_dir)
                    
                    # Leer el ZIP para descarga
                    with open(zip_path, "rb") as f:
                        zip_data = f.read()
                    
                    # Botón de descarga ZIP
                    st.download_button(
                        label="📦 Descargar Todos los Archivos (ZIP)",
                        data=zip_data,
                        file_name="archivos_renombrados_savia.zip",
                        mime="application/zip",
                        use_container_width=True
                    )
                    
                    # Descargas individuales
                    st.markdown("**Descargas Individuales:**")
                    cols = st.columns(3)
                    archivos_renombrados = [r for r in resultados if r['tipo'] == 'success']
                    
                    for i, archivo in enumerate(archivos_renombrados):
                        with cols[i % 3]:
                            file_path = os.path.join(temp_dir, archivo['nuevo'])
                            if os.path.exists(file_path):
                                with open(file_path, "rb") as f:
                                    file_data = f.read()
                                
                                st.download_button(
                                    label=f"📄 {archivo['nuevo'][:20]}...",
                                    data=file_data,
                                    file_name=archivo['nuevo'],
                                    mime="application/octet-stream",
                                    key=f"download_{i}"
                                )
                else:
                    st.warning("No hay archivos renombrados para descargar")

else:
    st.info("👆 Por favor, selecciona al menos un archivo para procesar")

# INSTRUCCIONES
with st.expander("📖 Instrucciones de Uso"):
    st.markdown("""
    ### Cómo usar el Renombrador RIPS Savia:
    
    1. **Selecciona archivos**: Haz clic en 'Browse files' o arrastra los archivos
    2. **Revisa los archivos**: Verifica que sean los correctos en la lista
    3. **Procesa**: Haz clic en 'Renombrar Archivos'
    4. **Descarga**: Obtén los archivos renombrados individualmente o en ZIP
    
    ### Ejemplos de renombrado:
    - `factura_RIPS.pdf` → `factura.pdf`
    - `reporte_RIPS.xlsx` → `reporte.xlsx`
    - `datos_RIPS.csv` → `datos.csv`
    
    ### Características:
    - ✅ Elimina automáticamente "_RIPS" del nombre
    - ✅ Mantiene la extensión original
    - ✅ Procesamiento masivo simultáneo
    - ✅ Descarga en ZIP o individual
    """)

# FOOTER
st.markdown("---")
st.caption("📋 Renombrador RIPS - Savia Salud • v1.0 • Eliminación automática de '_RIPS'")
