#Abrir y leer un archivo usando with

with open('archivo.txt', 'r') as archivo:
    contenido=archivo.read()
    print(contenido)

with open('archivo2.txt','w') as archivo:
    archivo.write('programación explorador')