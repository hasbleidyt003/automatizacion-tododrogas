import streamlit as st

def modern_navbar():
    # Barra lateral para navegación (MEJORA DE ACCESIBILIDAD)
    with st.sidebar:
        st.markdown("### 🧭 Navegación Rápida")
        st.page_link("app.py", label="🏠 Inicio", icon="🏠")
        st.page_link("pages/Cuentas_Medicas.py", label="📋 Cuentas Médicas", icon="📋")
        st.page_link("pages/Cartera.py", label="💰 Cartera", icon="💰") 
        st.page_link("pages/Tesoreria.py", label="🏦 Tesorería", icon="🏦")
        st.page_link("pages/Metricas_y_Contacto.py", label="📊 Métricas", icon="📊")
        
        st.markdown("---")
        st.markdown("### 🔐 Sesión")
        if st.button("🚪 Cerrar Sesión", use_container_width=True):
            st.success("Sesión cerrada exitosamente")
    
    st.markdown("""
    <style>
    .modern-navbar {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        padding: 0.8rem 0;
        margin-bottom: 0;
        border-bottom: 1px solid rgba(0, 102, 204, 0.1);
        position: relative;
        z-index: 1000;
    }
    
    .nav-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    .nav-title {
        color: #1a1a1a;
        font-size: 1.4rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        font-family: 'Inter', sans-serif;
    }
    
    .nav-title span {
        background: linear-gradient(135deg, #0066cc, #00a8ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .nav-user {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .user-info {
        text-align: right;
    }
    
    .user-name {
        font-weight: 600;
        color: #1a1a1a;
        font-size: 0.9rem;
    }
    
    .user-role {
        color: #666;
        font-size: 0.8rem;
    }
    
    @media (max-width: 768px) {
        .nav-content {
            flex-direction: column;
            gap: 1rem;
        }
        
        .nav-user {
            width: 100%;
            justify-content: center;
        }
    }
    </style>

    <div class="modern-navbar">
        <div class="nav-content">
            <div class="nav-title">Todo<span>drogas</span> • Automatización</div>
            <div class="nav-user">
                <div class="user-info">
                    <div class="user-name">Usuario: Admin</div>
                    <div class="user-role">Sistema • Conectado</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
