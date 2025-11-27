import streamlit as st
import json
import os
import re
import tempfile
import shutil
from pathlib import Path
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

# Configurar tema y navbar
configure_modern_theme()
st.set_page_config(
    page_title="Conversor + Renombrador - Coosalud", 
    page_icon="🔄", 
    layout="wide"
)
modern_navbar()

st.title("🔄 Conversor + Renombrador - Coosalud")
st.markdown("Procesa archivos JSON de Mantis y renombra archivos con patrón NE###### **al mismo tiempo**")

# Función de procesamiento JSON CORREGIDA
def procesar_archivos_json(directorio):
    archivos_procesados = []
    errores = []
    
    try:
        archivos_json = [archivo for archivo in os.listdir(directorio) if archivo.lower().endswith('.json')]
        
        for nombre_archivo in archivos_json:
            try:
                ruta_archivo = os.path.join(directorio, nombre_archivo)
                with open(ruta_archivo, 'r', encoding='utf-8') as file:
                    datos_originales = json.load(file)
                
                # PRESERVAR DATOS ORIGINALES - NO REEMPLAZAR CON null
                fecha_original = datos_originales.get('fechaRadicacion') or datos_originales.get('FechaRadicacion')
                result_state = datos_originales.get('resultState') or datos_originales.get('ResultState')
                proceso_id = datos_originales.get('procesoId') or datos_originales.get('ProcesoId')
                num_factura = datos_originales.get('numFactura') or datos_originales.get('NumFactura')
                codigo_cuv = datos_originales.get('codigoUnicoValidacion') or datos_originales.get('CodigoUnicoValidacion')
                ruta_archivos = datos_originales.get('rutaArchivos') or datos_originales.get('RutaArchivos')
                
                nuevo_nombre_archivo = nombre_archivo
                
                # Renombrar archivos con fecha 0000-00-00
                if fecha_original == "0000-00-00T00:00:00":
                    nombre_base, extension = os.path.splitext(nombre_archivo)
                    nuevo_nombre_archivo = f"{nombre_base}-SIN FECHA{extension}"
                    os.rename(ruta_archivo, os.path.join(directorio, nuevo_nombre_archivo))
                    ruta_archivo = os.path.join(directorio, nuevo_nombre_archivo)
                
                # Formatear fecha válida (solo si existe y necesita corrección)
                fecha_procesada = fecha_original
                if fecha_original and fecha_original != "0000-00-00T00:00:00" and '+' in fecha_original:
                    fecha_procesada = fecha_original.split('+')[0]
                
                # Buscar número de factura en el nombre del archivo si no está en los datos
                if not num_factura:
                    patron_factura = r'(NE\d+)'
                    coincidencia_factura = re.search(patron_factura, nombre_archivo)
                    if coincidencia_factura:
                        num_factura = coincidencia_factura.group(1)
                
                # Estructura final - PRESERVAR DATOS EXISTENTES
                resultado = {
                    "resultState": result_state,
                    "procesoId": proceso_id,
                    "numFactura": num_factura,
                    "codigoUnicoValidacion": codigo_cuv,
                    "fechaRadicacion": fecha_procesada,
                    "rutaArchivos": ruta_archivos,
                    "resultadosValidacion": datos_originales.get('resultadosValidacion', [])
                }
                
                # Solo procesar si hay datos diferentes o estructura que corregir
                necesita_procesamiento = (
                    fecha_original and '+' in fecha_original and fecha_original != "0000-00-00T00:00:00" or
                    fecha_original == "0000-00-00T00:00:00" or
                    'resultadosValidacion' not in datos_originales or
                    datos_originales.get('resultadosValidacion') is None
                )
                
                if necesita_procesamiento:
                    # Guardar archivo procesado
                    with open(ruta_archivo, 'w', encoding='utf-8') as file:
                        json_str = json.dumps(resultado, indent=2, ensure_ascii=False)
                        json_str = json_str.replace('"resultadosValidacion": []', '"resultadosValidacion":[]')
                        file.write(json_str)
                    
                    estado = "✅ Procesado y Corregido"
                else:
                    estado = "✅ Ya tiene formato correcto"
                
                archivos_procesados.append({
                    'nombre': nuevo_nombre_archivo,
                    'estado': estado,
                    'fecha': fecha_original if fecha_original else 'No encontrada',
                    'factura': num_factura if num_factura else 'No encontrada',
                    'resultState': "Sí" if result_state else "No",
                    'procesoId': "Sí" if proceso_id else "No",
                    'codigoCUV': "Sí" if codigo_cuv else "No"
                })
                
            except Exception as e:
                errores.append({
                    'nombre': nombre_archivo,
                    'error': str(e)
                })
        
        return archivos_procesados, errores
        
    except Exception as e:
        errores.append({'nombre': 'Sistema', 'error': f"Error general: {str(e)}"})
        return [], errores

