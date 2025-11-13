import streamlit as st

# =========================================================
# 💊 ESTILO GLASSMORPHISM CORPORATIVO TODODROGAS
# =========================================================
def apply_glass_tododrogas_style():
    st.markdown("""
    <style>
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
    }

    .stButton button {
        background: rgba(0, 255, 255, 0.1);
        color: #e0ffff;
        border: 1px solid rgba(0, 255, 255, 0.4);
        border-radius: 10px;
        padding: 8px 0;
        font-size: 14px;
        font-weight: 600;
        width: 160px !important;
        transition: all 0.3s ease;
        margin: 0 auto !important;
        display: block !important;
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

    .metric-number {
        font-size: 2.2em;
        font-weight: bold;
        color: #00ffff;
        text-shadow: 0 0 10px rgba(0,255,255,0.5);
    }
    </style>
    """, unsafe_allow_html=True)


# =========================================================
# 🧠 CONTENIDO PRINCIPAL
# =========================================================
def main():
    apply_glass_tododrogas_style()

    # ENCABEZADO CORPORATIVO
    st.markdown('<h1 class="main-title">💊 INVERSIONES TODODROGAS S.A.S</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Sistema de automatización y control interno</p>', unsafe_allow_html=True)

    st.sidebar.success("✅ Conectado a servidor Streamlit")
    st.sidebar.info("Interfaz visual restringida (solo vista corporativa).")

    # =========================================================
    # ÁREA PRINCIPAL - CUENTAS MÉDICAS (SIN BOTÓN)
    # =========================================================
    st.markdown("## 🩺 CUENTAS MÉDICAS")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("""
    st.markdown('<div class="GESTION INTEGRAL DE CUENTAS">', unsafe_allow_html=True)
    Sistema unificado para la validación de archivos, procesamiento masivo de datos,
    generación de reportes automáticos, control de calidad y auditoría.
    
    **Incluye módulos para todas las EPS operativas.**
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # =========================================================
    # SUBMÓDULOS EPS (SOLO BOTONES “ACCEDER …”)
    # =========================================================
    st.markdown("## ⚙️ Submódulos de EPS")

    eps_col1, eps_col2, eps_col3 = st.columns(3)

    with eps_col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 💊 SALUD TOTAL")
        st.markdown("""
        • Procesador de actas (OCR)  
        • Conversor MANTIS y SISPRO  
        • Renombradores CUV y RIPS  
        • Reportes automáticos  
        """)
        st.button("ACCEDER SALUD TOTAL", key="salud_total")
        st.markdown('</div>', unsafe_allow_html=True)

    with eps_col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 📋 COOSALUD")
        st.markdown("""
        • Conversores MANTIS/SISPRO  
        • Renombradores CUV/RIPS  
        • Validación estructural  
        • Exportación de reportes  
        """)
        st.button("ACCEDER COOSALUD", key="coosalud")
        st.markdown('</div>', unsafe_allow_html=True)

    with eps_col3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 🏥 SAVIA")
        st.markdown("""
        • MANTIS JSON adaptado  
        • SISPRO JSON específico  
        • CUV/RIPS automatizados  
        • Reportes corporativos  
        """)
        st.button("ACCEDER SAVIA", key="savia")
        st.markdown('</div>', unsafe_allow_html=True)

    # =========================================================
    # SISTEMAS COMPLEMENTARIOS (SOLO “ACTIVAR …”)
    # =========================================================
    st.markdown("## 🧩 Sistemas complementarios")

    sys_col1, sys_col2 = st.columns(2)

    with sys_col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 🧠 VALIDACIÓN INTELIGENTE")
        st.markdown("""
        • Verificación automática de formatos  
        • Corrección estructural  
        • Validación de campos RIPS  
        • Normalización de datos  
        """)
        st.button("ACTIVAR MÓDULO", key="validacion")
        st.markdown('</div>', unsafe_allow_html=True)

    with sys_col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 🔒 CONTROL DE CALIDAD")
        st.markdown("""
        • Monitoreo de errores  
        • Logs en tiempo real  
        • Indicadores de cumplimiento  
        • Auditoría de procesos  
        """)
        st.button("ACTIVAR CONTROL", key="control_calidad")
        st.markdown('</div>', unsafe_allow_html=True)

    # =========================================================
    # MÉTRICAS Y FUTURO (SOLO “MÁS INFORMACIÓN”)
    # =========================================================
    st.markdown("## 📈 Métricas del sistema y próximos desarrollos")

    met1, met2, met3 = st.columns(3)

    with met1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### ⚡ Rendimiento actual")
        st.markdown('<div class="metric-number">99.3%</div>', unsafe_allow_html=True)
        st.markdown("Eficiencia promedio en procesamiento")
        st.markdown('</div>', unsafe_allow_html=True)

    with met2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 📂 Archivos procesados")
        st.markdown('<div class="metric-number">12,874</div>', unsafe_allow_html=True)
        st.markdown("Desde la implementación v2.0")
        st.markdown('</div>', unsafe_allow_html=True)

    with met3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 🚀 Próximamente")
        st.markdown("""
        • 📊 Dashboard Ejecutivo  
        • 🤖 IA Predictiva  
        • 🌐 Integración SISPRO Cloud  
        """)
        st.button("MÁS INFORMACIÓN", key="proximamente")
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
