import platform
import psutil
import wmi
import speedtest
import pythoncom
import pandas as pd

def generar_excel(nombre_archivo="resultado_validacion.xlsx"):
    pythoncom.CoInitialize()
    w = wmi.WMI()
    cpu = w.Win32_Processor()[0].Name.strip()
    so = platform.system() + " " + platform.release()
    arquitectura = platform.architecture()[0]
    nucleos_fisicos = psutil.cpu_count(logical=False)
    nucleos_logicos = psutil.cpu_count(logical=True)
    ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    disco = round(psutil.disk_usage('/').total / (1024 ** 3), 2)
    estado_hw = "APROBADO" if (ram >= 4 and disco >= 256 and any(x in cpu.lower() for x in ["i3", "i5", "i7"])) else "RECHAZADO"

    st = speedtest.Speedtest()
    st.get_best_server()
    descarga = round(st.download() / (1024 ** 2), 2)
    carga = round(st.upload() / (1024 ** 2), 2)
    latencia = round(st.results.ping, 2)
    estado_net = "APROBADO" if (descarga >= 25 and carga >= 10 and latencia <= 30) else "RECHAZADO"

    data = {
        "Sistema Operativo": [so],
        "Arquitectura": [arquitectura],
        "Procesador": [cpu],
        "Núcleos físicos": [nucleos_fisicos],
        "Núcleos lógicos": [nucleos_logicos],
        "RAM (GB)": [ram],
        "Disco (GB)": [disco],
        "Estado equipo": [estado_hw],
        "Descarga (Mbps)": [descarga],
        "Carga (Mbps)": [carga],
        "Latencia (ms)": [latencia],
        "Estado internet": [estado_net]
    }

    df = pd.DataFrame(data)
    df.to_excel(nombre_archivo, index=False)
    return nombre_archivo
