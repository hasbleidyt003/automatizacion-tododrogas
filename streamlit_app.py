import streamlit as st
import base64

def apply_cyberpunk_style():
    st.markdown("""
    <style>
    /* FONDO CYBERPUNK CON EFECTO MATRIX */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #001a00 50%, #003300 100%);
        position: relative;
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
            radial-gradient(circle at 20% 80%, rgba(0, 255, 0, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(0, 255, 100, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(0, 200, 0, 0.05) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
    }
    
    /* EFECTO GRID TECNOLÓGICO */
    .cyber-grid {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(0, 255, 0, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 255, 0, 0.1) 1px, transparent 1px);
        background-size: 50px 50px;
        pointer-events: none;
        z-index: -1;
    }
    
    /* TÍTULOS NEÓN VERDES */
    .cyber-title {
        font-family: 'Courier New', monospace;
        font-size: 4em;
        font-weight: bold;
        text-align: center;
        color: #00ff00;
        text-shadow: 
            0 0 10px #00ff00,
            0 0 20px #00ff00,
            0 0 30px #00ff00,
            0 0 40px #00ff00;
        margin-bottom: 0;
        letter-spacing: 3px;
        text-transform: uppercase;
    }
    
    .cyber-subtitle {
        font-family: 'Courier New', monospace;
        text-align: center;
        color: #00cc00;
        font-size: 1.3em;
        text-shadow: 0 0 10px #00cc00;
        margin-bottom: 40px;
        letter-spacing: 2px;
    }
    
    /* TARJETAS CYBERPUNK */
    .cyber-card {
        background: rgba(0, 20, 0, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid #00ff00;
        border-radius: 0;
        padding: 25px;
        margin: 15px 0;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
        box-shadow: 
            0 0 20px rgba(0, 255, 0, 0.3),
            inset 0 0 20px rgba(0, 255, 0, 0.1);
    }
    
    .cyber-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 255, 0, 0.2), transparent);
        transition: left 0.5s ease;
    }
    
    .cyber-card:hover::before {
        left: 100%;
    }
    
    .cyber-card:hover {
        transform: translateY(-5px);
        box-shadow: 
            0 0 30px rgba(0, 255, 0, 0.5),
            inset 0 0 30px rgba(0, 255, 0, 0.2);
        border: 1px solid #00ff88;
    }
    
    /* BOTONES CYBERPUNK */
    .stButton button {
        background: transparent;
        color: #00ff00;
        border: 2px solid #00ff00;
        border-radius: 0;
        padding: 15px 30px;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 16px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        width: 100%;
        margin: 5px 0;
    }
    
    .stButton button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 255, 0, 0.3), transparent);
        transition: left 0.5s ease;
    }
    
    .stButton button:hover::before {
        left: 100%;
    }
    
    .stButton button:hover {
        background: rgba(0, 255, 0, 0.1);
        color: #00ff88;
        border: 2px solid #00ff88;
        box-shadow: 
            0 0 20px rgba(0, 255, 0, 0.5),
            inset 0 0 20px rgba(0, 255, 0, 0.1);
        transform: scale(1.05);
    }
    
    /* BARRAS DE PROGRESO CYBERPUNK */
    .stProgress > div > div {
        background: linear-gradient(90deg, #00ff00, #00ff88);
        border-radius: 0;
    }
    
    /* TEXTO GENERAL */
    .main .block-container {
        color: #00cc00;
        font-family: 'Courier New', monospace;
    }
    
    /* SCROLLBAR PERSONALIZADO */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(0, 20, 0, 0.5);
    }
    
    ::-webkit-scrollbar-thumb {
        background: #00ff00;
        border-radius: 0;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #00ff88;
    }
    </style>
    
    <div class="cyber-grid"></div>
    """, unsafe_allow_html=True)

def main():
    apply_cyberpunk_style()
    
    # TÍTULO PRINCIPAL CON EFECTO MATRIX
    st.markdown('<h1 class="cyber-title">TODODROGAS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="cyber-subtitle">INVERSIONES TODO DROGAS S.A.S</p>', unsafe_allow_html=True)
    st.markdown('<p class="cyber-subtitle">[ SISTEMA CYBER-AUTOMATION v2.0 ]</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ÁREAS PRINCIPALES
    st.markdown("### [>> SELECCIÓN DE MÓDULO <<]")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        st.markdown("### ▸ CUENTAS MÉDICAS")
        st.markdown("`[PROCESAMIENTO_JSON_RIPS]`")
        st.markdown("```\nEPS: COOSALUD | SAVIA | SALUD_TOTAL\nFUNCION: Validación y conversión\n```")
        if st.button(">> INICIAR SISTEMA <<", key="cuentas_medicas"):
            st.success("Módulo activado - Redirigiendo...")
            # Aquí puedes agregar la funcionalidad específica
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        st.markdown("### ▸ INVENTARIOS")
        st.markdown("`[GESTIÓN_STOCK]`")
        st.markdown("```\nSTATUS: EN DESARROLLO\nFUNCION: Control automático\n```")
        st.button(">> SISTEMA BLOQUEADO <<", key="inventarios", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        st.markdown("### ▸ REPORTES IA")
        st.markdown("`[ANÁLISIS_PREDICTIVO]`")
        st.markdown("```\nSTATUS: EN DESARROLLO\nFUNCION: Analytics avanzado\n```")
        st.button(">> SISTEMA BLOQUEADO <<", key="ia", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # SECCIÓN DE ESTADÍSTICAS
    st.markdown("---")
    st.markdown("### [>> MÉTRICAS DEL SISTEMA <<]")
    
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        st.markdown("**PROCESAMIENTO**")
        st.markdown("```\n📊 95% EFICIENCIA\n```")
        st.progress(0.95)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        st.markdown("**VELOCIDAD**")
        st.markdown("```\n⚡ 2.4s PROMEDIO\n```")
        st.progress(0.88)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with metric_col3:
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        st.markdown("**UPTIME**")
        st.markdown("```\n🟢 99.9% ACTIVO\n```")
        st.progress(0.999)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with metric_col4:
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        st.markdown("**SEGURIDAD**")
        st.markdown("```\n🔒 100% PROTEGIDO\n```")
        st.progress(1.0)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # STATUS DEL SISTEMA
    st.markdown("---")
    st.markdown("### [>> STATUS DEL SISTEMA <<]")
    
    status_col1, status_col2, status_col3 = st.columns(3)
    
    with status_col1:
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        st.markdown("**▸ NÚCLEO PRINCIPAL**")
        st.markdown("```diff\n+ SISTEMA OPERATIVO\n```")
        st.markdown("**▸ VERSIÓN**")
        st.markdown("```\nv2.0.1 CYBER-EDITION\n```")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with status_col2:
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        st.markdown("**▸ MÓDULOS ACTIVOS**")
        st.markdown("```diff\n+ CUENTAS_MÉDICAS: ONLINE\n- INVENTARIOS: OFFLINE\n- REPORTES_IA: OFFLINE\n```")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with status_col3:
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        st.markdown("**▸ CONEXIONES**")
        st.markdown("```diff\n+ BD PRINCIPAL: CONECTADO\n+ API EXTERNA: STANDBY\n+ CLOUD SYNC: ACTIVO\n```")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # FOOTER
    st.markdown("---")
    st.markdown(
        '<div style="text-align: center; color: #00cc00; font-family: Courier New;">'
        '**TODODROGAS AUTOMATION SYSTEM** • **v2.0 CYBER-EDITION** • **© 2024 INVERSIONES TODO DROGAS S.A.S**'
        '</div>', 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
