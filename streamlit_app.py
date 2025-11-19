import streamlit as st
from components.navbar import modern_navbar
from config.theme import configure_modern_theme
import time
from datetime import datetime

# Configurar tema moderno
configure_modern_theme()

# Configurar página
st.set_page_config(
    page_title="Plataforma Inteligente Tododrogas",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Cache para datos pesados (OPTIMIZACIÓN)
@st.cache_data(ttl=3600)  # Cache por 1 hora
def get_system_metrics():
    """Simula métricas del sistema - optimizado con cache"""
    time.sleep(0.5)  # Simula procesamiento pesado
    return {
        'automatizaciones_ejecutadas': 1247,
        'tiempo_ahorrado': '342 horas',
        'eficiencia_incrementada': '68%',
        'usuarios_activos': 23
    }

# Navbar moderna
modern_navbar()

# CSS mejorado con fondo futurista animado
st.markdown("""
<style>
    /* Base mejorada con fondo futurista */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 0;
    }
    
    /* Fondo futurista animado para toda la app */
    .stApp {
        background: linear-gradient(-45deg, #0a0f2c, #1b2a41, #0d1b2a, #1b263b);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Hero section con efecto cristal mejorado */
    .hero-glass {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 28px;
        padding: 4rem 2rem;
        margin: 1rem 0 4rem 0;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 
            0 25px 50px rgba(0, 0, 0, 0.25),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }
    
    .hero-glass::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 102, 204, 0.1), transparent);
        transition: left 0.8s ease;
    }
    
    .hero-glass:hover::before {
        left: 100%;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1.2rem;
        line-height: 1.1;
        font-family: "Inter", sans-serif;
        background: linear-gradient(135deg, #00a8ff 0%, #0066cc 50%, #0097e6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
        text-shadow: 0 4px 20px rgba(0, 168, 255, 0.3);
    }
    
    .hero-subtitle {
        color: rgba(255, 255, 255, 0.85);
        font-size: 1.4rem;
        font-weight: 400;
        margin-bottom: 2rem;
        line-height: 1.5;
        font-family: "Inter", sans-serif;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Métricas interactivas con diseño mejorado */
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.2rem;
        margin: 2rem 0;
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        padding: 2rem 1.5rem;
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #00a8ff, #0097e6, #0066cc);
    }
    
    .metric-card:hover {
        transform: translateY(-8px);
        box-shadow: 
            0 20px 40px rgba(0, 102, 204, 0.25),
            0 0 30px rgba(0, 168, 255, 0.1);
        border-color: rgba(0, 168, 255, 0.3);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        color: #00a8ff;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 10px rgba(0, 168, 255, 0.3);
    }
    
    .metric-label {
        font-size: 0.95rem;
        color: rgba(255, 255, 255, 0.7);
        font-weight: 500;
    }
    
    /* Tarjetas con glass-morphism mejorado para fondo oscuro */
    .card-glass {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 24px;
        padding: 2.5rem;
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
        height: 100%;
        box-shadow: 
            0 20px 40px rgba(0, 0, 0, 0.25),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }
    
    .card-glass::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #00a8ff, #0097e6, #0066cc);
        border-radius: 24px 24px 0 0;
    }
    
    .card-glass::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transition: left 0.8s ease;
    }
    
    .card-glass:hover::after {
        left: 100%;
    }
    
    .card-glass:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 
            0 30px 60px rgba(0, 102, 204, 0.3),
            0 0 40px rgba(0, 168, 255, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
        border-color: rgba(0, 168, 255, 0.4);
    }
    
    .card-icon-glass {
        width: 80px;
        height: 80px;
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #00a8ff, #0066cc);
        font-size: 2rem;
        color: white;
        transition: all 0.4s ease;
        box-shadow: 
            0 12px 30px rgba(0, 102, 204, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
    }
    
    .card-glass:hover .card-icon-glass {
        transform: scale(1.15) rotate(8deg);
        box-shadow: 
            0 16px 40px rgba(0, 102, 204, 0.5),
            inset 0 1px 0 rgba(255, 255, 255, 0.4);
    }
    
    .card-title-glass {
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1.2rem;
        line-height: 1.3;
    }
    
    .card-description-glass {
        color: rgba(255, 255, 255, 0.75);
        line-height: 1.6;
        margin-bottom: 2.5rem;
        font-size: 1rem;
        flex-grow: 1;
    }
    
    .btn-glass {
        background: transparent;
        color: #00a8ff;
        border: 2px solid #00a8ff;
        padding: 1rem 2rem;
        border-radius: 14px;
        font-weight: 600;
        font-size: 0.95rem;
        cursor: pointer;
        transition: all 0.4s ease;
        width: 100%;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    .btn-glass::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 168, 255, 0.2), transparent);
        transition: left 0.6s ease;
    }
    
    .btn-glass:hover::before {
        left: 100%;
    }
    
    .btn-glass:hover {
        background: #00a8ff;
        color: white;
        transform: translateY(-3px);
        box-shadow: 
            0 12px 30px rgba(0, 168, 255, 0.4),
            0 0 20px rgba(0, 168, 255, 0.2);
    }
    
    /* Filtros interactivos mejorados */
    .filters-container {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        margin: 3rem 0;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    }
    
    /* Efectos de neón mejorados */
    .neon-glow {
        box-shadow: 
            0 0 30px rgba(0, 168, 255, 0.4),
            0 0 60px rgba(0, 168, 255, 0.2),
            0 0 90px rgba(0, 168, 255, 0.1);
    }
    
    /* Animaciones mejoradas */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }
    
    .floating {
        animation: float 8s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    .pulse {
        animation: pulse 3s ease-in-out infinite;
    }
    
    /* Ajustes para texto en fondo oscuro */
    h1, h2, h3, h4, h5, h6 {
        color: rgba(255, 255, 255, 0.95) !important;
    }
    
    p, div, span {
        color: rgba(255, 255, 255, 0.8) !important;
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION MEJORADA CON NUEVO TEXTO
st.markdown("""
<div class="hero-glass">
    <h1 class="hero-title">Plataforma Inteligente Tododrogas</h1>
    <p class="hero-subtitle">Tecnología que impulsa tu operación al siguiente nivel</p>
</div>
""", unsafe_allow_html=True)

# SECCIÓN DE AUTOMATIZACIONES MEJORADA
st.markdown("""
<div style='text-align: center; margin: 3rem 0 2rem 0;'>
    <h2 style='color: rgba(255, 255, 255, 0.95); font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem;'>
        Áreas de Automatización
    </h2>
    <p style='color: rgba(255, 255, 255, 0.75); font-size: 1.2rem;'>
        Selecciona un área para acceder a herramientas especializadas
    </p>
</div>
""", unsafe_allow_html=True)

# GRID DE TARJETAS CON GLASS-MORPHISM MEJORADO
areas_data = [
    {
        "name": "Cuentas Médicas",
        "icon": "📋",
        "description": "SAVIA & COOSALUD: Conversores JSON, Renombradores RIPS/CUV. SALUD TOTAL: Procesador OCR + Renombrado",
        "status": "Activo",
        "users": "8 usuarios"
    },
    {
        "name": "Cartera", 
        "icon": "💰",
        "description": "Gestión automatizada de estados de cuenta y reportes financieros con análisis inteligente y predicciones",
        "status": "Activo",
        "users": "6 usuarios"
    },
    {
        "name": "Tesorería",
        "icon": "🏦",
        "description": "Control automatizado de estados bancarios, flujo financiero y conciliaciones con máxima seguridad",
        "status": "En desarrollo", 
        "users": "4 usuarios"
    },
    {
        "name": "Métricas",
        "icon": "📊",
        "description": "Dashboard ejecutivo con análisis de impacto, ROI y métricas de todas las automatizaciones implementadas",
        "status": "Activo",
        "users": "5 usuarios"
    }
]

# Crear grid responsive
cols = st.columns(2)
for i, area in enumerate(areas_data):
    with cols[i % 2]:  # Distribuye en 2 columnas
        status_color = "#00a86b" if area["status"] == "Activo" else "#ff6b35"
        st.markdown(f"""
        <div class="card-glass">
            <div class="card-icon-glass">{area['icon']}</div>
            <h3 class="card-title-glass">{area['name']}</h3>
            <div style='display: flex; justify-content: space-between; margin-bottom: 1.5rem;'>
                <span style='background: {status_color}; color: white; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.85rem; font-weight: 600;'>
                    {area['status']}
                </span>
                <span style='color: rgba(255, 255, 255, 0.7); font-size: 0.85rem; font-weight: 500;'>
                    {area['users']}
                </span>
            </div>
            <p class="card-description-glass">{area['description']}</p>
            <button class="btn-glass" onclick="navigateTo('{area['name'].lower().replace(' ', '_').replace('métricas', 'metricas')}')">
                Acceder al Módulo
            </button>
        </div>
        """, unsafe_allow_html=True)

# SEPARADOR VISUAL MEJORADO
st.markdown("<div style='height: 3px; background: linear-gradient(90deg, transparent, #00a8ff, transparent); margin: 5rem 0;'></div>", unsafe_allow_html=True)

# MÉTRICAS INTERACTIVAS EN TIEMPO REAL
st.markdown("""
<div style='text-align: center; margin-bottom: 2rem;'>
    <h2 style='color: rgba(255, 255, 255, 0.95); font-size: 2.2rem; font-weight: 800; margin-bottom: 1rem;'>
        Dashboard Ejecutivo
    </h2>
    <p style='color: rgba(255, 255, 255, 0.75); font-size: 1.1rem;'>
        Métricas en tiempo real del sistema
    </p>
</div>
""", unsafe_allow_html=True)

# Obtener métricas (optimizado con cache)
metrics = get_system_metrics()

# Mostrar métricas en grid
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{metrics['automatizaciones_ejecutadas']}</div>
        <div class="metric-label">Automatizaciones Ejecutadas</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{metrics['tiempo_ahorrado']}</div>
        <div class="metric-label">Tiempo Ahorrado</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{metrics['eficiencia_incrementada']}</div>
        <div class="metric-label">Eficiencia Incrementada</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{metrics['usuarios_activos']}</div>
        <div class="metric-label">Usuarios Activos</div>
    </div>
    """, unsafe_allow_html=True)

# FILTROS INTERACTIVOS
st.markdown("""
<div class="filters-container">
    <div style='text-align: center; margin-bottom: 1.5rem;'>
        <h3 style='color: rgba(255, 255, 255, 0.95); font-size: 1.5rem; font-weight: 700;'>
            Filtros y Configuración
        </h3>
    </div>
""", unsafe_allow_html=True)

# Filtros en columnas
filter_col1, filter_col2, filter_col3 = st.columns(3)
with filter_col1:
    departamento = st.selectbox(
        "Filtrar por Departamento",
        ["Todos", "Cuentas Médicas", "Cartera", "Tesorería", "Métricas"]
    )
with filter_col2:
    estado = st.selectbox(
        "Filtrar por Estado",
        ["Todos", "Activo", "En desarrollo", "Pendiente"]
    )
with filter_col3:
    fecha_inicio = st.date_input("Fecha de inicio")

st.markdown("</div>", unsafe_allow_html=True)

# SECCIÓN DE AYUDA Y SOPORTE
st.markdown("""
<div style='text-align: center; margin: 3rem 0;'>
    <h2 style='color: rgba(255, 255, 255, 0.95); font-size: 2rem; font-weight: 800; margin-bottom: 1.5rem;'>
        ¿Necesitas Ayuda?
    </h2>
</div>
""", unsafe_allow_html=True)

help_col1, help_col2, help_col3 = st.columns(3)
with help_col1:
    if st.button("📚 Documentación", use_container_width=True):
        st.session_state.show_docs = True
with help_col2:
    if st.button("🎥 Video Tutoriales", use_container_width=True):
        st.session_state.show_tutorials = True
with help_col3:
    if st.button("🆘 Soporte Técnico", use_container_width=True):
        st.session_state.show_support = True

# Mostrar contenido según selección
if st.session_state.get('show_docs'):
    with st.expander("📚 Documentación Técnica", expanded=True):
        st.markdown("""
        ### Guías de uso por módulo:
        
        **Cuentas Médicas**
        - Conversor JSON: Sube archivos .json para convertirlos a formato estándar
        - Renombrador RIPS: Automatiza el renombrado masivo de archivos
        - Procesador OCR: Convierte imágenes y PDFs a texto editable
        
        **Cartera**
        - Generador de reportes: Crea reportes financieros automáticamente
        - Análisis predictivo: Visualiza tendencias y proyecciones
        """)

if st.session_state.get('show_tutorials'):
    with st.expander("🎥 Video Tutoriales", expanded=True):
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # URL de ejemplo

if st.session_state.get('show_support'):
    with st.expander("🆘 Soporte Técnico", expanded=True):
        st.text_input("Tu email")
        st.text_area("Describe el problema")
        if st.button("Enviar solicitud"):
            st.success("✅ Solicitud enviada. Te contactaremos en 24 horas.")

# FOOTER MEJORADO
st.markdown("""
<div style='
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 3rem;
    margin-top: 5rem;
    text-align: center;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
'>
    <h4 style='color: rgba(255, 255, 255, 0.95); margin-bottom: 1.2rem; font-size: 1.4rem; font-weight: 700;'>
        TodoDrogas - Plataforma Inteligente
    </h4>
    <p style='color: rgba(255, 255, 255, 0.75); margin-bottom: 0.8rem; font-size: 1rem;'>
        Tecnología que impulsa tu operación al siguiente nivel • v3.0
    </p>
    <p style='color: rgba(255, 255, 255, 0.6); font-size: 0.9rem;'>
        Última actualización: """ + datetime.now().strftime("%d/%m/%Y %H:%M") + """ • © 2024 Todos los derechos reservados
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