# Función de renombrado CUV (Renombrador Coosalud)
def renombrar_archivos_cuv(directorio):
    resultados = []
    contador = 0
    
    try:
        for archivo in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, archivo)
            
            # Verificar si es un archivo (no carpeta) y no es JSON (para evitar conflictos)
            if os.path.isfile(ruta_completa) and not archivo.lower().endswith('.json'):
                # Buscar el patrón NE seguido de números en el nombre del archivo
                patron = r'(NE\d+)'
                coincidencia = re.search(patron, archivo)
                
                if coincidencia:
                    numero_factura = coincidencia.group(1)
                    nombre_base, extension = os.path.splitext(archivo)
                    
                    # Crear el nuevo nombre: CUV_NE651.ext (FORMATO COOSALUD)
                    nuevo_nombre = f"CUV_{numero_factura}{extension}"
                    nueva_ruta = os.path.join(directorio, nuevo_nombre)
                    
                    # Renombrar el archivo
                    try:
                        os.rename(ruta_completa, nueva_ruta)
                        resultados.append({
                            'original': archivo,
                            'nuevo': nuevo_nombre,
                            'estado': '✅ Renombrado',
                            'tipo': 'success',
                            'numero_factura': numero_factura
                        })
                        contador += 1
                    except Exception as e:
                        resultados.append({
                            'original': archivo,
                            'nuevo': nuevo_nombre,
                            'estado': f'❌ Error: {str(e)}',
                            'tipo': 'error',
                            'numero_factura': numero_factura
                        })
                else:
                    # Solo mostrar info si no es un archivo JSON (para evitar duplicados)
                    if not archivo.lower().endswith('.json'):
                        resultados.append({
                            'original': archivo,
                            'nuevo': archivo,
                            'estado': 'ℹ No coincide con patrón NE######',
                            'tipo': 'info',
                            'numero_factura': 'N/A'
                        })
        
        return resultados, contador
        
    except Exception as e:
        st.error(f"Error general: {str(e)}")
        return [], 0

# Función principal que procesa TODO
def procesar_todo(directorio):
    """Procesa tanto archivos JSON como archivos para renombrar"""
    # Procesar archivos JSON
    json_procesados, json_errores = procesar_archivos_json(directorio)
    
    # Procesar archivos para renombrar
    renombrados, contador_renombrados = renombrar_archivos_cuv(directorio)
    
    return {
        'json_procesados': json_procesados,
        'json_errores': json_errores,
        'archivos_renombrados': renombrados,
        'total_renombrados': contador_renombrados
    }

# INTERFAZ PRINCIPAL
st.header("📤 Subida de Archivos")

# Subida de archivos múltiples (todos los tipos)
uploaded_files = st.file_uploader(
    "Selecciona archivos para procesar (JSON de Mantis y archivos con patrón NE######)",
    accept_multiple_files=True,
    help="Puedes seleccionar archivos JSON y otros archivos con formato NE651.pdf, NE999999.xlsx, etc.",
    type=['json', 'pdf', 'xlsx', 'xls', 'txt', 'doc', 'docx', 'jpg', 'png', 'jpeg']
)

