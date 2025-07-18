# Validador Web

Este proyecto muestra las características del sistema y velocidad de internet del dispositivo en tiempo real desde cualquier navegador. No guarda datos.

## Cómo ejecutar localmente

1. Instala Flask:

pip install flask

2. Ejecuta la app:
python app.py
less
Copiar
Editar

Luego abre en tu navegador: http://localhost:5000

## Despliegue en Render

1. Sube este repositorio a GitHub.
2. Ve a [https://render.com](https://render.com)
3. Crea un nuevo "Web Service" desde tu repositorio.
4. Selecciona:
   - Runtime: Python 3.x
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`
5. Render te dará un enlace público.
