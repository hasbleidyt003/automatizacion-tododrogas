import streamlit as st
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

# Configurar tema y navbar
configure_modern_theme()
st.set_page_config(page_title="Cuentas Médicas", page_icon="📋", layout="wide")
modern_navbar()

st.title("📋 Cuentas Médicas")
st.markdown("Selecciona la EPS para procesar archivos")

# Navegación a EPS específicas con RUTAS CORREGIDAS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🏥 Coosalud")
    st.markdown("Conversores JSON y Renombradores RIPS/CUV")
    
    # Botones para Coosalud
    if st.button("🔧 Conversor Mantis", use_container_width=True, key="coosalud_mantis"):
        st.switch_page("./1_Cuentas_Medicas/coosalud/Conversor_Mantis.py")
    
    if st.button("🔄 Conversor Sispro", use_container_width=True, key="coosalud_sispro"):
        st.switch_page("./1_Cuentas_Medicas/coosalud/Conversor_sispro.py")
    
    if st.button("🏷️ Renombrador CUV", use_container_width=True, key="coosalud_cuv"):
        st.switch_page("./1_Cuentas_Medicas/coosalud/Renombradores_cuv.py")
    
    if st.button("📋 Renombrador RIPS", use_container_width=True, key="coosalud_rips"):
        st.switch_page("./1_Cuentas_Medicas/coosalud/Renombradores_rips.py")
    
    if st.button("🔗 Renombrador Sispro CUV", use_container_width=True, key="coosalud_sispro_cuv"):
        st.switch_page("./1_Cuentas_Medicas/coosalud/Renombradores_sispro_cuv.py")

with col2:
    st.markdown("### 💊 Savia Salud") 
    st.markdown("Renombradores RIPS y CUV")
    
    # Botones para Savia Salud
    if st.button("📋 Página Principal Savia", use_container_width=True, key="savia_principal"):
        st.switch_page("./1_Cuentas_Medicas/savia_salud/pagina_principal_cm.py")
    
    if st.button("🏷️ Renombrador CUV Savia", use_container_width=True, key="savia_cuv"):
        st.switch_page("./1_Cuentas_Medicas/savia_salud/Renombrador_cuv.py")
    
    if st.button("📋 Renombrador RIPS Savia", use_container_width=True, key="savia_rips"):
        st.switch_page("./1_Cuentas_Medicas/savia_salud/Renombrador_rips.py")

with col3:
    st.markdown("### 🩺 Salud Total")
    st.markdown("Procesador OCR + Renombrado")
    
    # Botones para Salud Total
    if st.button("🔍 Procesador OCR Salud Total", use_container_width=True, key="salud_total_ocr"):
        st.switch_page("./1_Cuentas_Medicas/salud_total/Procesador_Renombrador.py")

# Métricas rápidas
st.markdown("---")
st.subheader("📊 Resumen de Actividad")

col_metrics1, col_metrics2, col_metrics3 = st.columns(3)
with col_metrics1:
    st.metric("Archivos Hoy", "24", "+5")
with col_metrics2:
    st.metric("Tasa Éxito", "98.2%", "+0.5%")
with col_metrics3:
    st.metric("Tiempo Promedio", "45s", "-10s")

# Información adicional
st.markdown("---")
with st.expander("ℹ️ Información de Módulos"):
    st.markdown("""
    ### Módulos Disponibles por EPS:
    
    **🏥 Coosalud:**
    - 🔧 Conversor Mantis: Procesa archivos JSON de Mantis
    - 🔄 Conversor Sispro: Convierte archivos JSON de Sispro
    - 🏷️ Renombrador CUV: Renombra archivos por código único
    - 📋 Renombrador RIPS: Aplica estándar RIPS
    - 🔗 Renombrador Sispro CUV: Combinación Sispro + CUV
    
    **💊 Savia Salud:**
    - 📋 Página Principal: Menú principal de Savia
    - 🏷️ Renombrador CUV: Renombrado por código único
    - 📋 Renombrador RIPS: Aplica estándar RIPS
    
    **🩺 Salud Total:**
    - 🔍 Procesador OCR: OCR + Renombrado automático
    """)

# Footer
st.markdown("---")
st.caption("📋 Plataforma Cuentas Médicas • TodoDrogas • v1.0")
