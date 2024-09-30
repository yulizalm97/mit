const parrafo=document.getElementById('texto');

//cambiar el texto se usa la función setinterval, cada vez que ingresemos al javascript el me va a ejecutar lo que le vamos a colocar en el setinterval

//textcontent cambia el contenido del HTML

setInterval(() => {
    parrafo.textContent = 'El texto ha cambiado';

}, 3000);