import streamlit as st

def modern_navbar():
    # Navbar con la misma estructura cool pero en nativo
    with st.container():
        nav_col1, nav_col2 = st.columns([3, 1])
        
        with nav_col1:
            st.markdown("### ⚡ TODO DROGAS AUTOMATION")
            
        with nav_col2:
            # Estadísticas del navbar
            stat_col1, stat_col2 = st.columns(2)
            with stat_col1:
                st.success("SISTEMA ACTIVO")
            with stat_col2:
                st.write("v2.1.0")
