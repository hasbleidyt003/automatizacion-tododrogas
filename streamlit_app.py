import streamlit as st
import base64

def apply_glass_tododrogas_style():
    st.markdown("""
    <style>
    /* ====== ESTILO GLASSMORPHISM TODODROGAS ====== */

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

    .stApp::after {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image:
            linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
        background-size: 60px 60px;
        z-index: -1;
        pointer-events: none;
    }

    .glass-title {
        font-size: 4em;
        font-weight: 700;
        text-align: center;
        color: #e0f7fa;
        text-shadow: 0 0 25px rgba(0,255,255,0.6);
        letter-spacing: 2px;
        margin-bottom: 0;
        text-transform: uppercase;
    }

    .glass-subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #a7f0ff;
        margin-bottom: 40px;
        letter-spacing: 1.5px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
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

    .stButton button {
        background: rgba(0, 255, 255, 0.1);
        color: #e0ffff;
        border: 1px solid rgba(0, 255, 255, 0.3);
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        width: 100%;
    }

    .stButton button:hover {
        background: rgba(0, 255, 255, 0.2);
        border-color: rgba(0, 255, 255, 0.5);
        color: #00ffff;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
        transform: scale(1.05);
    }

    code, pre {
        background: rgba(0, 40, 60, 0.3);
        color: #80ffff;
        border-radius: 8px;
        padding: 8px;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    apply_glass_tododrogas_style()
    
    st.markdown('<h1 class="glass-title">TODODROGAS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="glass-subtitle">INVERSIONES TODO DROGAS S.A.S</p>', unsafe_allow_html=True)
    st.markdown('<p class="glass-subtitle">[ SISTEMA GLASS-AUTOMATION v2.0 ]</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 💎 SELECCIONA UN MÓDULO")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### ▸ CUENTAS MÉDICAS")
        st.markdown("`[PROCESAMIENTO_JSON_RIPS]`")
        st.markdown("```\nEPS: COOSALUD | SAVIA | SALUD_TOTAL\nFUNCION: Validación y conversión\n```")
        if st.button("INICIAR SISTEMA", key="cuentas_medicas"):
            st.switch_page("pages/1_Cuentas_Medicas.py")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### ▸ INVENTARIOS")
        st.markdown("`[GESTIÓN_STOCK]`")
        st.markdown("```\nSTATUS: EN DESARROLLO\nFUNCION: Control automático\n```")
        st.button("SISTEMA BLOQUEADO", key="inventarios", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### ▸ REPORTES IA")
        st.markdown("`[ANÁLISIS_PREDICTIVO]`")
        st.markdown("```\nSTATUS: EN DESARROLLO\nFUNCION: Analytics avanzado\n```")
        st.button("SISTEMA BLOQUEADO", key="ia", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ⚙️ STATUS DEL SISTEMA")

    status_col1, status_col2, status_col3 = st.columns(3)
    with status_col1:
        st.markdown("**▸ NÚCLEO PRINCIPAL**")
        st.markdown("```diff\n+ SISTEMA OPERATIVO\n```")

    with status_col2:
        st.markdown("**▸ MÓDULOS ACTIVOS**")
        st.markdown("```diff\n+ CUENTAS_MÉDICAS: ONLINE\n```")

    with status_col3:
        st.markdown("**▸ CONEXIÓN BD**")
        st.markdown("```diff\n+ CONECTADO\n```")


if __name__ == "__main__":
    main()
