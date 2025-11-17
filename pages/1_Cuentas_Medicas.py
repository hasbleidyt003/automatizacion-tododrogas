import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

# Configurar página
st.set_page_config(
    page_title="Cuentas Médicas - TodoDrogas",
    page_icon="📋",
    layout="wide"
)

# Título de la página
st.title("📋 Cuentas Médicas")
st.markdown("Automatización de procesos para cuentas médicas")

# SECCIÓN DE PROCESAMIENTO DE ARCHIVOS
st.header("🔄 Procesamiento de Archivos")

# Pestañas para diferentes procesos
tab1, tab2, tab3, tab4 = st.tabs([
    "SAVIA & COOSALUD - Conversores", 
    "SAVIA & COOSALUD - Renombradores", 
    "SALUD TOTAL - Procesador OCR", 
    "SALUD TOTAL - Renombrador"
])

with tab1:
    st.subheader("Conversores MANTIS/SISPRO")
    st.info("Convierte archivos entre formatos MANTIS y SISPRO")
    
    uploaded_file = st.file_uploader(
        "Sube archivo para conversión", 
        type=['xlsx', 'xls', 'csv'],
        key="conversor"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        conversion_type = st.selectbox(
            "Tipo de conversión",
            ["MANTIS a SISPRO", "SISPRO a MANTIS"],
            key="conversion_type"
        )
    
    with col2:
        if uploaded_file:
            if st.button("🔄 Convertir Archivo", use_container_width=True):
                with st.spinner("Procesando conversión..."):
                    # Simulación de procesamiento
                    import time
                    time.sleep(2)
                    st.success("✅ Conversión completada exitosamente!")
                    
                    # Simular archivo de descarga
                    st.download_button(
                        label="📥 Descargar Archivo Convertido",
                        data="contenido simulado del archivo convertido",
                        file_name=f"convertido_{uploaded_file.name}",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

with tab2:
    st.subheader("Renombradores CUV/RIPS")
    st.info("Renombra archivos según estándares CUV y RIPS")
    
    uploaded_files = st.file_uploader(
        "Sube archivos para renombrar", 
        type=['xlsx', 'xls', 'csv', 'txt'],
        accept_multiple_files=True,
        key="renombrador"
    )
    
    if uploaded_files:
        st.write(f"📁 Archivos seleccionados: {len(uploaded_files)}")
        
        naming_convention = st.selectbox(
            "Convención de nombres",
            ["CUV - Estándar", "RIPS - Facturación", "Personalizado"],
            key="naming_convention"
        )
        
        if st.button("🔄 Renombrar Archivos", use_container_width=True):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, file in enumerate(uploaded_files):
                progress = (i + 1) / len(uploaded_files)
                progress_bar.progress(progress)
                status_text.text(f"Procesando {file.name}...")
                # Simular procesamiento
                import time
                time.sleep(0.5)
            
            st.success("✅ Todos los archivos han sido renombrados!")
            
            # Mostrar preview de nombres nuevos
            st.subheader("Preview de nombres nuevos:")
            for i, file in enumerate(uploaded_files):
                new_name = f"renamed_{i+1}_{file.name}"
                st.write(f"• {file.name} → **{new_name}**")

with tab3:
    st.subheader("Procesador OCR")
    st.info("Procesa imágenes y PDFs mediante reconocimiento óptico de caracteres")
    
    ocr_files = st.file_uploader(
        "Sube imágenes o PDFs para OCR", 
        type=['jpg', 'jpeg', 'png', 'pdf'],
        accept_multiple_files=True,
        key="ocr"
    )
    
    if ocr_files:
        col1, col2 = st.columns(2)
        
        with col1:
            ocr_language = st.selectbox(
                "Idioma del texto",
                ["Español", "Inglés", "Español/Inglés"],
                key="ocr_language"
            )
        
        with col2:
            output_format = st.selectbox(
                "Formato de salida",
                ["Excel (.xlsx)", "CSV (.csv)", "Texto (.txt)"],
                key="output_format"
            )
        
        if st.button("🔍 Procesar con OCR", use_container_width=True):
            with st.spinner("Extrayendo texto de los documentos..."):
                import time
                time.sleep(3)
                
                st.success("✅ Procesamiento OCR completado!")
                
                # Simular resultados
                st.subheader("Texto extraído (ejemplo):")
                st.text_area(
                    "Texto detectado:",
                    "EJEMPLO DE TEXTO EXTRAÍDO MEDIANTE OCR:\n\n"
                    "FACTURA No: 12345\n"
                    "Fecha: 15/Nov/2023\n"
                    "Paciente: Juan Pérez\n"
                    "Servicio: Consulta médica\n"
                    "Valor: $150.000",
                    height=150
                )

with tab4:
    st.subheader("Renombrador de Archivos")
    st.info("Renombra archivos de forma masiva según patrones específicos")
    
    bulk_files = st.file_uploader(
        "Sube archivos para renombrar", 
        accept_multiple_files=True,
        key="bulk_rename"
    )
    
    if bulk_files:
        st.write(f"📂 Total de archivos: {len(bulk_files)}")
        
        rename_pattern = st.text_input(
            "Patrón de renombrado:",
            placeholder="Ej: factura_{numero}_{fecha}",
            help="Usa {numero} para contador, {fecha} para fecha actual"
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            start_number = st.number_input("Número inicial:", value=1, min_value=1)
        
        with col2:
            add_date = st.checkbox("Incluir fecha", value=True)
        
        if st.button("🔄 Renombrar Lote", use_container_width=True):
            progress_bar = st.progress(0)
            
            for i, file in enumerate(bulk_files):
                progress = (i + 1) / len(bulk_files)
                progress_bar.progress(progress)
                
                # Simular renombrado
                import time
                time.sleep(0.3)
            
            st.success(f"✅ {len(bulk_files)} archivos renombrados exitosamente!")

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
        'Archivos': np.random.randint(10, 100, len(dates)),  # LÍNEA CORREGIDA
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
    'Archivo': ['facturas_enero.xlsx', 'rips_noviembre.csv', 'ocr_imagenes.zip'],
    'Proceso': ['Conversión MANTIS', 'Renombrado RIPS', 'Procesamiento OCR'],
    'Estado': ['✅ Completado', '✅ Completado', '⚠️ Advertencias'],
    'Usuario': ['admin', 'operador1', 'operador2']
}

historial_df = pd.DataFrame(historial_data)
st.dataframe(historial_df, use_container_width=True)

# INSTRUCCIONES DE USO
with st.expander("📖 Instrucciones de Uso"):
    st.markdown("""
    ### Guía Rápida:
    
    **SAVIA & COOSALUD - Conversores:**
    - Sube archivos en formato Excel o CSV
    - Selecciona el tipo de conversión (MANTIS/SISPRO)
    - Descarga el archivo convertido
    
    **SAVIA & COOSALUD - Renombradores:**
    - Selecciona múltiples archivos
    - Elige la convención de nombres (CUV/RIPS)
    - Los archivos se renombrarán automáticamente
    
    **SALUD TOTAL - Procesador OCR:**
    - Sube imágenes (JPG, PNG) o PDFs
    - Selecciona el idioma del texto
    - El texto extraído estará disponible para descarga
    
    **SALUD TOTAL - Renombrador:**
    - Renombra lotes grandes de archivos
    - Usa patrones personalizados
    - Incluye contadores y fechas automáticamente
    """)

# FOOTER
st.markdown("---")
st.markdown(
    "**Cuentas Médicas** • Sistema de Automatización TodoDrogas • "
    "Para soporte técnico contacte al administrador del sistema."
)
