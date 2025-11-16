import streamlit as st

def configure_futurist_theme():
    st.markdown("""
    <style>
    /* FONDO FUTURISTA CON EFECTO MATRIX */
    .stApp {
        background: 
            radial-gradient(ellipse at 20% 20%, rgba(0, 245, 255, 0.1) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 80%, rgba(138, 43, 226, 0.1) 0%, transparent 50%),
            radial-gradient(ellipse at 40% 40%, rgba(255, 0, 255, 0.05) 0%, transparent 50%),
            linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* OCULTAR ELEMENTOS POR DEFECTO */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* BOTONES DE STREAMLIT FUTURISTAS */
    .stButton > button {
        border-radius: 25px;
        border: 1px solid rgba(0, 245, 255, 0.3);
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.1), rgba(138, 43, 226, 0.1));
        color: #00f5ff;
        font-weight: 600;
        padding: 0.7rem 1.5rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.2), rgba(138, 43, 226, 0.2));
        border-color: rgba(0, 245, 255, 0.6);
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.4);
        transform: translateY(-2px);
        color: #ffffff;
    }
    
    /* INPUTS FUTURISTAS */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stDateInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 245, 255, 0.3) !important;
        border-radius: 15px !important;
        color: #e0e0e0 !important;
        padding: 0.8rem 1rem !important;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus,
    .stDateInput > div > div > input:focus {
        border-color: #00f5ff !important;
        box-shadow: 0 0 15px rgba(0, 245, 255, 0.3) !important;
        background: rgba(0, 245, 255, 0.1) !important;
    }
    
    /* FILE UPLOADER FUTURISTA */
    .stFileUploader > div {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        border: 2px dashed rgba(0, 245, 255, 0.3) !important;
        border-radius: 20px !important;
        padding: 2rem !important;
        transition: all 0.3s ease;
    }
    
    .stFileUploader > div:hover {
        border-color: #00f5ff !important;
        background: rgba(0, 245, 255, 0.1) !important;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.2);
    }
    
    /* EXPANDER FUTURISTA */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 245, 255, 0.2) !important;
        border-radius: 15px !important;
        color: #00f5ff !important;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(0, 245, 255, 0.1) !important;
        border-color: #00f5ff !important;
        box-shadow: 0 0 15px rgba(0, 245, 255, 0.3);
    }
    
    /* TABS FUTURISTAS */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        border-radius: 15px !important;
        color: #e0e0e0 !important;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00f5ff, #8a2be2) !important;
        color: white !important;
        box-shadow: 0 0 15px rgba(0, 245, 255, 0.5);
    }
    
    /* SCROLLBAR PERSONALIZADO */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #00f5ff, #8a2be2);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #8a2be2, #ff00ff);
    }
    
    /* CONTAINERS PRINCIPALES */
    .main .block-container {
        padding-top: 0;
        max-width: 100%;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    
    /* EFECTO DE PARTICULAS (SIMULADO) */
    body::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(0, 245, 255, 0.03) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(138, 43, 226, 0.03) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
    }
    </style>
    """, unsafe_allow_html=True)
