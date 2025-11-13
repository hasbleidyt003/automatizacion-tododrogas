import streamlit as st

def apply_glass_tododrogas_style():
    st.markdown("""
    <style>
    /* ====== ESTILO GLASSMORPHISM COOSALUD ====== */

    .stApp {
        background: linear-gradient(135deg, #00111a 0%, #001f33 50%, #002b40 100%);
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
            radial-gradient(circle at 20% 20%, rgba(0, 255, 255, 0.08), transparent 40%),
            radial-gradient(circle at 80% 80%, rgba(0, 200, 255, 0.05), transparent 50%);
        z-index: -2;
    }

    .glass-title {
        font-size: 3em;
        font-weight: 700;
        color: #e0f7fa;
        text-align: center;
        text-shadow: 0 0 25px rgba(0,255,255,0.6);
        margin-bottom: 10px;
    }

    .glass-subtitle {
        text-align: center;
        font-size: 1.1em;
        color: #a7f0ff;
        margin-bottom: 35px;
        letter-spacing: 1.2px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 255, 255, 0.2);
        border-radius: 18px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 4px 30px rgba(0, 255, 255, 0.1);
        transition: all 0.3s ease;
    }

    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 40px rgba(0, 255, 255, 0.3);
        border: 1px solid rgba(0, 255, 255, 0.3);
    }

    .tool-title {
        font-size: 1.4em;
        font-weight: 600;
        color: #b3ffff;
        margin-bottom: 8px;
        text-shadow: 0 0 10px rgba(0,255,255,0.6);
    }

    .tool-description {
        font-size: 0.95em;
        color: #ccffff;
        line-height: 1.5;
        margin-bottom: 10px;
    }

    .module-tag {
        background: rgba(0, 255, 255, 0.1);
        border: 1px solid rgba(0, 255, 255, 0.4);
        padding: 3px 8px;
        border-radius: 10px;
        font-size: 0.8em;
        margin: 2px;
        display: inline-block;
        color: #b3ffff;
    }

    .stButton button {
        background: rgba(0, 255, 255, 0.1);
        color: #e0ffff;
        border: 1px solid rgba(0, 255, 255, 0.3);
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 14px;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        transition: all 0.3s ease;
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

    # HEADER
    st.markdown('<h1 class="glass-title">COOSALUD</h1>', unsafe_allow_html=True)
    st.markdown('<p class="glass-subtitle">Módulo de procesamiento - Inversiones TODODROGAS S.A.S</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 🧠 Seleccione herramienta de procesamiento")

    # CONVERSORES JSON
    st.markdown("#### ▸ CONVERSORES JSON")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">MANTIS PROCESSOR</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-description">Procesamiento de archivos JSON MANTIS con validación de estructura, fechas y exportación formateada.</div>', unsafe_allow_html=True)
        st.markdown('<div class="module-tag">JSON_PROCESSOR</div><div class="module-tag">DATA_VALIDATION</div>', unsafe_allow_html=True)
        if st.button("EJECUTAR MANTIS", key="mantis"):
            st.switch_page("pages/coosalud/1_MANTIS_JSON.py")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">SISPRO INTERFACE</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-description">Conversión JSON SISPRO con validación de campos, normalización y reporte automático.</div>', unsafe_allow_html=True)
        st.markdown('<div class="module-tag">SISPRO_API</div><div class="module-tag">DATA_NORMALIZATION</div>', unsafe_allow_html=True)
        if st.button("EJECUTAR SISPRO", key="sispro"):
            st.switch_page("pages/coosalud/2_SISPRO_JSON.py")
        st.markdown('</div>', unsafe_allow_html=True)

    # RENOMBRADORES
    st.markdown("#### ▸ RENOMBRADORES AUTOMATIZADOS")

    col3, col4, col5 = st.columns(3)

    with col3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">CUV MANTIS</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-description">Renombrado automático por CUV con validación y organización de archivos.</div>', unsafe_allow_html=True)
        st.markdown('<div class="module-tag">CUV_SYSTEM</div><div class="module-tag">AUTO_RENAME</div>', unsafe_allow_html=True)
        if st.button("EJECUTAR CUV", key="cuv_mantis"):
            st.switch_page("pages/coosalud/3_CUV_MANTIS.py")
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">RIPS MANAGER</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-description">Procesamiento y validación de RIPS con generación de reportes automáticos.</div>', unsafe_allow_html=True)
        st.markdown('<div class="module-tag">RIPS_PROTOCOL</div><div class="module-tag">FORMAT_VALIDATION</div>', unsafe_allow_html=True)
        if st.button("EJECUTAR RIPS", key="rips"):
            st.switch_page("pages/coosalud/4_RIPS.py")
        st.markdown('</div>', unsafe_allow_html=True)

    with col5:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">SISPRO + CUV</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-description">Integración SISPRO + CUV para validación cruzada y renombrado automático.</div>', unsafe_allow_html=True)
        st.markdown('<div class="module-tag">SISPRO_CUV</div><div class="module-tag">CROSS_VALIDATION</div>', unsafe_allow_html=True)
        if st.button("EJECUTAR SISPRO+CUV", key="sispro_cuv"):
            st.switch_page("pages/coosalud/5_SISPRO_CUV.py")
        st.markdown('</div>', unsafe_allow_html=True)

    # STATUS
    st.markdown("---")
    st.markdown("### ⚙️ STATUS COOSALUD")

    status_col1, status_col2 = st.columns(2)

    with status_col1:
        st.markdown("**▸ MÓDULOS ACTIVOS:**")
        st.markdown("```bash\n✓ MANTIS_JSON_PROCESSOR\n✓ SISPRO_CONVERTER\n✓ CUV_RENAMER\n✓ RIPS_VALIDATOR\n```")

    with status_col2:
        st.markdown("**▸ ESTADÍSTICAS:**")
        st.markdown("```bash\n# SYSTEM_STATS\n> Archivos procesados: 1,247\n> Tasa de éxito: 98.7%\n> Última ejecución: ONLINE\n```")

    # BOTONES NAVEGACIÓN
    st.markdown("---")
    col_volver1, col_volver2 = st.columns(2)

    with col_volver1:
        if st.button("⬅ VOLVER A CUENTAS MÉDICAS"):
            st.switch_page("pages/1_Cuentas_Medicas.py")

    with col_volver2:
        if st.button("🏠 VOLVER AL NÚCLEO"):
            st.switch_page("streamlit_app.py")


if __name__ == "__main__":
    main()
