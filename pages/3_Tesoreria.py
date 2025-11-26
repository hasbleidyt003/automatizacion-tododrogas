import streamlit as st
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

configure_modern_theme()
st.set_page_config(page_title="Tesorería", page_icon="🏦", layout="wide")
modern_navbar()

st.title("🏦 Módulo de Tesorería")
st.warning("🚧 **Módulo en desarrollo** - Próximamente disponible")

st.markdown("""
### Funcionalidades en desarrollo:
- 💳 Control automatizado de estados bancarios
- 📊 Flujo financiero en tiempo real
- 🔒 Conciliaciones con máxima seguridad
- 📈 Análisis de liquidez
""")

# Placeholder para futuras funciones
with st.expander("🔮 Vista Previa - Funcionalidades Planificadas"):
    st.write("""
    **Control de Estados Bancarios:**
    - Procesamiento automático de extractos
    - Conciliación inteligente
    - Detección de discrepancias
    
    **Flujo Financiero:**
    - Dashboard en tiempo real
    - Proyecciones de caja
    - Alertas de liquidez
    """)
