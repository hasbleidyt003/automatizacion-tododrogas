import streamlit as st

def apply_glass_tododrogas_style():
    st.markdown("""
    <style>
    /* ====== ESTILO GLASSMORPHISM CUENTAS MÉDICAS ====== */

    .stApp {
        background: linear-gradient(135deg, #00111a 0%, #001f33 50%, #002b40 100%);
        color: #e0f7fa;
        position: relative;
        overflow: hidden;
        font-family: 'Poppins', sans-serif;
    }

    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background:
            radial-gradient(circle at 20% 20%, rgba(0, 255, 255, 0.08), transparent 40%),
            radial-gradient(circle at 80% 80%, rgba(0, 200, 255, 0.05), transparent 50%);
        z-index: -2;
    }

    .glass-title {
        font-size: 3em;
        font-weight: 700;
        color: #e0f7fa;
        text-shadow: 0 0 20px rgba(0,255,255,0.6);
        letter-spacing: 2px;
        text-align: center;
        margin-bottom: 5px;
    }

    .glass-subtitle {
        text-align: center;
        font-size: 1.1em;
        color: #a7f0ff;
        margin-bottom: 35px;
        letter-spacing: 1.5px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 255, 255, 0.2);
        border-radius: 18px;
        padding: 25px;
        margin: 15px 0;
        transition: all 0.3s ease;
        box-shadow: 0 2px 20px rgba(0, 255, 255, 0.1);
    }

    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 40px rgba(0, 255, 255, 0.3);
        border: 1px solid rgba(0, 255, 255, 0.3);
    }

    .client-title {
        font-size: 1.4em;
        font-weight: 600;
        color: #b3ffff;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 0 0 10px rgba(0,255,255,0.6);
    }

    .client-list {
        font-family: 'Poppins', sans-serif;
        color: #ccffff;
        font-size: 0.95em;
        margin-bottom: 10px;
        line-height: 1.6;
    }

    .stButton button {
        background: rgba(0, 255, 255, 0.1);
        color: #e0ffff;
        border: 1px solid rgba(0, 255, 255, 0.3);
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 14px;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        width: 100%;
    }

    .stButton button:hover {
        background: rgba(0, 255, 255, 0.25);
        border-color: rgba(0, 255, 255, 0.5);
        color: #00ffff;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    apply_glass_tododrogas_style()

    st.markdown('<h1 class="glass-title">MÓDULO CUENTAS MÉDICAS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="glass-subtitle">Inversiones TODODROGAS S.A.S | Gestión Inteligente EPS</p>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### 💎 SELECCIONE CLIENTE EPS")

    col1, col2, col3 = st.columns(3)

    # COOSALUD
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="client-title">COOSALUD</div>', unsafe_allow_html=True)
        st.markdown('<div class="client-list">', unsafe_allow_html=True)
        st.markdown("""
        ▸ Conversores JSON  
        ▸ Renombradores CUV  
        ▸ Validación RIPS  
        ▸ SISPRO Mantis
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button("Acceder COOSALUD", key="coosalud"):
            st.switch_page("pages/2_COOSALUD.py")
        st.markdown('</div>', unsafe_allow_html=True)

    # SAVIA
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="client-title">SAVIA</div>', unsafe_allow_html=True)
        st.markdown('<div class="client-list">', unsafe_allow_html=True)
        st.markdown("""
        ▸ Conversores JSON  
        ▸ Renombradores CUV  
        ▸ Validación RIPS  
        ▸ SISPRO Mantis
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button("Acceder SAVIA", key="savia"):
            st.switch_page("pages/3_SAVIA.py")
        st.markdown('</div>', unsafe_allow_html=True)

    # SALUD TOTAL
    with col3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="client-title">SALUD TOTAL</div>', unsafe_allow_html=True)
        st.markdown('<div class="client-list">', unsafe_allow_html=True)
        st.markdown("""
        ▸ Procesador PDF  
        ▸ OCR Avanzado  
        ▸ Validador de Documentos  
        ▸ Extracción de Datos
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button("Acceder SALUD TOTAL", key="salud_total"):
            st.switch_page("pages/4_Salud_Total.py")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ⚙️ STATUS DEL SISTEMA")

    status_col1, status_col2 = st.columns(2)

    with status_col1:
        st.markdown("**▸ MÓDULOS ACTIVOS:**")
        st.markdown("```bash\n✓ COOSALUD_JSON_PROCESSOR\n✓ SAVIA_VALIDATION_TOOLS\n✓ SALUD_TOTAL_PDF_OCR\n```")

    with status_col2:
        st.markdown("**▸ ÚLTIMO ACCESO:**")
        st.markdown("```bash\n# SYSTEM_LOG\n> Todas las EPS operativas\n> Procesamiento: ONLINE\n> Seguridad: ACTIVADA\n```")

    st.markdown("---")
    if st.button("⬅ VOLVER AL NÚCLEO PRINCIPAL"):
        st.switch_page("streamlit_app.py")


if __name__ == "__main__":
    main()
