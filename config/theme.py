import streamlit as st

def configure_modern_theme():
    # Configuración minimalista usando solo CSS esencial
    st.markdown("""
    <style>
    .main .block-container {
        padding-top: 1rem;
    }
    
    /* Ocultar elementos por defecto */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
