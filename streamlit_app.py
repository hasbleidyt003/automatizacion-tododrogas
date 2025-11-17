import streamlit as st
from components.navbar import minimalist_navbar
from config.theme import configure_minimalist_theme

# Configurar tema minimalista
configure_minimalist_theme()

# Configurar página
st.set_page_config(
    page_title="Sistema de Automatización - TodoDrogas",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Navbar minimalista
minimalist_navbar()

# TÍTULO Y DESCRIPCIÓN MINIMALISTA
st.markdown("""
<div style='text-align: center; margin: 3rem 0 4rem 0;'>
    <h1 style='
        color: #0066cc;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
        letter-spacing: 2px;
        font-family: "Arial", sans-serif;
    '>
    SISTEMA DE AUTOMATIZACIÓN
    </h1>
    
    <div style='
        color: #333333;
        border-left: 4px solid #0066cc;
        padding-left: 2rem;
        margin: 0 auto;
        max-width: 900px;
        text-align: left;
    '>
        <p style='font-size: 1.3rem; line-height: 1.8; margin-bottom: 1.5rem;'>
        El futuro es la tecnología, y hoy se convierte en nuestra mejor herramienta.
        </p>
        <p style='font-size: 1.3rem; line-height: 1.8; margin-bottom: 1.5rem;'>
        Este sistema centraliza todas las automatizaciones desarrolladas por área con el fin garantizar un uso más eficiente y enfocado.
        </p>
        <p style='font-size: 1.3rem; line-height: 1.8;'>
        Permitiendo optimizar procesos, reducir tiempos y mejorar la eficiencia operativa.
        </p>
    </div>
</div>

<style>
.minimalist-card {
    background: white;
    border: 2px solid #e0e0e0;
    border-radius: 12px;
    padding: 2.5rem;
    margin: 2rem 0;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.minimalist-card:hover {
    border-color: #0066cc;
    box-shadow: 0 6px 20px rgba(0,102,204,0.15);
    transform: translateY(-2px);
}

.section-header {
    color: #0066cc;
    font-size: 2rem;
    font-weight: 600;
    margin-bottom: 2rem;
    text-align: center;
    border-bottom: 2px solid #0066cc;
    padding-bottom: 1rem;
}

.client-section {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 2rem;
    margin: 1.5rem 0;
    border-left: 4px solid #0066cc;
}

.feature-item {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    margin-bottom: 1.5rem;
    padding: 1rem;
    background: white;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
}

.feature-icon {
    color: #0066cc;
    font-size: 1.5rem;
    min-width: 40px;
}

.feature-content h4 {
    color: #0066cc;
    margin: 0 0 0.5rem 0;
    font-size: 1.2rem;
}

.feature-content p {
    color: #666;
    margin: 0;
    line-height: 1.5;
}

.minimalist-button {
    background: #0066cc;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 1rem 2rem;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    width: 100%;
    text-align: center;
}

.minimalist-button:hover {
    background: #0052a3;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0,102,204,0.3);
}
</style>
""", unsafe_allow_html=True)

# --- CUENTAS MÉDICAS - MINIMALISTA ---
st.markdown("""
<div class='minimalist-card'>
    <div class='section-header'>
        CUENTAS MÉDICAS
    </div>
    
    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;'>
        <!-- SAVIA Y COOSALUD -->
        <div class='client-section'>
            <h3 style='color: #0066cc; text-align: center; margin-bottom: 1.5rem; font-size: 1.4rem;'>
            SAVIA & COOSALUD
            </h3>
            
            <div class='feature-item'>
                <div class='feature-icon'>🔄</div>
                <div class='feature-content'>
                    <h4>Conversores MANTIS/SISPRO</h4>
                    <p>Transformación automática de formatos de datos entre sistemas</p>
                </div>
            </div>
            
            <div class='feature-item'>
                <div class='feature-icon'>📁</div>
                <div class='feature-content'>
                    <h4>Renombradores CUV/RIPS</h4>
                    <p>Estandarización automatizada de archivos según protocolos</p>
                </div>
            </div>
            
            <div class='feature-item'>
                <div class='feature-icon'>👁️</div>
                <div class='feature-content'>
                    <h4>Procesador de Actas (OCR)</h4>
                    <p>Digitalización inteligente de documentos mediante reconocimiento óptico</p>
                </div>
            </div>
            
            <button class='minimalist-button' onclick="window.location.href='/pages/1_Cuentas_Medicas'">
                Acceder al Sistema
            </button>
        </div>
        
        <!-- SALUD TOTAL -->
        <div class='client-section'>
            <h3 style='color: #0066cc; text-align: center; margin-bottom: 1.5rem; font-size: 1.4rem;'>
            SALUD TOTAL
            </h3>
            
            <div class='feature-item'>
                <div class='feature-icon'>👁️</div>
                <div class='feature-content'>
                    <h4>Procesador de Actas (OCR)</h4>
                    <p>Digitalización inteligente de documentos mediante reconocimiento óptico</p>
                </div>
            </div>
            
            <div class='feature-item'>
                <div class='feature-icon'>📂</div>
                <div class='feature-content'>
                    <h4>Renombrador de Archivos</h4>
                    <p>Organización automatizada de archivos y documentos</p>
                </div>
            </div>
            
            <button class='minimalist-button' onclick="window.location.href='/pages/1_Cuentas_Medicas'">
                Iniciar Automatización
            </button>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- CARTERA - MINIMALISTA ---
st.markdown("""
<div class='minimalist-card'>
    <div class='section-header'>
        CARTERA
    </div>
    
    <div style='display: flex; align-items: center; gap: 3rem;'>
        <div style='flex: 1;'>
            <h3 style='color: #0066cc; margin-bottom: 1.5rem; font-size: 1.5rem;'>
            Sistema Automatizado de Estados de Cuenta
            </h3>
            
            <div class='feature-item'>
                <div class='feature-icon'>📊</div>
                <div class='feature-content'>
                    <h4>Estados de Cuenta Automatizados</h4>
                    <p>Generación y distribución automática de estados financieros para gestión eficiente de cartera</p>
                </div>
            </div>
            
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 2rem;'>
                <div style='text-align: center; padding: 1rem; background: #f8f9fa; border-radius: 8px;'>
                    <div style='color: #0066cc; font-size: 1.5rem;'>⚡</div>
                    <div style='color: #333; font-weight: 600;'>Tiempo Real</div>
                </div>
                <div style='text-align: center; padding: 1rem; background: #f8f9fa; border-radius: 8px;'>
                    <div style='color: #0066cc; font-size: 1.5rem;'>🔒</div>
                    <div style='color: #333; font-weight: 600;'>Seguro</div>
                </div>
                <div style='text-align: center; padding: 1rem; background: #f8f9fa; border-radius: 8px;'>
                    <div style='color: #0066cc; font-size: 1.5rem;'>📈</div>
                    <div style='color: #333; font-weight: 600;'>Analítico</div>
                </div>
                <div style='text-align: center; padding: 1rem; background: #f8f9fa; border-radius: 8px;'>
                    <div style='color: #0066cc; font-size: 1.5rem;'>🚀</div>
                    <div style='color: #333; font-weight: 600;'>Eficiente</div>
                </div>
            </div>
        </div>
        
        <div style='flex-shrink: 0; text-align: center;'>
            <div style='
                background: #0066cc;
                color: white;
                padding: 2rem;
                border-radius: 50%;
                width: 120px;
                height: 120px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto;
            '>
                <span style='font-size: 2.5rem;'>💳</span>
            </div>
        </div>
    </div>
    
    <button class='minimalist-button' style='margin-top: 2rem;' onclick="window.location.href='/pages/2_Cartera'">
        Iniciar Sistema de Cartera
    </button>
</div>
""", unsafe_allow_html=True)

# --- TESORERÍA - MINIMALISTA ---
st.markdown("""
<div class='minimalist-card'>
    <div class='section-header'>
        TESORERÍA
    </div>
    
    <div style='display: flex; align-items: center; gap: 3rem;'>
        <div style='flex: 1;'>
            <h3 style='color: #0066cc; margin-bottom: 1.5rem; font-size: 1.5rem;'>
            Control Financiero Automatizado
            </h3>
            
            <div class='feature-item'>
                <div class='feature-icon'>🏦</div>
                <div class='feature-content'>
                    <h4>Estados de Cuenta Automatizados</h4>
                    <p>Control y seguimiento financiero automatizado para gestión de tesorería</p>
                </div>
            </div>
            
            <div style='background: #f8f9fa; padding: 1.5rem; border-radius: 8px; margin-top: 1.5rem;'>
                <h4 style='color: #0066cc; margin-bottom: 1rem;'>Beneficios</h4>
                <ul style='color: #333; line-height: 1.8;'>
                    <li>• Reportes financieros en tiempo real</li>
                    <li>• Conciliación automática con bancos</li>
                    <li>• Control de flujo de caja automatizado</li>
                    <li>• Alertas y notificaciones inteligentes</li>
                </ul>
            </div>
        </div>
        
        <div style='flex-shrink: 0; text-align: center;'>
            <div style='
                background: #0066cc;
                color: white;
                padding: 2rem;
                border-radius: 50%;
                width: 120px;
                height: 120px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto;
            '>
                <span style='font-size: 2.5rem;'>💰</span>
            </div>
        </div>
    </div>
    
    <button class='minimalist-button' style='margin-top: 2rem;' onclick="window.location.href='/pages/3_Tesoreria'">
        Activar Sistema de Tesorería
    </button>
</div>
""", unsafe_allow_html=True)

# --- MÉTRICAS Y CONTACTO - MINIMALISTA ---
st.markdown("""
<div class='minimalist-card'>
    <div class='section-header'>
        MÉTRICAS Y CONTACTO
    </div>
    
    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;'>
        <!-- MÉTRICAS -->
        <div class='client-section'>
            <h3 style='color: #0066cc; text-align: center; margin-bottom: 1.5rem; font-size: 1.4rem;'>
            MÉTRICAS Y RESULTADOS
            </h3>
            
            <p style='color: #333; line-height: 1.6; margin-bottom: 2rem; text-align: center;'>
            Visualización del impacto y resultados obtenidos con las automatizaciones implementadas. 
            Monitorea el rendimiento y eficiencia de cada proceso.
            </p>
            
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 2rem;'>
                <div style='text-align: center; padding: 1rem; background: white; border-radius: 8px; border: 1px solid #e0e0e0;'>
                    <div style='color: #0066cc; font-size: 1.2rem; font-weight: 700;'>12</div>
                    <div style='color: #666; font-size: 0.9rem;'>Procesos Automatizados</div>
                </div>
                <div style='text-align: center; padding: 1rem; background: white; border-radius: 8px; border: 1px solid #e0e0e0;'>
                    <div style='color: #0066cc; font-size: 1.2rem; font-weight: 700;'>45h</div>
                    <div style='color: #666; font-size: 0.9rem;'>Horas Ahorradas</div>
                </div>
            </div>
            
            <button class='minimalist-button' onclick="window.location.href='/pages/4_Metricas_y_Contacto'">
                Ver Métricas Detalladas
            </button>
        </div>
        
        <!-- CONTACTO -->
        <div class='client-section'>
            <h3 style='color: #0066cc; text-align: center; margin-bottom: 1.5rem; font-size: 1.4rem;'>
            CONTACTO
            </h3>
            
            <p style='color: #333; line-height: 1.6; margin-bottom: 2rem; text-align: center;'>
            ¿Requieres una nueva automatización o tienes alguna sugerencia? 
            Contáctanos para desarrollar soluciones personalizadas.
            </p>
            
            <div style='background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid #e0e0e0; margin-bottom: 2rem;'>
                <div style='color: #0066cc; font-weight: 600; margin-bottom: 0.5rem;'>📧 Email</div>
                <div style='color: #333;'>soporte@tododrogas.com</div>
                
                <div style='color: #0066cc; font-weight: 600; margin: 1rem 0 0.5rem 0;'>📞 Teléfono</div>
                <div style='color: #333;'>+57 300 123 4567</div>
            </div>
            
            <button class='minimalist-button' onclick="window.location.href='/pages/4_Metricas_y_Contacto'">
                Contactar al Equipo
            </button>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# JavaScript para navegación
st.markdown("""
<script>
function navigateTo(url) {
    window.location.href = url;
}
</script>
""", unsafe_allow_html=True)
