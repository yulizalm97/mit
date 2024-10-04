#Función saludar

def saludar():
    
    print("programación python")
    
#llamar la función (el sistema salta la función porque no se ha llamada, en el momento en que se llama regrasa a la linea en que esté en la función)

saludar()

#Función de suma de dos números

def sumar(a, b):
    
    resultado= a + b
    
    return resultado

suma= sumar(5 , 3)

print (f"la suma es: {suma} ")

#Calcular el área de un rectangulo

def rectangulo (a,b):
    
    area = a * b
    
    return area
print (f"El area del rectangulo es: (rectangulo {5, 7}")


#parametro por defecto.

def nombre(nombre="Invitado"):
    print(f"¡hola,{nombre}!")
           
nombre ("juan")
nombre()
