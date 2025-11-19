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

# CSS para efectos modernos con paleta azul/gris
st.markdown("""
<style>
    /* Efectos 3D mejorados para las tarjetas */
    .card-3d {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 
            0 8px 25px rgba(0,0,0,0.08),
            0 2px 8px rgba(0,0,0,0.03),
            inset 0 1px 0 rgba(255,255,255,0.8);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid rgba(255,255,255,0.5);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    .card-3d::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #0066cc, #004499);
        border-radius: 16px 16px 0 0;
    }
    
    .card-3d:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 
            0 20px 40px rgba(0,0,0,0.12),
            0 8px 20px rgba(0,0,0,0.06),
            inset 0 1px 0 rgba(255,255,255,0.9);
    }
    
    /* Iconos con efecto 3D mejorado */
    .icon-3d {
        width: 60px;
        height: 60px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #0066cc, #004499);
        box-shadow: 
            0 8px 20px rgba(0, 102, 204, 0.25),
            inset 0 1px 0 rgba(255,255,255,0.3);
        position: relative;
        transition: all 0.3s ease;
    }
    
    .card-3d:hover .icon-3d {
        transform: scale(1.1) rotate(5deg);
        box-shadow: 
            0 12px 30px rgba(0, 102, 204, 0.35),
            inset 0 1px 0 rgba(255,255,255,0.4);
    }
    
    /* Botones con efecto 3D mejorado */
    .btn-3d {
        background: linear-gradient(135deg, #0066cc, #004499);
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 10px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 
            0 6px 20px rgba(0, 102, 204, 0.25),
            0 2px 4px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
        width: 100%;
        font-family: inherit;
    }
    
    .btn-3d::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .btn-3d:hover::before {
        left: 100%;
    }
    
    .btn-3d:hover {
        transform: translateY(-2px);
        box-shadow: 
            0 8px 25px rgba(0, 102, 204, 0.4),
            0 3px 6px rgba(0,0,0,0.15);
    }
    
    /* Hero section mejorada con azul/gris */
    .hero-gradient {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin: 1rem 0 3rem 0;
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .hero-gradient::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(180deg); }
    }
    
    /* Grid de mini-cards para características */
    .feature-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.5rem;
        margin: 1rem 0;
    }
    
    .feature-mini {
        text-align: center;
        padding: 0.6rem;
        background: rgba(255,255,255,0.1);
        border-radius: 8px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Efectos de texto */
    .text-glow {
        text-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    /* Mejoras específicas para el hero azul/gris */
    .hero-blue {
        background: linear-gradient(135deg, #0066cc 0%, #004499 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin: 1rem 0 3rem 0;
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .hero-blue::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.15) 1px, transparent 1px);
        background-size: 60px 60px;
        animation: float 8s ease-in-out infinite;
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION MEJORADA - MANTENIENDO ESTRUCTURA ORIGINAL
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="hero-blue">
        <h1 style='
            color: white;
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            line-height: 1.1;
            font-family: "Inter", sans-serif;
            text-shadow: 0 4px 12px rgba(0,0,0,0.2);
        '>
        SISTEMA DE<br>AUTOMATIZACIÓN
        </h1>
        
        <h2 style='
            color: rgba(255,255,255,0.9);
            font-size: 1.8rem;
            font-weight: 400;
            margin-top: 0.5rem;
            margin-bottom: 1.5rem;
            line-height: 1.3;
            font-family: "Inter", sans-serif;
        '>
        Transformando procesos mediante tecnología inteligente
        </h2>
        
        <div style='
            color: rgba(255,255,255,0.8);
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 2rem;
        '>
            <p>El futuro es la tecnología, y hoy se convierte en nuestra mejor herramienta.</p>
            <p>Centralizamos automatizaciones por área para optimizar procesos y mejorar la eficiencia operativa.</p>
        </div>
        
        <div class="feature-grid">
            <div class="feature-mini">
                <div style="font-size: 1.2rem; font-weight: bold;">12+</div>
                <div style="font-size: 0.8rem;">Automatizaciones</div>
            </div>
            <div class="feature-mini">
                <div style="font-size: 1.2rem; font-weight: bold;">99.8%</div>
                <div style="font-size: 0.8rem;">Eficiencia</div>
            </div>
            <div class="feature-mini">
                <div style="font-size: 1.2rem; font-weight: bold;">24/7</div>
                <div style="font-size: 0.8rem;">Operación</div>
            </div>
            <div class="feature-mini">
                <div style="font-size: 1.2rem; font-weight: bold;">3</div>
                <div style="font-size: 0.8rem;">Áreas Activas</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-3d" style="height: 100%;">
        <div style='text-align: center; color: #1a1a1a;'>
            <div class="icon-3d">
                <span style='color: white; font-size: 1.5rem;'>🚀</span>
            </div>
            <h3 style='margin-bottom: 1rem; font-size: 1.2rem; color: #1a1a1a;'>Beneficios Clave</h3>
            <div style='text-align: left; line-height: 1.6; color: #666;'>
                <div style='display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.8rem;'>
                    <span style='font-size: 1.2rem; color: #0066cc;'>✓</span> <span>Reducción de tiempos</span>
                </div>
                <div style='display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.8rem;'>
                    <span style='font-size: 1.2rem; color: #0066cc;'>✓</span> <span>Mayor precisión</span>
                </div>
                <div style='display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.8rem;'>
                    <span style='font-size: 1.2rem; color: #0066cc;'>✓</span> <span>Reportes automáticos</span>
                </div>
                <div style='display: flex; align-items: center; gap: 0.5rem;'>
                    <span style='font-size: 1.2rem; color: #0066cc;'>✓</span> <span>Integración total</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# SEPARADOR
st.markdown("<div style='height: 1px; background: linear-gradient(90deg, transparent, #e0e0e0, transparent); margin: 3rem 0;'></div>", unsafe_allow_html=True)

# SECCIÓN DE AUTOMATIZACIONES - MANTENIENDO ESTRUCTURA ORIGINAL
st.markdown("""
<div style='text-align: center; margin-bottom: 2rem;'>
    <h2 style='
        color: #1a1a1a;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        text-shadow: 0 2px 8px rgba(0,0,0,0.05);
    '>
    Áreas de Automatización
    </h2>
    <p style='color: #666666; font-size: 1.1rem;'>
    Selecciona un área para acceder a sus herramientas especializadas
    </p>
</div>
""", unsafe_allow_html=True)

# GRID DE TARJETAS 3D - MANTENIENDO ESTRUCTURA ORIGINAL
col1, col2, col3, col4 = st.columns(4)

# Datos de las áreas para reutilización - MEJORADOS
areas_data = [
    {
        "name": "Cuentas Médicas",
        "icon": "📋",
        "accent_color": "#0066cc",
        "accent_dark": "#004499", 
        "description": "SAVIA & COOSALUD: Conversores JSON, Renombradores RIPS/CUV<br>SALUD TOTAL: Procesador OCR + Renombrado",
        "button_text": "Acceder",
        "status": "🟢 ACTIVO"
    },
    {
        "name": "Cartera",
        "icon": "💰",
        "accent_color": "#00875a",
        "accent_dark": "#006644",
        "description": "Gestión automatizada de estados de cuenta y reportes financieros con análisis inteligente",
        "button_text": "Acceder",
        "status": "🟢 ACTIVO"
    },
    {
        "name": "Tesorería",
        "icon": "🏦", 
        "accent_color": "#ff6b35",
        "accent_dark": "#cc552b",
        "description": "Control automatizado de estados bancarios y flujo financiero con máxima seguridad",
        "button_text": "Acceder", 
        "status": "🟢 ACTIVO"
    },
    {
        "name": "Métricas",
        "icon": "📊",
        "accent_color": "#8a2be2",
        "accent_dark": "#6a1cb3",
        "description": "Dashboard de resultados y análisis de impacto de todas las automatizaciones implementadas",
        "button_text": "Acceder",
        "status": "🟡 DESARROLLO"
    }
]

# Renderizar tarjetas 3D - MANTENIENDO ESTRUCTURA ORIGINAL
columns = [col1, col2, col3, col4]
for i, (col, area) in enumerate(zip(columns, areas_data)):
    with col:
        st.markdown(f"""
        <div class="card-3d" style="height: 320px; display: flex; flex-direction: column;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
                <div class="icon-3d">
                    <span style='color: white; font-size: 1.5rem;'>{area['icon']}</span>
                </div>
                <div style="font-size: 0.7rem; font-weight: 600; color: #666; background: rgba(0,0,0,0.05); padding: 0.2rem 0.5rem; border-radius: 8px;">
                    {area['status']}
                </div>
            </div>
            
            <h3 style='
                color: #1a1a1a;
                font-size: 1.3rem;
                font-weight: 700;
                margin-bottom: 1rem;
                line-height: 1.3;
            '>
            {area['name']}
            </h3>
            
            <div style='
                color: #666666;
                line-height: 1.5;
                margin-bottom: 1.5rem;
                flex-grow: 1;
                font-size: 0.85rem;
            '>
                {area['description']}
            </div>
            
            <button class="btn-3d" style="width: 100%; margin-top: auto;">
                {area['button_text']}
            </button>
        </div>
        """, unsafe_allow_html=True)

# FOOTER MEJORADO - MANTENIENDO ESTRUCTURA ORIGINAL
st.markdown("""
<div style='
    background: linear-gradient(135deg, #f8f9fa, #e9ecef);
    padding: 2.5rem 0;
    margin-top: 4rem;
    text-align: center;
    border-top: 1px solid #e0e0e0;
'>
    <h4 style='color: #1a1a1a; margin-bottom: 0.8rem; font-size: 1.2rem; font-weight: 600;'>TodoDrogas - Sistema de Automatización</h4>
    <p style='color: #666666; margin-bottom: 0.4rem; font-size: 0.95rem;'>Optimizando procesos mediante tecnología avanzada</p>
    <p style='color: #999999; font-size: 0.8rem;'>© 2024 Todos los derechos reservados | v2.1.0</p>
</div>
""", unsafe_allow_html=True)
