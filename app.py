from flask import Flask, render_template, request, jsonify
from exportar_excel import generar_excel

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    datos = request.get_json()
    equipo = datos.get('equipo', {})
    internet = datos.get('internet', {})

    # Evaluación simple de criterios
    estado_equipo = "APROBADO" if (
        equipo.get('ram', 0) >= 8 and
        equipo.get('disco', 0) >= 100 and
        equipo.get('nucleos_fisicos', 0) >= 4
    ) else "RECHAZADO"

    estado_internet = "APROBADO" if (
        internet.get('velocidad_descarga', 0) >= 10 and
        internet.get('latencia', 999) <= 100
    ) else "RECHAZADO"

    return jsonify({
        "equipo": equipo,
        "internet": internet,
        "estado_equipo": estado_equipo,
        "estado_internet": estado_internet
    })

@app.route('/descargar_excel', methods=['POST'])
def descargar_excel():
    datos = request.get_json()
    archivo = generar_excel(datos)
    return archivo

if __name__ == '__main__':
    app.run(debug=True)
    
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
