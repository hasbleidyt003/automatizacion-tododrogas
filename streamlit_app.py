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

# CSS personalizado para el diseño
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 3rem 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        margin: 1rem 0;
        color: white;
    }
    
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        font-family: 'Inter', sans-serif;
    }
    
    .main-subtitle {
        font-size: 1.3rem;
        opacity: 0.9;
        font-weight: 300;
    }
    
    .section-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 3rem 0 1rem 0;
        color: #1a1a1a;
    }
    
    .section-description {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 3rem;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .area-card {
        background: white;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid #f0f0f0;
        transition: all 0.3s ease;
    }
    
    .area-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    
    .area-header {
        display: flex;
        align-items: center;
        gap: 1.5rem;
        margin-bottom: 2rem;
    }
    
    .area-icon {
        font-size: 3rem;
    }
    
    .area-name {
        font-size: 2rem;
        font-weight: 700;
        color: #1a1a1a;
        margin: 0;
    }
    
    .area-desc {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    .stats-grid {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .stat-item {
        text-align: center;
        padding: 1.5rem;
        background: #f8f9fa;
        border-radius: 15px;
        min-width: 120px;
    }
    
    .stat-number {
        font-size: 1.8rem;
        font-weight: 700;
        color: #0066cc;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #666;
        font-weight: 500;
    }
    
    .automation-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .automation-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        border-left: 4px solid #0066cc;
        transition: all 0.3s ease;
    }
    
    .automation-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.12);
    }
    
    .automation-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .automation-subtitle {
        font-size: 0.9rem;
        color: #666;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    .feature-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .feature-list li {
        padding: 0.3rem 0;
        color: #666;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .feature-list li:before {
        content: "▸";
        color: #0066cc;
        font-weight: bold;
    }
    
    .action-button {
        background: linear-gradient(135deg, #0066cc, #004499);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        text-decoration: none;
    }
    
    .action-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,102,204,0.3);
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div class="main-header">
    <div class="main-title">Sistema de Automatización</div>
    <div class="main-subtitle">Transformando procesos mediante tecnología inteligente</div>
</div>
""", unsafe_allow_html=True)

# INTRODUCCIÓN
st.markdown("""
<div class="section-title">Optimización por Áreas Especializadas</div>
<div class="section-description">
    Centralizamos soluciones automatizadas diseñadas específicamente para cada departamento, 
    maximizando la eficiencia y reduciendo tiempos operativos.
