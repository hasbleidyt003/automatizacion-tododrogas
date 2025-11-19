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

# CSS minimalista
st.markdown("""
<style>
    /* Reset minimalista */
    .main .block-container {
        padding-top: 1rem;
        max-width: 1200px;
    }
    
    /* Tarjetas minimalistas con borde flotante */
    .minimal-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #e1e5e9;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        transition: all 0.3s ease;
        height: 100%;
        position: relative;
    }
    
    .minimal-card:hover {
        border-color: #0066cc;
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        transform: translateY(-2px);
    }
    
    /* Iconos minimalistas */
    .minimal-icon {
        width: 40px;
        height: 40px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
        background: #f8f9fa;
        color: #0066cc;
        font-size: 1rem;
        border: 1px solid #e9ecef;
    }
    
    /* Botones minimalistas */
    .minimal-btn {
        background: white;
        color: #0066cc;
        border: 1px solid #0066cc;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-weight: 500;
        font-size: 0.85rem;
        cursor: pointer;
        transition: all 0.2s ease;
        width: 100%;
        text-align: center;
        text-decoration: none;
        display: block;
    }
    
    .minimal-btn:hover {
        background: #0066cc;
        color: white;
    }
    
    /* Header minimalista */
    .minimal-header {
        background: white;
        padding: 2rem 0;
        margin: 0.5rem 0 2rem 0;
        border-bottom: 1px solid #e1e5e9;
    }
    
    /* Beneficios en horizontal */
    .benefits-horizontal {
        display: flex;
        gap: 1.5rem;
        justify-content: space-between;
        margin: 1rem 0;
    }
    
    .benefit-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.9rem;
        color: #495057;
    }
    
    .benefit-check {
        color: #00a86b;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# HEADER MINIMALISTA
with st.container():
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div class="minimal-header">
            <h1 style='
                color: #1a1a1a;
                font-size: 2rem;
                font-weight: 600;
                margin-bottom: 0.5rem;
                line-height: 1.2;
            '>
            Sistema de Automatización
            </h1>
            
            <h2 style='
                color: #666666;
                font-size: 1.1rem;
                font-weight: 400;
                margin-bottom: 1rem;
                line-height: 1.4;
            '>
            Transformando procesos mediante tecnología inteligente
            </h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="minimal-card">
            <h3 style='
                color: #1a1a1a;
                font-size: 1rem;
                font-weight: 600;
                margin-bottom: 1rem;
            '>
            Beneficios Clave
            </h3>
            <div class="benefits-horizontal">
                <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                    <div class="benefit-item">
                        <span class="benefit-check">✓</span> Reducción de tiempos
                    </div>
                    <div class="benefit-item">
                        <span class="benefit-check">✓</span> Mayor precisión
                    </div>
                </div>
                <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                    <div class="benefit-item">
                        <span class="benefit-check">✓</span> Reportes automáticos
                    </div>
                    <div class="benefit-item">
                        <span class="benefit-check">✓</span> Integración total
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# SEPARADOR SUTIL
st.markdown("<div style='height: 1px; background: #f1f3f4; margin: 2rem 0;'></div>", unsafe_allow_html=True)

# SECCIÓN DE MÓDULOS
st.markdown("""
<div style='margin-bottom: 1.5rem;'>
    <h3 style='
        color: #1a1a1a;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    '>
    Áreas de Automatización
    </h3>
    <p style='color: #666666; font-size: 0.9rem;'>
    Selecciona un área para acceder a sus herramientas especializadas
    </p>
</div>
""", unsafe_allow_html=True)

# DATOS DE LOS MÓDULOS MINIMALISTAS
modules_data = [
    {
        "name": "Cuentas Médicas",
        "icon": "📋",
        "description": "Procesamiento automatizado de cuentas médicas con conversores JSON y renombrado RIPS/CUV",
        "features": ["SAVIA & COOSALUD", "SALUD TOTAL", "Procesador OCR"],
        "status": "active"
    },
    {
        "name": "Cartera", 
        "icon": "💰",
        "description": "Gestión automatizada de estados de cuenta y reportes financieros con análisis inteligente",
        "features": ["Estados de Cuenta", "Reportes Financieros", "Análisis"],
        "status": "active"
    },
    {
        "name": "Tesorería",
        "icon": "🏦",
        "description": "Control automatizado de estados bancarios y gestión de flujo financiero",
        "features": ["Estados Bancarios", "Conciliación", "Flujo Financiero"],
        "status": "active"
    },
    {
        "name": "Métricas",
        "icon": "📊",
        "description": "Dashboard de métricas y análisis de impacto de las automatizaciones",
        "features": ["Dashboard", "Análisis", "Reportes"],
        "status": "development"
    }
]

# GRID DE MÓDULOS
cols = st.columns(4)
for i, (col, module) in enumerate(zip(cols, modules_data)):
    with col:
        status_color = "#00a86b" if module["status"] == "active" else "#ff6b35"
        status_text = "Activo" if module["status"] == "active" else "Desarrollo"
        
        st.markdown(f"""
        <div class="minimal-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
                <div class="minimal-icon">
                    {module['icon']}
                </div>
                <div style="font-size: 0.7rem; font-weight: 500; color: {status_color}; 
                          background: rgba({status_color.replace('#', '')}, 0.1); 
                          padding: 0.2rem 0.5rem; border-radius: 8px; border: 1px solid rgba({status_color.replace('#', '')}, 0.2);">
                    {status_text}
                </div>
            </div>
            
            <h4 style='
                color: #1a1a1a;
                font-size: 1rem;
                font-weight: 600;
                margin-bottom: 0.5rem;
                line-height: 1.3;
            '>
            {module['name']}
            </h4>
            
            <div style='
                color: #666666;
                line-height: 1.4;
                margin-bottom: 1rem;
                font-size: 0.8rem;
            '>
                {module['description']}
            </div>
            
            <div style='margin-bottom: 1rem;'>
        """, unsafe_allow_html=True)
        
        # Features como mini badges
        for feature in module["features"]:
            st.markdown(f"""
            <span style='
                display: inline-block;
                background: #f8f9fa;
                color: #495057;
                padding: 0.15rem 0.4rem;
                border-radius: 6px;
                font-size: 0.65rem;
                margin: 0.1rem;
                border: 1px solid #e9ecef;
            '>
            {feature}
            </span>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
            </div>
            
            <a href="/{module['name'].replace(' ', '_').replace('&', 'y')}" class="minimal-btn">
                Acceder
            </a>
        </div>
        """, unsafe_allow_html=True)

# SEPARADOR
st.markdown("<div style='height: 1px; background: #f1f3f4; margin: 2rem 0;'></div>", unsafe_allow_html=True)

# ESTADÍSTICAS MINIMALISTAS
st.markdown("""
<div style='margin-bottom: 1rem;'>
    <h3 style='
        color: #1a1a1a;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1rem;
    '>
    Estado del Sistema
    </h3>
</div>
""", unsafe_allow_html=True)

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
st.markdown("""
<div style='
    background: #f8f9fa;
    padding: 1.5rem 0;
    margin-top: 3rem;
    text-align: center;
    border-top: 1px solid #e9ecef;
'>
    <div style='color: #666666; font-size: 0.9rem;'>
        <strong>TodoDrogas Automation</strong> • v2.1.0 • Sistema integrado de gestión
    </div>
</div>
""", unsafe_allow_html=True)
