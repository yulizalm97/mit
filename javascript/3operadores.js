//de esta manera queda (n fijos
let a=10;
let b=5;
let res= a + b;

// es= (a+b)
document.write("a = " + "b =" + b + "<br>");
document.write("suma ( a + b )  = " + res  + "<br>");
document.write("resta (a - b ) = " + (a -b) + "<br>");
document.write("multiplicación (a * b ) = " + (a *b) + "<br>");
document.write("división (a / b ) = " + (a /b) + "<br>");

//operadores de asignación

let c=8;

c+=2; //c= c+2
c*=3;

//Operadores de comparación

document.write (" a == b "+ (a == b) + "<br>"); //para mirar si son iguales
document.write ("a != b"+ (a != b) + "<br>"); //para mirar si son diferentes
document.write ("a > b"+ (a > b) + "<br>"); //para saber si a es mayor que b
document.write ("a < b"+ (a < b) + "<br>"); //para saber si a es menor que b

//operadores lógicos

let ver=true;
let fal=false;

document.write (" ver  && fal " + (ver && fal) + "<br>"); //AND
document.write (" ver  || fal " + (ver || fal) + "<br>"); //OR
document.write (" ver(negado) " + (!ver) + "<br>"); //NOT

//Operadores de incremento y decremento

let contador=0;

contador++; //contador= contador+1

document.write(" contador incremento" + contador + "<br>");

contador--; //contador=contador-1
document.write(" contador decremento" + contador + "<br>");
