archivo=open('archivo.txt', 'r')#para abrir un archivo en modo lectura

#leer el contenido del archivo.txt

contenido=archivo.read()
print("contenido completo del archivo:", contenido)
      
archivo.close()

#readline() leer una sola linea del archivo
#readlines () leer todad las lineas del archivo

# Escritura de archivos de texto
archivo=open('archivoescritura.txt', 'w') # abrir un archivo en modo escritura

archivo.write("primera linea \n")
archivo.write("segunda linea \n")


archivo.close()

#agregar más texto

archivo=open('archivoescritura.txt', 'a') #abrir un archivo en modo escritura
archivo.write("tercera linea ")
archivo.close()