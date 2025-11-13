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

    /* BOTONES PRINCIPALES - MÁS COMPACTOS */
    .main-button {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 255, 255, 0.25);
        border-radius: 15px;
        padding: 20px 15px;
        margin: 10px;
        box-shadow: 0 8px 30px rgba(0, 255, 255, 0.2);
        transition: all 0.3s ease;
        text-align: center;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        cursor: pointer;
    }

    .main-button:hover {
        transform: translateY(-3px);
        border-color: rgba(0, 255, 255, 0.5);
        box-shadow: 0 12px 40px rgba(0, 255, 255, 0.35);
        background: rgba(255, 255, 255, 0.12);
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

    /* BOTONES ACCEDER - COMPACTOS */
    .stButton button {
        background: rgba(0, 255, 255, 0.15);
        color: #e0ffff;
        border: 1px solid rgba(0, 255, 255, 0.4);
        border-radius: 8px;
        padding: 8px 0;
        font-size: 14px;
        font-weight: 600;
        width: 160px !important;
        min-width: 160px !important;
        max-width: 160px !important;
        transition: all 0.3s ease;
        margin: 10px auto 0 auto !important;
        display: block !important;
    }

    .stButton button:hover {
        background: rgba(0, 255, 255, 0.25);
        color: #00ffff;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.4);
        transform: scale(1.05);
    }

    .footer {
        text-align: center;
        font-size: 0.8em;
        margin-top: 30px;
        color: #99e6ff;
    }
    
    /* CONTENIDO DE BOTÓN PRINCIPAL */
    .button-content {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }
    
    /* LISTA COMPACTA */
    .compact-list {
        font-size: 0.8em;
        line-height: 1.2;
        text-align: left;
        margin: 8px 0;
        color: #c0f0ff;
    }
    
    .eps-title {
        font-size: 1.3em;
        font-weight: bold;
        color: #00ffff;
        margin-bottom: 8px;
        text-shadow: 0 0 10px rgba(0,255,255,0.5);
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
    # BOTONES PRINCIPALES DE EPS - COMPACTOS
    # =========================================================
    st.markdown("### 🔄 MÓDULOS DE PROCESAMIENTO POR EPS")
    
    eps_col1, eps_col2, eps_col3 = st.columns(3)
    
    with eps_col1:  # SALUD TOTAL
        if st.button("", key="salud_total_main"):
            st.switch_page("pages/4_💊_Salud_Total.py")
        st.markdown("""
        <div class="main-button" onclick="this.parentNode.querySelector('button').click()">
            <div class="button-content">
                <div class="eps-title">💊 SALUD TOTAL</div>
                <div class="compact-list">
                - PROCESADOR DE ACTAS - OCR AVANZADO<br>
                - CONVERSOR MANTIS JSON<br>
                - CONVERSOR SISPRO JSON<br>
                - RENOMBRADOR CUV MANTIS
                </div>
            </div>
            <div style="margin-top: 10px;">
                <small>Haz clic para acceder</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with eps_col2:  # COOSALUD
        if st.button("", key="coosalud_main"):
            st.switch_page("pages/2_📋_COOSALUD.py")
        st.markdown("""
        <div class="main-button" onclick="this.parentNode.querySelector('button').click()">
            <div class="button-content">
                <div class="eps-title">📋 COOSALUD</div>
                <div class="compact-list">
                - CONVERSOR MANTIS JSON<br>
                - CONVERSOR SISPRO JSON<br>
                - RENOMBRADOR CUV MANTIS<br>
                - RENOMBRADOR RIPS
                </div>
            </div>
            <div style="margin-top: 10px;">
                <small>Haz clic para acceder</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with eps_col3:  # SAVIA
        if st.button("", key="savia_main"):
            st.switch_page("pages/3_🏥_SAVIA.py")
        st.markdown("""
        <div class="main-button" onclick="this.parentNode.querySelector('button').click()">
            <div class="button-content">
                <div class="eps-title">🏥 SAVIA</div>
                <div class="compact-list">
                - CONVERSOR MANTIS JSON<br>
                - CONVERSOR SISPRO JSON<br>
                - RENOMBRADOR CUV MANTIS<br>
                - RENOMBRADOR RIPS
                </div>
            </div>
            <div style="margin-top: 10px;">
                <small>Haz clic para acceder</small>
            </div>
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
    <div class="main-button" onclick="this.parentNode.querySelector('button').click()">
        <div class="button-content">
            <div class="eps-title">🏥 GESTIÓN INTEGRAL DE CUENTAS</div>
            <div class="compact-list">
            • Validación de archivos RIPS<br>
            • Procesamiento masivo de datos<br>
            • Generación de reportes automáticos<br>
            • Control de calidad y auditoría<br>
            • Integración con todas las EPS
            </div>
        </div>
        <div style="margin-top: 10px;">
            <small>Haz clic para acceder al área completa</small>
        </div>
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
        
        st.markdown("""
        <div style='
            background: rgba(255,255,255,0.05); 
            padding: 15px; 
            border-radius: 10px; 
            border: 1px solid rgba(0,255,255,0.2);
            margin-top: 10px;
        '>
            <div style='color: #9eefff; font-size: 0.9em;'><b>Eficiencia del Sistema:</b></div>
            <div style='color: #c0f0ff; font-size: 0.8em;'>
            • 99.2% Tiempo Activo<br>
            • 15.7s Procesamiento Promedio<br>
            • 0 Errores Críticos
            </div>
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
        
        st.markdown("""
        <div style='
            background: rgba(255,255,255,0.05); 
            padding: 15px; 
            border-radius: 10px; 
            border: 1px solid rgba(0,255,255,0.2);
            margin-top: 10px;
        '>
            <div style='color: #9eefff; font-size: 0.9em;'><b>Actividad Reciente:</b></div>
            <div style='color: #c0f0ff; font-size: 0.8em;'>
            • 34 archivos COOSALUD<br>
            • 28 archivos SAVIA<br>
            • 12 archivos Salud Total
            </div>
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
