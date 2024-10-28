document.addEventListener("DOMContentLoaded", function () {
    // Obtener el formulario y el campo de edad
    const form = document.querySelector("form");
    const edadInput = document.getElementById("edad");

    // Agregar un evento de validación al enviar el formulario
    form.addEventListener("submit", function (event) {
        const edad = parseInt(edadInput.value, 10);

        // Validar que la edad esté en el rango válido
        if (isNaN(edad) || edad < 1 || edad > 120) {
            alert("Por favor, ingrese una edad válida entre 1 y 120.");
            event.preventDefault(); // Evitar que el formulario se envíe
        }
    });
});
