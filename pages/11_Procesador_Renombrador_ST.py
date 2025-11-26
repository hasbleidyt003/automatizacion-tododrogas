import streamlit as st
import re
import os
import tempfile
import shutil
from pathlib import Path
import threading
from datetime import datetime
import traceback
import pandas as pd
import time

# Configurar página
st.set_page_config(
    page_title="Procesador OCR - Salud Total",
    page_icon="🔍",
    layout="wide"
)

# Verificar e importar dependencias
try:
    import PyPDF2
    PDF2_AVAILABLE = True
except ImportError:
    PDF2_AVAILABLE = False
    st.warning("⚠️ PyPDF2 no está instalado. Ejecute: `pip install PyPDF2`")

try:
    from pdf2image import convert_from_path
    PDF2IMAGE_AVAILABLE = True
except ImportError:
    PDF2IMAGE_AVAILABLE = False
    st.warning("⚠️ pdf2image no está instalado. El OCR no funcionará.")

try:
    import pytesseract
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False
    st.warning("⚠️ pytesseract no está instalado. El OCR no funcionará.")

try:
    from PIL import Image, ImageEnhance, ImageFilter
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    st.warning("⚠️ Pillow no está instalado. El OCR no funcionará.")

class PDFProcessorST:
    def __init__(self):
        self.processing = False
        self.processed_files = 0
        self.renamed_files = 0
        self.error_files = 0
        
    def check_dependencies(self):
        """Verificar dependencias disponibles"""
        deps_status = {
            "PyPDF2": PDF2_AVAILABLE,
            "pdf2image": PDF2IMAGE_AVAILABLE,
            "pytesseract": TESSERACT_AVAILABLE,
            "Pillow": PIL_AVAILABLE
        }
        return deps_status
    
    def extract_code_from_text(self, texto):
        """Extraer código D0 del texto"""
        if not texto:
            return None
            
        texto_limpio = texto.replace(" ", "").replace("\n", "").replace("\t", "")
        
        # Códigos específicos de Salud Total
        codigos_especificos = [
            "D07250606369", "D07250721912", "D07250723288", 
            "D07250725472", "D07250711286", "D07250712248",
            "D07250703567", "D07250723001", "D07250723086",
            "D07250722866", "D07250725611"
        ]
        
        for codigo in codigos_especificos:
            if codigo in texto_limpio:
                st.session_state.log_messages.append(f"🔍 Código específico encontrado: {codigo}")
                return codigo
        
        # Patrones mejorados para Salud Total
        patrones_mejorados = [
            r"\*(D0\d{10})\*", r"\*(D0\d{9,11})\*",
            r"Acta de Entrega\s*\*(D0\d{9,11})\*",
            r"Acta de Entrega[^\d]*(D0\d{10})",
            r"\b(D0\d{10})\b", r"\b(D0\d{9,11})\b",
            r"NRO\s+ENTREGA.*?(D0\d{10})",
        ]
        
        for i, patron in enumerate(patrones_mejorados):
            try:
                busqueda = re.search(patron, texto, re.IGNORECASE | re.DOTALL)
                if busqueda:
                    codigo = busqueda.group(1).strip()
                    codigo = re.sub(r'[^\dD]', '', codigo.upper())
                    if re.match(r'^D0\d{10}$', codigo):
                        st.session_state.log_messages.append(f"✅ Código encontrado (patrón {i+1}): {codigo}")
                        return codigo
            except Exception as e:
                st.session_state.log_messages.append(f"⚠ Error con patrón {i+1}: {e}")
        
        return None
    
    def extract_text_with_pdfminer(self, pdf_path):
        """Extraer texto usando pdftotext"""
        try:
            poppler_path = st.session_state.poppler_path
            if poppler_path and Path(poppler_path).exists():
                pdftotext_path = Path(poppler_path) / "pdftotext.exe"
                
                if pdftotext_path.exists():
                    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
                        temp_text_path = temp_file.name
                    
                    import subprocess
                    cmd = [str(pdftotext_path), "-layout", "-nopgbrk", str(pdf_path), temp_text_path]
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                    
                    if result.returncode == 0:
                        with open(temp_text_path, 'r', encoding='utf-8', errors='ignore') as f:
                            texto = f.read()
                        os.unlink(temp_text_path)
                        return texto
                    
                    if os.path.exists(temp_text_path):
                        os.unlink(temp_text_path)
                        
        except Exception as e:
            st.session_state.log_messages.append(f"⚠ Error con pdftotext: {e}")
        
        return None
    
    def process_single_file(self, archivo_pdf):
        """Procesar un solo archivo PDF"""
        st.session_state.log_messages.append(f"🔍 Analizando: {archivo_pdf.name}")
        texto = ""
        
        # Intentar con pdftotext primero
        texto_pdftotext = self.extract_text_with_pdfminer(archivo_pdf)
        if texto_pdftotext:
            codigo = self.extract_code_from_text(texto_pdftotext)
            if codigo:
                st.session_state.log_messages.append(f"✅ Código encontrado con pdftotext: {codigo}")
                return codigo, texto_pdftotext
            texto = texto_pdftotext
        
        # Intentar con PyPDF2
        try:
            with open(archivo_pdf, "rb") as f:
                lector = PyPDF2.PdfReader(f)
                for pagina in lector.pages:
                    contenido = pagina.extract_text()
                    if contenido:
                        texto += contenido + "\n"
                
                codigo = self.extract_code_from_text(texto)
                if codigo:
                    return codigo, texto
                
                # Intentar con extracción de layout
                texto_layout = ""
                for pagina in lector.pages:
                    try:
                        contenido = pagina.extract_text(0)
                        if contenido:
                            texto_layout += contenido + "\n"
                    except:
                        pass
                
                if texto_layout != texto:
                    codigo = self.extract_code_from_text(texto_layout)
                    if codigo:
                        return codigo, texto_layout
        except Exception as e:
            st.session_state.log_messages.append(f"⚠ Falló la extracción de texto directo: {e}")
        
        # Usar OCR como último recurso
        if (PDF2IMAGE_AVAILABLE and TESSERACT_AVAILABLE and PIL_AVAILABLE and 
            st.session_state.use_ocr):
            try:
                st.session_state.log_messages.append(f"🔍 Usando OCR para: {archivo_pdf.name}")
                
                # Configurar Tesseract
                if st.session_state.tesseract_path and Path(st.session_state.tesseract_path).exists():
                    pytesseract.pytesseract.tesseract_cmd = st.session_state.tesseract_path
                
                paginas = convert_from_path(
                    archivo_pdf,
                    dpi=300,
                    poppler_path=st.session_state.poppler_path,
                    first_page=1,
                    last_page=3,  # Limitar a las primeras 3 páginas por rendimiento
                    grayscale=True
                )
                
                for page_num, img in enumerate(paginas):
                    # Preprocesamiento de imagen
                    img = img.convert('L')
                    img = ImageEnhance.Brightness(img).enhance(st.session_state.brightness)
                    img = ImageEnhance.Contrast(img).enhance(st.session_state.contrast)
                    img = ImageEnhance.Sharpness(img).enhance(st.session_state.sharpness)
                    img = img.filter(ImageFilter.SHARPEN)
                    
                    configuraciones = [
                        '--psm 6 -c tessedit_char_whitelist=0123456789D*',
                        '--psm 3 -c tessedit_char_whitelist=0123456789D*',
                        '--psm 11 -c tessedit_char_whitelist=0123456789D*',
                    ]
                    
                    for config in configuraciones:
                        texto_ocr = pytesseract.image_to_string(img, lang="spa", config=config)
                        codigo = self.extract_code_from_text(texto_ocr)
                        if codigo:
                            st.session_state.log_messages.append(f"✅ Código encontrado via OCR (página {page_num+1}): {codigo}")
                            return codigo, texto_ocr
            except Exception as e:
                st.session_state.log_messages.append(f"⚠ Error en OCR: {e}")
        
        if not codigo:
            st.session_state.log_messages.append("❌ No se pudo encontrar el código")
        
        return None, texto
    
    def process_files(self, input_folder, output_folder):
        """Procesar todos los archivos PDF"""
        self.processing = True
        self.processed_files = 0
        self.renamed_files = 0
        self.error_files = 0
        
        pdf_files = list(Path(input_folder).glob("*.pdf"))
        total_files = len(pdf_files)
        
        if total_files == 0:
            st.session_state.log_messages.append("❌ No hay archivos PDF para procesar")
            self.processing = False
            return
        
        st.session_state.progress_total = total_files
        st.session_state.progress_current = 0
        
        resultados = []
        
        for i, archivo_pdf in enumerate(pdf_files):
            if not self.processing:
                break
                
            try:
                self.processed_files += 1
                st.session_state.progress_current = i + 1
                
                codigo, texto = self.process_single_file(archivo_pdf)
                
                resultado = {
                    'archivo': archivo_pdf.name,
                    'codigo_encontrado': codigo if codigo else "NO_ENCONTRADO",
                    'estado': '✅ ÉXITO' if codigo else '❌ ERROR',
                    'nuevo_nombre': '',
                    'ruta_original': str(archivo_pdf)
                }
                
                if codigo:
                    nuevo_nombre = f"{codigo}.pdf"
                    nueva_ruta = Path(output_folder) / nuevo_nombre
                    
                    # Manejar duplicados
                    counter = 1
                    while nueva_ruta.exists():
                        nuevo_nombre = f"{codigo}_{counter}.pdf"
                        nueva_ruta = Path(output_folder) / nuevo_nombre
                        counter += 1
                    
                    # Crear carpeta de salida si no existe
                    Path(output_folder).mkdir(parents=True, exist_ok=True)
                    
                    if output_folder != input_folder:
                        shutil.copy2(archivo_pdf, nueva_ruta)
                        st.session_state.log_messages.append(f"✓ COPIADO: {archivo_pdf.name} -> {nuevo_nombre}")
                    else:
                        archivo_pdf.rename(nueva_ruta)
                        st.session_state.log_messages.append(f"✓ RENOMBRADO: {archivo_pdf.name} -> {nuevo_nombre}")
                    
                    resultado['nuevo_nombre'] = nuevo_nombre
                    resultado['ruta_destino'] = str(nueva_ruta)
                    self.renamed_files += 1
                    
                else:
                    st.session_state.log_messages.append(f"✗ No se encontró código en: {archivo_pdf.name}")
                    self.error_files += 1
                
                resultados.append(resultado)
                
            except Exception as e:
                st.session_state.log_messages.append(f"✗ Error procesando {archivo_pdf.name}: {str(e)}")
                self.error_files += 1
                resultados.append({
                    'archivo': archivo_pdf.name,
                    'codigo_encontrado': 'ERROR',
                    'estado': '❌ ERROR',
                    'nuevo_nombre': '',
                    'ruta_original': str(archivo_pdf),
                    'error': str(e)
                })
        
        self.processing = False
        st.session_state.resultados = resultados
        
        # Resumen final
        st.session_state.log_messages.append("\n" + "=" * 60)
        st.session_state.log_messages.append(" RESUMEN DEL PROCESAMIENTO ")
        st.session_state.log_messages.append("=" * 60)
        st.session_state.log_messages.append(f"Archivos procesados: {self.processed_files}")
        st.session_state.log_messages.append(f"Archivos renombrados: {self.renamed_files}")
        st.session_state.log_messages.append(f"Archivos con errores: {self.error_files}")
        st.session_state.log_messages.append("=" * 60)

