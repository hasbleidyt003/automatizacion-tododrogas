import streamlit as st
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

# Configurar tema y navbar
configure_modern_theme()
st.set_page_config(page_title="Cuentas Médicas", page_icon="📋", layout="wide")
modern_navbar()

st.title("📋 Cuentas Médicas")
st.markdown("Selecciona la EPS para procesar archivos")

# Navegación a EPS específicas
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🏥 Coosalud")
    st.markdown("Conversores JSON y Renombradores RIPS/CUV")
    if st.button("Acceder a Coosalud", use_container_width=True):
        st.switch_page("pages/1_Cuentas_Medicas/coosalud/Conversor_Mantis.py")

with col2:
    st.markdown("### 💊 Savia Salud") 
    st.markdown("Renombradores RIPS y CUV")
    if st.button("Acceder a Savia", use_container_width=True):
        st.switch_page("pages/1_Cuentas_Medicas/savia_salud/pagina_principal_cm.py")

with col3:
    st.markdown("### 🩺 Salud Total")
    st.markdown("Procesador OCR + Renombrado")
    if st.button("Acceder a Salud Total", use_container_width=True):
        st.switch_page("pages/1_Cuentas_Medicas/salud_total/Procesador_Renombrador.py")

# Métricas rápidas
st.markdown("---")
st.subheader("📊 Resumen de Actividad")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Archivos Hoy", "24", "+5")
with col2:
    st.metric("Tasa Éxito", "98.2%", "+0.5%")
with col3:
    st.metric("Tiempo Promedio", "45s", "-10s")
