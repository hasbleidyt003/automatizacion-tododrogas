import streamlit as st
import re
import pandas as pd
import zipfile
import io
from datetime import datetime
import PyPDF2
from typing import Dict, List, Tuple, Optional

# Importar componentes
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

# Configurar tema y navbar
configure_modern_theme()

# Configurar página
st.set_page_config(
    page_title="Procesador Salud Total - Cloud",
    page_icon="🏥",
    layout="wide"
)

# LLAMAR EL NAVBAR COMPLETO (CON SIDEBAR)
modern_navbar()

class CloudPDFProcessor:
    """Procesador 100% cloud-compatible para Salud Total"""
    
    def __init__(self):
        self.invoice_cache = {}
        
    def extract_invoice_from_txt_name(self, txt_filename: str) -> Optional[str]:
        """Extraer número de factura del nombre del archivo TXT"""
        try:
            # Patrones flexibles para nombres de archivo
            patterns = [
                r'(NE\d+)',                      # NE123
                r'(\d{6,10})',                   # 123456
                r'([A-Z]{2,4}\d{3,8})',          # AB12345
                r'(FACTURA[_-]?\d+)',            # FACTURA123
            ]
            
            filename = txt_filename.upper().replace('.TXT', '')
            
            for pattern in patterns:
                match = re.search(pattern, filename)
                if match:
                    invoice = match.group(1)
                    st.success(f"✅ Factura detectada: {invoice}")
                    return invoice
            
            return None
            
        except Exception as e:
            st.error(f"❌ Error extrayendo factura: {e}")
            return None
    
    def extract_patient_data_advanced(self, pdf_content: bytes) -> Dict[str, str]:
        """Extracción avanzada de datos del paciente usando múltiples estrategias"""
        
        def safe_pdf_extraction(content: bytes) -> str:
            """Extracción segura de texto PDF"""
            try:
                pdf_file = io.BytesIO(content)
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                
                for page in pdf_reader.pages:
                    page_text = page.extract_text() or ""
                    text += page_text + "\n"
                
                return text
            except Exception as e:
                st.warning(f"⚠ Error lectura PDF: {e}")
                return ""
        
        # Extraer texto del PDF
        pdf_text = safe_pdf_extraction(pdf_content)
        
        if not pdf_text or len(pdf_text.strip()) < 50:
            return {"error": "Texto insuficiente en PDF"}
        
        # NORMALIZAR TEXTO
        normalized_text = self.normalize_text(pdf_text)
        
        # ESTRATEGIAS DE EXTRACCIÓN EN CASCADA
        extraction_results = {
            "document_number": None,
            "patient_name": None,
            "confidence": 0
        }
        
        # ESTRATEGIA 1: PATRONES ESTRUCTURADOS (Alta confianza)
        structured_doc = self.extract_with_structured_patterns(normalized_text)
        if structured_doc:
            extraction_results["document_number"] = structured_doc
            extraction_results["confidence"] += 80
        
        # ESTRATEGIA 2: ANÁLISIS POR CONTEXTO (Media confianza)
        if not extraction_results["document_number"]:
            context_doc = self.extract_with_context_analysis(normalized_text)
            if context_doc:
                extraction_results["document_number"] = context_doc
                extraction_results["confidence"] += 60
        
        # ESTRATEGIA 3: BÚSQUEDA INTELIGENTE (Baja confianza)
        if not extraction_results["document_number"]:
            smart_doc = self.extract_with_smart_search(normalized_text)
            if smart_doc:
                extraction_results["document_number"] = smart_doc
                extraction_results["confidence"] += 40
        
        # Extraer nombre del paciente si es posible
        extraction_results["patient_name"] = self.extract_patient_name(normalized_text)
        
        return extraction_results
    
    def normalize_text(self, text: str) -> str:
        """Normalizar texto para mejor procesamiento"""
        # Unificar espacios y saltos de línea
        text = re.sub(r'\s+', ' ', text)
        
        # Normalizar caracteres especiales
        replacements = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
            'ñ': 'n', 'Ñ': 'N'
        }
        
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        return text.upper()
    
    def extract_with_structured_patterns(self, text: str) -> Optional[str]:
        """Extracción con patrones estructurados de alta confianza"""
        
        structured_patterns = [
            # Formato: CC-NUMERO-
            r'CC[-\s]*(\d{8,12})(?=\s|$|-)',
            
            # Formato: DOCUMENTO: NUMERO
            r'DOCUMENTO[:\s]*(\d{8,12})(?=\s|$)',
            
            # Formato: N° DOCUMENTO: NUMERO
            r'N[°\s]*DOCUMENTO[:\s]*(\d{8,12})(?=\s|$)',
            
            # Formato: CEDULA: NUMERO
            r'CEDULA[:\s]*(\d{8,12})(?=\s|$)',
            
            # Formato: IDENTIFICACION: NUMERO
            r'IDENTIFICACION[:\s]*(\d{8,12})(?=\s|$)',
            
            # Formato en línea de paciente: PACIENTE: ... CC-NUMERO
            r'PACIENTE[^:]*CC[-\s]*(\d{8,12})',
        ]
        
        for pattern in structured_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if self.validate_document_number(match):
                    st.info(f"📄 Documento encontrado (estructurado): {match}")
                    return match
        
        return None
    
    def extract_with_context_analysis(self, text: str) -> Optional[str]:
        """Extracción mediante análisis contextual"""
        
        # Buscar secciones que contengan datos del paciente
        context_keywords = ['PACIENTE', 'DOCUMENTO', 'IDENTIFICACION', 'CEDULA', 'DATOS PERSONALES']
        
        lines = text.split('\n')
        candidate_lines = []
        
        for i, line in enumerate(lines):
            if any(keyword in line for keyword in context_keywords):
                # Agregar línea actual y contexto alrededor
                start = max(0, i - 2)
                end = min(len(lines), i + 3)
                context = ' '.join(lines[start:end])
                candidate_lines.append(context)
        
        # Buscar números en contexto relevante
        for context in candidate_lines:
            numbers = re.findall(r'\b\d{8,12}\b', context)
            for number in numbers:
                if self.validate_document_number(number):
                    st.info(f"📄 Documento encontrado (contextual): {number}")
                    return number
        
        return None
    
    def extract_with_smart_search(self, text: str) -> Optional[str]:
        """Búsqueda inteligente con validación múltiple"""
        
        # Encontrar todos los números candidatos
        all_numbers = re.findall(r'\b\d{7,13}\b', text)
        candidates = []
        
        for number in all_numbers:
            if self.validate_document_number(number):
                # Calcular puntuación basada en contexto
                score = self.calculate_document_confidence(number, text)
                candidates.append((number, score))
        
        # Ordenar por confianza y tomar el mejor
        if candidates:
            best_candidate = max(candidates, key=lambda x: x[1])
            if best_candidate[1] > 50:  # Umbral mínimo de confianza
                st.info(f"📄 Documento encontrado (búsqueda inteligente): {best_candidate[0]} (confianza: {best_candidate[1]}%)")
                return best_candidate[0]
        
        return None
    
    def validate_document_number(self, number: str) -> bool:
        """Validación avanzada de número de documento"""
        if not number or not number.isdigit():
            return False
        
        length = len(number)
        
        # Longitudes típicas de documentos colombianos
        if length not in [8, 10, 11, 12]:
            return False
        
        # Excluir números que probablemente no sean documentos
        invalid_patterns = [
            r'^12345678',      # Secuencias obvias
            r'^11111111',      # Números repetidos
            r'^20\d{6}',       # Posibles años
            r'^19\d{6}',       # Posibles años
            r'^300\d{7}',      # Posibles teléfonos
        ]
        
        for pattern in invalid_patterns:
            if re.match(pattern, number):
                return False
        
        return True
    
    def calculate_document_confidence(self, number: str, context: str) -> int:
        """Calcular confianza del documento basado en contexto"""
        confidence = 0
        
        # Bonus por palabras clave cercanas
        keywords = ['PACIENTE', 'DOCUMENTO', 'CC', 'CEDULA', 'IDENTIFICACION']
        for keyword in keywords:
            if keyword in context:
                # Calcular proximidad
                keyword_pos = context.find(keyword)
                number_pos = context.find(number)
                if abs(keyword_pos - number_pos) < 200:
                    confidence += 25
        
        # Bonus por formato específico
        if f"CC-{number}" in context or f"CC {number}" in context:
            confidence += 30
        
        # Bonus por estar en líneas con formato de datos personales
        if re.search(r'PACIENTE.*CC.*\d', context) or re.search(r'DOCUMENTO.*\d', context):
            confidence += 20
        
        # Penalizar por contexto de contacto
        if any(word in context for word in ['TELEFONO', 'CELULAR', 'EMAIL', '@']):
            confidence -= 15
        
        return min(100, max(0, confidence))
    
    def extract_patient_name(self, text: str) -> Optional[str]:
        """Extraer nombre del paciente si es posible"""
        try:
            # Buscar patrones de nombre después de "PACIENTE:"
            name_patterns = [
                r'PACIENTE[:\s]+([A-Z\s]{10,50}?)(?=\s|CC|DOCUMENTO|$)',
                r'NOMBRE[:\s]+([A-Z\s]{10,50}?)(?=\s|$)',
            ]
            
            for pattern in name_patterns:
                match = re.search(pattern, text)
                if match:
                    name = match.group(1).strip()
                    # Validar que parece un nombre (múltiples palabras)
                    if len(name.split()) >= 2:
                        return name
            
            return None
            
        except Exception:
            return None

