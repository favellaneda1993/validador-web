(function () {
  try {
    // Obtener info avanzada del sistema cuando sea posible
    const hardwareInfo = {
      userAgent: navigator.userAgent,
      platform: navigator.platform,
      hardwareConcurrency: navigator.hardwareConcurrency || null,
      deviceMemory: navigator.deviceMemory || null,
      language: navigator.language,
      // Espacio para futuras APIs (Privacy-preserving):
      // gpu: navigator.gpu ? 'available' : 'unavailable'
    };

    // Exponer la información de forma segura en window bajo un namespace
    window.__VALIDADOR_HW__ = hardwareInfo;

    // Permitir a la página leer estos datos mediante un CustomEvent
    const event = new CustomEvent('validador-hw-ready', { detail: hardwareInfo });
    window.dispatchEvent(event);
  } catch (e) {
    console.error('Validador HW Helper error:', e);
  }
})();

