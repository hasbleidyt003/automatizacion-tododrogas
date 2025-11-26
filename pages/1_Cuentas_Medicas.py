import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

# IMPORTAR EL NAVBAR - ESTO FALTABA
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

# Configurar tema moderno
configure_modern_theme()

# Configurar página
st.set_page_config(
    page_title="Cuentas Médicas - TodoDrogas",
    page_icon="📋",
    layout="wide"
)

# LLAMAR EL NAVBAR - ESTO FALTABA
modern_navbar()

# Título de la página
st.title("📋 Cuentas Médicas")
st.markdown("Automatización de procesos para cuentas médicas")

# SECCIÓN DE PROCESAMIENTO DE ARCHIVOS
st.header("🔄 Procesamiento de Archivos")

# Pestañas para diferentes procesos
tab1, tab2, tab3 = st.tabs([
    "SAVIA & COOSALUD - Conversores JSON", 
    "SAVIA & COOSALUD - Renombradores", 
    "SALUD TOTAL - Procesador OCR y Renombrador"
])

with tab1:
    st.subheader("Conversores JSON - SAVIA & COOSALUD")
    st.info("Procesa archivos JSON para conversión de formatos")
    
    uploaded_file = st.file_uploader(
        "Sube archivo JSON para procesar", 
        type=['json'],
        key="conversor_json"
    )
    
    if uploaded_file:
        st.success(f"✅ Archivo {uploaded_file.name} cargado correctamente")
        
        col1, col2 = st.columns(2)
        
        with col1:
            proceso_type = st.selectbox(
                "Tipo de procesamiento",
                ["Validación de estructura", "Conversión de formatos", "Extracción de datos"],
                key="proceso_json"
            )
        
        with col2:
            if st.button("🔄 Procesar JSON", use_container_width=True):
                with st.spinner("Procesando archivo JSON..."):
                    # Simulación de procesamiento
                    import time
                    time.sleep(2)
                    st.success("✅ Procesamiento JSON completado exitosamente!")
                    
                    # Simular archivo de descarga
                    st.download_button(
                        label="📥 Descargar Archivo Procesado",
                        data="contenido simulado del archivo procesado",
                        file_name=f"procesado_{uploaded_file.name}",
                        mime="application/json"
                    )

