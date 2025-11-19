import streamlit as st
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

# Configurar tema moderno
configure_modern_theme()

# Configurar página
st.set_page_config(
    page_title="Sistema de Automatización - Tododrogas",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Navbar moderna
modern_navbar()

# CSS minimalista y futurista
st.markdown("""
<style>
    /* Reset y base minimalista */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 0;
    }
    
    /* Hero section minimalista */
    .hero-minimal {
        background: transparent;
        padding: 2rem 0 1rem 0;
        margin: 0;
        text-align: center;
        position: relative;
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        line-height: 1.1;
        font-family: "Inter", sans-serif;
        background: linear-gradient(135deg, #0066cc 0%, #00a8ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        color: #666;
        font-size: 1.1rem;
        font-weight: 400;
        margin-bottom: 2rem;
        line-height: 1.4;
        font-family: "Inter", sans-serif;
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Grid de tarjetas futuristas */
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .card-futurist {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 16px;
        padding: 2rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .card-futurist::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, #0066cc, transparent);
    }
    
    .card-futurist::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 102, 204, 0.05), transparent);
        transition: left 0.6s ease;
    }
    
    .card-futurist:hover::after {
        left: 100%;
    }
    
    .card-futurist:hover {
        transform: translateY(-5px);
        box-shadow: 
            0 20px 40px rgba(0, 102, 204, 0.1),
            0 8px 25px rgba(0, 0, 0, 0.05);
        border-color: rgba(0, 102, 204, 0.2);
    }
    
    .card-icon {
        width: 50px;
        height: 50px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #0066cc, #00a8ff);
        font-size: 1.3rem;
        color: white;
        transition: all 0.3s ease;
    }
    
    .card-futurist:hover .card-icon {
        transform: scale(1.1) rotate(5deg);
    }
    
    .card-title {
        color: #1a1a1a;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        line-height: 1.3;
    }
    
    .card-description {
        color: #666;
        line-height: 1.5;
        margin-bottom: 1.5rem;
        font-size: 0.9rem;
    }
    
    .card-button {
        background: transparent;
        color: #0066cc;
        border: 1.5px solid #0066cc;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.85rem;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        position: relative;
        overflow: hidden;
    }
    
    .card-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 102, 204, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .card-button:hover::before {
        left: 100%;
    }
    
    .card-button:hover {
        background: #0066cc;
        color: white;
        transform: translateY(-1px);
    }
    
    /* Sección de beneficios minimalista */
    .benefits-section {
        background: transparent;
        margin: 3rem 0;
    }
    
    .benefits-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }
    
    .benefit-item {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .benefit-item:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0, 102, 204, 0.1);
        border-color: rgba(0, 102, 204, 0.2);
    }
    
    .benefit-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #0066cc, #00a8ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .benefit-title {
        color: #1a1a1a;
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .benefit-description {
        color: #666;
        font-size: 0.85rem;
        line-height: 1.4;
    }
    
    /* Footer minimalista */
    .footer-minimal {
        background: transparent;
        padding: 2rem 0;
        margin-top: 3rem;
        text-align: center;
        border-top: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    /* Efectos de partículas sutiles */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .floating {
        animation: float 6s ease-in-out infinite;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.2rem;
        }
        
        .hero-subtitle {
            font-size: 1rem;
        }
        
        .cards-grid {
            grid-template-columns: 1fr;
            gap: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION MINIMALISTA
st.markdown("""
<div class="hero-minimal">
    <h1 class="hero-title">Sistema de Automatización</h1>
    <p class="hero-subtitle">Optimizando procesos mediante tecnología inteligente y eficiente</p>
</div>
""", unsafe_allow_html=True)

# SECCIÓN DE AUTOMATIZACIONES
st.markdown("""
<div style='text-align: center; margin: 2rem 0;'>
    <h2 style='color: #1a1a1a; font-size: 1.5rem; font-weight: 600; margin-bottom: 0.5rem;'>
        Áreas de Automatización
    </h2>
    <p style='color: #666; font-size: 0.95rem;'>
        Herramientas especializadas para cada departamento
    </p>
</div>
""", unsafe_allow_html=True)

# GRID DE TARJETAS FUTURISTAS
areas_data = [
    {
        "name": "Cuentas Médicas",
        "icon": "📋",
        "description": "Procesamiento automatizado de documentos médicos y conversión de formatos",
        "button_text": "Acceder"
    },
    {
        "name": "Cartera",
        "icon": "💰", 
        "description": "Gestión inteligente de estados de cuenta y reportes financieros",
        "button_text": "Acceder"
    },
    {
        "name": "Tesorería",
        "icon": "🏦",
        "description": "Control automatizado de estados bancarios y flujo financiero",
        "button_text": "Acceder"
    },
    {
        "name": "Métricas",
        "icon": "📊",
        "description": "Dashboard de resultados y análisis de impacto en tiempo real",
        "button_text": "Acceder"
    }
]

# Crear el grid con HTML
st.markdown("""
<div class="cards-grid">
""", unsafe_allow_html=True)

for area in areas_data:
    st.markdown(f"""
    <div class="card-futurist">
        <div class="card-icon">{area['icon']}</div>
        <h3 class="card-title">{area['name']}</h3>
        <p class="card-description">{area['description']}</p>
        <button class="card-button" onclick="navigateTo('{area['name'].lower().replace(' ', '_').replace('métricas', 'metricas')}')">
            {area['button_text']}
        </button>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# SEPARADOR SUTIL
st.markdown("<div style='height: 1px; background: linear-gradient(90deg, transparent, #e0e0e0, transparent); margin: 3rem 0;'></div>", unsafe_allow_html=True)

# BENEFICIOS CLAVE
st.markdown("""
<div class="benefits-section">
    <div style='text-align: center;'>
        <h2 style='color: #1a1a1a; font-size: 1.5rem; font-weight: 600; margin-bottom: 0.5rem;'>
            Beneficios Clave
        </h2>
        <p style='color: #666; font-size: 0.95rem; margin-bottom: 2rem;'>
            Ventajas competitivas de nuestra plataforma
        </p>
    </div>
    
    <div class="benefits-grid">
        <div class="benefit-item">
            <div class="benefit-icon">⚡</div>
            <h4 class="benefit-title">Reducción de Tiempos</h4>
            <p class="benefit-description">Procesa en minutos lo que antes tomaba horas</p>
        </div>
        
        <div class="benefit-item">
            <div class="benefit-icon">🎯</div>
            <h4 class="benefit-title">Mayor Precisión</h4>
            <p class="benefit-description">Elimina errores humanos con validaciones automáticas</p>
        </div>
        
        <div class="benefit-item">
            <div class="benefit-icon">📊</div>
            <h4 class="benefit-title">Reportes Automáticos</h4>
            <p class="benefit-description">Genera insights en tiempo real sin intervención manual</p>
        </div>
        
        <div class="benefit-item">
            <div class="benefit-icon">🔗</div>
            <h4 class="benefit-title">Integración Total</h4>
            <p class="benefit-description">Conecta todos tus sistemas en una plataforma unificada</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# FOOTER MINIMALISTA
st.markdown("""
<div class="footer-minimal">
    <h4 style='color: #1a1a1a; margin-bottom: 0.5rem; font-size: 1rem; font-weight: 600;'>
        TodoDrogas - Sistema de Automatización
    </h4>
    <p style='color: #666; font-size: 0.85rem; margin: 0;'>
        Optimizando procesos mediante tecnología avanzada
    </p>
</div>

<script>
function navigateTo(area) {
    const routes = {
        'cuentas_médicas': '/Cuentas_Medicas',
        'cartera': '/Cartera',
        'tesorería': '/Tesoreria',
        'metricas': '/Metricas_y_Contacto'
    };
    if (routes[area]) {
        window.location.href = routes[area];
    }
}
</script>
""", unsafe_allow_html=True)
