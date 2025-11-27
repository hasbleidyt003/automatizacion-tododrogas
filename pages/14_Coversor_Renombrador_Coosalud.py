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
    page_title="Herramientas Coosalud - Renombrador y Conversor", 
    page_icon="🔄", 
    layout="wide"
)
modern_navbar()

st.title("🔄 Herramientas Coosalud - Renombrador y Conversor")
st.markdown("Procesa archivos JSON de Mantis y renombra archivos con patrón NE######")

# Función de procesamiento JSON (Conversor Mantis)
def procesar_archivos_json(directorio):
    archivos_procesados = []
    errores = []
    
    try:
        os.chdir(directorio)
        archivos_json = [archivo for archivo in os.listdir() if archivo.lower().endswith('.json')]
        
        for nombre_archivo in archivos_json:
            try:
                with open(nombre_archivo, 'r', encoding='utf-8') as file:
                    datos = json.load(file)
                
                fecha_original = datos.get('fechaRadicacion') or datos.get('FechaRadicacion')
                
                # Renombrar archivos con fecha 0000-00-00
                if fecha_original == "0000-00-00T00:00:00":
                    nombre_base, extension = os.path.splitext(nombre_archivo)
                    nuevo_nombre = f"{nombre_base}-SIN FECHA{extension}"
                    os.rename(nombre_archivo, nuevo_nombre)
                    nombre_archivo = nuevo_nombre
                
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
                
                # Guardar CON sangría pero SIN espacio en resultadosValidacion
                with open(nombre_archivo, 'w', encoding='utf-8') as file:
                    json_str = json.dumps(resultado, indent=2, ensure_ascii=False)
                    json_str = json_str.replace('"resultadosValidacion": []', '"resultadosValidacion":[]')
                    file.write(json_str)
                
                archivos_procesados.append({
                    'nombre': nombre_archivo,
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
            
            # Verificar si es un archivo (no carpeta)
            if os.path.isfile(ruta_completa):
                # Buscar el patrón NE seguido de números en el nombre del archivo
                patron = r'(NE\d+)'
                coincidencia = re.search(patron, archivo)
                
                if coincidencia:
                    numero_factura = coincidencia.group(1)  # Extraer el NE651, NE99999999, etc.
                    
                    # Obtener la extensión del archivo
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

# INTERFAZ PRINCIPAL
st.header("🛠️ Selecciona la Herramienta")

# Selector de herramienta
herramienta = st.radio(
    "Selecciona la funcionalidad que necesitas:",
    ["🔢 Renombrador CUV", "📊 Conversor Mantis JSON"],
    horizontal=True
)

st.markdown("---")

if herramienta == "🔢 Renombrador CUV":
    st.subheader("🔢 Renombrador CUV - Coosalud")
    st.markdown("Convierte archivos con patrón NE###### a formato CUV_NE######")
    
    # Subida de archivos para renombrador
    uploaded_files = st.file_uploader(
        "Selecciona archivos para renombrar (patrón NE######)",
        accept_multiple_files=True,
        help="Archivos con formato: NE651.pdf, NE999999.xlsx, etc.",
        key="renombrador"
    )
    
    # Información adicional para renombrador
    st.info("""
    **ℹ️ Funcionalidad:**
    - Convierte archivos con patrón `NE######` a `CUV_NE######`
    - Ejemplo: `NE651.pdf` → `CUV_NE651.pdf`
    - Procesa múltiples archivos simultáneamente
    - No modifica el contenido, solo el nombre
    """)
    
    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} archivo(s) listo(s) para procesar")
        
        # Mostrar archivos seleccionados
        with st.expander("📋 Archivos Seleccionados", expanded=True):
            for i, file in enumerate(uploaded_files):
                # Verificar si coincide con el patrón
                patron = r'(NE\d+)'
                coincidencia = re.search(patron, file.name)
                estado_patron = "✅ Coincide" if coincidencia else "❌ No coincide"
                st.write(f"{i+1}. {file.name} - {estado_patron}")
        
        # Botón de procesamiento para renombrador
        if st.button("🚀 Renombrar Archivos", type="primary", use_container_width=True, key="btn_renombrar"):
            with st.spinner("Procesando archivos..."):
                # Crear directorio temporal
                with tempfile.TemporaryDirectory() as temp_dir:
                    # Guardar archivos subidos en directorio temporal
                    for uploaded_file in uploaded_files:
                        temp_path = os.path.join(temp_dir, uploaded_file.name)
                        with open(temp_path, "wb") as f:
                            f.write(uploaded_file.getvalue())
                    
                    # Procesar archivos con renombrador
                    resultados, contador = renombrar_archivos_cuv(temp_dir)
                    
                    # MOSTRAR RESULTADOS
                    st.markdown("---")
                    st.header("📊 Resultados del Renombrado")
                    
                    # Estadísticas rápidas
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Total Archivos", len(uploaded_files))
                    with col2:
                        st.metric("Renombrados", contador)
                    with col3:
                        no_coinciden = len(uploaded_files) - contador
                        st.metric("No Coinciden", no_coinciden)
                    with col4:
                        tasa_renombre = (contador / len(uploaded_files)) * 100 if uploaded_files else 0
                        st.metric("Tasa Renombre", f"{tasa_renombre:.1f}%")
                    
                    # Resultados detallados
                    st.subheader("📋 Detalle de Archivos")
                    
                    # Separar por tipo de resultado
                    renombrados = [r for r in resultados if r['tipo'] == 'success']
                    errores = [r for r in resultados if r['tipo'] == 'error']
                    info = [r for r in resultados if r['tipo'] == 'info']
                    
                    if renombrados:
                        st.markdown("#### ✅ Archivos Renombrados Exitosamente")
                        for resultado in renombrados:
                            st.success(f"**{resultado['original']}** → **{resultado['nuevo']}**")
                            st.caption(f"Número de factura: {resultado['numero_factura']}")
                    
                    if errores:
                        st.markdown("#### ❌ Errores en Renombrado")
                        for resultado in errores:
                            st.error(f"**{resultado['original']}** → {resultado['estado']}")
                    
                    if info:
                        st.markdown("#### ℹ️ Archivos No Procesados")
                        for resultado in info:
                            st.info(f"**{resultado['original']}** → {resultado['estado']}")
                    
                    # PREPARAR DESCARGA
                    st.markdown("---")
                    st.subheader("📥 Descargar Archivos Renombrados")
                    
                    if contador > 0:
                        # Crear ZIP con archivos renombrados
                        zip_path = os.path.join(temp_dir, "archivos_cuv_renombrados.zip")
                        shutil.make_archive(zip_path.replace('.zip', ''), 'zip', temp_dir)
                        
                        # Leer el ZIP para descarga
                        with open(zip_path, "rb") as f:
                            zip_data = f.read()
                        
                        # Botón de descarga ZIP
                        st.download_button(
                            label="📦 Descargar Todos los Archivos (ZIP)",
                            data=zip_data,
                            file_name="archivos_cuv_coosalud.zip",
                            mime="application/zip",
                            use_container_width=True
                        )
                        
                        # Descargas individuales
                        st.markdown("**Descargas Individuales:**")
                        cols = st.columns(3)
                        
                        for i, archivo in enumerate(renombrados):
                            with cols[i % 3]:
                                file_path = os.path.join(temp_dir, archivo['nuevo'])
                                if os.path.exists(file_path):
                                    with open(file_path, "rb") as f:
                                        file_data = f.read()
                                    
                                    st.download_button(
                                        label=f"📄 {archivo['nuevo'][:20]}...",
                                        data=file_data,
                                        file_name=archivo['nuevo'],
                                        mime="application/octet-stream",
                                        key=f"download_ren_{i}"
                                    )
                    else:
                        st.warning("No hay archivos renombrados para descargar")

else:  # Conversor Mantis JSON
    st.subheader("📊 Conversor Mantis JSON - Coosalud")
    st.markdown("Procesa archivos JSON de Mantis para Coosalud")
    
    # Subida de archivos para conversor
    uploaded_files = st.file_uploader(
        "Selecciona archivos JSON para procesar",
        type=['json'],
        accept_multiple_files=True,
        help="Puedes seleccionar múltiples archivos JSON",
        key="conversor"
    )
    
    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} archivo(s) listo(s) para procesar")
        
        # Mostrar archivos seleccionados
        with st.expander("📋 Archivos Seleccionados", expanded=True):
            for i, file in enumerate(uploaded_files):
                st.write(f"{i+1}. {file.name}")
        
        # Botón de procesamiento para conversor
        if st.button("🚀 Procesar Archivos", type="primary", use_container_width=True, key="btn_procesar"):
            with st.spinner("Procesando archivos JSON..."):
                # Crear directorio temporal
                with tempfile.TemporaryDirectory() as temp_dir:
                    # Guardar archivos subidos en directorio temporal
                    for uploaded_file in uploaded_files:
                        temp_path = os.path.join(temp_dir, uploaded_file.name)
                        with open(temp_path, "wb") as f:
                            f.write(uploaded_file.getvalue())
                    
                    # Procesar archivos con conversor
                    archivos_procesados, errores = procesar_archivos_json(temp_dir)
                    
                    # MOSTRAR RESULTADOS
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("✅ Archivos Procesados")
                        if archivos_procesados:
                            for archivo in archivos_procesados:
                                st.success(f"**{archivo['nombre']}**")
                                st.caption(f"Fecha: {archivo['fecha']}")
                        else:
                            st.info("No se procesaron archivos")
                    
                    with col2:
                        st.subheader("❌ Errores")
                        if errores:
                            for error in errores:
                                st.error(f"**{error['nombre']}**: {error['error']}")
                        else:
                            st.success("No hubo errores")
                    
                    # PREPARAR DESCARGA
                    st.markdown("---")
                    st.subheader("📥 Descargar Archivos Procesados")
                    
                    if archivos_procesados:
                        # Crear ZIP con archivos procesados
                        zip_path = os.path.join(temp_dir, "archivos_procesados.zip")
                        shutil.make_archive(zip_path.replace('.zip', ''), 'zip', temp_dir)
                        
                        # Leer el ZIP para descarga
                        with open(zip_path, "rb") as f:
                            zip_data = f.read()
                        
                        st.download_button(
                            label="📦 Descargar Todos los Archivos (ZIP)",
                            data=zip_data,
                            file_name="archivos_procesados_coosalud.zip",
                            mime="application/zip",
                            use_container_width=True
                        )
                        
                        # Descargas individuales
                        st.markdown("**Descargas Individuales:**")
                        cols = st.columns(3)
                        for i, archivo in enumerate(archivos_procesados):
                            with cols[i % 3]:
                                file_path = os.path.join(temp_dir, archivo['nombre'])
                                with open(file_path, "rb") as f:
                                    file_data = f.read()
                                
                                st.download_button(
                                    label=f"📄 {archivo['nombre'][:15]}...",
                                    data=file_data,
                                    file_name=archivo['nombre'],
                                    mime="application/json",
                                    key=f"download_conv_{i}"
                                )
                    else:
                        st.warning("No hay archivos para descargar")

