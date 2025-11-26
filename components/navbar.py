import streamlit as st
import streamlit as st

def modern_navbar():
    # CSS PARA OCULTAR ELEMENTOS NO DESEADOS
    st.markdown("""
    <style>
    /* OCULTAR HEADER DE STREAMLIT POR DEFECTO */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* OCULTAR BOTONES DE COMPARTIR Y GITHUB */
    .stAppDeployButton {display: none;}
    .stAppViewContainerMain [data-testid="stToolbar"] {display: none;}
    
    /* OCULTAR BOTÓN DE HAMBURGUESA (MENÚ) */
    .stAppViewContainerMain [data-testid="stSidebarNav"] {display: none;}
    
    /* OCULTAR ELEMENTOS DEL HEADER SUPERIOR */
    .stAppViewContainerMain [data-testid="stHeader"] {display: none;}
    
    /* OCULTAR BOTÓN DE GITHUB */
    .stAppViewContainerMain [data-testid="stGitHubButton"] {display: none;}
    
    /* OCULTAR BOTÓN DE COMPARTIR */
    .stAppViewContainerMain [data-testid="stShareButton"] {display: none;}
    
    /* OCULTAR BOTÓN DE ESTRELLA (FAVORITO) */
    .stAppViewContainerMain [data-testid="stAppMarkdownContainer"] > div:first-child {display: none;}
    
    /* ELIMINAR ESPACIO EXTRA DEL HEADER */
    .stApp > header {
        display: none !important;
    }
    
    /* OCULTAR TODO EL TOOLBAR SUPERIOR */
    .stAppViewContainerMain [data-testid="stToolbar"] {
        display: none !important;
    }
    
    /* ELIMINAR PADDING SUPERIOR */
    .stApp {
        margin-top: -50px;
    }
    
    /* MANTENER TU SIDEBAR VISIBLE */
    .css-1d391kg {
        visibility: visible !important;
    }
    </style>
    """, unsafe_allow_html=True)
def modern_navbar():
    # Barra lateral simplificada para navegación
    with st.sidebar:
        st.markdown("### 🧭 Navegación Rápida")
        
        # Botones de navegación simples
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🏠 Inicio", use_container_width=True):
                st.switch_page("streamlit_app.py")
        with col2:
            if st.button("📊 Métricas", use_container_width=True):
                st.switch_page("pages/4_Metricas_y_Contacto.py")
        
        col3, col4 = st.columns(2)
        with col3:
            if st.button("📋 Médicas", use_container_width=True):
                st.switch_page("pages/1_Cuentas_Medicas.py")
        with col4:
            if st.button("💰 Cartera", use_container_width=True):
                st.switch_page("pages/2_Cartera.py")
        
        if st.button("🏦 Tesorería", use_container_width=True):
            st.switch_page("pages/3_Tesoreria.py")
        
        st.markdown("---")
        st.markdown("### 🔐 Sesión")
        
        # Estado de la sesión
        st.info("🟢 Conectado como Administrador")
        if st.button("🚪 Cerrar Sesión", use_container_width=True):
            st.success("Sesión cerrada exitosamente")
            # Aquí iría la lógica real de cierre de sesión

    # Navbar principal - CSS CORREGIDO
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
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-right: 1px solid rgba(0, 102, 204, 0.1);
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
    """, unsafe_allow_html=True)

    # HTML del navbar - SEPARADO del CSS
    st.markdown("""
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
