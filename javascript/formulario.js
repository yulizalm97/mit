function validarformulario(){
    
    const nombre= document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const mensaje= document.getElementById('mensaje').value;

    if (nombre.trim()===""){
        alert("por favor ingresa tu nombre");
        return false;
    }
//vamos a comparar unos espacios y simbolos,  /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    const comparar=  /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!comparar.test(email)) {

        alert ("por favor ingresa un correo electrónico válido");
        return false;
    }

    if (mensaje.trim()===""){

        alert ("por favor digite su mensaje");
        return false;
    }

    alert ("formulario enviado con éxito");
    return true;
    
    
}

// se utiliza para comentar una sola línea

/*para comentar varias lineas*/

//Ctrl + K + C se utiliza para todo

