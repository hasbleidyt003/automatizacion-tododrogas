import streamlit as st

def modern_navbar():
    st.markdown("""
    <style>
    /* Navbar minimalista con borde flotante */
    .minimal-navbar {
        background: white;
        padding: 1rem 0;
        margin: -1rem -1rem 1rem -1rem;
        border-bottom: 1px solid #e1e5e9;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        position: sticky;
        top: 0;
        z-index: 100;
        backdrop-filter: blur(10px);
    }
    
    .nav-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    .nav-brand {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a1a;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .nav-items {
        display: flex;
        gap: 2rem;
        align-items: center;
    }
    
    .nav-item {
        color: #666666;
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 500;
        padding: 0.3rem 0;
        border-bottom: 2px solid transparent;
        transition: all 0.2s ease;
    }
    
    .nav-item:hover {
        color: #0066cc;
        border-bottom-color: #0066cc;
    }
    
    .nav-status {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.8rem;
        color: #00a86b;
        background: rgba(0, 168, 107, 0.1);
        padding: 0.3rem 0.8rem;
        border-radius: 12px;
        border: 1px solid rgba(0, 168, 107, 0.2);
    }
    
    .status-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #00a86b;
    }
    </style>
    
    <div class="minimal-navbar">
        <div class="nav-content">
            <div class="nav-brand">
                <span>⚡</span>
                <span>TodoDrogas Automation</span>
            </div>
            
            <div class="nav-items">
                <a href="#" class="nav-item">Inicio</a>
                <a href="#" class="nav-item">Cuentas Médicas</a>
                <a href="#" class="nav-item">Cartera</a>
                <a href="#" class="nav-item">Tesorería</a>
                <a href="#" class="nav-item">Métricas</a>
                
                <div class="nav-status">
                    <div class="status-dot"></div>
                    <span>En línea</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
