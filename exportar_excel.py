import pandas as pd
from datetime import datetime
from detector_equipo import evaluar_equipo
from detector_internet import evaluar_internet

def generar_excel():
    equipo = evaluar_equipo()
    internet = evaluar_internet()
    nombre_archivo = "resultado_validacion.xlsx"

    datos = {
        "Sistema Operativo": [equipo["sistema_operativo"]],
        "Arquitectura": [equipo["arquitectura"]],
        "Procesador": [equipo["procesador"]],
        "Núcleos físicos": [equipo["nucleos_fisicos"]],
        "Núcleos lógicos": [equipo["nucleos_logicos"]],
        "RAM (GB)": [equipo["ram"]],
        "Disco (GB)": [equipo["disco"]],
        "Estado del equipo": [equipo["estado"]],
        "Descarga (Mbps)": [internet["descarga"]],
        "Carga (Mbps)": [internet["carga"]],
        "Latencia (ms)": [internet["latencia"]],
        "Estado de internet": [internet["estado_internet"]],
        "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    }

    df = pd.DataFrame(datos)
    df.to_excel(nombre_archivo, index=False)
    return nombre_archivo

