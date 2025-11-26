import os
import re
import argparse
from pathlib import Path

def renombrar_archivos_savia(carpeta_base=None):
    """
    Renombra archivos RIPS para SAVIA eliminando prefijos específicos
    - Elimina "FEV_830500960_"
    - Elimina "_" antes de "NE"
    
    Args:
        carpeta_base (str): Ruta de la carpeta con archivos a renombrar. 
                           Si es None, usa el directorio actual.
    
    Returns:
        dict: Estadísticas del proceso
    """
    # Usar carpeta actual si no se especifica
    if carpeta_base is None:
        CARPETA = Path.cwd()
    else:
        CARPETA = Path(carpeta_base)
    
    print(f"🔄 Renombrando archivos en: {CARPETA}")
    print("-" * 50)
    
    # Verificar si la carpeta existe
    if not CARPETA.exists():
        print(f"❌ Error: La carpeta '{CARPETA}' no existe.")
        return {"renombrados": 0, "errores": 1, "total": 0}
    
    contador = 0
    total_archivos = 0
    
    # Expresión regular: busca "NE" seguido de números
    patron = re.compile(r"NE\d+")
    
    for archivo in os.listdir(CARPETA):
        ruta_completa = CARPETA / archivo
        total_archivos += 1

        if os.path.isfile(ruta_completa):
            # Solo procesar archivos que contengan "NE" seguido de números
            if patron.search(archivo):
                nuevo_nombre = archivo

                # 1️⃣ Eliminar "FEV_830500960_"
                nuevo_nombre = nuevo_nombre.replace("FEV_830500960_", "")

                # 2️⃣ Eliminar "_" justo antes de "NE"
                nuevo_nombre = re.sub(r"_+(?=NE\d+)", "", nuevo_nombre)

                # Quitar espacios sobrantes
                nuevo_nombre = nuevo_nombre.strip()

                # Si el nombre cambió, renombrar
                if nuevo_nombre != archivo:
                    nueva_ruta = CARPETA / nuevo_nombre
                    try:
                        os.rename(ruta_completa, nueva_ruta)
                        print(f"✅ Renombrado: {archivo} -> {nuevo_nombre}")
                        contador += 1
                    except Exception as e:
                        print(f"❌ Error renombrando {archivo}: {str(e)}")
                else:
                    print(f"ℹ️  Sin cambios: {archivo}")
            else:
                print(f"📄 Archivo sin 'NE' seguido de números: {archivo} (no se renombra)")

    print("-" * 50)
    print(f"📊 Procesamiento completado.")
    print(f"   • Total archivos revisados: {total_archivos}")
    print(f"   • Archivos renombrados: {contador}")
    
    return {"renombrados": contador, "errores": 0, "total": total_archivos}

def main():
    """Función principal con interfaz de línea de comandos"""
    parser = argparse.ArgumentParser(description='Renombrador RIPS SAVIA - Elimina prefijos de archivos')
    parser.add_argument('--carpeta', '-c', type=str, 
                       help='Ruta de la carpeta a procesar (por defecto: directorio actual)')
    parser.add_argument('--interactivo', '-i', action='store_true',
                       help='Modo interactivo (espera entrada del usuario al final)')
    
    args = parser.parse_args()
    
    # Ejecutar el renombrador
    resultados = renombrar_archivos_savia(args.carpeta)
    
    # Esperar entrada si está en modo interactivo
    if args.interactivo:
        input("\n⏎ Presiona Enter para continuar...")
    
    return resultados

if __name__ == "__main__":
    main()
