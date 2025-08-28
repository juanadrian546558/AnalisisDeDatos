# analisis.py
# Script básico de análisis de datos en Python

import pandas as pd

def cargar_datos(ruta_csv):
    """Carga un archivo CSV y devuelve un DataFrame de pandas."""
    try:
        df = pd.read_csv(ruta_csv)
        print("✅ Datos cargados correctamente")
        return df
    except Exception as e:
        print(f"❌ Error al cargar datos: {e}")
        return None

def resumen_datos(df):
    """Imprime un resumen rápido de los datos."""
    print("\n--- Información del DataFrame ---")
    print(df.info())
    print("\n--- Primeras filas ---")
    print(df.head())
    print("\n--- Estadísticas descriptivas ---")
    print(df.describe())

if __name__ == "__main__":
    # Cambia esta ruta por el archivo que quieras analizar
    ruta = "datos.csv"
    df = cargar_datos(ruta)

    if df is not None:
        resumen_datos(df)
