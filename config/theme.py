import streamlit as st

def configure_modern_theme():
    st.markdown("""
    <style>
        /* Variables CSS para colores azules */
        :root {
            --primary-color: #0066cc;
            --primary-dark: #004499;
            --primary-light: #0088ff;
            --accent-color: #0066cc;
            --accent-dark: #004499;
            --accent-rgb: 0, 102, 204;
        }
        
        /* Estilos base de Streamlit */
        .stApp {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        }
        
        /* Headers */
        h1, h2, h3, h4, h5, h6 {
            color: #1a1a1a !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        h1 {
            font-weight: 800 !important;
            background: linear-gradient(135deg, #1a1a1a, #0066cc, #004499) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
        }
        
        h2 {
            font-weight: 700 !important;
            color: #1a1a1a !important;
        }
        
        h3 {
            font-weight: 600 !important;
            color: #1a1a1a !important;
        }
        
        /* Texto general */
        p, div, span {
            font-family: 'Inter', sans-serif !important;
            color: #666666 !important;
        }
        
        /* Botones de Streamlit */
        .stButton > button {
            background: linear-gradient(135deg, #0066cc, #004499) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.5rem 1rem !important;
            font-weight: 600 !important;
            font-family: 'Inter', sans-serif !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(0, 102, 204, 0.3) !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(0, 102, 204, 0.4) !important;
            background: linear-gradient(135deg, #0052a3, #003366) !important;
        }
        
        /* Inputs y selects */
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input,
        .stSelectbox > div > div > div {
            border: 1px solid #e0e0e0 !important;
            border-radius: 8px !important;
            padding: 0.5rem !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        .stTextInput > div > div > input:focus,
        .stNumberInput > div > div > input:focus,
        .stSelectbox > div > div > div:focus {
            border-color: #0066cc !important;
            box-shadow: 0 0 0 2px rgba(0, 102, 204, 0.1) !important;
        }
        
        /* Sidebar */
        .css-1d391kg {
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
            border-right: 1px solid rgba(0, 102, 204, 0.1) !important;
        }
        
        /* Progress bars */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #0066cc, #004499) !important;
        }
        
        /* Success messages */
        .stAlert > div {
            background: rgba(0, 102, 204, 0.1) !important;
            border: 1px solid rgba(0, 102, 204, 0.3) !important;
            border-radius: 8px !important;
            color: #0066cc !important;
        }
        
        /* Info messages */
        .stInfo > div {
            background: rgba(0, 102, 204, 0.1) !important;
            border: 1px solid rgba(0, 102, 204, 0.3) !important;
            border-radius: 8px !important;
            color: #0066cc !important;
        }
        
        /* Error messages */
        .stError > div {
            background: rgba(220, 53, 69, 0.1) !important;
            border: 1px solid rgba(220, 53, 69, 0.3) !important;
            border-radius: 8px !important;
            color: #dc3545 !important;
        }
        
        /* Warning messages */
        .stWarning > div {
            background: rgba(255, 193, 7, 0.1) !important;
            border: 1px solid rgba(255, 193, 7, 0.3) !important;
            border-radius: 8px !important;
            color: #856404 !important;
        }
        
        /* Dataframes y tablas */
        .dataframe {
            border-radius: 8px !important;
            overflow: hidden !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1) !important;
        }
        
        .dataframe th {
            background: linear-gradient(135deg, #0066cc, #004499) !important;
            color: white !important;
            font-weight: 600 !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        .dataframe td {
            font-family: 'Inter', sans-serif !important;
            border-bottom: 1px solid #e0e0e0 !important;
        }
        
        /* Expanders */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, #f8f9fa, #e9ecef) !important;
            border-radius: 8px !important;
            border: 1px solid rgba(0, 102, 204, 0.1) !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
        }
        
        .streamlit-expanderHeader:hover {
            background: linear-gradient(135deg, #e9ecef, #dee2e6) !important;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px !important;
            background-color: #f8f9fa !important;
            border-radius: 8px !important;
            padding: 4px !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px !important;
            background-color: transparent !important;
            border-radius: 6px !important;
            padding: 0 20px !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 500 !important;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #0066cc, #004499) !important;
            color: white !important;
        }
        
        /* Scrollbar personalizada */
        ::-webkit-scrollbar {
            width: 6px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 3px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #0066cc, #004499);
            border-radius: 3px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #0052a3, #003366);
        }
        
        /* Loading spinner */
        .stSpinner > div {
            border-color: #0066cc transparent transparent transparent !important;
        }
        
        /* Metric cards */
        [data-testid="metric-container"] {
            background: white !important;
            border-radius: 12px !important;
            padding: 1rem !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1) !important;
            border: 1px solid rgba(0, 102, 204, 0.1) !important;
        }
        
        [data-testid="metric-container"]::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #0066cc, #004499);
            border-radius: 12px 12px 0 0;
        }
        
        /* Remove Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
    </style>
    """, unsafe_allow_html=True)
