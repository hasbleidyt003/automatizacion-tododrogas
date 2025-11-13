import streamlit as st

# =========================================================
# 💊 ESTILO GLASSMORPHISM CORPORATIVO TODODROGAS - CORREGIDO
# =========================================================
def apply_glass_tododrogas_style():
    st.markdown("""
    <style>
    /* ======= ESTILO GLASSMORPHISM TODODROGAS ======= */
    .stApp {
        background: linear-gradient(135deg, #00111a 0%, #001f33 50%, #00334d 100%);
        color: #e0f7fa;
        font-family: 'Poppins', sans-serif;
        overflow: hidden;
    }

    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background:
            radial-gradient(circle at 25% 25%, rgba(0, 255, 255, 0.05), transparent 40%),
            radial-gradient(circle at 80% 80%, rgba(0, 200, 255, 0.08), transparent 50%);
        z-index: -2;
    }

    /* CONTENEDOR PRINCIPAL MEJORADO */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* TARJETAS GLASSMORPHISM */
    .glass-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 255, 255, 0.25);
        border-radius: 20px;
        padding: 25px 20px;
        margin: 10px 0;
        box-shadow: 0 8px 30px rgba(0, 255, 255, 0.2);
        transition: all 0.3s ease;
        text-align: center;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .glass-card:hover {
        transform: translateY(-5px);
        border-color: rgba(0, 255, 255, 0.5);
        box-shadow: 0 12px 40px rgba(0, 255, 255, 0.35);
    }

    /* CONTENIDO DE TARJETAS */
    .card-content {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    /* BOTONES MEJORADOS - TAMAÑOS FIJOS */
    .stButton button {
        background: rgba(0, 255, 255, 0.1);
        color: #e0ffff;
        border: 1px solid rgba(0, 255, 255, 0.4);
        border-radius: 12px;
        padding: 12px 0;
        font-size: 14px;
        font-weight: 600;
        width: 180px !important;
        min-width: 180px !important;
        max-width: 180px !important;
        transition: all 0.3s ease;
        margin: 10px auto !important;
        display: block !important;
    }

    .stButton button:hover {
        background: rgba(0, 255, 255, 0.25);
        color: #00ffff;
        box-shadow: 0 0 25px rgba(0, 255, 255, 0.4);
        transform: scale(1.05);
        border-color: rgba(0, 255, 255, 0.7);
    }

    /* BOTÓN DESHABILITADO */
    .stButton button:disabled {
        background: rgba(128, 128, 128, 0.2);
        color: #88aaff;
        border: 1px solid rgba(128, 128, 128, 0.4);
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }

    .stButton button:disabled:hover {
        background: rgba(128, 128, 128, 0.2);
        color: #88aaff;
        border: 1px solid rgba(128, 128, 128, 0.4);
        transform: none;
        box-shadow: none;
    }

    /* CONTENEDOR DE BOTONES CENTRADO */
    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: auto;
        padding-top: 15px;
        width: 100%;
    }

    /* TÍTULOS */
    .main-title {
        text-align: center;
        font-size: 2.8em;
        font-weight: 700;
        color: #b3ffff;
        text-shadow: 0 0 20px rgba(0,255,255,0.6);
        margin-bottom: 10px;
        padding-top: 1rem;
    }

    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #9eefff;
        margin-bottom: 30px;
        letter-spacing: 1px;
    }

    /* SEPARADOR */
    .stMarkdown hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(0,255,255,0.5), transparent);
        margin: 30px 0;
    }

    /* FOOTER */
    .footer {
        text-align: center;
        font-size: 0.9em;
        margin-top: 30px;
        color: #99e6ff;
        padding: 20px;
    }

    /* SIDEBAR */
    .sidebar .sidebar-content {
        background: rgba(0, 30, 60, 0.8);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(0, 255, 255, 0.2);
    }

    /* RESPONSIVE */
    @media (max-width: 768px) {
        .glass-card {
            min-height: 180px;
            padding: 20px 15px;
        }
        
        .main-title {
            font-size: 2.2em;
        }
        
        .stButton button {
            width: 160px !important;
            min-width: 160px !important;
            max-width: 160px !important;
            padding: 10px 0;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# =========================================================
# 🧠 CONTENIDO PRINCIPAL - ESTRUCTURA CORREGIDA
# =========================================================
def main():
    apply_glass_tododrogas_style()

    st.markdown('<h1 class="main-title">💊 INVERSIONES TODODROGAS S.A.S</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Sistema de automatización y control interno</p>', unsafe_allow_html=True)

    st.sidebar.success("✅ Conectado a servidor Streamlit")
    st.sidebar.info("Interfaz visual restringida (solo vista corporativa).")

    # =========================================================
    # TARJETAS PRINCIPALES - BOTONES CON TAMAÑOS FIJOS
    # =========================================================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-content">', unsafe_allow_html=True)
        st.markdown("### 📊 CUENTAS MÉDICAS")
        st.write("Gestión de EPS, validación de archivos y reportes automáticos.")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        if st.button("ACCEDER", key="cuentas_medicas"):
            st.switch_page("pages/1_🏥_Cuentas_Medicas.py")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-content">', unsafe_allow_html=True)
        st.markdown("### 📦 INVENTARIOS")
        st.write("Gestione y analice el stock de productos, entradas y salidas.")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        st.button("PRÓXIMAMENTE", key="inventarios", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-content">', unsafe_allow_html=True)
        st.markdown("### 🤖 REPORTES IA")
        st.write("Generación de reportes automáticos mediante inteligencia artificial.")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        st.button("PRÓXIMAMENTE", key="reportes_ia", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # =========================================================
    # INFORMACIÓN ADICIONAL
    # =========================================================
    st.markdown("---")
    
    info_col1, info_col2 = st.columns(2)
    
    with info_col1:
        st.markdown("### 📋 EPS Conectadas")
        st.markdown("""
        - **COOSALUD**
        - **SAVIA** 
        - **SALUD TOTAL**
        """)
    
    with info_col2:
        st.markdown("### 🔄 Procesos Automatizados")
        st.markdown("""
        - Validación de archivos RIPS
        - Generación de reportes
        - Sincronización en tiempo real
        """)

    # =========================================================
    # PIE DE PÁGINA
    # =========================================================
    st.markdown("---")
    st.markdown(
        '<p class="footer">© 2025 Inversiones TODODROGAS S.A.S | Todos los derechos reservados</p>',
        unsafe_allow_html=True
    )

# =========================================================
# 🚀 EJECUCIÓN PRINCIPAL
# =========================================================
if __name__ == "__main__":
    main()
