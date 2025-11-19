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
    
    /* Efectos 3D mejorados para las tarjetas (MANTENIDO IGUAL) */
    .card-3d {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 
            0 10px 30px rgba(0,0,0,0.1),
            0 1px 8px rgba(0,0,0,0.05),
            inset 0 1px 0 rgba(255,255,255,0.8);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid rgba(255,255,255,0.3);
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
            0 20px 50px rgba(0,0,0,0.15),
            0 5px 15px rgba(0,0,0,0.1),
            inset 0 1px 0 rgba(255,255,255,0.9);
    }
    
    /* Iconos con efecto 3D - Solo azules */
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
            0 8px 20px rgba(0, 102, 204, 0.3),
            inset 0 1px 0 rgba(255,255,255,0.3);
        position: relative;
        transition: all 0.3s ease;
    }
    
    .card-3d:hover .icon-3d {
        transform: scale(1.1) rotate(5deg);
        box-shadow: 
            0 12px 30px rgba(0, 102, 204, 0.4),
            inset 0 1px 0 rgba(255,255,255,0.4);
    }
    
    /* Botones con efecto 3D - Solo azules */
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
            0 6px 20px rgba(0, 102, 204, 0.3),
            0 2px 4px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
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
    
    /* BENEFICIOS CON SOMBRA 3D (MANTENIDO IGUAL) */
    .benefits-3d {
        background: white;
        border-radius: 16px;
        padding: 2.5rem;
        box-shadow: 
            0 12px 35px rgba(0,0,0,0.1),
            0 3px 10px rgba(0,0,0,0.06),
            inset 0 1px 0 rgba(255,255,255,0.8);
        border: 1px solid rgba(255,255,255,0.4);
        position: relative;
        margin: 2rem 0;
        transition: all 0.3s ease;
    }
    
    .benefits-3d:hover {
        box-shadow: 
            0 15px 45px rgba(0,0,0,0.15),
            0 5px 15px rgba(0,0,0,0.1),
            inset 0 1px 0 rgba(255,255,255,0.9);
    }
    
    .benefits-3d::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #0066cc, #0088ff, #004499);
        border-radius: 16px 16px 0 0;
    }
    
    .benefit-item {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        padding: 1rem 0;
        border-bottom: 1px solid rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    
    .benefit-item:hover {
        background: rgba(0,0,0,0.02);
        border-radius: 8px;
        padding: 1rem;
        margin: 0 -0.5rem;
    }
    
    .benefit-item:last-child {
        border-bottom: none;
    }
    
    .benefit-icon {
        font-size: 1.2rem;
        min-width: 30px;
        text-align: center;
        background: linear-gradient(135deg, #0066cc, #004499);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .benefit-content h4 {
        color: #1a1a1a;
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
        font-family: "Inter", sans-serif;
    }
    
    .benefit-content p {
        color: #666;
        font-size: 0.85rem;
        line-height: 1.4;
        margin: 0;
        font-family: "Inter", sans-serif;
    }
    
    /* Footer con sombra 3D sutil (MANTENIDO IGUAL) */
    .footer-3d {
        background: white;
        padding: 2rem 0;
        margin-top: 3rem;
        text-align: center;
        border-radius: 16px 16px 0 0;
        box-shadow: 
            0 -5px 25px rgba(0,0,0,0.08),
            0 -2px 10px rgba(0,0,0,0.04);
        border-top: 1px solid rgba(0,0,0,0.05);
        position: relative;
    }
    
    .footer-3d::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #0066cc, #0088ff, #004499);
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION MINIMALISTA (PARTE QUE TE GUSTA)
st.markdown("""
<div class="hero-minimal">
    <h1 class="hero-title">Sistema de Automatización</h1>
    <p class="hero-subtitle">Optimizando procesos mediante tecnología inteligente y eficiente</p>
</div>
""", unsafe_allow_html=True)

# SECCIÓN DE AUTOMATIZACIONES (MANTENIDO IGUAL)
st.markdown("""
<div style='text-align: center; margin-bottom: 2rem;'>
    <h2 style='
        color: #1a1a1a;
        font-size: 2rem;
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

# GRID DE TARJETAS 3D (MANTENIDO EXACTAMENTE IGUAL)
col1, col2, col3, col4 = st.columns(4)

# Datos de las áreas para reutilización - Solo azules
areas_data = [
    {
        "name": "Cuentas Médicas",
        "icon": "📋",
        "description": "SAVIA & COOSALUD: Conversores JSON, Renombradores RIPS/CUV<br>SALUD TOTAL: Procesador OCR + Renombrado",
        "button_text": "Acceder"
    },
    {
        "name": "Cartera",
        "icon": "💰",
        "description": "Gestión automatizada de estados de cuenta y reportes financieros con análisis inteligente",
        "button_text": "Acceder"
    },
    {
        "name": "Tesorería",
        "icon": "🏦", 
        "description": "Control automatizado de estados bancarios y flujo financiero con máxima seguridad",
        "button_text": "Acceder"
    },
    {
        "name": "Métricas",
        "icon": "📊",
        "description": "Dashboard de resultados y análisis de impacto de todas las automatizaciones implementadas",
        "button_text": "Acceder"
    }
]

# Renderizar tarjetas 3D (MANTENIDO IGUAL)
columns = [col1, col2, col3, col4]
for i, (col, area) in enumerate(zip(columns, areas_data)):
    with col:
        st.markdown(f"""
        <div class="card-3d" style="height: 320px; display: flex; flex-direction: column;">
            <div class="icon-3d">
                <span style='color: white; font-size: 1.5rem;'>{area['icon']}</span>
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
            
            <button class="btn-3d" style="width: 100%;" onclick="navigateTo('{area['name'].lower().replace(' ', '_').replace('métricas', 'metricas')}')">
                {area['button_text']}
            </button>
        </div>
        """, unsafe_allow_html=True)

# SEPARADOR ANTES DE BENEFICIOS (MANTENIDO IGUAL)
st.markdown("<div style='height: 1px; background: linear-gradient(90deg, transparent, #e0e0e0, transparent); margin: 3rem 0;'></div>", unsafe_allow_html=True)

# BENEFICIOS CLAVE - CON SOMBRA 3D (MANTENIDO IGUAL)
st.markdown("""
<div class="benefits-3d">
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h3 style='
            color: #1a1a1a;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            font-family: "Inter", sans-serif;
        '>
        Beneficios Clave
        </h3>
        <p style='color: #666666; font-size: 0.95rem; font-family: "Inter", sans-serif;'>
        Ventajas competitivas de nuestras soluciones de automatización
        </p>
    </div>
    
    <div style='max-width: 800px; margin: 0 auto;'>
        <div class="benefit-item">
            <div class="benefit-icon">⚡</div>
            <div class="benefit-content">
                <h4>Reducción de Tiempos</h4>
                <p>Procesa en minutos lo que antes tomaba horas de trabajo manual repetitivo</p>
            </div>
        </div>
        
        <div class="benefit-item">
            <div class="benefit-icon">🎯</div>
            <div class="benefit-content">
                <h4>Mayor Precisión</h4>
                <p>Elimina errores humanos con procesos automatizados y validados</p>
            </div>
        </div>
        
        <div class="benefit-item">
            <div class="benefit-icon">📊</div>
            <div class="benefit-content">
                <h4>Reportes Automáticos</h4>
                <p>Genera reportes en tiempo real sin intervención manual continua</p>
            </div>
        </div>
        
        <div class="benefit-item">
            <div class="benefit-icon">🔗</div>
            <div class="benefit-content">
                <h4>Integración Total</h4>
                <p>Conecta todos tus sistemas y procesos en una sola plataforma unificada</p>
            </div>
        </div>
        
        <div class="benefit-item">
            <div class="benefit-icon">🛡️</div>
            <div class="benefit-content">
                <h4>Seguridad Avanzada</h4>
                <p>Protección de datos con encriptación y controles de acceso granular</p>
            </div>
        </div>
        
        <div class="benefit-item">
            <div class="benefit-icon">📈</div>
            <div class="benefit-content">
                <h4>Escalabilidad</h4>
                <p>Adapta el sistema a tu crecimiento sin necesidad de reinversiones</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# FOOTER CON SOMBRA 3D (MANTENIDO IGUAL)
st.markdown("""
<div class="footer-3d">
    <h4 style='color: #1a1a1a; margin-bottom: 0.8rem; font-size: 1.1rem; font-weight: 600; font-family: "Inter", sans-serif;'>TodoDrogas - Sistema de Automatización</h4>
    <p style='color: #666666; margin-bottom: 0.4rem; font-size: 0.9rem; font-family: "Inter", sans-serif;'>Optimizando procesos mediante tecnología avanzada</p>
    <p style='color: #999999; font-size: 0.8rem; font-family: "Inter", sans-serif;'>© 2024 Todos los derechos reservados</p>
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