# Información adicional
st.info("""
**🔄 Funcionalidad Combinada - Coosalud:**

**Para archivos JSON:**
- ✅ **PRESERVA** datos existentes (no los reemplaza con null)
- ✅ Corrige formato de fechas con zona horaria
- ✅ Renombra archivos con fechas inválidas (0000-00-00)
- ✅ Busca número de factura en nombre del archivo
- ✅ Mantiene estructura `resultadosValidacion:[]` sin espacios

**Para archivos con patrón NE######:**
- ✅ Convierte `NE651.pdf` → `CUV_NE651.pdf` (Formato Coosalud)
- ✅ Detecta automáticamente patrones NE######
""")

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} archivo(s) listo(s) para procesar")
    
    # Mostrar archivos seleccionados
    with st.expander("📋 Archivos Seleccionados", expanded=True):
        for i, file in enumerate(uploaded_files):
            # Verificar tipo de archivo
            if file.name.lower().endswith('.json'):
                # Leer contenido JSON para previsualización
                try:
                    contenido = json.loads(file.getvalue().decode('utf-8'))
                    num_factura = contenido.get('numFactura') or contenido.get('NumFactura') or 'No encontrado'
                    tipo = f"📊 JSON (Factura: {num_factura})"
                except:
                    tipo = "📊 JSON (Error lectura)"
            else:
                patron = r'(NE\d+)'
                coincidencia = re.search(patron, file.name)
                if coincidencia:
                    tipo = f"🔢 Archivo para Renombrar ({coincidencia.group(1)})"
                else:
                    tipo = "📄 Otro archivo"
            
            st.write(f"{i+1}. {file.name} - {tipo}")
    
    # Botón de procesamiento COMBINADO
    if st.button("🚀 Procesar Todo", type="primary", use_container_width=True):
        with st.spinner("Procesando archivos JSON y renombrando archivos..."):
            # Crear directorio temporal
            with tempfile.TemporaryDirectory() as temp_dir:
                # Guardar archivos subidos en directorio temporal
                for uploaded_file in uploaded_files:
                    temp_path = os.path.join(temp_dir, uploaded_file.name)
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getvalue())
                
                # Procesar TODO
                resultados = procesar_todo(temp_dir)
                
                # MOSTRAR RESULTADOS COMBINADOS
                st.markdown("---")
                st.header("📊 Resultados del Procesamiento Combinado")
                
                # Estadísticas generales
                total_json = len(resultados['json_procesados']) + len(resultados['json_errores'])
                total_archivos = len(uploaded_files)
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Archivos", total_archivos)
                with col2:
                    st.metric("JSON Procesados", len(resultados['json_procesados']))
                with col3:
                    st.metric("Archivos Renombrados", resultados['total_renombrados'])
                with col4:
                    tasa_exito = ((len(resultados['json_procesados']) + resultados['total_renombrados']) / total_archivos * 100) if total_archivos > 0 else 0
                    st.metric("Tasa Éxito", f"{tasa_exito:.1f}%")
                
                # RESULTADOS DETALLADOS - JSON
                if resultados['json_procesados'] or resultados['json_errores']:
                    st.subheader("📊 Resultados Conversor JSON")
                    
                    # Mostrar tabla detallada de JSON procesados
                    if resultados['json_procesados']:
                        st.markdown("#### ✅ JSON Procesados Exitosamente")
                        
                        # Crear DataFrame para mejor visualización
                        df_data = []
                        for archivo in resultados['json_procesados']:
                            df_data.append({
                                'Archivo': archivo['nombre'],
                                'Estado': archivo['estado'],
                                'Factura': archivo['factura'],
                                'Fecha': archivo['fecha'],
                                'resultState': archivo['resultState'],
                                'procesoId': archivo['procesoId'],
                                'codigoCUV': archivo['codigoCUV']
                            })
                        
                        df = pd.DataFrame(df_data)
                        st.dataframe(df, use_container_width=True)
                    
                    if resultados['json_errores']:
                        st.markdown("#### ❌ Errores en JSON")
                        for error in resultados['json_errores']:
                            st.error(f"**{error['nombre']}**: {error['error']}")
                
                # RESULTADOS DETALLADOS - RENOMBRADO
                if resultados['archivos_renombrados']:
                    st.subheader("🔢 Resultados Renombrado CUV - Coosalud")
                    
                    # Separar por tipo de resultado
                    renombrados = [r for r in resultados['archivos_renombrados'] if r['tipo'] == 'success']
                    errores_renombre = [r for r in resultados['archivos_renombrados'] if r['tipo'] == 'error']
                    info_renombre = [r for r in resultados['archivos_renombrados'] if r['tipo'] == 'info']
                    
                    if renombrados:
                        st.markdown("#### ✅ Archivos Renombrados Exitosamente")
                        for resultado in renombrados:
                            st.success(f"**{resultado['original']}** → **{resultado['nuevo']}**")
                            st.caption(f"Número de factura: {resultado['numero_factura']} - Formato Coosalud")
                    
                    if errores_renombre:
                        st.markdown("#### ❌ Errores en Renombrado")
                        for resultado in errores_renombre:
                            st.error(f"**{resultado['original']}** → {resultado['estado']}")
                    
                    if info_renombre:
                        st.markdown("#### ℹ️ Archivos No Procesados")
                        for resultado in info_renombre:
                            st.info(f"**{resultado['original']}** → {resultado['estado']}")
                
                # PREPARAR DESCARGA COMBINADA
                st.markdown("---")
                st.subheader("📥 Descargar Todos los Archivos Procesados")
                
                archivos_para_descargar = (
                    len(resultados['json_procesados']) > 0 or 
                    resultados['total_renombrados'] > 0
                )
                
                if archivos_para_descargar:
                    # Crear ZIP con todos los archivos procesados
                    zip_path = os.path.join(temp_dir, "archivos_procesados_coosalud.zip")
                    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', temp_dir)
                    
                    # Leer el ZIP para descarga
                    with open(zip_path, "rb") as f:
                        zip_data = f.read()
                    
                    # Botón de descarga ZIP completo
                    st.download_button(
                        label="📦 Descargar TODOS los Archivos Procesados (ZIP)",
                        data=zip_data,
                        file_name="archivos_procesados_coosalud.zip",
                        mime="application/zip",
                        use_container_width=True
                    )
                    
                    # Descargas individuales por categoría
                    st.markdown("**Descargas Individuales por Categoría:**")
                    
                    # Archivos JSON procesados
                    if resultados['json_procesados']:
                        st.markdown("**📊 Archivos JSON Procesados:**")
                        cols_json = st.columns(3)
                        for i, archivo in enumerate(resultados['json_procesados']):
                            with cols_json[i % 3]:
                                file_path = os.path.join(temp_dir, archivo['nombre'])
                                if os.path.exists(file_path):
                                    with open(file_path, "rb") as f:
                                        file_data = f.read()
                                    
                                    st.download_button(
                                        label=f"📄 {archivo['nombre'][:15]}...",
                                        data=file_data,
                                        file_name=archivo['nombre'],
                                        mime="application/json",
                                        key=f"json_{i}"
                                    )
                    
                    # Archivos renombrados
                    renombrados_exitosos = [r for r in resultados['archivos_renombrados'] if r['tipo'] == 'success']
                    if renombrados_exitosos:
                        st.markdown("**🔢 Archivos Renombrados (Formato Coosalud):**")
                        cols_ren = st.columns(3)
                        for i, archivo in enumerate(renombrados_exitosos):
                            with cols_ren[i % 3]:
                                file_path = os.path.join(temp_dir, archivo['nuevo'])
                                if os.path.exists(file_path):
                                    with open(file_path, "rb") as f:
                                        file_data = f.read()
                                    
                                    st.download_button(
                                        label=f"📄 {archivo['nuevo'][:15]}...",
                                        data=file_data,
                                        file_name=archivo['nuevo'],
                                        mime="application/octet-stream",
                                        key=f"ren_{i}"
                                    )
                else:
                    st.warning("No hay archivos procesados para descargar")

