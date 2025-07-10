import subprocess
import re

def ejecutar_comando(comando):
    try:
        resultado = subprocess.check_output(comando, shell=True, text=True)
        return resultado.strip()
    except Exception as e:
        return str(e)

def evaluar_internet():
    descarga = medir_descarga()
    carga = 10  # Valor fijo aproximado en Render (sin pruebas reales)
    latencia = medir_latencia()

    estado = "APROBADO"
    if descarga < 25 or carga < 10 or latencia > 30:
        estado = "RECHAZADO"

    return {
        "descarga": descarga,
        "carga": carga,
        "latencia": latencia,
        "estado_internet": estado
    }

def medir_descarga():
    try:
        resultado = ejecutar_comando("curl -s -w '%{speed_download}\\n' -o /dev/null https://speed.hetzner.de/100MB.bin")
        velocidad_bytes = float(resultado)
        velocidad_mbps = round(velocidad_bytes / 1024 / 1024, 2)  # Convertir a Mbps
        return velocidad_mbps
    except:
        return 0.0

def medir_latencia():
    try:
        resultado = ejecutar_comando("ping -c 1 8.8.8.8")
        match = re.search(r'time=(\d+\.?\d*) ms', resultado)
        if match:
            return float(match.group(1))
        return 999.0
    except:
        return 999.0
