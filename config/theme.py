import streamlit as st

def configure_modern_theme():
    st.markdown("""
    <style>
    /* Tema principal profesional */
    :root {
        --primary-color: #0066cc;
        --secondary-color: #00a86b;
        --accent-color: #ff6b35;
    }
    
    .stApp {
        background-color: #fafbfc;
    }
    
    /* Mejoras generales de Streamlit */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 8px;
        border: 1px solid #e9ecef;
    }
    
    /* Ocultar elementos por defecto de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
