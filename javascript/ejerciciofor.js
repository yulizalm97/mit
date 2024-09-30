function calcular() {

    let numero = parseInt(document.getElementById ('numero').value);

    let resultado1 = retornosumatoria(numero);
    let resultado2 = retornofactorial (numero);

    document.getElementById ('resultado').textContent = 'la suma de los numeros del 1 al ' + numero + ' es: ' + resultado1 + 'y el factorial de ' + numero + ' es ' + resultado2;
}



function retornosumatoria(num1){

    let resultado= 0;

    for (let i=1; i<= num1; i++) {
        resultado+= i;
    }

    return resultado;
}

function retornofactorial (num2){


    let resultado =1;

    for (let i=1; i<=num2; i++){
        resultado*=i;
    }
    return resultado;
}