function modificarDOM(){

    const parrafo=document.getElementById('parrafo');
    parrafo.textContent = 'El contenido ha sido modificado';

    //vamos a cambiar el estilo añadiento una clase css
    parrafo.classList.add('cambiocss');

    //crear un nuevo parrafo
    const nuevoparrafo=document.createElement('p');
    nuevoparrafo.textContent = 'Este es el nuevo parrafo';
    document.body.appendChild(nuevoparrafo);
}





