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

# CSS para el diseño Pinterest
st.markdown("""
<style>
    .hero-section {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 24px;
        margin: 1rem 0 3rem 0;
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        font-family: 'Inter', sans-serif;
        text-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        opacity: 0.9;
        font-weight: 300;
        max-width: 600px;
        margin: 0 auto;
    }
    
    .section-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 4rem 0 2rem 0;
        color: #1a1a1a;
    }
    
    .area-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .area-card {
        background: white;
        border-radius: 20px;
        padding: 0;
        overflow: hidden;
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid #f0f0f0;
        cursor: pointer;
    }
    
    .area-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 50px rgba(0,0,0,0.15);
    }
    
    .card-header {
        padding: 2rem 2rem 1.5rem 2rem;
        background: linear-gradient(135deg, var(--accent-color), var(--accent-dark));
        color: white;
    }
    
    .card-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0;
        line-height: 1.3;
    }
    
    .card-description {
        font-size: 1rem;
        opacity: 0.9;
        margin: 0.5rem 0 0 0;
        line-height: 1.4;
    }
    
    .automation-list {
        padding: 1.5rem 2rem 2rem 2rem;
    }
    
    .automation-item {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        padding: 1rem 0;
        border-bottom: 1px solid #f5f5f5;
        transition: all 0.2s ease;
    }
    
    .automation-item:last-child {
        border-bottom: none;
    }
    
    .automation-item:hover {
        background: #fafafa;
        margin: 0 -1rem;
        padding: 1rem;
        border-radius: 12px;
    }
    
    .automation-icon {
        font-size: 1.5rem;
        margin-top: 0.2rem;
        flex-shrink: 0;
    }
    
    .automation-content {
        flex: 1;
    }
    
    .automation-name {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a1a;
        margin: 0 0 0.3rem 0;
    }
    
    .automation-subtitle {
        font-size: 0.9rem;
        color: #666;
        font-weight: 500;
        margin: 0 0 0.5rem 0;
    }
    
    .automation-features {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .automation-features li {
        font-size: 0.85rem;
        color: #666;
        padding: 0.2rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .automation-features li:before {
        content: "•";
        color: var(--accent-color);
        font-weight: bold;
    }
    
    .action-section {
        text-align: center;
        margin: 3rem 0;
        padding: 2rem;
    }
    
    .action-button {
        background: linear-gradient(135deg, #0066cc, #004499);
        color: white;
        border: none;
        padding: 1.2rem 3rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1.1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(0,102,204,0.3);
        display: inline-flex;
        align-items: center;
        gap: 0.8rem;
    }
    
    .action-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0,102,204,0.4);
    }
    
    .footer {
        text-align: center;
        color: #666;
        padding: 3rem 0 1rem 0;
        margin-top: 4rem;
        border-top: 1px solid #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div class="hero-section">
    <div class="hero-title">Sistema de Automatización</div>
    <div class="hero-subtitle">Transformando procesos mediante tecnología inteligente y soluciones especializadas por área</div>
</div>
""", unsafe_allow_html=True)

# TÍTULO DE SECCIÓN
st.markdown("""
<div class="section-title">Áreas de Automatización</div>
""", unsafe_allow_html=True)

