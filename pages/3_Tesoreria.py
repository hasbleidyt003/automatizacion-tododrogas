import streamlit as st
import pandas as pd
import io
from datetime import datetime

# Configuración
st.set_page_config(page_title="Tesorería - TodoDrogas", page_icon="🏦", layout="wide")

# Navbar
from components.navbar import modern_navbar
modern_navbar()

# Título
st.markdown("""
<div style='text-align: center; margin-bottom: 3rem;'>
    <h1 style='color: #1a1a1a; font-size: 2.5rem; margin-bottom: 1rem;'>🏦 Tesorería - Estados de Cuenta Proveedores</h1>
    <p style='color: #666; font-size: 1.2rem;'>Procesamiento de estados de cuenta de acreedores y proveedores</p>
</div>
""", unsafe_allow_html=True)

# Sección principal
st.markdown("### 📤 Procesar Estados de Cuenta de Proveedores")

uploaded_files = st.file_uploader(
    "Subir estados de cuenta de proveedores (archivos XLS/XLSX)",
    type=['xlsx', 'xls'],
    accept_multiple_files=True,
    help="Solo archivos Excel (.xls, .xlsx) de estados de cuenta de proveedores"
)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} archivo(s) XLS cargado(s)")
    
    # Mostrar archivos cargados
    with st.expander("📁 Archivos Cargados", expanded=True):
        for i, file in enumerate(uploaded_files):
            st.write(f"{i+1}. **{file.name}** - {file.size / 1024:.1f} KB")
    
    # Procesamiento
    if st.button("🚀 Procesar Estados de Proveedores", type="primary", use_container_width=True):
        with st.spinner("Procesando archivos XLS de proveedores..."):
            # Procesar cada archivo
            resultados = []
            total_pendiente = 0
            
            for file in uploaded_files:
                try:
                    # Leer archivo Excel
                    df = pd.read_excel(file)
                    
                    # Simular análisis de cuentas por pagar
                    saldo_pendiente = df.select_dtypes(include=['number']).sum().sum() if not df.empty else 0
                    total_pendiente += saldo_pendiente
                    
                    resultados.append({
                        'Proveedor': file.name.replace('.xlsx', '').replace('.xls', ''),
                        'Archivo': file.name,
                        'Registros': len(df),
                        'Saldo Pendiente': f"${saldo_pendiente:,.0f}",
                        'Estado': '✅ Procesado'
                    })
                    
                except Exception as e:
                    resultados.append({
                        'Proveedor': 'N/A',
                        'Archivo': file.name,
                        'Registros': 0,
                        'Saldo Pendiente': '$0',
                        'Estado': f'❌ Error: {str(e)}'
                    })
            
            # Mostrar resultados
            st.success("✅ Procesamiento completado!")
            resultados_df = pd.DataFrame(resultados)
            st.dataframe(resultados_df, use_container_width=True)
            
            # Resumen general
            st.metric("Total Pendiente por Pagar", f"${total_pendiente:,.0f}")
            
            # Botón de descarga consolidado
            if st.button("📥 Descargar Reporte Proveedores", use_container_width=True):
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    resultados_df.to_excel(writer, sheet_name='Resumen Proveedores', index=False)
                    
                    # Agregar hojas por cada proveedor
                    for file in uploaded_files:
                        try:
                            df = pd.read_excel(file)
                            sheet_name = file.name.replace('.xlsx', '').replace('.xls', '')[:31]
                            df.to_excel(writer, sheet_name=sheet_name, index=False)
                        except:
                            pass
                
                st.download_button(
                    label="⏬ Descargar Excel Consolidado",
                    data=output.getvalue(),
                    file_name=f"tesoreria_proveedores_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx",
                    mime="application/vnd.ms-excel"
                )

# Información de ayuda
st.markdown("---")
st.markdown("""
**📝 Notas:**
- Solo se aceptan archivos en formato Excel (.xls, .xlsx)
- Los archivos deben contener estados de cuenta de proveedores/acreedores
- El sistema calculará automáticamente los saldos pendientes de pago
""")
