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

# HERO SECTION - CORREGIDA Y MEJORADA
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div style='padding: 0.5rem 0 2rem 0; margin-top: -0.8cm;'>
        <h1 style='
            color: #1a1a1a;
            font-size: 3.8rem;
            font-weight: 800;
            margin-bottom: 0;
            line-height: 1;
            font-family: "Inter", sans-serif;
            letter-spacing: -0.5px;
        '>
        SISTEMA DE AUTOMATIZACIÓN
        </h1>
        
        <h2 style='
            color: #0066cc;
            font-size: 2rem;
            font-weight: 400;
            margin-top: 0.3rem;
            margin-bottom: 1.5rem;
            line-height: 1.2;
            font-family: "Inter", sans-serif;
        '>
        Sistema de Automatización
        </h2>
        
        <div style='
            color: #666666;
            font-size: 1.2rem;
            line-height: 1.6;
            margin-bottom: 2rem;
        '>
            <p>El futuro es la tecnología, y hoy se convierte en nuestra mejor herramienta.</p>
            <p>Centralizamos automatizaciones por área para optimizar procesos y mejorar la eficiencia operativa.</p>
        </div>
        
        <div style='
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
        '>
            <button style='
                background: #0066cc;
                color: white;
                border: none;
                padding: 0.8rem 1.8rem;
                border-radius: 8px;
                font-weight: 600;
                font-size: 1rem;
                cursor: pointer;
                transition: background 0.3s ease;
            '>
                Explorar Automatizaciones
            </button>
            
            <button style='
                background: transparent;
                color: #0066cc;
                border: 2px solid #0066cc;
                padding: 0.8rem 1.8rem;
                border-radius: 8px;
                font-weight: 600;
                font-size: 1rem;
                cursor: pointer;
                transition: all 0.3s ease;
            '>
                Ver Demo
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #0066cc, #004499);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        box-shadow: 0 6px 20px rgba(0,102,204,0.15);
        margin-top: 1rem;
    '>
        <div style='font-size: 2.5rem; margin-bottom: 1rem;'>🚀</div>
        <h3 style='margin-bottom: 1rem; font-size: 1.2rem;'>Beneficios Clave</h3>
        <div style='text-align: left; line-height: 1.6;'>
            <div style='display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.8rem;'>
                <span style='font-size: 1.2rem;'>✓</span> <span>Reducción de tiempos</span>
            </div>
            <div style='display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.8rem;'>
                <span style='font-size: 1.2rem;'>✓</span> <span>Mayor precisión</span>
            </div>
            <div style='display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.8rem;'>
                <span style='font-size: 1.2rem;'>✓</span> <span>Reportes automáticos</span>
            </div>
            <div style='display: flex; align-items: center; gap: 0.5rem;'>
                <span style='font-size: 1.2rem;'>✓</span> <span>Integración total</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# SEPARADOR
st.markdown("<div style='height: 2px; background: #f0f0f0; margin: 3rem 0;'></div>", unsafe_allow_html=True)

