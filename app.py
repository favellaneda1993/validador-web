from flask import Flask, render_template, send_file
from exportar_excel import generar_excel
from detector_equipo import evaluar_equipo
from detector_internet import evaluar_internet
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    equipo = evaluar_equipo()
    internet = evaluar_internet()
    return render_template('resultado.html', equipo=equipo, internet=internet)

@app.route('/descargar_excel')
def descargar_excel():
    archivo = generar_excel()
    return send_file(archivo, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
