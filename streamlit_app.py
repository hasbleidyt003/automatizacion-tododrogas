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

# HERO SECTION 3D MODERNA
st.markdown("""
<style>
.hero-3d {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 5rem 2rem;
    border-radius: 20px;
    margin: 2rem 0;
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
    font-size: 4rem;
    font-weight: 800;
    text-align: center;
    margin-bottom: 1rem;
    text-shadow: 0 10px 30px rgba(0,0,0,0.3);
    font-family: 'Inter', sans-serif;
}

.hero-subtitle {
    color: rgba(255,255,255,0.9);
    font-size: 1.5rem;
    text-align: center;
    margin-bottom: 2rem;
    font-weight: 300;
}

/* TARJETAS 3D */
.card-3d {
    background: white;
    border-radius: 20px;
    padding: 2.5rem;
    margin: 1rem 0;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    backdrop-filter: blur(10px);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
}

.card-3d::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #0066cc, #00a86b, #ff6b35, #8a2be2);
}

.card-3d:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 25px 50px rgba(0,0,0,0.15);
}

/* BOTONES FLOTANTES */
.floating-btn {
    background: linear-gradient(135deg, #0066cc, #004499);
    color: white;
    border: none;
    padding: 1.2rem 2.5rem;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1.1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(0,102,204,0.3);
    position: relative;
    overflow: hidden;
}

.floating-btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s;
}

.floating-btn:hover::before {
    left: 100%;
}

.floating-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 40px rgba(0,102,204,0.4);
}

/* MENÚ DESPLEGABLE 3D */
.accordion-3d {
    background: linear-gradient(135deg, #f8f9fa, #e9ecef);
    border-radius: 15px;
    margin: 1rem 0;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.accordion-header {
    background: linear-gradient(135deg, #0066cc, #004499);
    color: white;
    padding: 1.5rem 2rem;
    cursor: pointer;
    font-weight: 600;
    font-size: 1.2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.3s ease;
}

.accordion-header:hover {
    background: linear-gradient(135deg, #0052a3, #003366);
}

.accordion-content {
    padding: 2rem;
    background: white;
    display: none;
}

.accordion-3d.active .accordion-content {
    display: block;
    animation: slideDown 0.3s ease;
}

@keyframes slideDown {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ESTADÍSTICAS FLOTANTES */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin: 3rem 0;
}

.stat-card {
    background: white;
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    border: 1px solid #f0f0f0;
}

.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.12);
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 700;
    color: #0066cc;
    margin-bottom: 0.5rem;
}

.stat-label {
    color: #666;
    font-size: 0.9rem;
    font-weight: 500;
}
</style>

<div class="hero-3d">
    <div class="hero-title">Sistema de Automatización</div>
    <div class="hero-subtitle">Transformando procesos mediante tecnología inteligente</div>
</div>
""", unsafe_allow_html=True)

# MENSAJE PRINCIPAL CENTRADO
st.markdown("""
<div style='text-align: center; margin: 3rem 0;'>
    <h2 style='color: #1a1a1a; font-size: 2.2rem; font-weight: 600; margin-bottom: 1rem;'>
        Optimización por Áreas Especializadas
    </h2>
    <p style='color: #666666; font-size: 1.3rem; line-height: 1.6; max-width: 800px; margin: 0 auto;'>
        Centralizamos soluciones automatizadas diseñadas específicamente para cada departamento, 
        maximizando la eficiencia y reduciendo tiempos operativos.
    </p>
</div>
""", unsafe_allow_html=True)

# ESTADÍSTICAS IMPACTANTES
st.markdown("""
<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-number">+85%</div>
        <div class="stat-label">Reducción de tiempos</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">99.2%</div>
        <div class="stat-label">Precisión en procesos</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">+200</div>
        <div class="stat-label">Procesos automatizados</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">24/7</div>
        <div class="stat-label">Disponibilidad</div>
    </div>
</div>
""", unsafe_allow_html=True)

# SECCIÓN DE ÁREAS CON MENÚ DESPLEGABLE 3D
st.markdown("""
<div style='text-align: center; margin: 4rem 0 2rem 0;'>
    <h2 style='color: #1a1a1a; font-size: 2.5rem; font-weight: 600; margin-bottom: 1rem;'>
        Áreas de Automatización
    </h2>
    <p style='color: #666666; font-size: 1.2rem;'>
        Explora nuestras soluciones especializadas por departamento
    </p>
</div>
""", unsafe_allow_html=True)

