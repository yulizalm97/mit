archivo=open('archivo.txt', 'r')#para abrir un archivo en modo lectura

#leer el contenido del archivo.txt

contenido=archivo.read()
print("contenido completo del archivo:", contenido)
      
archivo.close()