def main():
    # El navbar ya se llamó arriba, ahora solo el contenido principal
    
    # CONTENIDO PRINCIPAL
    st.title("🏥 Procesador Salud Total - Cloud")
    st.markdown("Procesamiento 100% automático de facturas **sin dependencias externas**")
    
    # Inicializar procesador
    processor = CloudPDFProcessor()
    
    # SECCIÓN DE CARGA DE ARCHIVOS - EN ÁREA PRINCIPAL
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📄 Archivo TXT")
        uploaded_txt = st.file_uploader(
            "Subir archivo TXT (el nombre contiene la factura)",
            type=['txt'],
            key="txt_uploader"
        )
        
        if uploaded_txt:
            invoice_number = processor.extract_invoice_from_txt_name(uploaded_txt.name)
            if invoice_number:
                st.session_state.invoice_number = invoice_number
                st.success(f"**Factura detectada:** `{invoice_number}`")
            else:
                st.error("No se pudo detectar el número de factura del nombre del archivo")
    
    with col2:
        st.subheader("📁 Archivos PDF")
        uploaded_pdfs = st.file_uploader(
            "Subir PDFs escaneados",
            type=['pdf'],
            accept_multiple_files=True,
            key="pdf_uploader"
        )
        
        if uploaded_pdfs:
            st.success(f"**{len(uploaded_pdfs)} PDFs** listos para procesar")
    
    # INFORMACIÓN ADICIONAL EN EL ÁREA PRINCIPAL
    st.markdown("---")
    
    with st.expander("📋 Información del Proceso", expanded=True):
        st.markdown("""
        **🔍 ¿Cómo funciona?**
        
        1. **Sube un archivo TXT** cuyo nombre contenga el número de factura (ej: `NE6.txt`)
        2. **Sube los PDFs** escaneados de Salud Total
        3. **El sistema automáticamente** extraerá:
           - 📄 Número de factura del nombre del TXT
           - 🆔 Cédula del paciente del contenido del PDF
        4. **Descarga un ZIP** con los PDFs renombrados en formato:  
           `CRC_830500960_NE6_CC123456789.pdf`
        """)
    
    # PROCESAMIENTO
    if uploaded_txt and uploaded_pdfs and 'invoice_number' in st.session_state:
        st.markdown("---")
        st.subheader("🚀 Procesamiento")
        
        if st.button("Iniciar Procesamiento", type="primary", use_container_width=True):
            progress_bar = st.progress(0)
            results = []
            processed_count = 0
            
            with st.spinner("Procesando archivos..."):
                for i, pdf_file in enumerate(uploaded_pdfs):
                    try:
                        # Actualizar progreso
                        progress = (i + 1) / len(uploaded_pdfs)
                        progress_bar.progress(progress)
                        
                        # Procesar PDF
                        pdf_content = pdf_file.getvalue()
                        patient_data = processor.extract_patient_data_advanced(pdf_content)
                        
                        # Preparar resultado
                        result = {
                            'archivo_original': pdf_file.name,
                            'numero_factura': st.session_state.invoice_number,
                            'documento_paciente': patient_data.get('document_number', 'NO_ENCONTRADO'),
                            'nombre_paciente': patient_data.get('patient_name', 'NO_ENCONTRADO'),
                            'confianza': patient_data.get('confidence', 0),
                            'estado': '✅ ÉXITO' if patient_data.get('document_number') else '❌ ERROR'
                        }
                        
                        results.append(result)
                        processed_count += 1
                        
                        # Mostrar resultado individual
                        with st.expander(f"📄 {pdf_file.name}", expanded=False):
                            if result['documento_paciente'] != 'NO_ENCONTRADO':
                                st.success(f"**Documento:** {result['documento_paciente']}")
                                st.info(f"**Confianza:** {result['confianza']}%")
                                if result['nombre_paciente']:
                                    st.info(f"**Paciente:** {result['nombre_paciente']}")
                            else:
                                st.error("No se pudo extraer el documento del paciente")
                        
                    except Exception as e:
                        st.error(f"Error procesando {pdf_file.name}: {str(e)}")
                        results.append({
                            'archivo_original': pdf_file.name,
                            'numero_factura': st.session_state.invoice_number,
                            'documento_paciente': 'ERROR',
                            'nombre_paciente': 'ERROR',
                            'confianza': 0,
                            'estado': '❌ ERROR'
                        })
            
            # ACTUALIZAR ESTADO
            st.session_state.processed_files = processed_count
            st.session_state.results = results
            
            # MOSTRAR RESUMEN
            st.markdown("---")
            st.subheader("📊 Resumen del Procesamiento")
            
            successful = len([r for r in results if r['estado'] == '✅ ÉXITO'])
            failed = len([r for r in results if r['estado'] == '❌ ERROR'])
            
            col1, col2, col3 = st.columns(3)
            col1.metric("✅ Exitosos", successful)
            col2.metric("❌ Fallidos", failed)
            col3.metric("📄 Total", len(results))
            
            # GENERAR Y DESCARGAR RESULTADOS
            if successful > 0:
                st.markdown("---")
                st.subheader("📦 Descargar Resultados")
                
                # Crear DataFrame
                df_results = pd.DataFrame(results)
                
                # Crear ZIP con PDFs renombrados
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                    # Agregar PDFs renombrados exitosos
                    for i, (result, pdf_file) in enumerate(zip(results, uploaded_pdfs)):
                        if result['estado'] == '✅ ÉXITO':
                            new_filename = f"CRC_830500960_{result['numero_factura']}_CC{result['documento_paciente']}.pdf"
                            zip_file.writestr(new_filename, pdf_file.getvalue())
                    
                    # Agregar CSV con resultados
                    csv_data = df_results.to_csv(index=False)
                    zip_file.writestr("resultados_detallados.csv", csv_data)
                
                zip_buffer.seek(0)
                
                # Botón de descarga
                st.download_button(
                    label="📥 Descargar ZIP con PDFs Renombrados",
                    data=zip_buffer.getvalue(),
                    file_name=f"salud_total_{st.session_state.invoice_number}_{datetime.now().strftime('%Y%m%d_%H%M')}.zip",
                    mime="application/zip",
                    use_container_width=True
                )
                
                # Mostrar tabla de resultados
                st.subheader("📋 Resultados Detallados")
                st.dataframe(
                    df_results,
                    use_container_width=True,
                    column_config={
                        "archivo_original": "Archivo Original",
                        "numero_factura": "N° Factura",
                        "documento_paciente": "Documento Paciente",
                        "nombre_paciente": "Nombre Paciente",
                        "confianza": "Confianza (%)",
                        "estado": "Estado"
                    }
                )

if __name__ == "__main__":
    main()
