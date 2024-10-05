import json

with open('json/estudiante.json','r') as archivo:
    datos=json.load(archivo)
print (datos)

#se puede acceder a los valores como si fuera un diccionario

print("Nombre:", datos ['nombre'])
print("Apellido", datos ['apellido'])
print("Nota1:", datos ['nota1'])