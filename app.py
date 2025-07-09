from flask import Flask, render_template
from flask import send_file
from exportar_excel import generar_excel
import platform
import psutil
import wmi
import speedtest
import pythoncom

app = Flask(__name__)

@app.route("/descargar_excel")
def descargar_excel():
    archivo = generar_excel()
    return send_file(archivo, as_attachment=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    # Inicializar COM para usar WMI en entorno web
    pythoncom.CoInitialize()

    # Hardware
    w = wmi.WMI()
    cpu = w.Win32_Processor()[0].Name.strip()
    so = platform.system() + " " + platform.release()
    arquitectura = platform.architecture()[0]
    nucleos_fisicos = psutil.cpu_count(logical=False)
    nucleos_logicos = psutil.cpu_count(logical=True)
    ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    disco = round(psutil.disk_usage('/').total / (1024 ** 3), 2)

    estado_hardware = "APROBADO"
    if ram < 4 or disco < 256 or not any(x in cpu.lower() for x in ["i3", "i5", "i7"]):
        estado_hardware = "RECHAZADO"

    # Internet
    st = speedtest.Speedtest()
    st.get_best_server()
    descarga = round(st.download() / (1024 ** 2), 2)
    carga = round(st.upload() / (1024 ** 2), 2)
    latencia = round(st.results.ping, 2)

    estado_internet = "APROBADO"
    if descarga < 25 or carga < 10 or latencia > 30:
        estado_internet = "RECHAZADO"

    return render_template("resultado.html",
                           so=so,
                           arquitectura=arquitectura,
                           procesador=cpu,
                           nucleos_fisicos=nucleos_fisicos,
                           nucleos_logicos=nucleos_logicos,
                           ram=ram,
                           disco=disco,
                           estado_hardware=estado_hardware,
                           descarga=descarga,
                           carga=carga,
                           latencia=latencia,
                           estado_internet=estado_internet
                           )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
