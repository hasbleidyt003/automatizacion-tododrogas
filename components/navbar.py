import streamlit as st

def modern_navbar():
    st.markdown("""
    <style>
    .modern-navbar {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 0.8rem 2rem;
        margin-bottom: 1rem;
        box-shadow: 
            0 4px 20px rgba(0,0,0,0.08),
            0 2px 8px rgba(0,0,0,0.05),
            inset 0 1px 0 rgba(255,255,255,0.8);
        border-bottom: 1px solid rgba(255,255,255,0.3);
        position: relative;
        z-index: 1000;
        backdrop-filter: blur(10px);
        height: 70px;
    }
    
    .modern-navbar::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #0066cc, #0088ff, #004499);
        border-radius: 0 0 10px 10px;
    }
    
    .nav-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
        height: 100%;
    }
    
    .nav-title {
        color: #1a1a1a;
        font-size: 1.5rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        font-family: 'Inter', sans-serif;
        text-shadow: 0 2px 4px rgba(0,0,0,0.05);
        position: relative;
    }
    
    .nav-title span {
        background: linear-gradient(135deg, #0066cc, #004499);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        position: relative;
    }
    
    .nav-title span::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, #0066cc, #004499);
        border-radius: 2px;
    }
    
    .nav-links {
        display: flex;
        gap: 0.3rem;
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        border-radius: 10px;
        padding: 0.3rem;
        border: 1px solid rgba(255,255,255,0.5);
        box-shadow: 
            inset 0 1px 0 rgba(255,255,255,0.6),
            0 4px 12px rgba(0,0,0,0.08);
        backdrop-filter: blur(10px);
        position: relative;
    }
    
    .nav-links::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(255,255,255,0.8), rgba(255,255,255,0.4));
        border-radius: 10px;
        z-index: -1;
    }
    
    .nav-link {
        color: #666666;
        text-decoration: none;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-weight: 500;
        font-size: 0.85rem;
        font-family: 'Inter', sans-serif;
        position: relative;
        overflow: hidden;
        background: transparent;
        border: 1px solid transparent;
    }
    
    .nav-link::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: left 0.5s;
    }
    
    .nav-link:hover::before {
        left: 100%;
    }
    
    .nav-link:hover {
        background: rgba(255,255,255,0.9);
        color: #0066cc;
        box-shadow: 
            0 4px 15px rgba(0,102,204,0.15),
            0 2px 4px rgba(0,0,0,0.05);
        transform: translateY(-1px);
        border: 1px solid rgba(0,102,204,0.1);
    }
    
    .nav-link.active {
        background: linear-gradient(135deg, #0066cc, #004499);
        color: white;
        box-shadow: 
            0 4px 15px rgba(0,102,204,0.25),
            inset 0 1px 0 rgba(255,255,255,0.2);
        border: 1px solid rgba(0,102,204,0.3);
        text-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    
    .nav-link.active:hover {
        background: linear-gradient(135deg, #0052a3, #003366);
        transform: translateY(-1px);
        box-shadow: 
            0 6px 20px rgba(0,102,204,0.3),
            inset 0 1px 0 rgba(255,255,255,0.2);
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .modern-navbar {
            padding: 0.8rem 1rem;
            height: auto;
        }
        
        .nav-content {
            flex-direction: column;
            gap: 1rem;
        }
        
        .nav-links {
            width: 100%;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        .nav-link {
            padding: 0.5rem 1rem;
            font-size: 0.8rem;
        }
    }
    </style>

    <div class="modern-navbar">
        <div class="nav-content">
            <div class="nav-title">Todo<span>drogas</span></div>
            <div class="nav-links">
                <a href="/" class="nav-link active">Inicio</a>
                <a href="/Cuentas_Medicas" class="nav-link">Cuentas Médicas</a>
                <a href="/Cartera" class="nav-link">Cartera</a>
                <a href="/Tesoreria" class="nav-link">Tesorería</a>
                <a href="/Metricas_y_Contacto" class="nav-link">Métricas</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
