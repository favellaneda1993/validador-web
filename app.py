from flask import Flask, render_template, jsonify, send_file
import psutil
import platform
import speedtest
import os
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
import io

app = Flask(__name__)

def obtener_caracteristicas_equipo():
    """Obtiene las características del equipo"""
    try:
        # Información del sistema
        sistema = platform.system()
        version = platform.version()
        arquitectura = platform.architecture()[0]
        
        # Información del procesador
        procesador = platform.processor()
        nucleos_fisicos = psutil.cpu_count(logical=False)
        nucleos_logicos = psutil.cpu_count(logical=True)
        
        # Información de memoria
        memoria = psutil.virtual_memory()
        ram_gb = round(memoria.total / (1024**3), 1)
        
        # Información del disco
        disco = psutil.disk_usage('/')
        disco_gb = round(disco.total / (1024**3), 2)
        
        # Evaluar estado del equipo (simplificado)
        estado_equipo = "APROBADO" if ram_gb >= 4 and nucleos_fisicos >= 2 else "RECHAZADO"
        
        return {
            'sistema_operativo': f"{sistema} {version}",
            'arquitectura': arquitectura,
            'procesador': procesador,
            'nucleos_fisicos': nucleos_fisicos,
            'nucleos_logicos': nucleos_logicos,
            'ram': f"{ram_gb} GB",
            'disco': f"{disco_gb} GB",
            'estado_equipo': estado_equipo
        }
    except Exception as e:
        return {
            'error': f"Error al obtener características del equipo: {str(e)}"
        }

def medir_velocidad_internet():
    """Mide la velocidad de internet"""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        
        # Medir velocidad de descarga
        velocidad_descarga = st.download() / 1_000_000  # Convertir a Mbps
        
        # Medir velocidad de carga
        velocidad_carga = st.upload() / 1_000_000  # Convertir a Mbps
        
        # Obtener latencia
        latencia = st.results.ping
        
        # Evaluar estado de internet
        estado_internet = "APROBADO" if velocidad_descarga >= 10 and velocidad_carga >= 5 else "RECHAZADO"
        
        return {
            'velocidad_descarga': round(velocidad_descarga, 2),
            'velocidad_carga': round(velocidad_carga, 2),
            'latencia': round(latencia, 2),
            'estado_internet': estado_internet
        }
    except Exception as e:
        return {
            'error': f"Error al medir velocidad de internet: {str(e)}"
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluar')
def evaluar():
    """Endpoint para realizar la evaluación completa"""
    caracteristicas = obtener_caracteristicas_equipo()
    velocidad = medir_velocidad_internet()
    
    return jsonify({
        'equipo': caracteristicas,
        'internet': velocidad
    })

@app.route('/exportar-excel')
def exportar_excel():
    """Exporta los resultados a un archivo Excel"""
    try:
        # Obtener datos
        caracteristicas = obtener_caracteristicas_equipo()
        velocidad = medir_velocidad_internet()
        
        # Crear workbook
        wb = Workbook()
        ws = wb.active
        ws.title = "Resultado Evaluación"
        
        # Estilos
        titulo_font = Font(bold=True, size=14, color="FFFFFF")
        subtitulo_font = Font(bold=True, size=12)
        header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
        green_fill = PatternFill(start_color="70AD47", end_color="70AD47", fill_type="solid")
        
        # Título principal
        ws['A1'] = "RESULTADO DE EVALUACIÓN"
        ws['A1'].font = titulo_font
        ws['A1'].fill = header_fill
        ws.merge_cells('A1:C1')
        
        # Fecha
        ws['A2'] = f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        ws.merge_cells('A2:C2')
        
        # Evaluación del Equipo
        ws['A4'] = "EVALUACIÓN DEL EQUIPO"
        ws['A4'].font = subtitulo_font
        ws['A4'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
        ws['A4'].font = Font(bold=True, color="FFFFFF")
        ws.merge_cells('A4:C4')
        
        # Datos del equipo
        datos_equipo = [
            ["Sistema Operativo", caracteristicas.get('sistema_operativo', 'N/A')],
            ["Arquitectura", caracteristicas.get('arquitectura', 'N/A')],
            ["Procesador", caracteristicas.get('procesador', 'N/A')],
            ["Núcleos físicos", caracteristicas.get('nucleos_fisicos', 'N/A')],
            ["Núcleos lógicos", caracteristicas.get('nucleos_logicos', 'N/A')],
            ["RAM", caracteristicas.get('ram', 'N/A')],
            ["Disco", caracteristicas.get('disco', 'N/A')],
            ["Estado del equipo", caracteristicas.get('estado_equipo', 'N/A')]
        ]
        
        for i, (campo, valor) in enumerate(datos_equipo, start=5):
            ws[f'A{i}'] = campo
            ws[f'B{i}'] = valor
            if campo == "Estado del equipo":
                if valor == "APROBADO":
                    ws[f'B{i}'].fill = green_fill
                    ws[f'B{i}'].font = Font(bold=True, color="FFFFFF")
        
        # Evaluación de Internet
        ws['A14'] = "EVALUACIÓN DE INTERNET"
        ws['A14'].font = subtitulo_font
        ws['A14'].fill = PatternFill(start_color="70AD47", end_color="70AD47", fill_type="solid")
        ws['A14'].font = Font(bold=True, color="FFFFFF")
        ws.merge_cells('A14:C14')
        
        # Datos de internet
        datos_internet = [
            ["Velocidad de descarga", f"{velocidad.get('velocidad_descarga', 'N/A')} Mbps"],
            ["Velocidad de carga", f"{velocidad.get('velocidad_carga', 'N/A')} Mbps"],
            ["Latencia", f"{velocidad.get('latencia', 'N/A')} ms"],
            ["Estado de internet", velocidad.get('estado_internet', 'N/A')]
        ]
        
        for i, (campo, valor) in enumerate(datos_internet, start=15):
            ws[f'A{i}'] = campo
            ws[f'B{i}'] = valor
            if campo == "Estado de internet":
                if valor == "APROBADO":
                    ws[f'B{i}'].fill = green_fill
                    ws[f'B{i}'].font = Font(bold=True, color="FFFFFF")
        
        # Ajustar ancho de columnas
        ws.column_dimensions['A'].width = 25
        ws.column_dimensions['B'].width = 30
        
        # Guardar en memoria
        excel_file = io.BytesIO()
        wb.save(excel_file)
        excel_file.seek(0)
        
        return send_file(
            excel_file,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=f'evaluacion_equipo_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
        )
        
    except Exception as e:
        return jsonify({'error': f'Error al exportar Excel: {str(e)}'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

