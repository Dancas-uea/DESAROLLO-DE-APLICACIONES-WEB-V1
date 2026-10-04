document.addEventListener('DOMContentLoaded', function() {
    console.log('Aplicación Flask cargada correctamente.');
    
    // Función demostrativa para simular interactividad local
    const alertBox = document.getElementById('demoAlert');
    if (alertBox) {
        setTimeout(() => {
            alertBox.classList.add('fade');
        }, 5000);
    }
});