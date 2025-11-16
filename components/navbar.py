import streamlit as st

def futurist_navbar():
    st.markdown("""
    <style>
    .futurist-navbar {
        background: rgba(10, 10, 30, 0.8);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(0, 245, 255, 0.3);
        padding: 1.2rem 3rem;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 30px rgba(0, 245, 255, 0.2);
    }
    
    .futurist-navbar::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 245, 255, 0.1), transparent);
        animation: slide 4s linear infinite;
    }
    
    @keyframes slide {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .nav-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1400px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
    }
    
    .nav-title {
        background: linear-gradient(135deg, #00f5ff, #8a2be2, #ff00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1.6rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-family: 'Arial Black', sans-serif;
        text-shadow: 0 0 20px rgba(0, 245, 255, 0.5);
    }
    
    .nav-links {
        display: flex;
        gap: 0.5rem;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        padding: 0.5rem;
    }
    
    .nav-link {
        color: #e0e0e0;
        text-decoration: none;
        padding: 0.8rem 1.5rem;
        border-radius: 20px;
        transition: all 0.3s ease;
        font-weight: 600;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }
    
    .nav-link::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 245, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .nav-link:hover::before {
        left: 100%;
    }
    
    .nav-link:hover {
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.2), rgba(138, 43, 226, 0.2));
        color: #00f5ff;
        box-shadow: 0 0 15px rgba(0, 245, 255, 0.3);
        transform: translateY(-2px);
    }
    
    .nav-link.active {
        background: linear-gradient(135deg, #00f5ff, #8a2be2);
        color: white;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.5);
    }
    </style>

    <div class="futurist-navbar">
        <div class="nav-content">
            <div class="nav-title">🚀 SISTEMA DE AUTOMATIZACIÓN</div>
            <div class="nav-links">
                <a href="/" class="nav-link active">🏠 INICIO</a>
                <a href="/pages/1_Cuentas_Medicas" class="nav-link">🔮 CUENTAS</a>
                <a href="/pages/2_Cartera" class="nav-link">💎 CARTERA</a>
                <a href="/pages/3_Tesoreria" class="nav-link">🏦 TESORERÍA</a>
                <a href="/pages/4_Metricas_y_Contacto" class="nav-link">📊 MÉTRICAS</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
