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

# Función de procesamiento JSON (Conversor Mantis)
def procesar_archivos_json(directorio):
    archivos_procesados = []
    errores = []
    
    try:
        archivos_json = [archivo for archivo in os.listdir(directorio) if archivo.lower().endswith('.json')]
        
        for nombre_archivo in archivos_json:
            try:
                ruta_archivo = os.path.join(directorio, nombre_archivo)
                with open(ruta_archivo, 'r', encoding='utf-8') as file:
                    datos = json.load(file)
                
                fecha_original = datos.get('fechaRadicacion') or datos.get('FechaRadicacion')
                nuevo_nombre_archivo = nombre_archivo
                
                # Renombrar archivos con fecha 0000-00-00
                if fecha_original == "0000-00-00T00:00:00":
                    nombre_base, extension = os.path.splitext(nombre_archivo)
                    nuevo_nombre_archivo = f"{nombre_base}-SIN FECHA{extension}"
                    os.rename(ruta_archivo, os.path.join(directorio, nuevo_nombre_archivo))
                
                # Formatear fecha válida
                if fecha_original and fecha_original != "0000-00-00T00:00:00" and '+' in fecha_original:
                    fecha_procesada = fecha_original.split('+')[0]
                    if 'fechaRadicacion' in datos:
                        datos['fechaRadicacion'] = fecha_procesada
                    if 'FechaRadicacion' in datos:
                        datos['FechaRadicacion'] = fecha_procesada
                
                # Estructura final
                resultado = {
                    "resultState": datos.get('resultState', datos.get('ResultState')),
                    "procesoId": datos.get('procesoId', datos.get('ProcesoId')),
                    "numFactura": datos.get('numFactura', datos.get('NumFactura')),
                    "codigoUnicoValidacion": datos.get('codigoUnicoValidacion', datos.get('CodigoUnicoValidacion')),
                    "fechaRadicacion": datos.get('fechaRadicacion', datos.get('FechaRadicacion')),
                    "rutaArchivos": datos.get('rutaArchivos', datos.get('RutaArchivos')),
                    "resultadosValidacion":[]
                }
                
                # Guardar archivo procesado
                ruta_final = os.path.join(directorio, nuevo_nombre_archivo)
                with open(ruta_final, 'w', encoding='utf-8') as file:
                    json_str = json.dumps(resultado, indent=2, ensure_ascii=False)
                    json_str = json_str.replace('"resultadosValidacion": []', '"resultadosValidacion":[]')
                    file.write(json_str)
                
                archivos_procesados.append({
                    'nombre': nuevo_nombre_archivo,
                    'estado': '✅ Procesado',
                    'fecha': fecha_original if fecha_original else 'No encontrada'
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
                    
                    # Crear el nuevo nombre: CUV_NE651.ext
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
**🔄 Funcionalidad Combinada:**

**Para archivos JSON:**
- ✅ Corrige formato de fechas
- ✅ Renombra archivos con fechas inválidas
- ✅ Estructura JSON según estándar Coosalud

**Para archivos con patrón NE######:**
- ✅ Convierte `NE651.pdf` → `CUV_NE651.pdf`
- ✅ Detecta automáticamente patrones NE######
- ✅ Procesamiento masivo simultáneo
""")

# Mostrar ejemplos de patrones
with st.expander("🔍 Ejemplos de Archivos Aceptados"):
    st.markdown("""
    **Archivos JSON (Conversor Mantis):**
    - `radicacion_12345.json` → Procesa y corrige estructura JSON
    - `factura_NE651.json` → Corrige fechas y estructura
    
    **Archivos para Renombrar (Patrón NE######):**
    - `NE651.pdf` → `CUV_NE651.pdf`
    - `NE999999.xlsx` → `CUV_NE999999.xlsx`
    - `documento_NE8888.txt` → `CUV_NE8888.txt`
    
    **Puedes mezclar ambos tipos en una sola operación**
    """)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} archivo(s) listo(s) para procesar")
    
    # Mostrar archivos seleccionados
    with st.expander("📋 Archivos Seleccionados", expanded=True):
        for i, file in enumerate(uploaded_files):
            # Verificar tipo de archivo
            if file.name.lower().endswith('.json'):
                tipo = "📊 JSON (Conversor Mantis)"
            else:
                patron = r'(NE\d+)'
                coincidencia = re.search(patron, file.name)
                if coincidencia:
                    tipo = "🔢 Archivo para Renombrar"
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
                    
                    col_json1, col_json2 = st.columns(2)
                    
                    with col_json1:
                        st.markdown("#### ✅ JSON Procesados Exitosamente")
                        if resultados['json_procesados']:
                            for archivo in resultados['json_procesados']:
                                st.success(f"**{archivo['nombre']}**")
                                st.caption(f"Fecha: {archivo['fecha']}")
                        else:
                            st.info("No se procesaron archivos JSON")
                    
                    with col_json2:
                        st.markdown("#### ❌ Errores en JSON")
                        if resultados['json_errores']:
                            for error in resultados['json_errores']:
                                st.error(f"**{error['nombre']}**: {error['error']}")
                        else:
                            st.success("No hubo errores en JSON")
                
                # RESULTADOS DETALLADOS - RENOMBRADO
                if resultados['archivos_renombrados']:
                    st.subheader("🔢 Resultados Renombrado CUV")
                    
                    # Separar por tipo de resultado
                    renombrados = [r for r in resultados['archivos_renombrados'] if r['tipo'] == 'success']
                    errores_renombre = [r for r in resultados['archivos_renombrados'] if r['tipo'] == 'error']
                    info_renombre = [r for r in resultados['archivos_renombrados'] if r['tipo'] == 'info']
                    
                    if renombrados:
                        st.markdown("#### ✅ Archivos Renombrados Exitosamente")
                        for resultado in renombrados:
                            st.success(f"**{resultado['original']}** → **{resultado['nuevo']}**")
                            st.caption(f"Número de factura: {resultado['numero_factura']}")
                    
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
                    zip_path = os.path.join(temp_dir, "archivos_procesados_completos.zip")
                    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', temp_dir)
                    
                    # Leer el ZIP para descarga
                    with open(zip_path, "rb") as f:
                        zip_data = f.read()
                    
                    # Botón de descarga ZIP completo
                    st.download_button(
                        label="📦 Descargar TODOS los Archivos Procesados (ZIP)",
                        data=zip_data,
                        file_name="archivos_procesados_completos_coosalud.zip",
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
                        st.markdown("**🔢 Archivos Renombrados:**")
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
    ### Cómo usar el Conversor + Renombrador Combinado:
    
    1. **Selecciona archivos**: Haz clic en 'Browse files' o arrastra los archivos
    2. **Mezcla tipos**: Puedes seleccionar archivos JSON y archivos con patrón NE###### juntos
    3. **Procesa**: Haz clic en 'Procesar Todo' - se ejecutarán ambas operaciones
    4. **Descarga**: Obtén todos los archivos procesados en un ZIP o individualmente
    
    ### Transformaciones aplicadas:
    
    **Para archivos JSON:**
    - Corrige formato de fechas: `"2023-01-01T00:00:00+00:00"` → `"2023-01-01T00:00:00"`
    - Renombra archivos con fecha inválida: `archivo.json` → `archivo-SIN FECHA.json`
    - Estructura JSON según estándar Coosalud
    
    **Para archivos con patrón NE######:**
    - `NE651.pdf` → `CUV_NE651.pdf`
    - `NE999999.xlsx` → `CUV_NE999999.xlsx`
    - `documento_NE8888.txt` → `CUV_NE8888.txt`
    
    ### Características:
    - ✅ Procesamiento simultáneo de JSON y renombrado
    - ✅ Detección automática de tipos de archivo
    - ✅ Validación de patrones antes del procesamiento
    - ✅ Descarga combinada en ZIP o individual
    """)

# FOOTER
st.markdown("---")
st.caption("🔄 Conversor + Renombrador - Coosalud • v2.0 • Procesamiento Combinado")