def initialize_session_state():
    """Inicializar estado de la sesión"""
    if 'log_messages' not in st.session_state:
        st.session_state.log_messages = []
    if 'processing' not in st.session_state:
        st.session_state.processing = False
    if 'progress_current' not in st.session_state:
        st.session_state.progress_current = 0
    if 'progress_total' not in st.session_state:
        st.session_state.progress_total = 0
    if 'resultados' not in st.session_state:
        st.session_state.resultados = []
    if 'tesseract_path' not in st.session_state:
        st.session_state.tesseract_path = ""
    if 'poppler_path' not in st.session_state:
        st.session_state.poppler_path = ""
    if 'use_ocr' not in st.session_state:
        st.session_state.use_ocr = True
    if 'brightness' not in st.session_state:
        st.session_state.brightness = 1.3
    if 'contrast' not in st.session_state:
        st.session_state.contrast = 2.5
    if 'sharpness' not in st.session_state:
        st.session_state.sharpness = 2.0

def main():
    # Inicializar estado
    initialize_session_state()
    
    # Título principal
    st.title("🔍 Procesador OCR - Salud Total")
    st.markdown("Procesador inteligente de actas PDF con reconocimiento de códigos D0")
    
    # Crear instancia del procesador
    processor = PDFProcessorST()
    
    # Sidebar para configuración
    with st.sidebar:
        st.header("⚙️ Configuración")
        
        # Rutas de herramientas
        st.subheader("Rutas de Herramientas")
        st.session_state.tesseract_path = st.text_input(
            "Ruta de Tesseract OCR",
            value=st.session_state.tesseract_path,
            help="Ruta al ejecutable tesseract.exe"
        )
        
        st.session_state.poppler_path = st.text_input(
            "Ruta de Poppler",
            value=st.session_state.poppler_path,
            help="Ruta a la carpeta bin de Poppler"
        )
        
        # Configuración de OCR
        st.subheader("Configuración OCR")
        st.session_state.use_ocr = st.checkbox(
            "Usar OCR cuando sea necesario", 
            value=st.session_state.use_ocr
        )
        
        st.session_state.brightness = st.slider(
            "Brillo", 0.5, 2.0, st.session_state.brightness, 0.1
        )
        st.session_state.contrast = st.slider(
            "Contraste", 0.5, 4.0, st.session_state.contrast, 0.1
        )
        st.session_state.sharpness = st.slider(
            "Nitidez", 0.5, 3.0, st.session_state.sharpness, 0.1
        )
        
        # Estado de dependencias
        st.subheader("🔧 Estado de Dependencias")
        deps_status = processor.check_dependencies()
        for dep, status in deps_status.items():
            icon = "✅" if status else "❌"
            st.write(f"{icon} {dep}")
    
    # Contenido principal
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📁 Procesamiento de Archivos")
        
        # Selección de carpetas
        input_folder = st.text_input(
            "Carpeta de entrada con PDFs",
            placeholder="Ruta a la carpeta con archivos PDF..."
        )
        
        output_folder = st.text_input(
            "Carpeta de salida (opcional)",
            placeholder="Ruta para archivos renombrados (dejar vacío para misma carpeta)..."
        )
        
        # Botones de control
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if st.button("🚀 Iniciar Procesamiento", type="primary", use_container_width=True):
                if not input_folder or not Path(input_folder).exists():
                    st.error("❌ La carpeta de entrada no existe")
                else:
                    st.session_state.processing = True
                    st.session_state.log_messages = []
                    
                    # Ejecutar en thread separado
                    import threading
                    thread = threading.Thread(
                        target=processor.process_files,
                        args=(input_folder, output_folder or input_folder)
                    )
                    thread.start()
        
        with col_btn2:
            if st.button("⏹️ Detener Procesamiento", type="secondary", use_container_width=True):
                st.session_state.processing = False
                processor.processing = False
                st.session_state.log_messages.append("⏹️ Procesamiento detenido por el usuario")
        
        # Barra de progreso
        if st.session_state.processing:
            progress = st.session_state.progress_current / max(st.session_state.progress_total, 1)
            st.progress(progress)
            st.write(f"Procesando: {st.session_state.progress_current} / {st.session_state.progress_total}")
        
        # Área de logs
        st.subheader("📋 Registro de Actividad")
        log_container = st.container(height=300)
        with log_container:
            for message in st.session_state.log_messages[-50:]:  # Mostrar últimos 50 mensajes
                st.text(message)
    
    with col2:
        st.header("📊 Estadísticas")
        
        # Métricas en tiempo real
        if st.session_state.resultados:
            total = len(st.session_state.resultados)
            exitosos = len([r for r in st.session_state.resultados if r['estado'] == '✅ ÉXITO'])
            errores = total - exitosos
            
            st.metric("Archivos Procesados", total)
            st.metric("Renombrados Exitosos", exitosos)
            st.metric("Errores", errores)
            
            # Gráfico simple
            chart_data = pd.DataFrame({
                'Categoría': ['Éxitos', 'Errores'],
                'Cantidad': [exitosos, errores]
            })
            st.bar_chart(chart_data.set_index('Categoría'))
        
        # Botón para exportar resultados
        if st.session_state.resultados:
            st.download_button(
                label="📥 Descargar Resultados",
                data=pd.DataFrame(st.session_state.resultados).to_csv(index=False),
                file_name=f"resultados_procesamiento_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime="text/csv"
            )
    
    # Sección de resultados detallados
    if st.session_state.resultados:
        st.header("📋 Resultados Detallados")
        
        df_resultados = pd.DataFrame(st.session_state.resultados)
        
        # Filtros
        col_filt1, col_filt2 = st.columns(2)
        with col_filt1:
            filtro_estado = st.selectbox(
                "Filtrar por estado",
                ["Todos", "✅ ÉXITO", "❌ ERROR"]
            )
        
        with col_filt2:
            buscar_archivo = st.text_input("Buscar archivo...")
        
        # Aplicar filtros
        if filtro_estado != "Todos":
            df_resultados = df_resultados[df_resultados['estado'] == filtro_estado]
        
        if buscar_archivo:
            df_resultados = df_resultados[df_resultados['archivo'].str.contains(buscar_archivo, case=False)]
        
        # Mostrar tabla
        st.dataframe(
            df_resultados,
            use_container_width=True,
            column_config={
                "archivo": "Archivo Original",
                "codigo_encontrado": "Código Encontrado",
                "estado": "Estado",
                "nuevo_nombre": "Nuevo Nombre"
            }
        )

if __name__ == "__main__":
    main()
