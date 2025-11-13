import streamlit as st

def apply_glass_tododrogas_style():
    st.markdown("""
    <style>
    /* ====== ESTILO GLASSMORPHISM SALUD TOTAL ====== */

    .stApp {
        background: linear-gradient(135deg, #021a10 0%, #013d2a 50%, #004d33 100%);
        color: #e0ffe6;
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
            radial-gradient(circle at 30% 20%, rgba(0, 255, 128, 0.08), transparent 40%),
            radial-gradient(circle at 80% 80%, rgba(0, 255, 128, 0.06), transparent 50%);
        z-index: -2;
    }

    .glass-title {
        font-size: 3em;
        font-weight: 700;
        color: #b9ffd0;
        text-align: center;
        text-shadow: 0 0 25px rgba(0,255,170,0.6);
        margin-bottom: 10px;
    }

    .glass-subtitle {
        text-align: center;
        font-size: 1.1em;
        color: #a8ffcb;
        margin-bottom: 35px;
        letter-spacing: 1.2px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 255, 170, 0.2);
        border-radius: 18px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 4px 30px rgba(0, 255, 170, 0.1);
        transition: all 0.3s ease;
    }

    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 40px rgba(0, 255, 170, 0.3);
        border: 1px solid rgba(0, 255, 170, 0.3);
    }

    .tool-title {
        font-size: 1.3em;
        font-weight: 600;
        color: #b3ffcc;
        margin-bottom: 8px;
        text-shadow: 0 0 10px rgba(0,255,170,0.6);
    }

    .tool-description {
        font-size: 0.95em;
        color: #ccffdd;
        line-height: 1.5;
        margin-bottom: 10px;
    }

    .module-tag {
        background: rgba(0, 255, 170, 0.1);
        border: 1px solid rgba(0, 255, 170, 0.4);
        padding: 3px 8px;
        border-radius: 10px;
        font-size: 0.8em;
        margin: 2px;
        display: inline-block;
        color: #b3ffcc;
    }

    .stButton button {
        background: rgba(0, 255, 170, 0.1);
        color: #e0ffee;
        border: 1px solid rgba(0, 255, 170, 0.3);
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
        background: rgba(0, 255, 170, 0.25);
        border-color: rgba(0, 255, 170, 0.5);
        color: #00ffaa;
        box-shadow: 0 0 20px rgba(0, 255, 170, 0.5);
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    apply_glass_tododrogas_style()

    # HEADER
    st.markdown('<h1 class="glass-title">SALUD TOTAL EPS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="glass-subtitle">Procesamiento documental avanzado - Inversiones TODODROGAS S.A.S</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📄 Seleccione procesador de documentos")

    # SISTEMA PDF
    st.markdown("#### ▸ PROCESAMIENTO PDF")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">PDF PROCESSOR</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-description">Extracción de texto, validación de documentos, clasificación automática y compresión inteligente.</div>', unsafe_allow_html=True)
        st.markdown('<div class="module-tag">PDF_AI</div><div class="module-tag">OCR_ENGINE</div>', unsafe_allow_html=True)
        if st.button("EJECUTAR PROCESADOR PDF", key="pdf_processor"):
            st.switch_page("pages/salud_total/1_Procesador_PDF.py")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">VALIDADOR DOCS</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-description">Verificación de formatos, detección de anomalías y auditoría de metadatos de documentos.</div>', unsafe_allow_html=True)
        st.markdown('<div class="module-tag">VALIDATION_AI</div><div class="module-tag">AUDIT_LOG</div>', unsafe_allow_html=True)
        if st.button("EJECUTAR VALIDADOR", key="validador_docs"):
            st.switch_page("pages/salud_total/2_Validador_PDF.py")
        st.markdown('</div>', unsafe_allow_html=True)

    # SISTEMA ESCÁNER
    st.markdown("#### ▸ PROCESAMIENTO ESCÁNER")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">SCAN PROCESSOR</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-description">Optimización de imágenes escaneadas, eliminación de ruido, corrección de orientación y mejora de calidad.</div>', unsafe_allow_html=True)
        st.markdown('<div class="module-tag">SCAN_OPTIMIZER</div><div class="module-tag">IMAGE_CLEANER</div>', unsafe_allow_html=True)
        if st.button("EJECUTAR PROCESADOR ESCÁNER", key="scan_processor"):
            st.switch_page("pages/salud_total/3_Procesador_Scan.py")
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="tool-title">OCR AVANZADO</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-description">Reconocimiento óptico inteligente, extracción de datos, validación de campos y exportación JSON/Excel.</div>', unsafe_allow_html=True)
        st.markdown('<div class="module-tag">ADVANCED_OCR</div><div class="module-tag">MACHINE_LEARNING</div>', unsafe_allow_html=True)
        if st.button("EJECUTAR OCR", key="ocr_avanzado"):
            st.switch_page("pages/salud_total/4_OCR_Avanzado.py")
        st.markdown('</div>', unsafe_allow_html=True)

    # STATUS
    st.markdown("---")
    st.markdown("### ⚙️ STATUS SALUD TOTAL")

    status_col1, status_col2 = st.columns(2)

    with status_col1:
        st.markdown("**▸ MÓDULOS ACTIVOS:**")
        st.markdown("```bash\n✓ PDF_PROCESSOR_AI\n✓ DOCUMENT_VALIDATOR\n✓ SCAN_OPTIMIZER\n✓ ADVANCED_OCR\n```")

    with status_col2:
        st.markdown("**▸ ESTADÍSTICAS:**")
        st.markdown("```bash\n# SYSTEM_STATS\n> Documentos procesados: 2,148\n> Tasa de reconocimiento: 96.3%\n> Velocidad promedio: 0.8s/doc\n```")

    # NAVEGACIÓN
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ VOLVER A CUENTAS MÉDICAS"):
            st.switch_page("pages/1_Cuentas_Medicas.py")

    with col2:
        if st.button("🏠 VOLVER AL NÚCLEO"):
            st.switch_page("streamlit_app.py")


if __name__ == "__main__":
    main()
