import streamlit as st
import base64

# =========================================================
# 🎨 ESTILO GLASSMORPHISM CORPORATIVO TODODROGAS
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

    .glass-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 255, 255, 0.25);
        border-radius: 20px;
        padding: 25px;
        margin: 10px;
        box-shadow: 0 8px 30px rgba(0, 255, 255, 0.2);
        transition: all 0.3s ease;
        text-align: center;
    }

    .glass-card:hover {
        transform: translateY(-5px);
        border-color: rgba(0, 255, 255, 0.5);
        box-shadow: 0 12px 40px rgba(0, 255, 255, 0.35);
    }

    .main-title {
        text-align: center;
        font-size: 3em;
        font-weight: 700;
        color: #b3ffff;
        text-shadow: 0 0 20px rgba(0,255,255,0.6);
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #9eefff;
        margin-bottom: 40px;
        letter-spacing: 1px;
    }

    .stButton button {
        background: rgba(0, 255, 255, 0.1);
        color: #e0ffff;
        border: 1px solid rgba(0, 255, 255, 0.4);
        border-radius: 10px;
        padding: 12px 25px;
        font-size: 16px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton button:hover {
        background: rgba(0, 255, 255, 0.25);
        color: #00ffff;
        box-shadow: 0 0 25px rgba(0, 255, 255, 0.4);
        transform: scale(1.05);
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

    # Render forzado inicial
    st.write("")

    # Encabezado principal
    st.markdown('<h1 class="main-title">🏭 INVERSIONES TODODROGAS S.A.S</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Sistema de automatización y control interno</p>', unsafe_allow_html=True)

    st.sidebar.success("✅ Conectado a servidor Streamlit")
    st.sidebar.info("Seleccione un módulo del sistema para continuar.")

    # =========================================================
    # TARJETAS DE ACCESO PRINCIPALES
    # =========================================================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📊 CUENTAS MÉDICAS")
        st.write("Gestión de EPS, validación de archivos y reportes automáticos.")
        if st.button("ACCEDER", key="cuentas"):
            st.switch_page("pages/1_Cuentas_Medicas.py")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📦 INVENTARIOS")
        st.write("Gestione y analice el stock de productos, entradas y salidas.")
        st.button("PRÓXIMAMENTE", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 🤖 REPORTES IA")
        st.write("Generación de reportes automáticos mediante inteligencia artificial.")
        st.button("PRÓXIMAMENTE", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)

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
