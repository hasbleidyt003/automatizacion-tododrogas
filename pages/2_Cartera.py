import streamlit as st
import pandas as pd
import io
from datetime import datetime

# Configuración
st.set_page_config(page_title="Cartera", page_icon="💰", layout="wide")

# Navbar
from components.navbar import modern_navbar
modern_navbar()

# Título
st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h1 style='color: #1a1a1a; font-size: 2.5rem; margin-bottom: 1rem;'>💰 Cartera - Automatización Estados de Cuenta </h1>
</div>
""", unsafe_allow_html=True)

# Sección principal
st.markdown("### 📤 Procesar archivos")

uploaded_files = st.file_uploader(
    "Subir estados de cuenta de clientes (archivos XLS/XLSX)",
    type=['xlsx', 'xls'],
    accept_multiple_files=True,
    help="Solo archivos Excel (.xls, .xlsx) de estados de cuenta de clientes"
)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} archivo(s) XLS cargado(s)")
    
    # Mostrar archivos cargados
    with st.expander("📁 Archivos Cargados", expanded=True):
        for i, file in enumerate(uploaded_files):
            st.write(f"{i+1}. **{file.name}** - {file.size / 1024:.1f} KB")
    
    # Procesamiento
    if st.button("🚀 Procesar Estados de Cuenta", type="primary", use_container_width=True):
        with st.spinner("Procesando archivos XLS de clientes..."):
            # Procesar cada archivo
            resultados = []
            
            for file in uploaded_files:
                try:
                    # Leer archivo Excel
                    df = pd.read_excel(file)
                    
                    # Simular análisis básico
                    saldo_total = df.select_dtypes(include=['number']).sum().sum() if not df.empty else 0
                    
                    resultados.append({
                        'Archivo': file.name,
                        'Registros': len(df),
                        'Columnas': len(df.columns),
                        'Saldo Detectado': f"${saldo_total:,.0f}",
                        'Estado': '✅ Procesado'
                    })
                    
                except Exception as e:
                    resultados.append({
                        'Archivo': file.name,
                        'Registros': 0,
                        'Columnas': 0,
                        'Saldo Detectado': '$0',
                        'Estado': f'❌ Error: {str(e)}'
                    })
            
            # Mostrar resultados
            st.success("✅ Procesamiento completado!")
            resultados_df = pd.DataFrame(resultados)
            st.dataframe(resultados_df, use_container_width=True)
            
            # Botón de descarga consolidado
            if st.button("📥 Descargar Reporte Consolidado", use_container_width=True):
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    resultados_df.to_excel(writer, sheet_name='Resumen', index=False)
                    
                    # Agregar hojas por cada archivo procesado
                    for file in uploaded_files:
                        try:
                            df = pd.read_excel(file)
                            sheet_name = file.name[:31]  # Limitar nombre de hoja
                            df.to_excel(writer, sheet_name=sheet_name, index=False)
                        except:
                            pass
                
                st.download_button(
                    label="⏬ Descargar Excel Consolidado",
                    data=output.getvalue(),
                    file_name=f"cartera_consolidado_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx",
                    mime="application/vnd.ms-excel"
                )

# Información de ayuda
st.markdown("---")
st.markdown("""
**📝 Notas:**
- Solo se aceptan archivos en formato Excel (.xls, .xlsx).
- Los archivos deben contener estados de cuenta de clientes.
- El sistema procesará y estructurará automáticamente las cuentas por cobrar.
""")
