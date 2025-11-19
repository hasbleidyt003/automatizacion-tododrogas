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
    
    /* BOTONES PRINCIPALES - MODERNO 3D */
    .stButton > button {
        background: linear-gradient(135deg, #0066cc, #004499);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.8rem 1.8rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        font-family: "Inter", sans-serif;
        box-shadow: 0 6px 20px rgba(0,102,204,0.3);
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
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #0052a3, #003366);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,102,204,0.4);
    }
    
    /* BOTONES SECUNDARIOS */
    .stButton > button[kind="secondary"] {
        background: transparent;
        color: #0066cc;
        border: 2px solid #0066cc;
        box-shadow: 0 4px 15px rgba(0,102,204,0.1);
    }
    
    .stButton > button[kind="secondary"]:hover {
        background: #0066cc;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,102,204,0.3);
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
        border-radius: 10px !important;
        color: #1a1a1a !important;
        padding: 0.8rem 1rem !important;
        font-size: 0.9rem !important;
        transition: all 0.3s ease !important;
        font-family: "Inter", sans-serif !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus,
    .stDateInput > div > div > input:focus {
        border-color: #0066cc !important;
        box-shadow: 0 0 0 2px rgba(0,102,204,0.1) !important;
    }
    
    /* METRICS - MODERNO 3D */
    [data-testid="metric-container"] {
        background: white;
        border: 1px solid #f0f0f0;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border-top: 4px solid #0066cc;
    }
    
    [data-testid="metric-container"]:hover {
        box-shadow: 0 12px 35px rgba(0,0,0,0.12);
        transform: translateY(-3px);
    }
    
    /* EXPANDER - MODERNO */
    .streamlit-expanderHeader {
        background: #f8f9fa !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 10px !important;
        color: #1a1a1a !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        font-family: "Inter", sans-serif !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .streamlit-expanderHeader:hover {
        background: #f0f7ff !important;
        border-color: #0066cc !important;
        box-shadow: 0 4px 15px rgba(0,102,204,0.1);
    }
    
    /* TABS - MODERNO */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: #f8f9fa;
        border-radius: 12px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        border-radius: 8px !important;
        color: #666666 !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        font-family: "Inter", sans-serif !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: #0066cc !important;
        color: white !important;
        box-shadow: 0 2px 8px rgba(0,102,204,0.2);
    }
    
    /* SCROLLBAR MODERNO */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #c1c1c1;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #a8a8a8;
    }
    
    /* ALERTS - MODERNO */
    .stAlert {
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    
    /* PROGRESS BAR */
    .stProgress > div > div {
        background: linear-gradient(90deg, #0066cc, #004499);
        border-radius: 4px;
    }
    
    /* RESPONSIVE */
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        
        .stButton > button {
            width: 100%;
            margin-bottom: 0.5rem;
        }
    }
    
    /* ANIMACIONES SUAVES */
    * {
        transition: all 0.2s ease-in-out;
    }
    </style>
    
    <!-- CARGAR FUENTE INTER -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)
