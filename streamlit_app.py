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

# HERO SECTION MODERNA
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div style='padding: 3rem 0;'>
        <h1 style='
            color: #1a1a1a;
            font-size: 3.2rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            line-height: 1.2;
            font-family: "Inter", sans-serif;
        '>
        Sistema de<br>Automatización
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Texto descriptivo
    st.markdown("""
    <div style='
        color: #666666;
        font-size: 1.3rem;
        line-height: 1.6;
        margin-bottom: 2.5rem;
    '>
        <p>El futuro es la tecnología, y hoy se convierte en nuestra mejor herramienta.</p>
        <p>Centralizamos automatizaciones por área para optimizar procesos y mejorar la eficiencia operativa.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Botones con componentes nativos de Streamlit
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        if st.button(
            "🚀 **Explorar Automatizaciones**", 
            use_container_width=True,
            type="primary"
        ):
            st.switch_page("pages/1_Cuentas_Medicas.py")
    
    with col_btn2:
        if st.button(
            "👀 **Ver Demo**", 
            use_container_width=True,
            type="secondary"
        ):
            st.info("🔍 Función de demo en desarrollo...")

with col2:
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #0066cc, #004499);
        padding: 2.5rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,102,204,0.15);
        margin-top: 2rem;
    '>
        <div style='font-size: 3rem; margin-bottom: 1rem;'>🚀</div>
        <h3 style='margin-bottom: 1rem; font-size: 1.3rem;'>Beneficios Clave</h3>
        <div style='text-align: left; line-height: 1.8;'>
            <div style='display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.8rem;'>
                <span>✓</span> <span>Reducción de tiempos</span>
            </div>
            <div style='display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.8rem;'>
                <span>✓</span> <span>Mayor precisión</span>
            </div>
            <div style='display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.8rem;'>
                <span>✓</span> <span>Reportes automáticos</span>
            </div>
            <div style='display: flex; align-items: center; gap: 0.5rem;'>
                <span>✓</span> <span>Integración total</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# SEPARADOR
st.markdown("<div style='height: 2px; background: #f0f0f0; margin: 4rem 0;'></div>", unsafe_allow_html=True)

# SECCIÓN DE AUTOMATIZACIONES
st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h2 style='
        color: #1a1a1a;
        font-size: 2.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    '>
    Áreas de Automatización
    </h2>
    <p style='color: #666666; font-size: 1.2rem;'>
    Selecciona un área para acceder a sus herramientas
    </p>
</div>
""", unsafe_allow_html=True)

