import streamlit as st

def configure_modern_theme():
    st.markdown("""
    <style>
    /* TEMA PRINCIPAL MODERNO */
    .stApp {
        background: #ffffff;
        color: #1a1a1a;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* OCULTAR ELEMENTOS POR DEFECTO */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* BOTONES PRINCIPALES - MODERNO */
    .stButton > button {
        background: #0066cc;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.8rem 1.8rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        font-family: "Inter", sans-serif;
        box-shadow: 0 2px 8px rgba(0,102,204,0.2);
    }
    
    .stButton > button:hover {
        background: #0052a3;
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0,102,204,0.3);
    }
    
    /* CONTAINER PRINCIPAL */
    .main .block-container {
        padding-top: 0;
        max-width: 1200px;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    
    /* INPUTS Y SELECTORES - MODERNO */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stDateInput > div > div > input {
        background: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 8px !important;
        color: #1a1a1a !important;
        padding: 0.8rem 1rem !important;
        font-size: 0.9rem !important;
        transition: all 0.3s ease !important;
        font-family: "Inter", sans-serif !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus,
    .stDateInput > div > div > input:focus {
        border-color: #0066cc !important;
        box-shadow: 0 0 0 2px rgba(0,102,204,0.1) !important;
    }
    </style>
    
    <!-- CARGAR FUENTE INTER -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)
