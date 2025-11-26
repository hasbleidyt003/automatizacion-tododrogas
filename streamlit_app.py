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

# CSS con efectos solo en elementos interactivos
st.markdown("""
<style>
    /* Base mejorada - FONDO ORIGINAL */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 0;
    }
    
    /* Hero section con efecto cristal sutil */
    .hero-glass {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 24px;
        padding: 3rem 2rem;
        margin: 1rem 0 3rem 0;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 
            0 10px 30px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.8);
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        line-height: 1.1;
        font-family: "Inter", sans-serif;
        background: linear-gradient(135deg, #0066cc 0%, #00a8ff 50%, #004499 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        color: #666;
        font-size: 1.3rem;
        font-weight: 400;
        margin-bottom: 2rem;
        line-height: 1.4;
        font-family: "Inter", sans-serif;
    }
    
    /* Métricas interactivas con efectos al hover */
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.2rem;
        margin: 2rem 0;
    }
    
    .metric-card {
        background: white;
        border: 1px solid rgba(0, 102, 204, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #0066cc, #00a8ff);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 102, 204, 0.15);
        border-color: rgba(0, 102, 204, 0.3);
    }
    
    .metric-card:hover::before {
        height: 5px;
        background: linear-gradient(90deg, #00a8ff, #0066cc, #004499);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #0066cc;
        margin-bottom: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover .metric-value {
        color: #00a8ff;
        transform: scale(1.05);
    }
    
    .metric-label {
        font-size: 0.95rem;
        color: #666;
        font-weight: 500;
    }
    
    /* Tarjetas con efectos al hover */
    .card-glass {
        background: white;
        border: 1px solid rgba(0, 102, 204, 0.1);
        border-radius: 20px;
        padding: 2rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
        height: 100%;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }
    
    .card-glass::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #0066cc, #00a8ff);
        border-radius: 20px 20px 0 0;
        transition: all 0.3s ease;
    }
    
    .card-glass:hover::before {
        background: linear-gradient(90deg, #00a8ff, #0066cc, #004499);
        height: 6px;
    }
    
    .card-glass:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 
            0 25px 50px rgba(0, 102, 204, 0.15),
            0 10px 30px rgba(0, 0, 0, 0.1);
        border-color: rgba(0, 102, 204, 0.3);
    }
    
    .card-icon-glass {
        width: 70px;
        height: 70px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #0066cc, #004499);
        font-size: 1.8rem;
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(0, 102, 204, 0.3);
    }
    
    .card-glass:hover .card-icon-glass {
        transform: scale(1.1) rotate(5deg);
        box-shadow: 0 12px 35px rgba(0, 102, 204, 0.4);
        background: linear-gradient(135deg, #00a8ff, #0066cc);
    }
    
    .card-title-glass {
        color: #1a1a1a;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1rem;
        line-height: 1.3;
        transition: all 0.3s ease;
    }
    
    .card-glass:hover .card-title-glass {
        color: #0066cc;
    }
    
    .card-description-glass {
        color: #666;
        line-height: 1.6;
        margin-bottom: 2rem;
        font-size: 0.95rem;
        flex-grow: 1;
    }
    
    /* Botones con efectos futuristas al hover */
    .btn-glass {
        background: transparent;
        color: #0066cc;
        border: 2px solid #0066cc;
        padding: 0.8rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.9rem;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        position: relative;
        overflow: hidden;
    }
    
    .btn-glass::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 102, 204, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .btn-glass:hover::before {
        left: 100%;
    }
    
    .btn-glass:hover {
        background: #0066cc;
        color: white;
        transform: translateY(-2px);
        box-shadow: 
            0 8px 25px rgba(0, 102, 204, 0.3),
            0 0 20px rgba(0, 102, 204, 0.2);
        border-color: #0066cc;
    }
    
    .btn-glass:active {
        transform: translateY(0);
        box-shadow: 
            0 4px 15px rgba(0, 102, 204, 0.3),
            inset 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Filtros interactivos */
    .filters-container {
        background: white;
        border: 1px solid rgba(0, 102, 204, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 2rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
    }
    
    .filters-container:hover {
        box-shadow: 0 8px 25px rgba(0, 102, 204, 0.15);
        border-color: rgba(0, 102, 204, 0.2);
    }
    
    /* Efectos de neón para elementos al hover */
    .neon-glow:hover {
        box-shadow: 
            0 0 20px rgba(0, 102, 204, 0.3),
            0 0 40px rgba(0, 102, 204, 0.2),
            0 0 60px rgba(0, 102, 204, 0.1);
    }
    
    /* Animaciones mejoradas solo para hover */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .card-glass:hover {
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    .btn-glass:hover {
        animation: pulse 2s ease-in-out infinite;
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION MEJORADA
st.markdown("""
<div class="hero-glass">
    <h1 class="hero-title">Plataforma Inteligente Tododrogas</h1>
    <p class="hero-subtitle">Tecnología que impulsa tu operación al siguiente nivel</p>
</div>
""", unsafe_allow_html=True)

# SECCIÓN DE AUTOMATIZACIONES MEJORADA - CON BOTONES FUNCIONALES
st.markdown("""
<div style='text-align: center; margin: 3rem 0 2rem 0;'>
    <h2 style='color: #1a1a1a; font-size: 2.2rem; font-weight: 800; margin-bottom: 0.8rem;'>
        Áreas de Automatización
    </h2>
    <p style='color: #666; font-size: 1.1rem;'>
        Selecciona un área para acceder a herramientas especializadas
    </p>
</div>
""", unsafe_allow_html=True)

# ÁREAS CON BOTONES STREAMLIT NATIVOS - ESTO SÍ FUNCIONA
areas_data = [
    {
        "name": "Cuentas Médicas",
        "icon": "📋",
        "description": "SAVIA & COOSALUD: Conversores JSON, Renombradores RIPS/CUV. SALUD TOTAL: Procesador OCR + Renombrado",
        "status": "Activo",
        "users": "8 usuarios",
        "page": "pages/1_Cuentas_Medicas.py"  # ✅ RUTA CORRECTA
    },
    {
        "name": "Cartera", 
        "icon": "💰",
        "description": "Gestión automatizada de estados de cuenta y reportes financieros con análisis inteligente y predicciones",
        "status": "Activo", 
        "users": "6 usuarios",
        "page": "pages/2_Cartera.py"  # ✅ RUTA CORRECTA
    },
    {
        "name": "Tesorería",
        "icon": "🏦", 
        "description": "Control automatizado de estados bancarios, flujo financiero y conciliaciones con máxima seguridad",
        "status": "En desarrollo",
        "users": "4 usuarios", 
        "page": "pages/3_Tesoreria.py"  # ✅ RUTA CORRECTA
    },
    {
        "name": "Métricas",
        "icon": "📊",
        "description": "Dashboard ejecutivo con análisis de impacto, ROI y métricas de todas las automatizaciones implementadas", 
        "status": "Activo",
        "users": "5 usuarios",
        "page": "pages/Metricas_y_Contacto.py"  # ✅ RUTA CORRECTA
    }
]

# CREAR GRID CON BOTONES QUE SÍ FUNCIONAN
cols = st.columns(2)
for i, area in enumerate(areas_data):
    with cols[i % 2]:
        status_color = "#00a86b" if area["status"] == "Activo" else "#ff6b35"
        
        # Tarjeta con diseño (solo visual)
        st.markdown(f"""
        <div class="card-glass">
            <div class="card-icon-glass">{area['icon']}</div>
            <h3 class="card-title-glass">{area['name']}</h3>
            <div style='display: flex; justify-content: space-between; margin-bottom: 1rem;'>
                <span style='background: {status_color}; color: white; padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600;'>
                    {area['status']}
                </span>
                <span style='color: #666; font-size: 0.8rem; font-weight: 500;'>
                    {area['users']}
                </span>
            </div>
            <p class="card-description-glass">{area['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # ✅ BOTÓN STREAMLIT NATIVO - ESTE SÍ FUNCIONA
        if st.button(f"Acceder al Módulo - {area['name']}", 
                    key=f"area_btn_{i}", 
                    use_container_width=True):
            st.switch_page(area["page"])

# SEPARADOR VISUAL MEJORADO
st.markdown("<div style='height: 2px; background: linear-gradient(90deg, transparent, #0066cc, transparent); margin: 4rem 0;'></div>", unsafe_allow_html=True)

# MÉTRICAS INTERACTIVAS EN TIEMPO REAL
st.markdown("""
<div style='text-align: center; margin-bottom: 1rem;'>
    <h2 style='color: #1a1a1a; font-size: 1.8rem; font-weight: 700; margin-bottom: 0.5rem;'>
        Dashboard Ejecutivo
    </h2>
    <p style='color: #666; font-size: 1rem;'>
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
    <div style='text-align: center; margin-bottom: 1rem;'>
        <h3 style='color: #1a1a1a; font-size: 1.3rem; font-weight: 600;'>
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
<div style='text-align: center; margin: 2rem 0;'>
    <h2 style='color: #1a1a1a; font-size: 1.8rem; font-weight: 700; margin-bottom: 1rem;'>
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
    background: white;
    border: 1px solid rgba(0, 102, 204, 0.1);
    border-radius: 16px;
    padding: 2rem;
    margin-top: 4rem;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
'>
    <h4 style='color: #1a1a1a; margin-bottom: 1rem; font-size: 1.2rem; font-weight: 600;'>
        TodoDrogas - Plataforma Inteligente
    </h4>
    <p style='color: #666; margin-bottom: 0.5rem; font-size: 0.9rem;'>
        Tecnología que impulsa tu operación al siguiente nivel • v3.0
    </p>
    <p style='color: #999; font-size: 0.8rem;'>
        Última actualización: """ + datetime.now().strftime("%d/%m/%Y %H:%M") + """ • © 2024 Todos los derechos reservados
    </p>
</div>
""", unsafe_allow_html=True)
