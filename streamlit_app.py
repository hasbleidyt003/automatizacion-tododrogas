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

# CSS mejorado para plataforma profesional
st.markdown("""
<style>
    /* Reset y base profesional */
    .main .block-container {
        padding-top: 2rem;
        max-width: 1200px;
    }
    
    /* Tarjetas profesionales para plataforma */
    .platform-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    
    .platform-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(180deg, var(--accent-color), var(--accent-dark));
        transition: width 0.3s ease;
    }
    
    .platform-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-color: var(--accent-color);
    }
    
    .platform-card:hover::before {
        width: 6px;
    }
    
    /* Iconos profesionales */
    .platform-icon {
        width: 50px;
        height: 50px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, var(--accent-color), var(--accent-dark));
        color: white;
        font-size: 1.2rem;
        box-shadow: 0 4px 12px rgba(var(--accent-rgb), 0.2);
    }
    
    /* Botones de acción profesional */
    .platform-btn {
        background: linear-gradient(135deg, var(--accent-color), var(--accent-dark));
        color: white;
        border: none;
        padding: 0.7rem 1.2rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.9rem;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        text-align: center;
        text-decoration: none;
        display: block;
    }
    
    .platform-btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(var(--accent-rgb), 0.3);
        color: white;
        text-decoration: none;
    }
    
    /* Header profesional */
    .platform-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 12px;
        margin: 1rem 0 2rem 0;
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .platform-header::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
    }
    
    /* Estadísticas rápidas */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1rem;
        margin: 1.5rem 0;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
        background: rgba(255,255,255,0.1);
        border-radius: 8px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Badges de estado */
    .status-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .status-active {
        background: rgba(76, 175, 80, 0.1);
        color: #4caf50;
        border: 1px solid rgba(76, 175, 80, 0.3);
    }
    
    .status-development {
        background: rgba(255, 152, 0, 0.1);
        color: #ff9800;
        border: 1px solid rgba(255, 152, 0, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# HEADER PROFESIONAL
st.markdown("""
<div class="platform-header">
    <div style="position: relative; z-index: 2;">
        <h1 style='
            color: white;
            font-size: 2.8rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            line-height: 1.1;
        '>
        Plataforma de Automatización
        </h1>
        
        <h2 style='
            color: rgba(255,255,255,0.9);
            font-size: 1.4rem;
            font-weight: 400;
            margin-bottom: 1.5rem;
        '>
        TodoDrogas - Sistema integrado de gestión automatizada
        </h2>
        
        <div class="stats-container">
            <div class="stat-item">
                <div style="font-size: 1.8rem; font-weight: 700;">3</div>
                <div style="font-size: 0.8rem; opacity: 0.9;">Áreas Activas</div>
            </div>
            <div class="stat-item">
                <div style="font-size: 1.8rem; font-weight: 700;">12+</div>
                <div style="font-size: 0.8rem; opacity: 0.9;">Automatizaciones</div>
            </div>
            <div class="stat-item">
                <div style="font-size: 1.8rem; font-weight: 700;">99.8%</div>
                <div style="font-size: 0.8rem; opacity: 0.9;">Eficiencia</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# SECCIÓN PRINCIPAL - MÓDULOS DE AUTOMATIZACIÓN
st.markdown("""
<div style='margin-bottom: 2rem;'>
    <h2 style='
        color: #1a1a1a;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    '>
    Módulos de Automatización
    </h2>
    <p style='color: #666666;'>
    Sistemas especializados por área operativa. Selecciona un módulo para acceder a sus herramientas.
    </p>
</div>
""", unsafe_allow_html=True)

# DATOS DE LOS MÓDULOS - ACTUALIZADO PARA MATCH CON TU ESTRUCTURA
modules_data = [
    {
        "name": "Cuentas Médicas",
        "icon": "📋",
        "accent_color": "#0066cc",
        "accent_dark": "#004499", 
        "accent_rgb": "0, 102, 204",
        "description": "Procesamiento automatizado de cuentas médicas con conversores JSON, renombrado RIPS/CUV y procesamiento OCR.",
        "status": "active",
        "status_text": "En Producción",
        "features": ["SAVIA & COOSALUD", "SALUD TOTAL", "Procesador OCR"],
        "page": "1_Cuentas_Medicas"  # Match con tu estructura de archivos
    },
    {
        "name": "Cartera", 
        "icon": "💰",
        "accent_color": "#00a86b",
        "accent_dark": "#007a4d",
        "accent_rgb": "0, 168, 107",
        "description": "Gestión automatizada de estados de cuenta, reportes financieros y análisis de cartera.",
        "status": "active", 
        "status_text": "En Producción",
        "features": ["Estados de Cuenta", "Reportes Financieros", "Análisis Inteligente"],
        "page": "2_Cartera"  # Match con tu estructura de archivos
    },
    {
        "name": "Tesorería",
        "icon": "🏦",
        "accent_color": "#ff6b35", 
        "accent_dark": "#cc552b",
        "accent_rgb": "255, 107, 53",
        "description": "Control automatizado de estados bancarios, conciliación y gestión de flujo financiero.",
        "status": "active",
        "status_text": "En Producción", 
        "features": ["Estados Bancarios", "Conciliación", "Flujo Financiero"],
        "page": "3_Tesoreria"  # Match con tu estructura de archivos
    },
    {
        "name": "Métricas & Reportes",
        "icon": "📊",
        "accent_color": "#8a2be2",
        "accent_dark": "#6a1cb3",
        "accent_rgb": "138, 43, 226", 
        "description": "Dashboard de métricas, análisis de impacto y reportes consolidados del sistema.",
        "status": "development",
        "status_text": "En Desarrollo",
        "features": ["Dashboard", "Análisis de Impacto", "Reportes"],
        "page": "Metricas"  # Puedes crear este archivo después
    }
]

# GRID DE MÓDULOS
cols = st.columns(2)
for i, module in enumerate(modules_data):
    with cols[i % 2]:  # Distribuye en 2 columnas
        status_class = "status-active" if module["status"] == "active" else "status-development"
        
        st.markdown(f"""
        <div class="platform-card" style="
            --accent-color: {module['accent_color']}; 
            --accent-dark: {module['accent_dark']}; 
            --accent-rgb: {module['accent_rgb']};
        ">
            <div class="status-badge {status_class}">
                {module['status_text']}
            </div>
            
            <div class="platform-icon">
                {module['icon']}
            </div>
            
            <h3 style='
                color: #1a1a1a;
                font-size: 1.3rem;
                font-weight: 600;
                margin-bottom: 0.8rem;
            '>
            {module['name']}
            </h3>
            
            <div style='
                color: #666666;
                line-height: 1.5;
                margin-bottom: 1.2rem;
                font-size: 0.9rem;
            '>
                {module['description']}
            </div>
            
            <div style='margin-bottom: 1.5rem;'>
        """, unsafe_allow_html=True)
        
        # Features como badges
        for feature in module["features"]:
            st.markdown(f"""
            <span style='
                display: inline-block;
                background: rgba(var(--accent-rgb), 0.1);
                color: var(--accent-color);
                padding: 0.2rem 0.6rem;
                border-radius: 12px;
                font-size: 0.75rem;
                margin: 0.2rem;
                border: 1px solid rgba(var(--accent-rgb), 0.2);
            '>
            {feature}
            </span>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
            </div>
            
            <a href="/{module['page']}" class="platform-btn" style="text-decoration: none;">
                Acceder al Módulo
            </a>
        </div>
        """, unsafe_allow_html=True)

# SEPARADOR
st.markdown("<div style='height: 1px; background: #e9ecef; margin: 2rem 0;'></div>", unsafe_allow_html=True)

# SECCIÓN DE ESTADO DEL SISTEMA
st.markdown("""
<div style='margin-bottom: 2rem;'>
    <h2 style='
        color: #1a1a1a;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    '>
    Estado del Sistema
    </h2>
</div>
""", unsafe_allow_html=True)

# ESTADÍSTICAS RÁPIDAS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="platform-card" style="--accent-color: #00a86b; --accent-dark: #007a4d; --accent-rgb: 0, 168, 107;">
        <div style="text-align: center;">
            <div style="font-size: 2rem; color: #00a86b; margin-bottom: 0.5rem;">⚡</div>
            <h3 style="color: #1a1a1a; font-size: 1.1rem; margin-bottom: 0.5rem;">Tiempo Activo</h3>
            <div style="font-size: 1.5rem; font-weight: 700; color: #00a86b;">24/7</div>
            <div style="color: #666666; font-size: 0.8rem;">Operación continua</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="platform-card" style="--accent-color: #0066cc; --accent-dark: #004499; --accent-rgb: 0, 102, 204;">
        <div style="text-align: center;">
            <div style="font-size: 2rem; color: #0066cc; margin-bottom: 0.5rem;">🔄</div>
            <h3 style="color: #1a1a1a; font-size: 1.1rem; margin-bottom: 0.5rem;">Procesos Hoy</h3>
            <div style="font-size: 1.5rem; font-weight: 700; color: #0066cc;">1,247</div>
            <div style="color: #666666; font-size: 0.8rem;">Automatizaciones ejecutadas</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="platform-card" style="--accent-color: #8a2be2; --accent-dark: #6a1cb3; --accent-rgb: 138, 43, 226;">
        <div style="text-align: center;">
            <div style="font-size: 2rem; color: #8a2be2; margin-bottom: 0.5rem;">✅</div>
            <h3 style="color: #1a1a1a; font-size: 1.1rem; margin-bottom: 0.5rem;">Eficiencia</h3>
            <div style="font-size: 1.5rem; font-weight: 700; color: #8a2be2;">99.8%</div>
            <div style="color: #666666; font-size: 0.8rem;">Tasa de éxito</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# FOOTER PROFESIONAL
st.markdown("""
<div style='
    background: #f8f9fa;
    padding: 2rem 0;
    margin-top: 3rem;
    text-align: center;
    border-top: 1px solid #e9ecef;
'>
    <div style='color: #1a1a1a; font-weight: 600; margin-bottom: 0.5rem;'>TodoDrogas - Plataforma de Automatización</div>
    <div style='color: #666666; font-size: 0.9rem;'>Sistema integrado de gestión • v2.1.0</div>
    <div style='color: #999999; font-size: 0.8rem; margin-top: 0.5rem;'>© 2024 Sistema de Automatización</div>
</div>
""", unsafe_allow_html=True)
