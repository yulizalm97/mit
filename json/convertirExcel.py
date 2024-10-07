import json
import csv

with open('json/registroestud.json','r') as archivo:
    estudiantes=json.load(archivo)
    
with open('json/registroestud.csv','w', newline='') as archivo_csv:
    campos=['nombre', 'apellido','corte_academico','nota1','nota2','nota3']
    
    #Crea un objeto dicwriter que permite escribir diccionario en el archivo
    writer= csv.DictWriter(archivo_csv, fieldnames=campos)
    writer.writeheader() #escribe la fila de encabezado del archivo csv
    writer.writerows(estudiantes)
    
    
