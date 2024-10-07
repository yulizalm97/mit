import json

with open('json/taller2.json','r') as archivo:
    datos=json.load(archivo)
    
#Modificar datos

datos['mision1']= 3.0 #actualizar la nota1

#guardar cambios

with open('json/taller2.json','w') as archivo:
     json.dump(datos,archivo,indent=4)