def modern_navbar():
    # AGREGAR ESTE CSS PARA FORZAR SIDEBAR IZQUIERDO
    st.markdown("""
    <style>
    /* FORZAR SIDEBAR IZQUIERDO */
    .css-1d391kg {
        position: fixed;
        left: 0;
        top: 0;
        bottom: 0;
        width: 20rem !important;
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-right: 1px solid rgba(0, 102, 204, 0.1);
        z-index: 999;
    }
    
    /* AJUSTAR CONTENIDO PRINCIPAL */
    .main .block-container {
        margin-left: 21rem !important;
        padding-top: 1rem;
    }
    
    /* NAVBAR SUPERIOR */
    .modern-navbar {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        padding: 0.8rem 0;
        margin-bottom: 2rem;
        border-bottom: 1px solid rgba(0, 102, 204, 0.1);
        position: relative;
        z-index: 1000;
        margin-left: 20rem;
        width: calc(100% - 20rem);
    }
    
    .nav-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # EL RESTO DE TU CÓDIGO ORIGINAL SE MANTIENE IGUAL
    with st.sidebar:
        st.markdown("### 🧭 Navegación Rápida")
        
        # Botones de navegación simples
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🏠 Inicio", use_container_width=True):
                st.switch_page("streamlit_app.py")
        with col2:
            if st.button("📊 Métricas", use_container_width=True):
                st.switch_page("pages/Metricas_y_Contacto.py")
        
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
        st.info("🟢 Conectado como Administrador")
        if st.button("🚪 Cerrar Sesión", use_container_width=True):
            st.success("Sesión cerrada exitosamente")

    # Navbar principal (se ajusta automáticamente con el CSS)
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
