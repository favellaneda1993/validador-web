# 🖥️ Validador de Equipos e Internet (Flask)

Este proyecto es una aplicación web construida con **Python Flask** que permite:

✅ Detectar automáticamente las características del equipo:
- Sistema operativo
- Arquitectura (32 o 64 bits)
- Procesador
- Núcleos físicos y lógicos
- Memoria RAM
- Almacenamiento total

✅ Evaluar la conexión a internet:
- Velocidad de descarga (Mbps)
- Velocidad de carga (estimada)
- Latencia (ms)

✅ Determinar si el equipo cumple con los requisitos mínimos:
- Procesador i3 6ta gen o superior (o Ryzen)
- RAM ≥ 4 GB
- Disco ≥ 256 GB
- Descarga ≥ 25 Mbps
- Carga ≥ 10 Mbps
- Latencia ≤ 30 ms

✅ Exportar los resultados a un archivo Excel

---

## 🌐 Despliegue en Render

La aplicación está adaptada para funcionar correctamente en servidores Linux como **Render.com**.

### Requisitos

- Python 3.x
- Flask
- pandas
- openpyxl

### Estructura

