import streamlit as st

def configure_modern_theme():
    st.markdown("""
    <style>
        /* Tema personalizado - FONDO ORIGINAL */
        .stApp {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        }
        
        /* Personalización de componentes */
        .stButton > button {
            background: linear-gradient(135deg, #0066cc, #004499);
            color: white;
            border: none;
            border-radius: 10px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 102, 204, 0.3);
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #1a1a1a !important;
            font-weight: 700 !important;
        }
        
        p, div, span {
            color: #333 !important;
        }
        
        /* Ocultar elementos por defecto de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
