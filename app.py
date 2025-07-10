from flask import Flask, request, render_template, jsonify
from exportar_excel import generar_excel

app = Flask(__name__)

resultado = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluar', methods=['POST'])
def evaluar():
    global resultado
    datos = request.json
    resultado = datos

    # Evaluación simple
    resultado["estado_equipo"] = "APROBADO" if float(datos.get("ram", 0)) >= 4 else "RECHAZADO"
    resultado["estado_internet"] = "APROBADO" if float(datos.get("velocidad_descarga", 0)) >= 5 else "RECHAZADO"
    return jsonify({"estado": "OK"})

@app.route('/resultado')
def resultado_final():
    return render_template('resultado.html', **resultado)

@app.route('/descargar_excel')
def descargar_excel():
    archivo = generar_excel(resultado)
    return send_file(archivo, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
