import csv

#listas para almacenar nombres y edades

nombres=[]
edades=[]
ciudades=[]

#vvamos a leer el archivo csv y almacenar nombre y las edades

with open('csv/datos.csv','r') as archivo_csv:
    lectura=csv.reader(archivo_csv)
    
#para quitar el encabezado(se lo salta)

    next(lectura)
    
    for fila in lectura:
        nombres.append(fila[0])
        edades.append(int(fila[1]))
        ciudades.append(fila[2])
        
#calcular la edad promedio

promedio= sum(edades)/len(edades)
print(f'la edad promedio es: {promedio}')

print(nombres)
print(edades)
print(ciudades)

with open('csv/datos.csv','r') as archivo_csv:
    lector_csv=csv.reader(archivo_csv)
    
#leer el archivo linea por linea

    for linea in lector_csv:
         print(linea)


