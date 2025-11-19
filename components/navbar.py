import streamlit as st

def modern_navbar():
    st.markdown("""
    <style>
    .navbar {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem 2rem;
        border-radius: 0 0 12px 12px;
        margin-bottom: 2rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .navbar-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
    }
    .navbar-brand {
        font-size: 1.3rem;
        font-weight: 700;
    }
    .navbar-user {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    </style>
    
    <div class="navbar">
        <div class="navbar-content">
            <div class="navbar-brand">⚡ TodoDrogas Automation</div>
            <div class="navbar-user">Sistema Centralizado</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