# DATOS DE LAS ÁREAS
areas_data = [
    {
        "id": "cuentas-medicas",
        "icon": "📋",
        "title": "Cuentas Médicas",
        "description": "Automatización de procesos médicos y administrativos",
        "accent_color": "#0066cc",
        "accent_dark": "#004499",
        "automations": [
            {
                "icon": "🔄",
                "name": "Procesadores JSON",
                "subtitle": "SAVIA & COOSALUD",
                "features": ["Validación automática de estructura", "Conversión entre formatos", "Extracción de datos"]
            },
            {
                "icon": "🏷️",
                "name": "Renombradores Inteligentes",
                "subtitle": "RIPS & CUV", 
                "features": ["Renombrado masivo por estándares", "Aplicación automática CUV", "Validación de políticas"]
            },
            {
                "icon": "🔍",
                "name": "Procesador OCR + Renombrado",
                "subtitle": "SALUD TOTAL",
                "features": ["Reconocimiento óptico en PDF", "Extracción inteligente de datos", "Renombrado automático"]
            }
        ]
    },
    {
        "id": "cartera",
        "icon": "💰", 
        "title": "Cartera",
        "description": "Gestión automatizada de estados financieros",
        "accent_color": "#00a86b",
        "accent_dark": "#007a4d",
        "automations": [
            {
                "icon": "📊",
                "name": "Procesador Estados de Cuenta",
                "subtitle": "Análisis Automático",
                "features": ["Procesamiento automático", "Detección de anomalías", "Clasificación inteligente"]
            },
            {
                "icon": "📈",
                "name": "Generador de Reportes",
                "subtitle": "Business Intelligence",
                "features": ["Reportes financieros automáticos", "Dashboards personalizados", "Análisis predictivo"]
            }
        ]
    },
    {
        "id": "tesoreria",
        "icon": "🏦",
        "title": "Tesorería", 
        "description": "Control automatizado del flujo financiero",
        "accent_color": "#ff6b35",
        "accent_dark": "#cc552b",
        "automations": [
            {
                "icon": "🔄",
                "name": "Conciliador Automático",
                "subtitle": "Bancos & Sistemas",
                "features": ["Conciliación bancaria automática", "Detección de diferencias", "Generación de asientos"]
            },
            {
                "icon": "📋",
                "name": "Gestor de Estados Bancarios", 
                "subtitle": "Control Total",
                "features": ["Procesamiento en tiempo real", "Alertas de movimientos", "Reportes automáticos"]
            }
        ]
    },
    {
        "id": "metricas",
        "icon": "📊",
        "title": "Métricas y Contacto",
        "description": "Seguimiento y soporte integral",
        "accent_color": "#8a2be2",
        "accent_dark": "#6a1cb3", 
        "automations": [
            {
                "icon": "📈",
                "name": "Dashboard de Métricas",
                "subtitle": "Análisis de Impacto",
                "features": ["Métricas en tiempo real", "ROI por área", "Reportes comparativos"]
            },
            {
                "icon": "💡",
                "name": "Centro de Soporte",
                "subtitle": "Soporte Integral",
                "features": ["Solicitud de automatizaciones", "Soporte técnico", "Capacitación"]
            }
        ]
    }
]

# CREAR GRID DE ÁREAS
st.markdown('<div class="area-grid">', unsafe_allow_html=True)

for area in areas_data:
    # Construir HTML para las automatizaciones
    automations_html = ""
    for automation in area['automations']:
        features_html = "".join([f"<li>{feature}</li>" for feature in automation['features']])
        automations_html += f"""
        <div class="automation-item">
            <div class="automation-icon">{automation['icon']}</div>
            <div class="automation-content">
                <div class="automation-name">{automation['name']}</div>
                <div class="automation-subtitle">{automation['subtitle']}</div>
                <ul class="automation-features">
                    {features_html}
                </ul>
            </div>
        </div>
        """
    
    # Tarjeta completa del área
    area_html = f"""
    <div class="area-card" onclick="navigateTo('{area['id']}')" 
         style="--accent-color: {area['accent_color']}; --accent-dark: {area['accent_dark']};">
        <div class="card-header">
            <div class="card-icon">{area['icon']}</div>
            <h3 class="card-title">{area['title']}</h3>
            <p class="card-description">{area['description']}</p>
        </div>
        <div class="automation-list">
            {automations_html}
        </div>
    </div>
    """
    
    st.markdown(area_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# SECCIÓN DE ACCIÓN
st.markdown("""
<div class="action-section">
    <h3 style="color: #1a1a1a; font-size: 1.8rem; margin-bottom: 1.5rem;">
        ¿Listo para transformar tus procesos?
    </h3>
    <p style="color: #666; font-size: 1.1rem; margin-bottom: 2rem; max-width: 500px; margin-left: auto; margin-right: auto;">
        Descubre cómo nuestras automatizaciones pueden optimizar tu flujo de trabajo
    </p>
    <button class="action-button" onclick="navigateTo('cuentas-medicas')">
        🚀 Comenzar Ahora
    </button>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
    <h4 style="margin-bottom: 1rem;">TodoDrogas - Sistema de Automatización</h4>
    <p style="margin-bottom: 0.5rem;">Transformando procesos mediante tecnología de vanguardia</p>
    <small>© 2024 Todos los derechos reservados</small>
</div>
""", unsafe_allow_html=True)

# JAVASCRIPT PARA NAVEGACIÓN
st.markdown("""
<script>
function navigateTo(areaId) {
    const routes = {
        'cuentas-medicas': '/Cuentas_Medicas',
        'cartera': '/Cartera',
        'tesoreria': '/Tesoreria', 
        'metricas': '/Metricas_y_Contacto'
    };
    
    if (routes[areaId]) {
        window.location.href = routes[areaId];
    }
}

// Agregar efecto de click a las tarjetas
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.area-card');
    cards.forEach(card => {
        card.style.cursor = 'pointer';
        card.addEventListener('click', function() {
            const areaId = this.getAttribute('onclick').match(/'([^']+)'/)[1];
            navigateTo(areaId);
        });
    });
});
</script>
""", unsafe_allow_html=True)
