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
    
    /* FILE UPLOADER - MODERNO */
    .stFileUploader > div {
        background: #f8f9fa !important;
        border: 2px dashed #e0e0e0 !important;
        border-radius: 12px !important;
        padding: 2rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stFileUploader > div:hover {
        border-color: #0066cc !important;
        background: #f0f7ff !important;
        box-shadow: 0 4px 12px rgba(0,102,204,0.1);
    }
    
    /* EXPANDER - MODERNO */
    .streamlit-expanderHeader {
        background: #f8f9fa !important;
        border: 1px solid #e0e0e0 !important;
        border-radius: 8px !important;
        color: #1a1a1a !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        font-family: "Inter", sans-serif !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: #f0f7ff !important;
        border-color: #0066cc !important;
        box-shadow: 0 2px 8px rgba(0,102,204,0.1);
    }
    
    /* TABS - MODERNO */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: #f8f9fa;
        border-radius: 10px;
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
    
    /* METRICS - MODERNO */
    [data-testid="metric-container"] {
        background: white;
        border: 1px solid #f0f0f0;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    
    [data-testid="metric-container"]:hover {
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        transform: translateY(-2px);
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
    
    /* TABLAS - MODERNO */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border: 1px solid #f0f0f0;
    }
    
    /* SPINNER */
    .stSpinner > div {
        border-color: #0066cc transparent transparent transparent;
    }
    
    /* SUCCESS/ERROR MESSAGES - MODERNO */
    .stAlert {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    /* PROGRESS BAR */
    .stProgress > div > div {
        background-color: #0066cc;
        border-radius: 4px;
    }
    
    /* CHECKBOX Y RADIO */
    .stCheckbox > label, .stRadio > label {
        font-family: "Inter", sans-serif;
        font-weight: 500;
    }
    
    /* SLIDER */
    .stSlider > div > div > div {
        background: #0066cc;
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
    
    /* ESTILOS ESPECÍFICOS PARA EL DISEÑO MODERNO */
    .modern-card {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
    }
    
    .modern-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    
    /* ANIMACIONES SUAVES */
    * {
        transition: all 0.2s ease-in-out;
    }
    </style>
    
    <!-- CARGAR FUENTE INTER -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)
