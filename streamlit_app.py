import streamlit as st

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
        top: 0; left: 0; width: 100%; height: 100%;
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
        margin: 15px;
        box-shadow: 0 8px 30px rgba(0, 255, 255, 0.2);
        transition: all 0.3s ease;
        text-align: center;
        min-height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
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
    }
    .card-title {
        font-size: 1.4em;
        font-weight: 700;
        color: #b3ffff;
        text-shadow: 0 0 10px rgba(0,255,255,0.4);
        margin-bottom: 12px;
    }
    .card-desc {
        font-size: 0.95em;
        color: #b8f2ff;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    /* BOTONES PERSONALIZADOS */
    .custom-btn {
        display: inline-block;
        background: rgba(0, 255, 255, 0.15);
        color: #e0ffff;
        border: 1px solid rgba(0, 255, 255, 0.4);
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 14px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        cursor: pointer;
        margin-top: 10px;
    }
    .custom-btn:hover {
        background: rgba(0, 255, 255, 0.3);
        color: #00ffff;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
        transform: translateY(-2px);
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

def main():
    apply_glass_tododrogas_style()

    st.markdown('<h1 class="main-title">INVERSIONES TODODROGAS S.A.S</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Sistema de automatización y control interno</p>', unsafe_allow_html=True)
    st.sidebar.success("Conectado a servidor Streamlit")
    st.sidebar.info("Interfaz visual restringida (solo vista corporativa).")

    # === ÁREA PRINCIPAL ===
    st.markdown("## ÁREA PRINCIPAL: CUENTAS MÉDICAS")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("""
    <h4 class="card-title">GESTIÓN INTEGRAL DE CUENTAS</h4>
    <p class="card-desc">
        Sistema unificado para la validación de archivos, procesamiento masivo de datos,<br>
        generación de reportes automáticos, control de calidad y auditoría.<br><br>
        <strong>Incluye módulos para todas las EPS operativas.</strong>
    </p>
    """, unsafe_allow_html=True)
    st.markdown('<a href="#" class="custom-btn">ACCEDER AL ÁREA</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # === SUBMÓDULOS EPS ===
    st.markdown("## Submódulos de EPS")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h4 class="card-title">SALUD TOTAL</h4>', unsafe_allow_html=True)
        st.markdown("""
        <p class="card-desc">
        • Procesador de actas (OCR)<br>
        • Conversor MANTIS y SISPRO<br>
        • Renombradores CUV y RIPS<br>
        • Reportes automáticos
        </p>
        """, unsafe_allow_html=True)
        st.markdown('<a href="#" class="custom-btn">ACCEDER SALUD TOTAL</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h4 class="card-title">COOSALUD</h4>', unsafe_allow_html=True)
        st.markdown("""
        <p class="card-desc">
        • Conversores MANTIS/SISPRO<br>
        • Renombradores CUV/RIPS<br>
        • Validación estructural<br>
        • Exportación de reportes
        </p>
        """, unsafe_allow_html=True)
        st.markdown('<a href="#" class="custom-btn">ACCEDER COOSALUD</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h4 class="card-title">SAVIA</h4>', unsafe_allow_html=True)
        st.markdown("""
        <p class="card-desc">
        • MANTIS JSON adaptado<br>
        • SISPRO JSON específico<br>
        • CUV/RIPS automatizados<br>
        • Reportes corporativos
        </p>
        """, unsafe_allow_html=True)
        st.markdown('<a href="#" class="custom-btn">ACCEDER SAVIA</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # === COMPLEMENTARIOS ===
    st.markdown("## Sistemas complementarios")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h4 class="card-title">VALIDACIÓN INTELIGENTE</h4>', unsafe_allow_html=True)
        st.markdown("""
        <p class="card-desc">
        • Verificación automática de formatos<br>
        • Corrección estructural<br>
        • Validación de campos RIPS<br>
        • Normalización de datos
        </p>
        """, unsafe_allow_html=True)
        st.markdown('<a href="#" class="custom-btn">ACTIVAR MÓDULO</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h4 class="card-title">CONTROL DE CALIDAD</h4>', unsafe_allow_html=True)
        st.markdown("""
        <p class="card-desc">
        • Monitoreo de errores<br>
        • Logs en tiempo real<br>
        • Indicadores de cumplimiento<br>
        • Auditoría de procesos
        </p>
        """, unsafe_allow_html=True)
        st.markdown('<a href="#" class="custom-btn">ACTIVAR CONTROL</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # === MÉTRICAS ===
    st.markdown("## Métricas del sistema y próximos desarrollos")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h4 class="card-title">Rendimiento actual</h4>', unsafe_allow_html=True)
        st.markdown('<div class="metric-number">99.3%</div>', unsafe_allow_html=True)
        st.markdown("Eficiencia promedio en procesamiento")
        st.markdown('</div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h4 class="card-title">Archivos procesados</h4>', unsafe_allow_html=True)
        st.markdown('<div class="metric-number">12,874</div>', unsafe_allow_html=True)
        st.markdown("Desde la implementación v2.0")
        st.markdown('</div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h4 class="card-title">Próximamente</h4>', unsafe_allow_html=True)
        st.markdown("""
        • Dashboard Ejecutivo<br>
        • IA Predictiva<br>
        • Integración SISPRO Cloud
        """)
        st.markdown('<a href="#" class="custom-btn">MÁS INFORMACIÓN</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<p class="footer">© 2025 Inversiones TODODROGAS S.A.S | Todos los derechos reservados</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
