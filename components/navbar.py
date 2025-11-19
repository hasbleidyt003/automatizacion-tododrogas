import streamlit as st

def modern_navbar():
    # Usar columns nativas para el navbar
    nav_col1, nav_col2, nav_col3 = st.columns([2, 3, 1])
    
    with nav_col1:
        st.write("### ⚡ TodoDrogas Automation")
    
    with nav_col2:
        # Menú de navegación horizontal
        nav_cols = st.columns(5)
        with nav_cols[0]:
            if st.button("Inicio", use_container_width=True):
                st.switch_page("streamlit_app.py")
        with nav_cols[1]:
            if st.button("Cuentas Médicas", use_container_width=True):
                st.switch_page("pages/1_Cuentas_Medicas.py")
        with nav_cols[2]:
            if st.button("Cartera", use_container_width=True):
                st.switch_page("pages/2_Cartera.py")
        with nav_cols[3]:
            if st.button("Tesorería", use_container_width=True):
                st.switch_page("pages/3_Tesoreria.py")
        with nav_cols[4]:
            if st.button("Métricas", use_container_width=True):
                st.switch_page("pages/4_Metricas.py")
    
    with nav_col3:
        st.success("🟢 En línea")
