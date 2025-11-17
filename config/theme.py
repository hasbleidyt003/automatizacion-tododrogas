import streamlit as st

def configure_minimalist_theme():
    st.markdown("""
    <style>
    .stApp {
        background: #ffffff;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stButton > button {
        background: #0066cc;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.7rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: #0052a3;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,102,204,0.3);
    }
    
    .main .block-container {
        padding-top: 0;
        max-width: 100%;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #0066cc;
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True)
