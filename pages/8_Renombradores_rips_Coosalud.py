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
    page_title="Renombrador RIPS - Coosalud", 
    page_icon="📋", 
    layout="wide"
)
modern_navbar()

st.title("📋 Renombrador RIPS - Coosalud")
st.markdown("Elimina '_RIPS' de los nombres de archivos")

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
                        'estado': 'ℹ No contiene _RIPS (no se renombra)',
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
    "Selecciona archivos para renombrar (deben contener '_RIPS' en el nombre)",
    accept_multiple_files=True,
    help="Archivos con formato: archivo_RIPS.pdf, documento_RIPS.xlsx, etc."
)

# Información adicional
st.info("""
**ℹ️ Funcionalidad:**
- Elimina el texto '_RIPS' de los nombres de archivos
- Ejemplo: `archivo_RIPS.pdf` → `archivo.pdf`
- Procesa múltiples archivos simultáneamente
- No modifica el contenido, solo el nombre
""")

# Mostrar ejemplos de patrones
with st.expander("🔍 Ejemplos de Transformación"):
    st.markdown("""
    **Archivos que SÍ serán renombrados:**
    - `factura_RIPS.pdf` → `factura.pdf`
    - `documento_RIPS.xlsx` → `documento.xlsx`
    - `reporte_RIPS.json` → `reporte.json`
    - `datos_RIPS_2024.txt` → `datos_2024.txt`
    
    **Archivos que NO serán renombrados:**
    - `factura_normal.pdf` (no contiene _RIPS)
    - `archivo.pdf` (ya está sin _RIPS)
    - `RIPS_solo.pdf` (no contiene _RIPS completo)
    """)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} archivo(s) listo(s) para procesar")
    
    # Mostrar archivos seleccionados
    with st.expander("📋 Archivos Seleccionados", expanded=True):
        for i, file in enumerate(uploaded_files):
            # Verificar si contiene "_RIPS"
            contiene_rips = "_RIPS" in file.name
            estado_patron = "✅ Contiene _RIPS" if contiene_rips else "❌ No contiene _RIPS"
            st.write(f"{i+1}. {file.name} - {estado_patron}")
    
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
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Archivos", len(uploaded_files))
                with col2:
                    st.metric("Renombrados", contador)
                with col3:
                    no_coinciden = len(uploaded_files) - contador
                    st.metric("No Coinciden", no_coinciden)
                with col4:
                    tasa_renombre = (contador / len(uploaded_files)) * 100 if uploaded_files else 0
                    st.metric("Tasa Renombre", f"{tasa_renombre:.1f}%")
                
                # Resultados detallados
                st.subheader("📋 Detalle de Archivos")
                
                # Separar por tipo de resultado
                renombrados = [r for r in resultados if r['tipo'] == 'success']
                errores = [r for r in resultados if r['tipo'] == 'error']
                info = [r for r in resultados if r['tipo'] == 'info']
                
                if renombrados:
                    st.markdown("#### ✅ Archivos Renombrados Exitosamente")
                    for resultado in renombrados:
                        st.success(f"**{resultado['original']}** → **{resultado['nuevo']}**")
                
                if errores:
                    st.markdown("#### ❌ Errores en Renombrado")
                    for resultado in errores:
                        st.error(f"**{resultado['original']}** → {resultado['estado']}")
                
                if info:
                    st.markdown("#### ℹ️ Archivos No Procesados")
                    for resultado in info:
                        st.info(f"**{resultado['original']}** → {resultado['estado']}")
                
                # PREPARAR DESCARGA
                st.markdown("---")
                st.subheader("📥 Descargar Archivos Renombrados")
                
                if contador > 0:
                    # Crear ZIP con archivos renombrados
                    zip_path = os.path.join(temp_dir, "archivos_rips_renombrados.zip")
                    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', temp_dir)
                    
                    # Leer el ZIP para descarga
                    with open(zip_path, "rb") as f:
                        zip_data = f.read()
                    
                    # Botón de descarga ZIP
                    st.download_button(
                        label="📦 Descargar Todos los Archivos (ZIP)",
                        data=zip_data,
                        file_name="archivos_rips_coosalud.zip",
                        mime="application/zip",
                        use_container_width=True
                    )
                    
                    # Descargas individuales
                    st.markdown("**Descargas Individuales:**")
                    cols = st.columns(3)
                    
                    for i, archivo in enumerate(renombrados):
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
    ### Cómo usar el Renombrador RIPS:
    
    1. **Selecciona archivos**: Haz clic en 'Browse files' o arrastra los archivos
    2. **Verifica nombres**: Los archivos deben contener '_RIPS' en el nombre
    3. **Procesa**: Haz clic en 'Renombrar Archivos'
    4. **Descarga**: Obtén los archivos renombrados individualmente o en ZIP
    
    ### Transformación aplicada:
    - `archivo_RIPS.ext` → `archivo.ext`
    - `documento_RIPS.ext` → `documento.ext`
    
    ### Características:
    - ✅ Detecta automáticamente archivos con '_RIPS'
    - ✅ Elimina '_RIPS' manteniendo el resto del nombre
    - ✅ Procesamiento masivo simultáneo
    - ✅ Validación de nombres antes del procesamiento
    
    ### Casos especiales:
    - Si hay múltiples '_RIPS', solo elimina el primero
    - Funciona con cualquier tipo de archivo y extensión
    - No modifica archivos que ya no tienen '_RIPS'
    """)

# FOOTER
st.markdown("---")
st.caption("📋 Renombrador RIPS - Coosalud • v1.0 • Eliminación de '_RIPS' en nombres de archivos")
