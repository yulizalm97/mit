import json

with open('json/taller.json','r') as archivo:
    taller=json.load(archivo)
    
Nuevo_taller={
        "mision4": 3.7,
        "mision5": 3.8,
        "mision6": 4.3,
        "proyectofinal2": 3.5
}

if isinstance(taller, list):
    taller.append(Nuevo_taller)
else:
    print ("Error: El archivo json no contiene una lista con unidades")
    
    
with open('json/1taller.json','w') as archivo:
    json.dump(taller, archivo, indent=4)
    
    print(taller)