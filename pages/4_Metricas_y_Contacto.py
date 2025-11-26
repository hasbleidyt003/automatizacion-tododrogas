import streamlit as st
from components.navbar import modern_navbar
from config.theme import configure_modern_theme
import pandas as pd
import plotly.express as px

configure_modern_theme()
st.set_page_config(page_title="Métricas y Contacto", page_icon="📊", layout="wide")
modern_navbar()

st.title("📊 Métricas y Contacto")

# Pestañas para métricas y contacto
tab1, tab2 = st.tabs(["📈 Métricas del Sistema", "📞 Contacto y Soporte"])

with tab1:
    st.header("Dashboard Ejecutivo")
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Automatizaciones", "1,247", "+128")
    with col2:
        st.metric("Tiempo Ahorrado", "342h", "+45h")
    with col3:
        st.metric("Eficiencia", "68%", "+12%")
    with col4:
        st.metric("Usuarios Activos", "23", "+5")
    
    # Gráfico simulado
    st.subheader("Actividad Mensual")
    data = pd.DataFrame({
        'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May'],
        'Archivos': [120, 150, 180, 210, 240],
        'Usuarios': [15, 18, 20, 22, 23]
    })
    
    fig = px.line(data, x='Mes', y=['Archivos', 'Usuarios'], 
                  title='Crecimiento Mensual', markers=True)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("📞 Soporte Técnico")
    
    st.info("¿Necesitas ayuda? Contáctanos para soporte técnico")
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre completo")
            email = st.text_input("Email")
        with col2:
            departamento = st.selectbox("Departamento", 
                                      ["Cuentas Médicas", "Cartera", "Tesorería", "General"])
            urgencia = st.selectbox("Nivel de urgencia", 
                                  ["Baja", "Media", "Alta", "Crítica"])
        
        descripcion = st.text_area("Describe el problema o solicitud")
        
        if st.form_submit_button("📨 Enviar Solicitud"):
            st.success("✅ Solicitud enviada. Te contactaremos en 24 horas.")
    
    st.markdown("---")
    st.subheader("📞 Contacto Directo")
    st.write("**Email:** soporte@tododrogas.com")
    st.write("**Teléfono:** +57 1 234 5678")
    st.write("**Horario:** Lunes a Viernes 8:00 AM - 6:00 PM")
