document.getElementById('mostrar').onclick = function () {

let numero = parseInt ( document.getElementById('numeroinput').value);
let contador=1;
let resultado=0 + "<br>";

while (contador<=numero) {
    resultado += contador + "<br>";
    contador ++;
}

document.getElementById('resultado').innerHTML=resultado;
};