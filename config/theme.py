import streamlit as st

def configure_minimalist_theme():
    st.markdown("""
    <style>
    /* TEMA PRINCIPAL MINIMALISTA */
    .stApp {
        background: #ffffff;
        color: #1a1a1a;
        font-family: 'Arial', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* OCULTAR ELEMENTOS POR DEFECTO */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* BOTONES PRINCIPALES - MINIMALISTA */
    .stButton > button {
        background: #0066cc;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.8rem 1.8rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        font-family: "Arial", sans-serif;
    }
    
    .stButton > button:hover {
        background: #0052a3;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,102,204,0.3);
    }
    
    /* CONTAINER PRINCIPAL */
    .main .block-container {
        padding-top: 0;
        max-width: 1200px;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    
    /* INPUTS Y SELECTORES - MINIMALISTA */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stDateInput > div > div > input {
        background: #ffffff !important;
        border: 2px solid #e0e0e0 !important;
        border-radius: 8px !important;
        color: #1a1a1a !important;
        padding: 0.8rem 1rem !important;
        font-size: 0.9rem !important;
        transition: all 0.3s ease !important;
        font-family: "Arial", sans-serif !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus,
    .stDateInput > div > div > input:focus {
        border-color: #0066cc !important;
        box-shadow: 0 0 0 2px rgba(0,102,204,0.1) !important;
    }
    
    /* FILE UPLOADER - MINIMALISTA */
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
    }
    
    /* EXPANDER - MINIMALISTA */
    .streamlit-expanderHeader {
        background: #f8f9fa !important;
        border: 2px solid #e0e0e0 !important;
        border-radius: 8px !important;
        color: #1a1a1a !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        font-family: "Arial", sans-serif !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: #f0f7ff !important;
        border-color: #0066cc !important;
    }
    
    /* TABS - MINIMALISTA */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: #f8f9fa;
        border-radius: 12px;
        padding: 0.5rem;
        border: 1px solid #e0e0e0;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        border-radius: 8px !important;
        color: #666666 !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        font-family: "Arial", sans-serif !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: #0066cc !important;
        color: white !important;
    }
    
    /* METRICS - MINIMALISTA */
    [data-testid="metric-container"] {
        background: #f8f9fa;
        border: 2px solid #e0e0e0;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
    }
    
    /* SCROLLBAR MINIMALISTA */
    ::-webkit-scrollbar {
        width: 6px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 3px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #c1c1c1;
        border-radius: 3px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #a8a8a8;
    }
    
    /* TABLAS - MINIMALISTA */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        border: 2px solid #e0e0e0;
    }
    
    /* SPINNER */
    .stSpinner > div {
        border-color: #0066cc transparent transparent transparent;
    }
    
    /* SUCCESS/ERROR MESSAGES - MINIMALISTA */
    .stAlert {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
    }
    
    /* PROGRESS BAR */
    .stProgress > div > div {
        background-color: #0066cc;
    }
    
    /* CHECKBOX Y RADIO */
    .stCheckbox > label, .stRadio > label {
        font-family: "Arial", sans-serif;
    }
    
    /* RESPONSIVE */
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        
        .stButton > button {
            width: 100%;
        }
    }
    
    /* ESTILOS ESPECÍFICOS PARA EL DISEÑO MINIMALISTA */
    .minimalist-section {
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .minimalist-section:hover {
        border-color: #0066cc;
        box-shadow: 0 4px 12px rgba(0,102,204,0.1);
    }
    </style>
    """, unsafe_allow_html=True)
