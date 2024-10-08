import csv 

#para abrir el archivo csv

with open('csv/datos.csv','r') as archivo_csv:
    lector_csv=csv.reader(archivo_csv)
    
#leer el archivo linea por linea

    for linea in lector_csv:
         print(linea)
    
#Escritura de archivos csv

with open('archivo_nuevo.csv','w') as archivo:
    escribir=csv.writer(archivo)
    
    #lo que queremos que contenga

    escribir.writerow(['Nombre','Edad','Ciudad'])
    escribir.writerow(['Manuel','25','Cali'])
    escribir.writerow(['Vanesa','30','Manizales'])