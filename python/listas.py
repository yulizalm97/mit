#crear listas

numeros= [1,2,3,4,5] #Lista de numeros enteros

frutas= ["manzana","uva","mango"] #Lista de cadenas de texto

Mixtas=[1,"hola", 3.14, True] #Se pueden manejar listas mixtas

print(numeros)

print (frutas)

print (Mixtas)

print (frutas [0])

print (Mixtas [-1])

print(numeros[3])

#Modificar elementos de una lista 

numeros[2]=8

print(numeros)

#agregar elementos al final del la lista

numeros.append(6)

print(numeros)

#Insertar elementos en una posición específica

frutas.insert(1,"piña")
print(frutas)


#cómo llenamos los elementos de una  o cómo hacemos para llenar una lista.
lista=[]

for i in range(5):
    numero= int(input(f"Ingresa el {i+1} número "))
    lista.append(numero)
    
    print(f"Esta es tu lista: {lista}")

#tarea, colocar una excepción, para que no salga error si no que me diga que ingrese un número válido.

#Las duplas no se pueden modificar como las listas.