# GRID DE TARJETAS MODERNO
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style='
        background: white;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
        height: 320px;
        display: flex;
        flex-direction: column;
    '>
        <div style='
            background: linear-gradient(135deg, #0066cc, #004499);
            width: 60px;
            height: 60px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
        '>
            <span style='color: white; font-size: 1.5rem;'>📋</span>
        </div>
        
        <h3 style='
            color: #1a1a1a;
            font-size: 1.4rem;
            font-weight: 600;
            margin-bottom: 1rem;
        '>
        Cuentas Médicas
        </h3>
        
        <div style='
            color: #666666;
            line-height: 1.5;
            margin-bottom: 2rem;
            flex-grow: 1;
        '>
            <p><strong>SAVIA & COOSALUD:</strong></p>
            <p style='font-size: 0.9rem;'>• Conversores MANTIS/SISPRO</p>
            <p style='font-size: 0.9rem;'>• Renombradores CUV/RIPS</p>
            <p style='font-size: 0.9rem;'>• Procesador OCR</p>
            
            <p style='margin-top: 1rem;'><strong>SALUD TOTAL:</strong></p>
            <p style='font-size: 0.9rem;'>• Procesador OCR</p>
            <p style='font-size: 0.9rem;'>• Renombrador archivos</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acceder a Cuentas Médicas", key="btn_cuentas", use_container_width=True):
        st.switch_page("pages/1_Cuentas_Medicas.py")

with col2:
    st.markdown("""
    <div style='
        background: white;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
        height: 320px;
        display: flex;
        flex-direction: column;
    '>
        <div style='
            background: linear-gradient(135deg, #00a86b, #007a4d);
            width: 60px;
            height: 60px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
        '>
            <span style='color: white; font-size: 1.5rem;'>💰</span>
        </div>
        
        <h3 style='
            color: #1a1a1a;
            font-size: 1.4rem;
            font-weight: 600;
            margin-bottom: 1rem;
        '>
        Cartera
        </h3>
        
        <div style='
            color: #666666;
            line-height: 1.5;
            margin-bottom: 2rem;
            flex-grow: 1;
        '>
            <p style='font-size: 0.95rem; margin-bottom: 1rem;'>
            Gestión automatizada de estados de cuenta y reportes financieros.
            </p>
            
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;'>
                <div style='text-align: center; padding: 0.5rem; background: #f8f9fa; border-radius: 6px;'>
                    <div style='color: #00a86b; font-size: 1.2rem;'>⚡</div>
                    <div style='color: #666; font-size: 0.8rem;'>Rápido</div>
                </div>
                <div style='text-align: center; padding: 0.5rem; background: #f8f9fa; border-radius: 6px;'>
                    <div style='color: #00a86b; font-size: 1.2rem;'>📊</div>
                    <div style='color: #666; font-size: 0.8rem;'>Preciso</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acceder a Cartera", key="btn_cartera", use_container_width=True):
        st.switch_page("pages/2_Cartera.py")

with col3:
    st.markdown("""
    <div style='
        background: white;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
        height: 320px;
        display: flex;
        flex-direction: column;
    '>
        <div style='
            background: linear-gradient(135deg, #ff6b35, #cc552b);
            width: 60px;
            height: 60px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
        '>
            <span style='color: white; font-size: 1.5rem;'>🏦</span>
        </div>
        
        <h3 style='
            color: #1a1a1a;
            font-size: 1.4rem;
            font-weight: 600;
            margin-bottom: 1rem;
        '>
        Tesorería
        </h3>
        
        <div style='
            color: #666666;
            line-height: 1.5;
            margin-bottom: 2rem;
            flex-grow: 1;
        '>
            <p style='font-size: 0.95rem; margin-bottom: 1rem;'>
            Control automatizado de estados de cuenta y flujo financiero.
            </p>
            
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;'>
                <div style='text-align: center; padding: 0.5rem; background: #f8f9fa; border-radius: 6px;'>
                    <div style='color: #ff6b35; font-size: 1.2rem;'>🔒</div>
                    <div style='color: #666; font-size: 0.8rem;'>Seguro</div>
                </div>
                <div style='text-align: center; padding: 0.5rem; background: #f8f9fa; border-radius: 6px;'>
                    <div style='color: #ff6b35; font-size: 1.2rem;'>📈</div>
                    <div style='color: #666; font-size: 0.8rem;'>Analítico</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acceder a Tesorería", key="btn_tesoreria", use_container_width=True):
        st.switch_page("pages/3_Tesoreria.py")

with col4:
    st.markdown("""
    <div style='
        background: white;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
        height: 320px;
        display: flex;
        flex-direction: column;
    '>
        <div style='
            background: linear-gradient(135deg, #8a2be2, #6a1cb3);
            width: 60px;
            height: 60px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
        '>
            <span style='color: white; font-size: 1.5rem;'>📊</span>
        </div>
        
        <h3 style='
            color: #1a1a1a;
            font-size: 1.4rem;
            font-weight: 600;
            margin-bottom: 1rem;
        '>
        Métricas
        </h3>
        
        <div style='
            color: #666666;
            line-height: 1.5;
            margin-bottom: 2rem;
            flex-grow: 1;
        '>
            <p style='font-size: 0.95rem; margin-bottom: 1rem;'>
            Dashboard de resultados y análisis de impacto de las automatizaciones.
            </p>
            
            <div style='background: #f8f9fa; padding: 1rem; border-radius: 8px;'>
                <p style='font-size: 0.9rem; color: #8a2be2; font-weight: 600; margin: 0;'>¿Nueva automatización?</p>
                <p style='font-size: 0.8rem; color: #666; margin: 0.3rem 0 0 0;'>Contáctanos</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acceder a Métricas", key="btn_metricas", use_container_width=True):
        st.switch_page("pages/4_Metricas_y_Contacto.py")

# FOOTER MODERNO
st.markdown("""
<div style='
    background: #f8f9fa;
    padding: 3rem 0;
    margin-top: 4rem;
    text-align: center;
    border-top: 1px solid #e0e0e0;
'>
    <h4 style='color: #1a1a1a; margin-bottom: 1rem;'>Tododrogas - Sistema de Automatización</h4>
    <p style='color: #666666; margin-bottom: 0.5rem;'>Optimizando procesos mediante tecnología</p>
    <p style='color: #999999; font-size: 0.9rem;'>© Todos los derechos reservados</p>
</div>
""", unsafe_allow_html=True)
