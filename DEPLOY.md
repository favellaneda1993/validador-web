# 🚀 Despliegue Rápido - Validador Web

## Opción Más Fácil: Render (5 minutos)

### 1. Preparar el repositorio
```bash
# Asegúrate de que todos los archivos estén en GitHub
git add .
git commit -m "Ready for deployment"
git push origin main
```

### 2. Desplegar en Render
1. Ve a [render.com](https://render.com)
2. Crea cuenta gratuita
3. Haz clic en "New +" → "Web Service"
4. Conecta tu repositorio de GitHub
5. Selecciona `validador-web`
6. Configura:
   - **Name**: `validador-web`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
7. Haz clic en "Create Web Service"

### 3. ¡Listo!
- Tu URL será: `https://tu-app.onrender.com`
- Compártela con quien quieras

## Alternativa: Railway (3 minutos)

1. Ve a [railway.app](https://railway.app)
2. Crea cuenta
3. "New Project" → "Deploy from GitHub repo"
4. Selecciona tu repositorio
5. ¡Automático!

## Verificar que funciona

1. Abre la URL en tu navegador
2. Deberías ver "Resultado de Evaluación"
3. La evaluación se ejecuta automáticamente
4. Prueba el botón "Exportar resultado a Excel"

## Solución de problemas

### Error: "Module not found"
- Verifica que `requirements.txt` tenga todas las dependencias
- Render/Railway instalará automáticamente

### Error: "Port already in use"
- El archivo `app.py` ya está configurado para usar la variable `PORT`
- No debería dar problemas

### La app no carga
- Revisa los logs en Render/Railway
- Verifica que el repositorio esté actualizado

## Compartir

Una vez desplegado, comparte la URL:
- **Email**: Copia y pega la URL
- **WhatsApp**: Envía el enlace
- **Redes sociales**: Publica la URL

¡Cualquier persona puede usar tu validador desde cualquier dispositivo! 