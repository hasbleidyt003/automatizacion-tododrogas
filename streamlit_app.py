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

# HERO SECTION 3D MODERNA (se mantiene igual)
st.markdown("""
<style>
.hero-3d {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 4rem 2rem;
    border-radius: 20px;
    margin: 1rem 0;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}

.hero-3d::before {
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
    50% { transform: translateY(-20px) rotate(180deg); }
}

.hero-title {
    color: white;
    font-size: 3.5rem;
    font-weight: 800;
    text-align: center;
    margin-bottom: 1rem;
    text-shadow: 0 10px 30px rgba(0,0,0,0.3);
    font-family: 'Inter', sans-serif;
}

.hero-subtitle {
    color: rgba(255,255,255,0.9);
    font-size: 1.3rem;
    text-align: center;
    margin-bottom: 1rem;
    font-weight: 300;
}

/* SECCIONES FUTURISTAS POR ÁREA */
.area-section {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border-radius: 25px;
    padding: 3rem;
    margin: 2rem 0;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.1);
    border: 1px solid rgba(255,255,255,0.3);
    backdrop-filter: blur(10px);
}

.area-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: linear-gradient(90deg, var(--accent-color), transparent);
}

.area-header {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.area-icon {
    font-size: 4rem;
    filter: drop-shadow(0 10px 20px rgba(0,0,0,0.2));
}

.area-title {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--accent-color);
    margin: 0;
    text-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.area-description {
    font-size: 1.3rem;
    color: #666;
    margin-bottom: 2rem;
    line-height: 1.6;
}

/* GRID DE AUTOMATIZACIONES */
.automations-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.automation-card {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    border-left: 5px solid var(--accent-color);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.automation-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(var(--accent-rgb), 0.05), transparent);
    transition: left 0.6s;
}

.automation-card:hover::before {
    left: 100%;
}

.automation-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}

.automation-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: var(--accent-color);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.automation-features {
    list-style: none;
    padding: 0;
    margin: 0;
}

.automation-features li {
    padding: 0.5rem 0;
    color: #666;
    border-bottom: 1px solid #f0f0f0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.automation-features li:last-child {
    border-bottom: none;
}

.automation-features li::before {
    content: '▸';
    color: var(--accent-color);
    font-weight: bold;
}

/* BOTÓN DE ACCIÓN */
.action-btn {
    background: linear-gradient(135deg, var(--accent-color), var(--accent-dark));
    color: white;
    border: none;
    padding: 1rem 2.5rem;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1.1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(var(--accent-rgb), 0.3);
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.action-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 40px rgba(var(--accent-rgb), 0.4);
}

/* ESTADÍSTICAS COMPACTAS */
.stats-compact {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
}

.stat-item {
    text-align: center;
    padding: 1.5rem;
    background: rgba(var(--accent-rgb), 0.1);
    border-radius: 15px;
    border: 1px solid rgba(var(--accent-rgb), 0.2);
}

.stat-number {
    font-size: 2rem;
    font-weight: 700;
    color: var(--accent-color);
    margin-bottom: 0.5rem;
}

.stat-label {
    font-size: 0.9rem;
    color: #666;
    font-weight: 500;
}
</style>

<div class="hero-3d">
    <div class="hero-title">Sistema de Automatización</div>
    <div class="hero-subtitle">Transformando procesos mediante tecnología inteligente</div>
</div>
""", unsafe_allow_html=True)

# MENSAJE PRINCIPAL COMPACTO
st.markdown("""
<div style='text-align: center; margin: 2rem 0;'>
    <h2 style='color: #1a1a1a; font-size: 2rem; font-weight: 600; margin-bottom: 1rem;'>
        Optimización por Áreas Especializadas
    </h2>
    <p style='color: #666666; font-size: 1.2rem; line-height: 1.6; max-width: 800px; margin: 0 auto;'>
        Centralizamos soluciones automatizadas diseñadas específicamente para cada departamento, 
        maximizando la eficiencia y reduciendo tiempos operativos.
    </p>
</div>
""", unsafe_allow_html=True)

