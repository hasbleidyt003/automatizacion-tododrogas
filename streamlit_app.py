import streamlit as st
from components.navbar import futurist_navbar
from config.theme import configure_futurist_theme

# Configurar tema futurista
configure_futurist_theme()

# Configurar página
st.set_page_config(
    page_title="Sistema de Automatización - TodoDrogas",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Navbar futurista
futurist_navbar()

# TÍTULO Y DESCRIPCIÓN CON ESTILO FUTURISTA
st.markdown("""
<div style='text-align: center; margin: 3rem 0 4rem 0;'>
    <div style='
        background: linear-gradient(135deg, #00f5ff, #8a2be2, #ff00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: hologram 4s ease-in-out infinite;
    '>
        <h1 style='font-size: 4.5rem; font-weight: 900; margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 4px; font-family: "Arial Black", sans-serif;'>
        🤖 SISTEMA DE AUTOMATIZACIÓN
        </h1>
    </div>
    
    <div style='
        background: linear-gradient(90deg, #00f5ff, #8a2be2, #ff00ff, #00f5ff);
        background-size: 300% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: shimmer 4s linear infinite;
    '>
        <p style='font-size: 1.5rem; line-height: 1.8; max-width: 1100px; margin: 0 auto; font-weight: 300; font-family: "Segoe UI", sans-serif;'>
        ⚡ El futuro es la tecnología, y hoy se convierte en nuestra mejor herramienta.<br>
        🌟 Este sistema centraliza todas las automatizaciones desarrolladas por área<br>
        🚀 Permitiendo optimizar procesos, reducir tiempos y mejorar la eficiencia operativa.
        </p>
    </div>
</div>

<style>
@keyframes shimmer {
    0% { background-position: 0% center; }
    100% { background-position: 300% center; }
}

@keyframes hologram {
    0%, 100% { 
        filter: hue-rotate(0deg) drop-shadow(0 0 20px #00f5ff);
        transform: translateY(0px);
    }
    50% { 
        filter: hue-rotate(180deg) drop-shadow(0 0 30px #ff00ff);
        transform: translateY(-5px);
    }
}

@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    33% { transform: translateY(-15px) rotate(1deg); }
    66% { transform: translateY(-8px) rotate(-1deg); }
}

@keyframes matrix {
    0% { background-position: 0% 0%; }
    100% { background-position: 100% 100%; }
}

.futurist-card {
    background: 
        linear-gradient(135deg, rgba(0, 245, 255, 0.1), rgba(138, 43, 226, 0.1)),
        url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect fill="none" stroke="rgba(0,245,255,0.05)" stroke-width="0.5" x="0" y="0" width="100" height="100"/></svg>');
    backdrop-filter: blur(20px);
    border: 1px solid rgba(0, 245, 255, 0.3);
    border-radius: 25px;
    padding: 3rem;
    margin: 3rem 0;
    position: relative;
    overflow: hidden;
    box-shadow: 
        0 0 50px rgba(0, 245, 255, 0.2),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.futurist-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    transition: left 0.7s;
}

.futurist-card:hover::before {
    left: 100%;
}

.futurist-card::after {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: conic-gradient(from 0deg, transparent, rgba(0, 245, 255, 0.1), transparent);
    animation: rotate 10s linear infinite;
    z-index: -1;
}

@keyframes rotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.glass-effect {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 20px;
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.neon-text {
    text-shadow: 
        0 0 10px currentColor,
        0 0 20px currentColor,
        0 0 40px currentColor;
}

.pulse-glow {
    animation: pulse-glow 2s ease-in-out infinite;
}

@keyframes pulse-glow {
    0%, 100% { 
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.5);
        transform: scale(1);
    }
    50% { 
        box-shadow: 0 0 40px rgba(255, 0, 255, 0.8);
        transform: scale(1.05);
    }
}

.hologram-button {
    background: linear-gradient(45deg, #00f5ff, #8a2be2, #ff00ff);
    background-size: 200% auto;
    border: none;
    border-radius: 30px;
    color: white;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 2px;
    padding: 1.2rem 2.5rem;
    cursor: pointer;
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
    animation: button-shimmer 3s linear infinite;
}

.hologram-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
    transition: left 0.5s;
}

.hologram-button:hover::before {
    left: 100%;
}

.hologram-button:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 
        0 10px 40px rgba(0, 245, 255, 0.6),
        0 0 60px rgba(255, 0, 255, 0.4);
}

@keyframes button-shimmer {
    0% { background-position: 0% center; }
    100% { background-position: 200% center; }
}

.matrix-bg {
    background-image: 
        radial-gradient(circle at 20% 80%, rgba(0, 245, 255, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(138, 43, 226, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(255, 0, 255, 0.05) 0%, transparent 50%);
    background-size: 200% 200%;
    animation: matrix 20s linear infinite;
}
</style>
""", unsafe_allow_html=True)

# --- CUENTAS MÉDICAS - FUTURISTA ---
st.markdown("""
<div class='futurist-card' style='animation: float 8s ease-in-out infinite;'>
    <div style='
        background: linear-gradient(135deg, #00f5ff, #8a2be2, #ff00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 3rem;
    '>
        <h2 style='font-size: 3rem; font-weight: 900; display: flex; align-items: center; gap: 1.5rem; justify-content: center;'>
        <span style='animation: pulse-glow 3s infinite; font-size: 3rem;'>🔮</span> 
        CUENTAS MÉDICAS
        <span style='animation: pulse-glow 3s infinite 1.5s; font-size: 3rem;'>⚡</span>
        </h2>
    </div>
    
    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 3rem;'>
        <!-- SAVIA Y COOSALUD -->
        <div class='glass-effect' style='padding: 2.5rem; animation: pulse-glow 4s ease-in-out infinite;'>
            <h4 style='color: #00f5ff; margin-bottom: 2rem; font-size: 1.5rem; text-align: center;' class='neon-text'>
            🌐 SAVIA & COOSALUD
            </h4>
            <div style='color: #e0e0e0; line-height: 2; font-size: 1.2rem;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;'>
                    <span style='color: #00f5ff; font-size: 1.5rem;'>🌀</span>
                    <div>
                        <strong>CONVERSORES MANTIS/SISPRO</strong><br>
                        <span style='color: #b0b0b0; font-size: 1rem;'>Transformación cuántica de formatos</span>
                    </div>
                </div>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;'>
                    <span style='color: #00f5ff; font-size: 1.5rem;'>🎯</span>
                    <div>
                        <strong>RENOMBRADORES CUV/RIPS</strong><br>
                        <span style='color: #b0b0b0; font-size: 1rem;'>Estandarización algorítmica avanzada</span>
                    </div>
                </div>
                <div style='display: flex; align-items: center; gap: 1rem;'>
                    <span style='color: #00f5ff; font-size: 1.5rem;'>👁️</span>
                    <div>
                        <strong>PROCESADOR OCR DE ACTAS</strong><br>
                        <span style='color: #b0b0b0; font-size: 1rem;'>Visión artificial para digitalización</span>
                    </div>
                </div>
            </div>
            <button class='hologram-button' style='width: 100%; margin-top: 2.5rem; font-size: 1.1rem;'
            onclick="window.location.href='/pages/1_Cuentas_Medicas'">
            🚀 ACTIVAR SISTEMA
            </button>
        </div>
        
        <!-- SALUD TOTAL -->
        <div class='glass-effect' style='padding: 2.5rem; animation: pulse-glow 4s ease-in-out infinite 2s;'>
            <h4 style='color: #ff00ff; margin-bottom: 2rem; font-size: 1.5rem; text-align: center;' class='neon-text'>
            🌌 SALUD TOTAL
            </h4>
            <div style='color: #e0e0e0; line-height: 2; font-size: 1.2rem;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;'>
                    <span style='color: #ff00ff; font-size: 1.5rem;'>👁️</span>
                    <div>
                        <strong>PROCESADOR OCR DE ACTAS</strong><br>
                        <span style='color: #b0b0b0; font-size: 1rem;'>Visión artificial para digitalización</span>
                    </div>
                </div>
                <div style='display: flex; align-items: center; gap: 1rem;'>
                    <span style='color: #ff00ff; font-size: 1.5rem;'>📁</span>
                    <div>
                        <strong>RENOMBRADOR DE ARCHIVOS</strong><br>
                        <span style='color: #b0b0b0; font-size: 1rem;'>Organización neuronal de datos</span>
                    </div>
                </div>
            </div>
            <button class='hologram-button' style='width: 100%; margin-top: 2.5rem; font-size: 1.1rem; background: linear-gradient(45deg, #ff00ff, #8a2be2, #00f5ff);'
            onclick="window.location.href='/pages/1_Cuentas_Medicas'">
            🌠 INICIAR AUTOMATIZACIÓN
            </button>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- CARTERA - FUTURISTA ---
st.markdown("""
<div class='futurist-card' style='animation: float 8s ease-in-out infinite 1s;'>
    <div style='
        background: linear-gradient(135deg, #00ff88, #00ccff, #0099ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 3rem;
    '>
        <h2 style='font-size: 3rem; font-weight: 900; display: flex; align-items: center; gap: 1.5rem; justify-content: center;'>
        <span style='animation: pulse-glow 3s infinite; font-size: 3rem;'>💎</span> 
        CARTERA INTELIGENTE
        <span style='animation: pulse-glow 3s infinite 1s; font-size: 3rem;'>📊</span>
        </h2>
    </div>
    
    <div class='glass-effect' style='padding: 3rem; animation: pulse-glow 4s ease-in-out infinite 0.5s;'>
        <div style='display: flex; align-items: center; gap: 3rem;'>
            <div style='flex: 1;'>
                <h4 style='color: #00ff88; margin-bottom: 2rem; font-size: 1.6rem;' class='neon-text'>
                🚀 SISTEMA AUTOMATIZADO
                </h4>
                <div style='color: #e0e0e0; line-height: 1.8; font-size: 1.3rem;'>
                    <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem;'>
                        <span style='color: #00ff88; font-size: 2rem;'>🤖</span>
                        <div>
                            <strong style='color: #00ff88;'>ESTADOS DE CUENTA AUTOMATIZADOS</strong><br>
                            <span style='color: #b0b0b0; font-size: 1.1rem;'>Generación y distribución inteligente con IA</span>
                        </div>
                    </div>
                </div>
                <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 2rem;'>
                    <div style='text-align: center;'>
                        <div style='color: #00ff88; font-size: 2rem;'>⚡</div>
                        <div style='color: #e0e0e0; font-size: 0.9rem;'>Tiempo Real</div>
                    </div>
                    <div style='text-align: center;'>
                        <div style='color: #00ccff; font-size: 2rem;'>🔒</div>
                        <div style='color: #e0e0e0; font-size: 0.9rem;'>Seguro</div>
                    </div>
                    <div style='text-align: center;'>
                        <div style='color: #0099ff; font-size: 2rem;'>📈</div>
                        <div style='color: #e0e0e0; font-size: 0.9rem;'>Analítico</div>
                    </div>
                    <div style='text-align: center;'>
                        <div style='color: #00ff88; font-size: 2rem;'>🚀</div>
                        <div style='color: #e0e0e0; font-size: 0.9rem;'>Rápido</div>
                    </div>
                </div>
            </div>
            <div style='flex-shrink: 0;'>
                <div style='
                    background: linear-gradient(45deg, #00ff88, #00ccff, #0099ff);
                    padding: 2rem;
                    border-radius: 50%;
                    width: 150px;
                    height: 150px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    animation: pulse-glow 3s infinite;
                    box-shadow: 0 0 50px rgba(0, 255, 136, 0.5);
                '>
                    <span style='font-size: 4rem;'>💳</span>
                </div>
            </div>
        </div>
        <button class='hologram-button' style='
            background: linear-gradient(45deg, #00ff88, #00ccff, #0099ff);
            padding: 1.5rem 4rem;
            font-size: 1.3rem;
            display: block;
            margin: 3rem auto 0 auto;
        '
        onclick="window.location.href='/pages/2_Cartera'">
        🌟 INICIAR SISTEMA CARTERA
        </button>
    </div>
</div>
""", unsafe_allow_html=True)

# Continuaré con los demás archivos en la siguiente respuesta...
