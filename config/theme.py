import streamlit as st

def configure_modern_theme():
    st.markdown("""
    <style>
    /* Tema principal azul/blanco/gris */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Mejoras generales de Streamlit */
    .stButton>button {
        border-radius: 6px;
        border: 1px solid #0066cc;
        background-color: #0066cc;
        color: white;
        font-weight: 500;
    }
    
    .stButton>button:hover {
        background-color: #0052a3;
        border-color: #0052a3;
    }
    
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 6px;
        border: 1px solid #e1e5e9;
    }
    
    /* Headers consistentes */
    h1, h2, h3 {
        color: #1a1a1a;
    }
    
    /* Ocultar elementos por defecto de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Mejorar los containers */
    .stContainer {
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)
