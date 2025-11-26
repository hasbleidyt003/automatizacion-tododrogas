import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
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

# LLAMAR EL NAVBAR
modern_navbar()

# Título de la página
st.title("📋 Cuentas Médicas")
st.markdown("Automatización de procesos para cuentas médicas por EPS")

# SECCIÓN DE EPS - ORGANIZADA POR EMPRESA
st.header("🏥 Selecciona la EPS para Procesar Archivos")

# Crear pestañas para cada EPS
tab1, tab2, tab3 = st.tabs(["🏥 COOSALUD", "💊 SAVIA SALUD", "🩺 SALUD TOTAL"])

with tab1:
    st.subheader("COOSALUD - Procesamiento de Archivos")
    st.info("Herramientas especializadas para Coosalud")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔄 Conversores JSON")
        if st.button("🔧 Conversor Mantis", use_container_width=True, key="coosalud_mantis"):
            st.switch_page("pages/5_Conversor_Mantis_Coosalud.py")
        
        if st.button("🔄 Conversor SISPRO", use_container_width=True, key="coosalud_sispro"):
            st.switch_page("pages/6_Conversor_SISPRO_Coosalud.py")
    
    with col2:
        st.markdown("### 🏷️ Renombradores")
        if st.button("📋 Renombrador RIPS", use_container_width=True, key="coosalud_rips"):
            st.switch_page("pages/8_Renombradores_rips_Coosalud.py")
        
        if st.button("🔢 Renombrador CUV", use_container_width=True, key="coosalud_cuv"):
            st.switch_page("pages/7_Renombradores_cuv_Coosalud.py")

with tab2:
    st.subheader("SAVIA SALUD - Procesamiento de Archivos")
    st.info("Herramientas especializadas para Savia Salud")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📋 Renombrador CUV")
        if st.button("🔢 Renombrador CUV Savia", use_container_width=True, key="savia_cuv"):
            st.switch_page("pages/9_Renombrador_cuv_Savia.py")
    
    with col2:
        st.markdown("### 📋 Renombrador RIPS")
        if st.button("📋 Renombrador RIPS Savia", use_container_width=True, key="savia_rips"):
            st.switch_page("pages/10_Renombrador_rips_Savia.py")

with tab3:
    st.subheader("SALUD TOTAL - Procesamiento de Archivos")
    st.info("Herramientas especializadas para Salud Total")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔍 Procesador OCR")
        if st.button("🔍 Procesador + Renombrador", use_container_width=True, key="salud_total_ocr"):
            st.switch_page("pages/11_Processador_Renombrador_ST.py")
    
    with col2:
        st.markdown("### ⚡ Procesamiento Avanzado")
        st.info("OCR inteligente con renombrado automático")

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
st.subheader("Actividad Reciente por EPS")

# Crear datos de ejemplo para el gráfico por EPS
try:
    eps_data = pd.DataFrame({
        'EPS': ['COOSALUD', 'SAVIA SALUD', 'SALUD TOTAL'],
        'Archivos_Procesados': [45, 32, 28],
        'Tasa_Éxito': [98.5, 97.8, 96.2]
    })
    
    fig = px.bar(
        eps_data, 
        x='EPS', 
        y='Archivos_Procesados',
        title='Archivos Procesados por EPS (Última Semana)',
        color='Tasa_Éxito',
        color_continuous_scale='Blues'
    )
    
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
except Exception as e:
    st.error(f"Error al generar gráfico: {e}")

# SECCIÓN DE HISTORIAL POR EPS
st.header("📋 Historial de Procesos por EPS")

# Datos de ejemplo para el historial organizado por EPS
historial_data = {
    'Fecha': ['2024-01-15 10:30', '2024-01-15 11:15', '2024-01-14 16:45', '2024-01-14 14:20'],
    'EPS': ['COOSALUD', 'COOSALUD', 'SAVIA SALUD', 'SALUD TOTAL'],
    'Archivo': ['datos_mantis.json', 'facturas_sispro.csv', 'historias_savia.pdf', 'documentos_st.pdf'],
    'Proceso': ['Conversor Mantis', 'Conversor SISPRO', 'Renombrado RIPS', 'Procesador OCR'],
    'Estado': ['✅ Completado', '✅ Completado', '✅ Completado', '⚠️ Advertencias'],
    'Usuario': ['admin', 'operador1', 'operador2', 'operador3']
}

historial_df = pd.DataFrame(historial_data)
st.dataframe(historial_df, use_container_width=True)

# INFORMACIÓN ADICIONAL ORGANIZADA POR EPS
with st.expander("ℹ️ Información de Módulos por EPS"):
    st.markdown("""
    ### 🏥 COOSALUD:
    **🔧 Conversor Mantis:** 
    - Procesa archivos JSON de Mantis
    - Convierte a formato estándar Coosalud
    - Corrige formatos de fecha y estructura
    
    **🔄 Conversor SISPRO:**
    - Transforma archivos JSON de SISPRO  
    - Adapta al formato requerido por Coosalud
    - Valida y estandariza datos
    
    **🏷️ Renombradores:**
    - **RIPS:** Aplica estándar de facturación RIPS
    - **CUV:** Renombra por código único de validación
    
    ---
    
    ### 💊 SAVIA SALUD:
    **🏷️ Renombrador CUV:**
    - Renombra archivos por código único
    - Mantiene estructura requerida por Savia
    
    **📋 Renombrador RIPS:**
    - Aplica estándar RIPS de facturación
    - Automatiza proceso masivo
    
    ---
    
    ### 🩺 SALUD TOTAL:
    **🔍 Procesador OCR + Renombrador:**
    - Procesa documentos escaneados (PDF/Imágenes)
    - Aplica OCR inteligente para extracción de texto
    - Renombrado automático basado en contenido
    - Proceso combinado en un solo paso
    """)

# FOOTER
st.markdown("---")
st.markdown(
    "**Cuentas Médicas** • Sistema de Automatización TodoDrogas • "
    "Organizado por EPS: COOSALUD, SAVIA SALUD, SALUD TOTAL"
)
