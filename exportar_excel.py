import pandas as pd
from io import BytesIO

def generar_excel(equipo, internet):
    data = {
        "Evaluación": ["Sistema Operativo", "Arquitectura", "Procesador", "Núcleos físicos", "Núcleos lógicos", "RAM", "Disco", "Estado del equipo",
                       "Velocidad de descarga", "Velocidad de carga", "Latencia", "Estado del internet"],
        "Resultado": [
            equipo.get("sistema_operativo", ""),
            equipo.get("arquitectura", ""),
            equipo.get("procesador", ""),
            equipo.get("nucleos_fisicos", ""),
            equipo.get("nucleos_logicos", ""),
            equipo.get("ram", ""),
            equipo.get("disco", ""),
            equipo.get("estado", ""),
            internet.get("velocidad_descarga", ""),
            internet.get("velocidad_carga", ""),
            internet.get("latencia", ""),
            internet.get("estado", "")
        ]
    }

    df = pd.DataFrame(data)

    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name="Evaluación")

    output.seek(0)
    return output

