import json

#leer el archivo json existente
with open('json/registroestud.json','r') as archivo:
    estudiantes=json.load(archivo)
    
#agregar un nuevo estudiante

nuevo_estudiante={
    "nombre":"Alex",
    "apellido":"Gonzo",
    "corte_academico":"Corte1",
    "nota1": 3.5,
    "nota2": 3.8,
    "nota3": 4.6
}

#verifica que estudiantes sea una lista

if isinstance(estudiantes, list):
    estudiantes.append(nuevo_estudiante)
else:
    print("ERROR: el archivo json no contiene una lista de estudiantes")
    
#guardamos cambios

with open('json/registroestud.json', 'w') as archivo:
    json.dump(estudiantes, archivo, indent=4)
   
#imprimimos la lista para verificar 
print(estudiantes)