# SECCIÓN DE AUTOMATIZACIONES
st.markdown("""
<div style='text-align: center; margin-bottom: 2rem;'>
    <h2 style='
        color: #1a1a1a;
        font-size: 2.2rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
    '>
    Áreas de Automatización
    </h2>
    <p style='color: #666666; font-size: 1.1rem;'>
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
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
        height: 300px;
        display: flex;
        flex-direction: column;
    '>
        <div style='
            background: linear-gradient(135deg, #0066cc, #004499);
            width: 50px;
            height: 50px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.2rem;
        '>
            <span style='color: white; font-size: 1.3rem;'>📋</span>
        </div>
        
        <h3 style='
            color: #1a1a1a;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 0.8rem;
        '>
        Cuentas Médicas
        </h3>
        
        <div style='
            color: #666666;
            line-height: 1.4;
            margin-bottom: 1.5rem;
            flex-grow: 1;
            font-size: 0.85rem;
        '>
            <p><strong>SAVIA & COOSALUD:</strong></p>
            <p>• Conversores MANTIS/SISPRO</p>
            <p>• Renombradores CUV/RIPS</p>
            <p>• Procesador OCR</p>
            
            <p style='margin-top: 0.8rem;'><strong>SALUD TOTAL:</strong></p>
            <p>• Procesador OCR</p>
            <p>• Renombrador archivos</p>
        </div>
        
        <button style='
            background: #0066cc;
            color: white;
            border: none;
            padding: 0.6rem 1.2rem;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
            font-size: 0.9rem;
        '>
        Acceder
        </button>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
        height: 300px;
        display: flex;
        flex-direction: column;
    '>
        <div style='
            background: linear-gradient(135deg, #00a86b, #007a4d);
            width: 50px;
            height: 50px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.2rem;
        '>
            <span style='color: white; font-size: 1.3rem;'>💰</span>
        </div>
        
        <h3 style='
            color: #1a1a1a;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 0.8rem;
        '>
        Cartera
        </h3>
        
        <div style='
            color: #666666;
            line-height: 1.4;
            margin-bottom: 1.5rem;
            flex-grow: 1;
            font-size: 0.9rem;
        '>
            <p>Gestión automatizada de estados de cuenta y reportes financieros.</p>
            
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 0.4rem; margin-top: 0.8rem;'>
                <div style='text-align: center; padding: 0.4rem; background: #f8f9fa; border-radius: 5px;'>
                    <div style='color: #00a86b; font-size: 1rem;'>⚡</div>
                    <div style='color: #666; font-size: 0.7rem;'>Rápido</div>
                </div>
                <div style='text-align: center; padding: 0.4rem; background: #f8f9fa; border-radius: 5px;'>
                    <div style='color: #00a86b; font-size: 1rem;'>📊</div>
                    <div style='color: #666; font-size: 0.7rem;'>Preciso</div>
                </div>
            </div>
        </div>
        
        <button style='
            background: #00a86b;
            color: white;
            border: none;
            padding: 0.6rem 1.2rem;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
            font-size: 0.9rem;
        '>
        Acceder
        </button>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
        height: 300px;
        display: flex;
        flex-direction: column;
    '>
        <div style='
            background: linear-gradient(135deg, #ff6b35, #cc552b);
            width: 50px;
            height: 50px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.2rem;
        '>
            <span style='color: white; font-size: 1.3rem;'>🏦</span>
        </div>
        
        <h3 style='
            color: #1a1a1a;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 0.8rem;
        '>
        Tesorería
        </h3>
        
        <div style='
            color: #666666;
            line-height: 1.4;
            margin-bottom: 1.5rem;
            flex-grow: 1;
            font-size: 0.9rem;
        '>
            <p>Control automatizado de estados de cuenta y flujo financiero.</p>
            
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 0.4rem; margin-top: 0.8rem;'>
                <div style='text-align: center; padding: 0.4rem; background: #f8f9fa; border-radius: 5px;'>
                    <div style='color: #ff6b35; font-size: 1rem;'>🔒</div>
                    <div style='color: #666; font-size: 0.7rem;'>Seguro</div>
                </div>
                <div style='text-align: center; padding: 0.4rem; background: #f8f9fa; border-radius: 5px;'>
                    <div style='color: #ff6b35; font-size: 1rem;'>📈</div>
                    <div style='color: #666; font-size: 0.7rem;'>Analítico</div>
                </div>
            </div>
        </div>
        
        <button style='
            background: #ff6b35;
            color: white;
            border: none;
            padding: 0.6rem 1.2rem;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
            font-size: 0.9rem;
        '>
        Acceder
        </button>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style='
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
        height: 300px;
        display: flex;
        flex-direction: column;
    '>
        <div style='
            background: linear-gradient(135deg, #8a2be2, #6a1cb3);
            width: 50px;
            height: 50px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.2rem;
        '>
            <span style='color: white; font-size: 1.3rem;'>📊</span>
        </div>
        
        <h3 style='
            color: #1a1a1a;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 0.8rem;
        '>
        Métricas
        </h3>
        
        <div style='
            color: #666666;
            line-height: 1.4;
            margin-bottom: 1.5rem;
            flex-grow: 1;
            font-size: 0.9rem;
        '>
            <p>Dashboard de resultados y análisis de impacto de las automatizaciones.</p>
            
            <div style='background: #f8f9fa; padding: 0.8rem; border-radius: 6px; margin-top: 0.8rem;'>
                <p style='font-size: 0.8rem; color: #8a2be2; font-weight: 600; margin: 0;'>¿Nueva automatización?</p>
                <p style='font-size: 0.7rem; color: #666; margin: 0.2rem 0 0 0;'>Contáctanos</p>
            </div>
        </div>
        
        <button style='
            background: #8a2be2;
            color: white;
            border: none;
            padding: 0.6rem 1.2rem;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
            font-size: 0.9rem;
        '>
        Acceder
        </button>
    </div>
    """, unsafe_allow_html=True)

# FOOTER MODERNO
st.markdown("""
<div style='
    background: #f8f9fa;
    padding: 2rem 0;
    margin-top: 3rem;
    text-align: center;
    border-top: 1px solid #e0e0e0;
'>
    <h4 style='color: #1a1a1a; margin-bottom: 0.8rem; font-size: 1.1rem;'>Tododrogas - Sistema de Automatización</h4>
    <p style='color: #666666; margin-bottom: 0.4rem; font-size: 0.9rem;'>Optimizando procesos mediante tecnología</p>
    <p style='color: #999999; font-size: 0.8rem;'>© 2024 Todos los derechos reservados</p>
</div>
""", unsafe_allow_html=True) 