else:
    st.info("👆 Por favor, selecciona al menos un archivo para procesar")

# INSTRUCCIONES
with st.expander("📖 Instrucciones de Uso"):
    st.markdown("""
    ### Cómo usar el Conversor + Renombrador Combinado - Coosalud:
    
    1. **Selecciona archivos**: Haz clic en 'Browse files' o arrastra los archivos
    2. **Mezcla tipos**: Puedes seleccionar archivos JSON y archivos con patrón NE###### juntos
    3. **Procesa**: Haz clic en 'Procesar Todo' - se ejecutarán ambas operaciones
    4. **Descarga**: Obtén todos los archivos procesados en un ZIP o individualmente
    
    ### Transformaciones aplicadas:
    
    **Para archivos JSON:**
    - **PRESERVA** todos los datos existentes
    - Solo corrige: formato de fechas con zona horaria y estructura `resultadosValidacion`
    - Renombra archivos con fecha inválida (0000-00-00)
    
    **Para archivos con patrón NE###### (Formato Coosalud):**
    - `NE651.pdf` → `CUV_NE651.pdf` (CUV al inicio)
    - `NE999999.xlsx` → `CUV_NE999999.xlsx`
    
    ### Características:
    - ✅ **NO REEMPLAZA** datos existentes con null
    - ✅ Extracción robusta de datos JSON
    - ✅ Procesamiento simultáneo de JSON y renombrado
    """)

# FOOTER
st.markdown("---")
st.caption("🔄 Conversor + Renombrador - Coosalud • v4.0 • Preserva Datos Existentes")
