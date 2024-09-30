  // Función para cambiar el texto del párrafo
  function cambiarTexto() {
    const texto = document.getElementById('miTexto');
    texto.textContent = '¡El texto ha sido cambiado con JavaScript!';
}

// Función para cambiar el color del texto del párrafo
function cambiarColor() {
    const texto = document.getElementById('miTexto');
    texto.style.color = texto.style.color === 'red' ? 'black' : 'red'; // Alterna entre rojo y negro
}

// Función para agregar un nuevo elemento a la lista
function agregarElemento() {
    const lista = document.getElementById('miLista');
    const nuevoElemento = document.createElement('li');
    nuevoElemento.textContent = `Elemento ${lista.children.length + 1}`;
    lista.appendChild(nuevoElemento);
}

// Función para eliminar el último elemento de la lista
function eliminarElemento() {
    const lista = document.getElementById('miLista');
    if (lista.children.length > 0) {
        lista.removeChild(lista.lastElementChild);
    } else {
        alert('No hay más elementos para eliminar.');
    }
}

