# Validador Web - Evaluación de Equipo e Internet

Este proyecto es una aplicación web que valida las características del equipo y la velocidad de internet, mostrando los resultados en una interfaz moderna y permitiendo exportar los datos a Excel.

## Características

### Evaluación del Equipo
- **Sistema Operativo**: Detecta el SO y versión
- **Arquitectura**: 32 o 64 bits
- **Procesador**: Información del CPU
- **Núcleos físicos y lógicos**: Cantidad de cores
- **RAM**: Memoria total disponible
- **Disco**: Espacio total en disco
- **Estado**: Aprobado/Rechazado según criterios

### Evaluación de Internet
- **Velocidad de descarga**: Mbps
- **Velocidad de carga**: Mbps
- **Latencia**: Ping en milisegundos
- **Estado**: Aprobado/Rechazado según velocidad mínima

### Funcionalidades
- ✅ Interfaz moderna y responsiva
- ✅ Evaluación automática al cargar
- ✅ Botón para re-evaluar
- ✅ Exportación a Excel con formato profesional
- ✅ Indicadores visuales de estado (APROBADO/RECHAZADO)

## Instalación Local

1. **Clonar el repositorio**:
```bash
git clone <url-del-repositorio>
cd validador-web
```

2. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

3. **Ejecutar la aplicación**:
```bash
python app.py
```

4. **Abrir en el navegador**:
```
http://localhost:5000
```

## 🚀 Despliegue en la Nube (Recomendado)

### Opción 1: Render (Gratuito)

1. **Crear cuenta en Render**:
   - Ve a [render.com](https://render.com) y crea una cuenta gratuita

2. **Conectar repositorio**:
   - Haz clic en "New +" → "Web Service"
   - Conecta tu repositorio de GitHub
   - Selecciona el repositorio `validador-web`

3. **Configurar el servicio**:
   - **Name**: `validador-web` (o el nombre que prefieras)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`

4. **Desplegar**:
   - Haz clic en "Create Web Service"
   - Render te dará una URL como: `https://tu-app.onrender.com`

### Opción 2: Heroku (Gratuito)

1. **Instalar Heroku CLI**:
   ```bash
   # Windows
   winget install --id=Heroku.HerokuCLI
   
   # macOS
   brew tap heroku/brew && brew install heroku
   ```

2. **Crear aplicación**:
   ```bash
   heroku login
   heroku create tu-validador-web
   ```

3. **Desplegar**:
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

4. **Abrir aplicación**:
   ```bash
   heroku open
   ```

### Opción 3: Railway (Gratuito)

1. **Crear cuenta en Railway**:
   - Ve a [railway.app](https://railway.app) y crea una cuenta

2. **Conectar repositorio**:
   - Haz clic en "New Project" → "Deploy from GitHub repo"
   - Selecciona tu repositorio

3. **Configurar**:
   - Railway detectará automáticamente que es una app Python
   - Se desplegará automáticamente

4. **Obtener URL**:
   - Railway te dará una URL automáticamente

## 🐳 Ejecutar con Docker

### Requisitos
- Docker y Docker Compose instalados

### Construir y ejecutar con Docker

```bash
# Construir la imagen
docker build -t validador-web:latest .

# Ejecutar el contenedor
docker run --rm -p 5000:5000 --name validador-web validador-web:latest
```

### Usar docker-compose

```bash
docker-compose up --build
```

Luego abre: `http://localhost:5000`

## Dependencias

- **Flask**: Framework web
- **psutil**: Información del sistema
- **speedtest-cli**: Medición de velocidad de internet
- **openpyxl**: Generación de archivos Excel

## Uso

1. **Evaluación automática**: Al abrir la página, se realiza automáticamente la evaluación
2. **Re-evaluar**: Usar el botón "Volver a evaluar" para realizar una nueva medición
3. **Exportar Excel**: Hacer clic en "Exportar resultado a Excel" para descargar el reporte

## 🌐 Compartir el Enlace

Una vez desplegado, puedes compartir el enlace con cualquier persona:

- **Ejemplo de URL**: `https://tu-validador-web.onrender.com`
- **Cualquier usuario** puede acceder desde cualquier dispositivo
- **No requiere instalación** - funciona directamente en el navegador
- **Compatible** con Windows, macOS, Linux, Android, iOS

### Cómo compartir:

1. **Copiar la URL** de tu aplicación desplegada
2. **Compartir por**:
   - Email
   - WhatsApp
   - Telegram
   - Slack
   - Cualquier red social
3. **Los usuarios** solo necesitan hacer clic en el enlace

## Criterios de Evaluación

### Equipo (APROBADO si):
- RAM ≥ 4 GB
- Núcleos físicos ≥ 2

### Internet (APROBADO si):
- Velocidad de descarga ≥ 10 Mbps
- Velocidad de carga ≥ 5 Mbps

## Estructura del Proyecto

```
validador-web/
├── app.py              # Aplicación principal Flask
├── requirements.txt    # Dependencias Python
├── README.md          # Documentación
├── Procfile           # Configuración para Heroku
├── templates/
│   └── index.html     # Template principal
└── static/            # Archivos estáticos (si los hay)
```

## Tecnologías Utilizadas

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Librerías**: psutil, speedtest-cli, openpyxl
- **Estilos**: CSS personalizado con gradientes y animaciones

## Notas Importantes

- La medición de velocidad de internet puede tomar varios segundos
- Se requiere conexión a internet para la medición de velocidad
- El archivo Excel se genera con formato profesional y colores
- La aplicación es responsiva y funciona en dispositivos móviles

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
