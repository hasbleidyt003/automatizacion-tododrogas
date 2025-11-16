# STREAMLIT PRINCIPAL SIN IMÁGENES, CON FONDO ESTILO GOOGLE COLAB FUTURISTA

import streamlit as st

# ------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ------------------------------
st.set_page_config(page_title="Sistema de Automatización - Tododrogas", layout="wide")

# ------------------------------
# ESTILO FUTURISTA / TIPO GOOGLE COLAB
# ------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0f0f 0%, #1c1c1c 40%, #2a2a2a 100%);
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
    }

    /* EFECTOS LUMINOSOS FUTURISTAS */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        background: radial-gradient(circle at 20% 30%, rgba(0, 255, 255, 0.07), transparent 60%),
                    radial-gradient(circle at 80% 70%, rgba(0, 255, 180, 0.06), transparent 60%);
        z-index: -1;
    }

    .main-title {
        text-align: center;
        color: #00eaff;
        font-size: 3.2em;
        font-weight: 700;
        text-shadow: 0 0 25px rgba(0,255,255,0.7);
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #e0ffff;
        font-size: 1.3em;
        margin-bottom: 40px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 20px;
        border-radius: 18px;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 18px rgba(0,255,255,0.15);
        color: #d6ffff;
        margin-bottom: 25px;
    }

    .metric-number {
        font-size: 2.5em;
        font-weight: 900;
        color: #00ffff;
        text-shadow: 0 0 15px rgba(0,255,255,0.6);
    }

    .footer {
        text-align: center;
        font-size: 0.9em;
        margin-top: 40px;
        color: #b8ffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------
# TÍTULOS PRINCIPALES
# ------------------------------
st.markdown('<h1 class="main-title">SISTEMA DE AUTOMATIZACIÓN</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">El futuro es la tecnología, y hoy se convierte en nuestra mejor herramienta. Este sistema centraliza todas las automatizaciones por área, optimizando procesos y mejorando resultados.</p>', unsafe_allow_html=True)

# ------------------------------
# SECCIÓN CUENTAS MÉDICAS
# ------------------------------
st.markdown("## 🩺 CUENTAS MÉDICAS")
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown(
    """
    **Automatizaciones disponibles:**

    • Procesador de actas (OCR)  
    • Conversor MANTIS y SISPRO  
    • Renombradores CUV y RIPS  
    • Reportes automáticos para SAVIA, COOSALUD y SALUD TOTAL
    """
)
st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# SECCIÓN CARTERA
# ------------------------------
st.markdown("## 💰 CARTERA")
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown(
    """
    **Automatizaciones desarrolladas:**

    • Informes automáticos de cartera  
    • Estados de cuenta automatizados  
    • Estructura automática de informes de pago  
    • Reporte semanal automatizado
    """
)
st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# SECCIÓN TESORERÍA
# ------------------------------
st.markdown("## 🏦 TESORERÍA")
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown(
    """
    **Automatización disponible:**

    • Generación automatizada de estados de cuenta
    """
)
st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# MÉTRICAS Y PRÓXIMOS DESARROLLOS
# ------------------------------
st.markdown("## 📈 Métricas y próximos desarrollos")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("#### ⚡ Rendimiento actual")
    st.markdown('<div class="metric-number">99.3%</div>', unsafe_allow_html=True)
    st.write("Eficiencia en procesamiento")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("#### 📂 Archivos procesados")
    st.markdown('<div class="metric-number">12,874</div>', unsafe_allow_html=True)
    st.write("Desde implementación v2.0")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("#### 🚀 Próximamente")
    st.write("• Dashboard Ejecutivo  ")
    st.write("• IA Predictiva  ")
    st.write("• Integración SISPRO Cloud")
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# CONTACTO
# ------------------------------
st.markdown('---')
st.markdown(
    '<p class="footer">© 2025 Inversiones TODODROGAS S.A.S | Contacto: soporte@tododrogas.com</p>',
    unsafe_allow_html=True
)
