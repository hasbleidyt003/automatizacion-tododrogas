import streamlit as st

def minimalist_navbar():
    st.markdown("""
    <style>
    .minimalist-navbar {
        background: white;
        padding: 1.5rem 2rem;
        margin-bottom: 2rem;
        border-bottom: 2px solid #0066cc;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
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
        letter-spacing: -0.5px;
        font-family: "Arial", sans-serif;
    }
    
    .nav-links {
        display: flex;
        gap: 0.5rem;
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
        font-family: "Arial", sans-serif;
    }
    
    .nav-link:hover {
        background: white;
        color: #0066cc;
        box-shadow: 0 2px 8px rgba(0,102,204,0.1);
    }
    
    .nav-link.active {
        background: #0066cc;
        color: white;
        box-shadow: 0 2px 8px rgba(0,102,204,0.2);
    }
    
    @media (max-width: 768px) {
        .nav-content {
            flex-direction: column;
            gap: 1rem;
        }
        
        .nav-links {
            width: 100%;
            justify-content: center;
        }
    }
    </style>

    <div class="minimalist-navbar">
        <div class="nav-content">
            <div class="nav-title">Tododrogas</div>
            <div class="nav-links">
                <a href="/" class="nav-link active">Inicio</a>
                <a href="/pages/1_Cuentas_Medicas" class="nav-link">Cuentas Médicas</a>
                <a href="/pages/2_Cartera" class="nav-link">Cartera</a>
                <a href="/pages/3_Tesoreria" class="nav-link">Tesorería</a>
                <a href="/pages/4_Metricas_y_Contacto" class="nav-link">Métricas</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
