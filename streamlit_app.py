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
    st.title("Sistema de Automatización")
    st.subheader("Transformando procesos mediante tecnología inteligente")
    
    # Métricas del sistema
    col1_1, col1_2, col1_3 = st.columns(3)
    with col1_1:
        st.metric("Automatizaciones", "12+")
    with col1_2:
        st.metric("Eficiencia", "99.8%")
    with col1_3:
        st.metric("Áreas Activas", "3")

with col2:
    with st.container():
        st.write("**Beneficios Clave**")
        
        # Beneficios en dos columnas
        ben_col1, ben_col2 = st.columns(2)
        
        with ben_col1:
            st.write("✓ Reducción de tiempos")
            st.write("✓ Mayor precisión")
            
        with ben_col2:
            st.write("✓ Reportes automáticos")
            st.write("✓ Integración total")

# SEPARADOR
st.divider()

# SECCIÓN DE MÓDULOS
st.header("Áreas de Automatización")
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
                st.write(f"#### {module['icon']}")
            with status_col:
                status_color = "🟢" if module["status"] == "active" else "🟡"
                st.write(f"{status_color} **{module['status'].title()}**")
            
            # Título
            st.write(f"**{module['name']}**")
            
            # Descripción
            st.write(module['description'])
            
            # Features
            for feature in module["features"]:
                st.caption(f"• {feature}")
            
            # Botón de acceso
            if st.button(f"Acceder a {module['name']}", key=f"btn_{module['page']}"):
                st.switch_page(f"pages/{module['page']}.py")

# SEPARADOR
st.divider()

# ESTADÍSTICAS DEL SISTEMA
st.header("Estado del Sistema")
stats_cols = st.columns(4)

with stats_cols[0]:
    st.metric("Tiempo Activo", "24/7", "Operación continua")
with stats_cols[1]:
    st.metric("Procesos Hoy", "1,247", "+12%")
with stats_cols[2]:
    st.metric("Eficiencia", "99.8%", "+0.2%")
with stats_cols[3]:
    st.metric("Áreas Activas", "3/4", "75%")

# INFORMACIÓN ADICIONAL
with st.expander("📋 Información del Sistema"):
    info_cols = st.columns(2)
    
    with info_cols[0]:
        st.write("**Versiones Activas:**")
        st.write("- Cuentas Médicas: v2.1.0")
        st.write("- Cartera: v1.8.2") 
        st.write("- Tesorería: v1.5.1")
        st.write("- Métricas: v0.9.0")
        
    with info_cols[1]:
        st.write("**Soporte Técnico:**")
        st.write("**Email:** soporte@tododrogas.com")
        st.write("**Horario:** 24/7")
        st.write("**Versión Plataforma:** 2.1.0")

# FOOTER
st.divider()
footer_cols = st.columns(3)

with footer_cols[0]:
    st.write("**TodoDrogas Automation**")
    st.write("Sistema integrado de gestión")

with footer_cols[1]:
    st.write("**Versión:** 2.1.0")
    st.write("**Última actualización:** Enero 2024")

with footer_cols[2]:
    st.write("**Estado:** 🟢 En línea")
    st.write("**Soporte:** Disponible 24/7")
