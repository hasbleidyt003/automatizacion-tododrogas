# streamlit_app.py
import streamlit as st
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

# Configurar tema moderno
configure_modern_theme()

# Configurar página
st.set_page_config(
    page_title="Sistema de Automatización - TodoDrogas",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Navbar moderna minimalista
modern_navbar()

# HEADER MINIMALISTA
col1, col2 = st.columns([3, 2])

with col1:
    # Título principal
    st.markdown("# Sistema de Automatización")
    st.markdown("### Transformando procesos mediante tecnología inteligente")
    
    # Métricas en grid
    metric_cols = st.columns(4)
    with metric_cols[0]:
        st.metric("12+", "Automatizaciones")
    with metric_cols[1]:
        st.metric("99.8%", "Eficiencia")
    with metric_cols[2]:
        st.metric("24/7", "Operación")
    with metric_cols[3]:
        st.metric("3", "Áreas Activas")

with col2:
    # Tarjeta de beneficios
    with st.container():
        st.markdown("#### Beneficios Clave")
        
        # Beneficios en dos columnas
        ben_col1, ben_col2 = st.columns(2)
        
        with ben_col1:
            st.write("✓ Reducción de tiempos")
            st.write("✓ Mayor precisión")
            
        with ben_col2:
            st.write("✓ Reportes automáticos")
            st.write("✓ Integración total")

# SEPARADOR SUTIL
st.divider()

# SECCIÓN DE MÓDULOS
st.markdown("### Áreas de Automatización")
st.caption("Selecciona un área para acceder a sus herramientas especializadas")

# DATOS DE LOS MÓDULOS
modules_data = [
    {
        "name": "Cuentas Médicas",
        "icon": "📋",
        "description": "Procesamiento automatizado de cuentas médicas con conversores JSON y renombrado RIPS/CUV",
        "features": ["SAVIA & COOSALUD", "SALUD TOTAL", "Procesador OCR"],
        "status": "active",
        "page": "1_Cuentas_Medicas"
    },
    {
        "name": "Cartera", 
        "icon": "💰",
        "description": "Gestión automatizada de estados de cuenta y reportes financieros con análisis inteligente",
        "features": ["Estados de Cuenta", "Reportes Financieros", "Análisis"],
        "status": "active",
        "page": "2_Cartera"
    },
    {
        "name": "Tesorería",
        "icon": "🏦",
        "description": "Control automatizado de estados bancarios y gestión de flujo financiero",
        "features": ["Estados Bancarios", "Conciliación", "Flujo Financiero"],
        "status": "active",
        "page": "3_Tesoreria"
    },
    {
        "name": "Métricas",
        "icon": "📊",
        "description": "Dashboard de métricas y análisis de impacto de las automatizaciones",
        "features": ["Dashboard", "Análisis", "Reportes"],
        "status": "development",
        "page": "4_Metricas"
    }
]

# GRID DE MÓDULOS
cols = st.columns(4)
for i, (col, module) in enumerate(zip(cols, modules_data)):
    with col:
        with st.container():
            # Header con icono y estado
            icon_col, status_col = st.columns([1, 2])
            with icon_col:
                st.markdown(f"#### {module['icon']}")
            with status_col:
                status_color = "🟢" if module["status"] == "active" else "🟡"
                st.caption(f"{status_color} {module['status'].title()}")
            
            # Título
            st.markdown(f"**{module['name']}**")
            
            # Descripción
            st.write(module['description'])
            
            # Features como badges
            for feature in module["features"]:
                st.code(feature, language="")
            
            # Botón de acceso
            if st.button(f"Acceder", key=f"btn_{module['page']}", use_container_width=True):
                st.switch_page(f"pages/{module['page']}.py")

# SEPARADOR
st.divider()

# ESTADÍSTICAS DEL SISTEMA
st.markdown("### Estado del Sistema")
stats_cols = st.columns(4)

with stats_cols[0]:
    st.metric("Tiempo Activo", "24/7", "Operación continua")
with stats_cols[1]:
    st.metric("Procesos Hoy", "1,247", "+12%")
with stats_cols[2]:
    st.metric("Eficiencia", "99.8%", "+0.2%")
with stats_cols[3]:
    st.metric("Áreas Activas", "3/4", "75%")

# FOOTER MINIMALISTA
st.divider()
st.markdown(
    "<div style='text-align: center; color: #666666; font-size: 0.9rem;'>"
    "<strong>TodoDrogas Automation</strong> • v2.1.0 • Sistema integrado de gestión"
    "</div>",
    unsafe_allow_html=True
)
