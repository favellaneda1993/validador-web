async function detectarEquipo() {
    const info = {
        sistema: navigator.platform,
        arquitectura: navigator.userAgent.includes("x86_64") ? "64bit" : "32bit",
        ram: navigator.deviceMemory || 0,
        procesador: navigator.userAgent,
        nucleos: navigator.hardwareConcurrency || 1
    };

    const respuesta = await fetch('/evaluar_equipo', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(info)
    });

    const resultado = await respuesta.json();
    mostrarResultado(resultado);
}

function mostrarResultado(data) {
    document.getElementById("resultado").innerHTML = `
        <h3>Estado del equipo: ${data.estado}</h3>
        <pre>${JSON.stringify(data, null, 2)}</pre>
    `;
}

window.onload = detectarEquipo;
