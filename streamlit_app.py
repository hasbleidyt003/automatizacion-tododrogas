import streamlit as st

# =========================================================
# 💊 ESTILO GLASSMORPHISM CORPORATIVO TODODROGAS
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

    /* BOTONES EPS - SOLO NOMBRE */
    .eps-button {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 255, 255, 0.25);
        border-radius: 15px;
        padding: 30px 20px;
        margin: 10px;
        box-shadow: 0 8px 30px rgba(0, 255, 255, 0.2);
        transition: all 0.3s ease;
        text-align: center;
        min-height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
    }

    .eps-button:hover {
        transform: translateY(-3px);
        border-color: rgba(0, 255, 255, 0.5);
        box-shadow: 0 12px 40px rgba(0, 255, 255, 0.35);
        background: rgba(255, 255, 255, 0.12);
    }

    .eps-name {
        font-size: 1.4em;
        font-weight: bold;
        color: #00ffff;
        text-shadow: 0 0 10px rgba(0,255,255,0.5);
        margin-bottom: 5px;
    }

    .click-hint {
        font-size: 0.8em;
        color: #9eefff;
        margin-top: 5px;
    }

    .main-title {
        text-align: center;
        font-size: 2.5em;
        font-weight: 700;
        color: #b3ffff;
        text-shadow: 0 0 20px rgba(0,255,255,0.6);
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 1.1em;
        color: #9eefff;
        margin-bottom: 30px;
        letter-spacing: 1px;
    }

    .footer {
        text-align: center;
        font-size: 0.8em;
        margin-top: 30px;
        color: #99e6ff;
    }
    </style>
    """, unsafe_allow_html=True)

# =========================================================
# 🧠 CONTENIDO PRINCIPAL
# =========================================================
def main():
    apply_glass_tododrogas_style()

    st.markdown('<h1 class="main-title">💊 INVERSIONES TODODROGAS S.A.S</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Sistema de automatización y control interno</p>', unsafe_allow_html=True)

    st.sidebar.success("✅ Conectado a servidor Streamlit")
    st.sidebar.info("Interfaz visual restringida (solo vista corporativa).")

    # =========================================================
    # BOTONES EPS - SOLO NOMBRE
    # =========================================================
    st.markdown("### 🔄 MÓDULOS DE PROCESAMIENTO POR EPS")
    
    eps_col1, eps_col2, eps_col3 = st.columns(3)
    
    with eps_col1:  # SALUD TOTAL
        if st.button("", key="salud_total_main"):
            st.switch_page("pages/4_💊_Salud_Total.py")
        st.markdown("""
        <div class="eps-button" onclick="this.parentNode.querySelector('button').click()">
            <div class="eps-name">💊 SALUD TOTAL</div>
            <div class="click-hint">Haz clic para acceder</div>
        </div>
        """, unsafe_allow_html=True)
    
    with eps_col2:  # COOSALUD
        if st.button("", key="coosalud_main"):
            st.switch_page("pages/2_📋_COOSALUD.py")
        st.markdown("""
        <div class="eps-button" onclick="this.parentNode.querySelector('button').click()">
            <div class="eps-name">📋 COOSALUD</div>
            <div class="click-hint">Haz clic para acceder</div>
        </div>
        """, unsafe_allow_html=True)
    
    with eps_col3:  # SAVIA
        if st.button("", key="savia_main"):
            st.switch_page("pages/3_🏥_SAVIA.py")
        st.markdown("""
        <div class="eps-button" onclick="this.parentNode.querySelector('button').click()">
            <div class="eps-name">🏥 SAVIA</div>
            <div class="click-hint">Haz clic para acceder</div>
        </div>
        """, unsafe_allow_html=True)

    # =========================================================
    # ÁREA DE CUENTAS MÉDICAS
    # =========================================================
    st.markdown("---")
    st.markdown("### 📊 ÁREA DE CUENTAS MÉDICAS")
    
    if st.button("", key="cuentas_main"):
        st.switch_page("pages/1_🏥_Cuentas_Medicas.py")
    st.markdown("""
    <div class="eps-button" onclick="this.parentNode.querySelector('button').click()" style="min-height: 100px;">
        <div class="eps-name">🏥 GESTIÓN INTEGRAL DE CUENTAS</div>
        <div class="click-hint">Haz clic para acceder al área completa</div>
    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # MÉTRICAS DEL SISTEMA
    # =========================================================
    st.markdown("---")
    st.markdown("### 📈 MÉTRICAS DEL SISTEMA")
    
    metric_col1, metric_col2 = st.columns(2)

    with metric_col1:
        st.markdown("""
        <div style='
            background: rgba(255,255,255,0.05); 
            padding: 15px; 
            border-radius: 10px; 
            border: 1px solid rgba(0,255,255,0.2);
            text-align: center;
        '>
            <div style='font-size: 2em; color: #00ffff; font-weight: bold;'>1,247</div>
            <div style='color: #9eefff; font-size: 0.9em;'>Archivos Procesados</div>
        </div>
        """, unsafe_allow_html=True)

    with metric_col2:
        st.markdown("""
        <div style='
            background: rgba(255,255,255,0.05); 
            padding: 15px; 
            border-radius: 10px; 
            border: 1px solid rgba(0,255,255,0.2);
            text-align: center;
        '>
            <div style='font-size: 2em; color: #00ffff; font-weight: bold;'>89</div>
            <div style='color: #9eefff; font-size: 0.9em;'>Sesiones Activas</div>
        </div>
        """, unsafe_allow_html=True)

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
