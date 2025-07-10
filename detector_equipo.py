import platform
import psutil

def evaluar_equipo():
    sistema_operativo = platform.system() + " " + platform.release()
    arquitectura = platform.architecture()[0]

    try:
        procesador = platform.processor()
        if not procesador:
            procesador = "Intel o AMD multinúcleo"
    except Exception:
        procesador = "No detectado"

    try:
        nucleos_fisicos = psutil.cpu_count(logical=False)
        nucleos_logicos = psutil.cpu_count(logical=True)
    except Exception:
        nucleos_fisicos = nucleos_logicos = "No detectado"

    try:
        ram = round(psutil.virtual_memory().total / (1024**3), 1)  # En GB
    except Exception:
        ram = "No detectado"

    try:
        disco = round(psutil.disk_usage('/').total / (1024**3), 2)  # En GB
    except Exception:
        disco = "No detectado"

    estado = "APROBADO"
    if not (
        ("i3" in procesador.lower() or "i5" in procesador.lower() or "i7" in procesador.lower() or "ryzen" in procesador.lower())
        and "6" in plataforma_generacion(procesador)
        and isinstance(ram, (int, float)) and ram >= 4
        and isinstance(disco, (int, float)) and disco >= 256
    ):
        estado = "RECHAZADO"

    return {
        "sistema_operativo": sistema_operativo,
        "arquitectura": arquitectura,
        "procesador": procesador,
        "nucleos_fisicos": nucleos_fisicos,
        "nucleos_logicos": nucleos_logicos,
        "ram": ram,
        "disco": disco,
        "estado": estado
    }

def plataforma_generacion(procesador):
    # Función auxiliar para detectar generación desde nombre
    if "i3-6" in procesador or "i5-6" in procesador or "i7-6" in procesador:
        return "6"
    elif "i3-7" in procesador or "i5-7" in procesador or "i7-7" in procesador:
        return "7"
    elif "i3-8" in procesador or "i5-8" in procesador or "i7-8" in procesador:
        return "8"
    elif "i3-9" in procesador or "i5-9" in procesador or "i7-9" in procesador:
        return "9"
    else:
        return "desconocida"

