import streamlit as st

def configure_modern_theme():
    st.markdown("""
    <style>
    /* Tema minimalista */
    .stApp {
        background-color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    /* Mejoras de componentes Streamlit */
    .stButton>button {
        border-radius: 6px;
        border: 1px solid #e1e5e9;
        background: white;
        color: #1a1a1a;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        border-color: #0066cc;
        color: #0066cc;
    }
    
    /* Ocultar elementos por defecto */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
