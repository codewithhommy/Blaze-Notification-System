import pandas as pd
import os
import json

def generate_ros_json(row):
    """Genera un reporte ROS en formato JSON para cada alerta detectada."""
    report_data = {
        "metadata": {
            "sistema": "SENTINEL-AML-V1",
            "tipo_reporte": "ROS_AUTOMATIZADO"
        },
        "sujeto": {
            "cliente_id": int(row['id_cliente']),
            "monto_operacion": float(row['monto']),
            "limite_perfil": float(row['limite_autorizado'])
        },
        "analisis": "Detección por exceso de límite transaccional histórico."
    }
    
    file_path = f"reports/ros_reports/ROS_CLIENTE_{int(row['id_cliente'])}.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=4, ensure_ascii=False)

def run_aml_check(input_file):
    print(f"[+] Leyendo archivo: {input_file}")
    df = pd.read_csv(input_file)
    
    # Creamos las carpetas necesarias
    os.makedirs('reports/ros_reports', exist_ok=True)
    
    # Identificamos alertas
    alertas = df[df['monto'] > df['limite_autorizado']]
    
    # Generamos los ROS para cada alerta encontrada
    for index, row in alertas.iterrows():
        generate_ros_json(row)
        print(f"[!] Archivo ROS generado para: {int(row['id_cliente'])}")
    
    print(f"[*] Proceso completado. Alertas detectadas: {len(alertas)}")

if __name__ == "__main__":
    archivo = 'data/transaction_input.csv'
    if os.path.exists(archivo):
        run_aml_check(archivo)
    else:
        print(f"[!] Error: No se encuentra el archivo {archivo}")
