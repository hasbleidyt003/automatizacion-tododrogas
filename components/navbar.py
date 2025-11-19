import streamlit as st

def modern_navbar():
    # Usar columns nativas de Streamlit para el navbar
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.write("### ⚡ TodoDrogas Automation")
    
    with col2:
        st.write("**Sistema Centralizado**")
    
    with col3:
        st.write("🟢 **En Línea**")
