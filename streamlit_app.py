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

# CSS mínimo para mejorar el diseño
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
    
    .area-card {
        background: white;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid #f0f0f0;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .stat-box {
        text-align: center;
        padding: 1.5rem;
        background: #f8f9fa;
        border-radius: 15px;
        min-width: 120px;
    }
    
    .automation-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        border-left: 4px solid #0066cc;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div class="main-header">
    <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 1rem; font-family: 'Inter', sans-serif;">Sistema de Automatización</h1>
    <p style="font-size: 1.3rem; opacity: 0.9; font-weight: 300;">Transformando procesos mediante tecnología inteligente</p>
</div>
""", unsafe_allow_html=True)

# INTRODUCCIÓN
st.markdown("## Optimización por Áreas Especializadas")
st.markdown("""
<div style="text-align: center; margin-bottom: 3rem;">
    <p style="font-size: 1.2rem; color: #666; max-width: 800px; margin: 0 auto;">
        Centralizamos soluciones automatizadas diseñadas específicamente para cada departamento, 
        maximizando la eficiencia y reduciendo tiempos operativos.
    </p>
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

# Renderizar cada área usando componentes nativos de Streamlit
for area in areas:
    with st.container():
        # Tarjeta de área
        st.markdown(f"""
        <div class="area-card">
            <div style="display: flex; align-items: center; gap: 1.5rem; margin-bottom: 2rem;">
                <div style="font-size: 3rem;">{area['name'].split()[0]}</div>
                <div>
                    <h2 style="font-size: 2rem; font-weight: 700; color: #1a1a1a; margin: 0;">{area['name']}</h2>
                    <p style="font-size: 1.2rem; color: #666; margin: 0.5rem 0 0 0;">{area['description']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Estadísticas
        col1, col2, col3, col4 = st.columns(4)
        stats = area['stats']
        with col1:
            st.metric(label=stats[0]['label'], value=stats[0]['number'])
        with col2:
            st.metric(label=stats[1]['label'], value=stats[1]['number'])
        with col3:
            st.metric(label=stats[2]['label'], value=stats[2]['number'])
        with col4:
            st.metric(label=stats[3]['label'], value=stats[3]['number'])
        
        # Automatizaciones
        st.subheader("🚀 Automatizaciones Disponibles")
        for automation in area['automations']:
            with st.expander(f"{automation['title']} - {automation['subtitle']}", expanded=True):
                for feature in automation['features']:
                    st.write(f"• {feature}")
        
        # Botón de acción
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button(
                f"🚀 Acceder a {area['name'].split()[-1].replace('📊', 'Métricas')}", 
                key=f"btn_{area['page']}",
                use_container_width=True
            ):
                st.switch_page(f"pages/{area['page']}.py")
        
        st.markdown("---")

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
