// Detectar equipo
document.getElementById('so').textContent = navigator.platform;
document.getElementById('navegador').textContent = navigator.userAgent;
document.getElementById('arquitectura').textContent = navigator.userAgent.includes("Win64") || navigator.userAgent.includes("x86_64") ? "64 bits" : "32 bits";
document.getElementById('ram').textContent = navigator.deviceMemory ? `${navigator.deviceMemory} GB` : 'No disponible';

// Medir velocidad de descarga
async function medirInternet() {
  const start = new Date().getTime();
  try {
    const response = await fetch("https://speed.hetzner.de/100MB.bin", { method: 'GET', cache: 'no-cache' });
    const end = new Date().getTime();
    const duration = (end - start) / 1000;
    const bitsLoaded = 100 * 1024 * 1024 * 8;
    const speedMbps = (bitsLoaded / duration / 1024 / 1024).toFixed(2);
    document.getElementById('download').textContent = `${speedMbps} Mbps`;
  } catch {
    document.getElementById('download').textContent = "Error al medir";
  }

  // Simulación de carga
  setTimeout(() => {
    document.getElementById('upload').textContent = "2.5 Mbps (simulado)";
    document.getElementById('latency').textContent = "42 ms (simulado)";
  }, 1000);
}

medirInternet();
