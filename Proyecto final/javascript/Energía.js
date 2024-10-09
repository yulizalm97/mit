//mostrar videos en fuentes de energía
function mostrar () {

    const video = document.getElementById('video')
    const boton = document.getElementById('boton')
    
    if (video.style.display==='none'){
        video.style.display = 'block';
        boton.classList.remove('fa-plus');
        boton.classList.add('fa-minus');
    }else {
        video.style.display='none';
        boton.classList.remove('fa-minus');
        boton.classList.add('fa-plus');
        
    }
}
       



