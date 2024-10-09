import csv

ruta_archivo='cuadradocubo.csv'

datos=[['numero','cuadrado','cubo']]

for numero in range (1,16):
    datos.append([numero,numero**2,numero**3])
    
#guardar el archivo

with open(ruta_archivo,'w') as archivo:
    escribir=csv.writer(archivo)
    escribir.writerow(datos)
    
print ('archivo creado con exito')

with open(ruta_archivo,'r') as archivo:
    lectura=csv.reader(archivo)
    
    for fila in lectura:
        print(fila)