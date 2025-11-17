import streamlit as st

def minimalist_navbar():
    st.markdown("""
    <style>
    .minimalist-navbar {
        background: white;
        border-bottom: 3px solid #0066cc;
        padding: 1.5rem 3rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .nav-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .nav-title {
        color: #0066cc;
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: 1px;
    }
    
    .nav-links {
        display: flex;
        gap: 1rem;
    }
    
    .nav-link {
        color: #333;
        text-decoration: none;
        padding: 0.7rem 1.2rem;
        border-radius: 6px;
        transition: all 0.3s ease;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    .nav-link:hover {
        background: #0066cc;
        color: white;
    }
    
    .nav-link.active {
        background: #0066cc;
        color: white;
    }
    </style>

    <div class="minimalist-navbar">
        <div class="nav-content">
            <div class="nav-title">TODO DROGAS</div>
            <div class="nav-links">
                <a href="/" class="nav-link active">INICIO</a>
                <a href="/pages/1_Cuentas_Medicas" class="nav-link">CUENTAS MÉDICAS</a>
                <a href="/pages/2_Cartera" class="nav-link">CARTERA</a>
                <a href="/pages/3_Tesoreria" class="nav-link">TESORERÍA</a>
                <a href="/pages/4_Metricas_y_Contacto" class="nav-link">MÉTRICAS</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
