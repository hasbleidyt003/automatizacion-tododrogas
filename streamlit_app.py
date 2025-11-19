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

# Navbar moderna
modern_navbar()

# CSS mejorado con paleta azul/blanco/gris
st.markdown("""
<style>
    /* Reset y base profesional */
    .main .block-container {
        padding-top: 2rem;
        max-width: 1200px;
    }
    
    /* Tarjetas profesionales */
    .platform-card {
        background: white;
        border-radius: 8px;
        padding: 1.5rem;
        border: 1px solid #e1e5e9;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: all 0.2s ease;
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    
    .platform-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-color: #0066cc;
    }
    
    /* Iconos profesionales */
    .platform-icon {
        width: 48px;
        height: 48px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
        background: #0066cc;
        color: white;
        font-size: 1.2rem;
    }
    
    /* Botones de acción */
    .platform-btn {
        background: #0066cc;
        color: white;
        border: none;
        padding: 0.6rem 1rem;
        border-radius: 6px;
        font-weight: 500;
        font-size: 0.9rem;
        cursor: pointer;
        transition: all 0.2s ease;
        width: 100%;
        text-align: center;
        text-decoration: none;
        display: block;
    }
    
    .platform-btn:hover {
        background: #0052a3;
        color: white;
        text-decoration: none;
    }
    
    /* Header profesional */
    .platform-header {
        background: white;
        padding: 2rem;
        border-radius: 8px;
        margin: 1rem 0 2rem 0;
        border: 1px solid #e1e5e9;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Badges de estado */
    .status-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .status-active {
        background: #e6f2ff;
        color: #0066cc;
        border: 1px solid #b3d9ff;
    }
    
    .status-development {
        background: #fff4e6;
        color: #cc5500;
        border: 1px solid #ffd9b3;
    }
    
    /* Features badges */
    .feature-badge {
        display: inline-block;
        background: #f8f9fa;
        color: #495057;
        padding: 0.2rem 0.6rem;
        border-radius: 10px;
        font-size: 0.7rem;
        margin: 0.1rem;
        border: 1px solid #e9ecef;
    }
</style>
""", unsafe_allow_html=True)

# HEADER CON COMPONENTES NATIVOS DE STREAMLIT
with st.container():
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.title("Plataforma de Automatización")
        st.subheader("TodoDrogas - Sistema integrado de gestión automatizada")
        
        # Métricas usando columns nativas
        metric_cols = st.columns(3)
        with metric_cols[0]:
            st.metric("Áreas Activas", "3", "100% operativas")
        with metric_cols[1]:
            st.metric("Automatizaciones", "12+", "En crecimiento")
        with metric_cols[2]:
            st.metric("Eficiencia", "99.8%", "+0.2%")
    
    with col2:
        st.info("✅ **Sistema Operativo**\n\nTodas las funciones activas y estables")

# SECCIÓN PRINCIPAL - MÓDULOS DE AUTOMATIZACIÓN
st.header("Módulos de Automatización")
st.write("Sistemas especializados por área operativa. Selecciona un módulo para acceder a sus herramientas.")

# DATOS DE LOS MÓDULOS
modules_data = [
    {
        "name": "Cuentas Médicas",
        "icon": "📋",
        "description": "Procesamiento automatizado de cuentas médicas con conversores JSON, renombrado RIPS/CUV y procesamiento OCR.",
        "status": "active",
        "status_text": "En Producción",
        "features": ["SAVIA & COOSALUD", "SALUD TOTAL", "Procesador OCR"],
        "page": "Cuentas_Medicas"
    },
    {
        "name": "Cartera", 
        "icon": "💰",
        "description": "Gestión automatizada de estados de cuenta, reportes financieros y análisis de cartera.",
        "status": "active", 
        "status_text": "En Producción",
        "features": ["Estados de Cuenta", "Reportes Financieros", "Análisis Inteligente"],
        "page": "Cartera"
    },
    {
        "name": "Tesorería",
        "icon": "🏦",
        "description": "Control automatizado de estados bancarios, conciliación y gestión de flujo financiero.",
        "status": "active",
        "status_text": "En Producción", 
        "features": ["Estados Bancarios", "Conciliación", "Flujo Financiero"],
        "page": "Tesoreria"
    },
    {
        "name": "Métricas & Reportes",
        "icon": "📊",
        "description": "Dashboard de métricas, análisis de impacto y reportes consolidados del sistema.",
        "status": "development",
        "status_text": "En Desarrollo",
        "features": ["Dashboard", "Análisis de Impacto", "Reportes"],
        "page": "Metricas"
    }
]

# GRID DE MÓDULOS USANDO COLUMNS NATIVAS
for i in range(0, len(modules_data), 2):
    cols = st.columns(2)
    
    for j in range(2):
        if i + j < len(modules_data):
            module = modules_data[i + j]
            with cols[j]:
                # Usar container nativo de Streamlit
                with st.container():
                    # Status badge
                    status_color = "🟢" if module["status"] == "active" else "🟡"
                    st.write(f"{status_color} **{module['status_text']}**")
                    
                    # Icono y título
                    col_icon, col_title = st.columns([1, 4])
                    with col_icon:
                        st.write(f"<div class='platform-icon'>{module['icon']}</div>", unsafe_allow_html=True)
                    with col_title:
                        st.subheader(module["name"])
                    
                    # Descripción
                    st.write(module["description"])
                    
                    # Features
                    features_html = "".join([f"<span class='feature-badge'>{feature}</span>" for feature in module["features"]])
                    st.write(f"<div style='margin: 0.5rem 0;'>{features_html}</div>", unsafe_allow_html=True)
                    
                    # Botón de acceso
                    if st.button(f"Acceder a {module['name']}", key=f"btn_{module['page']}"):
                        st.switch_page(f"pages/{module['page']}.py")

# SEPARADOR
st.divider()

# SECCIÓN DE ESTADO DEL SISTEMA
st.header("Estado del Sistema")

# ESTADÍSTICAS USANDO METRICS NATIVAS
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Tiempo Activo", 
        value="24/7", 
        delta="Operación continua",
        delta_color="off"
    )

with col2:
    st.metric(
        label="Procesos Hoy", 
        value="1,247", 
        delta="+12% vs ayer"
    )

with col3:
    st.metric(
        label="Eficiencia del Sistema", 
        value="99.8%", 
        delta="+0.2%",
        delta_color="normal"
    )

# INFORMACIÓN ADICIONAL DEL SISTEMA
with st.expander("📋 Información Técnica del Sistema"):
    tech_cols = st.columns(2)
    
    with tech_cols[0]:
        st.write("**Versiones Activas:**")
        st.write("- Cuentas Médicas: v2.1.0")
        st.write("- Cartera: v1.8.2") 
        st.write("- Tesorería: v1.5.1")
        
    with tech_cols[1]:
        st.write("**Próximas Actualizaciones:**")
        st.write("- Métricas & Reportes: Q1 2024")
        st.write("- API Integration: Q2 2024")
        st.write("- Mobile App: Q3 2024")

# FOOTER CON COMPONENTES NATIVOS
st.divider()
footer_cols = st.columns(3)

with footer_cols[0]:
    st.write("**TodoDrogas Automation**")
    st.write("Sistema integrado de gestión")

with footer_cols[1]:
    st.write("**Versión:** 2.1.0")
    st.write("**Última actualización:** Enero 2024")

with footer_cols[2]:
    st.write("**Soporte Técnico**")
    st.write("soporte@tododrogas.com")
