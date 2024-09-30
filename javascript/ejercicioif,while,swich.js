function ciclos() {

    let numero=parseInt(document.getElementById('procesarnumero').value);
    let resultado1= whilef(numero);
    let resultado2= iff(numero);
    let resultado3= switchf (numero);
    document.getElementById('resultado').innerHTML = resultado2 + resultado3 + ' contando hasta el número ingresado ' + "<br>" + resultado1 + "<br>";
}

function iff (numero) {
    let resultado;

if (numero<0){
    resultado= 'el número ' + numero + ' es negativo,' 
} else {
    resultado= 'el número ' + numero + ' es positivo,' 
}
return resultado
};

function whilef(numero){

    let resultado=0 + " ";
    let contador=1;

        while (contador<=numero){

            resultado += contador + " ";
            contador ++
        }
        return resultado

    };

function switchf(numero) {

    let resultado;
   switch (numero){
    case 1:
        resultado='el numero elegido es 1';
        break;
    
    case 2:
        resultado='el numero elegido es 2';
        break;
       
    case 3:
        resultado='el numero elegido es 3';
        break;
            
    case 4:
        resultado='el numero elegido es 4';
        break;
                
    case 5:
        resultado='el numero elegido es 5';
        break;

    default:
        resultado= 'el número ingresado ha superado el limite propuesto en el ejercicio';
        break;
   }
    return resultado;
};




        





   