</div>
""", unsafe_allow_html=True)

# ÁREAS DE AUTOMATIZACIÓN
areas = [
    {
        "name": "📋 Cuentas Médicas",
        "color": "#0066cc",
        "description": "Automatización integral de procesos médicos y administrativos para optimizar la gestión de cuentas",
        "stats": [
            {"number": "85%", "label": "Reducción tiempos"},
            {"number": "99.2%", "label": "Precisión"},
            {"number": "24/7", "label": "Disponibilidad"},
            {"number": "±0", "label": "Errores"}
        ],
        "automations": [
            {
                "title": "🔄 Procesadores JSON",
                "subtitle": "SAVIA & COOSALUD",
                "features": [
                    "Validación automática de estructura JSON",
                    "Conversión entre formatos específicos", 
                    "Extracción y transformación de datos"
                ]
            },
            {
                "title": "🏷️ Renombradores Inteligentes", 
                "subtitle": "RIPS & CUV",
                "features": [
                    "Renombrado masivo por estándares RIPS",
                    "Aplicación automática de nomenclatura CUV",
                    "Validación de nombres según políticas"
                ]
            },
            {
                "title": "🔍 Procesador OCR + Renombrado",
                "subtitle": "SALUD TOTAL",
                "features": [
                    "Reconocimiento óptico de caracteres en PDF",
                    "Extracción inteligente de datos clave",
                    "Renombrado automático por contenido"
                ]
            }
        ],
        "page": "Cuentas_Medicas"
    },
    {
        "name": "💰 Cartera",
        "color": "#00a86b", 
        "description": "Gestión automatizada de estados financieros y reportes con inteligencia artificial",
        "stats": [
            {"number": "92%", "label": "Procesos auto"},
            {"number": "±0", "label": "Discrepancias"},
            {"number": "5min", "label": "Por reporte"},
            {"number": "100%", "label": "Trazabilidad"}
        ],
        "automations": [
            {
                "title": "📊 Procesador Estados de Cuenta",
                "subtitle": "Análisis Automático",
                "features": [
                    "Procesamiento automático de extractos",
                    "Detección de anomalías y discrepancias",
                    "Clasificación inteligente de transacciones"
                ]
            },
            {
                "title": "📈 Generador de Reportes",
                "subtitle": "Business Intelligence", 
                "features": [
                    "Reportes financieros automáticos",
                    "Dashboards interactivos personalizados",
                    "Análisis predictivo de cartera"
                ]
            }
        ],
        "page": "Cartera"
    },
    {
        "name": "🏦 Tesorería",
        "color": "#ff6b35",
        "description": "Control y gestión automatizada del flujo financiero con máxima seguridad",
        "stats": [
            {"number": "99.9%", "label": "Exactitud"},
            {"number": "3min", "label": "Conciliación"}, 
            {"number": "0", "label": "Errores humanos"},
            {"number": "100%", "label": "Auditoría"}
        ],
        "automations": [
            {
                "title": "🔄 Conciliador Automático",
                "subtitle": "Bancos & Sistemas",
                "features": [
                    "Conciliación automática bancaria",
                    "Detección automática de diferencias",
                    "Generación de asientos contables"
                ]
            },
            {
                "title": "📋 Gestor de Estados Bancarios",
                "subtitle": "Control Total", 
                "features": [
                    "Procesamiento de estados en tiempo real",
                    "Alertas de movimientos inusuales",
                    "Reportes de flujo de caja automáticos"
                ]
            }
        ],
        "page": "Tesoreria"
    },
    {
        "name": "📊 Métricas y Contacto",
        "color": "#8a2be2",
        "description": "Seguimiento, análisis y soporte integral para todas las automatizaciones",
        "stats": [
            {"number": "360°", "label": "Visibilidad"},
            {"number": "24/7", "label": "Soporte"},
            {"number": "±0", "label": "Downtime"},
            {"number": "100%", "label": "Satisfacción"}
        ],
        "automations": [
            {
                "title": "📈 Dashboard de Métricas",
                "subtitle": "Análisis de Impacto",
                "features": [
                    "Métricas de eficiencia en tiempo real",
                    "ROI de automatizaciones por área",
                    "Reportes de productividad comparativa"
                ]
            },
            {
                "title": "💡 Centro de Soporte",
                "subtitle": "Soporte Integral", 
                "features": [
                    "Solicitud de nuevas automatizaciones",
                    "Soporte técnico especializado",
                    "Capacitación y documentación"
                ]
            }
        ],
        "page": "Metricas_y_Contacto"
    }
]

# Renderizar cada área usando una función para evitar problemas con unsafe_allow_html
def render_area_card(area):
    # Construir el HTML para las estadísticas
    stats_html = ""
    for stat in area['stats']:
        stats_html += f"""
        <div class="stat-item">
            <div class="stat-number" style="color: {area['color']}">{stat['number']}</div>
            <div class="stat-label">{stat['label']}</div>
        </div>
        """
    
    # Construir el HTML para las automatizaciones
    automations_html = ""
    for automation in area['automations']:
        features_html = "".join([f"<li>{feature}</li>" for feature in automation['features']])
        automations_html += f"""
        <div class="automation-card">
            <div class="automation-title">{automation['title']}</div>
            <div class="automation-subtitle">{automation['subtitle']}</div>
            <ul class="feature-list">
                {features_html}
            </ul>
        </div>
        """
    
    # HTML completo de la tarjeta
    area_html = f"""
    <div class="area-card">
        <div class="area-header">
            <div class="area-icon">{area['name'].split()[0]}</div>
            <div>
                <h2 class="area-name">{area['name']}</h2>
                <p class="area-desc">{area['description']}</p>
            </div>
        </div>
        
        <div class="stats-grid">
            {stats_html}
        </div>
        
        <div class="automation-grid">
            {automations_html}
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <a href="/{area['page']}" class="action-button">
                🚀 Acceder a {area['name'].split()[-1].replace('📊', 'Métricas')}
            </a>
        </div>
    </div>
    """
    
    return area_html

# Mostrar cada área
for area in areas:
    area_html = render_area_card(area)
    st.markdown(area_html, unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; padding: 2rem 0;'>"
    "<h4>TodoDrogas - Sistema de Automatización</h4>"
    "<p>Transformando procesos mediante tecnología de vanguardia</p>"
    "<small>© 2024 Todos los derechos reservados</small>"
    "</div>",
    unsafe_allow_html=True
)