# MENÚ DESPLEGABLE 3D PARA CADA ÁREA
areas = [
    {
        "title": "📋 Cuentas Médicas",
        "icon": "📋",
        "color": "#0066cc",
        "description": "Automatización de procesos médicos y administrativos",
        "features": [
            "Procesamiento JSON - SAVIA & COOSALUD",
            "Renombradores RIPS y CUV", 
            "OCR y Renombrado - SALUD TOTAL",
            "Validación automática de formatos"
        ]
    },
    {
        "title": "💰 Cartera",
        "icon": "💰", 
        "color": "#00a86b",
        "description": "Gestión automatizada de estados financieros",
        "features": [
            "Procesamiento de estados de cuenta",
            "Reportes automáticos",
            "Análisis de cartera",
            "Alertas inteligentes"
        ]
    },
    {
        "title": "🏦 Tesorería", 
        "icon": "🏦",
        "color": "#ff6b35",
        "description": "Control y gestión del flujo financiero",
        "features": [
            "Automatización de conciliaciones",
            "Control de estados bancarios",
            "Reportes de tesorería",
            "Análisis de flujo de caja"
        ]
    },
    {
        "title": "📊 Métricas y Contacto",
        "icon": "📊",
        "color": "#8a2be2", 
        "description": "Seguimiento y análisis de resultados",
        "features": [
            "Dashboard de métricas",
            "Reportes de impacto",
            "Análisis de eficiencia",
            "Soporte y contacto"
        ]
    }
]

for i, area in enumerate(areas):
    st.markdown(f"""
    <div class="accordion-3d" id="accordion-{i}">
        <div class="accordion-header" onclick="toggleAccordion({i})">
            <span>{area['icon']} {area['title']}</span>
            <span>▼</span>
        </div>
        <div class="accordion-content">
            <div style='color: #666; font-size: 1.1rem; margin-bottom: 1.5rem;'>
                {area['description']}
            </div>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 2rem;'>
                {''.join([f'<div style="color: #666; font-size: 0.95rem; padding: 0.5rem; background: #f8f9fa; border-radius: 8px;">✓ {feature}</div>' for feature in area['features']])}
            </div>
            <button class="floating-btn" onclick="navigateToArea({i})">
                Acceder a {area['title'].split()[-1]}
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# BOTONES FLOTANTES DE ACCIÓN RÁPIDA
st.markdown("""
<div style='text-align: center; margin: 4rem 0;'>
    <h3 style='color: #1a1a1a; font-size: 1.8rem; margin-bottom: 2rem;'>
        Acciones Rápidas
    </h3>
    <div style='display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap;'>
        <button class="floating-btn" onclick="navigateToArea(0)">
            🚀 Iniciar Automatización
        </button>
        <button class="floating-btn" style="background: linear-gradient(135deg, #00a86b, #007a4d);">
            📊 Ver Reportes
        </button>
        <button class="floating-btn" style="background: linear-gradient(135deg, #8a2be2, #6a1cb3);">
            💡 Solicitar Soporte
        </button>
    </div>
</div>
""", unsafe_allow_html=True)

# TARJETA DE BENEFICIOS
st.markdown("""
<div class="card-3d">
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h3 style='color: #1a1a1a; font-size: 2rem; margin-bottom: 1rem;'>¿Por qué automatizar?</h3>
    </div>
    <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;'>
        <div style='text-align: center;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>⚡</div>
            <h4 style='color: #1a1a1a; margin-bottom: 0.5rem;'>Velocidad</h4>
            <p style='color: #666;'>Procesa en minutos lo que antes tomaba horas</p>
        </div>
        <div style='text-align: center;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>🎯</div>
            <h4 style='color: #1a1a1a; margin-bottom: 0.5rem;'>Precisión</h4>
            <p style='color: #666;'>Elimina errores humanos en procesos repetitivos</p>
        </div>
        <div style='text-align: center;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>📈</div>
            <h4 style='color: #1a1a1a; margin-bottom: 0.5rem;'>Escalabilidad</h4>
            <p style='color: #666;'>Crece sin incrementar carga operativa</p>
        </div>
        <div style='text-align: center;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>💼</div>
            <h4 style='color: #1a1a1a; margin-bottom: 0.5rem;'>Enfoque</h4>
            <p style='color: #666;'>Tu equipo se concentra en lo realmente importante</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# JAVASCRIPT PARA INTERACTIVIDAD
st.markdown("""
<script>
function toggleAccordion(index) {
    const accordion = document.getElementById(`accordion-${index}`);
    accordion.classList.toggle('active');
}

function navigateToArea(index) {
    const areas = ['Cuentas_Medicas', 'Cartera', 'Tesoreria', 'Metricas_y_Contacto'];
    window.location.href = `/${areas[index]}`;
}

// Efecto de aparición suave
document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.card-3d, .stat-card');
    elements.forEach((el, index) => {
        setTimeout(() => {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, index * 200);
    });
});
</script>

<style>
.card-3d, .stat-card {
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.6s ease;
}
</style>
""", unsafe_allow_html=True)

# FOOTER MODERNO
st.markdown("""
<div style='
    background: #f8f9fa;
    padding: 3rem 0;
    margin-top: 4rem;
    text-align: center;
    border-top: 1px solid #e0e0e0;
'>
    <h4 style='color: #1a1a1a; margin-bottom: 1rem;'>TodoDrogas - Sistema de Automatización</h4>
    <p style='color: #666666; margin-bottom: 0.5rem;'>Transformando procesos mediante tecnología de vanguardia</p>
    <p style='color: #999999; font-size: 0.9rem;'>© 2024 Todos los derechos reservados</p>
</div>
""", unsafe_allow_html=True)