# INSTRUCCIONES
with st.expander("📖 Instrucciones de Uso"):
    if herramienta == "🔢 Renombrador CUV":
        st.markdown("""
        ### Cómo usar el Renombrador CUV:
        
        1. **Selecciona archivos**: Haz clic en 'Browse files' o arrastra los archivos
        2. **Verifica patrones**: Los archivos deben tener formato `NE######`
        3. **Procesa**: Haz clic en 'Renombrar Archivos'
        4. **Descarga**: Obtén los archivos renombrados individualmente o en ZIP
        
        ### Transformación aplicada:
        - `NE651.ext` → `CUV_NE651.ext`
        - `NE999999.ext` → `CUV_NE999999.ext`
        
        ### Características:
        - ✅ Detecta automáticamente patrones NE######
        - ✅ Convierte a formato estándar CUV_NE######
        - ✅ Procesamiento masivo simultáneo
        - ✅ Validación de patrones antes del procesamiento
        """)
    else:
        st.markdown("""
        ### Cómo usar el Conversor Mantis:
        
        1. **Selecciona archivos JSON**: Haz clic en 'Browse files' o arrastra los archivos JSON
        2. **Revisa los archivos**: Verifica que sean los correctos en la lista
        3. **Procesa**: Haz clic en 'Procesar Archivos'
        4. **Descarga**: Obtén los archivos procesados individualmente o en ZIP
        
        ### Características del procesamiento:
        - ✅ Corrige formato de fechas
        - ✅ Renombra archivos con fechas inválidas
        - ✅ Estructura JSON según estándar Coosalud
        - ✅ Mantiene codificación UTF-8
        """)

# FOOTER
st.markdown("---")
st.caption("🔄 Herramientas Coosalud • v2.0 • Renombrador CUV + Conversor Mantis")