with tab2:
    st.subheader("Renombradores RIPS y CUV - SAVIA & COOSALUD")
    st.info("Renombra archivos según estándares RIPS y CUV")
    
    uploaded_files = st.file_uploader(
        "Sube archivos para renombrar", 
        type=['xlsx', 'xls', 'csv', 'txt', 'json'],
        accept_multiple_files=True,
        key="renombrador"
    )
    
    if uploaded_files:
        st.write(f"📁 Archivos seleccionados: {len(uploaded_files)}")
        
        naming_convention = st.selectbox(
            "Estándar de renombrado",
            ["RIPS - Facturación", "CUV - Codificación", "Ambos estándares"],
            key="naming_convention"
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 Aplicar RIPS", use_container_width=True):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for i, file in enumerate(uploaded_files):
                    progress = (i + 1) / len(uploaded_files)
                    progress_bar.progress(progress)
                    status_text.text(f"Aplicando RIPS a {file.name}...")
                    # Simular procesamiento
                    import time
                    time.sleep(0.5)
                
                st.success("✅ Estándar RIPS aplicado exitosamente!")
        
        with col2:
            if st.button("🔄 Aplicar CUV", use_container_width=True):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for i, file in enumerate(uploaded_files):
                    progress = (i + 1) / len(uploaded_files)
                    progress_bar.progress(progress)
                    status_text.text(f"Aplicando CUV a {file.name}...")
                    # Simular procesamiento
                    import time
                    time.sleep(0.5)
                
                st.success("✅ Estándar CUV aplicado exitosamente!")

with tab3:
    st.subheader("Procesador OCR y Renombrador - SALUD TOTAL")
    st.info("Procesa documentos escaneados (PDF/Imágenes) con OCR y renombra archivos automáticamente")
    
    # Subida de archivos escaneados para OCR
    ocr_files = st.file_uploader(
        "Sube documentos escaneados (PDF o imágenes)", 
        type=['pdf', 'jpg', 'jpeg', 'png'],
        accept_multiple_files=True,
        key="ocr_salud_total"
    )
    
    if ocr_files:
        st.write(f"📄 Documentos escaneados cargados: {len(ocr_files)}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Configuración OCR
            st.subheader("Configuración OCR")
            ocr_language = st.selectbox(
                "Idioma para OCR",
                ["Español", "Inglés", "Español/Inglés"],
                key="ocr_language_salud"
            )
            
            extraction_type = st.selectbox(
                "Tipo de extracción",
                ["Datos estructurados", "Texto completo", "Campos específicos"],
                key="extraction_type"
            )
        
        with col2:
            # Configuración renombrado
            st.subheader("Configuración Renombrado")
            auto_rename = st.checkbox("Renombrado automático", value=True)
            
            if auto_rename:
                rename_pattern = st.selectbox(
                    "Patrón de renombrado",
                    ["Nombre original + fecha", "Secuencial + contenido", "Personalizado"],
                    key="rename_pattern"
                )
        
        # Botón de procesamiento único para OCR y renombrado
        if st.button("🔍 Procesar OCR y Renombrar", use_container_width=True):
            with st.spinner("Procesando documentos escaneados con OCR y aplicando renombrado..."):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for i, file in enumerate(ocr_files):
                    progress = (i + 1) / len(ocr_files)
                    progress_bar.progress(progress)
                    status_text.text(f"Procesando {file.name}...")
                    # Simular procesamiento combinado
                    import time
                    time.sleep(1)
                
                st.success("✅ Procesamiento OCR y renombrado completado!")
                
                # Mostrar resultados combinados
                st.subheader("Resultados del Procesamiento:")
                for i, file in enumerate(ocr_files):
                    st.write(f"• **{file.name}** → OCR procesado + renombrado correctamente")

# SECCIÓN DE ESTADÍSTICAS Y MÉTRICAS
st.header("📊 Métricas y Estadísticas")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Archivos Procesados Hoy",
        value="24",
        delta="+5 vs ayer"
    )

with col2:
    st.metric(
        label="Tasa de Éxito",
        value="98.2%",
        delta="+0.5%"
    )

with col3:
    st.metric(
        label="Tiempo Promedio",
        value="45s",
        delta="-10s"
    )

# GRÁFICO DE ACTIVIDAD (SIMULADO)
st.subheader("Actividad Reciente")

# Crear datos de ejemplo para el gráfico
try:
    dates = pd.date_range(start='2024-01-01', end='2024-01-30', freq='D')
    activity_data = pd.DataFrame({
        'Fecha': dates,
        'Archivos': np.random.randint(10, 100, len(dates)),
        'Errores': np.random.randint(0, 5, len(dates))
    })
    
    fig = px.line(
        activity_data, 
        x='Fecha', 
        y='Archivos',
        title='Archivos Procesados por Día',
        color_discrete_sequence=['#0066cc']
    )
    
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=300
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
except Exception as e:
    st.error(f"Error al generar gráfico: {e}")

# SECCIÓN DE HISTORIAL
st.header("📋 Historial de Procesos")

# Datos de ejemplo para el historial
historial_data = {
    'Fecha': ['2024-01-15 10:30', '2024-01-15 11:15', '2024-01-14 16:45'],
    'Archivo': ['datos_savia.json', 'facturas_rips.csv', 'historias_salud.pdf'],
    'Proceso': ['Procesamiento JSON', 'Renombrado RIPS', 'OCR + Renombrado'],
    'Estado': ['✅ Completado', '✅ Completado', '⚠️ Advertencias'],
    'Usuario': ['admin', 'operador1', 'operador2']
}

historial_df = pd.DataFrame(historial_data)
st.dataframe(historial_df, use_container_width=True)

# INSTRUCCIONES DE USO ACTUALIZADAS
with st.expander("📖 Instrucciones de Uso - Actualizadas"):
    st.markdown("""
    ### Guía Rápida Actualizada:
    
    **SAVIA & COOSALUD - Conversores JSON:**
    - Sube archivos en formato JSON
    - Selecciona el tipo de procesamiento (validación, conversión, extracción)
    - Descarga el archivo procesado
    
    **SAVIA & COOSALUD - Renombradores:**
    - Selecciona múltiples archivos
    - Aplica estándares RIPS (facturación) o CUV (codificación)
    - Los archivos se renombrán según el estándar seleccionado
    
    **SALUD TOTAL - Procesador OCR y Renombrador:**
    - Sube documentos escaneados (PDF o imágenes)
    - Configura el idioma y tipo de extracción OCR
    - El sistema procesa OCR y aplica renombrado automáticamente
    - **Nota:** Esta automatización combina OCR y renombrado en un solo proceso
    
    ### Formatos de Archivo:
    - **JSON:** Para procesamiento de datos estructurados (SAVIA & COOSALUD)
    - **PDF/Imágenes:** Para procesamiento OCR en Salud Total
    - **Excel/CSV:** Para renombrado en SAVIA & COOSALUD
    """)

# FOOTER
st.markdown("---")
st.markdown(
    "**Cuentas Médicas** • Sistema de Automatización TodoDrogas • "
    "Para soporte técnico contacte al administrador del sistema."
)
