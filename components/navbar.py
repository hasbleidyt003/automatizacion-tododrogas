import streamlit as st

def modern_navbar():
    st.markdown("""
    <style>
    /* Navbar super cool con efectos 3D */
    .cool-navbar {
        background: linear-gradient(135deg, #0066cc 0%, #004499 100%);
        padding: 1rem 2rem;
        border-radius: 0 0 20px 20px;
        margin: -2rem -2rem 2rem -2rem;
        box-shadow: 0 8px 32px rgba(0, 102, 204, 0.3);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
        border: none;
    }
    
    .cool-navbar::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
    }
    
    .cool-navbar::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: rgba(255,255,255,0.1);
    }
    
    .navbar-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        position: relative;
        z-index: 2;
    }
    
    .navbar-brand {
        font-size: 1.4rem;
        font-weight: 800;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .navbar-brand::before {
        content: '⚡';
        font-size: 1.6rem;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
    }
    
    .navbar-stats {
        display: flex;
        gap: 1.5rem;
        font-size: 0.9rem;
    }
    
    .stat-item {
        display: flex;
        align-items: center;
        gap: 0.3rem;
        background: rgba(255,255,255,0.1);
        padding: 0.3rem 0.8rem;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #00ff88;
        box-shadow: 0 0 10px #00ff88;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    </style>
    
    <div class="cool-navbar">
        <div class="navbar-content">
            <div class="navbar-brand">
                TODODROGAS
            </div>
            <div class="navbar-stats">
                <div class="stat-item">
                    <div class="status-dot"></div>
                    <span>SISTEMA ACTIVO</span>
                </div>
                <div class="stat-item">
                    <span>v2.1.0</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
