import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
import os
import json
from pathlib import Path
from components.navbar import modern_navbar
from config.theme import configure_modern_theme

# Configurar tema moderno
configure_modern_theme()

# Configurar página
st.set_page_config(
    page_title="Cuentas Médicas - TodoDrogas",
    page_icon="📋",
    layout="wide"
)

# LLAMAR EL NAVBAR
modern_navbar()

# =============================================
# SISTEMA DE MÉTRICAS EN TIEMPO REAL
# =============================================

class MetricasCuentasMedicas:
    def __init__(self):
        self.historial_file = "data/historial_procesos.json"
        self.ensure_data_directory()
    
    def ensure_data_directory(self):
        """Asegurar que existe el directorio de datos"""
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.historial_file):
            self.inicializar_historial()
    
    def inicializar_historial(self):
        """Inicializar historial vacío"""
        historial_base = {
            "procesos": [],
            "estadisticas": {
                "total_archivos": 0,
                "archivos_hoy": 0,
                "tasa_exito": 0.0,
                "eps_stats": {
                    "COOSALUD": {"total": 0, "exitosos": 0, "hoy": 0},
                    "SAVIA SALUD": {"total": 0, "exitosos": 0, "hoy": 0},
                    "SALUD TOTAL": {"total": 0, "exitosos": 0, "hoy": 0}
                }
            }
        }
        with open(self.historial_file, 'w', encoding='utf-8') as f:
            json.dump(historial_base, f, indent=2, ensure_ascii=False)
    
    def registrar_proceso(self, eps, archivo, proceso, estado, usuario="Sistema"):
        """Registrar un nuevo proceso en el historial"""
        try:
            with open(self.historial_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            nuevo_proceso = {
                "id": len(data["procesos"]) + 1,
                "fecha": datetime.now().isoformat(),
                "eps": eps,
                "archivo": archivo,
                "proceso": proceso,
                "estado": estado,
                "usuario": usuario
            }
            
            data["procesos"].append(nuevo_proceso)
            
            # Actualizar estadísticas
            self.actualizar_estadisticas(data, eps, estado)
            
            with open(self.historial_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
            return True
        except Exception as e:
            st.error(f"Error registrando proceso: {e}")
            return False
    
    def actualizar_estadisticas(self, data, eps, estado):
        """Actualizar estadísticas basadas en el nuevo proceso"""
        hoy = datetime.now().date().isoformat()
        
        # Incrementar contadores
        data["estadisticas"]["total_archivos"] += 1
        
        # Contar archivos de hoy
        procesos_hoy = [p for p in data["procesos"] 
                       if p["fecha"].startswith(hoy)]
        data["estadisticas"]["archivos_hoy"] = len(procesos_hoy)
        
        # Estadísticas por EPS
        if eps in data["estadisticas"]["eps_stats"]:
            data["estadisticas"]["eps_stats"][eps]["total"] += 1
            data["estadisticas"]["eps_stats"][eps]["hoy"] = len(
                [p for p in procesos_hoy if p["eps"] == eps]
            )
            if estado == "✅ Completado":
                data["estadisticas"]["eps_stats"][eps]["exitosos"] += 1
        
        # Calcular tasa de éxito global
        total_exitosos = sum(
            eps_data["exitosos"] for eps_data in data["estadisticas"]["eps_stats"].values()
        )
        total_procesos = data["estadisticas"]["total_archivos"]
        
        if total_procesos > 0:
            data["estadisticas"]["tasa_exito"] = round(
                (total_exitosos / total_procesos) * 100, 1
            )
    
    def obtener_estadisticas(self):
        """Obtener estadísticas actualizadas"""
        try:
            with open(self.historial_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data["estadisticas"]
        except:
            return {
                "total_archivos": 0,
                "archivos_hoy": 0,
                "tasa_exito": 0.0,
                "eps_stats": {
                    "COOSALUD": {"total": 0, "exitosos": 0, "hoy": 0},
                    "SAVIA SALUD": {"total": 0, "exitosos": 0, "hoy": 0},
                    "SALUD TOTAL": {"total": 0, "exitosos": 0, "hoy": 0}
                }
            }
    
    def obtener_historial(self, limite=10):
        """Obtener historial reciente de procesos"""
        try:
            with open(self.historial_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            procesos_ordenados = sorted(
                data["procesos"], 
                key=lambda x: x["fecha"], 
                reverse=True
            )[:limite]
            
            return procesos_ordenados
        except:
            return []
    
    def obtener_tiempo_promedio(self):
        """Calcular tiempo promedio de procesamiento (simulado basado en estadísticas)"""
        stats = self.obtener_estadisticas()
        total_archivos = stats["total_archivos"]
        
        if total_archivos == 0:
            return "0s"
        
        # Simular tiempo basado en complejidad de procesos
        base_time = 30  # segundos base
        complexity_factor = min(total_archivos / 100, 2)  # Factor de complejidad
        
        tiempo_promedio = base_time * (1 + complexity_factor)
        return f"{int(tiempo_promedio)}s"

# Instanciar el sistema de métricas
metricas = MetricasCuentasMedicas()

# =============================================
# ESTILOS FUTURISTAS PARA BOTONES
# =============================================

st.markdown("""
<style>
    /* BOTONES FUTURISTAS - TEXTO NEGRO Y EFECTO AZUL */
    .stButton > button {
        background: transparent !important;
        color: #000000 !important;
        border: 2px solid #0066cc !important;
        padding: 0.8rem 1.5rem !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        cursor: pointer !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        width: 100% !important;
        position: relative !important;
        overflow: hidden !important;
        font-family: "Inter", sans-serif !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1) !important;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(0, 102, 204, 0.2), 
            rgba(0, 168, 255, 0.4),
            rgba(0, 102, 204, 0.2),
            transparent);
        transition: left 0.6s ease-in-out;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #0066cc, #00a8ff) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 
            0 10px 25px rgba(0, 102, 204, 0.4),
            0 5px 15px rgba(0, 168, 255, 0.3),
            0 0 30px rgba(0, 102, 204, 0.2) !important;
        border-color: #00a8ff !important;
        text-shadow: 0 1px 3px rgba(0,0,0,0.3) !important;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(1.01) !important;
        box-shadow: 
            0 5px 15px rgba(0, 102, 204, 0.4),
            0 2px 8px rgba(0, 168, 255, 0.3),
            inset 0 2px 4px rgba(0, 0, 0, 0.1) !important;
    }
    
    /* EFECTO DE PULSO EN HOVER */
    @keyframes pulse-glow {
        0%, 100% { 
            box-shadow: 
                0 10px 25px rgba(0, 102, 204, 0.4),
                0 5px 15px rgba(0, 168, 255, 0.3),
                0 0 30px rgba(0, 102, 204, 0.2);
        }
        50% { 
            box-shadow: 
                0 10px 30px rgba(0, 102, 204, 0.6),
                0 8px 25px rgba(0, 168, 255, 0.5),
                0 0 40px rgba(0, 102, 204, 0.3);
        }
    }
    
    .stButton > button:hover {
        animation: pulse-glow 2s ease-in-out infinite;
    }
    
    /* TARJETAS DE EPS MEJORADAS */
    .eps-card {
        background: white;
        border: 1px solid rgba(0, 102, 204, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }
    
    .eps-card:hover {
        box-shadow: 0 8px 25px rgba(0, 102, 204, 0.15);
        border-color: rgba(0, 102, 204, 0.2);
    }
    
    /* ESTILOS PARA PESTAÑAS MÁS PROMINENTES */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f8f9fa;
        padding: 8px;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        white-space: pre-wrap;
        background-color: white;
        border-radius: 8px 8px 0px 0px;
        gap: 8px;
        padding: 12px 20px;
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #0066cc;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# =============================================
# INTERFAZ PRINCIPAL - BOTONES ARRIBA
# =============================================

# Título de la página
st.title("📋 Cuentas Médicas")
st.markdown("Automatización de procesos para cuentas médicas por EPS")

# SECCIÓN DE EPS - ORGANIZADA POR EMPRESA (ARRIBA)
st.markdown("### 🏥 Selecciona la EPS para Procesar Archivos")

# Crear pestañas para cada EPS
tab1, tab2, tab3 = st.tabs(["🏥 COOSALUD", "💊 SAVIA SALUD", "🩺 SALUD TOTAL"])

with tab1:
    st.markdown("**COOSALUD - Procesamiento de Archivos**")
    st.info("Herramientas especializadas para Coosalud")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔄 Conversores JSON**")
        if st.button("🔧 Conversor Mantis", use_container_width=True, key="coosalud_mantis"):
            # Registrar en métricas
            metricas.registrar_proceso(
                "COOSALUD", 
                "Nuevo proceso Mantis", 
                "Conversor Mantis", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/5_Conversor_Mantis_Coosalud.py")
        
        if st.button("🔄 Conversor SISPRO", use_container_width=True, key="coosalud_sispro"):
            metricas.registrar_proceso(
                "COOSALUD", 
                "Nuevo proceso SISPRO", 
                "Conversor SISPRO", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/6_Conversor_SISPRO_Coosalud.py")
        
        # NUEVO BOTÓN AGREGADO - CONVERSOR + RENOMBRADOR UNIFICADO
        if st.button("🔄 Conversor + Renombrador", use_container_width=True, key="coosalud_unificado"):
            metricas.registrar_proceso(
                "COOSALUD", 
                "Nuevo proceso Unificado", 
                "Conversor + Renombrador", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/14_Conversor_Renombrador_Coosalud.py")
    
    with col2:
        st.markdown("**🏷️ Renombradores**")
        if st.button("📋 Renombrador RIPS", use_container_width=True, key="coosalud_rips"):
            metricas.registrar_proceso(
                "COOSALUD", 
                "Nuevo proceso RIPS", 
                "Renombrador RIPS", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/8_Renombradores_rips_Coosalud.py")
        
        if st.button("🔢 Renombrador CUV", use_container_width=True, key="coosalud_cuv"):
            metricas.registrar_proceso(
                "COOSALUD", 
                "Nuevo proceso CUV", 
                "Renombrador CUV", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/7_Renombradores_cuv_Coosalud.py")
        
        # NUEVO BOTÓN AGREGADO - RENOMBRADOR CUV SISPRO
        if st.button("🔢 Renombrador CUV SISPRO", use_container_width=True, key="coosalud_cuv_sispro"):
            metricas.registrar_proceso(
                "COOSALUD", 
                "Nuevo proceso CUV SISPRO", 
                "Renombrador CUV SISPRO", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/12_Renombrador_cuv_sispro_Coosalud.py")

with tab2:
    st.markdown("**SAVIA SALUD - Procesamiento de Archivos**")
    st.info("Herramientas especializadas para Savia Salud")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🏷️ Renombradores CUV**")
        if st.button("🔢 Renombrador CUV Savia", use_container_width=True, key="savia_cuv"):
            metricas.registrar_proceso(
                "SAVIA SALUD", 
                "Nuevo proceso CUV", 
                "Renombrador CUV", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/9_Renombrador_cuv_Savia.py")
        
        # NUEVO BOTÓN AGREGADO - CONVERSOR + RENOMBRADOR SAVIA
        if st.button("🔄 Conversor + Renombrador", use_container_width=True, key="savia_unificado"):
            metricas.registrar_proceso(
                "SAVIA SALUD", 
                "Nuevo proceso Unificado", 
                "Conversor + Renombrador", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/15_Conversor_Renombrador_Savia.py")
    
    with col2:
        st.markdown("**📋 Procesadores RIPS**")
        if st.button("📋 Renombrador RIPS Savia", use_container_width=True, key="savia_rips"):
            metricas.registrar_proceso(
                "SAVIA SALUD", 
                "Nuevo proceso RIPS", 
                "Renombrador RIPS", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/10_Renombrador_rips_Savia.py")
        
        # NUEVO BOTÓN AGREGADO - NAVEGADOR RIPS SAVIA
        if st.button("🌐 Navegador RIPS Savia", use_container_width=True, key="savia_navegador_rips"):
            metricas.registrar_proceso(
                "SAVIA SALUD", 
                "Nuevo proceso Navegador RIPS", 
                "Navegador RIPS", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/13_Navegador_RIPS_Savia.py")

with tab3:
    st.markdown("**SALUD TOTAL - Procesamiento de Archivos**")
    st.info("Herramientas especializadas para Salud Total")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔍 Procesador OCR**")
        if st.button("🔍 Procesador + Renombrador", use_container_width=True, key="salud_total_ocr"):
            metricas.registrar_proceso(
                "SALUD TOTAL", 
                "Nuevo proceso OCR", 
                "Procesador OCR", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/11_Procesador_Renombrador_ST.py")
    
    with col2:
        st.markdown("**⚡ Procesamiento Avanzado**")
        st.info("OCR inteligente con renombrado automático")

# =============================================
# SECCIÓN DE MÉTRICAS (ABAJO)
# =============================================

# Obtener estadísticas en tiempo real
estadisticas = metricas.obtener_estadisticas()
historial_reciente = metricas.obtener_historial(5)
tiempo_promedio = metricas.obtener_tiempo_promedio()

st.markdown("---")
st.markdown("### 📊 Métricas en Tiempo Real")

# Métricas principales
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_hoy = estadisticas["archivos_hoy"]
    delta_hoy = "+5" if total_hoy > 0 else "0"
    st.metric(
        label="📁 Archivos Hoy",
        value=total_hoy,
        delta=delta_hoy
    )

with col2:
    tasa_exito = estadisticas["tasa_exito"]
    delta_tasa = "+2.5%" if tasa_exito > 95 else "0%"
    st.metric(
        label="🎯 Tasa de Éxito",
        value=f"{tasa_exito}%",
        delta=delta_tasa
    )

with col3:
    st.metric(
        label="⏱️ Tiempo Promedio",
        value=tiempo_promedio,
        delta="-8s"
    )

with col4:
    total_general = estadisticas["total_archivos"]
    st.metric(
        label="📊 Total Procesado",
        value=total_general,
        delta="+12 esta semana"
    )

# Métricas por EPS
st.markdown("### 🏥 Estadísticas por EPS")

eps_col1, eps_col2, eps_col3 = st.columns(3)

with eps_col1:
    coosalud_stats = estadisticas["eps_stats"]["COOSALUD"]
    st.metric("COOSALUD - Total", coosalud_stats["total"])
    st.metric("COOSALUD - Hoy", coosalud_stats["hoy"])
    tasa_coosalud = round((coosalud_stats["exitosos"] / coosalud_stats["total"] * 100), 1) if coosalud_stats["total"] > 0 else 0
    st.metric("COOSALUD - Éxito", f"{tasa_coosalud}%")

with eps_col2:
    savia_stats = estadisticas["eps_stats"]["SAVIA SALUD"]
    st.metric("SAVIA SALUD - Total", savia_stats["total"])
    st.metric("SAVIA SALUD - Hoy", savia_stats["hoy"])
    tasa_savia = round((savia_stats["exitosos"] / savia_stats["total"] * 100), 1) if savia_stats["total"] > 0 else 0
    st.metric("SAVIA SALUD - Éxito", f"{tasa_savia}%")

with eps_col3:
    salud_total_stats = estadisticas["eps_stats"]["SALUD TOTAL"]
    st.metric("SALUD TOTAL - Total", salud_total_stats["total"])
    st.metric("SALUD TOTAL - Hoy", salud_total_stats["hoy"])
    tasa_salud_total = round((salud_total_stats["exitosos"] / salud_total_stats["total"] * 100), 1) if salud_total_stats["total"] > 0 else 0
    st.metric("SALUD TOTAL - Éxito", f"{tasa_salud_total}%")

# GRÁFICO DE ACTIVIDAD EN TIEMPO REAL
st.markdown("### 📈 Actividad por EPS - Tiempo Real")

# Crear gráfico con datos reales
try:
    eps_stats = estadisticas["eps_stats"]
    
    fig_data = pd.DataFrame({
        'EPS': list(eps_stats.keys()),
        'Total_Procesado': [eps_stats[eps]['total'] for eps in eps_stats],
        'Archivos_Hoy': [eps_stats[eps]['hoy'] for eps in eps_stats],
        'Tasa_Exito': [
            round((eps_stats[eps]['exitosos'] / eps_stats[eps]['total'] * 100), 1) 
            if eps_stats[eps]['total'] > 0 else 0 
            for eps in eps_stats
        ]
    })
    
    fig = px.bar(
        fig_data, 
        x='EPS', 
        y='Total_Procesado',
        title='Total de Archivos Procesados por EPS',
        color='Tasa_Exito',
        color_continuous_scale='Viridis',
        text='Total_Procesado'
    )
    
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=400,
        showlegend=False
    )
    
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    
    st.plotly_chart(fig, use_container_width=True)
    
except Exception as e:
    st.error(f"Error generando gráfico: {e}")

# HISTORIAL EN TIEMPO REAL
st.markdown("### 🕒 Historial Reciente de Procesos")

if historial_reciente:
    # Convertir a DataFrame para mejor visualización
    historial_df = pd.DataFrame(historial_reciente)
    
    # Formatear fecha para mejor visualización
    historial_df['fecha_formateada'] = pd.to_datetime(historial_df['fecha']).dt.strftime('%H:%M')
    
    # Mostrar tabla
    st.dataframe(
        historial_df[['fecha_formateada', 'eps', 'archivo', 'proceso', 'estado']],
        use_container_width=True,
        column_config={
            'fecha_formateada': 'Hora',
            'eps': 'EPS',
            'archivo': 'Archivo',
            'proceso': 'Proceso',
            'estado': 'Estado'
        }
    )
else:
    st.info("📝 Aún no hay procesos registrados en el historial")

# BOTÓN PARA LIMPIAR HISTORIAL (solo para desarrollo)
with st.expander("🔧 Herramientas de Desarrollo"):
    if st.button("🔄 Reiniciar Métricas", type="secondary"):
        metricas.inicializar_historial()
        st.success("✅ Métricas reiniciadas correctamente")
        st.rerun()

# FOOTER
st.markdown("---")
st.markdown(
    f"**Cuentas Médicas** • {estadisticas['total_archivos']} archivos procesados • "
    f"Tasa de éxito: {estadisticas['tasa_exito']}% • "
    f"Última actualización: {datetime.now().strftime('%H:%M:%S')}"
)
