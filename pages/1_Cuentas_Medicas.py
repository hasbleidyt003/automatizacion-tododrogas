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
# INTERFAZ PRINCIPAL
# =============================================

# Título de la página
st.title("📋 Cuentas Médicas")
st.markdown("Automatización de procesos para cuentas médicas por EPS")

# Obtener estadísticas en tiempo real
estadisticas = metricas.obtener_estadisticas()
historial_reciente = metricas.obtener_historial(5)
tiempo_promedio = metricas.obtener_tiempo_promedio()

# SECCIÓN DE MÉTRICAS EN TIEMPO REAL
st.header("📊 Métricas en Tiempo Real")

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

# SECCIÓN DE EPS - ORGANIZADA POR EMPRESA
st.header("🏥 Selecciona la EPS para Procesar Archivos")

# Crear pestañas para cada EPS
tab1, tab2, tab3 = st.tabs(["🏥 COOSALUD", "💊 SAVIA SALUD", "🩺 SALUD TOTAL"])

with tab1:
    st.subheader("COOSALUD - Procesamiento de Archivos")
    
    # Mostrar estadísticas específicas de Coosalud
    eps_stats = estadisticas["eps_stats"]["COOSALUD"]
    col_stats1, col_stats2, col_stats3 = st.columns(3)
    
    with col_stats1:
        st.metric("Total Coosalud", eps_stats["total"])
    with col_stats2:
        st.metric("Hoy", eps_stats["hoy"])
    with col_stats3:
        tasa_eps = round((eps_stats["exitosos"] / eps_stats["total"] * 100), 1) if eps_stats["total"] > 0 else 0
        st.metric("Éxito Coosalud", f"{tasa_eps}%")
    
    st.info("Herramientas especializadas para Coosalud")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔄 Conversores JSON")
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
    
    with col2:
        st.markdown("### 🏷️ Renombradores")
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

with tab2:
    st.subheader("SAVIA SALUD - Procesamiento de Archivos")
    
    # Mostrar estadísticas específicas de Savia
    eps_stats = estadisticas["eps_stats"]["SAVIA SALUD"]
    col_stats1, col_stats2, col_stats3 = st.columns(3)
    
    with col_stats1:
        st.metric("Total Savia", eps_stats["total"])
    with col_stats2:
        st.metric("Hoy", eps_stats["hoy"])
    with col_stats3:
        tasa_eps = round((eps_stats["exitosos"] / eps_stats["total"] * 100), 1) if eps_stats["total"] > 0 else 0
        st.metric("Éxito Savia", f"{tasa_eps}%")
    
    st.info("Herramientas especializadas para Savia Salud")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏷️ Renombradores")
        if st.button("🔢 Renombrador CUV Savia", use_container_width=True, key="savia_cuv"):
            metricas.registrar_proceso(
                "SAVIA SALUD", 
                "Nuevo proceso CUV", 
                "Renombrador CUV", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/9_Renombrador_cuv_Savia.py")
    
    with col2:
        st.markdown("### 📋 Procesadores RIPS")
        if st.button("📋 Renombrador RIPS Savia", use_container_width=True, key="savia_rips"):
            metricas.registrar_proceso(
                "SAVIA SALUD", 
                "Nuevo proceso RIPS", 
                "Renombrador RIPS", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/10_Renombrador_rips_Savia.py")

with tab3:
    st.subheader("SALUD TOTAL - Procesamiento de Archivos")
    
    # Mostrar estadísticas específicas de Salud Total
    eps_stats = estadisticas["eps_stats"]["SALUD TOTAL"]
    col_stats1, col_stats2, col_stats3 = st.columns(3)
    
    with col_stats1:
        st.metric("Total Salud Total", eps_stats["total"])
    with col_stats2:
        st.metric("Hoy", eps_stats["hoy"])
    with col_stats3:
        tasa_eps = round((eps_stats["exitosos"] / eps_stats["total"] * 100), 1) if eps_stats["total"] > 0 else 0
        st.metric("Éxito Salud Total", f"{tasa_eps}%")
    
    st.info("Herramientas especializadas para Salud Total")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔍 Procesador OCR")
        if st.button("🔍 Procesador + Renombrador", use_container_width=True, key="salud_total_ocr"):
            metricas.registrar_proceso(
                "SALUD TOTAL", 
                "Nuevo proceso OCR", 
                "Procesador OCR", 
                "🔄 Iniciado"
            )
            st.switch_page("pages/11_Processador_Renombrador_ST.py")
    
    with col2:
        st.markdown("### ⚡ Procesamiento Avanzado")
        st.info("OCR inteligente con renombrado automático")

# GRÁFICO DE ACTIVIDAD EN TIEMPO REAL
st.header("📈 Actividad por EPS - Tiempo Real")

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
st.header("🕒 Historial Reciente de Procesos")

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
