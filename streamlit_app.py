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

# CSS para efectos 3D
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin: 1rem 0 3rem 0;
        color: white;
        text-align: center;
    }
    
    .area-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid #f0f0f0;
        transition: all 0.3s ease;
        border-top: 4px solid;
    }
    
    .area-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    
    .icon-container {
        width: 70px;
        height: 70px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1.5rem;
        font-size: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION CON COMPONENTES NATIVOS
st.markdown("""
<div class="main-header">
    <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 0.5rem;">
        SISTEMA DE AUTOMATIZACIÓN
    </h1>
</div>
""", unsafe_allow_html=True)

# TEXTO PRINCIPAL CON COMPONENTES NATIVOS
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Transformando procesos mediante tecnología inteligente")
    st.markdown("""
    El futuro es la tecnología, y hoy se convierte en nuestra mejor herramienta.
    
    Centralizamos automatizaciones por área para optimizar procesos y mejorar la eficiencia operativa.
    """)
    
    # Botones con componentes nativos
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("🚀 Explorar Automatizaciones", use_container_width=True):
            st.switch_page("pages/1_Cuentas_Medicas.py")
    with col_btn2:
        if st.button("👀 Ver Demo", use_container_width=True, type="secondary"):
            st.info("🔍 Función de demo en desarrollo...")

with col2:
    # Tarjeta de beneficios con componentes nativos
    with st.container():
        st.markdown("### 🚀 Beneficios Clave")
        st.markdown("✓ **Reducción de tiempos** - Procesos más rápidos")
        st.markdown("✓ **Mayor precisión** - Eliminación de errores")
        st.markdown("✓ **Reportes automáticos** - Información en tiempo real")
        st.markdown("✓ **Integración total** - Sistemas conectados")

# SEPARADOR
st.markdown("---")

# SECCIÓN PRINCIPAL DE ÁREAS - MÁS PROTAGONISMO
st.markdown("## 🎯 Áreas de Automatización")
st.markdown("Selecciona un área para acceder a sus herramientas especializadas")

# DATOS DE LAS ÁREAS CON MÁS DETALLE
areas_data = [
    {
        "name": "Cuentas Médicas",
        "icon": "📋",
        "color": "#0066cc",
        "description": "Automatización de procesos médicos y administrativos",
        "automations": [
            "🔄 Procesadores JSON - SAVIA & COOSALUD",
            "🏷️ Renombradores RIPS & CUV", 
            "🔍 Procesador OCR + Renombrado - SALUD TOTAL"
        ],
        "page": "Cuentas_Medicas"
    },
    {
        "name": "Cartera",
        "icon": "💰",
        "color": "#00a86b",
        "description": "Gestión automatizada de estados financieros y reportes",
        "automations": [
            "📊 Procesador Estados de Cuenta",
            "📈 Generador de Reportes - Business Intelligence"
        ],
        "page": "Cartera"
    },
    {
        "name": "Tesorería",
        "icon": "🏦",
        "color": "#ff6b35", 
        "description": "Control automatizado del flujo financiero",
        "automations": [
            "🔄 Conciliador Automático - Bancos & Sistemas",
            "📋 Gestor de Estados Bancarios"
        ],
        "page": "Tesoreria"
    },
    {
        "name": "Métricas y Contacto",
        "icon": "📊",
        "color": "#8a2be2",
        "description": "Seguimiento y análisis de resultados",
        "automations": [
            "📈 Dashboard de Métricas - Análisis de Impacto",
            "💡 Centro de Soporte - Soporte Integral"
        ],
        "page": "Metricas_y_Contacto"
    }
]

# CREAR TARJETAS DE ÁREAS CON MÁS PROTAGONISMO
for area in areas_data:
    # Usar columnas para dar más ancho a cada área
    col1, col2 = st.columns([1, 4])
    
    with col1:
        # Icono grande y prominente
        st.markdown(
            f"""<div class="icon-container" style="background: linear-gradient(135deg, {area['color']}, {area['color']}dd); color: white; justify-content: center;">
                {area['icon']}
            </div>""", 
            unsafe_allow_html=True
        )
    
    with col2:
        # Contenido de la área
        with st.container():
            st.markdown(f"### {area['name']}")
            st.markdown(f"**{area['description']}**")
            
            # Mostrar automatizaciones
            for automation in area['automations']:
                st.markdown(f"• {automation}")
            
            # Botón de acceso
            if st.button(
                f"🚀 Acceder a {area['name']}", 
                key=f"btn_{area['page']}",
                use_container_width=True
            ):
                st.switch_page(f"pages/{area['page']}.py")
    
    st.markdown("---")

# SECCIÓN ADICIONAL DE ESTADÍSTICAS
st.markdown("## 📊 Impacto de las Automatizaciones")

# Métricas en grid
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Reducción de Tiempos",
        value="85%",
        delta="+5% vs mes anterior"
    )

with col2:
    st.metric(
        label="Precisión", 
        value="99.2%",
        delta="+0.8%"
    )

with col3:
    st.metric(
        label="Procesos Automatizados",
        value="24",
        delta="+3 nuevos"
    )

with col4:
    st.metric(
        label="Disponibilidad",
        value="24/7",
        delta="Siempre activo"
    )

# CALL TO ACTION FINAL
st.markdown("---")
st.markdown("## 🚀 ¿Listo para transformar tus procesos?")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button(
        "🎯 Comenzar con Cuentas Médicas", 
        use_container_width=True,
        type="primary"
    ):
        st.switch_page("pages/1_Cuentas_Medicas.py")
    
    if st.button(
        "💼 Solicitar Demo Personalizado", 
        use_container_width=True,
        type="secondary"
    ):
        st.info("📞 Nos contactaremos contigo pronto para coordinar el demo")

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