# DEFINICIÓN DE ÁREAS CON AUTOMATIZACIONES ESPECÍFICAS
areas_data = [
    {
        "id": "cuentas-medicas",
        "title": "📋 Cuentas Médicas",
        "accent_color": "#0066cc",
        "accent_rgb": "0, 102, 204",
        "accent_dark": "#004499",
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
                    "Extracción y transformación de datos",
                    "Validación de reglas de negocio"
                ]
            },
            {
                "title": "🏷️ Renombradores Inteligentes", 
                "subtitle": "RIPS & CUV",
                "features": [
                    "Renombrado masivo por estándares RIPS",
                    "Aplicación automática de nomenclatura CUV",
                    "Validación de nombres según políticas",
                    "Generación de logs de cambios"
                ]
            },
            {
                "title": "🔍 Procesador OCR + Renombrado",
                "subtitle": "SALUD TOTAL",
                "features": [
                    "Reconocimiento óptico de caracteres en PDF",
                    "Extracción inteligente de datos clave",
                    "Renombrado automático por contenido",
                    "Integración con sistemas existentes"
                ]
            }
        ]
    },
    {
        "id": "cartera", 
        "title": "💰 Cartera",
        "accent_color": "#00a86b",
        "accent_rgb": "0, 168, 107",
        "accent_dark": "#007a4d",
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
                    "Clasificación inteligente de transacciones",
                    "Generación de alertas en tiempo real"
                ]
            },
            {
                "title": "📈 Generador de Reportes",
                "subtitle": "Business Intelligence", 
                "features": [
                    "Reportes financieros automáticos",
                    "Dashboards interactivos personalizados",
                    "Análisis predictivo de cartera",
                    "Exportación multi-formato"
                ]
            }
        ]
    },
    {
        "id": "tesoreria",
        "title": "🏦 Tesorería", 
        "accent_color": "#ff6b35",
        "accent_rgb": "255, 107, 53",
        "accent_dark": "#cc552b",
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
                    "Generación de asientos contables",
                    "Integración cross-platform"
                ]
            },
            {
                "title": "📋 Gestor de Estados Bancarios",
                "subtitle": "Control Total", 
                "features": [
                    "Procesamiento de estados en tiempo real",
                    "Alertas de movimientos inusuales",
                    "Reportes de flujo de caja automáticos",
                    "Proyecciones financieras inteligentes"
                ]
            }
        ]
    },
    {
        "id": "metricas",
        "title": "📊 Métricas y Contacto",
        "accent_color": "#8a2be2", 
        "accent_rgb": "138, 43, 226",
        "accent_dark": "#6a1cb3",
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
                    "Reportes de productividad comparativa",
                    "Alertas de rendimiento"
                ]
            },
            {
                "title": "💡 Centro de Soporte",
                "subtitle": "Soporte Integral", 
                "features": [
                    "Solicitud de nuevas automatizaciones",
                    "Soporte técnico especializado",
                    "Capacitación y documentación",
                    "Mejora continua de procesos"
                ]
            }
        ]
    }
]

# RENDERIZAR SECCIONES FUTURISTAS PARA CADA ÁREA
for area in areas_data:
    st.markdown(f"""
    <div class="area-section" style="--accent-color: {area['accent_color']}; --accent-rgb: {area['accent_rgb']}; --accent-dark: {area['accent_dark']};">
        <div class="area-header">
            <div class="area-icon">{area['title'].split()[0]}</div>
            <div>
                <h2 class="area-title">{area['title']}</h2>
                <p class="area-description">{area['description']}</p>
            </div>
        </div>
        
        <div class="stats-compact">
            {''.join([f'''
            <div class="stat-item">
                <div class="stat-number">{stat['number']}</div>
                <div class="stat-label">{stat['label']}</div>
            </div>
            ''' for stat in area['stats']])}
        </div>
        
        <div class="automations-grid">
            {''.join([f'''
            <div class="automation-card">
                <div class="automation-title">
                    {automation['title']}
                    <span style="font-size: 0.9rem; color: #999; font-weight: 400;">{automation['subtitle']}</span>
                </div>
                <ul class="automation-features">
                    {''.join([f'<li>{feature}</li>' for feature in automation['features']])}
                </ul>
            </div>
            ''' for automation in area['automations']])}
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <button class="action-btn" onclick="navigateToArea('{area['id']}')">
                🚀 Acceder a {area['title'].split()[-1]}
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# JAVASCRIPT PARA NAVEGACIÓN
st.markdown("""
<script>
function navigateToArea(areaId) {
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

// Animación de aparición escalonada
document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('.area-section');
    sections.forEach((section, index) => {
        setTimeout(() => {
            section.style.opacity = '1';
            section.style.transform = 'translateY(0)';
        }, index * 300);
    });
});
</script>

<style>
.area-section {
    opacity: 0;
    transform: translateY(50px);
    transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>
""", unsafe_allow_html=True)

# FOOTER MODERNO COMPACTO
st.markdown("""
<div style='
    background: #f8f9fa;
    padding: 2rem 0;
    margin-top: 3rem;
    text-align: center;
    border-top: 1px solid #e0e0e0;
'>
    <h4 style='color: #1a1a1a; margin-bottom: 1rem;'>TodoDrogas - Sistema de Automatización</h4>
    <p style='color: #666666; margin-bottom: 0.5rem;'>Transformando procesos mediante tecnología de vanguardia</p>
    <p style='color: #999999; font-size: 0.9rem;'>© 2024 Todos los derechos reservados</p>
</div>
""", unsafe_allow_html=True)
