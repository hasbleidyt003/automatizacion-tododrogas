# streamlit_app.py
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

# HERO SECTION - Misma estructura exacta
col1, col2 = st.columns([2, 1])

with col1:
    # Título principal
    st.markdown("# SISTEMA DE AUTOMATIZACIÓN")
    
    # Subtítulo
    st.markdown("### Transformando procesos mediante tecnología inteligente")
    
    # Descripción
    st.write("El futuro es la tecnología, y hoy se convierte en nuestra mejor herramienta.")
    st.write("Centralizamos automatizaciones por área para optimizar procesos y mejorar la eficiencia operativa.")
    
    # Grid de características
    col1_1, col1_2, col1_3, col1_4 = st.columns(4)
    with col1_1:
        st.metric("12+", "Automatizaciones")
    with col1_2:
        st.metric("99.8%", "Eficiencia")
    with col1_3:
        st.metric("24/7", "Operación")
    with col1_4:
        st.metric("3", "Áreas Activas")

with col2:
    # Tarjeta de beneficios
    with st.container():
        st.markdown("#### Beneficios Clave")
        
        # Beneficios en lista
        st.write("✓ Reducción de tiempos")
        st.write("✓ Mayor precisión") 
        st.write("✓ Reportes automáticos")
        st.write("✓ Integración total")

# SEPARADOR
st.markdown("---")

# SECCIÓN DE ÁREAS - Misma estructura exacta
st.markdown("## Áreas de Automatización")
st.write("Selecciona un área para acceder a sus herramientas especializadas")

# GRID DE TARJETAS - Misma estructura de 4 columnas
col1, col2, col3, col4 = st.columns(4)

# Datos de las áreas (mismo contenido)
areas_data = [
    {
        "name": "Cuentas Médicas",
        "icon": "📋",
        "description": "SAVIA & COOSALUD: Conversores JSON, Renombradores RIPS/CUV\nSALUD TOTAL: Procesador OCR + Renombrado",
        "button_text": "Acceder",
        "status": "🟢 ACTIVO"
    },
    {
        "name": "Cartera",
        "icon": "💰", 
        "description": "Gestión automatizada de estados de cuenta y reportes financieros con análisis inteligente",
        "button_text": "Acceder",
        "status": "🟢 ACTIVO"
    },
    {
        "name": "Tesorería",
        "icon": "🏦",
        "description": "Control automatizado de estados bancarios y flujo financiero con máxima seguridad", 
        "button_text": "Acceder",
        "status": "🟢 ACTIVO"
    },
    {
        "name": "Métricas",
        "icon": "📊",
        "description": "Dashboard de resultados y análisis de impacto de todas las automatizaciones implementadas",
        "button_text": "Acceder", 
        "status": "🟡 DESARROLLO"
    }
]

# Renderizar tarjetas en las mismas posiciones
columns = [col1, col2, col3, col4]
for i, (col, area) in enumerate(zip(columns, areas_data)):
    with col:
        with st.container():
            # Header con icono y estado
            icon_col, status_col = st.columns([1, 1])
            with icon_col:
                st.write(f"### {area['icon']}")
            with status_col:
                st.write(area['status'])
            
            # Título
            st.write(f"**{area['name']}**")
            
            # Descripción
            st.write(area['description'])
            
            # Botón
            if st.button(area['button_text'], key=f"btn_{i}"):
                # Navegación a las páginas según tu estructura
                if area['name'] == "Cuentas Médicas":
                    st.switch_page("pages/1_Cuentas_Medicas.py")
                elif area['name'] == "Cartera":
                    st.switch_page("pages/2_Cartera.py") 
                elif area['name'] == "Tesorería":
                    st.switch_page("pages/3_Tesoreria.py")
                elif area['name'] == "Métricas":
                    st.switch_page("pages/4_Metricas.py")

# FOOTER - Misma estructura exacta  
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns([1, 1, 1])

with footer_col1:
    st.write("**TodoDrogas - Sistema de Automatización**")

with footer_col2:
    st.write("Optimizando procesos mediante tecnología avanzada")

with footer_col3:
    st.write("© 2024 Todos los derechos reservados")
