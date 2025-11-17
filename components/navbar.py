import streamlit as st

def modern_navbar():
    st.markdown("""
    <style>
    .modern-navbar {
        background: white;
        padding: 1.2rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 20px rgba(0,0,0,0.08);
        border-bottom: 1px solid #f0f0f0;
    }
    
    .nav-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .nav-title {
        color: #1a1a1a;
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    .nav-title span {
        color: #0066cc;
    }
    
    .nav-links {
        display: flex;
        gap: 0.3rem;
        background: #f8f9fa;
        border-radius: 12px;
        padding: 0.4rem;
        border: 1px solid #e0e0e0;
    }
    
    .nav-link {
        color: #666666;
        text-decoration: none;
        padding: 0.7rem 1.5rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        font-weight: 500;
        font-size: 0.9rem;
    }
    
    .nav-link:hover {
        background: white;
        color: #0066cc;
        box-shadow: 0 2px 12px rgba(0,102,204,0.15);
    }
    
    .nav-link.active {
        background: #0066cc;
        color: white;
    }
    </style>

    <div class="modern-navbar">
        <div class="nav-content">
            <div class="nav-title">Todo<span>drogas</span></div>
            <div class="nav-links">
                <a href="/" class="nav-link">Inicio</a>
                <a href="/Cuentas_Medicas" class="nav-link">Cuentas Médicas</a>
                <a href="/Cartera" class="nav-link">Cartera</a>
                <a href="/Tesoreria" class="nav-link">Tesorería</a>
                <a href="/Metricas_y_Contacto" class="nav-link">Métricas</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
