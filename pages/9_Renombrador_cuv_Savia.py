import streamlit as st
import os
import re
import tempfile
import shutil
from pathlib import Path
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

# Configurar tema y navbar
configure_modern_theme()
st.set_page_config(
    page_title="Renombrador CUV - Savia Salud", 
    page_icon="🔢", 
    layout="wide"
)
modern_navbar()

st.title("🔢 Renombrador CUV - Savia Salud")
st.markdown("Convierte archivos con patrón NE###### a formato NE######_CUV")

# Función de procesamiento
def renombrar_archivos_cuv_savia(directorio):
    resultados = []
    contador = 0
    
    try:
        for archivo in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, archivo)
            
            # Verificar si es un archivo (no carpeta)
            if os.path.isfile(ruta_completa):
                # Buscar el patrón NE seguido de números en el nombre del archivo
                patron = r'(NE\d+)'
                coincidencia = re.search(patron, archivo)
                
                if coincidencia:
                    numero_factura = coincidencia.group(1)  # Extraer el NE651, NE99999999, etc.
                    
                    # Obtener la extensión del archivo
                    nombre_base, extension = os.path.splitext(archivo)
                    
                    # Crear el nuevo nombre: NE651_CUV.ext (formato Savia)
                    nuevo_nombre = f"{numero_factura}_CUV{extension}"
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

# INTERFAZ STREAMLIT
st.header("📤 Subida de Archivos")

# Opción 1: Subir archivos directamente
uploaded_files = st.file_uploader(
    "Selecciona archivos para renombrar (patrón NE######)",
    accept_multiple_files=True,
    help="Archivos con formato: NE651.pdf, NE999999.xlsx, etc."
)

# Información adicional
st.info("""
**ℹ️ Funcionalidad:**
- Convierte archivos con patrón `NE######` a `NE######_CUV`
- Ejemplo: `NE651.pdf` → `NE651_CUV.pdf`
- Procesa múltiples archivos simultáneamente
- No modifica el contenido, solo el nombre
""")

# Mostrar ejemplos de patrones
with st.expander("🔍 Ejemplos de Patrones Válidos"):
    st.markdown("""
    **Patrones que SÍ serán renombrados:**
    - `NE651.pdf` → `NE651_CUV.pdf`
    - `NE999999.xlsx` → `NE999999_CUV.xlsx`
    - `NE123456789.json` → `NE123456789_CUV.json`
    - `documento_NE8888.txt` → `NE8888_CUV.txt`
    
    **Patrones que NO serán renombrados:**
    - `factura_normal.pdf`
    - `NE651_CUV.pdf` (ya está en formato correcto)
    - `CUV_NE651.pdf` (formato Coosalud, no Savia)
    """)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} archivo(s) listo(s) para procesar")
    
    # Mostrar archivos seleccionados
    with st.expander("📋 Archivos Seleccionados", expanded=True):
        for i, file in enumerate(uploaded_files):
            # Verificar si coincide con el patrón
            patron = r'(NE\d+)'
            coincidencia = re.search(patron, file.name)
            estado_patron = "✅ Coincide" if coincidencia else "❌ No coincide"
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
                resultados, contador = renombrar_archivos_cuv_savia(temp_dir)
                
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
                        st.caption(f"Número de factura: {resultado['numero_factura']}")
                
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
                    zip_path = os.path.join(temp_dir, "archivos_cuv_savia_renombrados.zip")
                    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', temp_dir)
                    
                    # Leer el ZIP para descarga
                    with open(zip_path, "rb") as f:
                        zip_data = f.read()
                    
                    # Botón de descarga ZIP
                    st.download_button(
                        label="📦 Descargar Todos los Archivos (ZIP)",
                        data=zip_data,
                        file_name="archivos_cuv_savia.zip",
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
    ### Cómo usar el Renombrador CUV Savia:
    
    1. **Selecciona archivos**: Haz clic en 'Browse files' o arrastra los archivos
    2. **Verifica patrones**: Los archivos deben tener formato `NE######`
    3. **Procesa**: Haz clic en 'Renombrar Archivos'
    4. **Descarga**: Obtén los archivos renombrados individualmente o en ZIP
    
    ### Transformación aplicada:
    - `NE651.ext` → `NE651_CUV.ext`
    - `NE999999.ext` → `NE999999_CUV.ext`
    
    ### Características:
    - ✅ Detecta automáticamente patrones NE######
    - ✅ Convierte a formato Savia: NE######_CUV
    - ✅ Procesamiento masivo simultáneo
    - ✅ Validación de patrones antes del procesamiento
    
    ### Diferencia con otros renombradores:
    - **Savia Salud**: `NE651_CUV.ext` (CUV al final)
    - **Coosalud**: `CUV_NE651.ext` (CUV al inicio)
    - **Coosalud SISPRO**: `CUV_NE651.ext` (de `NE651-CUV.ext`)
    """)

# FOOTER
st.markdown("---")
st.caption("🔢 Renombrador CUV - Savia Salud • v1.0 • Formato NE######_CUV")
