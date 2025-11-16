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
        letter-spacing: 1px;
    }

    /* BOTONES MEJORADOS - TAMAÑOS FIJOS Y CENTRADOS */
    .stButton button {
        background: rgba(0, 255, 255, 0.1);
        color: #e0ffff;
        border: 1px solid rgba(0, 255, 255, 0.4);
        border-radius: 10px;
        padding: 12px 0;
        font-size: 15px;
        font-weight: 600;
        width: 200px !important;
        min-width: 200px !important;
        max-width: 200px !important;
        transition: all 0.3s ease;
        margin: 15px auto 0 auto !important;
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
    
    /* CONTENIDO DE TARJETA */
    .card-content {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    /* MÉTRICAS Y ESTADÍSTICAS */
    .metric-number {
        font-size: 2.5em;
        font-weight: bold;
        color: #00ffff;
        text-shadow: 0 0 10px rgba(0,255,255,0.5);
        margin: 10px 0;
    }
    
    .metric-label {
        font-size: 0.9em;
        color: #9eefff;
        margin-bottom: 15px;
    }
    
    /* BOTONES ALINEADOS */
    .button-container {
        margin-top: auto;
        padding-top: 20px;
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
    # SECCIÓN EPS - DE PRIMERAS Y REORGANIZADA
    # =========================================================
    st.markdown("### 🔄 MÓDULOS DE PROCESAMIENTO POR EPS")
    
    # REORGANIZADO: Salud Total a la izquierda
    eps_col1, eps_col2, eps_col3 = st.columns(3)
    
    with eps_col1:  # SALUD TOTAL A LA IZQUIERDA
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-content">', unsafe_allow_html=True)
        st.markdown("#### 💊 SALUD TOTAL")
        st.markdown("""
        - PROCESADOR DE ACTAS - OCR AVANZADO
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        if st.button("ACCEDER SALUD TOTAL", key="salud_total"):
            st.switch_page("pages/4_💊_Salud_Total.py")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with eps_col2:  # COOSALUD EN EL CENTRO
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-content">', unsafe_allow_html=True)
        st.markdown("#### 📋 COOSALUD")
        st.markdown("""
        - CONVERSOR MANTIS JSON
        - CONVERSOR SISPRO JSON  
        - RENOMBRADOR CUV MANTIS
        - RENOMBRADOR RIPS
        - PROCESADOR DE ACTAS - OCR AVANZADO
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        if st.button("ACCEDER COOSALUD", key="coosalud"):
            st.switch_page("pages/2_📋_COOSALUD.py")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with eps_col3:  # SAVIA A LA DERECHA
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-content">', unsafe_allow_html=True)
        st.markdown("#### 🏥 SAVIA")
        st.markdown("""
        - CONVERSOR MANTIS JSON
        - CONVERSOR SISPRO JSON  
        - RENOMBRADOR CUV MANTIS
        - RENOMBRADOR RIPS
        - PROCESADOR DE ACTAS - OCR AVANZADO
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        if st.button("ACCEDER SAVIA", key="savia"):
            st.switch_page("pages/3_🏥_SAVIA.py")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # =========================================================
    # ÁREA PRINCIPAL - CUENTAS MÉDICAS
    # =========================================================
    st.markdown("---")
    st.markdown("### 📊 ÁREA DE CUENTAS MÉDICAS")
    
    area_col1, area_col2 = st.columns([2, 1])
    
    with area_col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-content">', unsafe_allow_html=True)
        st.markdown("#### 🏥 GESTIÓN INTEGRAL DE CUENTAS")
        st.markdown("""
        **Sistema unificado para:**  
        • Validación de archivos RIPS  
        • Procesamiento masivo de datos  
        • Generación de reportes automáticos  
        • Control de calidad y auditoría  
        • Integración con todas las EPS
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        if st.button("ACCEDER ÁREA CUENTAS MÉDICAS", key="cuentas_medicas"):
            st.switch_page("pages/1_🏥_Cuentas_Medicas.py")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with area_col2:
        st.markdown("#### 📈 Resumen de Actividad")
        st.markdown("""
        **Procesos Activos:**  
        ✅ RIPS Automatizado  
        ✅ Validación JSON  
        ✅ Reportes en Tiempo Real  
        
        **Próximamente:**  
        🔄 Análisis Predictivo  
        🔄 Dashboard Ejecutivo
        """)

    # =========================================================
    # MÉTRICAS DEL SISTEMA - ABAJO
    # =========================================================
    st.markdown("---")
    st.markdown("### 📈 MÉTRICAS Y ESTADÍSTICAS DEL SISTEMA")
    
    metric_col1, metric_col2 = st.columns(2)

    with metric_col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-content">', unsafe_allow_html=True)
        st.markdown("#### 📊 ESTADÍSTICAS DE USO")
        st.markdown("---")
        
        # MÉTRICAS SIMULADAS
        col_m1, col_m2 = st.columns(2)
        
        with col_m1:
            st.markdown('<div class="metric-number">1,247</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Archivos Procesados</div>', unsafe_allow_html=True)
            
        with col_m2:
            st.markdown('<div class="metric-number">89</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Sesiones Activas</div>', unsafe_allow_html=True)
        
        st.markdown("**Eficiencia del Sistema:**")
        st.markdown("- 99.2% Tiempo Activo")
        st.markdown("- 15.7s Procesamiento Promedio")
        st.markdown("- 0 Errores Críticos")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        if st.button("VER MÉTRICAS DETALLADAS", key="metricas"):
            st.success("🔍 Mostrando métricas detalladas...")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with metric_col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-content">', unsafe_allow_html=True)
        st.markdown("#### 🔄 ACTIVIDAD RECIENTE")
        st.markdown("---")
        
        st.markdown("**Últimas 24 horas:**")
        st.markdown("• 34 archivos COOSALUD")
        st.markdown("• 28 archivos SAVIA") 
        st.markdown("• 12 archivos Salud Total")
        st.markdown("• 5 reportes generados")
        
        st.markdown("**Tendencias:**")
        st.markdown("📈 +15% procesamiento")
        st.markdown("✅ 100% precisión")
        st.markdown("⚡ 2.3s velocidad avg")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        if st.button("VER ACTIVIDAD COMPLETA", key="actividad"):
            st.success("📋 Mostrando actividad completa...")
        st.markdown('</div>', unsafe_allow_html=True)
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
