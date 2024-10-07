import json
with open('json/taller2.json','r') as archivo:
    datos=json.load(archivo)

print(datos)

print (datos['mision1']) 
