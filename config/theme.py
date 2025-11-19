import streamlit as st

def configure_modern_theme():
    st.markdown("""
    <style>
        /* Tema personalizado Tododrogas */
        .stApp {
            background: linear-gradient(135deg, #f8faff 0%, #f0f4ff 50%, #ffffff 100%);
            font-family: 'Inter', sans-serif;
        }
        
        /* Personalización de colores primarios */
        .stButton > button {
            background: linear-gradient(135deg, #0066cc, #00a8ff);
            color: white;
            border: none;
            border-radius: 12px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 102, 204, 0.3);
        }
        
        /* Mejorar contraste y legibilidad */
        h1, h2, h3 {
            color: #1a1a1a !important;
            font-weight: 700 !important;
        }
        
        p, div, span {
            color: #333 !important;
        }
        
        /* Sidebar personalizado */
        .css-1d391kg {
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
            border-right: 1px solid rgba(0, 102, 204, 0.1);
        }
        
        /* Ocultar elementos por defecto de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Scrollbar personalizada */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #0066cc, #00a8ff);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #0052a3, #0088cc);
        }
    </style>
    """, unsafe_allow_html=True)
