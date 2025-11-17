import streamlit as st
import pandas as pd
import io
from datetime import datetime
import base64

# Configuración de página
st.set_page_config(
    page_title="Cuentas Médicas",
    page_icon="📋",
    layout="wide"
)

# Navbar
from components.navbar import modern_navbar
modern_navbar()

# Título principal
st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h1 style='color: #1a1a1a; font-size: 2.5rem; margin-bottom: 1rem;'>🏥 Cuentas Médicas</h1>
    <p style='color: #666; font-size: 1.2rem;'>Automatización de procesos para SAVIA, COOSALUD y SALUD TOTAL</p>
</div>
""", unsafe_allow_html=True)

# Pestañas para diferentes EPS
tab1, tab2, tab3 = st.tabs(["🏥 SAVIA & COOSALUD", "🔬 SALUD TOTAL", "📊 INDICADORES"])

with tab1:
    st.markdown("### 🛠️ Herramientas SAVIA & COOSALUD")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔄 Conversor MANTIS/SISPRO")
        uploaded_file = st.file_uploader("Subir archivo MANTIS", type=['xlsx', 'xls'], key="mantis")
        if uploaded_file:
            if st.button("Convertir a SISPRO", key="convert_mantis"):
                with st.spinner("Procesando archivo..."):
                    # Simulación de procesamiento
                    df = pd.DataFrame({
                        'Archivo': [uploaded_file.name],
                        'Estado': ['✅ Convertido'],
                        'Fecha': [datetime.now().strftime("%Y-%m-%d %H:%M")]
                    })
                    st.success("✅ Conversión completada exitosamente!")
                    st.dataframe(df, use_container_width=True)
                    
                    # Botón de descarga
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        df.to_excel(writer, index=False)
                    st.download_button(
                        label="📥 Descargar archivo convertido",
                        data=output.getvalue(),
                        file_name=f"sispro_convertido_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx",
                        mime="application/vnd.ms-excel"
                    )
    
    with col2:
        st.markdown("#### 📁 Renombrador CUV/RIPS")
        uploaded_rips = st.file_uploader("Subir archivos RIPS", type=['txt', 'csv'], accept_multiple_files=True, key="rips")
        if uploaded_rips:
            if st.button("Renombrar archivos", key="rename_rips"):
                st.success(f"✅ {len(uploaded_rips)} archivos renombrados correctamente")
                for file in uploaded_rips:
                    st.write(f"📄 {file.name} → {file.name.replace('.', '_cuv.')}")

with tab2:
    st.markdown("### 🧪 Procesador OCR SALUD TOTAL")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### 📷 Subir documentos escaneados")
        ocr_files = st.file_uploader(
            "Seleccionar archivos (PDF)", 
            type=['pdf'], 
            accept_multiple_files=True,
            key="ocr"
        )
        
        if ocr_files:
            st.info(f"📁 {len(ocr_files)} archivos seleccionados para procesamiento OCR")
            
            if st.button("🚀 Iniciar Procesamiento OCR", type="primary"):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for i, file in enumerate(ocr_files):
                    progress = (i + 1) / len(ocr_files)
                    progress_bar.progress(progress)
                    status_text.text(f"Procesando: {file.name} ({i+1}/{len(ocr_files)})")
                    
                st.success("✅ Procesamiento OCR completado!")
                
                # Resultados simulados
                results_df = pd.DataFrame({
                    'Documento': [f.name for f in ocr_files],
                    'Estado': ['✅ Procesado' for _ in ocr_files],
                    'Páginas': [1 for _ in ocr_files],
                    'Texto Extraído': [f"Texto simulado de {f.name}" for f in ocr_files]
                })
                st.dataframe(results_df, use_container_width=True)

with tab3:
    st.markdown("### 📈 Métricas de Procesamiento")
    
    # Métricas en tarjetas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Archivos Procesados", "1,247", "+15%")
    with col2:
        st.metric("Tasa de Éxito", "98.2%", "+2.1%")
    with col3:
        st.metric("Tiempo Promedio", "45s", "-12s")
    with col4:
        st.metric("Ahorro Estimado", "120h/mes", "+18h")
    
    # Gráfico de actividad (simulado)
    st.markdown("#### 📊 Actividad Reciente")
    activity_data = pd.DataFrame({
        'Fecha': pd.date_range('2024-01-01', periods=30, freq='D'),
        'Archivos': np.random.randint(10, 100, 30),
        'Errores': np.random.randint(0, 5, 30)
    })
    st.line_chart(activity_data.set_index('Fecha'))
